#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "thinkers/plato/catalog/catalog-v0.1.4.json"


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

    expected_epistle_addressees = {
        "I": ["Dionysius II of Syracuse"],
        "II": ["Dionysius II of Syracuse"],
        "III": ["Dionysius II of Syracuse"],
        "IV": ["Dion"],
        "V": ["Perdiccas III of Macedon"],
        "VI": ["Hermias of Atarneus", "Erastus", "Coriscus"],
        "VII": ["Friends and associates of Dion"],
        "VIII": ["Friends and associates of Dion"],
        "IX": ["Archytas of Tarentum"],
        "X": ["Aristodorus"],
        "XI": ["Laodamas"],
        "XII": ["Archytas of Tarentum"],
        "XIII": ["Dionysius II of Syracuse"],
    }
    for letter in letter_members:
        meta = letter.get("epistolary_metadata")
        require(meta is not None, f"{letter['catalog_id']} has epistolary metadata")
        numeral = meta["traditional_number_roman"]
        labels = [a["label"] for a in meta["addressees"]]
        require(labels == expected_epistle_addressees[numeral], f"Epistle {numeral} addressee mapping is correct")
        require(
            {"PLSRC.DL_3_57_62", "PLSRC.BURY_EPISTLES_LOEB"} <= set(meta["source_refs"]),
            f"Epistle {numeral} addressee mapping has ancient and edition-level support"
        )

    epistle_x = next(e for e in letter_members if e["catalog_id"] == "TH.PLATO.CAT.EPISTLE_X")
    require(
        epistle_x["epistolary_metadata"]["addressee_review_status"] == "SOURCE_VERIFIED_WITH_VARIANT",
        "Epistle X preserves Aristodemus/Aristodorus variant rather than flattening it"
    )

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

    allowed_scope_classes = {
        "THRASYLLAN_CANON",
        "THRASYLLAN_COLLECTION_MEMBER",
        "EXTRA_CANONICAL_EXTANT_ATTRIBUTION",
        "ANCIENT_EXPLICIT_SPURIA",
        "LOST_ATTRIBUTION",
        "ANTHOLOGICAL_ASCRIPTION",
    }
    require(
        all(e.get("scope_classes") and set(e["scope_classes"]) <= allowed_scope_classes for e in entries),
        "every catalog entry has at least one valid historical scope class"
    )
    require(
        all(
            "THRASYLLAN_CANON" in e["scope_classes"]
            for e in thrasyllan
        ),
        "all Thrasyllan slots carry THRASYLLAN_CANON"
    )
    require(
        all(
            "THRASYLLAN_COLLECTION_MEMBER" in e["scope_classes"]
            for e in letter_members
        ),
        "all thirteen Epistles carry THRASYLLAN_COLLECTION_MEMBER"
    )
    require(
        all(
            "LOST_ATTRIBUTION" in e["scope_classes"]
            and "ANCIENT_EXPLICIT_SPURIA" in e["scope_classes"]
            for e in lost
        ),
        "lost ancient spurious titles preserve both scope dimensions"
    )
    require(
        "ANTHOLOGICAL_ASCRIPTION" in epigrams["scope_classes"],
        "Epigrammata is explicitly separated as anthological attribution"
    )

    epigram_members=[
        e for e in entries
        if e.get("parent_catalog_id") == "TH.PLATO.CAT.EPIGRAMMATA"
    ]
    require(len(epigram_members) == 23, "Epigrammata collection has 23 individually addressable anthology members in the current inventory")
    refs={e["anthology_metadata"]["reference"] for e in epigram_members}
    expected_refs={
        "AP 5.78","AP 5.79","AP 5.80",
        "AP 6.1","AP 6.43",
        "AP 7.99","AP 7.100","AP 7.256","AP 7.259","AP 7.265","AP 7.268","AP 7.269","AP 7.669","AP 7.670",
        "AP 9.3","AP 9.39","AP 9.51","AP 9.506","AP 9.747","AP 9.823","AP 9.826",
        "AP 16.13","AP 16.248",
    }
    require(refs == expected_refs, "Epigram member references match the current Anthologia Graeca Plato inventory")
    ap16248=next(e for e in epigram_members if e["anthology_metadata"]["reference"] == "AP 16.248")
    require(
        ap16248["anthology_metadata"]["addressee_review_status"] if False else
        ap16248["anthology_metadata"]["attribution_review_status"] == "SOURCE_VERIFIED_WITH_COMPETING_ATTRIBUTION",
        "AP 16.248 preserves a competing attribution instead of flattening it"
    )

    extra_epistles=[
        e for e in entries
        if (e.get("provisional_work_code") or "").startswith("EXTRA_EPISTLE_HERCHER_")
    ]
    require(len(extra_epistles) == 9, "catalog includes nine extra-canonical Hercher-numbered Platonic epistles")
    expected_extra={14,15,24,25,26,30,31,70,85}
    actual_extra={
        int(e["provisional_work_code"].rsplit("_",1)[1])
        for e in extra_epistles
    }
    require(actual_extra == expected_extra, "extra-canonical epistle inventory matches current corpus-history scholarship")
    require(
        all("EXTRA_CANONICAL_EXTANT_ATTRIBUTION" in e["scope_classes"] for e in extra_epistles),
        "all extra-canonical epistles carry the correct historical scope class"
    )
    require(
        all(e["runtime_candidacy"] == "PENDING_REVIEW" for e in extra_epistles),
        "extra-canonical epistles are not automatically admitted to runtime"
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
