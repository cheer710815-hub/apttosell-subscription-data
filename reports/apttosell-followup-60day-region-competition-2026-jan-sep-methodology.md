# 60-day follow-up by region and competition band (2026)

Release: 2026-10-10. Observation cutoff: 2026-10-04. Source: 196-project ApplyHome-derived CSV in this repository. License for AptToSell analysis: CC BY 4.0.

## Results

The source dataset contains 196 projects; 161 have at least 60 days of observation, and 83 of those have a follow-up notice within 60 days (51.55%). This differs from the published high-competition (>=10:1) subset of 13/36 (36.11%).

| Competition | Capital region | Non-capital region |
|---|---|---|
| <1:1 | 14/26 | 20/49 |
| 1-5:1 | 13/19 | 14/15 |
| 5-10:1 | 3/6 | 6/8 |
| 10-30:1 | 7/13 | 5/7 |
| >=30:1 | 1/14 | 0/2 |

## Method

Filter eligible_60d_observation == true, then group by broad_region and competition_band. Count followup_within_60d == true. Use quote-aware CSV parsing. The source and derived cross-tab CSV are in the reports directory.

## Limits

Follow-up notices are not contract failure, cancellations, or a count of unsold units. Small cells (including 0/2) are not reliable estimates of future outcomes. The upstream announcement matching has not been independently revalidated for this derivative. No causal inference is supported.

## Citation

AptToSell (2026), 60-day follow-up supply by region and competition band. Underlying dataset DOI: https://doi.org/10.6084/m9.figshare.34064439
