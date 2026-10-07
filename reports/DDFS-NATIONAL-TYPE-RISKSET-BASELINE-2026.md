# 2026 National DDFS Type-Level Risk-Set Baseline

## Scope

This analysis uses all first-follow-up projects in the frozen 2026 registry for which the initial general-supply first-priority aggregate housing-type competition reached at least 6.0x.

- first-follow-up projects in registry: 103
- projects with at least one initial >=6x housing type: 52
- housing types in national risk set: 184
- reappeared in first follow-up: 78
- did not reappear: 106
- type-level reappearance rate: **42.39%**

Outcome:
`reappeared_first_followup = 1` if the same housing type appears in the project's first follow-up supply, otherwise 0.

This is a type-level reappearance analysis, not a project DDFS percentage.

## Descriptive result: initial competition depth

Reappearance rate by initial aggregate first-priority competition:

- 6 to <10x: **61.7%** (29/47)
- 10 to <20x: **52.2%** (35/67)
- 20 to <50x: **22.5%** (9/40)
- 50x or more: **16.7%** (5/30)

Within the >=6x risk set, deeper initial application competition is associated with a lower probability that the same type reappears.

Mann-Whitney comparison of initial competition:
- median reappeared type: about **11.47x**
- median non-reappeared type: about **20.55x**
- p ≈ **4.27e-06**

## Initial supply size

Median initial general-supply count:
- reappeared: **25**
- non-reappeared: **10**
- Mann-Whitney p ≈ **0.00054**

Reappearance rate by supply-size quartile:
- smallest quartile: **27.1%**
- Q2: **38.6%**
- Q3: **47.8%**
- largest quartile: **56.5%**

This suggests that absolute type-level supply volume is an important candidate mechanism.

## Sale price

Unadjusted median initial type price:
- reappeared: about **8.54억원**
- non-reappeared: about **13.34억원**
- Mann-Whitney p ≈ **0.0011**

However, the price signal attenuates after accounting for competition depth, supply size, and broad region.

## Region

Type-level reappearance:
- Seoul: **26.2%** (17/65)
- Gyeonggi/Incheon: **44.8%** (26/58)
- non-capital regions: **57.4%** (35/61)

These are descriptive frequencies, not causal regional effects.

## Cluster-robust logistic model

Specification:

`reappeared ~ log(initial_competition) + log(initial_supply) + log(initial_price) + days_to_first_followup + broad_region`

Standard errors clustered by project.

### Competition depth
For a doubling of initial competition:
- OR ≈ **0.55**
- 95% CI ≈ **0.37 to 0.82**
- p ≈ **0.0037**

Interpretation:
among housing types that already cleared the 6x threshold, doubling initial competition was associated with roughly 45% lower odds of the same type reappearing in first follow-up supply.

### Initial supply
For a doubling of initial general-supply count:
- OR ≈ **1.16**
- 95% CI ≈ **0.97 to 1.39**
- p ≈ **0.097**

Direction is positive but not conventionally significant.

### Initial price
For a doubling of initial type price:
- OR ≈ **1.02**
- p ≈ **0.958**

No independent signal after the above controls.

### Time to first follow-up
For an additional 30 days:
- OR ≈ **0.78**
- p ≈ **0.551**

No statistically clear signal in this baseline model.

## Most important conceptual change

The national type-level data do not support the simple story:

> “The higher the initial competition, the more surprising and unexplained a later reappearance is.”

Instead, within the >=6x risk set, the most intensely oversubscribed types were **less** likely to reappear.

A more useful research question is:

> Among types that already demonstrated meaningful initial demand, how do demand depth, absolute supply volume, financing conditions and product structure jointly determine whether enough contract conversion fails for the same type to re-enter follow-up supply?

## Current interpretation

Three findings are worth carrying forward:

1. **Competition depth is protective.**
   Very high initial competition is associated with lower reappearance probability.

2. **Supply volume matters.**
   Larger high-competition types reappear more often in raw data, consistent with a larger absolute number of contracts being needed to clear inventory.

3. **Price alone is not enough.**
   The unadjusted price difference largely disappears after demand depth, supply and region are considered.

## Next step

Add policy-normalized financing variables to all 184 types:
- regulation status at relevant financing date
- applicable LTV
- policy-implied interim self-funding amount
- final mortgage cap
- equity-floor proxy

Then estimate:
1. baseline demand/supply model
2. financing-only model
3. combined model
4. interaction tests: supply × competition, financing × region, price × financing regime

All results remain associational; no causal claim should be made from this observational dataset.
