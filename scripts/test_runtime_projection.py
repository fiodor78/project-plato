#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from runtime.projection import build_corpus_model_payload


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def main() -> int:
    corpus = [
        load_json(path)
        for path in sorted((ROOT / "fixtures/phase0/corpus").glob("*.json"))
    ]
    config = load_json(ROOT / "thinkers/plato/profile/runtime-projection.json")

    payload = build_corpus_model_payload(corpus, config)
    serialized = json.dumps(payload, ensure_ascii=False, sort_keys=True)

    assert payload, "projection produced no model payload"

    # Positive controls: epistemically permitted information survives.
    assert "1a" in serialized
    assert "Synthetic Speaker" in serialized
    assert "SYNTHETIC GREEK WITNESS" in serialized
    assert "SYNTETYCZNY PRZEKŁAD" in serialized

    # Negative controls: technical and modern editorial metadata must not survive.
    forbidden_field_names = [
        "thinker_id",
        "work_id",
        "segment_id",
        "witness_id",
        "translation_id",
        "assertion_id",
        "edition_id",
        "runtime_visibility",
        "source_checksum",
        "source_uri",
        "publication_year",
        "editor_or_translator",
        "redistribution_status",
        "license_ref",
        "custodian_notes",
        "classification",
        "classification_label",
        "classification_system",
        "basis_ref",
        "basis_refs",
        "rationale",
    ]
    for field in forbidden_field_names:
        assert f'"{field}"' not in serialized, f"hidden field leaked: {field}"

    forbidden_values = [
        "SYNTHETIC_TEST",
        "SYNTHETIC_TEST_B",
        "SYNTHETIC_TRANSLATION",
        "PSEUDO_PLATONIC",
        "PUBLIC_DOMAIN_CONFIRMED",
        "example.invalid",
        "Synthetic fixture edition; not a scholarly source.",
        "Second synthetic fixture edition; not a scholarly source.",
        "01a108c0-",  # UUIDv7 creation-time-bearing technical identifiers
    ]
    for value in forbidden_values:
        assert value not in serialized, f"hidden value leaked: {value}"

    print(json.dumps(payload, ensure_ascii=False, indent=2))
    print("\nRuntime epistemic projection leakage test passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
