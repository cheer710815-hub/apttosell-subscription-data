# CSV parsing discrepancy resolved — 2026-10-18

The previous 43-project / 18-followup recount was **incorrect**. It split CSV rows on literal commas without respecting quoted fields. Two project names contain embedded commas: ATS-2026-054 and ATS-2026-161. The latter was wrongly excluded from the high-competition cohort.

Using a quote-aware CSV parser on all 196 rows restores the published summary counts:

- 10–<30:1: 23 projects / 17 broad-followup projects.
- >=30:1: 21 projects / 2 broad-followup projects.
- **Combined >=10:1: 44 projects / 19 broad-followup projects (43.2% crude rate).**

The [candidate audit CSV](./high-competition-followup-candidates-2026-audit.csv) now includes 19 candidates, including ATS-2026-161 (세종 우미 린 센터파크). All official followup category and type-level fields remain **pending verification**.

**Scope limitation:** `has_followup` is broader than official 무순위(사후) and may include 임의공급 and other categories. 43.2% must not be described as a verified 무순위 incidence rate, contract-cancellation rate, or national population estimate. Observation periods differ by initial notice date.
