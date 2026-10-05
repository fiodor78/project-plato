# AUTHENTICITY COVERAGE 0001 — Phase 1 snapshot

**Catalog:** `catalog-v0.1.4.json`  
**Status:** working coverage snapshot after Letter VIII assessment

## Coverage

The current historical catalog contains **95 entries**.

Of those, **88** are extant, individually addressable `WORK` or `MEMBER` records that can meaningfully receive a work-level authorship assessment.

Current A/B/C/D coverage:

| Grade | Count |
|---|---:|
| A — strongly accepted | 26 |
| B — disputed | 4 |
| C — probably inauthentic | 7 |
| D — pseudo-Platonic | 10 |
| **Assessed** | **47 / 88** |

Coverage: **53.4%**.

## Remaining 41 cases

All unresolved extant individual texts now belong to three explicit research queues:

- **9 canonical Epistles** — II, III, IV, V, VI, IX, X, XI, XIII;
- **23 epigrams** — individual Greek Anthology attributions;
- **9 extra-canonical epistles** — Hercher 14, 15, 24, 25, 26, 30, 31, 70, 85.

There are currently **no unresolved ordinary dialogues or other Appendix-Platonica prose works outside those queues**.

## CI contract

`scripts/check_authenticity_coverage.py` recalculates this state from the catalog and assertion files.

It intentionally does not require the unresolved count to remain 41: the number must decrease as research progresses.

It does require that any unresolved item belong to one of the explicitly tracked queues. If a new extant text is added to the historical catalog without entering the authenticity workflow, CI will fail instead of silently losing track of it.
