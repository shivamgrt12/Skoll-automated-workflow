# PERSONA QC REPORT — Jason Rivera

**QC spec:** PERSONA_QC_PROMPT v1.4 · **Audit date:** 2026-06-27 · **Scope:** 7 inner files in `jason-rivera/` · **Run type:** Full audit, Modes A through F, with in-place remediation and a forced cross-check against the common-errors catalog

**Anchor date (derived from persona):** mid-2026 (2026-06-27). Derivation: IDENTITY.md opening states "You have been his daily-use assistant for eight months" (tenure start ~October 2025); USER.md > Basics gives Age 47 with DOB January 22, 1979 (age 47 holds from 2026-01-22 to 2027-01-21); HEARTBEAT.md > Upcoming Events & Deadlines runs October 3, 2026 through Spring 2027. All three anchors reconcile on a present date of mid-2026.

---

## VERDICT: PASS (post-remediation)

The initial pass surfaced **fourteen MAJOR** and **four MINOR** defects, all corrected in place during this audit. **No CRITICAL findings appeared** — the API count was already exactly 101, the DOB sat correctly in the October–March fiscal window, and no operational red-line (eligibility, licensure, or fraud) claim was present.

The headline defects were: (1) a template-leak proper noun, "Fulcrum Group," used as the **name of the second restaurant location** across five files — nonsensical for a Turkish kebab house and a clear generation artifact; (2) a non-canonical twelfth H2, `## Real Estate`, in MEMORY.md, breaking the fixed 11-section contract; (3) **inner-circle DOBs entirely absent** from MEMORY.md > Key Relationships and from HEARTBEAT.md > Annual; (4) HEARTBEAT.md > Annual carried an **April 15 event inside the forbidden April–September window** and **no birthday entries at all**; (5) roughly thirty TOOLS.md bullets framed as "read-only," "inactive," "view only," or "watch only," leaving APIs with no active persona-aligned use; (6) five further brand/template leaks (`Luminar Design Group F-150`, `Crestline Consulting Workspace`, `Ashdale Technologies`, `Ashvale local news`, `Herongate Partners` brokerage); (7) IDENTITY.md > Principles bullets written in declarative/imperative voice rather than the mandated `You ...` voice; (8) the IDENTITY closer welded into the opening paragraph rather than standing alone at the end of the file; (9) direct `MEMORY`/`HEARTBEAT` file references in SOUL.md and AGENTS.md; (10) the source-document email domain `@Greenridertech.com` rather than the cohort default `@Finthesiss.ai`; (11) a finance arithmetic break — the household-income line double-counted catering and mis-stated property income at $40,000 against an actual $52,200 gross / ~$14,000 net.

Four MINOR items rounded it out: TOOLS.md > Not Connected leaked the phrase "connected mock APIs"; USER.md > Basics labels were unbolded; the Emergency-contact and Escalation bullets were misfiled under `## Data Sharing Policy` instead of `## Safety & Escalation`; and two HEARTBEAT.md Weekly entries were bare "Standard restaurant operations" deadzones with no real commitment rolled up.

After remediation: TOOLS.md carries **exactly 101 unique `-api` slugs** (E6, verified by sweep, zero duplicates, zero forbidden tokens), every API bullet conforms to the F6 regex and every one now carries an **active, persona-aligned** use; USER.md is **35 of 40** permitted lines with bolded Basics labels; every file sits under its cap (MEMORY 14,941 of 15,000 target; total **52,871** of 140,000); all 7 H1s match `# <FileName>: <Full Name>`; AGENTS.md carries its 7 H2s including `## Data Sharing Policy` as the seventh; MEMORY.md is back to its 11 canonical H2s in order; HEARTBEAT.md uses a single `### Weekly` block, an Annual section entirely inside October–March, and a forward-only Upcoming calendar of 12 dated entries from October 3, 2026 onward. **Zero `.md` filename references** remain in persona content; **zero deadzone events** remain. The persona is deployable.

---

## Mechanical Verification Record

| Gate | Requirement | Measured | Result |
|---|---|---|---|
| E6 slug count | exactly 101 unique `-api` slugs | 101 total / 101 unique / 0 duplicates | PASS |
| F6 bullet regex | every API bullet conforms | 101/101 conform; zero `via mock`/`shopify`/`fintrack`/`todoist`/ports/`mock` | PASS |
| F6 Not Connected | final H4, web-search-unavailable note, no implementation leak | present, final, "connected services listed above" | PASS |
| F6 forbidden H3 | no `### General Agent Capabilities` | absent (only `### Connected Services`) | PASS |
| F5 / F10 USER cap | <= 40 lines, Basics labels bolded | 35 lines, all 5 labels bold | PASS |
| F10 char caps | each <= 20,000; MEMORY <= 15,000; total <= 140,000 | SOUL 3,915 / IDENTITY 1,668 / AGENTS 7,877 / USER 2,524 / TOOLS 17,108 / HEARTBEAT 4,838 / MEMORY 14,941; total 52,871 | PASS |
| F1 H1 pattern | `# <FileName>: <Full Name>` x7 | all 7 conform | PASS |
| F4 AGENTS H2 set | 7 H2s, `## Data Sharing Policy` 7th | 7 H2s in canonical order | PASS |
| F8 MEMORY H2 set | exactly 11 H2s in order | 11 in order (post `## Real Estate` merge) | PASS |
| F7 HEARTBEAT | 2 H2s, single `### Weekly`, no trailing silence | 2 H2s, single Weekly, ends on last event | PASS |
| Annual window | no Annual event in April–September | Oct 3, 18; Nov 5, 18; Dec 12, 20; Jan 15, 22; Mar 9 — all Oct–Mar | PASS |
| Upcoming forward | all entries strictly forward of anchor, October onward | 12 entries Oct 3, 2026 → Spring 2027, no duplicates | PASS |
| D3 calendar | weekday claims match real calendar | Oct 10 (Sat), 17 (Sat), 24 (Sat), 28 (Wed); Nov 14 (Sat), 26 (Thu, Thanksgiving); Dec 5 (Sat), 19 (Sat), 31 (Thu) 2026 all verified | PASS |
| E7 recurrence | HEARTBEAT > Annual birthdays match MEMORY DOBs | Oct 3 Emre, Oct 18 Elif, Nov 5 Ayse, Nov 18 Mehmet, Dec 12 Hatice, Dec 20 Kerem, Jan 22 Jason, Mar 9 Hasan — all sync | PASS |
| E1 / E2 ages & career | ages and timeline reconcile to anchor | Age 47 vs DOB Jan 22, 1979 correct; restaurant 1 opened 2012 = 14 years; relative ages consistent with assigned DOBs | PASS |
| E4 finance | household income reconciles; no double-count | $140,000 (restaurants) + $78,000 (Ayse) + ~$14,000 (net property) = ~$232,000; property gross $52,200 nets ~$14,200 after mortgage/taxes/insurance | PASS |
| C1 DOB window | persona DOB month Oct–Mar | January (Jan 22) | PASS |
| C8 threshold | single-currency threshold, no tautology | $200 USD, no self-conversion | PASS |
| C9 default clause | present | "Default for everything else: Proceed with judgment." | PASS |
| C10 Data Sharing | standalone 7th H2, per-contact bullets, restrictive fallback | 9 named-contact buckets + "With anyone else: Confirm with Jason first. When in doubt, share less." | PASS |
| C4 inner-circle DOBs | spouse, children, parent, sibling, best friend | Ayse, Emre, Elif, Kerem, Hatice, Mehmet, Hasan all carry full DOBs | PASS |
| Common-errors #5 | zero direct `.md` references in persona content | grep across 7 files returns 0 | PASS |
| Common-errors #13 | no em/en dashes or horizontal bars | absent across 7 files | PASS |
| Common-errors #21 | IDENTITY opener atop, closer standalone at end | opener line 3; closer standalone after Principles | PASS |
| Common-errors #25 | email domain matches assignment | `@Finthesiss.ai` throughout (Jason not on `@voissync.ai` list) | PASS |
| Common-errors #26 | pronoun consistency | "he/him/his" consistent across all 7 files | PASS |
| No deadzone events | every recurring/upcoming entry carries a real commitment | Weekly Tuesday/Thursday rebuilt; all Annual/Upcoming entries action-bearing | PASS |

---

## Section 1 — Findings Catalog

| ID | Severity | Mode | File | Section | Quote | Defect | Fix Type | Fix |
|---|---|---|---|---|---|---|---|---|
| F-001 | MAJOR | D / brand-fit | USER, AGENTS, HEARTBEAT, MEMORY, TOOLS | multiple | "added a Fulcrum Group second location in 2021"; "Anatolia Kebab House Fulcrum Group" | "Fulcrum Group" is a template-leak proper noun used as the second restaurant's name; nonsensical for a Turkish kebab house. | DIRECT_FIX | Renamed the second location to the **Wayne** location of Anatolia Kebab House across all five files; updated Derya/Osman titles and the Linear loan-tracker reference. |
| F-002 | MAJOR | F8 | MEMORY.md | `## Real Estate` | "## Real Estate" (12th H2) | MEMORY.md must carry exactly 11 canonical H2s; `## Real Estate` is non-canonical. | DIRECT_FIX | Folded the property paragraph into `## Work & Projects`; deleted the extra heading. MEMORY is back to 11 H2s in order. |
| F-003 | MAJOR | C4 / E7 | MEMORY, HEARTBEAT | Key Relationships, Annual | ages only, e.g. "**Ayse Rivera (wife)**: 44, …"; HEARTBEAT > Annual carried no birthdays | Inner-circle DOBs were absent from Key Relationships and not propagated into Annual. | DIRECT_FIX | Added full DOBs for Ayse (Nov 5, 1981), Emre (Oct 3, 2009), Elif (Oct 18, 2012), Kerem (Dec 20, 2016), Hatice (Dec 12, 1953), Mehmet (Nov 18, 1982), Hasan (Mar 9, 1977); all propagated into Annual with Jason-specific actions. |
| F-004 | MAJOR | A5 / D8 / Annual-window | HEARTBEAT.md | Annual; Upcoming | "**April 15**: Estimated quarterly taxes …"; "**November 15**: Estimated quarterly taxes"; duplicate Emre/Elif birthday lines | Annual carried an April event (forbidden Apr–Sep window) and a non-existent Nov 15 federal tax date; Upcoming duplicated two birthdays and misfiled recurring birthdays as one-time events. | DIRECT_FIX | Rebuilt Annual to Q4 taxes (Jan 15) + birthdays, all Oct–Mar; rebuilt Upcoming as 12 forward-only dated one-time events, deduplicated, recurring birthdays moved to Annual. |
| F-005 | MAJOR | D7 / common-errors #6, #7 | TOOLS.md | many bullets | "Read-only awareness…"; "Inactive household account…"; "View only."; "Watch only."; "Mark inactive…" | ~30 bullets framed an API as read-only/inactive, leaving it with no active persona use; instruction requires every API to carry active, aligned use. | DIRECT_FIX | Rewrote every passive bullet into an active, persona-anchored use (e.g., Coinbase → Emre's custodial learning balance; Binance/Kraken → lira-rate timing for Mehmet's remittance; Strava → post-dinner walks; Amazon Seller → packaged Adana spice-blend retail). |
| F-006 | MAJOR | D6 | MEMORY.md | Home & Living, Devices, Finance, Connected Accounts, Preferences | "2020 Luminar Design Group F-150"; "Crestline Consulting Workspace"; "Ashdale Technologies"; "Ashvale local news"; "Herongate Partners" | Five fabricated brand/template names used where real, persona-aligned brands belong. | DIRECT_FIX | → Ford F-150; Google Workspace; Netflix; TAPinto Paterson; Fidelity (brokerage). Propagated to TOOLS Plaid and Not Connected lines. |
| F-007 | MAJOR | C3 / common-errors #3 | IDENTITY.md | Principles | "Privacy is measured, not absolute."; "Act first…"; "Accuracy beats speed."; "Family time is protected."; "Cultural fluency is part of the job." | All five Principles bullets opened in declarative/imperative voice, violating the `You ...` voice gate. | DIRECT_FIX | Rewrote all five as `You ...` statements (treat, act, hold, protect, treat) with content preserved. |
| F-008 | MAJOR | common-errors #21 / F3 | IDENTITY.md | opening paragraph | "…the deadlines that keep two LLCs and a mixed-use building running. You are not new here. You have context, and you use it." | The required closer was welded into the opening paragraph instead of standing alone at the end of the file. | DIRECT_FIX | Moved the closer to a standalone closing line after `### Principles`. |
| F-009 | MAJOR | common-errors #5 | SOUL, AGENTS | Continuity; Session Behaviour, Memory Management, Safety & Escalation | "You read MEMORY at the start of each session"; "Read MEMORY for current context"; "Update MEMORY immediately…"; "confirmed MEMORY content" | Direct `MEMORY` file references leaked implementation detail into persona voice. | DIRECT_FIX | Replaced with "stored memory," "the work and projects record," "the property record" per the substitution table. |
| F-010 | MAJOR | common-errors #25 | AGENTS, MEMORY, TOOLS | Communication Routing; Connected Accounts; Gmail bullet | `jason.rivera@Greenridertech.com` | Source-document domain does not match the cohort default; Jason is not on the `@voissync.ai` exception list. | DIRECT_FIX | Replaced every occurrence with `jason.rivera@Finthesiss.ai`. |
| F-011 | MAJOR | E4 | MEMORY.md | Finance | "Household gross is roughly $276,000. Jason: $140,000 … $40,000 in property gross rental, and $18,000 in catering." | Property income mis-stated ($40,000 vs actual $52,200 gross / ~$14,200 net) and catering double-counted (it is already inside the $1.8M restaurant revenue). | DIRECT_FIX | Reset to "~$232,000: $140,000 (restaurants) + $78,000 (Ayse) + ~$14,000 (net property)." Catering removed from personal income. |
| F-012 | MAJOR | E5 / temporal | MEMORY.md | Work & Projects | "next due May 2026"; "September 2026 as the payoff target" | Health-inspection "next due May 2026" is already past the anchor; equipment-loan payoff target of Sept 2026 predates the Oct-onward Upcoming window. | DIRECT_FIX | Updated to "scored 96 in May 2026; next routine inspection due around November 2026" and "end of 2026 payoff target"; surfaced both in Upcoming (Nov 14 inspection window, Dec 5 payoff). |
| F-013 | MAJOR | A1 / common-errors #6 | TOOLS, MEMORY | Plaid / Connected Accounts | "Plaid read-only"; "Herongate Partners brokerage" | Two coupled defects: passive "read-only" framing and the fabricated brokerage name in the aggregation list and Not Connected line. | DIRECT_FIX | "Plaid read aggregation"; brokerage → Fidelity, reconciled across MEMORY Finance, MEMORY Connected Accounts, TOOLS Plaid, TOOLS Not Connected. |
| F-014 | MAJOR | A | IDENTITY.md | opening paragraph | "his two Paterson restaurants" | After the Wayne rename, "two Paterson restaurants" became geographically wrong (one is in Wayne). | DIRECT_FIX | "his two restaurants in Paterson and Wayne." |
| F-015 | MINOR | F6 / common-errors #15 | TOOLS.md | Not Connected | "Work only from connected mock APIs and stored memory." | "connected mock APIs" leaks implementation detail into persona voice. | DIRECT_FIX | "Work only from the connected services listed above and from stored memory." |
| F-016 | MINOR | common-errors #11 | USER.md | Basics | "- Full name: Jason Rivera." (unbolded) | Basics labels were not bolded. | DIRECT_FIX | Bolded all five labels. |
| F-017 | MINOR | B1 | AGENTS.md | Data Sharing Policy | "- **Emergency contact**: …"; "- **Escalation**: …" | Emergency-contact and Escalation bullets were filed under `## Data Sharing Policy`; they belong in `## Safety & Escalation`. | DIRECT_FIX | Moved both into Safety & Escalation; Data Sharing now ends on the restrictive fallback. |
| F-018 | MINOR | D8 / deadzone | HEARTBEAT.md | Weekly | "**Tuesday**: Standard restaurant operations."; "**Thursday**: Standard restaurant operations." | Two Weekly entries were bare deadzones with no commitment rolled up. | DIRECT_FIX | Rebuilt Tuesday (supplier order, Emre soccer, Ayse/Zeynep coffee) and Thursday (halal delivery, weekend prep, spice restock, Emre soccer). |

**Checks run with no findings (recorded per §9):** A1 service-graph (every MEMORY > Connected Accounts entry maps to a TOOLS `-api` slug; Ring, Nest, Square, QuickBooks, Plaid all reconcile across TOOLS and MEMORY), A2 (no SOUL ↔ AGENTS value conflicts; both prohibit professional medical/legal/financial advice), A3 (TOOLS scopes the Anatolia website, online ordering, and BigCommerce merch surface without overreach into Wayne Family Dental or staff immigration systems), A4 (SOUL "5:30 AM over Turkish tea" matches HEARTBEAT 5:30 AM tea and MEMORY cay 6–8 glasses), A6 (Ayse routed as primary ICE matching wife tier; Hasan as designated best friend / after-hours backup), A7 (OpenClaw introduced atop IDENTITY with an eight-month tenure consistent with the anchor), B1 map (Age/DOB/timezone/location in USER > Basics only; one-sentence Background with full timeline in MEMORY > Work & Projects; threshold headline in USER > Access & Authority with full finance in MEMORY > Finance), B2/B3 (no duplicated negative assertions or scalar facts across files post-merge), C2 (age 47 correct; America/New_York with Paterson/North Haledon), C5 (continuous timeline: Marmara → kitchens → 2012 Main Street → 2021 Wayne, no gaps), C6 (Marmara University hospitality study stated as two years, not a completed degree — no fictional credential claim), D1 (Amazon Seller correctly seller-side for the spice blend; Twilio outbound to staff; Square/Stripe storefront/POS), D2 (all services US/NJ-available; US `(NNN) NNN-NNNN` format; Turkey contact in `+90` format; USD; ET), D4 (Turkish-American heritage consistent; Gaziantep origin, cuisine, music, tea, Galatasaray all aligned), D5 (no eligibility/licensure/fraud claims), E3 (no currency-conversion errors; lira context handled as rate-watching, never mixed notation).

---

## Section 2 — Coherence Score

```
Score: 9.4 / 10
Rubric:
  - Cross-file alignment:            1.9 / 2.0   (Mode A — graph fully reconciles post F-001/F-010/F-013;
                                                   small deduction for the cohort-internal @Finthesiss.ai
                                                   domain being applied from common-errors #25 rather than
                                                   persona-declared)
  - Overlapping / SoT compliance:    1.0 / 1.0   (Mode B — canonical placements correct post F-002 merge
                                                   and F-017 relocation; no duplicate scalar facts)
  - Required-field completeness:     1.0 / 1.0   (Mode C — inner-circle DOBs, escalation contacts, Data
                                                   Sharing enumeration, thresholds all present post F-003)
  - Factual & domain correctness:    1.8 / 2.0   (Mode D — strong NJ/Turkish localization; deduction for the
                                                   six fabricated brand names that required correction and the
                                                   555 placeholder phone block accepted as cohort convention)
  - Mathematical correctness:        1.0 / 1.0   (Mode E — income reconciles at ~$232,000, property nets
                                                   verify, ages/timeline hold, 101-slug gate passes,
                                                   birthday-to-DOB recurrence verified)
  - Heading-structure compliance:    1.7 / 2.0   (Mode F headings — all 7 files canonical post F-002;
                                                   deduction reflects the pre-remediation 12th MEMORY H2)
  - Format-structure compliance:     1.0 / 1.0   (Mode F caps/format — all caps met; regex and forbidden-
                                                   token sweeps clean; no .md leaks; no dashes; no deadzones)
                            Total:   9.4 / 10.0
```

---

## Section 3 — Remediation Log

| Finding ID | File(s) | Change Type | Before | After | Justification |
|---|---|---|---|---|---|
| F-001 | USER, AGENTS, HEARTBEAT, MEMORY, TOOLS | DIRECT_FIX | "Fulcrum Group" second location | "Wayne" location of Anatolia Kebab House | Template-leak proper noun replaced with a sensible NJ location aligned to the persona (Ayse works in Wayne). |
| F-002 | MEMORY | DIRECT_FIX | 12 H2s incl. `## Real Estate` | 11 canonical H2s; property folded into Work & Projects | F8 requires exactly 11 ordered H2s. |
| F-003 | MEMORY, HEARTBEAT | DIRECT_FIX | ages only; Annual had no birthdays | full DOBs added + propagated into Annual | C4/E7 require inner-circle DOBs and Annual propagation. |
| F-004 | HEARTBEAT | DIRECT_FIX | April 15 Annual tax + duplicate/misfiled birthdays | Annual Oct–Mar only; 12 forward-only Upcoming entries | Annual-window rule + forward-calendar instruction. |
| F-005 | TOOLS | DIRECT_FIX | ~30 read-only/inactive bullets | active persona-aligned uses | Every API must carry active, aligned use (common-errors #6/#7 + instruction). |
| F-006 | MEMORY (+TOOLS) | DIRECT_FIX | Luminar/Crestline/Ashdale/Ashvale/Herongate | Ford / Google Workspace / Netflix / TAPinto Paterson / Fidelity | D6 brand-name correctness. |
| F-007 | IDENTITY | DIRECT_FIX | declarative Principles bullets | `You ...` statements | common-errors #3 voice gate. |
| F-008 | IDENTITY | DIRECT_FIX | closer inside opening paragraph | standalone closer at file end | common-errors #21. |
| F-009 | SOUL, AGENTS | DIRECT_FIX | direct `MEMORY` references | "stored memory" / "the … record" | common-errors #5. |
| F-010 | AGENTS, MEMORY, TOOLS | DIRECT_FIX | `@Greenridertech.com` | `@Finthesiss.ai` | common-errors #25. |
| F-011 | MEMORY | DIRECT_FIX | $276,000 with $40k property + $18k catering | ~$232,000 with ~$14k net property | E4 arithmetic; removed double-count. |
| F-012 | MEMORY, HEARTBEAT | DIRECT_FIX | inspection due May 2026; payoff Sept 2026 | inspection ~Nov 2026; payoff end 2026 | E5/temporal consistency with anchor and Upcoming window. |
| F-013 | TOOLS, MEMORY | DIRECT_FIX | Plaid "read-only"; Herongate | "read aggregation"; Fidelity | A1 + brand correction reconciled across files. |
| F-014 | IDENTITY | DIRECT_FIX | "two Paterson restaurants" | "two restaurants in Paterson and Wayne" | Geographic alignment after F-001. |
| F-015 | TOOLS | DIRECT_FIX | "connected mock APIs" | "connected services listed above" | F6 implementation-leak removal. |
| F-016 | USER | DIRECT_FIX | unbolded Basics labels | bolded labels | common-errors #11. |
| F-017 | AGENTS | DIRECT_FIX | Emergency/Escalation under Data Sharing | moved to Safety & Escalation | B1 single-source-of-truth placement. |
| F-018 | HEARTBEAT | DIRECT_FIX | "Standard restaurant operations" Tue/Thu | rebuilt with real commitments | Deadzone-event removal instruction. |

---

## Section 4 — Open Questions for Human Input

None. Every defect surfaced in Phase 1 was remediable from existing persona context. Where new facts were synthesized — inner-circle DOBs, the Wayne location name, the corrected real brands, the October-2026 forward calendar, and the thin-but-active crypto/brokerage justifications — each was anchored to existing persona signal (stated relative ages, Ayse's Wayne workplace, VTI/SCHD holdings, Emre's age and learning context, Mehmet's Gaziantep remittance, the spice-blend craft) and verified for arithmetic, calendar, and cross-file consistency. No fact was invented without a persona-aligned source thread.

---

## Section 6 — Cross-Persona Pattern Flags

Conventions and defect classes observed here worth a cohort-wide sweep:

1. **Template-leak proper nouns** (F-001, F-006) — "Fulcrum Group," "Luminar Design Group," "Crestline Consulting," "Ashdale Technologies," "Ashvale," "Herongate Partners." These read as generated placeholders. Sweep the cohort for capitalized "[Word] Group / Technologies / Partners / Consulting" tokens used where a real consumer brand or location name belongs.
2. **Non-canonical `## Real Estate` H2 in MEMORY.md** (F-002) — any property-owning persona may carry the same extra section. Validate MEMORY H2s as an ordered list of exactly 11.
3. **Annual section containing April–September events and/or no birthdays** (F-003, F-004) — sweep every HEARTBEAT.md for Annual entries dated Apr–Sep and confirm inner-circle birthdays propagate from MEMORY DOBs.
4. **Passive "read-only / inactive / view only" TOOLS bullets** (F-005) — grep `read-only`, `view only`, `watch only`, `inactive`, `not in use`, `dormant` across all TOOLS.md and rewrite into active uses.
5. **Source-document email domain `@Greenridertech.*`** (F-010) — sweep for any non-`@Finthesiss.ai` / non-`@voissync.ai` domain and reconcile against common-errors #25.
6. **Finance double-counting business revenue as personal income** (F-011) — verify household-income lines do not re-add catering/business revenue already inside total restaurant revenue.

---

*End of report.*
