# System design

FAANG "design" interviews are really **three different rounds** — know which one
you're in, because they test different skills:

| Round | What it is | Here |
|---|---|---|
| **HLD** (High-Level / System Design) | Architect a distributed system — services, data, scale, trade-offs | [`fundamentals.md`](fundamentals.md) + [`high-level/`](high-level/) |
| **LLD** (Low-Level / Object-Oriented Design) | Model a domain as clean classes — SOLID, patterns | [`low-level-design.md`](low-level-design.md) |
| **OS / CS fundamentals** | Processes, memory, concurrency, networking | [`os-internals/`](os-internals/) |

Plus a focused topic: [`multi-tenancy.md`](multi-tenancy.md).

## Where to start

1. **[`fundamentals.md`](fundamentals.md)** — the HLD building blocks (load balancing,
   caching, replication/sharding, consistency/CAP, queues, CDN, estimation) and the
   interview framework. **Read this first** — every design in `high-level/` assembles
   from these blocks.
2. **[`high-level/`](high-level/)** — ten worked designs (TinyURL, chat, rate limiter,
   news feed, notification system, payment system, search, distributed cache/logging/
   file system). Practice narrating each with the framework from `fundamentals.md`.
3. **[`low-level-design.md`](low-level-design.md)** — the OOD round: the design
   process, SOLID, the patterns that recur, and a worked parking-lot example.
4. **[`os-internals/`](os-internals/)** — OS/CS fundamentals that underpin the above
   (and show up directly in systems-heavy roles).

## How senior loops differ from junior

At senior/staff level the interviewer cares less about whether you *know* a component
and more about **trade-off reasoning**: why this consistency model, why shard on this
key, what breaks at 10×, what you'd give up. Lead with "it depends, and here's on
what." Drive the conversation through the framework rather than waiting to be asked.

## Cross-references
- Data-layer depth (SQL/NoSQL, indexing, CAP): [`../data/`](../data/)
- Cloud/infra building blocks (LB, containers, queues in practice): [`../devops/`](../devops/)
- AI system design (RAG/agent architectures): [`../ai-ml/README.md`](../ai-ml/README.md)
