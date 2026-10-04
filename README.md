# PROJECT PLATO

PROJECT PLATO is an experimental attempt to construct an epistemically constrained language-based cognitive agent whose primary knowledge is derived from the **Corpus Platonicum**, while later knowledge is acquired through controlled interaction.

The goal is **not** to imitate an ancient philosopher stylistically, and not to build an encyclopedia about Plato. The experiment asks a stricter question:

> If an agent had access to Plato's corpus, a reconstructed Platonic mode of inquiry, and a controlled history of later experience, how would it reason about questions and phenomena outside its original world?

## Two environments

- **CUSTODIAN** — researcher, librarian, architect, observer and auditor. CUSTODIAN may use modern scholarship and external sources.
- **PLATO** — the experimental agent. PLATO may use only its approved original corpus, explicitly acquired knowledge, its episodic history and its own derived inferences.

CUSTODIAN is not PLATO and is not intended to answer on PLATO's behalf during normal experiments.

## Core epistemic rule

Epistemic honesty takes precedence over fluency.

If PLATO cannot justify knowledge through an admissible source, the correct answer may be:

> I do not know.

The project therefore focuses on **controlled access to knowledge**, not on pretending that the base language model's latent knowledge does not exist.

## Knowledge classes

- **ORIGINAL** — read-only access to the approved Corpus Platonicum release.
- **ACQUIRED** — information introduced during the experiment.
- **EPISODIC** — remembered conversations and events.
- **INFERENCE** — conclusions derived by PLATO from admissible sources.
- **PROVENANCE** — an audit layer recording where claims and inferences came from.

ORIGINAL is a logical memory class, not a mutable duplicate of the corpus.

## Repository role

This public repository is the canonical source of truth for:

- Architecture Decision Records (ADRs)
- technical specifications
- schemas
- runtime code
- tests
- experiment protocols
- release manifests
- redistributable corpus metadata

Google Drive is complementary storage for working documents, source scans/PDFs, large files and material that cannot legally be redistributed.

## Current status

The project is in **Phase 0 — architecture before corpus ingestion**.

No corpus source is considered production-ingested until stable identifiers, schemas, provenance and access boundaries are defined.

### Phase 0 exit criteria

1. Stable identifier convention.
2. Corpus data model.
3. Memory data model.
4. Provenance data model.
5. Structural + semantic retrieval design.
6. CUSTODIAN / PLATO access separation.
7. Versioning and snapshot model.
8. Infrastructure migration path.
9. Deterministic ingestion acceptance criteria.

## Repository structure

```text
docs/
  adr/
  specs/
  architecture/
schemas/
  corpus/
  memory/
  provenance/
tests/
experiments/
runtime/
corpus/
  metadata/
  manifests/
releases/
```

Large or non-redistributable source texts are intentionally not committed by default.

## Licensing

No project-wide license has been selected yet. Licensing of project code/documentation and licensing or public-domain status of corpus sources will be decided separately before redistribution beyond materials that are unquestionably safe to publish.
