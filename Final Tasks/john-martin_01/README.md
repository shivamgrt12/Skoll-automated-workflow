# Bundle README — John Martin

This bundle contains the Stage 1 prompt package for the **John Martin ("OpenClaw")** persona. It is a single-turn, complex-prompt exercise in the **personal** domain, anchored on John's upcoming quarterly rheumatology appointment with Dr. Harper.

## Files in this bundle

| File | Purpose |
|------|---------|
| `PROMPT.md` | The user-facing prompt itself, delivered in John's first-person voice. 881 words (measured), sitting inside the 800–1000-word single-turn band. This is the seed the whole downstream bundle grows from. |
| `TRUTH.md` | The single golden-truth reference for the task (reference-only; not consumed by the harness). Inlines the design-intent, deliverables checklist, mock-data change log, and API selection that earlier generator drafts kept in separate side files — see `TRUTH.md` §2, §3, §4, §7, §12. |
| `rubric.json` | 31 criteria (27 positive + 4 negative), scored against the agent's `user_facing_message` and `state_change` outputs. Channel B of the grading harness. |
| `test_outputs.py` | 18 test functions (17 positive `test_behavioral_*` + 1 negative `test_distractor_apis_touched`). Channel A of the grading harness. |
| `test_weights.json` | 1:1 weight map for the 18 test functions; positive pool +47, negative magnitude 5. |
| `task.yaml` | The full runtime task manifest — `task_description` (the prompt body), `system_prompt` (with the 7 persona files embedded), `platform`, `required_apis:` (12), and `distractor_apis:` (8). |
| `mock_data/` | 20 API folders (12 required + 8 distractor) matching `task.yaml` element-for-element. |
| `persona/` | 7 persona files: `AGENTS.md`, `HEARTBEAT.md`, `IDENTITY.md`, `MEMORY.md`, `SOUL.md`, `TOOLS.md`, `USER.md`. |
| `inject/stage0/mutations.json` | Seed anchor (empty `mutations: []` array — consistent with single-turn shape). |
| `data/` | 56 mixed-format files (xlsx/pdf/tsv/docx/mp3/mp4/jpg/pptx/html/xml) — unlinked seed content, not referenced by rubric or tests. |
| `README.md` | This file. |

## Grading fingerprint

- **Rubric criteria**: 31 total (27 positive + 4 negative); positive pool +93, negative magnitude 16.
- **Test functions**: 18 total (17 positive + 1 negative); positive pool +47, negative magnitude 5.
- **API triad** (clean bijection across `task.yaml`, `test_outputs.py` `*_API_URL` env vars, and `mock_data/`): 20 callable APIs = 12 required + 8 distractor.
- **Boundary services** (zero-call by construction — no folder, no env var, no probe): `google-drive-api`, `google-contacts-api`, `box-api`, `dropbox-api`.

## How the pieces fit

1. `PROMPT.md` is the input a rater or model will see. Everything else in the bundle exists to make that prompt reviewable, executable, and gradeable.
2. `TRUTH.md` is the human-readable golden-truth reference. It is NOT consumed by the harness — the harness reads only `rubric.json`, `test_outputs.py`, `test_weights.json`, `task.yaml`, and the mock data. TRUTH.md's job is to be the source everything else is measured against during review.
3. `rubric.json` + `test_outputs.py` + `test_weights.json` are the two grading channels. Rubric is LLM-judged content; tests are HTTP-call detectors against the running mock-API servers.
4. `mock_data/` + `task.yaml` are the runtime state and manifest the harness needs to spin the mock APIs up and route the agent's calls.

## Design decisions at a glance

- **Turn shape**: single complex prompt (one `--- TURN 1 ---` header).
- **Domain**: personal.
- **Fixed anchor**: upcoming quarterly rheumatology appointment with Dr. Harper (Dec 10, 2026, 10:30 AM CT).
- **Prompt length**: 881 words, inside the 800–1000 single-turn band.
- **Target effort**: approximately 8–10 hours for a skilled human.
- **Constraints honored**: no API names, no year/month/date/day-of-week references, no AI vocabulary, no reliance on the 4 forbidden storage services (google-drive, google-contacts, box, dropbox).

## Review flow

1. Open `PROMPT.md` first. If it does not read like a real person handing off a stack of morning work to a trusted assistant, stop and re-scope.
2. Read `TRUTH.md` in full — §2 for the deliverables checklist, §3 for the locked anchor values, §4 for the six cross-source conflicts, §6 for the eleven red lines, §7 for the API split, §10 for the fifteen poison pills.
3. Cross-check `rubric.json` and `test_outputs.py` against the TRUTH.md fingerprint block in §8/§9 — 31 rubric criteria, 18 tests, all counts and polarities named.
4. Spot-check `mock_data/` for the specific records TRUTH.md §3 cites (e.g., `mock_data/obsidian-api/note_contents.json` for the 8-day symptom-log gap; `mock_data/google-calendar-api/events.json` for the silent-changed choir slot).

## Persona quick-reference

- John Martin, age fifty, registered nurse in Murfreesboro. Widowed at forty-four. Managing rheumatoid arthritis. Two adult children: Kayla (twenty-four, daughter, healthcare proxy and power-of-attorney holder) and Marcus (twenty-one, son, in engineering school). Best friend Pat Williams. Pastor Michael Henderson at New Vision Baptist. Rheumatologist Dr. Yolanda Harper. Estate attorney Donna Reeves. Tyrone's brother Kevin Martin is on a hard no-contact list.
- Operating mode: ask-first on anything outbound or irreversible; act-first on everything else. Financial confirmation threshold: seventy-five dollars.
- Communication tone: warm, professional, Southern courtesy with real substance. Checklists. Brief. Steady.
