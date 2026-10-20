# N01 project matching gate — 2026-10-20

This is a methodological supplement to RESEARCH-PROTOCOL.md, not a new dataset or publication.

## Mandatory source fields

Keep source values unchanged: request_region, request_month, sggCd, umdNm, jibun, aptNm, excluUseAr, floor, dealYear, dealMonth, dealDay, dealAmount, ownershipGbn, cdealType, dealingGbn, slerGbn, buyerGbn.

## Matching decision sequence

1. Exclude explicitly identified occupancy rights, cancelled trades, non-brokered trades and trades where either party is not private, with an auditable reason per row. If a required value is missing or ambiguous, do not silently promote it to an exact match.
2. Build a search key with whitespace and punctuation normalization **without overwriting aptNm**.
3. Compare the original name and normalized candidate against the geographic identity (sggCd, umdNm), original project identifier, cadastral lot (jibun), and independently corroborated project phase/block. Reject any contradictory block/phase.
4. An official notice identifier and contemporaneous original or corrected supply schedule are mandatory for offering-price comparisons. The notice version must be effective and relevant to the resale date.
5. For an exact type-level match, verify exclusive area **and** the A/B/C type discriminator and floor or unit-based price schedule. If the trade API lacks the discriminator, report a price interval only where the official source warrants it, otherwise mark AMBIGUOUS_TYPE_OR_FLOOR.
6. Never infer premium, gain or profit directly from a reported resale amount minus an offering-price field without verifying the transaction amount definition and inclusions.
7. No public row-level export, DOI, or research conclusion until all above gates pass.

## Name-alias review gates

| Alias family | Issue | Working decision |
| --- | --- | --- |
| Daejeon Yuseong Doan Umi Lynn Tree Shade | Source lot references differ | NAME_ALIAS_ONLY, hold project-ID merge |
| Asan Tangjeong Prugio River Park | Source lot vs block identifier differs; neighboring Center Park also exists | NAME_ALIAS_ONLY, hold project-ID merge |
| Gimhae The Sharp Sinmun Greenity | Numbered phase 2 is separately represented | PHASE_UNRESOLVED, no automatic merging |

These labels are search aids only. Preserve original text and lot for audit.

## Current validation scope

Source observations: 717; preliminary eligibility candidates: 557. These are not necessarily unique source filing IDs, validated exact-price joins, or a reproduced version of the historical national 980-row cohort. All joins to initial advertised unit/floor prices remain blocked pending official source and exact unit-type verification.
