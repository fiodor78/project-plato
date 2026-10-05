# EPIGRAMMATA PELUCCHI INVENTORY 0001 — source-explicit references from Pelucchi 2025

**Status:** Phase 1 working inventory; incomplete by design

## Purpose

Record only those epigram references that can be verified directly from Marco Pelucchi's 2025 survey before the full 2026 critical-edition list is obtained.

Pelucchi states that the historical corpus under Plato's name consists of **37 texts**. This document does not infer the seven not yet resolved from arithmetic; it separates source-explicit references from unresolved members.

Primary source:
Marco Pelucchi, “Gli epigrammi attribuiti a Platone: problemi ecdotici di un corpus pseudepigrafo”, *Atene e Roma* 19 (2025), 140–157.
DOI: https://doi.org/10.7347/AR-2025-p140

## References explicitly recoverable from the 2025 article

### Erotic / biographical / Socratic associations
- AP 5.78 — Agathon
- AP 5.79 — apple-courtship poem; explicitly treated as assigned to Plato
- AP 5.80 — Xanthippe; competing Philodemus transmission
- AP 7.99 — Dion
- AP 7.100 — Phaedrus/Alexis context
- AP 7.217 — Archeanassa tradition / relationship to the non-Anthology Platonic version
- AP 7.669 — Aster
- AP 7.670 — Aster

### Sepulchral
- AP 7.256 — Eretrians
- AP 7.259 — Eretrians
- AP 7.265 — shipwreck
- AP 7.268 — shipwreck
- AP 7.269 — shipwreck

### Dedications / anathematic
- AP 6.1 — Laïs and the mirror
- AP 6.43 — frog dedication

### Poets / literary figures
- Cougny III 33 — Aristophanes; also transmitted by Vitae Aristophanis / Platonic biographical tradition
- AP 9.506 — Sappho
- AP 7.516b / AP 7.35 — Pindar textual tradition; competing Leonidas attribution

### Gnomic / anecdotal / miscellaneous
- AP 9.51 — time
- AP 9.3 — tree lament; competing Antipater of Thessalonica attribution
- AP 9.44 — gold/halter anecdote; competing Statyllius Flaccus attribution
- AP 9.45 — paired gold/halter anecdote
- AP 9.359 — philosophical/gnomic poem; assigned in one tradition to Plato Comicus and elsewhere to Posidippus/other authors

### Bucolic / locus amoenus
- AP 9.823
- APl 11
- APl 13
- APl 210

### Ecphrastic
- AP 9.747
- AP 9.826
- APl 248
- APl 160 — Cnidian Aphrodite
- APl 161 — Cnidian Aphrodite

### Explicit Plato Junior / homonymy layer
The same article explicitly identifies three texts transmitted as works of **Plato the Younger**:
- AP 9.13a
- AP 9.748
- AP 9.751

These must be represented as a homonymy/attribution layer and must not be silently treated as works of Plato the philosopher.

## Count and caution

The source-explicit list above contains more than the original 23-item PROJECT PLATO inventory and demonstrates several distinct attribution mechanisms.

It must **not** yet be equated mechanically with Pelucchi's final 37 edited texts because:

1. some references represent variant witnesses of one logical epigram rather than separate texts;
2. AP 7.217 is related to a Platonic Archeanassa version transmitted outside the Anthology;
3. AP 7.516b / AP 7.35 is a witness relationship;
4. the three Plato Junior texts involve a homonymous author;
5. AP 9.359 is explicitly attributed to Plato Comicus in one transmission;
6. Pelucchi's final 2026 edition may normalize, split or combine witnesses differently.

## Important corrections to the current PROJECT PLATO assumptions

### AP 5.78 is real, not an accidental substitute for AP 5.77

Pelucchi 2025 explicitly discusses the famous Agathon epigram as **AP 5.78** and cites modern work on AP 5.78. This agrees with Perseus/Paton and other modern scholarship.

The Page/Massimo extraction that prints EG III as AP 5.77 therefore cannot be used to replace the current AP 5.78 record. The discrepancy remains a crosswalk problem.

### AP 7.268 and AP 9.3 are not noise

Both appear in the broader modern discussion of Plato-attributed material. Their presence in the current catalog is therefore substantively justified, even though they do not align cleanly with the 31-row Massimo/Page baseline.

### AP 9.44 and AP 9.45 belong to a paired anecdotal tradition

Pelucchi explicitly treats both as part of the Plato-attribution problem. This strengthens the case that EG XXXI “on gold” needs to be crosswalked to this two-text tradition rather than naively mapped to one AP number without apparatus review.

## Current PROJECT PLATO action

Do not yet create `catalog-v0.1.5`.

Before catalog mutation:

- obtain the exact 37-item numbering/order from Pelucchi 2026;
- determine which references above are witnesses vs distinct logical texts;
- model explicit homonymy (Plato the Younger; Plato Comicus);
- reconcile AP 5.78 with Page/Massimo's extracted AP 5.77;
- resolve the gold/halter pair AP 9.44–45;
- map the non-Anthology Aristophanes and Archeanassa witnesses;
- then migrate the catalog once, with tests.

## Source significance

Pelucchi's article is especially valuable because it shows that the problem is not simply “which epigrams are authentic”. The prior question is **which historical textual objects were actually attributed to which Plato, in which witness and at what stage of transmission**.

That distinction should be represented structurally in the profile before individual authenticity grades are frozen.
