# N01 Jinju September–October 2026 authenticated raw-data QA

**Data cut: 2026-10-19. This is a partial-October pilot; not the nationwide N01 study nor a claim of price premium.**

Source: MOLIT SilvTrade API, legal area code 48170; raw user-provided exports, not included here.

| Field / selection | September (202609) | October (202610) |
| --- | ---: | ---: |
| Raw rows | 26 | 83 |
| Brokered `dealingGbn=중개거래` | 26 | 77 |
| Direct `dealingGbn=직거래` | 0 | 6 |
| Both seller/buyer marked private individual | 26 | 83 |
| `cdealType=O` cancellation-marked | 1 | 1 |
| Brokered, both individuals, **no cancellation marker** | **25** | **76** |
| Extra identical row contents in that subset | 1 | 3 |
| Unique **row contents** in that subset | 24 | 73 |

Two-month raw sum 109; brokered private-to-private without cancellation marker 101; unique row contents 97. **Do not treat identical rows as definitely duplicate filings**: no official unique transaction ID in exported fields.

October observed contract day range: 2–14 October, so this is not an entire calendar-month cohort. October cancellation was recorded with `cdealDay=26.10.14`. `ownershipGbn` is blank in all 109 rows; official source guide explains `입` marks occupancy rights, but the absence of a value is not independent transaction-by-transaction corroboration.

SHA-256 of received raw CSVs: September `8794f8e5857507c1e745dec29863a1119135867d813c6c6e73e1a145e39f9b89`; October `a97027320db67f41099ebf9669fad22f995b834d6897dafd7117bd83250b2a56`. October raw manifest not provided, so its `expected_total` and API `totalCount` were **not independently cross-checked**.

**Restrictions:** 980-observation nationwide N01 cohort not reconstructed; do not assume two-city-month sample is representative or complete. Original offering price crosswalk not verified. No full transaction-level values uploaded to the public GitHub repository.
