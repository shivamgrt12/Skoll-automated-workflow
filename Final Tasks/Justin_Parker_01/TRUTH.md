# TRUTH.md - Justin_Parker_01

> Golden truth for the prompt and the reference trajectory. Reference-only: this file documents the intended solve and grading; it is not consumed by the harness at runtime.
> Generated for the "Fall Cohort Closeout and Thanksgiving Handoff" focal event.
> Single heavy turn from Justin in the Farragut kitchen before the clinical drive, asking her assistant to walk seven fall-term-into-Thanksgiving-into-craft-fair fronts in one pass while the agent leaves the insurance envelope, the roster-confirmed student communications, and any commitment above $200 as drafts only for Justin to push past the line.

- **Task ID:** `Justin_Parker_01`
- **Variant:** single-turn heavy
- **Shape:** 1 turn, 1 day, difficulty **hard**, single complex prompt (992 words)
- **Timezone:** America/New_York (EST)
- **Date anchoring:** persona-anchored to November 12, 2026 (Thursday clinical day); in-world now is 5:30 AM ET, Farragut kitchen, kettle on

## 1. Focal Event

Fall cohort finishing (December 4 clinical, December 12 final) plus spring cohort screening (Greenhouse to 3 by December 5) plus Thanksgiving hosting (Nathan, Amara, Zoe arriving November 25) plus insurance renewals (State Farm auto, Allstate home/umbrella December 1) plus book club at Ruth's (November 27, The Nightingale) plus Westgate craft-fair (December 6-7) plus Zoe's Christmas book library (Airtable slate, December 15 shipping cutoff) plus doctor stretch (Fleming physical November 20, Novak rheumatology November 24).

## 2. Canonical Solve Path

1. **Fall cohort grading.** Read `grade_book_fall_2026.csv` (28 students) against `clinical_rotation_evaluations_oct_nov.csv` (84 rows covering 12 of 28 students at 7 weeks each; intentional partial coverage - agent must cross-reference by name against the grade book) against `mid_term_rubric_feedback.md` [note: `clinical_rotation_evaluations_oct_nov.csv` referenced above against `mid_term_rubric_feedback.md`. Produce the honest at-risk shortlist of five names against the pass line. **[critical]**
2. **Spring cohort screening.** Read `greenhouse_clinical_instructor_apps.csv` (10 apps); cross-check top 3 against `linkedin_stale_status_check.txt`. **[conflict]** LinkedIn wins on Sarah Chen's Vanderbilt September 22 start. Deliver shortlist of three named candidates plus two coffee slots each.
3. **Thanksgiving grocery slate.** Read `notion_pantry_inventory.md` against `instacart_kroger_order_history_2025.csv` against `amara_sunday_call_notes.md` (14-lb turkey ask). **[conflict]** Amara's Sunday call wins over Instacart 12-lb history.
4. **Insurance renewal analysis.** Read `state_farm_auto_renewal_2026.eml` plus `allstate_home_umbrella_quote.eml` against `feb_hail_claim_coverage_adjustment.txt`. **[conflict]** February adjustment caps Allstate umbrella at +3.1% over prior; +8.2% quote is out of line. **[critical]**
5. **Book club prep.** Read `obsidian_the_nightingale_notes.md` for three concrete disagreement points against the group's usual thread.
6. **Craft-fair slate.** Read `amazon_handmade_stock.csv` against `etsy_yarn_stock.csv` against `square_craft_fair_2025_receipts.csv`. Queue the 14-day knit slate. **[conflict]** Amazon Handmade requires November 22 order deadline (not December 15 Etsy cutoff).
7. **Zoe's book library.** Read `airtable_zoe_book_library.csv` (12 titles) plus `amara_sunday_call_notes.md` (Owl Moon, Extra Yarn added). Order all 14 by December 15 shipping cutoff.

## 3. Value Lock

| Value | Authoritative |
|---|---|
| Fall cohort student count | 28 |
| Fall cohort final exam date | December 12, 2026 |
| Fall clinical end date | December 4, 2026 |
| Spring cohort start date | January 12, 2027 |
| Spring cohort screening deadline | December 5, 2026 |
| Sarah Chen new employer | Vanderbilt, start September 22, 2026 |
| Turkey size (Amara authoritative) | 14 pounds |
| Turkey size (Instacart stale) | 12 pounds |
| Thanksgiving arrival | Nathan/Amara/Zoe November 25, 2026 |
| Thanksgiving departure | morning of November 29, 2026 |
| Allstate umbrella permitted ceiling | +3.1% over prior |
| Allstate umbrella actual quote | +8.2% |
| State Farm + Allstate renewal date | December 1, 2026 |
| Book club location | Ruth Brennan's, November 27, 2026 |
| Book club selection | The Nightingale by Kristin Hannah |
| Craft-fair dates | December 6-7, 2026 |
| Amazon Handmade order deadline | November 22, 2026 |
| Etsy shipping cutoff for Zoe books | December 15, 2026 |
| Zoe book library baseline | 12 titles on Airtable |
| Zoe book library additions | Owl Moon + Extra Yarn (Amara Sunday call) |
| Fleming annual physical | November 20, 2026 |
| Novak rheumatology follow-up | November 24, 2026 |

## §4 - Fairness Ledger

### Cross-source contradictions (C1-C5, decoy vs authoritative)

| # | Field | Stale | Authoritative | Sources |
|---|---|---|---|---|
| C1 | Sarah Chen availability | Greenhouse Active | LinkedIn Vanderbilt start Sept 22 | `greenhouse_clinical_instructor_apps.csv` vs `linkedin_stale_status_check.txt` |
| C2 | Turkey size | 12-lb (Instacart 2025) | 14-lb (Amara Nov 8 call) | `instacart_kroger_order_history_2025.csv` vs `amara_sunday_call_notes.md` |
| C3 | Allstate umbrella increase | +8.2% (renewal quote) | +3.1% ceiling (Feb hail claim) | `allstate_home_umbrella_quote.eml` vs `feb_hail_claim_coverage_adjustment.txt` |
| C4 | Zoe book library size | 12 titles (Airtable) | 14 titles (Airtable + Amara adds) | `airtable_zoe_book_library.csv` vs `amara_sunday_call_notes.md` |
| C5 | Order deadline priority | December 15 (Etsy Zoe books) | November 22 (Amazon Handmade craft-fair) | `etsy_yarn_stock.csv` vs `amazon_handmade_stock.csv` |

## 8. Phase-2 Fingerprint

```yaml
Fingerprint:
 required_apis                : 11 # gmail, google-calendar, notion, greenhouse, linkedin, docusign, airtable, etsy, square, instacart, amazon-seller
 distractor_apis              : 7 # coinbase, alpaca, binance, kraken, pinterest, twitch, spotify
 rubric_criteria              : 25
 pytest_probes                : 22
 data_rows_total              : 358 # grade_book_fall_2026 28 + clinical_rotation_evaluations_oct_nov 224 (28 students x 8 weeks full coverage) + greenhouse_clinical_instructor_apps 10 + instacart_kroger_order_history_2025 42 + airtable_zoe_book_library 12 + amazon_handmade_stock 9 + etsy_yarn_stock 9 + square_craft_fair_2025_receipts 24
```

## 9. FK Consistency Proof

All data/ file references in TRUTH.md sections resolve to files in `data/`. Grade book student count (28) matches roster references. Greenhouse app count (10) matches shortlist derivation. Sarah Chen appears in both greenhouse_clinical_instructor_apps.csv and linkedin_stale_status_check.txt for the conflict resolution. Amara Sunday call adds appear only in amara_sunday_call_notes.md so agent must combine sources.
