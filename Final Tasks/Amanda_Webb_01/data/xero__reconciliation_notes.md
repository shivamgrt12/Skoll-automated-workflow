# Xero — Reconciliation Notes

- **service:** Xero
- **report_type:** System Notes — Reconciliation Variance vs QuickBooks
- **org_id:** xero-aw-instruction-2026
- **generated_at:** 2026-10-12T09:11:48-04:00
- **note:** These are not Amanda's notes. These are the Xero system's bank-feed integration status messages and the agent's job is to read them, compare against QuickBooks, and decide which ledger is the trusted source for the September and October figures.

## feed_status_alerts

- **xero-feed-7732**
  - feed: Square
  - raised_at: 2026-09-04T02:14:00-04:00
  - severity: warning
  - message: Square OAuth token expired. No transactions imported since 2026-09-03. Visit Settings > Connected Apps > Square > Reconnect to resume.
  - user_acknowledged: False
- **xero-feed-7741**
  - feed: Stripe
  - raised_at: 2026-09-13T02:12:00-04:00
  - severity: info
  - message: Stripe payout 2026-09-14 did not import due to upstream timeout. Manual entry required.
  - user_acknowledged: False
- **xero-feed-7758**
  - feed: Stripe
  - raised_at: 2026-09-29T02:10:00-04:00
  - severity: info
  - message: Stripe payout 2026-09-28 did not import due to upstream timeout. Manual entry required.
  - user_acknowledged: False

## known_missing_entries_when_compared_to_quickbooks

- **(entry)**
  - date: 2026-09-14
  - source: Stripe payout
  - net_amount_should_be: 295.4
  - memo: Three class-package purchases (Intermediate Wed monthly auto-pay batch). Present in QuickBooks Stripe feed at 03:14 the next morning.
- **(entry)**
  - date: 2026-09-22
  - source: Square deposit
  - net_amount_should_be: 97.88
  - memo: One walk-up Saturday Open class drop-in ($22), one Beginner Mon punch-card renewal ($80), less Square processing fee.
- **(entry)**
  - date: 2026-09-28
  - source: Stripe payout
  - net_amount_should_be: 284.7
  - memo: Two private-lesson deposits and one Eventbrite-routed Halloween prepay block.
- **(entry)**
  - date: 2026-10-03
  - source: Square deposit
  - net_amount_should_be: 49.5
  - memo: Saturday Open class, two drop-ins.
- **(entry)**
  - date: 2026-10-07
  - source: Square deposit
  - net_amount_should_be: 48.0
  - memo: Wednesday Intermediate, one drop-in plus tip.
- **total_variance_vs_quickbooks:** 972.0
- **note_on_priority:** QuickBooks has the live Square and Stripe feeds and is the live primary going forward. Xero needs the Square reconnect and the two Stripe payouts entered manually before the October close. This is reconciliation work, not a real discrepancy in the underlying revenue.
