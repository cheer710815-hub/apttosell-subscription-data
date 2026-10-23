# N01 schema completeness vs marker field values (2026-10-23)

Audited two private user-uploaded N01 ZIP archives with **44 manifest files covering 824 original CSV records**. Nine CSV files contain zero records, so a column schema cannot be inferred from their empty exports; they must be treated as `EMPTY_RESULT_SCHEMA_NOT_EVALUABLE`, not schema failure.

The other **35/35 nonempty files expose all eight required schema field names** (reported amount, area, cancellation status, trading mode, seller, buyer, rights type, floor). Nevertheless **44/44 legacy `candidate_filter_schema_complete=false`**, because the previous manifest gate conflated *nonblank values* with *field existence*. Per-field nonblank row frequencies: amount 824, exclusive area 824, cancellation flag 39, deal type 824, seller 824, buyer 824, rights kind 22, floor 824. These are **824-row source coverage** counts; zero-filled status fields are not automatic evidence of missing API columns.

Official government N01 SilvTrade HWP explicitly describes `ownershipGbn` as occupancy-right marker `입` when applicable. It follows that blank `ownershipGbn` can be a meaningful sentinel, though end-to-end upstream blank mapping and cancellation flag semantics have not been independently validated. `cdealType` 39 `O` and 785 blanks remain a source status pattern, not a proven 785 complete uncanceled contracts. Keep blank handling separate from code-validation logic.

**Corrected proposed QA dimensions**:
- `schema_field_names_present`: true for 35 nonempty files; null / not evaluable for 9 zero-row files. Never turn blank-rights-marker into a missing required field.
- `known_code_validity`: source-guided known codes and unknown codes, retaining blanks as separate category; do not reject null sentinels mechanically.
- `eligibility_preliminary`: existing conditional filter reproduces 606, not final certified presale cohort.
- `source_snapshot_vs_official_history`: pending for any subsequent cancellation/revision.
- `dealAmount_semantics`: pending competent authority answer.

**No source CSV or historical manifest overwritten**, and zero-row files cannot prove the collector queried the API correctly merely because its empty export is present. Retain legacy false flag untouched for traceability; version a separate corrected QA status rather than modifying prior experiment definitions.

Private comprehensive per-file CSV audit produced separately in conversation: `N01_824_schema_gate_audit_20261023.csv` (not uploaded to public GitHub). No individual reported transfer-price rows included in this public summary.

N01 balances unchanged: 824 raw; 606 provisionally filtered; 29 notice-source reference cases (25 unique tier price, 4 building-line price ranges); **0 validated financial comparisons**. Distinct historical N01 980 published study, no new DOI or premium claim.
