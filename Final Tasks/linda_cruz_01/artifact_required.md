# Artifact Requirements for linda-cruz-loan-review

This file records the artifact requirements and the artifact descriptions that follow directly from the PROMPT.md written for this persona. Every entry here traces back to a deliverable the prompt asks for. Nothing here widens scope beyond what the prompt requests.

The prompt asks for two saved work products, woven into the running prose as outcomes Linda wants (a brief she can lay in front of the accountant, and a private cash picture for herself with the estimated tax already subtracted). Both are captured below.

---

## Deliverable 1 — Loan-review brief for the practice accountant

**Save location**: `loan_review_brief.md` — Notion page in Linda's practice workspace (not shared outward, waiting for Linda's explicit go-ahead before any figure reaches the accountant).

### Artifact requirement

The brief must exist as a single reviewer-ready document Linda can put in front of the practice accountant at the November 2, 2026 loan-review meeting. To be considered done, it must carry:

- **A reconciled cash story for the trailing three-month window** drawing from the three payment rails Linda referenced (the front-desk in-person card reader, the online self-pay deposit flow, and the backup rail the handful of self-pay families still prefer), matched against the practice books' matched-deposit column, and cross-checked against the true dollars-landed in the practice operating account. The reconciliation must produce a plain list of every transaction where those views disagree, with a defensible ruling on which figure should stand and which should be treated as ghost, with a source citation per line.
- **An aging picture on the open provider-ticket queue with the largest commercial carrier**, bucketed by age (0-30, 31-60, 61-90, 90+ days), with dollar exposure per bucket, and a flag list of every ticket the carrier has marked "resolved" that the parents' own reports (via the booking-page message channel and the front-desk phone) contradict. Every contested "resolved" ticket must be corroborated with the specific parent-report evidence before it is flagged.
- **The true payroll cost trend over the trailing two quarters**, reconciled between the payroll rail and Carmen's staff schedule, expressed as fully-loaded cost per exam-room hour. Maria's proposed raise sized on an annualized frame. The two replacement paths for Jennifer's billing seat (temp billing service on a percent-of-collections basis vs. a full hire's loaded cost including hiring cost) modeled against the practice's actual trailing collections, with the cheaper path called out.
- **The overhead-adjusted break-even patient volume** under the landlord-signaled rent bump for the lease turn and the malpractice renewal rate that lives in the vendor-workspace renewal paperwork (not in the books, which are stale on that line). Medicaid weighted at what it actually cleared over the trailing three months, and self-pay weighted at the sliding-scale average rather than the rack card. Compared to the trailing actual visit volume.
- **A closing paragraph** on what the practice looks like carrying the standing loan balance into the lease turn if the rent bump lands as the landlord signaled — a straight, non-hedging read.

To be considered done, every headline figure in the brief must be defended twice from independent sources before it lands, and every figure the evidence for is genuinely thin must be held open in the ruling with the reasoning written out, rather than forced.

Judgment requirements the artifact must reflect:
- The prompt does not name which source wins in the reconciliation. The brief must arrive at the ruling on its own from the evidence and cite the winning source per contested line.
- No family name may appear anywhere near a billing exception. Every claim-aging reference that touches a family is aggregated or anonymized before the figure lands. HIPAA is absolute.
- Nothing in the brief is emailed, previewed, or sent to the practice accountant, to the largest commercial carrier, or to any external party before Linda has read the finished document and given explicit go-ahead.

### Artifact description

A structured, reviewer-ready markdown brief with the following shape:

- **Header block** — the practice name, the meeting date (November 2, 2026), and the trailing window covered by the reconciliation.
- **Section 1 — Reconciled cash story.**
  - Deposits by rail (card reader, online self-pay, backup rail) across the trailing three months, with a per-rail total.
  - Matched vs. actual comparison: rail totals vs. matched-deposit column vs. true bank feed.
  - Discrepancy table: one row per contested transaction with (transaction id, rail, matched-column figure, bank-feed figure, ruling, winning source).
  - Net trailing three-month deposits (the accountant-facing number), sourced and defended.
- **Section 2 — Claim-aging picture.**
  - Aging table by bucket (0-30, 31-60, 61-90, 90+ days), count and dollar exposure per bucket.
  - Contested-resolved list: one row per Jira "resolved" ticket the parent report contradicts, with the specific parent-report cite (Intercom thread reference or front-desk log reference) and the reason it is being held open in the aging.
- **Section 3 — Payroll cost trend.**
  - Fully-loaded cost per exam-room hour by quarter, with the payroll ↔ Trello reconciliation noted.
  - Maria's raise on an annualized frame: proposed bump, annualized cost with employer-tax and benefits load, and the framing of what a defensible raise looks like at the practice's current run rate.
  - Billing-seat replacement path model: temp billing service cost line (percent-of-collections × trailing collections × 12) vs. full-hire loaded cost line (salary + employer tax + benefits + one-time hiring cost), with the cheaper path called out and the reason.
- **Section 4 — Overhead-adjusted break-even.**
  - Fixed monthly overhead under the new inputs (rent line at signaled bump, malpractice line at renewal rate from the vendor-workspace envelope, other fixed lines unchanged).
  - Weighted-average per-visit revenue derived from the trailing visit mix (Medicaid share × actual cleared per-visit, self-pay share × sliding-scale average, commercial share × commercial per-visit).
  - Break-even patient volume; comparison to trailing actual volume; margin or gap called out.
- **Section 5 — Forward paragraph.** A single tight paragraph on what the practice looks like carrying the loan balance into the lease turn if the bump lands as signaled. No hedging, no bullet lists, just Linda's plain read for the accountant.
- **Sourcing discipline.** Every headline number carries a source citation and a "verified against" citation (twice-defended). Every open ruling is written out with reasoning.

---

## Deliverable 2 — Private cash picture for Linda

**Save location**: `private_cash_picture.md` — Notion page in Linda's private workspace, restricted (not shared to the practice workspace, not shared to the accountant, not shared to Marco unless Linda chooses).

### Artifact requirement

A short, decision-oriented cash view for Linda alone. To be considered done, it must:

- Cover the next-quarter horizon with the Q4 quarterly federal estimated tax payment already subtracted and the SBA loan service accounted for on its projected schedule.
- Show the room-to-move Linda actually has on Maria's raise and on Jennifer's billing-seat replacement decision.
- Name — plainly — the two floors that must not be touched: the household emergency-fund line (the Ally high-yield savings emergency cushion) and the $500/month supplement Linda sends her parents. Both are hard floors. Neither figures into the room-to-move.
- Close with an honest read on whether both decisions fit under the room-to-move, one fits, or neither fits.

Judgment requirements the artifact must reflect:
- The private cash picture is the number Linda actually makes the call on. It is not a copy of the brief. It is not intended for the accountant. It is not intended for anyone but Linda.
- The Ally emergency-cushion floor and the parents' monthly-supplement floor are inviolable — the room-to-move math must respect them as hard floors, not as soft targets.

### Artifact description

A short, decision-oriented markdown document with the following shape:

- **Opening line** naming the horizon (the quarter after the Q4 estimated tax payment lands) and the sourcing note that the cash-in projection is drawn from Deliverable 1's reconciled cash story.
- **Cash-in projection** — expected practice cash generation for the coming quarter, adjusted for any seasonal shape Linda has flagged (holiday-season slowdown, walk-in-clinic Saturdays).
- **Cash-out projection** — a compact line-item view: fixed household outflows, practice fixed outflows (rent at current line, malpractice at the new renewal rate, SBA loan service, other fixed lines), Q4 estimated tax subtracted, minus the two floors listed but not deducted from room-to-move.
- **Two floors named explicitly**:
  - Emergency-fund floor — the household high-yield savings emergency cushion. Untouchable.
  - Parents'-supplement floor — the $500/month sent to Roberto and Elena. Untouchable.
- **Room-to-move calculation** — `(cash-in projection − cash-out projection at floor-respecting baseline) = decision room`.
- **Two decision boxes**:
  - Maria's raise — annualized cost from Deliverable 1's payroll section; verdict on whether it fits under the room-to-move.
  - Billing-seat replacement — the cheaper path from Deliverable 1's replacement-path model with its annualized cost; verdict on whether it fits.
- **Closing line** — honest read: both fit / one fits (name which) / neither fits, with a one-sentence read of what that means for how Linda walks into the accountant meeting and how she talks to Maria.
