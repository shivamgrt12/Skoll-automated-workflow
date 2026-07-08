# TAVR Outcomes Study Protocol v3.2

**Study ID**: CCP-TAVR-2024-001
**Principal Investigator**: Jason Campbell, MD
**Co-Principal Investigator**: James Whitfield, MD, Lakewood Medical Research Center
**Coordinator**: Amanda Torres, RN, BSN
**Version**: 3.2 (Amendment 4 approved 2026-03-15)
**Sponsor**: Investigator-initiated, unfunded

## Study Sites

The multi center TAVR outcomes study runs across five clinical sites in three health systems:

- SITE-RM-01: Riverside Medical Center Jacksonville, main catheterization lab
- SITE-RM-02: Riverside Medical Center Jacksonville, Riverside South annex catheterization suite
- SITE-SM-01: Summit Heart Institute, primary structural heart program
- SITE-SM-02: Summit Heart Institute, satellite catheterization lab
- SITE-SJ-01: St Johns Cardiovascular Institute, main catheterization lab
- SITE-SJ-02: St Johns Cardiovascular Institute, St Johns Annex catheterization suite (relabeled 2026-04-08, previously listed as SITE-SJ-01B in older exports)

The two St Johns labels are separate clinical facilities. The spring relabel harmonized nomenclature but the physical labs are distinct and enrollment is counted independently.

## Enrollment Target

Target 500 patients across all sites over 36 months. Enrollment window opened 2024-11-01, closes December 2026.

## Objectives

Primary: 30-day mortality after transcatheter aortic valve replacement.
Secondary: 1-year MACE (major adverse cardiovascular events), procedural success, length of stay, readmission rate.

## Inclusion Criteria

- Age 65 or older
- Symptomatic severe aortic stenosis (AVA less than 1.0 cm2, mean gradient 40 mmHg or higher, or peak velocity 4.0 m/s or higher)
- STS-PROM risk score 3.0 or higher
- Informed consent obtained

## Exclusion Criteria

- Concomitant severe valvular disease requiring surgery
- Prior mechanical or bioprosthetic aortic valve
- Life expectancy under 12 months from non-cardiac condition
- Active endocarditis within 6 months
- Contraindication to antiplatelet or anticoagulant therapy

## Data Governance

De-identified enrollment data lives in the shared airtable base (base id `appTAVRStudy2024`). Line level participant identifiers stay inside the practice EHR. The airtable base carries site-level counts and demographics only.

No participant identifiers (MRN, DOB, name, address) appear in any airtable record. Identifiers are stored only in Riverside Medical Center and St. Francis Medical Center EHR systems, which are not connected to the assistant.

## Deliverables

- Quarterly enrollment report to the IRB (submitted by PI)
- Annual IRB renewal package (submitted by PI)
- Manuscript for Journal of Interventional Practice (target 2026 window)
