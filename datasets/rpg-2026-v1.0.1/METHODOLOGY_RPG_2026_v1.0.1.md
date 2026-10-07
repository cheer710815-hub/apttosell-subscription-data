# Methodology — AptToSell RPG 2026 v1.0.1
Research unit: recruitment-announcement project (`HOUSE_MANAGE_NO`). Demand: total first-priority applicants.
RPG(%) = (comparable price - sale price) / sale price × 100; comparable price is the median of comparable-apartment medians.
Frozen construction: pre-announcement six months; cancellations excluded; exact duplicates removed; area ±5%; completion age ≤20 years; ≥3 transactions/comparable; same-dong preferred; same-si/gun/gu fallback if fewer than 3 same-dong comparables; ≥3 comparable apartments required.
Regression: `log(1 + first_priority_applicants) ~ rpg_pct_median + log(project_top_price_10k) + log(general_supply) + broad_region`; Gyeonggi/Incheon reference; HC3 SE.
Official: Full N=183, RPG=0.027407, SE=0.007739, p=0.000397783, R²=0.333052. High-quality N=163, RPG=0.027898, SE=0.010802, p=0.009803703, R²=0.308556.
Limits: micro-location, schools, transit, brand, floor/line, redevelopment expectations, views, financing and expected appreciation are not fully controlled. Results are associational.
