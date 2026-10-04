# SPEC-0002 — Segmentation and discourse annotation policy

**Status:** Frozen for the first production-ingestion iteration (Phase 0 accepted).

## Objective

Create stable logical passage units that are independent of a particular textual witness while remaining fine-grained enough for retrieval, scholarly citation and discourse-aware provenance.

## Canonical segmentation rule

A logical segment is:

> the maximal structurally coherent span that does not cross a canonical locator boundary or a profile-defined primary structural boundary.

For the Plato profile, the canonical locator is normally a Stephanus subdivision.

Primary structural boundaries may include:

- a Stephanus subdivision boundary;
- an explicit top-level dialogue turn where reliably encoded;
- a lexical/definition entry boundary;
- a work-specific structural boundary approved by the profile.

A segment identity does **not** contain:

- speaker name;
- narrator;
- attributed author/source;
- authenticity classification;
- textual edition;
- translation;
- sentence number;
- token count;
- semantic topic.

## Why the earlier rule was revised

The initial draft defined a segment as the intersection of a Stephanus subdivision and a speaker turn or narrative block.

Testing against real structures showed this is too narrow:

- **Apology** contains long uninterrupted speeches crossing locator subdivisions.
- **Republic** contains narration with embedded direct/reported voices.
- **Symposium** contains nested narrative frames.
- **Menexenus** contains discourse uttered by one character but attributed to another source.
- **Letter VII** is epistolary rather than dialogical.
- **Definitiones** is organized as lexical entries rather than speaker turns or ordinary narrative.

See `docs/research/SEGMENTATION-PILOT-0001.md`.

## Hard boundaries

### Locator boundary

A segment must not cross a canonical locator subdivision chosen by the profile.

For Plato, a passage continuing from `514a` to `514b` becomes at least two segments even when the same voice continues.

### Profile structural boundary

A profile may define boundaries that occur inside a locator cell.

For example, Definitiones may split at definition-entry boundaries.

Such boundaries must be based on explicit structural evidence, not semantic chunking by an LLM.

## Non-boundaries by default

The following do not automatically create canonical segment boundaries:

- modern sentence punctuation;
- tokenizer chunks;
- embedding windows;
- topic changes inferred by a model;
- every embedded quotation;
- every inferred change of reported voice.

These may be represented as annotations.

## Discourse annotation

Speaker/voice information is annotation, not identity.

The annotation layer must be capable of representing:

- discourse mode;
- speaker/utterer;
- narrator;
- attributed source/composer;
- frame depth;
- reported or embedded speech;
- witness-specific spans where a phenomenon affects only part of a segment.

Expected modes include:

- `DIALOGUE_TURN`
- `NARRATION`
- `LONG_SPEECH`
- `REPORTED_SPEECH`
- `EMBEDDED_QUOTATION`
- `EPISTOLARY`
- `LEXICAL_ENTRY`
- `OTHER`

A speaker correction must not change `segment_id`.

## Witness-specific spans

Some discourse phenomena cannot safely be promoted to canonical boundaries because editions may differ in punctuation or quotation rendering.

Such annotations should target:

- a stable logical segment;
- a specific normalized textual witness;
- offsets in that witness representation;
- the checksum/version of the normalized text to which offsets apply.

## Structural-source rule

One designated structural source may be used during ingestion to locate explicit boundaries.

That source does **not** become the sole authoritative textual witness merely because it supplies topology.

Boundary decisions must retain provenance.

## Boundary corrections

Before a corpus release is frozen, provisional boundaries may be corrected.

After release freeze:

- metadata/annotation corrections preserve IDs where logical identity is unchanged;
- true boundary redefinition creates new segment IDs plus an explicit migration map;
- historical releases are not rewritten.

## Validation status

Segmentation Pilot 0001 tested:

- long speech;
- narrated dialogue;
- nested narrative frame;
- attributed embedded speech;
- epistolary material;
- lexical/pseudo-Platonic material.

The executable discourse-annotation schema and synthetic nested-voice fixtures passed the Phase 0 validation gate. This policy is therefore frozen for the first production-ingestion iteration. Any later incompatible change requires an explicit migration decision and, where architectural, a superseding ADR/spec revision.
