# DDFS prospective holdout-2 results — locked 20-project cohort

## Frozen rule

DDFS numerator:
first-followup supply units belonging to a housing type whose **initial general-supply first-priority aggregate type competition rate** was >=6.0x.

Important methodological clarification:
- use type-level first-priority applications across the applicable first-priority regions divided by the type's first-priority supply denominator;
- do not use a later regional residual competition rate as if it were a whole-type 6x rate;
- do not use 2nd-priority rates;
- do not use competition from the first unsold round.

This clarification was necessary because some public pages display a very high "other-region" rate against only the remaining units after local-region allocation. That rate is not equivalent to the aggregate type-level 1st-priority rate used in the DDFS series.

## Results

| Project | First unsold | From initial >=6x types | DDFS |
|---|---:|---:|---:|
| 북오산자이 리버블시티 | 90 | 1 | 1.11% |
| 사우역 지엔하임 | 3 | 0 | 0.00% |
| 서귀포시 서홍동 형남아파트6차 | 45 | 0 | 0.00% |
| 안양역 센트럴 아이파크 수자인 | 28 | 0 | 0.00% |
| 금정산 하늘채 루미엘 | 30 | 0 | 0.00% |
| 상주자이르네 | 257 | 0 | 0.00% |
| e편한세상 여수 글렌츠 | 51 | 0 | 0.00% |
| 부천역 에피트 어바닉 | 62 | 4 | 6.45% |
| 용인 플랫폼시티 라온프라이빗 아르디에 | 98 | 0 | 0.00% |
| 연수 월드메르디앙 어반포레 | 18 | 0 | 0.00% |
| 한화포레나 부산당리 | 6 | 0 | 0.00% |
| 경성대부경대역 비스타동원 더 프리미엄 | 24 | 0 | 0.00% |
| 엄궁역 트라비스 하늘채 | 272 | 0 | 0.00% |
| 르네오션 고성 퍼스트뷰 | 63 | 0 | 0.00% |
| 북전주 광신프로그레스 | 298 | 0 | 0.00% |
| 업성 푸르지오 레이크시티 | 364 | 8 | 2.20% |
| 중앙하이츠 갈산역 센트럴 | 45 | 0 | 0.00% |
| 야목역 서희스타힐스 그랜드힐 | 8 | 0 | 0.00% |
| 도안자이 센텀리체 1단지 | 660 | 0 | 0.00% |
| 문수로 라티에르 673 | 12 | 0 | 0.00% |

## Distribution

- DDFS = 0%: **17 / 20 projects**
- DDFS >0%: **3 / 20**
- DDFS >=10%: **0 / 20**
- DDFS >=50%: **0 / 20**
- median: **0%**
- maximum: **6.45%**

Non-zero cases:
1. 부천역 에피트 어바닉 — 6.45%
2. 업성 푸르지오 레이크시티 — 2.20%
3. 북오산자이 리버블시티 — 1.11%

## Key case checks

### 북오산자이 리버블시티
Initial:
- 126P: 12 first-priority applications / 2 units = 6.0x
- 127P: 7 / 1 = 7.0x

First unsold:
- 59B 89
- 126P 1
- 127P absent

DDFS = 1 / 90 = 1.11%.

### 안양역 센트럴 아이파크 수자인
Initial high-demand types include 59A, 59B and 84A.
The first unsold round contains only 39A, 43A and 43B.
Therefore DDFS = 0 / 28 = 0%.

### 부천역 에피트 어바닉
Initial:
- 67 type: 9 first-priority applications / 1 general-supply unit = 9.0x

First unsold:
- 67 type 4 units

DDFS = 4 / 62 = 6.45%.

### 용인 플랫폼시티 라온프라이빗 아르디에
A public page displays 84B "10.67x" for the other-region stage, but this is a residual-stage rate after local-region shortfall.
Under the frozen aggregate type-level rule, the type does not reach 6x.
DDFS = 0%.

### 한화포레나 부산당리
Initial:
- 115 type = 6.0x

First unsold:
- 6 units, all 101 type

DDFS = 0%.

### 업성 푸르지오 레이크시티
Initial:
- 84B = 529 / 48 = 11.0x

First unsold:
- 84A 127
- 84B 8
- 95A 188
- 95B 41

Only 84B qualifies under the 6x rule.
DDFS = 8 / 364 = 2.20%.

## Holdout implication

The mechanically selected second holdout is even more strongly concentrated at DDFS=0 than holdout-1.

This materially weakens any attempt to describe high-DDFS behavior as common among follow-up-supply projects.

Instead, the current evidence suggests:
- high DDFS is a **special subset**, not the modal pattern;
- most follow-up supply comes from types that were not deeply oversubscribed at the initial 1st-priority stage;
- the original high-DDFS 20-case analysis is useful for explaining the mechanisms **conditional on high DDFS**, but should not be read as a population-frequency sample.

## Generalization status

Original 20-case analysis:
- intentionally enriched with DDFS variation, including many high-DDFS cases.

Holdout-1:
- 10 projects
- dominated by TYPE_STRUCTURE
- maximum DDFS 45.48%

Holdout-2:
- 20 chronologically selected projects
- 17/20 at DDFS 0%
- maximum DDFS 6.45%

Therefore:

> The multi-path model remains useful as a taxonomy of high-DDFS mechanisms, but high-DDFS itself appears uncommon in a mechanically selected follow-up cohort.

## Next test

The next high-value step is to quantify **selection enrichment**:
compare the DDFS distribution of:
1. original 20-case development sample,
2. holdout-1,
3. chronological holdout-2.

Report:
- zero share
- median
- mean
- >=50% share
- 100% share

Then explicitly reframe the project from "what causes follow-up supply?" to:
"What distinguishes the rare cases where strongly oversubscribed types themselves reappear in follow-up supply?"
