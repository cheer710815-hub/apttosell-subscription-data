# N01 batch 7 — Cheongju Doosan / Artera A8 matching gate (2026-10-22)

Private underlying evidence: user-uploaded batch-7 43113 202609 and 202610 original CSVs. Include only intermediary trades between individuals, excluding `ownershipGbn=입` and `cdealType=O`. No per-trade reported amounts are published.

## Doosan Weve the Zenith Cheongju Central Park
- Source alias: `두산위브더제니스 청주 센트럴파크`; raw cadastral location `신봉동 528` matches original notice `신봉동 528번지 외 3필지`.
- Original offering 2025-10-17, ID `2025000466`; municipal approval 청주시 공동주택과-37756 (2025-10-16). Indexed original 2025 notice PDF https://eparajoo.com/ ; original developer publisher https://두산위브더제니스청주센트럴파크.com .
- Exact 4 preliminary candidates: 74.8409㎡/8F, 74.8409㎡/12F, 74.8409㎡/13F, 84.3782㎡/4F. Official types `074.8409`, `084.3782A` match. Separate `ownershipGbn=입` rows (same project) were excluded and must NOT creep into presale-right source cohort.
- Original notice publicly indexed type maximum values 74=441m KRW, 84A=491m KRW; these are **NOT their candidate floor-tier source prices**. Exact relevant floor rows are pending direct verification. Distinguish later 2025-11-26 no-rank offering (different round, notice `무순위`): do NOT substitute its unit prices.
- Status `PROJECT_LOT_AREA_MATCHED_FLOOR_PRICE_PENDING`.

## Cheongju Technopolis Artera 1 (A8 Block)
- Source raw label `청주테크노폴리스 아테라 1차 (A8블록)`, location `송절동 19`, same as 2024-06-21 initial approved notice `2024000264` (municipal approval 24286 dated 2024-06-20). Official referenced price/area notice PDF: https://cdn.weolbu.com/data_file/3885954d-e8e6-4cd8-a130-2d543de282d7.pdf ; initial project official brochure: https://arteracj.co.kr/data/cy/ng01.pdf ; government institutional confirmation for the A8 address/area: https://www.mss.go.kr/common/board/Download.do?bcIdx=1050498&cbIdx=249&streFileNm=16e880e1-ddfd-4dc5-9c13-b9ee61a293ea.pdf .
- Exact 3 preliminary candidates: 84.9565㎡/1F -> original *physical subtype* `84AL` or `84ALD`, both share 84.9565; 84.6592㎡/12F -> `84BH`; 84.9810㎡/12F -> `84CL`. Notice application categories `084.0000A` and `084.0000C` are **grouping codes not true four-decimal exclusive area**. Never match raw area to fictitious `84.0000` square meters; use physical subtype.
- Original notice headline max prices at abstract application type level are NOT floor/subtype prices. `84.9565` retains `AMBIGUOUS_PHYSICAL_SUBTYPE`, others `FLOOR_PRICE_PENDING`. Distinguish separate A7 2nd project and its later 2025 announcement `2025000100`: do not borrow its prices.
- Status `PROJECT_LOT_AREA_MATCHED_SUBTYPE_OR_PRICE_PENDING`.

## Research guardrails
Combined 7 preliminary cases all connected at project/lot/physical-area level, but none is a verified source price-by-floor comparison. No API `dealAmount` equivalence clarification yet, and later pricing amendments are unverified. Therefore final validated resale-to-original-price comparison remains 0, live raw 824 and preliminary screened 606 unchanged. Old N01 DOI 980-case aggregate remains separate. No new DOI, no premium/profit arithmetic.
