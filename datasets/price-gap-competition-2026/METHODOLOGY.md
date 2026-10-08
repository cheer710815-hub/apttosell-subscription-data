# Methodology — Presale Price Gap × First-Priority Competition 2026 v0.1

## Cohort

The starting cohort is the 62-project publication-ready sample from the AptToSell 84㎡ presale-price-gap dataset.

## Linkage

1. Price-gap projects were normalized by name, region and announcement date.
2. Each project was resolved to the 196-project AptToSell identity registry.
3. The official `house_manage_no` was then used to attach the project-level first-priority competition record.
4. All 62 projects received a competition record.

## Measures

- `all_gap_pct`: presale-price gap against all-age nearby comparison transactions.
- `build_10y_gap_pct`: presale-price gap against nearby comparison stock completed within 10 years.
- `first_priority_competition_rate`: project-level first-priority competition rate from the existing competition dataset.

## Descriptive association

Spearman rank correlation is emphasized because competition rates are highly skewed and include extreme values.

Observed coefficients:
- all-age gap vs competition: **-0.037**
- 10-year gap vs competition: **0.103**

Sensitivity:
- excluding competition >100:1: 10-year-gap Spearman **0.158**
- excluding Seoul: **0.178**
- non-capital area only: **0.152**

The direction and magnitude remain weak, so the evidence does not support a simple price-gap-only explanation of demand.

## Limitations

- 62 projects are a conservative research sample, not the full 2026 market.
- Price-gap construction depends on comparison-stock definitions.
- Competition is project-level while the presale-price reference is centered on the 84㎡ research design.
- No causal inference is made.
- No claim is made that a positive gap means overvaluation or that a negative gap means undervaluation.
