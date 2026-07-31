# System design fundamentals (HLD)

The specific designs in [`high-level/`](high-level/) all assemble from the same set of
building blocks. Master these and the interview becomes "pick the right blocks and
defend the trade-offs" instead of memorizing solutions. This is the primer; read it
before the individual designs.

## Contents
- [The interview framework](#the-interview-framework)
- [Back-of-the-envelope estimation](#back-of-the-envelope-estimation)
- [Load balancing](#load-balancing)
- [Caching](#caching)
- [Databases: replication, sharding, indexing](#databases)
- [Consistency & CAP](#consistency--cap)
- [Messaging & async processing](#messaging--async-processing)
- [CDN, API gateway, and the edges](#cdn-api-gateway-and-the-edges)
- [Communication styles](#communication-styles)
- [Reliability patterns](#reliability-patterns)
- [The scaling journey](#the-scaling-journey)
- [Trade-offs interviewers want to hear](#trade-offs-interviewers-want-to-hear)

---

## The interview framework

A repeatable 45-minute structure — driving it is half the score:
1. **Requirements (5 min).** Functional ("what does it do") and non-functional
   (scale, latency, availability, consistency, read/write ratio). *Nail the scope —
   don't design the whole of Twitter; agree on 2–3 core features.*
2. **Estimation (2–3 min).** QPS, storage, bandwidth (below). Sets the tone for every
   later decision.
3. **API design.** The handful of endpoints the core features need.
4. **Data model.** Entities, relationships, and the access patterns that decide
   SQL vs NoSQL and your indexes.
5. **High-level design.** Draw the boxes: clients → LB → services → cache → DB →
   queue. Get a working end-to-end path first.
6. **Deep dive.** The interviewer picks a component; go deep on *its* trade-offs.
7. **Bottlenecks & scale.** Where it breaks at 10×, and how you'd shard/cache/queue
   your way out.

Talk trade-offs the whole way. "It depends, and here's on what" is the senior signal.

## Back-of-the-envelope estimation

Know these cold; they make estimates fast:

**Latency numbers (orders of magnitude):** memory read ~100 ns; SSD read ~100 µs;
network round-trip within a datacenter ~0.5 ms; disk seek ~10 ms; inter-continental
round-trip ~150 ms. **Memory is ~10⁵× faster than disk** — the whole reason caches
exist.

**Powers of two / scale:** 2¹⁰ ≈ 1 K, 2²⁰ ≈ 1 M, 2³⁰ ≈ 1 B. A char ≈ 1 byte, a
typical row/record often 100 B–1 KB.

**QPS math:** 1 M daily active users × 10 requests/day ≈ 10 M req/day ≈ **~115 req/s
average**; multiply by ~2–3 for peak. Reads usually dominate writes (often 10:1 or
100:1) — design read and write paths separately.

**Storage math:** items/day × size × retention. E.g. 100 M photos/day × 1 MB × 365 ≈
~36 PB/year — which immediately tells you "object storage + CDN," not a SQL blob.

## Load balancing

Distributes traffic across servers so no one instance is overwhelmed, and provides a
stable entry point as instances come and go.
- **L4 (transport)** balances by IP/port — fast, protocol-agnostic. **L7
  (application)** understands HTTP — can route by path/header/cookie, do TLS
  termination, and enable sticky sessions.
- **Algorithms:** round-robin, least-connections, weighted, IP-hash (sticky).
- **Health checks** remove unhealthy instances automatically.
- Run **multiple LBs** (active-passive/active-active) so the LB itself isn't a single
  point of failure.

## Caching

The highest-leverage performance tool. **Cache close to where it's read.**
- **Layers:** browser → CDN (static/edge) → application/in-memory (Redis/Memcached) →
  database buffer cache.
- **Write policies:** *cache-aside* (app reads cache, on miss loads DB and populates —
  the default), *write-through* (write cache + DB together, consistent but slower
  writes), *write-back* (write cache, flush later — fast but risks data loss).
- **Eviction:** LRU (most common), LFU, TTL-based.
- **The hard part is invalidation** — stale caches cause the subtle bugs. Always set a
  TTL and have an invalidation story. Know **cache stampede** (many misses hit the DB
  at once when a hot key expires) and its fixes: locking, request coalescing, early
  recompute, jittered TTLs.
- **What not to cache:** highly personalized or rapidly-changing data with low reuse.

## Databases

(Deep dive on SQL/NoSQL/indexing lives in [`../data/`](../data/) — the design-relevant
parts:)

- **Replication** — copies for availability and read scaling.
  - *Leader-follower:* writes to the leader, reads from followers. Simple; followers
    lag → **eventual consistency** on reads.
  - *Multi-leader / leaderless:* higher write availability, but conflict resolution
    gets hard.
- **Sharding / partitioning** — split data across nodes when one box can't hold it or
  serve the write load.
  - *Range* partitioning (good for range scans, risks hot spots).
  - *Hash* partitioning (even spread, no range scans).
  - **Consistent hashing** — the key technique: hashes nodes and keys onto a ring so
    adding/removing a node moves only ~1/N of keys (not everything). This is *the*
    answer to "how do you add capacity to a cache/DB cluster without rehashing
    everything." Virtual nodes smooth the distribution.
  - Hard parts: choosing a shard key that spreads load and avoids **cross-shard
    joins/transactions**; rebalancing.
- **Indexing** — turns O(n) scans into O(log n); index what you filter/join/sort on;
  every index speeds reads but slows writes.

## Consistency & CAP

- **CAP:** under a network **P**artition you must choose **C**onsistency or
  **A**vailability. Partition tolerance is mandatory in a distributed system, so the
  real choice *during a partition* is C vs A. **PACELC** extends it: *else* (no
  partition) you trade **L**atency vs **C**onsistency.
- **Strong consistency** — every read sees the latest write (needed for money,
  inventory). Costs latency/availability.
- **Eventual consistency** — replicas converge over time (fine for feeds, likes,
  view counts). Buys availability and speed.
- Name the middle grounds: read-your-writes, monotonic reads, causal consistency.
- Senior move: pick consistency **per feature**, not per system (a payment is strong;
  a "seen by" count is eventual).

## Messaging & async processing

Decouple producers from consumers so slow/spiky work doesn't block the request path.
- **Message queue** (e.g. RabbitMQ/SQS) — point-to-point work distribution; smooths
  spikes, enables retries, provides backpressure.
- **Log/stream** (e.g. Kafka) — durable, replayable, ordered-within-partition; multiple
  consumer groups; the backbone of event-driven systems and analytics pipelines.
- **Delivery semantics:** at-most-once, at-least-once (the common default — so make
  consumers **idempotent**), exactly-once (hard/expensive).
- Use async for anything the user doesn't need to wait on: emails, notifications,
  thumbnails, analytics, fan-out.

## CDN, API gateway, and the edges

- **CDN** — caches static assets (and increasingly API responses) at edge locations
  near users; the biggest win for global latency and origin offload.
- **API gateway / reverse proxy** — single entry point that does auth, rate limiting,
  routing, TLS, and request aggregation in front of your services.
- **Rate limiting** — protect services from abuse/overload; token-bucket is the usual
  algorithm (full design in [`high-level/rate-limiter.md`](high-level/rate-limiter.md)).

## Communication styles

- **REST** — resource-oriented HTTP; simple, cacheable, universal. Default for public
  APIs.
- **gRPC** — binary (protobuf) over HTTP/2; fast, typed, streaming — great for
  internal service-to-service.
- **GraphQL** — client specifies exactly what it needs; avoids over/under-fetching;
  cost is server complexity and caching difficulty.
- **WebSockets / SSE** — persistent/one-way push for real-time (chat, live feeds).
- **Sync vs async:** call synchronously when the caller needs the result now; use a
  queue when it doesn't.

## Reliability patterns

- **Idempotency** — safe retries; use idempotency keys for writes/payments.
- **Retries with exponential backoff + jitter** — recover from transient failures
  without stampeding.
- **Circuit breaker** — stop calling a failing dependency to let it recover and fail
  fast.
- **Bulkhead / graceful degradation** — isolate failures; serve a reduced experience
  rather than a total outage.
- **Redundancy across AZs**, health checks, and automated failover for HA.
- **Single points of failure** — hunt them down; every tier should be replaceable.

## The scaling journey

The classic narrative to walk when asked "how does this scale?":
1. **Single server** (app + DB together).
2. **Split the database** onto its own machine.
3. **Add read replicas** + a **load balancer** across multiple app servers (make the
   app tier **stateless** so any server handles any request; push sessions to Redis).
4. **Add a cache** (Redis) in front of hot reads.
5. **Add a CDN** for static/edge content.
6. **Shard the database** when one box can't hold the data or writes.
7. **Introduce queues** for async work and spikes.
8. **Split into services** when teams/domains demand independent scaling & deploys —
   accepting the distributed-systems cost (network, consistency, ops).

## Trade-offs interviewers want to hear

- **SQL vs NoSQL** — structure + transactions vs scale + flexible schema (match access
  patterns).
- **Strong vs eventual consistency** — correctness vs availability/latency, per feature.
- **Monolith vs microservices** — simplicity vs independent scaling/deploys and org
  scaling (don't start with microservices).
- **Sync vs async** — immediacy vs decoupling/resilience.
- **Normalization vs denormalization** — integrity vs read performance.
- **Latency vs throughput vs cost** — you can't max all three; know which the problem
  prioritizes.

> There is rarely one right answer — the interview scores whether you can name the
> options, pick one for *this* problem's constraints, and articulate what you gave up.
