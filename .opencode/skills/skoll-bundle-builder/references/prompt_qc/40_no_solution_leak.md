# Prompt QC gate: no solution leak / over-prescription

You are reviewing a generated Skoll task `PROMPT.md` for one failure only:
**the prompt tells the agent how to solve the problem instead of letting the
agent decide.**

The prompt should state what the principal wants and the constraints that bind
it. It must not lay out the method, the order of operations, or the answers. An
over-prescriptive prompt turns a hard reasoning task into a checklist and
destroys what the task is meant to measure.

## What to read

- `PROMPT.md` in the work directory (the artifact under review).
- `prompt_design_notes.md` (to see which conflicts, decoys, red lines, and
  winning values are meant to stay hidden).

## What counts as a violation

- Step-by-step instructions on how to reach the deliverable.
- Naming which files, records, or APIs to consult in what order.
- Revealing a hidden conflict, which value "wins", or how to reconcile it.
- Announcing the decoys or the red lines outright rather than letting the agent
  discover the trap.
- Any phrasing that pre-decides the approach the agent should have chosen for
  itself.

## What good looks like

- The ask and the constraints are clear; the path is not.
- Conflicts, decoys, and red lines are present in the underlying data but never
  spelled out in the prompt.
- The agent has to decide for itself where to look and how to resolve tension.

Judge only this dimension. Do not comment on word count, redundant context,
difficulty, or persona voice; those are other gates.
