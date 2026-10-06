# Methodology — Follow-Up Event Registry 2026

## 1. Scope and unit of observation

Version 0.2 contains one public row for each project with an identified first observed follow-up supply event.

One row represents the first observed follow-up event for one project. Later follow-up events are not materialized as separate rows in this release.

## 2. Source framework

The registry was constructed from AptToSell's 2026 project-level subscription and follow-up analysis, which is based on official Korea Real Estate Board ApplyHome recruitment and follow-up notices.

The public release preserves the initial housing-management number and an identified official follow-up notice ID so that the relationship can be checked against the official notice system.

## 3. Public fields

The public v0.2 file contains exactly these seven fields:

- `apttosell_project_id`
- `project_name`
- `initial_house_manage_no`
- `first_followup_date`
- `official_followup_notice_id`
- `canonical_official_source_url`
- `evidence_grade`

## 4. First follow-up event rule

For each project, AptToSell records the earliest follow-up supply event identified after the initial recruitment notice.

`first_followup_date` is the date associated with that first identified follow-up event.

The registry does not claim that later follow-up notices are absent; v0.2 is intentionally a first-event registry.

## 5. Evidence grades

### PRIMARY_VERIFIED

The first follow-up event was verified against a primary official notice and its identifying information.

### ID_CORROBORATED_SECONDARY

The event's official notice identifier and canonical official notice URL were recovered and corroborated, while the full event record was not reclassified as primary-verified during the v0.2 verification pass.

These grades describe evidence strength for the registry entry. They are not measures of project quality, sales performance, cancellation, or unsold inventory.

## 6. v0.2 verification summary

Public v0.2 contains 103 project rows.

- Official follow-up notice IDs present: 103 / 103
- Canonical official source URLs present: 103 / 103
- `PRIMARY_VERIFIED`: 13
- `ID_CORROBORATED_SECONDARY`: 90

## 7. Interpretation limits

An observed follow-up supply event does **not** equal a contract-failure rate, cancellation rate, or unsold-housing rate.

A later notice can arise from different supply circumstances and should be interpreted only as an observed later official supply event unless a separate analysis verifies the underlying cause.

## 8. Versioning and citation

Current public release: **v0.2**

Persistent identifier:

https://doi.org/10.5281/zenodo.23176906

License: **CC BY 4.0**

Recommended citation:

Kim, Eun. *AptToSell Follow-Up Event Registry 2026*, version 0.2, 2026-10-06. AptToSell. CC BY 4.0. https://doi.org/10.5281/zenodo.23176906
