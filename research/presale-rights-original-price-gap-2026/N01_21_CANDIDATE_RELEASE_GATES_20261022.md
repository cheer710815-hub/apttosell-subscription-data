# N01 — 21 source-price reference candidates: release gates and agency response decision matrix
Date: 2026-10-22. This is a QA protocol, **not** a new statistical result or DOI.

## Cohort accounting
New live collection **824 raw, 606 preliminary eligible**; historical published N01 aggregate **980 distinct from this unreconciled collection**. In 5 separate projects, 21 already screened candidate rows have original notice reference prices identified: 19 uniquely within original type/floor schedules, two Namulsan candidates remain building-line ambiguous. Breakdown: Gagyeong IPARK 6 6/6 unique, Namulsan Norway Forest 3/5 unique, Doosan Zenith Cheongju 4/4 unique, Artera A8 3/3 unique, Asan C2 3/3 unique. These 21 are not extra rows to add to 606. Exclude Down2 20 from price-join subtotal because official B-2 parcel inclusion for 301-1 unresolved (19 areas matched, one nonmatched).

## Gate matrix (PASS / FAIL / UNKNOWN)
| Gate | Rule | Current |
|---|---|---|
| Transaction screen | brokered individual-to-individual, not canceled, not occupancy right | Preliminary PASS for all 21; confirm any revised live data |
| Project location | original offer project + original lot/block same | Gagyeong6, Namulsan, Doosan, Artera A8 supported; Asan BL-C2 still needs authoritative block provenance |
| Original offering document | approved number/source preserved, identifiable notice version | Gagyeong6 approved-number PDF (2023-11-23) SHA256 d4377061d8b2bb43d2caa25e370b2375e920ebdff49ef583c77ffac1e199bffe PASS; others source notice accessible but master binary hash/version coverage incomplete |
| Exact area subtype | distinguish physical subtype, not grouped marketing A/B labels | Matched for 21 on reviewed original notice schedules, subject to project location gate |
| Floor AND building line | a unique original notice base price applicable to reported floor | Unique 19, ambiguous 2 (Namulsan 59A 19F, 74A 9F) |
| Later revision | correction/addenda & applicable sale terms not missed | UNKNOWN, not proof of absence just because web search found none |
| API dealAmount mapping | authoritative documentation links API field to report form total price and specifies included components | UNKNOWN; agency query submitted, awaiting answer |
| Individual original contract | original assigned unit, option selections and subsequent price/terms amendments where needed | UNKNOWN for all 21 |
| Revised/canceled source | refresh as-of extraction date, retain snapshots and exclude cancellations | Not yet repeated for 2026-10 partial month |

## Deterministic response handling
**If official agency confirms dealAmount is the 신고서 총 실제 거래가격:**
- Record source date, exact authority quote/link, and schema version.
- Do not call (dealAmount - published original supply price) a *premium*: options, supply contract modifications, tax and interim interest may affect meaning.
- A carefully labeled *unadjusted nominal difference against original notice base supply price* may be evaluated only where project, unique floor price, reporting component inclusion, applicable notice amendments, and row lineage are defensible, with explicit exclusions/caveats. Do not claim profit.
- For premium isolating, require transaction-specific separated premium/option components or a directly applicable official rule explicitly validating inference and no unexplained components.

**If official agency confirms dealAmount is rights-only consideration or previously-paid amounts rather than total:** prohibit difference calculation against original total base price; redesign research around compatible measures.

**If the answer says values vary, have exceptions, or is ambiguous:** retain AMOUNT_COMPONENTS_UNVERIFIED, request concrete examples of report form-to-API mapping and schema documentation.

**If no agency response yet:** continue source inventory, notice-version QA, and geographic data collection/reconciliation only. No price-gap/premium publication.

## Acceptance and next order
1. Preserve agency response PDF/email with date and cite precise decision statement once received, without exposing personal details.
2. Prioritize independently archiving and hashing A8 2024 initial full notice and Doosan 2025 official price PDF; then correct notices.
3. For Namulsan, obtain authoritative building and line to resolve 2 ambiguous cases or permanently exclude them from point-price claims.
4. For Asan C2, verify BL-C2 identification independently; preserve 2 separate 84D month rows; do not deduplicate by identical area/floor.
5. Maintain 0 FINAL_FINANCIAL_COMPARISONS until all necessary gates pass. New DOI forbidden for repackaging N01.

## Traceability
Consolidated original table: N01_CONSOLIDATED_PRICE_REFERENCE_QA_20261022.md (2026-10-22); agency amount query details: TRANSACTION_AMOUNT_COMPARABILITY_QA_20261020.md.
