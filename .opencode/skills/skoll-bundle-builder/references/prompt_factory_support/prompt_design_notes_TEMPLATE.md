# Prompt Design Notes for <PERSONA_ID>

This file is the handoff from the prompt-creation stage to the full bundle-creation stage.
The prompt above is the seed. These notes are the design behind it. The bundle author uses
these to build the world, the value lock, the traps, and the checkers. Fill every field.
Nothing here is shown to the agent. This is internal author truth only.

## 1. Domain and focal event
- Domain (Enterprise | Personal | Professional/Prosumer): <one>
- Persona one liner: <name, role, what they own>
- Focal event (the whole job in one sentence): <...>
- Prompt shape (single | multi-turn with N turns): <...>
- Per-turn weight (which turns are heavy fan-out and which are light follow ups): <...>

Note. The agent-facing prompt header is now just `--- TURN N ---` with no Light or
Multi-Agent label. That designation lives here instead, and the bundle stage carries it into
task.yaml and the per-turn expected config. Record it on this line so it is not lost.

## 2. Connected surfaces vs boundary surfaces
- Connected services the task may touch (from persona TOOLS): <list>
- Boundary services that must stay zero-call (distractor bait): <list>

## 3. Workstreams (the parallel fan-out, drives subagents)
List four to eight independent streams. Each should sit on its own surface.
1. <stream> / surface / what a subagent would do
2. ...

## 4. Deliverables the person expects saved
List at least two professional work products and their rough shape.
1. <deliverable> / sections and format expected
2. ...

## 5. Hidden cross-source conflicts (NEVER in the prompt)
At least two. For each, give both values, both sources, and which one wins and why.
| # | Value at stake | Authoritative source + value | Decoy source + value | Winner rule |
|---|----------------|------------------------------|----------------------|-------------|
| 1 | <...> | <file:cell = value> | <file:cell = value> | newest / most authoritative |
| 2 | ... | | | |

## 6. Calculation(s)
- What must be computed: <...>
- Inputs and where they live: <...>
- Method and expected result: <...>

## 7. Red lines (the obvious-but-wrong actions)
At least one. For each, what the agent is baited to do and what it must do instead.
1. <bait> -> required behavior (refuse / hold / draft-only)

## 8. Dependencies and sequencing
Steps that cannot all happen at once, in rough order.
- <...>

## 9. Eight-hour floor justification
List the concrete instances proving a competent human needs 8+ hours.
- Surfaces to reconcile: <count and which>
- Conflicts to resolve: <count>
- Deliverables to produce: <count>
- Calculations: <count>
- Boundaries to respect: <count>

## 10. Database richness plan
How rich must the seeded world be to make this hard, and how is coherence kept.
- Records per key service (aim well above ten where it raises difficulty): <...>
- Coherence anchors (the foreign-key relationships that must stay consistent): <...>
