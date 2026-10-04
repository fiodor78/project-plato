# ADR-0013 — Historical corpus scope is attestation-based, not authenticity-based

**Status:** Accepted

## Context

PROJECT PLATO aims to preserve the complete historical corpus transmitted or attributed under Plato's name, not merely the subset accepted as authentic by modern scholarship.

A single flat category such as “Platonic / non-Platonic” would collapse several historically distinct facts:

- inclusion in the Thrasyllan tetralogical canon;
- explicit ancient rejection as spurious;
- survival in later manuscript/editorial corpora;
- attribution in anthology traditions;
- modern scholarly judgments about authorship;
- titles known from ancient testimony but no longer extant.

These facts can overlap. For example, a work may survive in the later pseudo-Platonic corpus and also be explicitly listed as spurious by Diogenes Laertius.

## Decision

The Plato profile maintains a **historical attribution catalog** separate from both the generic corpus store and modern authenticity assertions.

Catalog inclusion means:

> there is evidence that a textual work, collection or title was historically transmitted, cataloged or ascribed under Plato's name or within the Platonic corpus tradition.

Catalog inclusion does **not** mean:

- Plato wrote the text;
- the text will automatically enter PLATO's ORIGINAL runtime corpus;
- the modern project accepts an ancient attribution;
- a lost title provides content to the active thinker.

Each catalog entry records one or more independent **attestations**. An attestation identifies:

- a source/edition;
- an attestation system or tradition;
- the status asserted by that source;
- source-specific notes.

Examples of attestation systems:

- `THRASYLLAN_TETRALOGIES`
- `DIOGENES_SPURIOUS_LIST`
- `BURNET_OCT_VOL5`
- `ANTHOLOGICAL_ASCRIPTION`

Modern authenticity judgments remain separate CUSTODIAN-only assertions.

## Catalog scope vs runtime scope

Two sets must never be conflated.

### HISTORICAL CATALOG SCOPE

May include:
- extant canonical works;
- disputed works;
- pseudo-Platonic works;
- epistolary collections and members;
- anthologically attributed material;
- lost titles known only through testimony.

### ORIGINAL RUNTIME SCOPE

Contains only extant text objects deliberately admitted to a frozen Thinker Profile release.

A lost work can therefore be fully cataloged while contributing **zero text** to PLATO.

## Collections and members

Historical collection units and text-addressable members may both be represented.

For example, `Epistles` occupies one slot in the ninth Thrasyllan tetralogy but contains thirteen letters. The catalog may preserve the collection-level attestation while registering individual letters as member entries for text-level ingestion.

The same principle may later be used for epigram collections.

## Consequences

- Historical transmission is preserved without pretending all transmitted works are authentic.
- Modern scholarship can be revised without rewriting historical catalog facts.
- Lost works do not accidentally become knowledge of the active thinker.
- Different scholarly definitions of “Appendix Platonica” can coexist as source-specific attestations rather than one project-imposed absolute boundary.
- The generic Thinker Core remains philosopher-neutral.
