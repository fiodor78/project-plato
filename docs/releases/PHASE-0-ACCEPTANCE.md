# PHASE 0 ACCEPTANCE — architecture gate

**Status:** Accepted  
**Project:** PROJECT PLATO / Thinker Framework  
**Acceptance basis:** GitHub Actions Phase 0 validation run `37236432320` completed successfully.

## Purpose

Phase 0 existed to prevent the project from ingesting a large philosophical corpus before the experiment's identities, epistemic boundaries, provenance rules, memory model and reproducibility requirements were explicit and testable.

This document records that the architecture gate has been passed for the **first production-ingestion iteration**.

It does not claim that the architecture is final forever. Later changes remain possible, but incompatible changes must preserve migration/provenance history and must not silently rewrite frozen experimental states.

## Accepted capabilities

The Phase 0 implementation demonstrates:

1. **Generic Thinker architecture** — reusable Core, philosopher-specific Profile, isolated running Instance.
2. **CUSTODIAN / Thinker separation** — modern research and hidden metadata remain outside the active thinker's epistemic world by default.
3. **Stable identity** — opaque runtime objects use UUIDv7; scholarly locators are separate from machine identity.
4. **Immutable original knowledge** — ORIGINAL resolves through frozen corpus manifests rather than mutable memory.
5. **Mutable epistemic memory** — ACQUIRED, EPISODIC and INFERENCE are structurally distinct.
6. **Provenance** — acquired claims and mixed-origin inferences can be traced to explicit sources.
7. **Dual retrieval design** — deterministic structural retrieval and semantic discovery resolve to stable corpus objects.
8. **Deny-by-default runtime projection** — model context is an allow-listed projection, not a raw storage record.
9. **Leakage tests** — modern edition metadata, source URLs, authenticity labels, technical IDs and other hidden values are checked for non-disclosure.
10. **Immutable/checksummed source assets** — acquisition and transformation lineage can be reproduced.
11. **Release/snapshot lineage** — frozen baselines can produce divergent experimental descendants.
12. **Generic locator abstraction** — Plato uses a Stephanus adapter without hard-coding Stephanus into Thinker Core.
13. **Segmentation policy** — canonical segments are locator-bounded and may use profile-defined structural boundaries.
14. **Discourse annotation** — narrator/speaker/embedded quotation/nested frames can be represented separately from segment identity, including witness-specific spans pinned to normalized-text checksums.
15. **Automated validation** — schemas, fixtures, the synthetic ingestion gate and runtime projection leakage checks execute in CI.

## Evidence

The acceptance CI run completed successfully with these stages:

- JSON Schema and fixture validation;
- synthetic Phase 0 ingestion gate;
- runtime epistemic projection leakage test.

Segmentation policy was also tested against representative real structural patterns from Platonic material without yet treating those sources as production-ingested corpus objects. See:

- `docs/research/SEGMENTATION-PILOT-0001.md`
- `docs/specs/SPEC-0002-segmentation-speakers.md`

## Frozen-for-ingestion decisions

For the first production-ingestion iteration:

- opaque generated object IDs: UUIDv7;
- logical segment identity is independent of edition, speaker and scholarly locator;
- profile locator for Plato: Stephanus;
- source editions: CUSTODIAN-only metadata;
- runtime visibility: deny by default plus field allow-list;
- ORIGINAL: immutable corpus view;
- canonical segmentation: locator boundary plus explicit profile structural boundary;
- discourse/voice: annotation layer, not segment identity.

## Known limitations accepted for Phase 1

- The underlying language model still contains latent modern knowledge; Phase 0 controls admissible use rather than deleting such knowledge from model weights.
- Semantic retrieval implementation remains replaceable; Phase 0 freezes the provenance requirement, not one embedding model.
- The production database technology is not yet frozen; data contracts are intended to be storage-independent.
- Plato-specific work catalog and authenticity classifications are intentionally deferred to Phase 1.
- Production Greek source editions and redistribution rights are intentionally deferred to Phase 2.
- GitHub Pages requires a one-time repository setting to be enabled; this does not block corpus architecture.
- Speaker/discourse annotations may be refined as production material exposes edge cases; frozen releases must retain historical mappings.

## Exit decision

**Phase 0 is closed. Phase 1 may begin.**

The next authoritative task is to define the scope and taxonomy of the historical Corpus Platonicum, then build the work catalog before source-text ingestion.
