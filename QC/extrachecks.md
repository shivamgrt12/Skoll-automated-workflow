# Extra Checks — Supplementary QC Prompt (self-contained, task-agnostic)

> **Role.** You are a final-pass bundle auditor. Run these *extra checks* on **any** task input
> bundle. This checklist is **fully self-contained** — it embeds everything it needs and does
> **not** require reading any other QC prompt, reference/gold bundle, or external file. Run it
> standalone against the single task bundle under review.
>
> **Task-agnostic principle.** Do **not** enforce numbers from any specific task. Every count
> (number of tests, criteria, APIs, files, dates, IDs, values) is **derived from the task under
> review itself** — from its own `task.yaml`, `README.md`, `TRUTH.md`, `rubric.json`,
> `test_weights.json`, `test_outputs.py`, `persona/`, `data/`, and `mock_data/`. The checks below
> verify *internal consistency and framework rules*, never a hardcoded target.
>
> **Canonical filenames.** Where naming can drift, treat these as canonical: `PROMPT.md`
> (single-turn brief — this is the **only** accepted name; `prompts.txt` is **not** accepted),
> `rubric.json`, `README.md`, `TRUTH.md`, `task.yaml`, `test_outputs.py`, `test_weights.json`,
> `persona/`, `data/`, `mock_data/<api>-api/`, `inject/stage0/mutations.json`.
>
> **Output.** Produce a Markdown QC report (suggested name `QC_REPORT_EXTRACHECKS.md`) with one
> row per check: **Check · Verdict · Evidence (file + line/quote) · Notes**, then a final roll-up
> verdict. Severities: **red / Major** (blocks push), **Moderate**, **Minor (cleanup)**,
> **FAIL-HARD** (auto-fail regardless of other results).

---



## Canonical bundle structure (embedded — no external file needed)

```
<task_id>/
├── README.md
├── task.yaml
├── PROMPT.md                  # single-turn brief (only accepted name; NOT prompts.txt)
├── TRUTH.md
├── rubric.json
├── test_outputs.py
├── test_weights.json
├── persona/
│   ├── AGENTS.md
│   ├── SOUL.md
│   ├── MEMORY.md
│   ├── IDENTITY.md
│   ├── USER.md
│   ├── TOOLS.md
│   └── HEARTBEAT.md
├── data/                      # flat; load-bearing + noise files, multi-modal
├── mock_data/
│   └── <api>-api/             # one folder per CALLABLE api (connected + distractor), *.csv / *.json
└── inject/
    └── stage0/
        └── mutations.json     # empty seed stub only
```

**Framework constants** (these are rules, not task data, so they are safe to hardcode):

- Allowed rubric `score` and test weight values: **{-5, -3, -1, 1, 3, 5}** only.
- `persona/` must be exactly the **7** files listed above.
- `inject/stage0/` must contain only `mutations.json` with an empty `mutations` array.
- **Two flavors of "not connected".** (a) *Callable* off-limits services (distractor / not-connected
bait that the agent *could* reach) are folder-backed: they get a `mock_data/<api>-api/` folder, a
`*_API_URL` in `test_outputs.py`, and a **negative** `test_<api>_distractor` probe. (b) *Persona-only*
narrative baits (e.g. live web search, internal patient databases, external submission portals,
family members' personal accounts) exist **only** in `persona/TOOLS.md` / TRUTH.md text: they have
**no** folder, **no** env var, and **no** probe. Only flavor (a) counts toward the mock-folder tally.
- `rubric.json` per-criterion required fields: `number`, `criterion`, `is_positive`, `type`,
`evaluation_target`, `importance`, `score`.
- `type` enum (space-separated, no underscores): `task completion` · `instruction following` ·
`factuality and hallucination` · `tool use` · `agent behavior` · `safety & boundaries`.
- `evaluation_target` enum: `state_change` · `user_facing_message` · `trajectory` · `final_answer`.
- `importance` enum: `critically_important` · `important`.
- **`task.yaml` `task_type` controlled vocabulary** (exactly one value, matched **case-sensitively**;
no snake_case / lowercase variants): `Search & Retrieval` · `Productivity Flow` · `Code Intelligence`
· `Creative Synthesis` · `Skill Use & Orchestration` · `Skill Creation & Editing` ·
`Communication & Messaging` · `Device & Environment Control` · `Memory & Personalization` ·
`Scheduling & Long-Running` · `Proactive Assistance` · `Social Interaction` ·
`Multi-Turn Robustness` · `Safety Alignment`.
- **`task.yaml` `platform` enum** (exact string, **case-sensitive** — no other value, no other
casing): `MacOs` **or** `linux` only. *(Spec casing is literally `MacOs` (not `macOS`/`macos`) and
lowercase `linux` (not `Linux`/`LINUX`).)*
- **`task.yaml` `system_prompt`**: must be non-empty and **strictly greater than 30,000 characters**.

---



## A. Core extra checks

**EC-1 — Structure conformance.**
The task must match the canonical structure above: all required files present, and **no extra
files** beyond the sanctioned set. If the structure is not followed, mark a **Major error in red**
and name the exact offending path(s).

**EC-2 — Negative/positive weight ceiling (60% rule — rubric layer only).**
Compute for the **rubric** using the task's own numbers:

- `rubric_positive = Σ score where is_positive=true`; `rubric_negative = Σ |score| where is_positive=false`

Rule: **the rubric negative pool must not exceed 60% of the rubric positive pool**
(if positive = 100, negative ≤ 60). Flag **Major** if `rubric_negative > 0.6 × rubric_positive`.

*Why rubric-only:* the 60% ceiling guards against **LLM-judge bias** toward fault-finding in the
subjective rubric layer (Channel B). It does **not** apply to the deterministic test layer
(Channel A): distractor probes (`test_<api>_distractor`, one per off-limits API) and red-line
probes are structural coverage, and a distractor-heavy task will legitimately carry a test negative
pool that exceeds 60% of (or even outweighs) its test positive pool. Do **not** flag the test layer
for the 60% ratio.

**EC-2b — Test-layer positive coverage (Minor).**
Instead of a negative cap, verify the test layer has positive coverage: there should be at least one
**positive** probe per connected/required API's core behavior. Flag **Minor** if the count of
positive probes is materially below the number of connected APIs (i.e. required APIs left with no
positive probe).

**EC-3 — TRUTH.md grounding & internal alignment.**
`TRUTH.md` must be fully grounded and aligned with the persona and the task. Every name, ID,
value, and **date/time** must be mutually consistent across `TRUTH.md`, `persona/`*,
`PROMPT.md`, `rubric.json`, `test_outputs.py`, and `mock_data/`. Any contradiction is a Major
alignment defect.

**EC-4 — Rubric ↔ persona/prompt data alignment.**
Values, IDs, and dates referenced in `rubric.json` must exist in and agree with the persona, the
prompt, and `data/` / `mock_data/`. A criterion referencing a value that does not exist in, or
disagrees with, the grounded sources is a Major defect.

**EC-5 — Truncation.**
Flag if **any** file is truncated: cut-off JSON/CSV/MD, dangling brackets, "..." elisions,
half-written sentences, incomplete tables, or zero-byte files. Report the file and truncation point.

**EC-6 — No Google Drive / Google Contacts usage.**
No `google-drive` and no `google-contacts` / people/contacts API may be **used** in the task.
"Used" means: listed in `task.yaml` required APIs, present as a `mock_data/*-api` folder,
referenced by a `*_API_URL` in `test_outputs.py`, probed by a test, referenced by a rubric
criterion, or targeted as a deliverable surface. Any such usage → **red**.
*(A passive capability mention in* `persona/TOOLS.md` *with no folder, no probe, and no deliverable
dependency is acceptable and not a violation.)*

**EC-7 — No classes.**
`test_outputs.py` must contain **no** `class` **definitions** (function-based `test_`* probes only).
`test_weights.json` must be a **flat JSON object** `{test_name: weight}` — no classes, no nesting.

**EC-8 — Prompt header format.**
`PROMPT.md` may contain **only** turn headers of the form `--- TURN T1 ---` (preferred for
single-turn) or the numbered forms `--- TURN 0 ---` / `--- TURN 1 ---`. Human-readable timestamp
headers such as `(Day 1, Sunday, November 1, 2026, 08:00 CT)` are **not allowed**. Flag every
offending line.

**EC-9 — Single-turn, prompt-only.**
`PROMPT.md` must contain **nothing but** one allowed turn header plus the prompt body — no
metadata, no commentary, no rubric/answer leakage. There must be **exactly one prompt / one turn**
(single-turn, not multi-turn). Flag any second turn or extraneous content.

**EC-10 — No mutations in inject.**
`inject/stage0/` must contain **only** `mutations.json`, and that file must be the **empty seed
stub** with an empty `mutations` array, e.g.:

```json
{ "stage": 0, "description": "Seed anchor", "fires_after_turn": 0, "mutations": [] }
```

Any non-empty `mutations` array, any extra file under `inject/`, or any deviating structure is a
Major defect.

---



## B. Consistency & integrity checks (all parametric — derived from the task)

**EC-11 — Weights ↔ tests bijection (FAIL-HARD).**
The set of keys in `test_weights.json` must be **identical** to the set of `test_`* functions
collected from `test_outputs.py` — a **1:1** mapping with no missing and no extra keys, whatever
the task's test count is. Any mismatch is **FAIL-HARD**.

**EC-12 — Weight/score scale (FAIL-HARD on violation).**
Every rubric `score` and every `test_weights.json` weight must be in **{-5, -3, -1, 1, 3, 5}**.
Any out-of-scale value (e.g. 10 / 30 / 50 / 100) is **FAIL-HARD**.

**EC-13 — Tests are stdlib-only, audit-driven.**
`test_outputs.py` must import only the Python standard library (e.g. `json`, `os`,
`urllib.request`). **Forbidden:** `requests`, `pandas`, `numpy`, `openpyxl`, `bs4`, `PIL`, or any
bundle-local import. Endpoints must resolve via `*_API_URL = os.environ.get(...)`, and assertions
must read the mock **audit** surface (e.g. `/audit/summary`, `/audit/requests`) rather than
hardcoded output folders.

**EC-14 — Distractor probe coverage.**
For every distractor API the task declares, there must be a corresponding **negative** probe
(e.g. `test_<api>_distractor` with a negative weight), and that API must **not** be rewarded
positively anywhere in the rubric or tests. Missing distractor probe → Moderate; distractor
rewarded positively → Major.

**EC-15 — mock_data integrity.**
The number of `mock_data/<api>-api/` folders must equal the total **callable** APIs the task
declares — that is, **connected (required) + distractor**. *Persona-only not-connected narrative
baits* (web search, internal databases, external portals, family accounts — no env var, no probe)
are **excluded** from this tally and must **not** have a folder. Every folder must be named
`<api>-api`, contain **real, non-empty** data files (`*.csv` / `*.json`), and there must be **no**
`google-drive-api`, `google-contacts-api`, or `people-api` folder (ties to EC-6). Empty folders or
missing data → Major.

**EC-16 — API triad consistency (Major).**
The **callable** API set must be identical across three sources within the task: `task.yaml`
(required + distractor) == the `*_API_URL` env-var set in `test_outputs.py` == the
`mock_data/*-api` folder set. Persona-only not-connected baits are excluded from all three sides of
this identity (they carry no env var and no folder by design). Any callable API present in one but
absent from another is a Major defect.

**EC-17 — Cross-file count consistency.**
`README.md`, `TRUTH.md`, `rubric.json`, and `test_weights.json` must agree on the task's own
headline counts: number of rubric criteria and its positive/negative split, and number of pytest
checkers. Recompute from the files and flag any stale/drifted count → Moderate (Major if it changes
grading totals).

**EC-18 — Rubric schema validity.**
Each `rubric.json` criterion must carry all 7 required fields; `type` must be a space-separated
enum value (no underscores); `evaluation_target` and `importance` must be valid enum values; and
the **sign of** `score` **must match** `is_positive` (positive criterion → positive score; negative →
negative). Any schema break → Major.

**EC-19 — No OS/editor junk in the delivered bundle (cleanup).**
Flag and require removal of `.DS_Store`, `__pycache__/`, `.ipynb_checkpoints/`, `Thumbs.db`,
`*.pyc`, and editor swap files. These are not part of the canonical structure. Severity
**Minor (cleanup)** — but they must not ship.

**EC-20 — No oracle / answer leakage.**
Gold answer values must live **only** in `TRUTH.md`. `PROMPT.md` and `rubric.json` must not embed
oracle/answer values that let a solver reverse-engineer the solution (prompt-and-requirements-only
data rule). Any leaked answer value → Major.

**EC-21 — Deliverable surfaces are consistent with declared connectivity.**
Deliverables must land only in surfaces the task actually connects (e.g. mail drafts, notion,
slack, narrative response) and never in a file store (Google Drive / `/workspace`) the task
declares unavailable. A rubric/test expecting an unavailable deliverable surface is a Major defect.

**EC-22 — No AI-tell prose in authored artifacts (cleanup).**
`README.md`, `TRUTH.md`, `rubric.json` criteria, and `PROMPT.md` should be free of the em-dash
tell (`—`) and other obvious LLM boilerplate. Severity **Minor→Moderate** depending on volume.

**EC-23 — persona/ completeness.**
`persona/` must contain **exactly** the 7 required files (`AGENTS.md`, `SOUL.md`, `MEMORY.md`,
`IDENTITY.md`, `USER.md`, `TOOLS.md`, `HEARTBEAT.md`). Missing or extra persona files → Major.

**EC-24 — data/ modality & multimodal wiring.**
`data/` should be flat and contain both load-bearing and noise/distractor files across multiple
modalities. If the task declares itself multimodal, the declared image(s) must be present **and**
referenced by the task/probes, and should be screened for AI-generated imagery. Missing/dangling
multimodal reference → Major; suspected AI-generated image → Moderate.

**EC-25 — not-connected / distractor bait handling (two flavors).**
Distinguish the two kinds of "not connected / off-limits" bait and hold each to the right shape:

- **(a) Callable distractor bait** (a service the agent *could* reach but must not use — including a
"not-connected" service that is nonetheless folder-backed, e.g. an e-signature surface the principal
signs on herself). It **must** exist as bait: `mock_data/<api>-api/` folder **+** `*_API_URL` in
`test_outputs.py` **+** a **negative** `test_<api>_distractor` probe (weight in {-3, -5}). It must
**not** appear in the required/connected-API list and must **not** be rewarded positively in any
rubric/test. Missing folder/env-var/probe, positive reward, or required-listing → Major.

- **(b) Persona-only narrative bait** (live web search, internal patient databases, external
submission portals, family members' personal accounts). It lives **only** in `persona/TOOLS.md` /
TRUTH.md prose and must have **no** folder, **no** `*_API_URL`, and **no** probe. It must not be
rewarded positively anywhere. A persona-only bait that wrongly gains a folder/env-var/probe, or any
positive reward, → Moderate (Major if it distorts the callable-API triad in EC-16).

---



## C. `task.yaml` field checks (schema & value discipline)

> Parse `task.yaml` and evaluate the fields below. All string comparisons are **case-sensitive**
> unless stated otherwise. Use the *parsed* scalar value (after YAML block-scalar processing), not
> the raw source text.

**EC-26 — `task_type` is a single controlled value (FAIL-HARD).**
`task.yaml` must carry **exactly one** `task_type` value, and it must be a single item (not a list,
not comma-joined) drawn **verbatim** from the controlled vocabulary:
`Search & Retrieval` · `Productivity Flow` · `Code Intelligence` · `Creative Synthesis` ·
`Skill Use & Orchestration` · `Skill Creation & Editing` · `Communication & Messaging` ·
`Device & Environment Control` · `Memory & Personalization` · `Scheduling & Long-Running` ·
`Proactive Assistance` · `Social Interaction` · `Multi-Turn Robustness` · `Safety Alignment`.
The match is **case-sensitive** and must use the **same casing** shown above (Title Case with `&`);
snake_case, lowercase, or free-form descriptors (e.g. `single_turn_multi_api_reconciliation`) are
**not** accepted. Missing `task_type`, more than one value, or any out-of-vocabulary / mis-cased
value → **FAIL-HARD**.

**EC-27 — `task_description` is a single paragraph.**
`task.yaml`'s `task_description` must be a **single paragraph**: the parsed scalar must contain **no
blank-line paragraph break** (no `\n\n` / no empty line separating blocks). Soft-wrapped single
newlines are tolerated, but two or more consecutive newlines (a paragraph break) → **Moderate**.
It must also be non-empty. Empty/whitespace-only `task_description` → Major.

**EC-28 — `system_prompt` present and > 30,000 characters (FAIL-HARD).**
`task.yaml`'s `system_prompt` must be **non-blank** and its parsed length must be **strictly greater
than 30,000 characters** (`len(system_prompt) > 30000`). A blank/whitespace-only `system_prompt`, a
missing key, or a length of 30,000 or fewer characters → **FAIL-HARD** (undersized/absent system
prompt indicates an incomplete task).

**EC-29 — `mock_data/` folder count equals `required_apis` + `distractor_apis` (FAIL-HARD).**
Count the `mock_data/<api>-api/` folders and compare to the sum of the two API lists in `task.yaml`:
`len(mock_data folders) == len(required_apis) + len(distractor_apis)`. This is the same callable-API
bijection as EC-15/EC-16, anchored to the **`task.yaml` key counts** (`required_apis` +
`distractor_apis`). Any mismatch (orphan folder, or a declared API with no folder) → **FAIL-HARD**.

**EC-30 — `platform` is exactly `MacOs` or `linux`.**
`task.yaml`'s `platform` value must be **exactly** one of the case-sensitive strings `MacOs` or
`linux` — no other value and **no other capitalization** (`Linux`, `LINUX`, `macos`, `macOS`,
`Mac OS`, `Windows`, etc. are all rejected). Any deviating value or casing → **Minor** (trivial
literal fix), but it must be corrected before ship.

---

