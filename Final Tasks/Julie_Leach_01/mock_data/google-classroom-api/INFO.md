# google-classroom-api

**Status.** Persona-connected surface (per `julie-leach/TOOLS.md`, student materials and state-board prep handouts). The SKOLL_GK Mock Data Generator does not carry an env schema or builder for Google Classroom.

**Julie-side canonical carrier.** The cohort roster lives in `Julie Leach\Mock Data\airtable-api\records_cohort_roster.csv` (16 students matching STU-201 through STU-216) and can be joined against a Google Classroom mock via student_id.

**Contract.** If a Google Classroom mock is added, it must expose the cohort as a course roster with the same 16 student IDs and matching first_name/last_name pairs from the airtable table.
