# GenAI system design — worked examples

The AI system-design round is now a standard part of GenAI/AI-engineering loops, and
it's where candidates most often stumble ("design a RAG system for our support
product" ends more interviews than any coding question). This file is the GenAI analog
of the [`../system-design/high-level/`](../system-design/high-level/) worked designs:
each example leads with the **centerpiece decision**, reasons through the trade-offs,
and ends with what to voice. It builds on the framework in [`README.md`](README.md) and
the depth in [`rag.md`](rag.md), [`agents.md`](agents.md), and
[`evaluation-and-safety.md`](evaluation-and-safety.md).

## The framework (drive it)

1. **Clarify** — users, volume/QPS, latency budget, accuracy bar, data sources,
   freshness, privacy/compliance, and *what "good" means* (the eval metric).
2. **Data & retrieval** — sources, chunking, embeddings, index, refresh, access control.
3. **Model** — hosted vs self-hosted; size/cost/latency; a fallback/cheaper tier.
4. **Orchestration** — prompt flow / agent loop, tool use, guardrails.
5. **Evaluation** — an offline golden set + online metrics + human review.
6. **Serving** — streaming, caching, routing, autoscaling, cost controls.
7. **Safety & ops** — prompt-injection defense, PII handling, observability, on-call.

Two things separate a senior answer: you **lead with evaluation** (an AI feature you
can't measure is one you can't ship), and you treat **cost and latency** as first-class
constraints, not afterthoughts.

## 1. RAG customer-support assistant

The canonical GenAI design. Answer user questions grounded in a company's help
docs/tickets, with citations.

- **Ingestion & index:** chunk documents (~200–500 tokens with overlap; respect
  structure — don't split mid-table), embed them, and store vectors (pgvector, or a
  dedicated store at scale). Re-index on doc changes (freshness).
- **Retrieval (the core quality lever):** **hybrid search** (semantic + keyword/BM25) to
  catch both meaning and exact terms, then a **cross-encoder reranker** on the top-k for
  precision. Retrieval quality — not the LLM — is where most RAG systems win or lose.
- **Generation:** stuff the reranked context into a grounded prompt; require
  **citations**; instruct the model to say **"I don't know"** when the answer isn't in
  context (the #1 hallucination control).
- **Evaluation:** a versioned **golden set** of question→expected-answer pairs; measure
  retrieval (recall@k, MRR) and generation (faithfulness/groundedness, answer relevance)
  with **RAGAS**-style metrics + **LLM-as-judge**; run it in CI so changes don't regress.
- **Cost/latency:** cache by **semantic similarity** (near-duplicate questions are
  common in support), stream tokens, and **route by difficulty** (small model for easy
  Qs, frontier only when needed).
- **Safety:** filter PII, defend against prompt injection in retrieved content, and
  provide a **human handoff** when confidence is low.
- **Trade-offs to voice:** retrieval precision vs recall (rerank cost); context size vs
  cost/latency ("lost in the middle" with huge contexts); fine-tune vs RAG (behavior vs
  knowledge — RAG here, since support content changes constantly).

## 2. Tool-using agent (task/coding assistant)

Design an agent that accomplishes multi-step tasks by calling tools (search, code
execution, internal APIs).

- **The loop:** plan → act (call a tool) → observe (feed the result back) → repeat until
  done. Frame it as a **state machine**; **LangGraph**-style stateful orchestration is
  the current default over ad-hoc chains.
- **Tools:** the model emits a structured **function call**; your code executes it and
  returns the result. Tools must have clear schemas and unambiguous outputs.
- **Memory:** short-term (the working scratchpad/context) vs long-term (a vector store
  of past interactions/facts). Manage the context budget aggressively.
- **The hard problems (name these):** agents that **loop forever** or wander → cap
  iterations, add a termination check, make tool results unambiguous. **Compounding
  errors** across steps → smaller verifiable steps, self-check/critique, and validation
  between steps.
- **Safety:** **sandbox** anything that executes code or touches the outside world;
  least-privilege tool access; a human approval gate for destructive/irreversible
  actions.
- **Evaluation:** score the **trajectory, not just the final output** — tool-call
  accuracy and whether each step was justified (the **GAIA** benchmark exists precisely
  because agents are far below humans on multi-step tasks). Shadow-run and regression-test.
- **Trade-offs to voice:** autonomy vs control (more steps = more capability *and* more
  failure surface); cost/latency of multi-step loops; single powerful agent vs a
  multi-agent decomposition.

## 3. Enterprise document Q&A with access control (regulated/FinTech)

A knowledge assistant over internal/regulated data — the version that matters in
FinTech/healthcare where getting security wrong is worse than getting the answer wrong.

- **The centerpiece: access-controlled retrieval.** A user must **never retrieve a
  chunk from a document they aren't authorized to see.** Enforce permissions **at the
  retrieval layer** — filter the vector search by the user's ACLs (metadata filters /
  per-tenant partitions), not after generation. This is the detail interviewers probe
  and most candidates miss.
- **Multi-tenancy:** isolate tenants' data (separate namespaces/indexes or strict
  metadata filtering); see [`../system-design/multi-tenancy.md`](../system-design/multi-tenancy.md).
- **Compliance:** PII redaction before prompts, **audit logging** of prompts +
  retrieved sources + outputs (traceability), data residency, and often **self-hosted /
  VPC model hosting** so regulated data never leaves the boundary.
- **Grounding & trust:** citations to source documents; conservative "I don't know"
  behavior; human review for high-stakes answers.
- **Trade-offs to voice:** hosted (cheap, capable) vs self-hosted (control, compliance,
  cost); strict access filtering adds retrieval complexity but is non-negotiable; audit
  overhead vs latency.

## Cross-cutting decisions (bring these to any GenAI design)

- **Hosted vs self-hosted models** — capability/speed-to-ship vs control/cost/data
  residency. Have a fallback tier.
- **Cost & latency levers** — prompt length, output length, model size, reasoning
  effort, call count, semantic caching, and difficulty-based routing.
- **Evaluation is the deliverable** — golden set + LLM-as-judge + CI regression + online
  metrics + human review. Say this early.
- **Safety** — prompt-injection defense (especially with retrieved/tool content), PII
  handling, output validation against a schema, and guardrails.
- **Observability** — trace every call (inputs, outputs, tokens, latency, cost, tool
  calls); you can't improve what you don't trace.

## Trade-offs to voice (summary)
- **RAG vs fine-tune vs long context** — knowledge vs behavior vs paste-it-in (usually
  RAG for changing knowledge).
- **Retrieval precision vs recall** — reranking cost vs missed context.
- **Agent autonomy vs control** — capability vs failure surface and cost.
- **Hosted vs self-hosted** — speed/capability vs control/compliance.
- **Accuracy vs cost/latency** — the frontier model isn't always the right call; route.
