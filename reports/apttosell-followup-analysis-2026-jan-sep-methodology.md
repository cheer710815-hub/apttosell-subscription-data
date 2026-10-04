# AptToSell 2026 Apartment Subscription Competition × Follow-up Supply Analysis

**Observation period:** Initial announcements from 2026-01-01 through 2026-09-30  
**Observation cutoff:** 2026-10-04  
**Final cohort:** 196 apartment projects  
**Competition-rate coverage:** 193 projects

## Headline finding

Among 44 projects with an aggregated first-priority subscription competition rate of at least 10:1, 19 later had a follow-up supply announcement identified in the official ApplyHome data. This is 43.18% on a simple observed basis.

Restricting the denominator to projects that had at least 60 days of observation time, 13 of 36 projects had a follow-up supply event within 60 days, or 36.11%.

## Definitions

### Initial cohort
The cohort uses the initial recruitment announcement date (`RCRIT_PBLANC_DE`). Special/reissued announcements such as member-cancellation supply, vacant-unit resale, additional recruitment rounds, rental recruitment and other non-initial supply announcements are excluded from the primary cohort.

### First-priority competition rate
For each project:
1. Keep rows marked as first-priority subscription.
2. Count each housing model's general-supply household count once.
3. Sum first-priority application counts across applicable residence rows.
4. Project-level competition rate = total first-priority applications / total first-priority general-supply households.

### Follow-up supply
A project is marked as having follow-up supply when an official later announcement classified as residual/unsold supply or optional supply is matched to the initial project by normalized project name, exact supply address, and a later announcement date.

**Important:** Follow-up supply is not the same as a contract failure rate or non-contract rate. Follow-up announcements may result from several causes, including disqualification, cancellation, remaining units, and other administrative reasons.

### Price
Price uses the official ApplyHome housing-model field `LTTOT_TOP_AMOUNT`, expressed in units of KRW 10,000. The project maximum price is the maximum value across housing models. A weighted representative price is also calculated using general + special supply households as weights.

### 60-day standardized rate
To reduce right-censoring from recent announcements, the 60-day rate includes only projects with at least 60 days between the initial announcement date and the observation cutoff.

## Official source families

- Korea Real Estate Board ApplyHome apartment announcement detail API
- ApplyHome subscription competition-rate API
- ApplyHome residual/unsold supply announcement API
- ApplyHome optional-supply announcement API
- ApplyHome housing-model detail / presale-price API

## Citation

Suggested citation:

> AptToSell. "2026 Apartment Subscription Competition and Follow-up Supply Analysis." Data cutoff 2026-10-04. Derived from Korea Real Estate Board ApplyHome public API data.

Canonical site: https://apttosell.com/

Persistent identifier: https://doi.org/10.6084/m9.figshare.34064439

## Files

- Summary CSV: `apttosell-followup-analysis-2026-jan-sep-summary.csv`
- This methodology: `apttosell-followup-analysis-2026-jan-sep-methodology.md`
