#!/usr/bin/env python3
"""
Consistency checker for ami3go/Powe-supply-tests.

Implements the check the matrix itself asks for under "Suggested next repository
additions": fail CI on duplicate/missing IDs and inconsistent classifications.

Run from the repository root:
    python3 check_matrix_consistency.py            # check
    python3 check_matrix_consistency.py --fix-csv  # regenerate the CSV from the Markdown

Against commit a4c4198 this exits 1 and reports the two defects documented in
deep-review-and-gap-analysis-2026-09-21.md (D-1 abbreviation divergence,
D-2 title drift).
"""

import csv
import re
import sys
from pathlib import Path

DOCS = Path("docs")
MATRIX_MD = DOCS / "automotive-power-supply-test-matrix.md"
MATRIX_CSV = DOCS / "automotive-power-supply-test-matrix.csv"
CLASS_CSV = DOCS / "iso26262-test-classification.csv"
MAPPING_MD = DOCS / "iso26262-asil-test-mapping.md"

ID_RE = re.compile(r"^\| *([A-Z0-9]+-\d{3}) *\|")
ASIL_LEGEND = {"REQ", "++", "+", "o", "T", "n/a", "—", "FI+", "FI++", "WC+"}
COLUMNS = 15

# Abbreviations the repo removed in commit 015136a. Keeping them out of the CSV
# is what stops the two files drifting into opposite editorial styles again.
ABBREVIATIONS = ["Vin", "Vout", "UVLO", "OVLO", "DMM", "PGOOD", "DUT", "ALSE",
                 "ESD", "BCI", "OTP", "FRA", "NVM", "MLCC", "PD", "CMTI"]

errors: list[str] = []
warnings: list[str] = []


def parse_md_rows(path: Path) -> list[list[str]]:
    rows = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if ID_RE.match(line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) != COLUMNS:
                errors.append(f"{path}:{n} {cells[0]} has {len(cells)} columns, expected {COLUMNS}")
            rows.append(cells)
    return rows


def norm(s: str) -> str:
    """Compare titles ignoring markdown escaping, spacing and case."""
    return re.sub(r"\s+", " ", s.replace("\\", "").replace("/", " / ")).strip().lower()


def main(fix_csv: bool = False) -> int:
    for p in (MATRIX_MD, MATRIX_CSV, CLASS_CSV, MAPPING_MD):
        if not p.exists():
            print(f"missing file: {p}")
            return 2

    md_rows = parse_md_rows(MATRIX_MD)
    md = {r[0]: r for r in md_rows}
    csv_rows = list(csv.DictReader(MATRIX_CSV.open(encoding="utf-8-sig")))
    cls_rows = list(csv.DictReader(CLASS_CSV.open(encoding="utf-8-sig")))
    map_ids = set(re.findall(r"^\| *`?([A-Z0-9]+-\d{3})", MAPPING_MD.read_text(encoding="utf-8"), re.M))

    # --- duplicates ---
    seen = set()
    for r in md_rows:
        if r[0] in seen:
            errors.append(f"duplicate ID in matrix.md: {r[0]}")
        seen.add(r[0])

    # --- ID set agreement across all four artefacts ---
    sets = {
        "matrix.csv": {r["ID"] for r in csv_rows},
        "iso26262-test-classification.csv": {r["test_id"] for r in cls_rows},
        "iso26262-asil-test-mapping.md": map_ids,
    }
    for name, ids in sets.items():
        for missing in sorted(seen - ids):
            errors.append(f"{missing} in matrix.md but not in {name}")
        for extra in sorted(ids - seen):
            errors.append(f"{extra} in {name} but not in matrix.md")

    # --- title agreement ---
    for r in csv_rows:
        if r["ID"] in md and norm(md[r["ID"]][2]) != norm(r["Test"]):
            errors.append(f"title drift {r['ID']}: md={md[r['ID']][2]!r} csv={r['Test']!r}")
    for r in cls_rows:
        if r["test_id"] in md and norm(md[r["test_id"]][2]) != norm(r["test"]):
            warnings.append(f"title drift {r['test_id']}: md={md[r['test_id']][2]!r} classification={r['test']!r}")

    # --- ASIL vocabulary ---
    for r in md_rows:
        for col, cell in zip("ABCD", r[10:14]):
            token = cell.replace("\\", "").split(" · ")[0]
            if token.endswith("*"):
                token = token[:-1]
            if token not in ASIL_LEGEND:
                errors.append(f"{r[0]} ASIL {col}: {cell!r} not in the legend")

    # --- editorial style: CSV stays fully expanded ---
    csv_text = MATRIX_CSV.read_text(encoding="utf-8-sig")
    # An abbreviation introduced parenthetically after its expansion is fine,
    # e.g. "bulk current injection (BCI)". Only bare use is a style leak.
    csv_text = re.sub(r"\s*\([A-Z]{2,6}\)", "", csv_text)
    leaked = [a for a in ABBREVIATIONS if re.search(rf"\b{re.escape(a)}\b", csv_text)]
    if leaked:
        errors.append(f"abbreviations leaked into the CSV: {', '.join(leaked)}")

    # --- every row has a reference ---
    for r in md_rows:
        if not r[14] or r[14] in {"—", "-"}:
            errors.append(f"{r[0]} has no entry in 'Main reference'")

    if fix_csv:
        header = list(csv_rows[0].keys())
        with MATRIX_CSV.open("w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f, lineterminator="\n")
            w.writerow(header)
            for r in md_rows:
                w.writerow([c.replace("\\*", "*").replace("\\|", "|") for c in r])
        print(f"regenerated {MATRIX_CSV} from {MATRIX_MD} ({len(md_rows)} rows)")
        print("note: expand abbreviations in the Markdown first, or they will carry over")
        return 0

    for w_ in warnings:
        print(f"WARN  {w_}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\n{len(md_rows)} rows checked · {len(errors)} errors · {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(fix_csv="--fix-csv" in sys.argv))
