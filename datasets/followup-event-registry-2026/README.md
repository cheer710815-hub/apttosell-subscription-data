# AptToSell Follow-Up Event Registry 2026

> Status: **published public release v0.2**. Zenodo DOI: https://doi.org/10.5281/zenodo.23176906

This pilot moves from project-level follow-up indicators to an event-shaped structure while preserving the limitations of the published 2026 competition/follow-up analysis.

## Snapshot

- Original project cohort: **196**
- Projects with follow-up supply observed: **103**
- First-event rows generated: **103**
- Stable AptToSell project-ID matches: **103 / 103**
- Event subtype: **not assigned unless separately verified**
- DOI: **https://doi.org/10.5281/zenodo.23176906**

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


## Package metadata

- Public version: **0.2**
- [Data Package metadata](./datapackage.json)
- [Citation metadata](./CITATION.cff)
- [Schema.org Dataset JSON-LD](./schemaorg-dataset.jsonld)
- [Release notes](./RELEASE-NOTES.md)
- [Reconciliation note](./PILOT-RECONCILIATION.md)

The public v0.2 registry is DOI-backed. Further work should focus on optional primary-source promotion of corroborated rows while preserving the published v0.2 release.


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
- Primary-verified events: **13**
- Secondary/corroborated events: **90**

A compact crosswalk is available at [FOLLOWUP-NOTICE-ID-CROSSWALK-v0.1.csv](./FOLLOWUP-NOTICE-ID-CROSSWALK-v0.1.csv).

The event-linking stage is complete. For the 90 non-primary rows, the canonical source link is now the official ApplyHome detail URL generated from the recovered notice ID. Primary promotion is optional enrichment, not a prerequisite for using the registry.


## Notice-ID discovery completion

The first-event notice-ID recovery pass is now complete.

- First-event cohort: **103**
- Evidence-reviewed: **103 / 103**
- Numeric first follow-up notice IDs recovered: **103 / 103**
- Discovery TODO: **0**
- Direct-primary verified: **13**

See [PRIMARY-PROMOTION-ACCESS-AUDIT.md](./PRIMARY-PROMOTION-ACCESS-AUDIT.md) for the distinction between canonical ApplyHome linking and optional direct-artifact promotion.


## Primary-verified subset

A separate conservative subset now contains only events supported by directly inspected official artifacts.

- File: [PRIMARY-VERIFIED-SUBSET-v0.1.csv](./PRIMARY-VERIFIED-SUBSET-v0.1.csv)
- Current rows: **13**
- Included: 포레나더샵 인천시청역, 아크로 리버스카이, 청주 푸르지오 씨엘리체, 두산위브 더센트럴 수원, 드파인 아르티아, 쌍용 더 플래티넘 온수역, 의왕역 SK VIEW

This subset is intentionally small and should grow only through direct official-artifact verification.


## Canonical source-link policy

For registry use, the official ApplyHome detail URL is the canonical source link whenever the numeric notice ID is known.

- 103 / 103 first follow-up notice IDs are recovered.
- 90 non-primary rows now link directly to the corresponding ApplyHome detail URL.
- 13 primary rows retain their directly inspected official project/public-agency artifact links.
- A row does **not** need an additional project-hosted PDF merely to have an official source link.
- `PRIMARY_VERIFIED` remains a separate evidence-grade label used only when the event artifact itself was directly inspected.


## Publication-ready public file

A compact citation-oriented public file is now available:

- [apttosell-followup-event-registry-public-v0.2.csv](./apttosell-followup-event-registry-public-v0.2.csv)
- Rows: **103**
- Official source links: **103/103**
- Primary verified: **13**
- Corroborated with ApplyHome links: **90**

Supporting reuse documents:

- [Publication notes](./PUBLICATION-NOTES.md)
- [Media brief](./MEDIA-BRIEF.md)
- [Submission kit](./SUBMISSION-KIT.md)
