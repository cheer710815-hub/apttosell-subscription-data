# Research audit log (2026-11-24)

**Status:** Draft changes on `audit/doi-provenance-20261124` only. Default branch not changed. No DOI creation, provider login, file deletion, or CSV rewrite.

## Verified by connected GitHub file reads
- The root `CITATION.cff` formerly listed six identifiers spanning baseline reference, legacy mirrors, 196-project follow-up analysis, and 103-project derivative; proposed revision removes unrelated identifiers from root and directs readers to research-specific records.
- Two 196-project CSVs had identical sets of 196 house-management IDs. The comparable follow-up flag, count, first date, days, initial announcement date, and rates (tolerance 0.001) yielded no mismatches.
- All 103 first-event registry projects belong to those 196 source project IDs.
- A further historical Figshare identifier `10.6084/m9.figshare.33948868` is referenced in README for a deposit-table record and needs provider reconciliation.
- Prior audit reports compared two CSVs in Figshare record `34064439`, but did not complete frozen methodology/document dictionary reconciliation.

## Proposed doc-only changes
- `RESEARCH_INVENTORY.md`: research families/derivatives/verification boundaries.
- `DOI_REGISTRY.md`: legacy identifiers and current uncertainty.
- `PUBLICATION_POLICY.md`: temporary submission freeze, citation, reuse, originality safeguards.
- `CITATION.cff`: repository catalog citation; study-specific DOI moved to research inventory.
- `README.md`: prominent audit status and documentation links.

## Still unresolved
- Full Figshare deposited files and metadata (including disabled-account record `34536966` and private draft `34948234`).
- Zenodo/Dataverse/Mendeley actual record accessibility and version identity.
- DDFS overlap/independence, external source rights and copied-text comparison.
- Remaining GitHub branches, histories, supplementary unpublished files, and all repository file manifests.
- Other accessible repositories (real-estate-mcp, awesome-real-estate, awesome-real-estate-investing, apd-core, awesome-public-data-sources, k-skill) require upstream license/fork checks before any modifications.

**Release rule:** Do not merge the documentation proposal until reviewed. Never interpret this audit log as a provider-policy clearance or a claim of no account-restriction risk.
