# DDFS × price-gap linkage revalidation — 20-case matrix

## 목적

기존 84㎡ 분양가-실거래가 격차 데이터셋을 DDFS 20개 표본과 연결해 가격저항이 전체 DDFS를 설명하는지 검정한다.

Primary price-gap methodology:
- 84㎡ class
- maximum presale price
- same legal dong
- six months before announcement
- 82–86㎡ transactions
- median transaction price
- minimum 5 comparable trades for calculated research statistics

## 1. Strict all-age complete cases

Usable same-dong all-age price-gap cases: n=10.

Cases and gaps:
- 힐스테이트 평거 센트럴: DDFS 45.0%, gap +48.00%
- 더샵 안동더퍼스트: 44.3%, +40.71%
- 더샵 관저아르테: 15.2%, +49.77%
- 천안 아이파크 시티 6단지: 4.4%, +26.56%
- 래미안 엘라비네: 83.9%, +149.73%
- 드파인 아르티아: 66.7%, +77.21%
- 더샵 트리센트: 100.0%, +60.19%
- 라클라체자이드파인: 100.0%, +74.67%
- 호반써밋 풍무Ⅲ: 0.0%, +87.12%
- 쌍용 더 플래티넘 온수역: 100.0%, +25.70%

Spearman:
- rho = **0.018**
- p = **0.960**

### Interpretation

There is effectively no monotonic relationship between same-dong all-age price premium and DDFS in the available sample.

Price resistance therefore cannot be promoted to a global explanation of DDFS.

## 2. Newer-stock sensitivity

Cases with >=5 transactions in the <=10-year group: n=6.

- 힐스테이트 평거 센트럴: DDFS 45.0%, gap +37.60%
- 더샵 관저아르테: 15.2%, +25.69%
- 천안 아이파크 시티 6단지: 4.4%, +26.56%
- 더샵 트리센트: 100.0%, +40.10%
- 호반써밋 풍무Ⅲ: 0.0%, +23.98%
- 쌍용 더 플래티넘 온수역: 100.0%, +24.33%

Spearman:
- rho = **0.493**
- p = **0.321**

Direction is positive but sample size is too small and the relationship is not statistically established.

## 3. Strong counterexamples

### High price gap, low DDFS
호반써밋 풍무Ⅲ:
- all-age gap +87.12%
- <=10y gap +23.98%
- DDFS 0%

더샵 관저아르테:
- all-age +49.77%
- <=10y +25.69%
- DDFS 15.2%

### Moderate price gap, DDFS 100%
쌍용 더 플래티넘 온수역:
- all-age +25.70%
- <=10y +24.33%
- DDFS 100%

### Low/neutral adjacent-new-stock sensitivity, DDFS 100%
엘리프 성성호수공원 1BL:
- strict same-dong comparison unavailable
- adjacent 2023-built 84㎡ sensitivity median 576m KRW
- 84A max presale 588.6m KRW
- sensitivity gap +2.19%
- DDFS 100%

This is the most important price counterexample, although the comparison method differs and must remain flagged.

## 4. Updated conclusion

> **Price resistance is a real mechanism in some projects, but it is not a common cause of DDFS across the sample.**

The result reinforces the multi-path structure:

1. TYPE_STRUCTURE
2. CONTRACT_CONVERSION_GAP
3. CONTRACT_FRICTION

Price belongs inside the contract-friction path, not above the entire model as a single universal cause.

## 5. Variable status after revalidation

- Demand Breadth alone: rejected
- Deposit percentage alone: rejected
- Time to first midterm alone: rejected
- Time to move-in alone: rejected
- Price gap alone: rejected as global explanation
- Mandatory self-funded midterm burden: strongest current exploratory friction signal, but not necessary and not yet 5% significant

## 6. Strongest clean conversion-gap candidate

엘리프 성성호수공원 1BL is currently the strongest candidate because:
- DDFS 100%
- high first-priority competition
- broad application evidence does not explain attrition
- 60% midterm loan coverage
- 0% mandatory self-funded midterm under current coding
- no obvious timing-friction signal
- no strong price premium in adjacent-new-stock sensitivity

This does not identify the hidden micro-cause (ineligibility, contract abandonment, reserve-list attrition, overlapping wins, financing re-evaluation, etc.). It supports only the higher-level claim that application volume did not fully convert into contractable demand.

## Next step

The highest-value next test is to split the 20 observations into path labels using explicit rules and then perform leave-one-out stability on the classification:
- TYPE_STRUCTURE
- CONTRACT_FRICTION
- CONVERSION_GAP
- MIXED

This avoids forcing one global causal coefficient onto a visibly heterogeneous process.
