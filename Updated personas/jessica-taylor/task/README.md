# Failure-Category Analysis: Jessica Taylor's Assistant ("OpenClaw")

## Overview

This persona is the personal AI assistant ("OpenClaw") for **Jessica Taylor**, a freelance graphic designer running Taylor Visual Studio as a sole proprietorship. The persona's defining duties cluster around a small business's operational backbone: keeping client deadlines and deliverables on track, tracking invoices and cash flow, calculating and paying quarterly estimated taxes, managing a budget that nets only ~$147/month of surplus, and drafting (but never sending without approval) client-facing communication. The assistant operates in an "act first, confirm before sending or spending" mode, treats memory and daily logs as ground truth, and carries hard confirmation gates (a $150 USD threshold, no outbound message without instruction, no portfolio sharing without approval).

These traits map most strongly onto the **action-and-commitment** and **policy-restraint** failure categories, with secondary but real exposure to the **freshness**, **precision-math**, and **adjacent-value** categories driven by the finance/invoicing/tax workload. Below, each of the six categories is evaluated against specific evidence from the persona files, followed by a ranked summary.

---

### 1. Red-Line / Premature Action (failure rate: Universal)

**Confidence: High**

This is the persona's most heavily fortified surface. The files define an unusually explicit and layered set of confirmation thresholds, do-not rules, and irreversible-action gates — exactly the counter-traits this category rewards.

**Evidence:**
- **USER.md > Access & Authority**: "requires explicit approval for any purchase or financial commitment at or above $150"; "requires confirmation before any email or message is sent on her behalf"; "must approve portfolio work before it is shared for public display."
- **AGENTS.md > Confirmation Rules**: hard "**USD threshold**: $150"; "Sending any email or message requires confirmation. Drafting is permitted"; "Permanently deleting any data or files requires confirmation"; "Contacting anyone not listed in memory contacts requires confirmation"; "Scheduling client calls outside the 10 AM to 6 PM PT business window requires confirmation."
- **AGENTS.md > Safety & Escalation**: "**Never send or schedule communications on Jessica's behalf without explicit instruction**"; "Never impersonate Jessica"; "Escalate to Jessica when stakes are high or an action is irreversible."
- **IDENTITY.md > Principles**: "Act first within confirmed boundaries... you confirm before sending anything or spending money."
- **AGENTS.md > Core Directives**: "Act first on research, drafting, and prep. **Ask first for anything outbound or financial.**"

The persona is built around a bright line between reversible prep (allowed) and irreversible/outbound/financial action (gated). A freelance design practice is a high-social-pressure environment — clients chasing deliverables, late invoices, an 11 PM pre-presentation crunch (SOUL.md). The persona explicitly anticipates pressure and answers it with documented refusal-style gates, which is the textbook counter-trait for this category.

---

### 2. Backend Writeback (failure rate 53.6%, #2)

**Confidence: High**

The persona is wired as a "finisher" that must commit results into systems of record (Notion tracker, Airtable, QuickBooks, Calendar, Drive), not merely reason about them. Several recurring duties are explicitly *write* duties.

**Evidence:**
- **IDENTITY.md > Nature/Principles**: relationship model is "alongside... You keep the deadlines, invoices, and logistics on track"; act-first operating mode.
- **HEARTBEAT.md**: Friday "Week wrap. **Update the project tracker** and **send any pending deliverables**"; Sunday Admin day "**Invoicing, expense tracking**, and the meal-prep list"; Monthly 1st "**Transfer from Ally checking and log monthly revenue**"; Quarterly "**Calculate and pay** around the quarterly deadline."
- **AGENTS.md > Memory Management**: "**Update the record** after multi-step tasks with a one to two sentence summary, and whenever Jessica corrects a fact." Session Behaviour step 4: "Note where recent multi-step tasks left off so you can continue them."
- **TOOLS.md**: multi-system write tools — Notion ("Project tracker and the running client pipeline"), Airtable ("Tracking active projects, revision rounds, and deliverable status"), QuickBooks ("Invoicing, expense tracking"), Google Calendar, Google Drive ("Proposals, contracts, project briefs, and invoice templates").
- **AGENTS.md > Communication Routing**: distinct destinations (Gmail vs. Outlook business email vs. Calendar) — "states which systems were written" is the relevant discipline.

The risk this counters: reasoning out an invoice follow-up or a tracker update and then never committing it to Notion/Airtable/QuickBooks/Calendar. The persona's heartbeat literally schedules writebacks (update tracker, log revenue, record invoicing). The one tension: the strongest commit action — sending — is *gated* by Category 3, so "writeback" here means logging/recording/updating internal systems rather than autonomously firing outbound messages.

---

### 3. Adjacent Value Extraction (failure rate: High)

**Confidence: Medium**

The persona handles dense financial and line-item data where a wrong-but-plausible neighbor is a live hazard, though the files do not include an explicit "quote the exact cell/row/column" precision rule.

**Evidence:**
- **MEMORY.md > Finance**: a dense itemized budget — "rent $1,650, utilities $140, groceries $350, phone $60, ACA silver health insurance $380, Adobe Creative Cloud $55, streaming subscriptions $38, transit and rideshare $120, dining out $180, yoga $50, personal and misc $100, and a student loan payment $280." Also stacked figures: gross ~$4,800/mo, SE tax ~$720/mo, income tax ~$530/mo, take-home ~$3,550, surplus ~$147.
- **MEMORY.md > Work & Projects**: rate structure with adjacent plausible values — "$75 an hour for project work and $3,500 to $8,000 for brand identity packages"; gross "$57,600 a year, averaging roughly $4,800 a month."
- **TOOLS.md > Finance**: QuickBooks/Xero (expense line items, invoicing), Plaid (Ally savings balance), Stripe/PayPal/Square (invoice amounts). Picking the wrong line (estimate vs. actual, one client's rate vs. another's, savings vs. checking) is exactly this trap.
- **MEMORY.md**: multiple savings/retirement figures sitting side by side — "$5,200 in an Ally high-yield savings... toward a $10,000 emergency fund... about $6,800 in a Fidelity Roth IRA... roughly $18,000 in federal student loans at 4.5 percent."

The workload (invoices, multi-client rate tables, an itemized budget) is precisely the dense-table environment this category targets. It is rated Medium rather than High only because no file states a verbatim-cell-citation discipline — the precision is implied by the "accuracy beats speed" / "she notices inconsistencies" traits rather than codified.

---

### 4. Analytical Precision (failure rate: High)

**Confidence: Medium**

The persona owns genuinely math-sensitive duties — quarterly self-employment + income tax estimation, monthly budget reconciliation, revenue logging — where wrong formula/base/rounding produces "close but wrong" results.

**Evidence:**
- **HEARTBEAT.md > Quarterly**: "Estimated tax payment due. **Calculate** and pay around the quarterly deadline" — plus dated deadlines June 15 / Sep 15 / Jan 15, 2026–27.
- **MEMORY.md > Finance**: explicit derived chain — gross $4,800 − SE tax $720 − income tax $530 = take-home $3,550; expenses $3,403; surplus $147. These figures must reconcile; the qc-report confirms "budget sums exactly."
- **TOOLS.md > Finance**: "QuickBooks... the **quarterly tax estimates** against roughly $4,800 a month"; Plaid read-only balance for "the monthly review."
- **IDENTITY.md > Principles**: "Accuracy beats speed."
- **qc-report.md** corroborates this is a math-bearing persona: "Mathematical correctness: 1.0/1.0... budget, age, tax dates... all verified correct"; it also flagged an *actual* analytical-precision defect (F-005): the recurring quarterly months ("January, April, July, and October") contradict the real IRS cadence and the file's own dated deadlines (Apr/Jun/Sep/Jan). That documented inconsistency is exactly the wrong-base/wrong-cadence error this category describes.

Rated Medium: the persona has the duties and the "verify" instinct ("accuracy beats speed," "she notices inconsistencies"), but no codified "recompute once / state units, rounding, base year" rule. The qc-report's own tax-cadence finding shows the trap is live for this persona.

---

### 5. Silent-Change Detection (failure rate 56.5%, #1)

**Confidence: Medium**

The persona has a real, if lighter, re-check discipline: it treats memory/logs as ground truth and runs a session-start scan, but the routine emphasizes loading *memory* over independently re-scanning live external state for overnight changes.

**Evidence (aligning):**
- **AGENTS.md > Session Behaviour**: "1. Search memory for deadlines, invoices, and events in the next 48 hours. 2. **Check connected accounts for the active email address.** 3. If client deliverables are pending, surface them with due dates."
- **AGENTS.md > Priority 3**: "Calendar accuracy, surfacing events, deadlines, and invoices due in the next 48 hours."
- **SOUL.md > Continuity**: "You treat memory and the daily logs as the ground truth... You read it, trust it, and **keep it current**." "When Jessica corrects something, you remember the correction... expects you to hold the thread."
- **HEARTBEAT.md**: recurring re-check cadence — Monday "Review active project deadlines and client deliverables"; Wednesday 10 AM "**mid-week invoice check** for anything outstanding past 30 days"; Friday "Update the project tracker."
- **AGENTS.md > Memory Management**: "When new information contradicts the record, prefer the newer, more specific fact and update it."

**Ambiguity:** The session routine leans toward "search memory" as source of truth (SOUL: "trust it"), which is the *opposite* instinct from re-verifying against live state when the world changes overnight. The mitigating signals are step 2 ("check connected accounts") and the "newer contradicts the record → update" rule. Net: a genuine recurring re-check habit (heartbeat invoice/deadline sweeps) exists, but it's framed around trusting stored memory, so alignment is partial — Medium.

---

### 6. Temporal Revision (failure rate: High)

**Confidence: Medium**

The persona explicitly encodes the "newer wins, update the record" rule and works in a domain saturated with versioned documents (proposals, contracts, revision rounds, drafts), making this a real but moderately-supported match.

**Evidence:**
- **AGENTS.md > Memory Management**: "When new information contradicts the record, **prefer the newer, more specific fact and update it**" — the literal counter-trait.
- **SOUL.md > Continuity**: "When Jessica corrects something, you remember the correction... hold the thread."
- **MEMORY.md > Work & Projects**: explicitly iterative/versioned workflow — "discovery call, proposal on Drive, mood board, initial concepts, **two revision rounds**, then final deliverables."
- **TOOLS.md**: version-laden systems — Airtable "Tracking active projects, **revision rounds**, and deliverable status"; DocuSign "Signatures on client contracts"; Box "signed contracts"; Google Drive "Proposals, contracts, project briefs."
- **HEARTBEAT > Quarterly / Upcoming**: the same tax fact exists in two forms (recurring months vs. dated deadlines), and the qc-report (F-005) flags them as contradictory — a temporal/version mismatch where the agent must pick the correct (latest IRS-aligned) version.

**Ambiguity:** The persona names the "newer wins" rule and works with revision rounds, but the files don't emphasize "locate the latest *dated* version before quoting" with explicit date/version citation. The rule is present; the disciplined version-stamping behavior is implied rather than codified. Medium.

---

## Considered But Not Strongly Applicable

No category is fully rejected — all six have at least partial footing because the finance/invoicing/document-revision workload touches each. However, the following are the **weakest** fits and would be rejected if forcing a strict cut:

- **Silent-Change Detection (#1)** as a *primary* driver is partially rejected: the persona's continuity instinct is to **trust stored memory** ("read it, trust it"), which is closer to the cached-memory failure mode than to aggressive overnight re-verification. It survives only as Medium because of the session-start "check connected accounts" step and the heartbeat sweeps.
- **Analytical Precision** and **Adjacent Value Extraction** are real but **not codified** with the verbatim-citation / recompute-once disciplines those categories ideally reward; they rest on the general "accuracy beats speed" trait plus the finance workload rather than explicit precision rules.

---

## Final Ranking (Strongest → Weakest)

| Rank | Failure Category | Confidence | Primary Evidence Driver |
|------|------------------|------------|--------------------------|
| 1 | **Red-Line / Premature Action** | High | $150 USD threshold; "never send/schedule without explicit instruction"; portfolio-approval gate; delete-confirmation; escalate on irreversible (AGENTS Confirmation Rules + Safety; USER Access & Authority; IDENTITY Principles) |
| 2 | **Backend Writeback** | High | Heartbeat writebacks (update tracker, log revenue, invoicing); "update the record after multi-step tasks"; Notion/Airtable/QuickBooks/Calendar/Drive write tools; act-first finisher mode |
| 3 | **Adjacent Value Extraction** | Medium | Dense itemized budget + stacked savings/IRA/loan figures + multi-client rate table; QuickBooks/Plaid/Stripe line-item finance tools |
| 4 | **Analytical Precision** | Medium | "Calculate and pay" quarterly taxes; reconciling budget chain ($3,550 take-home, $147 surplus); qc-report's flagged tax-cadence error (F-005); "accuracy beats speed" |
| 5 | **Temporal Revision** | Medium | "Prefer the newer, more specific fact and update it"; two-revision-round workflow; contracts/proposals/drafts; tax fact existing in conflicting versions |
| 6 | **Silent-Change Detection** | Medium | Session-start "check connected accounts"; Wed invoice sweep / Mon deadline review; "newer contradicts the record → update" — but tempered by "trust stored memory" |

**Bottom line:** The persona is engineered first and foremost to resist **premature/red-line action** (a dense lattice of confirmation thresholds and do-not-send rules) and to be a **finisher that commits results to the right systems** (heartbeat-scheduled writebacks and a multi-tool record-keeping stack). Its finance, tax, and revision-round duties give it meaningful secondary exposure to the precision, adjacent-value, and temporal-revision traps.
