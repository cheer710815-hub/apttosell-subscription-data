# DataON 등록 메타데이터 초안 (아직 제출·승인되지 않음)

- 제목: 2026년 신규 아파트 동일 단지 주택형별 분양가격과 1순위 청약수요 비교 데이터
- English title: Within-Project Apartment Unit Price and First-Priority Application-to-Supply Ratio, South Korea, 2026
- 제작·검증일: 2026-10-09
- 자료 제공: AptToSell Research
- 원본 출처: 한국부동산원 청약홈 분양정보 조회 서비스, 청약접수 경쟁률 및 특별공급 신청현황 조회 서비스
- 출처 링크: https://www.data.go.kr/data/15098547/openapi.do ; https://www.data.go.kr/data/15098905/openapi.do
- 표본: 140개 최초 모집공고 아파트, 898개 주택형; 비교 205그룹
- 관측 결과: 고가 타입 수요비율 우세 145, 저가 타입 우세 56, 동률 4. 비동률 기준 145/201 = 72.14%
- 자료 구성: comparison_205_pairs.csv, reconciliation_898_types.csv, summary.csv, CODEBOOK.md, METHODOLOGY.md, README.md, CITATION.cff
- 키워드: 아파트 분양가, 청약 수요, 주택형, 1순위 청약, 부동산 데이터, 한국부동산원
- English keywords: apartment presale, application-to-supply ratio, housing subscription, type-level comparison, Korea
- 설명: 동일 단지 내 유사 전용면적 주택형 간 공고 최고 분양가격(㎡당)과 1순위 신청자/경쟁률 API 공급량의 비율을 비교한 관측 파생 데이터셋. 205개 비교그룹의 양 끝 가격 타입을 비교하며, 주택형 898개를 공식 API 필드로 대조함. 가격과 청약수요의 인과효과나 실제 계약률·지역별 표시 경쟁률을 뜻하지 않으며 전국 확률표본도 아님.
- 데이터 URL: https://github.com/cheer710815-hub/apttosell-subscription-data/tree/main/datasets/within-project-price-demand-2026/
- 라이선스: 공공데이터포털은 두 출처 API 모두 '이용허락범위 제한 없음'이라고 명시. 파생 파일에 별도 적용할 명시적 라이선스 선택과 데이터 출처 표기는 등록자 최종 검토 필요.
- DOI: 아직 발급되지 않음. 다른 데이터셋 DOI를 기재하면 안 됨.
- 제출 상태: 준비 완료, DataON 로그인 사용자 승인요청 미진행.
