# DDFS v1.0 — model reproduction (added 2026-11-05)

This folder contains the **existing, frozen 2026 national DDFS 184-type dataset** and its original published results. The reproduction files below support independent verification of **two already published models**, not a new research study or DOI.

## Files added

- `reproduce_ddfs_logit_v1.py`: Python command-line script that fits the primary structure and financing logistic models.
- `requirements-reproduction.txt`: versions used in the local verification.

## Run

Using Python 3.13, in this directory:

```bash
python -m pip install -r requirements-reproduction.txt
python reproduce_ddfs_logit_v1.py --input apttosell-ddfs-national-type-riskset-2026-v1.0.csv --output ddfs_reproduction_results.json
```

The script reads the **publicly released 31-column CSV**, validates 184 unique housing types from 52 projects, requires 78 positive outcomes, fits each model, prints model estimates, and writes its input SHA-256 and library versions into JSON. It exits with an error if a published coefficient differs beyond its stated rounding tolerance. The generated JSON is a *local output* and is **not committed** as a new version of the research dataset.

## Statistical specification

`reappeared_first_followup` is a 0/1 outcome for the identical type's appearance in the project's **first follow-up supply**. This is not a contract-cancellation rate.

- PRIMARY_STRUCTURE: `log2(rate)`, `log2(type_supply_share_pct)`, `log2(project_general_supply)`, `log2(initial_type_price_krw)`, `regulated_flag`, and `capital_region_flag`.
- FINANCING: `log2(rate)`, `log2(type_supply_share_pct)`, `log2(project_general_supply)`, `log2(equity_floor_proxy_krw)`, and `capital_region_flag`.
- GLM, binomial family, logit link, with **cluster-robust standard errors grouped by `HOUSE_MANAGE_NO`** and statsmodels `use_correction=True` (finite-sample correction).
- Odds ratios for log2 predictors represent doubling of that variable; binary predictor odds ratios compare the two categories. Confidence intervals are Wald 95% intervals.

## Local verification record and scope

Using an **archived 184-row, 32-column version of the same research risk set**, the script's statistical specification was independently executed with Python 3.13.5, pandas 2.2.3, NumPy 2.3.5, SciPy 1.17.0, and statsmodels 0.14.6.

The archived input produced, to published rounding:

| Model | Term | Verified OR | 95% CI | p-value |
|---|---|---:|---|---:|
| PRIMARY_STRUCTURE | Initial competition (doubling) | 0.537969 | 0.360113–0.803666 | 0.002468 |
| PRIMARY_STRUCTURE | Type supply share (doubling) | 1.249251 | 1.038302–1.503057 | 0.018361 |
| FINANCING | Initial competition (doubling) | 0.536146 | 0.356376–0.806600 | 0.002777 |
| FINANCING | Equity floor proxy (doubling) | 0.843281 | 0.602465–1.180356 | 0.320466 |

**Disclosure:** At the time these files were added, this execution environment could read the GitHub public 31-column CSV via GitHub tooling but could not download it into the Python execution container. Therefore, **a Python run against the actual GitHub-hosted CSV has not yet been independently completed**. An earlier column audit found that 26 common columns matched by string and `type_supply_share_pct` in the public version was rounded to six decimals; across 184 rows the largest difference from the `supply / project_general_supply * 100` formula was under 0.0000005 percentage points. The archived file has extra or different columns. Do not treat this as byte-for-byte identity.

Reproduction of the entire upstream dataset construction, RPG-linked model, grouped cross-validation, eligibility/notice joins, and alternate-threshold robustness **is not covered** by this script. The source record should not be represented as a causal experiment.

## Provenance and citation

- Original dataset: `apttosell-ddfs-national-type-riskset-2026-v1.0.csv` (unchanged).
- Original result table: `apttosell-ddfs-national-type-model-results-2026-v1.0.csv` (unchanged).
- Canonical original record: https://doi.org/10.5281/zenodo.23328833
- Article and interpretation: https://apttosell.com/ddfs-type-reappearance-2026/
- Original license and citation metadata: see `README.md`, `CITATION.cff` and `.zenodo.json`.

These reproduction aids are provided under CC BY 4.0 consistent with the surrounding public research package. They **do not create another DOI** or change the original study conclusions.
