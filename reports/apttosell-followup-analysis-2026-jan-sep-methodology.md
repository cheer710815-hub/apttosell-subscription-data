# AptToSell 2026 Apartment Subscription Competition × Follow-up Supply Analysis

**Observation period:** Initial announcements from 2026-01-01 through 2026-09-30  
**Observation cutoff:** 2026-10-04  
**Final cohort:** 196 apartment projects  
**Competition-rate coverage:** 193 projects

**Public-summary cohort rule (verified 2026-11-05):** the published competition-band and price-band summary tables both use the **193 projects with a nonblank project-level first-priority competition rate**, not all 196 projects. Three rows are retained in the public project CSV but excluded from both grouped summary tables because their competition rate is unavailable (housing management numbers `2026000230`, `2026000135`, `2026000416`). They must not be counted as zeros or added to the published price-band denominators.

**Derived-output consistency check (2026-11-05):** the public 196-row CSV and 11-row summary CSV were independently parsed and cross-counted: 196 unique IDs, 193 nonblank rates, 44 projects at >=10:1, 19 with follow-up announcements, and 13/36 within 60 days. All published competition-band and price-band subgroup counts match after the three unavailable-rate records are excluded. **This is an internal consistency check of published derived tables only; no original ApplyHome API response archive or end-to-end extraction/linkage program was reproduced.**

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

Persistent identifier (published dataset): https://doi.org/10.6084/m9.figshare.34064439

### Research discovery and reuse routes

- **RePEc study handle:** `RePEc:gyv:aptsub:1`
- **IDEAS/RePEc bibliography:** https://ideas.repec.org/p/gyv/aptsub/1.html
- **AptToSell canonical study article:** https://apttosell.com/%ec%b2%ad%ec%95%bd-%ea%b2%bd%ec%9f%81%eb%a5%a0/
- **Project-level observations:** [196-project CSV](apttosell-apartment-subscription-followup-projects-2026-jan-sep.csv)
- **Variable definitions:** [data dictionary](apttosell-followup-analysis-data-dictionary.md)
- **Aggregate results:** [summary CSV](apttosell-followup-analysis-2026-jan-sep-summary.csv)

RePEc is a bibliographic discovery route for this same research, **not** a second underlying study or an independent citation. For reproducibility, the public derived tables and the transformation rules are provided; the presence of these materials alone does not demonstrate that an independent party has re-run the full extraction and linkage workflow. Confirm the preserved source snapshot and executable pipeline before claiming end-to-end independent reproduction.

## Files

- Summary CSV: `apttosell-followup-analysis-2026-jan-sep-summary.csv`
- Derived-output verification: [`verify_public_followup_196.py`](verify_public_followup_196.py). Download or clone the repository and run `python reports/verify_public_followup_196.py` from any working directory. The script reads both published CSVs, checks all 11 grouped/overall summary rows and their displayed percentages, and exits nonzero on inconsistencies. **Passing this checker does not validate the original ApplyHome API archive or end-to-end matching pipeline.**
- This methodology: `apttosell-followup-analysis-2026-jan-sep-methodology.md`
