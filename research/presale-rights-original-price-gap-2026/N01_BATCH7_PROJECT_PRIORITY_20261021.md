# N01 Batch 7: project prioritization and lot-number gates (2026-10-21)

Private primary source: user-uploaded N01_7th_107records.zip, six raw CSVs. Filter preliminary candidate: dealingGbn=중개거래, slerGbn=개인, buyerGbn=개인, ownershipGbn != 입, cdealType != O. Result **49 records across 12 distinct (region, aptNm, umdNm, jibun) combinations**. Report only aggregates, not transaction-level resale amounts.

| Candidate source project label / lot | Region | Count |
|---|---|---:|
| 울산 다운2지구 우미린 더 시그니처 / 서사리 301-1 | 31710 | 20 |
| 청주 가경 아이파크 6단지 / 가경동 330 | 43113 | 6 |
| 남울산 노르웨이숲 / 발리 440-1 | 31710 | 5 |
| 두산위브더제니스 청주 센트럴파크 / 신봉동 528 | 43113 | 4 |
| 청주테크노폴리스 아테라 1차 (A8블록) / 송절동 19 | 43113 | 3 |
| 태화강 에피트 / 굴화리 BL-S1 | 31710 | 2 |
| 세종 5-1 양우내안애 아스펜 / 합강동 22-28 | 36110 | 2 |
| 복대자이 더 스카이 / 복대동 100-28 | 43113 | 2 |
| 신영지웰 푸르지오 테크노폴리스 센트럴 / 송절동 산4-2 | 43113 | 2 |
| 울산KTX 우방 아이유쉘 퍼스트 / 신화리 1601-2 | 31710 | 1 |
| 해링턴 플레이스 테크노폴리스 / 송절동 513-2 | 43113 | 1 |
| 복대자이더스카이 / 복대동 3411 | 43113 | 1 |

## Official source reconciliation
1. Highest-count project `울산 다운2지구 우미린 더 시그니처` has private raw lot `301-1`, **but the 2023-10-20 presale public notice metadata for `울산 다운2지구 B-2BL` reports `서사리 305번지 일원`**, source listing: https://www.aptdamoa.com/sale-info/apt/2023000543/contents.html. This could reflect cadastral changes or an administrative proxy, but the project's identity and cadastral alias **must not be assumed**. Separate 2024 project `울산 다운2지구 우미 린 어반파크` is NOT the same project: https://ul2.lynn.co.kr/parcel-chungyak . For the 20 candidates, type areas in source: `84.955`, `84.9498`, `84.995`; the 2023 application notice listing shows only 84A, 84B in secondary sources. Area-to-type mapping unverified. **BLOCKED_PROJECT_LOT_ALIAS + BLOCKED_AREA_TYPE_MAPPING**. Do not borrow Urbanpark price schedules.
2. `청주 가경 아이파크 6단지`: six candidate areas 84.9967 (2), 101.9926 (2), 99.9745 (1), 116.9892 (1). Developer I-PARK confirms `가경동 330 일원`, types 84, 99, 101, 116, initial sale date 2023-11-24: https://www.i-park.com/project/view?seq=14416 . **PROJECT_IDENTITY_SUPPORTED**, but floor-specific prices and original/corrected PDF not yet verified. Best next official-price document priority.
3. `복대자이 더 스카이` and `복대자이더스카이`: source lots `100-28` and `3411`; do not merge names/alias without independent cadastral proof.
4. All remaining labels are only preliminary source-project names, not verified joins.

No resale-minus-original-price arithmetic, premiums, profits, final price matched rows, public statistical claims or new DOI. Live raw count=824; preliminary screened count=606. Existing published N01 980-case aggregate remains a different cohort. API dealAmount detailed composition clarification pending.
