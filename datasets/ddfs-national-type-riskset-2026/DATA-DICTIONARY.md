# DDFS National Type Risk-set — Data Dictionary v1.0

## Unit of observation
One official housing type (HOUSE_TY) within an initial recruitment announcement.

## Eligibility
A row is included only when:
- the project has a verified first follow-up supply event;
- the housing type's initial general-supply first-priority aggregate competition is >=6.0x.

## Core identifiers
- HOUSE_MANAGE_NO: initial recruitment announcement management number
- project: project name
- HOUSE_TY: official ApplyHome housing type
- official_followup_notice_id: first follow-up notice identifier

## Initial demand
- supply: initial general-supply units for the type
- project_general_supply: total initial general-supply units for the project
- type_supply_share_pct: supply / project_general_supply * 100
- applicants: initial first-priority aggregate applicants for the type
- rate: applicants / supply

## Outcome
- reappeared_first_followup: 1 when the identical housing type appears in the project's first follow-up supply; otherwise 0
- first_followup_type_units: number of units of the identical type in that first follow-up supply
- reappearance_verification_status: audit status of the type match

## Price and finance
- initial_type_price_krw: initial type maximum sale price
- regulated_flag: regulated-area flag at the relevant first-follow-up policy point used for the standardized comparison
- capital_region_flag: Seoul/Gyeonggi/Incheon indicator
- ltv_proxy_pct: standardized ordinary-borrower LTV proxy
- final_mortgage_price_cap_krw: standardized home-purchase mortgage cap where applicable
- final_mortgage_proxy_krw: min(LTV amount, applicable price-tier cap)
- equity_floor_proxy_krw: initial_type_price_krw - final_mortgage_proxy_krw
- equity_floor_pct: equity_floor_proxy_krw / initial_type_price_krw * 100
- midterm_60pct_scenario_self_fund_krw: scenario-only self-fund amount assuming a 60% interim-payment schedule; this is not a claim about the actual schedule of every project

## Provenance
- canonical_official_source_url: official or primary-verified first-follow-up source where available
- evidence_grade: provenance quality label

## Linked analysis
RPG is linked separately by HOUSE_MANAGE_NO + HOUSE_TY:
- rpg_pct: (comparable existing-home price - sale price) / sale price * 100
- positive means the comparable price is above the sale price
- quality_warning identifies weaker comparable construction

## Interpretation rules
Do not interpret:
- DDFS as a cancellation rate
- reappearance as proof of winner contract abandonment
- financing proxies as individual loan quotes
- model coefficients as causal effects

## Frozen version
v1.0 methodology is frozen. Corrections require a new release version and release notes.
