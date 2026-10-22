# N01 — batch 7: remaining 11 provisionally eligible rows (2026-10-22)

Recomputed directly from user-supplied archive `N01_7th_107records.zip`: source CSV counts 39+24 for Ulsan 31710, 2+1 for Sejong 36110, 33+8 for Cheongju 43113 = **107 raw**, filtered `dealingGbn=중개거래`, `slerGbn=개인`, `buyerGbn=개인`, `ownershipGbn != 입`, `cdealType != O` -> **49 provisional rows**. Of those, 18 already in existing source-price reference pool (Gagyeong6 6, Namulsan 5, Doosan4, Artera A8 3); 20 Ulsan Down2 B-2 candidates blocked on 301-1/305 cadastral alias; **11 distinct remaining rows**. These are all a subset of the existing 606 provisional eligible, NOT additions.

| Source project | Candidate count | Exact reported area / floor only | Matching gate / caution |
|---|---:|---|---|
| 태화강 에피트, BL-S1 | 2 | 84.7646 / 3F, 8F | Need original official block S1 offer notice to verify BL-S1 identity and floor prices |
| 울산KTX 우방 아이유쉘 퍼스트, 삼남읍 신화리 1601-2 | 1 | 84.9850 / 26F | Need original government approval notice + detailed floor pricing |
| 세종 5-1 양우내안애 아스펜, 합강동 22-28 | 2 | **84** / 8F and **84.5013** / 10F | Original notice ID `2024000725`, approval 세종시 주택과-887 (2025-01-09), site L12BL. **Reported '84' precision insufficient** to uniquely map subtype; 84.5013 equals official 84A actual area. Do not convert 84 to 84.5013. Original notice source: https://image.r114.co.kr/imgdata/notice_file/2025/A17010040250001.pdf . Later 임의공급 is a distinct round, not initial pricing. Official KHBA confirms project L12BL: https://khba.or.kr/user/isale/moveInInfo.do?busiResuSeq=1&memSeq=2024-0080 |
| 해링턴 플레이스 테크노폴리스, 송절동 513-2 | 1 | 84.9707 / 23F | Need official project lot/physical area and original notice |
| 복대자이 더 스카이, 복대동 100-28 | 2 | 103.9937 / 36F and 3F | KHBA confirms exact official site, total 715 homes: https://www.khba.or.kr/user/isale/isaleInfo.do?busiResuSeq=331&memSeq=2004-1076 . Original 2023 recruiting notice price table pending |
| 복대자이더스카이, 복대동 **3411** | 1 | 84.9977 / 41F | Same project name (different spacing) but **different lot**. Do NOT auto-merge with 100-28 until cadastral road-to-old lot or building/lot crosswalk; project identity blocked |
| 신영지웰 푸르지오 테크노폴리스 센트럴, 송절동 산4-2 | 2 | 130.8820 / 4F and 111.8417 / 46F | Need official construction plot and subtype floor price; unusual tall-floor difference requires correct type |

Checks: 2+1+2+1+2+1+2=**11**. The 11 rows have **no new unit original-source reference values established** by this triage. Stage: 11 outstanding `PROJECT_SOURCE_NOTICE_OR_SUBTYPE_PENDING`. Name similarity is never enough to establish lot equivalence. Transaction price `dealAmount` is not used to calculate premium. Published older 980 aggregate is separate. Live global 824 raw, 606 screened provisional, 21 notice source reference candidates, 0 finalized monetary comparisons unchanged. Ministry reply not found in connected Gmail searches as of 2026-10-22; that search does not prove that a reply wasn't delivered via a different route.

Next: original official initial notice and specific area/floor tier for KHBA site-confirmed 복대자이 2 and 세종 아스펜 84.5013/10F; retain 84/8F as unidentified floor type until full-precision record is available.
