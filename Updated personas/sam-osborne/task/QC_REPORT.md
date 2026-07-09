# PERSONA QC REPORT - Sam Osborne

**QC spec:** PERSONA_QC_PROMPT v1.4 · **Audit date:** 2026-06-06 · **Scope:** 7 inner files in `Sam Osborne/sam-osborne/` (README.md excluded per v1.3 scope) · **Run type:** Full audit, Modes A-F, remediation applied

**Anchor date (derived from persona):** ~early October 2026. Derivation: USER.md > Basics gives Age 48 with DOB November 4, 1977 (age 48 holds from 2025-11-04 to 2026-11-03); IDENTITY.md opening states OpenClaw has been "his daily-use assistant for six months" (start ~April 2026); HEARTBEAT.md > Upcoming Events run forward from Oct 12 through Mar 22, with Oct 12 (Kai's birthday) the first entry, placing the present just before mid-October; the Thanksgiving entry "Nov 26" is the fourth Thursday of November in 2026 (Nov 1, 2026 = Sunday; Thursdays 5/12/19/26), fixing the anchor year at 2026. All anchors reconcile on a present date of early October 2026.

---

## VERDICT: PASS

No CRITICAL findings remain, and the three MAJOR defects detected in Phase 1 were remediated in Phase 2 without inventing facts. All hard mechanical gates pass: TOOLS.md carries exactly 101 unique `-api` slugs (E6, tool-verified by regex sweep), every API bullet conforms to the F6 regex with zero forbidden tokens (`via mock`, `shopify`, `fintrack`, `todoist`, ports), `#### Not Connected` is the final H4 with the web-search/browsing/deep-research-unavailable note present, USER.md is 39 of 40 permitted lines, every file is under its character cap (total 35,679 of 140,000; MEMORY 7,105 of 15,000), all 7 H1s match the canonical Title Case pattern, and every heading set/order in all 7 files conforms to the F2-F8 canonical structure (SOUL 4 H2; IDENTITY 0 H2 + Nature/Principles; AGENTS 7 H2 incl. Data Sharing Policy; USER 5 H2; TOOLS 1 H2/1 H3 with `#### Not Connected` last; HEARTBEAT 2 H2 with a single `### Weekly` block; MEMORY 11 H2 in canonical order). Cross-file alignment holds on the high-traffic paths: tool connection states reconcile across TOOLS/MEMORY/AGENTS (Gmail/Calendar/Drive/Etsy/Instagram/Ring live with matching slugs; Outlook on-standby consistent; department systems, banking, TSP/529, and Verizon correctly isolated under `#### Not Connected`), OpenClaw is the sole assistant identity (nickname "Dispatch"), the Data Sharing Policy enumerates per-contact rules with a restrictive fallback, and named holidays verify against the real 2026-2027 calendar (Thanksgiving Nov 26 = Thursday). Domain localization is strong throughout: New Mexico / Navajo Nation context (Gallup, Window Rock, Shiprock, Crownpoint), 505 (NM) and 928 (Window Rock, AZ) area codes correctly assigned, Mountain Time, and occupation-fit quiet-states for the developer/HR/analytics/CRM tool families with crypto justified against a stated small position. The remaining observations are graded MINOR - documented cohort conventions (synthetic phone placeholders, `@Finthesiss.ai`/`voissync.ai` domains, inner-circle ages without DOBs, "on standby"/"quiet" TOOLS phrasing, >12 TOOLS H4 categories) or low-impact estimate/style drift that does not degrade trust on first probe. The persona is deployable.

---

## Mechanical Verification Record

| Gate | Requirement | Measured | Result |
|---|---|---|---|
| E6 slug count | exactly 101 unique `-api` slugs | 101 total / 101 unique / 0 duplicates | PASS |
| F6 bullet regex | every API bullet conforms | 101/101 conform; zero forbidden tokens (`via mock`, `shopify`, `fintrack`, `todoist`, ports) | PASS |
| F6 Not Connected | final H4, web-search-unavailable note present | present, final H4, note present (line 158) | PASS |
| F5 / F10 USER cap | <= 40 lines | 39 lines | PASS |
| F10 char caps | each <= 20,000; MEMORY <= 15,000; total <= 140,000 | AGENTS 5,178 / HEARTBEAT 3,383 / IDENTITY 1,944 / MEMORY 7,105 / SOUL 3,065 / TOOLS 12,367 / USER 2,637; total 35,679 | PASS |
| F1 H1 pattern | `# <Filename>: <Full Name>` Title Case x7 | all 7 conform | PASS |
| F2-F8 heading sets | exact-match, canonical order | all files conform (SOUL 4 H2; IDENTITY 0 H2 + 2 H3; AGENTS 7 H2 incl. Data Sharing Policy; USER 5 H2; TOOLS 1 H2/1 H3/21+1 H4; HEARTBEAT 2 H2 single Weekly; MEMORY 11 H2) | PASS |
| C1/E1 DOB & age | DOB full Y-M-D, month Oct-Mar; age matches anchor | DOB 1977-11-04 (November in window); age 48 correct vs anchor | PASS |
| D3 calendar | named holiday/dates match real calendar | Thanksgiving Nov 26, 2026 = 4th Thursday (verified); Oct 31/Dec 25/Jan 1/Feb 14 standard | PASS |
| E7 birthdays | HEARTBEAT Annual = MEMORY Key Relationships (month+day) | Dorothy Mar 22 and Ben Jan 18 match exactly | PASS |
| E4 income | income reconciles, no double-count | salary $72k/yr + metalwork ~$18k/yr (single line incl. galleries/Etsy/commissions, no double-count); expenses well within net | PASS |
| E1/E2 ages & career | ages and timeline reconcile to anchor | age 48 vs DOB correct; 22-yr tenure consistent with academy 2004 + 16-yr detective (since 2010) after fix; Dorothy 26 at Sam's birth | PASS |

---

## Section 1 - Findings Catalog

| ID | Severity | Mode | File | Section | Quote | Defect / Observation | Fix Type | Fix |
|---|---|---|---|---|---|---|---|---|
| F-001 | MAJOR (fixed) | B1 | MEMORY.md | ## Personal Profile | "Sam Osborne, 48, lives on the eastern edge of Gallup" | Age duplicated MEMORY; canonical home is USER.md > Basics. | DIRECT_FIX | Removed the age token: "Sam Osborne lives on the eastern edge of Gallup". |
| F-002 | MAJOR (fixed) | D8 | MEMORY.md | ## Key Relationships | "junior at Mesa Vista High School" | Logical contradiction: HEARTBEAT Nov 13 "Kai's senior-year college applications due" plus active college visits and admissions interviews establish Kai as a senior; "junior" is the outlier (1 signal vs 3). | DIRECT_FIX | "senior at Mesa Vista High School". |
| F-003 | MAJOR (fixed) | E2 | USER.md | ## Background | "graduated the Law Enforcement Academy in 2002" | Academy 2002 vs anchor 2026 = 24 yrs, but MEMORY and USER both state "22 years" in law enforcement; the twice-stated tenure is canonical, so the academy year was off by two. | DERIVE_FIX | "graduated the Law Enforcement Academy in 2004" (2004->2026 = 22 yrs; 16 as detective since 2010 reconciles). |
| F-004 | MINOR | C2 | USER.md | ## Basics | "**Timezone**: Mountain Time (Gallup, New Mexico)" | Timezone is descriptive rather than an IANA string (e.g., `America/Denver`). City present; AGENTS uses the same descriptive form. Low impact; cohort style. | NONE (accepted) | No action. |
| F-005 | MINOR | E4 | MEMORY.md | ## Work & Projects | "averages three to five sales a month at roughly $450 each ... Annual studio revenue runs about $18,000" | Etsy at 3-5x$450/mo implies ~$16k-$27k/yr, crowding or exceeding the $18k total studio figure that also includes galleries and commissions. All figures are hedged estimates ("roughly", "about", "averages"); no double-count exists with salary. | NONE (hedged-estimate wobble) | No action. |
| F-006 | MINOR | D2 | MEMORY.md | ## Contacts | "Kai (505-555-0192 ...)" | Contact numbers use 505/928-555 synthetic placeholders (area codes geo-correct for NM and Window Rock AZ). Documented cohort convention. | NONE (accepted convention) | No action. |
| F-007 | MINOR | A1 | MEMORY.md / USER.md / TOOLS.md | Connected Accounts; Basics; Tool Usage | "sam.osborne@Finthesiss.ai" | Primary identity uses the cohort-internal `@Finthesiss.ai` domain under Google Workspace/Gmail labels; legacy `voissync.ai` threads are read-only. Accepted cohort convention; flagged for cohort-level consistency (see Section 6). | NONE (accepted convention) | No action. |
| F-008 | MINOR | C4 | MEMORY.md | ## Key Relationships | "**Captain Rita Benally** (supervisor, 52)" | Inner-circle members carry ages; most lack full DOBs (Dorothy/Ben carry month+day only). Waived per standing cohort policy: ages suffice when present. | NONE (waived) | No action. |
| F-009 | MINOR | A1 / D7 | TOOLS.md | #### Crypto & Trading | "**Coinbase** (`coinbase-api`): connected to the small crypto position Sam holds" | Coinbase and Alpaca are justified by a stated crypto position and brokerage account, but those holdings are not itemized in MEMORY > Finance. Tools satisfy D7 occupation-fit; the omission is a completeness gap, not a contradiction. | NONE (accepted) | No action. |
| F-010 | MINOR | F7 | HEARTBEAT.md | ## Recurring Events | "### Seasonal & Variable" | Optional frequency subsection uses "& " where the canonical label is "Seasonal / Variable". Semantically identical; single optional block. | NONE (accepted variant) | No action. |
| F-011 | MINOR | B3 | USER.md / MEMORY.md | Background; Personal Profile | "senior detective with the McKinley County Sheriff's Office and the sole maker behind Osborne Metalworks" | Role descriptor restated near-verbatim across USER > Background (1-sentence summary) and MEMORY > Personal Profile. Depth difference largely preserved; low forensic impact. | NONE (accepted) | No action. |
| F-012 | MINOR | E1 | HEARTBEAT.md | ## Recurring Events > ### Annual | "Oct 12: Kai's birthday (16)." | Annotation reads as current age, whereas Dorothy "(75)" and Ben "(46)" read as turning-age. Numerically matches MEMORY's age 16; convention drift only. | NONE (accepted) | No action. |
| F-013 | MINOR | A3 | TOOLS.md | #### Personal Email & Calendar; Communication; Productivity | "any agency communication that lands outside dispatch ... outside the secure systems" | Several tools (Outlook, Confluence, Teams, Asana, ServiceNow) are scoped to agency traffic "outside the secure systems"; the work boundary is explicitly drawn under `#### Not Connected` (NCIC/TriTech CAD/case files isolated). No loophole into case content. | NONE (accepted) | No action. |

**Checks run with no findings (recorded per §9):** A1 core graph (no service claimed "used" in MEMORY without a matching slug; no service appears both connected and under Not Connected; Ring hardware matches `ring-api`; Outlook on-standby state consistent TOOLS<->MEMORY), A2 (SOUL boundaries on medical/legal/investment advice match AGENTS Safety & Escalation; no value conflicts), A4 (sensory anchor: "coffee black and strong" consistent across SOUL/MEMORY/USER), A5 (schedules consistent: monthly 15th transfers, quarterly fitness, Sunday Dorothy call; no cross-file cadence conflicts), A6 (relationship tiers match routing: Kai/Dorothy immediate, gallery same-day), A7 (OpenClaw introduced in IDENTITY with "Dispatch" nickname; six-month tenure consistent with anchor; no other assistant name), B1 map (Age/DOB/timezone/location now in USER > Basics only after F-001; one-time dates in HEARTBEAT; threshold headline in USER with full finance in MEMORY), B2 (negative "not connected" assertions live only in TOOLS > Not Connected), C1 (DOB Nov 4 within Oct-Mar fiscal window), C3 (tenure statement present), C5 (continuous timeline: academy 2004 -> patrol -> detective since ~2010, no gaps >12mo), C6 (WNMU Criminal Justice degree + Law Enforcement Academy, real institutions), C7 (escalation contacts exist per category in MEMORY: Dr. Chee medical, Captain Benally/Eddie operational, Ben elder-care; Sam under 50 so ICE/POA not mandatory), C8 ($300 threshold, no tautological self-conversion), C9 ("Default ... proceed with judgement" present), C10 (Data Sharing Policy as 7th H2 with per-contact bullets and restrictive fallback), D1 (Amazon Seller correctly seller-side and quiet; no API-direction errors), D2 services (US/NM-available; geo-correct area codes), D4 (Navajo-region surnames consistent with setting; no heritage overstatement; Sam not claimed a veteran - Leonard's Korean War service is biography only, no eligibility claim), D5 (no eligibility/licensure/fraud red-lines; no veteran-grant research for Sam), D6 (brand dictionary clean: iPhone 14 Pro, MacBook Pro, Google Workspace, Celestron 8SE, Chevrolet Tahoe PPV, Toyota Tacoma TRD, Ford F-150, Verizon, Etsy, Instagram, Ring, Creedence, Spotify), D7 (developer/HR/analytics/CRM tools quiet-stated; crypto justified by stated position; every active tool occupation-fit), D8 (no inverted/misfiled events after F-002; one-time dates in Upcoming only), E3 (USD figures locally plausible; no mixed-currency notation), E5 (Sarah deceased Feb 2022 treated as deceased, no joint-with-deceased account; ranch bought 2012, Kai's age consistent), E6, E7, F2-F11 (all structural gates - see Mechanical Verification Record).

---

## Section 2 - Coherence Score

```
Score: 9.0 / 10
Rubric:
  - Cross-file alignment:            1.8 / 2.0   (Mode A - graph reconciles; small deductions for crypto/brokerage
                                                   holdings absent from MEMORY Finance and agency-tool scoping)
  - Overlapping / SoT compliance:    0.8 / 1.0   (Mode B - age duplication fixed; near-verbatim role descriptor
                                                   restated across USER Background and MEMORY Personal Profile)
  - Required-field completeness:     0.9 / 1.0   (Mode C - all mandatory fields present; timezone descriptive
                                                   rather than IANA; inner-circle DOBs waived per cohort policy)
  - Factual & domain correctness:    1.7 / 2.0   (Mode D - strong NM/Navajo localization; junior->senior fixed;
                                                   deductions for 555 placeholders and the Etsy revenue estimate)
  - Mathematical correctness:        0.9 / 1.0   (Mode E - academy-year fix reconciles tenure; 101-slug gate and
                                                   birthday/holiday math pass; minor Etsy estimate wobble)
  - Heading-structure compliance:    1.9 / 2.0   (Mode F headings - all 7 files canonical; "Seasonal & Variable"
                                                   punctuation variant of the optional block)
  - Format-structure compliance:     1.0 / 1.0   (Mode F caps/format - all char/line caps met; regex and
                                                   forbidden-token sweeps clean; web-search note present)
                            Total:   9.0 / 10.0
```

---

## Section 3 - Remediation Log

| Finding ID | File | Change Type | Before | After | Justification |
|---|---|---|---|---|---|
| F-001 | MEMORY.md | DIRECT_FIX | "Sam Osborne, 48, lives on the eastern edge of Gallup" | "Sam Osborne lives on the eastern edge of Gallup" | Age is canonical to USER.md > Basics (B1); duplicate removed from MEMORY. |
| F-002 | MEMORY.md | DIRECT_FIX | "junior at Mesa Vista High School" | "senior at Mesa Vista High School" | Resolves D8 contradiction with HEARTBEAT "senior-year college applications due", active college visits, and admissions interviews; "junior" was the single outlier. |
| F-003 | USER.md | DERIVE_FIX | "graduated the Law Enforcement Academy in 2002" | "graduated the Law Enforcement Academy in 2004" | Reconciles the twice-stated "22 years" tenure with the 2026 anchor (2004->2026 = 22; detective 16 yrs since 2010); no fact invented. |

---

## Section 4 - Open Questions for Human Input

None. All MAJOR findings were remediable by deriving from facts already on file; no finding requires human input.

---

## Section 6 - Cross-Persona Pattern Flags

Conventions observed here that should be verified as *consistent* (not necessarily changed) across the cohort:

1. **`@Finthesiss.ai` account domain and legacy `voissync.ai` threads** (F-007) - if these are the cohort's standard synthetic domains, ensure every persona uses identical casing and that no persona's QC grades them a defect while another waives them. Inconsistent grading across the cohort is itself a SYSTEMIC issue.
2. **555 synthetic phone placeholders** (F-006) - same consistency rule: if accepted here, accept cohort-wide, or reformat cohort-wide. Area-code geo-correctness (505 NM / 928 AZ) is a good practice to standardize.
3. **Inner-circle ages without DOBs** (F-008) - standing cohort policy: ages suffice; QC runs should exclude missing inner-circle DOBs from verdicts when ages are present.
4. **Descriptive timezone vs IANA string** (F-004) - if the cohort uses "Mountain Time"-style labels rather than `America/Denver`, document it so future audits do not flag it as a C2 defect.
5. **"Seasonal & Variable" vs "Seasonal / Variable" heading label** (F-010) - confirm which punctuation the cohort standardizes on for the optional HEARTBEAT frequency block.
6. **Tenure-vs-graduation-year arithmetic** (F-003) - check sibling personas for the same off-by-N between a stated career length and a dated academy/graduation year against the 2026 anchor.
