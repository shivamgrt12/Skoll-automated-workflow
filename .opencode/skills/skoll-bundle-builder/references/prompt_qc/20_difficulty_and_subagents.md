# Prompt QC gate: difficulty and coherence

You are reviewing a generated Skoll task `PROMPT.md` for one dimension only:
**is it hard enough through depth on ONE coherent job?**

A Skoll task must be something a competent human would need roughly 8 to 10+
hours to finish, and that effort must come from the depth of a single focal
event: stale-vs-live conflicts, decoys, red-line pressure, cross-source
reconciliation over a large coherent population, and draft discipline — never
from stapling together several loosely related asks.

The litmus test: **one owner, one event, one outcome — every sentence in the
prompt must trace back to the focal event.**

## What to read

- `PROMPT.md` in the work directory (the artifact under review).
- `prompt_design_notes.md` (the intended workstreams, deliverables, conflicts).
- `api_selection.json` (the required APIs the task leans on).
- `meta.resolved.json` (check `shape.multi_agent_complex_turns`).

## What counts as a violation

- Any workstream or deliverable that does not serve the single focal event.
  Apply the deletion test: if the workstream could be deleted without affecting
  the focal deliverables, it is padding. Typical padding: a weather report for
  its own sake, a generic catalog or inventory dump, a hobby side-quest, a
  family or social errand bolted on, social-post staging unrelated to the focal
  outcome.
- The whole task collapses into a single linear chain a person could clear in
  an afternoon.
- Only one deliverable, or deliverables that are trivial restatements of input.
- No cross-source reconciliation, no calculation, no judgment under conflicting
  evidence — nothing that creates genuine hours of work.

## What good looks like

- One focal event that the whole prompt serves; every workstream feeds the
  same outcome and survives the deletion test.
- Difficulty carried by stale-vs-live source-of-truth conflicts, decoys,
  red-line pressure, cross-source reconciliation over a large coherent
  population of records, and draft discipline — not by thread count.
- Two or more substantive deliverables that each require synthesis.
- At least one non-trivial calculation and at least one conflict the agent must
  resolve, so the effort floor is honestly 8 to 10+ hours.

## Subagent pressure (conditional)

Read `meta.resolved.json` in the work directory. Only if
`shape.multi_agent_complex_turns` is non-empty, additionally verify that the
job fans out into parallel strands **of the same event** (several surfaces the
one focal event genuinely lives across), so a capable agent is rewarded for
spawning subagents. If `shape.multi_agent_complex_turns` is empty or absent,
do not demand subagent fan-out and do not penalize a task that a strong agent
could work through in sequence, as long as the depth requirements above hold.

Judge only this dimension. Do not comment on word count, redundant context,
persona voice, or solution leakage; those are other gates.
