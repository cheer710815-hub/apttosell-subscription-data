# Data Dictionary — Follow-Up Event Registry 2026

Public release: **v0.2**

| Field | Meaning |
|---|---|
| apttosell_project_id | Stable AptToSell project identifier used to distinguish projects in the registry |
| project_name | Project name associated with the initial recruitment notice |
| initial_house_manage_no | Official housing-management number for the initial recruitment notice |
| first_followup_date | Date of the first identified follow-up supply event for the project |
| official_followup_notice_id | Identifier of the official follow-up notice associated with the recorded first follow-up event |
| canonical_official_source_url | Canonical ApplyHome official notice URL for the recorded follow-up notice |
| evidence_grade | Verification grade assigned to the registry entry: `PRIMARY_VERIFIED` or `ID_CORROBORATED_SECONDARY` |

## Evidence grade definitions

### PRIMARY_VERIFIED
The first follow-up event was verified against a primary official notice and its identifying information.

### ID_CORROBORATED_SECONDARY
The official notice identifier and canonical official notice URL were recovered and corroborated, while the entry was not classified as primary-verified during the v0.2 verification pass.

## Interpretation note

A follow-up event means that a later official supply event was observed for the project. It must not be interpreted as a cancellation rate, contract-failure rate, or unsold-housing rate.

## Persistent identifier

DOI: https://doi.org/10.5281/zenodo.23176906

License: CC BY 4.0
