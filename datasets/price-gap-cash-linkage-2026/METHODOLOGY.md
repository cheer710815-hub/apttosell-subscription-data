# Methodology — Price Gap × Pre-Move-In Cash Linkage Pilot v0.1

## Inputs

Three public files were used:
- 41-project pre-move-in cash publication-ready subset
- 62-project presale-price-gap publication-ready subset
- 196-project AptToSell identity map

## Join procedure

1. The cash dataset was linked to the project registry by `house_manage_no`.
2. Price-gap project names were normalized for spacing and punctuation.
3. Candidate matches were restricted to the same region.
4. Name similarity and initial announcement date were used together to identify the registry project.
5. The registry's `apttosell_project_id` was then used to join the price-gap record to the cash record.
6. Only high-confidence linked overlaps were retained.

## Output

The final pilot contains **11** linked projects.

## What is not done

- No Pearson or Spearman significance test is reported.
- No regression is reported.
- No national or market-wide conclusion is made.
- No causal interpretation is permitted.

The small overlap would make such claims unstable and potentially misleading.

## Variable notes

`pre_movein_direct_cash_10k_krw` is the standardized project-level direct cash amount from the cash dataset's reference price, not an individual borrower's required cash.

`all_gap_pct` and `build_10y_gap_pct` are descriptive presale-price gaps relative to nearby comparison transactions under the source dataset's methodology.

`gap_change_pp` is the percentage-point difference between the all-age comparison gap and the 10-year comparison gap.

## Reproducibility

The source datasets remain unchanged. This file is a separate derived linkage layer so existing releases and DOI-backed assets remain reproducible.
