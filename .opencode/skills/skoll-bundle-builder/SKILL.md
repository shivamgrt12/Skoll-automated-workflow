---
name: skoll-bundle-builder
description: Build a harness-ready Skoll SFT input bundle for one persona. Use when a team member has a persona-team input folder (7 persona MD files at root, plus home/, task/, and mock_data/) and needs the full native bundle (PROMPT.md, rubric.json, test_outputs.py, test_weights.json, TRUTH.md, task.yaml, README.md). REQUIRED FIRST STEP before running anything: ask the user the three design questions in chat (turn shape, domain, anchor) and wait for their answers, then pass them to the CLI as flags. Triggers: "build a Skoll bundle", "make the input bundle for persona X", "run the Skoll pipeline".
---

# Skoll Bundle Builder

Turns a persona-team input folder into a complete, harness-ready Skoll input
bundle. One command, one persona, every artifact.

## REQUIRED FIRST STEP — ask before you run (do not skip)

You are running inside an opencode chat. The pipeline's own terminal prompts
**cannot** reach the user, so the user will never see the design questions unless
**you ask them in chat first**. Before you invoke the CLI for a new bundle you
**must**:

1. Ask the user these three questions in chat and **wait for their reply**:
   - **Turn shape** — single complex prompt, or multi-turn (one heavy opening
     turn plus 2–3 light follow-ups)?
   - **Domain** — enterprise, personal, or professional?
   - **Fixed anchor** — any fixed anchor event or deadline? (optional)
2. Take the **output bundle path** from the user's request. The user specifies
   where the finished bundle should be written in their initial prompt (e.g.
   "build a Skoll bundle for crystal-hayes into ./out/crystal_01"). Use that path
   for `--out`. If the user did not say where to write it, **ask them** — do not
   invent or reuse a default output directory.
3. Then invoke the CLI, passing each answer as a flag: `--turn-shape single|multi`,
   `--domain enterprise|personal|professional`, `--anchor "<text>"`, and the
   user's path as `--out <their path>`. **Omit** any design flag the user leaves
   blank so the model infers that one field.

Do **not** run the prompt stage before asking. Do **not** pass `--auto` to skip
the questions — `--auto` is only for fully unattended runs where the model infers
all three. Passing any design flag already makes the run non-interactive.

## What the persona team gives you (the input)

A single persona folder holding:

- the 7 flat MD files at the folder root: `AGENTS.md SOUL.md IDENTITY.md USER.md TOOLS.md MEMORY.md HEARTBEAT.md`
- `home/` — a fake home-directory tree of workspace artifacts; the prompt uses some as inputs and leaves the rest as intentional noise
- `task/` — the persona team's `README.md` (design brief and trap map) and `QC_REPORT.md`
- `mock_data/<service>-api/` — the full API catalog; the prompt selects a persona-relevant subset and splits it into required and distractor services

Mock data comes from the persona team and is treated as read-only by default.
Stage 0 validates this folder before spending any model call. The pipeline may,
under strict guardrails, **enrich existing mock-data values** so the data stays
aligned with the persona and the prompt — see "Governed mock-data enrichment"
below. It never invents schema, never touches banned services, and never creates
new files.

## What you also supply (design metadata)

A small `meta.yaml` (or `.json`) carrying the non-derivable design decisions.
The required/distractor split is a design choice, so it must be declared here
(`mock_data/` holds the union of both).

Fill every value for YOUR persona. Do not copy another persona's numbers. The
values below are shape-only placeholders showing the expected type of each field:

```yaml
task_id: <persona_NN>
variant: <domain_flavour_slug>
principal: <Full Name>
timezone: <IANA/Zone>
domain: <enterprise|personal|professional>
shape: {turns: <int>, days: <int>, difficulty: <easy|medium|hard>, multi_agent_complex_turns: [<turn ints>]}
confirmation_threshold: {single_charge_usd: <int>, recurring_monthly_usd: <int>}
drafting_language: <iso code, e.g. en>
runtime_model: <model id, omit to use pipeline default>
runtime_thinking: "<on|off>"
required_apis: [<svc-api>, ...]        # must have a matching mock_data/<svc>-api folder; banned services (below) are not allowed
distractor_apis: [<svc-api>, ...]      # must also have a matching mock_data/<svc>-api folder; banned services (below) are not allowed
deliverables: [data/<name>.md, ...]    # files the agent writes at runtime
```

**Banned services.** Four APIs must never be used by a bundle — not as a required
service, not as a distractor, and not referenced anywhere in the prompt — even if
the persona ships mock data for them: `google-drive-api`, `google-contacts-api`,
`box-api`, and `dropbox-api`. The prompt-generation meta-prompt refuses to select
them and the mid-stage mock-data QC gate (`references/mock_data_qc/`) blocks any
run that lists them.

## The pipeline (6 stages)

| # | stage | kind | produces |
|---|-------|------|----------|
| 0 | validate | script | fail-loud checklist against `input-contract.yaml` |
| 1 | prompt | model | `PROMPT.md`, `prompt_design_notes.md`, `README.md`, `api_selection.json` (then review — see below) |
| 2 | rubric | model | `rubric.json`, `test_outputs.py`, `test_weights.json` |
| 3 | truth | model | `TRUTH.md` |
| 4 | assemble | script | `task.yaml`, final `README.md`, copied trees (no `inject/`) |
| 5 | qc | script+model | pass/fail gates from `references/qc/` |

Each stage writes a checkpoint into `<work>/bundle-manifest.json`, so a run can
be resumed or a single stage regenerated.

## QC runs mid-pipeline and at the end

QC happens in two places. Every generating stage is followed by a **mid-stage
QC sweep** that audits the artifact it just produced, and the whole assembled
bundle is audited again by the **final Stage 5 QC**. The mid-stage sweeps catch
a bad artifact early — before later stages spend tokens on it — and, like the
prompt review, they run an **auto-fix loop**: a failing model-audit gate revises
the artifact and re-checks, up to three rounds, before the run halts.

| after stage | mid-stage gate folder | audits |
|---|---|---|
| 1 prompt | `references/prompt_qc/` | `PROMPT.md` (+ its review loop) |
| 1 prompt | `references/mock_data_qc/` | `api_selection.json` (service selection) + mock-data / persona alignment |
| 2 rubric | `references/rubric_qc/` | `rubric.json` |
| 2 rubric | `references/pytest_qc/` | `test_outputs.py`, `test_weights.json` |
| 3 truth | `references/truth_qc/` | `TRUTH.md` |
| 5 qc (final) | `references/qc/` | the whole assembled bundle |

Mid-stage gates block by default; a failure at `block` severity stops the run.
Set a gate to `warn` in its folder's `manifest.yaml` to make it non-blocking.
The final Stage 5 QC still runs its full gate set on the assembled bundle, so the
mid-stage checks are an early-catch layer, not a replacement.

Every sweep (each mid-stage sweep and the final Stage 5 QC) writes a per-stage
report to `<work>/QC_reports/`, named `NN_<stage>.md` in pipeline order. Each
report lists every gate's verdict (`PASS`/`WARN`/`FAIL`) and the model's audit
findings text for model gates. Reports land under the work dir (not the output
bundle) so they survive a mid-pipeline halt; if a sweep halts on a blocking
failure, that stage's report is still written first and marked `HALTED`.

## Governed mock-data enrichment

Mock data is read-only by default, but the prompt stage may edit **existing**
mock-data values so the data actually backs the scenario. Two triggers, both
persona-aligned:

- **Proactive (during prompt creation):** the model may enrich values it uses to
  raise the difficulty of the prompt — real names, amounts, dates that the task
  reasons over — instead of leaving thin or stub data.
- **Reactive (gate-flagged):** the mid-stage model gate
  `references/mock_data_qc/20_mock_data_alignment_qc.md` flags placeholder/stub
  values in load-bearing fields, population too thin for the job, or data that
  contradicts the persona or the prompt. Its auto-fix pass then enriches the
  flagged values (same guardrails), up to three rounds before the run halts.

Guardrails are enforced in code (`_guarded_mock_writeback` / `_guard_values_only`
in `cli/skoll_bundle.py`), not just asked of the model:

- **Values only, never schema** — records may gain or change values, but no field
  may be renamed, added, dropped, and the container/envelope shape is preserved.
- **Existing files only** — writes must target an existing `mock_data/<svc>-api/`
  file; new files and path escapes are rejected.
- **Banned services are never written** (`google-drive/contacts/box/dropbox`).
- **Valid placeholders are preserved** — deliberate aggregate/summary/null rows
  (e.g. QuickBooks `Multiple - See Batch Detail`) are left alone.

Every enrichment run records what it changed to `<work>/mock_data_changes.json`.
Edits land in the persona's `input_dir/mock_data`, so assemble copies the enriched
subset into the bundle. A final deterministic scan,
`references/qc/40_mock_data_placeholders.py` (severity `warn`), catches any stub
values left behind.

## How the run behaves once the questions are answered

After you collect the three answers (see the REQUIRED FIRST STEP above) and pass
them as flags, the run is non-interactive: the pipeline skips its own terminal
questions and per-stage pauses, and the prompt review happens through you in chat
rather than through terminal prompts. If the user wants to review or revise the
generated prompt, read `<work>/PROMPT.md`, discuss it, and re-run `--stage prompt`
with adjusted flags or an edited meta.

## The prompt is the soul of the task — its review loop

The prompt stage does more than generate. It runs in phases:

- **Phase 0 (design decisions):** turn shape (single/multi), domain
  (enterprise/personal/professional), and any fixed anchor event. In an opencode
  chat these come from the `--turn-shape/--domain/--anchor` flags you set from
  the user's answers. Run directly in a terminal with none of those flags (and
  without `--auto`) and the CLI asks the three questions itself. Any field left
  open is inferred by the model.
- **Phase 1:** the model writes `PROMPT.md`, `prompt_design_notes.md`,
  `README.md`, and `api_selection.json`.
- **Phase 2 — self-repair sweep:** each review gate in `references/prompt_qc/`
  runs one at a time. A judgment gate that finds a violation revises `PROMPT.md`
  in place (and re-syncs `api_selection.json`/deliverables/notes/README when the
  fix changes scope). This runs in both interactive and `--auto` modes.

There is no interactive human-review loop. To review or revise the generated
prompt, read `<work>/PROMPT.md`, discuss it in chat, and re-run `--stage prompt`
with adjusted flags or an edited meta.

The review gates map to the crucial prompt questions: no redundant context,
difficulty/subagent pressure, heavy-turn word count (800–1000 target, 1050 hard
ceiling, **blocking**), no solution leak, and persona alignment. Two vendor gates
run alongside them: `60_prompt_qc_vendor.py` (deterministic forbidden-content /
form / word-band checks) and `70_prompt_qc_review.md` (model-audit reading
comprehension). All gates block by default.

## Adding or changing prompt review gates

The prompt review is **directory-driven**, exactly like Stage 5 QC. Drop files
into `references/prompt_qc/`:

1. **Ordering + naming**: two-digit prefix, e.g. `60_my_check.md`. Gates run in
   filename order.
2. **Contract**:
   - `.md` gate: a single review question. In the self-repair sweep it may revise
     `PROMPT.md` and re-emit any changed artifact wrapped in `===FILE: <name>===` /
     `===END===` markers; in a check-only recheck it must not modify anything and
     must end with `QC_RESULT: pass|warn|fail`.
   - `.py` gate: mechanical check invoked as `python <gate> <work_dir>`; reads
     `PROMPT.md` from that dir; **exit 0 = pass, non-zero = fail**.
3. **Severity** in `references/prompt_qc/manifest.yaml`: `block` (must pass) or
   `warn` (advisory). Unlisted defaults to `block`.

## One-command usage

From an opencode chat (design answers collected in chat, passed as flags). The
`--out` path is whatever the user asked for — it is not fixed by this skill:

```bash
python3 .opencode/skills/skoll-bundle-builder/cli/skoll_bundle.py \
  --input  ./Persona_testing/crystal-hayes \
  --work   ./.work/crystal \
  --out    <output path the user gave>/crystal-hayes_01 \
  --meta   ./metas/crystal-hayes.yaml \
  --turn-shape multi --domain enterprise --anchor "Q4 board packet due Friday"
```

Interactive in a real terminal (CLI asks the three questions itself, then pauses
after each stage):

```bash
python3 .opencode/skills/skoll-bundle-builder/cli/skoll_bundle.py \
  --input  ./inputs/Natalie_Dunn_01 \
  --work   ./.work/natalie \
  --out    ./bundles/Natalie_Dunn_01 \
  --meta   ./inputs/Natalie_Dunn_01/meta.yaml
```

Fully automated (no pauses):

```bash
python3 .opencode/skills/skoll-bundle-builder/cli/skoll_bundle.py \
  --input ./inputs/Natalie_Dunn_01 --work ./.work/natalie \
  --out ./bundles/Natalie_Dunn_01 --meta ./inputs/Natalie_Dunn_01/meta.yaml --auto
```

Resume after a fix, or regenerate one stage:

```bash
# skip stages already marked complete in the manifest
... --resume

# re-run only the rubric stage (e.g. after editing the meta-prompt)
... --stage rubric
```

`--harness` defaults to `SKOLL_GK/Environment_SN_Harness` (the `service.toml`
port registry source); override it if your checkout differs.

## Rollout guidance

Keep the interactive default for the first ~2 weeks so operators eyeball each
stage. Once outputs are consistently clean, switch teams to `--auto`.

## Adding the new QC folder (for the QC team)

Stage 5 is **directory-driven**: it auto-discovers gates in `references/qc/`.
No orchestrator code changes are needed to add checks. To drop in the new QC
suite, copy the files into `references/qc/` following two rules:

1. **Ordering + naming**: prefix each file with two digits, e.g. `40_foo.py`,
   `50_bar.md`. Gates run in filename order.
2. **Pass/fail contract**:
   - `.py` gate: invoked as `python <gate> <bundle_dir> <harness_dir>`, so the
     bundle being checked is `sys.argv[1]` and the canonical environment/harness
     dir is `sys.argv[2]`. **exit 0 = pass, non-zero = fail.** Print a
     human-readable report to stdout. A gate that only needs the bundle can
     ignore `argv[2]`.
   - `.md` gate: a model-audit meta-prompt; the model's output must end with a line `QC_RESULT: pass` or `QC_RESULT: fail`.

If a gate is a heavier tool with its own flag-based CLI or a bundled example
snapshot (like the vendored `_mock_overlay_validator/`), add a thin wrapper file
that adapts the two-positional convention onto that tool — see
`30_mock_data_qc.py` for the pattern. Any file whose name does **not** start
with two digits (e.g. a leading `_`) is skipped by discovery, so keep vendor
tools and helpers underscore-prefixed (directories included).

Current final-bundle gates: `10_rubric_qc.md`, `20_test_outputs_qc.md`,
`30_mock_data_qc.py`, `35_mock_boot_check.py`, `40_mock_data_placeholders.py`
(warn), `50_truth_qc.md`, `60_check_ai_images.py`. `30_mock_data_qc.py` audits
each `mock_data/<svc>-api/` overlay against the vendored canonical example
snapshot in `_mock_overlay_validator/examples/` (stdlib-only, self-contained, so
it ignores the `<harness_dir>` argument). `60_check_ai_images.py` scans
`<bundle>/data` for AI-generated / stock images and **requires Pillow**
(`pip install Pillow`); with Pillow absent it errors (exit 2) rather than
silently passing, so install it on every runner.

Optionally set severity in `references/qc/manifest.yaml`:

```yaml
severity:
  40_foo.py: warn   # non-blocking, reported only
  50_bar.md: block  # default; failure stops the pipeline
```

That is the entire integration surface — add files, optionally list severity,
done.

## Adding or changing mid-stage QC gates

The four mid-stage folders (`references/{mock_data_qc,rubric_qc,pytest_qc,truth_qc}/`)
are directory-driven the same way, with one difference in the contract: because
these gates run on the in-progress artifacts in the **work dir** (not an
assembled bundle), their invocation is work-dir-based.

- `.py` gate: invoked as `python <gate> <work_dir>`, so the work dir holding the
  artifact is `sys.argv[1]`. exit 0 = pass.
- `.md` gate: a model-audit meta-prompt. It runs in **auto-fix mode** — if the
  artifact violates the checklist, the model revises it and re-emits the changed
  file wrapped in `===FILE: name===` / `===END===` markers, which the orchestrator
  writes back. The instruction and the `QC_RESULT:` contract are injected at
  runtime, so the gate `.md` only needs the checklist itself.

Same two-digit ordering, same `manifest.yaml` severity map (default `block`),
same underscore-prefix rule for vendored helpers. To QC an artifact a stage
already produces, drop a gate into that stage's folder; to QC something new,
create a folder and wire one `_stage_qc_sweep(...)` call after that stage.

## Files in this skill

- `cli/skoll_bundle.py` — the orchestrator (entrypoint)
- `scripts/validate_input.py` — Stage 0 input gate
- `scripts/build_service_registry.py` — scrapes `service.toml` → `{service: port}`
- `scripts/assemble.py` — Stage 4 assembler (builds `task.yaml` byte-faithfully)
- `references/prompt_generation.md`, `references/rubric_pytest_combined.md`, `references/truth_guide.md` — the model meta-prompts (verbatim)
- `references/prompt_qc/` — Stage 1 prompt review gates (auto-discovered)
- `references/mock_data_qc/`, `references/rubric_qc/`, `references/pytest_qc/`, `references/truth_qc/` — mid-stage QC gates (auto-discovered)
- `references/qc/` — Stage 5 bundle QC gates (auto-discovered)
- `templates/input-contract.yaml` — the Stage 0 contract
- `templates/system_prompt_*.txt` — the fixed `task.yaml` system-prompt blocks
- `templates/bundle-manifest.schema.json` — manifest shape
