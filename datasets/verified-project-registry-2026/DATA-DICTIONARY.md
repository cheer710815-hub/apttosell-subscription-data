# Data Dictionary — AptToSell Verified Project Registry 2026

> Pilot schema. Field definitions may change before Version 1.0.

| Field | Meaning |
|---|---|
| index | Pilot row index |
| apttosell_project_id | Stable AptToSell internal project identifier |
| house_name | Housing project name |
| sido | Province / metropolitan city |
| sigungu | City / district |
| supply_address | Supply location |
| first_house_manage_no | First known housing-management number |
| first_announcement_date | First recruitment announcement date |
| initial_general_supply | Initial general-supply households |
| initial_applicants | Initial applicants |
| initial_competition_rate | Initial competition rate |
| cohort_year | Registry cohort year |
| followup_confirmed | Whether a later follow-up supply event was confirmed |
| latest_followup_date | Latest confirmed follow-up date in the pilot |
| data_status | Current verification state |
| source_initial | Source for initial project / competition facts |
| source_followup | Source for follow-up confirmation |

## Planned Version 1.0 additions

- canonical_house_name
- official_source_system
- official_notice_no
- official_source_url
- project_identity_status
- duplicate_review_note
- verified_date
- publication_ready


## Pilot v0.3 verification fields

| Field | Meaning |
|---|---|
| identity_verification_status | Verification level for project identity and initial notice facts |
| competition_verification_status | Verification level for applicant / competition-result facts |
| official_initial_source | Primary-source recruitment document or official project source |
| source_initial_reference | Existing supporting source retained for traceability |
| verification_note | Field-level verification caveat |
| verified_date | Date of the latest source verification |
