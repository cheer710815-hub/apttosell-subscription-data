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
