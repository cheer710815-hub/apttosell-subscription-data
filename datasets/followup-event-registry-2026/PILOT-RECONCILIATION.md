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

The mismatch is not silently corrected.

It indicates that the older event seed does not currently contain the earliest follow-up notice implied by the published project-level table. The June 8 event remains a valid historical seed candidate, but it must not be labeled as the project's first follow-up event until the missing earlier notice is reconstructed.

The July 23 OPTIONAL event is retained as a later event and is not part of the first-event comparison.

## Quality rule added

When project-level `days_to_first_followup` and an event-level notice disagree:

1. preserve both records,
2. flag the project for reconciliation,
3. do not overwrite either date,
4. do not renumber later event sequences until official notice chronology is reconstructed.
