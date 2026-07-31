# JavaScript for interviews

JavaScript interviews are really about four things: **closures, `this`, the
prototype chain, and the event loop.** Nail those and the rest follows.

## Scope, hoisting & closures

- **`var`** is function-scoped and hoisted (initialized to `undefined`); **`let`/
  `const`** are block-scoped and in a "temporal dead zone" until declared. Use
  `const` by default, `let` when reassigning, never `var`.
- **Closure:** a function retains access to its lexical scope even after the outer
  function has returned. It's the basis of data privacy, callbacks, and hooks.
```js
function counter() {
  let n = 0;                 // captured by the returned closure
  return () => ++n;
}
const next = counter();
next(); next();              // 1, 2  — `n` lives on
```
- **Classic loop bug:** `var` in a loop shares one binding, so async callbacks all
  see the final value. `let` creates a fresh binding per iteration — the fix.

## `this`

`this` is determined by **how a function is called**, not where it's defined:
- Plain call → `undefined` (strict) or global object.
- Method call `obj.fn()` → `obj`.
- `call`/`apply`/`bind` → explicitly set.
- `new` → the newly created object.
- **Arrow functions** have no own `this`; they capture it lexically from the
  enclosing scope. That's why arrows are used for callbacks that need the outer
  `this` — and why you must *not* use them as object methods that rely on `this`.

## Prototypes

- Every object has an internal link to a **prototype**; property lookups walk the
  **prototype chain** until found or `null`.
- `class` is syntactic sugar over prototypes — know that under the hood it's still
  prototypal inheritance.

## The event loop (the senior differentiator)

JS is single-threaded. Concurrency comes from the event loop:
1. Run the current synchronous **call stack** to completion.
2. Drain **all microtasks** (Promise callbacks, `queueMicrotask`).
3. Take **one macrotask** (timers, I/O, events), then drain microtasks again. Repeat.

**Microtasks beat macrotasks**, so:
```js
console.log(1);
setTimeout(() => console.log(2));      // macrotask
Promise.resolve().then(() => console.log(3));  // microtask
console.log(4);
// Order: 1, 4, 3, 2
```
This ordering question comes up constantly.

## Promises & async/await

- A Promise is a value that resolves/rejects later. `async/await` is syntactic sugar
  over promises; `await` pauses the async function without blocking the thread.
- Run independent async work **in parallel** with `Promise.all` (fails fast) or
  `Promise.allSettled` (waits for all) — not sequential `await`s, a common perf miss.
- Always handle rejections (`try/catch` around `await`, or `.catch`).

## Coercion & equality

- `===` compares type + value with no coercion; `==` coerces and has surprising
  rules. **Use `===`.**
- Falsy values to memorize: `false`, `0`, `""`, `null`, `undefined`, `NaN`.
- `null == undefined` is `true`, but `null === undefined` is `false`.

## Modern JS you should use

- Destructuring, spread/rest (`...`), template literals, optional chaining `?.`,
  nullish coalescing `??` (differs from `||`: only `null`/`undefined` trigger it),
  default params, ES modules (`import`/`export`).
- `map`/`filter`/`reduce` over manual loops for clarity.

## Common questions

- **Explain closures with a real use.** Private state / memoization / event handlers.
- **`==` vs `===`?** Coercion vs strict; always `===`.
- **What logs first, a Promise or a `setTimeout`?** The Promise — microtasks run
  before the next macrotask.
- **`null` vs `undefined`?** `undefined` = not assigned; `null` = intentional "no value."
- **Debounce vs throttle?** Debounce waits for a pause; throttle caps rate. Be ready
  to implement both with closures + timers.
- **Deep vs shallow copy?** `{...obj}`/`Object.assign` are shallow; use
  `structuredClone(obj)` for deep.

*Full legacy Q&A preserved in [`javascript-legacy-qa.md`](javascript-legacy-qa.md).*
