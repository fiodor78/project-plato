# PROJECT PLATO

PROJECT PLATO is the first reference implementation of a reusable **Thinker Framework** for constructing epistemically constrained language-based cognitive agents grounded in the corpus of a historical philosopher.

The first Thinker Profile is **PLATO**. Its primary knowledge will be derived from the approved **Corpus Platonicum**; later knowledge may be acquired through controlled interaction.

The goal is **not** to imitate Plato stylistically and not to build an encyclopedia about Plato. The experiment asks:

> If an agent had access to Plato's corpus, a reconstructed Platonic mode of inquiry, and a controlled history of later experience, how would it reason about questions and phenomena outside its original world?

## Reusable architecture

The framework is deliberately designed so the same method can later support other isolated philosopher profiles.

Examples:

- PLATO — Stephanus citation adapter;
- ARISTOTLE — Bekker citation adapter;
- NIETZSCHE — work/section or aphorism adapter;
- WITTGENSTEIN — proposition/remark adapter.

Each thinker receives a separate profile, corpus release, memory store and experimental lineage. Their epistemic worlds are not mixed by default.

## Three layers

### THINKER CORE

Generic:

- source ingestion;
- corpus objects;
- acquired/episodic/inference memory;
- provenance;
- structural + semantic retrieval;
- access projection;
- releases and snapshots;
- integrity/leakage tests.

### THINKER PROFILE

Philosopher-specific:

- corpus scope;
- citation/locator schemes;
- work registry;
- attribution/authenticity rules;
- speaker/narrator annotations where relevant;
- epistemic constitution;
- cognitive/personality reconstruction;
- profile-specific tests.

PLATO lives under `thinkers/plato/`.

### THINKER INSTANCE

A running experimental lineage created from a frozen profile release, for example:

```text
PLATO-1.0-A
PLATO-1.0-B
```

Two instances may begin identically and acquire different experiences.

## CUSTODIAN and the thinker

- **CUSTODIAN** — researcher, librarian, architect, observer and auditor. It may use modern scholarship and external sources.
- **PLATO** — the first experimental thinker. It may use only its approved original corpus, explicitly acquired knowledge, episodic history and its own derived inferences.

CUSTODIAN is not PLATO and is not intended to answer on PLATO's behalf during normal experiments.

## Core epistemic rule

Epistemic honesty takes precedence over fluency.

If the active thinker cannot justify knowledge through an admissible source, the correct answer may be:

> I do not know.

The system therefore controls **permission to use knowledge**, rather than pretending the base LLM contains no latent modern knowledge.

## Knowledge classes

- **ORIGINAL** — read-only access to the frozen profile corpus.
- **ACQUIRED** — information introduced during the experiment.
- **EPISODIC** — remembered conversations and events.
- **INFERENCE** — conclusions derived from admissible sources.
- **PROVENANCE** — audit lineage showing where claims and inferences came from.

ORIGINAL is a logical memory class, not a mutable duplicate of corpus data.

## Repository role

This public repository is the canonical source of truth for architecture, schemas, tests, profile definitions and redistributable metadata.

Google Drive remains complementary storage for working research, scans/PDFs, large source files and material that cannot legally be redistributed.

## Current status

The project is in **Phase 0 — architecture before real corpus ingestion**.

The generic Core/Profile boundary has been introduced before importing actual Platonic source text.

## Repository structure

```text
framework/
  README.md

thinkers/
  plato/
    profile/

docs/
  adr/
  specs/
  architecture/

schemas/
  framework/
  corpus/
  ingestion/
  memory/
  provenance/
  retrieval/
  releases/

fixtures/
scripts/
experiments/
runtime/
releases/
```

Large or non-redistributable source texts are intentionally not committed by default.

## Licensing

No project-wide license has yet been selected. Code/documentation licensing and source-text redistribution rights will be decided explicitly before public redistribution of real corpus assets.
