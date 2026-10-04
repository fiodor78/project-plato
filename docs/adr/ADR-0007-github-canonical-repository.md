# ADR-0007 — GitHub is the canonical public repository

**Status:** Accepted

## Context

PROJECT PLATO requires transparent versioning, reproducibility, public inspection of methodology and stable review history.

## Decision

The canonical project repository is the public GitHub repository:

`fiodor78/project-plato`

GitHub is the source of truth for:

- README and orientation
- ADRs and specifications
- schemas
- source code and runtime components
- tests
- experiment protocols
- release manifests
- machine-readable corpus metadata where redistribution is permitted

Google Drive remains complementary storage for working research, source scans/PDFs, large files, restricted copyrighted material and archival working artifacts.

No secrets, credentials, personal information or non-redistributable copyrighted source text may be committed to the public repository.

Repository history is authoritative when a GitHub artifact and a Drive working copy diverge, except for source material deliberately excluded for legal or privacy reasons.

## Consequences

- The experiment has a public, versioned methodological record.
- Public/private storage boundaries must be explicit.
- Corpus licensing must be decided before source redistribution.
