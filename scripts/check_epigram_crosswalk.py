#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "thinkers/plato/profile/epigram-crosswalk.schema.json"
CROSSWALK = ROOT / "thinkers/plato/catalog/epigram-crosswalk-v0.1.0.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)
    print(f"PASS {message}")


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    data = json.loads(CROSSWALK.read_text(encoding="utf-8"))
    errors = sorted(Draft202012Validator(schema).iter_errors(data), key=lambda e: list(e.path))
    require(not errors, "epigram crosswalk validates against schema")

    rows = data["rows"]
    require(len(rows) == 31, "Page/Massimo baseline has exactly 31 rows")
    require(len({r["row_id"] for r in rows}) == 31, "epigram crosswalk row IDs are unique")
    require(len({r["page_eg"] for r in rows}) == 31, "Page EG numbers are unique")

    junior = [r for r in rows if r["attribution_target"] == "PLATO_YOUNGER"]
    require(len(junior) == 7, "Plato Junior homonymy layer is explicit for seven Page/Massimo rows")
    require(
        all(r["catalog_mapping_status"] == "EXCLUDE_FROM_PHILOSOPHER_PROFILE" for r in junior),
        "Plato Junior rows cannot silently enter the philosopher-Plato profile"
    )

    unresolved = [r for r in rows if r["catalog_mapping_status"] == "UNRESOLVED"]
    require(
        {r["page_eg"] for r in unresolved} >= {"III", "XXXI"},
        "AP 5.77/5.78 and EG XXXI/AP 9.44 conflicts remain explicitly unresolved"
    )

    missing = [r for r in rows if r["catalog_mapping_status"] == "MISSING"]
    require(len(missing) >= 3, "crosswalk records known catalog gaps rather than hiding them")

    require(
        all(r["pelucchi_2026_number"] is None for r in rows),
        "Pelucchi 2026 numbering is not fabricated before the exact 37-item list is captured"
    )

    print("\nEpigram crosswalk gate passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
