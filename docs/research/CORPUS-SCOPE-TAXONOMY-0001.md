# CORPUS SCOPE TAXONOMY 0001 — Plato profile

**Status:** Frozen for Phase 1 catalog construction

## Purpose

This taxonomy records **why an item belongs to the historical PROJECT PLATO research scope**.

It is independent from modern authorship/authenticity.

An entry may have more than one scope class because historical transmission facts overlap.

## Classes

### THRASYLLAN_CANON

The work or collection occupies one of the thirty-six slots in the nine tetralogies attributed to Thrasyllus and reported by Diogenes Laertius.

This is a transmission/canon fact, not a claim that Plato wrote the work.

### THRASYLLAN_COLLECTION_MEMBER

The text is an independently addressable member of a Thrasyllan collection slot.

Current use: the thirteen individual Epistles beneath the collection-level `Epistles` slot.

### EXTRA_CANONICAL_EXTANT_ATTRIBUTION

An extant text historically attributed to Plato or included in the wider Platonic corpus tradition but not occupying its own Thrasyllan tetralogical slot.

Examples include pseudo-Platonic works printed in later critical corpora and Halcyon/Alcyon in its separate surviving transmission.

### ANCIENT_EXPLICIT_SPURIA

Ancient testimony explicitly reports the work/title as spurious under Plato's name.

This class may overlap with an extant text or with a lost title.

### LOST_ATTRIBUTION

A historically attested Platonic title for which no usable production text is presently known to survive.

Such entries are **catalog-only** and cannot contribute text to ORIGINAL knowledge.

### ANTHOLOGICAL_ASCRIPTION

Material attributed to Plato through anthology transmission rather than the dialogue/epistle manuscript corpus.

Current use: the Epigrammata collection.

## Rules

1. Scope classes are historical/transmission metadata and remain `CUSTODIAN_ONLY`.
2. Scope classes do not determine A/B/C/D authenticity grades.
3. Multiple classes are allowed and expected.
4. A lost attribution cannot become a runtime text candidate without a separately verified surviving text.
5. A new scope class requires profile-level documentation and schema revision.
6. Source-specific details remain in `attestations`; the taxonomy is a normalized analytical view over them.

## Phase 1 consequence

The historical scope taxonomy is now frozen for the first complete catalog pass.

The remaining catalog work concerns completeness, member-level resolution (especially Epigrams), source verification and modern authenticity assessment.
