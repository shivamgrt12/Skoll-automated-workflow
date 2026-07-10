# Client and Manager Requirements (distilled)

This file is the calibration source for `prompt_generation.md`. Any model running the
generator must read this file fully before writing a prompt. It captures the client's
delivery feedback, the manager's hard style rules, and the complexity anchors drawn from
the three reference papers (ClawMark, GDPval, JobBench). Treat every line here as binding.

---

## 1. What the client asked us to change

The most recent sample delivery was marked down for one core pattern. Many trajectories
had lots of user turns, but each individual ask was small and self contained, and topics
kept switching. The client wants the opposite shape.

1. The long horizon must be driven by **a single very complex user prompt** in the
   beginning. That one opening turn should carry most of the requirements and teach the
   model to work autonomously for a long time on a hard job.
2. It is fine to add **2 to 3 more user turns** only to clarify, follow up, or inject a
   small organic intrusion. These follow ups stay light. Hints inside them can be masked.
3. The anchor for difficulty is one question. **Would a normal competent person need more
   8 to 10 hours to do this well?** If the honest answer is no, the task is not hard enough.
4. The difficulty lever the client trusts most is a **rich and coherent underlying
   database**. Ten emails and ten contacts is too thin. Managing 100 people is a different
   task than managing 10. The challenge is keeping that larger world coherent, so richness
   without coherence is a defect, not progress. The hardest sample prompts the client has
   shown us reach this through **scale of objects**. They ask for independent review of
   dozens of core objects and reconciliation across many thousands of records. At least one
   workstream in a hard task should operate over a population that large rather than a
   handful, because a job that fits in ten records can be single threaded in minutes.
5. **Small business and enterprise tasks tend to be more long horizon** than personal
   chores. Lean toward work that a company, a consultancy, or a busy professional would
   actually own.

## 2. The three domains we author for

Every prompt must sit inside exactly one of these. Pick the one that fits the persona best.

- **Enterprise.** The kind of task or project you would take on at a large company.
  Cross functional, multi system, ownership over a workstream, real stakes.
- **Personal.** Long complicated work you would do for yourself or your family. For
  example preparing a full tax return from raw records, or running a complex family event.
- **Professional or Prosumer.** The work a small business or a consultancy would need to
  do. We have particular interest in tasks that map onto the GDPval or JobBench style of
  real occupational work.

## 3. Manager hard rules for the prompt text

These are non negotiable. The generator must self check against every one before output.

1. **No unnecessary context.** The agent already has the full persona, the files, and the
   environment. Never restate anything the agent can read for itself. Do not name the
   systems to use, do not spell out which entity lives in which service, and never hand
   over the plan. Carry intent and the goal, not the orchestration. This is the single
   most important rule. A prompt fails if it tells the agent how to do its own job.
2. **No em dashes anywhere.** Use a comma, a full stop, or a fresh sentence instead.
3. **No semicolons and no colons** in the prompt body. Restructure into separate sentences.
   The only colons allowed are inside the turn header line itself.
4. The opening turn must be **complex enough to force the agent to spawn multiple
   subagents**. A single threaded reading of it should be visibly inadequate. It must fan
   out across several independent surfaces or workstreams that can be pursued in parallel.
5. **Paragraph shape.** Do not write one impenetrable wall, and do not force a rigid three
   paragraph essay. Let the opening turn break naturally where the workstream shifts, the
   way a busy person actually dictates a pile of tasks. Complexity is required, padding is
   not. If a paragraph break does not reflect a real change of subject, remove it.
6. **No temporal lexicon.** Do not open with a time of day or a date stamp. Do not use
   weekday names or relative time words such as today, tomorrow, tonight, overnight, this
   morning, this week, this weekend, or noon. When a date is genuinely needed, use an
   absolute persona calendar date such as October 23, 2026. This matches QC Gates 39 and 40.

## 4. Complexity anchors from the three papers

The client named these three benchmarks as the bar to aim at, and asked us to enrich the
underlying database as the main difficulty lever. The generator reads this section so it
knows what hard means in our setting and where each paper pushes us. Read them as three
different pressures on the same goal. ClawMark pushes on a changing multi service world over
many days. GDPval pushes on the quality of the finished professional deliverable. JobBench
pushes on reasoning through a cluttered workspace of mixed files to do what a human actually
wants delegated. A prompt that scores well against us should feel hard along all three.

### ClawMark, the living world coworker benchmark (Final_skoll_delivery_fixed_stage_nodrive/ClawMark.pdf)

What it is. A benchmark of 100 tasks across 13 professional scenarios such as legal
assistant, insurance, investment analyst, clinical assistant, HR, and project management.
Each task is a multi turn workflow where one turn is one in world working day, running
against five stateful sandboxed services (filesystem, email, calendar, knowledge base,
spreadsheet) plus the wider set in our own mock harness. Tasks run from 2 to 6 turns with a
mean of 3.6, and carry 6 to 29 weighted checkers with a mean of 15.4. Scoring is fully rule
based over the real post turn state of the services, with 1,537 deterministic checkers and
55 red line constraints, and no model is ever used as the judge.

What makes it hard. Between turns the world changes on its own. Announced loud events arrive
in the wake up message, and unannounced silent mutations appear in the services with no
notification at all, so a competent coworker has to refresh state every turn instead of
trusting a day one mental model. Evidence is multimodal and delivered untranscribed, so
photos, scanned PDFs, audio, video, and spreadsheets each carry decision critical values the
agent must parse for itself. Red lines capture actions a coworker must never take, such as
approving a decision before the required report has arrived.

The numbers that matter. The strongest frontier model reaches only 75.8 weighted score, and
the best strict end to end task success is just 20 percent, so finishing the whole job
cleanly is rare even when partial progress is common. The two failure modes that dominate
are silent change detection at a 56.5 percent failure rate and backend writeback at 53.6
percent, both nearly double the benchmark average. Performance drops the most on the first
day the environment changes under the agent. Project management is the hardest scenario for
every model.

Lesson for us. Build cross source conflicts and a silent change that the agent will only
catch by re checking reality. Make at least one deliverable require committing a result back
to the right service, not just describing it. Reward the agent that refreshes state and
verifies, and penalise the one that acts on memory. Put at least one red line where the
obvious helpful action is the forbidden one.

### GDPval, real economically valuable knowledge work (arxiv 2510.04374)

What it is. A benchmark that covers the majority of US Bureau of Labor Statistics work
activities for 44 occupations across the top 9 sectors that contribute to US GDP. Every task
is built from the representative work of real industry professionals whose average experience
is 14 years, and 220 gold tasks are open sourced with a public automated grading service.

What makes it hard. Each task asks for the actual artifact a professional would hand in, such
as a polished document, a worked spreadsheet, an analysis, a plan, or a deck, and the output
is graded by domain experts against what a competent practitioner in that role would
genuinely produce. The bar is the finished work product, not a short answer about it.

The numbers that matter. Frontier model quality is rising roughly linearly over time and the
best models are now approaching industry experts on deliverable quality, so the easy version
of this work is already close to solved. The paper also shows that more reasoning effort,
more task context, and more scaffolding each improve model performance, which tells us where
real difficulty now lives.

Lesson for us. Anchor the prompt to a believable occupational deliverable that a person in
that role would actually be asked for, and set the bar at a finished professional work
product. Because more context and more scaffolding help the model, do not make the task hard
by hiding the goal. Make it hard through the depth and messiness of the real work and the
judgment it takes to get the deliverable right.

### JobBench, aligning agent work with what humans want delegated (arxiv 2605.26329)

What it is. A benchmark of 130 agentic tasks across 35 occupations, scoped not by economic
value but by the workflows that experts say they most want to hand off. Each task is packaged
as a workspace of heterogeneous reference files, so the agent has to reason through the
cluttered information streams of real professional work. Outputs are graded by a fact
anchored chain of rubrics that averages 35.6 binary criteria per task.

What makes it hard. The signal is buried in clutter. The agent is handed a messy pile of
mixed files and must find the relevant facts, hold the goal across a long trajectory, and
self organise the many dependent steps that finish the job. The grading is fine grained, so
a near miss on any one fact still costs a criterion.

The numbers that matter. Across 36 evaluated models the strongest result is Claude Opus 4.7
running under Claude Code at only 45.9 percent, so long horizon delegated work is far from
solved. The framing is enhancement over replacement, meaning the work that matters is the
work a busy human genuinely wants taken off their plate.

Lesson for us. Make the opening turn a whole job to be owned, with several dependent
deliverables rather than one isolated question. Surround the real signal with believable
clutter and decoys so finding the right facts is itself part of the work. Choose a job a busy
person in that role would actually want delegated, which is exactly the small business and
busy professional skew the client asked for.

## 5. The 8 to 10 hour test, made concrete

Before shipping any prompt, justify the 8 to 10 hour floor with specifics. A prompt clears the
floor only if a competent human would need to do most of these.

- Gather and reconcile information from at least five independent surfaces.
- Resolve at least two cross source conflicts where the newest or most authoritative source
  must win and the stale source must be set aside.
- Produce at least two substantive professional deliverables that depend on the gathered data.
- Run at least one non trivial calculation or analysis with a defensible method.
- Respect at least one boundary or red line where the obvious action is the wrong one.
- Sequence work with real dependencies, so steps cannot all be done at once by one thread.
- Carry at least one workstream over a large coherent population of objects rather than a
  handful. For an Enterprise or a Professional or Prosumer task that means dozens to
  hundreds of objects or many thousands of rows that must be reconciled and held consistent.
  For a Personal task the same pressure comes from the volume and coherence of a real life
  data load, such as years of records or a large household of people and accounts, rather
  than from a forced object count.
- Expect depth on each significant object, not a single pass over a list. A competent human
  would confirm an important object against more than one source before trusting it, and
  would hold an open conclusion when the evidence is thin rather than forcing a verdict.

If you cannot list concrete instances of most of these for your prompt, the task is too easy.

## 6. House conflict style (carry into the prompt, not the plan)

When two sources disagree, the intended behavior is newest or most authoritative wins, and
the agent must name the source it trusted and the source it set aside. State this as an
expectation of judgment in the prompt. Do not reveal which specific values conflict, since
discovering the conflict is the test.

## 7. The client complexity examples, and the trap inside them

The client shared two heavy sample prompts from a health and functional diet research center,
one a compliance audit after a regulation changed and one a P0 incident retrace. The client
was explicit that these are the bar for **complexity** and that they are **overly
prescriptive**, which is a flaw to avoid, not a style to copy.

Learn the complexity from them. Both reach a real eight to ten hour weight through scale and
depth. They review dozens of core objects one at a time, reconcile across many thousands of
records, work over a multi year history, keep parallel status lines, force documented
fallback when a source is paginated or rate limited or empty, and demand a conservative open
conclusion when evidence is thin. They also frame the work as read only over the business
state, which turns every write into a potential boundary violation. That mix of scale, depth,
conflict, and conservative judgment is exactly what we want to reach.

Do not copy how they say it. Both examples hand the agent the entire plan in numbered stages,
name the exact deliverable filenames and the exact JSON field names, and dictate how many
traces each object must leave. That is the prescriptiveness the client dislikes and it breaks
our most important rule. In our house style the prompt carries the outcome and the judgment
calls only. The agent decides the stages, the structure, and the schema for itself. The
deliverable shape is described as an outcome a person wants, never as a filename with a field
list. Both examples are also full of semicolons and em dashes, which we never allow. So take
their ambition and reject their form. Reach their scale and depth while staying intent only,
concise, and in the persona's voice.
