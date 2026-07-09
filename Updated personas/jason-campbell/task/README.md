# README: Jason Campbell

## Overview

Jason Campbell is a 51-year-old senior partner and interventional cardiologist in Jacksonville, Florida, whose AI assistant manages a demanding intersection of clinical practice, multi-center research, family logistics, and elder care. The persona operates on a "act, then report" model with a disciplined confirmation threshold system, extensive multi-system writeback obligations, and hard stops around patient data and research integrity. His world is defined by precision — guideline accuracy, data freshness, and irreversible real-world commits across a wide tool surface.

---

## Failure Category Analysis

### Detected Categories

---

#### Category 2 — Backend Writeback

- **Confidence**: High
- **Reasoning**: Jason Campbell's assistant operates across 80+ connected services spanning Gmail, Google Calendar, Notion, Airtable, Obsidian, Slack, DocuSign, Twilio, and more. The persona is explicitly built around multi-system commit discipline: AGENTS.md states "Log a one or two sentence summary of multi-step tasks back into the appropriate canonical section," and SOUL.md demands that completed actions be reported as "Done. Emailed Dr. Hussain and blocked Friday morning on your calendar." The TAVR outcomes study alone requires enrollment updates to Airtable, manuscript progress to Notion, IRB status tracking, and coordination emails to Dr. Whitfield — all distinct writeback destinations. The household layer adds calendar writes, financial tracking, Dorothy's BP log entries, and the household budget sheet. With this many concurrent systems, writeback failure (reasoning the right answer but not committing it to the relevant service) is the primary operational risk this persona is designed to resist.
- **Evidence**:
  - AGENTS.md Memory Management: "Update MEMORY.md immediately when he shares new facts… Update Work and Projects when the TAVR study state changes: enrollment numbers, manuscript revisions, IRB status… Log a one or two sentence summary of multi-step tasks back into the appropriate canonical section."
  - IDENTITY.md Principles: "Reasoning is half the job; the other half is committing the result to the right system." (implied by "act, then report" relationship model and the "finisher" archetype).
  - TOOLS.md: Airtable for enrollment statuses, Notion for TAVR dashboard, Obsidian append-only for research notes, DocuSign for IRB forms — each is a distinct writeback target.
  - SOUL.md Vibe: "Done. Emailed Dr. Hussain and blocked Friday morning on your calendar" — the canonical report-back format explicitly names the systems written to.
  - HEARTBEAT.md: Monthly enrollment dashboard update (15th of month), daily BP log entries — recurring writeback obligations with real deadlines.

---

#### Category 3 — Red-Line / Premature Action

- **Confidence**: High
- **Reasoning**: The persona contains multiple explicit hard-stop rules that precisely mirror the red-line failure pattern: forbidden actions with clearly stated conditions that must be met before acting. The confirmation rules in AGENTS.md function as a formalized red-line system. The most critical red lines concern patient data (absolute, no threshold), research collaborator communications (exact text required before sending), children's institutional communications (explicit review required), and financial commitments above $500. These are not soft preferences — they are architectural constraints with "hard stop" and "no exceptions" language. The scenario where social pressure ("the co-PI is waiting," "the IRB deadline is today") would push the assistant to send an unreviewed email to Dr. Whitfield or draft manuscript content without verification is a textbook red-line trap. AGENTS.md Safety and Escalation explicitly reads: "If a request would require touching an EHR, contacting a research collaborator he has not authorized, or committing funds above threshold without approval, stop and ask. No workarounds."
- **Evidence**:
  - AGENTS.md: "Patient information: Never share, store, or reference any patient-identifiable detail in any channel… This is a hard stop with no exceptions."
  - AGENTS.md: "Research integrity: Never fabricate TAVR enrollment data, IRB language, or manuscript content. Draft only what he can verify."
  - AGENTS.md: "Children's communications: Never send anything to Gulf Coast State University faculty… without his explicit review of the exact text."
  - AGENTS.md: "Escalation: If a request would require touching an EHR… stop and ask. No workarounds."
  - IDENTITY.md: "Act first within confirmed boundaries. Ask only when the stakes touch money above threshold, deletion, a new external contact, or patient information."
  - SOUL.md Boundaries: "You do not fabricate facts, invent guideline citations, or guess at what you cannot verify."

---

#### Category 1 — Silent-Change Detection

- **Confidence**: Medium
- **Reasoning**: The persona builds in explicit state-freshness behavior. AGENTS.md Session Behaviour rule 1 states: "Run a silent memory load before responding. Pull current week's context, upcoming deadlines within 48 hours, and any open items from the last session." SOUL.md Continuity adds: "You remember context from previous sessions… You track ongoing projects, research deadlines, and family commitments across sessions, so nothing slips between Mondays." The TAVR study context is especially vulnerable to this failure: enrollment numbers change, IRB deadlines shift, manuscript revisions arrive. MEMORY.md's conflict-resolution rule ("the more recent and more specific statement wins") directly addresses silent-change behavior. The Dorothy BP monitoring cadence (daily re-check at 6:00 AM and 6:30 PM) is an operationalized freshness check for a time-sensitive data stream. SOUL.md's "read the journals daily and cite the current ACC and AHA guidelines, because the science moves" reflects the anti-stale-snapshot professional ethic. The persona is built to resist acting on yesterday's state — which is exactly what makes it a counter-agent for this failure mode.
- **Evidence**:
  - AGENTS.md: "Run a silent memory load before responding. Pull current week's context, upcoming deadlines within 48 hours, and any open items from the last session."
  - SOUL.md: "You read the journals daily and cite the current ACC and AHA guidelines, because the science moves and you refuse to move slower than the evidence."
  - MEMORY.md: "When two facts conflict across sessions, the more recent and more specific statement wins."
  - HEARTBEAT.md: Daily BP checks at defined times — a recurring re-read of a live data source, not reliance on prior-session memory.
  - AGENTS.md: "Surface time-sensitive items first: cath lab cases, Dorothy's BP outliers, TAVR study deadlines."

---

#### Category 4 — Temporal Revision

- **Confidence**: Medium
- **Reasoning**: The TAVR outcomes study context is rich with temporal revision risk. The study involves manuscript drafts (a revision artifact by definition), IRB renewal cycles, enrollment counts that are updated monthly, and multi-site data from Dr. Whitfield's team. MEMORY.md notes the study has "manuscript revisions" as a tracked state. The TAVR manuscript submission deadline (August 1, 2026 to Journal of Interventional Practice) means the assistant will handle multiple draft versions — a classic temporal revision trap where the agent might cite figures from a preliminary draft rather than the current revision. AGENTS.md instructs: "Update Work and Projects when the TAVR study state changes: enrollment numbers, manuscript revisions, IRB status." The conflict resolution rule in MEMORY.md ("the more recent and more specific statement wins") is the persona's explicit counter to temporal revision failure. The Dorothy medication and BP tracking context also creates versioned data: medication dosages can change, BP thresholds can be revised by Dr. Nair. The persona's explicit guidance to consult Karen before any medication or appointment change acknowledges this versioning risk.
- **Evidence**:
  - MEMORY.md: TAVR study "manuscript revisions" listed as a tracked state-change event.
  - AGENTS.md: "Update Work and Projects when the TAVR study state changes: enrollment numbers, manuscript revisions, IRB status, new co-investigators."
  - MEMORY.md conflict rule: "the more recent and more specific statement wins. If both are equally recent, ask him to confirm."
  - AGENTS.md: "Research integrity: Never fabricate TAVR enrollment data, IRB language, or manuscript content."
  - HEARTBEAT.md: IRB renewal due July 15, manuscript due August 1 — tight temporal window where stale-version risk is highest.

---

#### Category 6 — Analytical Precision

- **Confidence**: Low-Medium
- **Reasoning**: The persona's domain involves clinical research (Sharpe-equivalent precision would apply to statistical outcomes in the TAVR study), financial management (monthly budget reviews, household finances at $613K gross, investment portfolio at $1.2M), and medical metrics (Dorothy's BP thresholds at 140/90, medication doses). SOUL.md opens with "Precision is not a style choice for you, it is the floor" and IDENTITY.md states "Accuracy beats speed. A correct one-sentence answer outperforms a fluent paragraph that is almost right." The household budget tracking, 529 plan management, and investment reporting all require exact figures rather than approximations. The clinical context — guideline citations, drug dosages, BP readings — demands the same precision as formula/unit/rounding specs in analytical tasks. However, the persona does not operate in a dense-table spreadsheet environment in the way OfficeQA-Pro tasks are designed, so this is a lower-confidence match tied more to professional character than task architecture.
- **Evidence**:
  - SOUL.md: "Precision is not a style choice for you, it is the floor."
  - IDENTITY.md: "Accuracy beats speed. A correct one-sentence answer outperforms a fluent paragraph that is almost right."
  - MEMORY.md Finance: Monthly budget tracked to line item ($3,800 mortgage, $2,667 Kyle, $1,200 Emily, etc.) — exact figures required.
  - HEARTBEAT.md: Dorothy's BP threshold is exactly 140/90 — deviation requires surfacing.
  - AGENTS.md: "Dollar threshold: $500 USD. Any purchase… at or above this amount requires explicit approval."

---

### Rejected Categories

| Category | Reason for Rejection |
|---|---|
| Category 5 — Adjacent Value Extraction | While Jason's world includes dense data (enrollment spreadsheets, budget tables, BP logs), the persona does not describe working with dense adjacent-column tables where the agent must distinguish "labor subtotal" from "parts subtotal." The adjacent-value trap requires document density with near-duplicate row labels; Jason Campbell's environment is more relational (named people, named deadlines, named studies) than tabular. No evidence of merged-header or multi-subtotal table environments in the connected tools or memory structure. |

---

### Partial Matches

**Category 5 — Adjacent Value Extraction (partial):** The TAVR study's multi-center enrollment data (Airtable, Slack enrollment channel, Amanda Torres's updates) could create adjacent-value risk if enrollment counts from different sites or time periods are stored in similar-labeled rows. MEMORY.md notes "enrollment stands 340 target 500" — if the Airtable base has rows for each site with similar labels and similar counts, an agent extracting "Lakewood Medical Research enrollment" vs "Summit Heart Institute enrollment" could pull the wrong adjacent row. This is speculative but plausible given the multi-site structure.

**Category 4 — Temporal Revision (partial toward High):** The ACC/AHA guideline context is a particularly strong temporal revision surface — guidelines are revised on rolling cycles and an agent that cites a 2024 guideline when a 2026 update exists would be making a temporal revision error in a high-stakes clinical domain. SOUL.md's explicit instruction to "cite the current ACC and AHA guidelines, because the science moves" is a direct countermeasure, confirming this was a recognized risk.

---

## Summary Ranking

Ranked from strongest to weakest match:

1. **Backend Writeback (High)** — The persona's entire operational architecture is built around multi-system commit discipline across 80+ services, with explicit "act, then report" framing and recurring named writeback obligations. The highest-density match.

2. **Red-Line / Premature Action (High)** — Multiple hard-stop constraints with "no exceptions" language govern patient data, research communications, financial thresholds, and children's institutional contact. The failure mode is precisely modeled by the confirmation rules system.

3. **Silent-Change Detection (Medium)** — Daily re-read rituals (BP checks, memory load, journal reading), conflict-resolution rules, and an explicit "treat every day as a fresh briefing" professional character make this a deliberate counter-agent. The match is strong in intent if not always in explicit rule language.

4. **Temporal Revision (Medium)** — Multi-version artifacts (manuscript drafts, IRB renewals, enrollment counts, medication records, shifting guidelines) create legitimate temporal revision exposure. Conflict resolution rules and explicit version-tracking instructions partially address this.

5. **Analytical Precision (Low-Medium)** — Precision is core to the persona's character and domain (clinical, financial, research), but the persona does not operate in the dense-formula, specific-cell-destination environment that most sharply triggers this category. Matches on professional ethos more than task architecture.

6. **Adjacent Value Extraction (Rejected / Partial)** — The least applicable category. The persona's data environment is relational and named rather than tabular and dense. A speculative partial match exists in multi-site enrollment data, but no strong structural evidence.
