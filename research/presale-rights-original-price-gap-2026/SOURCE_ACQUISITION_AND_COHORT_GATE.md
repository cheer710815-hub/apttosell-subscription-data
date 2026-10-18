# N01 original offering-price linkage — source acquisition and cohort gate

Updated: 2026-10-18. Research state: **NOT READY FOR PRICE-GAP PUBLICATION**.

## Candidate-count reconciliation

| Set | Reported count | Audit status |
| --- | ---: | --- |
| Original resale transactions cleaned | 1,436 | Historical project handoff, raw row-level file not located in connected Drive/repository during this check |
| Person-to-person broker-mediated transactions | 980 | Published **aggregate** N01 v2.0, DOI https://doi.org/10.5281/zenodo.23432291 |
| Initial-offering project linkage candidates | 115 | Historical handoff only; row-level candidate linkage CSV not located |
| Jinju pilot candidate transactions | 56 | Historical handoff only; 56 row-level provenance records not located |
| Exact verified resale-to-original-price joins | **0 confirmed** | No official original/amended price PDF and no row-by-row linkage verified |

**Crucial distinction:** The 980-observation Zenodo release consists of aggregate tables and is NOT the missing 115-row candidate join table. Do not reconstruct individual transactions from aggregated data or confuse 115 candidates with 115 validated matches.

## Current source discovery (2026-10-18)

- Official regional SME office published a 2026-07-13 institutional referral notice with proposed offering announcement 2026-08-14; this confirms marketing/administrative context **not floor-specific prices**: https://www.mss.go.kr/site/gyeongnam/ex/bbs/View.do?bcIdx=1069781&cbIdx=255
- Its 2026-08-19 referral-results notice explicitly directs readers to ApplyHome for the actual offering announcement: https://www.mss.go.kr/site/gyeongnam/ex/bbs/View.do?bcIdx=1070553&cbIdx=255
- Third-party offering record identifies project **2026000383**, 2026-08-14 announcement and six types but is not an authoritative PDF: https://www.aptdamoa.com/sale-info/apt/2026000383/contents.html
- **Official initial and revised price schedule PDFs:** not recovered from source in this pass.
- **115 linked candidate rows:** not located in the connected Google Drive document search or GitHub content search in this pass. Searches returning no matches do not prove files never existed in other local or private storage.

## Next go/no-go decision

1. Recover candidate-level export with transaction year/month, region, project, exclusive area, announcement identifier, source trace and cancellation/party/broker flags. No personal identifiers in public repo.
2. Identify candidate projects with accessible **official** original and amended offering notices. Compare official prices by exact housing type, floor band and effective notice version.
3. Retrieve transaction definitions and verify whether each transaction's reported amount can be compared to the offering price on the same basis. If not, classify as **NONCOMPARABLE_AMOUNT**.
4. Preserve classifications: `OFFICIAL_PRICE_VERIFIED`, `AMBIGUOUS_TYPE_OR_FLOOR`, `CORRECTION_NOT_VERIFIED`, `NONCOMPARABLE_AMOUNT`, `UNAVAILABLE_SOURCE`.
5. Publish a gap estimate only for exact verified matched rows with clearly stated denominator, coverage and selection bias; never label a gross price difference seller profit.

**Operational hold:** Do not assign a new DOI, announce premiums or mark any of 56 or 115 rows as validated until these evidence gates pass.
