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
