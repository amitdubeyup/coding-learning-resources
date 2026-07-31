# Retrieval-Augmented Generation (RAG)

RAG grounds an LLM in your data: retrieve relevant context, put it in the prompt,
generate an answer citing it. It's the default way to give a model knowledge it
wasn't trained on — without fine-tuning.

## The pipeline

```
Documents → chunk → embed → index (vector store)
                                     │
Query → embed → retrieve top-k → (rerank) → build prompt → LLM → cited answer
```

**Ingestion (offline):** load → clean → chunk → embed each chunk → store vectors
+ metadata. Re-run on data changes.

**Query (online):** embed the query → similarity search for top-k chunks →
optionally rerank → assemble a grounded prompt → generate.

## Minimal reference implementation

```python
# Retrieval + grounded generation (pseudo-real; swap in your SDKs)
def answer(query, store, llm, k=5):
    q_vec = embed(query)
    hits = store.search(q_vec, k=k)              # [(chunk_text, metadata, score)]
    context = "\n\n".join(
        f"[{i+1}] {h.text} (source: {h.metadata['source']})"
        for i, h in enumerate(hits)
    )
    prompt = (
        "Answer using ONLY the context. Cite sources as [n]. "
        "If the answer isn't in the context, say you don't know.\n\n"
        f"Context:\n{context}\n\nQuestion: {query}"
    )
    return llm.generate(prompt, temperature=0)
```

The three lines that make it *good*: "use ONLY the context", "cite sources", and
"say you don't know." Without them you get confident hallucinations.

## The knobs that decide quality

- **Chunking.** Start ~200–500 tokens with ~10–20% overlap. Split on semantic
  boundaries (headings, paragraphs), not blindly by character count. Too large →
  irrelevant noise dilutes retrieval; too small → answers lose context.
- **Embeddings.** Pick a current, well-benchmarked embedding model; keep the
  *same* model for indexing and querying. Normalize vectors; use cosine similarity.
- **Top-k.** More context isn't better — it adds noise and cost. Tune k by eval.
- **Hybrid search.** Combine dense (vector) with sparse keyword (BM25) retrieval;
  fuse with Reciprocal Rank Fusion. Dense catches meaning, sparse catches exact
  terms, IDs, and rare tokens. Hybrid beats either alone on most corpora.
- **Reranking.** Retrieve ~20–50 candidates with a fast bi-encoder, then reorder
  with a cross-encoder reranker and keep the top 3–5. Biggest precision win per
  unit effort.
- **Metadata filtering.** Filter by tenant, date, permissions, doc type *before*
  or *during* search — critical for correctness and access control.

## Choosing a vector store

- **pgvector (Postgres):** default if you already run Postgres — one system,
  transactional, metadata filtering via SQL, good to millions of vectors.
- **Dedicated stores:** reach for one when you need very large scale, low-latency
  ANN, or managed ops. Evaluate on recall@k, latency, filtering, and cost.
- Know the index type trade-off: **HNSW** (fast, high-recall, more memory) vs
  **IVF** (smaller memory, needs training/tuning). Both are ANN — approximate,
  trading a little recall for big speed.

## Evaluating RAG (this is what separates seniors)

Measure retrieval and generation **separately**:
- **Retrieval:** recall@k / precision@k / MRR against a labeled query→relevant-doc
  set. If the right chunk isn't retrieved, no prompt can save you.
- **Generation:** faithfulness (is every claim supported by the context?),
  answer relevance, and citation correctness — commonly scored with an
  LLM-as-judge and frameworks like RAGAS. See
  [`evaluation-and-safety.md`](evaluation-and-safety.md).

## Failure modes & fixes

| Symptom | Likely cause | Fix |
|---|---|---|
| Right facts exist but aren't retrieved | bad chunking / embeddings / low k | fix chunking, add hybrid + rerank, raise k |
| Retrieves relevant chunks, still wrong answer | weak prompt / model ignores context | stronger grounding prompt, lower temp, cite-and-verify |
| Confidently makes things up | no "I don't know" path | instruct abstention; validate against sources |
| Slow / expensive | too many/large chunks, no cache | rerank to fewer chunks, semantic cache, smaller model |
| Leaks other users' data | no metadata/permission filter | enforce access filters at retrieval time |

## Beyond basic RAG (know these exist)

- **Query rewriting / expansion** and **multi-query** retrieval for vague questions.
- **Agentic RAG:** the model decides *when* and *what* to retrieve, iteratively.
- **GraphRAG:** retrieve over a knowledge graph for multi-hop / relational questions.
- **Contextual retrieval:** prepend document-level context to each chunk before
  embedding to preserve meaning that chunking would otherwise strip.
