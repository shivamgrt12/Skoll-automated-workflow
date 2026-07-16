# data/ - Extracted Workspace Artifacts for clara-leon

Source: `clara-leon/home/` - Clara's fake home-directory tree of workspace artifacts.
Target task: quarterly investment review with Sheila Ramos (see `../PROMPT.md`).

Selection: **12 required** + **6 noisy** (distractor) artifacts, chosen against the
prompt's 10 workstreams and 8 deliverables. Every required entry directly supports a
workstream; every noisy entry is plausibly-adjacent but off-scope for this review.

Flat layout (subdirectory noise removed). The 12 required artifacts and 6 noisy
distractor artifacts live directly under `data/` so the agent sees them in a single flat directory listing.

---

## Required (12) - align with the prompt

| # | Path | What it is | Workstream role |
|---|---|---|---|
| 1 | `data/XL01.xlsx` | Monthly Budget | Cross-book reconciliation baseline (income $5,500, expenses $3,220, buffer $2,280) |
| 2 | `data/XL06.xlsx` | Giving Log | Charitable giving audit source (parish / library / heart charity / food bank) |
| 3 | `data/XL09.xlsx` | Estate Document Inventory | Estate signing-queue review - living trust, will, POA, healthcare proxy, living will |
| 4 | `data/XL03.xlsx` | 2025 Tax Worksheet | Charitable + income reconciliation reference |
| 5 | `data/DF01.pdf` | Coastal National Bank Statement | Live balance vs book - checking ...3071 + savings ...6620 with Jan 2026 transaction detail |
| 6 | `data/DF05.pdf` | Paloma Lakes HOA Statement | HOA expense line ($620/mo) for expense-drift analysis |
| 7 | `data/DF02.pdf` | Meridian Wealth Partners Q4 Statement | Sheila's shared summary - brokerage MWP-40817, portfolio anchor ($620,000) |
| 8 | `data/DF07.pdf` | Estate Plan Review Letter | Hartwell & Vance estate designations for signing-queue context |
| 9 | `data/XL02.xlsx` | Portfolio Holdings | Portfolio walk - allocation %, per-position market values |
| 10 | `data/PPDF02.pdf` | Retirement Income Plan Summary | Withdrawal rate + portfolio picture ($1,500/mo distribution, ~3% rate) |
| 11 | `data/DOC08.docx` | Letter to Sheila (draft) | Pre-meeting note reference - agenda items on allocation, cash reserve, taxes, estate |
| 12 | `data/DF08.pdf` | Homeowners HO-6 (Condo Policy) | Condo unit context for net-worth statement (7420 Paloma Lakes Circle #204) |

## Noisy (6) - plausible distractors, off-scope

| # | Path | What it is | Why it is noise |
|---|---|---|---|
| 1 | `data/XL07.xlsx` | Medications & BP Log | Health data - spreadsheet-looking distractor, off-scope |
| 2 | `data/DF03.pdf` | Medicare Supplement Insurance | Health-insurance premium - adjacent to budget lines but not a workstream input |
| 3 | `data/DF04.pdf` | Medical After-Visit Summary | Medical record - off-scope for financial review |
| 4 | `data/PPDF01.pdf` | Bridge Season Review | Hobby 'review' - surface-similar language to portfolio review |
| 5 | `data/DF06.pdf` | Auto Insurance Policy | Financial-adjacent but not part of the quarterly review workstreams |
| 6 | `data/DOC07.docx` | Senior Tax-Prep Volunteer Procs | 'Tax'-keyword volunteer procedures - not Clara's own finances |

---

## Coverage against the 10 workstreams (from `../prompt_design_notes.md`)

| # | Workstream | Primary home/ support |
|---|---|---|
| 1 | Cross-book category reconciliation | XL01 (budget baseline) |
| 2 | Live balance sweep vs book balances | DF01 (bank statement) + XL01 |
| 3 | Portfolio holding walk | XL02 + DF02 (Meridian statement) |
| 4 | Allocation drift calculation | XL02 (target vs actual allocation) |
| 5 | Effective withdrawal rate | PPDF02 + DF01 + DF02 |
| 6 | Charitable giving audit (3 channels) | XL06 (giving log) + XL03 (tax view) |
| 7 | Resale income tally | (no home file - sources are amazon-seller + paypal + quickbooks mock_data) |
| 8 | Net worth statement | XL02 + DF01 + PPDF02 + DF08 (condo context) |
| 9 | Estate signing queue review | XL09 (inventory) + DF07 (review letter) |
| 10 | Draft pre-meeting note to Sheila | DOC08 (draft letter reference) |

---

**Copy result:** 12/12 required + 6/6 noisy = **18/18** copied successfully.