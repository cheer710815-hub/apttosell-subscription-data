# DDFS prospective holdout-2 cohort lock — 20 projects

## Rule

This cohort is selected mechanically from the 2026 follow-up registry.

Selection:
1. sort by first follow-up notice date ascending;
2. exclude all projects used in the original DDFS 20-case classification;
3. exclude all projects used in holdout-1 (10 projects);
4. take the next 20 projects with an observed first follow-up event.

The cohort is frozen before contract, price, or path outcomes are reviewed.

## Locked cohort

1. 2026-02-20 — 북오산자이 리버블시티
2. 2026-02-26 — 사우역 지엔하임
3. 2026-03-05 — 서귀포시 서홍동 형남아파트6차
4. 2026-03-11 — 안양역 센트럴 아이파크 수자인
5. 2026-03-25 — 금정산 하늘채 루미엘
6. 2026-04-09 — 상주자이르네
7. 2026-04-15 — e편한세상 여수 글렌츠
8. 2026-04-15 — 부천역 에피트 어바닉
9. 2026-04-22 — 용인 플랫폼시티 라온프라이빗 아르디에
10. 2026-04-28 — 연수 월드메르디앙 어반포레
11. 2026-04-29 — 한화포레나 부산당리
12. 2026-05-06 — 경성대부경대역 비스타동원 더 프리미엄
13. 2026-05-07 — 엄궁역 트라비스 하늘채
14. 2026-05-12 — 르네오션 고성 퍼스트뷰
15. 2026-05-13 — 북전주 광신프로그레스
16. 2026-05-13 — 업성 푸르지오 레이크시티
17. 2026-05-14 — 중앙하이츠 갈산역 센트럴
18. 2026-05-18 — 야목역 서희스타힐스 그랜드힐
19. 2026-05-20 — 도안자이 센텀리체 1단지
20. 2026-05-21 — 문수로 라티에르 673

## Anti-leakage rule

For each project:
- first calculate DDFS from initial 1st-priority type competition and first follow-up type supply;
- only after DDFS is frozen, inspect contract terms, price gaps, or narrative causes;
- never substitute later unsold-round competition for initial competition;
- never replace a project because its DDFS is inconvenient.

## Known audit warning

Earlier cause-classification work showed a stage-mixing risk. Therefore every DDFS row must retain:
- initial_house_manage_no
- first_followup_notice_id
- initial type competition source
- first-followup type-supply source

before path classification.

## Status

Cohort frozen. DDFS calculation pending.
