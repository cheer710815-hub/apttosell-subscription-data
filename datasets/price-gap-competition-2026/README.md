# AptToSell Presale Price Merit × First-Priority Competition 2025–2026 — v1.0

## Overview

This release expands the earlier 2026-only v0.1 analytical layer into a 2025–2026 baseline study linking 84㎡-class presale prices, nearby apartment transaction medians and first-priority subscription competition.

The existing `price-gap-competition-2026` asset is versioned forward rather than duplicated.

## Main sample

- Main analytical sample: **153 projects**
- Sensitivity sample: **168 projects**
- 2025: **89 projects**
- 2026: **64 projects**
- Main-sample comparator rule: at least **10 transactions** in the same legal dong, 82–86㎡, stock completed within 10 years, during the six months before the subscription announcement

## Core results

- Spearman rho: **0.113**, p=**0.166**
- M1 price-merit coefficient: **1.3992**, p=**0.002937**, R²=**0.087**
- M2 price-merit coefficient: **0.8555**, p=**0.0177**
- M2 Seoul coefficient: **2.5982**, p=**2.32e-11**
- M2 prime-Seoul incremental coefficient: **1.4040**, p=**0.05102**
- M2 R²=**0.341**

The regression models show a positive association between price merit and log first-priority competition, while the simple rank correlation is not statistically significant. The prime-Seoul estimate is exploratory because the subgroup is very small.

## Files

- `apttosell-price-gap-competition-2025-2026-v1.0.csv` — main analytical sample
- `apttosell-price-gap-competition-2025-2026-v1.0-sensitivity.csv` — broader sensitivity sample
- `RESULTS-v1.0.md` — model outputs and interpretation rules
- `METHODOLOGY.md` — construction and analysis method
- `DATA-DICTIONARY.md` — column definitions
- `FINAL-QA-v1.0.txt` — baseline QA summary
- `CITATION.cff` — citation metadata
- `RELEASE_NOTES.md` — version history

The earlier `apttosell-price-gap-competition-2026-v0.1.csv` is preserved as the historical 2026-only release.

## Interpretation limits

This is an observational dataset. It must not be used to claim a causal effect of price merit on subscription demand. School district, transport, brand, price-cap rules, mortgage rates, unsold inventory and supply conditions are not yet populated as a full external-control model.

## License

CC BY 4.0 for AptToSell-derived files.
