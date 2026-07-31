# Async, streams & events in Node

The patterns that make Node's non-blocking model usable: how you write async code,
how you process data without loading it all into memory, and the event system the
whole platform is built on.

## The evolution of async (know all three)

1. **Callbacks** — the original. Lead to "callback hell" (deep nesting) and awkward
   error handling (error-first `(err, data)` convention).
2. **Promises** — a value available later; chainable with `.then`/`.catch`, flattening
   nesting.
3. **async/await** — syntactic sugar over promises; reads like synchronous code while
   staying non-blocking. The modern default.

```js
// Error handling with async/await
async function getUser(id) {
  try {
    const user = await db.findUser(id);
    return user;
  } catch (err) {
    logger.error(err);
    throw err;                 // rethrow or handle — never swallow silently
  }
}
```

## Run async work in parallel

A common performance miss is awaiting independent calls sequentially:

```js
// Slow — sequential
const a = await fetchA();
const b = await fetchB();

// Fast — parallel
const [a, b] = await Promise.all([fetchA(), fetchB()]);
```

Use `Promise.all` (fail-fast) or `Promise.allSettled` (wait for all, collect
results/errors) when calls don't depend on each other.

## Unhandled rejections

An unhandled promise rejection can crash the process (in modern Node). Always attach
a `.catch`/`try-catch`, and add a process-level `unhandledRejection` handler as a
backstop for logging.

## Streams (the memory-efficiency topic)

Streams process data in **chunks** instead of loading it all into memory — essential
for large files, network data, and pipelines. Four types: **Readable**, **Writable**,
**Duplex**, **Transform**.

```js
const { pipeline } = require("node:stream/promises");
const fs = require("node:fs");
const zlib = require("node:zlib");

// Stream a file through gzip to a new file — constant memory, backpressure handled
await pipeline(
  fs.createReadStream("big.log"),
  zlib.createGzip(),
  fs.createWriteStream("big.log.gz"),
);
```

- **Backpressure** — when a fast producer outpaces a slow consumer, streams pause the
  source so memory doesn't balloon. Use `pipeline`/`pipe` and they handle it for you;
  hand-rolling `data` events without backpressure is a classic bug.
- The interview line: "read a 10 GB file" → **stream it**, never `fs.readFile`.

## Buffers

`Buffer` holds raw binary data outside V8's heap — for file/network bytes, encoding
conversions, and binary protocols. Know that strings have encodings (`utf-8`,
`base64`, `hex`) and buffers are how Node handles bytes.

## EventEmitter

Node's core pub/sub primitive; many built-ins (streams, HTTP servers) are emitters.

```js
const { EventEmitter } = require("node:events");
const bus = new EventEmitter();
bus.on("order", (o) => process(o));   // subscribe
bus.emit("order", order);             // publish
```

Watch for memory leaks from listeners you never remove (the "possible EventEmitter
memory leak" warning) — remove listeners you no longer need.

## Common questions

- **Callback hell — how to avoid?** Promises + async/await, or named functions.
- **Read a huge file without exhausting memory?** Streams with backpressure.
- **`Promise.all` vs `Promise.allSettled`?** Fail-fast vs wait-for-all-and-report.
- **What is backpressure?** Flow control so a slow consumer doesn't get overwhelmed.
- **Where are EventEmitters used?** Streams, HTTP servers, process — the core async
  event mechanism.
