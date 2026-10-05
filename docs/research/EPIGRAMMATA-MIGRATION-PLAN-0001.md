# EPIGRAMMATA MIGRATION PLAN 0001 — pre-v0.1.5 catalog delta

**Status:** Active Phase 1 migration plan; catalog mutation not yet authorized

## Purpose

Convert the machine-readable Page/Massimo crosswalk into a deterministic pre-migration delta against the current `catalog-v0.1.4.json`.

This document originally blocked `catalog-v0.1.5` on recovery of the complete historical scope. That scope is now source-complete at 37 items from Pelucchi 2025. Full Pelucchi 2026 ordinal numbering is no longer a prerequisite for identity-safe catalog migration; unknown ordinals remain null rather than being inferred.

## Current Page/Massimo baseline delta

The 31 Page/Massimo rows divide into:

- **MATCH — 19**: already represented cleanly by current Epigrammata members;
- **MISSING — 3**: EG IX, XIV and XXIII require catalog objects once identity is source-verified;
- **UNRESOLVED — 2**: EG III (AP 5.77/5.78 conflict) and EG XXXI (gold/halter; AP 9.44 provisional match);
- **EXCLUDE_FROM_PHILOSOPHER_PROFILE — 7**: the Plato Junior/homonymy layer must not silently enter philosopher-Plato runtime scope.

The current 23-member catalog contains one historically justified item not represented as an exact Page/Massimo row: `TH.PLATO.CAT.EPIGRAM_9_3`. AP 7.268 is no longer supplemental: crosswalk v0.1.1 correctly identifies it as Page/FGE XVIII.

## Migration invariants

1. No `PLATO_YOUNGER` row may become a philosopher-Plato runtime candidate.
2. EG III remains one unresolved identity problem; do not create a separate AP 5.77 record while AP 5.78 is retained.
3. EG XXXI remains unresolved until the direct Page/Pelucchi apparatus confirms the AP 9.44 relationship.
4. Missing Page rows may now be normalized against the source-complete 37-item historical scope; no ordinal is inferred where Pelucchi 2026 numbering has not been directly verified.
5. Current supplemental AP 9.3 remains in place; AP 7.268 is now a normal Page/FGE XVIII match.
6. `pelucchi_2026_number` must not be fabricated from arithmetic or guessed ordering; null remains valid for unverified ordinals.

## Automated gate

`scripts/check_epigram_migration_plan.py` enforces the current bucket counts, current-catalog references, supplemental items and runtime exclusion of mapped Plato Junior material.

The script still protects the Page/Massimo delta. A separate historical-scope gate now establishes the complete 37-item source scope; the remaining migration blockers are data-model and identity normalization issues, not missing corpus scope.

## Historical scope milestone

The source-level 37-item scope has now been reconstructed directly from Pelucchi 2025 and is stored in `epigram-historical-scope-v0.1.0.json`. The 2026 edition remains important for exact ordinal numbering and apparatus work, but the catalog no longer depends on guessing that sequence.

Reference edition:

Marco Pelucchi, *Gli epigrammi di Platone. Studio introduttivo, edizione e commento*, Milano University Press, 2026, DOI 10.54103/consonanze.269.

The publisher page confirms that the volume is open access under CC BY-SA 4.0. Direct PDF retrieval is currently blocked in the present tool environment, so PROJECT PLATO must not infer the missing sequence indirectly.

## Correction note: EG XVIII

The first crosswalk version inherited an erroneous `AP 7.368` reading for EG XVIII. Cross-checking against independent scholarship shows that FGE XVIII 640 is **AP 7.268**. The migration plan now treats this row as an existing MATCH, not a catalog gap.
