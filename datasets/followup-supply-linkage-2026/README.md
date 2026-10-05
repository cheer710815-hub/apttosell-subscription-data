# AptToSell Follow-Up Supply Linkage 2026 — Pilot

> Status: **linked pilot / working dataset**. This package does not create a new DOI and does not replace the existing competition/follow-up analysis release.

This dataset connects AptToSell's 2026 competition/follow-up project table to the stable `apttosell_project_id` registry.

## Snapshot

- Project cohort: **196**
- Project-ID matches: **196 / 196**
- Unmatched: **0**
- Projects with observed follow-up supply in the project table: **103**
- Projects with first-priority competition rate ≥10:1: **44**
- Follow-up supply observed among ≥10:1 projects: **19**
- Existing analysis DOI remains: https://doi.org/10.6084/m9.figshare.34064439

## Important interpretation

`followup_supply_observed = true` means a later residual-unit, no-priority, or discretionary/follow-up supply notice was linked to the original project within the observation framework.

It does **not** mean:

- contract failure rate
- unsold rate
- cancellation rate
- the share of households that failed to contract

## Main file

- [apttosell-followup-projects-with-project-id-pilot-v0.1.csv](./apttosell-followup-projects-with-project-id-pilot-v0.1.csv)

## Join rule

The existing project table was joined to the verified-project-registry pilot by `house_manage_no`. The original official identifier is retained alongside the AptToSell project ID.

## Why this exists

The original analysis is already a published research asset. This linkage layer lets future price, payment, follow-up, and project-history datasets refer to the same project entity without mutating the frozen DOI release.

## Release decision

No new DOI is assigned to this linkage pilot. Cite the existing analysis DOI for the published competition/follow-up study and use this package only as the project-identity crosswalk.
