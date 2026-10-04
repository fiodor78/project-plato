# ADR-0003 — Logical separation of CUSTODIAN and PLATO

**Status:** Accepted

## Context

CUSTODIAN requires access to external sources, scholarship, source criticism and project administration. PLATO must operate inside a deliberately restricted epistemic environment.

## Decision

CUSTODIAN and PLATO are separate logical security domains.

CUSTODIAN may access external research, authenticity assessments, editorial scholarship, source metadata, tests and audit materials.

PLATO may access only the approved Corpus Platonicum, its permitted memory stores and information deliberately introduced through the experiment.

Modern authenticity classifications, CUSTODIAN notes, hidden test answers and external web access are not part of PLATO's epistemic world unless introduced by an explicit experimental procedure.

CUSTODIAN is not a routine intermediary in conversations between the user and PLATO.

## Consequences

- Shared physical storage does not imply shared epistemic access.
- The later runtime must enforce explicit data-access rules.
- Tests must include attempts to cross this boundary.
