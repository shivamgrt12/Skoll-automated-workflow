# Mesa Verde Paving and Gravel - Equipment Decommission Procedure (2013 revision)

**Procedure ID:** MV-PROC-DECOMM-v2013
**Space:** Equipment Maintenance
**Page ID:** CONF-EQ-PROC-DECOMM-2013-0117
**Revision:** 2013 revision (CANONICAL / ADOPTED)
**Stamped by:** J. Villareal (Equipment Manager)
**Stamped at:** 2013-08-02T09:00:00-06:00
**Adopted:** true
**Supersedes:** MV-PROC-DECOMM-v2001
**Superseded at:** null
**Superseded by:** null
**Signed page evidence:** scanned signature page attached in Confluence page attachment `signed_v2013_stampsheet.pdf`.
**Referenced by:** Jira project MV-EQ ticket bodies (post-2013), disposal readiness criteria page (`confluence_disposal_readiness_criteria.md`), per-unit interval specs page (`confluence_service_interval_specs.md`).

---

> This is the operative decommission procedure. Every disposal-prep ticket in Jira since the 2013 revision cutover references this by ID. Retain until formally superseded.

## 1. Scope

Applies to any Mesa Verde-owned wheel loader, motor grader, backhoe, or compactor that is being removed from active service for disposal, resale, or scrap.

## 2. Prerequisites

- Equipment Manager written approval (Confluence ticket or paper form).
- Unit on the yard, keys pulled, DEF/fluid supplies stocked for drain.
- Two-person crew minimum, one of whom is a Senior Diesel Mechanic or above.

## 3. Procedure

### 3.1 Hr-meter capture and photograph

Read hr-meter at start of shift. Photograph the meter face. This reading is the "last-service hr-meter" for the disposal file and MUST be logged in the Jira ticket body under `hr_meter_at_service`.

### 3.2 ECM data pull

Connect the OEM service tool (CAT ET, Deere Service Advisor, Komatsu KomTrax) and dump the last 90 days of fault codes and duty-cycle data to the disposal file. Save as `<asset_tag>_ecm_pull_<yyyy-mm-dd>.zip`.

### 3.3 Fluid drain

Drain engine oil, hydraulic oil, coolant, and fuel into labeled waste drums. Log volumes in the Jira ticket body.

### 3.4 Filter and hose removal

Pull all serviceable filters. Cap open hydraulic lines with the yellow plastic plugs. Do NOT reuse filters even if visually clean.

### 3.5 Hydraulic pressure log

With hydraulic system pressurized to spec one final time, record the hold pressures on main and secondary circuits. Log to Jira ticket body.

### 3.6 Battery disconnect

Disconnect and remove batteries. Battery cores to the recycler within 30 days.

### 3.7 DOT plate removal

Remove DOT plate and any state-issued serial tags. Photograph the machine's cast serial number pad before removal for the disposal file.

### 3.8 Cold-storage tag

Apply cold-storage yellow tag. Move unit to disposal-staging bay.

### 3.9 Jira ticket close

Close the Jira ticket with `resolution=Done`, procedure_ref=`MV-PROC-DECOMM-v2013`, and the hr-meter reading from step 3.1.

## 4. Records retention

- Jira ticket = system of record (post-2022 cutover).
- Photocopy of hr-meter photograph: attached to Jira ticket.
- ECM data pull ZIP: attached to Jira ticket.
- Paper worksheet no longer required; retained voluntarily by some techs.

## 5. Threshold rule

Consult `confluence_disposal_readiness_criteria.md`. Current threshold at the time of this revision is 12,000 hr for the wheel loader and grader classes.

## 6. Signoff

Stamped and adopted 2013-08-02 by:

- J. Villareal (Equipment Manager)
- R. Alvarado (Shop Foreman)
- Sophia Rivera (Senior Diesel Mechanic, witnessing)

Signed page evidence: attachment `signed_v2013_stampsheet.pdf` on this Confluence page. Confluence page history shows no edits to this section since 2013-08-02.

## 7. Change log

- 2013-08-02 - Initial adoption (J. Villareal).
- 2016-11-04 - Added CAT ET data-pull format note in 3.2 (no procedure-ID change).
- 2019-04-12 - Added `resolution=Done` requirement in 3.9 (no procedure-ID change).
- 2022-01-15 - Cutover note added: Jira ticket now system of record (no procedure-ID change).

## 8. Note on the 2024 draft

An unsigned draft revision (MV-PROC-DECOMM-v2024-draft) was opened by M. Chen (Compliance) on 2024-05-11 for potential threshold adjustment and additional environmental-line items. That draft has not been signed, has not been referenced by any Jira ticket, and does NOT supersede this procedure. Until the 2024 draft is signed and adopted, MV-PROC-DECOMM-v2013 remains canonical.
