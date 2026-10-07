# 2026 Korea Apartment Presale Price Gap Dataset

## Overview

This dataset was created by AptToSell to examine how the measured gap between new-apartment presale prices and nearby existing-apartment transaction prices changes depending on the age of the comparison apartment stock.

The central research question is:

> How much does the measured presale-price gap change when the comparison group includes all apartment ages versus only apartments completed within the previous 10 years?

The dataset is intended for reproducible use by journalists, researchers, public institutions, students, and analysts.

## Files

- `apttosell_84sqm_presale_price_gap_2026_public.csv`  
  Conservative publication-ready sample: 66 projects.

- `apttosell_84sqm_presale_price_gap_2026_research_sample.csv`  
  Deduplicated research sample: 155 projects.

- `DATA_DICTIONARY.csv` — Field definitions.
- `METHODOLOGY.md` — Methodology, inclusion rules, and limitations.
- `LICENSE.txt` — CC BY 4.0 licensing notice.
- `CITATION.cff` — Citation metadata.
- `RELEASE_NOTES.md` — Version notes.

## Key Findings

For the conservative publication-ready sample:

- 66 projects met the stricter publication / institutional criteria.
- The median difference between the full-age comparison gap and the 10-year comparison gap was 16.54 percentage points.
- 28 projects showed a difference of at least 20 percentage points.
- 16 projects showed a difference of at least 40 percentage points.

These are descriptive statistics, not causal estimates.

## Core Definition

Presale price gap (%):

`(presale price - median comparison transaction price) / median comparison transaction price × 100`

Comparison transactions are:
- in the same legal dong (법정동),
- from the six months before the presale announcement,
- between 82㎡ and 86㎡ exclusive-use area,
- summarized using the median transaction price.

## Interpretation

This dataset does not determine whether a presale price is overvalued, undervalued, fairly priced, discounted, or likely to rise.

Its purpose is to quantify how much a reported "nearby market price" comparison can change when the age composition of the comparison group changes.

## Recommended Attribution

Korean:

> 출처: AptToSell, 「2026 신규 아파트 분양가 비교군 연식에 따른 가격 괴리율 데이터」

English:

> Source: AptToSell, “2026 Korea Apartment Presale Price Gap by Comparison-Stock Age”

## License

CC BY 4.0. See `LICENSE.txt`.

## Version

Release date: 2026-10-07  
Version: 1.0