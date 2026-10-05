#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "thinkers/plato/profile/work-registry.schema.json"
REGISTRY = ROOT / "thinkers/plato/profile/work-registry-v0.1.0.json"
CATALOG = ROOT / "thinkers/plato/catalog/catalog-v0.1.4.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)
    print(f"PASS {message}")


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))

    errors = sorted(Draft202012Validator(schema).iter_errors(registry), key=lambda e: list(e.path))
    require(not errors, "work-code registry validates against schema")

    entries = registry["entries"]
    require(registry["registry_status"] == "PARTIAL_FROZEN", "registry explicitly remains partial while epigrams are unresolved")
    require(registry["deferred_scopes"] == ["EPIGRAMMATA_MEMBERS"], "only Epigrammata members are deferred")

    semantic_ids = [e["semantic_id"] for e in entries]
    catalog_ids = [e["catalog_id"] for e in entries]
    codes = [e["code"] for e in entries]
    require(len(semantic_ids) == len(set(semantic_ids)), "semantic work IDs are unique")
    require(len(catalog_ids) == len(set(catalog_ids)), "registry catalog references are unique")
    require(len(codes) == len(set(codes)), "frozen work codes are unique")

    epigram_members = {
        e["catalog_id"]
        for e in catalog["entries"]
        if e.get("parent_catalog_id") == "TH.PLATO.CAT.EPIGRAMMATA"
    }
    expected = {
        e["catalog_id"]
        for e in catalog["entries"]
        if e["catalog_id"] not in epigram_members
    }
    require(set(catalog_ids) == expected, "registry covers every current non-epigram catalog entry")
    require(not (set(catalog_ids) & epigram_members), "no individual Epigrammata member is prematurely frozen")

    by_catalog = {e["catalog_id"]: e for e in entries}
    require("TH.PLATO.CAT.EPIGRAMMATA" in by_catalog, "Epigrammata collection identity itself is frozen")
    require(
        by_catalog["TH.PLATO.CAT.EPIGRAMMATA"]["semantic_id"] == "TH.PLATO.COLLECTION.EPIGRAMMATA",
        "Epigrammata collection has a stable semantic collection ID"
    )

    for item in entries:
        suffix = item["catalog_id"].removeprefix("TH.PLATO.CAT.")
        require(item["code"] == suffix, f"{item['catalog_id']} uses catalog-stable code {suffix}")

    print(f"\nFrozen non-epigram semantic codes: {len(entries)}")
    print(f"Deferred epigram member codes: {len(epigram_members)}")
    print("\nWork-code registry gate passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
