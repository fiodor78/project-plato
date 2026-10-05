#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CROSSWALK = ROOT / "thinkers/plato/catalog/epigram-crosswalk-v0.1.1.json"
CATALOG = ROOT / "thinkers/plato/catalog/catalog-v0.1.4.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)
    print(f"PASS {message}")


def main() -> int:
    crosswalk = json.loads(CROSSWALK.read_text(encoding="utf-8"))
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))

    rows = crosswalk["rows"]
    by_id = {e["catalog_id"]: e for e in catalog["entries"]}
    epigram_members = {
        e["catalog_id"]: e
        for e in catalog["entries"]
        if e.get("parent_catalog_id") == "TH.PLATO.CAT.EPIGRAMMATA"
    }

    counts = Counter(r["catalog_mapping_status"] for r in rows)
    require(counts == {
        "MATCH": 19,
        "MISSING": 3,
        "UNRESOLVED": 2,
        "EXCLUDE_FROM_PHILOSOPHER_PROFILE": 7,
    }, "Page/Massimo migration-plan buckets are stable and exhaustive")

    mapped_catalog_ids = {
        r["current_catalog_id"]
        for r in rows
        if r.get("current_catalog_id") is not None
    }
    require(mapped_catalog_ids <= set(epigram_members), "all crosswalk catalog references resolve to Epigrammata members")

    supplemental = set(epigram_members) - mapped_catalog_ids
    require(
        supplemental == {
            "TH.PLATO.CAT.EPIGRAM_9_3",
        },
        "current catalog preserves exactly the one Page-baseline supplemental epigram"
    )

    excluded_with_catalog = [
        r for r in rows
        if r["catalog_mapping_status"] == "EXCLUDE_FROM_PHILOSOPHER_PROFILE"
        and r.get("current_catalog_id")
    ]
    for row in excluded_with_catalog:
        entry = by_id[row["current_catalog_id"]]
        require(
            entry["runtime_candidacy"] != "TEXT_CANDIDATE",
            f"{row['page_eg']} / {row['current_catalog_id']} is not a philosopher-Plato runtime text candidate"
        )

    unresolved = {r["page_eg"] for r in rows if r["catalog_mapping_status"] == "UNRESOLVED"}
    require(unresolved == {"III", "XXXI"}, "identity conflicts remain limited to EG III and EG XXXI in the Page baseline")

    missing = {r["page_eg"] for r in rows if r["catalog_mapping_status"] == "MISSING"}
    require(missing == {"IX", "XIV", "XXIII"}, "known Page-baseline catalog additions are explicit and stable")

    require(
        all(r["pelucchi_2026_number"] is None for r in rows),
        "catalog migration remains blocked until exact Pelucchi 2026 numbering is captured"
    )

    print("\nDeterministic epigram migration plan:")
    for status in ["MATCH", "MISSING", "UNRESOLVED", "EXCLUDE_FROM_PHILOSOPHER_PROFILE"]:
        members = [r["page_eg"] for r in rows if r["catalog_mapping_status"] == status]
        print(f"  {status}: {len(members)} -> {', '.join(members)}")
    print(f"  CURRENT_SUPPLEMENTAL: {len(supplemental)} -> {', '.join(sorted(supplemental))}")
    print("\nEpigram catalog migration is NOT authorized yet.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
