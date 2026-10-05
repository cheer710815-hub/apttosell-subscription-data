# Pilot Event Reconciliation — 2026-10-05

This quality-control check compares the newly generated first-follow-up event dates with the older verified-events pilot.

## Results

- **구리역 하이니티 리버파크**: MATCH
  - Derived first follow-up: 2026-04-13
  - Existing follow-up seed: 2026-04-13
  - Difference: 0 days

- **해링턴 플레이스 노원 센트럴**: MISMATCH — review required
  - Derived first follow-up from the published project-level analysis: 2026-04-28
  - Existing seed UNSOLD event: 2026-06-08
  - Difference: 41 days

The mismatch has now been structurally reconciled without overwriting the historical seed.

The missing earlier event has been reconstructed as a 2026-04-28 58-unit no-priority/residual supply notice with corroborated numeric notice ID `2026910100`. The June 8 event remains a later historical follow-up event.

The July 23 OPTIONAL event is retained as a later event and is not part of the first-event comparison.

## Quality rule added

When project-level `days_to_first_followup` and an event-level notice disagree:

1. preserve both records,
2. flag the project for reconciliation,
3. do not overwrite either date,
4. do not renumber later event sequences until official notice chronology is reconstructed.


## Notice-ID recovery update

The 2026-04-28 Harrington event is consistently reproduced under numeric notice ID `2026910100` across multiple independent public mirrors.

The direct ApplyHome detail URL pattern was tested, but the current web environment could not access the page. Therefore the event remains `SECONDARY_CORROBORATED`, not `PRIMARY_VERIFIED`.
