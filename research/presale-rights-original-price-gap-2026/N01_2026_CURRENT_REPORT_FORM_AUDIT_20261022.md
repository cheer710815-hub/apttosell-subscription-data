# N01 — 2026 effective transaction report form audit (2026-10-22)

## Authority and applicability
- Original current statutory Annex Form 1 PDF: https://www.law.go.kr/flDownload.do?bylClsCd=110202&flSeq=161474731&gubun=
- Regulation: 「부동산 거래신고 등에 관한 법률 시행규칙」, MOLIT Ordinance 1557, amended 2026-02-06, effective 2026-02-10. Art. 2(1) prescribes Annex 1. Supplementary provision applies amended form to contracts concluded from effective date: https://www.law.go.kr/lsInfoP.do?joNo=000200&lsId=012794
- PDF is 2 pages; visually inspected page 1 and page 2 (form and completion instructions).

## Exact current amount fields (PDF p.1 and instructions p.2)
- Section ⑧ `물건별 거래가격`: `공급계약 또는 전매` subcolumns `분양가격`, `발코니 확장 등 선택비용`, `추가 지급액 등`. Instructions ¶7: `추가 지급액 등` encompasses premium or amounts **above or below** sale price; include applicable VAT in each component.
- Section ⑨ `총 실제 거래가격(전체)`: aggregate total price, plus contractual deposit/interim/final instalments and payment dates. Instructions ¶8.
- Section ⑩ `종전 부동산`: for **입주권** only; prior property amount, additional amounts, entitlement price. Do not misread this as a required component of a 분양권.
- Notice ¶5: for supply or resale of rights, ⑧ and ⑨ include relevant VAT.
- Revision also adds foreign buyer statuses and contract deposit payment verification evidence for certain reporting procedures; these do not settle API monetary serialization.

## Compared with historical statutory reporting form
Prior historical form audit N01_REPORT_FORM_AMOUNT_COMPONENTS_QA_20261022.md found analogous division into sale price, selected options, additional amount and total actual. The 2026 effective form explicitly retains those categories. Avoid asserting every unrelated form field remained identical; only compared the monetary architecture.

## Critical API mapping is STILL UNVERIFIED
The government's SilvTrade HWP defines only `dealAmount = 거래금액(만원)`. Form ⑧ and ⑨ both contain monetary amounts. No published mapping found here proving whether dealAmount corresponds to ⑧ property price, ⑨ all-properties aggregate or another system-normalized measure; never assume one based on name alone. Agency written inquiry submitted 2026-10-21 remains pending.

## Additional follow-up questions for ministry
1. For endpoint `RTMSDataSvcSilvTrade/getRTMSDataSvcSilvTrade`, what RTMS filing table/field and Form 1 item (⑧ individual item price or ⑨ total actual, or another) maps to `dealAmount`? Specify codebook/effective dates.
2. For a single presale-right resale, which components of ⑧ (sale price, options, additional amount including ± premium) are reflected in `dealAmount`? Does API price represent VAT-inclusive number as stipulated in the filing form?
3. How does this mapping handle multiple jointly transferred objects, later amended contract prices, and historical versions of the report form? Is individual premium separately accessible to nonpersonal anonymized aggregate researchers?
4. Provide an official numerical illustrative filing-to-API mapping, and distinguish `ownershipGbn` blank from known presale status.

## Research disposition
Source collection 824 raw, 606 preliminary eligible, 21 notice reference candidates (19 unique, two building-line ambiguities), **0 validated monetary differences/premium**, unchanged. Historical N01 published descriptive sample of 980 is distinct. No public row-level transfer prices and no new DOI.
