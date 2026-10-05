# Integration Guide — AptToSell Project ID

Use `apttosell_project_id` as the internal join key across AptToSell datasets.

## Primary mapping file

`apttosell-project-id-map-196-pilot-v0.4.csv`

The safest external anchor is currently `house_manage_no`.

## Example join

For a dataset that already contains `house_manage_no`:

1. Load the 196-project ID map.
2. Join on `house_manage_no`.
3. Add `apttosell_project_id` to the downstream dataset.
4. Keep the original source identifier; do not replace it.
5. Do not manufacture an AptToSell ID for unmatched rows without identity review.

## Demonstration crosswalk

`pre-movein-public-41-with-project-id-pilot-v0.4.csv` demonstrates the join against the fixed Version 1.0 pre-move-in funding public subset.

All **41 of 41** public rows matched a project ID.

## Versioning rule

The fixed Version 1.0 pre-move-in funding CSV is not modified. The project ID is added in a separate crosswalk file so the published DOI dataset remains reproducible.
