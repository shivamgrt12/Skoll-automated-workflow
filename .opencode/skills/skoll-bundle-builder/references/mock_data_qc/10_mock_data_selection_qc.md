# Mock data QC gate: selection coherence

You are reviewing the mock-data **service selection** for one generated Skoll
task. The persona team ships a full catalogue of mock APIs; the pipeline picks a
persona-relevant subset and splits it into required vs distractor services. This
gate checks that the selection is coherent before the pipeline spends tokens on
later stages. The heavy per-file schema and image checks run again on the whole
assembled bundle at the final QC stage; do not repeat those here.

## What to read

- `api_selection.json` in the work directory (the artifact under review). It
  holds `required_apis`, `distractor_apis`, `input_artifacts`, and `deliverables`.
- `PROMPT.md` and `prompt_design_notes.md` in the work directory for what the
  task actually asks the agent to do.
- The `mock_data/` catalogue at the input root (the available `<service>-api/`
  folders the selection must draw from).

## What counts as a violation

- A required or distractor service that is not present in the input `mock_data/`
  catalogue (the selection names a service that was never shipped).
- The same service appears in both `required_apis` and `distractor_apis`.
- Fewer than 12 entries in `required_apis` (every task must declare at least 12).
- Any banned service appears in either list. The banned services are
  `google-drive-api`, `google-contacts-api`, `box-api`, and `dropbox-api` — none
  of them may appear in `required_apis` or `distractor_apis`, even if the persona
  ships mock data for them.
- A **required** service that the prompt gives the agent no reason to touch, or a
  clear task-critical service that was left out of `required_apis` (the required
  set should match what the deliverables actually depend on).
- The required-to-distractor ratio is wildly outside 1:1 to 2:1.

## What is fine

- Distractor services that are plausible for the persona but unused by the task
  (that is their purpose as noise).
- JSON-only mock data files (the harness accepts JSON; schema divergence versus
  the canonical CSV catalogue is handled, and downgraded, at the final QC stage).

If you find blocking violations, revise `api_selection.json` to fix them while
keeping the selection faithful to the prompt and the design notes.

Judge only the service selection. Do not audit individual mock-data file
contents, schemas, or images; those are covered by the final-stage gates.
