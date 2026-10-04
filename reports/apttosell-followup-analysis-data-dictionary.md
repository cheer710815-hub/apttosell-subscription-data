# Data Dictionary — 2026 Apartment Subscription Follow-up Dataset

Project-level file:
`reports/apttosell-apartment-subscription-followup-projects-2026-jan-sep.csv`

Observation cutoff: **2026-10-04**

| Column | Meaning |
|---|---|
| house_manage_no | ApplyHome housing management number for the initial announcement |
| project_name | Apartment project name |
| region | Province / metropolitan-city label from the source data |
| broad_region | 수도권 or 비수도권 classification used in AptToSell analysis |
| initial_announcement_date | Initial recruitment announcement date |
| total_supply_households | Total supply households reported for the project |
| first_priority_competition_rate | AptToSell derived project-level first-priority competition rate |
| competition_band | Competition-rate analysis band |
| min_model_top_price_10k_krw | Lowest model-level top sale price in units of KRW 10,000 |
| project_max_price_10k_krw | Highest model-level top sale price in units of KRW 10,000 |
| weighted_representative_price_10k_krw | Housing-model top prices weighted by general + special supply households |
| price_band | Project maximum-price analysis band |
| followup_supply_observed | Whether a matched later residual/unsold or optional-supply announcement was observed |
| followup_event_count | Number of matched follow-up supply announcements |
| days_to_first_followup | Days from initial announcement to first matched follow-up event |
| eligible_60d_observation | Whether at least 60 days of observation time were available by 2026-10-04 |
| followup_within_60d | Whether first follow-up occurred within 60 days; blank when the project was not 60-day eligible |
| source_url | ApplyHome detail-page URL for the initial announcement |

## Important interpretation notes

1. **followup_supply_observed is not a contract failure rate.** It only indicates that a later official residual/unsold or optional-supply announcement was matched to the initial project.
2. A blank `followup_within_60d` means the project did not yet have 60 days of observation time as of the cutoff, not that no follow-up occurred.
3. Price fields preserve the ApplyHome API unit of **KRW 10,000**.
4. The project-level competition rate is a derived metric. First-priority applicant counts are aggregated and divided by model-level general-supply households counted once per model.
5. Special/reissued notices such as member-cancellation supply, vacant-unit resale, additional recruitment and other non-initial notices are excluded from the primary cohort.

## Related files

- Summary statistics: `reports/apttosell-followup-analysis-2026-jan-sep-summary.csv`
- Methodology: `reports/apttosell-followup-analysis-2026-jan-sep-methodology.md`
- Canonical report: https://apttosell.com/%ec%b2%ad%ec%95%bd-%ea%b2%bd%ec%9f%81%eb%a5%a0/
