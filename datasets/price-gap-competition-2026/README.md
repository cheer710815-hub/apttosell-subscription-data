# AptToSell Presale Price Gap × First-Priority Competition 2026 — v0.1

## Overview

This derived dataset links AptToSell's conservative 62-project 84㎡ presale-price-gap sample to the 2026 first-priority apartment subscription competition dataset.

All **62 / 62** price-gap projects were linked to a competition record through the AptToSell project identity layer.

## Core descriptive result

The sample does not show a simple monotonic relationship in which a larger presale-price gap automatically corresponds to weaker first-priority competition.

- Projects: **62**
- Median first-priority competition: **1.10:1**
- Median all-age comparison gap: **46.42%**
- Median 10-year comparison gap: **31.21%**
- Spearman correlation, all-age gap vs competition: **-0.037**
- Spearman correlation, 10-year gap vs competition: **0.103**

Sensitivity checks remain weak:
- excluding competition above 100:1, 10-year-gap Spearman **0.158**
- excluding Seoul, 10-year-gap Spearman **0.178**
- non-capital-area sample, 10-year-gap Spearman **0.152**

These are descriptive associations, not causal estimates.

## Interpretation

A presale-price gap measures the difference between the presale price and a specified nearby transaction-price comparison group. Subscription competition reflects demand under many simultaneous factors such as location, supply volume, unit mix, eligibility rules, brand, financing conditions and local market expectations.

Therefore, this dataset should not be used to claim that price gap alone determines subscription demand.

## Files

- `apttosell-price-gap-competition-2026-v0.1.csv`
- `METHODOLOGY.md`
- `DATA-DICTIONARY.md`

## Source datasets

- Presale-price gap: `datasets/presale-price-gap-2026/apttosell_84sqm_presale_price_gap_2026_public.csv`
- Competition/follow-up project table: `reports/apttosell-apartment-subscription-followup-projects-2026-jan-sep.csv`
- Project identity map: `datasets/verified-project-registry-2026/apttosell-project-id-map-196-pilot-v0.4.csv`

## Release decision

Version **v0.1** is a derived analytical layer. No new DOI is assigned at this stage. Cite the underlying presale-price-gap DOI where appropriate: **10.5281/zenodo.23207987**.

## License

CC BY 4.0 for the AptToSell-derived file.
