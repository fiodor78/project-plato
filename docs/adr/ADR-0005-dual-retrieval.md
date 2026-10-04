# ADR-0005 — Dual corpus retrieval: structural plus semantic

**Status:** Accepted

## Context

PLATO must retrieve passages deterministically by corpus structure and approximately by meaning.

## Decision

Corpus retrieval has two interoperable paths.

### Structural retrieval

Uses work ID, Stephanus coordinates, segment sequence, speaker annotations, textual witness and other explicit metadata. It is deterministic.

### Semantic retrieval

Uses embeddings or successor semantic-search techniques over approved corpus representations. Semantic results always resolve back to stable `segment_id` values.

Semantic search is a discovery mechanism, not a source of corpus facts.

Every retrieved text remains traceable to its segment, textual witness, source edition and retrieval event.

CUSTODIAN-only metadata must not be exposed to PLATO merely because the retrieval engine can access it internally.

## Consequences

- Exact citation and conceptual retrieval coexist.
- Embedding models can change without changing corpus identity.
- Semantic indexes can be rebuilt independently.
- Retrieval becomes auditable.
