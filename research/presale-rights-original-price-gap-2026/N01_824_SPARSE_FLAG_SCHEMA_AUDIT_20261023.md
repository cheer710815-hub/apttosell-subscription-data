# N01 sparse status-field audit — 2026-10-23

Audited all saved primary data CSVs: 38 prior + 6 batch7 = 44 files / 824 source records. The original manifests for all 44 carry `candidate_filter_schema_complete=false` and `classification_status=BLOCKED_PENDING_LIVE_VALUES_AND_COHORT_RECONCILIATION` because status marker fields are not nonblank in every row. This is a **manifest completeness gate**, not positive proof of corrupt or missing API values.

Source field frequencies: `ownershipGbn`: 802 blank / 22 `입`. `cdealType`: 785 blank / 39 `O`. `dealingGbn`: 655 `중개거래` / 169 `직거래`. Applying previous provisional filter (brokered trade, both actors individuals, ownership not `입`, cancellation not `O`) recomputes **606 provisional candidates**. All 606 have blank `ownershipGbn` and `cdealType`. Source government's HWP coding guidance says `ownershipGbn` is filled `입` for occupancy rights; blank does NOT necessarily mean missing value. The cancellation flag's blank-vs-`O` semantics must be separately confirmed in original schema/authority documentation before elevating this to a validated absence of rescission. Never reinterpret blank automatically as a third right kind or missing classification.

Sejong September area `84` source investigation remains unresolved: 2026-09-26 8F brokered and 2026-09-11 7F direct both have integer area in saved CSV, source HTTP response XML not archived. Non-destructive v1.1 requery requires government service key; no live query performed.

Research stance: unchanged 824 raw, 606 *preliminary* screen, 29 notice-reference candidates (25 unique tier prices, 4 line-dependent price intervals), **0 final monetary transfer-price comparisons**. The historical N01 published descriptive 980 is distinct. Do not publish premium/gain or new DOI.
