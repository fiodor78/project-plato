# EPIGRAMMATA CROSSWALK 0001 — Page / Massimo baseline

**Status:** Phase 1 working crosswalk, not yet frozen

## Purpose

Build a source-controlled bridge between:

- D. L. Page, *Epigrammata Graeca* (EG, 1975);
- D. L. Page, *Further Greek Epigrams* (FGE, 1981);
- Davide Massimo's 2020 prospectus of the 31 Page epigrams;
- Greek Anthology / Appendix Planudea references;
- non-Anthology literary witnesses;
- the current PROJECT PLATO catalog.

This document is an intermediate research artifact. It does **not** replace the catalog and must not be used as a complete corpus definition until checked against Pelucchi's 2026 critical edition.

## Evidence baseline

Massimo states that Page's *Epigrammata Graeca* contained 31 epigrams variously ascribed to Plato, while *Further Greek Epigrams* narrowed that working set to 24. Twenty-nine of the 31 have Greek Anthology transmission; one is preserved through Athenaeus and one through the *Vita Aristophanis* / Olympiodorus tradition.

Source:
Davide Massimo, “Defining a ‘Pseudo–Plato’ Epigrammatist” (2020), DOI:
https://doi.org/10.1515/9783110684629-004

## Page / Massimo 31-item crosswalk

| EG | FGE | Anthology / witness | Current PROJECT PLATO | Status / note |
|---:|---:|---|---|---|
| I | I | AP 7.669 | `TH.PLATO.CAT.EPIGRAM_7_669` | MATCH |
| II | II | AP 7.670 | `TH.PLATO.CAT.EPIGRAM_7_670` | MATCH |
| III | III | **Massimo table: AP 5.77** | current catalog has AP 5.78 | **NUMBERING CONFLICT — VERIFY AGAINST PELUCCHI** |
| IV | IV | AP 5.79 | `TH.PLATO.CAT.EPIGRAM_5_79` | MATCH |
| V | V | AP 5.80 | `TH.PLATO.CAT.EPIGRAM_5_80` | MATCH |
| VI | VI | AP 7.100 | `TH.PLATO.CAT.EPIGRAM_7_100` | MATCH |
| VII | VII | AP 9.39 | `TH.PLATO.CAT.EPIGRAM_9_39` | MATCH; anthology attribution is not uniform |
| VIII | VIII | AP 6.1 | `TH.PLATO.CAT.EPIGRAM_6_1` | MATCH |
| IX | IX | Diog. Laert. 3.31; Ath. 13.589c; cf. AP 7.217 | no exact current record | MISSING / relationship to AP 7.217 must be normalized |
| X | X | AP 7.99 | `TH.PLATO.CAT.EPIGRAM_7_99` | MATCH |
| XI | XI | AP 7.259 | `TH.PLATO.CAT.EPIGRAM_7_259` | MATCH |
| XII | XII | AP 7.256 | `TH.PLATO.CAT.EPIGRAM_7_256` | MATCH |
| XIII | XIII | AP 9.506 | `TH.PLATO.CAT.EPIGRAM_9_506` | MATCH |
| XIV | XIV | *Vita Aristophanis* 52 Koster; Olympiodorus; Prolegomena | no current record | MISSING non-Anthology witness |
| XV | XV | AP 9.51 | `TH.PLATO.CAT.EPIGRAM_9_51` | MATCH |
| XVI | XVI | “AP 9.823” / minor sylloge | `TH.PLATO.CAT.EPIGRAM_9_823` | MATCH |
| XVII | XVII | AP 16.13 | `TH.PLATO.CAT.EPIGRAM_16_13` | MATCH |
| XVIII | XVIII | **AP 7.268** | `TH.PLATO.CAT.EPIGRAM_7_268` | **MATCH — corrected from erroneous AP 7.368 extraction** |
| XIX | XIX | AP 7.265 | `TH.PLATO.CAT.EPIGRAM_7_265` | MATCH |
| XX | XX | AP 7.269 | `TH.PLATO.CAT.EPIGRAM_7_269` | MATCH |
| XXI | XXI | AP 6.43 | `TH.PLATO.CAT.EPIGRAM_6_43` | MATCH |
| XXII | XXII(a) | “AP 9.826” / minor sylloge | `TH.PLATO.CAT.EPIGRAM_9_826` | MATCH |
| XXIII | XXII(b) | “AP 9.827” / minor sylloge | no current record | MISSING; Ammonius/Plato attribution variation |
| XXIV | — | AP 16.248 | `TH.PLATO.CAT.EPIGRAM_16_248` | MATCH; competing attribution; Page links to Plato Junior |
| XXV | XXIII | AP 16.160 | no current record | MISSING; Page assigns to Plato Junior |
| XXVI | — | AP 16.161 | no current record | MISSING; Page assigns to Plato Junior |
| XXVII | — | AP 9.747 | `TH.PLATO.CAT.EPIGRAM_9_747` | MATCH; Page assigns to Plato Junior |
| XXVIII | — | AP 9.748 (OCR in one table extraction reads 8.748) | no current record | MISSING; explicitly Plato Junior |
| XXIX | — | AP 9.751 | no current record | MISSING; explicitly Plato Junior |
| XXX | — | AP 9.13 | no current record | MISSING; explicitly Plato Junior |
| XXXI | — | Diog. Laert. 3.33 “on gold”; AP 9.44 tradition | no current record | **PROVISIONAL MATCH — verify direct Page/Pelucchi mapping** |

## Current catalog items not accounted for by the Page/Massimo 31 baseline

Two current PROJECT PLATO member records required special handling in the first crosswalk:

- AP 5.78
- AP 9.3

These must **not** be deleted. Later and broader scholarship clearly treats at least these references as part of the historical Plato-attribution problem.

In particular:

- current scholarship commonly cites the Agathon kiss epigram as **AP 5.78**, while the extracted Massimo table prints **AP 5.77** for EG III;
- the first machine extraction incorrectly read EG XVIII as AP 7.368; independent scholarly citation gives **AP 7.268 = FGE XVIII 640**, so v0.1.1 maps EG XVIII to the already existing AP 7.268 record;
- other modern scholarship explicitly discusses AP 9.3 as “Plato” or Antipater of Thessalonica.

This indicates an editorial-numbering / transmission-scope problem, not merely a bad catalog scrape.

## Plato Junior / homonymy warning

Massimo records a distinct homonymy layer:

- AP 9.748, AP 9.751 and AP 9.13 explicitly bear a heading equivalent to **Plato the Younger**;
- following Page, AP 9.747, AP 16.161, AP 16.248 and AP 16.160 are also associated with Plato Junior;
- Massimo raises the possibility that the minor-sylloge AP 9.826 / 9.827 pair may belong to the same layer.

PROJECT PLATO must therefore distinguish:

1. ancient attribution to **Plato the philosopher**;
2. ancient attribution simply to “Plato” where homonymy is unresolved;
3. explicit or strong attribution to **Plato Junior**.

A text associated specifically with Plato Junior should not silently become ORIGINAL knowledge for the philosopher-Plato profile merely because a generic digital author index files it under “Plato”.

## The AP 5.77 / AP 5.78 problem

The extracted Massimo table gives EG III as AP 5.77, while numerous independent modern sources and the current Perseus Plato catalog identify the famous Agathon “soul at the lips” epigram as AP 5.78.

Therefore:

- retain current AP 5.78;
- do not add AP 5.77 as a separate Plato epigram yet;
- mark the Page/Massimo crosswalk cell as unresolved until checked against the printed Page/Pelucchi apparatus.

This is exactly the kind of numbering/witness conflict the crosswalk is intended to prevent from becoming a duplicate logical work.

## The XXXI / AP 9.44 problem

Massimo explicitly says Diogenes Laertius quotes EG XXXI “on gold”. AP 9.44 is transmitted under Statyllius Flaccus with an alternative attribution to Plato and has the same gold/halter narrative.

The identification is therefore highly plausible, but PROJECT PLATO keeps it **PROVISIONAL** until direct Page or Pelucchi confirmation is captured.

## Relation to Pelucchi's broader 37-text corpus

Pelucchi (2025) describes 37 texts transmitted under Plato's name and his 2026 critical edition claims to include all epigrams assigned to “Plato” by ancient tradition.

His 2025 overview explicitly mentions, among others:

- AP 5.78, 5.80;
- AP 7.99, 7.100;
- AP 7.217, 7.669, 7.670;
- AP 7.256, 7.259;
- AP 7.265, 7.268, 7.269;
- AP 6.1, 6.43;
- Cougny III 33;
- AP 9.506;
- AP 7.516b / 7.35.

This demonstrates that Pelucchi's 37-item corpus cannot be reconstructed safely by taking Page's 31 and simply appending arbitrary digital-index results.

## Next gate

Before modifying the production catalog:

1. obtain Pelucchi 2026's complete 37-item edition list;
2. map all 37 to the Page/Massimo rows where possible;
3. resolve AP 5.77/5.78;
4. verify XXXI/AP 9.44;
5. distinguish philosopher Plato vs Plato Junior vs unresolved homonymy;
6. identify which current 23 records are valid additions beyond Page's 31;
7. only then create catalog v0.1.5.

## Current conclusion

The Page/Massimo baseline proves that the current 23-member `Epigrammata` inventory is incomplete and also that simple “author = Plato” metadata is insufficient.

The next catalog version should be driven by a **transmission crosswalk**, not by one anthology's author index.

## EG XVIII correction

Crosswalk v0.1.0 inherited **AP 7.368** from a machine-readable extraction of the Massimo/Page table. This was incorrect.

Independent scholarship on the seventh book of the Anthologia Palatina identifies the Platonic item as:

`AP 7.268 = FGE XVIII 640`.

By contrast, AP 7.368 is transmitted as an epigram of Erycius.

Crosswalk v0.1.1 therefore changes EG XVIII to AP 7.268 and maps it to the existing catalog record `TH.PLATO.CAT.EPIGRAM_7_268`.

This correction reduces Page-baseline `MISSING` rows from four to three and demonstrates why automated source cross-checks are required before catalog expansion.
