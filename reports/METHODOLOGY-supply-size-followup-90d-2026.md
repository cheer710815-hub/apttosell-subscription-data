# Methodology — Supply Size and Follow-Up Supply Within 90 Days

## Research question

How did the observed rate of first follow-up supply within 60 and 90 days differ by the number of households in the initial supply project?

## Source

Underlying project-level file:

`reports/apttosell-apartment-subscription-followup-projects-2026-jan-sep.csv`

Source data originate from Korea Real Estate Board ApplyHome public data and AptToSell project-level matching.

## Observation cutoff

2026-10-04.

## Fixed cohort

The analysis uses projects that:

1. have a valid first-priority competition rate;
2. have a non-missing initial supply household count; and
3. have at least 90 days of observation.

Fixed cohort: **140 projects**.

## Supply-size bands

- under 300 households
- 300–499 households
- 500–999 households
- 1,000 households or more

## Results

| Supply size | Projects | 60-day follow-up | 90-day follow-up | Median first-priority competition |
|---|---:|---:|---:|---:|
| Under 300 | 60 | 28 (46.7%) | 35 (58.3%) | 1.17:1 |
| 300–499 | 33 | 14 (42.4%) | 15 (45.5%) | 0.60:1 |
| 500–999 | 29 | 18 (62.1%) | 19 (65.5%) | 1.40:1 |
| 1,000+ | 18 | 13 (72.2%) | 14 (77.8%) | 1.65:1 |
| Total | 140 | 73 (52.1%) | 83 (59.3%) | — |

## Interpretation

Projects with 1,000 households or more had the highest observed 90-day follow-up rate in this cohort: 14 of 18 projects (77.8%).

However, the pattern is not strictly monotonic across all size bands. In particular, the under-300 group had a higher rate than the 300–499 group.

Therefore this analysis should **not** be summarized as “larger complexes always have more follow-up supply.”

It is a descriptive comparison, not a causal estimate.

## Critical caveat

A follow-up supply event is not the same as:

- unsold-housing rate;
- contract-failure rate;
- contract cancellation rate;
- sales-completion rate.

Differences across size bands can also reflect location, price, demand, project composition, or other factors not controlled for here.

The 1,000+ group contains only 18 projects, so its percentage should be reported together with the numerator and denominator.

## License

CC BY 4.0.
