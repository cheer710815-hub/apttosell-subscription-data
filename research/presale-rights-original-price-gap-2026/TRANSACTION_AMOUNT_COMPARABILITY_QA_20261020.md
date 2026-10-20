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
