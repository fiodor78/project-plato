# ADR-0012 — UUIDv7 for opaque runtime object identifiers

**Status:** Accepted

## Context

The framework needs opaque identifiers for logical segments, witnesses, translations, assertions, mutable memories, provenance records, retrieval events, snapshots, source assets and similar runtime-created objects.

The identifier format must be collision-resistant, usable without central coordination, sortable enough for operational storage, independent of philosopher-specific citation schemes and standardized outside this project.

Embedding Stephanus, Bekker, speaker, edition or semantic labels in machine identity would couple identity to mutable scholarly interpretation.

## Decision

Production-generated opaque object identifiers use **UUID version 7** as standardized by RFC 9562.

UUIDv7 suffixes are represented in canonical lowercase textual form.

Examples:

```text
TH.PLATO.SEG.01a108c0-4799-75a7-9445-69a6fdd19b35
TH.PLATO.PROV.01a108c0-479a-793e-9541-5556f8e12b9b
SRC.01a108c0-7d35-761a-8595-c9e9ccfabe0a
```

Semantic identifiers remain appropriate for stable profile-owned registries such as:

- `TH.PLATO`
- `TH.PLATO.WORK.REP`
- `TH.PLATO.ED.SLINGS2003`
- `TH.PLATO.SPEAKER.SOCRATES`

UUIDv7 creation time is operational metadata and is **not epistemic knowledge of the thinker**. Raw generated IDs must therefore remain in runtime/audit envelopes and must not be exposed to model-visible context unless an explicit experiment requires it.

The project does not derive UUIDs deterministically from citation coordinates or text contents. Once assigned, identity is persisted in release artifacts and migration maps.

## Rationale

RFC 9562 defines UUIDv7 as a 128-bit UUID using Unix-epoch millisecond time in the most significant 48 bits plus version/variant and random or monotonic data. It is an IETF-standard UUID format and avoids maintaining a project-specific identifier standard.

Reference: https://www.rfc-editor.org/rfc/rfc9562.html#name-uuid-version-7

## Consequences

- Machine identity is independent of Stephanus/Bekker and other profile locators.
- Operational ordering improves compared with fully random identifiers.
- Rebuilding a corpus from source does not silently recreate identities; released manifests are the identity authority.
- Technical IDs must be stripped from thinker-visible prompt payloads.
