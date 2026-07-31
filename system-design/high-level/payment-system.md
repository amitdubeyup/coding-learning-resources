# Design a payment system

Money is unforgiving: the bar is **correctness first, performance second**. The
interview rewards the concepts that keep money from being lost or duplicated —
idempotency, a ledger, strong consistency, and PCI handling — far more than raw scale.

## 1. Requirements

**Functional:** charge a payment method; support cards, wallets, bank transfers;
refunds and disputes; transaction history. **Non-functional:** **strong consistency &
correctness** (no double-charge, no lost money — never eventual consistency for
balances), very **high availability**, auditable, and **PCI-DSS compliant**.

## 2. Idempotency — the #1 payment concept

Networks retry. A client (or your own retry logic) can send the same "charge $50"
request twice; without protection you **double-charge**. The fix: the client sends an
**idempotency key** with each payment request; the server records it, and any repeat
with the same key returns the **original result** instead of charging again. Say this
first — it's the point interviewers most want to hear.

## 3. Never touch raw card data — tokenize (PCI)

Storing raw card numbers (PAN) drags your whole system into **PCI-DSS** scope and is a
huge liability. Instead, the card is sent directly to a **payment gateway / PSP**
(Stripe/Adyen/Braintree) which returns a **token**; you store the token, not the card.
Your system references the token to charge. This keeps card data out of your servers.

## 4. The payment state machine + ledger

Model a payment as an explicit **state machine**, not a boolean:
`initiated → authorized → captured → settled`, with `failed` / `refunded` /
`disputed` branches. Each transition is recorded.

Record money movements in a **double-entry ledger** — an **immutable, append-only**
record where every transaction is balanced (a debit and a matching credit). You never
*update* a balance in place; you append entries and derive balances. This gives you
auditability, correctness, and a natural way to handle refunds/reversals. Mentioning
the ledger is a strong senior signal most candidates omit.

## 5. Consistency & reliable side effects

- Use a **transactional (ACID) store** for the ledger and transaction records — this is
  the canonical case where you **do not** trade away strong consistency.
- Payment touches multiple systems (ledger, PSP, order service, notifications).
  Coordinate with a **saga** (a sequence of steps with compensating actions on failure)
  rather than a distributed 2PC, and publish events reliably with the **outbox
  pattern** (write the event in the same DB transaction as the state change, then a
  relay publishes it) so you never "charged but forgot to tell the order service."

## 6. The flow

1. Client tokenizes the card with the PSP → gets a token.
2. Client calls your payment API with token + amount + **idempotency key**.
3. Server checks the idempotency key (dedup), runs a **fraud/risk check**, records the
   payment as `initiated` in the ledger transaction.
4. Server calls the PSP to **authorize** then **capture** (with its own idempotency
   toward the PSP); update state; append ledger entries — **atomically**.
5. **Settlement** (moving funds) happens asynchronously; a background job reconciles.
6. Emit a `payment.succeeded` event via the outbox for downstream services.

## 7. Reconciliation

Your records and the PSP's/bank's must agree. A scheduled **reconciliation** job
compares your ledger against provider settlement reports and flags mismatches
(missed webhooks, partial failures). This catches the money bugs that slip through
in real time.

## 8. Scaling & availability

- Availability target is very high (99.99%+), but **correctness dominates** — favor
  consistency in CAP for the ledger path.
- Partition by account/merchant; keep the ledger's integrity within a partition.
- Multiple PSPs for redundancy and routing (cost/geography), behind a gateway adapter.

## Trade-offs to voice
- **Strong consistency (mandatory here) vs availability/latency** — money can't be
  eventually consistent.
- **In-house vs PSP** — control/fees vs offloading PCI scope and card handling (almost
  always use a PSP).
- **Saga/outbox vs distributed 2PC** — resilient, eventually-consistent-across-services
  with compensation vs brittle lock-heavy 2PC.
- **Sync authorize+capture vs async settlement** — immediate user feedback vs funds
  moving on the banking network's schedule.
