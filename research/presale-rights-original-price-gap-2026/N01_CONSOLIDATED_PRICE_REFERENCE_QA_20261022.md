# N01 consolidated original-offering reference-price QA — 2026-10-22

This file consolidates existing N01 GitHub QA. **It does not certify a resale original-price spread, premium, or financial profit.** Only the original notice's type/floor reference amounts are classified. No raw per-transaction reported prices are included.

| Project | Original notice ID | Preliminary transactions | Unique original notice price | Ambiguous source price | Evidence limitation |
|---|---|---:|---:|---:|---|
| 청주 가경 아이파크 6단지 | 2023000621 | 6 | 6 | 0 | User-supplied municipality-approved-number PDF SHA256 d4377061d8b2bb43d2caa25e370b2375e920ebdff49ef583c77ffac1e199bffe; later corrections not ruled out |
| 남울산 노르웨이숲 | 2024000750 | 5 | 3 | 2 | Official condensed PDF; two candidates have building/line dependent original price |
| 두산위브더제니스 청주 센트럴파크 | 2025000466 | 4 | 4 | 0 | Price tiers indexed from original notice, PDF binary/hash pending |
| 청주테크노폴리스 아테라 A8 | 2024000264 | 3 | 3 | 0 | Developer original condensed PDF; corrections and binary/hash pending; never use separate A7 prices |
| 탕정 푸르지오 리버파크 C2 | 2023-10-25 notice | 3 | 3 | 0 | Developer original notice; original lot/notice amendments and per-transaction price semantics pending |
| **Unique project subtotal** | | **21** | **19** | **2** | **0 finalized API-versus-original-price financial comparisons** |

## Excluded from price-reference subtotal
울산 다운2지구 우미 린 더 시그니처: 20 preliminary candidate trades; 19 exact-area correspondence to original official types and one unmatched area. Transactions use 서사리 301-1; official housing block is 서사리 305/B-2BL. Worksite notices associate 301-1 with the named project but cadastral inclusion/renumbering is unproven, so **all 20 remain outside the price-reference 21**. No conversion of 19 matches to confirmed joins.

## Type/floor reference rows (unit: KRW)
- Gagyeong IPARK6: 84.9967 17F 433,000,000; 84.9967 24F 437,000,000; 99.9745 22F 504,000,000; 101.9926 6F 510,000,000; 101.9926 18F 515,000,000; 116.9892 15F 588,000,000.
- Namulsan Norway Forest: 59.9957 4F 324,000,000; 59.9957 19F 324,000,000–334,000,000 (ambiguous building/line); 74.5847 9F 398,000,000–410,000,000 (ambiguous building/line); 84.9350 14F 480,000,000; 84.9350 24F 489,000,000.
- Doosan Zenith Cheongju: 74.8409 8F 432,000,000; 74.8409 12F and 13F each 437,000,000; 84.3782 4F 467,000,000.
- Artera A8: 84.9565 1F 352,000,000 (84AL; same-area ALD has no 1F units); 84.6592 12F 427,000,000 (84BH); 84.9810 12F 401,000,000 (84CL).
- Asan C2: 84.9008 8F 429,000,000 (two separate preliminary transaction rows); 74.9376 2F 348,000,000.

## Non-overlap and counting discipline
The 18 candidates in Gagyeong6 (6), Namulsan (5), Doosan (4), Artera A8 (3) belong to new batch 7; Asan C2's three belong to previous collected cohort. All counts represent source rows in separate project+area+floor (and, when repeats, contract-month) categories, *not guaranteed unique government filings*. No novel candidates beyond the earlier 606 provisional sample. Live collection total **824 raw / 606 prelim eligible**; distinct earlier published N01 980 aggregate is not reproduced.

## Blocking gates
1. Agency clarification of the MOLIT SilvTrade API `dealAmount` components remains pending, so do not equate reported total minus original supply price to premium.
2. Subsequent corrections, supply-condition changes and specific unit-contract changes may alter comparison applicability.
3. Two Namulsan building/line price ambiguities remain even at original notice reference level.
4. Down2 cadastral site identity and mismatched area remain blocked.
5. October 2026 API data partial and revisable.

No new DOI, no statistics describing price spreads or profits, and no raw transaction-price data shared in this public file.

Prior QA docs: N01_GAGYEONG_IPARK6_NOTICE_GATE_20261021.md; N01_NAMULSAN_5_CANDIDATE_QA_20261022.md; N01_CHEONGJU_DOOSAN_ATERA_7_CANDIDATES_QA_20261022.md; N01_ARTERA_A8_CORRECTION_CHECK_20261022.md; ASAN_C2_3CANDIDATE_FLOOR_QA_20261020.md; N01_ULSAN_DOWN2_IDENTIFICATION_QA_20261021.md.
