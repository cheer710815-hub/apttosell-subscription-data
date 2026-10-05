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
