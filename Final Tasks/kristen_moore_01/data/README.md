# data/ -- Persona-owned document artifacts

Inventory index for the 15 load-bearing persona-facing artifacts in this folder. All API-shaped mock data (CSV/JSON/TSV of API endpoints) lives under `mock_data/<api>-api/` and is served to the harness at runtime, never duplicated here. Full per-value carriers and trust rules live in `TRUTH.md` sections 3 (VALUE_LOCK) and 7 (Deliverable Authoring Notes).

Flat layout, 4 formats (EML, MD, PDF, YAML). Total 15 files + this README index = 16 top-level entries (matches `TRUTH.md` §8 `input_artifacts = 16`).

## Correspondence (EML, 8 files)

| File | Load-bearing for | Anchor |
|---|---|---|
| `email_fidelity_q3_2026_statement.eml` | C3 Fidelity 529 balance -- confirms Plaid live $42,200 against persona memory $45,000 | C3 corroboration |
| `email_church_giving_statement_thru_sep.eml` | C4 tithing -- Grace Tabernacle statement $3,750 through September (partial view, excludes October) | C4 partial-view carrier |
| `email_hr_open_enrollment_reminder.eml` | November 14 enrollment deadline anchor | R13 benefits window |
| `email_bamboohr_benefits_summary.eml` | C2 decoy side -- 403(b) at stale 4%; full benefits summary (health, dental, vision, life) | C2 decoy |
| `email_gusto_pay_stub_oct_30.eml` | C2 authoritative side -- 403(b) at live 5%, net pay $1,910.96 | C2 authoritative |
| `email_gusto_rate_change_apr17.eml` | C2 anchor -- confirms transition 4% -> 5% effective April 17 2026, per-period impact $95.38 -> $119.23 | C2 changepoint |
| `email_will_mlk_weekend_visit.eml` | SC2 anchor -- Will's flight arrives Memphis 11:15 AM Jan 17 2027 | SC2 anchor |
| `email_tanya_thanksgiving_plan.eml` | Thanksgiving Nov 26 coordination -- Tanya stopping by for dessert | R14 anchor |

## Formal documents (PDF, 5 files)

| File | Load-bearing for | Anchor |
|---|---|---|
| `marcus_life_insurance_policy.pdf` | Origin of Fidelity 529 seed ($250K MetLife payout Feb 2022) | C3 provenance |
| `fidelity_529_setup_confirmation.pdf` | C3 corroborator on the memory side -- $45,000 initial deposit | C3 decoy corroborator |
| `grace_tabernacle_giving_2026.pdf` | C4 partial view -- church-issued giving summary $3,750 through September | C4 partial-view corroborator |
| `gusto_pay_stub_oct_30_2026.pdf` | C2 authoritative corroborator -- gross $2,384.62, 5%, net $1,910.96 | C2 corroborator |
| `xero_year_end_rollup_loretta_2026.pdf` | C1 partial third view -- $1,950 direct-billed Loretta costs; explicit note that Kristen out-of-pocket is excluded | C1 partial-view corroborator |

## Persona-resident notes (MD + YAML, 2 files)

| File | Load-bearing for | Anchor |
|---|---|---|
| `kristen_notebook_budget.md` | Paper-notebook mirror of the QuickBooks budget; month-by-month notes | Notebook-side of the reconciliation |
| `loretta_medications.yaml` | Latanoprost q8wk cycle + appointment schedule | C6 anchor (8-week cycle vs 11-week Plaid gap) |

## Format count

| Format | Files |
|---|---|
| EML | 8 |
| PDF | 5 |
| MD | 1 (+ this README) |
| YAML | 1 |
| **Total load-bearing** | **15** |
| **Total incl. this index** | **16** |

No image, audio, or video artifacts. Task is explicitly non-multimodal: `PROMPT.md`, `rubric.json`, and `test_outputs.py` reason from text content only.
