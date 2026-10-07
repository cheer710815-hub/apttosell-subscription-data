from pathlib import Path
import pandas as pd
import numpy as np
import statsmodels.api as sm

INPUT = Path("apttosell_rpg_regression_input_2026_v1.0.1.csv")
OUTPUT = Path("apttosell_rpg_regression_results_2026_v1.0.1_reproduced.csv")

df = pd.read_csv(INPUT)

def fit(data, with_rpg):
    d = data.copy()
    X = pd.DataFrame({
        "const": 1.0,
        "log_price": d["log_price"],
        "log_supply": d["log_supply"],
        "서울": (d["region_group"] == "서울").astype(int),
        "지방광역시": (d["region_group"] == "지방광역시").astype(int),
        "기타지방": (d["region_group"] == "기타지방").astype(int),
    })
    # Reference category: 경기·인천
    if with_rpg:
        X["rpg_pct_median"] = d["rpg_pct_median"]
    return sm.OLS(d["log_applicants"], X).fit(cov_type="HC3")

rows = []
samples = [
    ("all_183", df),
    ("high_quality", df[df["high_quality_project"] == True]),
]
for sample_name, data in samples:
    for model_name, with_rpg in [("base", False), ("plus_rpg", True)]:
        model = fit(data, with_rpg)
        for term in model.params.index:
            rows.append({
                "sample": sample_name,
                "n": int(model.nobs),
                "model": model_name,
                "term": term,
                "coef": model.params[term],
                "std_err_HC3": model.bse[term],
                "p_value": model.pvalues[term],
                "r_squared": model.rsquared,
            })

pd.DataFrame(rows).to_csv(OUTPUT, index=False, encoding="utf-8-sig")
print(f"Created: {OUTPUT}")
