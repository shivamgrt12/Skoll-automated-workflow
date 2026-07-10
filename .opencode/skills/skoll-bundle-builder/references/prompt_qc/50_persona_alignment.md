# Prompt QC gate: persona alignment

You are reviewing a generated Skoll task `PROMPT.md` for one dimension only:
**does it sound like this principal, in their world, asking for their work?**

The prompt is written as the principal speaking to their assistant. It must
match the principal's voice, register, and domain as established by the persona
files. A prompt that reads generic, or drifts into a register the principal
would never use, breaks the illusion and weakens the task.

## What to read

- `PROMPT.md` in the work directory (the artifact under review).
- `SOUL.md`, `IDENTITY.md`, `USER.md` at the input root (voice, character,
  relationship to the assistant).

## What counts as a violation

- Voice or register that does not match the persona (too corporate for a
  casual principal, too breezy for a formal one, wrong code-switching, etc.).
- Domain drift: the ask sits outside the world the persona lives in.
- Named people, places, accounts, or habits that contradict the persona files.
- Flat, assistant-neutral phrasing where the principal has a distinct voice.

## What good looks like

- The prompt reads unmistakably as this principal.
- Register, idiom, and any code-switching match the persona files.
- The situation and relationships are consistent with IDENTITY.md / USER.md.

Judge only this dimension. Do not comment on word count, redundant context,
difficulty, or solution leakage; those are other gates.
