# Independent Study 04 — Release status (2026-11-01)

**Working title:** Round-Number Pricing in Seoul Apartment Transactions: Brokerage, Direct Sales, and Buyer Composition (2025)

**Status:** Exploratory reproducibility package candidate; DOI NOT issued. This file is an administrative release-gate memo, **not** the dataset or a claim of independent verification.

## Previously reported results (pending package reinspection)
- Share of prices at KRW 10 million increments: private-to-private direct transactions 74.09%; brokered transactions 66.74%; unadjusted difference +7.35 percentage points.
- Within-comparison analysis: 230 strata grouped by complex, area band and floor; 566 direct transactions and 5,557 brokered transactions.
- Previously reported adjusted difference: +16.98 percentage points (cluster bootstrap 95% CI: +12.54 to +21.28 percentage points).
- Previous package names: `ARHRN_PRICE_HEAPING_SEOUL_2025_MATCHED_V03_20261101.zip` and `ARHRN_Independent_04_Release_Gate_v3.zip`. Neither archive's contents or SHA-256 were revalidated in this update.

## Release gates
- [ ] Retrieve final v3 source package and verify archive CRC, SHA-256 manifest, scripts, outputs and license.
- [ ] Confirm definitions of transaction type and buyer composition and full eligibility/exclusion counts.
- [ ] Conduct independent holdout-period replication (not yet completed).
- [ ] Check prior literature coverage and avoid novelty claims.
- [ ] Inspect all files for personal information, secrets, and source-data redistribution rights.
- [ ] Publish reproducibility code, derived tables and methodology to this repository.
- [ ] Deposit an appropriate versioned dataset with Zenodo **after account access is restored**, then verify the DOI metadata.
- [ ] Link the citable dataset and limitations from AptToSell.

## Publication boundary
Do not advertise this memo as a published dataset, peer-reviewed result or DOI-linked publication. The percentage estimates listed above are transcribed from an earlier research record, not recomputed during the present registration audit.

**Provenance:** Ministry of Land, Infrastructure and Transport apartment sales transaction disclosure data (exact source download URL and retrieval date to be preserved in the forthcoming release README).
