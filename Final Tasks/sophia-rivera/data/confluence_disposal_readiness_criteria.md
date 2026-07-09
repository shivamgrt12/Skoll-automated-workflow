# Mesa Verde Paving and Gravel - Disposal Readiness Criteria

**Space:** Equipment Maintenance
**Page ID:** CONF-EQ-CRIT-DR-2013-0129
**Owner:** J. Villareal (Equipment Manager)
**Last edited by:** J. Villareal
**Last edited at:** 2023-04-18T11:04:00-06:00
**Applies to procedure:** MV-PROC-DECOMM-v2013
**Adopted:** true

---

> Threshold and readiness rules used to classify Mesa Verde equipment for disposal, resale, or continued service.

## 1. Hr-meter threshold rule

For wheel loader and motor grader classes on the 1990s line, the disposal readiness threshold is:

**12,000 hr on the last-service hr-meter reading.**

- **Under 12,000 hr:** unit is in-service. Not eligible for disposal on hr-meter grounds alone. Verdict tag: `clean`.
- **At or above 12,000 hr:** unit is flagged for decommission per MV-PROC-DECOMM-v2013. Verdict tag: `over_threshold`.

Backhoe and compactor classes have separate thresholds (see appendix); the 1990s line consultation does not scope to those.

## 2. Data source for last-service hr-meter

The last-service hr-meter comes from the most recent decommission-prep or PM service work order in Jira project MV-EQ, resolved by a Mesa Verde technician, with `procedure_ref=MV-PROC-DECOMM-v2013`.

**Order of precedence:**

1. Jira ticket in project MV-EQ, resolved, with procedure_ref match.
2. If no matching Jira ticket exists for a unit, use the Confluence per-unit spec page.
3. Confluence legacy shop-log files (`.log` in the archive attachments) are NOT authoritative and are retained for archival cross-reference only. They pre-date the 2022 Jira migration and were never reconciled at cutover.

## 3. Reconciliation rule

If a Jira ticket and a Confluence legacy shop log disagree on the last-service hr-meter for a unit, the Jira ticket wins. The Confluence legacy shop log entry is flagged as `unreconciled_legacy` on the disposal file and the unit is reviewed by a Senior Diesel Mechanic or the Equipment Manager before disposal.

## 4. Special case: CAT-966F S/N 7HK02184

This unit (MV-LDR-105) has a known unreconciled disagreement:

- Jira MV-EQ-4187 (2019-10-14, resolved by D. Ruiz, ticket sign-off by J. Villareal): 11,840 hr.
- Confluence legacy shop log `confluence_966f_service_history_legacy.log` (entry dated 2021-06-02, initials DR): 12,103 hr.

Per section 3 (reconciliation rule), the Jira ticket wins: **11,840 hr** is the operative last-service reading. Verdict under section 1: `clean` (11,840 < 12,000).

## 5. Verdict grid (recap)

| Last-service hr-meter | Verdict tag |
|---|---|
| < 11,000 | clean, comfortable margin |
| 11,000 - 11,999 | clean, watch on next service |
| 12,000 - 12,499 | over_threshold, standard decommission |
| >= 12,500 | over_threshold, expedited decommission |

## 6. Change log

- 2013-08-02 - Initial threshold set at 12,000 hr for 1990s wheel loader/grader classes.
- 2016-11-04 - Added order-of-precedence text in section 2.
- 2022-01-15 - Added section 3 reconciliation rule after Jira migration cutover.
- 2023-04-18 - Added section 4 CAT-966F 7HK02184 special-case entry.

## 7. Note on the 2024 draft

The unsigned MV-PROC-DECOMM-v2024-draft proposes lowering the wheel-loader threshold to 10,000 hr and the grader threshold to 11,000 hr. That draft is not adopted; the 12,000 hr rule in section 1 remains operative.
