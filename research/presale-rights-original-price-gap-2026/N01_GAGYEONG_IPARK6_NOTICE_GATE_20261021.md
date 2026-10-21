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
