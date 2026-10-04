# ADR-0009 — Corpus releases and PLATO baselines are immutable

**Status:** Accepted

## Context

The experiment requires reproducible starting states, alternative lineages and later comparison of PLATO instances that began from identical original knowledge.

## Decision

A released corpus baseline is immutable.

Every corpus release is represented by a manifest containing:

- release identifier;
- schema versions;
- included works;
- approved textual witnesses and translations;
- source checksums;
- manifest checksum;
- creation timestamp;
- release status.

A PLATO baseline references exactly one frozen corpus manifest plus frozen epistemic/runtime configuration.

Mutable memory is not part of the original corpus release.

Experimental instances may descend from a baseline and accumulate independent memory. Snapshots record lineage and state but do not mutate the baseline they descend from.

Corrections to corpus content create a new corpus release rather than altering a released manifest in place.

## Consequences

- PLATO-A and PLATO-B can begin from byte-identical original knowledge.
- Historical experiment runs remain reproducible.
- Corpus corrections are explicit version changes.
- Release manifests become a core provenance anchor.
