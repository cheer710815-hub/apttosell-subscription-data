# DDFS type-level nearest-neighbor matching — 2026

## 목적

프로젝트 평균이 아니라 최초 1순위 aggregate 경쟁률이 6x 이상인 주택형 단위에서,
재등장하지 않은 control 타입과 실제 첫 후속공급에 재등장한 high-DDFS case 타입을 직접 비교한다.

## 매칭

매칭 변수:
- log(initial aggregate first-priority rate)
- log(initial type max presale price)

두 변수를 pooled sample에서 표준화한 뒤 Euclidean nearest-neighbor distance를 사용했다.

Control:
- DDFS=0 프로젝트의 최초 6x 이상 비재등장 타입
- 북오산 127P
- 호반써밋 풍무III 59A/59B/84A
- 도안자이 센텀리체 2단지 134
- 한화포레나 부산당리 115

Case:
- DDFS>=50 프로젝트에서 실제 첫 후속공급에 재등장한 최초 6x 이상 타입

## 결과

6개 matched pairs 중 5개에서 case의 policy-normalized equity floor가 control보다 높았다.

Equity gap (case - control):
- median: 약 +2.393억원
- mean: 약 +3.674억원

Paired Wilcoxon:
- p = 0.0625

Binomial sign test:
- 5/6 positive
- two-sided p = 0.21875

## 가장 좋은 common-support pair

호반써밋 풍무III 84A vs 엘리프 성성호수공원 1BL 111:
- competition: 11.96x vs 13.68x
- price: 7.625억 vs 7.994억
- price difference: 약 4.8%
- control initial supply: 57
- case initial supply: 244
- equity floor: 2.2875억 vs 2.3982억

가격과 경쟁률은 매우 비슷하지만 결과가 반대다.
따라서 금융부담만으로는 재등장을 설명하지 못하며, 타입 공급규모와 계약전환 구조가 추가 후보가 된다.

## 또 다른 유용한 pair

도안자이 센텀리체 2단지 134 vs 라클라체자이드파인 59B:
- competition: 30.0x vs 42.4x
- price: 21.699억 vs 21.899억
- price difference: 약 0.9%
- initial supply: 2 vs 5
- equity floor: 6.5097억 vs 17.899억

가격이 거의 같은데 equity floor 차이가 큰 이유는 규제지역/잔금대출 상한 차이다.
이는 금융규제가 같은 가격대에서도 계약 유지에 필요한 자기자금을 크게 바꿀 수 있음을 보여주는 사례다.

## 한계

- control 타입이 6개뿐이다.
- 일부 nearest-neighbor pair는 가격 차이가 20~32%로 common support가 약하다.
- case는 개발표본의 high-DDFS 사례에서 왔으므로 선택편향이 있다.
- 이 분석은 인과효과 추정이 아니다.

## 해석

현재 자료가 지지하는 가장 안전한 표현:

> 비슷한 초기 경쟁률과 가격대를 가진 주택형끼리 비교했을 때, 재등장한 high-DDFS 타입은 재등장하지 않은 타입보다 더 높은 정책정규화 자기자금 부담을 보이는 방향성이 있었으나, 작은 표본에서는 통계적으로 확정적이지 않았다.

## 다음 단계

전국 2026 후속공급 레지스트리에서:
1. 최초 6x 이상 타입이 존재하는 모든 프로젝트 추출
2. 각 6x 타입의 first-followup reappearance binary 생성
3. 타입별 price / supply / region / LTV / equity floor 생성
4. 재등장 vs 비재등장을 type-level logistic/Firth model로 비교

이 단계가 완료되면 개발표본 선택편향에서 벗어날 수 있다.
