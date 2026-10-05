#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]
SCHEMA=ROOT/"thinkers/plato/profile/epigram-historical-scope.schema.json"
SCOPE=ROOT/"thinkers/plato/catalog/epigram-historical-scope-v0.1.1.json"
CATALOG=ROOT/"thinkers/plato/catalog/catalog-v0.1.5.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)
    print(f"PASS {message}")


def main() -> int:
    schema=json.loads(SCHEMA.read_text(encoding="utf-8"))
    scope=json.loads(SCOPE.read_text(encoding="utf-8"))
    catalog=json.loads(CATALOG.read_text(encoding="utf-8"))
    errors=sorted(Draft202012Validator(schema).iter_errors(scope),key=lambda e:list(e.path))
    require(not errors, "37-item epigram historical scope validates against schema")

    items=scope["items"]
    require(scope["scope_version"]=="0.1.1", "historical scope version is 0.1.1")
    require(len(items)==37, "Pelucchi 2025 source-explicit historical scope contains exactly 37 logical items")
    require(len({x["scope_id"] for x in items})==37, "historical-scope IDs are unique")
    require(len({x["logical_reference"] for x in items})==37, "logical references are unique")
    require(all(x["catalog_mapping_status"]=="PRESENT" and x["current_catalog_id"] for x in items), "all 37 historical-scope items map to catalog identities")

    epigram_members={
        e["catalog_id"]
        for e in catalog["entries"]
        if e.get("parent_catalog_id")=="TH.PLATO.CAT.EPIGRAMMATA"
    }
    mapped={x["current_catalog_id"] for x in items}
    require(len(mapped)==37, "historical scope maps to 37 unique catalog identities")
    require(mapped==epigram_members, "historical scope and catalog v0.1.5 epigram membership are identical")
    require(not [x for x in items if x["catalog_mapping_status"]=="MISSING"], "no historical-scope item remains missing from catalog v0.1.5")

    refs={x["logical_reference"] for x in items}
    require("AP 9.39" in refs and "AP 9.827" in refs, "previously omitted Pelucchi items AP 9.39 and AP 9.827 are present")
    require("AP 9.144" not in refs, "spurious prior AP 9.144 lead is excluded")
    require("AP 7.268" in refs and "AP 7.368" not in refs, "EG XVIII correction is reflected in historical scope")

    explicit_junior={"AP 9.13a","AP 9.748","AP 9.751"}
    junior={x["logical_reference"] for x in items if "PLATO_YOUNGER" in x["attribution_targets"]}
    require(explicit_junior <= junior, "explicit Plato the Younger witnesses are isolated from philosopher Plato")
    comic=next(x for x in items if x["logical_reference"]=="AP 9.359")
    require(comic["profile_relation"]=="HOMONYM_EXCLUDED", "Plato Comicus AP 9.359 is excluded from philosopher-Plato candidacy")

    anchors={x["logical_reference"]:x["pelucchi_2026_number"] for x in items if x["pelucchi_2026_number"] is not None}
    require(anchors=={
        "AP 7.669":1, "AP 7.670":2, "AP 7.99":3, "AP 7.100":4,
        "Archeanassa Platonic tradition":5, "AP 5.79":7, "AP 5.80":8,
        "AP 7.259":10, "AP 7.256":11,
    }, "only directly verified Pelucchi 2026 numbering anchors are recorded")

    by_id={e["catalog_id"]:e for e in catalog["entries"]}
    for item in items:
        e=by_id[item["current_catalog_id"]]
        require(e["epigrammatic_metadata"]["historical_scope_id"]==item["scope_id"], f"{item['scope_id']} resolves to matching catalog epigram metadata")
    require(all(by_id[i]["runtime_candidacy"]!="TEXT_CANDIDATE" for i in epigram_members), "epigram historical scope remains outside automatic philosopher-Plato runtime admission")

    print("\nEpigram historical scope gate passed.")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
