# Frontend

Frontend interview prep: the web platform fundamentals plus the major frameworks.

## Contents

- [`html-css.md`](html-css.md) — HTML semantics, CSS layout (flexbox/grid), the box
  model, responsive design, accessibility, and browser fundamentals.
- [`graphql.md`](graphql.md) — GraphQL schema design, queries/mutations/subscriptions,
  resolvers, and REST-vs-GraphQL trade-offs.
- **[`react/`](react/)** — the fully rebuilt React module:
  - [`react/README.md`](react/README.md) — core model + hooks
  - [`react/rendering-and-performance.md`](react/rendering-and-performance.md)
  - [`react/advanced-and-modern.md`](react/advanced-and-modern.md) — state, RSC, Suspense, SSR/CSR/SSG/ISR, testing
  - `react/react-legacy-qa.md` — original long-form Q&A (reference, pending review)
- [`angular.md`](angular.md) — Angular: DI, RxJS, change detection, signals,
  standalone components. (Original preserved as `angular-legacy-qa.md`.)
- [`vue.md`](vue.md) — Vue 3: reactivity, Composition API, composables, Pinia.
  (Original preserved as `vue-legacy-qa.md`.)

## How to use

Master the **fundamentals first** (`html-css.md`) — framework questions assume you
know the box model, the event loop's effect on the DOM, and accessibility. Then go
deep on the framework the role uses. For most FAANG-adjacent frontend roles that's
**React**; start with `react/README.md` and make sure you can explain *why a
component re-renders* (`react/rendering-and-performance.md`) — the single most common
senior React question.

## Cross-references

- JavaScript/TypeScript language depth: [`../languages/`](../languages/).
- API design that frontends consume: [`graphql.md`](graphql.md) and
  [`../system-design/`](../system-design/).
