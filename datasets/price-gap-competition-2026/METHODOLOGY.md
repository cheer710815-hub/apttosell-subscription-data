# Methodology — Presale Price Merit × First-Priority Competition 2025–2026 v1.0

## Research question

The baseline study tests whether project-level first-priority apartment subscription competition is associated with (1) price merit versus nearby apartment transactions and (2) Seoul / prime-Seoul location indicators.

## Cohort

The analytical cohort combines 2025 and 2026 Korean apartment subscription announcements with:
- project-level first-priority competition records,
- an 84㎡-class presale-price reference,
- same-legal-dong apartment transaction comparators.

Atypical supply cases are excluded from the main public analytical sample.

## Price-merit construction

For each project:
1. identify the matched legal dong,
2. collect apartment transactions during the six months before the announcement date,
3. keep exclusive areas from 82㎡ through 86㎡,
4. exclude cancelled transactions,
5. restrict the main comparator to stock completed within 10 years,
6. require at least 10 qualifying transactions,
7. calculate the median comparison transaction price.

Price merit is the difference between the nearby comparison-market median and the presale price, scaled relative to the comparison median. Positive values therefore mean the nearby comparison median is above the presale price.

A <=5-year comparator is retained as a sensitivity field when available.

## Outcome

The baseline dependent variable is:

`log(1 + first-priority competition ratio)`

## Baseline models

- Descriptive price-merit bands
- Spearman rank correlation
- OLS with HC3 robust standard errors
- M1: price merit only
- M2: price merit + Seoul + prime-Seoul incremental indicator + year-2026 indicator

## v1.0 sample

- Main sample: 153 projects
- Sensitivity sample: 168 projects
- 2025 main sample: 89
- 2026 main sample: 64

## Baseline results

- Spearman rho=0.113, p=0.166
- M1 price-merit beta=1.3992, p=0.002937, R²=0.087
- M2 price-merit beta=0.8555, p=0.0177
- M2 Seoul beta=2.5982, p=2.32e-11
- M2 prime-Seoul incremental beta=1.4040, p=0.05102
- M2 R²=0.341

## Interpretation limits

This is observational evidence, not a causal estimate. The simple rank correlation is not statistically significant, while the regression price-merit coefficient is positive and statistically significant in the baseline specifications.

The prime-Seoul subgroup is small, so the prime-Seoul estimate is exploratory. Reserved fields for school district, transport, brand, price-cap rules, regulation, mortgage rates, unsold inventory, supply and local market conditions are retained for a later expanded-control model and should not be treated as completed controls in v1.0.
