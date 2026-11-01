# Round-number price reporting in Seoul apartment transactions (2025)

**ARHRN independent research 04 · exploratory computational dataset · version 0.3 · 2026-11-01**

## Study
This study compares the frequency of reported Seoul apartment sale prices that are exact multiples of KRW 10 million between brokerage and direct transactions, illustrating how buyer/seller composition can reverse the apparent association. All figures use one MOLIT contract-date CSV snapshot of 2025-01-01 to 2025-12-30 (filename dated 2026-10-30). **This is not official government transaction statistics, nor an estimate of causality.**

## Principal results
- Raw entries: **83,627**; entries without a cancellation flag: **77,212**.
- Brokered transactions (all seller/buyer types): **73,901**, **66.73%** rounded to KRW 10 million.
- Direct transactions (all seller/buyer types): **3,311**, **47.06%** rounded to KRW 10 million.
- Individual-to-individual brokered: **73,369**, **48,965** rounded (**66.74%**).
- Individual-to-individual direct: **1,845**, **1,367** rounded (**74.09%**).
- Thus the direction **reverses** after restricting to individual-to-individual sales. This is a descriptive comparison influenced by composition and selection.
- In 2025, 22 of 25 districts and all 12 calendar months exhibited a higher descriptive proportion of rounded reported prices for direct individual-to-individual trades.

## Source and transparency
- MOLIT real-estate transaction public data: https://rt.molit.go.kr/pt/xls/xls.do
- Source catalog: https://www.data.go.kr/data/3050988/fileData.do
- Raw CSV SHA-256: `2700ee4b1b86e01c8829bbc575a76f18a5a1ad49300a3663fc200e314b5f14a1`.
- The raw CSV is **not redistributed** here; access the provider's official download page. Reproductions require the same source snapshot, which may be revised by the provider.
- The research excludes 2025-12-31 and does not establish market-wide probabilities, representativeness, causal mechanisms, or negotiation behavior.
- Adjusted regression results were exploratory; transaction price appears as a covariate despite its mechanical relationship to round-number outcomes. Therefore regression odds ratios should **not** be treated as confirmatory evidence.
- The research hypothesis was not preregistered; multiple exploratory subgroup checks were not multiplicity-adjusted. Another time period/snapshot has not been independently replicated.

## Files
- `group_summary.csv`: four directly reproducible headline descriptive groups.
- `METADATA.json`: machine-readable dataset description and limitations.
- Further scripts, district/month tables and robustness materials are maintained in a verified local v3 release-candidate package. They are not claimed to be uploaded here until independently verified on GitHub.

## Citation and status
Suggested citation: *ARHRN Independent Research 04 (2026). Round-number price reporting and trade-composition reversal in Seoul apartment transactions, 2025. Exploratory derived dataset, GitHub.*

**DOI:** not assigned. **Zenodo:** pending account access. **Peer review:** none. This repository entry is a research-data release, not a refereed publication.
