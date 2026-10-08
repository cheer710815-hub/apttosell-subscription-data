# AptToSell Price Gap × Pre-Move-In Cash Linkage 2026 — Pilot v0.1

## Purpose

This pilot joins two already-public AptToSell datasets at the apartment-project level:

1. the conservative 41-project pre-move-in direct-cash dataset, and
2. the conservative 62-project 84㎡ presale-price-gap dataset.

The purpose is to test whether price-comparison metrics and pre-move-in cash-burden metrics can be studied together using the stable AptToSell project identity layer.

## Result

- Pre-move-in cash public projects: **41**
- Presale-price-gap public projects: **62**
- Reliably linked overlap: **11 projects**
- Median pre-move-in direct cash in the linked overlap: **5,839 (10k KRW)**
- Cash-ratio distribution: **5.0%: 6, 10.0%: 2, 40.0%: 1, 30.0%: 2**

Because the overlap is only 11 projects, this package is **not** used for national inference, correlation claims, or causal conclusions.

## Main file

- `apttosell-price-gap-cash-linkage-public-pilot-v0.1.csv`

## Source datasets

- Pre-move-in cash: `datasets/initial-contract-cash-2026/apttosell-initial-cash-publication-ready-2026-10-05.csv`
- Presale price gap: `datasets/presale-price-gap-2026/apttosell_84sqm_presale_price_gap_2026_public.csv`
- Project identity map: `datasets/verified-project-registry-2026/apttosell-project-id-map-196-pilot-v0.4.csv`

## Interpretation

A higher presale-price gap does not imply a higher or lower cash burden. The two variables measure different concepts:
- price gap compares a presale price with nearby transaction-price benchmarks;
- pre-move-in direct cash standardizes the contract deposit plus explicitly self-funded interim payments.

This pilot only demonstrates cross-dataset linkage.

## Release decision

No DOI is assigned. The overlap is too small for a standalone analytical release. Expand the shared project coverage before publishing a statistical article from this linkage.

## License

CC BY 4.0 for the AptToSell-derived linkage file. Original-source terms continue to apply to underlying public data.

## Version

v0.1 — 2026-10-08
