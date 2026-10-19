# Windows one-month trial — N01 presale-rights API

Keep `collect_molit_presale_rights.py` and `run_one_month_windows.ps1` in the same local directory. Install Python 3 and the Windows Python launcher (`py`). In PowerShell, navigate to the directory and run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\run_one_month_windows.ps1 -Region 48170 -Month 202609
```

This command tests **Jinju (48170), September 2026** only. It does **not** reconstruct the nationwide 980-record cohort.

When prompted, enter the **decoding/plain (not URL-encoded) service key** locally, not in ChatGPT, a GitHub issue, a screenshot, or a tracked file. The masked prompt does not write the key to disk; the environment variable is cleared after the collector exits. The underlying Python process necessarily holds the key temporarily in memory and transmits it to the API.

Output: `private_raw/molit_presale_rights_48170_202609_raw.csv` and the corresponding `_manifest.json`. Treat them as **private raw research files**. Do not commit raw CSV or share it publicly before privacy review; to request analysis share only a redacted manifest with the service-key value absent.

Expected: `resultCode=000`; data rows vary and may be zero. A nonzero exit, authentication response code 30, quota response code 22, or network error is a failed/blocked collection, not zero records. 

IMPORTANT: This is a single-city/month pilot, not a verified N01 sample. Classification status remains BLOCKED until values and the original N01 selection policy are verified. Document the response's field inventory and compare the manifest total with the raw CSV. Distinguish pre-sale rights from occupancy rights by checking `ownershipGbn`; do not infer identity from blank optional fields alone.

Security: do not paste your key into shell command arguments, GitHub, email, or chat; rotate it if exposed. Verify actual service permissions and API traffic allowance in your own data.go.kr account before extending the geographic/monthly scope.
