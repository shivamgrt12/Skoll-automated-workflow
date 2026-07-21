# Using the Skoll Bundle Generator — New Member Guide

Welcome. This guide takes you from a fresh clone to a finished, QC'd Skoll
bundle. Read it top to bottom the first time; after that you'll only need the
[Quick reference](#quick-reference) at the end.

The generator turns **one persona input folder** into a complete, harness-ready
Skoll bundle (`PROMPT.md`, `rubric.json`, `test_outputs.py`, `test_weights.json`,
`TRUTH.md`, `task.yaml`, `README.md`) with **one command**. It is an
[opencode](https://opencode.ai) skill called `skoll-bundle-builder`.

> Already comfortable? The short version lives in [`ONBOARDING.md`](./ONBOARDING.md).
> This document is the fuller, step-by-step walkthrough with every stage explained.

---

## Table of contents

1. [Before you start (mental model)](#1-before-you-start-mental-model)
2. [One-time setup](#2-one-time-setup)
3. [Get a persona to build (important — not in the clone)](#3-get-a-persona-to-build-important--not-in-the-clone)
4. [The two ways to run the generator](#4-the-two-ways-to-run-the-generator)
5. [The prompt you use](#5-the-prompt-you-use)
6. [What happens at each stage](#6-what-happens-at-each-stage)
7. [Where the output lands](#7-where-the-output-lands)
8. [Run the manual QC (second terminal)](#8-run-the-manual-qc-second-terminal)
9. [Fixing and re-running](#9-fixing-and-re-running)
10. [Troubleshooting](#10-troubleshooting)
11. [Quick reference](#quick-reference)

---

## 1. Before you start (mental model)

Three things you must internalise before your first run:

- **One persona in, one bundle out.** The generator always operates on a single
  persona input folder and writes a single bundle. You never batch.
- **Run from the repo root.** The skill finds the 104-service registry through
  the relative path `SKOLL_GK/Environment_SN_Harness`. If your working directory
  isn't the repo root, it can't find the harness and the run fails at Stage 0.
- **QC happens twice.** The generator runs QC **inside** the pipeline (mid-stage,
  auto-fixing) and again on the finished bundle. On top of that, **you** run the
  human **manual QC** (`manual_QCs/`) by hand at the end. Both matter.

The pipeline has six stages. Two are plain scripts, three call a model, and one
does both:

| # | Stage | Kind | Produces |
|---|-------|------|----------|
| 0 | validate | script | Fails loudly if the input folder is malformed — before any model spend |
| 1 | prompt | model | `PROMPT.md`, `prompt_design_notes.md`, `README.md`, `api_selection.json` |
| 2 | rubric | model | `rubric.json`, `test_outputs.py`, `test_weights.json` |
| 3 | truth | model | `TRUTH.md` |
| 4 | assemble | script | `task.yaml`, final `README.md`, copied trees |
| 5 | qc | script + model | Pass/fail gates over the whole assembled bundle |

Full detail on every stage is in [section 6](#6-what-happens-at-each-stage).

---

## 2. One-time setup

Do this once per machine.

### 2.1 Clone and enter the repo

```bash
git clone https://github.com/shivamgrt12/Skoll-automated-workflow.git
cd Skoll-automated-workflow
```

> Everything below assumes your terminal is **at the repo root** (the folder that
> contains `.opencode/`, `SKOLL_GK/`, and `requirements.txt`). Do not `cd` into a
> subfolder to run the generator.

#### Folder structure — keep the generator at the root

Keep the cloned generator folder **as your top-level working folder** and run
everything **from inside it**. Do **not** create an extra wrapper folder and nest
the generator one level down — if you then run commands from the wrapper, the
skill can't find `SKOLL_GK/Environment_SN_Harness` (it's looked up relative to
where you run) and the build fails at Stage 0.

**Correct layout — the repo itself is the root you work from:**

```text
Skoll-automated-workflow/        ← clone here; cd into THIS folder and run from here
├── .opencode/                   ← the skill lives here (skoll-bundle-builder)
├── SKOLL_GK/
│   └── Environment_SN_Harness/  ← the 104-service harness (must be here)
├── Persona/                     ← persona input folders (request from team lead)
│   └── <persona-name>/          ← 7 MD files + home/ + task/ + mock_data/ + meta.yaml
├── Output/                      ← finished bundles land here
├── manual_QCs/                  ← human QC checklists (request from team lead)
├── requirements.txt
├── USING_THE_GENERATOR.md
└── ONBOARDING.md
```

**Wrong layout — do not do this:**

```text
my-work/                         ← extra wrapper folder
└── Skoll-automated-workflow/    ← generator nested inside; running from my-work/ breaks Stage 0
```

> Rule of thumb: your terminal's current directory must be the folder that
> **directly contains** `SKOLL_GK/`, `Persona/`, and `.opencode/`. If you ever
> must run from somewhere else, pass the harness explicitly with
> `--harness /absolute/path/to/SKOLL_GK/Environment_SN_Harness`.

### 2.2 Install opencode

The generator drives an LLM through the `opencode` CLI. Install opencode
**v1.15.0 or newer** before continuing.

### 2.3 Set up your opencode configuration (do this before authenticating)

The generator and its agents expect a specific opencode configuration (the model
is pinned to `anthropic/claude-opus-4-8` and the required plugins are declared).
Your team lead will send you **two JSON files in a message**:

- `opencode.json`
- `oh-my-openagent.json`

Place **both** files into your opencode config directory:

```bash
mkdir -p ~/.config/opencode
# then save the two files the team shared into:
#   ~/.config/opencode/opencode.json
#   ~/.config/opencode/oh-my-openagent.json
```

> **Important:** copy the files exactly as shared. They set every agent and
> category to `anthropic/claude-opus-4-8` and load the plugins the workflow
> depends on. If these are missing or wrong, runs will use the wrong model or
> fail to start.

### 2.4 Authenticate

Now log in once so opencode can reach the model:

```bash
opencode auth login
```

> After placing the config **and** logging in, **restart opencode** — it reads
> its configuration at startup, so changes only take effect on a fresh start.

### 2.5 Install the Python dependencies

Python **3.11+** is required. Only two third-party packages are needed
(everything else is standard library):

```bash
pip install -r requirements.txt   # installs pyyaml + Pillow
```

- **pyyaml** — reads the persona `meta.yaml` and the QC manifests.
- **Pillow** — needed by the image-check QC gate (`60_check_ai_images.py`). If
  Pillow is missing, that gate errors out instead of silently passing, so
  install it even though it feels optional.

### 2.6 Sanity check

```bash
python3 .opencode/skills/skoll-bundle-builder/cli/skoll_bundle.py --help
```

If you see the flag list (`--input`, `--work`, `--out`, `--meta`, …), your setup
is good.

---

## 3. Get a persona to build (important — not in the clone)

**Read this even if everything above worked.** The persona input folders
(`Persona/`) and the output folder (`Output/`) are **deliberately git-ignored** —
they are large and member-specific, so a fresh clone will **not** contain them.
You must obtain a persona folder and drop it in before you can build anything.

A persona input folder is one directory named after the persona (e.g.
`jennifer-tanaka`) containing:

```
jennifer-tanaka/
├── AGENTS.md        ┐
├── SOUL.md          │
├── IDENTITY.md      │  the 7 flat persona MD files
├── USER.md          │
├── TOOLS.md         │
├── MEMORY.md        │
├── HEARTBEAT.md     ┘
├── home/            # fake home-directory tree of workspace files (inputs + noise)
├── task/            # the persona team's README.md (design brief) + QC_REPORT.md
├── mock_data/       # <service>-api/ folders — the full API catalog for this persona
└── meta.yaml        # the design metadata for this persona (already filled in)
```

**Where to get it:** ask your team lead for the persona folder (from the
persona-team drop / shared drive). Place it under `Persona/` at the repo root:

```
Persona/
└── jennifer-tanaka/
    └── ...
```

> **Good news:** each persona folder ships its **own `meta.yaml`**, already
> filled in with that persona's `required_apis`, `distractor_apis`, difficulty,
> and thresholds. You do **not** author meta from scratch — you point `--meta` at
> the one inside the persona folder. (If you're ever asked to create one, its
> shape is documented in the skill's `SKILL.md`.)

**Four banned services** must never appear in any bundle (not as required, not as
distractor, not mentioned in the prompt): `google-drive-api`,
`google-contacts-api`, `box-api`, `dropbox-api`. The generator refuses them and a
QC gate blocks any run that lists them — so you never need to police this by
hand, but know that it's enforced.

---

## 4. The two ways to run the generator

There are two supported ways to run. **New members should use the opencode-chat
way** for the first couple of weeks — it asks you the design questions and walks
each stage. The direct CLI is for when you want full control or scripting.

### 4.1 The easy way — opencode chat (recommended for onboarding)

1. Open opencode at the repo root:
   ```bash
   opencode
   ```
2. Give it the build prompt (see [section 5](#5-the-prompt-you-use)):
   > build perfect skoll bundle for `Persona/jennifer-tanaka` and save it in
   > `Output/jennifer-tanaka_01`
3. The skill will **ask you three design questions in chat** before it runs.
   Answer them and it takes over the whole pipeline.

The three questions it asks (answer in chat):

| Question | Options | What it means |
|----------|---------|---------------|
| **Turn shape** | `single` or `multi` | One heavy complex prompt, or one heavy opening turn + 2–3 light follow-ups |
| **Domain** | `enterprise`, `personal`, `professional` | The flavour of the task world |
| **Fixed anchor** | free text (optional) | A deadline/event the task hangs on, e.g. "Q4 board packet due Friday". Leave blank if none |

> You **must** answer in chat — the pipeline's own terminal questions cannot
> reach you through opencode, so if you skip them the model just infers, which is
> usually not what you want on a real build.

### 4.2 The direct way — the CLI

Run the orchestrator directly. `--input`, `--work`, `--out`, and `--meta` are
**required**:

```bash
python3 .opencode/skills/skoll-bundle-builder/cli/skoll_bundle.py \
  --input Persona/jennifer-tanaka \
  --work  .work/jennifer \
  --out   Output/jennifer-tanaka_01 \
  --meta  Persona/jennifer-tanaka/meta.yaml \
  --turn-shape single --domain enterprise
```

Passing `--turn-shape` and `--domain` (and optionally `--anchor`) skips the
interactive questions. The full flag list:

| Flag | Required? | Meaning |
|------|-----------|---------|
| `--input` | ✅ | Persona input folder (the 7 MD files + `home/` + `task/` + `mock_data/`) |
| `--work` | ✅ | Scratch dir for intermediates + the resumable manifest |
| `--out` | ✅ | Destination bundle dir (you choose — no default) |
| `--meta` | ✅ | The persona's `meta.yaml` (use the one inside the persona folder) |
| `--harness` | — | Harness dir; defaults to `SKOLL_GK/Environment_SN_Harness` (only set if you run from elsewhere) |
| `--turn-shape` | — | `single` \| `multi` (omit to let the model infer) |
| `--domain` | — | `enterprise` \| `personal` \| `professional` (omit to infer) |
| `--anchor` | — | Fixed anchor event/deadline text (omit if none) |
| `--auto` | — | Fully unattended — no pauses, model infers any unset design field |
| `--resume` | — | Skip stages already marked complete in the manifest |
| `--stage <name> …` | — | Re-run only these stage(s): `validate prompt truth rubric assemble qc` |

---

## 5. The prompt you use

The build prompt you give in opencode chat is simply:

```
build perfect skoll bundle for {persona_path} and save it in {output_path}
```

- `{persona_path}` — the persona input folder, e.g. `Persona/jennifer-tanaka`.
- `{output_path}` — where the finished bundle should be written, e.g.
  `Output/jennifer-tanaka_01`.

A concrete example:

```
build perfect skoll bundle for Persona/jennifer-tanaka and save it in Output/jennifer-tanaka_01
```

After you send it, answer the three design questions
([section 4.1](#41-the-easy-way--opencode-chat-recommended-for-onboarding)) and
the skill runs the whole pipeline.

---

## 6. What happens at each stage

You don't have to babysit these — the pipeline runs them in order and writes a
checkpoint after each into `<work>/bundle-manifest.json` (so a run can resume).
But you should understand what each does so you can read the output and debug.

### Stage 0 — validate (script)
Checks your persona folder against the input contract **before** spending a
single model call: the 7 MD files present, `home/`/`task/`/`mock_data/` present,
`meta.yaml` well-formed, every `required_apis`/`distractor_apis` entry has a
matching `mock_data/<svc>-api/` folder, and no banned service is listed. If
anything is off, it fails here — cheap and loud.

### Stage 1 — prompt (model) — *the soul of the task*
Writes `PROMPT.md` (the task the agent will be given), plus
`prompt_design_notes.md`, a `README.md`, `api_selection.json` (the
required-vs-distractor service split), and a short `task_description.txt`
blurb used later for `task.yaml`. It runs in phases:
- **Design** — uses your turn-shape/domain/anchor answers.
- **Generate** — writes the prompt and picks the API subset.
- **Self-repair sweep** — every gate in `references/prompt_qc/` runs; a gate that
  finds a violation revises `PROMPT.md` in place and re-checks (up to 3 rounds).

This stage may also **enrich existing mock-data values** (never schema, never new
files, never banned services) so the data actually backs the scenario. Changes
are logged to `<work>/mock_data_changes.json`.

The prompt QC gates enforce: no redundant context, difficulty/subagent pressure,
heavy-turn **word count (800–1000 target, 1050 hard ceiling — blocking)**, no
solution leak, persona alignment, English-only, plus two deterministic backstops
(`15_no_deliverable_list.py`, `18_no_reconciliation_rule.py`) and a deep
model-audit read (`70_prompt_qc_review.md`).

### Stage 2 — truth (model)
Writes `TRUTH.md` — the ground-truth answer key, authored right after the
prompt (before any rubric or tests exist). It resolves every planted conflict
and records the correct/stale/decoy values in a typed `VALUE_LOCK` block.
Mid-stage QC (`references/truth_qc/`) checks it's grounded in the prompt,
persona, and mock data.

### Stage 3 — rubric (model)
Writes `rubric.json` (how the agent's work is scored) and the pytest layer
`test_outputs.py` + `test_weights.json`, using `TRUTH.md`'s `VALUE_LOCK` as its
coverage map. Mid-stage QC audits the rubric (`references/rubric_qc/`) and the
tests (`references/pytest_qc/`, including a route/needle satisfiability check
against the real mock routes and a VALUE_LOCK coverage check).

### Stage 4 — assemble (script)
Builds the final `task.yaml` byte-faithfully, writes the final `README.md`, and
copies the required trees into the output bundle. No model call.

### Stage 5 — qc (script + model)
Runs the full gate set in `references/qc/` over the **assembled** bundle: rubric,
tests, mock-data schema validation, a mock-data **boot check** (actually boots the
data through the harness loader), truth, placeholder scan (warn), and AI-image
scan (warn). This is the automated final backstop.

> **Where to read QC results:** every sweep (each mid-stage sweep and the final
> Stage 5) writes a report to `<work>/QC_reports/`, named `NN_<stage>.md` in
> pipeline order, listing each gate's `PASS`/`WARN`/`FAIL` and the model's audit
> findings. If a blocking gate fails, that report is still written and marked
> `HALTED`, so you can always see why a run stopped.

When it finishes you'll see:

```
bundle ready at Output/jennifer-tanaka_01
```

---

## 7. Where the output lands

- **The finished bundle** is at your `--out` path (e.g.
  `Output/jennifer-tanaka_01`). It contains `PROMPT.md`, `rubric.json`,
  `test_outputs.py`, `test_weights.json`, `TRUTH.md`, `task.yaml`, `README.md`,
  and the copied `mock_data/` / `home/` trees.
- **The work dir** (`--work`, e.g. `.work/jennifer`) holds the intermediates,
  the resumable `bundle-manifest.json`, `QC_reports/`, and
  `mock_data_changes.json`. Keep it until you've confirmed the bundle is good — it's
  what lets you `--resume` or regenerate a single stage.

> Remember `Output/` is git-ignored — your finished bundle stays local. Hand it
> off however your team collects bundles (shared drive, upload, etc.).

---

## 8. Run the manual QC (second terminal)

Once the bundle is built, run the **human manual QC** by hand. This is a separate,
standalone copy of every gate, meant to be run by a person as an independent
second check. **Open a new/second terminal** for this so it doesn't disturb your
generator session.

```bash
cd /Users/macbookpro/Desktop/Skoll_bundle_generator/manual_QCs
```

> The `manual_QCs/` folder is also git-ignored and lives outside the skill — it's
> a member-run checklist, not part of the automated pipeline. If you don't have it
> after cloning, ask your team lead for it (same as personas).

The folder mirrors the pipeline: subfolders `01`–`05` are the mid-stage sweeps
and `06` is the final whole-bundle sweep. Run them **in numeric order** against
your bundle. Full instructions live in `manual_QCs/README.md`; the essentials:

**`.py` gates** — run from a terminal (`<bundle_dir>` = your `--out` folder,
`<harness_dir>` = `SKOLL_GK/Environment_SN_Harness`, exit `0` = pass). For example
the final-bundle set:

```bash
python3 06_final_bundle_qc/30_mock_data_qc.py        <bundle_dir>
python3 06_final_bundle_qc/35_mock_boot_check.py     <bundle_dir> <harness_dir>
python3 06_final_bundle_qc/40_mock_data_placeholders.py <bundle_dir>   # warn
python3 06_final_bundle_qc/60_check_ai_images.py     <bundle_dir>      # warn; needs Pillow
```

**`.md` gates** — model-audit checklists. Paste the gate's full text as the
system/instruction prompt to an LLM, attach the artifact it names (plus the 7
persona MD files where asked), and read the verdict. `manual_QCs/README.md` has a
ready-to-paste member prompt.

**Verdicts:** treat anything that isn't a clean pass as blocking, **except** the
two gates marked `warn` (`40_mock_data_placeholders.py`,
`60_check_ai_images.py`). Fix the artifact and re-run the gate until it passes.

Recommended order:

```
01_prompt_qc  →  02_mock_data_qc  →  03_rubric_qc  →  04_pytest_qc  →  05_truth_qc  →  06_final_bundle_qc
```

---

## 9. Fixing and re-running

You rarely re-run from scratch. Use the work dir:

- **Resume a halted run** (skip completed stages):
  ```bash
  python3 .opencode/skills/skoll-bundle-builder/cli/skoll_bundle.py \
    --input Persona/jennifer-tanaka --work .work/jennifer \
    --out Output/jennifer-tanaka_01 --meta Persona/jennifer-tanaka/meta.yaml \
    --resume
  ```
- **Regenerate one stage** (e.g. after editing meta or reviewing the prompt):
  ```bash
  ... --stage prompt      # re-run only the prompt stage
  ... --stage rubric      # re-run only the rubric stage
  ```
- **Review/revise the prompt:** read `<work>/PROMPT.md`, discuss it, then re-run
  `--stage prompt` with adjusted flags or an edited meta. There's no interactive
  human-review pause in chat mode — you review by reading the file and re-running.

---

## 10. Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `harness dir not found` / Stage 0 fails immediately | Not running from the repo root | `cd` to the repo root and re-run; or pass `--harness /abs/path/to/SKOLL_GK/Environment_SN_Harness` |
| `No such file or directory: Persona/...` | Personas aren't in a fresh clone (git-ignored) | Get the persona folder from your team lead, place under `Persona/` ([section 3](#3-get-a-persona-to-build-important--not-in-the-clone)) |
| Stage 0 fails on a service | `required/distractor` API has no matching `mock_data/<svc>-api/` folder, or a banned service is listed | Fix `meta.yaml` — every listed API needs a mock-data folder; remove any banned service |
| `command not found: opencode` | opencode not installed / not on PATH | Install opencode ([section 2.2](#22-install-opencode)), then set up config and `opencode auth login` ([section 2.4](#24-authenticate)) |
| `ModuleNotFoundError: yaml` or Pillow errors | Deps not installed | `pip install -r requirements.txt` |
| `60_check_ai_images.py` exits `2` | Pillow missing | `pip install Pillow` |
| Run stopped mid-pipeline | A blocking gate failed after 3 auto-fix rounds | Read `<work>/QC_reports/NN_<stage>.md` (marked `HALTED`) for the exact finding, fix, then `--resume` |
| Design questions never appeared in chat | You passed design flags (or `--auto`), which makes the run non-interactive | Omit `--turn-shape/--domain/--anchor/--auto` to be asked; or just pass the answers as flags |

---

## Quick reference

**Setup (once):**
```bash
git clone https://github.com/shivamgrt12/Skoll-automated-workflow.git
cd Skoll-automated-workflow
opencode auth login
pip install -r requirements.txt
# then place your persona folder under Persona/  (not included in the clone)
```

**Build (opencode chat, from repo root):**
```
build perfect skoll bundle for Persona/<name> and save it in Output/<name>_01
```
→ answer: turn shape (`single`/`multi`), domain (`enterprise`/`personal`/`professional`), anchor (optional).

**Build (CLI):**
```bash
python3 .opencode/skills/skoll-bundle-builder/cli/skoll_bundle.py \
  --input Persona/<name> --work .work/<name> \
  --out Output/<name>_01 --meta Persona/<name>/meta.yaml \
  --turn-shape single --domain enterprise
```

**Manual QC (second terminal):**
```bash
cd manual_QCs        # run 01 → 06 in order; see manual_QCs/README.md
```

**Key paths:**
- Skill / CLI: `.opencode/skills/skoll-bundle-builder/`
- Harness: `SKOLL_GK/Environment_SN_Harness/`
- Personas (you supply): `Persona/<name>/`
- Output (you choose): `Output/<name>_01/`
- Work dir + QC reports: `.work/<name>/` and `.work/<name>/QC_reports/`
- Manual QC: `manual_QCs/`

**Golden rules:** run from the repo root · answer the three design questions ·
read `QC_reports/` when a run halts · always finish with the manual QC.
