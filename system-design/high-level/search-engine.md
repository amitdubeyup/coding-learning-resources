# Design a search engine

Two flavors get asked: **web-scale search** (crawl the internet, rank with link
analysis) and, more commonly, a **search feature** over your own corpus (products,
docs, messages). Both stand on the same idea — the **inverted index** — so lead with
that, then adapt.

## 1. Requirements

**Functional:** full-text search over a large corpus; relevance ranking; filters/
facets; autocomplete; near-real-time indexing of new/updated docs. **Non-functional:**
low latency (<~200 ms), high availability, scale to billions of docs, good relevance.

## 2. The core idea: the inverted index

A naive scan of every document per query is impossible at scale. Instead, build an
**inverted index**: for each **term**, store a **posting list** of the documents (and
positions) containing it.

```
"machine" → [doc3, doc7, doc42, ...]
"learning" → [doc7, doc42, doc99, ...]
```

A query for `machine learning` then becomes: fetch both posting lists, **intersect**
them (AND) or union (OR), and you have candidate docs without touching the corpus.
Positions in the postings enable **phrase** search. This is what engines like Lucene/
Elasticsearch implement — for a "search feature" interview, the right answer is usually
"use an inverted-index engine and design the ingestion, index, ranking, and sharding
around it."

## 3. Pipeline

1. **Ingest** — crawl (web) or consume a change stream (your data).
2. **Analyze** — tokenize, lowercase, remove stop-words, stem/lemmatize, so "running"
   matches "run." Do the *same* analysis at index and query time.
3. **Index** — write terms → postings; support **near-real-time** updates by indexing
   into small segments and merging in the background.
4. **Serve** — analyze the query, fetch postings, combine, **rank**, paginate.

## 4. Ranking (the relevance half)

- **Term relevance:** **TF-IDF / BM25** — a term is more significant if frequent in a
  doc but rare across the corpus. BM25 is the standard baseline.
- **Query-independent signals:** popularity, freshness, and for the web, **link
  analysis (PageRank-style)** — authoritative pages rank higher.
- **Learning-to-rank:** an ML model combines these signals from click/engagement data
  — the modern top layer.

## 5. Sharding a huge index (scatter-gather)

- **Document partitioning (the common choice):** each shard holds a *complete* index
  for its slice of documents. A query **scatters** to all shards, each returns its top
  results, and a coordinator **gathers** and merges them. Scales with document count;
  every query hits every shard.
- **Term partitioning:** each shard owns certain terms' postings. Less common — hot
  terms create hotspots and multi-term queries touch multiple shards awkwardly.
- Replicate shards for availability and query throughput; **cache** hot queries.

## 6. Autocomplete

A separate low-latency path: a **trie** (prefix tree) or an FST of popular queries,
ranked by frequency — returns suggestions in a few ms, independent of the main index.

## Trade-offs to voice
- **Document vs term partitioning** — even load + simple merges (scatter-gather) vs
  fewer shards touched but hotspots.
- **Freshness vs cost** — real-time indexing (segment merges) vs cheaper batch rebuilds.
- **Precision vs recall** — strict matching vs stemming/synonyms that broaden results.
- **Build vs buy** — a tuned Lucene/Elasticsearch cluster vs a from-scratch index
  (almost always use the engine).
