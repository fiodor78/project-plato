#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "thinkers/plato/catalog/catalog-v0.1.0.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)
    print(f"PASS {message}")


def main() -> int:
    with CATALOG.open("r", encoding="utf-8") as f:
        catalog = json.load(f)

    entries = catalog["entries"]
    sources = {s["source_id"] for s in catalog["sources"]}

    ids = [e["catalog_id"] for e in entries]
    require(len(ids) == len(set(ids)), "catalog IDs are unique")

    referenced_sources = {
        a["source_id"]
        for e in entries
        for a in e["attestations"]
    }
    require(referenced_sources <= sources, "every attestation source_id resolves")

    thrasyllan = []
    positions = []
    for e in entries:
        for a in e["attestations"]:
            if a["system"] == "THRASYLLAN_TETRALOGIES":
                thrasyllan.append(e)
                positions.append(a["position"])

    require(len(thrasyllan) == 36, "Thrasyllan catalog contains exactly 36 tetralogical slots")
    expected_positions={f"{t}.{p}" for t in range(1,10) for p in range(1,5)}
    require(set(positions) == expected_positions, "all nine tetralogies contain positions 1–4 exactly once")

    epistles = next(e for e in entries if e["catalog_id"] == "TH.PLATO.CAT.EPISTLES")
    require(epistles["entry_type"] == "COLLECTION", "Epistles tetralogical slot is preserved as a collection")

    letter_members=[
        e for e in entries
        if e["parent_catalog_id"] == "TH.PLATO.CAT.EPISTLES"
    ]
    require(len(letter_members) == 13, "Epistles collection has thirteen separately addressable members")

    lost=[e for e in entries if e["survival_status"] == "LOST"]
    require(bool(lost), "catalog preserves ancient lost-title attestations")
    require(
        all(e["runtime_candidacy"] == "CATALOG_ONLY" for e in lost),
        "lost titles cannot become runtime text candidates"
    )

    explicitly_spurious=[
        e for e in entries
        if any(a["status"] == "EXPLICITLY_SPURIOUS" for a in e["attestations"])
    ]
    require(bool(explicitly_spurious), "ancient explicit spurious attestations are preserved")

    overlap=[
        e for e in explicitly_spurious
        if any(a["system"] == "BURNET_OCT_VOL5" for a in e["attestations"])
    ]
    require(bool(overlap), "one entry can preserve overlapping ancient and editorial attestations")

    epigrams=next(e for e in entries if e["catalog_id"] == "TH.PLATO.CAT.EPIGRAMMATA")
    require(
        epigrams["entry_type"] == "ANTHOLOGY_COLLECTION"
        and epigrams["runtime_candidacy"] == "PENDING_REVIEW",
        "anthological Plato attribution is cataloged without automatic runtime admission"
    )

    require(
        all(e["runtime_visibility"] == "CUSTODIAN_ONLY" for e in entries),
        "historical catalog metadata is CUSTODIAN-only"
    )

    kinds=Counter(e["entry_type"] for e in entries)
    print("\nCatalog entry counts:")
    for kind,count in sorted(kinds.items()):
        print(f"  {kind}: {count}")
    print(f"  TOTAL: {len(entries)}")

    print("\nPhase 1 catalog structural gate passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
