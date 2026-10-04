# ADR-0001 — Project workspace and infrastructure boundary

**Status:** Accepted

## Context

PROJECT PLATO needs a durable cloud workspace immediately, while the final runtime architecture is not yet deployed. Documentation, research materials, source files, schemas, tests and release artifacts must not depend on a single local computer.

## Decision

Google Drive is the canonical project workspace for the design and research phase. It stores governance documents, research materials, source files and working artifacts.

Google Drive is **not** the final PLATO runtime datastore. The project will use GitHub as the canonical version-controlled repository and will later add a database layer suitable for structured corpus, memory and provenance data.

CUSTODIAN and PLATO remain logically separate environments even when some physical infrastructure is shared.

## Consequences

- Work can begin without dependence on a local workstation.
- Runtime storage remains replaceable.
- Migration must preserve stable identifiers, provenance and release history.
