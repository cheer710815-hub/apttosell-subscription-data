# Reconciliation and analysis methodology (2026-10-09)

1. Reconcile 140 official housing-project notices and 898 housing type records using `HOUSE_MANAGE_NO` and trimmed `HOUSE_TY`.
2. Cross-check 898 unit-type maximum advertised prices against official model API `LTTOT_TOP_AMOUNT`.
3. Cross-check 898 competition API supply denominators `SUPLY_HSHLDCO` and summed first-priority (`SUBSCRPT_RANK_CODE=1`) regional applications (`REQ_CNT`).
4. Group unit types within the same project by rounded exclusive area and compare types at either end of maximum advertised price per actual area.
5. For each of 205 eligible groups compare first-priority applicant-to-supply ratios. 145 favor the higher-priced type, 56 the lower-priced, 4 tie. Percentage 145/(145+56)=72.14%.
6. Resample by project, rather than by pair, for 5,000 cluster-bootstrap repetitions: descriptive conditional interval approx. 64.9%–78.9%.

These descriptive figures should **not** be called official ApplyHome region-specific first-priority competition rates, a nationwide estimate, an investment recommendation or a causal price effect.

Original data sources (Korea Real Estate Board): https://www.data.go.kr/data/15098547/openapi.do and https://www.data.go.kr/data/15098905/openapi.do. Source retrieval date: 2026-10-09. The public folder includes derived study-specific CSVs (`comparison_205_pairs.csv` and `reconciliation_898_types.csv`), a results summary, and methodology. Full raw API JSON responses are not included. Reproduction of the source-data extraction therefore requires querying the cited official APIs with appropriate access; the available derived tables support independent review of the published comparisons.
