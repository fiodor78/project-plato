#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "fixtures" / "phase0"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_dir(name: str):
    out = []
    for path in sorted((FIX / name).glob("*.json")):
        obj = load_json(path)
        obj["_fixture_path"] = str(path.relative_to(ROOT))
        out.append(obj)
    return out


def require(condition: bool, message: str):
    if not condition:
        raise AssertionError(message)
    print(f"PASS {message}")


def main() -> int:
    profile = load_json(ROOT / "thinkers/plato/profile/profile.json")
    thinker_id = profile["thinker_id"]

    corpus = load_dir("corpus")
    memories = load_dir("memory")
    provenance = load_dir("provenance")
    retrievals = load_dir("retrieval")
    ingestion = load_dir("ingestion")
    annotations = load_dir("annotations")

    require(thinker_id == "TH.PLATO", "Plato profile has an explicit thinker_id")

    scoped_objects = [
        x for x in corpus + memories + provenance + retrievals + ingestion + annotations
        if x.get("thinker_id") is not None
    ]
    require(
        scoped_objects and all(x.get("thinker_id") == thinker_id for x in scoped_objects),
        "all Plato fixtures are thinker-scoped consistently"
    )

    # Validate profile-specific locator semantics separately from the generic core schema.
    locator_def = profile["locator_schemes"][0]
    locator_schema = load_json(ROOT / locator_def["profile_validator"])
    locator_validator = Draft202012Validator(locator_schema)

    locator_objects = []
    for item in corpus:
        if "locator" in item:
            locator_objects.append(item["locator"])
        if item.get("canonical_range"):
            locator_objects.extend([
                item["canonical_range"]["start"],
                item["canonical_range"]["end"],
            ])
    for event in retrievals:
        locator = event.get("query", {}).get("locator")
        if locator:
            locator_objects.append(locator)

    require(bool(locator_objects), "Plato fixtures contain canonical locators")
    require(
        all(not list(locator_validator.iter_errors(loc)) for loc in locator_objects),
        "all Plato locators validate through the Stephanus profile adapter"
    )

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
    require(len(same_seg_witnesses) >= 2, "two textual witnesses attach to the same segment")
    require(
        len({w["edition_id"] for w in same_seg_witnesses}) >= 2,
        "textual witnesses come from distinct editions"
    )

    require(any(t["segment_id"] == seg for t in translations), "translation attaches without changing segment identity")
    require(any(s["segment_id"] == seg for s in speakers), "speaker assertion attaches without changing segment identity")
    require(
        authenticity and all(a["runtime_visibility"] == "CUSTODIAN_ONLY" for a in authenticity),
        "authenticity classification is CUSTODIAN-only"
    )

    visible = [
        x for x in corpus
        if x.get("runtime_visibility") == "THINKER_VISIBLE"
    ]
    require(bool(visible), "runtime corpus contains explicitly THINKER_VISIBLE objects")
    require(
        all(x.get("entity_type") != "authenticity_assertion" for x in visible),
        "authenticity assertions cannot enter the Thinker-visible projection"
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
    require(
        seg in inf["derived_from"] and acq_id in inf["derived_from"],
        "inference explicitly derives from ORIGINAL corpus + ACQUIRED memory"
    )

    prov_by_subject = {p["subject_id"]: p for p in provenance}
    require(inf["memory_id"] in prov_by_subject, "inference has a provenance record")
    inf_sources = {s["source_id"] for s in prov_by_subject[inf["memory_id"]]["sources"]}
    require({seg, acq_id}.issubset(inf_sources), "provenance records both mixed-origin sources")

    require(acq_id in prov_by_subject, "acquired memory has testimony provenance")
    acq_source_kinds = {s["source_kind"] for s in prov_by_subject[acq_id]["sources"]}
    require("USER_UTTERANCE" in acq_source_kinds, "acquired knowledge traces back to interlocutor testimony")

    require(bool(annotations), "discourse annotation fixtures exist")
    require(
        all(a["segment_id"] == seg for a in annotations),
        "discourse annotations attach without changing logical segment identity"
    )
    require(
        any(a["scope"] == "SEGMENT" and a["frame_depth"] == 0 for a in annotations),
        "outer discourse frame is represented"
    )
    require(
        any(a["scope"] == "WITNESS_SPAN" and a["frame_depth"] > 0 for a in annotations),
        "nested witness-specific discourse frame is represented"
    )
    for annotation in annotations:
        if annotation["scope"] == "WITNESS_SPAN":
            span = annotation["span"]
            require(span["end_char"] > span["start_char"], "witness-span offsets are non-empty")
            require(bool(annotation["normalized_text_sha256"]), "witness-span annotation pins normalized text checksum")

    require(bool(ingestion), "immutable source-asset fixture exists")
    require(
        all("sha256" in x for x in ingestion if x.get("entity_type") == "source_asset"),
        "source assets are checksum-addressed"
    )

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
