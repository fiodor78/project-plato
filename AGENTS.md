# AGENTS.md — operating instructions for automated agents

This repository is an experimental research system. Automated agents are welcome to inspect and contribute, but they must preserve the project's epistemic and provenance boundaries.

## Canonical project

Repository: `fiodor78/project-plato`

GitHub is the canonical version-controlled source of truth for code, schemas, ADRs, specifications, tests and redistributable metadata.

Start by reading:

1. `README.md`
2. `ROADMAP.md`
3. `docs/specs/SPEC-0001-phase-0-architecture.md`
4. `docs/specs/SPEC-0003-thinker-core-profile-instance.md`
5. `docs/specs/SPEC-0004-runtime-epistemic-projection.md`
6. relevant ADRs in `docs/adr/`

## Critical conceptual distinction

**CUSTODIAN is not the active thinker.**

CUSTODIAN is the external research/engineering/audit environment and may use modern knowledge.

A Thinker instance (currently PLATO) may use only epistemically admissible information defined by its frozen profile/corpus plus acquired, episodic and inferred memory.

Do not “help” PLATO by injecting modern knowledge into thinker-visible data.

## Architecture

The reusable architecture is:

```text
Thinker Core
  -> Thinker Profile
       -> frozen profile release
            -> Thinker Instance / lineage
```

PLATO is the first profile, not the generic core.

Do not hard-code Plato-specific assumptions into generic framework components.

Examples of profile-specific features:
- Stephanus pagination;
- Plato-specific corpus scope;
- Plato attribution/authenticity labels;
- dialogue speaker conventions.

A future thinker may use Bekker numbers, fragment numbering, aphorisms or another locator scheme.

## Epistemic classes

Keep these distinct:

- ORIGINAL
- ACQUIRED
- EPISODIC
- INFERENCE
- PROVENANCE

ORIGINAL is a read-only view of a frozen corpus release, not mutable memory.

An interlocutor's claim is testimony, not automatically truth.

## Runtime boundary

The raw storage object is not the model payload.

Thinker-visible payloads must be produced only through the deny-by-default projection layer.

Never expose hidden fields merely because the underlying entity is visible.

Typical CUSTODIAN-only / runtime-only material includes:

- modern edition IDs;
- modern editor/translator metadata;
- publication years;
- source URLs;
- rights/licensing notes;
- authenticity classifications;
- CUSTODIAN notes;
- hidden test expectations;
- checksums;
- UUIDv7 technical IDs.

If a new field is introduced, treat it as hidden until explicitly allow-listed.

## Language-engine discipline

The base LLM is a replaceable execution engine.

- Do not hard-code a model vendor into Thinker Core semantics.
- Preferred first production gateway: OpenRouter.
- Frozen experimental baselines must pin the requested model and routing policy.
- Automatic model routing or silent provider fallback must not be used in a reproducible baseline unless explicitly part of the experiment.
- API keys are server-side secrets and must never be committed or exposed to the thinker.
- Model/provider/cost metadata is CUSTODIAN/runtime metadata unless deliberately communicated as ACQUIRED knowledge.

See `ADR-0015` and `SPEC-0006`.

## Synthetic fixtures are not corpus

Everything under `fixtures/phase0/` is synthetic architecture-test data unless explicitly documented otherwise.

Do not quote, index or classify those fixtures as Plato.

Real corpus ingestion must wait for the Phase 0 architecture gate.

## Identifiers

Do not derive logical identity from mutable scholarship.

- readable profile registries may have semantic IDs, e.g. `TH.PLATO.WORK.REP`;
- runtime-created opaque objects use UUIDv7;
- scholarly locators such as Stephanus/Bekker are separate data, not object identity.

Do not rewrite released IDs to make them prettier.

## ADR discipline

Accepted architectural decisions live in `docs/adr/`.

Do not silently rewrite the rationale of an accepted ADR to reflect a new design.

If a decision changes:
1. create a new ADR;
2. mark the old ADR superseded where appropriate;
3. provide migration consequences.

## Source-ingestion discipline

Source bytes and normalized derivatives are different assets.

For acquired sources preserve, where applicable:
- source URI;
- acquisition time;
- media type;
- checksum;
- rights/redistribution status;
- transformation lineage.

Never commit restricted copyrighted source material merely because it is technically accessible.

## Tests required for architecture changes

At minimum run:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_schemas.py
python scripts/check_phase0_gate.py
python scripts/test_runtime_projection.py
```

Do not mark Phase 0 complete while the main validation workflow is red.

## Contribution boundaries

Good agent contributions include:
- schema improvements;
- deterministic validation;
- provenance checks;
- leakage tests;
- documentation;
- profile-neutral abstractions;
- reproducibility tooling;
- corpus metadata work after the ingestion gate.

Ask for human/project-owner review before:
- changing the experiment's epistemic constitution;
- redefining corpus scope;
- changing authenticity methodology;
- choosing a project-wide license;
- exposing CUSTODIAN-only data to a thinker;
- introducing a new philosopher profile with disputed source policy.

## Repository readability

Maintain these machine/human entry points:

- `README.md` — full public overview;
- `AGENTS.md` — agent operating rules;
- `llms.txt` — compact machine entry point;
- `site/` — static documentation page;
- `ROADMAP.md` — current state.

When adding a major document, link it from at least one appropriate entry point.

## If GitHub HTML cannot be read

Do not infer that the repository is inaccessible.

Use the GitHub API, a connected GitHub tool, or raw-file URLs.

Canonical raw base:

`https://raw.githubusercontent.com/fiodor78/project-plato/main/`

## Non-goal

Do not optimize for theatrical role-play at the expense of provenance.

The governing principle is:

> epistemic honesty over convincing simulation.
