# Data folder

Mock API snapshots backing the artifacts described in `../artifact_description.md` and listed in `../artifacts_required.md`. All files live flat in this folder. Each file is named `{surface}__{snapshot}.json` so the connected service is visible at a glance. The snapshots are dated against a freeze point of **October 12, 2026 at 09:00 ET** (Monday morning, eight days before the October 20, 2026 sit-down with Maribel Santos, and before Amanda's 7pm Beginner class that evening). All figures, IDs, contact names, dollar amounts, and message text are synthetic.

## Files by surface

- **QuickBooks** — primary books of record for the studio practice.
  - `quickbooks__company_info.json`
  - `quickbooks__studio_pnl_ytd_2026.json`
  - `quickbooks__monthly_net_2026.json`
- **Xero** — parallel ledger maintained by CPA Priya Iyer. Square feed broke 2026-09-04 and Stripe feed has been intermittent since 2026-09-12, so the September net is currently understated here.
  - `xero__company_info.json`
  - `xero__studio_pnl_ytd_2026.json`
  - `xero__monthly_net_2026.json`
  - `xero__reconciliation_notes.json`
- **Plaid** — First Keystone Federal Credit Union balances and transactions across checking, household savings, and Studio Fund savings.
  - `plaid__accounts.json`
  - `plaid__balances_2026-10-12.json`
  - `plaid__transactions_recent.json`
- **Coinbase / Binance / Kraken** — small crypto position spread across three venues, earmarked but never moved into the Studio Fund.
  - `coinbase__portfolio.json`
  - `binance__portfolio.json`
  - `kraken__portfolio.json`
- **Alpaca** — brokerage watchlist with the auto-invest paused since July 2026 to push into the Studio Fund.
  - `alpaca__watchlist.json`
- **Square** — in-studio card terminal sales (drop-in, punch-card, four-week pass, private lesson deposits, costume co-pays, T-shirts, Halloween in-studio sign-ups).
  - `square__sales_summary_ytd_2026.json`
  - `square__halloween_in_studio_signups.json`
- **Stripe** — online payment rail (online class package auto-pay, online private lesson deposits, workshop tickets, three Halloween block-of-three prepays).
  - `stripe__transactions_ytd_2026.json`
  - `stripe__halloween_online_tickets.json`
- **PayPal** — informal class payments for three long-standing students still on friends-and-family.
  - `paypal__informal_transfers_ytd_2026.json`
- **HubSpot** — student CRM imported from old Mailchimp on 2026-06-08 and not maintained since. Carries 52 contacts tagged "active student" against the actual roster of 43.
  - `hubspot__student_roster.json`
- **Airtable** — working student roster and showcase tracking maintained by Nat Taveras. Authoritative roster of record.
  - `airtable__student_roster.json`
  - `airtable__showcase_tracking.json`
  - `airtable__costume_sizing.json`
- **Salesforce** — grant pipeline (five women-entrepreneur programs with deadlines stretching into 2027).
  - `salesforce__grant_programs.json`
  - `salesforce__activity_log.json`
- **Box** — grant paperwork repository.
  - `box__grant_documents_index.json`
- **LinkedIn** — grant announcements feed Amanda follows and one held draft post about the showcase.
  - `linkedin__grant_announcements_feed.json`
- **Zillow** — three candidate commercial spaces shortlisted for the dance academy.
  - `zillow__candidate_listings.json`
- **Monday** — live production board for the November 14 Fall Showcase at Santander Performing Arts Pavilion.
  - `monday__showcase_production_board.json`
- **Eventbrite** — Halloween Social advance tickets and the staged-not-live showcase event page.
  - `eventbrite__halloween_2026-10-31_tickets.json`
  - `eventbrite__showcase_2026-11-14_tickets.json`
- **Gmail** — `amanda.webb@Finthesiss.ai` inbox slice covering the studio, books, grants, showcase, Halloween, wedding, personal, and CEU threads relevant to the October 20 sit-down.
  - `gmail__inbox.json`
- **Google Calendar** — Amanda's personal, studio, hospital-mirror, and wedding calendars across the relevant window.
  - `google_calendar__schedule.json`
- **Mailchimp** — student newsletter audience and campaign history, plus two held drafts.
  - `mailchimp__newsletter_history.json`
- **Notion** — studio plan workspace index (Year One Recap, Capital Target Tracker, Grant Pipeline, Showcase working page, Halloween playbook, CEN tracker, MOH standup, audit log working page).
  - `notion__studio_plan_workspace.json`
- **Trello** — MOH planner board (Jess and Carmen's shared wedding board; Amanda's lane is MOH closeout).
  - `trello__moh_planner.json`
- **Airbnb** — Lancaster cottage booking for the night of October 16, 2026.
  - `airbnb__lancaster_booking.json`
- **BambooHR** — nursing credential ledger and CE hour record (read-only on Amanda's side; clinical hospital systems remain off-limits).
  - `bamboohr__credentials.json`
- **Google Classroom** — ENA online CE module ledger Amanda's hospital pays for. Source of truth for completed and in-progress CEN modules.
  - `google_classroom__ceu_modules.json`
- **OpenWeather** — Wyomissing-anchored forecast through October 21 plus event-day outlook for October 31 and November 14.
  - `openweather__reading_forecast.json`
- **Instagram** — three unread DMs from prospective students and four held post drafts. Public posts are draft-only by persona discipline.
  - `instagram__dm_drafts.json`

## Surfaces deliberately absent

- **Google Drive** — excluded by operator instruction.
- **Google Contacts** — excluded by operator instruction.
- **Laurel Creek hospital systems** — EMR, scheduling, payroll, internal staff messaging, and any clinical workflow surface are off-limits per persona discipline. Only the BambooHR credentials read and the read-only Google Calendar shift mirror cross the boundary.
- **Phone-only surfaces** — iMessage, SMS, Venmo (Amanda treats Venmo as a phone-only personal rail and does not pull it into the studio file), TikTok, and Facebook are not connected.
- **Carlos's accounts, Carol's accounts, Grandma Ruth's accounts, Derek's accounts, and any pet (Luna) thread** — explicitly out of scope for the business file.
- **Spotify** — referenced for the Halloween playlist but the live playlist is constructed in the Notion playbook draft (not seeded separately as a standalone file because Amanda only consumes Spotify, she does not pull structured data from it).
- **Ambient surfaces** — Discord, Twitch, YouTube, Vimeo, Reddit, Twitter, and the Obsidian private journal are not seeded as snapshot files. They are referenced in narrative where relevant (for instance, the Vimeo sync license quote for the "Carry" routine appears as a Gmail thread, not as a Vimeo snapshot).

## Three hidden cross-source conflicts seeded for the house-judgment rule

The artifact design names three cross-source disagreements an honest reconciliation must catch. The seed data carries all three. None are flagged in the data itself; the agent surfaces them by reading authoritative records against staler ones.

1. **Monthly net for September 2026 (books conflict).** QuickBooks carries September net at **$1,261.40**. Xero carries it at **$683.62**, a gap of $577.78 driven by the broken Square feed (2026-09-04) and the intermittent Stripe feed (2026-09-12). The full reconciliation is laid out in `xero__reconciliation_notes.json` and corroborated by the Priya Iyer Gmail thread `thr-2026-10-09-priya`. Five missing entries totaling $972 explain the broader YTD variance. QuickBooks is newer and authoritative until the Xero reconnect is completed.

2. **Halloween Social door count (rails conflict).** The Eventbrite advance ticket list carries 37 tickets, 32 unique buyers (three bought blocks of three). The Square in-studio sign-up sheet carries 18 separate sign-ups, six of which are also on the Eventbrite list. Each rail is authoritative for its own channel but neither alone is the door count. The true projected attendance is `37 + 18 − 6 = 49`.

3. **Active student roster (CRM conflict).** HubSpot carries 52 contacts tagged "active student" (a stale import from old Mailchimp on 2026-06-08 that was never pruned). Airtable, maintained by Nat Taveras and last edited 2026-10-11 18:42, carries 43 active. The 9-row gap breaks down to 2 known duplicates and 7 stale solo-visitors or moved-out names. Airtable is newer and authoritative.

## Stored-memory baselines that have aged out

Amanda's working memory still carries figures that the live data now contradicts. The agent should catch each one and log the resolution in the trust register.

- **"$12,000 in the Studio Fund."** Plaid balance at freeze is **$13,650.42**. The $12,000 was a late-September estimate.
- **"$400 per month transfer cadence."** The actual transfers were $450 (July), $450 (August), $500 (September). Priya Iyer's October 8 email asks whether the new $500 is the running rate.
- **"Forty to fifty students."** Airtable shows 43 active across the four classes. HubSpot shows 52 because of the unpruned Mailchimp import.

## Suggested read order for the agent

1. `quickbooks__*` for the authoritative books, then `xero__*` and the reconciliation notes to catch Conflict 1.
2. `plaid__*` for cash position. Compare the Studio Fund balance to the stored-memory $12,000 baseline.
3. `square__*`, `stripe__*`, `paypal__*` for revenue by rail across the four classes.
4. `airtable__student_roster.json` then `hubspot__student_roster.json` to catch Conflict 3 before any per-class contribution math.
5. `airtable__showcase_tracking.json` and `monday__showcase_production_board.json` for showcase status.
6. `square__halloween_in_studio_signups.json` and `eventbrite__halloween_2026-10-31_tickets.json` to catch Conflict 2.
7. `salesforce__grant_programs.json`, `salesforce__activity_log.json`, `box__grant_documents_index.json`, `gmail__inbox.json` (grant threads), and `linkedin__grant_announcements_feed.json` for the grant pipeline.
8. `zillow__candidate_listings.json` and `google_calendar__schedule.json` (walking-distance and conflict checks) for the spaces comparison.
9. `airbnb__lancaster_booking.json`, `trello__moh_planner.json`, and the Gmail wedding threads for the MOH closeout.
10. `bamboohr__credentials.json` and `google_classroom__ceu_modules.json` for the CEN renewal brief.
11. `notion__studio_plan_workspace.json` for what already exists in the workspace and where to write the new artifacts.
12. `gmail__inbox.json` cross-checked last, since it both seeds the conflicts and confirms the held-draft and outbound-comms posture.
