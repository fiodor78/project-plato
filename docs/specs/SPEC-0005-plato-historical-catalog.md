# SPEC-0005 — Plato historical attribution catalog

**Status:** Active Phase 1 specification

## Purpose

Define the CUSTODIAN-side catalog used to decide what belongs in research scope before production text ingestion.

The catalog is broader than a runtime corpus release.

## Entry types

- `WORK` — an independently addressable textual work.
- `COLLECTION` — a historical/editorial grouping such as the Epistles.
- `MEMBER` — a text-addressable member of a collection.
- `LOST_TITLE` — a title attested historically for which no usable text survives.
- `ANTHOLOGY_COLLECTION` — material attributed through an anthology tradition rather than the dialogue manuscript corpus.

## Survival status

- `EXTANT`
- `LOST`
- `FRAGMENTARY`
- `UNKNOWN`

## Runtime candidacy

Catalog entries carry a CUSTODIAN planning field:

- `TEXT_CANDIDATE` — extant and potentially eligible for a later ORIGINAL corpus release;
- `CATALOG_ONLY` — historical metadata only, no source text can enter the release;
- `PENDING_REVIEW` — scope or transmission evidence still needs review.

This is **not** an authenticity grade.

## Attestations

Each attestation contains:

- `source_id`;
- `system`;
- `status`;
- optional `position`;
- optional note.

Initial status vocabulary:

- `INCLUDED`
- `EXPLICITLY_SPURIOUS`
- `ASCRIBED`
- `EDITORIALLY_INCLUDED`

Attestation systems are profile-specific controlled vocabulary.

## Modern authenticity

Modern authorship/authenticity evaluation does not belong in the historical catalog record.

It remains a separate CUSTODIAN-only assertion layer using the Plato profile's A/B/C/D model and cited scholarly bases.

## Historical collections

The Thrasyllan Epistles must be represented at two levels:

1. collection-level position in Tetralogy IX;
2. individual letters as child/member records once numbering/recipient mapping is verified.

Anthological epigrams are represented separately from the dialogue/epistle manuscript corpus and are not automatically promoted into a runtime release.

## Phase 1 freeze condition

The historical catalog can be frozen when:

1. every Thrasyllan tetralogical slot is registered;
2. all thirteen Epistles are separately registered and linked to the collection;
3. extant pseudo-Platonic material outside the Thrasyllan canon is registered;
4. ancient explicitly spurious/lost titles are registered;
5. anthological Plato-attributions relevant to scope are registered;
6. every entry has at least one traceable attestation;
7. duplicate/alternate titles are resolved without inventing duplicate works.
