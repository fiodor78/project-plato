# ADR-0014 — Modern authenticity is versioned evidence, not catalog identity

**Status:** Accepted

## Context

The historical attribution catalog answers: “what has been transmitted, cataloged or ascribed under Plato's name?”

It does not answer: “did Plato write this?”

Modern authenticity scholarship is heterogeneous. Some texts are almost universally accepted, some remain genuinely disputed, some are broadly regarded as non-Platonic despite ancient canonical inclusion, and some were already treated as spurious in antiquity.

A single irreversible flag on a work record would collapse scholarship into infrastructure.

## Decision

Modern authenticity is represented as a **versioned CUSTODIAN-only assertion** separate from historical catalog identity and separate from runtime-visible text.

The Plato profile uses a four-level working classification:

- **A — strongly accepted as Platonic**: substantial current scholarly consensus supports Platonic authorship; no major live authenticity dispute material to the project has been identified.
- **B — disputed**: significant modern scholarly disagreement remains; credible arguments exist on more than one side.
- **C — probably inauthentic**: modern scholarship substantially favors non-Platonic authorship, while the work remains historically important to the Platonic corpus and may still have defenders or unresolved dating/provenance.
- **D — pseudo-Platonic**: the work belongs to the historical attribution tradition but authorship by Plato is overwhelmingly rejected or was explicitly rejected in the ancient corpus tradition.

These letters are project shorthand, not universal scholarly terminology.

## Evidence rule

No A/B/C/D assertion is accepted solely because one secondary summary assigns a label.

Each accepted assertion should normally include:

1. historical/external evidence where relevant;
2. at least one current or major scholarly reference directly discussing the work or authenticity problem;
3. a second independent scholarly reference for B/C/D judgments where practical;
4. an explicit rationale;
5. an assessment version/date.

Where scholarship is genuinely divided, the project must prefer **B** over false precision.

## Collection rule

Collections do not automatically transfer authenticity to members.

In particular:

- the Epistles collection may have a collection-level summary;
- each of the thirteen letters requires its own authorship assertion before catalog freeze;
- an individual letter can have a different A/B/C/D assessment from the collection-level consensus.

The same principle applies to anthological epigrams if they are later split into individual members.

## Runtime rule

Authenticity assertions are `CUSTODIAN_ONLY`.

They may influence retrieval policy or release construction, but the active thinker does not automatically learn modern scholarly verdicts.

If an experiment deliberately teaches such a verdict, it must enter as ACQUIRED knowledge, not by exposing hidden catalog metadata.

## Consequences

- New scholarship can revise authenticity without rewriting corpus identity.
- Disagreement remains visible instead of being averaged away.
- Historical transmission and modern authorship remain separate questions.
- PLATO cannot infer modern authenticity judgments from hidden ranking metadata unless an experiment explicitly permits it.
