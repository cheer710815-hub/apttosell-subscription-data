# Raw API JSON and first-round PDF evidence gate — 2026-10-20

## Work performed
- Examined the previously supplied CSV reports and existing batch collector code.
- Confirmed the collector already writes 18 original response JSON files to results/raw_api when run successfully.
- Current two submitted CSV files do not include those JSON bytes, so recorded SHA-256 strings cannot be independently recomputed from the submitted evidence.
- Prepared a local offline exporter/validator that reads the original 18 JSON files without another API call, recalculates SHA-256, redoes the 16 model count comparisons from the raw payloads, inventories nine PDF files, and bundles evidence into a ZIP.
- Test using currently available CSVs only: 0 JSON files available, 0 recomputed hashes, 0 original PDFs; the tool appropriately reports not verified.

## Files produced for user
- AptToSell_9_EVIDENCE_EXPORT.zip; Windows entry point EXPORT_RESULTS.bat.
- Keep the collector results folder including raw_api untouched; copy into the new tool directory and run exporter.
- User must not include API access token or service key in the resulting archive.

## Current research figures (unchanged)
- 25 eligible models, 366 provisional first-round no-priority offered units.
- 16 models and 220 units matched to user-executed official API batch CSV reports; raw JSON SHA-256 still to recheck.
- 9 models and 146 units had a directly checked original first-round PDF in prior audits.
- The remaining 9 projects (220 units) still require original first-round PDF document table checks.

No DOI, website publication, or PDF-evidence grade upgrade.
