# Release Notes — Follow-Up Event Registry 2026

> Historical pilot notes are retained below. The public v0.2 registry was published on 2026-10-06; the 2026-11-10 change affects only the live GitHub CSV.

## 2026-11-10 — GitHub CSV URL-only correction (post-publication)

The existing public CSV `apttosell-followup-event-registry-public-v0.2.csv` was corrected on GitHub to repair the official ApplyHome detail-page path in 90 `ID_CORROBORATED_SECONDARY` rows. The 13 `PRIMARY_VERIFIED` rows, event identifiers, project names, dates, field definitions, row order and 103-row total were unchanged. The 90 replacement pages were individually checked against the CSV project names and notice dates.

- Correction commit: https://github.com/cheer710815-hub/apttosell-subscription-data/commit/b3d2c97770c7f36641769f078434149054185010
- Original GitHub CSV SHA-256 (before correction): `954d224276d902701a5b3c0b13de69c8a05bdb9807c769a24fa3059e1c1cee73`
- Corrected GitHub CSV SHA-256: `51282c326fd0f25ebdda645d8486653db462cf347ffd6eb63167541ed8466f52`
- DOI `10.5281/zenodo.23176906` identifies an earlier deposited release; this correction was applied **only to the live GitHub file**, not to the Zenodo archive. Do not assume the archived CSV is byte-identical to the corrected GitHub CSV.
- The existing citation, release date (2026-10-06), DOI and evidence-grade classifications are retained. No new DOI was issued.

## Historical 0.1-pilot notes

Release date: **2026-10-05**

## Included

- First-event rows for **103** projects with observed follow-up supply
- Stable AptToSell project IDs for all 103 rows
- Derived first-event dates from the published project-level analysis
- Imported event seed for existing verified/secondary events
- Explicit reconciliation of the Harrington Place Nowon Central chronology

## Harrington reconciliation

The project-level derived first-follow-up date is 2026-04-28.

A same-project 58-unit no-priority/residual supply event dated 2026-04-28 is corroborated by multiple public sources. Later events remain 2026-06-08 and 2026-07-23.

The 2026-04-28 row now carries corroborated numeric notice ID `2026910100`, but remains `SECONDARY_CORROBORATED` until the original ApplyHome record is directly accessible and verified.

## Historical DOI decision (0.1-pilot only)

No DOI is assigned to this pilot.

A versioned event-level DOI release requires official notice-level identifiers, dates and event subtypes for a clearly bounded cohort.


## Full queue screening milestone

The initial first-event verification queue is fully screened:

- 103 / 103 evidence-reviewed
- 103 numeric notice IDs recovered
- 0 discovery TODO rows remaining
- 13 primary-verified events

The pilot remains non-DOI because primary-source coverage is not yet sufficient for a bounded event-level release.


## Notice-ID discovery complete

All **103 / 103** first-event rows now have a recovered numeric follow-up notice ID.

The remaining limitation is not event identification; it is direct official-artifact access for primary-source promotion.


## Primary-verified subset

A conservative direct-official-artifact subset has been added with **13** events.

This subset is separate from the full 103-row notice-ID crosswalk and is suitable for higher-confidence reuse.

- **두산위브 더센트럴 수원** promoted from the official project-hosted no-priority notice PDF (2026-04-09, notice ID 2026910083, 25 residual units).

- **드파인 아르티아** promoted from the official SK DEFINE no-priority notice PDF. The first-event ID was corrected from secondary-recovered `2026910233` (second no-priority notice) to official first-event ID `2026910214` dated 2026-08-07.

- **쌍용 더 플래티넘 온수역** promoted from its official project-hosted no-priority notice PDF (2026-03-25, notice ID 2026910070, 3 residual units).

- **더샵 송도그란테르 G5-11/G5-3/G5-4/G5-5** promoted from official POSCO E&C project-hosted no-priority notice PDFs dated 2026-07-30 (IDs 2026910207, 2026910204, 2026910205, 2026910206).

- **의왕역 SK VIEW** promoted from the official SK VIEW project-hosted no-priority notice PDF (2026-08-28, notice ID 2026910225, 17 residual units).

- **천안 아이파크 시티 6단지 / 5단지** promoted from official project-hosted first no-priority recruitment notice PDFs (IDs 2026910074 / 2026910073).


## Canonical ApplyHome link completion

All **103 / 103** first-event rows now carry an official source link.

- 13 primary rows retain directly inspected official-artifact links.
- 90 secondary/corroborated rows point to the corresponding official ApplyHome detail URL generated from the recovered notice ID.

Primary verification is now treated as an evidence-grade enhancement rather than a prerequisite for official source linking.
