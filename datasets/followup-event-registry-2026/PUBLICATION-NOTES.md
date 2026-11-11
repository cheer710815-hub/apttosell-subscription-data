# Publication Notes — Follow-Up Event Registry 2026

## Public release file

- File: `apttosell-followup-event-registry-public-v0.2.csv`
- Version: **0.2**
- Release date: **2026-10-06**
- Rows: **103**
- Numeric first follow-up notice IDs: **103 / 103**
- Canonical official source links: **103 / 103**
- `PRIMARY_VERIFIED`: **13**
- `ID_CORROBORATED_SECONDARY`: **90**
- License: **CC BY 4.0**
- DOI: **https://doi.org/10.5281/zenodo.23176906**

## Field design

The publication file intentionally keeps only the stable, reusable fields needed for citation and joins:

- stable AptToSell project ID
- project name
- original housing-management number
- first follow-up date
- first follow-up notice ID
- canonical official source URL
- evidence grade

Long verification notes remain in the working crosswalk and are not duplicated into the compact public file.

## Source-link policy

The canonical source for an ID-corroborated secondary row is the official ApplyHome detail page derived from the recovered follow-up notice ID.

Rows already supported by a directly inspected official project/public-agency artifact retain that official artifact URL.

## Interpretation

A follow-up supply event does **not** mean a contract-failure rate or unsold-rate estimate. It means a later official residual, no-priority, optional or discretionary-supply event was identified and linked to the initial project.

## Citation suggestion

AptToSell. *AptToSell Follow-Up Event Registry 2026*, version 0.2, 2026-10-06. CC BY 4.0. GitHub repository: https://github.com/cheer710815-hub/apttosell-subscription-data/tree/main/datasets/followup-event-registry-2026

For version-specific scholarly citation, use https://doi.org/10.5281/zenodo.23176906.

## 2026-11-10 — GitHub CSV URL-only correction (post-publication)

The existing public CSV `apttosell-followup-event-registry-public-v0.2.csv` was corrected on GitHub to repair the official ApplyHome detail-page path in 90 `ID_CORROBORATED_SECONDARY` rows. The 13 `PRIMARY_VERIFIED` rows, event identifiers, project names, dates, field definitions, row order and 103-row total were unchanged. The 90 replacement pages were individually checked against the CSV project names and notice dates.

- Correction commit: https://github.com/cheer710815-hub/apttosell-subscription-data/commit/b3d2c97770c7f36641769f078434149054185010
- Original GitHub CSV SHA-256 (before correction): `954d224276d902701a5b3c0b13de69c8a05bdb9807c769a24fa3059e1c1cee73`
- Corrected GitHub CSV SHA-256: `51282c326fd0f25ebdda645d8486653db462cf347ffd6eb63167541ed8466f52`
- DOI `10.5281/zenodo.23176906` identifies an earlier deposited release; this correction was applied **only to the live GitHub file**, not to the Zenodo archive. Do not assume the archived CSV is byte-identical to the corrected GitHub CSV.
- The existing citation, release date (2026-10-06), DOI and evidence-grade classifications are retained. No new DOI was issued.

