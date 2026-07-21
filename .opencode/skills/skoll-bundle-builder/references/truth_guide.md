# TRUTH_GUIDE.md — How to generate a `TRUTH.md` from a task bundle

> **What this file is.** This is the *generator*. There is no Python script and no
> parser any more. To produce a `TRUTH.md` for a task, you (the model) read this
> guide, then read the **prompt, the mock data, and the design notes** the user hands
> you, and emit a single `TRUTH.md` that follows the exact nine-section structure
> locked below.
>
> **When this runs — read carefully.** `TRUTH.md` is authored **right after the prompt
> stage and before the rubric/tests stage**. That means **`rubric.json`,
> `test_outputs.py`, and `test_weights.json` DO NOT EXIST YET.** You are writing the
> **answer key first**; the rubric and the deterministic tests are generated *afterward*
> and they **consume** your `TRUTH.md` (especially its `VALUE_LOCK` block) as their
> coverage map. Never read, cite, count, or cross-check against a rubric criterion or a
> pytest probe — none exist. Build every fact from the sources that *do* exist at this
> point: `PROMPT.md`, `prompt_design_notes.md`, `mock_data/`, the persona files, and the
> task brief.
>
> **The contract.** Whatever bundle is provided, the output must (a) use the **same
> structure** every time (header + §1–§9, the two fenced blocks, the markers, the
> tables), and (b) be **correct and complete** — every load-bearing value, red line,
> API, conflict, and deliverable that the design implies must be represented and must
> trace back to a real carrier in the bundle. Never invent a number, a date, or an
> email. If a source does not contain something, say so explicitly rather than guessing.
>
> `TRUTH.md` is **reference-only**: it documents the intended solve and grading. It is
> **not** consumed by the harness at runtime. It **is** consumed, at generation time, by
> the rubric-and-tests stage that runs next.

---

## 0. Inputs — what the bundle contains and what each file is for

At this stage (right after prompt generation) the working bundle looks like this. The
files marked **generated later** DO NOT EXIST yet — do not read them:

```
<TASK_DIR>/
├── PROMPT.md                  # the actual turn prompts (--- TURN n --- blocks, Multi-Agent/Light tags)
├── prompt_design_notes.md     # the designer's handoff: conflicts, winners/decoys, planted defects, deliverables
├── README.md                  # human overview: turn map, traps, red lines (if already present)
├── persona/                   # AGENTS.md, SOUL.md, IDENTITY.md, USER.md, TOOLS.md, MEMORY.md
│   └── …                      #   → confirmation threshold, connected vs not-connected, voice, contacts
├── mock_data/<api>/<entity>.csv   # the live world state per service (the carriers)
├── mock_data_changes.json     # audit trail of any values-only enrichment applied during prompt design
├── data/ (or home/)           # input artifacts (pdf/png/jpg/mp3/csv/json/txt) the agent reads
├── task/                      # persona-team design brief (README.md, optional QC_REPORT.md)
│   ── task.yaml               # (generated later, at assemble) machine facts
│   ── rubric.json             # (generated later) Channel B — LLM-judge criteria
│   ── test_outputs.py         # (generated later) Channel A — deterministic pytest probes
│   └── test_weights.json      # (generated later) weight (±) for every probe
```

**Where each TRUTH section gets its facts (read these, in this order):**

| To fill… | Read primarily… | Cross-check against… |
|---|---|---|
| Header bullets | `PROMPT.md`, `persona/AGENTS.md`, `persona/USER.md`, `prompt_design_notes.md` | the required/distractor API split the prompt design chose |
| §1 Focal Event / Scope | `PROMPT.md`, `prompt_design_notes.md`, `persona/AGENTS.md` | `README.md` if present |
| §2 Canonical Solve Path | `PROMPT.md` (turns), `prompt_design_notes.md` (solve + winners) | `mock_data/` carriers each step names |
| §3 Value Lock | `mock_data/<api>/*.csv`, `data/` artifacts, `prompt_design_notes.md` §5 conflicts | the persona (values must be persona-consistent) |
| §4 Fairness Ledger | `prompt_design_notes.md` (planted defects + conflicts), `mock_data` decoy rows | `mock_data_changes.json` (what was enriched) |
| §5 Signal Set | the prompt design's `required_apis` / `distractor_apis`, `persona/TOOLS.md` "Not Connected" | `mock_data/` (a required API must have carriers) |
| §6 Poison-Pill | `PROMPT.md` pressures, `persona/AGENTS.md` rules, `prompt_design_notes.md` red lines | the persona rule each pill binds against |
| §7 Deliverable Notes | `prompt_design_notes.md` deliverables, `PROMPT.md` (does it name a file?) | `mock_data`/artifacts the deliverable must echo |
| §8 Fingerprint | counts **declared by** TRUTH itself (conflicts, defects, pills, deliverables, APIs) | every other section (must reconcile internally) |
| §9 FK Consistency | `mock_data/<api>/*.csv` foreign keys | `prompt_design_notes.md` (intended drift only) |

**Golden rule of provenance.** Every load-bearing value in §3, §4, and §9 must cite a
**carrier** — a real `path:row|key` inside the bundle (e.g.
`mock_data/plaid-api/transactions.csv:txn_pension:amount` or
`data/nasa_milwaukee_irradiance_chart.png`). If two sources disagree, name the
**authoritative** one and the **decoy** one; never silently pick. **Carriers are input
data files (mock_data, data/) — never a deliverable the agent has not written yet.**

---

## 1. Output structure — LOCKED. Emit exactly this skeleton, every time.

The output is a single Markdown file. The order, the headings, the two fenced code
blocks (`VALUE_LOCK { … }`, `PHASE2_FINGERPRINT { … }`), and the marker legend are
**fixed**. Fill the `‹…›` placeholders from the bundle; keep everything else verbatim.

````markdown
# TRUTH.md — ‹TASK_ID›

> Golden truth for the prompts and the reference trajectory. Reference-only: this file documents the intended solve and grading; it is **not** consumed by the harness at runtime.
> Generated for the "‹short focal-event name›" focal event by the Rubrics_and_PY_Generator.
> ‹one-sentence pitch: who the principal is, the single turn/window, what the assistant must do, and what it must leave alone.›

- **Task ID:** `‹task_id›`
- **Variant:** ‹variant›
- **Shape:** ‹N› turn · ‹N› day · difficulty **‹easy|medium|hard›** · multi-agent-complex turn = `‹[…]›`
- **Principal:** ‹name, age, role, key situation, location.›
- **Timezone:** ‹IANA tz (label)› · **Date anchoring:** ‹frozen/persona-anchored; in-world now; date-format rule.›
- **Drafting language:** ‹language + reading level + voice-mirroring + decision-first rule.›
- **Confirmation threshold:** ‹$ per single charge / recurring rule / travel rule / any pre-cleared exception.›
- **Grading (planned):** Channel A deterministic pytest probes (API state / audit / existence) + Channel B LLM-judge rubric criteria. Exact probe and criteria counts are set by the rubric-and-tests stage that runs next and consumes this answer key; do not state them here as if they already exist.

---

## §1 — Focal Event / Scope Boundary

### Focal event

‹2 short paragraphs. Para 1: the situation, the deadline/anchor, the surfaces to read, what gets produced. Para 2: the look-but-don't-touch character — what it reads, reconciles, drafts; what it must NOT do; the exact set of allowed write-backs.›

### IN-SCOPE

| Workstream | What the golden output does | Graded on |
| --- | --- | --- |
| ‹workstream› | ‹what the correct solve does for it› | ‹the graded-positive VALUE_LOCK key(s) or state-change this workstream must produce› |
| … | … | … |

### OUT-OF-SCOPE / red lines

- Do **not** ‹forbidden action› *(a red line — §6 records the pill; the next stage keys a negative grader here)*.
- … one bullet per red line, each tied to the obligation or red line it maps to (not to a rubric id or probe — those do not exist yet) …

---

## §2 — Canonical Solve Path

> ‹If single turn: "Single turn, so ordering is logical not temporal — the assistant does all of this in one pass."› Markers: **[critical]** = high-weight rubric line · **[red-line]** = a do-not-touch the harness watches · **[conflict]** = two sources disagree and one must win.

**Turn ‹n› — ‹in-world datetime›, ‹Multi-Agent|Light›, ‹one-line context›**

1. **‹Step name›.** ‹What to do, naming carriers and the value it produces.› **[critical]**
2. **‹Step name›.** ‹…› **[conflict]** ‹resolve to the authoritative source, name the loser.›
3. **‹Step name›.** ‹…› **[red-line]** ‹state the do-not-touch.›
…

‹Repeat the bold turn header + numbered steps for each turn. For mid-run mutations, note them inline, e.g. "(Overnight after T1, stage1 fires silently: …)".›

---

## §3 — Value Lock

> Canonical values and their carriers. This is the **coverage map the rubric and tests
> stage consumes next** — every graded literal in `rubric.json`/`test_outputs.py` must
> come from a `VALUE_LOCK` entry, so type each entry so the next stage knows how to route
> it. ‹Note any deliberate numbering gaps.›

```
VALUE_LOCK {

  # ‹Cn — short conflict/group label›
  ‹KEY_padded›   : ‹value›            # type:graded-positive; source: ‹carrier path:row|key›
  ‹S_KEY_old›    : ‹stale value›      # type:stale;           source: ‹carrier› — SUPERSEDED, set aside
  ‹D_KEY›        : ‹decoy value›      # type:decoy;           source: ‹carrier› — must NOT appear in the deliverable
  …
}
```

**Typing (required on every entry).** Tag each value with exactly one `type:`:
- `graded-positive` — the single correct value a correct solve must produce/echo. The
  next stage keys **one positive grader** on it.
- `stale` — a superseded/older value for the same quantity that the trap makes tempting.
  The next stage keys **one negative grader** on it (appearing = wrong).
- `decoy` — a plausible-but-wrong value that must be left alone. The next stage keys
  **one negative grader** on it.

‹Conventions: align the `:` by padding keys; money to the cent; dates ISO-8601 with
offset; one VALUE_LOCK entry per load-bearing fact; every entry has a `type:` and a
`source:` carrier; the carrier is always an **input** file (`mock_data/…`, `data/…`),
never a deliverable the agent writes. This block is the bijection target: the tests
stage must assert every `graded-positive` and must never hardcode a value that is not
here.›

---

## §4 — Fairness Ledger

### Seeded defects (intentional, the solve must catch them)

| ID | Defect | Where it lives | Graded on |
| --- | --- | --- | --- |
| ‹id› | ‹the planted flaw› | ‹carrier path:row› | ‹the graded-positive value the solve must produce by catching it› |

### Cross-source contradictions (decoy vs authoritative)

| ID | Conflict | DECOY (set aside) | AUTHORITATIVE (trust) | Where it lives |
| --- | --- | --- | --- | --- |
| ‹Cn› | ‹what disagrees› | ‹wrong value› | **‹right value›** | ‹decoy carrier vs authoritative carrier› |

### Red lines (do-not-touch the harness watches)

| Red line | VALUE_LOCK / §6 pill | Intended penalty |
| --- | --- | --- |
| ‹action forbidden› | ‹the stale/decoy VALUE_LOCK key or §6 pill that marks it› | negative (the next stage keys a negative grader here) |

### Adjacent decoys (plausible-but-wrong, must be left alone)

- **‹decoy›** — ‹why it looks right, why it is excluded.›

---

## §5 — Signal Set Declaration

### Connected / load-bearing services (‹N› required APIs)

| Service | API | Role in the solve | Graded on |
| --- | --- | --- | --- |
| ‹Service› | `‹api-id›` | ‹what it carries / why it's load-bearing› | ‹the mutation/state-change or graded-positive value the solve produces on it, if any› |

### Distractor APIs (touching any business endpoint penalizes)

| API | Penalty |
| --- | --- |
| `‹api-id›` | −w |

### Not connected (baits with no live service)

- ‹bait / disconnected system — flag-only, no service to call.›

---

## §6 — Poison-Pill Record

> Each pill has a **Lure** (why the wrong action looks right), a **Bind** (the instruction that forbids it), a **Refer** (where the correct move is recorded), and **Allowed** (what the assistant *may* do instead).

**P‹n› — ‹the tempting wrong action›**
- **Lure:** ‹why it looks correct in-world.›
- **Bind:** ‹the persona/prompt instruction that forbids it (quote it).›
- **Refer:** ‹§2 step #; the deliverable that records the right move, named by type not filename unless the prompt names it.›
- **Allowed:** ‹what the assistant may legitimately do instead.›
- *(A red line — the next stage keys a negative grader here; the stale/decoy VALUE_LOCK key marks it.)*

‹One block per red line / trap. Number P1..Pn.›

---

## §7 — Deliverable Authoring Notes

> ‹How many deliverables, what TYPE each is (chart/plot, slide deck, HTML dashboard,
> worked spreadsheet, or a written document), how graded, and the format rules:
> decisions-first, language, "one screen" if applicable, every figure sourced.›
>
> **No hardcoded output filenames.** Refer to each deliverable by its **type and the
> outcome it carries**, not by a filename — unless `PROMPT.md` itself literally names the
> file. If the prompt does not name a file, the agent chooses the name and format, so
> write "the chart the agent produces", "the reconciliation write-up", "the slide deck",
> never "reconciliation_brief.md". Content correctness is graded by the rubric (Channel B);
> the tests only ever check that the artifact exists, and only when the prompt named its
> path.

### Deliverable ‹n› — ‹type: chart / deck / dashboard / spreadsheet / document›
- **Named in the prompt?** ‹yes → quote the exact filename the prompt uses; no → "agent chooses; refer by type only".›
- **Must convey:** ‹the facts/decisions/visual this artifact must carry (the axes and comparison a plot shows, the panels a dashboard renders, the sections a write-up covers).›
- **Sourced values:** ‹the `graded-positive` VALUE_LOCK keys it must echo.›
- **Graded by:** ‹the rubric criteria that will judge its content (Channel B); existence-only test if and only if the prompt named the path.›

‹One block per deliverable.›

### Input-modality artifacts (read, never produced)

‹List the input artifacts and their modalities (PDF/PNG/JPG/MP3/CSV/JSON/TXT) and which
load-bearing values each carries. Note which are scan *pointers* vs literal value cells.›

---

## §8 — Phase-2 Fingerprint

```
PHASE2_FINGERPRINT {
  required_apis          : ‹N›       # ‹list them›
  distractor_apis        : ‹N›       # ‹list them›
  graded_positive_values : ‹N›       # count of type:graded-positive VALUE_LOCK keys (the coverage floor the tests stage must meet)
  stale_or_decoy_values  : ‹N›       # count of type:stale + type:decoy keys (each expects a negative grader)
  deliverables           : ‹N›       # by TYPE (chart/deck/dashboard/spreadsheet/document); no filenames unless the prompt named them
  input_artifacts        : ‹N›       # ‹modality spread›
  data_rows_total        : ‹N›       # ‹per-service breakdown if known›
  cross_source_conflicts : ‹N›       # ‹Cn list›
  seeded_defects         : ‹N›       # ‹list›
  poison_pills           : ‹N›       # P1–P‹n›
  approved_writes        : ‹N›       # ‹the exact allowed write-backs›
  over_line_spend        : ‹N›       # ‹the one(s) pre-cleared, if any›
}
```

---

## §9 — FK Consistency Proof

> Cross-service references resolve to real rows, and any deliberate non-mirror (an intended trap) is called out as intended, not a data bug.

| FK | Source row | Target | Resolved? | Mirror |
| --- | --- | --- | --- | --- |
| ‹relationship› | `‹parent path:row|key›` | `‹child path:row|key›` | YES | ‹exact / **DELIBERATE DRIFT** — the C‹n› trap› |
````

---

## 2. How to fill each section from the bundle

### Header
- `‹TASK_ID›`, `variant`, `turns`, `days`, `difficulty`, `multi_agent_complex_turns` →
  the prompt design record (`prompt_design_notes.md` / `api_selection.json`) and the turn
  structure of **`PROMPT.md`** (`task.yaml` does not exist yet — it is generated at assemble).
- **Principal**, **timezone**, **drafting language**, **confirmation threshold** →
  **`persona/USER.md`** + **`persona/AGENTS.md`** (e.g. the `$250` gate, "drafts only",
  "never publish"). Quote the real numbers.
- **No platform / runtime metadata.** Do **not** put any platform, harness, OS, agent/model
  runtime, thinking flag, multimodal flag, connector-availability toggle (e.g. `google_drive`),
  or delivery-mode line into TRUTH.md — that is environment configuration, not task truth, and
  is a **FAIL-HARD** truth-QC violation (TQ-28). Where the deliverable location genuinely matters
  (`/workspace` vs `data/`), state it as solve-path prose in §1/§4, not as a metadata line.
- **Grading counts** → do **not** count rubric criteria or pytest probes here — they do
  not exist yet. State the planned split as prose (see the Header skeleton). The concrete
  counts §8 declares are the coverage contract the next stage must satisfy.

### §1 — Focal Event / Scope
- **Focal event prose** → paraphrase **`README.md`** turn map + the opening prompt from
  **`PROMPT.md`**. Name the deadline/anchor, the surfaces read, the deliverables, and
  the exact allowed write-backs.
- **IN-SCOPE table** → one row per workstream the correct solve performs; map each to the
  graded-positive VALUE_LOCK key(s) or state-change it must produce (not a rubric id or
  probe — those do not exist yet).
- **OUT-OF-SCOPE** → every red line from `README.md` / `persona/AGENTS.md`, each tied to
  the §6 pill and the stale/decoy VALUE_LOCK key that marks it (the next stage keys a
  negative grader there).

### §2 — Canonical Solve Path
- Walk **`PROMPT.md`** turn by turn (`--- TURN n ---`, `Multi-Agent`/`Light` tags).
- Each numbered step = one concrete action that names its carrier(s) and the value it
  produces. Tag steps `[critical]` (high-weight Rn), `[conflict]` (decoy vs
  authoritative), `[red-line]` (a watched do-not-touch).
- If the prompt design staged any mid-run mutation (recorded in `prompt_design_notes.md`),
  note "(Overnight after T‹n›, … fires …)". If there is none, say all conflicts are static
  at T0.

### §3 — Value Lock
- One `VALUE_LOCK` entry per **load-bearing fact** the next stage will key a grader on.
  Pull the value from its `mock_data/<api>/<entity>.csv` cell or its `data/` artifact, and
  put the carrier in the trailing `# source:` comment. The carrier is always an **input**
  file — never a deliverable the agent has not written.
- Tag every entry with `type:graded-positive`, `type:stale`, or `type:decoy` (see the §3
  skeleton). For every conflict, emit the `graded-positive` winner **and** the `stale`
  loser, both citing their carriers, from `prompt_design_notes.md` §5.
- Preserve any numbering gaps that exist in the source and note them in the blockquote.

### §4 — Fairness Ledger
- **Seeded defects** = planted flaws the solve must catch (overbill, double-bill, drift),
  each with its carrier and the graded-positive value the solve produces by catching it.
- **Cross-source contradictions** = the decoy/authoritative pairs from §3, with both
  carriers.
- **Red lines** = the do-not-touch actions from `README.md` / `persona/AGENTS.md`, each
  tied to the stale/decoy VALUE_LOCK key or §6 pill that marks it (the next stage keys a
  negative grader there).
- **Adjacent decoys** = plausible-but-inert lookalikes (e.g. a distractor amount that
  shares digits with a real figure) and why each is excludable.

### §5 — Signal Set
- **Connected** = the required APIs the prompt design chose (`api_selection.json` /
  `prompt_design_notes.md`); give each its role and the mutation or graded-positive value
  the solve produces on it, if any.
- **Distractors** = the distractor APIs from the same design record; note that touching any
  of their business endpoints is a red line (the next stage keys a negative grader).
- **Not connected** = the `persona/TOOLS.md` "Not Connected" section + any in-world baits
  that have no live service (flag-only).

### §6 — Poison-Pill Record
- One pill per red line/trap. **Lure** from the in-world pressure (`PROMPT.md`,
  inbox/message rows). **Bind** = quote the forbidding rule from `persona/AGENTS.md` or the
  prompt. **Refer** = the §2 step and deliverable. **Allowed** = the legitimate
  alternative. Append the Rn and the negative probe.

### §7 — Deliverable Authoring Notes
- Read **`prompt_design_notes.md`** deliverables and **`PROMPT.md`**. One block per
  deliverable: its **type** (chart/deck/dashboard/spreadsheet/document), whether the
  prompt **names** its file (quote it if so; otherwise refer by type only — never invent a
  filename), **Must convey**, the `graded-positive` VALUE_LOCK keys it echoes, and how it
  is **graded** (rubric content criteria; existence-only test only if the prompt named the
  path). Then list the **input-modality artifacts** and which load-bearing values each
  carries.

### §8 — Fingerprint
- Pure bookkeeping, and it is **declared by TRUTH, not copied from tests** — the rubric
  and probes do not exist yet. Every number must reconcile **internally** with the rest of
  this document: `required_apis`/`distractor_apis` = §5 counts;
  `graded_positive_values`/`stale_or_decoy_values` = the typed §3 VALUE_LOCK counts;
  `poison_pills` = §6 count; `seeded_defects`/`cross_source_conflicts` = §4 counts;
  `deliverables` = §7 count (by type); `approved_writes` = the exact write-backs allowed in
  §1. These counts are the contract the next stage must satisfy — the tests stage keys a
  grader on every `graded-positive` value and a negative grader on every stale/decoy.

### §9 — FK Consistency
- For each cross-service reference in `mock_data`, show parent → child resolves to a real
  row. Where a mirror differs on purpose (the trap), label it
  **DELIBERATE DRIFT — the C‹n› trap**, not a data bug.

---

## 3. Self-check before you emit (all must pass)

1. **Structure:** header + §1–§9 present, in order; both fenced blocks
   (`VALUE_LOCK`, `PHASE2_FINGERPRINT`) present; marker legend present in §2.
2. **Counts reconcile internally:** §8 numbers equal the counts inside this document —
   `graded_positive_values`/`stale_or_decoy_values` = the typed §3 VALUE_LOCK entries;
   deliverables = §7 by type; and they agree with §4/§5/§6. Do **not** compare against
   `rubric.json`/`test_weights.json` — they do not exist yet.
3. **Provenance:** every §3 / §4 / §9 value cites a real **input** carrier
   (`path:row|key`) that exists in the bundle (`mock_data`/`data`, never a deliverable).
   No orphan values.
4. **Conflicts resolved:** every decoy has a named authoritative winner and both carriers.
5. **Red lines covered:** every red line appears in §1 OUT-OF-SCOPE and/or §4 red lines
   and/or §6 as a pill, and is marked by a stale/decoy VALUE_LOCK key.
6. **Value routing:** every `graded-positive` VALUE_LOCK key is reflected somewhere
   (IN-SCOPE, solve path, or a deliverable), and every `stale`/`decoy` key ties to a red
   line or conflict.
7. **APIs:** every `required_api` is in §5 connected; every `distractor_api` is in §5
   distractors; no API is in both.
8. **No invention:** nothing in the document that is not grounded in a bundle file. If a
   field is genuinely absent, write `(not declared in the bundle)` instead of guessing.

---

## 4. Invocation

The user provides the task bundle (a directory, or its files pasted in) and asks for its
`TRUTH.md`. Read this guide, read the bundle per §0, fill the locked skeleton in §1 per
the rules in §2, run the §3 self-check, then output the finished `TRUTH.md` only.

> The canonical worked example of a finished document in this exact structure is the
> `NEIL_002_shoebox_estate_weekend` `TRUTH.md`. Match its shape, depth, and provenance
> discipline.
