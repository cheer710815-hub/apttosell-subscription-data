# N01 — Sale-right transfer transaction amount comparability gate (2026-10-20)

## Authoritative reporting framework

The reporting form and its instructions under the Enforcement Rule of the Act on Report on Real Estate Transactions distinguish, for initial supply or presale-right transfer contracts, original supply price, balcony expansion / selected option costs, additional payments (including positive or negative premium), and the reported total actual transaction price. Official legal-form reference: https://law.go.kr/flDownload.do?bylClsCd=110202&flSeq=113467037&gubun= .

This is evidence of the **reporting components**. It does NOT independently establish the precise mapping or field-level inclusion/exclusion policy for the MOLIT SilvTrade API's single `dealAmount` item across all records. The SilvTrade official API guide only labels `dealAmount` as transaction amount (unit: 10,000 KRW); it does not expose option-price or premium component fields.

## Project-specific test: Asan Tangjeong Prugio River Park C2 block

Preliminary linkage candidates: 3, among 5 BL-C2 lot-labelled source rows. By the developer's 2023-10-25 original published price table (not yet amended-verified), 74B on 2nd floor has KRW 348,000,000 offering price (1 candidate) and 84D on 8th floor has KRW 429,000,000 offering price (2 candidates). Developer PDF: https://www.prugio.com/ht/2023/tangjeong_c2/final/sub/announcement2.pdf .

**No conclusion of net premium or gross price gap is authorized** because the three actual reported resale prices may include option items, the effective corrected notice and lot/phase identity remain to be verified, and transfer-price component reconciliation is incomplete.

## Decision codes and gate

- `AMOUNT_COMPONENTS_UNVERIFIED`: default for candidate links without itemized reporting evidence or an official API explanation identifying exactly what `dealAmount` aggregates.
- `NOTICE_VERSION_UNVERIFIED`: original notice exists but corrections and application to transaction have not been established.
- `PROJECT_ID_UNVERIFIED`: raw BL-C2/lot aliases have not been corroborated for the individual reported filing.
- `PROVISIONAL_TYPE_FLOOR_REFERENCE`: floor/type associated with initial schedule, not an actual verified resale-to-offering-price comparison.
- `PRICE_GAP_PUBLISHABLE`: forbidden until each relevant gate passes; any price difference then must be labeled by exactly comparable terms and expressly not equated with seller net profit.

Privacy: keep transaction-level resale amounts and rows in private working data, not GitHub. No new DOI, no revision of historic N01 aggregate DOI. N01 internal collected 717 source rows and 557 preliminary candidates unchanged.

## 2026-10-20 follow-up: explicit 2026 reporting form and fee-base distinction

The official 2026-02-06-revised Real Estate Transaction Report form (Annex Form 1) has separate boxes for **supply price**, **balcony expansion/other options**, **additional payment**, and **total actual transaction price**. Primary official government form: https://law.go.kr/lbook/lbFileDownload.do?flExt=pdf&lbookConflSeq=85167&lbookSeq=91616 . A government's older form instructions explicitly describe positive/negative premium as part of additional payments: https://www.yeonggwang.kr/widget/get_download?name=%EB%B6%80%EB%8F%99%EC%82%B0%EA%B1%B0%EB%9E%98%EA%B3%84%EC%95%BD+%EC%8B%A0%EA%B3%A0%EC%84%9C.pdf&real_file=%2Fdata%2Fweb%2Fsample14.pdf .

**Do not confuse the brokerage commission calculation base** (paid-to-date including loans plus premium) with the transaction price published in SilvTrade. The municipal brokerage guidance at https://www.busan.go.kr/depart/ahestateprice01 describes a commission fee basis, not the API `dealAmount` mapping. The official SilvTrade API guide labels `dealAmount` as amount (10,000 KRW), without disaggregating form boxes. Hence neither the reported total nor the commission base can be substituted for option-adjusted premium.

**Precise gate**: Require a primary government data dictionary or competent-agency explanation of which report-form field populates `dealAmount`. If it is the *total actual transaction price*, the difference from original supply price may include option/additional-payment components. Do not label the difference premium or seller gain. Itemized matched reports would still be needed to isolate the premium. With no such evidence, preserve `AMOUNT_COMPONENTS_UNVERIFIED` and forbid numerical gap claims for the three C2 candidates.
