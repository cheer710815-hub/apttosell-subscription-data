# 2026 National DDFS Type-level Study — Final v1.0

## Executive finding
This study analyzes 184 housing types from 52 Korean apartment projects that met two conditions:
- the project later produced a verified first follow-up supply event; and
- the housing type had initial general-supply first-priority aggregate competition of at least 6x.

Of 184 eligible types, 78 (42.39%) reappeared in the first follow-up supply and 106 did not.

The final result is clearer than the earlier project-level case study:

> Initial demand depth and the housing type's share of project supply are the two most stable observable signals of first-follow-up reappearance. Financing constraints, absolute sale price, regulated-area status and relative price position do not independently explain reappearance once demand depth and supply structure are considered.

## 1. Outcome construction
Primary outcome:
- reappeared_first_followup = 1 if the identical official housing type reappeared in the project's first follow-up supply
- 0 otherwise

Initial competition:
- general-supply first priority only
- aggregate applicants by official housing type
- threshold >=6.0x
- second priority excluded
- later follow-up competition never used as initial demand

## 2. Descriptive result: demand depth
Reappearance rates:
- 6-10x: 29/47 = 61.7%
- 10-20x: 35/67 = 52.2%
- 20-50x: 9/40 = 22.5%
- 50x+: 5/30 = 16.7%

The relationship is monotonic across the main bands: deeper initial competition corresponds to lower first-follow-up reappearance.

## 3. Supply structure
Type supply share is:
type initial general supply / total project initial general supply.

By quartile, reappearance rates rise from:
- lowest quartile: 21.7%
- Q2: 39.1%
- Q3: 47.8%
- highest quartile: 60.9%

Primary model:
reappearance ~ log(initial competition) + log(type supply share) + log(project general supply) + log(initial type price) + regulated flag + capital-region flag

Project-clustered standard errors.

Results:
- competition, per doubling: OR 0.538, 95% CI 0.360-0.804, p=0.0025
- type supply share, per doubling: OR 1.249, 95% CI 1.038-1.503, p=0.0184
- project general supply, per doubling: OR 0.720, p=0.097
- initial price, per doubling: OR 0.786, p=0.459
- regulated flag: OR 0.838, p=0.769

## 4. Financing
A standardized policy-normalized equity floor was constructed from sale price, LTV proxy and the applicable capital-region / regulated-area mortgage price cap.

Unadjusted medians differ strongly:
- reappeared types: equity floor about KRW 268.6m
- non-reappeared types: about KRW 714.7m

But adjustment changes the interpretation.

Financing model:
- competition, per doubling: OR 0.536, p=0.0028
- type supply share, per doubling: OR 1.251, p=0.0106
- equity floor, per doubling: OR 0.843, p=0.3205
- capital-region flag: p=0.093

Therefore financing burden is not supported as a general independent discriminator in this risk set.

## 5. Relative price position (RPG)
The existing AptToSell 2026 RPG dataset was linked by HOUSE_MANAGE_NO + HOUSE_TY.

Coverage:
- 139/184 risk-set types
- 122 types after excluding RPG quality warnings

In the quality-focused model, RPG is not independently significant:
- OR 1.097 per +10 percentage points
- p=0.500

This means local relative price position does not replace demand depth or supply structure as the main explanation.

## 6. Robustness
The negative competition effect remains under:
- threshold >=7x
- threshold >=10x
- excluding types with initial supply <3 units
- excluding types with initial supply <5 units

Type supply-share direction is positive but becomes less precise when very small supply types are excluded.

Grouped 5-fold cross-validation by project:
- competition only AUC: 0.677
- demand + supply structure AUC: 0.714
- demand + supply structure + finance AUC: 0.749

These are predictive diagnostics, not causal validation.

## 7. Publication-safe conclusion
Recommended wording:

> In AptToSell's 2026 first-follow-up risk set, 78 of 184 housing types that had initially achieved at least 6x first-priority competition reappeared in first follow-up supply. Reappearance was substantially less common at deeper initial competition levels and more common when the housing type represented a larger share of the project's initial general supply. After project-clustered adjustment, absolute sale price, regulated-area status, standardized financing burden and relative price gap were not independently associated with reappearance. The results are observational and should not be interpreted as proof of contract cancellation causes.

## 8. What this dataset can and cannot say
Can say:
- which high-competition types reappeared
- how reappearance varies with initial demand depth and supply structure
- how finance and relative price behave after adjustment

Cannot say:
- the legal or individual reason a winner failed to contract
- an individual borrower's available loan
- a project's cancellation rate
- that DDFS equals an uncontracted-unit rate

## 9. Source basis
Initial subscription/type/price:
- Korea Real Estate Board ApplyHome public data collected for AptToSell

First follow-up supply:
- official ApplyHome follow-up notices or project-hosted official notices, retained row-wise in canonical_official_source_url

Finance-policy references:
- https://www.fsc.go.kr/po020201/85466
- https://www.fsc.go.kr/no010102/85522
- https://www.fsc.go.kr/no010101/87222

RPG:
- AptToSell 2026 type-level Relative Price Gap dataset based on pre-announcement MOLIT apartment transaction data

## 10. Reproducibility
Unit of analysis: housing type.
Risk-set rule, 6x threshold, first-follow-up outcome, and v1.0 variable definitions are frozen for reproducibility.
