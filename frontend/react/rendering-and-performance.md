# React rendering & performance

Senior React interviews live here. If you can explain *why* a component re-rendered
and *how* to stop needless renders, you're ahead of most candidates.

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
`React.memo` addresses.

## The memoization toolkit — use with intent

- **`React.memo(Component)`** — skips a child's re-render if its props are shallow-equal
  to last time. Only helps if the parent re-renders often *and* the child is
  non-trivial to render.
- **`useMemo(fn, deps)`** — caches a computed value across renders. Use for genuinely
  expensive computations, or to keep an object/array **referentially stable** so it
  doesn't break a `memo`'d child or an effect dependency.
- **`useCallback(fn, deps)`** — same idea for function identity; pass stable callbacks
  to `memo`'d children.

**The trap:** `React.memo` does a shallow prop compare, so passing a fresh
object/array/function literal every render defeats it. Memoization only works when
the *whole chain* is stable.

```jsx
// Broken: `style` and `onClick` are new every render → memo does nothing.
<Child style={{color:'red'}} onClick={() => go(id)} />

// Fixed:
const style = useMemo(() => ({ color: 'red' }), []);
const onClick = useCallback(() => go(id), [id]);
<Child style={style} onClick={onClick} />
```

**Don't memoize everything.** Each `useMemo`/`useCallback` has its own cost and
clutters code. Measure first; memoize the hot path. A senior answer names the
trade-off, not "wrap it all in useMemo."

## Cutting re-renders without memo

Often the better fix is structural:
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
any optimization talk.

## Common questions

- **Virtual DOM faster than real DOM?** It avoids *unnecessary* real-DOM work via
  batched, minimal updates — the abstraction, not raw speed, is the win.
- **Everything re-renders on each state change — is that bad?** Usually no; renders
  are cheap. Optimize only measured problems.
- **`key` with index — when is it fine?** Only for static lists that never reorder,
  insert, or delete.
- **When NOT to use `useMemo`?** Cheap computations — the memo overhead outweighs the
  gain and hurts readability.
