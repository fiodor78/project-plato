# Contributing to PROJECT PLATO

Thank you for considering a contribution.

PROJECT PLATO combines research software, digital humanities, corpus engineering and LLM evaluation. Contributions are welcome, but the project deliberately moves slowly around corpus provenance and epistemic boundaries because mistakes there can invalidate later experiments.

## Before opening a change

Read:

- `README.md`
- `ROADMAP.md`
- `AGENTS.md`
- the relevant documents under `docs/specs/`
- relevant Architecture Decision Records under `docs/adr/`

## Useful contribution areas

We particularly welcome work in:

- Classical Greek and Platonic textual scholarship;
- critical-edition and textual-witness metadata;
- TEI/XML and digital-humanities pipelines;
- corpus normalization and alignment;
- information retrieval;
- provenance/data lineage;
- reproducibility;
- LLM leakage and adversarial evaluation;
- documentation;
- future thinker-profile adapters.

## Architecture changes

For a significant architectural change, propose an ADR.

An ADR should explain:

- context;
- decision;
- alternatives considered where useful;
- consequences;
- migration implications.

Do not rewrite accepted decision history to make it look as if the project had always used the new approach.

## Corpus contributions

Do not add source text until its provenance and redistribution status are known.

For source assets preserve:
- source/reference location;
- acquisition metadata;
- checksum;
- edition/editor/translator metadata in CUSTODIAN space;
- rights/redistribution status;
- transformation history.

The fact that text is available online does not imply that it is safe to redistribute.

## Epistemic-boundary changes

Changes that affect what an active Thinker can see require special care.

The default is deny-by-default.

Any new runtime-visible field should be justified and tested for indirect leakage.

Modern scholarly metadata is normally CUSTODIAN-only.

## Tests

Before proposing a change, run:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_schemas.py
python scripts/check_phase0_gate.py
python scripts/test_runtime_projection.py
```

A contribution that changes schemas, runtime projection or provenance should add or update fixtures/tests.

## Fixtures

`fixtures/phase0/` contains synthetic test data.

Never treat those strings as historical source material.

## New thinker profiles

The generic framework should not need to be forked for every thinker.

A future profile should normally define:
- thinker identity;
- corpus scope;
- work registry;
- locator/citation adapters;
- attribution policy;
- profile-specific annotations;
- epistemic/personality reconstruction;
- profile-specific tests.

Profiles do not share mutable memory by default.

## Issues and pull requests

Use an issue for:
- research questions;
- source uncertainty;
- architecture proposals;
- corpus-scope disputes;
- licensing uncertainty.

Pull requests should explain both **what changed** and **why the change preserves the experiment's epistemic integrity**.

## Licensing

A project-wide license has not yet been selected.

Until that decision is made, do not assume unrestricted reuse rights for repository content, and do not submit material whose redistribution rights are unclear.
