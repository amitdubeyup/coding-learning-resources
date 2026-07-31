# Design a rate limiter

Restrict how many requests a client can make in a window — to protect services from
abuse, accidental overload, and cost blowouts. The interview is mostly about
**which algorithm** and **how to make it correct and fast across many servers**.

## 1. Requirements

**Functional:** limit by key (user / IP / API key), configurable limits per
route, return standard `X-RateLimit-*` headers and **429 Too Many Requests** when
exceeded. **Non-functional:** very **low latency** (it's on every request's hot path —
add <~few ms), **highly available**, and **consistent enough** across a fleet of
servers. Decide **fail-open vs fail-closed** if the limiter's datastore is down
(usually **fail-open** — don't take the whole API down because Redis blipped).

## 2. Where it runs

Usually at the edge — an **API gateway** or a middleware in front of services — so bad
traffic is rejected before it costs you real work. The counters live in a **shared,
fast store (Redis)** so all app servers see the same count.

## 3. The algorithms (know the trade-offs)

| Algorithm | How | Trade-off |
|---|---|---|
| **Fixed window** | count per calendar window (e.g. per minute) | simplest; **boundary burst** — 2× the limit can slip through across the window edge |
| **Sliding window log** | store every request timestamp, count those in the last window | exact; **memory-heavy** at scale |
| **Sliding window counter** | weight current + previous fixed windows | great accuracy/memory balance — common production choice |
| **Token bucket** | tokens refill at a rate; each request spends one | **allows controlled bursts**; the usual default |
| **Leaky bucket** | queue drains at a fixed rate | **smooths** output to a constant rate; no bursts |

Senior framing: **token bucket** when you want to permit short bursts (most APIs);
**leaky bucket** when a downstream needs a steady rate; **sliding window counter**
when you want accurate per-window limits cheaply.

## 4. Token bucket (single-node reference)

```python
import time

class TokenBucket:
    def __init__(self, capacity, refill_per_sec):
        self.capacity = capacity
        self.refill = refill_per_sec
        self.tokens = capacity
        self.ts = time.monotonic()

    def allow(self, cost=1):
        now = time.monotonic()
        self.tokens = min(self.capacity, self.tokens + (now - self.ts) * self.refill)
        self.ts = now
        if self.tokens >= cost:
            self.tokens -= cost
            return True
        return False
```

## 5. Distributed correctness (the part people get wrong)

Across many servers the counter is shared in Redis — and the update **must be atomic**.
A `GET` then `INCR` is a **race**: two servers can both read "under limit" and both
increment, overshooting. Fix it one of these ways:

**(a) Atomic fixed/counter window — `INCR` first, set expiry on creation:**
```python
def allow(redis, key, limit, window_seconds):
    count = redis.incr(key)          # atomic; creates at 1 if absent
    if count == 1:
        redis.expire(key, window_seconds)
    return count <= limit
```
`INCR` is atomic, so no lost updates. (Minor caveat: if the process dies between
`incr` and `expire`, the key could lack a TTL — do both in a **Lua script** to make
the whole check-and-set atomic in production.)

**(b) Sliding window log with a sorted set** (accurate): store timestamps in a
`ZSET`, drop old entries with `ZREMRANGEBYSCORE`, then `ZCARD` to count — wrap in a Lua
script/pipeline so it's atomic.

The interview point: **name the race and reach for an atomic primitive (INCR/Lua/ZSET),
not read-modify-write.**

## 6. Scaling & operational concerns

- Redis handles very high throughput; **shard by key** if one node isn't enough, and
  co-locate the limiter with the gateway to keep latency low.
- **Local + global two-tier:** an in-process token bucket per server as a cheap first
  gate, backed by Redis for the shared truth — cuts Redis load.
- **Fail-open** when Redis is unreachable (availability > perfect enforcement), unless
  the endpoint is security-critical.
- Return `Retry-After` and `X-RateLimit-{Limit,Remaining,Reset}` so clients back off
  politely.

## Trade-offs to voice
- **Accuracy vs cost/latency** — sliding-window log is exact but heavy; counter/token
  approximate but cheap.
- **Local vs distributed** — per-node is fast but lets `N×limit` through; shared Redis
  is consistent but adds a network hop.
- **Fail-open vs fail-closed** — availability vs strict enforcement when the store is down.
- **Burst vs smooth** — token bucket vs leaky bucket.
