# Design a social media feed (news feed)

Twitter/Instagram-style home feed: show a user the recent posts from accounts they
follow, ranked, fast. The whole interview turns on **one decision — how the feed is
assembled (fan-out)** — and the edge case that breaks the naive answer.

## 1. Requirements

**Functional:** home feed of posts from followed accounts; mixed media; interactions
(like/comment/share); pagination/infinite scroll; ranking. **Non-functional:**
**read-dominant** and latency-sensitive (<~200 ms feed load), eventually consistent is
fine (a post appearing a second late is acceptable), huge scale with a **highly skewed
follower graph** (most users have hundreds of followers; a few have tens of millions).

## 2. The core decision: fan-out on write vs read

**Fan-out on write (push):** when a user posts, immediately **push the post id into
every follower's precomputed feed** (their "inbox," a Redis list). Reads are then
trivially fast — just read your inbox. This is the default because feeds are read far
more than they're written.

**Fan-out on read (pull):** store posts by author; at read time, **gather recent posts
from everyone you follow and merge** them. Cheap writes, expensive reads.

**Why push alone fails — the celebrity problem:** a user with 50 M followers posting
once triggers 50 M feed writes — a write storm, and wasteful for inactive followers.

**The hybrid (the senior answer):** fan-out on **write for normal users**, fan-out on
**read for celebrities/hot accounts**. A user's feed = their precomputed inbox
**merged at read time** with the latest posts from the few high-follower accounts they
follow. Best of both; name this explicitly.

## 3. Feed storage & the two flows

- **Feed cache:** per user, a capped list of recent post **ids** in Redis (store ids,
  not full posts — hydrate content separately).
- **Write flow:** create post → persist → enqueue a **fan-out job**; async workers push
  the id into followers' feed lists (skipping celebrity fan-out). Async so posting
  returns instantly.
- **Read flow:** read the feed's post ids from cache → **batch-hydrate** post content
  and live counts from cache/store → merge in celebrity posts → rank → return a page
  via **cursor** pagination.

## 4. Ranking

- **Chronological** is the simple baseline.
- **Ranked feeds** score each candidate by predicted engagement (affinity to author,
  post type, recency **time-decay**, past interaction) — usually an ML model. Say
  "ranking is a scoring layer over the candidate set from fan-out," and that recency
  decay prevents stale content dominating.

## 5. Scaling

- **Media** (images/video) → object storage + **CDN**, never through the feed service.
- **Shard** feed cache and post store by user/author id; heavy **read replicas**.
- **Fan-out workers** scale independently on a queue; back-pressure absorbs posting
  spikes.
- Counts (likes) are hot and approximate — cache and update asynchronously.

## Trade-offs to voice
- **Push vs pull vs hybrid** — fast reads/write-amplification vs cheap writes/slow
  reads vs the hybrid that handles the follower-count skew. *This is the answer they're
  listening for.*
- **Chronological vs ranked** — simple/predictable vs engaging/complex.
- **Consistency** — eventual is fine for a feed; don't pay for strong consistency here.
- **Store ids vs full posts in the feed** — hydrate for freshness/space vs denormalize
  for read speed.
