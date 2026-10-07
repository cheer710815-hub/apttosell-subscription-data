# DDFS self-funded midterm complete-case revalidation (n=18)

## Scope
Ordinary presale projects with numeric midterm loan coverage verified from the initial offering notice or official project materials.

## Groups

### Mandatory self-funded midterm 20% (n=4)
- 두산위브 더센트럴 수원 — DDFS 72.0%
- 래미안 엘라비네 — 83.9%
- 드파인 아르티아 — 66.7%
- 라클라체자이드파인 — 100.0%

### Mandatory self-funded midterm 0% (n=14)
- 더샵 트리센트 — 100.0%
- 쌍용 더 플래티넘 온수역 — 100.0%
- 호반써밋 풍무Ⅲ — 0.0%
- e편한세상 센텀 하이베뉴 — 0.0%
- 엘리프 성성호수공원 2BL — 0.0%
- 더샵 관저아르테 — 15.2%
- e편한세상 부천 어반스퀘어 — 9.3%
- 힐스테이트 평거 센트럴 — 45.0%
- 포레나더샵 인천시청역 — 0.0%
- 엘리프 성성호수공원 1BL — 100.0%
- 아산탕정자이 메트로시티(A3BL) — 63.4%
- 더샵 안동더퍼스트 — 44.3%
- 청주 푸르지오 씨엘리체 — 17.4%
- 천안 아이파크 시티 6단지 — 4.4%

## Results
- 20% self-funded group median DDFS: 77.95%
- 20% self-funded group mean DDFS: 80.65%
- 0% self-funded group median DDFS: 16.30%
- 0% self-funded group mean DDFS: 35.64%
- Spearman rho = 0.455
- Spearman p = 0.0575
- Mann–Whitney U = 45.5
- asymptotic two-sided p = 0.0681

## Interpretation
The signal strengthened relative to the earlier deposit-percentage test and remains close to conventional significance, but it still does not cross the 5% threshold. Therefore this remains an exploratory association, not a causal result.

The contrast with the deposit-percentage test is material:
- contract deposit percentage: rho 0.197, p 0.405
- mandatory self-funded midterm burden: rho 0.455, p 0.0575

This supports keeping mandatory self-funded midterm burden as a primary contract-friction variable.

## Critical counterexamples
A 20% self-funded midterm is not necessary for high DDFS:
- 더샵 트리센트 — 0% self-funded, DDFS 100%
- 쌍용 더 플래티넘 온수역 — 0% self-funded, DDFS 100%
- 엘리프 성성호수공원 1BL — 0% self-funded, DDFS 100%

Therefore the result is compatible with a multi-path model rather than a single-cause model.

## Leave-one-out sensitivity
Leaving out one project at a time:
- Spearman rho range: 0.381 to 0.543
- p-value range: 0.024 to 0.131

The association direction stays positive in every leave-one-out run, but statistical significance is sensitive to individual cases. This is consistent with a real exploratory signal in a still-small sample, not a robust final estimate.

## Updated model
The evidence currently supports:
1. Type-structure path
2. Contract-conversion gap path
3. Contract-friction path

The contract-friction path should be represented by a vector, not by deposit percentage alone:
- deposit timing
- mandatory self-funded midterm percentage
- actual loan coverage
- interest structure
- time to first midterm payment
- post-completion / short-balance structure
- price resistance

## Next step
The next highest-value test is timing friction:
- days from contract to first midterm payment
- months from contract to expected move-in

These variables can separate projects with the same 60% loan coverage but very different cash-flow timing.
