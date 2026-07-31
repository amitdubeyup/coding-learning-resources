# Advanced & modern React

State management, React 19's Actions model, Server Components, Suspense/concurrent,
rendering strategies, testing, and patterns — the topics that separate a 2020 answer
from a current one.

## State management: pick the smallest tool that works

A senior answer is a decision tree, not "use Redux":

1. **Local state** (`useState`/`useReducer`) — default. Most state is local.
2. **Lift state up** — when a few nearby components need to share it.
3. **Context** — for low-frequency global values (theme, current user, locale).
   Not a general state manager: every consumer re-renders on change.
4. **A dedicated library** — only when you have complex, high-frequency, widely-shared
   client state. Lightweight stores (e.g. Zustand/Jotai) are now often preferred over
   Redux for their smaller boilerplate; Redux Toolkit remains common in large apps.
5. **Server state is different.** Data from an API is not really "state" you own —
   use a data-fetching/caching library (React Query/SWR-style) that handles caching,
   revalidation, and loading/error status. Don't hand-roll this in `useEffect`.

The most common mistake: reaching for a global store when local state or a
server-cache library would do. Match the tool to the *kind* of state.

## Data fetching, the modern way

- **Client components:** prefer a caching library over raw `useEffect` fetches — you
  get dedup, caching, retries, and stale-while-revalidate for free, and you avoid the
  race conditions and waterfalls of manual effects.
- **The `use()` API** can read a promise directly during render and suspend until it
  resolves — handy for passing a fetch promise down and unwrapping it under a Suspense
  boundary.
- **Server-first frameworks** (below): fetch on the server, stream HTML, and hydrate —
  less client JS and better first-load.

## React 19: Actions & the new hooks

The headline React 19 feature. An **Action** is an async function wired into React's
transition system so pending state, errors, and optimistic updates are handled *for*
you — collapsing the old "five hooks glued together" form pattern.

```jsx
import { useActionState } from "react";

function EditName({ save }) {
  const [error, submitAction, isPending] = useActionState(
    async (_prev, formData) => {
      const res = await save(formData.get("name"));
      return res.ok ? null : "Save failed";
    },
    null,
  );

  return (
    <form action={submitAction}>       {/* pass the Action straight to <form> */}
      <input name="name" />
      <button disabled={isPending}>Save</button>
      {error && <p role="alert">{error}</p>}
    </form>
  );
}
```

The supporting cast:
- **`<form action={fn}>`** — react-dom submits the form through your Action (and resets
  uncontrolled fields on success).
- **`useActionState`** — `[state, dispatch, isPending]`; folds pending/error/result into
  one hook.
- **`useFormStatus`** — a child (e.g. a submit button in a design system) reads the
  parent form's pending status without prop-drilling.
- **`useOptimistic`** — render the expected result immediately; React reverts it if the
  Action fails.

Also in React 19: **`ref` as a normal prop** (no more `forwardRef`), and **native
document metadata** (`<title>`/`<meta>`/`<link>` render anywhere and hoist to `<head>`).

> Performance note: React 19's **compiler** auto-memoizes, so most `useMemo`/
> `useCallback`/`memo` disappears from new code — see
> [`rendering-and-performance.md`](rendering-and-performance.md).

## Server Components & the current model

- **React Server Components (RSC):** components that render on the **server**, never
  ship their JS to the client, and can access server resources (DB, filesystem)
  directly. They cut bundle size and move data-fetching server-side. **Stable in
  React 19.**
- **Client Components** (`"use client"`) are the interactive ones with hooks and event
  handlers. A real app interleaves both: server components for data/shell, client
  components for interactivity.
- **Server Actions** (`"use server"`) let client code call server functions for
  mutations without you hand-writing an API endpoint — and they plug into the same
  Actions/`useActionState` machinery above.
- Delivered mainly through frameworks (Next.js App Router, React Router 7+, TanStack
  Start); know the *concepts* even if the interview doesn't name a framework.

## Suspense & concurrent features

- **`<Suspense fallback>`** lets a subtree "wait" for something (lazy code, a promise
  read via `use()`, data) and show a fallback meanwhile — enabling streaming and
  coordinated loading states. React 19 improved streaming hydration (fewer mismatches,
  faster interactivity).
- **Concurrent rendering** lets React interrupt/prioritize work. `useTransition` keeps
  urgent input responsive while a heavy update renders in the background;
  `useDeferredValue` defers expensive derived UI.

## Rendering strategies (know the trade-offs)

| Strategy | When rendered | Best for | Trade-off |
|---|---|---|---|
| **CSR** (client) | in the browser | highly interactive apps, dashboards | slow first paint, weak SEO |
| **SSR** (server, per request) | on each request | dynamic, personalized, SEO-sensitive pages | server cost/latency per request |
| **SSG** (static) | at build time | mostly-static content (docs, blogs) | rebuild needed for changes |
| **ISR** (incremental static) | build + revalidate on a schedule | large mostly-static sites needing periodic freshness | slight staleness window |

The interview answer is always "it depends on interactivity, SEO, and how often the
data changes" — then pick per route, not per app.

## Error boundaries

Class components (or a library wrapper) that catch render-time errors in their subtree
via `getDerivedStateFromError`/`componentDidCatch` and show a fallback. They do **not**
catch errors in event handlers or async code — handle those with try/catch (Actions
route their errors to the nearest boundary automatically). Place boundaries around
risky subtrees so one failure doesn't blank the whole app.

## Testing

- **React Testing Library** is the standard: test behavior the user sees (query by
  role/text, fire events, assert output), **not** implementation details.
- Mock network at the boundary (e.g. a request-mocking layer), not internal functions.
- Add end-to-end tests (Playwright/Cypress) for critical flows.
- The philosophy to state: "test what the user experiences, so refactors don't break
  tests."

## Patterns worth naming

- **Custom hooks** — the primary logic-reuse mechanism (replaced most HOC/render-prop
  usage).
- **Compound components** — related components sharing implicit state via context
  (e.g. `<Tabs><Tab/></Tabs>`), for flexible, expressive APIs.
- **Container/presentational** — separate data-fetching from rendering; less rigid now
  that hooks and Server Components exist, but still a useful mental split.
- **Controlled vs uncontrolled** — see the core module.

## Common questions

- **Redux — still needed?** Often not. Local state + context + a server-cache library
  cover most apps; reach for a global store only for genuinely complex shared client
  state.
- **RSC vs SSR?** SSR renders client components to HTML on the server then hydrates;
  RSC components render on the server and **never** ship to the client at all. Different
  goals: hydration vs zero client JS.
- **What are Actions / `useActionState`?** React 19's built-in way to handle async
  mutations (esp. forms) with automatic pending, error, and optimistic state.
- **Suspense — what problem does it solve?** Declarative loading/streaming boundaries
  instead of scattered `isLoading` flags.
- **`use()` vs `useEffect`+`useState` for a promise?** `use()` reads the promise during
  render and suspends — no effect, no loading flag, and it can be called conditionally.
- **Prevent a fetch waterfall?** Fetch in parallel / hoist fetching to the server / use
  a caching library that dedupes and parallelizes.
