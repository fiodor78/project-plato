# ADR-0015 — Provider-neutral language engine with OpenRouter as the default production gateway

**Status:** Accepted

## Context

PROJECT PLATO requires a powerful language model for generation and reasoning, but the experimental subject must not be defined by a single commercial model vendor.

The corpus, memory, provenance, retrieval, epistemic projection and experiment lineage belong to the Thinker Framework. A language model is an execution engine used by the runtime after admissible context has been assembled.

Binding PLATO directly to one provider would:

- make costs harder to control;
- make model comparisons unnecessarily difficult;
- couple experiment continuity to one vendor;
- weaken reproducibility when provider-side model aliases change;
- encourage accidental treatment of the base model as the thinker's memory or knowledge base.

OpenRouter provides a common gateway to models from multiple vendors and exposes provider-routing controls. It can therefore reduce operational coupling and make price/quality experiments easier.

## Decision

### 1. LanguageEngine is provider-neutral

The generic runtime will expose a `LanguageEngine` abstraction.

The Thinker Core must not assume OpenAI, Anthropic, Google, OpenRouter or any other specific model vendor.

### 2. OpenRouter is the default production gateway

For the first operational PLATO runtime, the preferred gateway is **OpenRouter**.

This is a deployment choice, not part of Plato's identity and not a dependency of the corpus model.

Direct-provider adapters may coexist for benchmarking, failover experiments or future migration.

### 3. Baseline experiments must pin model and routing

A reproducible experimental baseline must record at least:

- gateway;
- exact model identifier requested;
- provider-routing policy;
- whether fallbacks are allowed;
- relevant inference parameters;
- privacy/data-routing constraints;
- timestamped runtime configuration version.

Automatic model selection is **not permitted for a frozen baseline**.

Provider fallbacks are disabled by default for reproducibility unless the experiment explicitly studies fallback behavior.

### 4. Actual execution metadata is audited

For every model call the audit layer should record, where the gateway exposes it:

- requested model;
- resolved model;
- resolved provider/endpoint;
- input/output token counts;
- latency;
- cost;
- retry/fallback events;
- runtime configuration identifier.

These fields are CUSTODIAN/runtime metadata and are not automatically thinker-visible.

### 5. Privacy policy is explicit

Routing policy should prefer endpoints that do not train on experiment inputs.

Where practical, production configurations should require Zero Data Retention (ZDR) for conversations containing user data.

ZDR is a provider-side retention constraint, not a substitute for application-side logging policy.

### 6. Cost controls are mandatory

Production deployments must support budget limits outside the thinker prompt itself.

The runtime should fail safely rather than silently switching to a more expensive model when a configured cost/routing constraint cannot be satisfied.

### 7. Engine changes create a new experimental condition

Changing the model, routing policy or materially relevant inference configuration does not rewrite an existing frozen baseline.

Comparisons should be represented as distinct experimental conditions or descendant lineages, for example:

```text
PLATO-1.0 / engine-A
PLATO-1.0 / engine-B
```

The corpus and initial memory state may be identical while the language engine differs.

## Consequences

- PLATO remains portable across model vendors.
- OpenRouter can be used for cost-effective model selection without contaminating the conceptual architecture.
- Expensive models can be reserved for benchmark or difficult-reasoning runs.
- Runtime reproducibility requires stricter provider pinning than an ordinary consumer chatbot.
- Model/provider metadata becomes part of the audit record, not the thinker's epistemic world.
