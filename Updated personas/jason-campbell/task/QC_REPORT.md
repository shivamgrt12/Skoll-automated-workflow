# PERSONA QC REPORT — Jason Campbell

**QC spec:** PERSONA_QC_PROMPT v1.4 · **Audit date:** 2026-06-27 · **Scope:** 7 inner files in `jason-campbell/` · **Run type:** Full forensic audit, Modes A through F, with in-place remediation. README.md and the `task/` folder are out of scope.

**Anchor date (derived from persona):** 2026-06-27. Derivation: USER.md > Basics gives Age 51 with DOB November 14, 1974 (age 51 holds from 2025-11-14 to 2026-11-13); IDENTITY.md opening states the OpenClaw relationship began "since August 2025" (~10-month tenure at a mid-2026 present); HEARTBEAT.md > Upcoming Events & Deadlines opens October 1, 2026 and runs forward to February 2027. All three anchors reconcile on a present date of late June 2026.

---

## VERDICT: PASS (post-remediation)

The persona entered the audit structurally sound on the high-stakes axes — correct H1 set, the seventh `## Data Sharing Policy` H2 already present, exactly 101 unique `-api` slugs, DOB inside the October–March fiscal window, and no patient-confidentiality red-line in the clinical content — but it failed forensic inspection on fifteen points, none CRITICAL, six MAJOR and nine MINOR. Every defect was remediable from existing persona signal without escalation. The six MAJOR fixes were: (1) the IDENTITY.md > Principles bullets opened with declarative-plus-imperative phrasings ("Privacy is measured...", "Act first...", "Accuracy beats speed...") in violation of the `You ...` voice gate; (2) the required closing line was welded into the opening paragraph and the tenure phrase was a vague "for ten months" rather than a concrete since-date; (3) the email domain across AGENTS, MEMORY, and TOOLS was the non-canonical `@Greenridertech.com` rather than the cohort default `@Finthesiss.ai`; (4) roughly forty TOOLS.md bullets were framed "read-only", "inactive", "view only", "not in household use", or "legacy", leaving APIs listed without an active persona-aligned use, against the standing instruction that all 101 carry live, persona-aligned purpose; (5) inner-circle DOBs were entirely absent from MEMORY.md > Key Relationships and consequently from HEARTBEAT.md > Annual; (6) AGENTS.md > Data Sharing Policy carried misplaced emergency-contact and escalation bullets that belong under Safety & Escalation, the section lacked the C7-mandatory ICE / medical-proxy / durable-POA designations for an over-50 persona, and a blank line was missing before the H2. The nine MINOR items covered a dead-zone annual dentist event, a cross-file study-deadline contradiction, unbolded USER Basics labels, a Gainesville-vs-Panama-City geography slip, a colleague email domain inconsistent with the practice name, a past-dated "next inspection 2025", a dead-zone Step 2 exam month, the "connected mock APIs" implementation leak, and bare file-like section references in AGENTS Memory Management.

After remediation: TOOLS.md carries exactly 101 unique `-api` slugs (E6, verified by count and a duplicate sweep), every bullet conforms to the canonical regex and the forbidden-token sweep (`via mock`, `shopify`, `fintrack`, `todoist`, ports) returns zero, USER.md sits at 35 of 40 permitted lines with bolded Basics labels, every file is under its character cap (TOOLS ~16,100 / MEMORY ~11,900; total ~44,900 of 140,000), all 7 H1s match `# <FileName>: <Full Name>`, and AGENTS now carries 7 H2s in order with the seventh `## Data Sharing Policy`. Cross-file alignment holds end-to-end: the household gross reconciles ($485,000 + $128,000 = $613,000), every inner-circle age reconciles to its new DOB against the anchor, the study deadlines now agree between MEMORY and HEARTBEAT, and every annual recurring event and birthday sits inside the October–March window with the Upcoming Events list running strictly forward of the anchor from October 2026 to February 2027. No direct `.md` filename reference, em-dash, or en-dash appears anywhere in the 7 inner files. The persona is deployable.

---

## Mechanical Verification Record

| Gate | Requirement | Measured | Result |
|---|---|---|---|
| E6 slug count | exactly 101 unique `-api` slugs | 101 total / 101 unique (duplicate sweep empty) | PASS |
| F6 bullet regex | every API bullet conforms | 101/101 conform; zero forbidden tokens | PASS |
| F6 Not Connected | final H4, web-search-unavailable note present, no leak | present, final, "connected services listed above" | PASS |
| F6 forbidden H3 | no `### General Agent Capabilities` | absent | PASS |
| F5 / F10 USER cap | <= 40 lines, Basics labels bold | 35 lines, all 5 labels bolded | PASS |
| F10 char caps | each <= 20,000; MEMORY <= 15,000; total <= 140,000 | TOOLS ~16,100; MEMORY ~11,900; total ~44,900 | PASS |
| F1 H1 pattern | `# <FileName>: <Full Name>` x7 | all 7 conform | PASS |
| F2–F8 heading sets | exact-match, canonical order | SOUL 4 H2; IDENTITY no H2, 2 H3 + standalone closer; AGENTS 7 H2 incl. Data Sharing Policy 7th; USER 5 H2; TOOLS 1 H2 / 1 H3 / 12 H4 with Not Connected last; HEARTBEAT 2 H2, single Weekly; MEMORY 11 H2 | PASS |
| C1 DOB window | persona DOB month Oct–Mar | November 14 | PASS |
| C2 age / timezone | age vs DOB + anchor; IANA-style tz + city | 51 vs Nov 14 1974 correct; Eastern Time, Jacksonville FL | PASS |
| C3 tenure phrase | concrete since-date in IDENTITY opening | "since August 2025" | PASS |
| C4 inner-circle DOBs | spouse/children/parent/sibling full DOBs + Annual propagation | Karen Feb 9 1978, Kyle Dec 3 2003, Emily Jan 22 2008, Dorothy Oct 12 1949, Brian Oct 20 1978, Jason Nov 14 1974 all synced to Annual | PASS |
| C7 ICE / proxy / POA | mandatory for over-50 persona | ICE Karen primary / Brian backup; medical proxy Karen; durable financial POA Karen | PASS |
| C8 threshold | single-currency, no tautology | $500 USD | PASS |
| C9 default clause | present at end of Confirmation Rules | "Default for everything else: Proceed with judgment." | PASS |
| C10 Data Sharing | standalone 7th H2, per-contact, restrictive fallback | 9 named contacts + "With anyone else: confirm with Jason first." | PASS |
| E1 ages | inner-circle ages reconcile to DOB + anchor | all reconcile; Dorothy 25 at Jason's birth, Jason 29 / Karen 25 at Kyle's birth, all plausible | PASS |
| E4 budget | household gross reconciles to sources | $485,000 + $128,000 = $613,000 | PASS |
| E7 recurrence | Annual birthdays match Key Relationships DOBs, all Oct–Mar | Oct 12, Oct 20, Nov 14, Dec 3, Jan 22, Feb 9 all match | PASS |
| A5 schedule | study deadlines agree across files | MEMORY IRB Oct 1 / manuscript Oct 15 = HEARTBEAT | PASS |
| Dead-zone (Apr–Sep) | no annual/recurring event or deadline in window | none remain; dentist moved Jul→Feb, deadlines aligned to Oct | PASS |
| Upcoming window | events start October onward, sorted, sufficient depth | 9 entries Oct 1 2026 → Feb 2027 | PASS |
| Common-errors #5 | zero direct `.md` references in persona content | 0 across all 7 files | PASS |
| Common-errors #13 | no em / en / horizontal-bar dashes | 0 across all 7 files | PASS |
| Common-errors #25 | email domain matches assignment | `@Finthesiss.ai` (Jason not on voissync exception list) | PASS |
| Common-errors #26 | pronoun consistency | "he/him/his" consistent across all 7 files | PASS |

---

## Section 1 — Findings Catalog

| ID | Severity | Mode | File | Section | Quote | Defect | Fix Type | Fix |
|---|---|---|---|---|---|---|---|---|
| F-001 | MAJOR | Common-errors #3 | IDENTITY.md | ### Principles | "Privacy is measured, not absolute. Share with..."; "Act first within confirmed boundaries. Ask only when..."; "Accuracy beats speed."; "Patient confidentiality is non-negotiable."; "Family time is protected by default." | Five Principles bullets opened with a declarative sentence plus an imperative, violating the `You ...` voice gate for IDENTITY bullets. | DIRECT_FIX | Rewrote all five as `You treat / act / honor / hold / protect ...` statements from the verb palette; content preserved. |
| F-002 | MAJOR | C3 / Common-errors #21 | IDENTITY.md | opening paragraph | "...you have been his daily-use assistant for ten months..."; closer welded onto the opening paragraph | Tenure phrase was vague rather than a concrete since-date, and the required closer was not a standalone closing line. | DIRECT_FIX | Set "since August 2025" (10 months before the anchor) and reinstated "You are not new here. You have context, and you use it." as a standalone closing line after Principles. |
| F-003 | MAJOR | Common-errors #25 | AGENTS.md, MEMORY.md, TOOLS.md | Communication Routing; Connected Accounts; Gmail bullet | `jason.campbell@Greenridertech.com` | Non-canonical email domain; cohort default is `@Finthesiss.ai` and Jason is not on the `@voissync.ai` exception list. | DIRECT_FIX | Replaced every occurrence with `jason.campbell@Finthesiss.ai`. |
| F-004 | MAJOR | D7 / user instruction | TOOLS.md | Email, Workspace, Research, Finance, Marketing, Developer, Media, Family Logistics | "Read-only access."; "Inactive."; "View only."; "Not in household use."; "Mark as legacy..."; "Read-only mirror..." (~40 bullets) | Roughly forty connected APIs were listed with passive read-only / inactive framings, leaving them without an active persona-aligned use, against the standing instruction that all 101 carry live purpose. | DIRECT_FIX | Rewrote each into an active use anchored to a named relationship or recurring activity (e.g., Coinbase/Binance/Kraken as Kyle's gift split across exchanges; Alpaca as the platform Jason learns before guiding the kids; Kubernetes during a checkout outage; BambooHR for Karen's fall open enrollment). |
| F-005 | MINOR | F6 / leak | TOOLS.md | #### Not Connected | "Work only from connected mock APIs and stored memory." | The phrase "connected mock APIs" leaked implementation detail into the persona voice. | DIRECT_FIX | Replaced with "the connected services listed above and from stored memory." |
| F-006 | MAJOR | C4 / E7 | MEMORY.md, HEARTBEAT.md | Key Relationships; Annual | ages only ("Karen ... 48", "Kyle ... 22"), HEARTBEAT > Annual carried no birthdays | Inner-circle DOBs absent from the canonical home and not propagated into HEARTBEAT > Annual. | DERIVE_FIX | Added age-consistent DOBs all inside Oct–Mar: Karen Feb 9 1978, Kyle Dec 3 2003, Emily Jan 22 2008, Dorothy Oct 12 1949, Brian Oct 20 1978; propagated all six (plus Jason Nov 14) into HEARTBEAT > Annual with Jason-specific actions. |
| F-007 | MAJOR | A5 / temporal | MEMORY.md, HEARTBEAT.md | Work & Projects; Upcoming Events | MEMORY: "manuscript draft is due August 1 ... IRB renewal is due July 15"; HEARTBEAT: "rescheduled from July 15 / August 1" | Cross-file deadline contradiction, and the MEMORY dates fell in the April–September dead zone. | DIRECT_FIX | Aligned MEMORY to the live dates (IRB October 1, manuscript October 15) and dropped the dead-zone reschedule parentheticals from HEARTBEAT. |
| F-008 | MAJOR | F4 / C7 | AGENTS.md | Data Sharing Policy / Safety & Escalation | "Emergency contact: Karen ... Escalation: ..." bullets under Data Sharing Policy; no ICE/proxy/POA; missing blank line before H2 | Safety content sat under the wrong H2, the C7 over-50 designations were absent, and an H2 lacked its preceding blank line. | DIRECT_FIX | Moved emergency/escalation bullets into Safety & Escalation; added ICE (Karen primary / Brian backup), medical proxy (Karen), durable financial POA (Karen); inserted the blank line. |
| F-009 | MINOR | Common-errors #11 | USER.md | Basics | "- Full name: Jason Campbell." (plain) | Basics labels were not bolded. | DIRECT_FIX | Wrapped all five labels in `**...**`. |
| F-010 | MINOR | D2 | TOOLS.md | Family Logistics; Travel | "gifts to Kyle and Emily in Gainesville"; "rentals near Gainesville" | Children attend Gulf Coast State University (Panama City), not Gainesville (University of Florida) — geographic slip. | DIRECT_FIX | Changed both references to "Panama City." |
| F-011 | MINOR | A1 / coherence | MEMORY.md | Contacts | `r.hussain@baptistheart.com`, `s.chen@baptistheart.com`, `a.torres@baptistheart.com` | Practice colleague emails used a domain unrelated to the named practice (Coastal Cardiology Partners). | DIRECT_FIX | Reassigned all three to `@coastalcardiology.com`. |
| F-012 | MINOR | D8 / temporal | MEMORY.md | Home & Living | "next inspection 2025" | Roof inspection date sits in the past relative to the 2026 anchor. | DIRECT_FIX | Advanced to "next inspection 2027." |
| F-013 | MINOR | D8 / dead-zone | MEMORY.md | Key Relationships | "Studying for USMLE Step 2 with a target date in August" | Step 2 target month fell in the April–September dead zone and disagreed with the HEARTBEAT October target. | DIRECT_FIX | Changed to "a target exam date in October." |
| F-014 | MINOR | D8 / dead-zone | MEMORY.md | Key Relationships | "comes home for Mother's Day and major holidays" | Mother's Day (May) is a recurring April–September reference. | DIRECT_FIX | Reduced to "comes home for major holidays." |
| F-015 | MINOR | Common-errors #5 / #27 | AGENTS.md | Memory Management | "Update MEMORY immediately..."; "Update Work and Projects..."; "confirmed MEMORY content" | Bare capitalized section names read as file references; no explicit session-only guard. | DIRECT_FIX | Rephrased to "stored memory" / "the work and projects record"; added a session-only memory guard per common-errors #27. |

**Checks run with no findings (recorded per §9):** A1 service graph (every MEMORY > Connected Accounts entry maps to a TOOLS `-api` slug; Ring connected in both TOOLS and MEMORY > Devices & Services; Plaid aggregation consistent across TOOLS, MEMORY > Finance, and Connected Accounts), A2 (no SOUL ↔ AGENTS value conflicts), A3 (TOOLS scopes the practice website, patient portal, and IT-volunteer infrastructure without claiming EHR access; institutional systems single-homed in Not Connected), A4 (SOUL "5:00 AM before a cath lab shift" matches HEARTBEAT 5:15 AM running and MEMORY black-French-press coffee), A6 (Karen routed primary ICE matching her spouse tier), A7 (OpenClaw introduced atop IDENTITY with an August 2025 since-date consistent with the anchor), B1/B2/B3 (no duplicate scalar facts; DOB/age/timezone single-homed in USER > Basics; negative connection assertions single-homed in TOOLS > Not Connected), C5 (continuous career timeline, no gaps), C6 (MD, fellowship, and BS credentials each carry an institution), C8/C9/C10 (threshold, default clause, per-contact data sharing), D1 (Amazon Seller used for the brother's seller-side shop, Twilio for outbound reminders, Stripe/Square scoped to practice payments), D3 (no weekday claims on named dates to falsify), D4 (working-class Dearborn / Yankee heritage consistent), D5 (no eligibility, licensure, or authority misclaims), D6 (brand dictionary clean: iPhone 15 Pro Max, Apple Watch Ultra, Tesla Model S, Yamaha CLP-785, Nest, Ring, Lutron, Generac, Spotify), E2/E3 (career math and USD figures plausible), F7 (single Weekly block, no trailing silence clause), F11 (no empty mandatory headings).

---

## Section 2 — Coherence Score

```
Score: 9.4 / 10
Rubric:
  - Cross-file alignment:            1.9 / 2.0   (Mode A — graph fully reconciles post F-003/F-007/F-011;
                                                   small deduction for the cohort-internal @Finthesiss.ai
                                                   convention being applied rather than persona-declared)
  - Overlapping / SoT compliance:    1.0 / 1.0   (Mode B — canonical placements correct; no duplicate
                                                   scalar facts after F-006/F-008)
  - Required-field completeness:     1.0 / 1.0   (Mode C — inner-circle DOBs, credentials, threshold,
                                                   ICE/proxy/POA, and Data Sharing enumeration all present)
  - Factual & domain correctness:    1.9 / 2.0   (Mode D — strong Jacksonville/cardiology localization;
                                                   small deduction for the 555 placeholder phone block
                                                   accepted as cohort convention)
  - Mathematical correctness:        1.0 / 1.0   (Mode E — gross income reconciles, all ages/timelines
                                                   verify, 101-slug gate passes, birthday-to-DOB sync clean)
  - Heading-structure compliance:    1.7 / 2.0   (Mode F headings — all 7 files now exact-match canonical
                                                   sets and order; deduction reflects the pre-remediation
                                                   misplaced Safety bullets and missing H2 blank line)
  - Format-structure compliance:     0.9 / 1.0   (Mode F caps/format — all caps met, regex and token sweeps
                                                   clean; deduction for the pre-remediation unbolded Basics
                                                   labels and the "connected mock APIs" leak)
                            Total:   9.4 / 10.0
```

---

## Section 3 — Remediation Log

| Finding ID | File | Change Type | Before | After | Justification |
|---|---|---|---|---|---|
| F-001 | IDENTITY.md | DIRECT_FIX | 5 declarative-plus-imperative Principles bullets | 5 `You ...` bullets (treat / act / honor / hold / protect) | Common-errors #3 voice gate. |
| F-002 | IDENTITY.md | DIRECT_FIX | "for ten months"; closer welded into opening paragraph | "since August 2025"; standalone closer after Principles | C3 concrete tenure; common-errors #21 closer. |
| F-003 | AGENTS / MEMORY / TOOLS | DIRECT_FIX | `@Greenridertech.com` | `@Finthesiss.ai` | Common-errors #25 cohort default. |
| F-004 | TOOLS.md | DIRECT_FIX | ~40 read-only / inactive / view-only / legacy bullets | active, persona-anchored use cases | User instruction: all 101 APIs carry live, persona-aligned purpose. |
| F-005 | TOOLS.md | DIRECT_FIX | "connected mock APIs and stored memory" | "the connected services listed above and from stored memory" | Implementation-leak removal. |
| F-006 | MEMORY / HEARTBEAT | DERIVE_FIX | ages only; no Annual birthdays | DOBs added (all Oct–Mar) and propagated into Annual | C4 + E7. |
| F-007 | MEMORY / HEARTBEAT | DIRECT_FIX | MEMORY Jul 15 / Aug 1; HEARTBEAT "rescheduled from" notes | both at IRB Oct 1 / manuscript Oct 15 | A5 cross-file agreement; dead-zone removal. |
| F-008 | AGENTS.md | DIRECT_FIX | Safety bullets under Data Sharing; no ICE/proxy/POA; missing H2 blank line | bullets moved to Safety; ICE/proxy/POA added; blank line inserted | F4 placement + C7 over-50 designations. |
| F-009 | USER.md | DIRECT_FIX | plain Basics labels | bolded labels | Common-errors #11. |
| F-010 | TOOLS.md | DIRECT_FIX | "Gainesville" (x2) | "Panama City" | D2 geography matches Gulf Coast State University. |
| F-011 | MEMORY.md | DIRECT_FIX | `@baptistheart.com` (x3) | `@coastalcardiology.com` | A1 practice-name coherence. |
| F-012 | MEMORY.md | DIRECT_FIX | "next inspection 2025" | "next inspection 2027" | D8 past-dated future event. |
| F-013 | MEMORY.md | DIRECT_FIX | Step 2 "target date in August" | "target exam date in October" | Dead-zone + agreement with HEARTBEAT. |
| F-014 | MEMORY.md | DIRECT_FIX | "Mother's Day and major holidays" | "major holidays" | Dead-zone recurring reference removed. |
| F-015 | AGENTS.md | DIRECT_FIX | "Update MEMORY..."; "confirmed MEMORY content" | "stored memory" / "the work and projects record"; session-only guard added | Common-errors #5 + #27. |

---

## Section 4 — Open Questions for Human Input

None. Every defect surfaced in Phase 1 was remediable from existing persona context. Where new facts were synthesized — inner-circle DOBs, ICE/proxy/POA designations, the small-balance crypto and brokerage justifications, and the October-forward calendar — each was anchored to existing persona signal (stated ages, the brother's October 20 birthday already present in the upcoming list, Karen's role as pharmacist and household manager, Kyle's gift context, the storm-damaged roof, the 32-year practice tenure) and verified for arithmetic, calendar, and cross-file consistency. No fact was invented without a persona-aligned source thread.

---

## Section 5 — Cross-Persona Pattern Flags

Conventions and defect classes observed here worth a cohort-wide sweep:

1. **IDENTITY Principles imperative voice** (F-001) — grep `### Principles` and confirm every bullet leads with `You ...`.
2. **IDENTITY closer welded to opening paragraph + vague tenure** (F-002) — confirm the verbatim closer stands alone and the since-date is a concrete Month Year.
3. **Non-canonical email domain `@Greenridertech.com`** (F-003) — grep every persona for any domain other than its assigned `@Finthesiss.ai` / `@voissync.ai`.
4. **TOOLS "read-only" / "inactive" / "view only" / "legacy" framings** (F-004) — grep these tokens across TOOLS.md cohort-wide; each API must carry an active persona-aligned use.
5. **Missing inner-circle DOBs and HEARTBEAT > Annual propagation** (F-006) — verify every spouse, child, parent, sibling carries a DOB and that each propagates into Annual.
6. **April–September dead-zone events** (F-007, F-013, F-014) — verify no annual/recurring event, deadline, or recurring reference falls in the fiscal dead zone, and that Upcoming Events run strictly forward of the anchor from October onward.
7. **Misplaced Safety bullets and missing C7 designations for over-50 personas** (F-008) — verify ICE, medical proxy, and durable POA sit under Safety & Escalation for every persona over 50.

---

*End of report.*
