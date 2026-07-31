# Node.js

Node.js interviews revolve around one thing above all: **the event loop and the
async model.** If you can explain how a single-threaded runtime handles massive
concurrency, you've answered half the interview.

Module split:
- **This file** — runtime model + event loop.
- [`async-streams-events.md`](async-streams-events.md) — callbacks/promises/async, streams, buffers, EventEmitter.
- [`apis-and-express.md`](apis-and-express.md) — HTTP, Express, middleware, REST, auth, validation.
- [`production.md`](production.md) — scaling, performance, security, error handling, testing.
- [`nodejs-legacy/`](nodejs-legacy/) — the original 400-question set (reference, pending review).

## What Node.js is

Node is a JavaScript runtime built on Chrome's **V8** engine plus **libuv**, which
provides the event loop and a thread pool for async I/O. Its model is
**single-threaded, non-blocking, event-driven** — one thread runs your JS, while I/O
is delegated and completions are handled via callbacks.

## Why single-threaded can handle huge concurrency

Traditional thread-per-request servers spend most threads *blocked* waiting on I/O
(DB, network, disk). Node instead **never blocks** the main thread: it kicks off the
I/O, keeps processing other requests, and runs your callback when the I/O completes.
For I/O-bound workloads (most web services) this is extremely efficient with tiny
memory overhead. The flip side: **CPU-bound work blocks everyone** (see below).

## The event loop (know the phases)

After the main script runs, libuv cycles through phases repeatedly:

1. **timers** — `setTimeout` / `setInterval` callbacks whose time has elapsed.
2. **pending callbacks** — some deferred system callbacks.
3. **poll** — retrieve new I/O events; execute I/O callbacks (the loop spends most
   time here).
4. **check** — `setImmediate` callbacks.
5. **close** — close callbacks (e.g. socket close).

**Between each phase (and after each callback), Node drains the microtask queues:**
`process.nextTick` first, then Promise callbacks. This ordering is a favorite question:

```js
console.log("1");
setTimeout(() => console.log("2"));        // timers phase (macrotask)
setImmediate(() => console.log("3"));      // check phase (macrotask)
Promise.resolve().then(() => console.log("4"));  // microtask
process.nextTick(() => console.log("5"));  // runs before other microtasks
console.log("6");
// 1, 6, 5, 4, then 2/3 (2 and 3 order can vary by context)
```

Key takeaways to say out loud: sync code runs first; **`process.nextTick` beats
Promises**; both microtask queues fully drain before the loop moves to the next
macrotask phase.

## The libuv thread pool

Some operations aren't truly async at the OS level (file system, DNS, crypto,
compression). libuv runs these on a small **thread pool** (default 4, tunable via
`UV_THREADPOOL_SIZE`) and calls back when done. So Node isn't *purely* single-threaded
— your JS is, but I/O uses threads under the hood.

## The CPU-bound trap (senior insight)

A heavy synchronous computation (big loop, sync crypto, JSON on a huge payload)
**blocks the event loop**, so every other request stalls. Fixes:
- Offload to **worker threads** (`worker_threads`) for CPU work.
- Use the **cluster** module / multiple processes to use all cores.
- Break work into chunks or move it to a queue/background service.
This is the #1 way naive Node services fall over — name it unprompted.

## Modules: CommonJS vs ES Modules

- **CommonJS** (`require`/`module.exports`) — original Node system, synchronous
  loading.
- **ES Modules** (`import`/`export`) — the standard, now well-supported; async,
  statically analyzable. New projects use ESM (`"type": "module"`).
- Know that you can't `require` an ESM module directly and that `__dirname` isn't
  available in ESM (use `import.meta.url`).

## Common questions

- **Is Node single-threaded?** Your JS runs on one thread; libuv uses a thread pool
  for some I/O, and you can add worker threads/processes for CPU parallelism.
- **`setTimeout` vs `setImmediate` vs `process.nextTick`?** Timers phase vs check
  phase vs "immediately after the current operation, before other microtasks."
- **Why is Node good for I/O-bound but not CPU-bound work?** Non-blocking I/O vs a
  single JS thread that CPU work monopolizes.
- **How does Node achieve concurrency without threads per request?** The event loop +
  non-blocking I/O + callbacks/promises.
