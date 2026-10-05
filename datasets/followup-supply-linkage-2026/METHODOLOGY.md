# Methodology — Follow-Up Supply Linkage 2026

## Unit of observation

One row represents one original 2026 project-level cohort record from the existing AptToSell competition/follow-up analysis.

## Join key

Primary join:

`house_manage_no`

Added internal key:

`apttosell_project_id`

The official housing-management number is preserved and is not replaced.

## Follow-up interpretation

Follow-up supply is an observed later supply event linked to the project. It is not interpreted as a contract-failure or unsold-household rate.

## Reproducibility rule

The original Figshare/analysis files are not rewritten. This pilot adds the stable project ID in a separate derived file.

## Verification gate

A successful join does not automatically upgrade the underlying competition or follow-up evidence quality. Verification status remains governed by the source dataset and the project registry.
