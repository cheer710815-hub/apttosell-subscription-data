# N01 government SilvTrade HWP technical schema review — 2026-10-22

Primary official public dataset: https://www.data.go.kr/data/15126471/openapi.do
Locally available 128 KiB HWP 5.0 document: `아파트 분양권전매 실거래가 자료 기술문서.hwp`. Parsed OLE BodyText/Section0 text in this session and independently examined response-field table and XML sample; this is an actual downloaded source document, not an inference from third-party articles.

## Confirmed response field definitions
- `dealAmount`: exactly **거래금액 (만원)**, sample value `95,815`.
- `ownershipGbn`: **구분: 분양권 및 입주권**; migration mapping section explicitly reads `입주권일경우만 ‘입’으로 표기`. This clarifies coding intent but does not establish completeness/accuracy of blank data in every API row.
- `dealingGbn`: **거래유형 (중개및직거래여부)**.
- `slerGbn`, `buyerGbn`: transaction actor (개인/법인/공공기관/기타).
- `cdealType`: 해제여부; `cdealDay`: 해제사유발생일.
- Other source fields include apartment, lot, legal-dong, area, floor, contract date and broker district.

## Critical undefined monetary semantics
The HWP describes `dealAmount` as **거래금액(만원)** only. It does **not** define composition relative to the original supply contract price, premiums, balcony expansion, options, paid instalments, contract revisions, other fees, or seller net gain. The HWP provides no validated identity such as dealAmount = initial supply price + premium; any subtraction yielding premium/profit is unsupported.

The public portal description says only **floor** is provided for transfer rights for privacy, preventing unit/building-line identification in some original pricing tables. Official written agency reply already requested on 2026-10-21 remains an unresolved research gate; this file does not assert the reply's existence or content.

## Decision
Maintain `AMOUNT_COMPONENTS_UNVERIFIED` and stop at reference prices for 21 candidate source rows (19 uniquely mapped source tier values and two line-dependent intervals) across five projects. New collected 824 raw / 606 preliminary screened, finalized resale-price comparisons 0. Historical published 980 N01 aggregate is separate; do not create duplicate DOI or publish purported premium/gain.

## Evidence trace
HWP section `상세기능내역` response items, including exact line:
`dealAmount / 거래금액 / 거래금액(만원)` and XML `<dealAmount>95,815</dealAmount>`.
HWP response mapping appendix: `ownershipGbn / 구분 / 분양권및입주권 (입주권일경우만 ‘입’으로표기)`.
