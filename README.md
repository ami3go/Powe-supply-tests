# Power Supply Tests

Automotive power-supply validation plans, test matrices, standards references, stimulus profiles and automation assets.

## Repository structure

### Standards

Standards mappings and standards-driven test matrices live in [`Standards/`](Standards/):

- [Global Power-Supply Testing Standards — Cross-Industry Research](Standards/global-power-supply-testing-standards-research-2026-09-21.md) — cross-industry standards inventory covering general power electronics, medical/life-support, railway, marine, aviation, military, space and nuclear applications.
- [Automotive Power Supply Validation Test Matrix](Standards/automotive-power-supply-test-matrix.md) — authoritative 121-row human-readable validation matrix.
- [Automotive Power Supply Validation Test Matrix (CSV)](Standards/automotive-power-supply-test-matrix.csv) — machine-readable copy generated from the matrix.
- [ISO 26262 ASIL Test Mapping](Standards/iso26262-asil-test-mapping.md) — per-test functional-safety role, ASIL grading, rationale and change log.
- [ISO 26262 Test Classification (CSV)](Standards/iso26262-test-classification.csv) — machine-readable CORE/ROB/TRIG/QUAL/SUPP classification.

### Reference

Research provenance, reviewed URLs and source indexes live in [`reference/`](reference/):

- [Global standards research source ledger](reference/global-power-supply-testing-standards-research-links-2026-09-21.md) — preserved/reviewed links from the cross-industry standards search.
- [Research Source Links](reference/research-source-links.md) — original curated research index.
- [Research Source Links v2](reference/research-source-links-v2.md) — second research pass with expanded standards and market coverage.
- [Full Research Material Index](reference/research-material-full-index.md) — full research trail and provenance notes.

### Engineering documents

Implementation plans, reviews and templates remain in [`docs/`](docs/):

- [Automated Power-Supply Validation Bench](docs/automated-power-supply-validation-bench.md) — automation coverage and recommended N6700/e-load/DPO4000/chamber/fault-fixture architecture.
- [Deep Review and Gap Analysis — 2026-09-21](docs/deep-review-and-gap-analysis-2026-09-21.md) — repository-wide review and verified gaps.
- [Test Matrix Additions — 2026-09-21](docs/test-matrix-additions-2026-09-21.md) — rationale and applicability filter for integrated rows.
- [Mission Profile Template](docs/mission-profile-template.md) — project input template for lifetime, robustness, environmental and margin-test derivation.

### Tooling

- [`check_matrix_consistency.py`](check_matrix_consistency.py) — CI guard against duplicate/missing IDs, title/classification drift, invalid ASIL vocabulary and missing references.

## Intended bench

The matrix is organized around a programmable DC power supply, electronic load, oscilloscope and thermal chamber. Each test indicates whether the existing bench is sufficient or whether additional equipment is required.

## Reference families

The project currently maps tests to relevant standards and industry requirements including ISO 16750, ISO 7637, ISO 10605, ISO 11452, CISPR 25, ISO 21780, ISO 21498, ISO 20653 and LV 124 / VW 80000-derived requirements.

> Exact severity levels and acceptance criteria must always be taken from the applicable customer/OEM requirement and licensed edition of the referenced standard.
