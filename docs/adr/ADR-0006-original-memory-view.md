# ADR-0006 — ORIGINAL memory is a corpus view, not duplicated mutable memory

**Status:** Accepted

## Context

Duplicating Corpus Platonicum into mutable memory would create two sources of truth and allow later memory operations to contaminate original knowledge.

## Decision

ORIGINAL is a logical memory class but not an independently mutable store.

`MEMORY_ORIGINAL` resolves to approved corpus objects through stable segment IDs and the release-specific corpus manifest.

ACQUIRED, EPISODIC and INFERENCE are persistent memory stores created during the life of a PLATO instance.

No runtime memory operation may write back into the original corpus.

A release contains:

1. an immutable corpus manifest defining original knowledge;
2. mutable instance memory created after first boot;
3. provenance linking later memories and inferences to corpus and/or acquired testimony.

## Consequences

- Initial epistemic state can be reproduced.
- PLATO-A and PLATO-B can share one immutable corpus while accumulating different experiences.
- Memory corruption cannot silently rewrite Corpus Platonicum.
