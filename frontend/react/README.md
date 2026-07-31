# React

React interviews test three things: do you understand **how React renders**, do
you use **hooks correctly**, and can you reason about **performance and modern
patterns**. This module is split accordingly:

- **This file** — core model + hooks.
- [`rendering-and-performance.md`](rendering-and-performance.md) — reconciliation, re-renders, memoization, perf.
- [`advanced-and-modern.md`](advanced-and-modern.md) — state management, Server Components, Suspense, SSR/CSR/SSG/ISR, testing, patterns.
- [`react-legacy-qa.md`](react-legacy-qa.md) — the original long-form Q&A (kept for reference, pending review).

Modern React = **function components + hooks**. Class components still work but are
legacy for new code; know their lifecycle only well enough to translate it to hooks.

## The mental model

- **JSX** is syntactic sugar for `React.createElement(...)`; it compiles to plain
  function calls that return element objects (a description of UI, not the UI itself).
- React builds a tree of elements, diffs it against the previous tree
  (**reconciliation**), and commits the minimal set of real-DOM changes. Details in
  [`rendering-and-performance.md`](rendering-and-performance.md).
- **UI = f(state).** You describe what the UI should look like for a given state;
  React figures out the DOM operations. You almost never touch the DOM directly.
- **One-way data flow:** data flows down via props; changes flow up via callbacks.

## State vs props

- **Props** are read-only inputs passed from parent to child.
- **State** is data a component owns and can change; updating it triggers a re-render.
- **Never mutate** state or props. Create new objects/arrays:
  `setItems([...items, next])`, not `items.push(next)`. React detects changes by
  reference, so mutation makes updates "invisible" and causes stale-UI bugs.

## The hooks you must know cold

### `useState`
```jsx
const [count, setCount] = useState(0);
// Functional update when the next value depends on the previous one:
setCount(c => c + 1);
```
Use the functional form inside async callbacks or when batching multiple updates —
reading `count` directly can be stale.

### `useEffect`
Runs side effects (subscriptions, fetches, manual DOM work) *after* render.
```jsx
useEffect(() => {
  const id = setInterval(tick, 1000);
  return () => clearInterval(id);   // cleanup runs before re-run and on unmount
}, [deps]);                          // effect re-runs when a dep changes
```
- `[]` → run once on mount. No array → run after *every* render (usually a bug).
- The **dependency array must list every reactive value the effect uses.** Missing
  deps cause stale closures; the `eslint-plugin-react-hooks` exhaustive-deps rule
  catches these.
- **Don't overuse effects.** Data derived from props/state should be computed during
  render, not synced via an effect. Effects are for *external* systems.

### `useRef`
A mutable box that persists across renders **without** causing a re-render. Two uses:
holding a DOM node (`ref={myRef}`) and storing mutable values (timers, previous
values, instance-like data).

### `useMemo` / `useCallback`
Memoize an expensive computed value / a stable function identity across renders.
Use them to prevent needless work or re-renders — **not by default**. Covered in
[`rendering-and-performance.md`](rendering-and-performance.md).

### `useContext`
Read a context value without prop-drilling. Every consumer re-renders when the
context value changes — so keep context values stable and split contexts by concern.

### `useReducer`
For complex state with multiple sub-values or interdependent transitions:
```jsx
const [state, dispatch] = useReducer(reducer, initialState);
dispatch({ type: "increment" });
```
Prefer it over multiple `useState`s when updates are logically grouped.

### Custom hooks
Extract reusable stateful logic into a `useSomething()` function that calls other
hooks. This — not render props or HOCs — is the modern way to share logic.
```jsx
function useDebounced(value, ms) {
  const [v, setV] = useState(value);
  useEffect(() => {
    const id = setTimeout(() => setV(value), ms);
    return () => clearTimeout(id);
  }, [value, ms]);
  return v;
}
```

## Rules of hooks (a guaranteed question)

1. **Only call hooks at the top level** — never inside conditions, loops, or nested
   functions. React tracks hooks *by call order*, so the order must be identical
   every render.
2. **Only call hooks from React function components or other custom hooks.**

Break rule 1 and you get the classic "rendered more/fewer hooks than expected" crash.

## Keys (small topic, frequent question)

When rendering a list, give each item a **stable, unique `key`** so React can match
elements across renders. Never use the array index as a key for lists that reorder,
insert, or delete — it causes wrong state/DOM reuse. Use a stable id from the data.

## Controlled vs uncontrolled inputs

- **Controlled:** value lives in React state (`value={x} onChange={...}`). Predictable,
  the default choice.
- **Uncontrolled:** the DOM holds the value; you read it via a ref. Handy for simple
  or performance-sensitive forms and file inputs.

## Quick-fire answers

- **Why keys?** Stable identity for efficient, correct list reconciliation.
- **Why does my effect run twice in dev?** React 18+ Strict Mode intentionally
  double-invokes effects in development to surface missing cleanup. It doesn't happen
  in production.
- **`useEffect` vs `useLayoutEffect`?** `useLayoutEffect` fires synchronously after
  DOM mutations, before paint — use it only when you must measure/adjust layout to
  avoid a flicker; otherwise `useEffect`.
- **How to share logic between components?** Custom hooks.
