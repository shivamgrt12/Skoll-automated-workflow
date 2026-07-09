# Paul Rivera — Persona QC Report (v1.4)

> **Audit scope:** 7 inner files at `paul-rivera/` (AGENTS.md, HEARTBEAT.md, IDENTITY.md, MEMORY.md, SOUL.md, TOOLS.md, USER.md). `README.md` is out of scope per QC v1.3/v1.4.
>
> **Anchor date:** 2026-06-09 (system date).
>
> **DOB anchor:** February 5, 1958 (USER.md > Basics). Age 68 verified.
>
> **OpenClaw tenure:** "14 months" (IDENTITY.md). Derives to "since April 2025."
>
> **Posture:** Adversarial skepticism. Findings quote verbatim evidence and cite file:section.

---

## Section 1 — Findings Catalog

| ID | Severity | Mode | File | Section | Quote | Defect | Fix Type | Fix |
|---|---|---|---|---|---|---|---|---|
| F-001 | **MAJOR** | A1 | MEMORY.md | `## Connected Accounts` | `"- **Facebook**: Posts photos from golf and national park trips, follows Brett and Kelsey. No other social platforms."` | Facebook is asserted as a "Connected Account" but no `facebook-api` slug exists in TOOLS.md (Facebook is not one of the 101 canonical mock APIs). MEMORY/TOOLS contradiction. | DIRECT_FIX | Either (a) remove the Facebook bullet from `## Connected Accounts` and move the fact ("uses Facebook to post golf and national park photos") to `## Preferences` as a social-media usage note, or (b) drop it entirely. Recommendation: (a) — move the usage note to Preferences. |
| F-002 | **MAJOR** | A5 / D8 / E7 | HEARTBEAT.md + MEMORY.md | HEARTBEAT `### Annual` + MEMORY `## Health & Wellness` + HEARTBEAT `## Upcoming Events & Deadlines` | HEARTBEAT: `"**Every 6 months**: Dr. Robert Kaplan cardiology follow-up."` and `"**February 12, 2027**: Cardiology follow-up with Dr. Robert Kaplan."` MEMORY: `"Follows up with Dr. Robert Kaplan every 6 months"` | From anchor 2026-06-09, the next scheduled follow-up is 8 months out (June 2026 to Feb 2027). The Aug 2026 visit was removed earlier in this session. Recurring cadence ("every 6 months") and the upcoming-events list disagree. | DERIVE_FIX | Either (a) reinstate a `2026-08-XX` cardiology follow-up in `## Upcoming Events & Deadlines`, OR (b) loosen the recurring rule to `**Approximately every 6 months**` and add a one-line note in MEMORY > Health & Wellness ("Next follow-up: February 12, 2027 after a longer-than-usual interval"). |
| F-003 | **MAJOR** | C4 | MEMORY.md | `## Key Relationships` | No DOB/birthday recorded for Judith (wife), Brett (son), Kelsey (daughter), Hannah (DiL), Daniel (SiL), Owen (grandson), Lily (granddaughter), Jim Rivera (brother), Tom Hadley (best friend) | C4 mandates full DOBs for spouse, children, parents, siblings, and designated best friend in MEMORY > Key Relationships. None are present. Note: Paul's parents are not introduced in the persona at all, so the spec for parents reduces to "if living, record." | REQUIRES_HUMAN_INPUT | See Q1–Q6 in Section 4. |
| F-004 | **MAJOR** | C4 / E7 | HEARTBEAT.md | `### Annual` | Current Annual block contains only Paul's birthday (Feb 5), Mother's Day, cardiology cadence, and annual physical. | C4 mandates that inner-circle DOBs propagate to `HEARTBEAT.md > Recurring Events > ### Annual` as birthday entries. Missing: Judith's birthday, Brett's birthday, Kelsey's birthday, Owen's birthday (recurring annual; only the Oct 16-18 2026 weekend is in Upcoming), Lily's birthday, Tom Hadley's birthday, plus the wedding anniversary (Paul + Judith, 41 years). | DERIVE_FIX (downstream of F-003) | After F-003 is answered, add one bullet per birthday in `### Annual`: `- **<Month Day>**: <Person>'s birthday.` Plus `- **<Month Day>**: Wedding anniversary with Judith (<N> years).` Also add Owen's recurring birthday (currently only captured as Upcoming). |
| F-005 | **MAJOR** | C5 / E2 | MEMORY.md | `## Personal Profile` and `## Work & Projects` | Personal Profile: `"He attended Clearfield Aeronautical University (B.S. Aviation Science, 1980)"`. Work & Projects: `"35-year career at SkyBridge Airlines"` retired March 2023 → start year 1988. | 8-year unexplained gap between BS degree (1980) and SkyBridge start (1988). C5 forbids unexplained gaps > 12 months. Plausible explanations: military aviation service, regional carrier hour-building, instructor work. | REQUIRES_HUMAN_INPUT | See Q7. |
| F-006 | **MINOR** | B1 / B3 | MEMORY.md | `## Home & Living` (line 72) and `## Contacts` (line 106) | Home & Living: `"**Address**: 7421 East Pinnacle Vista Drive, Scottsdale, AZ 85255."` Contacts: `"**Home address**: 7421 East Pinnacle Vista Drive, Scottsdale, AZ 85255."` | Same street address recorded verbatim in two MEMORY sections. Per B1, mailing addresses live in MEMORY > Contacts only. | DIRECT_FIX | Delete the `**Address**: ...` line from `## Home & Living`. Keep the house description (single-story stucco, gated community, 3BR/2.5BA, ~2,600 sq ft, etc.). |
| F-007 | **MINOR** | B3 | MEMORY.md | `## Key Relationships` | Brett's bullet: `"Two children: Owen (7) and Lily (4)."` Separate standalone bullets exist for `**Owen Rivera (grandson, 7)**` and `**Lily Rivera (granddaughter, 4)**`. | Owen's and Lily's ages and existence appear in two bullets within the same section. Depth-difference rule applies, but the ages are duplicated verbatim. | DIRECT_FIX | Remove "Two children: Owen (7) and Lily (4)" from Brett's bullet (replace with "Two children, Owen and Lily, who have their own bullets below."). Keep the standalone Owen/Lily bullets as canonical. |
| F-008 | **MINOR** | B1 | AGENTS.md | `## Communication Routing` | `"- **FaceTime**: Reserved for Kelsey (Sunday 4:00 PM), Brett (when scheduled), and the grandkids."` HEARTBEAT.md `### Weekly` already carries: `"- **Sunday, 4:00 PM**: FaceTime with Kelsey. Reminder at 3:50 PM."` | "Sunday 4:00 PM" is a recurring schedule fact. Per B1, recurring schedules live in HEARTBEAT.md only; AGENTS Communication Routing should describe the channel choice, not embed the schedule. | DIRECT_FIX | In AGENTS Communication Routing, change `"Reserved for Kelsey (Sunday 4:00 PM), Brett (when scheduled), and the grandkids."` to `"Reserved for Kelsey on her standing weekly slot, Brett when scheduled, and the grandkids."` |
| F-009 | **MINOR** | C7 | MEMORY.md | `## Contacts` | `"**Emergency designations**: Judith Rivera is ICE and medical proxy. Brett Rivera is secondary medical contact."` | Persona is 68 (over 50). Power-of-Attorney (POA) is strongly recommended; not explicitly stated. | REQUIRES_HUMAN_INPUT | See Q8. |
| F-010 | **MINOR** | D4 | MEMORY.md | `## Personal Profile` | Surname is Rivera; persona describes "basic Spanish (picked up from layovers and travel)" in the legacy MEMORY but the rewritten Personal Profile says `"English is his native language; he picked up basic Spanish from international layovers."` Heritage is otherwise unspecified. | Rivera is a Spanish-language surname. D4 requires surname/heritage alignment or explanation. The persona reads as a Spanish-surnamed American without explicit Latino/Hispanic identity. | REQUIRES_HUMAN_INPUT | See Q9. |
| F-011 | **MINOR** | C3 | IDENTITY.md | Opening paragraph | `"You have been his assistant for 14 months..."` | C3 prefers an absolute tenure ("since [Month Year]") over a relative one ("for N months") so the statement does not drift as the anchor date advances. 14 months before 2026-06 = April 2025. | DIRECT_FIX | Replace `"You have been his assistant for 14 months"` with `"You have been his assistant since April 2025"`. |
| F-012 | **MINOR** | E2 | MEMORY.md | `## Work & Projects` | `"Approximately 22,000 total flight hours."` over 35 years = ~628 hours/year average. | This is plausible for a career pilot (typical commercial captain 600–1,000 hrs/yr), but verify against the FAA Part 121 max of 1,000 hrs/year. No defect; flagged only as a sanity-check note. | INFO ONLY | No change needed. Math passes. |

---

## Section 2 — Coherence Score

```
Score: 7.8 / 10
Rubric:
  - Cross-file alignment:            1.5 / 2.0   (Mode A: F-001 Facebook, F-002 cardiology cadence; rest aligned)
  - Overlapping / SoT compliance:    0.7 / 1.0   (Mode B: F-006 address, F-007 grandkids, F-008 Sunday time)
  - Required-field completeness:     0.4 / 1.0   (Mode C: F-003 inner-circle DOBs missing, F-004 birthdays absent from Annual, F-009 POA missing)
  - Factual & domain correctness:    1.6 / 2.0   (Mode D: F-005 8-yr career gap, F-010 heritage; otherwise clean)
  - Mathematical correctness:        0.9 / 1.0   (Mode E: budget $7,000 sums perfectly, income $14,000 sums perfectly, age math passes, 101-API count passes; F-002 recurrence math off)
  - Heading-structure compliance:    2.0 / 2.0   (Mode F: all 7 files match the canonical heading set; F1–F9 all pass)
  - Format-structure compliance:     0.7 / 1.0   (Mode F: caps and formats pass; HEARTBEAT > Annual is undersized relative to the inner-circle birthday requirement, indirectly via F-004)
                            Total:   7.8 / 10.0
```

**Verdict:** The persona's **structural skeleton is clean** (Mode F passes top-to-bottom; the prior v1.4 fixes for the Data Sharing Policy H2, single Weekly block, and removal of `### General Agent Capabilities` are in place). The remaining defects cluster in **Required-Field Completeness (Mode C)** — specifically, the inner-circle DOBs that downstream block HEARTBEAT > Annual — and a small set of cross-file alignment slips (Mode A/B). The persona would survive a casual deployment but **would not survive a 30-day forensic audit by a determined user** until the C-mode gaps are closed.

---

## Section 3 — Remediation Log (Phase 2)

| Finding ID | File | Change Type | Before | After | Justification |
|---|---|---|---|---|---|
| F-001 | MEMORY.md | DIRECT_FIX | `## Connected Accounts`: `- **Facebook**: Posts photos from golf and national park trips, follows Brett and Kelsey. No other social platforms.` | Remove from Connected Accounts. Add to `## Preferences`: `- **Social media**: Uses Facebook to post golf and national park trip photos and to follow Brett and Kelsey. No other social platforms. Not connected to the agent.` | Facebook is not in the 101 canonical mock APIs. Connected Accounts must reconcile with TOOLS.md slugs. The factual content survives in Preferences. |
| F-002 | HEARTBEAT.md (and optionally MEMORY.md) | DERIVE_FIX | `### Annual`: `- **Every 6 months**: Dr. Robert Kaplan cardiology follow-up. Morning appointment; Judith drives.` | Option A: Add to Upcoming Events `- **August 13, 2026**: Cardiology follow-up with Dr. Robert Kaplan. Morning slot; Judith drives.` Option B: Change Annual to `- **Approximately every 6 months**: Dr. Robert Kaplan cardiology follow-up. Morning appointment; Judith drives. Next scheduled visit shown under Upcoming Events.` | Removes the cadence/upcoming disagreement that today's anchor date exposes. Option A restores the original cadence; Option B documents the longer interval. Pick one. |
| F-003 | MEMORY.md | REQUIRES_HUMAN_INPUT | Key Relationships bullets lack DOBs | After Q1–Q6 answered, append "(DOB: YYYY-MM-DD)" to each named relationship's bullet. | C4 compliance. Required for downstream F-004. |
| F-004 | HEARTBEAT.md | DERIVE_FIX (after F-003) | `### Annual` currently has 4 entries. | Add: `- **<Judith DOB>**: Judith's birthday.` `- **<Brett DOB>**: Brett's birthday.` `- **<Kelsey DOB>**: Kelsey's birthday.` `- **<Owen DOB>**: Owen's birthday. (Annual reminder; weekend trip in Upcoming when applicable.)` `- **<Lily DOB>**: Lily's birthday.` `- **<Tom Hadley DOB>**: Tom Hadley's birthday.` `- **<Anniversary date>**: Wedding anniversary with Judith.` | Birthdays must propagate from Key Relationships to Annual recurring per C4/E7. |
| F-005 | MEMORY.md | REQUIRES_HUMAN_INPUT | Personal Profile: `"B.S. Aviation Science, Clearfield Aeronautical University (1980)"` Work & Projects: SkyBridge 1988–2023 | After Q7 answered, insert one sentence in Work & Projects covering 1980–1988 (likely a regional carrier or military pilot tour). | C5 compliance — no unexplained career gap > 12 months. |
| F-006 | MEMORY.md | DIRECT_FIX | `## Home & Living` line: `- **Address**: 7421 East Pinnacle Vista Drive, Scottsdale, AZ 85255.` | Remove that line entirely. The address remains in `## Contacts > Home address`. | B1: mailing addresses live in MEMORY > Contacts only. Home & Living describes the house, not the address. |
| F-007 | MEMORY.md | DIRECT_FIX | Brett's bullet: `"Two children: Owen (7) and Lily (4). Steady, pragmatic..."` | `"Two children, Owen and Lily (both have their own bullets below). Steady, pragmatic..."` | B3: ages duplicated. Standalone Owen/Lily bullets remain canonical for each child's details. |
| F-008 | AGENTS.md | DIRECT_FIX | `## Communication Routing`: `- **FaceTime**: Reserved for Kelsey (Sunday 4:00 PM), Brett (when scheduled), and the grandkids.` | `- **FaceTime**: Reserved for Kelsey on her standing weekly slot, Brett when scheduled, and the grandkids.` | B1: Sunday 4:00 PM is the schedule; HEARTBEAT is its canonical home. |
| F-009 | MEMORY.md | REQUIRES_HUMAN_INPUT | Contacts: `"Judith Rivera is ICE and medical proxy. Brett Rivera is secondary medical contact."` | Either add `"Power of attorney: <name>"` or add explicit `"No formal POA on file at this time."` | C7: POA designation strongly recommended for personas over 50. |
| F-010 | MEMORY.md | REQUIRES_HUMAN_INPUT | Personal Profile is silent on cultural identity. Surname Rivera unexplained. | After Q9 answered, add a sentence to Personal Profile clarifying heritage (e.g., "Paul's father immigrated from <country>; the family was raised English-speaking.") OR leave blank with a note acknowledging the omission is intentional. | D4: surname/heritage alignment. |
| F-011 | IDENTITY.md | DIRECT_FIX | `"You have been his assistant for 14 months"` | `"You have been his assistant since April 2025"` | C3: absolute tenure preferred over relative tenure that drifts with the anchor date. |
| F-012 | — | INFO ONLY | — | — | Flight-hour math passes; no action needed. |

---

## Section 4 — Open Questions for Human Input

```
Q1. Resolves F-003 (Judith's DOB).
    Judith Rivera is Paul's wife (age 66). Please provide Judith's full date of birth.
    Constraint: month must fall in October–March (OpenClaw fiscal-year constraint applies
    to the primary persona, but inner-circle DOBs have no month constraint).
    Answer: ____-__-__

Q2. Resolves F-003 (Brett's DOB) and F-004.
    Brett Rivera is Paul's son (age 38). Please provide Brett's full date of birth.
    Answer: ____-__-__

Q3. Resolves F-003 (Kelsey's DOB) and F-004.
    Kelsey Rivera-Cho is Paul's daughter (age 35). Please provide Kelsey's full date of birth.
    Answer: ____-__-__

Q4. Resolves F-003 (Owen's DOB) and F-004.
    Owen Rivera is Paul's grandson (age 7); he turns 8 the weekend of October 16-18, 2026
    (already in Upcoming Events). Please confirm his exact date of birth.
    Answer: 2018-__-__

Q5. Resolves F-003 (Lily's DOB) and F-004.
    Lily Rivera is Paul's granddaughter (age 4). Please provide Lily's full date of birth.
    Answer: 2021- or 2022-__-__

Q6. Resolves F-003 and F-004 (Jim, Tom, Hannah, Daniel, Anniversary).
    Please provide the following:
      - Jim Rivera (brother, 71): DOB ____-__-__
      - Tom Hadley (best friend, 70): DOB ____-__-__
      - Hannah Rivera (daughter-in-law, 36): DOB ____-__-__ (optional)
      - Daniel Cho (son-in-law, 36): DOB ____-__-__ (optional)
      - Wedding anniversary with Judith: ____-__-__

Q7. Resolves F-005 (pre-SkyBridge career, 1980-1988).
    Paul earned his BS Aviation Science in 1980 and started at SkyBridge Airlines in 1988.
    What did he do in the intervening 8 years? Common options:
      (a) U.S. Air Force / Navy pilot (military service)
      (b) Regional carrier first officer building hours
      (c) Cargo / freight pilot (FedEx / UPS / regional cargo)
      (d) Flight instructor / corporate aviation
      (e) Other (please describe)
    Answer: _______________

Q8. Resolves F-009 (POA designation).
    Does Paul have a formal Power of Attorney on file? If yes, name the holder
    (likely Judith). If no, confirm "No formal POA on file at this time" and we will
    record that.
    Answer: _______________

Q9. Resolves F-010 (heritage / surname).
    The surname Rivera typically suggests Spanish, Mexican, Filipino, or other Latin
    heritage. The persona does not currently state Paul's cultural identity. Please
    select one:
      (a) Mexican-American (e.g., father or grandfather emigrated from Mexico)
      (b) Cuban-American
      (c) Puerto Rican
      (d) Filipino-American
      (e) Spanish (Iberian) heritage
      (f) Surname is family-only with no cultural attachment (e.g., adopted, blended)
      (g) Other (please describe)
    Answer: _______________

    Follow-up: if (a)–(e), should the persona's Personal Profile add one sentence
    on family heritage, or leave it implicit?
    Answer: _______________
```

---

## Section 5 — Proposed Corrected Files

Per the user's request ("make a QC report"), corrected file contents are **not auto-applied** in this report. All DIRECT_FIX items listed in Section 3 are ready to apply on request. The DERIVE_FIX and REQUIRES_HUMAN_INPUT items need either the F-002 cardiology decision (Option A or B) or the Section 4 answers (Q1–Q9) before they can be applied.

**Ready to apply now (no input needed):** F-001, F-006, F-007, F-008, F-011.

**Pending one decision (Option A vs B):** F-002.

**Pending Section 4 answers:** F-003, F-004, F-005, F-009, F-010.

---

## Section 6 — Cross-Persona Pattern Flags

This audit covered only the Paul Rivera persona. No cohort-level comparison was performed in this session. Patterns that may be SYSTEMIC across the cohort (worth checking against the other persona folders under `Persona creation/`):

- **Facebook (or other non-canonical social platforms) leaking into MEMORY > Connected Accounts** without a matching `*-api` slug in TOOLS.md. If this appears in other personas, raise as SYSTEMIC and add a template-level check to the QC v1.5 prompt: "Every Connected Accounts bullet must trace to a `*-api` slug in TOOLS.md or be moved to Preferences."
- **Relative-tenure phrasing ("for 14 months") instead of absolute "since Month Year"** in IDENTITY.md openers. If other personas in the cohort show the same, recommend a v1.5 amendment to enforce the absolute form.
- **Inner-circle DOBs absent** from MEMORY > Key Relationships, with HEARTBEAT > Annual carrying only the persona's own birthday. This is the most common cohort-level gap based on prior QC observations.

---

## Section 7 — Final Deliverable Checklist

- [x] Every check in §5 (MODES A–F) was run
- [x] MODE F (heading-structure) cross-checked against the v1.4 spec
- [x] AGENTS.md contains all 7 H2 sections including `## Data Sharing Policy` as the seventh
- [x] TOOLS.md contains NO `### General Agent Capabilities` heading
- [x] TOOLS.md was verified to contain exactly 101 unique `-api` slugs
- [x] USER.md was verified to be ≤ 40 lines (30 lines actual)
- [x] Every finding has a verbatim quote + file:section
- [x] Every finding has a severity tag
- [x] Every finding has a Fix Type (DIRECT_FIX / DERIVE_FIX / REQUIRES_HUMAN_INPUT)
- [x] No finding has both "fix" and "REQUIRES_HUMAN_INPUT"
- [x] Coherence score is justified by the rubric
- [x] All REQUIRES_HUMAN_INPUT items are surfaced as questions (Q1–Q9)
- [x] No cohort comparison was attempted (single persona)
- [x] README.md was NOT audited (out of scope under v1.3/v1.4)

---

*End of QC report. 12 findings catalogued: 5 MAJOR, 6 MINOR, 1 INFO. 5 ready for immediate DIRECT_FIX, 1 needs an A/B decision, 5 need human input. Coherence score 7.8 / 10. Structural skeleton clean; required-field gaps (C-mode) are the dominant remaining defect class.*
