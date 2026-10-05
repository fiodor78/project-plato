# EPIGRAMMATA HISTORICAL SCOPE 0003 — source-complete 37-item corpus

**Status:** Phase 1 historical scope complete at source-reference level; identity normalization remains active

## Finding

Marco Pelucchi's 2025 survey states explicitly that **thirty-seven epigrams** are variously attributed to Plato in Greek and Latin sources.

Pages 142–143 enumerate the thematic groups and most of the references. Page 144 supplies the important attribution/homonymy layer, including AP 9.39, AP 9.827, three texts explicitly transmitted as Plato the Younger, and AP 9.359 assigned to Plato Comicus. AP 5.79 is discussed explicitly later in the article (p. 153) as a poem assigned to Plato.

Taken together, these source-explicit references yield exactly 37 logical historical items.

## Correction of two earlier project errors

### AP 9.144

An earlier working scope note mentioned AP 9.144. That was not supported by Pelucchi's 37-item list and is removed from the PROJECT PLATO source-complete scope.

AP 9.144 is not used to make the count reach 37.

### Page EG XVIII

The first machine crosswalk inherited AP 7.368 for Page EG XVIII from an extracted table. Cross-checking against independent scholarship shows that the Platonic Page/FGE item is **AP 7.268 = FGE XVIII 640**. AP 7.368 belongs to Erycius.

The historical scope therefore includes AP 7.268, not AP 7.368.

## Why the previous count looked like 35

The first PROJECT PLATO Pelucchi working inventory contained 35 source-explicit logical items but omitted two references that are stated on p. 144 of Pelucchi 2025:

- AP 9.39 (with competing Musicius attribution);
- AP 9.827 (with competing Ammianus attribution).

Adding those two produces the stated total of 37 without inventing a missing item.

## Structural result

The machine artifact `epigram-historical-scope-v0.1.0.json` now contains exactly 37 items.

Of those:

- 23 map one-to-one to the current provisional Epigrammata child records;
- 14 require catalog insertion or identity normalization;
- explicit Plato-the-Younger and Plato-Comicus material remains inside the **historical attribution scope** but is structurally excluded from philosopher-Plato candidacy;
- competing and anonymous attributions remain visible rather than being flattened.

## Pelucchi 2026 numbering

The historical scope is now complete **without fabricating the full 2026 ordinal sequence**.

Only directly verified 2026 numbering anchors are stored. Unknown ordinals remain null. The project no longer needs every 2026 number merely to know which 37 historical objects belong to the attribution scope.

## Consequence for catalog v0.1.5

The blocker has changed.

The project no longer lacks the 37-item historical scope. The remaining work before catalog migration is:

1. normalize the 14 missing items into catalog objects;
2. preserve witness relationships for Archeanassa and the Pindar tradition;
3. preserve competing attributions;
4. keep homonymous Plato Junior / Plato Comicus items out of philosopher-Plato runtime candidacy;
5. update the catalog schema so epigram metadata is not limited to a simple Greek-Anthology AP number.

This is now an **identity/data-model migration problem**, not a missing-scope problem.
