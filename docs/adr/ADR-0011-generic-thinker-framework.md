# ADR-0011 — Generic Thinker framework with isolated philosopher profiles

**Status:** Accepted

## Context

PROJECT PLATO is the first implementation of an epistemically constrained historical-philosopher agent. The underlying architecture — corpus isolation, acquired knowledge, episodic memory, inference memory, provenance, retrieval, releases, snapshots and leakage testing — is not inherently specific to Plato.

A reusable design would make it possible to construct analogous agents for other philosophers without mixing their corpora, identities or experimental histories.

The current Phase 0 schemas contain Plato-specific assumptions, especially Stephanus addressing and `PL.*` identifiers. These assumptions would make reuse difficult for thinkers whose corpora use Bekker numbers, fragment systems, aphorism numbers, proposition numbers, book/chapter references or no standard scholarly locator at all.

## Decision

PROJECT PLATO becomes the **first reference implementation of a generic Thinker framework**.

The architecture is separated into three layers.

### 1. THINKER CORE

Generic and reusable:

- epistemic classes;
- mutable memory;
- provenance;
- retrieval events;
- access projection;
- source-asset ingestion;
- releases and snapshots;
- experiment lineage;
- leakage and integrity tests.

The core must not assume Stephanus pagination, Plato-specific work codes or Plato-specific authenticity rules.

### 2. THINKER PROFILE

Philosopher-specific configuration and knowledge environment:

- `thinker_id`;
- corpus catalog;
- citation/locator schemes;
- work-code registry;
- authenticity or attribution model where relevant;
- speaker/narrator model where relevant;
- epistemic constitution extensions;
- personality/cognitive reconstruction;
- approved source editions and translations;
- profile-specific tests.

PLATO is the first profile.

Future examples may include:

- ARISTOTLE — Bekker numbering;
- NIETZSCHE — work/book/section or aphorism addressing;
- WITTGENSTEIN — proposition/remark numbering;
- PRE-SOCRATICS — fragment/testimonia systems.

### 3. THINKER INSTANCE

A running experimental lineage created from one frozen Thinker Profile release.

Examples:

```text
PLATO-1.0-A
PLATO-1.0-B
ARISTOTLE-1.0-A
```

Instances never share mutable memory unless an explicit experiment transfers information between them.

## Repository strategy

The current public repository `fiodor78/project-plato` remains the development home and reference implementation during Phase 0.

Generic components are placed in reusable framework-level paths, while Plato-specific assets move under a dedicated profile namespace.

A later ADR may extract the generic core into a separate repository or template once the interfaces stabilize. Premature repository splitting is avoided.

A new philosopher should normally be created from the frozen generic framework plus a new isolated Thinker Profile, not by placing multiple philosophers inside one runtime epistemic environment.

## Locator rule

The core uses a generic **canonical locator** abstraction rather than a hard-coded Stephanus field.

A locator contains:

- a `scheme` identifier;
- a normalized display/reference value;
- structured components when available;
- an ordinal when multiple logical segments share one scholarly location.

Examples:

```text
scheme=STEPHANUS       value=514a
scheme=BEKKER          value=980a21
scheme=APHORISM        value=GS.125
scheme=PROPOSITION     value=PI.201
```

## Identifier rule

Machine identity must not depend on one philosopher's citation system.

Canonical entity IDs therefore move toward thinker-scoped, scheme-independent identifiers.

Human-readable scholarly citations remain separate fields.

ADR-0004 remains historically informative but its Plato-specific identifier examples are superseded by this ADR where they conflict.

## Consequences

- PROJECT PLATO can become a reusable experimental methodology rather than a one-off simulation.
- Each philosopher remains epistemically isolated.
- Core tests can be reused across profiles.
- Profile-specific citation and corpus problems remain local.
- Current Phase 0 schemas must be refactored before real corpus ingestion.
