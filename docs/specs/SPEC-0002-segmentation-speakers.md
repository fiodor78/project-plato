# SPEC-0002 — Segmentation and speaker annotation policy

**Status:** Active draft; must be tested against real Corpus Platonicum sources before freeze.

## Objective

Create stable logical passage units that are independent of a particular Greek edition while remaining fine-grained enough for speaker-aware retrieval and provenance.

## Proposed canonical segment

A logical segment is the intersection of:

1. a Stephanus subdivision boundary, and
2. a top-level dialogue speaker turn or narrative block.

This means:

- a speaker turn that crosses from `514a` to `514b` becomes at least two logical segments;
- several speaker turns inside `514a` receive sequential ordinals;
- segment identity does not contain the speaker name;
- changing a speaker annotation does not change `segment_id`.

Example:

```text
PL.SEG.REP.514A.001
PL.SEG.REP.514A.002
PL.SEG.REP.514B.001
```

## Why not sentence-level segmentation

Sentence punctuation is editorial and varies by edition. Sentence-based identity would therefore make the canonical topology depend too strongly on a modern editor.

## Why not fixed token chunks

Token chunks are model- and tokenizer-dependent, unsuitable as scholarly identifiers, and unstable across preprocessing changes.

## Speaker model

Speaker identity is an annotation, not part of passage identity.

A speaker assertion records:

- stable `speaker_id`;
- display label;
- assertion status;
- basis/reference;
- runtime visibility.

Top-level statuses currently include:

- `ASSERTED`
- `UNCERTAIN`
- `NARRATOR`
- `EMBEDDED_QUOTATION`
- `CHORAL_OR_MULTIPLE`

Embedded quotations and reported dialogue may require a second annotation layer. They do not automatically redefine the top-level segment boundary.

## Structural-source rule

The canonical topology may use one designated structural source to locate speaker and Stephanus boundaries during ingestion. That source does **not** become the sole authoritative Greek witness merely because it provides topology.

Textual witnesses remain separate objects aligned to the logical segment.

## Boundary corrections

Before a corpus release is frozen, provisional boundaries may be corrected.

After a release is frozen:

- metadata corrections preserve IDs where identity is unchanged;
- a true boundary redefinition creates an explicit migration map from old segment IDs to new segment IDs;
- historical releases are not rewritten.

## Validation required before freeze

The policy must be tested on at least:

- a simple Socratic dialogue;
- a dialogue with framing/narration;
- a work containing long speeches;
- nested quotation/reported dialogue;
- letters or non-dialogue material;
- pseudo-Platonic material included in the historical corpus.

Only then may this specification become frozen.
