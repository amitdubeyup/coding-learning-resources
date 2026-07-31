# LLM foundations — how the models actually work

Senior AI interviews open here. The bar has shifted: AI-engineer loops are now
majority-GenAI, and the fastest way to fail is to *use* LLMs without being able to
explain how they work when something breaks. This file is the "foundations" tier —
tokenization, attention, positional encoding, scaling, fine-tuning, and the
reasoning/inference-time-compute paradigm. Application (RAG, agents) and production
(evals, serving) live in the sibling files.

## Contents
- [Tokenization & embeddings](#tokenization--embeddings)
- [The Transformer & attention](#the-transformer--attention)
- [Positional encoding](#positional-encoding)
- [Scaling laws](#scaling-laws)
- [How a model is trained (pretrain → align)](#how-a-model-is-trained)
- [Fine-tuning & PEFT (LoRA / QLoRA)](#fine-tuning--peft)
- [Reasoning models & inference-time compute](#reasoning-models--inference-time-compute)
- [Multimodal models](#multimodal-models)
- [Decoding & sampling](#decoding--sampling)
- [Rapid-fire Q&A](#rapid-fire-qa)
- [Key papers](#key-papers)

---

## Tokenization & embeddings

- **Tokens, not words.** Text is split into subword units (usually **Byte-Pair
  Encoding** or similar). ~4 chars/token in English. Everything you pay for and every
  limit you hit — cost, context window, latency — is measured in tokens.
- **Why subwords?** They balance vocabulary size against sequence length and handle
  rare/unseen words by composing them from pieces (no out-of-vocabulary problem).
- **Embeddings** map each token to a dense vector. Learned so that
  semantically-related tokens land near each other. *Contextual* embeddings (produced
  by the model's layers) differ from *static* ones — "bank" gets a different vector in
  "river bank" vs "bank account."
- Interview trap: an embedding **model** for retrieval (bi-encoder producing one
  vector per text) is a different thing from the token embeddings *inside* an LLM.

## The Transformer & attention

The 2017 "Attention Is All You Need" architecture replaced recurrence (RNNs/LSTMs,
which process tokens sequentially) with **self-attention**, which processes all tokens
in parallel — the unlock behind training at scale.

**Self-attention, in one breath:** every token produces a **Query**, **Key**, and
**Value** vector. A token's output is a weighted sum of all tokens' Values, where the
weights come from the softmax of its Query dotted with every Key (scaled by √d):

```
Attention(Q, K, V) = softmax(QKᵀ / √dₖ) · V
```

- **Why √dₖ?** Without scaling, large dot products push softmax into saturated regions
  with vanishing gradients.
- **Multi-head attention:** run several attention operations in parallel subspaces so
  the model attends to different relationships (syntax, coreference, …) at once.
- **The O(n²) cost:** attention compares every token to every other token, so compute
  and memory scale quadratically with sequence length. This is *the* reason long
  context is expensive and why work like FlashAttention (I/O-aware exact attention)
  and various sparse/linear approximations exist.
- **Three shapes:** decoder-only (GPT-style, **causal mask** so a token sees only
  earlier tokens — the dominant generative design), encoder-only (BERT-style,
  bidirectional — great for embeddings/classification), encoder-decoder (T5-style —
  translation/seq2seq).

## Positional encoding

Self-attention is **permutation-invariant** — on its own it has no notion of order, so
position must be injected. Know the progression:
- **Sinusoidal** (original) — fixed sine/cosine patterns.
- **Learned** — position embeddings trained like token embeddings.
- **RoPE (Rotary Positional Embedding)** — rotates Q/K by an angle proportional to
  position, encoding *relative* position directly in the dot product. **The default in
  most modern LLMs** because it extrapolates to longer contexts better; techniques like
  **YaRN** extend a RoPE model's usable context beyond its training length.
- **ALiBi** — biases attention scores by distance; another extrapolation-friendly
  option.

## Scaling laws

- **Chinchilla (2022)** showed most large models were *undertrained*: for a fixed
  compute budget, you should scale parameters and training tokens **together**, roughly
  **~20 tokens per parameter**. "Bigger model" isn't automatically better — data
  quantity and quality matter as much as parameter count.
- **Data quality** (curation, dedup, synthetic data — the "Phi" lesson) can beat raw
  scale. Interviewers like the nuance that scale is necessary but not sufficient.

## How a model is trained

Three stages — be able to name them:
1. **Pretraining** — self-supervised next-token prediction on a huge corpus. Produces a
   *base* model that completes text but doesn't reliably follow instructions.
2. **Instruction tuning (SFT)** — supervised fine-tuning on (instruction, response)
   pairs so the model follows directions.
3. **Preference alignment** — align outputs to human preferences via **RLHF** (reward
   model + PPO), or lighter-weight **DPO**; for reasoning, **GRPO**-style RL is now
   common. This is where "helpful/harmless/honest" behavior is shaped.

## Fine-tuning & PEFT

**Full fine-tuning** updates all weights — accurate but expensive (memory for optimizer
states, a full model copy per task). **PEFT (parameter-efficient fine-tuning)** avoids
that:

- **LoRA (Low-Rank Adaptation):** freeze the base weights `W₀`; learn a low-rank update
  `ΔW = B·A` where `A` is `r×d_in`, `B` is `d_out×r`, and rank `r` is small (≈8–64). At
  inference the effective weight is `W₀ + (α/r)·B·A`. At rank 16 on a 7B model you train
  well under 1% of parameters yet recover ~90–95% of full-fine-tune quality — and
  adapters are tiny and swappable per task.
- **QLoRA:** quantize the frozen base to 4-bit (NF4) and train LoRA adapters on top —
  a 7B model that needs ~14 GB in 16-bit fits in ~5–6 GB, so you can fine-tune large
  models on a single GPU.
- **Distillation** — train a smaller "student" to mimic a larger "teacher." Use it when
  the goal is a permanently cheaper model, not new behavior.

**When to fine-tune at all** (the decision, senior version): fine-tune to change
**behavior/format/skill/tone** or to make a small model good at a narrow task; use
**RAG** to inject **knowledge**, especially frequently-changing knowledge; use
**prompting** first because it's the cheapest thing that often works. They combine —
fine-tune *and* RAG the same model. (Full RAG-vs-fine-tune deep dive in [`rag.md`](rag.md).)

## Reasoning models & inference-time compute

The major 2024→2026 shift. Instead of only scaling *training*, you can scale
**compute at inference** to get better answers on hard problems:

- **Chain-of-thought (CoT)** — generate intermediate reasoning before the answer;
  helps mostly on math/symbolic/multi-step tasks.
- **Self-consistency** — sample several reasoning paths and take a majority vote;
  reliably beats a single greedy decode on reasoning.
- **Search at inference** — best-of-N, beam search, or Monte Carlo Tree Search,
  often guided by a reward/verifier model.
- **Reasoning models** (DeepSeek-R1, Qwen3-style) are *trained* (via RL) to produce
  long internal "thinking" tokens separate from the final answer — so the reasoning is
  learned, not just prompted.

The core idea: **test-time compute is now a scaling axis of its own** — a smaller model
that "thinks longer" can match a much larger one on suitable tasks. The trade-off is
blunt and interview-relevant: **more thinking = more tokens = more latency and cost**,
and it's not free lunch (there's even evidence of *inverse* scaling, where extra
reasoning sometimes hurts). Senior answer: gate reasoning effort by task difficulty and
route easy queries to a fast path.

## Multimodal models

Vision-language models (VLMs) pair an image encoder with the LLM:
- **Contrastive pretraining** (CLIP-style) aligns image and text embeddings in a shared
  space.
- A **projection layer** maps image features into the LLM's token space; **LLaVA-style
  instruction tuning** then teaches it to converse about images.
- **Failure modes to name:** hallucinated objects, brittle OCR/fine-text reading, and
  evaluation contamination.

## Decoding & sampling

- **Temperature** scales randomness (0 ≈ deterministic — use for extraction/
  classification; higher for creativity).
- **top-k / top-p (nucleus)** truncate the sampling distribution to the most likely
  tokens.
- **Greedy vs sampling** — greedy is repeatable but bland; sampling is diverse but
  variable.
- **Constrained / structured decoding** forces valid JSON/grammar — prefer it over
  "please return JSON" for reliability.

## Rapid-fire Q&A

- **Why does attention cost O(n²)?** Every token attends to every other token.
- **Why is positional encoding needed?** Attention is order-agnostic; position must be
  injected (RoPE is today's default).
- **LoRA vs full fine-tuning?** Train tiny low-rank adapters over frozen weights —
  ~1% of params, swappable, near-full quality — vs updating everything.
- **QLoRA's trick?** 4-bit-quantized frozen base + LoRA → fine-tune big models on one GPU.
- **Fine-tune vs RAG?** Behavior/skill vs knowledge (especially fresh knowledge).
- **What is a reasoning model?** One trained to spend inference compute "thinking"
  before answering; trades latency/cost for accuracy on hard tasks.
- **How do you cut long-context cost?** Retrieve less (RAG), summarize/trim history,
  or use models/attention variants designed for it — the cost is quadratic in tokens.
- **Encoder-only vs decoder-only?** Bidirectional (embeddings/classification) vs
  causal/generative.

## Key papers

Primary sources worth reading (search title or arXiv ID):
- *Attention Is All You Need* — Vaswani et al., 2017 (arXiv:1706.03762)
- *RoFormer* (RoPE) — Su et al., 2021 (arXiv:2104.09864)
- *Training Compute-Optimal LLMs* (Chinchilla) — Hoffmann et al., 2022 (arXiv:2203.15556)
- *Chain-of-Thought Prompting* — Wei et al., 2022 (arXiv:2201.11903)
- *Self-Consistency* — Wang et al., 2022 (arXiv:2203.11171)
- *LoRA* — Hu et al., 2021 (arXiv:2106.09685); *QLoRA* — Dettmers et al., 2023 (arXiv:2305.14314)
- *Scaling LLM Test-Time Compute* — Snell et al., 2024 (arXiv:2408.03314)
- *DeepSeek-R1* — DeepSeek-AI, 2025 (arXiv:2501.12948)
