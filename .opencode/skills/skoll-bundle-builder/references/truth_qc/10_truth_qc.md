# TRUTH.md QC — Grounding & Alignment Auditor (self-contained, task-agnostic)

> **Role.** You are the TRUTH.md auditor. Given one task bundle, verify that `TRUTH.md` is a
> fully grounded, internally consistent golden-truth reference, and that **every other file in the
> bundle aligns with it**. This checklist is **fully self-contained** — it embeds everything it
> needs and requires **no** other QC prompt, **no** reference/gold bundle, and **no** external file;
> the only files you read are those of the single task bundle under review. It is also
> **task-agnostic** (it enforces *consistency and grounding rules*, never numbers copied from any
> specific task).
>
> **What TRUTH.md is.** It is the single golden-truth reference for the task, and it is the
> **answer key the rubric-and-tests stage consumes next**. TRUTH.md is authored right after the
> prompt stage and **before** `rubric.json` and `test_outputs.py` exist. **Detect which phase you
> are auditing by file presence** (see the Inputs note below): if `rubric.json` /
> `test_outputs.py` / `test_weights.json` are absent you are at authoring time — audit TRUTH.md
> standalone; if they are present you are auditing a final assembled bundle — additionally run the
> backward reconciliation described below. In the final shipped bundle TRUTH.md is reference-only and is not
> consumed by the grading harness; here you are auditing it as the source of truth that the prompt,
> persona, data, and mock_data are measured against, and as the coverage map (its typed VALUE_LOCK)
> that the rubric and tests will later key on. If TRUTH.md and an **input** file (prompt, persona,
> data, mock_data, design notes) disagree, that is a defect to report (decide which side is wrong
> from the grounded sources — do not assume TRUTH.md is automatically right if the data contradicts it).
>
> **Task-agnostic principle.** Never enforce a value carried over from another task. Every count
> and value (typed VALUE_LOCK entries, APIs, dates, IDs, amounts, file counts) is **derived from the
> task under review** and cross-checked for agreement against the **inputs that exist** (PROMPT.md,
> prompt_design_notes.md, mock_data, persona). Any concrete value shown below is an *illustrative
> example only* and must not be enforced literally.
>
> **Output.** Produce a Markdown QC report (suggested name `QC_REPORT_TRUTH.md`) with one row per
> check: **Check · Verdict · Evidence (file + line/quote) · Notes**, then a final roll-up verdict.
> Severities: **red / Major** (blocks push), **Moderate**, **Minor (cleanup)**, **FAIL-HARD**
> (auto-fail regardless of other results).

---

## Inputs (read all of these from the task under review)

`TRUTH.md` (subject) · `PROMPT.md` (single-turn brief — this is the **only** accepted prompt
filename; `prompts.txt` is **not** accepted) · `prompt_design_notes.md` (the design record TRUTH.md
is built from) · `mock_data_changes.json` (enrichment/edit log) · `README.md` (if present) ·
`api_selection.json` (if present) · `persona/*` · `data/*` (or `home/*`) · `mock_data/<api>-api/*`.

> **Phase detection (presence-conditional):** `rubric.json`, `test_outputs.py`, `test_weights.json`,
> `task.yaml` may or may not exist depending on when this gate runs.
>
> - **If they are ABSENT** (mid-stage: TRUTH.md was just authored, before the rubric-and-tests and
>   assemble stages): do NOT hunt for them or fail on their absence. Audit TRUTH.md standalone —
>   every check that would compare TRUTH.md against them is a **forward contract** on TRUTH.md
>   itself (see D/E/F), not a cross-file reconciliation.
> - **If they are PRESENT** (final assembled bundle audit): in ADDITION to every check below, run
>   the **backward reconciliation**: (1) every `type:graded-positive` VALUE_LOCK key is covered by
>   **exactly one** grader — a pytest test in `test_outputs.py` (API-observable values, asserted
>   against the mock server) OR a rubric criterion in `rubric.json` (deliverable-only values) —
>   never both, never neither; (2) every `type:stale` / `type:decoy` key tied to a conflict or red
>   line keys a negative grader (negative-weight test or negative criterion) in exactly one channel;
>   (3) no graded literal asserted in `test_outputs.py` or quoted in `rubric.json` is absent from
>   VALUE_LOCK. An orphaned graded-positive key, a double-graded value, or an invented graded
>   literal is a **Major** defect.

---

## Expected TRUTH.md anatomy (embedded — no external reference needed)

A well-formed TRUTH.md carries a **header/metadata block** plus the load-bearing sections below.
Section titles/numbers may vary by generator version; check for the *substance*, not the exact
heading text.

- **Header / metadata:** a reference-only disclaimer, Task ID, principal/persona identity,
  timezone + in-world "now" date anchoring, confirmation threshold, and a **planned** grading
  summary in prose (Channel A deterministic pytest + Channel B rubric — exact probe/criteria counts
  are set later by the rubric-and-tests stage and must NOT be stated here as if they exist).
  **Platform/runtime metadata (harness/OS, agent + model runtime, thinking flag, multimodal flag,
  connector-availability flags, delivery mode) must NOT appear here — see TQ-28.**
- **§ Focal Event / Scope:** the scenario, the asks, and an explicit **out-of-scope / red-line** list.
- **§ Canonical Solve Path:** the ordered "golden solve" steps, ideally marked
  `[critical]` / `[conflict]` / `[red-line]`, each tied to the **graded-positive VALUE_LOCK key(s)
  or state-change** it produces (not to a rubric ID or probe name — those do not exist yet).
- **§ Value Lock:** the locked anchor values (identities, dates, amounts, IDs, statuses), **each
  typed** `type:graded-positive` / `type:stale` / `type:decoy` and **each citing a real INPUT
  carrier** (a `data/`, `mock_data/<api>` record, or `persona/` file that holds it — never a
  deliverable the agent has not written). Conflicts are expressed as a `graded-positive` winner plus
  a `stale`/`decoy` loser, both citing carriers.
- **§ Fairness Ledger:** seeded defects (silent mutations), cross-source contradictions
  (decoy vs authoritative), red lines, and adjacent decoys — each tied to its VALUE_LOCK type.
- **§ Signal Set:** connected APIs (with the state-change/graded-positive value they produce, if
  any), **callable** distractor APIs (folder + `*_API_URL`; touching their business endpoints is a
  red line), and **persona-only** not-connected narrative baits (no folder, no env var — they live
  only in `persona/TOOLS.md` / TRUTH.md prose).
- **§ Poison-Pill Record:** each lure with its bind (quote), the reason it is refused/held, the
  allowed behavior, and the `stale`/`decoy` VALUE_LOCK key that marks it (the next stage keys a
  negative grader there).
- **§ Deliverable Authoring Notes:** what each deliverable must contain, **referred to by type**
  (chart / deck / dashboard / spreadsheet / document), never by a hardcoded output filename unless
  `PROMPT.md` literally names the file (see TQ-29).
- **§ Fingerprint (counts):** a machine-readable count block whose numbers are **declared by TRUTH
  and reconcile internally** (APIs, graded-positive values, stale/decoy values, deliverables by
  type, conflicts, defects, poison pills) — not copied from a rubric or test file.
- **§ FK Consistency:** foreign-key/reference resolutions across records, and deliberate drifts.

---

## A. Structure & completeness of TRUTH.md

**TQ-1 — Reference-only disclaimer present.**
TRUTH.md must state it is the golden truth and is **not consumed by the grading harness** at
runtime (the shipped bundle is scored via the rubric and pytest that this answer key will produce).
Missing disclaimer → Minor; if TRUTH.md claims it is itself the graded artifact → Major.

**TQ-2 — Load-bearing sections present.**
The header/metadata block plus the Focal Event, Canonical Solve Path, Value Lock, Fairness Ledger,
Signal Set, and a counts/fingerprint block must all be present in substance. A missing load-bearing
section → Major; missing supporting section (Deliverable Notes, FK Consistency) → Moderate.

**TQ-3 — No truncation / placeholders.**
TRUTH.md must be complete: no cut-off tables, dangling code fences, "TODO/TBD/FIXME/XXX",
"..." elisions, or empty sections. Any truncation or unfilled placeholder → Major.

---

## B. Grounding (every asserted value traces to a real, matching source)

> **Grounding method.** For each locked/asserted value in TRUTH.md, follow its citation to the
> named source (a `data/` file, a `mock_data/<api>` record, a `persona/` file, `PROMPT.md`, or
> `prompt_design_notes.md`) and
> confirm the source **actually contains that value**. A value with no citation, a citation to a
> file that does not exist, or a citation whose content disagrees is a grounding defect.

**TQ-4 — Every Value-Lock anchor cites a real source.**
Each anchor in the Value Lock (and each key fact in the solve path) must name a source that exists
in the bundle. Uncited anchor → Moderate; citation to a non-existent file/record → Major.

**TQ-5 — Cited source content matches.**
The value TRUTH.md locks must equal what the cited source holds (IDs, amounts, statuses, dates).
Any mismatch between TRUTH.md and its own cited source → Major.

**TQ-6 — Persona anchors are grounded.**
Principal identity, DOB, timezone, confirmation threshold, and any roster/contact facts asserted in
TRUTH.md must match `persona/*` (e.g. `USER.md`, `MEMORY.md`, `AGENTS.md`). Mismatch → Major.

**TQ-7 — In-world "now" and timezone are consistent.**
A single in-world "now" timestamp and timezone must be declared and used consistently; all relative
timing ("14 hours before", "overnight", "two-day-stale") must be arithmetically consistent with it.
Contradictory or drifting now/timezone → Major.

---

## C. Internal consistency (dates, IDs, names, amounts cohere)

**TQ-8 — Date/time coherence.**
All dates/times in TRUTH.md must be mutually consistent and calendar-valid (correct weekday for a
given date, deadlines that precede the events they gate, no impossible ordering). Any impossible or
self-contradicting date → Major.

**TQ-9 — Identifier & name coherence.**
Every ID (record IDs, ticket keys, invoice/envelope IDs, page IDs, channel IDs) and proper name is
spelled and formatted identically everywhere it appears in TRUTH.md. Divergent spelling/casing of
the same entity → Moderate (Major if it would split a grading match).

**TQ-10 — Amounts & thresholds coherent.**
Monetary amounts, tax/derived figures, and threshold comparisons must be arithmetically correct and
consistent (e.g. a "held" amount is genuinely on the over-threshold side of the declared
threshold). Arithmetic or threshold-logic error → Major.

**TQ-11 — Recency-wins logic is sound.**
Where TRUTH.md says live state supersedes stale memory, the "live" value must be the one the APIs /
`mock_data` expose and the "stale" value the one in persona memory or a baseline export. An inverted
or ambiguous recency call → Major.

---

## D. Cross-file alignment (everything agrees with TRUTH.md)

**TQ-12 — Prompt alignment.**
Facts, constraints, and the in-world "now" in `PROMPT.md` must be consistent with TRUTH.md, and
every ask in the prompt must be represented in the solve path. For a single-turn brief the prompt
carries exactly one turn header (`--- TURN T1 ---`). Prompt asserts a fact that contradicts
TRUTH.md → Major; prompt ask missing from TRUTH.md → Moderate.

**TQ-13 — Decomposable into a rubric (forward contract).**
TRUTH.md must be decomposable into gradable obligations — every graded-positive VALUE_LOCK key, red
line, deliverable, and conflict resolution must be stated concretely enough that the rubric-and-tests
stage can later key exactly one grader to it. (Do **not** open `rubric.json`; it does not exist yet.)
A load-bearing obligation stated too vaguely to grade, or a conflict whose authoritative side is not
clearly the `graded-positive` value → Major.

**TQ-14 — Coverage map is well-formed (forward contract).**
The typed VALUE_LOCK is the coverage map the tests stage consumes. Every `graded-positive` entry
must be an observable the next stage can assert (an API state change / audit record, or a value in a
deliverable graded by the rubric), and every `stale`/`decoy` entry must tie to a red line or conflict
that earns a negative grader. (Do **not** open `test_outputs.py`/`test_weights.json`; they do not
exist yet.) A graded-positive value with no observable, or a stale/decoy value not tied to any red
line/conflict → Major; a large set of untyped or unroutable VALUE_LOCK entries → Moderate.

**TQ-15 — Data / mock_data alignment.**
Files and records TRUTH.md cites (data artifacts, API records) must exist and hold the stated
content, including the intended baseline-vs-live split (on-disk baseline vs API live state, when the
task uses that pattern). Missing cited artifact or wrong content → Major.

**TQ-16 — Persona/tooling alignment.**
Connectivity claims in TRUTH.md must match the prompt design record (`prompt_design_notes.md` /
`api_selection.json`) and `persona/TOOLS.md`, honoring the split:
**connected** and **callable distractor** services are folder-backed and env-var-backed; **persona-only
not-connected baits** appear only in `persona/TOOLS.md` / TRUTH.md prose and carry no folder, no
env var, and no probe. A service TRUTH.md calls connected but the task does not provide (or vice
versa) → Major; a persona-only bait wrongly given a folder/env-var/probe → Moderate.

---

## E. Conflict, red-line & poison-pill integrity

**TQ-17 — Conflicts name authoritative vs decoy.**
Every cross-source contradiction must explicitly label which side is **authoritative** and which is
the **decoy/superseded**, with both sources cited. An undocumented or unlabeled conflict → Major.

**TQ-18 — Authoritative side is typed graded-positive (forward contract).**
For each documented conflict, TRUTH.md must type the **authoritative** value `type:graded-positive`
and the superseded/decoy value `type:stale`/`type:decoy`, so the next stage rewards the authoritative
value and penalizes the decoy. A conflict whose authoritative side is not typed graded-positive, or
whose loser is left untyped (leaving the next stage free to reward the decoy) → Major.

**TQ-19 — Red lines are marked for negative grading (forward contract).**
Every red line / out-of-scope prohibition in TRUTH.md must be marked by a `stale`/`decoy` VALUE_LOCK
key and/or a §6 poison-pill record, so the next stage can key a **negative** grader to it — *except*
prohibitions that are purely persona-only not-connected baits (no callable surface), which are
enforced by narrative review. A callable red line with no stale/decoy or pill marking → Major; a
persona-only red line with no marking at all → Moderate.

**TQ-20 — Poison pills fully specified.**
Each poison pill must carry: the lure, a bind (quoted source/record), the refusal/hold reason, the
allowed behavior, and the `stale`/`decoy` VALUE_LOCK key that marks it (so the next stage keys a
negative grader there). Any missing element → Moderate (Major if the negative marking is absent).

**TQ-21 — not-connected vs distractor labeled correctly (two flavors).**
Distinguish the two kinds of off-limits bait:
- **Callable distractor** (folder-backed, `*_API_URL`-backed) — touching its business endpoints is a
  red line; it must be marked by a `stale`/`decoy` VALUE_LOCK key (the next stage keys a negative
  zero-hit grader here). A "not-connected" service that is nonetheless folder-backed (e.g. an
  e-signature surface the principal signs on herself) is marked here.
- **Persona-only not-connected bait** (web search, internal databases, external portals, family
  accounts) — has **no** folder and **no** env var; it is enforced by narrative review only.

Mislabeling a callable distractor as persona-only (or omitting its stale/decoy marking), or wrongly
attaching a folder/env var to a persona-only bait → Moderate.

---

## F. Fingerprint / count consistency (parametric)

**TQ-22 — Fingerprint reconciles internally.**
Every count in TRUTH.md's fingerprint/metadata must equal what TRUTH.md itself establishes and what
the **inputs** hold — required/connected count and distractor count (vs `prompt_design_notes.md` /
`api_selection.json` and the `mock_data/<api>-api/` folders), persona-only not-connected bait count,
`graded_positive_values` and `stale_or_decoy_values` (vs the typed VALUE_LOCK entries),
deliverables **by type** (vs §7), conflicts, defects, poison pills. Do **not** count rubric criteria
or pytest probes here — at authoring time they do not exist, and at final audit their coverage is
checked by the backward reconciliation (Inputs note), not by this fingerprint. Recompute each and
flag mismatches → Moderate (Major if it changes the coverage contract).

**TQ-23 — Typed value counts agree within TRUTH.md.**
`graded_positive_values` must equal the number of `type:graded-positive` VALUE_LOCK entries;
`stale_or_decoy_values` must equal the `type:stale` + `type:decoy` entries; deliverable count must
equal the §7 deliverable blocks (by type). These are **internal** reconciliations — do **not**
compare against `test_outputs.py` / `test_weights.json` / `rubric.json` / `README.md` here (absent
at authoring time; covered by the backward reconciliation at final audit). Any internal drift →
Moderate (Major if the coverage contract shifts).

**TQ-24 — API set agrees across the inputs.**
The **callable** API set in TRUTH.md (connected + distractor) must equal the union of the callable
APIs the prompt design chose (`prompt_design_notes.md` / `api_selection.json`) and the
`mock_data/<api>-api/` folders — a clean bijection across those two. Persona-only not-connected baits
are **excluded** (no folder by design) and are checked separately in TRUTH.md's Signal Set prose.
(Do **not** use `task.yaml` or `test_outputs.py` URLs for this check — absent at authoring time,
and at final audit the design record remains the source of truth.) Any callable API in
TRUTH.md but absent from the design/mock_data (or vice versa), or a persona-only bait that leaks a
folder/env var → Major.

---

## G. Leakage & hygiene

**TQ-25 — Answers live only in TRUTH.md.**
The oracle/answer values (the "correct" resolved values, refusal reasons) belong in TRUTH.md and
must **not** be pre-leaked into `PROMPT.md` in a way that hands the solver the answer (the prompt
carries only the worry, never the resolution rule/winner/decoy). Leakage into the prompt → Major.

**TQ-26 — No external cloud / file-share / contacts surface in the truth path.**
TRUTH.md must not require, name, or route a deliverable or data source through **Google Drive**,
**Google Contacts**, **Box**, or **Dropbox** — nor any equivalent external cloud-storage,
file-share, or external-contacts surface. These surfaces are banned regardless of whether the task
separately declares them unavailable. If any such surface appears in the truth path — a deliverable,
data source, send/upload/read target, or route — flag it as a **blocker**: severity **FAIL-HARD**
(auto-fail the bundle regardless of other results). (Documenting the availability *toggle* for these
surfaces inside TRUTH.md is separately barred by TQ-28.)

**TQ-27 — Grounding vs invention.**
No fact in TRUTH.md may be invented without a source. Any asserted value, quote, or record that
cannot be traced to `data/`, `mock_data/`, `persona/`, `prompt_design_notes.md`, or `PROMPT.md` → Major
(hallucinated truth).

**TQ-28 — No platform / runtime metadata in TRUTH.md.**
TRUTH.md is a golden-truth reference about the *task* (its scenario, values, solve path, grading).
It must **not** carry any **platform, harness, or agent-runtime metadata**, because that is
environment configuration, not task truth. Specifically, TRUTH.md must not state, assume, or depend
on any of:

- **harness / OS** (e.g. "harness = macOS", "runs on macOS/Linux/Windows");
- **agent or model runtime** (e.g. "agent = Claude", "runtime `claude-opus-4-8`", model/vendor
  names, context-window or tokenizer claims);
- **thinking / reasoning-mode flag** (e.g. "thinking off/on", chain-of-thought settings);
- **multimodal flag** or any statement gating which media types are readable (e.g.
  "multimodal = true", "XML/XLSX/TSV/DOCX/PDF/MP3 allowed");
- **connector-availability flags** (e.g. "google_drive = false", "Box/Dropbox banned" stated as a
  platform toggle);
- **delivery-channel / "nothing is sent" mode** stated as a platform setting.

If **any** such platform/runtime line is present in TRUTH.md, flag it as a **blocker**: severity
**FAIL-HARD** (auto-fail the bundle regardless of other results). Remove it; the task's own facts,
red-lines, and grounded sources must stand on their own. Note this is about *metadata placement*:
the actual **banned external surfaces** (Google Drive, Google Contacts, Box, Dropbox) are still
forbidden from the *truth path* under TQ-26 — TQ-28 additionally forbids *documenting the platform
toggle itself* inside TRUTH.md.

**TQ-29 — No hardcoded output-deliverable filename.**
TRUTH.md must refer to each agent-produced deliverable **by type** (chart / plot, slide deck, HTML
dashboard, worked spreadsheet, written document) and the outcome it must convey — **never** by a
hardcoded output filename or path (e.g. `reconciliation_brief.md`, `/workspace/output.csv`),
**unless** `PROMPT.md` literally names that file. The agent chooses the filename and format at
runtime, so a truth key that pins an invented deliverable name is wrong. Input carriers
(`mock_data/<api>/*.csv`, `data/*`) are **not** deliverables and must still be cited normally. A
deliverable filename TRUTH.md invented that the prompt never named → Major; refer-by-type instead.

**TQ-30 — VALUE_LOCK entries are typed and carrier-grounded.**
Every VALUE_LOCK entry must carry an explicit `type:` of exactly one of `graded-positive`, `stale`,
or `decoy`, and cite a real **input** carrier (a `data/`, `mock_data/<api>` record, or `persona/`
file — never a deliverable the agent has not written). An untyped entry, an entry with a type outside
that set, or an entry whose `source:` points at a deliverable rather than an input carrier → Major.

---

## H. Per-task invariants to compute (no fixed numbers)

Compute each from the task under review, record the observed value in your report, and confirm it
agrees everywhere listed. There are **no** hardcoded targets.

| Invariant | Derive from | Must agree with |
|---|---|---|
| In-world "now" + timezone | TRUTH.md header | `PROMPT.md`, `persona/USER.md` |
| Principal identity / DOB / threshold | TRUTH.md header | `persona/USER.md`, `AGENTS.md` |
| Graded-positive value count | `type:graded-positive` VALUE_LOCK entries | TRUTH.md fingerprint `graded_positive_values` (internal) |
| Stale/decoy value count | `type:stale` + `type:decoy` VALUE_LOCK entries | TRUTH.md fingerprint `stale_or_decoy_values` (internal) |
| Callable API set (connected + distractor) | `prompt_design_notes.md` / `api_selection.json` | `mock_data/*-api`, TRUTH.md Signal Set (1:1 bijection) |
| Persona-only not-connected baits | TRUTH.md Signal Set / `persona/TOOLS.md` | no folder, no env var |
| Conflicts (decoy vs authoritative) | TRUTH.md Fairness Ledger | authoritative = `graded-positive`, loser = `stale`/`decoy` |
| Red lines / poison pills | TRUTH.md | each marked by a `stale`/`decoy` key and/or §6 pill |
| Deliverables | TRUTH.md §7 | referred to by type, no invented filename (TQ-29) |
| Cited sources | TRUTH.md Value Lock citations | input carriers exist and contents match (never a deliverable) |
| Platform / runtime metadata | scan whole TRUTH.md | must be ABSENT: no harness/OS, agent+model runtime, thinking flag, multimodal flag, connector toggles, or delivery-mode lines (TQ-28) |
| Banned surfaces | TRUTH.md truth path | no Google Drive / Google Contacts / Box / Dropbox anywhere in the solve path (TQ-26) |

---

## Report format & verdict

Produce `QC_REPORT_TRUTH.md`:

1. **Summary** — task id, one-line health, counts observed (graded-positive values, stale/decoy
   values, APIs, deliverables by type).
2. **Findings** — table of every TQ check: `Check · Verdict · Evidence · Notes`.
3. **Grounding ledger** — for each Value-Lock anchor: `value · type · cited input carrier · exists? · matches?`.
4. **Cross-file alignment matrix** — TRUTH.md vs prompt / design notes / data / mock_data / persona.
   If `rubric.json` / `test_outputs.py` / `test_weights.json` are present (final assembled-bundle
   audit), add a **Backward reconciliation** section: per VALUE_LOCK key, its type, the grader
   covering it (test or criterion), and orphaned / double-graded / invented-literal findings.
5. **Verdict.**

> **Roll-up verdict rule:** any **FAIL-HARD** or ungrounded/contradicted load-bearing truth ⇒
> **FAIL**. This includes any occurrence of a **TQ-26** banned surface (Google Drive / Google
> Contacts / Box / Dropbox) in the truth path or any **TQ-28** platform/runtime metadata line in
> TRUTH.md — either one is a blocker that forces **FAIL** on its own. Otherwise any **red/Major** ⇒
> **NEEDS FIXES**. Only Minor/cleanup remaining ⇒ **PASS (with cleanup)**. Clean ⇒ **PASS**.
