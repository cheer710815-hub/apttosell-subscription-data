# DDFS National Type Risk-set 2026 — v1.0 release notes

## Release scope
This release freezes the 2026 national type-level risk set for first follow-up supply.

- 103 projects with a first follow-up event in the registry
- 52 projects with at least one initial first-priority aggregate housing type >=6x
- 184 eligible housing types
- 78 types reappeared in first follow-up supply
- 106 types did not reappear
- type-level reappearance rate: 42.39%

## Major audit corrections incorporated
The release supersedes earlier hand-audited intermediate files where type matching or denominator use was incomplete.

Examples corrected during QA:
- e편한세상 부천 어반스퀘어: strict 6x audit changed DDFS 9.3% -> 0%
- 천안 아이파크 시티 5단지: 6.29% -> 28.44%
- 천안 아이파크 시티 6단지: 4.4% -> 15.32%
- 북오산자이 리버블시티: 1.11% -> 0%
- 안양역 센트럴 아이파크 수자인: 0% -> 25.0%
- 두산위브 더센트럴 수원: 72% -> 100%

## Frozen eligibility rule
A housing type enters the risk set only when:
1. it belongs to a project with a verified first follow-up supply event;
2. initial general-supply first-priority aggregate competition is >=6.0x;
3. second priority is excluded;
4. later follow-up competition is never substituted for initial competition.

Outcome:
- reappeared_first_followup = 1 when the identical official housing type appears in the first follow-up supply;
- otherwise 0.

## Primary findings
Reappearance rate by initial competition:
- 6-10x: 61.7%
- 10-20x: 52.2%
- 20-50x: 22.5%
- 50x+: 16.7%

Primary project-clustered logistic model:
- doubling initial competition: OR 0.538, 95% CI 0.360-0.804, p=0.0025
- doubling type supply share: OR 1.249, 95% CI 1.038-1.503, p=0.0184
- initial type price: not independently significant
- regulated-area flag: not independently significant

Financing model:
- standardized equity-floor proxy is not independently significant after adjustment (OR 0.843 per doubling, p=0.3205)

RPG sensitivity:
- type-level relative price gap is not independently significant in the quality-focused sample.

## Interpretation
The strongest stable finding is not that "high competition still fails."

Rather:
> Within housing types that already achieved at least 6x initial first-priority competition, deeper initial demand materially reduces the probability that the same type reappears in first follow-up supply, while a larger share of the project's general supply allocated to that type raises reappearance risk.

This is consistent with a conversion-capacity interpretation: a large type can require many completed contracts even when its application ratio looks healthy.

## Finance-policy normalization
Official Financial Services Commission guidance used in the finance proxy:
- regulated-area ordinary-borrower LTV 40%
- non-regulated ordinary-borrower LTV 70%
- capital-region / regulated-area home-purchase mortgage cap: <=1.5bn KRW 600m, 1.5-2.5bn 400m, >2.5bn 200m
- price-tier 6/4/2 cap does not directly apply to interim-payment loans
- regulated-area LTV tightening does apply to interim-payment loans

Official references:
- https://www.fsc.go.kr/po020201/85466
- https://www.fsc.go.kr/no010102/85522
- https://www.fsc.go.kr/no010101/87222

## Limitations
- observational association, not causal identification
- individual DSR, income, credit, collateral appraisal and bank underwriting are not modeled
- policy-normalized equity floor is a standardized proxy, not an individual loan quote
- project-level clustering addresses within-project dependence but does not remove all omitted-variable bias
- first follow-up only; later follow-up events are outside the primary outcome

## Versioning
v1.0 is frozen. Future corrections must be released as v1.1+ with explicit change notes rather than silently overwriting the methodology.
