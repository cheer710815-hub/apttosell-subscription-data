# AptToSell 2026 subscription follow-up — Reproducibility audit kit

Research source: https://huggingface.co/datasets/eunguneun/korea-apartment-subscription-followup-supply-2026

**Status: Published on GitHub as an audit companion to the existing Hugging Face dataset (Stage 41).**

This kit uses the **existing** Hugging Face dataset, with 196 project records and 11 aggregate summary rows. No DOI is created, no original CSV is modified or redistributed here, and no independent citation or external reuse is claimed.

## Files
- `reproducibility/reproduce.py`: Python 3.9+ standard-library-only recomputation script; CSVs downloaded into local `source/` or used via `--offline`.
- `reproducibility/test_reproduce.py`: script unit tests.
- `results/audit.json`: user-executed PASS report received on 2026-11-16.
- `results/summary_comparison.csv`: 11 published summary rows compared with recalculated values.
- `results/price_band_sensitivity.csv`: 193-record complete-case versus 196-record price-band sensitivity.
- `MANIFEST.json`: file hashes and audit evidence/limitations.

## Run locally

From the `reproducibility` directory:

```cmd
py -3 -m unittest -v test_reproduce
py -3 reproduce.py
```

To avoid network requests, place the two original Hugging Face CSVs in `reproducibility/source/` and run:

```cmd
py -3 reproduce.py --offline
```

The tool writes `results/audit.json`, `results/summary_comparison.csv`, and `results/price_band_sensitivity.csv` relative to the current working directory. The `results/` folder included in this package contains the previously submitted Windows results, not a newly run full-source recomputation on this machine.

## Scope and caveats

- Aggregate CSV rows and result files are internally consistent in Stage 39/40 checks: **11/11 summary rows, 5/5 price bands**.
- The source CSV SHA-256 digests in `audit.json` were **computed on the user's Windows run** and are documented in `MANIFEST.json`. Their bytes have **not been independently re-downloaded and hashed** in the Stage 40 container because network DNS is unavailable.
- This does not independently verify ApplyHome announcements, attribution, event matching, or treatment of post-cutoff later notices.
- The high-competition figures are 19/44 = 43.18% observed follow-up and 13/36 = 36.11% for eligible 60-day follow-up; they are not cancellation or contract-failure rates.
- The original published `summary` uses 193 records with known competition rates, including its price-band rows. The full-cohort 196-project sensitivity results are supplemental.
- Do not mistake an automated Hugging Face Parquet conversion or a public directory listing for independent scholarly citation.

## GitHub placement proposal

Existing repository: `cheer710815-hub/apttosell-subscription-data` (publication approved by owner on 2026-11-17).
Published folder: `reproducibility/hf-followup-supply-2026/stage40/`.

The dataset's root is Hugging Face and is distinct from the separate 103-record event-registry data in this GitHub repository. Keep the two studies differentiated. No new DOI.