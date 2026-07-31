# High-level design — worked examples

Ten classic system-design problems, each written to a senior bar: lead with the core
decision, reason through the trade-offs, and close with what to voice in the interview.

> **Read [`../fundamentals.md`](../fundamentals.md) first.** Every design here assembles
> from those building blocks (load balancing, caching, sharding, replication,
> consistency, queues, estimation). This folder is practice at *applying* them.

## The designs — and the one idea each turns on

| Design | The centerpiece decision |
|---|---|
| [TinyURL](tinyurl.md) | Key generation (distributed ID + Base62) and **301 vs 302** redirects |
| [Rate limiter](rate-limiter.md) | Algorithm choice + **atomic** distributed counting (no read-modify-write race) |
| [Chat application](chat-application.md) | Routing a message to the server holding the recipient's **live WebSocket** |
| [News feed](social-media-feed.md) | **Fan-out on write vs read** + the celebrity problem → hybrid |
| [Notification system](notification-system.md) | A **queue** to decouple delivery; dedup, retries + DLQ, preferences |
| [Payment system](payment-system.md) | **Idempotency**, a double-entry **ledger**, PCI tokenization, state machine |
| [Search engine](search-engine.md) | The **inverted index** + ranking (BM25) + scatter-gather sharding |
| [Distributed cache](distributed-cache.md) | **Consistent hashing** + replication + the hot-key problem |
| [Distributed logging](distributed-logging.md) | A durable **buffer (Kafka)** decoupling producers; tiered storage |
| [Distributed file system](distributed-file-system.md) | **Blocks + replication** and the metadata/data-plane split (GFS/HDFS) |

## How to practice

Pick a design, then narrate it end-to-end using the framework from `fundamentals.md`:
requirements → estimation → API → data model → high-level design → deep dive →
bottlenecks. Don't memorize the answer — rehearse *making and defending the
centerpiece decision*, because the interviewer will push on your trade-offs, not your
recall.

## Recurring patterns across these designs
- **Read-heavy → cache + CDN + replicas** (TinyURL, feed, search).
- **Write spikes / slow downstream → a queue decouples it** (notifications, logging,
  feed fan-out, payments' outbox).
- **Scale a stateful tier → consistent hashing / sharding** (cache, DFS, search index).
- **Correctness-critical → idempotency + strong consistency** (payments).
- **Fan-out on write vs read** recurs wherever one event reaches many consumers (feed,
  chat groups, notifications).

## References
- *Designing Data-Intensive Applications* (Kleppmann) — the single best book here
- *System Design Interview* Vol. 1–2 (Alex Xu) · the original GFS / Dynamo / Kafka papers
