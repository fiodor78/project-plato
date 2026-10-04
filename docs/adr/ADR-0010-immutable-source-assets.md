# ADR-0010 — Source assets are immutable and checksum-addressed

**Status:** Accepted

## Context

Corpus ingestion must remain reproducible even if a hosting website changes, a file is replaced under the same URL, or later normalization modifies textual representation.

## Decision

Every acquired source file is registered as an immutable **source asset** before extraction or normalization.

A source asset records at minimum:

- source URI;
- acquisition timestamp;
- original filename and media type when available;
- byte size;
- SHA-256 checksum of the acquired bytes;
- rights/redistribution status;
- CUSTODIAN storage reference.

Derived files never replace the source asset. Each transformation creates a new derived asset or transformation record linked to its input checksum.

Checksums are calculated on raw bytes before text cleanup.

A changed file at the same URI is a new asset.

Public GitHub commits may contain the metadata record even when copyright or licensing prevents committing the source bytes themselves.

## Consequences

- Corpus builds can identify exact source bytes.
- Silent upstream replacement is detectable.
- Normalization can be reproduced and audited.
- Restricted source material can remain outside the public repository while retaining verifiable metadata.
