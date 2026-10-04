#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]

TARGETS = {
    ROOT / "schemas/corpus/corpus.schema.json": ROOT / "fixtures/phase0/corpus",
    ROOT / "schemas/memory/memory.schema.json": ROOT / "fixtures/phase0/memory",
    ROOT / "schemas/provenance/provenance.schema.json": ROOT / "fixtures/phase0/provenance",
    ROOT / "schemas/releases/corpus-manifest.schema.json": ROOT / "fixtures/phase0/releases",
    ROOT / "schemas/retrieval/retrieval-event.schema.json": ROOT / "fixtures/phase0/retrieval",
    ROOT / "schemas/releases/thinker-snapshot.schema.json": ROOT / "fixtures/phase0/releases",
    ROOT / "schemas/ingestion/source-asset.schema.json": ROOT / "fixtures/phase0/ingestion",
    ROOT / "schemas/framework/thinker-profile.schema.json": ROOT / "thinkers/plato/profile",
    ROOT / "schemas/runtime/runtime-projection.schema.json": ROOT / "thinkers/plato/profile",
    ROOT / "schemas/annotations/discourse-annotation.schema.json": ROOT / "fixtures/phase0/annotations",
    ROOT / "thinkers/plato/catalog/catalog.schema.json": ROOT / "thinkers/plato/catalog",
}


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def main() -> int:
    failures = 0

    for schema_path, fixture_dir in TARGETS.items():
        schema = load_json(schema_path)
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())

        fixtures = sorted(fixture_dir.glob("*.json"))
        if not fixtures:
            print(f"ERROR: no JSON candidates found in {fixture_dir.relative_to(ROOT)}")
            failures += 1
            continue

        matched = 0
        for fixture_path in fixtures:
            instance = load_json(fixture_path)
            errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
            if errors:
                continue
            matched += 1
            print(f"PASS {fixture_path.relative_to(ROOT)} against {schema_path.relative_to(ROOT)}")

        if matched == 0:
            failures += 1
            print(
                f"FAIL: no candidate in {fixture_dir.relative_to(ROOT)} "
                f"validated against {schema_path.relative_to(ROOT)}"
            )

    if failures:
        print(f"\nValidation failed: {failures} schema target(s) have no valid object.")
        return 1

    print("\nAll Phase 0 schema targets have at least one valid object.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
