# EPIGRAM ATTRIBUTION MODEL 0001 — witness-level author ascriptions and homonymy

**Status:** Phase 1 design note; proposed model, not yet frozen

## Problem

For the Platonic epigram corpus, a single work-level field such as `author = Plato` destroys historically important information.

The same logical text may be:

- explicitly attributed to Plato the philosopher in one witness;
- attributed simply to “Plato” in another witness;
- transmitted anonymously elsewhere;
- attributed to another named poet in a competing witness;
- assigned by modern editors to Plato the Younger because of homonymy;
- explicitly transmitted under Plato the Younger or Plato the Comic Poet.

These are different **transmission facts** and must remain separate from the modern A/B/C/D authenticity assessment.

## Decision direction

PROJECT PLATO should model author attribution as **witness-level assertions**, not as an intrinsic property of the logical epigram.

The logical text remains edition- and attribution-independent.

Conceptually:

```text
logical epigram
   |
   +-- witness A -> transmitted as "Plato the philosopher"
   +-- witness B -> anonymous
   +-- witness C -> "Philodemus"
   |
   +-- modern attribution analysis
          -> Plato Junior / Philodemus / uncertain
   |
   +-- separate authenticity assertion
          -> A/B/C/D for philosopher-Plato profile
```

## Required distinctions

### 1. Transmitted ascription

A claim directly present in an ancient/medieval witness, heading, quotation or scholium.

Examples:

- `PLATO_PHILOSOPHER`
- `PLATO_JUNIOR`
- `PLATO_COMICUS`
- `PLATO_UNSPECIFIED`
- another named author
- anonymous

This layer records what the witness says, not whether the witness is correct.

### 2. Modern attribution analysis

A modern scholarly conclusion about the likely author or authorial layer.

Examples:

- Page's assignment of several ecphrastic poems to Plato Junior;
- preference for Philodemus over Plato for AP 5.80;
- preference for Asclepiades as the source behind the Archeanassa tradition.

This must not overwrite the transmitted heading.

### 3. Profile authenticity

The existing `PLATO_AUTHENTICITY_AD_V1` A/B/C/D judgment answers a different question:

> How strong is the modern case that this logical text is by Plato the philosopher?

It remains CUSTODIAN-only and versioned under ADR-0014.

## Proposed attribution-target registry

For the Plato profile the registry should at minimum distinguish:

```text
TH.PLATO.ATTR_TARGET.PLATO_PHILOSOPHER
TH.PLATO.ATTR_TARGET.PLATO_UNSPECIFIED
TH.PLATO.ATTR_TARGET.PLATO_JUNIOR
TH.PLATO.ATTR_TARGET.PLATO_COMICUS
TH.PLATO.ATTR_TARGET.ANONYMOUS
```

Named competing authors should use stable registry targets rather than free-text-only values where identity can be established, for example Philodemus, Antipater of Thessalonica, Statyllius Flaccus, Ammianus, Hermocreon, Musicius, Leonidas or Posidippus.

A verbatim witness label should still be preserved alongside the normalized target.

## Proposed assertion shape

Illustrative only:

```json
{
  "assertion_id": "TH.PLATO.ATTR.<uuidv7>",
  "catalog_id": "TH.PLATO.CAT.EPIGRAM_5_80",
  "witness_ref": "...",
  "assertion_layer": "TRANSMITTED_ASCRIPTION",
  "target_id": "TH.PLATO.ATTR_TARGET.PLATO_UNSPECIFIED",
  "label_verbatim": "Πλάτωνος",
  "assertion_form": "HEADING",
  "status": "DIRECT",
  "runtime_visibility": "CUSTODIAN_ONLY"
}
```

A modern reassignment would be a different object:

```json
{
  "assertion_id": "TH.PLATO.ATTR.<uuidv7>",
  "catalog_id": "TH.PLATO.CAT.EPIGRAM_5_80",
  "source_ref": "...",
  "assertion_layer": "MODERN_ATTRIBUTION",
  "target_id": "TH.PLATO.ATTR_TARGET.PHILODEMUS",
  "status": "ARGUED",
  "runtime_visibility": "CUSTODIAN_ONLY"
}
```

## Important rule: attribution target is not logical identity

If one manuscript says “Plato” and another says “Philodemus”, that does **not** automatically create two logical epigrams.

Conversely, two texts with related subject matter or one derived from another should not be collapsed merely because both acquired the same author label.

Logical text identity must continue to depend on textual/work identity and source alignment.

## Important rule: homonymy is not forgery

A poem transmitted under `Πλάτωνος νεωτέρου` is not automatically “pseudo-Platonic” in the same sense as a deliberate forgery under the philosopher's name.

For the philosopher-Plato profile it may be non-original, but historically the mechanism can be simple homonymy.

PROJECT PLATO should therefore preserve at least these causal possibilities:

- deliberate pseudepigraphic attribution;
- later mistaken reassignment;
- homonymic confusion;
- anonymous text later supplied with an author;
- unresolved competing transmission.

These mechanisms belong to CUSTODIAN analysis and must not be collapsed into one `spurious=true` flag.

## Evidence motivating the model

Pelucchi 2025 explicitly records:

- three items transmitted as Plato the Younger: AP 9.13a, 9.748, 9.751;
- AP 9.359 assigned to Plato the Comic Poet in one transmission;
- competing attributions involving Philodemus, Musicius, Statyllius Flaccus, Ammianus, Hermocreon, Antipater and others;
- anonymous transmission for some otherwise “Platonic” items.

Massimo 2020 likewise shows that Page assigned several poems headed only “Plato” to Plato Junior and treats homonymy as a distinct mechanism of pseudepigraphic appearance.

## Runtime consequence

The active PLATO instance does not need this modern apparatus by default.

Witness-level attribution metadata and modern author analysis remain `CUSTODIAN_ONLY`.

If a future experiment deliberately teaches PLATO that a poem was historically disputed, that information becomes ACQUIRED testimony rather than hidden metadata leaking directly into ORIGINAL.

## Implementation sequence

1. finish the Pelucchi 37-item crosswalk;
2. create the attribution-target registry;
3. create a profile-level attribution-assertion schema;
4. migrate epigram member records without changing logical identity unnecessarily;
5. add structural tests for homonymy and competing attributions;
6. only then freeze epigram scope and assign work-level A/B/C/D authenticity grades.

This note deliberately postpones schema freezing until the complete 37-item transmission map has been reconstructed.
