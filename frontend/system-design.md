# Frontend system design

Senior/staff frontend loops now include a dedicated **frontend system-design** round.
It is *not* backend HLD — the constraints are the **browser, the network, the device,
and the user's perception of speed**. You're scored on component architecture, state
and data flow, performance, accessibility, and — above all — the trade-offs between
them. Drive it with a framework the same way you'd drive an HLD.

## The framework (drive the conversation)

1. **Requirements** — functional (features) and **non-functional**: a performance
   budget, target devices/connections, accessibility, internationalization, offline,
   SEO. Pin scope to 2–3 core features.
2. **Data & API contract** — what the backend exposes (REST/GraphQL), the shape of
   list/detail responses, and the pagination model. The API shape drives the UI.
3. **Component architecture** — the component tree, boundaries, and what's reusable.
4. **State** — *what* state exists, *where* it lives, and how it flows.
5. **Data fetching & caching** — loading/error states, dedup, revalidation, optimistic
   updates.
6. **Rendering strategy** — CSR / SSR / SSG / streaming (see
   [`react/advanced-and-modern.md`](react/advanced-and-modern.md)).
7. **Performance** — bundle size, list virtualization, images, Core Web Vitals.
8. **Accessibility** — semantics, keyboard, focus, ARIA (increasingly scored).
9. **Edge cases & failure** — empty, error, slow network, offline, huge lists.

## Building blocks

### Component architecture
Favor **composition over configuration** — a component with fifteen boolean props is a
smell; compose small pieces instead. Know **presentational vs container** split,
**compound components** (`<Tabs><Tab/></Tabs>` sharing state via context) for flexible
APIs, and controlled vs uncontrolled inputs. Design components around a clear boundary:
what they own vs what they receive.

### State — put it in the smallest place that works
A senior answer is a decision tree, not "Redux": local (`useState`) → lifted to a
common parent → **context** for low-frequency global values (theme, user, locale) →
a **store** (Zustand/Jotai/Redux Toolkit) only for complex, high-frequency shared
client state → and crucially, **server state is not client state** — cache it with a
data library (React Query/SWR). Keep state minimal and **derive** the rest during
render; duplicated/denormalized state is where bugs live.

### Data fetching & caching
- **REST vs GraphQL:** GraphQL lets the client request exactly what it needs (kills
  over/under-fetching) at the cost of server complexity and caching difficulty; REST is
  simpler and HTTP-cacheable.
- **Caching + stale-while-revalidate:** show cached data instantly, revalidate in the
  background. A caching library also gives you request **dedup** and retries for free.
- **Pagination:** **cursor**-based for infinite scroll and real-time lists (stable when
  items are inserted/removed); **offset** only for fixed, page-numbered tables (it
  double-counts/skips when the list shifts).
- **Race conditions:** cancel stale in-flight requests (`AbortController`) so a slow
  earlier response can't overwrite a newer one — the classic typeahead bug.
- **Optimistic updates:** reflect the change immediately, reconcile/rollback on failure.
- **Normalization:** store shared entities once (by id) so a like/edit updates
  everywhere.

### Rendering strategy
CSR (interactive apps, weak SEO/first paint), SSR (dynamic + SEO, server cost), SSG
(static content), ISR (static + periodic refresh), streaming SSR (fast first paint +
progressive hydration). Choose **per route**, not per app. Full treatment in
[`react/advanced-and-modern.md`](react/advanced-and-modern.md).

### Performance — the heart of the FE-SD round
- **Ship less JavaScript:** code-split by route (`lazy` + `Suspense`), tree-shake, and
  analyze the bundle. JS is the most expensive resource on mobile.
- **Rendering perf:** **virtualize/window** long lists so the DOM holds only visible
  rows (the single biggest win for feeds/tables); avoid needless re-renders (React 19's
  compiler auto-memoizes — see [`react/rendering-and-performance.md`](react/rendering-and-performance.md));
  **debounce/throttle** high-frequency handlers (input, scroll, resize).
- **Images/media:** responsive `srcset`, lazy-load offscreen images, modern formats
  (AVIF/WebP), serve via CDN. Images are usually the largest bytes on a page.
- **Network:** prefetch likely-next routes/data, use HTTP caching + compression + a CDN,
  and resource hints (`preconnect`, `preload`).
- **Core Web Vitals** (know all three): **LCP** (largest contentful paint — loading),
  **INP** (Interaction to Next Paint — responsiveness, which *replaced FID in 2024*),
  and **CLS** (cumulative layout shift — visual stability). Be able to say what moves
  each (LCP: image/render-blocking resources; INP: long tasks/main-thread work; CLS:
  unsized media/late-injected content).
- **Perceived performance:** skeletons, streaming, and optimistic UI make an app *feel*
  fast even when the network isn't.

### Real-time
Pick by direction and frequency: **polling** (simple, wasteful) → **long-polling** →
**SSE** (server→client only, simple, auto-reconnect) → **WebSocket** (bidirectional,
for chat/collaboration). Don't reach for WebSockets when SSE or polling suffices.

### Accessibility (a scored dimension now)
Semantic HTML first (`<button>`, `<nav>`, headings) — it gives you keyboard and
screen-reader behavior for free. Add **ARIA only when semantics fall short**. Ensure
keyboard navigation with a **visible focus** indicator, manage focus in SPAs and modals
(trap focus, restore it on close), meet color-contrast minimums, and label controls.
State this proactively — most candidates forget it entirely.

### Offline & resilience
Service workers + the Cache API for offline-first; background sync for queued writes;
optimistic writes reconciled when back online. Plus i18n/l10n, theming via **design
tokens**, and browser security (XSS/CSP — see
[`../backend/web-security.md`](../backend/web-security.md)).

## Worked examples

### Typeahead / autocomplete
The canonical FE-SD problem. Requirements: suggestions as you type, keyboard-navigable,
accessible, fast. Key decisions: **debounce** input (~200–300 ms) to cut request
volume; **cancel** stale requests (`AbortController`) to avoid the out-of-order-response
race; **cache** results per query (small LRU) so backspacing is instant; render top-N
with highlighting; handle empty/loading/error; wire up **ARIA combobox** roles and
arrow/enter/escape keys. The heavy ranking lives server-side (trie/inverted index — see
[`../system-design/high-level/search-engine.md`](../system-design/high-level/search-engine.md));
the client orchestrates. **Trade-offs:** debounce latency vs request count; cache
freshness vs memory.

### Infinite-scroll feed
Requirements: endless list, smooth scroll, media, near-real-time. Key decisions:
**cursor** pagination (offset breaks when items shift); an **IntersectionObserver**
sentinel to fetch the next page near the bottom; **list virtualization** so the DOM
stays small regardless of list length; lazy-loaded images with reserved dimensions (to
avoid CLS); preserved scroll position; optimistic likes/comments; skeleton loaders.
**Trade-offs:** virtualization complexity vs DOM cost; prefetch distance vs wasted
fetches. Backend fan-out is a separate concern (see
[`../system-design/high-level/social-media-feed.md`](../system-design/high-level/social-media-feed.md)).

### Reusable component library / design system
Requirements: consistent, themeable, accessible, tree-shakeable components used across
apps. Key decisions: **design tokens** (color/spacing/type) for theming; accessibility
(focus, ARIA, keyboard) **baked into primitives**; **composable/compound APIs** over
boolean-prop explosions; support controlled *and* uncontrolled usage; SSR-safe; semantic
versioning + docs; and **tree-shaking** (ESM, correct `sideEffects`) so consumers only
pay for what they import. **Trade-offs:** flexibility vs consistency; abstraction vs
escape hatches; bundle size vs feature richness.

## Trade-offs to voice
- **CSR vs SSR vs SSG** — interactivity vs first paint/SEO vs freshness, chosen per route.
- **Offset vs cursor pagination** — page numbers vs stability under change.
- **Client state vs server cache** — own it vs cache-and-revalidate it.
- **Virtualization vs simplicity** — DOM cost vs implementation complexity.
- **Prefetch vs bandwidth** — instant navigation vs wasted requests.
- **Accessibility & performance are features**, not afterthoughts — raise them yourself.
