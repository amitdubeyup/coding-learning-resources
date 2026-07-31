# React rendering & performance

Senior React interviews live here. If you can explain *why* a component re-rendered
and *how* to stop needless renders, you're ahead of most candidates. The mental model
below is timeless; the **tooling changed in React 19** (see the compiler section) —
know both, because most production code you'll discuss predates the compiler.

## The rendering pipeline

1. **Trigger** — initial mount, or a state/prop change.
2. **Render** — React calls your components to produce a new element tree. "Render"
   means *calling the function*, not touching the DOM.
3. **Reconcile** — React diffs the new tree against the previous one.
4. **Commit** — React applies the minimal set of real-DOM mutations, then browser paints.

**Virtual DOM** is just the in-memory element tree that makes the diff cheap.
**Fiber** (React 16+) is the reconciler that makes rendering *interruptible*: work is
split into units so high-priority updates (typing) can preempt low-priority ones.

## Reconciliation rules

- React compares element **type**. Same type → reuse the DOM node, update props.
  Different type → tear down the old subtree and build a new one.
- Among siblings, **keys** decide which element maps to which previous element.
  Wrong/index keys → React reuses the wrong node and state "leaks" between rows.

## Why a component re-renders

A component re-renders when:
1. its **state** changes,
2. its **parent** re-renders (by default children re-render too), or
3. a **context** it consumes changes.

The #1 misconception: "props changed, so it re-rendered." Actually a child re-renders
because its **parent** did — regardless of whether its props changed. That's what
`React.memo` (and now the compiler) addresses.

## The compiler era (React 19+) — read this before memoizing anything

The **React Compiler** is stable (1.0 since late 2025; works back to React 17). It
analyzes data flow at **build time** and inserts memoization for you automatically —
so in new, compiler-enabled code you generally **do not hand-write `useMemo`,
`useCallback`, or `React.memo`** at all. It memoizes more thoroughly than most people
do by hand, including inside dependencies.

So the modern senior answer to *"how do you optimize re-renders?"* is:
1. **Turn on the compiler** and let it auto-memoize.
2. Fix **structural** problems (below) that the compiler can't — those are about *where
   state lives*, not memoization.
3. Reach for **manual** memoization only as an escape hatch, or in the large body of
   pre-compiler code still in the wild.

You still must understand the manual toolkit — for interviews, for debugging, and for
older codebases — but "wrap everything in `useMemo`" is now actively outdated advice.

## The manual memoization toolkit (what the compiler automates)

- **`React.memo(Component)`** — skips a child's re-render if its props are shallow-equal
  to last time. Only helps if the parent re-renders often *and* the child is
  non-trivial to render.
- **`useMemo(fn, deps)`** — caches a computed value across renders. Use for genuinely
  expensive computations, or to keep an object/array **referentially stable** so it
  doesn't break a `memo`'d child or an effect dependency.
- **`useCallback(fn, deps)`** — same idea for function identity; pass stable callbacks
  to `memo`'d children.

**The trap (and why the compiler exists):** `React.memo` does a shallow prop compare,
so passing a fresh object/array/function literal every render defeats it. Manual
memoization only works when the *whole chain* is stable — easy to get wrong, which is
exactly what the compiler fixes:

```jsx
// Broken: `style` and `onClick` are new every render → memo does nothing.
<Child style={{color:'red'}} onClick={() => go(id)} />

// Manual fix (pre-compiler):
const style = useMemo(() => ({ color: 'red' }), []);
const onClick = useCallback(() => go(id), [id]);
<Child style={style} onClick={onClick} />

// Compiler era: write the first version — the compiler stabilizes it for you.
```

## Cutting re-renders without memo (the compiler can't do these)

Structural fixes are often better *and* are what remains your job under the compiler:
- **Lift content, not state:** pass expensive subtrees as `children` so they don't
  re-render when the stateful parent does.
- **Push state down:** move state into the smallest component that needs it, so a
  frequent update doesn't re-render a large tree.
- **Split contexts:** a single big context re-renders every consumer on any change;
  separate rarely- and frequently-changing values.

## Bundle & load performance

- **Code splitting:** `React.lazy(() => import('./X'))` + `<Suspense fallback>` to
  load routes/heavy components on demand.
- **List virtualization:** render only visible rows (e.g. a windowing library) for
  large lists — the single biggest win for long tables/feeds.
- **Concurrent features:** `useTransition` marks non-urgent updates so typing stays
  responsive; `useDeferredValue` defers expensive derived UI.

## Measuring (say this in interviews)

Don't guess — profile. Use the **React DevTools Profiler** to see what rendered and
why, and the browser Performance panel for paint/scripting. Optimize the measured
hot path, then re-measure. "I'd profile first" is the answer interviewers want before
any optimization talk — and in React 19 the fix is usually *structural or the
compiler*, not hand-written memoization.

## Common questions

- **Virtual DOM faster than real DOM?** It avoids *unnecessary* real-DOM work via
  batched, minimal updates — the abstraction, not raw speed, is the win.
- **Everything re-renders on each state change — is that bad?** Usually no; renders
  are cheap. Optimize only measured problems.
- **`key` with index — when is it fine?** Only for static lists that never reorder,
  insert, or delete.
- **Do you still need `useMemo`/`useCallback` in React 19?** Mostly no in
  compiler-enabled code — it auto-memoizes. You still reach for them as an escape hatch
  or in pre-compiler codebases, so know how they work and why the shallow-compare trap
  bites.
- **What can the compiler *not* fix?** Where state lives — lifting content, pushing
  state down, splitting contexts, and list virtualization are still on you.
