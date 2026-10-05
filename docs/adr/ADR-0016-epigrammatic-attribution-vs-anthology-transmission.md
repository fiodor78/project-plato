# ADR-0016 — Epigrammatic attribution is distinct from anthology transmission

**Status:** Accepted

## Context

The initial Plato catalog used `ANTHOLOGICAL_ASCRIPTION` as the scope class for Epigrammata because the first machine inventory came from Greek Anthology references.

Source-complete reconstruction of the 37-item historical corpus shows that this is too narrow.

The transmitted material includes:

- ordinary Anthologia Palatina / Appendix Planudea witnesses;
- a Platonic Archeanassa tradition also preserved through Diogenes Laertius and Athenaeus;
- Cougny III 33 with non-Anthology witnesses;
- variant/parallel witness relationships;
- items transmitted under Plato the Younger or Plato Comicus;
- competing author attributions.

Therefore a logical epigram identity cannot be equated with a single AP/APl locator.

## Decision

Add the profile scope class:

`EPIGRAMMATIC_ASCRIPTION`

Meaning:

> A logical epigrammatic object belongs to the historical Plato-attribution problem, regardless of whether its surviving witness is anthological, biographical, scholastic or otherwise indirect.

`ANTHOLOGICAL_ASCRIPTION` remains valid as a narrower transmission fact.

An epigram may therefore carry:

- both `EPIGRAMMATIC_ASCRIPTION` and `ANTHOLOGICAL_ASCRIPTION`; or
- only `EPIGRAMMATIC_ASCRIPTION` where the defining witness is non-anthological.

## Identity rule

The stable catalog object represents a **logical epigrammatic object**.

Witness references (AP, APl, Cougny, Diogenes, Athenaeus, etc.) are evidence attached to that object and do not define identity by themselves.

## Homonym rule

Historical scope may include material attributed to a homonymous Plato.

Such material remains relevant to corpus history but receives `HOMONYM_EXCLUDED` / `CATALOG_ONLY` treatment for the philosopher-Plato runtime unless later evidence changes the identity assessment.

## Consequence

Catalog v0.1.5 may represent all 37 source-explicit items without pretending that every item is simply an Anthologia Graeca number.

This ADR extends the Phase 1 scope taxonomy; it does not alter modern A/B/C/D authenticity semantics.
