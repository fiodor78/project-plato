# ADR-0002 — PLATO knowledge architecture and provenance

**Status:** Accepted

## Context

The base language model already contains broad historical and modern knowledge. PROJECT PLATO cannot guarantee epistemic isolation by removing knowledge from model weights.

## Decision

PLATO will not initially be fine-tuned on Corpus Platonicum.

Corpus Platonicum remains an external, addressable primary-knowledge store. Retrieval preserves work, Stephanus location, textual witness and other structural metadata.

PLATO knowledge is divided into ORIGINAL, ACQUIRED, EPISODIC and INFERENCE classes. A separate PROVENANCE layer records the origin and derivation of claims.

Knowledge available only from the base model is not an admissible epistemic source.

When no admissible source exists, PLATO may and sometimes must state that it does not know.

## Consequences

- Source origin is auditable.
- Acquired knowledge cannot silently become original knowledge.
- Corpus passages remain traceable.
- Isolation depends on retrieval and memory controls, not style prompting alone.
