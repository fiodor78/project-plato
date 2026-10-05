#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "thinkers/plato/catalog/catalog-v0.1.5.json"
EPIGRAM_SCOPE = ROOT / "thinkers/plato/catalog/epigram-historical-scope-v0.1.1.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)
    print(f"PASS {message}")


def main() -> int:
    catalog=json.loads(CATALOG.read_text(encoding="utf-8"))
    scope=json.loads(EPIGRAM_SCOPE.read_text(encoding="utf-8"))
    entries=catalog["entries"]
    sources={s["source_id"] for s in catalog["sources"]}

    require(catalog["schema_version"]=="0.1.4", "catalog uses schema 0.1.4")
    require(catalog["catalog_version"]=="0.1.5", "catalog version is 0.1.5")
    require(len(entries)==109, "catalog v0.1.5 has 109 entries")

    ids=[e["catalog_id"] for e in entries]
    require(len(ids)==len(set(ids)), "catalog IDs are unique")

    referenced_sources={a["source_id"] for e in entries for a in e["attestations"]}
    require(referenced_sources <= sources, "every attestation source_id resolves")

    thrasyllan=[]
    positions=[]
    for e in entries:
        for a in e["attestations"]:
            if a["system"]=="THRASYLLAN_TETRALOGIES":
                thrasyllan.append(e)
                positions.append(a["position"])
    require(len(thrasyllan)==36, "Thrasyllan catalog contains exactly 36 tetralogical slots")
    require(set(positions)=={f"{t}.{p}" for t in range(1,10) for p in range(1,5)}, "all nine tetralogies contain positions 1–4 exactly once")

    epistles=next(e for e in entries if e["catalog_id"]=="TH.PLATO.CAT.EPISTLES")
    require(epistles["entry_type"]=="COLLECTION", "Epistles tetralogical slot is preserved as a collection")
    letter_members=[e for e in entries if e.get("parent_catalog_id")=="TH.PLATO.CAT.EPISTLES"]
    require(len(letter_members)==13, "Epistles collection has thirteen separately addressable members")

    expected_epistle_addressees={
        "I":["Dionysius II of Syracuse"], "II":["Dionysius II of Syracuse"], "III":["Dionysius II of Syracuse"],
        "IV":["Dion"], "V":["Perdiccas III of Macedon"], "VI":["Hermias of Atarneus","Erastus","Coriscus"],
        "VII":["Friends and associates of Dion"], "VIII":["Friends and associates of Dion"],
        "IX":["Archytas of Tarentum"], "X":["Aristodorus"], "XI":["Laodamas"],
        "XII":["Archytas of Tarentum"], "XIII":["Dionysius II of Syracuse"],
    }
    for letter in letter_members:
        meta=letter.get("epistolary_metadata")
        require(meta is not None, f"{letter['catalog_id']} has epistolary metadata")
        numeral=meta["traditional_number_roman"]
        require([a["label"] for a in meta["addressees"]]==expected_epistle_addressees[numeral], f"Epistle {numeral} addressee mapping is correct")
        require({"PLSRC.DL_3_57_62","PLSRC.BURY_EPISTLES_LOEB"} <= set(meta["source_refs"]), f"Epistle {numeral} addressee mapping has ancient and edition-level support")
    epistle_x=next(e for e in letter_members if e["catalog_id"]=="TH.PLATO.CAT.EPISTLE_X")
    require(epistle_x["epistolary_metadata"]["addressee_review_status"]=="SOURCE_VERIFIED_WITH_VARIANT", "Epistle X preserves Aristodemus/Aristodorus variant rather than flattening it")

    lost=[e for e in entries if e["survival_status"]=="LOST"]
    require(bool(lost), "catalog preserves ancient lost-title attestations")
    require(all(e["runtime_candidacy"]=="CATALOG_ONLY" for e in lost), "lost titles cannot become runtime text candidates")

    explicitly_spurious=[e for e in entries if any(a["status"]=="EXPLICITLY_SPURIOUS" for a in e["attestations"])]
    require(bool(explicitly_spurious), "ancient explicit spurious attestations are preserved")
    require(bool([e for e in explicitly_spurious if any(a["system"]=="BURNET_OCT_VOL5" for a in e["attestations"])]), "one entry can preserve overlapping ancient and editorial attestations")

    allowed_scope_classes={
        "THRASYLLAN_CANON","THRASYLLAN_COLLECTION_MEMBER","EXTRA_CANONICAL_EXTANT_ATTRIBUTION",
        "ANCIENT_EXPLICIT_SPURIA","LOST_ATTRIBUTION","ANTHOLOGICAL_ASCRIPTION","EPIGRAMMATIC_ASCRIPTION",
    }
    require(all(e.get("scope_classes") and set(e["scope_classes"]) <= allowed_scope_classes for e in entries), "every catalog entry has at least one valid historical scope class")
    require(all("THRASYLLAN_CANON" in e["scope_classes"] for e in thrasyllan), "all Thrasyllan slots carry THRASYLLAN_CANON")
    require(all("THRASYLLAN_COLLECTION_MEMBER" in e["scope_classes"] for e in letter_members), "all thirteen Epistles carry THRASYLLAN_COLLECTION_MEMBER")
    require(all("LOST_ATTRIBUTION" in e["scope_classes"] and "ANCIENT_EXPLICIT_SPURIA" in e["scope_classes"] for e in lost), "lost ancient spurious titles preserve both scope dimensions")

    epigrammata=next(e for e in entries if e["catalog_id"]=="TH.PLATO.CAT.EPIGRAMMATA")
    require(epigrammata["entry_type"]=="ANTHOLOGY_COLLECTION" and epigrammata["runtime_candidacy"]=="PENDING_REVIEW", "Epigrammata collection remains outside automatic runtime admission")
    require({"ANTHOLOGICAL_ASCRIPTION","EPIGRAMMATIC_ASCRIPTION"} <= set(epigrammata["scope_classes"]), "Epigrammata collection records both anthology transmission and epigrammatic attribution scope")

    epigram_members=[e for e in entries if e.get("parent_catalog_id")=="TH.PLATO.CAT.EPIGRAMMATA"]
    require(len(epigram_members)==37, "Epigrammata collection has 37 source-complete historical members")
    require(all(e.get("epigrammatic_metadata") is not None for e in epigram_members), "all 37 epigram members have epigrammatic identity metadata")
    historical_ids={e["epigrammatic_metadata"]["historical_scope_id"] for e in epigram_members}
    scope_ids={x["scope_id"] for x in scope["items"]}
    require(len(historical_ids)==37 and historical_ids==scope_ids, "catalog epigram identities match the 37-item historical scope exactly")
    require(all("EPIGRAMMATIC_ASCRIPTION" in e["scope_classes"] for e in epigram_members), "all epigram members carry EPIGRAMMATIC_ASCRIPTION")
    require(all(e["runtime_candidacy"]!="TEXT_CANDIDATE" for e in epigram_members), "no epigram enters philosopher-Plato runtime automatically")

    homonyms=[e for e in epigram_members if e["epigrammatic_metadata"]["profile_relation"]=="HOMONYM_EXCLUDED"]
    require(len(homonyms)==8, "eight homonym-excluded epigram objects are explicit")
    require(all(e["runtime_candidacy"]=="CATALOG_ONLY" for e in homonyms), "all homonym-excluded epigrams are catalog-only")

    legacy_anthology=[e for e in epigram_members if e.get("anthology_metadata") is not None]
    require(len(legacy_anthology)==23, "the original 23 digital-index members retain legacy anthology metadata")
    ap16248=next(e for e in legacy_anthology if e["catalog_id"]=="TH.PLATO.CAT.EPIGRAM_16_248")
    require(ap16248["anthology_metadata"]["attribution_review_status"]=="SOURCE_VERIFIED_WITH_COMPETING_ATTRIBUTION", "AP 16.248 preserves competing attribution in legacy anthology metadata")

    archeanassa=next(e for e in epigram_members if e["catalog_id"]=="TH.PLATO.CAT.EPIGRAM_ARCHEANASSA")
    cougny=next(e for e in epigram_members if e["catalog_id"]=="TH.PLATO.CAT.EPIGRAM_COUGNY_III_33")
    require("ANTHOLOGICAL_ASCRIPTION" not in archeanassa["scope_classes"], "Archeanassa logical object is not falsely reduced to anthology transmission")
    require("ANTHOLOGICAL_ASCRIPTION" not in cougny["scope_classes"], "Cougny III 33 logical object is not falsely reduced to anthology transmission")

    extra_epistles=[e for e in entries if (e.get("provisional_work_code") or "").startswith("EXTRA_EPISTLE_HERCHER_")]
    require(len(extra_epistles)==9, "catalog includes nine extra-canonical Hercher-numbered Platonic epistles")
    require({int(e["provisional_work_code"].rsplit("_",1)[1]) for e in extra_epistles}=={14,15,24,25,26,30,31,70,85}, "extra-canonical epistle inventory matches current corpus-history scholarship")
    require(all("EXTRA_CANONICAL_EXTANT_ATTRIBUTION" in e["scope_classes"] for e in extra_epistles), "all extra-canonical epistles carry the correct historical scope class")
    require(all(e["runtime_candidacy"]=="PENDING_REVIEW" for e in extra_epistles), "extra-canonical epistles are not automatically admitted to runtime")
    require(all(e["runtime_visibility"]=="CUSTODIAN_ONLY" for e in entries), "historical catalog metadata is CUSTODIAN-only")

    counts=Counter(e["entry_type"] for e in entries)
    print("\nCatalog entry counts:")
    for k in sorted(counts):
        print(f"  {k}: {counts[k]}")
    print(f"  TOTAL: {len(entries)}")
    print("\nPhase 1 catalog structural gate passed.")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
