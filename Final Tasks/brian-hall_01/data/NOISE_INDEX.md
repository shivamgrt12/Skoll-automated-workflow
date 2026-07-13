# NOISE_INDEX.md - stale snapshots and noise map

This directory holds flat local snapshots that Brian and Karen keep as
working memory alongside the live connected services. Some of these
snapshots have drifted from the live source of truth. That is expected
and normal for personal working files. When a snapshot in `data/` and a
live connected API disagree on a number, a date, or a status, the live
API wins. This file names the places where drift lives so the trip
brief, the financial snapshot, and the lab readiness deliverable read
from the right source.

## Baseline standing rule

- Bank feed authoritative for cash position, cleared payments, Q3
  estimated tax clearing, buildout reserve balance.
- Live Google Calendar authoritative for confirmed events including the
  twins pediatric checkup with Dr Keisha Monroe.
- Live BambooHR and clinic scheduling authoritative for staff coverage.
- Live Xero and QuickBooks authoritative for project accounting.
- Live Plaid authoritative on any transaction date, amount, or account
  balance where a `data/` seed carries a memory figure.

Where a local seed carries a rounded mental figure, treat the seed as
context, not as a reconciled ledger read.

## Where snapshots may lag the live source

1. Q3 estimated tax mental baseline in `02_q3_tax_estimate_note.txt`
   carries a rounded per-installment figure (approximately five thousand
   eight hundred dollars) that Brian has kept penciled from prior
   quarters. The three actual Q3 clearing lines live in the Plaid feed
   as separate Federal and Georgia state entries. When those two views
   disagree, the Plaid clearing lines are authoritative and the seed
   figure is a stale mental baseline. Do not reconcile the seed in
   place; narrate the delta in the financial snapshot.

2. Lab buildout spend baseline in `04_lab_buildout_status_stale.md`
   carries an approximate spend-to-date figure (approximately fifty-two
   thousand dollars against the one hundred twenty thousand dollar
   approved budget). Live sources are the Peak Performance PT operating
   account, the lab buildout reserve, and Darren's running invoice log
   from Apex Build Group. When those disagree with the baseline seed,
   the live feeds win. Do not reconcile the seed in place; narrate the
   delta in the financial snapshot and the lab readiness deliverable.

3. Twins pediatric checkup hold in `05_twins_checkup_reminder.ics` and
   in `29_karen_calendar_export_stale.ics` shows an October fifteenth
   tentative slot with Dr Keisha Monroe. This is a held slot from an
   earlier planning cycle. The live Google Calendar view and any
   clinic-side payment record are authoritative for whether the
   checkup has already been completed or is still pending. Either way,
   the checkup must sit outside the Oct 22-25 Houston trip window per
   PROMPT. Do not confirm the Oct 15 date from these seeds alone.

## Local-only working files

- `01_trip_planning_scratch.md` - Brian's working notes; not a
  substitute for the live options that the trip brief will actually
  pull from Amadeus, Airbnb, Google Calendar, and QuickBooks.
- `03_household_budget_october.csv` - planned budget row set, not
  actuals. Actuals come from Plaid for the household accounts and from
  the operating account for clinic categories.
- `06_karen_pharmacy_shifts_oct.tsv` - Karen's shift file as she has it
  penciled. Her employer schedule is not connected here. Any conflict
  around the Oct 22-25 window has to route through Karen directly.
- `10_cookout_menu_brainstorm.md` - Brian's protein and menu working
  ideas for the Saturday cookout with Linda. Nothing to send.
- `11_apex_buildout_punchlist.md` - working punch list; Darren's
  running list is authoritative on the coordination side.
- `12_vald_equipment_pending.json` - Ryan Kimura equipment package in
  the exploration column; nothing committed, nothing invoiced.
- `20_flight_preferences.md` - anchors and preferences; the actual
  flight options come from Amadeus at brief-build time.
- `24_sba_loan_notes.md` - Live Oak Bank SBA equipment tranche in the
  exploration column; nothing drawn, nothing signed.
- `32_bookkeeping_reconciliation_notes.md` - reconciliation plan; the
  actual balances and Q3 clearing lines come from Plaid at
  snapshot-build time.

## Noise items to leave alone during this task

- `26_piedmont_dpt_student_schedule.tsv` - Piedmont DPT rotation
  schedule is clinic-side context and not part of trip planning. Listed
  here because it is easy to over-index on it.
- `27_crossfit_buckhead_matt_baker.md` - Matt Baker community context
  and the Fall Throwdown constraint; the anchor for scheduling is file
  15 not this file.
- `28_atlanta_firebirds_contract_summary.md` - Firebirds contract
  context; do not raise renewal during the Oct 22-25 window.
- `31_twins_school_calendar_notes.md` - Atlanta Global Academy notes;
  Karen handles the school-app absence notification, not the assistant.
- `33_notion_lab_wiki_index.md` - workspace index; do not create Notion
  pages during the trip window.

## What never leaves this directory

- No patient identifying content anywhere ever. Files 08, 26, 33, and
  35 explicitly restate this.
- No clinic revenue or invoice detail into family drafts (file 09).
- No Ring, Nest, or home device history into external comms (file 22).
- No PHI on J.H. or any patient in Notion, Jira, Airtable, HubSpot,
  Salesforce, Mailchimp, or WhatsApp (files 08, 18, 33, 34, 35).
