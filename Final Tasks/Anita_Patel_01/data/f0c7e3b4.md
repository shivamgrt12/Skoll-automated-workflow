# Cardinal MyCare Portal — Metric Definitions & Counting Changelog

**Instrumentation owners:** Analytics Eng (Segment tracking plan) + Product Analytics
**Window covered:** 2026-09-01 through 2026-09-30 (last full calendar month)
**Purpose:** Record of how each headline number is counted, every dated change to a definition, and every place the tools disagree.

---

## Dated definition changes this month

1. **Active-user counting change (2026-09-21).** The tracking plan was re-mapped so that an active user is counted on a completed authenticated session rather than on any daily event ping. Series read on a single unchanged basis will show a step at this date; the pre-change and post-change segments sit on different bases and are not directly comparable.
2. **Booking-completion counting change (2026-09-14).** Before the 14th, `booking_completed` fired on the confirmation pageview. From the 14th it fires on the server API 200 (`appointments.create` success). The pageview basis runs ~6–9% above the server basis because of reloads and back-button navigation.
3. **`mvp_message_sent` renamed to `message_sent` (2026-09-14).** Tools keyed to the old event name show a gap for Sep 1–13. The two names cover the same behavior across the split date.

---

## Counting methodology by metric

| Metric | Definition | Tool the number is drawn from |
|---|---|---|
| Journey start | First step event of the journey per authenticated user, per day | Amplitude (`user_id`) |
| Journey completion | Server-confirmed success event (API 200 / processor webhook) | Segment plan v2.4 + Amplitude |
| New user | First-ever authenticated session on the portal | Amplitude cohorts |
| Returning user | `user_id` seen in a prior calendar week | Amplitude cohorts |
| Device | Client platform at session start (desktop web / mobile web / iOS app / Android app) | Amplitude / GA agree within 1% |
| Acquisition source | `reminder_email` if landed via reminder UTM within 24h, else `cold_direct` | Segment source property |

---

## Tool-by-tool figures (where they disagree)

### Appointment booking — completions
- **GA4:** 12,540 completions (confirmation pageview basis, session-level).
- **Mixpanel:** 11,905 completions (event basis, not user-deduped).
- **Amplitude:** 11,830 unique users completed (authenticated `user_id`).
- **PostHog:** 3,667 on its ~31% instrumented subset (~11,830 extrapolated).

### Messages sent
- Old event `mvp_message_sent` (Sep 1–13) plus new event `message_sent` (Sep 14–30). Read as one aliased series they total 12,760. A dashboard filtered to only `message_sent` under-reports Sep 1–13.

### New vs returning
- **GA4 (cookie basis):** 29% new / 71% returning.
- **Amplitude (`user_id` basis):** 22% new / 78% returning.

### Bill pay success
- Tools agree within ~1% because `payment_success` fires on the processor webhook. 4,730 successful payments on 8,600 starts (55.0%). Coincides with the Sep 12–18 payment incident (Datadog latency spike on `/api/billpay/authorize`, Sentry `PaymentMethodTokenizationError`).

### Sampling caveat
- **PostHog** instruments ~31% of traffic (self-hosted subset, consent-gated). Its absolute counts are not portal totals; use it for session-replay evidence only.

---

## Open items

- Pre-Sep-14 booking completions were backfilled to the server-confirmed basis using the `appointments.create` log, at 98.6% join coverage; ~1.4% of early bookings could not be matched to a server event.
- Whether to show the W3 (Sep 14–20) retention dip as an incident annotation. It is incident-driven, not seasonal.

*This file is append-only. Do not overwrite prior entries; add below with a dated line.*
