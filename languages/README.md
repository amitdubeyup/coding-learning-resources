# Languages

Language-depth prep. Interviews use these to check that you understand the runtime
model — not just syntax — so each guide leads with the mental model and the gotchas
interviewers actually probe.

## Guides
- [`python.md`](python.md) — data model, the GIL & concurrency, generators,
  decorators, memory, typing.
- [`javascript.md`](javascript.md) — closures, `this`, prototypes, the event loop,
  promises/async, coercion.
- [`typescript.md`](typescript.md) — structural typing, narrowing, discriminated
  unions, generics, utility types.

Legacy long-form Q&A is preserved alongside each (`*-legacy-qa.md`) pending review.

## What interviewers test per language
- **Python:** "explain the GIL," mutable-default-arg, generators for memory,
  decorators, `is` vs `==`.
- **JavaScript:** closures, what `this` binds to, microtask-vs-macrotask ordering,
  `==` vs `===`.
- **TypeScript:** `any` vs `unknown`, `interface` vs `type`, modelling state with
  discriminated unions, generic constraints.

## Cross-references
- Async/event-loop concepts recur in [`../backend/`](../backend/) *(pending reorg)*.
- Language choice also shows up in [`../dsa/`](../dsa/) — pick the language you're
  fastest and cleanest in for the coding round.
