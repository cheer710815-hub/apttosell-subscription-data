# Release Notes

## v1.0 — 2026-10-08

Initial public release of the AptToSell DDFS National Type-level Risk-set 2026.

### Scope
- 52 South Korean apartment projects with a verified first follow-up supply event
- 184 official housing types with initial general-supply first-priority competition of at least 6.0x
- 78 housing types reappeared in the first follow-up supply
- 106 housing types did not reappear
- Type-level reappearance rate: 42.39%

### Main findings
- Initial competition depth was inversely associated with first-follow-up reappearance.
- Type supply share was positively associated with first-follow-up reappearance.
- Primary clustered logistic model:
  - competition per doubling: OR 0.538, 95% CI 0.360–0.804, p=0.0025
  - type supply share per doubling: OR 1.249, 95% CI 1.038–1.503, p=0.0184
- Absolute sale price, regulated-area status, standardized financing burden, and linked relative price gap were not independently significant after adjustment in the reported models.

### Files in this release
- `apttosell-ddfs-national-type-riskset-2026-v1.0.csv`
- `apttosell-ddfs-national-type-model-results-2026-v1.0.csv`
- `DATA-DICTIONARY.md`
- `METHODOLOGY-AND-FINDINGS.md`
- `README.md`
- `CITATION.cff`
- `datapackage.json`
- `.zenodo.json`

### Interpretation limits
This release measures whether the identical official housing type reappeared in the first follow-up supply. It does not measure cancellation rate, contract failure rate, winner abandonment, or individual loan availability. Results are observational and should not be interpreted as causal.

### License
CC BY 4.0.

### Canonical article
https://apttosell.com/ddfs-type-reappearance-2026/

### DOI
Pending Zenodo registration. After DOI issuance, update README.md, CITATION.cff, Dataset JSON-LD, and the canonical AptToSell article without altering the frozen v1.0 analytical files.
