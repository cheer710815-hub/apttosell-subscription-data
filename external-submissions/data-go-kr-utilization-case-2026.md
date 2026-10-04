# 공공데이터포털 활용사례 등록 준비 — AptToSell 2026 청약 경쟁률·후속공급 분석

## 활용사례명
2026 아파트 청약 경쟁률과 후속공급 분석

## 개발유형
웹사이트

## 서비스 URL
https://apttosell.com/%EC%B2%AD%EC%95%BD-%EA%B2%BD%EC%9F%81%EB%A5%A0/

## 활용 공공데이터
한국부동산원_청약홈 분양정보 조회 서비스
https://www.data.go.kr/data/15098547/openapi.do

주요 사용 API:
- 최초 입주자모집공고 상세
- 무순위/잔여세대 모집공고 상세
- 임의공급 모집공고 상세
- 1순위 경쟁률
- 주택형별 분양가/공급 정보

## 서비스 설명
AptToSell이 2026년 1월부터 9월까지 청약홈에 공개된 아파트 최초 모집공고를 기준으로 1순위 청약 경쟁률, 분양가, 이후 무순위·잔여세대·임의공급 공고를 프로젝트 단위로 연결해 분석한 공개 데이터 서비스입니다.

최종 분석 대상은 196개 단지이며, 이 중 193개 단지에서 1순위 경쟁률을 확인했습니다. 각 단지는 최초 모집공고일, 공급가구수, 1순위 경쟁률, 분양가 구간, 후속공급 발생 여부, 첫 후속공급까지의 경과일, 60일 관측 여부 등으로 표준화했습니다.

분석 결과와 함께 196개 단지 프로젝트별 CSV, 요약 CSV, 데이터사전, 방법론을 공개하고 있으며, Figshare DOI를 통해 영구 식별자도 제공합니다.

주의: 이 자료에서 '후속공급 발생'은 이후 무순위·잔여세대 또는 임의공급 공고가 관측됐다는 의미이며, 미계약률이나 계약 실패율을 뜻하지 않습니다.

## 주요 기능
- 196개 아파트 프로젝트별 청약 경쟁률·분양가·후속공급 데이터 조회
- 경쟁률 구간별 후속공급 발생률 비교
- 분양가 구간별 후속공급 비교
- 수도권·비수도권 비교
- 최초 모집공고 후 60일 관측기준 분석
- 프로젝트별 CSV 다운로드
- 데이터사전 및 분석 방법론 공개
- DOI 기반 연구·기사 인용 지원

## 활용 목적
청약 경쟁률만으로 분양시장의 후속공급 여부를 단정하지 않고, 최초 모집공고와 이후 공급 공고를 연결하여 실제 관측 데이터를 제공하기 위해 구축했습니다. 주택시장 기사, 연구, 교육자료, 데이터 분석 및 일반 이용자의 청약시장 이해를 위한 참고자료로 활용할 수 있습니다.

## 대표 수치
- 최종 분석 대상: 196개 단지
- 경쟁률 확인: 193개 단지
- 1순위 경쟁률 10대 1 이상: 44개 단지
- 이 중 후속공급 확인: 19개 단지 (단순 관측 43.2%)
- 60일 관측가능 단지: 36개
- 60일 이내 후속공급: 13개 (36.1%)

## 공개 데이터
프로젝트별 CSV:
https://raw.githubusercontent.com/cheer710815-hub/apttosell-subscription-data/main/reports/apttosell-apartment-subscription-followup-projects-2026-jan-sep.csv

요약 CSV:
https://raw.githubusercontent.com/cheer710815-hub/apttosell-subscription-data/main/reports/apttosell-followup-analysis-2026-jan-sep-summary.csv

방법론:
https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/reports/apttosell-followup-analysis-2026-jan-sep-methodology.md

데이터사전:
https://github.com/cheer710815-hub/apttosell-subscription-data/blob/main/reports/apttosell-followup-analysis-data-dictionary.md

Figshare DOI:
https://doi.org/10.6084/m9.figshare.34064439

SchemaFinder:
https://schemafinder.com/dataset/c-1791120376-dsjx89

## 등록 시 유의
- 공식 API 원자료와 AptToSell의 파생 계산값을 구분해 설명
- '미계약률', '계약 실패율' 표현 사용 금지
- 파생 경쟁률/분양가 계산 규칙은 방법론 문서로 연결
- 서비스 화면 캡처가 필요한 경우 AptToSell 분석 원문 상단 및 표 영역 사용
