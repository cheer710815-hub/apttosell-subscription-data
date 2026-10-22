# N01 — Namulsan Norway Forest: five batch-7 candidates QA (2026-10-22)

Private source: batch-7 raw CSV files, region 31710 contract months 202609 and 202610. Preliminary eligibility: intermediary transaction, both parties individuals, not recorded occupancy right and not cancelled. Five eligible rows (a sixth 84.4955/21F row is direct trade and excluded). All five source lots `온양읍 발리 440-1` match 2025 original notice address.

2025-01-24 initial notice number `2024000750`, Uljugun architecture approval `건축과-2935호`, 848 apartment units total with 332 general allocation, official-type areas: 59A 059.9957, 59B 059.9734, 74A 074.5847, 74B 074.9026, 84A 084.9350, 84B 084.4955. Primary original recruitment notice published by developer site: https://xn--q20blpu5qvwhh2bowlyjak1b.com/04/%EB%82%A8%EC%9A%B8%EC%82%B0_%EC%9E%85%EC%A3%BC%EC%9E%90%EB%AA%A8%EC%A7%91%EA%B3%B5%EA%B3%A0_%EC%B6%95%EC%95%BD%EB%B3%B8_fn2_0124.pdf ; public PDF is one-page reduced comprehensive table; direct text and screenshot inspected.

| Exact area sqm | Preliminary source floors | Eligible row count |
|---|---|---:|
| 59.9957 | 4, 19 | 2 |
| 74.5847 | 9 | 1 |
| 84.9350 | 14, 24 | 2 |

Critical: original supply prices vary **both by floor range and by specified building/line**, e.g. 59A 10–19F has multiple schedules dependent on building/line, therefore the source API's area and floor WITHOUT building/line cannot in general identify a unique original supply amount. Need enumerate possible official amounts per (area,floor) and report range/ambiguity internally; never impute a single original supply value without addressable building/line proof. Separate later 2026 association-member-cancellation recruitment notice (2026000004) must not be substituted for first offering.

Down2 B-2 LH district-drawing page could not be opened using the accessible browser; no cadastral proof of 301-1 vs 305, so its 19 candidate matches stay blocked. No premium or dealAmount-based price gap, no new DOI. Live sample raw 824 / screened 606 unchanged, final monetary joins 0.

## 2026-10-22 original notice price tier audit (primary 2025-01-24 one-page official reduced notice)

Primary publisher PDF: https://xn--q20blpu5qvwhh2bowlyjak1b.com/04/%EB%82%A8%EC%9A%B8%EC%82%B0_%EC%9E%85%EC%A3%BC%EC%9E%90%EB%AA%A8%EC%A7%91%EA%B3%B5%EA%B3%A0_%EC%B6%95%EC%95%BD%EB%B3%B8_fn2_0124.pdf ; price grid directly read from official reduced-notice PDF page 1. Supply prices are KRW; excludes separately contracted balcony extension and options.

| Area / type | Source floor | Relevant official building-line price, KRW | Status |
|---|---:|---|---|
| 59.9957 / 59A | 4 | 324,000,000 | **UNIQUE_NOTICE_TIER_PRICE** (other 112(4) line has no 3–4F units) |
| 59.9957 / 59A | 19 | 324,000,000 or 334,000,000 | **AMBIGUOUS_BUILDING_LINE** |
| 74.5847 / 74A | 9 | 398,000,000 or 410,000,000 | **AMBIGUOUS_BUILDING_LINE** |
| 84.9350 / 84A | 14 | 480,000,000 | **UNIQUE_NOTICE_TIER_PRICE** |
| 84.9350 / 84A | 24 | 489,000,000 | **UNIQUE_NOTICE_TIER_PRICE** |

Hence **3/5 candidate source floor-tier amounts unique within original published notice** and **2/5 ambiguous** due to lack of building/line in the public government trade API. The 2026 later cooperative/member cancellation notice is a different supply round and must never replace 2025 initial prices. Stage tag: `INITIAL_NOTICE_FLOOR_TIER_UNIQUE_3_AMBIGUOUS_2`. Even the three unique tier prices are **NOT guaranteed to equal each individual resale's originally contracted consideration** without original purchase contract and amendment verification. The agency interpretation of API `dealAmount` remains unresolved; thus no price gap, profit, or premium published, and final verified monetary gap sample stays zero. N01 newly collected 824 raw / 606 provisional screened unchanged.
