# ADR-0008 — PLATO runtime visibility is explicit and deny-by-default

**Status:** Accepted

## Context

CUSTODIAN and PLATO may share physical infrastructure, but PLATO must not gain access to modern scholarship, authenticity classifications, test answers or other CUSTODIAN-only metadata through an accidental query or retrieval join.

## Decision

Runtime visibility is an explicit property of data exposed through the PLATO retrieval boundary.

The PLATO runtime follows a **deny-by-default** rule:

- data explicitly marked `PLATO_VISIBLE` may be projected into PLATO's context;
- `CUSTODIAN_ONLY` data must never cross the runtime boundary;
- `PUBLIC_METADATA` is not automatically PLATO-visible merely because it is public;
- unknown or missing visibility is treated as **not visible**.

The runtime does not query the storage model directly. It queries an approved projection/API that strips forbidden fields and entities.

Authenticity assertions are always CUSTODIAN-only unless a future experiment deliberately introduces such knowledge through an explicit acquisition event.

Tests must verify both direct and indirect leakage, including joins, semantic indexes, metadata expansion and error messages.

## Consequences

- Public GitHub visibility does not imply epistemic visibility to PLATO.
- Access policy becomes testable.
- A storage mistake is less likely to become a cognitive leak.
- Retrieval adapters must implement a projection layer rather than returning raw database rows.
