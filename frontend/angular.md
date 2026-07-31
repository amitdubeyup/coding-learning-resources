# Angular

Angular is a full, opinionated framework (not a library): routing, forms, HTTP, DI,
and testing all come in the box. Interviews test dependency injection, RxJS, change
detection, and — increasingly — **signals** and **standalone components**, the modern
direction.

> **Currency note:** modern Angular (v16+/v17+) favors **standalone components** over
> NgModules and **signals** for reactivity. Know both the classic model and the new
> one; many codebases are mid-migration.

## Building blocks

- **Component** — a class + template + styles controlling a piece of UI. The unit you
  build everything from.
- **Template** — HTML with Angular syntax: interpolation `{{ }}`, property binding
  `[prop]`, event binding `(event)`, two-way `[(ngModel)]`.
- **Service** — a reusable class for logic/data, provided via DI.
- **Module (NgModule)** — the classic way to group components/services. **Standalone
  components** (current default for new code) remove most NgModule boilerplate.

## Dependency Injection (a core Angular topic)

Angular has a hierarchical DI system: you declare a dependency in the constructor
(or via `inject()`), and Angular supplies a singleton from the appropriate injector.

```ts
@Injectable({ providedIn: "root" })   // app-wide singleton
export class UserService {
  constructor(private http: HttpClient) {}
  getUser(id: string) { return this.http.get(`/api/users/${id}`); }
}

@Component({ /* ... */ })
export class UserComponent {
  private users = inject(UserService);   // modern inject() style
}
```

Why it matters: testability (swap real deps for mocks) and decoupling. Be ready to
explain `providedIn: 'root'` (app singleton) vs providing at component level (a new
instance per component).

## RxJS & observables (the steep part)

Angular is built on **Observables** (streams of values over time) via RxJS — HTTP
calls, router events, and forms all emit observables.

- **Observable vs Promise:** an observable is a *stream* (0..∞ values, lazy,
  cancellable); a promise is a *single* future value (eager, not cancellable).
- **Operators** transform streams: `map`, `filter`, `switchMap` (cancel previous inner
  observable — ideal for type-ahead search), `mergeMap`, `debounceTime`, `takeUntil`.
- **Subscriptions leak** if not cleaned up — unsubscribe in `ngOnDestroy`, use
  `takeUntil`/`takeUntilDestroyed`, or let the `async` pipe manage it (preferred in
  templates).

```ts
// Type-ahead: debounce input, cancel stale requests with switchMap
this.results$ = this.search.valueChanges.pipe(
  debounceTime(300),
  distinctUntilChanged(),
  switchMap(term => this.api.search(term)),
);
```

## Change detection & signals

- **Classic:** Zone.js patches async APIs and triggers change detection across the
  component tree. `OnPush` change detection limits checks to input changes / observable
  emissions — the main perf lever.
- **Signals (modern):** fine-grained reactive values (`signal()`, `computed()`,
  `effect()`) that update only what depends on them — less magic than Zone.js and the
  direction Angular is heading (toward zoneless). Mention signals as the current best
  practice for new reactive state.

## Forms

- **Template-driven** — logic in the template with `ngModel`; simple forms.
- **Reactive** — form model defined in the component (`FormGroup`/`FormControl`);
  explicit, testable, better for complex/dynamic forms and validation. Prefer reactive
  for anything non-trivial.

## Common questions

- **Angular vs React?** Full opinionated framework (DI, RxJS, forms, CLI built in) vs
  a focused UI library you compose. Angular gives structure; React gives flexibility.
- **Observable vs Promise?** Stream (multi-value, lazy, cancellable) vs single eager
  value.
- **What is `switchMap` for?** Cancel the previous inner request when a new one starts
  — the type-ahead pattern.
- **How do you avoid memory leaks?** Unsubscribe (`takeUntil`/`async` pipe) in
  `ngOnDestroy`.
- **`OnPush` — why?** Skip change-detection unless inputs/observables change — a key
  performance optimization.
- **Signals — what problem do they solve?** Fine-grained reactivity without Zone.js
  overhead.
- **Standalone components?** Components without NgModules — less boilerplate, the
  modern default.

*Deep legacy Q&A: [`angular-legacy-qa.md`](angular-legacy-qa.md).*
