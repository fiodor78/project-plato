#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "thinkers/plato/catalog/catalog-v0.1.4.json"
AUTH_DIR = ROOT / "thinkers/plato/catalog/authenticity"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)
    print(f"PASS {message}")


def main() -> int:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    entries = catalog["entries"]
    by_id = {e["catalog_id"]: e for e in entries}

    eligible = {
        e["catalog_id"]: e
        for e in entries
        if e["survival_status"] == "EXTANT"
        and e["entry_type"] in {"WORK", "MEMBER"}
    }

    assertions = []
    for path in sorted(AUTH_DIR.glob("*.json")):
        assertions.append(json.loads(path.read_text(encoding="utf-8")))

    assertion_ids = [a["catalog_id"] for a in assertions]
    require(len(assertion_ids) == len(set(assertion_ids)), "each catalog item has at most one current authenticity assertion")
    require(set(assertion_ids) <= set(eligible), "all authenticity assertions point to extant individually addressable texts")

    covered = set(assertion_ids)
    unresolved_ids = sorted(set(eligible) - covered)
    unresolved = [by_id[i] for i in unresolved_ids]

    buckets = {
        "canonical_epistles": [],
        "epigrams": [],
        "extra_canonical_epistles": [],
        "other": [],
    }

    for entry in unresolved:
        code = entry.get("provisional_work_code") or ""
        if entry.get("parent_catalog_id") == "TH.PLATO.CAT.EPISTLES":
            buckets["canonical_epistles"].append(entry)
        elif entry.get("parent_catalog_id") == "TH.PLATO.CAT.EPIGRAMMATA":
            buckets["epigrams"].append(entry)
        elif code.startswith("EXTRA_EPISTLE_HERCHER_"):
            buckets["extra_canonical_epistles"].append(entry)
        else:
            buckets["other"].append(entry)

    require(len(assertions) >= 46, "Phase 1 authenticity coverage has reached at least 46 assessed texts")
    require(not buckets["other"], "all currently unresolved authenticity cases belong to explicitly tracked backlog groups")

    grades = Counter(a["classification"] for a in assertions)

    print("\nAuthenticity coverage:")
    print(f"  eligible extant individual texts: {len(eligible)}")
    print(f"  assessed: {len(covered)}")
    print(f"  unresolved: {len(unresolved)}")
    print(f"  coverage: {len(covered) / len(eligible) * 100:.1f}%")

    print("\nGrades:")
    for grade in ["A", "B", "C", "D"]:
        print(f"  {grade}: {grades.get(grade, 0)}")

    print("\nUnresolved backlog:")
    for name in ["canonical_epistles", "epigrams", "extra_canonical_epistles", "other"]:
        items = buckets[name]
        print(f"  {name}: {len(items)}")
        for entry in items:
            print(f"    - {entry['catalog_id']} :: {entry['canonical_title']}")

    print("\nAuthenticity coverage gate passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
