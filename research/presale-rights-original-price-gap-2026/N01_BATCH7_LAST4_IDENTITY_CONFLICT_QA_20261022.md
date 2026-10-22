# N01 batch 7 — last four identity and transaction-type conflicts, 2026-10-22

Source of candidate descriptions and preliminary screening: user-supplied N01_7th_107records.zip in this conversation, checked from CSV. Only aggregate or type/floor information stored, no individual contract reported amounts. This does not increase existing 824 source records or 606 preliminary screened cases.

| Source site | Observed source area, floor | Finding | Gate |
|---|---|---|---|
| 울산KTX 우방 아이유쉘 퍼스트, 신화리 1601-2 | 84.9850, 26F | **2022-10-12 initial project** source areas are 84.9269, 84.9781, 84.9078 etc. **2025-09-19 separate published offer** at same lot for **울산역 폴리시아 아이유쉘**, notice 2025000437, has 84.9850A exactly. Historic report label points to old name even though area is aligned with new project. Before notice-price mapping, prove redevelopment/renaming/rights contractual genealogy and attach appropriate notice version. No shortcut matching by lot alone. | SOURCE_PROJECT_NAME_NOTICE_CONFLICT |
| 해링턴 플레이스 테크노폴리스, 송절동 513-2 | 84.9707, 23F | Initial offer 2023000141 dated 2023-04-21 same site. However a third-party RTMS display labels same source area/floor/2026-09-12 date **입주권**, while our raw API `ownershipGbn` is blank. The third-party label is not definitive, but introduces a **classification discrepancy** needing independent official verification. Do NOT promote to certified presale rights, and no source-price result until resolved. | OWNERSHIP_TYPE_CONFLICT |
| 세종 5-1 양우내안애 아스펜, 합강동 22-28 | 84.0000 (raw source `84`), 8F | Raw precision too low to choose from multiple actual physical 84xx sqm subtypes in notice 2024000725. Must not fill in the missing decimals from a grouped application code, and do not quote an individual floor price. | AREA_PRECISION_BLOCK |
| 복대자이더스카이, 복대동 3411 | 84.9977, 41F | Other verified-source project lot 100-28, same-looking project alias but no documented cadastral crosswalk to 3411. A name match alone is not evidence of identical transaction location and original price. | CADASTRAL_ALIAS_BLOCK |

## Reference evidence
- 2025 울산역 폴리시아 아이유쉘 announcement number and location: https://www.aptdamoa.com/sale-info/apt/2025000437/contents.html ; first-offering 2022 areas and distinct 2025 areas collated at https://aptsonpoom.com/danji/P1LYC9XDA7 (secondary; project 2025 original PDF still needed).
- 2023 Harrington original notice metadata: https://silgga.com/bunyang/2023000141 . Third-party transaction classification discrepancy: https://ndsts.com/apt_buy/apt_buylist_name?apt_name=%ED%95%B4%EB%A7%81%ED%84%B4%ED%94%8C%EB%A0%88%EC%9D%B4%EC%8A%A4%ED%85%8C%ED%81%AC%EB%85%B8%ED%8F%B4%EB%A6%AC%EC%8A%A4&dong=%EC%86%A1%EC%A0%88%EB%8F%99&region_code=43113 . Third-party is NOT dispositive; revalidate with government classification.
- Aspen official 2024000725 notice already reviewed in N01_BOKDAE_ASPEN_3_FLOOR_TIERS_20261022.md . 
- Bokdae official-lot identity gate already in N01_BATCH7_REMAINING_11_TRIAGE_20261022.md .

## Arithmetic
Batch7 raw 107, provisional screened 49: reference-valued candidates **25** in batch7 (earlier 18 + Bokdae/Aspen 3 + Taehwagang/ShinYoung 4); blocked Down2 20, last 4 remain identity/type ambiguous. Check 25+20+4=49 exactly. Overall references **28** across new and older batches: batch7 **25** plus older Asan C2 **3**; unique original notice reference tiers **24**, building-line ambiguous **4**. No increase due to last four. NOTE: preliminary status of Harrington may require reclassification upon official correction, so 606 not guaranteed stable.
- Overall 824 raw, 606 preliminary screened, **0 finalized monetary difference comparisons**, API `dealAmount` components still not mapped, no new DOI or premium calculations.
