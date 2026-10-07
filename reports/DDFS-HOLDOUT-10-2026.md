# DDFS holdout validation — 10 new projects (2026)

## Purpose

Apply the frozen 6x DDFS and four-path rules to 10 projects that were not part of the 20-case path-classification set.

Important:
The old A/D cause labels are not reused.
Initial subscription results and first unsold type allocations were re-separated before DDFS calculation.

## Holdout projects

1. 창원자이 더 스카이
2. 김해 신문 센트럴 아이파크
3. 천안 아이파크 시티 5단지
4. 도안자이 센텀리체 2단지
5. 구리역 하이니티 리버파크
6. 힐스테이트 양산더스카이 1단지
7. 검암역자이르네
8. 더 리치먼드 미아
9. 의정부역 센트럴 아이파크
10. 백석시그니처자이 2단지

## Recalculated DDFS

| Project | First unsold | From initial >=6x types | DDFS |
|---|---:|---:|---:|
| 창원자이 더 스카이 | 431 | 196 | 45.48% |
| 김해 신문 센트럴 아이파크 | 865 | 0 | 0.00% |
| 천안 아이파크 시티 5단지 | 334 | 21 | 6.29% |
| 도안자이 센텀리체 2단지 | 657 | 0 | 0.00% |
| 구리역 하이니티 리버파크 | 341 | 0 | 0.00% |
| 힐스테이트 양산더스카이 1단지 | 239 | 56 | 23.43% |
| 검암역자이르네 | 150 | 0 | 0.00% |
| 더 리치먼드 미아 | 98 | 14 | 14.29% |
| 의정부역 센트럴 아이파크 | 141 | 0 | 0.00% |
| 백석시그니처자이 2단지 | 261 | 0 | 0.00% |

Median DDFS = 0.00%.

Only one holdout case is above 40% DDFS:
- 창원자이 더 스카이 45.48%

No holdout case exceeds 50%.

## Frozen-rule path assignment

### CONTRACT_FRICTION
창원자이 더 스카이
- initial 84A 10.04x
- 196 units of 84A reappeared
- DDFS 45.48%
- strong price-burden evidence
- later contract terms were eased from the initial structure

### TYPE_STRUCTURE
- 김해 신문 센트럴 아이파크
- 천안 아이파크 시티 5단지
- 도안자이 센텀리체 2단지
- 구리역 하이니티 리버파크
- 힐스테이트 양산더스카이 1단지
- 검암역자이르네
- 더 리치먼드 미아
- 의정부역 센트럴 아이파크
- 백석시그니처자이 2단지

No new holdout project is classified as:
- CONVERSION_GAP
- MIXED

## Key finding

The four paths are **not evenly reproduced** in this holdout.

Path counts:
- TYPE_STRUCTURE: 9
- CONTRACT_FRICTION: 1
- CONVERSION_GAP: 0
- MIXED: 0

This means the first 10-project holdout does **not** validate the claim that all four paths will appear in every new sample.

It does support a different, important conclusion:

> The DDFS 6x stress-test classification is substantially stricter than the earlier A/D cause classification. Many projects previously described as contract-conversion weakness do not show reappearance of >=6x types and therefore collapse into TYPE_STRUCTURE under DDFS.

## Audit correction

During holdout verification, a source-mixing risk was detected in earlier cause-classification work.

Example:
- 구리역 하이니티 리버파크 values 59A 8.21x and 59B 10x correspond to the first unsold round, not the initial 1st-priority round.
- Initial 1st-priority rates were much lower and all below 6x.

Therefore:
- DDFS calculations must never reuse competition figures from a later unsold notice.
- Initial subscription and first-unsold stages must be keyed separately by announcement ID/date.

This correction should be applied to future holdout construction.

## Interpretation

The holdout does not falsify the existence of CONVERSION_GAP or MIXED paths in the original 20 cases, because those paths were directly observed there.

However it does show that:
1. those paths may be relatively uncommon,
2. sample composition matters strongly,
3. the old A/D labels cannot be used as proxies for DDFS path labels,
4. a larger and prospectively selected holdout is required before claiming generalization of the four-path frequency structure.

## Recommended next validation

Build a second holdout that is selected mechanically rather than from prior A/D labels:
- next 20 chronological projects with a first unsold event,
- exclude the original 20 and current holdout 10,
- calculate DDFS before reviewing contract or price variables,
- then apply the frozen path rules.

This avoids outcome-aware sampling and is the cleanest prospective test.

## Current status

The strongest publishable conclusion remains:

> High application competition followed by unsold reappearance is heterogeneous. In the original 20 cases multiple paths were observed, but a new 10-case holdout was dominated by TYPE_STRUCTURE and did not reproduce all four paths. Therefore the four-path framework should be treated as an explanatory taxonomy, not yet as a validated population-frequency model.
