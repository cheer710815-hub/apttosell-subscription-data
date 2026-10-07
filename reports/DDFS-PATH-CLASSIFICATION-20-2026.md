# DDFS 20-case explicit path classification — 2026

## 1. Classification rules

### TYPE_STRUCTURE
Use when the observed follow-up supply is mainly explained by weaker types rather than reappearance of strongly oversubscribed types.

Operational evidence:
- DDFS near zero, or
- no 6x type reappears, or
- unsold/follow-up units are concentrated in clearly lower-competition types.

### CONVERSION_GAP
Use when:
- competitive application demand is established,
- DDFS is material,
- no strong contract-friction signal is established.

Strong friction means one or more of:
- mandatory self-funded midterm >=20%
- post-completion / short-balance structure
- clearly high price resistance
- unusually concentrated up-front cash burden

### CONTRACT_FRICTION
Use when contract-stage burden is the dominant observable mechanism and conversion-gap evidence is weaker or DDFS is not extremely high.

### MIXED
Use when:
- DDFS is high,
- and at least one strong contract-friction signal is present,
- while competitive application demand is also clearly established.

These are descriptive path labels, not causal proof.

---

## 2. Classification result

| Path | Cases |
|---|---:|
| TYPE_STRUCTURE | 5 |
| CONVERSION_GAP | 5 |
| CONTRACT_FRICTION | 4 |
| MIXED | 6 |

### TYPE_STRUCTURE
- 천안 아이파크 시티 6단지
- 호반써밋 풍무Ⅲ
- e편한세상 센텀 하이베뉴
- 포레나더샵 인천시청역
- 엘리프 성성호수공원 2BL

### CONVERSION_GAP
- 엘리프 성성호수공원 1BL
- 아산탕정자이 메트로시티(A3BL)
- 힐스테이트 평거 센트럴
- 더샵 안동더퍼스트
- 청주 푸르지오 씨엘리체

### CONTRACT_FRICTION
- 해링턴플레이스 노원 센트럴
- 더샵 관저아르테
- e편한세상 부천 어반스퀘어
- 힐스테이트 안양펠루스

### MIXED
- 두산위브 더센트럴 수원
- 래미안 엘라비네
- 드파인 아르티아
- 더샵 트리센트
- 라클라체자이드파인
- 쌍용 더 플래티넘 온수역

---

## 3. Why the four-path structure fits better than one global cause

The same DDFS level can arise under very different observable conditions.

Examples:

- DDFS 100% + low/neutral price friction + 60% loan coverage:
  - 엘리프 성성호수공원 1BL
  - CONVERSION_GAP

- DDFS 100% + clear price friction:
  - 더샵 트리센트
  - 쌍용 더 플래티넘 온수역
  - MIXED

- DDFS 100% + post-completion / short-balance burden:
  - 해링턴플레이스 노원 센트럴
  - CONTRACT_FRICTION

- DDFS 0% despite large price premium:
  - 호반써밋 풍무Ⅲ
  - TYPE_STRUCTURE

A single-price, single-deposit or single-timing explanation cannot generate all four patterns.

---

## 4. Stability checks

### A. DDFS high threshold sensitivity

Base MIXED rule uses high DDFS plus strong friction.

When the high-DDFS boundary is changed from 50% to 40% or 60%:
- the six core MIXED cases remain MIXED
- no TYPE_STRUCTURE case moves into MIXED
- 엘리프 성성호수공원 1BL remains CONVERSION_GAP because strong friction is absent
- 해링턴 노원 remains CONTRACT_FRICTION because post-completion burden dominates

Therefore the core high-DDFS path split is not driven by one arbitrary DDFS cutoff.

### B. Price-friction threshold sensitivity

For matched projects, changing a descriptive “high price friction” boundary across roughly +20%, +25%, +30% affects only borderline price labels.

Stable:
- 더샵 트리센트 remains high-friction under all three
- 라클라체자이드파인 remains high-friction
- 래미안 엘라비네 remains high-friction
- 드파인 아르티아 remains high-friction
- 호반써밋 풍무Ⅲ remains a price-friction case but TYPE_STRUCTURE because DDFS is 0

Borderline:
- 쌍용 더 플래티넘 온수역 is sensitive around the 25% line, but stays at least MIXED/CONVERSION-GAP rather than TYPE_STRUCTURE
- 천안 아이파크 시티 6단지 is price-gap positive but remains TYPE_STRUCTURE because DDFS is only 4.4%

### C. Leave-one-out structural stability

Removing any one of the 20 observations does not eliminate any of the four path categories.

Minimum remaining category counts after any single omission:
- TYPE_STRUCTURE >=4
- CONVERSION_GAP >=4
- CONTRACT_FRICTION >=3
- MIXED >=5

Thus the existence of the four-path structure does not depend on one single project.

Important:
This is a structural leave-one-out check, not a fitted-model cross-validation score.

---

## 5. Confidence

### High confidence labels
Cases with direct type mapping, explicit contract structure or clear price evidence.

### Medium confidence
Cases where the path is plausible but one major variable remains incomplete.

### Low confidence
Cases with weak DDFS or incomplete price/contract evidence.

The purpose of confidence is to prevent the label from looking more certain than the underlying public data.

---

## 6. Strongest representatives

### TYPE_STRUCTURE
호반써밋 풍무Ⅲ
- DDFS 0%
- follow-up supply concentrated in lower-competition 84B/84D

### CONVERSION_GAP
엘리프 성성호수공원 1BL
- DDFS 100%
- 60% midterm loan coverage
- no mandatory self-funded midterm
- no strong price premium in adjacent-new-stock sensitivity

### CONTRACT_FRICTION
해링턴플레이스 노원 센트럴
- DDFS 100%
- post-completion / short-balance structure
- 10% deposit
- price-resistance evidence

### MIXED
라클라체자이드파인
- DDFS 100%
- all major types highly competitive
- mandatory 20% self-funded midterm
- strong price resistance

---

## 7. Main conclusion

> The 20-case evidence is best described as a heterogeneous multi-path process rather than a single-factor mechanism.

Observed paths:
1. TYPE_STRUCTURE
2. CONVERSION_GAP
3. CONTRACT_FRICTION
4. MIXED

The four categories remain present after leave-one-out removal and are not erased by reasonable changes to the high-DDFS or price-friction thresholds.

This supports using path classification, rather than a single global coefficient, as the main explanatory framework for the current sample.

## 8. Next test

The highest-value next step is not to add more variables to these same 20 cases.

Instead, apply the rule set prospectively to a new holdout sample of DDFS projects not used to build the classification.

Recommended:
- select 10 additional projects
- calculate the required variables without changing the rules
- assign path labels blind to desired outcome
- compare path frequencies and counterexamples

This is the cleanest way to test whether the current four-path structure generalizes.
