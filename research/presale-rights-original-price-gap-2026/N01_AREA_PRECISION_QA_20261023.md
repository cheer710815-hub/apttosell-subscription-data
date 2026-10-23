# N01 exclusive-area CSV precision audit (2026-10-23)

Checked saved ZIP CSV data and stored manifest hashes. Older private cohort: 38 CSVs, 717 rows, all decimal area values. Seventh batch: 6 CSVs, 107 rows, 105 decimal and two literal integer area values. Combined 44 files, 824 records, 822 decimal area strings, two literal `84` strings, zero missing/malformed, all 44 file SHA-256 checks and manifest row counts matched.

Both integer area values belong to September 2026 Sejong Aspen: an 8th-floor brokered record and a 7th-floor direct record. The direct deal is not provisionally eligible. Another October Aspen row retains area `84.5013`. This is not proof that either September `84` should be expanded to that subtype.

The archives contain CSV and JSON manifests, not original HTTP XML, so it is NOT possible to determine whether government response already said `84` or the collector transformed it. The available batch runner delegates raw parsing to an imported collector whose source is not included there. Re-query the original request month with unchanged collection preserved; store HTTP XML snapshot hash and compare strings by source-identifying fields.

No cohort change: original 824, provisional 606, notice reference 29 (25 unique price, 4 ambiguous), final monetary price comparisons 0. No DOI or premium inference.
