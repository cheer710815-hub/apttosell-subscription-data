# Methodology — Follow-Up Event Registry 2026

## 1. Unit of observation

One row represents the first observed follow-up supply event for one project.

## 2. Source

The source is the existing project-level AptToSell 2026 competition/follow-up analysis table.

## 3. Date derivation

`derived_first_followup_date = initial_announcement_date + days_to_first_followup`

The derived date is reproducible from existing published fields but is not treated as an independently re-verified official event date.

## 4. Event subtype

The project-level table does not preserve a subtype for each follow-up event. Therefore the pilot uses:

`followup_supply_observed_unspecified`

No residual-unit / no-priority / discretionary-supply subtype is guessed.

## 5. Multiple events

`project_followup_event_count` is retained, but only the first event is materialized in this pilot.

Later event dates must be reconstructed from underlying official notices before separate event rows are created.

## 6. Verification status

`DERIVED_FIRST_EVENT_DATE` means the date is deterministically reconstructed from published project-level fields.

It does not mean the individual event notice has been independently re-opened and primary-source verified.

## 7. Versioning

No DOI is assigned to this pilot. A versioned event registry requires official notice-level event IDs, dates, and subtypes.


## Secondary corroboration rule

When the project-level derived first-event date is independently reproduced by multiple public sources but the original official notice identifier is not yet recovered, the event may be stored as `SECONDARY_CORROBORATED`.

This status is sufficient to reconcile event chronology but not sufficient for a future primary-source public release.
