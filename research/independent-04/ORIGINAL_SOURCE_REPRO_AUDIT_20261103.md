# Study 04 — Original-source reproducibility audit (2026-11-03)

**Status:** Original 2025 v0.3 and 2026 disclosed-snapshot summary re-execution PASS. 2024 holdout incomplete. No DOI registration and no scholarly-publication claim.

## Newly located archived inputs
- `ARHRN_Independent_04_Release_Gate_v3.zip` (administrative release gate)
- `ARHRN_PRICE_HEAPING_SEOUL_2025_MATCHED_V03_20261101.zip` (v0.3 code, match table, bootstrap and subgroup statistics)
- `아파트(매매)_실거래가_20261031113607.csv` (2025 Seoul source; SHA-256 `a0d3df04e403f8dc2c2b49b512e763850f050dd65502854b2961efbf41a8372c`)
- `ARHRN_PRICE_HEAPING_SEOUL_2026_EXTERNAL_VALIDATION_20261102.zip` (original 2026 comparison code and summaries)
- `아파트(매매)_실거래가_20261102095954(1).csv` (2026 Seoul source; SHA-256 `6d863e491a54598ff1a3337d569d42075928bbb28f4131c0716f72db92567c32`)

## Re-execution verification
- 2025 original `v03_analysis.py` and `v03_bootstrap.py` executed on archived original CSV; both exit code 0.
- Reproduced `v03_complex_area10_matches.csv`, `v03_cluster_bootstrap.json`, and `v03_subset_sensitivity.json` match archived files **byte-for-byte**.
- Reproduced cohort 76,275 trades; 230 complex × 10-sqm-area strata (at least two observations per trade mode); 566 direct and 5,557 brokered matched transactions. Trade-count-weighted difference +16.983941705548336 percentage points; 213 clusters; 5,000 cluster bootstrap draws (seed 20261101); confidence interval [12.535242791574458, 21.280119863247197] pp.
- 2026 source SHA-256 matches the archived original audit. Its original `validate_external_year.py` re-executed on source with exit code 0, yielding **12 of 12** identical comparison rows.
- 2026, grid KRW 10 million: excluding public buyers, direct 57.692308% (n=1794), broker 66.865378% (n=51834), direct minus broker **-9.173070 pp**. Personal buyer and seller only: direct 75.330739% (n=1285), broker 66.876432% (n=51486), difference **+8.454307 pp**.

## Scope and limitations
- The 2026 CSV covers contracts **2026-01-01 to 2026-11-02** only, not the whole year. It cannot support equal-duration full-year comparison with 2025.
- The +16.98 pp 2025 estimate matches complex and **10㎡ area bins**, not floor; 2026 summary percentages are **unadjusted** and should not be equated with that 2025 matched estimator.
- Raw disclosures can be corrected or cancelled later; conclusions pertain only to each recorded snapshot. This does not establish causality, manipulation, or representativeness.
- Independent 2024 holdout and public release license/privacy checks remain unfinished; raw CSV is not redistributed.
- Zenodo deposit remains blocked pending account restoration and final authorization.

**Audit artifact locally generated:** `Study04_Original_Source_Reproducibility_20261103.zip` (report, regenerated summaries, original reproduction scripts and hashes, without raw CSV).
