# N01 transaction reporting form vs public dealAmount — 2026-10-22

## Primary legal/form evidence (version caution)
National Law Information Center original filed forms, historical amended editions:
- https://www.law.go.kr/LSW/flDownload.do?flNm=%5B%EB%B3%84%EC%A7%80+%EC%A0%9C1%ED%98%B8%EC%84%9C%EC%8B%9D%5D+%EB%B6%80%EB%8F%99%EC%82%B0%EA%B1%B0%EB%9E%98%EA%B3%84%EC%95%BD+%EC%8B%A0%EA%B3%A0%EC%84%9C&flSeq=31331759&gubun=
- https://www.law.go.kr/LSW/nwRvsLsInfoR.do?lsiSeq=197735

Instructions for reporting an initial supply or presale-right transfer contract provide separate entries for (1) supply price, (2) balcony expansion and option costs including installed air conditioning, (3) additional payments including premium (amount above or below supply price), and (4) overall actual transaction price. VAT included if applicable. Contract deposit/interim/final installment dates separately stated. These sources establish **reporting-form components**, not public API column mappings.

## Difference from public API
Locally inspected Ministry of Land SilvTrade API HWP describes `dealAmount` only as `거래금액(만원)`. Its field specification **does not state** whether it is mapped to form's `총 실제 거래가격`, `물건별 거래가격`, `추가지불액`, or another normalized value. It does not expose component fields analogous to individual form's option costs or premium. Do not infer a one-to-one mapping based on common-sounding labels.

The Busan municipal published formula for broker compensation uses [payments made until transfer + premium] times brokerage rate; it is **not** evidence of the governmental trade-reporting API price mapping: https://www.busan.go.kr/depart/ahestateprice01 .

## Documentation and version limits
The national form references retrieved include historical revisions around 2017, not proven the exact effective 2026-10-22 statutory annex wording. Before claiming the current legally operative entry method, compare the latest 2026 law.go.kr 시행규칙 별지 제1호서식 revision. Independently verify with ministry data owner which form box is serialized into API `dealAmount`.

## Research decision
A source with a clear section titled `추가지불액(프리미엄 등)` makes a more narrowly defined *component-level* research question possible IF individually reportable components can be obtained in authorized, privacy-safe form. Current anonymous public API lacks those fields. The 21 previously identified notice reference candidates (19 unique type/floor source tiers, 2 building-line ambiguous), total 824 raw/606 preliminary eligible, zero finalized reported-price differences remain unchanged. No individual premium calculation, net profit claim, new DOI, or public transaction-level leak.

## Follow-up: refine ministry written inquiry
Ask explicitly: (1) Does SilvTrade getRTMSDataSvcSilvTrade `dealAmount` map to the statutory 신고서 `총 실제 거래가격` or `물건별 거래가격`, or something else? (2) For 분양권 전매, are supply-price, options and premium included? (3) Are buyer-borne loans / prior instalments relevant to serialization or only payments, and are supply amendments reflected? (4) Is there a nonpersonal aggregate API/codebook or component access for premium rather than deriving it from single figure? (5) State reference schema/effective dates and offer anonymized numeric example.
