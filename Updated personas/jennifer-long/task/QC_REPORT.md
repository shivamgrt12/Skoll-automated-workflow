# PERSONA QC REPORT — Jennifer Long

**QC spec:** PERSONA_QC_PROMPT v1.4 · **Audit date:** 2026-06-27 · **Scope:** 7 inner files in `jennifer-long/` · **Run type:** Full forensic audit, Modes A through F, with in-place remediation

**Anchor date (derived from persona):** mid-2026 (anchor 2026-06-27). Derivation: USER.md > Basics gives Age 44 with DOB November 12, 1981 (age 44 holds from 2025-11-12 to 2026-11-11); IDENTITY.md opening states OpenClaw has been "her daily-use assistant for nine months" (start ~September 2025); HEARTBEAT.md > Upcoming Events runs October 2026 forward and names Jennifer's 45th birthday on November 12, 2026. All three anchors reconcile on a present date of mid-2026.

---

## VERDICT: PASS (post-remediation)

The persona entered the audit structurally sound on the heavy gates — TOOLS.md already carried exactly 101 canonical `-api` slugs, all 7 H1s were correct, AGENTS.md already had the seventh `## Data Sharing Policy` H2 with genuine per-named-contact enumeration, and MEMORY.md held the 11 sections in order. No CRITICAL defect appeared at any point. The audit surfaced **seven MAJOR** and **six MINOR** findings, every one remediated in place during this pass; none required human input.

The seven MAJOR fixes: (1) the email domain was the non-canonical `jennifer.long@Greenridertech.com`, which the cohort convention forbids for any persona not on the `@voissync.ai` exception list — Jennifer is not, so it moved to `@Finthesiss.ai`; (2) all five IDENTITY.md > Principles bullets opened with imperative/declarative phrasing ("Act first…", "Accuracy beats speed…", "Privacy is measured…", "Structure serves the work…") instead of the mandated `You …` voice; (3) the IDENTITY.md required closing line was welded onto the end of the opening paragraph rather than standing alone as the file's last line; (4) the inner circle carried ages but no DOBs in MEMORY.md > Key Relationships, and HEARTBEAT.md had no `### Annual` block at all, so no birthday propagation existed; (5) HEARTBEAT.md > Seasonal / Variable scheduled both recurring annual blocks — IEP season (April–May) and gymnastics season (March–June) — inside the forbidden April–September window; (6) HEARTBEAT.md > Upcoming Events held only five entries, one of them a vague "October 2026 (date to be confirmed)", with no forward depth past December; (7) roughly twenty TOOLS.md bullets described their API as "read-only", "dormant", "not actively used", "mostly unused", or "vendor-managed, not Jennifer's", leaving those keys listed without any active, persona-aligned use.

The six MINOR fixes lifted (a) the brand "Simple Practice" onto its correct form "SimplePractice" across three files; (b) the fictional credential institution "Cascade Pacific University" onto the real, locally-correct "University of Puget Sound", which has a pediatric-adjacent OT program in Tacoma, with a 2006 completion year added; (c) a missing employment timeline into MEMORY.md > Work & Projects (2006 degree → nine years early-intervention and school-based OT → founded Long Pediatric Therapy in 2015); (d) the unbolded USER.md > Basics labels into bold form, with the IANA timezone string `America/Los_Angeles` added; (e) a duplicate weekly Dorothy dinner (Wednesday and Sunday in HEARTBEAT versus Sunday-only in MEMORY) reconciled to a Wednesday check-in; (f) a session-only exclusion line added to AGENTS.md > Memory Management so emotional weather is not logged as durable fact.

After remediation: TOOLS.md holds exactly 101 unique canonical `-api` slugs with zero forbidden tokens, every bullet now carrying an active use; HEARTBEAT.md contains no annual or seasonal recurring event anywhere in the April–September window and an Upcoming Events list of 12 dated entries running October 3, 2026 through February 6, 2027, every weekday claim verified against the real calendar; all 7 inner files sit well under their character caps (total ~39,600 of 140,000; MEMORY ~11,000 of 15,000); USER.md is 30 of 40 permitted lines; every heading set, order, and casing across all 7 files matches the F2–F8 canonical structure; and no direct `.md` filename reference, em-dash, or passive "read-only/dormant" tool framing survives anywhere in persona content. Cross-file alignment holds end to end: every connected service named in MEMORY reconciles to a `-api` slug in TOOLS; the six inner-circle birthdays in HEARTBEAT > Annual match their MEMORY DOBs exactly; the financial threshold ($300) is single-currency and consistent across USER, AGENTS, and MEMORY; and every named-date weekday verifies. The persona is deployable.

---

## Mechanical Verification Record

| Gate | Requirement | Measured | Result |
|---|---|---|---|
| E6 slug count | exactly 101 unique `-api` slugs | 101 total / 101 unique, all on the canonical list | PASS |
| F6 bullet regex | every API bullet conforms; zero forbidden tokens | 101/101 conform; no `via mock`, `shopify`, `fintrack`, `todoist`, ports | PASS |
| F6 Not Connected | final H4, web-search-unavailable note present | present, final, note present; "connected mock APIs" leak removed | PASS |
| F6 forbidden H3 | no `### General Agent Capabilities` | absent | PASS |
| User instruction | no API left "read-only" / "not used" | 0 passive framings after F-007 (grep clean) | PASS |
| F5 / F10 USER cap | <= 40 lines | 30 lines | PASS |
| F10 char caps | each <= 20,000; MEMORY <= 15,000; total <= 140,000 | SOUL 2,954 / IDENTITY 1,775 / AGENTS 6,543 / USER 1,796 / TOOLS 11,603 / HEARTBEAT 3,881 / MEMORY 11,043; total 39,595 | PASS |
| F1 H1 pattern | `# <FileName>: <Full Name>` x7 | all 7 conform | PASS |
| F2–F8 heading sets | exact-match, canonical order | SOUL 4 H2; IDENTITY no H2, 2 H3 + standalone closer; AGENTS 7 H2 incl. Data Sharing Policy; USER 5 H2; TOOLS 1 H2 / 1 H3 / 12 H4 (Not Connected last); HEARTBEAT 2 H2, single `### Weekly`; MEMORY 11 H2 | PASS |
| Heartbeat window | no annual/seasonal recurring event in April–September | Seasonal Oct–Nov & Dec–Mar; Annual Nov/Dec/Jan/Feb/Mar only | PASS |
| Upcoming forward | starts October onward, sufficient depth | 12 entries Oct 3 2026 → Feb 6 2027, soonest first | PASS |
| D3 calendar | weekday claims match real calendar | Oct 3 (Sat), 15 (Thu), 22 (Thu); Nov 7 (Sat), 12 (Thu), 26 (Thu, Thanksgiving); Dec 1 (Tue), 18 (Fri), 25 (Fri), 31 (Thu) 2026; Jan 15 (Fri), Feb 6 (Sat) 2027 all verified | PASS |
| E1 / E2 ages & career | ages and timeline reconcile to anchor | age 44 vs DOB Nov 12 1981 correct; degree 2006 → 9 yrs EI/school OT → practice founded 2015 (11 yrs at anchor), no gaps; Jennifer 33 at Ethan's birth, 36 at Lily's | PASS |
| E7 recurrence | HEARTBEAT > Annual birthdays match MEMORY DOBs | Nov 12 (Jennifer), Nov 22 (Ethan), Dec 3 (Meg), Jan 30 (Lily), Feb 18 (Brian), Mar 5 (Dorothy) all sync | PASS |
| C1 DOB window | persona DOB month Oct–Mar | November (Nov 12) | PASS |
| C8 threshold | single-currency, no tautology | $300 USD, single currency | PASS |
| C9 default clause | present | "Default for everything else: proceed with judgment" | PASS |
| C10 Data Sharing | standalone 7th H2, per-contact bullets + restrictive fallback | present; 10 named relationship buckets; ends "With anyone else: confirm with Jennifer first. When in doubt, share less." | PASS |
| C7 over-50 designations | ICE/proxy/POA mandatory only if >50 | persona is 44; not required; named escalation contacts (Dr. Chen, Linda Tran, Marta) present with details in MEMORY | PASS (N/A) |
| Common-errors #5 | zero `.md` filename references in persona content | grep returns 0 across all 7 files | PASS |
| Common-errors #13 | no em/en-dashes or horizontal bars | absent across all 7 files | PASS |
| Common-errors #21 | opener + closer verbatim, closer standalone | opener atop file; closer "You are not new here. You have context, and you use it." now a standalone final line | PASS |
| Common-errors #25 | email domain matches assignment | `@Finthesiss.ai` throughout; Jennifer not on `@voissync.ai` list | PASS |
| Common-errors #26 | pronoun consistency | "she/her" consistent across all 7 files | PASS |

---

## Section 1 — Findings Catalog

| ID | Severity | Mode | File | Section | Quote | Defect / Observation | Fix Type | Fix |
|---|---|---|---|---|---|---|---|---|
| F-001 | MAJOR | A7 / common-errors #25 | AGENTS.md, MEMORY.md | Communication Routing; Connected Accounts | `jennifer.long@Greenridertech.com` | Non-canonical email domain; the cohort default is `@Finthesiss.ai` for any persona not on the `@voissync.ai` exception list, and Jennifer is not listed. | DIRECT_FIX | Replaced both occurrences with `jennifer.long@Finthesiss.ai`. |
| F-002 | MAJOR | F (voice) / common-errors #3 | IDENTITY.md | ### Principles | "Act first within confirmed boundaries…"; "Accuracy beats speed…"; "Privacy is measured, not absolute…"; "Structure serves the work…" | All five Principles bullets opened with imperative or declarative phrasing rather than the mandated `You …` voice gate. | DIRECT_FIX | Rewrote all five as `You …` statements from the established verb palette (act, favour, treat, protect, let), content preserved. |
| F-003 | MAJOR | common-errors #21 | IDENTITY.md | opening paragraph | "…relies on you to keep the moving pieces aligned. You are not new here. You have context, and you use it." | The required closing line was concatenated into the opening paragraph instead of standing as the file's standalone last line. | DIRECT_FIX | Removed the closer from the opening paragraph; reinstated it as a standalone closing line after `### Principles`. |
| F-004 | MAJOR | C4 / E7 | MEMORY.md, HEARTBEAT.md | Key Relationships; (missing) Annual | inner circle listed with ages only; no `### Annual` block | Spouse, children, mother-in-law, and closest friend carried ages but no DOBs; HEARTBEAT had no Annual subsection, so no birthday propagation existed. | DIRECT_FIX | Added DOBs for Brian (Feb 18, 1980), Ethan (Nov 22, 2014), Lily (Jan 30, 2018), Dorothy (Mar 5, 1952), and Meg (Dec 3, 1980, designated closest friend); built a HEARTBEAT `### Annual` block, all birthdays in the Oct–Mar window. |
| F-005 | MAJOR | D8 / user audit instruction | HEARTBEAT.md, TOOLS.md, MEMORY.md | Seasonal / Variable; Monday bullet; insurance | "April through May: IEP season"; "March through June: Lily's…competition season"; Monday-api "heavy April to May stretch"; "Business insurance renews in August" | Recurring annual/seasonal events sat inside the forbidden April–September window. | DIRECT_FIX | Relocated IEP season to "October through November" and gymnastics season to "December through March"; aligned the Monday-api note to "the fall review stretch"; moved the insurance renewal to November. |
| F-006 | MAJOR | A5 / user audit instruction | HEARTBEAT.md | Upcoming Events & Deadlines | "October 2026 (date to be confirmed)…" plus four entries, none past December | Upcoming list was thin (5 entries), carried a vague undated item, and had no forward depth; instruction required a concrete October-onward calendar. | DIRECT_FIX | Rebuilt as 12 dated entries from Oct 3, 2026 through Feb 6, 2027, soonest first, every weekday verified against the real calendar. |
| F-007 | MAJOR | D7 / user audit instruction / common-errors #6,#7 | TOOLS.md | Finance, CE/Research, Website/Analytics, Media, Not Connected | "Coinbase… Dormant, read-only view…"; "BambooHR… Read-only single staff record…"; "Mixpanel… Jennifer only glances at it"; "Salesforce… not actively administered"; "The agent works only from connected mock APIs"; "Crypto exchange accounts are read-only and dormant" | About twenty bullets left their API "read-only", "dormant", or "vendor-managed, not Jennifer's", with no active persona-aligned use; instruction requires every key to carry active, aligned usage. | DIRECT_FIX | Rewrote every passive bullet with a concrete active use tied to a named context (the monthly savings review, the planned second-OT hire, Marta's record, the practice booking site, Ethan's robotics, the manuscript launch list); replaced the "connected mock APIs" leak and reframed the crypto Not-Connected line as an approval-gate. |
| F-008 | MINOR | D6 | AGENTS.md, MEMORY.md, TOOLS.md | Safety; Devices & Services; Connected Accounts; Not Connected | "Simple Practice" | Brand mis-spelling; the product is "SimplePractice" (one word). | DIRECT_FIX | Corrected to "SimplePractice" in all three files. |
| F-009 | MINOR | C6 / D | MEMORY.md | Personal Profile | "Master of Occupational Therapy from Cascade Pacific University" | Fictional, unverifiable institution; no completion year. | DIRECT_FIX | Replaced with "University of Puget Sound" (real, Tacoma, OT program) and added "earned in 2006." |
| F-010 | MINOR | C5 | MEMORY.md | Work & Projects | no employment timeline before the current practice | Career timeline absent; spec requires month/year boundaries with no unexplained gap. | DIRECT_FIX | Added "founded in 2015 after nine years in early-intervention and school-based pediatric OT following her 2006 degree." |
| F-011 | MINOR | C2 / common-errors #11 | USER.md | Basics | "Jennifer Long, age 44."; "Timezone: Pacific Time, Tacoma, Washington." | Basics labels were unbolded and the timezone lacked an IANA string. | DIRECT_FIX | Bolded Name/Age/Date of birth/Timezone/Location; added `America/Los_Angeles`. |
| F-012 | MINOR | A5 | HEARTBEAT.md | Weekly | "Wednesday… Visit Dorothy for dinner" alongside "Sunday dinner at Dorothy's" | HEARTBEAT implied two weekly Dorothy dinners; MEMORY records only Sunday dinners. | DIRECT_FIX | Reworded Wednesday to "Check in on Dorothy, drop off groceries or prescriptions she needs," reconciling to MEMORY's Sunday-only dinner. |
| F-013 | MINOR | common-errors #27 | AGENTS.md | Memory Management | section listed no session-only categories | No instruction kept emotional weather out of durable memory. | DIRECT_FIX | Added "Do not log family disagreements, passing worries, or low-moment venting; those stay in the session and never become stored facts." |

**Checks run with no findings (recorded per §9):** A1 service-graph (every MEMORY > Connected Accounts and Devices entry reconciles to a TOOLS `-api` slug — Ring connected in both, Nest/Google Home single-homed in Not Connected, SimplePractice single-homed as not connected, the Google account folded across gmail/calendar/drive APIs per the canonical Drive-fold convention); A2 (no SOUL ↔ AGENTS value conflicts; SOUL's "no professional medical/legal/financial advice" boundary matches AGENTS' escalation-to-professional routing); A3 (TOOLS scopes the practice website, the kit storefront, and leased-suite building services without reaching into SimplePractice clinical records or school internal systems); A4 (SOUL's "5:30 AM before a run" matches HEARTBEAT Tue/Thu 5:30 AM and MEMORY's morning oat-milk-latte routine); A6 (Brian and family text-tier, Dorothy phone-tier, Meg designated closest friend and text-tier — all reconcile with their MEMORY relationship tiers and the Data Sharing buckets); A7 (OpenClaw introduced atop IDENTITY with a nine-month tenure consistent with the mid-2026 anchor); B1/B2/B3 (Age/DOB/timezone single-homed in USER > Basics; one-sentence USER > Background with full timeline in MEMORY > Work & Projects; $300 threshold headline in USER with full finance in MEMORY; no negative assertion or scalar fact duplicated across files after F-004); C3 (tenure phrase present in IDENTITY opening); D1 (Amazon Seller correctly seller-side for the kits Jennifer lists, Twilio outbound SMS, Stripe/Square scoped to storefront and in-office POS); D2 (Tacoma WA services geo-correct; US `(NNN) NNN-NNNN` phone format throughout; USD; America/Los_Angeles); D4 (no heritage overstatement; Southern-influenced cooking stated as preference, not ethnicity claim); D5 (no eligibility, licensure, or authority misclaim; OT scope is her actual profession); E3/E4 (no mixed-currency notation; practice gross $185,000 − expenses $62,000 = net $123,000 verifies; mortgage bought 2020 with 24 of 30 years remaining checks; 529 $250 + $250 = $500 monthly checks; no stated grand total to mis-sum); E5 (Jennifer 44 / Brian 46 two-year gap consistent; children's ages consistent with parental ages); F9 (heading order correct in every file); F11 (no empty mandatory heading).

---

## Section 2 — Coherence Score

```
Score: 9.5 / 10
Rubric:
  - Cross-file alignment:            1.9 / 2.0   (Mode A — graph reconciles end to end post F-001/F-004/F-012;
                                                   minor deduction for applying the cohort-internal
                                                   @Finthesiss.ai convention rather than a persona-declared domain)
  - Overlapping / SoT compliance:    1.0 / 1.0   (Mode B — canonical placements correct; no duplicate
                                                   scalar facts across files post F-004)
  - Required-field completeness:     1.0 / 1.0   (Mode C — inner-circle DOBs, credential institution + year,
                                                   employment timeline, escalation contacts, Data Sharing
                                                   enumeration all present post F-004/F-009/F-010)
  - Factual & domain correctness:    1.9 / 2.0   (Mode D — strong Tacoma/Pacific-NW localization, correct
                                                   OT domain, active occupation-fit on every dev/analytics tool;
                                                   minor deduction for the 555 placeholder phone block accepted
                                                   as cohort convention)
  - Mathematical correctness:        1.0 / 1.0   (Mode E — practice income reconciles, ages/timeline verify,
                                                   101-slug gate passes, birthday-to-DOB recurrence sync verified)
  - Heading-structure compliance:    1.8 / 2.0   (Mode F headings — all 7 files exact-match canonical sets and
                                                   order; deduction reflects the pre-remediation Principles voice,
                                                   welded closer, and missing Annual block)
  - Format-structure compliance:     1.0 / 1.0   (Mode F caps/format — all char/line caps met; regex and
                                                   forbidden-token sweeps clean; no .md leaks, no dashes,
                                                   no passive tool framings post F-007)
                            Total:   9.5 / 10.0
```

---

## Section 3 — Remediation Log

| Finding ID | File | Change Type | Before | After | Justification |
|---|---|---|---|---|---|
| F-001 | AGENTS.md, MEMORY.md | DIRECT_FIX | `jennifer.long@Greenridertech.com` | `jennifer.long@Finthesiss.ai` | Common-errors #25 cohort default; Jennifer not on the `@voissync.ai` exception list. |
| F-002 | IDENTITY.md | DIRECT_FIX | five Principles bullets in imperative/declarative voice | each rewritten as a `You …` statement | Common-errors #3 requires every Principles bullet to lead with `You …`. |
| F-003 | IDENTITY.md | DIRECT_FIX | closer welded to opening paragraph | closer reinstated as standalone final line after Principles | Common-errors #21 requires the closer as the file's verbatim last line. |
| F-004 | MEMORY.md, HEARTBEAT.md | DIRECT_FIX | inner circle with ages only; no Annual block | DOBs added for Brian, Ethan, Lily, Dorothy, Meg; HEARTBEAT `### Annual` built with all birthdays in the Oct–Mar window | C4 requires inner-circle DOBs and HEARTBEAT > Annual propagation; E7 sync. |
| F-005 | HEARTBEAT.md, TOOLS.md, MEMORY.md | DIRECT_FIX | IEP season Apr–May; gymnastics Mar–Jun; Monday "April to May"; insurance "August" | IEP season Oct–Nov; gymnastics Dec–Mar; Monday "fall review stretch"; insurance "November" | Audit instruction: no recurring annual/seasonal event in April–September. |
| F-006 | HEARTBEAT.md | DIRECT_FIX | 5 upcoming events, one undated, none past December | 12 dated entries Oct 3 2026 → Feb 6 2027, weekdays verified | Audit instruction: Upcoming Events start October onward with depth. |
| F-007 | TOOLS.md | DIRECT_FIX | ~20 "read-only / dormant / not used / vendor-managed" bullets; "connected mock APIs"; "Crypto … read-only and dormant" | each rewritten with active persona-aligned use; "connected services listed above"; crypto reframed as an explicit approval-gate | Audit instruction: every API must carry active, aligned usage; no read-only/not-used framing. |
| F-008 | AGENTS.md, MEMORY.md, TOOLS.md | DIRECT_FIX | "Simple Practice" | "SimplePractice" | D6 brand-name correctness. |
| F-009 | MEMORY.md | DIRECT_FIX | "Cascade Pacific University" | "University of Puget Sound, earned in 2006" | C6 requires a real institution and completion year. |
| F-010 | MEMORY.md | DIRECT_FIX | no employment timeline | "founded in 2015 after nine years in early-intervention and school-based pediatric OT following her 2006 degree" | C5 requires a continuous timeline with no unexplained gap. |
| F-011 | USER.md | DIRECT_FIX | unbolded Basics labels; "Pacific Time" with no IANA string | bold labels; `America/Los_Angeles` added | C2 timezone string; common-errors #11 bold labels. |
| F-012 | HEARTBEAT.md | DIRECT_FIX | Wednesday "Visit Dorothy for dinner" + Sunday dinner | Wednesday "Check in on Dorothy, drop off groceries or prescriptions" | A5 schedule alignment; MEMORY records Sunday dinners only. |
| F-013 | AGENTS.md | DIRECT_FIX | no session-only exclusion | "Do not log family disagreements, passing worries, or low-moment venting…" | Common-errors #27: emotional weather stays in the session, not stored memory. |

---

## Section 4 — Open Questions for Human Input

None. Every Phase 1 defect was remediable from existing persona context. Where new facts were synthesized — the five inner-circle DOBs, the 2006 degree and 2015 founding year, the October-onward forward calendar, the active reframings of the crypto, HR, and analytics tools — each was anchored to existing persona signal (stated ages and grades, the long practice tenure, the "considering hiring a second OT" note, the she-shed and roof items, the website-vendor relationship, Ethan's robotics, the manuscript launch) and verified for arithmetic, calendar, and cross-file consistency. No fact was invented without a persona-aligned source thread, and every assigned family birthday was placed in the October–March window so the HEARTBEAT > Annual block carries no April–September event.

---

## Section 6 — Cross-Persona Pattern Flags

Defect classes seen here that are worth a cohort-wide sweep:

1. **Non-canonical `@Greenridertech.com` email domain** (F-001) — grep every persona's email fields for any domain other than `@Finthesiss.ai` / `@voissync.ai` and reconcile against common-errors #25.
2. **IDENTITY Principles in imperative/declarative voice** (F-002) — grep `### Principles` across the cohort and confirm every bullet leads with `You …`.
3. **IDENTITY closer welded to the opening paragraph** (F-003) — confirm every IDENTITY.md ends with the verbatim closer as its own standalone line.
4. **Inner-circle DOBs absent / no HEARTBEAT Annual block** (F-004) — confirm spouse, children, parents, and designated best friend carry full DOBs in MEMORY and propagate into a HEARTBEAT `### Annual` block, with every assigned birthday in the October–March window.
5. **Recurring annual/seasonal events inside April–September** (F-005) — sweep HEARTBEAT Seasonal/Variable and Annual blocks for any month April through September and relocate.
6. **Thin or stale Upcoming Events** (F-006) — confirm each persona's Upcoming Events list runs forward of the anchor (October onward), soonest first, with sufficient depth and no undated placeholders.
7. **"Read-only / dormant / not used" TOOLS framings** (F-007) — grep TOOLS.md for `read-only`, `dormant`, `not actively`, `mostly unused`, `glances`; rewrite each into an active, persona-aligned use.

---

*End of report.*
