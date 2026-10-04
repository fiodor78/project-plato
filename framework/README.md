# Thinker Framework

This directory represents the reusable architecture underlying PROJECT PLATO.

A **Thinker** is an epistemically constrained language-agent profile built from:

1. a frozen original corpus;
2. thinker-specific citation and attribution rules;
3. a reconstructed cognitive/personality constitution;
4. controlled acquired knowledge;
5. episodic memory;
6. explicit inferences;
7. auditable provenance.

The framework is intentionally philosopher-neutral.

## Layers

- **Core** — generic schemas, memory, provenance, retrieval, release and test logic.
- **Profile** — philosopher-specific corpus rules, locator adapters and constitutions.
- **Instance** — one evolving experimental lineage created from a frozen profile release.

PLATO is the first reference profile under `thinkers/plato/`.

The generic framework may later be extracted to a dedicated repository once its interfaces stabilize.
