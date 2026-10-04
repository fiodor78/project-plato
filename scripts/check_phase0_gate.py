#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "fixtures" / "phase0"


def load_dir(name: str):
    out = []
    for path in sorted((FIX / name).glob("*.json")):
        with path.open("r", encoding="utf-8") as f:
            obj = json.load(f)
        obj["_fixture_path"] = str(path.relative_to(ROOT))
        out.append(obj)
    return out


def require(condition: bool, message: str):
    if not condition:
        raise AssertionError(message)
    print(f"PASS {message}")


def main() -> int:
    corpus = load_dir("corpus")
    memories = load_dir("memory")
    provenance = load_dir("provenance")
    retrievals = load_dir("retrieval")
    ingestion = load_dir("ingestion")

    works = [x for x in corpus if x.get("entity_type") == "work"]
    segments = [x for x in corpus if x.get("entity_type") == "segment"]
    witnesses = [x for x in corpus if x.get("entity_type") == "textual_witness"]
    translations = [x for x in corpus if x.get("entity_type") == "translation"]
    speakers = [x for x in corpus if x.get("entity_type") == "speaker_assertion"]
    authenticity = [x for x in corpus if x.get("entity_type") == "authenticity_assertion"]

    require(bool(works), "fixture registers a work")
    require(bool(segments), "fixture creates a logical segment")

    seg = segments[0]["segment_id"]
    same_seg_witnesses = [w for w in witnesses if w["segment_id"] == seg]
    require(len(same_seg_witnesses) >= 2, "two Greek witnesses attach to the same segment")
    require(
        len({w["edition_id"] for w in same_seg_witnesses}) >= 2,
        "Greek witnesses come from distinct editions"
    )

    require(any(t["segment_id"] == seg for t in translations), "translation attaches without changing segment identity")
    require(any(s["segment_id"] == seg for s in speakers), "speaker assertion attaches without changing segment identity")
    require(
        authenticity and all(a["runtime_visibility"] == "CUSTODIAN_ONLY" for a in authenticity),
        "authenticity classification is CUSTODIAN-only"
    )

    require(bool(retrievals), "structural retrieval event exists")
    selected = [
        r for event in retrievals
        for r in event.get("results", [])
        if r.get("selected_for_context")
    ]
    require(any(r["segment_id"] == seg for r in selected), "structural retrieval selects the logical segment")

    acquired = [m for m in memories if m["memory_type"] == "ACQUIRED"]
    inferred = [m for m in memories if m["memory_type"] == "INFERENCE"]
    require(bool(acquired), "acquired memory exists")
    require(bool(inferred), "inference memory exists")

    acq_id = acquired[0]["memory_id"]
    inf = inferred[0]
    require(seg in inf["derived_from"] and acq_id in inf["derived_from"],
            "inference explicitly derives from ORIGINAL corpus + ACQUIRED memory")

    prov_by_subject = {p["subject_id"]: p for p in provenance}
    require(inf["memory_id"] in prov_by_subject, "inference has a provenance record")
    inf_sources = {s["source_id"] for s in prov_by_subject[inf["memory_id"]]["sources"]}
    require({seg, acq_id}.issubset(inf_sources), "provenance records both mixed-origin sources")

    require(acq_id in prov_by_subject, "acquired memory has testimony provenance")
    acq_source_kinds = {s["source_kind"] for s in prov_by_subject[acq_id]["sources"]}
    require("USER_UTTERANCE" in acq_source_kinds, "acquired knowledge traces back to interlocutor testimony")

    require(bool(ingestion), "immutable source-asset fixture exists")
    require(all("sha256" in x for x in ingestion if x.get("entity_type") == "source_asset"),
            "source assets are checksum-addressed")

    print("\nTRACE where-did-this-come-from:")
    print(f"  {inf['memory_id']}")
    print(f"    <- ORIGINAL {seg}")
    print(f"    <- ACQUIRED {acq_id}")
    for source in prov_by_subject[acq_id]["sources"]:
        print(f"         <- {source['source_kind']} {source['source_id']}")

    print("\nFull Phase 0 synthetic ingestion gate passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
