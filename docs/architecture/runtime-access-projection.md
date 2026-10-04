# Runtime access projection

**Status:** Phase 0 draft implementing ADR-0003 and ADR-0008

## Rule

PLATO never queries the raw CUSTODIAN storage model.

The runtime receives an approved projection containing only fields needed for admissible epistemic operation.

## Entity access matrix

| Entity | CUSTODIAN | PLATO |
|---|---:|---:|
| Work metadata | read/write | approved subset |
| Logical segments | read/write | read |
| Approved Greek witness | read/write | read |
| Approved translation | read/write | read |
| Speaker assertion | read/write | approved assertion |
| Authenticity assertion | read/write | **no access** |
| Source licensing notes | read/write | no access |
| Editorial comparison notes | read/write | no access |
| Acquired memory | audit/read | own instance read/write |
| Episodic memory | audit/read | own instance read/write |
| Inference memory | audit/read | own instance read/write |
| Hidden test expectations | read/write | **no access** |
| Internet/search tools | yes | **no access** |

## Projection rules

1. Missing visibility means hidden.
2. `CUSTODIAN_ONLY` is never passed to the PLATO model.
3. `PUBLIC_METADATA` requires an explicit runtime rule before exposure.
4. Semantic-index payloads must be generated only from PLATO-approved fields.
5. Error messages must not reveal hidden row contents, hidden labels or modern scholarly annotations.
6. Retrieval logs remain available to CUSTODIAN for audit.
7. An intentional experiment that teaches PLATO previously hidden information must create an ACQUIRED memory/provenance event; it must not relax the general access rule.

## Test obligation

The leakage suite must attempt:
- direct lookup of hidden entities;
- semantic search for hidden terminology;
- prompt injection requesting CUSTODIAN metadata;
- indirect inference from hidden labels or ranking;
- accidental leakage in citations, debug output and exceptions.
