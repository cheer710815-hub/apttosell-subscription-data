# Independent Study 04 — Out-of-period validation protocol (v1, 2026-11-02)

**Status: protocol only; NO new data evaluated, no replication claim.**
**Scope:** Seoul apartment sales; round-number concentration in reported transaction prices, by transaction mode.
**Prerequisite:** Obtain and independently inspect the v3 package before executing any comparison. The original cohort, data extract date, inclusion rules and code must be fixed from the actual files, not reconstructed from remembered summaries.

## Research question
Does the brokered-versus-direct difference in price-ending concentration persist in an independent, non-overlapping contract period, and after standardizing composition?

## Data source and warnings
- MOLIT real transaction public CSV: https://rt.molit.go.kr/pt/xls/xls.do?mobileAt=
- Official portal: https://www.data.go.kr/data/3050988/fileData.do
- Download criteria: **Apartment / Sale / Seoul / contract-date interval**; record exact dates, retrieval timestamp, filename, SHA-256, source and column dictionary.
- MOLIT notes that contract-date disclosure can change because of delayed reports, revisions and cancellations. Do not portray this exploratory contract-date extract as the authority's official report-date statistics.
- Explicitly confirm the column that distinguishes brokerage/direct sale, and separately the columns describing buyer and seller composition (if present). Do not equate brokerage classification with buyer/seller composition.
- Preserve original raw files internally; release derived aggregates only after redistribution, disclosure and licensing checks.

## Holdout period decision
- Primary proposed holdout: **2024-01-01 through 2024-12-31**, IF the inspected v3 discovery cohort indeed covers only 2025 contracts and 2024 was not used in specification selection.
- If prior pilot or specification tuning used 2024, choose a truly unexamined period, record the reason, and revise this protocol *before viewing outcome statistics*.
- Extraction date must be fixed because later revisions may alter disclosed records.
- Predeclare a second sensitivity snapshot or a stable reporting lag; do not quietly combine different snapshots.

## Processing rules to freeze against v3
1. Retain Seoul apartment sales with valid contract date and strictly positive disclosed sale price; exclude records marked cancelled using the actual published field semantics.
2. Record counts before/after each filter, missingness, cancellation exclusions, duplicates and ambiguous transaction modes.
3. Convert reported price to integer KRW **only after validating original CSV units**. For values expressed in KRW 10,000, flag a round number if amount_in_10k_won % 1000 == 0.
4. Primary metric: round-number proportion for every mode with numerator and denominator.
5. Unadjusted contrast: direct minus brokerage in **percentage points**.
6. For adjusted results, reproduce exactly the v0.3 complex × 10㎡ area-band strata definitions, eligibility conditions, stratum weights, and cluster-resampling unit. The v0.3 report specifies a minimum of 2 trades per mode within each stratum and complex-level cluster bootstrap; FLOOR was NOT part of the reported +16.98pp estimate. Do not choose new rules to maximize agreement with 2025.
7. Recompute confidence intervals using v3 seeds and resampling specification if available; otherwise label results a distinct revised method.
8. Separate analyses for buyer/seller composition if the original columns support it; never infer parties' identity from transaction mode.

## Quality and robustness gates
- Raw archive checksum and schema/data-type audit pass.
- Exact eligible cohort and exclusions documented; no implicit silent column coercion.
- Independently executed script reproduces primary raw cohort metrics and adjustment tables from the same snapshot.
- Report thin-stratum exclusions and their coverage.
- Cluster bootstrap (by the cluster actually used in v3), plus sensitivity to minimum stratum count and price scale.
- Disclose sampling uncertainty, multiple-testing concerns, composition and report-revision effects.
- Report **negative/null findings** as prominently as positive ones.

## Proposed output files
- `2024_holdout_source_manifest.json`: source URLs, capture timestamp, original filename, SHA-256, selection settings.
- `2024_holdout_column_map.json`: mapping of raw fields to harmonized fields with unit and code labels.
- `2024_holdout_filter_audit.csv`: sequential filter counts/exclusion reasons.
- `2024_holdout_unadjusted.csv`: count, round-count, rate for each transaction mode.
- `2024_holdout_matched.csv`: eligible strata, weights, effect and uncertainty (only if v3 matching logic validated).
- `2024_holdout_independent_verification.md`: methodology, source snapshot, comparison and limitations.

## Release decision
HOLD until (a) final v3 file inspection, (b) holdout dataset retrieval, (c) independent execution, and (d) external publication permission checks. Zenodo deposit and DOI creation remain blocked while account access is restricted and until explicit release approval.


## Source-method correction (2026-11-03)
A previously retained summary incorrectly described the +16.98 percentage-point comparison as controlling for floor. The recovered `V03_REPORT.md` explicitly defines **complex × 10㎡ area interval**, with at least two transactions of each type in the same stratum, 230 eligible strata (566 direct and 5,557 brokered observations) and cluster bootstrap grouped into 213 complexes (5,000 replicates, seed 20261101).

The v0.3 report further distinguishes:
- Excluding public-institution buyers: 74,044 brokered (66.7360%) and 2,231 direct (65.9794%); difference **−0.7566pp**.
- Personal buyer **and** personal seller only: 73,513 brokered (66.7406%) and 1,849 direct (74.0941%); difference **+7.3535pp**.
- The +16.98pp comparison is a **matched-stratum descriptive contrast**, not a floor-controlled causal estimate.
- The 2024 intake audit currently computes an **unadjusted** difference for all non-cancelled known transaction modes. It is not a reproduction of the v0.3 buyer/seller restriction and must not be compared numerically with the personal-to-personal +7.3535pp without matching that filter.
