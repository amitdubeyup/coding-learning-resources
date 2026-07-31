# Evaluation, Safety & LLMOps

"How do you know it works?" and "how do you keep it safe?" are where senior AI
candidates separate from juniors. Non-deterministic systems need real evaluation
and real guardrails — vibes don't ship.

## Why evaluating LLMs is hard

There's rarely one correct output, outputs are non-deterministic, and quality is
often subjective. So you build **evaluation as an engineering discipline**, not a
one-off manual check.

## The evaluation toolkit

1. **Golden / eval set.** A curated, versioned set of representative inputs with
   expected outputs or rubrics. This is your regression suite — grow it every time
   you find a failure in prod.
2. **Deterministic checks first.** Where possible, assert exact/structural things:
   valid JSON, schema conformance, required fields, no banned content, latency and
   cost budgets. Cheap, fast, unambiguous.
3. **LLM-as-judge.** Use a strong model to score outputs against a rubric
   (faithfulness, relevance, helpfulness). Powerful but biased — mitigate with
   clear rubrics, reference answers, and periodic human calibration.
4. **Human review loop.** Sample production traffic for expert rating; feed
   disagreements back into the golden set and the judge rubric.
5. **RAG-specific:** faithfulness, answer relevance, context precision/recall
   (e.g. via RAGAS). Evaluate retrieval and generation **separately** — see
   [`rag.md`](rag.md).
6. **Agent-specific:** task-completion rate and trajectory correctness — see
   [`agents.md`](agents.md).

## Evals in CI

Treat prompts and chains like code: **version them**, and run the eval set on
every change. Gate deploys on the suite (e.g. "faithfulness ≥ threshold, zero
schema failures, p95 latency < budget"). This catches prompt regressions before
users do — and it's the answer to "how do you prevent a prompt tweak from silently
breaking things?"

## Online evaluation

Offline isn't enough. In production, track: user feedback (👍/👎, edits,
regenerations), task success, deflection/escalation rates, cost/latency per
request, and drift in inputs. A/B test prompt/model changes against these.

## Safety & security

- **Prompt injection** — untrusted input (user text, retrieved docs, tool output)
  contains instructions that hijack the model. The top LLM security risk. Defenses:
  separate instructions from data, never let retrieved/tool content carry authority,
  constrain outputs, and least-privilege every tool the model can call.
- **Jailbreaks** — attempts to bypass safety instructions. Layer input/output
  filters; don't rely on the system prompt alone.
- **PII / data leakage** — redact sensitive data before the prompt; enforce
  access control on the retrieval layer (users only retrieve what they may see);
  log carefully. Especially critical in regulated domains.
- **Guardrails** — validate on the way in (block malicious/off-topic input) and on
  the way out (schema checks, PII scrub, toxicity/topic filters, groundedness
  check). Have a safe fallback when a guardrail trips.
- **Hallucination control** — grounding + citations + abstention + output
  validation (covered in `rag.md`). Never present ungrounded output as fact in
  high-stakes flows.

## LLMOps essentials

- **Observability / tracing:** capture inputs, outputs, retrieved context, tool
  calls, tokens, latency, and cost for *every* call. This is the foundation for
  debugging, eval, and cost control.
- **Cost & latency control:** semantic caching, model routing by difficulty,
  prompt/output length discipline, streaming, batching. Set budgets and alerts.
- **Prompt & model versioning:** pin model versions (silent provider updates
  change behavior), version prompts, and keep a rollback path.
- **Reliability:** timeouts, retries with backoff, provider fallback, graceful
  degradation when the model/API is down.

## What interviewers are really testing

That you can make a stochastic system **trustworthy and operable**: you measure
quality objectively, catch regressions automatically, defend against injection and
data leakage, and control cost and latency — the same rigor you'd bring to any
production distributed system.
