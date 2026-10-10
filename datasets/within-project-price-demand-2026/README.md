# Within-project apartment unit-price and first-priority applicant-to-supply ratio, South Korea (2026)

AptToSell independent observational analysis, validated 2026-10-09. Article: https://apttosell.com/apartment-type-price-subscription-demand-2026/

## Research question
Within a housing project, for unit types with similar exclusive floor areas, is the unit type with the higher advertised maximum price per square metre more likely to show a higher first-priority application-to-supply ratio?

## Cohort and results
- 140 projects; 898 officially reconciled housing types; 3,678 rank/region API response rows.
- 205 project-by-rounded-area comparison groups: 145 higher-priced type higher ratio, 56 lower-priced type higher ratio, 4 ties.
- Among 201 non-tied groups, higher-priced type has the higher ratio in 72.14%.
- Cluster bootstrap by project (5,000 replications): conditional 95% interval approximately 64.9%–78.9% (not nationally representative).
- Official max asking price, competition API supply count, first-priority regional applicant sum and derived applicant/supply ratio reconciled for 898/898 housing types.

## Important interpretation
The ratio is **sum of regional applicants with SUBSCRPT_RANK_CODE=1 divided by SUPLY_HSHLDCO from the competition API**. It must not be misrepresented as ApplyHome's displayed local/regional competition rate, which may reflect allocation and closing rules. The general-supply count from the model API is a different field. This is descriptive association, NOT evidence that raising a price increases demand. The sample is not a probability sample of all presales.

## Data and reproducibility
- [205 project-area pair records (CSV)](./comparison_205_pairs.csv)
- [898 officially reconciled housing type records (CSV)](./reconciliation_898_types.csv)
- [Results summary](./summary.csv)
- [Data dictionary and limitations](./CODEBOOK.md)
- [Source and verification method](./METHODOLOGY.md)

The 205-pair and 898-type **derived reconciled tables are available above**. Their CSV row counts were verified against the local release (205 and 898 respectively). Full raw API JSON payloads are not hosted here; users can query the official Korea Real Estate Board APIs with their own key. No DOI is assigned to this research folder at this time. The public data portal identifies both source APIs as having unrestricted re-use permission; the original government/provider data provenance remains attributed.

## Provenance
Source APIs: https://www.data.go.kr/data/15098547/openapi.do and https://www.data.go.kr/data/15098905/openapi.do ; retrieval/verification 2026-10-09. Cite both the underlying official Korea Real Estate Board source and AptToSell's derived research. Derived original methodology and text: © 2026 AptToSell; licence for full data release is to be confirmed before redistribution.
