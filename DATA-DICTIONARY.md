# Data Dictionary — 2026 Housing Subscription Reference Tables

**Publisher:** AptToSell Data Project  
**Repository:** https://github.com/cheer710815-hub/apttosell-subscription-data  
**Canonical data center:** https://apttosell.com/housing-subscription-data/  
**Documentation checked:** 2026-11-03  
**License:** CC BY 4.0 (see repository licensing terms)

This dictionary documents the **two reference tables** below. It is not a dictionary for every analysis dataset or DOI cited elsewhere in the repository. Field definitions were checked against the actual public CSV headers and records, not inferred from their filenames.

## 1. `housing_subscription_score_2026.csv` — subscription-score reference

- **Observed rows:** 41, excluding header
- **Row grain:** one condition within one scoring category
- **Reference date field:** `base_date`; currently 2026-09-18 in the published CSV
- **Canonical description:** https://apttosell.com/cheongyak-score-data/

| Column | Type | Definition | Units / allowed values |
| --- | --- | --- | --- |
| `category` | string | One of the three scoring components. | `homeless_period`, `dependents`, `subscription_account_period` |
| `condition` | string | Encoded duration or dependent-count bracket within the component. | Codes such as `under_1_year`, `6_or_more`, `15_years_or_more`; interpret only within `category` |
| `score` | integer | Reference points assigned to the stated bracket. | Points, not a percentage |
| `base_date` | date string | Reference snapshot date used for this table. | `YYYY-MM-DD` |
| `canonical_source` | URL string | Canonical explanatory page for the reference table. | HTTPS URL |

**Integrity checks:** maximum score by category is 32 (homelessness), 35 (dependents), 17 (subscription account), totalling 84 points. A score is not an estimate of admission probability.

## 2. `private_housing_deposit_2026.csv` — regional deposit reference

- **Observed rows:** 4, excluding header
- **Row grain:** one housing-area eligibility band, with three location-specific reference deposit values
- **Unit:** `KRW_10k` = KRW 10,000 per numeric unit; for example, `300` means KRW 3,000,000
- **Source basis field:** currently `주택공급에 관한 규칙 별표2` in the published CSV

| Column | Type | Definition | Units / allowed values |
| --- | --- | --- | --- |
| `housing_area` | string | Housing size threshold / eligibility band. | `85sqm_or_less`, `102sqm_or_less`, `135sqm_or_less`, `all_areas` |
| `seoul_busan` | integer | Deposit reference value for Seoul and Busan. | `KRW_10k` |
| `other_metropolitan` | integer | Deposit reference value for other metropolitan cities. | `KRW_10k` |
| `other_city_county` | integer | Deposit reference value for other cities/counties. | `KRW_10k` |
| `unit` | string | Numeric deposit unit for the three location columns. | `KRW_10k` |
| `source_basis` | string | Stated regulation / source basis for the values. | Source citation text |
| `checked_date` | date string | Date the table's reference basis was checked. | `YYYY-MM-DD` |

**Important:** The size brackets and regional amounts are reference values, **not** a live eligibility decision. The applicant's region classification, relevant effective date, supply type, and latest recruitment notice must be checked separately.

## Scope, provenance, and citation

- `datapackage.json` is repository-level resource metadata; its version is **not** automatically the version of each separate DOI dataset.
- Current machine-readable files may be revised; for exact replication use a pinned Git commit, dated reference, or archived DOI record verified to contain the data.
- Original statutes, official notices, and corrections take precedence over this educational reference.
- For reproduction instructions see [REPRODUCE-REFERENCE-TABLES.md](REPRODUCE-REFERENCE-TABLES.md), and for general provenance see [METHODOLOGY.md](METHODOLOGY.md) and [SOURCE_POLICY.md](SOURCE_POLICY.md).
- **Suggested citation:** AptToSell Data Project. (2026). *South Korea Housing Subscription Reference Data: Scoring and Deposit Tables* [Data tables]. https://apttosell.com/housing-subscription-data/ ; check the specific archival identifier before citing a DOI.
