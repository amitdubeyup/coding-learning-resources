# Frontend Interview Questions & Answers

## Accessibility & Internationalization

**Q: What are accessibility (a11y) best practices in frontend development?**
A: Accessibility best practices include using semantic HTML, providing alt text for images, ensuring sufficient color contrast, supporting keyboard navigation, using ARIA attributes where necessary, and testing with screen readers. Example: Use `<button>` for actions instead of clickable `<div>`s.

**Q: What are ARIA roles and how do you use them?**
A: ARIA (Accessible Rich Internet Applications) roles and attributes help make web content more accessible to people with disabilities. Use roles like `role="button"` or `role="navigation"` to describe elements' purposes to assistive technologies. Example:
```html
<div role="button" tabindex="0">Click me</div>
```

**Q: How do you test and ensure accessibility in your applications?**
A: Use tools like Lighthouse, axe, or screen readers to audit accessibility. Manual testing with keyboard navigation and color contrast checkers is also important. Integrate accessibility checks into CI/CD pipelines.

**Q: What is internationalization (i18n) and localization (l10n)?**
A: Internationalization is the process of designing a product so it can be adapted to various languages and regions. Localization is the actual adaptation, such as translating text and formatting dates/currencies.

**Q: How do you implement i18n in a React or frontend app?**
A: Use libraries like `react-intl` or `i18next`. Store translations in JSON files and use context or hooks to switch languages. Example with `react-i18next`:
```js
import { useTranslation } from 'react-i18next';
const { t } = useTranslation();
<p>{t('welcome_message')}</p>
```

## React.js

**Q: What is React.js and how is it different from other libraries/frameworks?**
A: React.js is a JavaScript library for building user interfaces, especially single-page applications. It is component-based, uses a virtual DOM for efficient updates, and focuses on the view layer only, unlike frameworks like Angular or Vue.

**Q: What is the difference between Virtual DOM, Shadow DOM, and the real DOM in React?**
A: The real DOM is the browser's document structure. The Virtual DOM is a lightweight JS representation used by React to optimize updates. The Shadow DOM is a browser technology for encapsulating styles and markup, mainly used in Web Components.

**Q: What are controlled and uncontrolled components?**
A: Controlled components have their state managed by React (via props/state), while uncontrolled components store their own state internally (using refs).

**Q: What are the different types of components in React.js?**
A: Functional components (use hooks) and class components (use lifecycle methods). Functional components are now preferred.

**Q: What are hooks in React? List out hooks you have used so far. What are the rules of hooks?**
A: Hooks are functions that let you use state and lifecycle features in functional components. Common hooks: `useState`, `useEffect`, `useContext`, `useMemo`, `useCallback`, `useRef`, `useReducer`. Rules: Only call hooks at the top level and only in React functions.

**Q: Explain `useEffect`, `useState`, `useMemo`, `useCallback`, and `useRef` hooks in detail. What is the difference between useState, useRef, useContext, and useReducer?**
A: `useState` manages local state. `useEffect` runs side effects. `useMemo` memoizes expensive calculations. `useCallback` memoizes functions. `useRef` stores mutable values or DOM refs. `useContext` accesses context. `useReducer` manages complex state logic.

**Q: What is JSX? What is the difference between JSX and TSX? What are Babel and Webpack?**
A: JSX is a syntax extension for JavaScript that looks like HTML and is used in React. TSX is JSX with TypeScript. Babel transpiles JSX/TSX to JS. Webpack bundles modules for deployment.

**Q: What is Redux? Explain reducer, action, store, and Redux Toolkit. How does Redux Toolkit simplify Redux?**
A: Redux is a state management library. The store holds state, actions describe changes, reducers update state. Redux Toolkit simplifies setup and reduces boilerplate.

**Q: What is middleware in Redux? (e.g., Redux-Thunk, Redux-Saga)**
A: Middleware intercepts actions before they reach reducers, enabling async logic, logging, etc. Redux-Thunk allows async functions; Redux-Saga uses generators for complex flows.

**Q: Explain data flow in Redux.**
A: Data flows one way: UI dispatches actions → middleware (optional) → reducers update state → UI re-renders from store.

**Q: What is the difference between class components and function components?**
A: Class components use ES6 classes and lifecycle methods. Function components are simpler, use hooks, and are now preferred.

**Q: How can we implement `componentWillUnmount` in a function component?**
A: Use the cleanup function in `useEffect`:
```js
useEffect(() => {
  // setup
  return () => { /* cleanup */ };
}, []);
```

**Q: Explain lifecycle methods in React. How do functional components handle lifecycle methods?**
A: Class lifecycle methods: `componentDidMount`, `componentDidUpdate`, `componentWillUnmount`. In functions, use `useEffect` for all lifecycle needs.

**Q: What is the difference between `export default` and `export` in React?**
A: `export default` allows a single export per file, imported without curly braces. `export` allows multiple named exports, imported with curly braces.

**Q: What is a portal in React?**
A: Portals render children into a DOM node outside the parent hierarchy. Useful for modals/tooltips.

**Q: What is reconciliation in React?**
A: Reconciliation is React's process of updating the DOM by comparing the new virtual DOM with the previous one and applying minimal changes.

**Q: What is server-side rendering (SSR) in React? What is a React server component?**
A: SSR renders React components on the server and sends HTML to the client, improving performance and SEO. Server components (experimental) allow rendering parts of the UI on the server only.

**Q: What is React.StrictMode in React?**
A: A tool for highlighting potential problems in an app. Wrap components in `<React.StrictMode>` for extra checks.

**Q: What is a fragment in React? Difference between React.Fragment and a div wrapper?**
A: Fragments group multiple elements without adding extra nodes to the DOM. Use `<></>` or `<React.Fragment></React.Fragment>`.

**Q: What is React Router? How do you handle dynamic routing? What is the difference between React Router v5 and v6?**
A: React Router enables navigation between views. v6 uses nested routes and hooks, v5 uses render props. Dynamic routing is handled with route parameters.

**Q: What is a node module in React?**
A: A node module is a package installed via npm/yarn, found in `node_modules/`. React itself is a node module.

**Q: What is the default localhost server port in React.js? How can we change it?**
A: The default port is 3000. Change it by setting the `PORT` environment variable: `PORT=4000 npm start`.

**Q: What is a higher-order component (HOC) in React?**
A: An HOC is a function that takes a component and returns a new component, often for code reuse.

**Q: What is a pure component in React? What is React.memo and how does it work?**
A: Pure components only re-render if props/state change. In classes, extend `React.PureComponent`. In functions, use `React.memo`.

**Q: What is the difference between state and props? How does re-rendering happen when state changes?**
A: State is local and managed within a component. Props are passed from parent to child and are read-only. State changes trigger re-renders.

**Q: How do you optimize a React app? (e.g., memoization, code splitting, lazy loading, avoiding unnecessary re-renders)**
A: Use `React.memo`, `useMemo`, code splitting, lazy loading, and avoid unnecessary state/prop changes.

**Q: What is the difference between React.js and Angular.js?**
A: React is a UI library with one-way data flow and virtual DOM. Angular is a full framework with two-way binding and real DOM.

**Q: What is prop drilling and how do you overcome it? (e.g., Context API, Redux)**
A: Prop drilling is passing props through many layers. Overcome it with Context API, Redux, or state management libraries.

**Q: What is the Context API in React? Difference between Context API and Redux?**
A: Context API shares values between components without prop drilling. Redux is more powerful for global state and complex logic.

**Q: What are `super`, `constructor`, and `render` functions in React?**
A: In class components, `constructor` initializes state, `super` calls the parent constructor, and `render` returns JSX.

**Q: What are styled components? Have you implemented theming in React.js?**
A: Styled Components is a CSS-in-JS library for styling React components. Theming is done via a ThemeProvider and theme objects.

**Q: How do you share data among sibling components?**
A: Use a common parent to manage state, Context API, or a state management library.

**Q: How do you manage form validation, multistep forms, and optimize large forms in React?**
A: Use controlled components, validation libraries (Formik, Yup), and split large forms into smaller components or steps.

**Q: What are keys in React lists and why are they important?**
A: Keys help React identify which items have changed, are added, or are removed. They should be unique and stable.

**Q: What is virtualization in React? How do you optimize rendering of large lists?**
A: Virtualization renders only visible items in a list, improving performance. Use libraries like react-window or react-virtualized.

**Q: How do you avoid unnecessary re-rendering in React?**
A: Use `React.memo`, `useMemo`, `useCallback`, and avoid changing references unnecessarily.

**Q: What is the purpose of error boundaries in React?**
A: Error boundaries catch JavaScript errors in child components and display a fallback UI.

**Q: How do you handle errors in async operations in React?**
A: Use try/catch in async functions, error boundaries for rendering errors, and error states for UI feedback.

**Q: How do you fetch data in React? (e.g., fetch, Axios, retry logic, API key security)**
A: Use `fetch` or Axios in `useEffect` or data-fetching hooks. Store API keys securely (not in code). Implement retry logic with libraries or custom code.

**Q: How do you securely store API keys in React?**
A: Store keys in environment variables and never expose sensitive keys in frontend code.

**Q: How do you identify and fix memory leaks in React?**
A: Clean up subscriptions/timers in `useEffect`, use profiling tools, and avoid retaining references to unmounted components.

**Q: How do you build React applications for production? What is the purpose of the .env file?**
A: Use `npm run build` for optimized builds. `.env` files store environment variables for configuration.

**Q: What is the difference between useEffect and useLayoutEffect?**
A: `useEffect` runs after paint, `useLayoutEffect` runs synchronously after DOM mutations but before paint. Use `useLayoutEffect` for layout reads/writes.

**Q: What is the difference between useCallback and useMemo?**
A: `useCallback` memoizes functions, `useMemo` memoizes values.

**Q: What is a synthetic event in React? Difference between synthetic and real DOM events?**
A: Synthetic events are React's cross-browser wrapper for native events, providing a consistent API.

**Q: How do you pass arguments to event handlers in React?**
A: Use arrow functions or bind in JSX: `<button onClick={() => handleClick(id)} />`.

**Q: What is the difference between lazy loading and code splitting?**
A: Code splitting splits bundles; lazy loading loads code on demand. Both improve performance.

**Q: What is the difference between SSR, CSR, and SSG in React? What is hydration?**
A: SSR renders on the server, CSR on the client, SSG at build time. Hydration attaches event listeners to server-rendered HTML.

**Q: What is the difference between useState and useReducer?**
A: `useState` is for simple state, `useReducer` is for complex state logic or when the next state depends on the previous one.

## HTML

**Q: What is `<!DOCTYPE html>` in HTML5?**
A: It is a declaration that defines the document as HTML5, helping browsers render the page correctly.

**Q: What are semantic HTML elements? Give examples. What are semantic and non-semantic tags?**
A: Semantic elements (e.g., `<header>`, `<main>`, `<footer>`, `<article>`, `<section>`) describe their meaning. Non-semantic tags (e.g., `<div>`, `<span>`) do not.

**Q: What is the difference between block, inline, and inline-block elements? What is the difference between `<div>`, `<span>`, and inline-block elements?**
A: Block elements (e.g., `<div>`, `<p>`) start on a new line. Inline elements (e.g., `<span>`, `<a>`) do not. Inline-block elements flow inline but respect width/height.

**Q: What is the difference between id and class in HTML?**
A: `id` is unique per page, used for single elements. `class` can be shared by multiple elements for styling.

**Q: What is the difference between relative, absolute, and fixed URLs in HTML?**
A: Relative URLs are based on the current path. Absolute URLs include the full path. Fixed URLs is not a standard term; usually refers to absolute URLs.

**Q: What are data-* attributes used for?**
A: Custom attributes for storing extra data on elements, accessible via JavaScript (e.g., `data-user-id`).

**Q: What is the difference between HTML and HTML5? What are HTML5 new features? What is the difference between HTML and XHTML?**
A: HTML5 adds new elements (e.g., `<section>`, `<article>`), APIs (localStorage), and better multimedia support. XHTML is stricter, XML-based, and requires well-formed markup.

**Q: What is the `<iframe>` tag in HTML5?**
A: Embeds another HTML page within the current page. Example:
```html
<iframe src="https://example.com"></iframe>
```

**Q: What are formatting tags in HTML?**
A: Tags like `<b>`, `<i>`, `<strong>`, `<em>`, `<u>`, used to style text.

**Q: What is the difference between `<b>` and `<strong>`?**
A: `<b>` makes text bold visually. `<strong>` also makes text bold but adds semantic importance for accessibility.

**Q: What is the viewport attribute in HTML?**
A: The viewport meta tag controls layout on mobile browsers. Example:
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

**Q: What is an attribute in HTML?**
A: Attributes provide additional information about elements, e.g., `href` in `<a href="...">`.

**Q: Difference between <script>, <script async>, and <script defer>?**
A: `<script>` blocks rendering, `<script async>` loads and executes asynchronously, `<script defer>` loads asynchronously and executes after parsing.

**Q: Difference between <link> and @import for including CSS?**
A: `<link>` is preferred for performance and is parsed before rendering. `@import` is slower and used within CSS files.

**Q: What are meta tags in HTML?**
A: Tags in `<head>` providing metadata (e.g., description, charset, viewport) for browsers and search engines.

**Q: Difference between <canvas> and <svg>?**
A: `<canvas>` is pixel-based, good for dynamic graphics. `<svg>` is vector-based, good for static or interactive graphics.

**Q: What are accessibility (ARIA) attributes? Why are they important?**
A: ARIA attributes (e.g., `aria-label`, `role`) improve accessibility for users with disabilities by providing extra information to assistive technologies.

**Q: Difference between <section>, <article>, <aside>, and <main>?**
A: `<section>` is a thematic grouping, `<article>` is self-contained content, `<aside>` is tangential, `<main>` is the main content area.

## CSS

**Q: What is the difference between CSS and CSS3?**
A: CSS3 is the latest evolution, adding features like media queries, flexbox, grid, and animations.

**Q: What are selectors in CSS?**
A: Selectors target HTML elements to apply styles. Example: `.class`, `#id`, `div > p`.

**Q: What is a media query?**
A: Media queries apply styles based on device characteristics (e.g., width). Example:
```css
@media (max-width: 600px) { body { font-size: 14px; } }
```

**Q: What are the different position values in CSS? (relative, absolute, fixed, sticky)**
A: `static` (default), `relative` (offset from normal), `absolute` (relative to nearest positioned ancestor), `fixed` (relative to viewport), `sticky` (toggles between relative and fixed).

**Q: What is the BOM in CSS?**
A: BOM usually refers to the Browser Object Model (not CSS-specific), but in CSS context, it may be a typo or confusion with DOM.

**Q: What is the difference between px, unit, em, rem, %, vw, vh? Difference between relative and absolute units?**
A: `px` is absolute. `em` is relative to parent font size, `rem` to root font size, `%` to parent, `vw`/`vh` to viewport. Use relative units for responsive design.

**Q: What is Flexbox? What is the difference between Flexbox and CSS Grid?**
A: Flexbox arranges items in a row/column, good for 1D layouts. CSS Grid is for 2D layouts (rows and columns).

**Q: What are pseudo-selectors, pseudo-classes, and pseudo-elements? Give examples.**
A: Pseudo-classes (e.g., `:hover`, `:first-child`) target elements in a state. Pseudo-elements (e.g., `::before`, `::after`) style parts of elements.

**Q: How do you make a website responsive? What are breakpoints for viewport responsive devices? Difference between min-width and max-width in responsive design?**
A: Use fluid layouts, media queries, flexible images, and relative units. Breakpoints: 320px (mobile), 768px (tablet), 1024px (desktop). `min-width` triggers at larger screens, `max-width` at smaller.

**Q: Why do we use `box-sizing` in CSS?**
A: `box-sizing: border-box` includes padding and border in an element's total width/height, making layouts easier to manage.

**Q: What is the difference between inline, internal, and external CSS?**
A: Inline: in the element (`style` attribute). Internal: in `<style>` in `<head>`. External: in separate `.css` files.

**Q: What is z-index and how does it work?**
A: `z-index` controls stacking order of positioned elements. Higher values appear above lower ones.

**Q: Explain the concept of CSS Specificity.**
A: Specificity determines which CSS rule applies if multiple match. Inline > ID > class/attribute > element.

**Q: What is the difference between visibility: hidden and display: none?**
A: `visibility: hidden` hides the element but keeps its space. `display: none` removes it from the layout.

**Q: What is the difference between transform, transition, and animation in CSS?**
A: `transform` changes shape/position. `transition` animates property changes. `animation` defines keyframes for complex animations.

**Q: What is the difference between relative path vs absolute path in CSS?**
A: Relative paths are based on the current file location. Absolute paths start from the root or include the full URL.

**Q: Difference between inline styles and CSS classes in React?**
A: Inline styles are JS objects in the `style` prop. CSS classes use the `className` prop and external stylesheets.

**Q: Difference between CSS BEM methodology and normal CSS?**
A: BEM (Block Element Modifier) is a naming convention for classes to avoid conflicts and improve maintainability.

## JavaScript & TypeScript

**Q: What is ECMAScript? What are ES5 and ES6 features?**
A: ECMAScript is the standard JavaScript implements. ES5/ES6 introduced features like `let`, `const`, arrow functions, classes, modules, and more.

**Q: What is the difference between `let`, `const`, and `var`? What is the difference between == and ===?**
A: `let`/`const` are block-scoped, `var` is function-scoped. `const` cannot be reassigned. `==` compares values with type coercion, `===` compares value and type.

**Q: What are primitive and non-primitive data types?**
A: Primitive: string, number, boolean, null, undefined, symbol, bigint. Non-primitive: objects, arrays, functions.

**Q: What are the spread operator, rest operator, and default parameters?**
A: Spread (`...arr`) expands arrays/objects. Rest (`...args`) collects arguments into an array. Default parameters set fallback values in functions.

**Q: What is deep copy and shallow copy? Difference between mutable and immutable data in JS?**
A: Shallow copy copies references to nested objects; deep copy duplicates all levels. Mutable data can be changed, immutable cannot.

**Q: What are promises, callback functions, and async/await? What is promise chaining? Give an example.**
A: Promises represent future values. Callbacks are functions passed as arguments. `async/await` simplifies promises. Chaining: `promise.then().then()...`.

**Q: What is the difference between promises and callbacks? What are promise methods (all, race, any, allSettled)? What is the difference between promise.race and promise.any?**
A: Promises avoid callback hell and make async code easier to read. `Promise.all` waits for all, `race` for first, `any` for first fulfilled, `allSettled` for all to settle.

**Q: What is callback hell? How can it be avoided? What are the use cases for callback functions?**
A: Callback hell is deeply nested callbacks. Avoid with promises, async/await, or modular code. Use cases: event handlers, async operations.

**Q: What is event bubbling and event capturing? What is event delegation and event handling?**
A: Bubbling: event propagates from child to parent. Capturing: parent to child. Delegation: handle events at a parent for dynamic children.

**Q: What is a higher-order function?**
A: A function that takes or returns another function. Example: `Array.prototype.map`.

**Q: Explain different types of functions in JavaScript (declaration, expression, arrow, constructor, generator, IIFE).**
A: Declaration: `function foo() {}`. Expression: `const foo = function() {}`. Arrow: `() => {}`. Constructor: `function Foo() {}`. Generator: `function* foo() {}`. IIFE: `(function(){})()`.

**Q: What is an arrow function and how is it different from normal functions?**
A: Arrow functions are concise, do not have their own `this`, and cannot be used as constructors.

**Q: Why do we use `call`, `apply`, and `bind` methods? Difference between call, apply, and bind with example.**
A: They set the `this` context. `call`/`apply` invoke immediately, `bind` returns a new function. `call`/`apply` differ in argument passing.

**Q: How many ways can you create an object in JavaScript? What is the difference between class and constructor function?**
A: Object literals, constructors, `Object.create`, classes, factory functions. Classes are syntactic sugar over constructor functions.

**Q: What is prototype and prototype inheritance? Difference between prototype and __proto__?**
A: Objects inherit from their prototype. `prototype` is on constructors, `__proto__` is on instances.

**Q: What is TypeScript?**
A: TypeScript is a superset of JavaScript that adds static typing, interfaces, and advanced tooling.

**Q: What are common array and string methods? Difference between map(), forEach(), filter(), and reduce()? What is the difference between forEach and map?**
A: Array: `map`, `filter`, `reduce`, `forEach`, `find`. String: `split`, `replace`, `toUpperCase`, `includes`. `map` returns a new array, `forEach` does not.

**Q: What is the difference between Java and JavaScript?**
A: Java is a statically typed, compiled language. JavaScript is dynamically typed and interpreted in browsers.

**Q: What are throttling and debouncing?**
A: Throttling limits function calls to once per interval. Debouncing delays execution until a pause in events.

**Q: What is `null` and `undefined`? Difference between null and undefined?**
A: `null` is an assigned value meaning "no value". `undefined` means a variable has been declared but not assigned.

**Q: What are falsy values?**
A: Values that evaluate to false: `false`, `0`, `''`, `null`, `undefined`, `NaN`.

**Q: What is execution context, event loop, stack, call queue, and microtask queue? Explain the event loop in Node.js.**
A: Execution context is the environment for code execution. The event loop manages the call stack and queues, handling async code. Node.js event loop phases: timers, I/O callbacks, idle, poll, check, close callbacks.

**Q: What are `setTimeout` and `setInterval`?**
A: `setTimeout` runs code after a delay. `setInterval` runs code repeatedly at intervals.

**Q: What are `Object.seal` and `Object.freeze`?**
A: `Object.seal` prevents adding/removing properties. `Object.freeze` makes an object immutable.

**Q: What is the difference between `Map` and `Set`?**
A: `Map` stores key-value pairs. `Set` stores unique values.

**Q: What are `WeakMap` and `WeakSet`?**
A: Like `Map`/`Set`, but keys/values are weakly referenced, allowing garbage collection.

**Q: What are `sessionStorage`, `localStorage`, and cookies? Difference between localStorage, sessionStorage, and cookies?**
A: All store data in the browser. `localStorage` persists, `sessionStorage` lasts per tab, cookies are sent to the server.

**Q: Write a program to sort an array.**
A:
```js
const arr = [3, 1, 2];
arr.sort((a, b) => a - b);
```

**Q: What is the use of `JSON.stringify` and `JSON.parse()`? What is the difference between JSON and JavaScript objects?**
A: `JSON.stringify` converts objects to JSON strings. `JSON.parse` parses JSON strings to objects. JSON is a data format, JS objects are in-memory structures.

**Q: What is a generator function?**
A: A function that can pause and resume execution using `function*` and `yield`.

**Q: How do you stop event propagation?**
A: Use `event.stopPropagation()` in an event handler.

**Q: What is a closure? Explain with examples.**
A: A function that remembers its lexical scope even when called outside that scope.

**Q: What is hoisting in JavaScript?**
A: Variable and function declarations are moved to the top of their scope before code execution.

**Q: What is the temporal dead zone?**
A: The period between entering scope and variable declaration with `let`/`const` where the variable cannot be accessed.

**Q: What is function currying?**
A: Transforming a function with multiple arguments into a sequence of functions each taking a single argument.

**Q: What is a mutation observer?**
A: An API to watch for changes in the DOM tree.

**Q: What is memoization? Explain memorization concepts in JavaScript with examples.**
A: Caching function results to optimize performance for repeated calls with the same arguments.

**Q: What is the Nullish coalescing operator (??)?**
A: Returns the right-hand operand when the left is `null` or `undefined`. Example: `a ?? b`.

**Q: What is an IIFE (Immediately Invoked Function Expression)?**
A: A function that runs as soon as it is defined: `(function(){ ... })();`

**Q: What is the immutability concept in JavaScript?**
A: Immutability means data cannot be changed after creation. Use `Object.freeze`, spread operator, or libraries like Immutable.js.

**Q: What is code splitting in JavaScript?**
A: Splitting code into smaller bundles loaded on demand, improving performance.

**Q: What is strict mode in JavaScript?**
A: A way to opt in to a restricted variant of JS, catching common errors. Use `'use strict';` at the top of a file or function.

**Q: What are design patterns in JavaScript?**
A: Reusable solutions to common problems, e.g., Singleton, Observer, Factory, Module.

**Q: What is the difference between for...in and for...of loops?**
A: `for...in` iterates over keys, `for...of` over values (iterables).

**Q: What is the difference between DOM and BOM?**
A: DOM is the document structure, BOM is browser-specific objects (window, navigator).

**Q: Difference between innerHTML and innerText?**
A: `innerHTML` gets/sets HTML content, `innerText` gets/sets visible text only.

**Q: What is the difference between import and require?**
A: `import` is ES6 module syntax, static and hoisted. `require` is CommonJS, dynamic.

**Q: What is the difference between REST API and GraphQL in frontend usage?**
A: REST uses endpoints for resources, GraphQL lets clients specify data shape in a single query.

**Q: What is the difference between functional programming and OOP in JS?**
A: Functional programming emphasizes pure functions and immutability. OOP uses objects and classes.

## Team Leadership, Code Quality, and General Frontend Architecture

**Q: How do you ensure code quality in a team?**
A: Use code reviews, automated testing, linters, and enforce coding standards. Encourage knowledge sharing and pair programming.

**Q: What is the importance of code reviews?**
A: Code reviews catch bugs, improve code quality, share knowledge, and ensure consistency across the team.

**Q: How do you handle conflicts in a team?**
A: Address issues early, listen to all perspectives, focus on solutions, and involve a neutral party if needed.

**Q: How do you mentor junior developers?**
A: Provide guidance, encourage questions, pair program, give constructive feedback, and set clear goals.

**Q: What is the role of documentation in a project?**
A: Documentation helps onboard new team members, clarifies requirements, and ensures maintainability.

**Q: What is CI/CD?**
A: Continuous Integration/Continuous Deployment automates building, testing, and deploying code, improving reliability and speed.

**Q: What is the difference between unit, integration, and end-to-end testing?**
A: Unit tests check individual functions, integration tests check interactions between modules, end-to-end tests simulate user flows.

**Q: What is TDD (Test Driven Development)?**
A: Write tests before code, then implement code to pass tests, ensuring better design and fewer bugs.

**Q: What is the importance of version control?**
A: Version control (e.g., Git) tracks changes, enables collaboration, and allows rollback to previous states.

**Q: What is the difference between monolithic and microservices architecture?**
A: Monolithic: single codebase, tightly coupled. Microservices: independent services, loosely coupled, scalable.

**Q: What is server-side rendering (SSR) and client-side rendering (CSR)?**
A: SSR renders HTML on the server, improving SEO and initial load. CSR renders in the browser, enabling dynamic UIs.

**Q: What is a Single Page Application (SPA)?**
A: An SPA loads a single HTML page and updates content dynamically via JavaScript, without full page reloads.

**Q: What is Progressive Web App (PWA)?**
A: PWAs use modern web capabilities to deliver app-like experiences, including offline support and push notifications.

**Q: What is the difference between mobile-first and desktop-first design?**
A: Mobile-first prioritizes mobile layouts, then scales up. Desktop-first starts with desktop and adapts down.

**Q: What is accessibility (a11y) in web development?**
A: Making web apps usable by people with disabilities, e.g., using semantic HTML, ARIA attributes, keyboard navigation.

**Q: What is internationalization (i18n) and localization (l10n)?**
A: i18n prepares apps for multiple languages/cultures. l10n adapts content for specific locales.

**Q: What is the difference between functional and class components in React?**
A: Functional components are stateless and use hooks. Class components use lifecycle methods and state.

**Q: What is the importance of performance optimization in frontend?**
A: Improves user experience, SEO, and reduces bounce rates. Techniques: code splitting, lazy loading, caching, minimizing assets.

**Q: What is a design system?**
A: A collection of reusable components, guidelines, and assets for consistent UI/UX across products.

**Q: What is the difference between UI and UX?**
A: UI is the look and feel; UX is the overall experience and usability.

## Performance, Security, and General Tools

**Q: How do you optimize frontend performance?**
A: Minimize assets, use lazy loading, code splitting, caching, compress images, and reduce render-blocking resources.

**Q: What is lazy loading?**
A: Loading resources only when needed, e.g., images or components as they enter the viewport.

**Q: What is code splitting?**
A: Breaking code into smaller bundles loaded on demand, improving initial load time.

**Q: What is caching?**
A: Storing data locally (browser, CDN) to reduce server requests and speed up load times.

**Q: What is a CDN?**
A: Content Delivery Network distributes assets across global servers for faster delivery to users.

**Q: What is XSS (Cross-Site Scripting)?**
A: A security vulnerability where attackers inject malicious scripts into web pages viewed by others. Prevent by sanitizing inputs and using secure APIs.

**Q: What is CSRF (Cross-Site Request Forgery)?**
A: An attack tricking users into submitting unwanted actions. Prevent with tokens, same-site cookies, and proper authentication.

**Q: What is HTTPS and why is it important?**
A: HTTPS encrypts data between browser and server, ensuring privacy and security.

**Q: What is OAuth?**
A: OAuth is an open standard for access delegation, allowing users to grant third-party access without sharing credentials.

**Q: What is Webpack?**
A: Webpack is a module bundler for JavaScript applications, managing dependencies and optimizing assets.

**Q: What is Babel?**
A: Babel is a JavaScript compiler that converts modern JS code into backward-compatible versions for older browsers.

**Q: What is ESLint?**
A: ESLint is a tool for identifying and fixing problems in JavaScript code, enforcing coding standards.

**Q: What is Prettier?**
A: Prettier is an opinionated code formatter for consistent code style.

**Q: What is npm/yarn?**
A: Package managers for installing, updating, and managing project dependencies.

**Q: What is Git?**
A: Git is a distributed version control system for tracking code changes and collaboration.

**Q: What is Docker?**
A: Docker packages applications and dependencies into containers for consistent deployment across environments.

**Q: What is the difference between development, staging, and production environments?**
A: Development: for coding/testing. Staging: pre-production, simulates production. Production: live for users.

**Q: What is the difference between manual and automated testing?**
A: Manual: testers execute tests. Automated: scripts run tests, faster and repeatable.

**Q: What is the difference between black-box and white-box testing?**
A: Black-box: tests without internal knowledge. White-box: tests with knowledge of code structure.

**Q: What is the difference between smoke, regression, and sanity testing?**
A: Smoke: basic checks. Regression: ensure new changes don't break existing features. Sanity: quick checks after minor changes.

## Miscellaneous and General

**Q: What is the difference between frontend and backend development?**
A: Frontend is the client-side (UI/UX), backend is the server-side (logic, database, APIs).

**Q: What is API?**
A: API (Application Programming Interface) allows communication between different software systems.

**Q: What is the difference between synchronous and asynchronous programming?**
A: Synchronous: tasks run one after another. Asynchronous: tasks can run independently, not blocking the main thread.

**Q: What is the difference between authentication and authorization?**
A: Authentication verifies identity, authorization grants access to resources.

**Q: What is the difference between GET and POST requests?**
A: GET retrieves data, POST sends data to the server.

**Q: What is the difference between HTTP and HTTPS?**
A: HTTPS is HTTP with encryption (SSL/TLS) for secure communication.

**Q: What is the difference between cookies and sessions?**
A: Cookies store data on the client, sessions store data on the server.

**Q: What is the difference between SQL and NoSQL?**
A: SQL: structured, relational, uses tables. NoSQL: flexible, non-relational, uses documents, key-value, etc.

**Q: What is the difference between scaling vertically and horizontally?**
A: Vertical: add resources to a single server. Horizontal: add more servers.

**Q: What is cloud computing?**
A: Delivery of computing services (servers, storage, databases, networking, software) over the internet.

**Q: What is SaaS, PaaS, and IaaS?**
A: SaaS: Software as a Service (apps over internet). PaaS: Platform as a Service (tools for developers). IaaS: Infrastructure as a Service (virtualized computing resources).

**Q: What is DevOps?**
A: Practices that combine software development and IT operations to shorten development cycles and improve reliability.

**Q: What is Agile methodology?**
A: Iterative approach to software development with frequent releases, collaboration, and adaptability.

**Q: What is Scrum?**
A: Agile framework with defined roles, events, and artifacts for managing complex projects.

**Q: What is Kanban?**
A: Visual workflow management method for tracking tasks and optimizing flow.

**Q: What is MVP (Minimum Viable Product)?**
A: The simplest version of a product that can be released to validate an idea and get user feedback.

**Q: What is the difference between waterfall and agile methodologies?**
A: Waterfall is linear and sequential, agile is iterative and flexible.

**Q: What is the difference between a library and a framework?**
A: Library: collection of functions you call. Framework: provides structure and calls your code.

**Q: What is open source?**
A: Software with source code available for anyone to view, modify, and distribute.

**Q: What is the importance of soft skills in software development?**
A: Soft skills (communication, teamwork, problem-solving) are essential for collaboration and project success.
