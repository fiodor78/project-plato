# PROJECT PLATO roadmap

## Completed

- [x] Public canonical GitHub repository established.
- [x] CUSTODIAN / thinker logical separation accepted.
- [x] Provenance-first epistemic architecture accepted.
- [x] Edition-independent logical segment identity accepted.
- [x] Structural + semantic retrieval accepted.
- [x] ORIGINAL defined as an immutable corpus view.
- [x] Deny-by-default runtime visibility projection accepted.
- [x] Immutable corpus-release and instance-baseline model accepted.
- [x] Source assets made immutable and checksum-addressed.
- [x] Generic Thinker Core / Profile / Instance architecture accepted.
- [x] Plato moved conceptually into an isolated Thinker Profile.
- [x] Generic locator abstraction introduced.
- [x] Plato Stephanus locator adapter created.
- [x] Generic Corpus schema v0.2.0.
- [x] Generic Memory schema v0.2.0.
- [x] Generic Provenance schema v0.2.0.
- [x] Generic release/retrieval/snapshot schemas v0.2.0.
- [x] Thinker Profile schema created.
- [x] Synthetic fixtures include two witnesses, a translation, speaker assertion, acquired memory and mixed-origin inference.
- [x] Automated validation and executable Phase 0 ingestion gate.
- [x] Provider-neutral LanguageEngine architecture accepted; OpenRouter chosen as the preferred first production gateway with pinned routing for frozen baselines.

## Phase 0 — accepted

- [x] Verify full CI after the generic-framework migration.
- [x] Add explicit runtime-projection leakage tests (including hidden edition metadata).
- [x] Freeze generated-ID strategy (UUIDv7 for opaque runtime objects).
- [x] Test segmentation policy on representative real source structures without ingesting the complete corpus.
- [x] Validate nested discourse annotations in CI.
- [x] Freeze SPEC-0002 for the first ingestion iteration.
- [x] Pass the final Phase 0 architecture gate.

## Phase 1 — Corpus Platonicum catalog

- [x] Define attestation-based historical scope and catalog schema.
- [x] Create initial 63-entry catalog inventory and automated structural gate.
- [x] Define modern-authenticity assessment methodology and assertion schema.
- [x] Verify all 13 Epistle addressees and preserve the Letter X Aristodemus/Aristodorus variant.
- [x] Define and freeze the historical corpus-scope taxonomy (Thrasyllian canon, extra-canonical extant attributions, ancient spuria/lost titles, anthological attributions).
- [ ] Build the full Corpus Platonicum catalog.
  - [x] Split Epigrammata into 23 individually addressable Greek Anthology attributions (provisional member inventory).
  - [x] Add machine-readable 31-row Page/Massimo epigram crosswalk with explicit Plato / Plato Junior / homonymy handling and CI gate.
  - [x] Add deterministic pre-v0.1.5 epigram migration-plan gate; catalog mutation remains blocked until Pelucchi 2026 numbering is captured.
  - [ ] Complete the crosswalk against Pelucchi 2026 and expand the provisional 23-item inventory to the complete ancient attribution corpus.
  - [x] Add nine extra-canonical epistles (Hercher 14, 15, 24, 25, 26, 30, 31, 70, 85) identified by recent corpus-history scholarship.
- [ ] Establish profile-specific A/B/C/D attribution classifications with cited scholarly basis.
  - [x] Add automated authenticity coverage gate and explicit unresolved queues.
  - [x] Classify Epistles I and XII as high-confidence D cases with cited evidence.
  - [x] Classify Epistle VII as B (genuinely disputed) with evidence for both sides.
  - [x] Classify Epistle VIII as C (probably inauthentic; older acceptance preserved as reception history).
  - [x] Complete provisional A/B/C/D coverage for all thirteen canonical Epistles.
  - [x] Complete provisional A/B/C/D coverage for all nine extra-canonical Epistles (Hercher 14, 15, 24, 25, 26, 30, 31, 70, 85).
  - [x] Classify first Thrasyllan dubia tranche: B for Alcibiades I, Hippias Major, Clitophon; C for Alcibiades II, Hipparchus, Rival Lovers, Theages, Minos, Epinomis.
  - [x] Classify Definitions, On Justice and On Virtue as high-confidence D cases.
  - [x] Classify 26 core dialogues as provisional A (strongly accepted as Platonic).
- [ ] Freeze Plato work-code registry.
  - [x] Freeze 72 non-epigram semantic codes in a `PARTIAL_FROZEN` registry; defer the 23 current Epigrammata members until the historical epigram scope is resolved.

## Phase 2 — source editions and ingestion

- [ ] Select and register Greek source editions.
- [ ] Verify legal/redistribution status.
- [ ] Begin deterministic real corpus ingestion.
