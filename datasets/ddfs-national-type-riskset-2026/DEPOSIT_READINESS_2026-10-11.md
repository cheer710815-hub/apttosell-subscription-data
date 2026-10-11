# DDFS v1.0 — repository deposit readiness (2026-10-11)

## Purpose
Pre-submission QA for the **existing** AptToSell DDFS type-level risk-set study; this is not a new dataset or a new study version. No new DOI should be created without first checking the Zenodo account's existing unpublished drafts and any pre-existing DOI for the same release.

## Audited frozen dataset
- GitHub source: `datasets/ddfs-national-type-riskset-2026/`
- Study version: **1.0** (original release 2026-10-08)
- Source CSV: `apttosell-ddfs-national-type-riskset-2026-v1.0.csv`
- Observations: **184** unique project × official housing-type keys, **52** projects.
- CSV structure: **31 columns**, **184 data records**, **zero mismatched record widths**.
- First-follow-up type reappearance: **78** marked 1, **106** marked 0 (**42.39%** of the 184 study risk set).
- These counts were recalculated from the frozen public CSV on 2026-10-11. They do **not** measure contracts, cancellation, or actual loan availability.

## Eight expected deposit files confirmed on GitHub
1. `apttosell-ddfs-national-type-riskset-2026-v1.0.csv`
2. `apttosell-ddfs-national-type-model-results-2026-v1.0.csv`
3. `DATA-DICTIONARY.md`
4. `METHODOLOGY-AND-FINDINGS.md`
5. `README.md`
6. `CITATION.cff`
7. `RELEASE_NOTES.md`
8. `datapackage.json`

All eight paths were read successfully from GitHub on 2026-10-11. This note does not independently reproduce the reported logistic regressions or verify every official notice link.

## Deposit metadata and deduplication
Use the existing `ZENODO_SUBMISSION.md` for title, author, ORCID, CC BY 4.0 licensing assertion, version, method and linked original article.

**Before a Zenodo upload:** inspect the owner's existing draft records and issued DOIs for this exact study. A public search showing no record is not proof that there is no unpublished draft. If an exact matching draft exists, continue it; if a matching DOI already exists, update its metadata rather than creating an unnecessary duplicate.

After external publication, add the verified DOI to `README.md`, `CITATION.cff`, and the original AptToSell article. Follow-up Figshare / Mendeley / RePEc deposits must disclose the relation to the canonical dataset and avoid duplicate-study claims.

## Registration status
- GitHub source and QA: **publicly available**.
- Zenodo upload, DOI allocation, Mendeley / Figshare / RePEc new record: **not verified / not claimed by this note**.
