# QC Report: Jake Thornton

> **Audit standard:** v1.4 PERSONA_QC_PROMPT (five retained check families: alignment, overlapping, structure, mathematical, factual) + common-errors.md catalog.
> **Anchor date:** 2026-06-27 (Atlanta, GA). Derived from USER.md > Basics (age 32, DOB 1993-11-18) and the IDENTITY.md tenure phrase ("your assistant since February 2026").
> **Persona type:** Male, he/him. Trans man. Certified Nurse-Midwife at Magnolia Women's Health and founder of Jake's Table (home cooking instruction). East Lake, Atlanta, GA.
> **Auditor stance:** Adversarial skepticism. Persona assumed broken until each field proved itself against a journalist, a security researcher, and a domain expert (clinician) probing on first contact.
> **Scope:** 7 inner files only. README.md and task/ artifacts out of scope.
> **Override constraints applied this pass (per operator instruction):** (1) no annual event in HEARTBEAT may fall April through September; (2) Upcoming Events & Deadlines begin October onward with no events landing in the April-September deadzone; (3) all 101 canonical APIs must carry an active, persona-aligned use, with no "read-only / standby / dormant" filler descriptions; (4) no direct `.md` filename references inside any inner file.

---

## Verdict

**STATUS: PASS - DEPLOYMENT-READY**

**Coherence Score: 9.7 / 10.0**


## Section 1 — Findings Catalog

Every check in MODES A through F was run against all 7 inner files, including checks that passed. The table below lists each defect detected this pass and its remediation. All findings were closed in Phase 2.

| ID | Severity | Mode | File | Section | Quote | Defect | Fix Type | Fix |
|---|---|---|---|---|---|---|---|---|
| F-001 | MAJOR | F1 | IDENTITY.md | H1 | `# Identity: Jake Thornton's Assistant` | H1 carried the forbidden `'s Assistant` suffix; v1.4 F1 requires `# Identity: <Full Name>`. | DIRECT_FIX | Renamed to `# Identity: Jake Thornton`. |
| F-002 | MAJOR | F4 / C10 | AGENTS.md | `## Data Sharing` | `## Data Sharing` | Seventh H2 was named `## Data Sharing`; spec mandates the exact heading `## Data Sharing Policy`. | DIRECT_FIX | Renamed the H2 to `## Data Sharing Policy`. Per-contact enumeration and default-restrictive close retained. |
| F-003 | MAJOR | B1 / B2 | AGENTS.md | Safety & Escalation | "**Data sharing policy**: you may share Jake's information with trusted, verified recipients..." | A generic data-sharing rule lived under Safety & Escalation, duplicating the purpose of the standalone Data Sharing Policy section (single-source-of-truth violation). | DIRECT_FIX | Removed the bullet from Safety & Escalation; the Data Sharing Policy section is the sole home for sharing rules. |
| F-004 | MAJOR | D8 / E7 + override | HEARTBEAT.md | Recurring Events > Annual | "**May 15**: Son Ousmane Johnson's birthday." | Annual birthday fell inside the forbidden April-September window. | DERIVE_FIX | Reassigned Ousmane's DOB to 2025-03-15 and moved the Annual entry to **March 15**; propagated age (13 → 15 months) and birth-month references across USER.md, MEMORY.md > Key Relationships, and MEMORY.md > Health & Wellness. |
| F-005 | MAJOR | A5 + override | HEARTBEAT.md | Recurring Events > Annual | "**September 19**: Wedding anniversary with Marcus." | Anniversary fell in the deadzone (September). | DERIVE_FIX | Marriage month shifted to October 2020 in MEMORY.md > Key Relationships; Annual entry moved to **October 25**. |
| F-006 | MAJOR | override | HEARTBEAT.md | Recurring Events > Annual | "**July**: Annual physical with Dr. Rashida Moore..." | Annual health appointment fell in the deadzone (July). | DERIVE_FIX | Moved to **October 30**; MEMORY.md > Health & Wellness "next due July 2026" updated to "next due October 2026". |
| F-007 | MAJOR | override | HEARTBEAT.md | Recurring Events > Seasonal / Variable | "**Pop-up class season (May through September)**" | Seasonal recurring event sat squarely in the deadzone. | DIRECT_FIX | Reframed to "**Pop-up class season (October through March)**: cool-weather farmers market demos and pop-ups." |
| F-008 | MAJOR | D8 / override | HEARTBEAT.md | Upcoming Events & Deadlines | "**April 2, 2027**... / **May 15, 2027**... / **June 1, 2027**... / **July 4, 2027**..." | Four upcoming events landed in the April-September deadzone. | DIRECT_FIX | Alliance board brief moved to **February 26, 2027** (cadence changed to February in MEMORY.md); recipe-blog release moved to **March 1, 2027**; Ousmane's 2nd birthday recomputed to **March 15, 2027**; July 4 block party removed (inherently a deadzone date, beyond the Oct-Mar window). |
| F-009 | MINOR | override | HEARTBEAT.md | Upcoming Events & Deadlines | (no October event; first was Nov 4) | Operator requires upcoming events to start from October; the list opened in November. | DIRECT_FIX | Added **October 17, 2026** Jake's Table fall harvest class (calendar-verified Saturday) as the opening event. |
| F-010 | MINOR | D8 / E2 | HEARTBEAT.md | Upcoming Events & Deadlines | "**March 8, 2027**: CEU mid-year checkpoint. Target 10 of 20 hours logged." | "Mid-year" is wrong: the CEU year resets each January 1, so March 8 is early Q1, not mid-year; a 10/20 target two months in is implausible. | DIRECT_FIX | Reworded to "First-quarter CEU checkpoint. Target 5 of 20 hours logged for the new year." |
| F-011 | MAJOR | D7 + override | TOOLS.md | Connected Services (30+ bullets) | "Stands by for...", "currently quiet", "Read-only feed", "rarely opened", "otherwise untouched", "currently inactive" | Roughly a third of the 101 APIs were described as dormant, read-only, or conditional, violating the "active, persona-aligned use only" constraint and the D7 occupation-fit check (developer, HR, analytics, and crypto tools left unjustified for a midwife/cook). | DIRECT_FIX | Rewrote every weak bullet with a concrete, active, persona-anchored purpose tied to one of Jake's real workstreams (midwifery practice, Jake's Table, recipe blog, Maternal Wellness Alliance volunteering, household finance review). See Remediation Log. Count held at exactly 101. |
| F-012 | MAJOR | A1 / A3 | MEMORY.md + TOOLS.md | Connected Accounts; Marketing & Magnolia Admin categories | "Salesforce CRM... all via Okta SSO"; "**Salesforce**: Magnolia practice CRM"; "**Gusto**: Magnolia payroll" | Magnolia (a small midwifery practice) implausibly bundled an enterprise Salesforce CRM and external payroll, and the work-system boundary in AGENTS conflicted with treating these as freely connected. | DERIVE_FIX | Salesforce reassigned to the Atlanta Maternal Wellness Alliance nonprofit CRM (Jake's volunteer work); Gusto reassigned to Jake's Table contractor payroll; Xero reassigned to the Alliance's books; MEMORY.md > Connected Accounts restructured into Magnolia / Alliance / Jake's Table back-office groupings to match TOOLS.md. |
| F-013 | MINOR | D1 | TOOLS.md | Jake's Table Storefront | "**Amazon Seller** (`amazon-seller-api`): ...future... Currently quiet." | Amazon Seller API is correctly seller-side for Jake's branded merch, but was described as inactive. | DIRECT_FIX | Reframed as an active listing/fulfillment channel for the Jake's Table spice blend and aprons with inventory tracking. (No API-direction defect: seller-side use is correct here.) |
| F-014 | MINOR | C6 / D | MEMORY.md | Personal Profile | "He carries both CPM and CNM certifications." | Holding both CPM (direct-entry) and CNM (nurse-midwife) credentials is an uncommon, unverified pairing; his title everywhere is CNM. | DIRECT_FIX | Replaced with "active CNM certification through the American Midwifery Certification Board and a Georgia RN license," which covers both his hospital and low-risk home births. |
| F-015 | MINOR | A1 | TOOLS.md | Not Connected | "...beyond the shared Google Classroom view." | After Google Classroom was repurposed (F-011) to host Jake's cooking-course handouts, the Not Connected line still implied a shared view into Marcus's teaching account. | DIRECT_FIX | Trimmed to "Marcus Johnson's personal email, banking, and Oakwood Heights teacher accounts." |

**Open findings remaining after Phase 2:** 0.
**REQUIRES_HUMAN_INPUT items:** 0. All reassigned dates were derived from existing facts and re-checked for internal consistency; none required fabricating substantive new biography.

---

## Section 2 — Coherence Score

```
Score: 9.7 / 10
Rubric:
  - Cross-file alignment (Mode A):           2.0 / 2.0
  - Overlapping / SoT compliance (Mode B):   1.0 / 1.0
  - Required-field completeness (Mode C):    1.0 / 1.0
  - Factual & domain correctness (Mode D):   1.8 / 2.0   (101 fixed-list APIs force some enterprise/dev/crypto tools onto a midwife; each now carries a plausible active justification, but a handful remain a stretch by occupation)
  - Mathematical correctness (Mode E):       1.0 / 1.0
  - Heading-structure compliance (Mode F):   2.0 / 2.0
  - Format-structure compliance:             0.9 / 1.0   (all caps, line limits, single Weekly block, and deadzone rules satisfied; deduction reflects that quarterly cadence events still technically recur through Apr-Sep, which is inherent to the calendar and out of the annual/upcoming scope)
                            Total:           9.7 / 10.0
```

Mode E spot-checks that passed: every inner-circle age reconciles to its DOB against the 2026-06-27 anchor (Marcus 34, Linda 58, Katie 27, Gloria 62, Uncle Dave 55, Mariama 3, Ousmane 15 months, Nene 31); parent-at-birth math is plausible; household budget line items (~$5,990/mo) sit consistently under stated net take-home (~$9,800/mo); income components sum to the $164,000 gross (92 + 14 + 58); TOOLS.md holds exactly 101 unique canonical `-api` slugs.

---

## Section 3 — Remediation Log

| Finding ID | File | Change Type | Before | After | Justification |
|---|---|---|---|---|---|
| F-001 | IDENTITY.md | H1 rename | `# Identity: Jake Thornton's Assistant` | `# Identity: Jake Thornton` | F1 H1 pattern. |
| F-002 | AGENTS.md | H2 rename | `## Data Sharing` | `## Data Sharing Policy` | F4 / C10 mandatory seventh H2. |
| F-003 | AGENTS.md | Bullet removal | Generic "Data sharing policy" bullet under Safety & Escalation | (removed) | B1/B2 single-source-of-truth; rules live only in Data Sharing Policy. |
| F-004 | HEARTBEAT.md, USER.md, MEMORY.md | Date + age cascade | Ousmane DOB 2025-05-15, "13 months", "May 2025 birth", Annual "May 15" | DOB 2025-03-15, "15 months", "March 2025 birth", Annual "March 15", upcoming 2nd birthday "March 15, 2027" | No annual event Apr-Sep; age recomputed against anchor. |
| F-005 | HEARTBEAT.md, MEMORY.md | Date shift | "Married since September 2020"; Annual "September 19" | "Married since October 2020"; Annual "October 25" | Deadzone removal; no downstream age impact. |
| F-006 | HEARTBEAT.md, MEMORY.md | Date shift | Annual "July: Annual physical"; "next due July 2026" | Annual "October 30"; "next due October 2026" | Deadzone removal. |
| F-007 | HEARTBEAT.md | Reframe | "Pop-up class season (May through September)" | "Pop-up class season (October through March)" | Deadzone removal; Atlanta cool-season demos remain plausible. |
| F-008 | HEARTBEAT.md, MEMORY.md | Reseed / remove | April 2 / May 15 / June 1 / July 4 2027 events | Feb 26 (Alliance brief), Mar 1 (blog release), Mar 15 (Ousmane bday); July 4 removed | Upcoming events confined to Oct 2026-Mar 2027; no deadzone events. |
| F-009 | HEARTBEAT.md | Addition | (first event Nov 4, 2026) | Added Oct 17, 2026 fall harvest class | Upcoming events start from October. |
| F-010 | HEARTBEAT.md | Reword | "CEU mid-year checkpoint. Target 10 of 20" | "First-quarter CEU checkpoint. Target 5 of 20" | CEU year resets Jan 1; March is Q1, not mid-year. |
| F-011 | TOOLS.md | Bulk description rewrite (30+ bullets) | Standby / read-only / conditional filler | Active, persona-aligned uses (see Section 1) | Operator constraint + D7 occupation fit; count held at 101. |
| F-012 | MEMORY.md, TOOLS.md | Reassignment | Salesforce/Gusto/Xero as Magnolia enterprise systems | Salesforce → Alliance CRM; Gusto → Jake's Table payroll; Xero → Alliance books | A1/A3 cross-file alignment + plausibility. |
| F-013 | TOOLS.md | Reframe | Amazon Seller "currently quiet" | Active merch listing/fulfillment | Active-use constraint; seller-side direction correct. |
| F-014 | MEMORY.md | Credential correction | "both CPM and CNM certifications" | "active CNM certification (AMCB) and Georgia RN license" | C6 verifiable credential; matches stated title. |
| F-015 | TOOLS.md | Trim | "...beyond the shared Google Classroom view." | "...Oakwood Heights teacher accounts." | A1 consistency after F-011 repurpose. |

---

## Section 4 — Open Questions for Human Input

None block deployment. Two optional confirmations for the human:

- Q1. Ousmane's birth month was moved from May to March (DOB 2025-03-15) and his age updated from 13 to 15 months to satisfy the no-deadzone rule. If the real birth month must stay in May, an explicit override note is required and the deadzone rule would need relaxing for that single entry.
- Q2. The marriage month was shifted from September to October 2020 and the anniversary to October 25 for the same reason. Confirm if a specific wedding date must be preserved.

---

## Section 5 — Common-Errors Cross-Check (selected high-signal entries)

| # | Error | Status |
|---|---|---|
| 5 | Direct `.md` filename references inside persona files | PASS. grep across all 7 files returns zero matches. |
| 6 | Bare "Dormant." entries in TOOLS.md | PASS. Every API carries a one-line active description. |
| 7 | Unnatural "not in use" phrasings | PASS. All standby/read-only filler removed; descriptions are active and varied. |
| 10 | Duplicate API entries / count drift | PASS. Exactly 101 unique canonical slugs (verified by check_101_api.py: "All APIs match"). |
| 11 | Unbolded USER.md Basics labels | PASS. Name, Age, DOB, Timezone, Location all bolded. |
| 12 | DOB outside October-March window | PASS. Jake's DOB November 18, 1993 is in window. |
| 13 | Em/en/horizontal dashes | PASS. grep returns zero matches. |
| 15 | Forbidden tokens in TOOLS.md | PASS. No `via mock`, `shopify`, `fintrack`, `todoist`, or port numbers. |
| 16 | `### General Agent Capabilities` block | PASS. Absent; only `### Connected Services` H3 present. |
| 19 | AGENTS.md required H2 set | PASS. 7 H2s in order, ending with `## Data Sharing Policy`. |
| 20 | HEARTBEAT.md Weekly drift | PASS. Single `### Weekly` block, one bullet per day. |
| 21 | IDENTITY.md opener / closer | PASS. Opener "You are OpenClaw, Jake Thornton's personal AI assistant"; closer "You are not new here. You have context, and you use it." |
| 22 | MEMORY.md section order / count | PASS. 11 H2s in canonical order. |
| 23 | Data-sharing as separate heading | PASS. Standalone `## Data Sharing Policy` H2 with per-contact rules and default-restrictive close. |
| 26 | Pronoun drift | PASS. Uniform he/him across all 7 files. |
| 29 | Assistant nickname consistency | PASS. "Claw" appears once (IDENTITY.md opening); all else uses "OpenClaw". |

---

## Section 6 — File-Size & Structure Validation

| File | Characters | Lines | Cap | Status |
|---|---|---|---|---|
| SOUL.md | 3,938 | 41 | 20,000 | PASS |
| IDENTITY.md | 1,769 | 17 | 20,000 | PASS |
| AGENTS.md | 8,125 | 80 | 20,000 | PASS |
| USER.md | 2,100 | 34 | 20,000 / 40 lines | PASS |
| TOOLS.md | 13,806 | 152 | 20,000 | PASS |
| HEARTBEAT.md | 5,778 | 75 | 20,000 | PASS |
| MEMORY.md | 12,494 | 111 | 15,000 target / 20,000 hard | PASS |
| **Total** | **48,010** | — | **140,000** | **PASS (66% headroom)** |

Structure: SOUL 4 H2 / IDENTITY H1 + Nature + Principles / AGENTS 7 H2 / USER 5 H2 / TOOLS 1 H2 + 1 H3 + 12 H4 categories + Not Connected / HEARTBEAT 2 H2 (single Weekly) / MEMORY 11 H2 — all verified in canonical order.

---

## VERDICT

# **PASS** (Coherence Score: 9.7 / 10)

**Production-ready.** The jake-thornton persona survives the 30-day adversarial-deployment standard. All 15 defects detected this pass — one mis-formed H1, a mis-named seventh H2, a single-source-of-truth duplication, eight deadzone date/event defects, a CEU logic slip, a bulk of dormant API descriptions, three cross-file alignment/plausibility issues, and one credential correction — were remediated, and the corrected files re-pass MODE A (alignment), MODE B (overlap), and MODE F (structure) with no new contradictions introduced.

Key gates confirmed after remediation: TOOLS.md holds **exactly 101** unique canonical `-api` slugs, each now carrying an active, persona-aligned purpose with no read-only or standby filler; **no annual event and no upcoming event falls in the April-September deadzone**; upcoming events run cleanly from **October 17, 2026 through March 15, 2027**; no `.md` filename references, em/en dashes, or forbidden tokens exist anywhere; and all age, budget, and recurrence arithmetic reconciles to the 2026-06-27 anchor.

**No CRITICAL findings. No MAJOR findings remain open. Zero `REQUIRES_HUMAN_INPUT` items block deployment.** The two optional questions in Section 4 concern date reassignments made to satisfy the deadzone rule and can be confirmed or overridden by the operator without affecting deployability.

*Signed: Senior persona-systems QA engineer (adversarial-skepticism posture). Audit date 2026-06-27.*
