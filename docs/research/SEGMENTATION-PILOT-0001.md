# SEGMENTATION PILOT 0001 — representative Platonic text structures

**Status:** Completed Phase 0 research pilot  
**Purpose:** Test SPEC-0002 against real structural patterns without ingesting production corpus data.

This pilot examines only structural behavior. It does **not** register these source texts as production corpus objects.

## Sources consulted

Primary structural references were checked against public Perseus/Scaife records:

- Apology 17a ff.: https://scaife.perseus.org/library/urn:cts:greekLit:tlg0059.tlg002.perseus-grc2/
- Republic 327a ff.: https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0167
- Symposium 172a ff.: https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0173:text=Sym.
- Menexenus: https://beta.perseus.tufts.edu/urn:cts:greekLit:tlg0059.tlg028.perseus-grc2/
- Letter VII: https://www.perseus.tufts.edu/hopper/text?doc=urn:cts:greekLit:tlg0059.tlg036.perseus-grc1:7
- Definitiones: https://beta.perseus.tufts.edu/urn:cts:greekLit:tlg0059.tlg037.1st1K-grc1:1/

These references are research inputs only. Source-asset registration and redistribution decisions remain separate ingestion work.

## Case 1 — Apology: long uninterrupted speech

At 17a–17d Socrates' defense continues across several Stephanus subdivisions without a change of speaker.

### Result

The policy must split at canonical locator subdivisions even when the discourse voice continues.

A long speech is therefore represented as several adjacent logical segments sharing the same discourse/speaker annotation.

### Consequence

Speaker turn alone cannot define segment boundaries.

## Case 2 — Republic 327a ff.: narrated dialogue with embedded quotations

The opening is narrated retrospectively by Socrates. Inside that narration occur reported/direct utterances by other people.

### Result

A single field named `speaker` is not sufficient to describe every voice relation.

The canonical segmentation should not depend on detecting every embedded quotation, because quotation punctuation and rendering can be editorial.

### Consequence

We need to distinguish:

- outer narrator / discourse frame;
- surface dialogue speaker where structurally encoded;
- embedded or reported voice;
- attributed source of an embedded utterance.

Embedded quotation may require witness-span annotation rather than a new canonical segment.

## Case 3 — Symposium 172a ff.: multi-level narrative frame

Apollodorus tells companions a story that he learned through Aristodemus, who is the reported witness to the banquet.

### Result

A flat speaker model loses important provenance of narration.

### Consequence

The annotation model needs a `frame_depth` or equivalent relation capable of representing nested narrative provenance independently of canonical segment identity.

## Case 4 — Menexenus: long speech with attributed source

The dialogue begins with ordinary Socrates/Menexenus turns. Socrates then presents a funeral oration attributed within the dialogue to Aspasia.

### Result

The person physically/textually uttering a passage and the person to whom the discourse is attributed can differ.

### Consequence

The data model must distinguish at least:

- utterer/speaker;
- attributed source or composer;
- discourse mode.

The attributed source must not be encoded into `segment_id`.

## Case 5 — Letter VII: epistolary continuous discourse

Letter VII opens with an epistolary address and then continues as extended first-person discourse across Stephanus subdivisions.

### Result

The corpus model cannot assume dialogue turns.

### Consequence

`EPISTOLARY` must be a valid discourse mode. Locator boundaries remain usable even when no dialogue speaker structure exists.

## Case 6 — Definitiones: lexical/list structure

Definitiones is a sequence of definition entries. Multiple entries can occur within the same Stephanus subdivision.

### Result

The previous rule “Stephanus subdivision × speaker/narrative block” is insufficient.

### Consequence

Profile-defined **structural entry boundaries** must be allowed inside a locator cell. For Definitiones, a definition entry is a natural structural unit even though it is neither a speaker turn nor ordinary narrative.

## Revised segmentation principle

A canonical logical segment is:

> the maximal structurally coherent span that does not cross a canonical locator boundary or a profile-defined primary structural boundary.

For the Plato profile, primary structural boundaries may include:

1. Stephanus subdivision boundary;
2. explicit top-level dialogue turn where reliably encoded;
3. lexical/definition entry boundary;
4. other work-specific structural boundaries approved by the profile.

The following do **not** automatically create canonical segment boundaries:

- editorial sentence punctuation;
- tokenizer boundaries;
- semantic-topic shifts;
- every embedded quotation;
- every inferred change of reported voice.

Those phenomena belong in annotations unless the profile explicitly promotes them to structural boundaries.

## Required annotation layer

The pilot demonstrates the need for a discourse annotation model separate from segment identity.

It must be able to represent:

- discourse mode;
- speaker/utterer;
- narrator;
- attributed source;
- frame depth;
- embedded/reported speech;
- witness-specific spans when necessary.

## Phase 0 decision

SPEC-0002 should remain active but its original formulation is revised.

The pilot supports proceeding with:

- locator-bounded canonical segmentation;
- profile-defined structural boundaries;
- separate discourse/voice annotations;
- no sentence- or token-based canonical identity.

Before production ingestion, the discourse annotation schema and a synthetic nested-voice fixture must pass CI.
