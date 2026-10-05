# EPIGRAMMATA SCOPE 0002 — current 23-item inventory is not the complete historical corpus

**Status:** Active Phase 1 scope correction

## Finding

The current PROJECT PLATO catalog contains 23 individually addressable epigrams because that was the set exposed by the initial digital `Anthologia Graeca` author index used for the first inventory.

That set must **not** be treated as the complete historical corpus of epigrams attributed to Plato.

Recent specialist scholarship uses a broader corpus:

- Marco Pelucchi (2025) describes **37 texts transmitted under Plato's name**, widely regarded by modern scholars as spurious.
- Marco Pelucchi's 2026 critical edition states that it includes all epigrams assigned to Plato by ancient tradition.
- Davide Massimo (2020) notes that D. L. Page's `Epigrammata Graeca` included **31 epigrams variously ascribed to Plato**; Page's later `Further Greek Epigrams` narrowed that working selection to 24.
- Older anthology scholarship likewise records roughly thirty-one Plato-ascribed epigrams and notes that not all survive solely through the Greek Anthology.

Therefore the current 23-member catalog is a **provisional digital-index inventory**, not a frozen complete corpus.

## Why the counts differ

The historical Plato-epigram corpus is not defined by one anthology author page.

Relevant transmission can include:

- Palatine Anthology / Planudean Anthology attributions;
- competing attributions in manuscript witnesses;
- epigrams preserved outside the Anthology;
- epigrams quoted by Diogenes Laertius, Athenaeus and later authors;
- items separated by modern editors as `Plato Junior`, anonymous, doubtful or competing attribution;
- different editorial decisions about whether closely related textual witnesses count as one item or separate items.

Consequently, numerical totals such as 23, 24, 31 and 37 refer to different editorial/transmission scopes and cannot be equated without a crosswalk.

## Important examples already missing or requiring correction

The 2025 Pelucchi overview explicitly discusses material beyond the current PROJECT PLATO 23-item list, including:

- AP VII 217 (Archeanassa);
- AP VII 516b / VII 35 (Pindar tradition);
- AP IX 39 and AP IX 827 (omitted from the first working inventory but explicit in Pelucchi's attribution discussion);
- Cougny III 33 (Aristophanes);
- additional transmitted material that must be resolved from the critical edition.

The current Perseus catalog also signals AP 9.44? among Plato's `Epigrammata`, while the first PROJECT PLATO digital inventory did not include AP 9.44.

These discrepancies show that the catalog requires a source-by-source reconstruction rather than a simple scrape of one author index.

## Authenticity consequence

Do **not** bulk-classify the current 23 members as D before the corpus crosswalk is complete.

The modern scholarly baseline is strongly skeptical:

- Pelucchi (2026): the anciently attributed corpus is now almost unanimously regarded as inauthentic.
- Pelucchi (2025): 37 texts, widely regarded as spurious.
- Massimo (2020): the corpus is generally believed spurious and is often discussed as the work of “Pseudo-Plato”.

However, older and some modern discussions preserve individual candidates or subgroups as potentially authentic. The identity of those candidates must be mapped to exact AP/other-source references before assigning work-level A/B/C/D grades.

## Required next step — updated

The 37-item source-level historical scope is now complete. The project must now normalize the 14 scope items missing from catalog v0.1.4 and migrate once to catalog v0.1.5. The existing **Epigram Crosswalk** and historical-scope artifact provide the migration input.

The crosswalk records with one row per historically attested item and columns for at least:

- project catalog ID;
- Pelucchi 2026 number;
- Page `Epigrammata Graeca` number;
- Page `Further Greek Epigrams` number where applicable;
- Greek Anthology reference(s);
- non-Anthology source reference(s);
- manuscript attribution variants;
- competing author attribution(s);
- survival status;
- current PROJECT PLATO inclusion status;
- authenticity-review status.

PROJECT PLATO has now source-verified the 37-item historical scope. Before individual authenticity grades are frozen it must still: add/normalize the 14 missing catalog objects, preserve witness relationships and homonymy, and then freeze the migrated epigram identities.

## Principal sources

- Marco Pelucchi, “Gli epigrammi attribuiti a Platone: problemi ecdotici di un corpus pseudepigrafo”, *Atene e Roma* 19 (2025), pp. 140–157. DOI: https://doi.org/10.7347/AR-2025-p140
- Marco Pelucchi, *Gli epigrammi di Platone. Studio introduttivo, edizione e commento*, Milano University Press, 2026. DOI: https://doi.org/10.54103/consonanze.269 — open access, CC BY-SA 4.0.
- Davide Massimo, “Defining a ‘Pseudo–Plato’ epigrammatist”, in *Defining Authorship, Debating Authenticity*, 2020. DOI: https://doi.org/10.1515/9783110684629-004
- D. L. Page, *Epigrammata Graeca* (1975) and *Further Greek Epigrams* (1981).
- Perseus Catalog, `tlg0059.tlg039`.

## Catalog status

Until the crosswalk is completed:

- `TH.PLATO.CAT.EPIGRAMMATA` remains `PENDING_REVIEW`;
- its 23 current child records are retained as verified individual attributions from the initial source;
- the number 23 must not be described as the complete Plato epigram corpus;
- the source-level historical scope is now fixed at 37 items;
- Phase 1 “Build the full Corpus Platonicum catalog” remains open until the 14 missing objects are normalized into catalog v0.1.5.
