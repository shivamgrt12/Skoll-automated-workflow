# TRUTH_GUIDE.md — How to generate a `TRUTH.md` from a task bundle

> **What this file is.** This is the *generator*. There is no Python script and no
> parser any more. To produce a `TRUTH.md` for a task, you (the model) read this
> guide, then read the **entire task bundle** the user hands you, and emit a single
> `TRUTH.md` that follows the exact nine-section structure locked below.
>
> **The contract.** Whatever bundle is provided, the output must (a) use the **same
> structure** every time (header + §1–§9, the two fenced blocks, the markers, the
> tables), and (b) be **correct and complete** — every value, red line, API, probe,
> and deliverable that exists in the bundle must be represented and must trace back to
> a real carrier in the bundle. Never invent a number, a date, an email, a probe, or a
> rubric line. If the bundle does not contain something, say so explicitly rather than
> guessing.
>
> `TRUTH.md` is **reference-only**: it documents the intended solve and grading. It is
> **not** consumed by the harness at runtime.

---

## 0. Inputs — what the bundle contains and what each file is for

A complete task bundle looks like this (names are stable across tasks):

```
<TASK_DIR>/
├── README.md                  # human overview: turn map, traps, red lines
├── task.yaml                  # machine facts: ids, apis, turns/days/difficulty, variant, system_prompt
├── rubric.json                # Channel B — LLM-judge criteria R1..Rn (the +/- rubric)
├── test_outputs.py            # Channel A — deterministic pytest probes (audit-based)
├── test_weights.json          # weight (±) for every probe in test_outputs.py
├── PROMPT.md                  # the actual turn prompts (--- TURN n --- blocks, Multi-Agent/Light tags)
├── TASK_PHASE1.md             # (optional) volume bands / construction notes
├── persona/                   # AGENTS.md, SOUL.md, IDENTITY.md, USER.md, TOOLS.md, MEMORY.md
│   └── …                      #   → confirmation threshold, connected vs not-connected, voice, contacts
├── mock_data/<api>/<entity>.csv   # the live world state per service (the carriers)
├── data/                      # input artifacts (pdf/png/jpg/mp3/csv/json/txt) + README.md, and where the agent writes deliverables
└── inject/stage{0,1,2}/STAGE*_INJECT.json   # mid-run mutations (silent/loud); may be empty
```

**Where each TRUTH section gets its facts (read these, in this order):**

| To fill… | Read primarily… | Cross-check against… |
|---|---|---|
| Header bullets | `task.yaml`, `persona/AGENTS.md`, `persona/USER.md`, `README.md` | `rubric.json` count, `test_weights.json` count |
| §1 Focal Event / Scope | `README.md` (turn map, red lines), `PROMPT.md`, `persona/AGENTS.md` | `rubric.json`, `test_weights.json` |
| §2 Canonical Solve Path | `PROMPT.md` (turns), `README.md`, `golden_steer`/QC notes if present | `rubric.json` ordering |
| §3 Value Lock | `mock_data/<api>/*.csv`, `data/` artifacts | `rubric.json` (which value each Rn keys on) |
| §4 Fairness Ledger | `inject/stage*/*.json`, `mock_data` decoy rows, `README.md` traps | `test_weights.json` negatives |
| §5 Signal Set | `task.yaml` `required_apis` / `distractor_apis`, `persona/TOOLS.md` "Not Connected" | `test_outputs.py` URLs, `test_weights.json` |
| §6 Poison-Pill | `README.md` red lines, `persona/AGENTS.md` rules, `PROMPT.md` pressures | `rubric.json` (−) lines, `test_weights.json` (−) |
| §7 Authoring Notes | `data/README.md`, deliverable specs in `rubric.json`/prompts | `mock_data`, artifacts |
| §8 Fingerprint | counts derived from all of the above | every other section (must reconcile) |
| §9 FK Consistency | `mock_data/<api>/*.csv` foreign keys | `inject/*` (intended drift only) |

**Golden rule of provenance.** Every load-bearing value in §3, §4, and §9 must cite a
**carrier** — a real `path:row|key` inside the bundle (e.g.
`mock_data/plaid-api/transactions.csv:txn_pension:amount` or
`data/nasa_milwaukee_irradiance_chart.png`). If two sources disagree, name the
**authoritative** one and the **decoy** one; never silently pick.

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
- **Platform:** harness = ‹harness name› · agent = ‹agent name› · multimodal = ‹true|false› · google_drive = ‹true|false› (deliverables are ‹/workspace|data/› files).
- **Grading:** Channel A `test_outputs.py` (‹N› deterministic pytest probes, weighted) + Channel B `rubric.json` (‹N› LLM-judge criteria, R1–R‹n›).

---

## §1 — Focal Event / Scope Boundary

### Focal event

‹2 short paragraphs. Para 1: the situation, the deadline/anchor, the surfaces to read, what gets produced. Para 2: the look-but-don't-touch character — what it reads, reconciles, drafts; what it must NOT do; the exact set of allowed write-backs.›

### IN-SCOPE

| Workstream | What the golden output does | Rubric / tests |
| --- | --- | --- |
| ‹workstream› | ‹what the correct solve does for it› | ‹R‹n› (+w); `test_…`› |
| … | … | … |

### OUT-OF-SCOPE / red lines

- Do **not** ‹forbidden action› *(R‹n›; `test_…_detected` = −w)*.
- … one bullet per red line, each tied to its rubric id and/or negative probe …

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

> Canonical values and their carriers. Each is the single correct number/date the deliverables must echo; the DECOY column in §4 lists what must be set aside. ‹Note any deliberate numbering gaps.›

```
VALUE_LOCK {

  # ‹Cn — short conflict/group label›
  ‹KEY_padded›   : ‹value›            # ‹carrier path:row|key; second carrier if any›
  ‹S_KEY_old›    : ‹stale value›      # ‹carrier› — SUPERSEDED, set aside (R‹n› decoy)
  …
}
```

‹Conventions: align the `:` by padding keys; money to the cent; dates ISO-8601 with
offset; one VALUE_LOCK entry per load-bearing fact; every entry has a `# source:`
carrier; mark superseded/stale entries inline so §4 and §9 can reference them.›

---

## §4 — Fairness Ledger

### Seeded defects (intentional, the solve must catch them)

| ID | Defect | Where it lives | Caught by |
| --- | --- | --- | --- |
| ‹id› | ‹the planted flaw› | ‹carrier path:row› | ‹R‹n›› |

### Cross-source contradictions (decoy vs authoritative)

| ID | Conflict | DECOY (set aside) | AUTHORITATIVE (trust) | Where it lives |
| --- | --- | --- | --- | --- |
| ‹Cn› | ‹what disagrees› | ‹wrong value› | **‹right value›** | ‹decoy carrier vs authoritative carrier› |

### Red lines (do-not-touch the harness watches)

| Red line | Probe | Weight |
| --- | --- | --- |
| ‹action forbidden› | `test_…_detected` | −w |

### Adjacent decoys (plausible-but-wrong, must be left alone)

- **‹decoy›** — ‹why it looks right, why it is excluded.›

---

## §5 — Signal Set Declaration

### Connected / load-bearing services (‹N› required APIs)

| Service | API | Role in the solve | Probe (weight) |
| --- | --- | --- | --- |
| ‹Service› | `‹api-id›` | ‹what it carries / why it's load-bearing› | `test_…` (+w) |

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
- **Refer:** ‹§2 step #; the deliverable that records the right move.›
- **Allowed:** ‹what the assistant may legitimately do instead.›
- *(R‹n›; `test_…_detected` = −w)*

‹One block per red line / trap. Number P1..Pn.›

---

## §7 — Deliverable Authoring Notes

> ‹How many deliverables, where written (/workspace or data/), how graded (which Rn), the format rules: decisions-first, language, "one screen" if applicable, every figure sourced.›

### `‹/workspace|data›/‹deliverable_filename›.md`
- **Must contain:** ‹the facts/decisions this file must carry.›
- **Suggested H2s:** ‹section · section · section.›
- **Tests:** ‹R‹n›; supports R‹a›, R‹b›.›

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
  pytest_probes          : ‹N›       # ‹positive/negative breakdown›
  rubric_criteria        : ‹N›       # R1–R‹n› ‹note any gaps›
  positive_rubric_max    : ‹the +max lines, e.g. R1,R3,R6…›
  deliverables           : ‹N›       # ‹ids›, ‹location›, graded by R‹n›
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
  **`task.yaml`**.
- **Principal**, **timezone**, **drafting language**, **confirmation threshold** →
  **`persona/USER.md`** + **`persona/AGENTS.md`** (e.g. the `$250` gate, "drafts only",
  "never publish"). Quote the real numbers.
- **Platform / multimodal / google_drive** → `task.yaml` `system_prompt` (`Workspace`
  block tells you `/workspace` vs `data/`) and whether artifacts are multimodal.
- **Grading counts** → count entries in **`rubric.json`** (Channel B) and keys in
  **`test_weights.json`** (Channel A). These two counts must match §8.

### §1 — Focal Event / Scope
- **Focal event prose** → paraphrase **`README.md`** turn map + the opening prompt from
  **`PROMPT.md`**. Name the deadline/anchor, the surfaces read, the deliverables, and
  the exact allowed write-backs.
- **IN-SCOPE table** → one row per workstream the correct solve performs; map each to its
  rubric id(s) (`rubric.json`) and probe(s) (`test_weights.json`).
- **OUT-OF-SCOPE** → every red line from `README.md` / `persona/AGENTS.md`, each tied to
  its **negative** rubric line and/or `test_…_detected` weight.

### §2 — Canonical Solve Path
- Walk **`PROMPT.md`** turn by turn (`--- TURN n ---`, `Multi-Agent`/`Light` tags).
- Each numbered step = one concrete action that names its carrier(s) and the value it
  produces. Tag steps `[critical]` (high-weight Rn), `[conflict]` (decoy vs
  authoritative), `[red-line]` (a watched do-not-touch).
- Inject mutations where they fire: read **`inject/stage1|stage2/STAGE*_INJECT.json`**
  and note "(Overnight after T‹n›, stage‹k› fires …)". If `mutations: []`, say there is
  no mid-run mutation and all conflicts are static at T0.

### §3 — Value Lock
- One `VALUE_LOCK` entry per **load-bearing fact** a checker keys on. Pull the value from
  its `mock_data/<api>/<entity>.csv` cell or its `data/` artifact, and put the carrier in
  the trailing `# source:` comment.
- For every conflict, emit the authoritative entry **and** the superseded/stale entry,
  marking the latter `SUPERSEDED … (R‹n› decoy)`.
- Preserve any numbering gaps that exist in the source and note them in the blockquote.

### §4 — Fairness Ledger
- **Seeded defects** = planted flaws the solve must catch (overbill, double-bill, drift),
  each with its carrier and the Rn that catches it.
- **Cross-source contradictions** = the decoy/authoritative pairs from §3, with both
  carriers.
- **Red lines** = the **negative** probes from `test_weights.json` (`test_…_detected`,
  `test_…_write_detected`, distractor touches) with their weights.
- **Adjacent decoys** = plausible-but-inert lookalikes (e.g. a distractor amount that
  shares digits with a real figure) and why each is excludable.

### §5 — Signal Set
- **Connected** = `task.yaml:required_apis`; give each its role and its **positive** probe
  from `test_weights.json`. (Map probe → service via the `*_API_URL` constants and
  function bodies in `test_outputs.py`.)
- **Distractors** = `task.yaml:distractor_apis`; weight = the `test_…_distractor_touched`
  penalty.
- **Not connected** = the `persona/TOOLS.md` "Not Connected" section + any in-world baits
  that have no live service (flag-only).

### §6 — Poison-Pill Record
- One pill per red line/trap. **Lure** from the in-world pressure (`PROMPT.md`,
  inbox/message rows). **Bind** = quote the forbidding rule from `persona/AGENTS.md` or the
  prompt. **Refer** = the §2 step and deliverable. **Allowed** = the legitimate
  alternative. Append the Rn and the negative probe.

### §7 — Authoring Notes
- Read **`data/README.md`** and the deliverable-related rubric lines. One block per
  deliverable: **Must contain**, **Suggested H2s**, **Tests** (the Rn that grades it +
  the Rn it supports). Then list the **input-modality artifacts** and which load-bearing
  values each carries.

### §8 — Fingerprint
- Pure bookkeeping. Every number must reconcile with the rest of the document:
  `required_apis`/`distractor_apis` = §5 counts; `rubric_criteria` = `rubric.json` length;
  `pytest_probes` = `test_weights.json` length (split +/-); `poison_pills` = §6 count;
  `seeded_defects`/`cross_source_conflicts` = §4 counts; `deliverables` = §7 count;
  `approved_writes` = the exact write-backs allowed in §1.

### §9 — FK Consistency
- For each cross-service reference in `mock_data`, show parent → child resolves to a real
  row. Where a mirror differs on purpose (the trap), label it
  **DELIBERATE DRIFT — the C‹n› trap**, not a data bug.

---

## 3. Self-check before you emit (all must pass)

1. **Structure:** header + §1–§9 present, in order; both fenced blocks
   (`VALUE_LOCK`, `PHASE2_FINGERPRINT`) present; marker legend present in §2.
2. **Counts reconcile:** §8 numbers equal the real lengths of `rubric.json` and
   `test_weights.json` and the counts in §4/§5/§6/§7.
3. **Provenance:** every §3 / §4 / §9 value cites a real carrier
   (`path:row|key`) that exists in the bundle. No orphan values.
4. **Conflicts resolved:** every decoy has a named authoritative winner and both carriers.
5. **Red lines covered:** every negative probe in `test_weights.json` appears in §1
   OUT-OF-SCOPE and/or §4 red lines and/or §6 as a pill.
6. **Rubric coverage:** every `Rn` in `rubric.json` is reflected somewhere (IN-SCOPE,
   solve path, red line, or deliverable).
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
