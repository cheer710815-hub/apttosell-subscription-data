# Independent Study 04 — Public release eligibility audit (2026-11-03)

Status: **HOLD detailed strata and final license; DOI not issued**.

## Reinspected internal archives
Four original internal ZIP packages (v3 release gate, 2025 v0.3 matched, 2026 external validation, v0.7 sensitivity), totaling 28 members, passed archive CRC. Exact per-member SHA-256 is kept in the private release-gate package.

## Disclosure risk newly quantified
2025 v0.3 `v03_complex_area10_matches.csv` contains 230 complex × 10㎡ records, including **176 strata with exactly 2 direct transactions** and **225 strata where at least one trade mode has fewer than 5**. The table includes geographical and named-complex keys. Do **not** upload this detail table or the raw MOLIT CSV automatically to GitHub/Zenodo. Even suppressing small cells may not stop difference attacks using marginals.

## Distinguish publication levels
- Original-source reproducibility: verified previously for 2025 & 2026 source snapshots.
- Safe public data package: **not complete**. Candidate is high-level aggregate results, methodology and independently reviewed portable scripts.
- Independent 2024 holdout: **not complete**.
- Investigators' licensing of derived code/results: **not finalized**.
- Zenodo deposit / DOI: **not done** due account access restriction and pending final release approval.

## Official provenance
MOLIT real-transaction file data catalog: https://www.data.go.kr/data/3050988/fileData.do (listing states no restrictions for source use).
REB distinguishes contract-date MOLIT disclosure from its official report-date transaction-count statistics: https://www.reb.or.kr/r-one/portal/stat/easyStatPage/A_2024_00900.do.

This is an internal publication-gate status record, not a published research dataset. Details: `Study04_Public_Release_Gate_20261103.zip` generated internally (report, manifest, status JSON; excludes raw CSV and complex-level tables).
