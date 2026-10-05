# SPEC-0006 — LanguageEngine runtime and model-gateway policy

**Status:** Active specification

## Objective

Define the boundary between the Thinker Framework and external language-model inference services.

The language model is a replaceable reasoning/generation engine. It is not the corpus, long-term memory, provenance store or epistemic authority.

## Logical flow

```text
user message
    |
retrieval + memory selection
    |
runtime epistemic projection
    |
admissible model payload
    |
LanguageEngine
    |
model gateway / provider
    |
model response
    |
post-processing + provenance + memory policy
```

## Required interface

A future executable `LanguageEngine` adapter should expose conceptually:

```text
generate(request, engine_config) -> response + execution_metadata
```

The generic interface must allow at least:

- system/instruction content;
- conversation messages;
- inference parameters;
- structured/JSON response constraints where supported;
- token/cost accounting;
- model/provider execution metadata.

## Gateway policy

Supported architectural modes:

- `OPENROUTER` — preferred first production gateway;
- `DIRECT_PROVIDER` — optional direct vendor adapter;
- `MOCK` — deterministic/non-network tests.

Additional gateways may be added without changing Thinker Profile semantics.

## Frozen-baseline rule

A frozen baseline must not use automatic model selection.

For an experimental baseline:

- the requested model must be explicit;
- provider routing must be deterministic enough to audit;
- `allow_fallbacks` should be false unless fallback is itself part of the experiment;
- relevant parameters must be versioned;
- the resolved provider/model must be logged.

A normal non-baseline application deployment may use cheaper or more resilient routing, but it must not be confused with a reproducible experiment run.

## OpenRouter mapping

The adapter may map project-level configuration to OpenRouter provider controls such as:

- provider allow/order lists;
- fallback permission;
- parameter-support requirements;
- data-collection restrictions;
- ZDR requirement;
- price constraints.

Project configuration remains vendor-neutral at the core boundary even when an adapter supports OpenRouter-specific features.

## Data handling

Model-visible content must already have passed runtime epistemic projection before it reaches the LanguageEngine.

The engine adapter must never fetch hidden CUSTODIAN fields to improve an answer.

Provider/model execution metadata remains hidden from the thinker unless an experiment deliberately communicates it as ACQUIRED information.

## Secrets

API keys and billing credentials:

- are server-side secrets;
- are never committed to Git;
- are never included in thinker-visible prompts;
- are never stored in corpus/provenance text objects as content.

Expected first production secret:

```text
OPENROUTER_API_KEY
```

## Cost controls

At minimum the production runtime should support:

- per-request maximum cost or token budget;
- instance/session budget accounting;
- explicit refusal/failure when constraints cannot be met;
- no silent upgrade to a more expensive engine.

## Audit record

Each inference event should ultimately record:

```json
{
  "engine_config_id": "...",
  "gateway": "OPENROUTER",
  "requested_model": "...",
  "resolved_model": "...",
  "resolved_provider": "...",
  "fallback_occurred": false,
  "input_tokens": 0,
  "output_tokens": 0,
  "cost_usd": 0.0,
  "latency_ms": 0
}
```

This example is an audit envelope, not a thinker-visible payload.

## Current project decision

OpenRouter is the preferred first production gateway.

The actual PLATO baseline model is intentionally **not yet frozen**. Model selection will occur after corpus/runtime preparation and comparative evaluation of cost, leakage behavior and reasoning quality.
