# Methodology — Competition Band vs. Follow-Up Supply Within 30/60/90 Days

## Research question

Among 2026 apartment projects with enough observation time, how often did a first observed follow-up supply event appear within 30, 60, and 90 days of the initial recruitment announcement, and how did that differ by first-priority competition-rate band?

## Source data

Source file:

`reports/apttosell-apartment-subscription-followup-projects-2026-jan-sep.csv`

The project-level source was constructed from Korea Real Estate Board ApplyHome public data and AptToSell's project-level follow-up matching.

## Observation cutoff

2026-10-04.

## Cohort rule

To make 30/60/90-day rates directly comparable, this analysis uses **one fixed cohort**:

- project has a valid first-priority competition rate;
- initial recruitment announcement occurred at least 90 days before the observation cutoff.

This produces **140 projects**.

Projects announced too recently to have a full 90-day observation window are excluded from all three cumulative-window calculations.

## Competition-rate bands

- below 1:1
- 1–5:1
- 5–10:1
- 10–30:1
- 30:1 or higher

## Outcome

A project is counted as a hit within N days when:

1. a follow-up supply event was observed;
2. `days_to_first_followup` is available;
3. `days_to_first_followup <= N`.

The 30-, 60-, and 90-day results are cumulative.

## Key totals

Within the fixed 90-day-eligible cohort of 140 projects:

- within 30 days: 0 projects (0.0%)
- within 60 days: 73 projects (52.1%)
- within 90 days: 83 projects (59.3%)
- median time to first follow-up among the 83 projects observed within 90 days: 42 days
- observed range among those hits: 31–88 days

## Interpretation limits

A follow-up supply event means that a later official supply notice was observed for the project.

It **does not** equal:

- contract cancellation rate;
- unsold-housing rate;
- contract-failure rate;
- project sales rate.

This is a descriptive relationship between initial first-priority competition and later observed official supply events. It does not establish that the competition rate caused the later event.

Small band sizes, especially 5–10:1 and 30:1 or higher, should be interpreted cautiously.

## Reproducibility

The published band-level CSV is:

`reports/apttosell-followup-by-competition-band-90d-cohort-2026.csv`

License: CC BY 4.0.
