# Artifacts Description - Carlos Whitfield (carlos-whitfield_01)

**Total artifacts**: 40 files across 8 formats (csv, json, pdf, xlsx, tsv, docx, md, yml)
**Persona**: Carlos Whitfield, 72-year-old retired mechanical engineer, Beaverton, OR
**Prompt context**: Pre-appointment medical reconciliation, financial reconciliation, Garden Club year-end report, Oct 2026–Jan 2027 calendar consolidation, furnace replacement research

---

## Format Distribution

| Format | Count | Purpose |
|--------|-------|---------|
| CSV    | 7     | Tabular data - medications, budget, calendar, costs, conflicts |
| JSON   | 7     | Structured records - provider data, bank summary, checklists, scenarios |
| TSV    | 4     | Tab-delimited tables - pharmacy history, credit card, Garden Club, commitments |
| YML    | 6     | Configuration-style data - conflicts, financial snapshot, calendar, sources |
| MD     | 5     | Narrative reports and reference cards (including this file) |
| XLSX   | 4     | Formatted spreadsheets - medications, budget, Garden Club, calendar |
| DOCX   | 3     | Print-ready documents - reconciliation report, furnace analysis, executive summary |
| PDF    | 4     | Portable documents - wallet card, appointment packet, financial overview, Garden Club board report |

---

## Medical Artifacts (10 files)

### 1. medication_master_list.csv
- **Format**: CSV
- **Description**: Verified medication list with 9 entries. Columns: medication, dose, frequency, timing, prescriber, condition, last_filled, next_refill, notes.
- **Key data**: All medications cross-checked against provider records and Fred Meyer Pharmacy. Metoprolol flagged at 50mg (increased from 25mg Feb 2026).

### 2. medication_master_list.xlsx
- **Format**: XLSX
- **Description**: Formatted spreadsheet version of the medication list. Blue headers, yellow highlight on metoprolol row, allergy warning in red, conflict notice in orange.
- **Key data**: Same 9 medications with formatted presentation suitable for printing and handing to a provider.

### 3. provider_medication_records.json
- **Format**: JSON
- **Description**: Medication records as held by each provider - Dr. Sharma (PCP), Dr. James Whitfield (cardiology), Dr. Laura Chen (endocrinology), and Fred Meyer Pharmacy.
- **Key data**: Dr. Sharma's record shows metoprolol 25mg (outdated). All other sources show 50mg. Pharmacy dispensing confirms 50mg since February 2026.

### 4. pharmacy_dispensing_history.tsv
- **Format**: TSV
- **Description**: 21 prescription fill events from January through September 2026. Columns: fill_date, medication, dose, quantity, days_supply, prescriber, copay, notes.
- **Key data**: Tracks every fill including the February metoprolol dose increase and March atorvastatin generic switch.

### 5. medication_conflict_log.yml
- **Format**: YML
- **Description**: 3 identified conflicts across medication records.
- **Key data**: CONF-001 (metoprolol dose at Sharma, HIGH), CONF-002 (atorvastatin manufacturer change, LOW), CONF-003 (apixaban refill authorization running low, MEDIUM).

### 6. medication_reconciliation_report.md
- **Format**: Markdown
- **Description**: Full narrative reconciliation report with verified list, each conflict explained, pharmacy notes, and allergy information.
- **Key data**: Synthesizes all medication sources into one authoritative narrative.

### 7. medication_reconciliation_report.docx
- **Format**: DOCX
- **Description**: Print-ready Word document of the reconciliation report. Formatted with tables, section headers, and conflict callouts.
- **Key data**: Same content as the .md version, formatted for printing and presentation.

### 8. pre_appointment_checklist.json
- **Format**: JSON
- **Description**: Preparation tasks for each of the three specialist appointments (Oct 6 endocrinology, Nov 11 cardiology, Dec 9 PCP).
- **Key data**: HbA1c draw timing, Karen ride confirmation, apixaban refill auth renewal, metoprolol dose correction at Sharma's office.

### 9. prescription_refill_schedule.csv
- **Format**: CSV
- **Description**: Next refill date for each of 7 prescription medications. Columns: medication, dose, frequency, prescriber, last_filled, days_supply, next_refill, pharmacy, notes.
- **Key data**: Ensures no refill gaps during the Oct-Dec appointment period.

### 10. prescription_cost_analysis.csv
- **Format**: CSV
- **Description**: Budget vs. actual prescription costs. Monthly breakdown showing the impact of the metoprolol dose increase (+$8/mo) and atorvastatin generic switch (-$10/mo).
- **Key data**: Budgeted $185/mo, averaging $177/mo actual. Net annual savings of approximately $20 from the generic switch offsetting the dose increase.

---

## Financial Artifacts (9 files)

### 11. annual_budget_vs_actual_2026.csv
- **Format**: CSV
- **Description**: 15 expense categories with monthly actuals (Jan–Sep) vs. monthly budget. YTD totals and variance.
- **Key data**: YTD spending $17,613 vs. budget $18,288. Under budget by $681. Largest variance: utilities ($155 under) and home maintenance ($205 over, unbudgeted).

### 12. annual_budget_vs_actual_2026.xlsx
- **Format**: XLSX
- **Description**: Formatted spreadsheet with color-coded variance column (green = under, red = over), income section, and SUM formulas.
- **Key data**: Same data as CSV with Excel formatting for review at the kitchen table.

### 13. bank_transaction_summary.json
- **Format**: JSON
- **Description**: Account balances and transaction summaries for checking ($4,215.38), savings ($38,142.75), and Visa (paid in full monthly).
- **Key data**: Pension and Social Security deposits verified. No outstanding balances. Visa charges average $664/month.

### 14. credit_card_ytd_summary.tsv
- **Format**: TSV
- **Description**: Visa charges by category for each month, Jan–Sep. Total YTD: $5,975.
- **Key data**: Largest categories: groceries, dining, gas, prescriptions. All paid in full each month.

### 15. financial_snapshot_2026.yml
- **Format**: YML
- **Description**: Complete financial position - income, expenses, accounts, assets, net worth, furnace readiness assessment.
- **Key data**: Net worth approximately $825,858. Monthly surplus $1,494 average. Furnace replacement survivable from savings.

### 16. furnace_replacement_analysis.md
- **Format**: Markdown
- **Description**: Research-only analysis of furnace replacement costs, rebate potential, and savings impact.
- **Key data**: Cost range $4,500–$8,500. Rebates $1,400–$1,800 possible. Savings absorbs all scenarios. Recovery 3–6 months.

### 17. furnace_replacement_analysis.docx
- **Format**: DOCX
- **Description**: Print-ready Word document of the furnace analysis with tables and recommendations.
- **Key data**: Same as .md with formatted tables for options, scenarios, and next steps. Explicitly states no contractors contacted.

### 18. savings_durability_test.json
- **Format**: JSON
- **Description**: 5 scenarios testing savings impact - from baseline (no furnace) to emergency winter replacement ($9,000).
- **Key data**: Worst case leaves savings at $29,143. All scenarios survivable without IRA withdrawal or outside help.

### 19. financial_overview.pdf
- **Format**: PDF
- **Description**: Two-page financial overview with income, expense table, account balances, furnace readiness, and Rx cost analysis.
- **Key data**: Portable summary for kitchen-table review.

---

## Garden Club Artifacts (6 files)

### 20. garden_club_donations_2026.csv
- **Format**: CSV
- **Description**: 13 income entries totaling $2,270. Categories: dues ($740), fundraisers ($1,305), donations ($200), adjustments ($25).
- **Key data**: Every entry traced to deposit receipt or Square transaction.

### 21. garden_club_expenses_2026.tsv
- **Format**: TSV
- **Description**: 16 expense entries totaling $1,261.80. Categories: venue ($240), seeds/plants ($278.20), supplies/tools ($157.15), printing ($113.05), booths ($60), insurance ($180), refreshments ($63.40), Square fees ($45), misc ($25).
- **Key data**: Carlos's reimbursed Visa charges flagged as such.

### 22. garden_club_reconciliation.json
- **Format**: JSON
- **Description**: Bank reconciliation - ledger balance matches bank balance at $2,850.70. Difference: $0.00.
- **Key data**: Every Square deposit verified. Every check cleared.

### 23. garden_club_financial_summary.yml
- **Format**: YML
- **Description**: Board-ready summary with income/expense breakdown, net income, and projected year-end balance.
- **Key data**: Net income $1,008.20. Projected Dec 31 balance: $2,705.70 after Q4 expenses.

### 24. garden_club_year_end_report.xlsx
- **Format**: XLSX
- **Description**: Three-sheet workbook (Income, Expenses, Summary) formatted for board presentation. Green theme.
- **Key data**: Complete year-end treasurer's report. "An engineer kept the books."

### 25. garden_club_board_report.pdf
- **Format**: PDF
- **Description**: Print-ready board report with income/expense tables, percentages, and year-end projection.
- **Key data**: Same data as XLSX in portable format for Maggie and the board.

---

## Calendar Artifacts (7 files)

### 26. calendar_oct2026_jan2027.csv
- **Format**: CSV
- **Description**: Approximately 60 events across October 2026 through January 2027. Columns: date, day, time, event, category, location, notes.
- **Key data**: Every appointment, family date, standing commitment, and deadline in one flat file.

### 27. calendar_oct2026_jan2027.xlsx
- **Format**: XLSX
- **Description**: Color-coded calendar spreadsheet. Medical (light red), Family (light blue), Routine (light green), Financial (light yellow). Critical events bolded.
- **Key data**: Same events as CSV with visual formatting for quick scanning.

### 28. calendar_medical_prep.json
- **Format**: JSON
- **Description**: 9 medical events with detailed preparation tasks, required items, and completion status.
- **Key data**: HbA1c booking, Karen ride confirmation, medication list printing, refill auth renewal.

### 29. calendar_family_events.yml
- **Format**: YML
- **Description**: Family events Oct–Jan: Kevin birthday (Oct 24), June anniversary (Nov 14), David birthday (Nov 18), Carlos birthday (Dec 8), Maya art show (Dec 12), Maya birthday (Dec 14), Christmas shipping (Dec 15).
- **Key data**: Gift prep timelines and handling notes (e.g., June anniversary: Carlos handles himself).

### 30. calendar_standing_commitments.tsv
- **Format**: TSV
- **Description**: 19 recurring commitments - daily (walk, meds), weekly (Kevin call, workshop, Karen dinner), monthly (Garden Club, Doug lunch, Visa review, Rx check), quarterly (medical appointments).
- **Key data**: Complete standing schedule that forms the structure of Carlos's weeks.

### 31. calendar_full_view.md
- **Format**: Markdown
- **Description**: Month-by-month table view of Oct 2026 through Jan 2027 with bold highlighting for critical dates.
- **Key data**: The "laid flat" calendar view Carlos asked for - everything visible at once.

### 32. appointment_prep_packet.pdf
- **Format**: PDF
- **Description**: Three-page prep packet, one page per specialist appointment. Tasks, medications to discuss, questions to ask, and critical actions.
- **Key data**: Metoprolol conflict flagged for Dr. Sharma visit. Apixaban refill renewal flagged for cardiology.

---

## Consolidated Artifacts (8 files)

### 33. conflict_resolution_log.csv
- **Format**: CSV
- **Description**: 7 conflicts identified across medical, financial, and calendar domains. Columns: ID, domain, description, source_a, source_b, trusted_source, reasoning, action_required, priority.
- **Key data**: Every disagreement between sources documented with which was trusted and why.

### 34. data_sources_verified.yml
- **Format**: YML
- **Description**: Inventory of 16 sources checked (providers, pharmacy, bank, credit card, budget, pension, SS, Garden Club, calendar, persona files) and 4 not checked (with reasons).
- **Key data**: Full chain of custody for every number in the artifacts.

### 35. task_completion_status.json
- **Format**: JSON
- **Description**: Maps each of the 9 tasks from Carlos's prompt to the artifacts that fulfill them, with 7 remaining action items requiring his decision.
- **Key data**: Tracks what was asked and what was delivered.

### 36. shipping_deadlines_denver.yml
- **Format**: YML
- **Description**: UPS ground cutoff December 15 for Denver Christmas shipments. Backup options (Priority Mail, UPS 3-Day).
- **Key data**: Gift prep timeline starting late November.

### 37. allergy_and_emergency_card.md
- **Format**: Markdown
- **Description**: Wallet-sized reference card with allergies, conditions, medications, ICE contacts, and medical escalation path.
- **Key data**: Penicillin allergy, blood thinner alert, Karen/Kevin ICE numbers, provider contacts.

### 38. medication_wallet_card.pdf
- **Format**: PDF
- **Description**: Formatted wallet card with conditions, all medications in table format, emergency contacts, and allergy warning.
- **Key data**: Print-and-carry document for appointments or emergencies.

### 39. executive_summary.docx
- **Format**: DOCX
- **Description**: The kitchen-table document. Everything in one place - medical status, financial picture, Garden Club books, calendar, furnace math, and action items.
- **Key data**: The single document that answers "how do things stand" across every domain Carlos asked about.

---

## Data Integrity Notes

- All medication data cross-checked against MEMORY.md (Health & Wellness section) and HEARTBEAT.md (medication schedules).
- All financial figures derived from MEMORY.md (Finance section) with realistic monthly variation applied.
- All calendar dates verified against HEARTBEAT.md (Upcoming Events & Deadlines, Recurring Events, Annual dates).
- All relationship references verified against MEMORY.md (Key Relationships) and AGENTS.md (Data Sharing Policy).
- Conflict resolution follows the principle stated in the prompt: "go with whichever is newest and most authoritative" and disclose the reasoning.
- No contractors contacted. No appointments booked. No communications sent. Research and reconciliation only.
