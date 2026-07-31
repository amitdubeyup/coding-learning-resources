# Databases & data

Data-layer interviews test whether you can pick the right store, model data well,
make queries fast, and reason about consistency at scale. This guide is the core;
deep legacy Q&A is preserved in `*-legacy-qa.md`.

## Relational (SQL) fundamentals

- **Model:** tables with a fixed schema, rows, and relationships via foreign keys.
- **Normalization** removes redundancy (1NF→3NF); **denormalization** re-introduces it
  for read performance. Interview answer: normalize for integrity, denormalize
  deliberately for read-heavy paths.
- **Joins:** know INNER (matches only), LEFT (all left + matches), and when a join
  vs. two queries is appropriate.
- **ACID:** Atomicity, Consistency, Isolation, Durability — the guarantees a
  transaction gives. Be able to define each in a sentence.
- **Isolation levels:** Read Uncommitted → Read Committed → Repeatable Read →
  Serializable, trading concurrency for correctness. Know the anomalies each prevents
  (dirty read, non-repeatable read, phantom read).

## Indexing (the #1 performance topic)

- An index is a sorted structure (usually a **B-tree**) that turns an O(n) scan into
  an O(log n) lookup — at the cost of extra storage and slower writes.
- Index the columns you filter/join/sort on; a **composite index**'s column order
  matters (leftmost-prefix rule).
- **Trade-off to state:** every index speeds reads but slows writes and uses space —
  don't index everything.
- Use `EXPLAIN`/`EXPLAIN ANALYZE` to see whether a query uses an index or does a full
  scan. Saying "I'd check the query plan" is the senior move.

## The N+1 query problem

Fetching a list then querying once per item (1 + N queries) — a top real-world
performance bug. Fix with a join, an `IN (...)` batch, or eager loading. Expect this
in ORM-heavy interviews.

## SQL vs NoSQL — and the NoSQL families

Answer "it depends," then the axes: structured/relational data with strong
consistency and complex queries → **SQL**; flexible schema, massive scale, or a
specific access pattern → **NoSQL**. NoSQL families:
- **Document** (MongoDB) — JSON-like docs; flexible schema; great when data is
  accessed as whole documents.
- **Key–value** (Redis, DynamoDB) — fastest lookups by key; caching, sessions.
- **Wide-column** (Cassandra) — huge write throughput, query by known partition key.
- **Graph** (Neo4j) — relationship-heavy traversals.

Modern reality: PostgreSQL with `JSONB` covers many "I need NoSQL flexibility" cases
without giving up SQL — a strong point to make.

## CAP theorem

In a network **P**artition you must choose between **C**onsistency and
**A**vailability. Real systems tune along a spectrum (and PACELC extends it to
latency-vs-consistency in the *absence* of partitions). Don't recite "pick 2 of 3"
naively — explain that partition tolerance is mandatory in a distributed system, so
the real choice under a partition is C vs A.

## Caching with Redis

- Use Redis for hot key–value reads, sessions, rate limiting, queues, and pub/sub.
- **Cache-aside** is the default pattern: check cache → on miss, read DB and populate.
- Always set a **TTL**, and have an **invalidation** story — stale caches cause the
  subtle bugs. Know cache stampede and how a lock/"early recompute" mitigates it.

## Scaling a database (the design-interview arc)

1. **Indexes & query tuning** first — cheapest wins.
2. **Read replicas** to scale reads (accept replication lag → eventual consistency on
   replicas).
3. **Caching** (Redis) in front of hot reads.
4. **Vertical scaling** (bigger box) — simple but capped.
5. **Sharding / horizontal partitioning** — last resort; splits data by a shard key.
   Hard part: choosing a key that spreads load and avoids cross-shard joins.

## Common questions

- **When index vs not?** Index high-selectivity columns you filter/join on; skip
  low-selectivity or write-hot columns.
- **Transaction vs no transaction?** Wrap multi-step writes that must all-or-nothing.
- **SQL vs NoSQL for X?** Map the access pattern and consistency needs to the families
  above.
- **Optimize a slow query?** `EXPLAIN` → add/fix an index → avoid N+1 → reduce
  returned columns/rows → cache if read-heavy.
- **Strong vs eventual consistency?** Strong = every read sees the latest write;
  eventual = replicas converge over time. Pick per use case.

## Deep dives (legacy, pending review)
[`postgresql-legacy-qa.md`](postgresql-legacy-qa.md) ·
[`mongodb-legacy-qa.md`](mongodb-legacy-qa.md) ·
[`overview-legacy.md`](overview-legacy.md)
