# 2026 Korean Apartment Subscription Demand and Relative Price Gap (RPG) — v1.0.1
RPG(%) = (comparable housing price - sale price) / sale price × 100.

Frozen rule: pre-announcement 6 months; cancelled transactions excluded; exact duplicates removed; exclusive area ±5%; completion age ≤20 years; ≥3 transactions per comparable apartment; same legal dong preferred; same si/gun/gu fallback when fewer than 3 same-dong comparables exist; ≥3 comparable apartments per type; apartment-level medians before the median across apartments.

Dataset: 183 projects; 163 high-quality projects; 857 housing types; 15502 comparable-audit rows. Quality grades A 601, B 184, C 72; warnings 181.

Frozen regression: `log(1 + first_priority_applicants) ~ RPG + log(project_top_price) + log(general_supply) + broad_region`; Gyeonggi/Incheon reference; HC3 robust SE.
Full N=183: RPG 0.027407, p=0.000397783; R² 0.295033→0.333052.
High-quality N=163: RPG 0.027898, p=0.009803703; R² 0.278263→0.308556.

Association only, not causality. RPG is not guaranteed profit or expected return. License: CC BY 4.0. v1.0.1 supersedes exploratory regression figures.
