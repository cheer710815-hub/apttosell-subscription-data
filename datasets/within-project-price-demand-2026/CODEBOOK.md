# Codebook and scope

- `HOUSE_MANAGE_NO`: official project identifier.
- `HOUSE_TY`: official unit type identifier; leading/trailing whitespace removed for joins.
- `LTTOT_TOP_AMOUNT`: advertised maximum unit-type price, in KRW 10,000 units.
- `area`: original matched exclusive area, in m²; retained from matched source data because not all model response fields provide the same area variable.
- `area_band_m2`: rounded exclusive-area comparison band within a project.
- `low_type` / `high_type`: least / most expensive by advertised maximum price per m² among same-project, same-rounded-area candidates.
- `SUPLY_HSHLDCO` (competition API): denominator of applicant-to-supply ratio; **not identical to model API general supply**.
- `SUBSCRPT_RANK_CODE=1`: first-priority rank; sum `REQ_CNT` over region rows for each housing type.
- `applicant_to_supply_ratio`: summed first-priority applicants divided by competition API supply count.

Limits: nonrandom cohort; some very small supply types; distinct actual areas within rounded bands; multiple comparison groups may originate from the same project; floor, orientation, plan and view effects not controlled; individual region competition and allocation rules differ; no causal or contracted-sales conclusions.
