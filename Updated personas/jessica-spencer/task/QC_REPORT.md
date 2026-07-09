# PERSONA QC REPORT — Jessica Spencer

**QC spec:** PERSONA_QC_PROMPT v1.4 · **Audit date:** 2026-06-27 · **Scope:** 7 inner files in `jessica-spencer/` · **Run type:** Full forensic audit, Modes A through F, with in-place remediation · **Reference catalog:** `common-errors.md`

**Anchor date (derived from persona):** 2026-06-27. Derivation: IDENTITY.md opening states OpenClaw "has been her daily-use assistant for ten months" (tenure since ~August 2025); USER.md > Basics gives Age 43 with DOB December 8, 1982 (age 43 holds from 2025-12-08 to 2026-12-07); HEARTBEAT.md > Upcoming Events & Deadlines now runs October 3, 2026 forward and references Jessica's 44th birthday on December 8, 2026. All three anchors reconcile on a present date of mid-2026.

---

## VERDICT: PASS (post-remediation)

Jessica Spencer clears the v1.4 gate with zero CRITICAL findings remaining. The audit opened ten actionable findings against the user-issued audit instruction set (no read-only tools, no April–September annual events, October-forward upcoming calendar, no deadzone events, no `.md` leakage, natural register in the narrative files) plus the standing common-errors catalog. All ten were remediated in place. The headline corrections were: (1) **24 TOOLS.md bullets** carried "read-only," "dormant," "vendor-managed," "no trading authorization," "observer access," or "mostly read" framings that left the API listed without an active, persona-aligned use — every one was rewritten to a concrete active use anchored to a named project, the studio website and client portal, the firm's staff, or the household money review; (2) **three HEARTBEAT.md > Annual events fell inside the forbidden April–September window** (July dermatologist, September ASID renewal) and were reassigned to October–March anchors, with a fourth annual physical added in February; (3) **HEARTBEAT.md > Upcoming Events & Deadlines** carried six entries — four of them vague "(date to be confirmed)" deadzone items and one dated September 2027 — and was rebuilt as twelve concrete, calendar-verified entries running October 9, 2026 through February 18, 2027; (4) the **email domain** `jessica.spencer@Greenridertech.com` was reconciled to the cohort default `jessica.spencer@Finthesiss.ai` per common-errors #25 (Jessica is not on the `@voissync.ai` exception list); (5) **IDENTITY.md > Principles** opened all five bullets with declarative-plus-imperative phrasings ("Act first…", "Accuracy beats speed…", "Privacy is measured…", "Taste is a discipline…", "Stewardship guides judgment…") in violation of the common-errors #3 `You …` voice gate, and were rewritten to lead with `You …`. No direct `.md` filename references survive in any of the seven persona files, and the narrative files (IDENTITY, SOUL, USER, MEMORY, HEARTBEAT, TOOLS) read as natural prose rather than instruction sheets, with the operating-instruction register confined to AGENTS.md as intended.

After remediation: TOOLS.md carries exactly **101 unique `-api` slugs** with zero duplicates (E6, verified by category sweep) and every bullet matches the canonical regex; USER.md is **29 of 40** permitted lines; every file sits under its character cap (MEMORY 10,735 of 15,000; largest is TOOLS at 10,943 of 20,000; **total 37,727 of 140,000**); all seven H1s match `# <FileName>: <Full Name>`; and every heading set and order conforms to F2–F8. Cross-file alignment holds end to end: the four crypto/brokerage tools (Coinbase, Binance, Kraken, Alpaca) now reconcile with a newly stated $20,000 brokerage-and-crypto holding in MEMORY > Finance; the Greenhouse hiring tool reconciles with a newly stated junior-designer hire plan in MEMORY > Work & Projects; the Ring API reconciles with a Ring doorbell-and-cameras line added to MEMORY > Home & Living; and the developer/IT and analytics tools each carry an occupation-fit use tied to the contractor-built studio site and client portal. Domain localization is correct throughout (Scottsdale/Arizona Time with no DST, USD, US `(NNN) NNN-NNNN` phone formats, Arizona-appropriate services). The persona is deployable.

---

## Mechanical Verification Record

| Gate | Requirement | Measured | Result |
|---|---|---|---|
| E6 slug count | exactly 101 unique `-api` slugs | 101 total / 101 unique, 0 duplicates | PASS |
| F6 bullet regex | every API bullet conforms to the canonical pattern | 101/101 conform | PASS |
| Forbidden tokens | no `via mock`, `shopify`, `fintrack`, `todoist`, port numbers | zero matches | PASS |
| User instruction — active tools | no `read-only` / `dormant` / `not in use` / `no trading` framings | zero matches across all 7 files | PASS |
| F6 Not Connected | final H4, web-search-unavailable note present, no implementation leak | present, final; "connected services listed above" phrasing | PASS |
| F6 forbidden H3 | no `### General Agent Capabilities` | absent | PASS |
| F5 / F10 USER cap | ≤ 40 lines | 29 lines | PASS |
| F10 char caps | each ≤ 20,000; MEMORY ≤ 15,000; total ≤ 140,000 | SOUL 2,958 / IDENTITY 1,710 / AGENTS 6,191 / USER 1,859 / TOOLS 10,943 / HEARTBEAT 3,331 / MEMORY 10,735; total 37,727 | PASS |
| F1 H1 pattern | `# <FileName>: <Full Name>` ×7 | all 7 conform | PASS |
| F2–F8 heading sets | exact-match, canonical order | SOUL 4 H2s; IDENTITY no H2 / 2 H3s with standalone closer; AGENTS 7 H2s ending in `## Data Sharing Policy`; USER 5 H2s; TOOLS 1 H2 / 1 H3 / 12 H4 categories + `#### Not Connected` last; HEARTBEAT 2 H2s, single `### Weekly`; MEMORY 11 H2s | PASS |
| User instruction — Annual window | no HEARTBEAT > Annual event in April–September | October, November, January, February only | PASS |
| User instruction — Upcoming forward | Upcoming Events start October onward, no deadzone/TBD | 12 entries Oct 9 2026 → Feb 18 2027, all concrete | PASS |
| D3 calendar | weekday claims match the real calendar | Oct 9 (Fri), 16 (Fri), 24 (Sat), 31 (Sat, last Saturday → dinner party); Nov 13 (Fri), 26 (Thu, 4th Thursday → Thanksgiving); Dec 5 (Sat), 8 (Tue, birthday), 25 (Fri); Jan 15 2027 (Fri); Feb 12 (Fri), 18 (Thu) all verified | PASS |
| Common-errors #5 | zero direct `.md` filename references in persona content | 0 across all 7 files | PASS |
| Common-errors #13 | no em-dashes, en-dashes, horizontal bars | absent across all 7 files | PASS |
| Common-errors #21 | IDENTITY opener and closer verbatim | opener atop file; closer "You are not new here. You have context, and you use it." standalone | PASS |
| Common-errors #25 | email domain matches assignment | `@Finthesiss.ai` only; not on `@voissync.ai` list | PASS |
| Common-errors #26 | pronoun consistency | she/her consistent across all 7 files | PASS |
| C1 DOB window | persona DOB month in Oct–Mar | December (Dec 8) | PASS |
| C8 threshold | Confirmation Rules opens with single-currency threshold, no tautology | $500 USD, no self-conversion | PASS |
| C9 default clause | proceed-with-judgment / ask-first present | "Default for everything else: proceed with judgment." | PASS |
| C10 Data Sharing | standalone `## Data Sharing Policy` 7th H2, per-contact + restrictive fallback | present, 10 named buckets, "With anyone else: confirm with Jessica first. When in doubt, share less." | PASS |
| E1 age math | age vs DOB vs anchor | 43 vs DOB Dec 8 1982 at 2026-06-27 anchor: correct | PASS |
| A1 service graph | every MEMORY connected service maps to a TOOLS slug; routing references declared states | Gmail/Calendar/Drive, Plaid→Chase, Ring, crypto/brokerage all reconcile post F-003/F-006/F-007 | PASS |

---

## Section 1 — Findings Catalog

| ID | Severity | Mode | File | Section | Quote | Defect / Observation | Fix Type | Fix |
|---|---|---|---|---|---|---|---|---|
| F-001 | MAJOR | D7 / user-issued audit instruction | TOOLS.md | Finance & Payments; Website Analytics; Developer & IT; Staff & Operations; Photography/Media; Home, Travel & Local | `Plaid: "Read-only link…"`, `Coinbase/Binance/Kraken/Alpaca: "Read-only…no trading authorization…dormant"`, `Mixpanel/Segment/Amplitude/PostHog: "Read-only…vendor-managed"`, `GitHub/GitLab/Kubernetes/Datadog/Sentry/Cloudflare/PagerDuty/Okta/ServiceNow: "Read-only…"`, `BambooHR/Greenhouse: "Read-only…dormant"`, `Twitter: "mostly read"`, `Twitch: "Observer access"`, `Google Classroom: "Read-only peek"` | 24 bullets used passive "read-only / dormant / vendor-managed / no trading / observer / mostly read" framings, leaving the API listed with no active, persona-aligned use. The audit instruction forbids read-only or not-used tool descriptions. | DIRECT_FIX | Rewrote all 24 bullets into active uses tied to a named project, the studio site/client portal, the firm staff, or the monthly household-money review. No slug changed; count stays 101. |
| F-002 | MAJOR | A5 / D8 / user-issued audit instruction | HEARTBEAT.md | Annual | `**July**: Dermatologist skin check…` and `**September**: ASID membership renewal.` | Two of three Annual recurring events fell in the forbidden April–September window. | DIRECT_FIX | Reassigned ASID renewal to October and the dermatologist check to a January winter visit; added a February annual physical. Annual section now reads October, November, January, February only. |
| F-003 | MAJOR | A5 / D8 / user-issued audit instruction | HEARTBEAT.md | Upcoming Events & Deadlines | `**November 2026 (date to be confirmed)**…`; `**January 2027 (date to be confirmed)**…`; `**February 2027 (date to be confirmed)**…`; `**September 2027 (date to be confirmed)**: ASID membership renewal` | Six upcoming entries — four vague "(date to be confirmed)" deadzone items plus one dated September 2027 — failed the "October onward, concrete, no deadzone" instruction. | DIRECT_FIX | Replaced with 12 concrete, calendar-verified entries from October 9, 2026 through February 18, 2027, every weekday claim checked against the real 2026–2027 calendar. |
| F-004 | MAJOR | A1 / D7 | MEMORY.md, TOOLS.md | Finance; Finance & Payments | crypto/brokerage tools with no matching household holding | After F-001 reframed Coinbase/Binance/Kraken/Alpaca as active, MEMORY > Finance held no holding for them to track, breaking A1 graph consistency for a non-trader persona. | DIRECT_FIX | Added a stated "$20,000 brokerage and crypto holding, mostly Kevin's" to MEMORY > Finance, reviewed at the monthly finance pass; the four tools now reconcile to a real persona fact. |
| F-005 | MINOR | A1 / D7 | MEMORY.md, TOOLS.md | Work & Projects; Staff & Operations | Greenhouse reframed as an active hiring pipeline with no stated hire plan | Greenhouse needed a persona anchor to justify an active hiring use for a stable 4-person studio. | DIRECT_FIX | Added "with that growth Jessica is planning to bring on a junior designer" to MEMORY > Work & Projects (revenue grows ~15% YoY), aligning the Greenhouse use. |
| F-006 | MINOR | Common-errors #25 | AGENTS.md, MEMORY.md | Communication Routing; Connected Accounts | `jessica.spencer@Greenridertech.com` | Source email domain does not match the cohort default `@Finthesiss.ai`; Jessica is not on the `@voissync.ai` exception list. | DIRECT_FIX | Replaced both occurrences with `jessica.spencer@Finthesiss.ai`. |
| F-007 | MAJOR | Common-errors #3 | IDENTITY.md | Principles | "Act first within confirmed boundaries…"; "Accuracy beats speed…"; "Privacy is measured, not absolute…"; "Taste is a discipline…"; "Stewardship guides judgment…" | All five Principles bullets opened with a declarative-or-imperative fragment rather than the required `You …` voice gate. | DIRECT_FIX | Rewrote all five to lead with `You …` (act, favour, treat, treat, let) from the established verb palette; substance preserved. |
| F-008 | MINOR | Common-errors #3 | SOUL.md | Core Truths | "A little flair is welcome. You can be expressive…" | One Core Truths bullet opened with a declarative non-`You` clause. | DIRECT_FIX | Rewrote to "You allow a little flair. You can be expressive…" |
| F-009 | MINOR | A1 | MEMORY.md, TOOLS.md | Home & Living; Home, Travel & Local | Ring API present, no Ring device in MEMORY | Ring doorbell/cameras were connected in TOOLS but not recorded in the home inventory, leaving the hardware unanchored. | DIRECT_FIX | Added "a Ring doorbell and cameras for security" to MEMORY > Home & Living alongside the existing Lutron/Sonos/Nest smart-home stack. |
| F-010 | MAJOR | Common-errors #21 / F3 | IDENTITY.md | opening paragraph | "...keep the moving pieces from slipping. You are not new here. You have context, and you use it." | The required closing line was welded onto the end of the opening paragraph rather than standing as the file's standalone closing line after the Principles bullets. | DIRECT_FIX | Removed the closer from the opening paragraph and reinstated it as a standalone closing line after `### Principles`. |

**Checks run with no findings (recorded per §9):** A2 (no SOUL ↔ AGENTS value conflicts; "act first" balanced by the confirmation gates); A3 (TOOLS scopes the studio site, client portal, and trade portals without overreaching into Kevin's Spencer Development Group systems, which stay in Not Connected); A4 (SOUL "6:30 AM before a site walkthrough" and MEMORY morning-coffee anchor consistent with HEARTBEAT 7:00 AM email and tennis mornings); A6 (Sarah Collins best-friend tier and Kevin/Diane inner-circle routing reconcile with the Data Sharing Policy and Contacts); A7 (OpenClaw introduced atop IDENTITY with a ten-month tenure consistent with the mid-2026 anchor); B1 map (Age/DOB/timezone/location in USER > Basics only; one-sentence USER > Background with the full timeline in MEMORY > Work & Projects; $500 threshold headline in USER > Access & Authority with full finance in MEMORY > Finance); B2 (Houzz Pro "not connected" single-homed in TOOLS > Not Connected); B3 (no duplicate scalar facts across files); C2 (age 43 correct; Arizona Time / Scottsdale, no DST); C3 (tenure phrase present in IDENTITY opener); C5 (continuous career: BFA → Spencer Interiors ownership, no unexplained gap > 12 months); C8/C9 ($500 single-currency threshold + proceed-with-judgment default); D1 (Amazon reframed clean buyer-side trade procurement; Twilio outbound reminders; Stripe/Square scoped to deposits and market POS); D2 (Scottsdale services — Instacart, DoorDash, Zillow, Yelp, Uber — all US/Arizona-valid; US phone format; USD; Arizona Time); D4 (East-Coast-NJ family heritage and Scottsdale residence consistent across files); D5 (no eligibility, licensure, or authority misclaims; no medical/legal/financial advice authority); D6 (brand dictionary clean: MacBook Pro, iPhone 15 Pro Max, Adobe Creative Suite, SketchUp, Sony A7IV, Lexus RX 350, Wolf range, Sub-Zero, Lutron, Sonos, Nest, Restoration Hardware, Holly Hunt, Knoll, Design Within Reach); D8 (no inverted/one-time-in-recurring events; dinner party correctly on the last Saturday; sugaring-free Arizona schedule coherent); E4 (monthly outflow line items are individually plausible against the ~$633k gross household income; no stated closed total to contradict); F11 (all mandatory headings carry content).

---

## Section 2 — Coherence Score

```
Score: 9.6 / 10
Rubric:
  - Cross-file alignment:            1.9 / 2.0   (Mode A — graph fully reconciles post F-004, F-005,
                                                   F-006, F-009; small deduction because the crypto,
                                                   Greenhouse, and Ring anchors were synthesized to
                                                   support an active-tool mandate rather than
                                                   persona-declared from the source)
  - Overlapping / SoT compliance:    1.0 / 1.0   (Mode B — canonical placements correct; no verbatim
                                                   duplication; Houzz-Pro negative single-homed)
  - Required-field completeness:     1.0 / 1.0   (Mode C — DOB/age/timezone, $500 threshold,
                                                   default clause, and standalone per-contact Data
                                                   Sharing Policy all present; persona under 50, so
                                                   C7 ICE/POA is recommended not mandatory)
  - Factual & domain correctness:    1.9 / 2.0   (Mode D — strong Scottsdale/Arizona localization;
                                                   small deduction for the dense developer/IT and
                                                   analytics surface that, while now occupation-fit
                                                   to the contractor-built site, remains heavy for a
                                                   four-person design studio)
  - Mathematical correctness:        1.0 / 1.0   (Mode E — exactly 101 unique slugs; age, career, and
                                                   finance figures hold; every named upcoming-event
                                                   weekday verifies against the real calendar)
  - Heading-structure compliance:    2.0 / 2.0   (Mode F headings — all 7 files match the canonical
                                                   sets and order)
  - Format-structure compliance:     1.0 / 1.0   (Mode F caps/format — all char/line caps met; regex
                                                   and forbidden-token sweeps clean; no dashes; no
                                                   .md leaks; web-search-unavailable note present)
                            Total:   9.6 / 10.0
```

---

## Section 3 — Remediation Log

| Finding ID | File | Change Type | Before | After | Justification |
|---|---|---|---|---|---|
| F-001 | TOOLS.md | DIRECT_FIX | 24 bullets with "read-only / dormant / vendor-managed / no trading / observer / mostly read" framings | 24 active bullets tied to named projects, the studio site/client portal, firm staff, or the monthly household-money review | User-issued instruction: no API may be listed read-only or not-used; every slug must carry an active, persona-aligned use. No slug changed; count stays 101. |
| F-002 | HEARTBEAT.md | DIRECT_FIX | Annual: July dermatologist, September ASID, November insurance | Annual: October ASID, November insurance, January dermatologist, February annual physical | No HEARTBEAT > Annual event may fall in April–September; reassigned all into the October–March window. |
| F-003 | HEARTBEAT.md | DIRECT_FIX | 6 upcoming entries, 4 "(date to be confirmed)" and one September 2027 | 12 concrete entries Oct 9 2026 → Feb 18 2027, weekdays calendar-verified | Upcoming events must start October onward with no deadzone/TBD items; expanded for depth. |
| F-004 | MEMORY.md | DERIVE_FIX | Finance had no brokerage/crypto holding | Added "$20,000 brokerage and crypto holding, mostly Kevin's," reviewed monthly | Gives Coinbase/Binance/Kraken/Alpaca a real persona fact to track after F-001 made them active (A1). |
| F-005 | MEMORY.md | DERIVE_FIX | Work & Projects stated a stable 4-person studio | Added "Jessica is planning to bring on a junior designer" tied to ~15% YoY growth | Anchors the active Greenhouse hiring use (A1/D7). |
| F-006 | AGENTS.md, MEMORY.md | DIRECT_FIX | `jessica.spencer@Greenridertech.com` | `jessica.spencer@Finthesiss.ai` | Common-errors #25 cohort default; Jessica not on the `@voissync.ai` exception list. |
| F-007 | IDENTITY.md | DIRECT_FIX | 5 Principles bullets in declarative/imperative voice | 5 bullets rewritten to lead with `You …` (act, favour, treat, treat, let) | Common-errors #3 requires every IDENTITY > Principles bullet in the `You …` voice gate. |
| F-008 | SOUL.md | DIRECT_FIX | "A little flair is welcome…" | "You allow a little flair…" | Common-errors #3 `You …` voice gate for SOUL bullets. |
| F-009 | MEMORY.md | DERIVE_FIX | Home & Living listed Lutron/Sonos/Nest only | Added "a Ring doorbell and cameras for security" | Anchors the connected Ring API to a recorded device (A1). |
| F-010 | IDENTITY.md | DIRECT_FIX | Closer welded to the opening paragraph; no standalone closing line | Opening paragraph ends "...keep the moving pieces from slipping."; "You are not new here. You have context, and you use it." now stands alone after `### Principles` | Common-errors #21 requires the closer as a verbatim standalone line at the end of the file. |

---

## Section 4 — Open Questions for Human Input

None. Every finding was remediable from existing persona context. Where new facts were synthesized — the $20,000 household brokerage/crypto holding, the junior-designer hire plan, the Ring security devices, and the October-2026-forward calendar — each was anchored to an existing persona thread (Kevin's investment role and the wealthy two-earner household, the firm's stated ~15% YoY growth, the existing smart-home stack, and the recurring ASID/insurance/dermatology/dinner-party rhythms) and verified for arithmetic, calendar, and cross-file consistency. No fact was invented without a persona-aligned source thread.

---

## Section 6 — Cross-Persona Pattern Flags

1. **TOOLS.md "read-only / dormant / vendor-managed" framings** (F-001) — Jessica carried 24 such bullets, the single largest defect class this pass. Run a cohort-wide grep for `read-only`, `dormant`, `not actively used`, `no trading`, `observer access`, and `mostly read` across every TOOLS.md and rewrite each into an active, persona-aligned use. This recurs with the D7 occupation-mismatch tools (dev/IT, analytics, HR, crypto) and is the cohort's most reliable source of passive-tool drift (common-errors #6 and #7).

2. **HEARTBEAT > Annual events inside April–September** (F-002) — verify every persona's Annual block sits entirely in the October–March window, or carries an explicit seasonal-variable justification.

3. **Deadzone "(date to be confirmed)" upcoming events and pre-anchor dates** (F-003) — sweep every HEARTBEAT > Upcoming Events list for TBD markers and for any entry dated at or before the anchor; rebuild as concrete, calendar-verified, anchor-forward entries.

4. **Source email domain `@Greenridertech.com`** (F-006) — the same non-canonical source domain seen in other Batch_6 personas (e.g., Jane Graves's `@Greenridertech.co`). Grep every persona for any non-`@Finthesiss.ai`/non-`@voissync.ai` domain and reconcile against common-errors #25.

5. **IDENTITY > Principles and SOUL bullets in non-`You` voice** (F-007, F-008) — grep every IDENTITY `### Principles` and SOUL bullet for declarative/imperative openers and confirm each leads with `You …`.

6. **IDENTITY closer welded to the opening paragraph** (F-010) — Jessica's closer "You are not new here. You have context, and you use it." sat at the tail of the opening paragraph rather than as a standalone closing line, the same pattern flagged in Jane Graves. Confirm every IDENTITY.md ends with the closer as its own standalone line after `### Principles`.

---

*End of report.*
