# 200 VueJS Interview Questions & Answers

A comprehensive guide to the most commonly asked Vue.js interview questions covering fundamentals, advanced concepts, and best practices.

## Table of Contents
- [Basics & Fundamentals (1-50)](#basics--fundamentals-1-50)
- [Components & Props (51-100)](#components--props-51-100)
- [Reactivity & Data Management (101-150)](#reactivity--data-management-101-150)
- [Advanced Concepts (151-200)](#advanced-concepts-151-200)

---

## Basics & Fundamentals (1-50)

### 1. What is Vue.js?
**Answer:** Vue.js is a progressive JavaScript framework for building user interfaces. It's designed to be incrementally adoptable, meaning you can use as much or as little of it as needed. Vue focuses on the view layer and provides a rich ecosystem for building single-page applications.

### 2. What are the key features of Vue.js?
**Answer:** 
- **Reactive Data Binding**: Automatic DOM updates when data changes
- **Component-Based Architecture**: Reusable, self-contained components
- **Virtual DOM**: Efficient rendering and updates
- **Directives**: Special attributes with v- prefix for DOM manipulation
- **Lifecycle Hooks**: Methods that run at specific stages of component lifecycle
- **Computed Properties**: Cached, reactive properties
- **Watchers**: React to data changes

### 3. What is the difference between Vue.js and other frameworks like React and Angular?
**Answer:** 
- **Vue.js**: Progressive, lightweight, easy learning curve, template-based syntax
- **React**: More opinionated, JSX syntax, larger ecosystem, backed by Facebook
- **Angular**: Full-featured framework, TypeScript-first, steeper learning curve, backed by Google

### 4. What is the Vue instance?
**Answer:** The Vue instance is the root of every Vue application. It's created using the `new Vue()` constructor and serves as the entry point for the application.

```javascript
const app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  }
})
```

### 5. What is the el property in Vue.js?
**Answer:** The `el` property tells Vue which DOM element to mount the Vue instance to. It can be a CSS selector string or an actual DOM element.

### 6. What are directives in Vue.js?
**Answer:** Directives are special attributes with the `v-` prefix that apply reactive behavior to the DOM. Examples include `v-if`, `v-for`, `v-bind`, `v-on`, etc.

### 7. What is v-bind directive?
**Answer:** `v-bind` is used to dynamically bind one or more attributes or component props to an expression. The shorthand is `:`.

```html
<img v-bind:src="imageSrc" :alt="imageAlt">
```

### 8. What is v-on directive?
**Answer:** `v-on` is used to attach event listeners that invoke methods on Vue instances. The shorthand is `@`.

```html
<button v-on:click="handleClick" @click="handleClick">Click me</button>
```

### 9. What is v-if directive?
**Answer:** `v-if` conditionally renders an element based on the truthiness of the expression. The element and its children are completely destroyed and recreated when the condition changes.

```html
<div v-if="isVisible">This will show if isVisible is true</div>
```

### 10. What is the difference between v-if and v-show?
**Answer:** 
- **v-if**: Conditionally renders the element (creates/destroys DOM elements)
- **v-show**: Always renders the element but toggles its CSS display property

### 11. What is v-for directive?
**Answer:** `v-for` is used to render a list of items based on an array or object.

```html
<ul>
  <li v-for="item in items" :key="item.id">{{ item.name }}</li>
</ul>
```

### 12. What is the key attribute in v-for?
**Answer:** The `key` attribute helps Vue track each node's identity and reuse/reorder existing elements when data changes. It should be unique for each item.

### 13. What are computed properties?
**Answer:** Computed properties are cached, reactive properties that automatically update when their dependencies change. They're defined in the `computed` option.

```javascript
computed: {
  fullName() {
    return this.firstName + ' ' + this.lastName
  }
}
```

### 14. What is the difference between computed properties and methods?
**Answer:** 
- **Computed properties**: Cached based on dependencies, only recalculated when dependencies change
- **Methods**: Always executed when called, no caching

### 15. What are watchers?
**Answer:** Watchers allow you to perform asynchronous or expensive operations in response to changing data. They're defined in the `watch` option.

```javascript
watch: {
  searchQuery(newVal, oldVal) {
    this.performSearch(newVal)
  }
}
```

### 16. What is the data property in Vue.js?
**Answer:** The `data` property is a function that returns an object containing the component's reactive data properties.

```javascript
data() {
  return {
    message: 'Hello',
    count: 0
  }
}
```

### 17. What is the methods property in Vue.js?
**Answer:** The `methods` property contains functions that can be called from templates or other methods.

```javascript
methods: {
  increment() {
    this.count++
  }
}
```

### 18. What are lifecycle hooks in Vue.js?
**Answer:** Lifecycle hooks are methods that run at specific stages of a component's lifecycle, such as creation, mounting, updating, and destruction.

### 19. What is the created lifecycle hook?
**Answer:** `created` is called synchronously after the instance is created, before the DOM is mounted. It's good for initializing data and making API calls.

### 20. What is the mounted lifecycle hook?
**Answer:** `mounted` is called after the component has been mounted to the DOM. It's good for DOM manipulation and third-party library initialization.

### 21. What is the updated lifecycle hook?
**Answer:** `updated` is called after the component's data has changed and the DOM has been re-rendered.

### 22. What is the destroyed lifecycle hook?
**Answer:** `destroyed` is called when the component is destroyed. It's good for cleanup operations like removing event listeners.

### 23. What is the beforeDestroy lifecycle hook?
**Answer:** `beforeDestroy` is called right before the component is destroyed, allowing for cleanup before the component is removed.

### 24. What is the beforeMount lifecycle hook?
**Answer:** `beforeMount` is called right before the mounting begins, after the template has been compiled.

### 25. What is the beforeUpdate lifecycle hook?
**Answer:** `beforeUpdate` is called when the data changes, before the DOM is re-rendered.

### 26. What is the activated lifecycle hook?
**Answer:** `activated` is called when a kept-alive component is activated.

### 27. What is the deactivated lifecycle hook?
**Answer:** `deactivated` is called when a kept-alive component is deactivated.

### 28. What is the errorCaptured lifecycle hook?
**Answer:** `errorCaptured` is called when an error from any descendent component is captured.

### 29. What is the serverPrefetch lifecycle hook?
**Answer:** `serverPrefetch` is called during server-side rendering, before the component is rendered on the server.

### 30. What is the beforeCreate lifecycle hook?
**Answer:** `beforeCreate` is called synchronously immediately after the instance is initialized, before data observation and event/watcher setup.

### 31. What is the beforeUnmount lifecycle hook?
**Answer:** `beforeUnmount` is called right before the component is unmounted, allowing for cleanup before the component is removed.

### 32. What is the unmounted lifecycle hook?
**Answer:** `unmounted` is called when the component has been unmounted.

### 33. What is the renderTracked lifecycle hook?
**Answer:** `renderTracked` is called when a reactive dependency is tracked by the render function.

### 34. What is the renderTriggered lifecycle hook?
**Answer:** `renderTriggered` is called when a reactive dependency triggers the render function to be re-run.

### 35. What is the template property in Vue.js?
**Answer:** The `template` property contains the HTML template for the component. It can be a string or a template element.

### 36. What is the render function in Vue.js?
**Answer:** The `render` function is an alternative to templates that allows you to programmatically create virtual DOM nodes.

### 37. What is the name property in Vue.js?
**Answer:** The `name` property sets the component's name for debugging purposes and when using Vue DevTools.

### 38. What is the components property in Vue.js?
**Answer:** The `components` property registers child components that can be used in the template.

### 39. What is the props property in Vue.js?
**Answer:** The `props` property defines the properties that a component can receive from its parent.

### 40. What is the emits property in Vue.js?
**Answer:** The `emits` property declares the events that a component can emit to its parent.

### 41. What is the setup function in Vue 3?
**Answer:** The `setup` function is the entry point for Composition API in Vue 3. It runs before the component is created and provides access to props and context.

### 42. What is the ref function in Vue 3?
**Answer:** `ref` creates a reactive reference to a value. It's used in the Composition API to make primitive values reactive.

```javascript
import { ref } from 'vue'

const count = ref(0)
```

### 43. What is the reactive function in Vue 3?
**Answer:** `reactive` creates a reactive object. It's used in the Composition API to make objects reactive.

```javascript
import { reactive } from 'vue'

const state = reactive({
  count: 0,
  name: 'John'
})
```

### 44. What is the computed function in Vue 3?
**Answer:** `computed` creates a computed property in the Composition API.

```javascript
import { computed } from 'vue'

const doubleCount = computed(() => count.value * 2)
```

### 45. What is the watch function in Vue 3?
**Answer:** `watch` creates a watcher in the Composition API.

```javascript
import { watch } from 'vue'

watch(count, (newVal, oldVal) => {
  console.log('Count changed from', oldVal, 'to', newVal)
})
```

### 46. What is the watchEffect function in Vue 3?
**Answer:** `watchEffect` runs a function immediately and re-runs it whenever reactive dependencies change.

```javascript
import { watchEffect } from 'vue'

watchEffect(() => {
  console.log('Count is:', count.value)
})
```

### 47. What is the onMounted function in Vue 3?
**Answer:** `onMounted` registers a callback to be called after the component is mounted.

```javascript
import { onMounted } from 'vue'

onMounted(() => {
  console.log('Component mounted')
})
```

### 48. What is the onUnmounted function in Vue 3?
**Answer:** `onUnmounted` registers a callback to be called when the component is unmounted.

```javascript
import { onUnmounted } from 'vue'

onUnmounted(() => {
  console.log('Component unmounted')
})
```

### 49. What is the provide/inject pattern in Vue.js?
**Answer:** `provide` and `inject` allow ancestor components to pass data down to descendant components without explicitly passing props through every level.

### 50. What is the nextTick function in Vue.js?
**Answer:** `nextTick` waits for the next DOM update cycle to complete before executing a callback. It's useful when you need to wait for Vue to finish updating the DOM.

---

## Components & Props (51-100)

### 51. What is a component in Vue.js?
**Answer:** A component is a reusable Vue instance with a name. Components can be used as custom elements in templates and can accept props and emit events.

### 52. How do you create a component in Vue.js?
**Answer:** Components can be created using `Vue.component()` globally or by defining them in the `components` option locally.

```javascript
// Global component
Vue.component('my-component', {
  template: '<div>My Component</div>'
})

// Local component
export default {
  components: {
    'my-component': {
      template: '<div>My Component</div>'
    }
  }
}
```

### 53. What are props in Vue.js?
**Answer:** Props are custom attributes for passing data from parent components to child components. They are reactive and can be validated.

### 54. How do you define props in a component?
**Answer:** Props are defined in the `props` option as an array of strings or an object with validation.

```javascript
props: ['title', 'content']

// Or with validation
props: {
  title: {
    type: String,
    required: true,
    default: 'Default Title'
  }
}
```

### 55. What are the prop types available in Vue.js?
**Answer:** Vue supports String, Number, Boolean, Array, Object, Date, Function, and Symbol as prop types.

### 56. How do you pass props to a component?
**Answer:** Props are passed using the `v-bind` directive or its shorthand `:`.

```html
<my-component :title="pageTitle" :content="pageContent"></my-component>
```

### 57. What is prop validation in Vue.js?
**Answer:** Prop validation allows you to specify the type, required status, default value, and custom validator for props.

### 58. How do you emit events from a component?
**Answer:** Events are emitted using the `$emit` method.

```javascript
this.$emit('my-event', data)
```

### 59. How do you listen to events from a component?
**Answer:** Events are listened to using the `v-on` directive or its shorthand `@`.

```html
<my-component @my-event="handleEvent"></my-component>
```

### 60. What is the difference between props and events?
**Answer:** 
- **Props**: Pass data down from parent to child (one-way)
- **Events**: Pass data up from child to parent (one-way)

### 61. What is a slot in Vue.js?
**Answer:** Slots allow you to pass content from a parent component to a child component, enabling content distribution.

### 62. How do you define a slot in a component?
**Answer:** Slots are defined using the `<slot>` element in the component's template.

```html
<template>
  <div>
    <header>
      <slot name="header">Default header</slot>
    </header>
    <main>
      <slot>Default content</slot>
    </main>
  </div>
</template>
```

### 63. How do you use a slot in a parent component?
**Answer:** Slots are used by placing content between the component tags or using the `v-slot` directive.

```html
<my-component>
  <template v-slot:header>
    <h1>Custom Header</h1>
  </template>
  <p>Custom content</p>
</my-component>
```

### 64. What is a scoped slot in Vue.js?
**Answer:** Scoped slots allow the child component to pass data to the parent component's slot content.

### 65. How do you define a scoped slot?
**Answer:** Scoped slots are defined by passing data to the `<slot>` element.

```html
<slot :item="item" :index="index"></slot>
```

### 66. How do you use a scoped slot?
**Answer:** Scoped slots are used with the `v-slot` directive and can access the passed data.

```html
<my-component>
  <template v-slot:default="slotProps">
    <span>{{ slotProps.item.name }}</span>
  </template>
</my-component>
```

### 67. What is a dynamic component in Vue.js?
**Answer:** Dynamic components allow you to switch between different components using the `<component>` element with the `is` attribute.

### 68. How do you use dynamic components?
**Answer:** Dynamic components are used with the `is` attribute bound to a component name or component object.

```html
<component :is="currentComponent"></component>
```

### 69. What is the keep-alive component?
**Answer:** `<keep-alive>` is a built-in component that caches component instances when they are dynamically switched.

### 70. How do you use keep-alive?
**Answer:** `<keep-alive>` wraps dynamic components to preserve their state.

```html
<keep-alive>
  <component :is="currentComponent"></component>
</keep-alive>
```

### 71. What are the include and exclude props of keep-alive?
**Answer:** 
- `include`: Only cache components matching the pattern
- `exclude`: Don't cache components matching the pattern

### 72. What is the max prop of keep-alive?
**Answer:** The `max` prop limits the number of component instances that can be cached.

### 73. What is a functional component in Vue.js?
**Answer:** Functional components are stateless components that don't have their own state or lifecycle methods. They're purely presentational.

### 74. How do you create a functional component?
**Answer:** Functional components are created by setting the `functional` option to `true`.

```javascript
export default {
  functional: true,
  props: ['title'],
  render(h, context) {
    return h('div', context.props.title)
  }
}
```

### 75. What is the render function context in functional components?
**Answer:** The render function in functional components receives a context object containing props, children, data, and other properties.

### 76. What is a mixin in Vue.js?
**Answer:** Mixins are a way to distribute reusable functionality for Vue components. They can contain any component options.

### 77. How do you create and use a mixin?
**Answer:** Mixins are created as objects and used in the `mixins` option.

```javascript
const myMixin = {
  methods: {
    hello() {
      console.log('Hello from mixin')
    }
  }
}

export default {
  mixins: [myMixin]
}
```

### 78. What is the merge strategy for mixins?
**Answer:** Vue merges mixin options with component options using specific strategies:
- Data objects are merged recursively
- Methods and computed properties are merged
- Lifecycle hooks are called in order (mixin first, then component)

### 79. What is a plugin in Vue.js?
**Answer:** Plugins are a way to add global-level functionality to Vue. They can add global methods, directives, filters, or components.

### 80. How do you create a Vue plugin?
**Answer:** Plugins are created as objects with an `install` method and registered using `Vue.use()`.

```javascript
const MyPlugin = {
  install(Vue, options) {
    Vue.directive('my-directive', {
      bind(el, binding, vnode, oldVnode) {
        // directive logic
      }
    })
  }
}

Vue.use(MyPlugin)
```

### 81. What is the difference between mixins and plugins?
**Answer:** 
- **Mixins**: Add functionality to individual components
- **Plugins**: Add global functionality to the entire Vue application

### 82. What is a custom directive in Vue.js?
**Answer:** Custom directives allow you to add custom behavior to DOM elements.

### 83. How do you create a custom directive?
**Answer:** Custom directives are created using `Vue.directive()` or in the `directives` option.

```javascript
Vue.directive('focus', {
  inserted(el) {
    el.focus()
  }
})
```

### 84. What are the hook functions for custom directives?
**Answer:** 
- `bind`: Called when directive is first bound to the element
- `inserted`: Called when the bound element has been inserted into its parent node
- `update`: Called when the component is updated
- `componentUpdated`: Called after the component and its children have updated
- `unbind`: Called when the directive is unbound from the element

### 85. What is a filter in Vue.js?
**Answer:** Filters are functions that can be used to apply common text formatting. They're used with the pipe symbol `|`.

### 86. How do you create a filter?
**Answer:** Filters are created using `Vue.filter()` or in the `filters` option.

```javascript
Vue.filter('capitalize', function(value) {
  return value.charAt(0).toUpperCase() + value.slice(1)
})
```

### 87. How do you use a filter?
**Answer:** Filters are used in templates with the pipe symbol.

```html
{{ message | capitalize }}
```

### 88. What is the difference between filters and computed properties?
**Answer:** 
- **Filters**: Used for text formatting in templates
- **Computed properties**: Used for data transformation and caching

### 89. What is a transition in Vue.js?
**Answer:** Transitions allow you to apply CSS transitions and animations when elements are inserted, updated, or removed from the DOM.

### 90. How do you use transitions?
**Answer:** Transitions are applied using the `<transition>` component.

```html
<transition name="fade">
  <div v-if="show">Hello</div>
</transition>
```

### 91. What are transition classes in Vue.js?
**Answer:** Vue automatically adds CSS classes during transitions:
- `v-enter`: Starting state for enter
- `v-enter-active`: Active state for enter
- `v-enter-to`: Ending state for enter
- `v-leave`: Starting state for leave
- `v-leave-active`: Active state for leave
- `v-leave-to`: Ending state for leave

### 92. What is a transition group in Vue.js?
**Answer:** `<transition-group>` is used to animate lists of elements, such as when using `v-for`.

### 93. How do you use transition groups?
**Answer:** Transition groups wrap lists and animate individual items.

```html
<transition-group name="list" tag="ul">
  <li v-for="item in items" :key="item.id">
    {{ item.text }}
  </li>
</transition-group>
```

### 94. What is the tag prop in transition-group?
**Answer:** The `tag` prop specifies the HTML element that the transition group should render as.

### 95. What is the move class in transition-group?
**Answer:** The `move` class is applied to elements that are moving to new positions in the list.

### 96. What is a teleport in Vue 3?
**Answer:** `<teleport>` allows you to render a component's content in a different location in the DOM tree.

### 97. How do you use teleport?
**Answer:** Teleport is used to move content to a different DOM location.

```html
<teleport to="#modal">
  <div class="modal">
    <h2>Modal Content</h2>
  </div>
</teleport>
```

### 98. What is the to prop in teleport?
**Answer:** The `to` prop specifies the target location where the teleported content should be rendered.

### 99. What is the disabled prop in teleport?
**Answer:** The `disabled` prop allows you to conditionally disable teleporting.

### 100. What is a fragment in Vue 3?
**Answer:** Fragments allow components to return multiple root nodes without wrapping them in a single container element.

---

## Reactivity & Data Management (101-150)

### 101. What is reactivity in Vue.js?
**Answer:** Reactivity is Vue's ability to automatically track dependencies and update the DOM when data changes.

### 102. How does Vue's reactivity system work?
**Answer:** Vue uses getters and setters to track property access and modifications, automatically updating the DOM when reactive data changes.

### 103. What is the Object.defineProperty method used for in Vue 2?
**Answer:** Vue 2 uses `Object.defineProperty` to convert data properties into getters and setters for reactivity.

### 104. What is the Proxy object used for in Vue 3?
**Answer:** Vue 3 uses the `Proxy` object to create reactive objects, providing better performance and more capabilities than `Object.defineProperty`.

### 105. What are the limitations of Vue 2's reactivity system?
**Answer:** 
- Cannot detect property addition/deletion
- Cannot detect array index changes
- Cannot detect array length changes

### 106. How do you add reactive properties in Vue 2?
**Answer:** Use `Vue.set()` or `this.$set()` to add reactive properties.

```javascript
Vue.set(this.someObject, 'newProperty', value)
```

### 107. How do you add reactive properties in Vue 3?
**Answer:** In Vue 3, you can directly assign new properties to reactive objects.

```javascript
const obj = reactive({})
obj.newProperty = value
```

### 108. What is the difference between ref and reactive in Vue 3?
**Answer:** 
- `ref`: Used for primitive values, accessed with `.value`
- `reactive`: Used for objects, accessed directly

### 109. When should you use ref vs reactive?
**Answer:** 
- Use `ref` for primitive values (strings, numbers, booleans)
- Use `reactive` for objects and arrays

### 110. What is the toRef function in Vue 3?
**Answer:** `toRef` creates a ref for a property on a reactive object.

```javascript
const state = reactive({ count: 0 })
const countRef = toRef(state, 'count')
```

### 111. What is the toRefs function in Vue 3?
**Answer:** `toRefs` converts a reactive object into a plain object with refs for each property.

```javascript
const state = reactive({ count: 0, name: 'John' })
const { count, name } = toRefs(state)
```

### 112. What is the unref function in Vue 3?
**Answer:** `unref` returns the inner value if the argument is a ref, otherwise returns the argument itself.

```javascript
const value = unref(someRef) // returns the value
```

### 113. What is the isRef function in Vue 3?
**Answer:** `isRef` checks if a value is a ref object.

```javascript
if (isRef(value)) {
  console.log('This is a ref')
}
```

### 114. What is the isReactive function in Vue 3?
**Answer:** `isReactive` checks if an object is reactive.

```javascript
if (isReactive(obj)) {
  console.log('This object is reactive')
}
```

### 115. What is the isReadonly function in Vue 3?
**Answer:** `isReadonly` checks if an object is readonly.

```javascript
if (isReadonly(obj)) {
  console.log('This object is readonly')
}
```

### 116. What is the readonly function in Vue 3?
**Answer:** `readonly` creates a readonly proxy of an object.

```javascript
const original = reactive({ count: 0 })
const copy = readonly(original)
```

### 117. What is the markRaw function in Vue 3?
**Answer:** `markRaw` marks an object so it will never be converted to a proxy.

```javascript
const obj = markRaw({ count: 0 })
```

### 118. What is the shallowRef function in Vue 3?
**Answer:** `shallowRef` creates a ref that tracks its `.value` property but doesn't make its value reactive.

```javascript
const obj = shallowRef({ count: 0 })
```

### 119. What is the shallowReactive function in Vue 3?
**Answer:** `shallowReactive` creates a reactive proxy that only tracks reactivity at the root level.

```javascript
const state = shallowReactive({ nested: { count: 0 } })
```

### 120. What is the triggerRef function in Vue 3?
**Answer:** `triggerRef` forces a ref to trigger its effects.

```javascript
const count = ref(0)
triggerRef(count)
```

### 121. What is the customRef function in Vue 3?
**Answer:** `customRef` creates a custom ref with explicit control over its dependency tracking and triggering.

```javascript
const customRef = customRef((track, trigger) => {
  return {
    get() {
      track()
      return value
    },
    set(newValue) {
      value = newValue
      trigger()
    }
  }
})
```

### 122. What is the effectScope function in Vue 3?
**Answer:** `effectScope` creates an effect scope that can automatically dispose of all reactive effects.

```javascript
const scope = effectScope()
scope.run(() => {
  const doubled = computed(() => count.value * 2)
})
scope.stop()
```

### 123. What is the getCurrentScope function in Vue 3?
**Answer:** `getCurrentScope` returns the current active effect scope.

```javascript
const scope = getCurrentScope()
```

### 124. What is the onScopeDispose function in Vue 3?
**Answer:** `onScopeDispose` registers a callback to be called when the current effect scope is disposed.

```javascript
onScopeDispose(() => {
  console.log('Scope disposed')
})
```

### 125. What is the defineComponent function in Vue 3?
**Answer:** `defineComponent` provides type inference for component options.

```javascript
import { defineComponent } from 'vue'

export default defineComponent({
  props: {
    title: String
  }
})
```

### 126. What is the defineAsyncComponent function in Vue 3?
**Answer:** `defineAsyncComponent` defines an async component that is loaded on demand.

```javascript
const AsyncComp = defineAsyncComponent(() => import('./AsyncComponent.vue'))
```

### 127. What is the defineEmits function in Vue 3?
**Answer:** `defineEmits` declares the events that a component can emit.

```javascript
const emit = defineEmits(['update', 'delete'])
```

### 128. What is the defineProps function in Vue 3?
**Answer:** `defineProps` declares the props that a component can receive.

```javascript
const props = defineProps({
  title: String,
  count: Number
})
```

### 129. What is the defineExpose function in Vue 3?
**Answer:** `defineExpose` explicitly exposes properties to the parent component.

```javascript
defineExpose({
  focus: () => input.value.focus()
})
```

### 130. What is the withDefaults function in Vue 3?
**Answer:** `withDefaults` provides default values for props when using TypeScript.

```javascript
const props = withDefaults(defineProps<{
  title?: string
  count?: number
}>(), {
  title: 'Default Title',
  count: 0
})
```

### 131. What is the h function in Vue 3?
**Answer:** `h` is the render function that creates virtual DOM nodes.

```javascript
import { h } from 'vue'

export default {
  render() {
    return h('div', 'Hello World')
  }
}
```

### 132. What is the resolveComponent function in Vue 3?
**Answer:** `resolveComponent` resolves a component by name.

```javascript
import { resolveComponent } from 'vue'

const MyComponent = resolveComponent('MyComponent')
```

### 133. What is the resolveDirective function in Vue 3?
**Answer:** `resolveDirective` resolves a directive by name.

```javascript
import { resolveDirective } from 'vue'

const myDirective = resolveDirective('my-directive')
```

### 134. What is the withDirectives function in Vue 3?
**Answer:** `withDirectives` applies directives to a VNode.

```javascript
import { withDirectives, resolveDirective } from 'vue'

const myDirective = resolveDirective('my-directive')
return withDirectives(h('div'), [[myDirective, 'value', 'arg', { modifier: true }]])
```

### 135. What is the withModifiers function in Vue 3?
**Answer:** `withModifiers` adds event modifiers to an event handler.

```javascript
import { withModifiers } from 'vue'

return h('button', {
  onClick: withModifiers(() => {}, ['prevent', 'stop'])
}, 'Click me')
```

### 136. What is the withKeys function in Vue 3?
**Answer:** `withKeys` adds key modifiers to an event handler.

```javascript
import { withKeys } from 'vue'

return h('input', {
  onKeyup: withKeys(() => {}, ['enter'])
})
```

### 137. What is the withCtx function in Vue 3?
**Answer:** `withCtx` provides the component context to a function.

```javascript
import { withCtx } from 'vue'

const handler = withCtx(() => {
  // has access to component context
})
```

### 138. What is the useSlots function in Vue 3?
**Answer:** `useSlots` returns the slots object in the Composition API.

```javascript
import { useSlots } from 'vue'

const slots = useSlots()
```

### 139. What is the useAttrs function in Vue 3?
**Answer:** `useAttrs` returns the attrs object in the Composition API.

```javascript
import { useAttrs } from 'vue'

const attrs = useAttrs()
```

### 140. What is the useCssVars function in Vue 3?
**Answer:** `useCssVars` provides CSS variables to the component.

```javascript
import { useCssVars } from 'vue'

useCssVars(() => ({
  '--color': color.value
}))
```

### 141. What is the useSSRContext function in Vue 3?
**Answer:** `useSSRContext` provides the SSR context in the Composition API.

```javascript
import { useSSRContext } from 'vue'

const ssrContext = useSSRContext()
```

### 142. What is the useTransitionState function in Vue 3?
**Answer:** `useTransitionState` provides transition state in the Composition API.

```javascript
import { useTransitionState } from 'vue'

const transitionState = useTransitionState()
```

### 143. What is the useVModel function in Vue 3?
**Answer:** `useVModel` creates a two-way binding for a prop.

```javascript
import { useVModel } from 'vue'

const value = useVModel(props, 'value', emit)
```

### 144. What is the useVModels function in Vue 3?
**Answer:** `useVModels` creates multiple two-way bindings for props.

```javascript
import { useVModels } from 'vue'

const { value1, value2 } = useVModels(props, ['value1', 'value2'], emit)
```

### 145. What is the useToggle function in Vue 3?
**Answer:** `useToggle` creates a toggle function for a boolean ref.

```javascript
import { useToggle } from 'vue'

const [value, toggle] = useToggle()
```

### 146. What is the useCounter function in Vue 3?
**Answer:** `useCounter` creates a counter with increment and decrement functions.

```javascript
import { useCounter } from 'vue'

const { count, inc, dec, reset } = useCounter()
```

### 147. What is the useLocalStorage function in Vue 3?
**Answer:** `useLocalStorage` creates a ref that syncs with localStorage.

```javascript
import { useLocalStorage } from 'vue'

const value = useLocalStorage('key', 'default')
```

### 148. What is the useSessionStorage function in Vue 3?
**Answer:** `useSessionStorage` creates a ref that syncs with sessionStorage.

```javascript
import { useSessionStorage } from 'vue'

const value = useSessionStorage('key', 'default')
```

### 149. What is the useMouse function in Vue 3?
**Answer:** `useMouse` tracks mouse position.

```javascript
import { useMouse } from 'vue'

const { x, y } = useMouse()
```

### 150. What is the useKeyboard function in Vue 3?
**Answer:** `useKeyboard` tracks keyboard events.

```javascript
import { useKeyboard } from 'vue'

const { isPressed, key } = useKeyboard()
```

---

## Advanced Concepts (151-200)

### 151. What is Vuex and when should you use it?
**Answer:** Vuex is Vue's official state management library for managing global state in Vue applications. Use it when you need to share state between components that are not directly related.

### 152. What are the core concepts of Vuex?
**Answer:** 
- **State**: The single source of truth for your application's data
- **Getters**: Computed properties for the store
- **Mutations**: Synchronous functions that change state
- **Actions**: Asynchronous functions that commit mutations

### 153. How do you create a Vuex store?
**Answer:** 
```javascript
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    count: 0
  },
  mutations: {
    increment(state) {
      state.count++
    }
  }
})
```

### 154. What is the difference between mutations and actions in Vuex?
**Answer:** 
- **Mutations**: Synchronous, directly modify state
- **Actions**: Asynchronous, commit mutations to modify state

### 155. How do you access Vuex state in components?
**Answer:** Use `this.$store.state` or mapState helper:
```javascript
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState(['count'])
  }
}
```

### 156. What is the mapGetters helper in Vuex?
**Answer:** `mapGetters` is a helper that maps store getters to local computed properties.

### 157. What is the mapMutations helper in Vuex?
**Answer:** `mapMutations` is a helper that maps store mutations to component methods.

### 158. What is the mapActions helper in Vuex?
**Answer:** `mapActions` is a helper that maps store actions to component methods.

### 159. What are Vuex modules?
**Answer:** Vuex modules allow you to split your store into smaller, more manageable pieces.

### 160. How do you create a Vuex module?
**Answer:** 
```javascript
const moduleA = {
  state: { count: 0 },
  mutations: { increment(state) { state.count++ } },
  actions: { incrementAsync({ commit }) { setTimeout(() => commit('increment'), 1000) } },
  getters: { doubleCount: state => state.count * 2 }
}
```

### 161. What is namespacing in Vuex modules?
**Answer:** Namespacing prevents naming conflicts between modules by prefixing all getters, actions, and mutations with the module name.

### 162. What is Vue Router and how does it work?
**Answer:** Vue Router is the official router for Vue.js that allows you to build single-page applications with client-side routing.

### 163. How do you install and configure Vue Router?
**Answer:** 
```javascript
import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About }
]

const router = new VueRouter({ routes })
```

### 164. What are route parameters in Vue Router?
**Answer:** Route parameters are dynamic segments in the URL that can be accessed in components via `this.$route.params`.

### 165. What are query parameters in Vue Router?
**Answer:** Query parameters are optional parameters in the URL that can be accessed via `this.$route.query`.

### 166. What is the difference between $router and $route?
**Answer:** 
- `$router`: The router instance with navigation methods
- `$route`: The current route object with route information

### 167. What are navigation guards in Vue Router?
**Answer:** Navigation guards are functions that control navigation between routes. They can be global, per-route, or in-component.

### 168. What are the types of navigation guards?
**Answer:** 
- **Global guards**: `beforeEach`, `beforeResolve`, `afterEach`
- **Per-route guards**: `beforeEnter`
- **In-component guards**: `beforeRouteEnter`, `beforeRouteUpdate`, `beforeRouteLeave`

### 169. What is lazy loading in Vue Router?
**Answer:** Lazy loading allows you to load components only when they're needed, improving initial load performance.

```javascript
const User = () => import('./views/User.vue')
```

### 170. What is nested routing in Vue Router?
**Answer:** Nested routing allows you to have routes within routes, creating a hierarchy of components.

### 171. What is the difference between push and replace in Vue Router?
**Answer:** 
- `push`: Adds a new entry to the browser history
- `replace`: Replaces the current entry in the browser history

### 172. What is Vue CLI and what does it provide?
**Answer:** Vue CLI is a command-line tool for rapid Vue.js development that provides project scaffolding, build tools, and development server.

### 173. What are Vue CLI plugins?
**Answer:** Vue CLI plugins are packages that can modify the internal webpack configuration and inject commands into `vue-cli-service`.

### 174. What is the vue.config.js file?
**Answer:** `vue.config.js` is a configuration file for Vue CLI projects where you can customize webpack configuration and other build options.

### 175. What is the difference between development and production builds?
**Answer:** 
- **Development**: Includes source maps, hot reloading, and debugging tools
- **Production**: Minified, optimized, and tree-shaken for performance

### 176. What is tree shaking in Vue.js?
**Answer:** Tree shaking is a technique that eliminates dead code from the final bundle, reducing its size.

### 177. What is code splitting in Vue.js?
**Answer:** Code splitting allows you to split your code into smaller chunks that can be loaded on demand.

### 178. What is the difference between async and sync components?
**Answer:** 
- **Sync components**: Loaded immediately when the parent component loads
- **Async components**: Loaded only when needed, improving performance

### 179. What is the defineAsyncComponent function used for?
**Answer:** `defineAsyncComponent` defines an async component that is loaded on demand with loading and error states.

### 180. What is server-side rendering (SSR) in Vue.js?
**Answer:** SSR renders Vue components on the server and sends the rendered HTML to the client, improving SEO and initial page load.

### 181. What is Nuxt.js and how does it relate to Vue.js?
**Answer:** Nuxt.js is a framework built on top of Vue.js that provides SSR, static site generation, and other features out of the box.

### 182. What is static site generation (SSG) in Vue.js?
**Answer:** SSG pre-renders pages at build time, creating static HTML files that can be served directly.

### 183. What is hydration in Vue.js?
**Answer:** Hydration is the process of attaching Vue's reactivity system to server-rendered HTML.

### 184. What is the difference between SSR and CSR?
**Answer:** 
- **SSR**: Renders on server, sends HTML to client
- **CSR**: Renders entirely in the browser

### 185. What is the Vue DevTools?
**Answer:** Vue DevTools is a browser extension that provides debugging and inspection tools for Vue applications.

### 186. What is the difference between Vue 2 and Vue 3?
**Answer:** 
- **Vue 3**: Composition API, better TypeScript support, improved performance, smaller bundle size
- **Vue 2**: Options API, larger bundle size, less TypeScript support

### 187. What is the Composition API in Vue 3?
**Answer:** The Composition API is a new way to organize component logic using functions instead of options, providing better TypeScript support and logic reuse.

### 188. What is the Options API in Vue.js?
**Answer:** The Options API is the traditional way of organizing component logic using options like `data`, `methods`, `computed`, etc.

### 189. What is the difference between Composition API and Options API?
**Answer:** 
- **Composition API**: Function-based, better TypeScript support, logic reuse
- **Options API**: Option-based, easier for beginners, more familiar

### 190. What is the script setup syntax in Vue 3?
**Answer:** `<script setup>` is a compile-time syntactic sugar for using the Composition API inside Single File Components.

### 191. How do you use TypeScript with Vue.js?
**Answer:** Vue 3 has built-in TypeScript support. You can use TypeScript by adding type annotations and using `.ts` or `.vue` files with TypeScript.

### 192. What are Vue.js best practices?
**Answer:** 
- Use meaningful component names
- Keep components small and focused
- Use props for parent-child communication
- Use events for child-parent communication
- Use computed properties for derived state
- Use watchers sparingly
- Follow the single responsibility principle

### 193. What is the difference between v-model and :value + @input?
**Answer:** 
- `v-model`: Two-way binding shorthand
- `:value + @input`: Manual implementation of two-way binding

### 194. What is the difference between $emit and $refs?
**Answer:** 
- `$emit`: Child-to-parent communication
- `$refs`: Direct access to child component methods/properties

### 195. What is the difference between computed and watch?
**Answer:** 
- **Computed**: Derived state, cached, synchronous
- **Watch**: Side effects, not cached, can be asynchronous

### 196. What is the difference between v-for and v-if on the same element?
**Answer:** `v-for` has higher priority than `v-if`, so `v-if` will be evaluated for each item in the loop. It's better to use a computed property or move `v-if` to a wrapper element.

### 197. What is the difference between $nextTick and setTimeout?
**Answer:** 
- `$nextTick`: Waits for Vue's next DOM update cycle
- `setTimeout`: Waits for a specific time delay

### 198. What is the difference between provide/inject and props?
**Answer:** 
- **Props**: Explicit parent-child communication
- **Provide/inject**: Implicit ancestor-descendant communication

### 199. What is the difference between mixins and composition functions?
**Answer:** 
- **Mixins**: Options-based, can cause naming conflicts
- **Composition functions**: Function-based, better TypeScript support, no naming conflicts

### 200. What are the performance optimization techniques in Vue.js?
**Answer:** 
- Use `v-show` instead of `v-if` for frequently toggled elements
- Use `key` attribute with `v-for`
- Use computed properties instead of methods in templates
- Use `v-once` for static content
- Use `v-memo` for conditional rendering optimization
- Lazy load components and routes
- Use production builds
- Implement proper caching strategies

---

## Conclusion

This comprehensive guide covers the most important Vue.js concepts that are commonly asked in interviews. Remember to:

1. **Practice coding**: Implement the concepts you learn
2. **Build projects**: Create real applications to solidify your understanding
3. **Stay updated**: Keep up with the latest Vue.js features and best practices
4. **Understand the ecosystem**: Learn about related tools like Vuex, Vue Router, and Nuxt.js
5. **Master both APIs**: Be comfortable with both Options API and Composition API

Good luck with your Vue.js interviews! 🚀
