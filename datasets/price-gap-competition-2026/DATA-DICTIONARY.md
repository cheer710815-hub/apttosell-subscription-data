# Data Dictionary — v1.0

| Column | Definition |
|---|---|
| `year` | Announcement year (2025 or 2026). |
| `house_manage_no` | Official housing management number used as the project identifier. |
| `project_name` | Subscription announcement project name. |
| `announcement_date` | Subscription announcement date. |
| `region` | Subscription region label. |
| `lawd_cd` | Five-digit legal-dong API area code. |
| `target_dong` | Matched legal dong/eup/myeon. |
| `first_priority_ratio` | Project-level first-priority subscription competition ratio. |
| `log_competition` | log(1 + first_priority_ratio), baseline dependent variable. |
| `presale_84_max_10k` | Maximum 84㎡-class presale price, KRW 10,000 units. |
| `trade_10y_count` | Number of qualifying comparison transactions from stock completed within 10 years. |
| `trade_10y_median_10k` | Median qualifying <=10-year comparison transaction price, KRW 10,000 units. |
| `price_margin_pct_10y` | Price merit relative to the <=10-year median; positive means the comparison-market median is above the presale price. |
| `trade_5y_count` | Number of qualifying comparison transactions from stock completed within 5 years. |
| `trade_5y_median_10k` | Median qualifying <=5-year comparison transaction price. |
| `price_margin_pct_5y` | Price merit relative to the <=5-year median. |
| `region_group` | Analytical region group. |
| `seoul_flag` | 1 for Seoul. |
| `prime_seoul_flag` | 1 for the study prime-Seoul definition. |
| `capital_region_flag` | 1 for Seoul/Incheon/Gyeonggi. |
| `margin_band_10y` | Categorical 10-year price-merit band. |
| `atypical_candidate` | Atypical-supply flag. |
| `atypical_reason` | Reason for atypical-supply classification. |
| `source_status` | Source/verification status. |
| `school_proxy_score` | Reserved external-control field; not a completed baseline control. |
| `academy_density` | Reserved external-control field. |
| `nearest_station_m` | Reserved transport-control field. |
| `cbd_access_min` | Reserved CBD-access field. |
| `brand_tier` | Reserved brand-control field. |
| `total_units` | Reserved project-size control. |
| `reconstruction_flag` | Reserved redevelopment/reconstruction control. |
| `price_cap_flag` | Reserved price-cap control. |
| `regulated_area_flag` | Reserved regulated-area control. |
| `resale_limit_months` | Reserved resale-restriction control. |
| `residency_obligation_months` | Reserved occupancy-obligation control. |
| `market_sale_index_3m` | Reserved 3-month sale-market control. |
| `market_sale_index_6m` | Reserved 6-month sale-market control. |
| `market_jeonse_index_3m` | Reserved 3-month jeonse-market control. |
| `unsold_units_region` | Reserved regional unsold-housing control. |
| `completed_unsold_region` | Reserved completed-unsold control. |
| `recent_supply_units_6m` | Reserved recent-supply control. |
| `recent_hot_ratio_median_6m` | Reserved recent local subscription-heat control. |
| `mortgage_rate` | Reserved mortgage-rate control. |
| `year2026` | 1 for 2026 announcements. |
| `seoul` | Model-ready Seoul indicator. |
| `prime` | Model-ready prime-Seoul indicator. |

Reserved external-control fields are retained in the schema but are not treated as populated baseline controls unless values are explicitly present and verified.
