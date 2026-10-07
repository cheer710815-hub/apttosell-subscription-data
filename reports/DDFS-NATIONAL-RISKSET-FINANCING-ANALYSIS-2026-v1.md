# DDFS national type-level financing analysis — 2026 v1

## Sample

- 52 projects with at least one initial first-priority aggregate type >=6x
- 184 housing types
- 78 reappeared in the first follow-up supply
- 106 did not reappear

## Policy normalization

Official Financial Services Commission rules used:
- regulated-area ordinary-borrower LTV: 40%
- non-regulated ordinary-borrower LTV: 70%
- capital-region / regulated-area home-purchase mortgage cap:
  - <= KRW 1.5bn: KRW 600m
  - > KRW 1.5bn and <= KRW 2.5bn: KRW 400m
  - > KRW 2.5bn: KRW 200m
- the 6/4/2 mortgage price cap does not apply directly to interim-payment loans

Official sources:
- https://www.fsc.go.kr/no010101/86606
- https://www.fsc.go.kr/po020201/85466
- https://www.fsc.go.kr/no010101/87222
- https://www.fsc.go.kr/no040101?cnId=2914

2026-07-01 additions:
- Hwaseong Dongtan-gu
- Yongin Giheung-gu
- Guri-si

For each row, the policy status is normalized to the project's first-follow-up timing. This is a standardized research proxy, not an individual loan quote.

## Core variables

- ltv_proxy_pct
- ltv_amount_proxy_krw
- final_mortgage_price_cap_krw
- final_mortgage_proxy_krw
- equity_floor_proxy_krw
- equity_floor_pct
- midterm_60pct_scenario_self_fund_pct
- midterm_60pct_scenario_self_fund_krw

The 60% midterm field is scenario-only and does not assert that every project had a 60% interim-payment schedule.

## Unadjusted comparison

Reappeared types (n=78):
- median initial price: KRW 854.35m
- median equity-floor proxy: KRW 268.55m
- median equity-floor share: 30%
- regulated share: 29.5%
- median initial competition: 11.47x
- median initial supply: 25 units

Non-reappeared types (n=106):
- median initial price: KRW 1.3343bn
- median equity-floor proxy: KRW 714.66m
- median equity-floor share: 60%
- regulated share: 48.1%
- median initial competition: 20.55x
- median initial supply: 10 units

Mann-Whitney:
- price p = 0.0011
- equity-floor amount p = 0.0010
- equity-floor share p = 0.0024

These crude comparisons do not establish causality because price, region, supply size and initial demand differ strongly between groups.

## Cluster-robust logistic models

Primary policy model:
reappearance ~ log(initial competition) + log(initial supply) + log(price) + regulated + capital-region

Results:
- log competition: coefficient -0.879, OR 0.415, p = 0.0018
- log supply: OR 1.210, p = 0.152
- log price: OR 0.766, p = 0.545
- regulated-area flag: OR 0.848, p = 0.794
- capital-region flag: OR 0.582, p = 0.314

Project-clustered standard errors were used.

Equity model:
reappearance ~ log(initial competition) + log(initial supply) + log(equity floor)

Results:
- log competition: OR 0.428, p = 0.0010
- log supply: OR 1.221, p = 0.091
- log equity floor: OR 0.706, p = 0.060

## Interpretation

The national risk-set does not support the claim that regulated-area status alone explains type reappearance.

The strongest and most stable signal remains initial demand depth:
- as initial competition gets deeper, reappearance probability falls.

Supply size shows a positive direction:
- larger initially supplied types are more likely to reappear,
- but in the clustered multivariable model the effect is not conventionally significant.

Financing burden:
- is strongly different in crude comparison,
- but attenuates materially after demand depth and supply size are controlled,
- leaving only borderline evidence for the equity-floor proxy.

Recommended publication language:

> Among 184 housing types that had initial first-priority competition of at least 6x, types that reappeared in first follow-up supply had lower initial competition and larger supply on average. Financing burden differed sharply in unadjusted comparisons, but regulated-area status was not independently associated with reappearance after adjustment. A higher standardized equity requirement remained directionally associated with lower reappearance probability, but the estimate was borderline in the project-clustered model.

## Limitations

- association, not causal identification
- individual DSR, income, credit, collateral appraisal and bank underwriting are not modeled
- policy proxy uses initial type price
- exact interim-payment schedules are not yet project-specific in the national file
- multi-type projects create within-project dependence; clustered standard errors partially address this
