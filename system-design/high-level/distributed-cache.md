# Design a distributed cache

Design a cache cluster (think Redis Cluster / Memcached) that stores key-value data in
memory across many nodes with sub-millisecond reads. The interview centers on **how
keys are distributed**, **how you survive a node dying**, and the **hot-key** pitfall.
(General caching strategy — where/what to cache — is in [`../fundamentals.md`](../fundamentals.md); this is the cache *system* itself.)

## 1. Requirements

**Functional:** `get`/`set`/`delete` by key, TTL expiry, eviction when memory fills.
**Non-functional:** very **low latency** (<~1 ms), scale to millions of ops/s,
**highly available**, and **horizontally scalable** by adding nodes with minimal
disruption.

## 2. The core problem: distributing keys across nodes

Which node holds a given key? A naive `hash(key) % N` **remaps almost every key when N
changes** (a node added/removed) — a cache-wide miss storm that can stampede the
database.

**Consistent hashing** is the answer: hash both nodes and keys onto a ring; a key
belongs to the next node clockwise. Adding/removing a node moves only ~**1/N** of keys,
not all of them. **Virtual nodes** (each physical node placed at many ring positions)
even out the distribution and smooth rebalancing. This is *the* thing to say.

## 3. Availability: replication

A node dying shouldn't lose its whole keyspace or drop those reads. Give each shard a
**primary + one or more replicas** on different machines:
- **Async replication** (usual for caches) — fast writes, tiny window of possible loss
  on failover. Fine, because a cache is a rebuildable copy of the source of truth.
- **Sync/quorum** — stronger consistency, higher latency; only if the cache must not
  serve stale data.
On primary failure, promote a replica. Since the cache isn't the source of truth,
availability is usually favored over strict consistency (AP).

## 4. Eviction & expiry

Memory is bounded, so you need an **eviction policy** when full:
- **LRU** (evict least-recently-used) — the common default; **LFU** for frequency-
  skewed workloads; **TTL** expiry for time-bounded data.
Combine with a max-memory policy. This is what makes it a *cache* (lossy by design)
rather than a store.

## 5. The hot-key problem (senior pitfall)

Consistent hashing spreads keys evenly, but a **single viral key** (one celebrity, one
trending item) all lands on **one node** and melts it. Mitigations: **replicate hot
keys** across nodes and read from any; add a **client-side/local cache** for the
hottest keys; or key-suffix sharding for that key. Naming the hot-key problem
distinguishes a senior answer.

## 6. Client access & stampede

- **Smart client or proxy** knows the ring and routes each key to the right node
  (client-side sharding avoids a proxy hop).
- **Cache stampede:** when a hot key expires, many misses hit the DB at once — guard
  with a lock/single-flight, early recompute, or jittered TTLs.
- **Write policy** (cache-aside vs write-through vs write-back) is chosen by the app —
  see [`../fundamentals.md`](../fundamentals.md).

## Trade-offs to voice
- **Consistent hashing vs modulo** — minimal reshuffle on scaling vs mass invalidation.
- **Async vs sync replication** — speed + tiny loss window vs consistency + latency
  (async is usually right for a cache).
- **Availability vs consistency** — a cache normally chooses availability; it's not the
  source of truth.
- **Memory vs hit ratio** — more RAM/replicas improve hits at higher cost.
