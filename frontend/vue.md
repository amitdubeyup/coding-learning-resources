# Vue

Vue is a progressive framework that sits between React's minimalism and Angular's
full-framework approach. Interviews center on its **reactivity system** and the
**Composition API** (the Vue 3 default).

> **Currency note:** Vue 3 with the **Composition API** and `<script setup>` is the
> modern standard. The Options API still works and appears in older code — know both,
> but write new examples with Composition.

## Reactivity (the defining topic)

Vue tracks dependencies automatically: when reactive state changes, only the
components that used it re-render.

- **`ref()`** — wraps a single value; access via `.value` in script (auto-unwrapped in
  templates).
- **`reactive()`** — makes an object deeply reactive.
- Under the hood, Vue 3 uses **ES Proxies** to intercept get/set (Vue 2 used
  `Object.defineProperty`, which couldn't detect new properties or array index
  changes — a common "why Vue 3?" answer).

```vue
<script setup>
import { ref, computed, watch } from "vue";

const count = ref(0);
const doubled = computed(() => count.value * 2);   // cached, recomputes on dep change
watch(count, (n, old) => console.log(`${old} → ${n}`));

function inc() { count.value++; }
</script>

<template>
  <button @click="inc">{{ count }} (doubled: {{ doubled }})</button>
</template>
```

- **`computed`** — derived, **cached** value; recomputes only when a dependency
  changes. Use for derived state.
- **`watch` / `watchEffect`** — run side effects when reactive sources change. Use for
  effects, not for deriving values (that's `computed`).

## Composition API vs Options API

- **Options API** — organizes code by option type (`data`, `methods`, `computed`,
  lifecycle). Simple for small components; logic for one feature gets scattered.
- **Composition API** (`setup`/`<script setup>`) — organizes by **logical concern** and
  makes logic reusable via **composables** (Vue's answer to custom hooks). Better for
  large components and code reuse. The modern default.

```js
// A composable — reusable stateful logic (like a React custom hook)
export function useMouse() {
  const x = ref(0), y = ref(0);
  const update = (e) => { x.value = e.pageX; y.value = e.pageY; };
  onMounted(() => window.addEventListener("mousemove", update));
  onUnmounted(() => window.removeEventListener("mousemove", update));
  return { x, y };
}
```

## Components & communication

- **Props down, events up:** parent passes `props`; child emits events (`defineEmits`)
  to notify the parent. One-way data flow, like React.
- **`v-model`** — two-way binding sugar (prop + event) for form inputs and custom
  components.
- **Slots** — content projection so parents inject markup into a child (like
  `children`); named and scoped slots for flexible, reusable components.

## Directives & rendering

`v-if`/`v-else` (conditional, actually adds/removes DOM) vs `v-show` (toggles CSS
`display`); `v-for` (needs a stable `:key`, same reasoning as React); `v-bind` (`:`)
and `v-on` (`@`).

## State management & routing

- **Pinia** is the official state library (replaced Vuex) — simpler, TypeScript-first,
  Composition-API-friendly. Use it for shared cross-component state; keep local state
  local.
- **Vue Router** for SPA routing.

## Common questions

- **`ref` vs `reactive`?** `ref` wraps any single value (`.value`); `reactive` makes an
  object deeply reactive. `ref` is the common default.
- **`computed` vs `watch`?** Derive a cached value vs run a side effect on change.
- **Composition vs Options API?** Organize by logical concern + reusable composables vs
  by option type; Composition scales better.
- **How is Vue's reactivity implemented?** ES Proxies in Vue 3 (vs `defineProperty` in
  Vue 2, which had detection gaps).
- **`v-if` vs `v-show`?** Add/remove DOM vs toggle visibility — `v-show` is cheaper to
  toggle, `v-if` is cheaper if rarely shown.
- **Vue vs React?** Both are reactive component libraries with one-way data flow; Vue
  offers more built-in conventions (directives, `v-model`, official router/store),
  React is more minimal/flexible.

*Deep legacy Q&A: [`vue-legacy-qa.md`](vue-legacy-qa.md).*
