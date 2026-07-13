# Q1 2027 KPI Narrative - Reed Security Notes

Status: draft, awaiting Carlos Reed's approval
Coverage Window: February 8, 2027 through June 1, 2027
Reader: Monica Stevens (primary), Carlos Reed (review)

## Source of Truth

The event stream is the source of truth. Four downstream analytics destinations were reconciled against the event stream and disagreed with each other on Q4 2026 unique-reader counts by up to eighteen percent. The event stream itself was used for every count on the dashboard. Where a destination platform is referenced, it is a source of qualitative segmentation only, not of counts.

## Five KPIs

### 1. Reconciled Active Subscribers - 2,121

Unique readers marked subscribed in the reconciled ledger written on January 24, 2027. This is the send-list size for the March 2027 newsletter and the only reader-count number Monica should quote externally. It is 291 lower than the raw pre-reconciliation figure of 2,412 because the reconciliation moved unsubscribed and hard-bounce rows out of the active set.

Movement threshold for Monica to act: none. This number is the gate. Do not send to more than this number.

### 2. Q1 2027 Engaged Reader Rate - 47 percent

Share of the reconciled active subscribers who opened, clicked, or engaged with any Reed Security Notes surface (newsletter, post, download) during Q4 2026. Baseline for Q1 2027. Rationalized against the event stream after reconciling four downstream analytics destinations.

Movement threshold: if the Q1 2027 send lands under 38 percent engaged rate, Monica routes a note to Carlos before drafting the Q2 2027 outline. Under 30 percent is a hold-for-Carlos escalation.

### 3. Q4 2026 Post Unique Readers - 3,847

Unique readers who reached the Splunk dashboards post published December 31, 2026, measured on the event stream over the seventy-two hours following publish. This is the baseline for the March 2027 guest post. Historical Q4 posts have run in the 3,200 to 4,100 range.

Movement threshold: Monica's Q1 2027 guest post under 2,800 unique readers in the same seventy-two-hour window is a hold-for-Carlos escalation. Over 4,500 is a note to Carlos, no action, so he can update the sponsor deck on his return.

### 4. Sponsorship Realized Revenue - $48,100 (Q4 2026)

Settled sponsorship revenue for Q4 2026 pulled from the payment processors. This number sits behind the sponsor book and drives the Q1 2027 P&L. It is not for Monica. It is on this dashboard as a reference tile for Carlos only, so the KPI view stays on one page.

Movement threshold: not applicable during leave. Frozen until Carlos returns June 2027.

### 5. Open Reader-Support Tickets - 14

Unique open tickets across the three help-desk platforms after deduplication and after closing tickets already answered somewhere else. Twelve of the fourteen are on SIEM dashboard exports. Two are on detection-rule downloads. All fourteen carry a routing tag: Monica-actionable or hold-for-Carlos.

Movement threshold: if open ticket count crosses 30 during the leave window, Monica escalates to Jason Wu with a summary. If any single ticket has been open more than fourteen days, Monica routes to the hold-for-Carlos queue and does not attempt a technical reply.

## What This Dashboard Is Not

This dashboard is not the twenty-panel view Carlos runs on the WordPress admin plus the Segment console plus the sponsor CRM. It is deliberately narrower. Monica needs five numbers to steer March 2027. Twenty numbers is noise for someone running the blog for one quarter.

## Reconciliation Notes

- Amplitude, Mixpanel, PostHog, and Google Analytics disagreed with each other on Q4 2026 unique readers by up to 691 readers on the same time window. All four were set aside for count purposes. The event stream was trusted.
- The reconciled subscriber ledger (2,121 active) disagrees with the raw primary newsletter export (2,412) by 291. The ledger is authoritative for send-list purposes. The 291 delta is the recovered stale-segment population from the re-engagement platform.

## Open Findings on the Dashboard

- Engaged reader rate calculation assumes the Q4 2026 engagement window covers October 1, 2026 through December 31, 2026. Two of the destinations disagree on the November-December boundary due to a timezone drift. Event stream is trusted, drift documented, no action.
- The 3,847 Q4 2026 post unique-reader figure includes referral traffic from a LinkedIn share on January 3, 2027 that carried over the seventy-two-hour window. Held as an open finding, not adjusted.
