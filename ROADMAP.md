# Phase 0 roadmap

## Completed

- [x] Public canonical GitHub repository established.
- [x] CUSTODIAN / PLATO logical separation accepted.
- [x] Provenance-first epistemic architecture accepted.
- [x] Edition-independent segment identity accepted.
- [x] Structural + semantic retrieval accepted.
- [x] ORIGINAL defined as an immutable corpus view.
- [x] Initial Corpus schema v0.1.0.
- [x] Initial Memory schema v0.1.0.
- [x] Initial Provenance schema v0.1.0.

## Next

- [ ] Define corpus manifest and release manifest schemas.
- [ ] Define source-ingestion record and checksum policy.
- [ ] Freeze work-code registry after Corpus Platonicum catalog review.
- [ ] Define segmentation policy and speaker-annotation policy.
- [ ] Define CUSTODIAN/PLATO field-level access projection.
- [ ] Define retrieval event schema.
- [ ] Define instance snapshot and lineage model.
- [ ] Add automated JSON Schema validation.
- [ ] Build minimal fixture corpus for architecture tests.
- [ ] Pass Phase 0 ingestion gate.

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
