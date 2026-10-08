# AptToSell DDFS National Type Risk-set 2026 — v1.0

## What this dataset is

A type-level research dataset for South Korean apartment subscription projects that produced a verified first follow-up supply event in 2026.

The risk set contains only official housing types that had initial general-supply first-priority aggregate competition of at least 6.0x.

- First-follow-up registry projects: **103**
- Eligible projects with at least one 6x+ type: **52**
- Eligible housing types: **184**
- Reappeared in first follow-up: **78**
- Did not reappear: **106**
- Type-level reappearance rate: **42.39%**

## Main result

The two most stable observable signals of first-follow-up reappearance were:

1. **Initial demand depth** — deeper initial competition was associated with lower reappearance.
2. **Type supply share** — housing types representing a larger share of project general supply were more likely to reappear.

Primary project-clustered logistic model:
- competition, per doubling: **OR 0.538**, 95% CI 0.360–0.804, p=0.0025
- type supply share, per doubling: **OR 1.249**, 95% CI 1.038–1.503, p=0.0184

Absolute sale price, regulated-area status, standardized financing burden and linked relative price gap did not remain independently significant after adjustment.

## Files

- `apttosell-ddfs-national-type-riskset-2026-v1.0.csv` — canonical 184-row type-level dataset
- `apttosell-ddfs-national-type-model-results-2026-v1.0.csv` — final model estimates
- `METHODOLOGY-AND-FINDINGS.md` — frozen v1.0 methodology and publication-safe interpretation
- `DATA-DICTIONARY.md` — field definitions
- `CITATION.cff` — machine-readable citation metadata
- `datapackage.json` — machine-readable package metadata

## Interpretation

This dataset measures whether the identical official housing type reappeared in a project's **first** follow-up supply.

It does **not** measure:
- cancellation rate,
- contract failure rate,
- winner abandonment,
- individual loan availability.

The study is observational and does not establish causality.

## Sources

Initial subscription/type/price:
- Korea Real Estate Board ApplyHome public data collected for AptToSell

First follow-up supply:
- official ApplyHome notices or project-hosted official notices retained row-wise in `canonical_official_source_url`

Finance-policy normalization:
- Financial Services Commission official guidance

Linked RPG:
- AptToSell 2026 type-level Relative Price Gap dataset using pre-announcement MOLIT apartment transaction data

## License

CC BY 4.0.

## Recommended citation

> Kim, Eun. (2026). *2026 National DDFS Type-level Risk-set: Apartment Subscription Demand and First Follow-up Reappearance, v1.0*. AptToSell. https://apttosell.com/ddfs-type-reappearance-2026/

- ORCID: https://orcid.org/0009-0006-9445-4768
- Canonical article: https://apttosell.com/ddfs-type-reappearance-2026/
- Repository dataset: https://github.com/cheer710815-hub/apttosell-subscription-data/tree/main/datasets/ddfs-national-type-riskset-2026
- License: CC BY 4.0
- DOI: pending Zenodo registration

## Versioning

v1.0 is frozen. Corrections must be released as v1.1+ with explicit release notes rather than silently overwriting the methodology.
