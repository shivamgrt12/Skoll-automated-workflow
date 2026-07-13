# Subscriber Ledger Reconciliation Summary

Status: draft, awaiting Carlos Reed's approval
Reconciliation Date: January 24, 2027
Coverage: Reed Security Notes reader population, all connected newsletter, welcome, re-engagement, and transactional platforms.

## Reconciliation Rule

Newest opt-out wins. For any reader whose state disagrees across platforms, the most recent state-changing event (unsubscribe, hard bounce, opt-out, pause) is treated as authoritative regardless of which platform recorded it. A reader who was resubscribed after a later opt-out is treated as opted-out.

Tie-break order when no explicit state-changing event exists: primary newsletter platform (Mailchimp) reflects the send-list truth, welcome / segmentation and re-engagement destinations reflect the marketing state, transactional platforms are excluded from the opt-in determination.

## Population

- Unique readers reconciled: 2,412
- Deduplicated across five platforms by lowercased-email SHA-256 hash.
- Duplicate rows removed (same reader present on multiple platforms): 1,847 rows collapsed.

## Movement

- Active before reconciliation, active after: 1,894
- Active before reconciliation, moved to suppressed after: 291
- Suppressed before reconciliation, remain suppressed: 213
- New readers reconciled in from transactional-only history: 14

## Largest Drift Source

The re-engagement drip platform held the largest stale segment. 213 of the 291 readers moved from active to suppressed were sitting in an active re-engagement segment on that platform despite having unsubscribed through the primary newsletter platform in October 2026. The welcome-and-segmentation platform contributed a further 62. The remaining 16 came from disagreements between the two transactional platforms on hard-bounce history.

## Conflict Distribution

| Conflict Type | Count | Resolution |
|---|---|---|
| Primary newsletter unsubscribed, re-engagement still active | 213 | Suppressed |
| Primary newsletter subscribed, welcome-platform tagged unsubscribed | 62 | Suppressed |
| Hard bounce recorded on one transactional platform only | 16 | Suppressed |
| Engagement tier disagreement (no state conflict) | 148 | Trusted primary newsletter |
| Tag set drift | 331 | Union across platforms, primary newsletter tags authoritative on conflict |

## Open Findings

- 47 readers show a subscribed state on the primary newsletter platform but no engagement event across any platform in the last twelve months. Held as open. Recommendation on file: quiet-suppression review before the March 2027 send, no auto-action.
- 9 readers show conflicting timezone data between the welcome platform and the analytics event stream. Non-blocking for send-list determination. Flagged for the analytics reconciliation workstream.
- 3 email hashes match two distinct name records across platforms. Likely shared inbox. Flagged for manual review, held on the ledger under the primary newsletter platform's version.

## Send-List Statement

Under no circumstances does an email hash marked `unsubscribed`, `hard_bounce`, or `paused` in the reconciled ledger appear in the March 2027 Reed Security Notes newsletter, in any sponsor-facing communication, or in any outreach staged in the CRM. This ledger is the send-list gate. Monica Stevens's guest post send in Q1 2027 pulls from this ledger and only this ledger.

## Provenance

Reconciled ledger written to `subscriber_ledger_reconciled.csv` in this bundle. No live platform state was modified. All changes are ledger-side only. Platform sync to be performed by Carlos manually after approval.
