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
            print(f"ERROR: no fixtures found in {fixture_dir.relative_to(ROOT)}")
            failures += 1
            continue

        for fixture_path in fixtures:
            instance = load_json(fixture_path)
            errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
            label = fixture_path.relative_to(ROOT)
            if errors:
                failures += 1
                print(f"FAIL {label}")
                for error in errors:
                    where = ".".join(str(p) for p in error.path) or "<root>"
                    print(f"  {where}: {error.message}")
            else:
                print(f"PASS {label}")

    if failures:
        print(f"\nValidation failed: {failures} fixture/schema failure(s).")
        return 1

    print("\nAll Phase 0 schema fixtures are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
