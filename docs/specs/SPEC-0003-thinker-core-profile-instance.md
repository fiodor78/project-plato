# SPEC-0003 — Thinker Core / Profile / Instance architecture

**Status:** Active Phase 0 specification

## Objective

Define a reusable architecture for historically grounded epistemically constrained philosopher agents while preserving strict isolation between individual thinkers.

## Object hierarchy

```text
THINKER CORE
  |
  +-- Thinker Profile: PLATO
  |     +-- Corpus release
  |     +-- Epistemic constitution
  |     +-- Cognitive/personality constitution
  |     +-- Citation adapter: STEPHANUS
  |     +-- Profile tests
  |
  +-- Thinker Profile: ARISTOTLE
        +-- Corpus release
        +-- Citation adapter: BEKKER
        +-- Profile tests

Frozen profile release
  |
  +-- Thinker Instance A
  +-- Thinker Instance B
```

## Generic core entities

The following must be philosopher-neutral:

- Thinker
- Work
- Segment
- Canonical locator
- Source asset
- Textual witness
- Translation
- Annotation/assertion
- Mutable memory
- Provenance
- Retrieval event
- Corpus manifest
- Profile release
- Instance snapshot
- Experiment run

## Profile-owned entities

A profile owns:

- corpus inclusion decisions;
- work-code registry;
- citation schemes;
- source editions;
- authenticity/attribution assertions;
- speaker/narrator annotations;
- profile-specific semantic concepts;
- epistemic constitution extensions;
- personality reconstruction;
- profile-specific red-team tests.

## Canonical locator

The generic structure is:

```json
{
  "scheme": "STEPHANUS",
  "value": "514a",
  "components": {
    "page": 514,
    "section": "a"
  }
}
```

or:

```json
{
  "scheme": "BEKKER",
  "value": "980a21",
  "components": {
    "page": 980,
    "column": "a",
    "line": 21
  }
}
```

The core treats `components` as profile-defined structured metadata. It validates the common envelope; profile validators validate scheme-specific details.

## Isolation

Each running instance binds to exactly one:

- thinker profile release;
- corpus manifest;
- mutable memory store;
- provenance namespace;
- experiment lineage.

No cross-profile retrieval occurs by default.

## Repository layout target

```text
framework/
  docs/
  schemas/
  runtime/
  tests/

thinkers/
  plato/
    profile/
    corpus/
    tests/
    releases/

docs/
  adr/
  specs/

experiments/
```

During migration, existing paths may remain temporarily for compatibility.

## Phase 0 implication

Before real Plato ingestion:

1. remove Stephanus-specific assumptions from generic schemas;
2. introduce `thinker_id`;
3. introduce generic locator envelope;
4. move Plato-specific validation into a profile layer;
5. update fixtures and CI;
6. supersede incompatible identifier examples from ADR-0004.
