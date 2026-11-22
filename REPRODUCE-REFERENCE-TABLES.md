# Reproducing the 2026 reference-table checks

This guide covers the two *reference tables* in this repository, not the separate N09, N01-AGG or event-registry research releases.

## Inputs

- [housing_subscription_score_2026.csv](housing_subscription_score_2026.csv): 41 category/condition rows, grouped into homelessness duration, dependents and subscription-account duration.
- [private_housing_deposit_2026.csv](private_housing_deposit_2026.csv): four area bands, three regional deposit columns; units are KRW 10,000.
- [datapackage.json](datapackage.json): repository-level resource metadata (not an immutable research release).

## Reproduction without dependencies

1. Download the repository ZIP from GitHub and extract it.
2. Open the two CSV files in a spreadsheet or a UTF-8 text editor.
3. Group the score table by `category`. Check that the maximum `score` for `homeless_period` is **32**, `dependents` is **35**, and `subscription_account_period` is **17**. Their sum is **84**. Count the score rows: **41**.
4. Count deposit rows: **4**. Confirm the `unit` field is `KRW_10k` in every row. Read the `source_basis` and `checked_date` fields before interpreting the figures.
5. Compare both filenames against the `resources[].path` entries in `datapackage.json`.

The checks above are *structural reproducibility checks*. They do not establish that a rule remains legally current, that a specific applicant is eligible, or that a housing project's notice follows these general tables. For live applications, consult the relevant official recruitment notice and current law.

## Provenance and citation

- Canonical reference page: https://apttosell.com/cheongyak-score-data/
- Data-center index: https://apttosell.com/housing-subscription-data/
- Archived reference dataset: https://doi.org/10.5281/zenodo.22842058
- Cite the specific version actually used, including access date when referencing the evolving GitHub repository. Other DOI records listed in the repository refer to distinct datasets and should not be cited as if they describe these tables.

## Limitations

The repository may evolve after this guide is written. GitHub blob hashes, row counts, and check dates should be verified anew for later revisions. A structural PASS is not a legal or policy certification.

## Verified widget/CSV regression — 2026-11-22

The educational score widget is pinned in the AptToSell data-center embed to commit
`6330f9ef5acf85ef6510def8758ead38cdfcea65`. The reference CSV release remains
dated **2026-09-18**. The following validation is about the published example scores
and is **not** a change to that reference release:

- CSV: `housing_subscription_score_2026.csv` (41 rows).
- Widget: `widgets/apttosell-score-widget.js` (17 homelessness-duration, 7 dependent,
  17 account-duration, and 4 spouse-score options).
- Regression coverage: all **8,092** combinations, including a 17-point account cap
  and an 84-point total maximum.
- GitHub Actions workflow: [Validate reference CSV structure](.github/workflows/validate-reference-csv.yml).
- Verified successful GitHub Actions run **#3**, 2026-11-22, for commit
  [`370119ca9a9e658a5321be6d07abb8180dee5975`](https://github.com/cheer710815-hub/apttosell-subscription-data/commit/370119ca9a9e658a5321be6d07abb8180dee5975).
- GitHub Actions may be rerun for later revisions; any future changes need new
  recorded commit and result.

**Scope limit:** structural and arithmetic consistency, not legal currentness,
individual eligibility, or review of each site's copy of the embed. Existing DOI
deposits are unchanged, and this verification does not imply a new research release.
