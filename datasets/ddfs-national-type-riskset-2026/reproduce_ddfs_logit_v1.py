#!/usr/bin/env python3
"""Reproduce the two DDFS v1.0 housing-type logistic models from its released CSV.

Usage:
  pip install -r requirements-reproduction.txt
  python reproduce_ddfs_logit_v1.py --input apttosell-ddfs-national-type-riskset-2026-v1.0.csv --output reproduction_results.json

The script does not recreate the upstream cohort, RPG-linked models, or grouped CV.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

import numpy as np
import pandas as pd
import scipy
import statsmodels
import statsmodels.api as sm

REQUIRED = [
    "HOUSE_MANAGE_NO", "HOUSE_TY", "rate", "type_supply_share_pct",
    "project_general_supply", "initial_type_price_krw", "regulated_flag",
    "capital_region_flag", "equity_floor_proxy_krw", "reappeared_first_followup",
]
MODELS = {
    "PRIMARY_STRUCTURE": [
        "rate", "type_supply_share_pct", "project_general_supply",
        "initial_type_price_krw", "regulated_flag", "capital_region_flag",
    ],
    "FINANCING": [
        "rate", "type_supply_share_pct", "project_general_supply",
        "equity_floor_proxy_krw", "capital_region_flag",
    ],
}
LOG2 = {
    "rate", "type_supply_share_pct", "project_general_supply",
    "initial_type_price_krw", "equity_floor_proxy_krw",
}
# Published v1.0 figures, rounded as published: OR, lower CI, upper CI, p.
REFERENCE = {
    "PRIMARY_STRUCTURE": {
        "rate": (0.538, 0.360, 0.804, 0.0025),
        "type_supply_share_pct": (1.249, 1.038, 1.503, 0.0184),
        "project_general_supply": (0.720, 0.488, 1.061, 0.0971),
        "initial_type_price_krw": (0.786, 0.416, 1.486, 0.4593),
        "regulated_flag": (0.838, 0.258, 2.718, 0.7688),
    },
    "FINANCING": {
        "rate": (0.536, 0.356, 0.807, 0.0028),
        "type_supply_share_pct": (1.251, 1.054, 1.486, 0.0106),
        "project_general_supply": (0.717, 0.498, 1.032, 0.0734),
        "equity_floor_proxy_krw": (0.843, 0.602, 1.180, 0.3205),
        "capital_region_flag": (0.340, 0.097, 1.198, 0.0931),
    },
}


def reproduce(path: Path) -> dict:
    raw = path.read_bytes()
    df = pd.read_csv(
        path, dtype={"HOUSE_MANAGE_NO": "string", "HOUSE_TY": "string"}
    )
    absent = sorted(set(REQUIRED) - set(df.columns))
    if absent:
        raise ValueError(f"Required columns absent: {absent}")
    if len(df) != 184:
        raise ValueError(f"Expected 184 rows; received {len(df)}")
    if df[["HOUSE_MANAGE_NO", "HOUSE_TY"]].isna().any().any():
        raise ValueError("Missing housing type IDs")
    if df.duplicated(["HOUSE_MANAGE_NO", "HOUSE_TY"]).any():
        raise ValueError("Duplicate official housing-type key")
    for col in REQUIRED[2:]:
        df[col] = pd.to_numeric(df[col], errors="raise")
        if df[col].isna().any() or not np.isfinite(df[col]).all():
            raise ValueError(f"Invalid numeric column: {col}")
    if not df["reappeared_first_followup"].isin([0, 1]).all():
        raise ValueError("The outcome must be binary")
    for col in LOG2:
        if (df[col] <= 0).any():
            raise ValueError(f"Log2 predictor must be positive: {col}")
    if (
        df["HOUSE_MANAGE_NO"].nunique() != 52
        or int(df["reappeared_first_followup"].sum()) != 78
    ):
        raise ValueError("Expected 52 projects and 78 reappearing types")

    result = {
        "input_file": path.name,
        "input_sha256": hashlib.sha256(raw).hexdigest(),
        "n_types": len(df),
        "n_projects": int(df["HOUSE_MANAGE_NO"].nunique()),
        "n_reappeared": int(df["reappeared_first_followup"].sum()),
        "environment": {
            "python": platform.python_version(),
            "pandas": pd.__version__,
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "statsmodels": statsmodels.__version__,
        },
        "method": (
            "GLM binomial logit, HOUSE_MANAGE_NO cluster-robust covariance, "
            "use_correction=True, Wald 95% intervals"
        ),
        "models": {},
    }
    for name, fields in MODELS.items():
        x = pd.DataFrame(index=df.index)
        for field in fields:
            x[field] = np.log2(df[field]) if field in LOG2 else df[field]
        x = sm.add_constant(x, has_constant="add")
        fit = sm.GLM(
            df["reappeared_first_followup"],
            x,
            family=sm.families.Binomial(),
        ).fit(
            cov_type="cluster",
            cov_kwds={
                "groups": df["HOUSE_MANAGE_NO"],
                "use_correction": True,
            },
        )
        ci = fit.conf_int(alpha=0.05)
        terms = {}
        for term in fields:
            odds = float(np.exp(fit.params[term]))
            lo, hi = map(float, np.exp(ci.loc[term]))
            p_value = float(fit.pvalues[term])
            reference = REFERENCE[name].get(term)
            passed = None
            if reference:
                passed = (
                    abs(odds - reference[0]) < 0.0015
                    and abs(lo - reference[1]) < 0.002
                    and abs(hi - reference[2]) < 0.002
                    and abs(p_value - reference[3]) < 0.0002
                )
            terms[term] = {
                "odds_ratio": odds,
                "ci95_low": lo,
                "ci95_high": hi,
                "p_value": p_value,
                "unit": "per doubling" if term in LOG2 else "binary",
                "published_reference": reference,
                "matches_published_rounding": passed,
            }
        result["models"][name] = {
            "n": int(fit.nobs),
            "terms": terms,
            "all_checked_terms_match": all(
                t["matches_published_rounding"] is not False
                for t in terms.values()
            ),
        }
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument(
        "--output", default=Path("ddfs_reproduction_results.json"),
        type=Path,
    )
    args = parser.parse_args()
    result = reproduce(args.input)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    for model_name, model in result["models"].items():
        print(model_name, "PASS" if model["all_checked_terms_match"] else "MISMATCH")
        for term, t in model["terms"].items():
            print(
                f"  {term}: OR={t['odds_ratio']:.6f}; "
                f"CI=[{t['ci95_low']:.6f}, {t['ci95_high']:.6f}]; "
                f"p={t['p_value']:.6f}"
            )
    if not all(
        m["all_checked_terms_match"]
        for m in result["models"].values()
    ):
        raise SystemExit("One or more published coefficients failed comparison")


if __name__ == "__main__":
    main()
