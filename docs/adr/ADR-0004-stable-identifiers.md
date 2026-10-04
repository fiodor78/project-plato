# ADR-0004 — Stable identifiers and edition-independent passage identity

**Status:** Superseded in part by ADR-0011

## Context

The original decision established an important principle: logical corpus identity must remain separate from source edition, translation, speaker annotation and other mutable interpretation.

Its first identifier examples were Plato-specific and embedded Stephanus coordinates directly in segment IDs.

ADR-0011 generalized the architecture so the same framework can support other philosophers and citation systems.

## Decision retained

- Logical corpus identity is separate from textual witnesses and annotations.
- Correcting speaker attribution, preferred edition, translation or authenticity metadata must not normally change logical identity.
- Multiple textual witnesses may align to one logical segment.
- Provenance refers to stable logical objects.

## Decision superseded

The earlier examples such as:

```text
PL.SEG.REP.514A.001
```

are no longer the canonical identifier design.

The generic Thinker Framework uses thinker-scoped, citation-scheme-independent machine IDs, while Stephanus/Bekker/aphorism/proposition references live in separate locator objects.

See ADR-0011 and `docs/architecture/stable-identifiers.md`.
