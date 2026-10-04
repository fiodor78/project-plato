# Stable identifier conventions

**Status:** Phase 0 draft implementing ADR-0011  
**Schema family:** v0.2.x

## Principle

Identifiers encode **identity**, not mutable scholarly interpretation or one philosopher's citation convention.

Do not embed speaker attribution, authenticity classification, preferred edition, translation quality, model version, Stephanus/Bekker numbers or semantic labels in a logical segment ID.

## Thinker-scoped namespaces

| Entity | Pattern | Plato example |
|---|---|---|
| Thinker | `TH.<THINKER>` | `TH.PLATO` |
| Work | `TH.<THINKER>.WORK.<WORK>` | `TH.PLATO.WORK.REP` |
| Logical segment | `TH.<THINKER>.SEG.<ID>` | `TH.PLATO.SEG.01K...` |
| Edition | `TH.<THINKER>.ED.<EDITION>` | `TH.PLATO.ED.SLINGS2003` |
| Textual witness | `TH.<THINKER>.WIT.<ID>` | `TH.PLATO.WIT.01K...` |
| Translation | `TH.<THINKER>.TR.<ID>` | `TH.PLATO.TR.01K...` |
| Speaker assertion | `TH.<THINKER>.ASSERT.SPK.<ID>` | `TH.PLATO.ASSERT.SPK.01K...` |
| Attribution assertion | `TH.<THINKER>.ASSERT.AUTH.<ID>` | `TH.PLATO.ASSERT.AUTH.01K...` |
| Mutable memory | `TH.<THINKER>.MEM.<INSTANCE>.<TYPE>.<ID>` | `TH.PLATO.MEM.PLATO_1_0_A.ACQUIRED.01K...` |
| Provenance | `TH.<THINKER>.PROV.<ID>` | `TH.PLATO.PROV.01K...` |
| Retrieval event | `TH.<THINKER>.RET.<ID>` | `TH.PLATO.RET.01K...` |
| Snapshot | `TH.<THINKER>.SNAP.<ID>` | `TH.PLATO.SNAP.01K...` |

## Scholarly location is separate

Human-readable corpus addressing uses a locator object:

```json
{
  "scheme": "STEPHANUS",
  "value": "514a",
  "components": {
    "page": 514,
    "section": "a"
  }
}
```

A different profile may use:

```json
{
  "scheme": "BEKKER",
  "value": "980a21",
  "components": {
    "page": 980,
    "column": "a",
    "line": 21
  }
}
```

The generic framework validates the locator envelope. The Thinker Profile validates scheme-specific components.

## Generated IDs

Generated segment, assertion, memory, retrieval, snapshot and provenance IDs should be collision-resistant and sortable where practical.

ULID remains the preferred candidate for production-generated object suffixes, but the exact generator will be frozen separately before production ingestion.

## Change rule

A metadata correction retains an object's ID.

A genuinely incorrect logical segmentation boundary may require new segment IDs. Such changes must be recorded through an explicit migration map and may not rewrite already frozen releases.
