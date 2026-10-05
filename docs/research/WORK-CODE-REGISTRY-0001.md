# WORK-CODE REGISTRY 0001 — partial freeze

**Status:** Phase 1 partial freeze

## Decision

PROJECT PLATO now freezes semantic codes for every current catalog entity **except individual Epigrammata members**.

The registry is intentionally marked `PARTIAL_FROZEN`, not fully frozen.

## Stable ID rule

For current catalog entities, the stable code is the catalog suffix. Examples:

- `TH.PLATO.CAT.REPUBLIC` → `TH.PLATO.WORK.REPUBLIC`
- `TH.PLATO.CAT.EPISTLES` → `TH.PLATO.COLLECTION.EPISTLES`
- `TH.PLATO.CAT.MIDON` → `TH.PLATO.LOST.MIDON`

This prioritizes stability and transparent mapping over short scholarly abbreviations.

A later display layer may expose aliases such as `REP`, but aliases must never replace canonical semantic identity.

## Scope

The current registry freezes 72 semantic codes.

It includes:

- Thrasyllan works and collections;
- the thirteen individual Epistles;
- extra-canonical dialogues and spuria;
- lost attributed titles;
- extra-canonical Hercher epistles;
- the Epigrammata **collection identity** itself.

It excludes the 23 current individual Epigrammata members because their historical scope and homonymy layer remain under reconstruction against Pelucchi 2026.

## Independence from authenticity

A stable work code means only that PROJECT PLATO has stabilized the identity of a catalog object.

It does **not** mean:

- Plato authored the text;
- the object is runtime-admissible;
- the authenticity grade is frozen;
- a lost title has surviving text.

## Epigram rule

No individual epigram code may be frozen until:

1. the Pelucchi 2026 37-text scope is captured;
2. witness-vs-logical-text relations are resolved;
3. Plato Junior / Plato Comicus / unresolved homonymy is represented;
4. catalog v0.1.5 is created and passes migration gates.

## Artifacts

- `thinkers/plato/profile/work-registry.schema.json`
- `thinkers/plato/profile/work-registry-v0.1.0.json`
- `scripts/check_work_registry.py`
