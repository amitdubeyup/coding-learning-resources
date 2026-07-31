# Design a URL shortener (TinyURL / bit.ly)

The classic warm-up design. It looks trivial, so the interviewer scores you on the
*decisions*: how you generate keys, how you serve reads at scale, and the redirect
subtlety most people miss. Uses the building blocks in [`../fundamentals.md`](../fundamentals.md).

## 1. Requirements

**Functional:** shorten a long URL → short code; visiting the short code redirects to
the original; optional custom alias; optional expiry; basic click analytics.
**Non-functional:** redirects must be **fast** (<~10 ms) and **highly available**
(a dead shortener breaks every link ever made); short codes unique; massively
**read-heavy**.

## 2. Estimation (sets the shape)

Say 100 M new URLs/day and a **100:1 read:write** ratio → ~10 B redirects/day ≈
**~115 K reads/s**, ~1.2 K writes/s. Storage: ~100 M/day × ~500 B × years → tens of
TB. Two takeaways immediately: **optimize the read/redirect path hard** (cache + CDN),
and this is a **key-value** problem (`code → long URL`), not a relational one.

## 3. The core decision: generating the short code

This is the heart of the interview. Two families:

**A) Hash the long URL** (e.g. MD5/SHA, take first 7 chars, Base62). 
- Pro: same URL → same code (natural dedup). 
- Con: **collisions** must be detected and resolved (rehash/append), and it doesn't
  help with custom aliases.

**B) Unique ID → Base62 encode** (preferred senior answer). 
- Generate a globally unique 64-bit ID, then Base62-encode it to a short string.
  **Base62** `[a-zA-Z0-9]` gives 62⁷ ≈ **3.5 trillion** 7-char codes.
- No collisions by construction.
- Con: naive auto-increment is a bottleneck and makes codes **sequential/guessable**
  (enumeration risk). Fix by distributing ID generation:
  - a **ticket/range server** hands each app server a block of IDs (e.g. 1,000 at a
    time) to use locally — cheap and avoids per-write coordination; or
  - a **Snowflake-style** ID (timestamp + machine + sequence); or
  - a key-generation service that pre-generates unused keys.
- To defeat guessing, encode a permuted/salted ID rather than the raw counter.

**Custom aliases:** check uniqueness (a conditional insert / `SETNX`), validate length
and against a blocklist.

## 4. Data model & storage

A key-value mapping fits: `short_code (PK) → long_url, owner, created_at, expiry`.
- At this scale a **NoSQL KV/wide-column store** (or a sharded SQL store, sharded by
  `short_code`) serves lookups by primary key in O(1) — exactly the access pattern.
- Don't over-index; the redirect only needs point lookups by code.

## 5. The read/redirect path (where the traffic is)

1. Request hits `short_code`.
2. **Cache first (Redis), cache-aside.** With 100:1 reads and heavy skew (a few links
   go viral), cache hit rate is very high — most redirects never touch the DB.
3. On miss, read the DB, populate the cache (with TTL).
4. **Redirect — and here's the subtlety:** 
   - **301 (permanent)** → browsers cache it, so subsequent clicks skip your server:
     fewer hits, lower cost, but **you lose per-click analytics**. 
   - **302 (temporary)** → every click comes back to you: enables analytics and lets
     you change the target, at higher traffic. 
   Naming this trade-off is the senior signal; most candidates miss it. Pick 302 if
   analytics matter, 301 if raw scale/cost dominates.

## 6. Analytics without slowing redirects

Never write analytics synchronously on the redirect path. **Emit a click event to a
queue/stream (Kafka)** and process it asynchronously into an analytics store. The
redirect returns immediately; counting is eventually consistent (perfectly fine here).

## 7. Scaling & availability

- **Stateless app tier** behind a load balancer; scale horizontally.
- **Cache + CDN** absorb the read storm; edge-cache hot codes.
- **Shard** the store by `short_code`; add **read replicas**.
- **Expiry/cleanup** via a TTL or a background sweeper.
- Availability > strong consistency here: a slightly stale cache is fine, an outage is
  not (favor A in CAP for the read path).

## Trade-offs to voice
- **Hash vs ID-encode** — dedup-friendly-but-collisions vs collision-free-but-needs-
  distributed-IDs.
- **301 vs 302** — cost/scale vs analytics/flexibility.
- **SQL vs NoSQL** — you only need point lookups, so KV/NoSQL scales more simply.
- **Sequential vs permuted IDs** — simplicity vs unguessability.
