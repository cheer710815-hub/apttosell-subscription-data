# Study 04 — public-minimum v1.1 pred eposit QA (2026-11-03)

Status: **CANDIDATE ONLY; do not publish or issue DOI**.

The existing v1 minimum aggregate package passed ZIP CRC, six-file SHA-256 manifest, and structural/consistency checks. A v1.1 candidate was generated locally to add integer grid-aligned counts to the 8 aggregate rows so researchers can recompute the descriptive percentages directly.

The integer numerators were reconstructed from v1's 6-decimal percentages and row denominators, with less than 0.00000051 percentage-point discrepancy. **They were not re-extracted from transaction-level source for this release candidate**; the original 2025/2026 audits are separate.

The v1.1 checker passed; ZIP CRC and a six-member SHA manifest pass. Original transaction CSV and complex-level small-cell tables were excluded. v1.1 is a **high-level aggregate dataset**, not complete raw-source reproduction, and the original matched-stratum bootstrap cannot be independently regenerated from its files.

Known gates: (1) creator name approval (proposed: Kim, Eun); (2) actual creator-chosen derivative license and rights review; (3) final disclosure/privacy review; (4) optionally completing 2024 holdout; (5) account restoration and explicit release authorization before Zenodo.

Title draft: *Round-Number Pricing and Trade-Composition Reversals in Seoul Apartment Transaction Disclosures (2025; Partial 2026 Validation)*.

**Do not cite this administrative memo as a registered dataset.**