# SPEC-0004 — Runtime epistemic projection

**Status:** Active Phase 0 specification

## Objective

Prevent CUSTODIAN-only or merely technical metadata from entering the language model context even when the underlying storage object is otherwise eligible for thinker use.

## Two envelopes

A retrieval result is separated into:

1. **audit envelope** — internal runtime/CUSTODIAN data used for provenance, debugging and exact source tracking;
2. **model payload** — the only representation that may be serialized into the active Thinker's prompt/tool context.

The model payload must never contain the audit envelope.

## Deny-by-default rules

- an entity without explicit `THINKER_VISIBLE` status is ineligible;
- `CUSTODIAN_ONLY` entities are rejected;
- source-edition records are never model payloads;
- fields not explicitly allow-listed for the entity type are dropped;
- unknown entity types are dropped;
- raw UUIDv7 object IDs are runtime metadata and are not included in model payloads;
- errors must not echo raw hidden records.

## Plato Phase 0 allow-list

### work
- visible title selected by profile
- canonical scholarly range only when needed

### segment
- canonical locator
- end locator when present

### textual_witness
- language
- text

### translation
- language
- text

### speaker_assertion
- speaker label
- assertion status

## Explicitly hidden examples

- edition ID and edition name
- editor / translator identity unless deliberately taught
- publication year
- source URI
- license / redistribution fields
- CUSTODIAN notes
- authenticity classification
- source checksum
- assertion basis references
- generated runtime IDs

These remain fully available for audit/provenance.

## Integrity requirement

CI must create a projected model payload from raw fixtures and assert that:

1. all CUSTODIAN-only entities disappear;
2. hidden field names disappear;
3. sentinel values placed only in hidden fields cannot occur in the serialized model payload;
4. the visible Greek/translation text, locator and speaker survive projection.
