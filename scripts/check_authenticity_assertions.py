#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT=Path(__file__).resolve().parents[1]
CATALOG=ROOT/"thinkers/plato/catalog/catalog-v0.1.0.json"
SCHEMA=ROOT/"thinkers/plato/profile/authenticity-assertion.schema.json"
AUTH_DIR=ROOT/"thinkers/plato/catalog/authenticity"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)
    print(f"PASS {message}")


def main() -> int:
    catalog=json.loads(CATALOG.read_text(encoding="utf-8"))
    catalog_ids={e["catalog_id"] for e in catalog["entries"]}
    schema=json.loads(SCHEMA.read_text(encoding="utf-8"))
    validator=Draft202012Validator(schema,format_checker=FormatChecker())

    files=sorted(AUTH_DIR.glob("*.json"))
    require(bool(files),"authenticity assertion files exist")

    assertions=[]
    for path in files:
        obj=json.loads(path.read_text(encoding="utf-8"))
        errors=list(validator.iter_errors(obj))
        require(not errors,f"{path.name} validates against Plato authenticity schema")
        assertions.append(obj)

    ids=[a["assertion_id"] for a in assertions]
    require(len(ids)==len(set(ids)),"authenticity assertion IDs are unique")
    require(all(a["catalog_id"] in catalog_ids for a in assertions),"every authenticity assertion resolves to a catalog entry")
    require(all(a["runtime_visibility"]=="CUSTODIAN_ONLY" for a in assertions),"authenticity assertions are CUSTODIAN-only")
    require(
        all(len({e["source_ref"] for e in a["evidence"]})>=2 for a in assertions),
        "each current provisional D assertion has at least two distinct evidence sources"
    )

    print(f"\nValidated {len(assertions)} authenticity assertions.")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
