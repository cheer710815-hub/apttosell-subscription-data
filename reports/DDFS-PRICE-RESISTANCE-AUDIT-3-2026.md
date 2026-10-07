# DDFS price-resistance audit — three high-DDFS counterexamples (2026)

## Scope

Projects: 더샵 트리센트 / 쌍용 더 플래티넘 온수역 / 엘리프 성성호수공원 1BL

Primary comparison rule follows the existing presale-price-gap-2026 methodology: 84㎡ class, maximum presale price, same legal dong, six months before announcement, exclusive area 82–86㎡, median transaction price, with newer-stock sensitivity where available.

## 1. 더샵 트리센트
- Announcement: 2026-07-24
- 84㎡ maximum presale price: 849,000,000 KRW
- Same-dong all-age median: 530,000,000 KRW (91 trades), gap +60.19%
- <=20y median: 595,000,000 KRW (71 trades), gap +42.69%
- <=10y median: 606,000,000 KRW (52 trades), gap +40.10%

Interpretation: price resistance remains strong even against newer nearby apartments. Updated path: PRICE_RESISTANCE + CONVERSION_GAP. DDFS 100%.

## 2. 쌍용 더 플래티넘 온수역
- Announcement: 2026-02-13
- 84㎡ maximum presale price: 1,137,600,000 KRW
- Same-dong all-age median: 905,000,000 KRW (31 trades), gap +25.70%
- <=20y median: 915,000,000 KRW (21 trades), gap +24.33%
- <=10y median: 915,000,000 KRW (21 trades), gap +24.33%

Interpretation: a material price premium remains after restricting to newer stock. Updated path: MODERATE/HIGH PRICE RESISTANCE + CONVERSION GAP. DDFS 100%.

## 3. 엘리프 성성호수공원 1BL
- Announcement: 2026-04-23
- 84A maximum presale price: 588,600,000 KRW
- 84B maximum presale price: 568,500,000 KRW

Strict same-dong comparison is unavailable: the existing dataset has 0 eligible 84㎡ transactions in 업성동.

Adjacent-dong sensitivity comparator: 천안푸르지오레이크사이드, 성성동, completed 2023, 84.98–84.99㎡.
Pre-announcement transactions used (2026-02-12 through 2026-04-19): 582m, 582m, 582m, 570m, 550m, 585m, 546m, 530m KRW.
Median = 576,000,000 KRW.
84A maximum presale gap = +2.19%. 84B maximum presale price is below this comparator median.

Interpretation: this is not a strict same-dong result and must be flagged separately. However, a strong high-price explanation is not supported. Updated path: LOW_TO_NEUTRAL PRICE RESISTANCE / STRONG CONVERSION-GAP CANDIDATE. DDFS 100%.

## 4. Updated separation

| Project | DDFS | Price signal | Updated path |
|---|---:|---|---|
| 더샵 트리센트 | 100% | High (+40.1% vs <=10y same-dong median) | Price resistance + conversion gap |
| 쌍용 더 플래티넘 온수역 | 100% | Moderate/high (+24.3%) | Price resistance + conversion gap |
| 엘리프 성성호수공원 1BL | 100% | Low/neutral in adjacent-new-stock sensitivity (+2.2% for 84A max) | Strong conversion-gap candidate |

## 5. Implication

The price test does not collapse the multi-path model. Instead it separates price-assisted conversion failure from a cleaner conversion-gap case.

엘리프 성성호수공원 1BL currently combines DDFS 100%, high first-priority competition, 60% midterm loan coverage, 0% mandatory self-funded midterm burden under current coding, and no strong price premium in the adjacent-new-stock sensitivity test.

This makes it one of the strongest current observations supporting an independent contract-conversion-gap path.

## 6. Methodological caution

The 엘리프 sensitivity comparison uses adjacent 성성동 rather than strict same legal dong. Do not merge the +2.19% value mechanically into same-dong regressions without a method flag.

Recommended fields: price_gap_pct_strict / price_gap_pct_adjacent_sensitivity / price_comparison_method.

## Next step

Expand price-gap linkage to the full DDFS 20-case set using the existing presale-price-gap-2026 dataset, then test DDFS against all-age and <=10-year price gaps with leave-one-out sensitivity and explicit missing-comparable handling.