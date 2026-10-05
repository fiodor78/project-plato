#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "thinkers/plato/profile/epigram-historical-scope.schema.json"
SCOPE = ROOT / "thinkers/plato/catalog/epigram-historical-scope-v0.1.0.json"
CATALOG = ROOT / "thinkers/plato/catalog/catalog-v0.1.4.json"


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
    require(len(items)==37, "Pelucchi 2025 source-explicit historical scope contains exactly 37 logical items")
    require(len({x["scope_id"] for x in items})==37, "historical-scope IDs are unique")
    require(len({x["logical_reference"] for x in items})==37, "logical references are unique")

    epigram_members={
        e["catalog_id"]
        for e in catalog["entries"]
        if e.get("parent_catalog_id")=="TH.PLATO.CAT.EPIGRAMMATA"
    }
    mapped={x["current_catalog_id"] for x in items if x["current_catalog_id"]}
    require(len(mapped)==23, "exactly 23 historical-scope items map to the current provisional catalog")
    require(mapped==epigram_members, "all current 23 Epigrammata members are covered exactly once by the 37-item scope")
    require(sum(1 for x in items if x["catalog_mapping_status"]=="MISSING")==14, "fourteen historical-scope items remain to be added or normalized")

    refs={x["logical_reference"] for x in items}
    require("AP 9.39" in refs and "AP 9.827" in refs, "the two previously omitted Pelucchi items AP 9.39 and AP 9.827 are present")
    require("AP 9.144" not in refs, "spurious prior AP 9.144 lead is not part of the source-explicit Pelucchi scope")
    require("AP 7.268" in refs and "AP 7.368" not in refs, "EG XVIII correction is reflected in historical scope")

    explicit_junior={"AP 9.13a","AP 9.748","AP 9.751"}
    junior={x["logical_reference"] for x in items if "PLATO_YOUNGER" in x["attribution_targets"]}
    require(explicit_junior <= junior, "explicit Plato the Younger witnesses are isolated from philosopher Plato")
    comic=next(x for x in items if x["logical_reference"]=="AP 9.359")
    require(comic["profile_relation"]=="HOMONYM_EXCLUDED", "Plato Comicus AP 9.359 is excluded from philosopher-Plato candidacy")

    anchors={x["logical_reference"]:x["pelucchi_2026_number"] for x in items if x["pelucchi_2026_number"] is not None}
    require(anchors=={
        "AP 7.669":1,
        "AP 7.670":2,
        "AP 7.99":3,
        "AP 7.100":4,
        "Archeanassa Platonic tradition":5,
        "AP 5.79":7,
        "AP 5.80":8,
        "AP 7.259":10,
        "AP 7.256":11,
    }, "only directly verified Pelucchi 2026 numbering anchors are recorded")

    require(
        all(e["runtime_candidacy"]!="TEXT_CANDIDATE" for e in catalog["entries"] if e["catalog_id"] in epigram_members),
        "current epigram catalog members remain outside automatic philosopher-Plato runtime admission"
    )

    print("\nEpigram historical scope gate passed.")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
