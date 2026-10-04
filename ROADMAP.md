# Phase 0 roadmap

## Completed

- [x] Public canonical GitHub repository established.
- [x] CUSTODIAN / PLATO logical separation accepted.
- [x] Provenance-first epistemic architecture accepted.
- [x] Edition-independent segment identity accepted.
- [x] Structural + semantic retrieval accepted.
- [x] ORIGINAL defined as an immutable corpus view.
- [x] Deny-by-default runtime visibility projection accepted.
- [x] Immutable corpus-release and PLATO-baseline model accepted.
- [x] Initial Corpus schema v0.1.0.
- [x] Initial Memory schema v0.1.0.
- [x] Initial Provenance schema v0.1.0.
- [x] Corpus manifest schema v0.1.0.
- [x] Retrieval-event schema v0.1.0.
- [x] PLATO snapshot/lineage schema v0.1.0.
- [x] Automated JSON Schema validation.
- [x] Minimal synthetic fixture corpus for architecture tests.

## Next

- [ ] Define source-ingestion record and checksum policy.
- [ ] Define segmentation policy and speaker-annotation policy.
- [ ] Freeze work-code registry after Corpus Platonicum catalog review.
- [ ] Add a second textual witness and a translation to the fixture.
- [ ] Add inference-memory fixture derived from corpus + acquired testimony.
- [ ] Add leakage tests for runtime visibility.
- [ ] Pass the full Phase 0 ingestion gate.

## Phase 0 ingestion gate

Corpus ingestion may begin only when a test fixture can:

1. register a work;
2. create stable logical segments;
3. attach two independent Greek textual witnesses to the same segment;
4. attach a translation without changing segment identity;
5. attach/change a speaker assertion without changing segment identity;
6. attach a CUSTODIAN-only authenticity assertion;
7. retrieve a passage structurally;
8. record retrieval provenance;
9. create an acquired memory and an inference derived from corpus + acquired memory;
10. answer "where did this come from?" from provenance rather than free-form model reconstruction.
