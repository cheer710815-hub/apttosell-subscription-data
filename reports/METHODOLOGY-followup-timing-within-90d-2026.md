# Methodology — Timing of First Follow-Up Supply Within 90 Days

## Research question

Among apartment projects where a follow-up supply notice was observed within 90 days of the initial recruitment announcement, when did the first follow-up supply tend to occur?

## Source

Underlying project-level file:

`reports/apttosell-apartment-subscription-followup-projects-2026-jan-sep.csv`

Source data originate from Korea Real Estate Board ApplyHome public data and AptToSell project-level matching.

## Observation cutoff

2026-10-04.

## Fixed cohort

Projects were included only when:

1. a valid first-priority competition rate was available; and
2. at least 90 days had elapsed between the initial recruitment announcement and the observation cutoff.

Fixed 90-day-observable cohort: **140 projects**.

Among them, **83 projects** had a first observed follow-up supply event within 90 days.

## Timing variable

`days_to_first_followup` measures calendar days from the initial recruitment announcement date to the first observed later official supply notice matched to the same project.

## Results

Among the 83 projects with follow-up supply observed within 90 days:

- 31–45 days: 50 projects (60.2%)
- 46–60 days: 23 projects (27.7%)
- 61–75 days: 5 projects (6.0%)
- 76–90 days: 5 projects (6.0%)

Cumulative:

- within 45 days: 50 of 83 (60.2%)
- within 60 days: 73 of 83 (88.0%)
- after 60 days but within 90 days: 10 of 83 (12.0%)

Distribution:

- minimum: 31 days
- 25th percentile: 40 days
- median: 42 days
- 75th percentile: 48 days
- maximum: 88 days

## Interpretation

The observed first follow-up notices were concentrated around roughly six weeks after the initial recruitment announcement.

This is a descriptive result for the 83 projects that had a follow-up event within 90 days. It should not be interpreted as the probability that every project will receive follow-up supply around six weeks.

## Critical caveat

A follow-up supply event is **not** the same as:

- unsold-housing rate;
- contract-failure rate;
- contract cancellation rate;
- sales-completion rate.

The timing reflects when a later official supply notice was observed in the matched dataset.

## License

CC BY 4.0.
