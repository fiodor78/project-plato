# SPEC-0001 — PROJECT PLATO Phase 0 architecture

**Status:** Active specification

## Purpose

Phase 0 defines the data, governance and runtime boundaries that must exist before Corpus Platonicum is ingested.

No source text is considered production corpus until its target schema, provenance model and storage role are defined.

## Logical project zones

- **Governance** — ADRs, specifications, roadmap and registers.
- **Custodian** — research, source collection, audits and working material.
- **Corpus** — catalog, Greek sources, translations, metadata, normalized data, textual variants and licensing records.
- **Schemas** — machine-readable definitions for corpus, memory and provenance.
- **Plato Core** — epistemic/personality constitutions, retrieval and runtime design.
- **Memory** — memory-system design and snapshots.
- **Tests** — leakage, corpus, memory, adversarial and baseline tests.
- **Experiments** — protocols and experimental runs.
- **Releases** — frozen PLATO releases.
- **Archive** — superseded or retired material.

## Phase 0 deliverables

1. Corpus data model.
2. Memory data model.
3. Provenance data model.
4. Stable identifier convention.
5. Structural + semantic retrieval architecture.
6. Logical access model for CUSTODIAN and PLATO.
7. Versioning and snapshot model.
8. Migration plan from working storage to runtime infrastructure.
9. Acceptance criteria for beginning corpus ingestion.

## Working rule

GitHub is the canonical repository. Google Drive is complementary working/source storage.

## Exit condition

Phase 0 is complete when the schemas and access boundaries are precise enough that the first Greek source can be ingested deterministically, assigned stable identifiers, traced to its source and retrieved without exposing forbidden CUSTODIAN metadata to PLATO.
