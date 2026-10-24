# N01 — 청주 가경 아이파크 6단지 original notice linkage QA (2026-10-21)

## Sources and precise status
- Private source: N01 7th 107-record ZIP, specifically region 43113 CSVs for Sep/Oct 2026. Presale preliminary screen per existing batch-7 QA.
- Official developer HDC IPARK: https://www.i-park.com/project/view?seq=14416 ; address 충북 청주시 흥덕구 가경동 330 일원, 946 households, 84/99/101/116 sqm, offered 2023-11-24.
- Original published recruitment announcement identifier `2023000621`, Nov 24 2023, originally approved Nov 23 2023. Search-indexed announcement copies show exact area names, and state balcony expansion/options are **excluded** from quoted supply price (VAT included for units >85 sqm). Indexed original notice PDF search result was found but its **PDF binary could not be retrieved and independently inspected**, so do not claim notice PDF archival verification, per-page floor prices, correction absence, or SHA256.
- Highest supply-price summaries from application data, not floor-specific official PDF rows, in KRW 10,000: 84.9967=43,700; 99.9745=50,400; 101.9926=52,000; 116.9892=59,400. Source (summary, not a floor table): https://youngkk.com/housing/notice/apt/2023000621-2023000621 ; secondary detailed notice index: https://eparajoo.com/ .

## Six individually distinct preliminary transactions, date/amount deliberately unpublished
| Original sale area sqm | Source-reported floor | Rows | Original project/type/lot correspondence |
|---|---|---:|---|
| 84.9967 | 17, 24 | 2 | Supported at project and exact area level |
| 99.9745 | 22 | 1 | Supported at project and exact area level |
| 101.9926 | 6, 18 | 2 | Supported at project and exact area level |
| 116.9892 | 15 | 1 | Supported at project and exact area level |

The above six are **PROJECT_AND_AREA_MATCHED_FLOOR_PRICE_PENDING**, NOT independently checked exact-floor original-price joins. The presence of a publicly indexed PDF or a highest price does not establish the 6 floor-specific values; floor-specific notice rows and notice revisions are still needed. Trade amount `dealAmount` composition remains officially unanswered; no resale-minus-offering arithmetic, premium, profit, new DOI, or 980-reproduction claims.

## Next source-acquisition requirement
Acquire immutable publisher or government original/corrected 모집공고 PDF for `2023000621`; retain SHA256 and page references and extract price rows applicable to floors 6, 15, 17, 18, 22, 24 (with building-dependent grouping if specified). Until then the 6 records are eligible at *project/area* reference level only; final verified resale-price-to-original-price 0.

## 2026-10-21 further evidence: indexed full notice's floor-specific supply-price table

The search-indexed text of the 2023 original 모집공고 (no original PDF binary acquired; **not archive-verified**) has directly surfaced the floor-tier schedule for all six source type-and-floor candidates. The table is stated in KRW (not KRW 10,000). Reference full notice mirrors: https://eparajoo.com/ (indexed file-download notice for 2023000621) and https://byw.kr/wp-content/uploads/2023/11/ (public 2023-11 notice mirror). Search textual evidence, not document-binary checksum.

| Raw exclusive area sqm | Candidate floor | Notice price KRW | Original schedule tier |
|---|---:|---:|---|
| 84.9967 | 17 | 433,000,000 | 10–19F |
| 84.9967 | 24 | 437,000,000 | 20F+ |
| 99.9745 | 22 | 504,000,000 | 20F+ |
| 101.9926 | 6 | 510,000,000 | 5–9F |
| 101.9926 | 18 | 515,000,000 | 10–19F |
| 116.9892 | 15 | 588,000,000 | 10–19F |

**Evidence update:** six of six type/floor original schedule tier prices identified by search-indexed notice text. This improves prior `FLOOR_PRICE_PENDING` to `FLOOR_PRICE_INDEXED_TEXT_VERIFIED_PDF_UNARCHIVED`; it does not imply final financial comparisons. Source notice says balcony expansion and additional choices excluded from basic supply prices; the three >85 sqm types have VAT included. Corrected/replaced notices and individual sale-price revisions have not been ruled out; API dealAmount official composition clarification remains pending. No premium/gain claimed, no new DOI; six original resale-to-sale-price joins remain **provisional, not validated**.

## 2026-10-21 PDF trace and provenance follow-up

A **direct linked PDF attachment** for the named 2023 notice was located at this dated third-party 2023-11-30 distribution page: https://onedang.tistory.com/entry/%EC%B2%AD%EC%A3%BC-%EA%B0%80%EA%B2%BD-%EC%95%84%EC%9D%B4%ED%8C%8C%ED%81%AC-6%EB%8B%A8%EC%A7%80-%EC%B2%AD%EC%95%BD-%EC%9E%85%EC%A3%BC%EC%9E%90%EB%AA%A8%EC%A7%91%EA%B3%B5%EA%B3%A0%EB%AC%B8-%EB%B6%84%EC%96%91%EA%B0%80-%ED%8F%89%EB%A9%B4%EB%8F%84-%EC%A0%95%EB%B3%B4 . The anchor visibly names `2023000621 ... 입주자모집공고문.pdf` and identifies an ~1.66 MB attachment; the file host is Kakao CDN. The web downloader returned an unsupported/octet-stream content type, while the container could not access the page over HTTPS, so **the PDF binary was NOT acquired, SHA256 NOT computed, and full pages NOT directly checked**. An independent 62-page indexed PDF-text source on another public-hosted notice link carries the first page's jurisdictional approval `청주시 공동주택과-40557호 (2023.11.23)`, project `가경동 330`, and page 62 developer/footer; this bolsters the document identity but remains index-level evidence, not a verified downloaded master copy.

A search for correction notices surfaced an unrelated **2026 Cheonan I-PARK CITY 6** notice. That project is not 2023 **Cheongju Gagyeong IPARK 6**; do **not** treat it as a correction or use its prices. No Cheongju-specific correction notice was identified by the queries run; **absence is unproven** and remains `NOTICE_VERSION_UNVERIFIED`.

Status: six tentative floor-tier prices sourced from indexed text, 0 final certified resale/original-price comparisons. Next valid upgrade requires direct source PDF acquisition (or user upload) and SHA256 + notice-page references, plus a correction/version check. Do not create a new DOI or public spread/premium claim.

## 2026-10-21 approved-number PDF received and directly compared

A second user-supplied 62-page PDF, SHA256 `d4377061d8b2bb43d2caa25e370b2375e920ebdff49ef583c77ffac1e199bffe` (1,743,633 bytes), states Cheongju municipal notice approval `공동주택과-40557호 (2023-11-23)` on page 5, and project ID 2023000621. It is **distinct** from the earlier `(안)` 1,783,130-byte draft SHA256 `eddbacc148993e6740ec27401054efe6a90e0311b053832d9277636a1a525320`, whose approval number was `0000호`. The two 62-page PDFs were programmatically compared page by page: text identical on 60/62 pages; only page 5 approval identifier/date and page 30 typo `혼일` vs `혼인` differ. The complete source price-table text on PDF pages 6 and 7 was identical. Final-approved-number PDF directly supports candidate area/floor original schedule prices: 84.9967 17F 433m KRW, 84.9967 24F 437m, 99.9745 22F 504m, 101.9926 6F 510m, 101.9926 18F 515m, 116.9892 15F 588m. **6/6 floor-price source matches confirmed in document containing the original municipal approval number.** This is a successful original-notice-source validation, but **not** proof there were no later amendments, nor a determination of which components API `dealAmount` contains. Thus 0 final publishable price-gap joins; no premiums/profit published, no new DOI. Keep the two PDF binaries private, only record hashes.

## 2026-10-21 follow-up — correction search gate

Rechecked uploaded approved-number 62-page PDF with PyMuPDF: 1,743,633 bytes, SHA256 d4377061d8b2bb43d2caa25e370b2375e920ebdff49ef583c77ffac1e199bffe; page 5 approval number 40557 (2023-11-23); pages 6–7 direct supply price table present. Searches specifically combining project name, `2023000621`, 정정공고/변경공고/공급금액 found no independently identifiable correction changing this project's original price schedule. **This is a non-discovery, NOT proof of no correction**; retain NOTICE_VERSION_UNVERIFIED for later amendments. Developer project page https://www.i-park.com/project/view?seq=14416 identifies 2023 original Gagyeong IPARK 6, not 2026 separate Gagyeong IPARK 7/8. Six floor-tier source prices retain ORIGINAL_APPROVED_NUMBER_PDF_CHECKED; zero finalized dealAmount-based price differences while official API interpretation is pending.

## 2026-10-22 direct local approved-PDF recheck

Approved-number user-supplied source `8bb0b98144b51075f98f20724e42e3a9_1725519974.pdf`: **62 pages**, SHA-256 `d4377061d8b2bb43d2caa25e370b2375e920ebdff49ef583c77ffac1e199bffe` (recomputed from bytes 2026-10-22). PDF p.5 printed has approval `청주시 공동주택과-40557호(2023.11.23.)` and site `가경동 330`. PDF p.6 printed begins the `공급금액 및 납부일정(발코니 확장금액 별도)` table; source explicitly defines amounts as won, VAT included where applicable. Table rows checked directly include 84-type 10–19F 433,000,000 / 20F+ 437,000,000; 99-type 20F+ 504,000,000; 101-type 5–9F 510,000,000 and 10–19F 515,000,000. The 116-type 15F reference 588,000,000 was reported in the previously validated table. Thus the source's floor-group schedules corroborate six prior candidate reference values; **binary is physically present and hash verified**. No new row cohort, price gap, premium or profit has been established. Later contract amendments, corrections and authority mapping of trade amount remain unresolved; final comparisons 0.

## 2026-10-24 approved-PDF reacquisition
The archived approved 62-page notice PDF was recovered from file Library as `8bb0b98144b51075f98f20724e42e3a9_1725519974.pdf`, 1,743,633 bytes, SHA256 `d4377061d8b2bb43d2caa25e370b2375e920ebdff49ef583c77ffac1e199bffe`, matching the previously noted municipal-approved copy. Physical page 6 original floor schedule plus page 7 continuation checked directly from the local PDF; candidate price refs 84.9967 17F 433m and 24F 437m; 99.9745 22F 504m; 101.9926 6F 510m and 18F 515m; 116.9892 15F 588m KRW. Newly generated six-row reconciliation file `N01_Gagyeong6_6_approved_notice_original_price_verified_20261024.csv`, SHA256 `04f351cfa9390a7d1157dcd27c28b013ab9125f87edf7cb800ccd0c198b38411`, produced locally, not archived in GitHub. Primary notice approval and floor prices are independently document-byte-validated, but row-level raw transaction source files are not available this session, later corrections and original contract price applicability remain open. These six ALREADY belong to reference pool 58; no new rows, no difference/premium. Counters stay 824 raw / 606 preliminary / 58 reference / 0 final monetary comparisons.
