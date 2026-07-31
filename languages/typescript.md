# TypeScript for interviews

TypeScript adds a **structural, compile-time** type system to JavaScript. Interviews
test whether you use it to make illegal states unrepresentable — not whether you can
recite syntax.

## Core model

- **Structural typing ("duck typing"):** compatibility is by *shape*, not by name.
  If an object has the required members, it fits — regardless of its declared type.
- **Types erase at compile time.** There are no runtime type checks; TS compiles to
  plain JS. Runtime validation (e.g. of API input) still needs actual checks.
- **`any` vs `unknown`:** `any` disables checking (avoid it). `unknown` is the safe
  top type — you must narrow it before use. Prefer `unknown` at boundaries.

## Types vs interfaces

- `interface` — for object/class shapes; supports declaration merging and `extends`.
- `type` — everything interfaces do *plus* unions, intersections, tuples, mapped and
  conditional types.
- Rule of thumb: `interface` for public object contracts, `type` for unions and
  composed/computed types. Both are fine; consistency matters more than the choice.

## Narrowing (the everyday skill)

The compiler narrows a union as you check it:
```ts
function len(x: string | string[]): number {
  if (typeof x === "string") return x.length;   // x: string here
  return x.length;                                // x: string[] here
}
```
Tools: `typeof`, `instanceof`, `in`, truthiness, equality, and custom **type
guards** (`x is Foo`).

## Discriminated unions (bring this up unprompted)

The idiomatic way to model "one of several shapes" safely:
```ts
type Result =
  | { status: "ok"; data: string }
  | { status: "error"; message: string };

function handle(r: Result) {
  switch (r.status) {
    case "ok": return r.data;         // narrowed
    case "error": return r.message;   // narrowed
  }
}
```
Add a `never`-typed default to get a **compile error if you forget a case** —
exhaustiveness checking, a favorite senior detail.

## Generics

Reusable, type-safe abstractions:
```ts
function first<T>(arr: T[]): T | undefined { return arr[0]; }
// Constraints:
function pluck<T, K extends keyof T>(obj: T, key: K): T[K] { return obj[key]; }
```
`extends` constrains a type parameter; `keyof`, indexed access `T[K]`, and
conditional types (`T extends U ? X : Y`) are the building blocks of advanced types.

## Utility types worth knowing

`Partial<T>`, `Required<T>`, `Readonly<T>`, `Pick<T,K>`, `Omit<T,K>`, `Record<K,V>`,
`Returntype<F>`, `Parameters<F>`, `Awaited<T>`, `NonNullable<T>`. Be able to say what
each does and, ideally, roughly how one is built with mapped types.

## Config & strictness

- Turn on **`strict`** (bundles `strictNullChecks`, `noImplicitAny`, etc.). Interviews
  assume strict mode; `strictNullChecks` is what forces you to handle `null`/`undefined`.
- Prefer precise types over `any`; use `unknown` + narrowing at untrusted boundaries.

## Common questions

- **`interface` vs `type`?** As above — interfaces merge/extend; types do unions and
  computed types.
- **`any` vs `unknown`?** `any` opts out of safety; `unknown` forces narrowing first.
- **How is TS structural?** Compatibility by shape, not declared name.
- **Do types exist at runtime?** No — they erase; validate runtime data yourself.
- **Model "loading | success | error" cleanly?** A discriminated union with a
  `status` tag and exhaustive `switch`.
- **`enum` vs union of string literals?** String-literal unions are lighter, erase
  fully, and are usually preferred over runtime `enum`s.

*Full legacy Q&A preserved in [`typescript-legacy-qa.md`](typescript-legacy-qa.md).*
