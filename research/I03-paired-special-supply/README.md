# I03 — Paired first-time vs newlywed special-supply demand

**Study status:** Reproducible follow-up analysis of the already-published N07 dataset. **No independent DOI.**

**Parent source:** Kim, E. (2026), *South Korea Apartment Special Supply Applications and Allocations, 2025–2026: 471 Projects and 2,591 Housing Types* (v1.0), Zenodo. https://doi.org/10.5281/zenodo.23827229

## What was compared?
Within the same ApplyHome recruitment notice and housing type, match the first-time-buyer and newlywed categories only where **both have positive allocated units** and application totals are present. For each project aggregate matched housing types, calculate each category's total applications divided by total allocated units. This is a matched descriptive comparison, not an estimate of causal effects or individual winning probabilities.

## Independently replicated results
- Source: **20,728** housing-type × category records in N07.
- Matched: **1,679 housing-type pairs** across **452 projects**, 17 regions.
- Project-level first-time-buyer ratio higher: **395**; newlywed ratio higher: **45**; ties: **12** (all ties are zero applications in both categories).
- Excluding the 12 both-zero ties: first-time ratio higher in **395 of 440 (89.77%)** projects with at least one application.
- Regenerated the I03 matched outputs from the N07 source CSV: **zero row-level calculation mismatches**.

## Data and reproducibility
The locally prepared I03 research package contains paired and project-level CSV tables, region-level sensitivity counts, a Python cross-check, QA results with SHA-256 hashes, and research notes. It is **not yet deposited in this GitHub repository**; this page records the methodological and citation link to the public N07 source. The parent N07 CSVs and documentation can be downloaded from its Zenodo record.

## Limits
The matched design holds the observed project/housing-type constant; applicant eligibility and category allocation mechanisms are **not equivalent**. The sample excludes missing or zero-denominator categories and may exhibit selection bias. Application-to-allocation ratios are not legal subscription competition rates, individual winning odds, housing contracts, or census-complete nationwide statistics. **I03 is not an independent new dataset DOI.**

Original source: Korea Real Estate Board, ApplyHome public API. Research analysis: AptToSell.
