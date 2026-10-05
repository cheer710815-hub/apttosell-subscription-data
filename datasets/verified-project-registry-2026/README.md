# AptToSell Verified Project Registry 2026 — Pilot

> Status: **work in progress / pilot**. This is not a DOI release and does not claim national completeness.

This pilot defines a stable project-identity layer for AptToSell's 2026 housing-subscription datasets.

The purpose is to keep one reusable project identifier across competition-rate, follow-up supply, price, payment-condition, and later derived datasets, so the same apartment project is not treated as a different entity each time it appears in a new analysis.

## Pilot snapshot

- Snapshot date: **2026-10-05**
- Pilot rows: **2**
- Data status: **VERIFIED**
- Cohort year: **2026**

Current pilot projects:

1. 구리역 하이니티 리버파크
2. 해링턴 플레이스 노원 센트럴

## Core identifier

The internal identifier format is:

`ATS-YYYY-REGION-NNNNNN`

Examples:

- `ATS-2026-GG-000001`
- `ATS-2026-SEOUL-000001`

The identifier is intended to remain stable even when a project later receives separate residual-unit, follow-up supply, or other notice identifiers.

## Pilot file

- [apttosell-verified-projects-pilot-v0.2.csv](./apttosell-verified-projects-pilot-v0.2.csv)

## Important limitation

The current source URLs in this early pilot are not yet all official ApplyHome sources. Version 1.0 must not be released until project identity and first-announcement facts are re-verified against official or primary-source records.

## Relationship to existing AptToSell datasets

This registry is designed to become the join layer between:

- competition-rate data
- follow-up supply data
- housing-type / price data
- pre-move-in funding data
- future notice-correction or contract-condition datasets

## Release decision

No DOI is assigned to this pilot.

A future public release requires:

- official-source verification of project identity
- duplicate-resolution rules
- stable region coding
- documented handling of renamed projects
- clear rules for multiple housing-management numbers
- coverage statement and denominator


## Primary-source re-verification — 2026-10-05

Both pilot projects now have a primary-source recruitment document or project-owner source linked for identity verification.

- **구리역 하이니티 리버파크** — official DL E&C / eLife project materials and recruitment notice
- **해링턴 플레이스 노원 센트럴** — official project-hosted recruitment notice PDF

The registry now separates **project identity verification** from **competition-result verification**.

For both pilot rows, project identity is `PRIMARY_VERIFIED`. The competition totals remain `SECONDARY_VERIFIED` until the corresponding official ApplyHome result record or equivalent primary result evidence is captured.

## Current pilot file

- [apttosell-verified-projects-pilot-v0.3.csv](./apttosell-verified-projects-pilot-v0.3.csv)

The earlier v0.2 file is retained as a historical pilot snapshot and should not be treated as the latest registry draft.


## 196-project ID map — pilot v0.4

The registry has now been expanded from the two-row identity pilot to the full **196-project validation registry** used by the 2026 initial-cash project.

- File: [apttosell-project-id-map-196-pilot-v0.4.csv](./apttosell-project-id-map-196-pilot-v0.4.csv)
- Rows: **196**
- Unique housing-management numbers: **196**
- Unique project IDs: **196**
- Existing pilot IDs for 구리역 하이니티 리버파크 and 해링턴 플레이스 노원 센트럴 are preserved.

### Status meaning

`REGISTRY_SEEDED` means a stable AptToSell ID has been assigned from the existing 196-project validation registry. It does **not** mean every field has independently passed the final Version 1.0 primary-source gate.

This map is now the working join key for cross-dataset integration. Future datasets should reference `apttosell_project_id` rather than inventing a new project identifier.
