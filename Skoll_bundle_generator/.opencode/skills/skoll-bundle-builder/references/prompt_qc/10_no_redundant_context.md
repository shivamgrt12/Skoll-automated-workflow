# Prompt QC gate: no redundant context

You are reviewing a generated Skoll task `PROMPT.md` for one failure only:
**the prompt restates things the agent already knows.**

The agent runs with the full persona already loaded (its seven MD files:
AGENTS.md, SOUL.md, IDENTITY.md, USER.md, TOOLS.md, MEMORY.md, HEARTBEAT.md)
and with the workspace files and mock APIs already mounted. Anything the prompt
spells out that the agent could read for itself is wasted context that leaks
intent and flattens difficulty.

## What to read

- `PROMPT.md` in the work directory (the artifact under review).
- The seven persona MD files at the input root.
- `prompt_design_notes.md` for the intended framing.

## What counts as a violation

- The prompt re-explains the agent's own standing rules, confirmation
  thresholds, routing, or safety policy that already live in AGENTS.md.
- The prompt narrates persona facts (who the principal is, relationships,
  preferences) that already live in IDENTITY.md / USER.md / SOUL.md / MEMORY.md.
- The prompt lists or describes the contents of workspace files or API data
  instead of letting the agent discover them.
- The prompt hands the agent tool-usage instructions that TOOLS.md already
  covers.

## What is fine

- Naming the concrete deliverables the principal wants.
- Stating the situation, the ask, and the constraints in the principal's voice.
- Referring to a file or account by name when the principal would naturally do
  so, without describing its contents.

Judge only this dimension. Do not comment on word count, difficulty, persona
voice, or solution leakage; those are other gates.
