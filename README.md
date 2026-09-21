# Power Supply Tests

Cross-industry power-supply validation plans, test matrices, standards references, stimulus profiles and automation assets.

## Repository structure

### Standards

Standards research and normalized standards mappings live in [`Standards/`](Standards/):

- [Global Power-Supply Testing Standards — Cross-Industry Research](Standards/global-power-supply-testing-standards-research-2026-09-21.md) — cross-industry standards inventory covering general power electronics, medical/life-support, railway, marine, aviation, military, space, nuclear and related power-interface standards.

### Test matrices

All test-matrix artifacts live in [`Test-matrix/`](Test-matrix/):

- [Global Power Supply Validation Test Matrix](Test-matrix/global-power-supply-test-matrix.md) — cross-industry master matrix.
- [Automotive Power Supply Validation Test Matrix](Test-matrix/automotive-power-supply-test-matrix.md) — detailed 135-row automotive validation matrix.
- [Automotive Power Supply Validation Test Matrix (CSV)](Test-matrix/automotive-power-supply-test-matrix.csv) — machine-readable automotive matrix.
- [ISO 26262 ASIL Test Mapping](Test-matrix/iso26262-asil-test-mapping.md) — per-test functional-safety role, ASIL grading, rationale and change log.
- [ISO 26262 Test Classification (CSV)](Test-matrix/iso26262-test-classification.csv) — machine-readable CORE/ROB/TRIG/QUAL/SUPP classification.
- [Test Matrix Additions — 2026-09-21](Test-matrix/test-matrix-additions-2026-09-21.md) — rationale and applicability filter for integrated rows.

### Reference

Research provenance, reviewed URLs and source indexes live in [`reference/`](reference/):

- [Global standards research source ledger](reference/global-power-supply-testing-standards-research-links-2026-09-21.md) — preserved/reviewed links from the cross-industry standards search.
- [Research Source Links](reference/research-source-links.md) — original curated research index.
- [Research Source Links v2](reference/research-source-links-v2.md) — second research pass with expanded standards and market coverage.
- [Full Research Material Index](reference/research-material-full-index.md) — full research trail and provenance notes.

### Engineering documents

Implementation plans, reviews and templates remain in [`docs/`](docs/):

- [Electronic Power — Industry Coverage Map](docs/electronic-power-industry-coverage.md) — detailed industry-to-standards discovery map.
- [Automated Power-Supply Validation Bench](docs/automated-power-supply-validation-bench.md) — automation coverage and recommended N6700/e-load/DPO4000/chamber/fault-fixture architecture.
- [Deep Review and Gap Analysis — 2026-09-21](docs/deep-review-and-gap-analysis-2026-09-21.md) — repository-wide review and verified gaps.
- [Mission Profile Template](docs/mission-profile-template.md) — project input template for lifetime, robustness, environmental and margin-test derivation.

### Tooling

- [`check_matrix_consistency.py`](check_matrix_consistency.py) — CI guard against duplicate/missing IDs, title/classification drift, invalid ASIL vocabulary and missing references.

## Intended bench

The matrices are organized around a programmable DC power supply, electronic load, oscilloscope, thermal chamber and relay/fault-injection system. Each test indicates whether the existing bench is sufficient or whether additional equipment is required.

> Exact severity levels and acceptance criteria must always be taken from the applicable customer/OEM requirement and licensed edition of the referenced standard.
