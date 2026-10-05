# EPIGRAMMATA MIGRATION PLAN 0001 — pre-v0.1.5 catalog delta

**Status:** Active Phase 1 migration plan; catalog mutation not yet authorized

## Purpose

Convert the machine-readable Page/Massimo crosswalk into a deterministic pre-migration delta against the current `catalog-v0.1.4.json`.

This document does **not** authorize creation of `catalog-v0.1.5`. The exact Pelucchi 2026 37-item numbering/order remains a required gate.

## Current Page/Massimo baseline delta

The 31 Page/Massimo rows divide into:

- **MATCH — 18**: already represented cleanly by current Epigrammata members;
- **MISSING — 4**: EG IX, XIV, XVIII and XXIII require catalog objects once identity is source-verified;
- **UNRESOLVED — 2**: EG III (AP 5.77/5.78 conflict) and EG XXXI (gold/halter; AP 9.44 provisional match);
- **EXCLUDE_FROM_PHILOSOPHER_PROFILE — 7**: the Plato Junior/homonymy layer must not silently enter philosopher-Plato runtime scope.

The current 23-member catalog also contains two historically justified items not represented as exact Page/Massimo rows:

- `TH.PLATO.CAT.EPIGRAM_7_268`;
- `TH.PLATO.CAT.EPIGRAM_9_3`.

They are retained as **supplemental current-catalog evidence**, not deleted merely to make the Page count fit.

## Migration invariants

1. No `PLATO_YOUNGER` row may become a philosopher-Plato runtime candidate.
2. EG III remains one unresolved identity problem; do not create a separate AP 5.77 record while AP 5.78 is retained.
3. EG XXXI remains unresolved until the direct Page/Pelucchi apparatus confirms the AP 9.44 relationship.
4. Missing Page rows may be prepared, but catalog insertion waits for the Pelucchi 2026 crosswalk.
5. Current supplemental AP 7.268 and AP 9.3 remain in place.
6. `pelucchi_2026_number` must not be fabricated from arithmetic or guessed ordering.

## Automated gate

`scripts/check_epigram_migration_plan.py` enforces the current bucket counts, current-catalog references, supplemental items and runtime exclusion of mapped Plato Junior material.

The script ends by stating explicitly that migration is not authorized while the Pelucchi 2026 numbering remains uncaptured.

## Next source task

Obtain the exact 37-item sequence from:

Marco Pelucchi, *Gli epigrammi di Platone. Studio introduttivo, edizione e commento*, Milano University Press, 2026, DOI 10.54103/consonanze.269.

The publisher page confirms that the volume is open access under CC BY-SA 4.0. Direct PDF retrieval is currently blocked in the present tool environment, so PROJECT PLATO must not infer the missing sequence indirectly.
