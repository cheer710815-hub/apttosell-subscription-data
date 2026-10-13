# Zenodo / Figshare / Mendeley submission metadata — within-project price–demand study (2026)

Status: **submission-ready metadata; NOT deposited; no DOI assigned**.
Canonical research article: https://apttosell.com/apartment-type-price-subscription-demand-2026/
Source repository: https://github.com/cheer710815-hub/apttosell-subscription-data/tree/main/datasets/within-project-price-demand-2026/

## Suggested metadata

- Resource type: Dataset
- Title: Within-project Apartment Unit Price and First-priority Application-to-supply Comparisons in South Korea, 2026
- Creator: AptToSell Research (follow the existing CITATION.cff; do not invent an ORCID)
- Version: 1.0 (existing GitHub version; confirm release date before deposit)
- Language: English and Korean as applicable to uploaded files
- Keywords: South Korea; apartment presale; housing subscription; housing type; unit price; first-priority applications; within-project comparison
- License: Verify the source files and derivative rights before selecting CC BY 4.0 for the deposit. Attribution to the public-sector source does not convey ownership of underlying official data.
- Related identifier: canonical article above (IsDocumentedBy); GitHub dataset directory above (IsSupplementTo).

## Study scope and findings (observational)

- 140 reconciled housing projects, 898 official housing types, 205 project-by-rounded-area comparison groups.
- Of 201 non-tied groups, 145 (72.14%) had a higher application-to-supply ratio for the higher-priced type.
- Project-cluster bootstrap 95% interval approximately 64.9%–78.9%.
- This is a conditional comparison of a selected dataset, not a nationally representative population estimate.
- No causal inference about price increasing demand; applicant-to-supply ratio is not a signed contract rate.

## Prior-work overlap assessment (2026-10-13)

The central publication ledger was checked before this submission sheet was updated.

| Prior work | Existing record | Relationship to this dataset | Deposit decision |
|---|---|---|---|
| A01, price merit versus first-priority competition, 2025–2026 | Zenodo DOI 10.5281/zenodo.23258478 | Similar topic; project-level price merit versus competition, while this study compares similarly sized housing types *within* each project | Do not assert a new independent contribution until project-ID/sample and variable overlap are measured |
| A20, relative price gap (RPG) and subscription demand | Zenodo DOI 10.5281/zenodo.23251654 | Similar price–demand framing; RPG study records 183 projects in ledger versus 140 projects here; unit of analysis and model differ | Compare project identifiers, cohort dates, variable definitions and output tables before assigning another DOI |
| A17, this 140-project / 898-type / 205-group study | GitHub and AptToSell article already published | This is the **same** study, not a new release merely because a deposit sheet exists | Do not create duplicate records or present it as newly discovered |
| Q07, DDFS type-level first follow-up | Zenodo DOI 10.5281/zenodo.23328833 | Different outcome (type reappearance in follow-up supply); may share underlying ApplyHome projects | Keep DOI separate; cite as related research only where appropriate |

**Current determination:** distinct *research question*, but **raw project-ID overlap and original dataset reuse percentages have not yet been independently computed**. Therefore an additional DOI/deposit is **on hold pending measured overlap and an existing-record search**. This sheet is documentation, not an authorization or evidence of repository acceptance.

## Deposit checklist

1. Inspect all files in this directory and upload **the frozen CSV data, README.md, METHODOLOGY.md, CODEBOOK.md, CITATION.cff**, and any reproducibility scripts actually present. Do not invent filenames.
2. Verify checksums, row counts and publication-safe interpretation against the canonical article and CSV before deposit.
3. Search Zenodo, Figshare, Mendeley Data, and the central ledger for an existing DOI or draft **before** creating a record.
4. Deposit one canonical DOI record first; when mirroring, explicitly cite the canonical DOI and mark the upload as a copy/mirror, not a new independent study.
5. After DOI publication, update this file, CITATION.cff, README.md, and the AptToSell article with the exact DOI.
6. Record each actual submission, review state and published URL in the central ledger. Never label a draft as accepted or published.

## Reuse/citation

Cite AptToSell Research, *Within-project Apartment Unit Price and First-priority Application-to-supply Comparisons in South Korea, 2026*, version 1.0, GitHub dataset directory and canonical AptToSell article above. Add a DOI **only once actually assigned**.
