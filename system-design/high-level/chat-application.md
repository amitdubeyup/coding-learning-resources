# Design a real-time chat application (WhatsApp / Slack / Messenger)

The interesting part isn't sending a message — it's delivering it in real time to a
recipient whose live connection is held by *some other server* in a fleet of
thousands, plus persistence, ordering, and offline handling.

## 1. Requirements

**Functional:** 1:1 and group messaging in real time; delivery/read receipts
(sent → delivered → read); online/last-seen presence; message history; push
notifications when offline. **Non-functional:** **low latency** (<~100 ms delivery),
**highly available**, **durable** (never lose a message), ordered within a
conversation, scale to millions of **concurrent persistent connections**.

## 2. Transport: why WebSockets

HTTP is request/response — the server can't push. Options: long-polling (works,
wasteful, higher latency) or **WebSocket** (persistent, bidirectional) — the standard
choice. SSE is one-way (server→client) so it doesn't fit two-way chat. Clients hold an
open WebSocket to a **connection/gateway server**.

## 3. The core problem: routing a message to a live connection

Connections are **stateful** — user A is connected to gateway server G1, user B to
G17. When A sends to B, the server handling A must get the message to the *specific
server* holding B's connection. Two standard approaches:

- **A presence/registry** mapping `user_id → gateway server` (in Redis). G1 looks up
  B, finds G17, forwards the message (directly or via an internal message bus). 
- **A pub/sub backbone** (Redis pub/sub or Kafka): each gateway subscribes to channels
  for its connected users; publishing to B's channel reaches whichever server holds B.

This routing layer — not the API — is what makes chat hard, and it's what the
interviewer wants you to surface. Load balancing WebSockets also needs care (sticky/
consistent routing; connections are long-lived, so you can't rebalance freely).

## 4. Message flow

1. A sends over its WebSocket to its gateway.
2. Gateway **persists** the message (durability first) and assigns a per-conversation
   sequence number for **ordering**.
3. Gateway routes to B's gateway (via registry/pub-sub) → pushed down B's socket →
   client ACKs → status becomes **delivered**; when B views it → **read**.
4. If **B is offline** (no live connection): the message is already persisted; enqueue
   a **push notification** (APNs/FCM). B syncs history on reconnect.
- Make sends **idempotent** (client message id) so retries don't duplicate.

## 5. Storage: pick for the access pattern

Reads are "fetch the last N messages in a conversation, newest first," and writes are
enormous and append-only. That's a **wide-column store (Cassandra/HBase)** sweet spot:
partition by `chat_id`, cluster by time/sequence, so a conversation's recent messages
are a single efficient range read. (A sharded SQL store works at smaller scale; the
write volume is why large systems go wide-column.) Store `chat`, `chat_participants`,
and `message(chat_id, seq, sender, body, type, status, ts)`.

## 6. Group chat & fan-out

A group message must reach all members. Small groups: fan out on write (deliver to each
member's connection/queue). Very large groups/channels: fan out on read or via the
pub/sub topic for the channel, to avoid write amplification. Name the **fan-out-on-write
vs fan-out-on-read** trade-off (same as news-feed design).

## 7. Presence (online / last-seen)

Clients send periodic **heartbeats**; the gateway updates a presence entry (Redis) with
a TTL. Missed heartbeats → mark offline. Broadcasting every presence change to large
groups is expensive — debounce/limit it. Presence is inelegant to make perfectly
accurate; eventual/approximate is acceptable.

## 8. Scaling & reliability

- **Connection servers scale horizontally**; the hard limit is concurrent sockets per
  box (tune OS limits) — many servers, each holding a slice of users.
- **Registry/pub-sub** must scale with connections; shard it.
- **Durability before delivery** — persist, then deliver, so a crash never loses a
  message; clients reconcile via history sync on reconnect.
- **Ordering** is per-conversation (a sequence per `chat_id`), not global — global
  ordering is unnecessary and expensive.
- End-to-end encryption if required (keys client-side; server routes ciphertext).

## Trade-offs to voice
- **WebSocket vs long-polling** — efficient/complex/stateful vs simple/wasteful.
- **Fan-out on write vs read** — fast reads/heavy writes vs cheap writes/heavy reads,
  chosen by group size.
- **Wide-column vs SQL** — write-scale + range reads vs relational convenience.
- **Delivery guarantees** — at-least-once + idempotency (practical) vs exactly-once
  (costly).
- **Presence accuracy vs cost** — precise real-time status is expensive; approximate is fine.
