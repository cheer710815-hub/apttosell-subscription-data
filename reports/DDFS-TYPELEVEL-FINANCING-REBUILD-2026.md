# DDFS type-level financing rebuild — 2026

## 목적
DDFS 분자에 실제로 들어간 재등장 고경쟁 주택형을 한 행 단위로 만들고, 그 주택형의 가격과 금융규제를 연결한다.

## 핵심 원칙
- 6x 판정은 최초 일반공급 1순위 aggregate type-level rate를 사용한다.
- 동일 주택형의 해당지역/기타지역 REQ_CNT는 합산한다.
- 공급세대수는 주택형별 일반공급 분모를 1회만 사용한다.
- 첫 후속공급 경쟁률을 최초 경쟁률로 사용하지 않는다.
- 금융부담은 가능하면 첫 후속공급 실제 타입 최고가를 사용한다.
- 첫 후속공급 가격을 아직 단위별로 검증하지 못한 행은 최초 타입 최고가를 proxy로 사용하고 status 필드로 구분한다.

## 6x 재감사 정정
e편한세상 부천 어반스퀘어 84A는:
- 일반공급 34세대
- 최초 1순위 접수 176건
- aggregate rate 5.1765x

따라서 기존 6.53x 판정은 폐기하고 DDFS를 9.3%에서 0%로 수정했다.

## 현재 행 수
DDFS 분자에 들어가는 재등장 타입 27개 행.

## 가격 필드
- initial_type_max_price_krw: 최초 공고 타입 최고 공급금액
- first_followup_type_max_price_krw: 첫 후속공급 해당 타입 최고 공급금액이 별도 확인된 경우
- financing_price_basis_krw: 금융부담 계산에 실제 사용한 가격

첫 후속공급 가격을 별도 확인한 핵심 사례:
- 더샵 트리센트 75형: 7.43억원
- 더샵 트리센트 84형: 8.49억원
- 라클라체자이드파인 59B: 20.476억원
- 라클라체자이드파인 84A: 25.851억원
- 쌍용 더 플래티넘 온수역 84B: 11.376억원

## 금융규제
- 규제지역: LTV40
- 비규제지역: 일반 LTV70 proxy
- 수도권·규제지역 잔금단계 주택구입목적 주담대 가격상한: 15억 이하 6억 / 15억 초과 25억 이하 4억 / 25억 초과 2억
- 가격상한은 중도금대출에는 직접 적용하지 않고 잔금대출 전환 단계에 반영

## 계산
policy_midterm_self_fund =
max(0, midterm_schedule - LTV) × financing price basis

final_mortgage_proxy =
min(LTV amount, applicable final mortgage cap)

equity_floor_proxy =
financing price basis - final_mortgage_proxy

## 해석 주의
이 파일의 equity_floor_proxy는 개인별 대출승인액이 아니다.
DSR, 소득, 신용, 기존대출, 보유주택, 담보평가액, 은행심사에 따라 실제 대출은 더 적을 수 있다.

## 연구상 가치
이 데이터는 단지 평균가격이 아니라 '실제로 고경쟁 후 재등장한 타입'의 금융부담을 보여준다.
따라서 고가 대형타입이나 펜트하우스가 단지 평균을 왜곡하는 문제를 크게 줄인다.

## 다음 QA
1. INITIAL_TYPE_MAX_PROXY 행의 첫 후속공급 동·호수별 실제 공급금액 검증
2. 계약 및 첫 중도금 시점별 규제 적용일 검증
3. first_followup_notice_id 추가
4. individual-unit price range가 있는 경우 min/max/equity range로 확장
5. corrected DDFS를 모든 파생 보고서에 전파
