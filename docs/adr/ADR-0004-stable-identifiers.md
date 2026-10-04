# ADR-0004 — Stable identifiers and edition-independent passage identity

**Status:** Accepted

## Context

PROJECT PLATO must preserve stable references across changes in source edition, speaker annotation, translation, segmentation metadata and future corrections.

## Decision

Logical corpus identity is separated from textual witnesses and annotations.

Examples:

```text
PL.WORK.REP
PL.SEG.REP.514A.001
PL.WIT.GRK.SLINGS2003.REP.514A.001
PL.TR.PL.<EDITION>.REP.514A.001
PL.MEM.<INSTANCE>.<TYPE>.<ID>
PL.PROV.<ID>
PL.EXP.<LINEAGE>.<DATE>.<SEQUENCE>
```

A `segment_id` identifies a location in the canonical corpus topology. It does **not** encode speaker, authenticity class, edition, translation, tokenization or interpretation.

Speaker annotations are versioned assertions attached to `segment_id`.

## Consequences

- Correcting speaker attribution does not break references.
- Multiple editions can coexist for the same logical segment.
- Provenance can refer to stable corpus objects.
- Storage migration does not change identity.
