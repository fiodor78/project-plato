# Stable identifier conventions

**Status:** Phase 0 draft implementing ADR-0004  
**Schema family:** v0.1.0

## Principle

Identifiers encode **identity**, not mutable interpretation.

Do not put speaker attribution, authenticity classification, preferred edition, translation quality, model version or semantic labels inside a logical passage ID.

## Namespaces

| Entity | Pattern | Example |
|---|---|---|
| Work | `PL.WORK.<WORK>` | `PL.WORK.REP` |
| Logical segment | `PL.SEG.<WORK>.<STEPHANUS>.<ORDINAL>` | `PL.SEG.REP.514A.001` |
| Edition | `PL.ED.<EDITION>` | `PL.ED.SLINGS2003` |
| Greek witness | `PL.WIT.GRK.<EDITION>.<WORK>.<STEPHANUS>.<ORDINAL>` | `PL.WIT.GRK.SLINGS2003.REP.514A.001` |
| Translation | `PL.TR.<LANG>.<EDITION>.<WORK>.<STEPHANUS>.<ORDINAL>` | `PL.TR.PL.WITWICKI.REP.514A.001` |
| Speaker assertion | `PL.ASSERT.SPK.<ID>` | `PL.ASSERT.SPK.01J...` |
| Authenticity assertion | `PL.ASSERT.AUTH.<ID>` | `PL.ASSERT.AUTH.01J...` |
| Mutable memory | `PL.MEM.<INSTANCE>.<TYPE>.<ID>` | `PL.MEM.PLATO_1_0_A.ACQUIRED.01J...` |
| Provenance | `PL.PROV.<ID>` | `PL.PROV.01J...` |
| Experiment | `PL.EXP.<LINEAGE>.<DATE>.<SEQ>` | `PL.EXP.A.20261114.001` |

## Work codes

Work codes are controlled vocabulary and will be frozen only after Corpus Catalog review.

Examples such as `REP` are illustrative until the catalog registry is accepted.

## Stephanus normalization

- stored display form: lowercase, e.g. `514a`
- identifier form: uppercase, e.g. `514A`
- page/letter is not inferred from model output; it must come from corpus structure
- an ordinal distinguishes multiple logical segments beginning at the same Stephanus point

## IDs for generated objects

Generated assertion, memory and provenance IDs should be collision-resistant and sortable where practical. ULID is the current preferred candidate, but this is not yet frozen by ADR.

## Change rule

If a correction changes metadata about an existing logical object, retain its ID.

Create a new ID only when the correction establishes that the previous object boundary or identity was fundamentally wrong. Such remapping must be explicit and recorded in provenance/migration metadata.
