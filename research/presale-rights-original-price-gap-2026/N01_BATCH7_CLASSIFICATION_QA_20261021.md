# N01 batch 7 — verified collection and preliminary screening (2026-10-21)

## Inputs, provenance, and audit
Private user-uploaded archive `N01_7th_107records.zip` contains six raw CSVs and six JSON manifests for 31710, 36110, and 43113, contract months 202609/202610. All six CSV SHA-256 checks matched manifest `sha256`; saved records matched `records` and `expected_total`. The zero-result region-month pairs 41590/29170 were user-verified separately as 0/0 with valid hashes; those source files were not included in the uploaded archive.

## Screening rules
A row passes this **preliminary** screen only when `dealingGbn == 중개거래`, `slerGbn == 개인`, `buyerGbn == 개인`, `ownershipGbn != 입`, and `cdealType != O`. Empty `ownershipGbn` is *not* treated as an affirmative proof of presale-right classification. Overlapping exclusion reason categories are not added as disjoint counts. We do not deduplicate similar source transactions in the absence of stable government report identifiers.

| Code | Month | Raw | Preliminary eligible |
|---|---|---:|---:|
| 31710 | 202609 | 39 | 19 |
| 31710 | 202610 | 24 | 9 |
| 36110 | 202609 | 2 | 1 |
| 36110 | 202610 | 1 | 1 |
| 43113 | 202609 | 33 | 17 |
| 43113 | 202610 | 8 | 2 |
| **Total** | | **107** | **49** |

Exclusion (overlapping reason counts): nonbrokered/direct 48; occupancy-right 9; canceled `cdealType=O` 4; nonindividual buyer/seller 1. Union excluded 58. Exact equality of all CSV columns within archive: 0 identical rows; not a unique-government-filing check.

Accumulated new live API sample: earlier verified raw 717 and preliminary candidates 557, plus this batch raw 107 and preliminary candidates 49 = **raw 824, preliminary 606**. This is **not** the previously published N01 descriptive aggregate sample of 980 brokered individual transactions. Source dates remain partial, especially October 2026. N01 `dealAmount` amount-components official clarification is awaiting agency response. No original-price joins, premiums, net gains, or new DOI are asserted. Raw per-transaction contents remain private.
