# Prompt QC gate: difficulty and subagent pressure

You are reviewing a generated Skoll task `PROMPT.md` for one dimension only:
**is it hard enough and broad enough to force real multi-agent work?**

A Skoll task must be something a competent human would need roughly 8 to 10+
hours to finish, and it must fan out into enough independent workstreams that a
capable agent is pushed to spawn subagents rather than solve it linearly.

## What to read

- `PROMPT.md` in the work directory (the artifact under review).
- `prompt_design_notes.md` (the intended workstreams, deliverables, conflicts).
- `api_selection.json` (the required APIs the task leans on).

## What counts as a violation

- Fewer than four parallel workstreams that can run independently.
- The whole task collapses into a single linear chain a person could clear in
  an afternoon.
- Only one deliverable, or deliverables that are trivial restatements of input.
- No cross-source reconciliation, no calculation, no judgment under conflicting
  evidence — nothing that creates genuine hours of work.

## What good looks like

- Four or more genuinely parallel workstreams touching different data sources.
- Two or more substantive deliverables that each require synthesis.
- At least one non-trivial calculation and at least one conflict the agent must
  resolve, so the effort floor is honestly 8 to 10+ hours.

Judge only this dimension. Do not comment on word count, redundant context,
persona voice, or solution leakage; those are other gates.
