# Design a notification system

Deliver notifications across **push, email, and SMS** at scale, reliably, without
spamming users. The interview is about **decoupling, reliable delivery, dedup, and
respecting user preferences** — not the individual channel APIs.

## 1. Requirements

**Functional:** multiple channels (push via APNs/FCM, email via SES/SendGrid, SMS via
Twilio); templates with variable substitution; per-user **preferences / opt-out /
quiet hours**; delivery tracking; priority (a 2FA code beats a marketing blast).
**Non-functional:** **highly available**, scale to billions/day, **reliable delivery**
(at-least-once), low latency for high-priority, cost-aware (SMS is expensive).

## 2. Why a queue is the backbone

Callers (services that want to notify) must not block on third-party providers that are
slow or flaky. So the flow is **decoupled through a queue**:

```
producers → Notification API → [validate, dedup, apply prefs, render template]
          → per-channel queues → channel workers → provider (APNs/FCM/SES/Twilio)
          → delivery status ← webhooks
```

The queue smooths spikes, enables retries, and isolates a failing channel from the
rest. Use **priority queues** (or separate high/low queues) so transactional
notifications jump ahead of bulk ones.

## 3. The pieces and why each exists

- **Ingestion/API** — accept a notification request (`user, template, data, channels,
  priority`), validate, and enqueue fast.
- **Preference service** — check opt-outs, channel choice, and **quiet hours/DND**
  *before* sending. Skipping this is how products get reported as spam.
- **Template service** — versioned templates + variable substitution + localization;
  cache compiled templates.
- **Channel workers** — one per channel, each an **adapter** over a provider; they own
  provider-specific auth, formatting, and rate limits.
- **Tracking/analytics** — consume provider **webhooks** (delivered/bounced/opened) to
  update status and metrics.

## 4. Reliable delivery (the senior details)

- **At-least-once + idempotency/dedup.** Retries and duplicate upstream events mean the
  same notification can be requested twice — dedup on a **notification key** so a user
  isn't paged twice. Exactly-once is impractical across third parties; at-least-once +
  dedup is the pragmatic target.
- **Retries with exponential backoff + jitter**, then a **dead-letter queue** for
  messages that keep failing (for inspection/alerting), so one bad message doesn't
  block the queue.
- **Rate limiting / throttling per user** — cap notifications per user per window so a
  buggy producer can't spam someone (cross-ref [`rate-limiter.md`](rate-limiter.md)).
- **Provider failover** — a secondary provider per channel for resilience.

## 5. Scaling

- Channel workers scale independently on their queues (SMS workers ≠ push workers).
- Shard by user id; batch where providers support it (email/push batch sends).
- Precompute/cache preferences and templates; the hot path should be mostly queue I/O.

## Trade-offs to voice
- **At-least-once vs exactly-once** — practical (dedup) vs impractical across external
  providers.
- **Sync vs async** — always async via the queue; the caller shouldn't wait on a
  provider.
- **Priority separation** — dedicated high-priority path vs one queue (2FA must not sit
  behind a marketing batch).
- **Push vs pull for in-app** — server push vs client polls its notification inbox.
- **Cost vs reach** — SMS reliable but pricey; push cheap but requires app + opt-in.
