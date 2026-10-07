# DDFS sample-enrichment audit — development vs holdouts (2026)

## Purpose

Quantify how strongly the original 20-case development sample was enriched for high-DDFS observations compared with two out-of-sample holdouts.

Samples:
1. original 20-case development sample
2. holdout-1: 10 projects
3. holdout-2: 20 chronologically selected projects

## Distribution summary

| Sample | n | DDFS=0 | DDFS>0 | Median | Mean | DDFS>=50 | DDFS=100 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Original development | 20 | 20% | 80% | **44.65%** | **47.47%** | **45%** | **25%** |
| Holdout-1 | 10 | 60% | 40% | **0%** | **8.95%** | 0% | 0% |
| Chronological holdout-2 | 20 | **85%** | **15%** | **0%** | **0.49%** | 0% | 0% |

The original-sample mean DDFS is approximately 97 times the holdout-2 mean.

## Statistical comparison

### Original 20 vs chronological holdout-2

Non-zero DDFS:
- original: 16/20
- holdout-2: 3/20
- Fisher exact p = **0.0000875**

DDFS >=50%:
- original: 9/20
- holdout-2: 0/20
- Fisher exact p = **0.00123**

Distribution:
- Mann–Whitney U = 353
- p = **0.0000080**

These differences are too large to treat the original 20 as a frequency-representative sample of follow-up projects.

### Original 20 vs holdout-1

Mann–Whitney:
- p = **0.00978**

### Holdout-1 vs holdout-2

Mann–Whitney:
- p = **0.0800**

The two holdouts are much more similar to one another than either is to the original development sample, although holdout-1 is somewhat more enriched than the chronological sample.

### Three-sample test

Kruskal–Wallis:
- H = 22.245
- p = **0.0000148**

The three samples do not share a common DDFS distribution.

## Interpretation

The original 20-case set should now be explicitly described as a **mechanism-development / high-DDFS-enriched sample**, not a representative population sample.

This does not invalidate the mechanism findings inside that sample.

It changes the scope of inference:

Incorrect:
> Four DDFS pathways occur at these frequencies in the broader population of follow-up-supply projects.

Supported:
> Among deliberately enriched cases where deeply oversubscribed types reappeared, multiple mechanisms were observed. In mechanically selected follow-up cohorts, high DDFS itself was rare.

## Selection-enrichment magnitude

### Non-zero DDFS
- development sample: 80%
- chronological holdout: 15%
- relative prevalence: **5.33x**

### DDFS >=50%
- development sample: 45%
- chronological holdout: 0%

An ordinary ratio is undefined because the holdout count is zero; the important fact is that 9 of 20 development cases were >=50% while none of 20 chronological holdout cases were.

### DDFS=100%
- development sample: 25%
- chronological holdout: 0%

## Research-question reframing

The project should no longer be framed primarily as:

> Why does follow-up supply occur despite competition?

The data support a sharper question:

> **What distinguishes the rare projects in which housing types with very deep initial application demand (>=6x) themselves reappear in first follow-up supply?**

This reframing aligns the sampling design with the observed data.

## Updated conceptual structure

### Population-level modal pattern
Most mechanically selected follow-up projects:
- DDFS = 0%
- follow-up supply mainly comes from types that were not deeply oversubscribed initially.

### Exceptional pattern
A smaller subset:
- DDFS >0
- sometimes DDFS >=50 or 100
- deeply oversubscribed types themselves reappear.

The four-path taxonomy is most appropriate for explaining this exceptional subset, not for estimating population frequencies.

## Publication language

Recommended:
> "The initial 20-case analytical sample was intentionally enriched for cases with substantial reappearance of high-competition housing types. A subsequent chronological 20-project holdout had a median DDFS of 0%, with 17 of 20 projects at DDFS=0. Therefore pathway frequencies from the development sample should not be interpreted as population frequencies."

Avoid:
- "45% of projects are high-DDFS"
- "25% of projects have DDFS 100%"
- "the four pathways occur in these proportions nationally"

## Next step

The highest-value next step is to build a case-control design:

Cases:
- DDFS >=50%

Controls:
- DDFS =0%

Then match or stratify on:
- announcement month
- region
- project size
- average initial competition band

After matching, compare:
- mandatory self-funded midterm burden
- price gap
- post-completion structure
- contract cash timing

This directly tests what distinguishes rare high-DDFS cases from ordinary DDFS=0 follow-up projects without confusing mechanism sampling with population prevalence.
