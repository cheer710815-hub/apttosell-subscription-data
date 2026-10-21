# N01 — 울산 다운2지구 우미 린 더 시그니처 identification QA (2026-10-21)

Source: user-uploaded private batch-7 original transaction CSVs (31710/202609 and 31710/202610). Existing preliminary eligible filters yield 20 records, all labeled 울산 다운2지구 우미린 더 시그니처, 법정리 범서읍 서사리, 지번 301-1.

**Corrected official source lookup:** Initial secondary index incorrectly reported areas 84.9987/84.9426. **This was inaccurate for this project.** Direct Woomi official sales PDF https://ud2.lynn.co.kr/fileview/963/%EC%9A%B8%EC%82%B0%EB%8B%A4%EC%9A%B4_%EA%B3%B5%EA%B8%89%EC%95%88%EB%82%B4.pdf and published recruitment notice https://ud2.lynn.co.kr/fileview/945/%EB%AA%A8%EC%A7%91%EA%B3%B5%EA%B3%A0%28%EC%B6%95%EC%95%BD%EB%B3%B8%29.pdf identify **084.9550A** (84A, 1,159 total households = 253 presale-application + 906 main-sale) and **084.9498B** (84B, 271 = 68 presale-application + 203 main-sale). Main-sale total 1,109, whole project 1,430. Developer construction website https://www.lynn.co.kr/ko/movein/construction-view.do?product_works_id=200 gives **울주군 범서읍 서사리 305번지 일원 B-2BL** (not 301-1).

Private candidate distribution:
- `84.955`: **15 records**, same numeric area as official 084.9550A
- `84.9498`: **4 records**, exact 084.9498B
- `84.995`: **1 record**, no official type match, **EXCLUDE_FROM_TYPE_JOIN**
- Total 20; 19 area-matched, all 20 still **BLOCKED_PROJECT_LOT_ALIAS** until government or authoritative parcel-to-block crosswalk links 301-1 to official 305/B-2BL. Shared complex name and matching areas do NOT prove parcel alias.
- Official PDF floor tiers for 84B include 5–9F 431.5m KRW and baseline floor tier 439.8m KRW, but **no candidate floor-specific source price joins are authorized** until cadastral identity verified and reference floor range confirmed. No gap, no premium, no public individual transaction prices.
- Notice ID 2023000543 dated 2023-10-20, not a different 2024 Urbanpark project. Correction/amendments unverified. Official agency `dealAmount` composition response pending.

This QA fixes the erroneous area-code conclusion explicitly, without modifying N01 live raw 824/preliminary screened 606, historic N01 published 980, or final price gap count 0. No DOI.

## 2026-10-21 address link: construction-site evidence, cadastral inclusion still open

Independent 2023 construction-site job adverts explicitly describe **울산다운2지구 우미린 아파트현장 / 우미린 더 시그니처** with worksite **범서읍 서사리 301-1 일원**. See https://www.theteams.kr/recruit/wanted/2577428 and https://kor.748job.com/en/job/524529 . Separately, Ulsan city 2022 B-2BL traffic impact review specifies project site **서사리 305일원**, owner **우미개발**: https://www.ulsan.go.kr/u/traffic/transfer/vmtc/view.ulsan?curPage=11&mId=001002001002000000&vmtcNo=1055 ; developer project webpage agrees: https://www.lynn.co.kr/ko/movein/construction-view.do?product_works_id=200 .

This is new independent support that **301-1 was used as this project's construction worksite address** and helps explain raw transaction labeling. It is **not a cadastral parcel inclusion or lot-renumbering record**, nor a government assurance that 301-1 and 305 are interchangeable for any individual transaction. Status upgrade from `BLOCKED_PROJECT_LOT_ALIAS` to `WORKSITE_ALIAS_CORROBORATED_CADASTRAL_UNVERIFIED`, still **NOT price-join validated**. Keep 19 exact-area candidates and one area mismatch separate, final price comparisons 0. Seek land-division/land-register or developer's block parcel schedule for final cadastral equivalence; do not infer it from employment advertisements.
