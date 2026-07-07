# PROMPT_QC

Two-part quality gate for finished Skoll prompt artifacts (`PROMPT.md` /
`prompt.txt` / `prompts.txt`). It splits the 71-item checklist in
`PROMPT_FACTORY/PROMPT_QC_CHECKLIST.md` into the half a machine can prove and
the half a human or model must judge.

| File | Kind | Covers | Cost |
|------|------|--------|------|
| `run_qc.py` | One-command runner | Runs the gate AND emits a paste-ready judgment packet per task | free, instant |
| `prompt_qc.py` | Deterministic script | Machine-verifiable checks (forbidden content, file paths, header form, deliverable lists, form bands) | free, instant |
| `PROMPT_QC.md` | Judgment rubric (LLM + human) | ~41 reading-comprehension checks (framing, difficulty, voice, persona, AI-slop, client calibration, multi-agent forcing) | one paste into a model, or manual |

Everything else (`PROMPT_FACTORY/PROMPT_QC_CHECKLIST.md`, `QC_folder/Prompt_QC_Latest.md`) is left untouched.

## Workflow (the reviewer runs ONE command)

```
python3 PROMPT_QC/run_qc.py --task path/to/RDL_001_allocation_lock
```

That single command:

1. Runs the deterministic gate (same checks as `prompt_qc.py`) and prints the
   report. Exit code is `1` if the gate FAILs, `0` otherwise, so it drops into CI.
2. Auto-assembles a self-contained judgment packet at
   `PROMPT_QC/_qc_packets/<task>__QC_PACKET.md`. That packet already inlines the
   reviewer instruction, the finished prompt artifact, AND that persona's own
   files (USER / IDENTITY / TOOLS / MEMORY / HEARTBEAT / SOUL / AGENTS).

The reviewer's ONLY manual step is to paste that one packet file into their LLM.
Nothing has to be gathered, opened, or copied by hand. The persona files are
inlined because Section H (persona alignment) cannot be judged from the prompt
text alone.

Run every task under a directory at once:

```
python3 PROMPT_QC/run_qc.py --input-dir path/to/input
```

Then **combine verdicts** using the table at the bottom of `PROMPT_QC.md`.
Nothing moves to bundle creation while any blocking FAIL stands.

### Running the gate alone (optional, CI)

If you only want the deterministic gate without emitting packets:

```
python3 PROMPT_QC/prompt_qc.py --file path/to/PROMPT.md --verbose
python3 PROMPT_QC/prompt_qc.py --input-dir path/to/input
python3 PROMPT_QC/prompt_qc.py --input-dir path/to/input --task RDL_001_allocation_lock
```

## What the script enforces

Hard **FAIL** (forbidden content and malformed form -- must be fixed):

- `C#12` service api-handle leak. Only the technical `-api` / `_api` handle
  form fails (`whatsapp-api`, `slack_api`, `gmail-api`). A service named
  naturally in prose (`WhatsApp`, `Slack`, `Gmail`, `Notion`) is how a real
  person speaks and is allowed.
- `C#15` dictated file names (`*.pdf`, `*.csv`, ...)
- `C#15` explicit file paths (`/Users/...`, `/workspace/...`, `mock_data/...`, `a/b/c`)
- `C#16` JSON / field-schema tokens
- `C#18` em dash / en dash / ascii `--`
- `C#19` semicolons in a turn body
- `C#19b` parentheses in a turn body (a dictated aside uses no brackets)
- `C#20` colons in a turn body (allowed only in the `--- TURN N ---` header)
- `C#21` temporal lexicon: clock stamps (`9am`, `09:30`). Relative words
  (today, tomorrow) and weekday names are NOT flagged because a persona speaks
  in those naturally.
- `C#21b` explicit calendar years (four-digit `1900`-`2099`; written-out years
  like "twenty twenty six" are prose and pass)
- `D#23` an empty artifact with no turn body content
- `C#27` header not exactly `--- TURN N ---`
- `F#31` a deliverables / produce-this heading
- `F#32` a numbered or bulleted output list

Heuristic **MAJOR** (flags for review, the rubric judges intent):

- `C#11` restating context the agent already has, or pointing it at its own
  files / inbox / environment (things it should read or work out on its own)

Advisory **WARN** (form bands, non-blocking):

- `D#23` a turn body broken by a blank line (must be one unbroken paragraph)
- `D#24` heaviest turn outside the 800 to 1000 word band
- `D#25` a light follow-up turn outside 2 to 5 sentences (only fires when
  follow-ups exist; see prompt shapes below)

## Two valid prompt shapes

Both are accepted and neither is penalized for being the other:

1. **Single heavy complex turn** -- one `--- TURN 1 ---` block and nothing else.
   The gate does NOT flag it for lacking follow-ups. `D#25` never fires because
   the only turn is the heavy turn.
2. **Multi-turn** -- one heavy complex opening turn plus a small number of light
   follow-ups (2 to 3 max). Each follow-up under 180 words is checked for the
   2 to 5 sentence band (`D#25`, WARN only). A follow-up over 180 words is a
   second heavy turn and is left to the judgment rubric (`J2`) rather than
   flagged deterministically.

In both shapes the long horizon is driven by the ONE heavy opening turn. The
judgment rubric item `J2` is conditional: a single-turn prompt scores PASS on
`J2` by definition, and only multi-turn prompts are checked for light-follow-up
discipline.

## What the script deliberately does NOT check

Anything that needs reading comprehension is left to `PROMPT_QC.md`, because a
regex that pretends to judge "sounds like a real busy person dictating" or
"traps stay hidden" would give false confidence. Sections A, B, E, G, H, I, J, K
of the checklist live in the rubric.

## Notes

- Standard library only, Python 3.7+. No install step.
- Mirrors the `Finding` / severity / `compute_verdict` / report shape of
  `QC_folder/mock_data_qc.py` so the two QC tools read identically.
- The service allowlist in `prompt_qc.py` mirrors Appendix B of
  `QC_folder/Prompt_QC_Latest.md` (localhost:8000-8035 mock APIs). Update both
  together if the harness surface set changes.
