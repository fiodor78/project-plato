#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]
SCHEMA=ROOT/"thinkers/plato/profile/epigram-crosswalk.schema.json"
CROSSWALK=ROOT/"thinkers/plato/catalog/epigram-crosswalk-v0.1.2.json"
CATALOG=ROOT/"thinkers/plato/catalog/catalog-v0.1.5.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)
    print(f"PASS {message}")


def main() -> int:
    schema=json.loads(SCHEMA.read_text(encoding="utf-8"))
    data=json.loads(CROSSWALK.read_text(encoding="utf-8"))
    catalog=json.loads(CATALOG.read_text(encoding="utf-8"))
    errors=sorted(Draft202012Validator(schema).iter_errors(data),key=lambda e:list(e.path))
    require(not errors, "epigram crosswalk validates against schema")

    rows=data["rows"]
    require(data["crosswalk_version"]=="0.1.2", "epigram crosswalk version is 0.1.2")
    require(len(rows)==31, "Page/Massimo baseline has exactly 31 rows")
    require(len({r["row_id"] for r in rows})==31, "epigram crosswalk row IDs are unique")
    require(len({r["page_eg"] for r in rows})==31, "Page EG numbers are unique")

    counts=Counter(r["catalog_mapping_status"] for r in rows)
    require(counts=={"MATCH":22,"UNRESOLVED":2,"EXCLUDE_FROM_PHILOSOPHER_PROFILE":7}, "Page/Massimo crosswalk has no remaining MISSING rows")
    require(all(r.get("current_catalog_id") for r in rows), "all Page/Massimo rows now resolve to catalog identities")

    catalog_ids={e["catalog_id"] for e in catalog["entries"]}
    require({r["current_catalog_id"] for r in rows} <= catalog_ids, "all crosswalk catalog identities exist in catalog v0.1.5")

    junior=[r for r in rows if r["attribution_target"]=="PLATO_YOUNGER"]
    require(len(junior)==7, "Plato Junior homonymy layer is explicit for seven Page/Massimo rows")
    require(all(r["catalog_mapping_status"]=="EXCLUDE_FROM_PHILOSOPHER_PROFILE" for r in junior), "Plato Junior rows cannot silently enter the philosopher-Plato profile")

    unresolved={r["page_eg"] for r in rows if r["catalog_mapping_status"]=="UNRESOLVED"}
    require(unresolved=={"III","XXXI"}, "identity conflicts remain limited to EG III and EG XXXI")
    require(not [r for r in rows if r["catalog_mapping_status"]=="MISSING"], "no Page/Massimo row remains missing after catalog v0.1.5 migration")

    eg_xviii=next(r for r in rows if r["page_eg"]=="XVIII")
    require(
        eg_xviii["witnesses"][0]["reference"]=="7.268"
        and eg_xviii["current_catalog_id"]=="TH.PLATO.CAT.EPIGRAM_7_268"
        and eg_xviii["catalog_mapping_status"]=="MATCH",
        "EG XVIII maps to AP 7.268 / FGE XVIII 640 rather than erroneous AP 7.368"
    )

    require(all(r["pelucchi_2026_number"] is None for r in rows), "crosswalk does not fabricate unverified Pelucchi 2026 ordinal numbers")
    print("\nEpigram crosswalk gate passed.")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
