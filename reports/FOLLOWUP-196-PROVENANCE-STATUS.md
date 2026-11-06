# Provenance and reproducibility status — 196-project follow-up analysis

**Audit date:** 2026-11-06
**Study:** AptToSell apartment subscription competition and follow-up supply, initial announcements Jan–Sep 2026, observation cutoff 2026-10-04.
**Citation:** https://doi.org/10.6084/m9.figshare.34064439
**Canonical report:** https://apttosell.com/%ec%b2%ad%ec%95%bd-%ea%b2%bd%ec%9f%81%eb%a5%a0/

## What is directly verifiable

- Published project-level output: [196-project CSV](apttosell-apartment-subscription-followup-projects-2026-jan-sep.csv).
- Published aggregate output: [11-summary-row CSV](apttosell-followup-analysis-2026-jan-sep-summary.csv).
- [Methods](apttosell-followup-analysis-2026-jan-sep-methodology.md) and [field dictionary](apttosell-followup-analysis-data-dictionary.md).
- [Standalone derived-table consistency checker](verify_public_followup_196.py); run `python reports/verify_public_followup_196.py` from the cloned repository.
- The published derived CSVs were parsed and cross-tabulated on 2026-11-05: 196 unique project IDs, 193 nonblank competition rates, 44 projects at first-priority competition >=10:1, 19 with follow-up supply, and 13/36 followed within 60 days. Eleven grouped/headline summary rows match when the three rate-unavailable records are excluded from both group summaries.
- Every one of the 196 output rows carries a nonempty official ApplyHome detail URL. **These URLs are source pointers, not archived byte-for-byte evidence of the API response used.**

## What this audit cannot establish

The study is **NOT certified as end-to-end independently reproducible** from the originally retrieved official API responses. The following artifacts have not yet been authenticated as the original inputs and runnable transformation process for this exact 196-project release:

1. Original ApplyHome responses for announcement details, competition rates, model-level prices, residual/unsold notices, and optional-supply notices, preserving original bytes.
2. Collection manifest with endpoint, parameter tuple, retrieval date/time, request/response status, pagination, and raw-file path.
3. SHA-256 checksum manifest for each original response, with a complete file inventory.
4. Version-pinned script/notebook that derives the 196-project cohort and joins follow-up events and competition/price rows.
5. Explicit join keys, normalization rules, treatment of amended/duplicate notices, exclusion log, right-censoring rules, and deterministic output comparison.

A limited check looked for common manifest and pipeline filenames in the public repository, but did not establish that no files of those kinds exist elsewhere. **Do not treat filename checks as proof of nonexistence.**

## Release interpretation

- **Verified:** consistency of the *published derived tables* and the existence of the downloadable data, methods, and checker.
- **Not verified:** correctness of upstream source snapshots, completeness of collection, official-source provenance, or independent reproduction of the full pipeline.
- **No new DOI:** preserve the existing Figshare identifier. Do not re-release this research merely for a documentation update.
- **Decision:** `IMPROVE` pending a raw-source inventory and runnable transformation audit.

## Next evidence acceptance test

To move beyond derived-table verification, supply a manifest and raw files whose SHA-256 checksums validate, run the documented transformation in a clean environment, and compare the newly generated public project and summary CSVs against this release (documenting deliberate differences if any). Protect any personal or sensitive content and respect official API licensing and access rules.
