# AptToSell Follow-Up Event Registry 2026 — Pilot

> Status: **derived first-event pilot**. This is not a new DOI release.

This pilot moves from project-level follow-up indicators to an event-shaped structure while preserving the limitations of the published 2026 competition/follow-up analysis.

## Snapshot

- Original project cohort: **196**
- Projects with follow-up supply observed: **103**
- First-event rows generated: **103**
- Stable AptToSell project-ID matches: **103 / 103**
- Event subtype: **not assigned unless separately verified**
- DOI: **not assigned**

## What is derived

For projects with `followup_supply_observed = true`, the first follow-up date is reconstructed as:

`initial_announcement_date + days_to_first_followup`

This creates one first-event row per project.

## What is NOT claimed

The current project-level source does not preserve enough evidence to identify every follow-up event subtype or every later event date. Therefore:

- only event sequence 1 is represented
- `event_type` is set to `followup_supply_observed_unspecified`
- dates are labeled `DERIVED_FIRST_EVENT_DATE`
- later event counts are retained only as project-level context

## Main file

- [apttosell-first-followup-events-pilot-v0.1.csv](./apttosell-first-followup-events-pilot-v0.1.csv)

## Existing published analysis

The published competition/follow-up study remains the citation target:

https://doi.org/10.6084/m9.figshare.34064439

This pilot is a structural extension for future event-level verification, not a replacement for the published study.


## Reconciliation result — Harrington

The earlier mismatch for **해링턴 플레이스 노원 센트럴** has been structurally resolved.

Multiple public sources identify a same-project **58-unit residual/no-priority supply notice dated 2026-04-28**, matching the project-level derived first-follow-up date.

The event chronology is therefore retained as:

1. 2026-04-28 — 58-unit residual/no-priority supply, `SECONDARY_CORROBORATED`
2. 2026-06-08 — 58-unit later residual/no-priority supply candidate
3. 2026-07-23 — 17-unit discretionary/optional supply candidate

The 2026-04-28 row is **not promoted to primary-verified status** because the official ApplyHome notice identifier has not yet been directly reconstructed. The chronology is corrected without overstating source quality.


## Pilot package metadata

- Version: **0.1-pilot**
- [Data Package metadata](./datapackage.json)
- [Citation metadata](./CITATION.cff)
- [Schema.org Dataset JSON-LD](./schemaorg-dataset.jsonld)
- [Release notes](./RELEASE-NOTES.md)
- [Reconciliation note](./PILOT-RECONCILIATION.md)

This pilot is now structurally complete. Further work should focus on primary-source verification of individual follow-up notices rather than changing the frozen pilot schema.


## Official notice-ID verification register

A separate register now tracks whether each known follow-up event has a recovered numeric notice identifier and whether that identifier has been directly verified from an official source.

- [OFFICIAL-NOTICE-VERIFICATION.md](./OFFICIAL-NOTICE-VERIFICATION.md)

Current pilot IDs retained:

- 구리역 하이니티 리버파크: `2026910080`
- 해링턴 플레이스 노원 센트럴 2026-06-08: `2026910147`
- 해링턴 플레이스 노원 센트럴 2026-07-23: `2026940157`

The 2026-04-28 Harrington first follow-up now has corroborated numeric notice ID `2026910100`; direct ApplyHome primary-source access remains the final open verification gate.


## Evidence-review milestone — 2026-10-05

The full 103-project first-event queue has now been screened.

- Evidence-reviewed: **103 / 103**
- Remaining discovery TODO: **0**
- Numeric follow-up notice IDs recovered: **103 / 103**
- Primary-verified events: **5**
- Secondary/corroborated events: **102**

A compact crosswalk is available at [FOLLOWUP-NOTICE-ID-CROSSWALK-v0.1.csv](./FOLLOWUP-NOTICE-ID-CROSSWALK-v0.1.csv).

The next stage is primary-source promotion, not further ID guessing.


## Notice-ID discovery completion

The first-event notice-ID recovery pass is now complete.

- First-event cohort: **103**
- Evidence-reviewed: **103 / 103**
- Numeric first follow-up notice IDs recovered: **103 / 103**
- Discovery TODO: **0**
- Direct-primary verified: **1**

See [PRIMARY-PROMOTION-ACCESS-AUDIT.md](./PRIMARY-PROMOTION-ACCESS-AUDIT.md) for the remaining official-source access blocker.


## Primary-verified subset

A separate conservative subset now contains only events supported by directly inspected official artifacts.

- File: [PRIMARY-VERIFIED-SUBSET-v0.1.csv](./PRIMARY-VERIFIED-SUBSET-v0.1.csv)
- Current rows: **5**
- Included: 포레나더샵 인천시청역, 아크로 리버스카이, 청주 푸르지오 씨엘리체, 두산위브 더센트럴 수원, 드파인 아르티아

This subset is intentionally small and should grow only through direct official-artifact verification.
