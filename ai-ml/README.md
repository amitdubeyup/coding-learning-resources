# AI / ML Engineering — interview prep

Modern AI engineering interviews split into two tracks. Know which one you're in:

- **GenAI / LLM application engineering** — RAG, agents, prompting, evals,
  serving, cost/latency. This is where most hiring is. Start here.
- **Classic ML / MLOps** — modeling, features, training, deployment, monitoring.

This module covers both, GenAI-first — AI-engineer loops are now majority-GenAI, with
classical ML a minority of the technical rounds. Companion files:
[`foundations.md`](foundations.md) (LLM internals — start here for depth) ·
[`rag.md`](rag.md) · [`agents.md`](agents.md) ·
[`evaluation-and-safety.md`](evaluation-and-safety.md) ·
[`interview-qa.md`](interview-qa.md) (legacy Q&A, pending review).

The three question tiers senior loops draw from: **foundations** (tokenization,
attention, embeddings), **application** (RAG, agents, fine-tuning), and **production**
(cost, latency, evaluation, guardrails).

> **On model names/versions:** the frontier moves monthly. This guide teaches
> *capabilities and trade-offs*, not leaderboards. Always check current model
> cards before quoting a context window, price, or benchmark in an interview.

## Contents
- [LLM fundamentals you must be able to explain](#llm-fundamentals-you-must-be-able-to-explain)
- [Prompting that actually matters](#prompting-that-actually-matters)
- [RAG vs fine-tuning vs long context](#rag-vs-fine-tuning-vs-long-context)
- [The modern GenAI stack](#the-modern-genai-stack)
- [Serving, cost & latency](#serving-cost--latency)
- [Classic ML & MLOps essentials](#classic-ml--mlops-essentials)
- [Enterprise / regulated considerations](#enterprise--regulated-considerations)
- [The AI system-design interview](#the-ai-system-design-interview)
- [Rapid-fire Q&A](#rapid-fire-qa)

---

## LLM fundamentals you must be able to explain

> For the deep version of everything in this section — attention math, positional
> encoding, scaling laws, fine-tuning, reasoning models — see
> [`foundations.md`](foundations.md). This is the summary.

- **Transformer, in one breath:** tokens → embeddings → stacked self-attention +
  feed-forward blocks → next-token probability distribution. Attention lets every
  token weigh every other token; that's the whole trick (and why cost is O(n²) in
  sequence length).
- **Tokens, not words.** Cost, context limits, and latency are all measured in
  tokens (~4 chars/token in English). Be able to reason about token budgets.
- **Context window** = how many tokens the model can attend to at once. Bigger
  isn't free: latency and cost grow with input, and models still degrade on
  "lost in the middle" retrieval within huge contexts.
- **Temperature / top-p** control randomness. Temperature 0 ≈ deterministic
  (use for extraction/classification); higher for creative generation.
- **Decoder-only vs encoder-only vs encoder-decoder:** decoder-only (GPT-style)
  dominates generation; encoder-only (BERT-style) still wins for embeddings and
  classification; encoder-decoder (T5-style) for translation/seq2seq.
- **Reasoning models** trade *inference* compute for accuracy — trained to "think"
  before answering. Know the trade-off (latency/cost); details in `foundations.md`.
- **Why hallucinations happen:** the model optimizes for *plausible* next tokens,
  not truth. It has no grounding unless you provide it (→ RAG, tools, citations).
- **Structured outputs:** prefer native JSON/schema or function-calling modes
  over "please return JSON" — they constrain decoding and cut parse failures.

## Prompting that actually matters

The high-leverage techniques, in order:
1. **Be explicit about role, task, format, and constraints.** Ambiguity is the
   #1 cause of bad output.
2. **Few-shot examples** for format and edge cases when zero-shot is inconsistent.
3. **Chain-of-thought / "think step by step"** for reasoning tasks (or use a
   reasoning-tuned model, which does this internally).
4. **Decompose** big tasks into a pipeline of small, checkable steps.
5. **Ground it** — give the model the source material; ask it to cite and to say
   "I don't know" when the answer isn't present.

Anti-patterns interviewers listen for: stuffing everything into one mega-prompt,
no output schema, no failure handling, and treating prompt quality as luck rather
than something you evaluate and version.

## RAG vs fine-tuning vs long context

The most common architecture question. The honest answer is "it depends," so know
the axes:

| Need | Reach for |
|---|---|
| Inject fresh / proprietary **knowledge** | **RAG** |
| Change **behavior / format / tone / a skill** | **Fine-tuning** |
| Reason over a few specific documents *right now* | **Long context** (paste it in) |
| Cut latency/cost of a repeated narrow task | Fine-tune a smaller model |

Key point to land: **RAG changes what the model knows; fine-tuning changes how it
behaves.** They're complementary, not either/or. Long context is not a RAG
replacement at scale — it's expensive per query and doesn't persist knowledge.
Full RAG deep dive in [`rag.md`](rag.md); fine-tuning mechanics (LoRA/QLoRA) in
[`foundations.md`](foundations.md).

## The modern GenAI stack

- **Orchestration:** LangGraph (stateful agents), LangChain, LlamaIndex, or
  increasingly plain code + a thin SDK. Be ready to argue *against* heavy frameworks
  (hidden control flow, debugging pain) as much as for them.
- **Tool use / function calling:** the model emits a structured call; your code
  executes it and returns the result. Foundation of agents.
- **MCP (Model Context Protocol):** now the common standard for connecting models to
  tools/data sources through one interface — worth knowing by name.
- **Vector store:** pgvector (Postgres) by default; dedicated stores (Qdrant,
  Pinecone, Weaviate, Chroma) when scale/latency/hybrid-search demands it. See
  [`rag.md`](rag.md).
- **Embeddings + reranking:** a bi-encoder retrieves candidates; a cross-encoder
  reranker reorders the top-k for precision.
- **Observability:** trace every LLM call — inputs, outputs, tokens, latency,
  cost, tool calls. You cannot improve what you don't trace.

## Serving, cost & latency

- **Streaming** responses to cut perceived latency (time-to-first-token matters
  more than total time for chat UX).
- **Semantic caching:** cache by embedding similarity, not exact string match, to
  serve repeated/near-duplicate queries cheaply.
- **Route by difficulty:** small/cheap model for easy calls, frontier model only
  when needed. Big cost lever — and the same idea gates reasoning effort.
- **Batching + concurrency** for throughput; **quantization** (8-bit/4-bit) and
  **KV-cache** for self-hosted inference (vLLM/TGI).
- **Know your knobs:** prompt length, output length (`max_tokens`), model size,
  reasoning effort, and call count are the cost/latency levers.

## Classic ML & MLOps essentials

Still asked, especially outside pure-GenAI roles:
- **Bias–variance**, over/underfitting, regularization (L1/L2, dropout, early stop).
- **Train/val/test discipline**, cross-validation, and **data leakage** (the
  classic gotcha — features that encode the label or leak the future).
- **Metrics fit the problem:** precision/recall/F1 and PR-AUC for imbalanced
  classification (not accuracy); RMSE/MAE for regression.
- **Feature stores, reproducible training, model registry, CI/CD for models.**
- **Monitoring in prod:** data drift, concept drift, and performance decay — with
  alerts and a retraining trigger.

## Enterprise / regulated considerations

Relevant for many senior roles (and doubly so in regulated industries):
- **Data residency & privacy:** VPC/on-prem/private endpoints; never send
  regulated data to an unapproved API; PII redaction before the prompt.
- **Auditability:** log prompts, retrieved sources, and outputs for traceability.
- **Access control** on both the data *and* the retrieval layer (a user must not
  retrieve documents they can't see).
- **Human-in-the-loop** for high-stakes outputs; clear "AI-generated" labeling.

## The AI system-design interview

A repeatable framework for "design an AI assistant for X":
1. **Clarify:** users, volume, latency budget, accuracy bar, data sources,
   privacy constraints, offline vs online.
2. **Data & retrieval:** sources, chunking, embeddings, index, refresh strategy.
3. **Model choice:** hosted vs self-hosted, size/cost/latency trade-off, fallback.
4. **Orchestration:** prompt/agent flow, tool use, guardrails.
5. **Evaluation:** offline golden set + online metrics + human review loop.
6. **Serving:** caching, streaming, autoscaling, rate limits, cost controls.
7. **Safety & ops:** prompt-injection defense, PII handling, monitoring, on-call.

Worked examples of steps 2 and 5 live in [`rag.md`](rag.md) and
[`evaluation-and-safety.md`](evaluation-and-safety.md).

## Rapid-fire Q&A

- **Cut hallucinations?** Ground with RAG, require citations, lower temperature,
  add "say I don't know," and validate outputs against a schema/source.
- **Embeddings vs fine-tuning for search?** Embeddings — semantic search is a
  retrieval problem, not a behavior problem.
- **Chunk size?** Start ~200–500 tokens with overlap; tune by eval. Too big =
  noisy retrieval, too small = lost context.
- **Agent won't stop looping?** Cap iterations, add a termination check, and make
  tool results unambiguous; often a planning/observation problem, not the model.
- **Pick a vector DB?** Start with pgvector if you already run Postgres; move to a
  dedicated store only when scale/latency forces it.
- **Prove your LLM feature works?** A versioned eval set + LLM-as-judge +
  regression tests in CI — see [`evaluation-and-safety.md`](evaluation-and-safety.md).
