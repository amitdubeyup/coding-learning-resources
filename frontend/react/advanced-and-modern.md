# Advanced & modern React

State management, the modern React model (Server Components, Suspense, concurrent),
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
- **Server-first frameworks** (see below): fetch on the server, stream HTML, and
  hydrate — less client JS and better first-load.

## Server Components & the current model

- **React Server Components (RSC):** components that render on the **server**, never
  ship their JS to the client, and can access server resources (DB, filesystem)
  directly. They reduce bundle size and move data-fetching to the server.
- **Client Components** (`"use client"`) are the interactive ones with hooks and event
  handlers. A real app interleaves both: server components for data/shell, client
  components for interactivity.
- **Server Actions** let client code call server functions for mutations without you
  hand-writing an API endpoint.
- This model is delivered mainly through frameworks (Next.js App Router and similar);
  know the *concepts* even if the interview doesn't name a framework.

## Suspense & concurrent features

- **`<Suspense fallback>`** lets a subtree "wait" for something (lazy code, data) and
  show a fallback meanwhile — enabling streaming and coordinated loading states.
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
via `getDerivedStateFromError`/`componentDidCatch` and show a fallback. Note they do
**not** catch errors in event handlers or async code — handle those with try/catch.
Place boundaries around risky subtrees so one failure doesn't blank the whole app.

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
  that hooks exist, but still a useful mental split.
- **Controlled vs uncontrolled** — see the core module.

## Common questions

- **Redux — still needed?** Often not. Local state + context + a server-cache library
  cover most apps; reach for a global store only for genuinely complex shared client
  state.
- **RSC vs SSR?** SSR renders client components to HTML on the server then hydrates;
  RSC components render on the server and **never** ship to the client at all. Different
  goals: hydration vs zero client JS.
- **Suspense — what problem does it solve?** Declarative loading/streaming boundaries
  instead of scattered `isLoading` flags.
- **Prevent an effect from causing a fetch waterfall?** Fetch in parallel / hoist
  fetching to the server / use a caching library that dedupes and parallelizes.
