# PROJECT PLATO

[![Phase 0 validation](https://github.com/fiodor78/project-plato/actions/workflows/schema-validation.yml/badge.svg)](https://github.com/fiodor78/project-plato/actions/workflows/schema-validation.yml)

**PROJECT PLATO** is an open research-and-engineering project exploring whether a language-model-based agent can be made to reason as an **epistemically constrained historical thinker**: grounded in an approved primary corpus, allowed to acquire new knowledge through controlled interaction, and required to preserve the provenance of what it knows.

Plato is the first reference profile. The underlying architecture is deliberately reusable for other philosophers.

> The project is not trying to “resurrect Plato,” prove historical identity, or produce a stylistic impersonation. It is an experiment in controlled knowledge, provenance, memory, retrieval and intellectual development.

## The research question

The motivating question is:

> If an agent begins with a controlled body of texts associated with a historical thinker, a reconstructed mode of inquiry derived from that corpus, and no permission to use later knowledge unless it is explicitly acquired, how does it reason about unfamiliar questions and a world it gradually learns about?

For the first profile, that becomes:

> If PLATO has access to an approved Corpus Platonicum, can distinguish original knowledge from later testimony and inference, and is prevented from freely using the base model's modern knowledge, how does it respond to new ideas, technologies and historical information?

## What this project is

PROJECT PLATO combines several concerns that are usually treated separately:

- corpus engineering and textual provenance;
- retrieval with exact scholarly locators;
- long-term memory with explicit epistemic classes;
- lineage and reproducibility of experimental agents;
- source attribution and derivation graphs;
- isolation of hidden modern metadata from the active thinker;
- adversarial testing for latent-knowledge leakage;
- reusable thinker profiles for different historical authors.

The project is being built in public so that its assumptions, trade-offs and failures can be inspected.

## What this project is not

It is **not**:

- a claim that an LLM becomes the historical Plato;
- a generic “talk to Plato” role-play prompt;
- a modern philosophy tutor speaking in an archaic voice;
- an encyclopedia about Plato;
- a fine-tuned model whose learned weights are treated as auditable historical knowledge;
- an attempt to erase modern knowledge from the base model's weights.

The base model inevitably contains latent modern knowledge. The experiment therefore controls **permission to use knowledge**, not literal absence of knowledge from model parameters.

## Current maturity

**Status: Phase 0 accepted; Phase 1 (Corpus Platonicum catalog) has begun.**

The architecture, schemas, synthetic fixtures, runtime visibility model, segmentation/discourse model and CI integrity tests have passed the Phase 0 acceptance gate. Production corpus ingestion has **not** started yet; Phase 1 first establishes the historical corpus catalog, transmission classes and attribution metadata.

The accepted Phase 0 architecture demonstrates that it can:

1. assign stable logical identities independent of editions and scholarly locators;
2. align multiple textual witnesses and translations to one logical segment;
3. preserve speaker/narrator annotations separately from passage identity;
4. distinguish original, acquired, episodic and inferred knowledge;
5. trace conclusions through explicit provenance;
6. expose only approved fields to the active thinker;
7. keep modern editorial and CUSTODIAN-only metadata out of model context;
8. reproduce frozen baselines and descendant experimental lineages.

See [ROADMAP.md](ROADMAP.md) for the live status.

## Architecture

The project has three conceptual layers:

```text
                         THINKER CORE
             generic, reusable infrastructure
       corpus · memory · provenance · retrieval · tests
                              |
                +-------------+-------------+
                |                           |
         THINKER PROFILE              THINKER PROFILE
              PLATO                     future thinker
      Corpus Platonicum               e.g. Aristotle
      Stephanus adapter               Bekker adapter
      profile policies                profile policies
                |
         frozen profile release
                |
          +-----+-----+
          |           |
      PLATO-1.0-A  PLATO-1.0-B
      own memory    own memory
      own history   own history
```

### Thinker Core

The reusable layer contains:

- source ingestion and immutable source assets;
- logical corpus objects and textual witnesses;
- mutable memory;
- provenance;
- structural and semantic retrieval;
- runtime epistemic projection;
- release manifests and snapshots;
- integrity and leakage tests.

### Thinker Profile

A profile is philosopher-specific. It defines:

- corpus scope;
- work registry;
- citation/locator schemes;
- attribution/authenticity policy;
- speaker/narrator conventions where relevant;
- approved source editions and translations;
- epistemic-constitution extensions;
- cognitive/personality reconstruction;
- profile-specific tests.

PLATO is the first profile under [`thinkers/plato/`](thinkers/plato/).

### Thinker Instance

An instance is a running experimental lineage created from a frozen profile release.

Two instances can begin from the same baseline and later diverge through different conversations and acquired knowledge:

```text
PLATO-1.0-A
PLATO-1.0-B
```

Mutable memory is isolated per instance unless an experiment explicitly transfers information.

## CUSTODIAN and the active thinker

The project deliberately separates two roles.

### CUSTODIAN

CUSTODIAN is the external research, engineering and audit environment. It may:

- search the web;
- use modern scholarship;
- compare critical editions;
- classify attribution/authenticity;
- prepare corpus material;
- inspect logs and provenance;
- design tests;
- maintain the runtime and schemas.

### THINKER / PLATO

The active thinker may use only epistemically admissible material:

- approved ORIGINAL corpus material;
- ACQUIRED knowledge deliberately introduced during the experiment;
- EPISODIC memory from its own history;
- INFERENCE produced from admissible sources.

PLATO does not automatically have access to CUSTODIAN notes, hidden test expectations, modern editorial metadata, the web or external search.

## Epistemic model

The logical knowledge classes are:

| Class | Meaning |
|---|---|
| **ORIGINAL** | Read-only knowledge grounded in the frozen profile corpus |
| **ACQUIRED** | Information communicated after the instance begins |
| **EPISODIC** | Remembered interactions and events in that instance's history |
| **INFERENCE** | Conclusions derived from admissible sources |
| **PROVENANCE** | Audit lineage recording where claims and inferences came from |

A critical rule is:

> “The interlocutor told me X” is not the same thing as “X is true.”

Acquired claims therefore keep source and epistemic status rather than silently becoming historical fact.

ORIGINAL is implemented as a read-only view of a frozen corpus manifest, not as duplicated mutable memory.

## Provenance

The system is designed to answer questions such as:

> Where did this conclusion come from?

A derived conclusion may trace to multiple sources:

```text
Inference
├── ORIGINAL: corpus segment
├── ACQUIRED: interlocutor testimony
└── previous INFERENCE
```

This lineage is stored structurally rather than reconstructed after the fact by the language model.

## Corpus model

The project separates:

- **logical segment identity**;
- **scholarly locator**;
- **textual witness / edition**;
- **translation**;
- **speaker/narrator assertion**;
- **attribution/authenticity assessment**.

This allows an edition or speaker annotation to change without changing the identity of the underlying logical passage.

### Generic locators

The core does not hard-code one citation system.

Plato may use:

```json
{
  "scheme": "STEPHANUS",
  "value": "514a"
}
```

A future Aristotle profile may use Bekker numbers; another thinker may use aphorism, fragment or proposition numbering.

## Stable identifiers

Profile-owned semantic registries may use readable IDs, for example:

```text
TH.PLATO
TH.PLATO.WORK.REP
TH.PLATO.SPEAKER.SOCRATES
```

Opaque runtime-created objects use UUIDv7-based IDs. Scholarly coordinates such as Stephanus or Bekker numbers are not embedded into object identity.

Technical IDs are part of the runtime/audit layer and should not normally enter the thinker's language-model context.

See [ADR-0012](docs/adr/ADR-0012-uuidv7-identifiers.md).

## Runtime epistemic projection

A central safety mechanism is **deny-by-default projection**.

The database representation and the model-visible representation are not the same object.

A raw corpus record may contain modern technical or editorial information needed by CUSTODIAN. Before anything is sent to the active thinker, a profile-defined projection allow-list removes non-admissible fields.

Examples of information hidden from PLATO unless explicitly taught:

- modern edition identifiers;
- editor/translator metadata;
- publication year;
- source URLs;
- licensing metadata;
- CUSTODIAN notes;
- modern attribution/authenticity classifications;
- technical checksums and UUIDs.

The projection layer is tested adversarially for leakage.

See [SPEC-0004](docs/specs/SPEC-0004-runtime-epistemic-projection.md).

## Retrieval

Corpus retrieval has two complementary paths:

**Structural retrieval** is deterministic and uses work, locator, sequence and explicit annotations.

**Semantic retrieval** finds conceptually related material, but every semantic result must resolve back to a stable logical corpus object.

Semantic search is a discovery mechanism, not an independent source of truth.

## Threat model and limitations

The experiment faces a fundamental limitation: the underlying LLM already knows far more than the active thinker is supposed to know.

The project calls unauthorized use of that pre-existing information **latent knowledge leakage**.

The objective is therefore not to prove that forbidden knowledge is absent from the model. The objective is to make the system consistently refuse to use knowledge that lacks admissible provenance.

Tests include or will include:

- modern history questions;
- later philosophers;
- modern science and technology;
- false attributions;
- false premises;
- attempts to equate Socrates with Plato;
- prompt injection asking for CUSTODIAN-only metadata;
- indirect leakage through semantic ranking, debug output or citations;
- confusion between ORIGINAL and ACQUIRED knowledge.

A convincing answer is not considered successful if its epistemic origin is invalid.

## Reproducibility and lineage

Released corpus baselines and thinker baselines are immutable.

A release records the corpus manifest, schema versions and checksums. Experimental descendants accumulate their own mutable memories without rewriting the baseline.

This makes it possible to compare agents that began from the same initial state but experienced different conversations.

## Repository map

```text
.
├── README.md                  public project overview
├── AGENTS.md                  instructions for AI/code agents
├── CONTRIBUTING.md            contributor workflow and boundaries
├── llms.txt                   lightweight machine-readable entry point
├── ROADMAP.md                 current implementation status
│
├── framework/                 generic Thinker Framework documentation
├── thinkers/
│   └── plato/
│       └── profile/           Plato-specific profile configuration
│
├── schemas/
│   ├── framework/
│   ├── corpus/
│   ├── ingestion/
│   ├── memory/
│   ├── provenance/
│   ├── retrieval/
│   ├── releases/
│   └── runtime/
│
├── runtime/                   executable runtime boundary code
├── fixtures/                  synthetic architecture fixtures
├── scripts/                   validation and integrity tests
│
├── docs/
│   ├── adr/                   Architecture Decision Records
│   ├── specs/                 active technical specifications
│   └── architecture/          explanatory architecture notes
│
└── site/                      static public documentation site
```

## Important documentation

Start with:

- [ROADMAP.md](ROADMAP.md)
- [AGENTS.md](AGENTS.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [SPEC-0001 — Phase 0 architecture](docs/specs/SPEC-0001-phase-0-architecture.md)
- [SPEC-0003 — Thinker Core / Profile / Instance](docs/specs/SPEC-0003-thinker-core-profile-instance.md)
- [SPEC-0004 — Runtime epistemic projection](docs/specs/SPEC-0004-runtime-epistemic-projection.md)
- [ADR-0011 — Generic Thinker Framework](docs/adr/ADR-0011-generic-thinker-framework.md)
- [ADR-0012 — UUIDv7 identifiers](docs/adr/ADR-0012-uuidv7-identifiers.md)

ADRs record **why** major architectural decisions were made. Specifications describe the current operational design.

## Running the current validation suite

The current Phase 0 code is intentionally lightweight.

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_schemas.py
python scripts/check_phase0_gate.py
python scripts/test_runtime_projection.py
```

GitHub Actions runs the same architecture checks on pushes and pull requests.

The fixtures under `fixtures/phase0/` are synthetic. **They are not Plato's writings and must never be treated as corpus data.**

## Contributing

Contributions are welcome, especially in:

- ancient Greek text/corpus engineering;
- Plato scholarship and textual criticism;
- digital humanities / TEI;
- information retrieval;
- provenance and data lineage;
- LLM evaluation and red-team testing;
- reproducible research infrastructure;
- philosopher-specific corpus/citation adapters.

Before contributing, read [CONTRIBUTING.md](CONTRIBUTING.md) and the relevant ADRs/specifications.

For architectural changes, prefer proposing a new ADR rather than silently rewriting the rationale for an accepted decision.

## Source and licensing policy

The public repository may contain metadata, schemas, tests and source material only when redistribution is permitted.

Large files, working scans and restricted copyrighted material may be stored outside the public repository in CUSTODIAN-controlled storage.

Every acquired source asset is intended to carry provenance, acquisition metadata, rights status and a checksum.

A project-wide code/documentation license has **not yet been selected**. Until that decision is made, do not assume that repository contents are licensed for unrestricted reuse.

## Machine and agent access

If your tool cannot render the GitHub interface, use:

- [`llms.txt`](llms.txt) for a compact machine-oriented entry point;
- [`AGENTS.md`](AGENTS.md) for repository operating rules;
- GitHub's raw-file endpoint or API for individual Markdown/JSON files;
- the project documentation site once GitHub Pages is enabled.

The GitHub repository is the canonical version-controlled source of truth.

## Planned public documentation site

A static documentation site is maintained under `site/` and deployed through GitHub Pages. Its purpose is to provide a simple HTML entry point for humans and automated readers that cannot reliably parse GitHub's web interface.

## Road ahead

With Phase 0 accepted, the next work is:

1. build the complete historical Corpus Platonicum catalog;
2. establish profile-specific attribution/authenticity assessments with cited scholarly basis;
3. freeze the Plato work registry;
4. select and register Greek source editions;
5. verify redistribution/legal status;
6. begin deterministic corpus ingestion;
7. construct and test the first frozen PLATO baseline.

The same Core/Profile architecture can later support additional thinkers without sharing their epistemic worlds.

## Project integrity principle

When forced to choose between a more convincing simulation and a more epistemically honest one, the project chooses **epistemic honesty**.
