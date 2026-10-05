#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CROSSWALK=ROOT/"thinkers/plato/catalog/epigram-crosswalk-v0.1.2.json"
SCOPE=ROOT/"thinkers/plato/catalog/epigram-historical-scope-v0.1.1.json"
CATALOG=ROOT/"thinkers/plato/catalog/catalog-v0.1.5.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)
    print(f"PASS {message}")


def main() -> int:
    crosswalk=json.loads(CROSSWALK.read_text(encoding="utf-8"))
    scope=json.loads(SCOPE.read_text(encoding="utf-8"))
    catalog=json.loads(CATALOG.read_text(encoding="utf-8"))

    rows=crosswalk["rows"]
    by_id={e["catalog_id"]:e for e in catalog["entries"]}
    epigram_members={
        e["catalog_id"]:e
        for e in catalog["entries"]
        if e.get("parent_catalog_id")=="TH.PLATO.CAT.EPIGRAMMATA"
    }
    require(len(epigram_members)==37, "catalog v0.1.5 contains all 37 epigram historical objects")

    counts=Counter(r["catalog_mapping_status"] for r in rows)
    require(counts=={"MATCH":22,"UNRESOLVED":2,"EXCLUDE_FROM_PHILOSOPHER_PROFILE":7}, "Page/Massimo post-migration buckets are stable")
    require(all(r.get("current_catalog_id") in epigram_members for r in rows), "all Page/Massimo crosswalk rows resolve to epigram catalog objects")
    require(not [r for r in rows if r["catalog_mapping_status"]=="MISSING"], "post-migration crosswalk has zero missing rows")

    mapped={r["current_catalog_id"] for r in rows}
    supplemental=set(epigram_members)-mapped
    require(supplemental=={
        "TH.PLATO.CAT.EPIGRAM_9_3",
        "TH.PLATO.CAT.EPIGRAM_9_45",
        "TH.PLATO.CAT.EPIGRAM_9_359",
        "TH.PLATO.CAT.EPIGRAM_APL_11",
        "TH.PLATO.CAT.EPIGRAM_APL_210",
        "TH.PLATO.CAT.EPIGRAM_PINDAR_TRADITION",
    }, "six Pelucchi-scope objects sit outside the 31-row Page baseline exactly as expected")

    excluded=[r for r in rows if r["catalog_mapping_status"]=="EXCLUDE_FROM_PHILOSOPHER_PROFILE"]
    require(all(by_id[r["current_catalog_id"]]["runtime_candidacy"]=="CATALOG_ONLY" for r in excluded), "all Page homonym-excluded objects are catalog-only")
    unresolved={r["page_eg"] for r in rows if r["catalog_mapping_status"]=="UNRESOLVED"}
    require(unresolved=={"III","XXXI"}, "remaining crosswalk uncertainty is identity relation, not missing catalog data")

    scope_ids={x["current_catalog_id"] for x in scope["items"]}
    require(len(scope_ids)==37 and scope_ids==set(epigram_members), "37-item historical scope is fully migrated into catalog v0.1.5")
    require(all(x["catalog_mapping_status"]=="PRESENT" for x in scope["items"]), "historical-scope migration has no remaining MISSING state")

    print("\nDeterministic epigram migration result:")
    print("  catalog members: 37")
    print("  Page MATCH: 22")
    print("  Page UNRESOLVED identity relations: 2")
    print("  Page HOMONYM exclusions: 7")
    print("  Page-baseline supplemental Pelucchi objects: 6")
    print("\nEpigram catalog migration to v0.1.5 is complete.")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
