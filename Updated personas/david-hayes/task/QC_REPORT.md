# QC Report: David Hayes Persona

Adversarial QC pass over the 7-file OpenClaw persona for David Hayes, run against PERSONA_QC_PROMPT v1.4 (binding) and 7FILE_GENERATION_PROMPT v2. Anchor date 2026-06-09. All defects found during generation and audit were fixed in the files on disk before this report was written.

## 1. Findings Catalog

| ID | Severity | Mode | File | Section | Quote | Defect | Fix Type | Fix |
|---|---|---|---|---|---|---|---|---|
| F-001 | CRITICAL | F6/E6 | TOOLS.md | Connected Services | `**Stripe is for cards; Alpaca** (alpaca-api)` | Malformed display name; two services collapsed into one bold label, breaking the bullet regex and the 101-slug format. | DIRECT_FIX | Renamed to `**Alpaca** (alpaca-api)` with a clean one-sentence description. |
| F-002 | MAJOR | F6 | TOOLS.md | Connected Services | 13 content H4 categories plus Not Connected (14 total) | Exceeds the 6 to 12 H4 category limit in QC F6. | DIRECT_FIX | Merged crypto exchanges into Shop Accounting & Payments and folded Fitness into Media, Downtime & Fitness. Now 11 categories plus Not Connected. |
| F-003 | MAJOR | F2/D | SOUL.md | Core Truths, Vibe, Continuity | "He is loyal to the family and hungry for his own life"; "just him, the coffee"; "so he never has to reintroduce his own world" | Third-person pronouns about the user (he/his/him) violate the SOUL second-person rule. | DIRECT_FIX | Rewrote the affected bullets to remove all he/his/him references while preserving meaning. |
| F-004 | MAJOR | A1/D6 | AGENTS.md, MEMORY.md, TOOLS.md | Tool Usage / Devices / Connected Accounts | Legacy "Crestline Consulting Workspace" branding | Brand inconsistent and implausible for a solo auto shop; the persona uses his own Gmail domain. | DIRECT_FIX | Dropped the "Crestline Consulting" name; recorded the integration as Google Workspace on his own domain (david.hayes@voissync.ai). See Open Questions. |
| F-005 | MAJOR | C4/E7 | MEMORY.md, HEARTBEAT.md | Key Relationships / Annual | No inner-circle DOBs in legacy source | Required inner-circle birthdays missing; could not populate HEARTBEAT Annual. | DIRECT_FIX (generated) | Generated plausible DOBs consistent with stated ages for Robert, Linda, Emily, Frank, Diane, Kevin, Omar; propagated parents, sibling, cousin, and best friend into HEARTBEAT Annual. Flagged in Open Questions. |
| F-006 | MAJOR | F8/B1 | MEMORY.md | (legacy) Upcoming Events, Recurring Reminders, Previous Conversations, Family Schedule | Legacy MEMORY held dated events, recurring reminders, schedules, and a conversation log | Forbidden sections in MEMORY per F8. | DIRECT_FIX | Moved dated events and recurring items to HEARTBEAT; extracted durable facts (Firdale 12% discount, U-14 proposal) into Work & Projects; dropped the conversation log. |
| F-007 | MAJOR | F4 | AGENTS.md | (legacy headings) | Legacy AGENTS had `## Identity`, `## Tool Usage`, `## Communication Style`, `## Context You Should Know` | Forbidden AGENTS headings; identity, tools, and tone belong elsewhere. | DIRECT_FIX | Rebuilt AGENTS with the 7 canonical H2; identity moved to IDENTITY, tools to TOOLS, tone to SOUL, facts to MEMORY. |
| F-008 | MAJOR | F2 | SOUL.md | (legacy) Communication Preferences | Legacy SOUL had a `## Communication Preferences` section | Forbidden in SOUL. | DIRECT_FIX | Removed; comms-channel content moved to AGENTS Communication Routing and USER Preferences. |
| F-009 | MAJOR | F1/F3 | IDENTITY.md | H1 | Legacy `# Agent Configuration` with `## Identity` H2 | Wrong H1 pattern; forbidden H2. | DIRECT_FIX | H1 set to `# Identity: David Hayes`; opening paragraph then Nature and Principles H3 only. |
| F-010 | MAJOR | C10/F4 | AGENTS.md | Data Sharing Policy | Absent in legacy | Mandatory seventh H2 with per-contact enumeration missing. | DIRECT_FIX | Added `## Data Sharing Policy` with per-contact and per-tier rules ending in a default-restrictive fallback. |
| F-011 | MINOR | C8 | AGENTS.md | Confirmation Rules | Legacy "A financial transaction exceeds $200" | Needed canonical bullet form, no tautological self-conversion. | DIRECT_FIX | Rewrote as `**Spending threshold**: $200. Any purchase, booking, subscription, or financial commitment at or above this requires explicit approval.` |
| F-012 | MINOR | F6 | TOOLS.md | (legacy) Tool Usage | Legacy listed web search, browser, sub-agents, cron, memory_search as capabilities | Web access forbidden in connected list; memory_search and General Agent Capabilities forbidden under v1.4. | DIRECT_FIX | Omitted General Agent Capabilities entirely; web/browse limitation stated in Not Connected. |
| F-013 | MINOR | D1 | TOOLS.md | Shop Operations & Inventory | Amazon Seller usage | Amazon Seller is a seller-side API; David is a buyer. | DIRECT_FIX | Described as buyer-side sourcing only, explicitly noting he has no storefront. |

## 2. Coherence Score

```
Score: 9.6 / 10
Rubric:
  - Cross-file alignment:            2.0 / 2.0   (Mode A)
  - Overlapping / SoT compliance:    1.0 / 1.0   (Mode B)
  - Required-field completeness:     0.9 / 1.0   (Mode C: inner-circle DOBs generated, not source-verified)
  - Factual & domain correctness:    2.0 / 2.0   (Mode D)
  - Mathematical correctness:        1.0 / 1.0   (Mode E)
  - Heading-structure compliance:    2.0 / 2.0   (Mode F, headings)
  - Format-structure compliance:     0.7 / 1.0   (Mode F, caps & format: minor headroom note below)
                            Total:   9.6 / 10.0
```

Notes: The 0.1 deduction on completeness reflects that seven inner-circle DOBs are plausibly generated rather than source-verified (see Open Questions). The 0.3 deduction on format reflects that several APIs carry honest "Not used / left unconnected" descriptions per D7; these are accurate but thin by necessity for an auto-shop persona.

## 3. Remediation Log

| Finding ID | File | Change Type | Before | After | Justification |
|---|---|---|---|---|---|
| F-001 | TOOLS.md | DIRECT_FIX | `**Stripe is for cards; Alpaca** (alpaca-api): ...` | `**Alpaca** (alpaca-api): Not used. No brokerage trading; flagged low relevance and left unconnected.` | Restores valid bullet format and a single display name. |
| F-002 | TOOLS.md | DIRECT_FIX | 13 categories + Not Connected | 11 categories + Not Connected | Brings H4 count within the 6 to 12 limit. |
| F-003 | SOUL.md | DIRECT_FIX | Bullets with he/his/him about David | Reworded to second-person agent voice with named user | Enforces SOUL second-person rule. |
| F-004 | AGENTS/MEMORY/TOOLS | DIRECT_FIX | "Crestline Consulting Workspace" | "Google Workspace on his own domain" | Removes implausible brand; aligns with the persona. |
| F-005 | MEMORY/HEARTBEAT | DIRECT_FIX (generated) | No DOBs | Generated DOBs in Key Relationships; birthdays in Annual | Satisfies required-field and recurrence checks. |
| F-006 | MEMORY.md | DIRECT_FIX | Upcoming Events, Recurring Reminders, Family Schedule, Previous Conversations sections | Content relocated to HEARTBEAT or extracted; sections removed | Enforces MEMORY 11-section limit and single-source-of-truth. |
| F-007 | AGENTS.md | DIRECT_FIX | Legacy non-canonical headings | 7 canonical H2 sections | Enforces AGENTS structure. |
| F-008 | SOUL.md | DIRECT_FIX | `## Communication Preferences` | Removed; routed to AGENTS and USER | Forbidden SOUL section. |
| F-009 | IDENTITY.md | DIRECT_FIX | `# Agent Configuration` / `## Identity` | `# Identity: David Hayes` + paragraph + Nature/Principles | Enforces IDENTITY structure. |
| F-010 | AGENTS.md | DIRECT_FIX | (no policy) | `## Data Sharing Policy` per-contact section | Mandatory seventh H2. |
| F-011 | AGENTS.md | DIRECT_FIX | "A financial transaction exceeds $200" | Canonical spending-threshold bullet | Required form, no self-conversion. |
| F-012 | TOOLS.md | DIRECT_FIX | Web/browser/sub-agent/memory_search capabilities | General Agent Capabilities omitted; limits in Not Connected | v1.4 TOOLS rules. |
| F-013 | TOOLS.md | DIRECT_FIX | Amazon Seller (ambiguous) | Buyer-side sourcing only | Correct API surface for a buyer. |

## 4. Open Questions for Human Input

1. Resolves F-005. Inner-circle dates of birth were absent from source and were generated as plausible dates consistent with the stated ages. Please confirm or correct:
   - Robert Hayes (father), age 64: generated 1962-03-22. Answer: ____-__-__
   - Linda Hayes (mother), age 59: generated 1966-07-09. Answer: ____-__-__
   - Emily Hayes (sister), age 22: generated 2003-11-03. Answer: ____-__-__
   - Uncle Frank Hayes, age 60: generated 1966-01-15. Answer: ____-__-__
   - Aunt Diane Hayes, age 56: generated 1970-02-11. Answer: ____-__-__
   - Kevin Hayes (cousin), age 28: generated 1998-02-17. Answer: ____-__-__
   - Omar Bazzi (best friend), age 31: generated 1994-10-28. Answer: ____-__-__
   Note: Linda's generated birthday (July 9) falls outside the October-to-March fiscal window. That window is a constraint only on the persona's own DOB (David, December 14, which complies); relationship birthdays are unconstrained, so this is acceptable but flagged for awareness.
2. Resolves F-004. Legacy material named a "Crestline Consulting Workspace" for david.hayes@voissync.ai, which is inconsistent for a solo auto-shop owner with no separate work email. Resolved by treating the Google Workspace as connected to David's own domain and dropping the Crestline name. Please confirm the workspace is his own domain and not a third-party reseller/MSP brand. Answer: confirm / correct: __________
3. Minor. Emily's age (22) and pre-law junior status with a 2003 birth year are internally consistent. Confirm Emily's institution name is "Mapleton University" (used in source) versus any official name. Answer: __________

## 5. Corrected Files on Disk

All corrections above were applied directly to the seven files in `c:\Users\lenovo\Desktop\9_6_Mansa\david-hayes\`: `SOUL.md`, `IDENTITY.md`, `AGENTS.md`, `USER.md`, `TOOLS.md`, `HEARTBEAT.md`, `MEMORY.md`. The files are defect-free as of this report. Final verification: 101 unique `-api` slugs each appearing once; zero `via mock`/`shopify`/`fintrack`/`todoist`/port numbers; zero em/en/horizontal-bar dashes across all seven; USER.md 30 lines; MEMORY.md 10,740 characters; every file under 20,000 characters; all heading sets exact.

## 6. Cross-Persona Pattern Flags

- **SYSTEMIC (likely cohort-wide)**: Legacy 4-file personas embed identity in AGENTS, comms preferences in SOUL, and dated events plus recurring reminders in MEMORY. These three migrations (to IDENTITY, to AGENTS/USER, to HEARTBEAT) recur across personas and warrant a template-level migration pass.
- **SYSTEMIC**: Reseller/MSP workspace branding (here "Crestline Consulting") attached to a solo-operator persona's own Gmail domain is a recurring implausibility; recommend a template check that workspace brand matches the persona's business scale.
- **SYSTEMIC**: Missing inner-circle DOBs in legacy source is common; recommend the generation step always surface generated relationship DOBs as human-input questions rather than silently committing them.

## 7. Post-QC User Amendment (2026-06-09)

Per explicit user direction ("no need of inner circle dobs"), all GENERATED inner-circle dates of birth were removed from `MEMORY.md > Key Relationships` (Robert, Linda, Emily, Frank, Diane, Kevin, Omar), and the generated relationship birthday entries were removed from `HEARTBEAT.md > Recurring Events > Annual`. Retained: David's own DOB in `USER.md > Basics` (1995-12-14, source-derived from "turns 31 on Dec 14, 2026" and required by the DOB constraint), his own birthday in Annual, and the Thanksgiving entry. This intentionally waives QC checks **C4** (inner-circle birthdays) and the related **E7** propagation for this persona; it is a deliberate user decision, not a defect. Open Question 1 (relationship DOBs) is therefore moot; items 2 (workspace branding) and 3 (institution name) still stand.

## Final Verdict

**VERDICT: PASS** (coherence 9.6 / 10).

The David Hayes persona is approved for deployment. All structural gates pass: 7 canonical files with exact heading sets (AGENTS.md 7 H2 including Data Sharing Policy; TOOLS.md Connected Services only, no General Agent Capabilities; SOUL.md with no stray Communication Preferences section), TOOLS.md carries exactly 101 unique `-api` slugs each appearing once, zero `via mock`/`shopify`/`fintrack`/`todoist`/port tokens, zero em/en/horizontal-bar dashes across all seven files, USER.md within the 40-line cap (30 lines), MEMORY.md under 15,000 characters (10,740), and every file under 20,000. Cross-file alignment, single-source-of-truth, factual/domain, and mathematical checks pass; the legacy "Crestline Consulting Workspace" inconsistency was resolved to his own Google Workspace domain. No CRITICAL or MAJOR defects remain open; all findings were remediated in-file.

Residual items are non-blocking: David's own DOB is source-derived (Dec 14, 1995), inner-circle birthdays were intentionally removed per user direction (waiving C4/E7, see Section 7), and two cosmetic confirmations (workspace ownership, institution name) remain open. None affect deployment readiness.

**Disposition: SHIP.**
