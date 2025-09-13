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

**Q: What is React.js?**
A: React.js is a JavaScript library for building user interfaces, especially single-page applications. It uses a component-based architecture and a virtual DOM for efficient rendering.

**Q: What is the difference between Virtual DOM, Shallow DOM, and the regular DOM in React?**
A: The regular DOM is the browser's document structure. The Virtual DOM is a lightweight JS representation of the DOM used by React to optimize updates. Shallow rendering (Shallow DOM) is a testing concept where only the component itself is rendered, not its children.

**Q: What are controlled and uncontrolled components?**
A: Controlled components have their state managed by React (via props/state), while uncontrolled components store their own state internally (using refs). Example:
```js
// Controlled
<input value={value} onChange={e => setValue(e.target.value)} />
// Uncontrolled
<input ref={inputRef} />
```

**Q: What are hooks in React?**
A: Hooks are functions that let you use state and lifecycle features in functional components. Common hooks: `useState`, `useEffect`, `useContext`, `useMemo`, `useCallback`.

**Q: Explain `useEffect`, `useState`, `useMemo`, and `useCallback` hooks in detail.**
A:
- `useState` manages local state.
- `useEffect` runs side effects (e.g., data fetching, subscriptions).
- `useMemo` memoizes expensive calculations.
- `useCallback` memoizes callback functions to prevent unnecessary re-renders.
Example:
```js
const [count, setCount] = useState(0);
useEffect(() => { document.title = `Count: ${count}`; }, [count]);
const expensiveValue = useMemo(() => computeExpensive(count), [count]);
const handleClick = useCallback(() => setCount(c => c + 1), []);
```

**Q: What is JSX? What are Babel and Webpack?**
A: JSX is a syntax extension for JavaScript that looks like HTML and is used in React. Babel is a JS compiler that transpiles JSX and modern JS to browser-compatible code. Webpack is a module bundler for JS applications.

**Q: What is Redux? Explain reducer, action, and store in Redux.**
A: Redux is a state management library. The store holds the state, actions describe state changes, and reducers are pure functions that update the state based on actions.

**Q: What is middleware in Redux?**
A: Middleware in Redux intercepts actions before they reach the reducer, allowing for async logic, logging, etc. Example: `redux-thunk`, `redux-saga`.

**Q: Explain data flow in Redux.**
A: Data flows in one direction: UI dispatches actions → middleware (optional) → reducers update state → UI re-renders from store.

**Q: What is Redux-Thunk? What is Redux-Saga? Difference between Redux-Thunk and Redux-Saga.**
A: Redux-Thunk is middleware for async logic using functions (thunks). Redux-Saga uses generator functions for more complex async flows. Sagas are better for handling side effects and complex async logic.

**Q: What is the difference between class components and function components?**
A: Class components use ES6 classes and can have lifecycle methods. Function components are simpler and use hooks for state/lifecycle. Example:
```js
// Class
class MyComponent extends React.Component { render() { return <div>Hello</div>; } }
// Function
function MyComponent() { return <div>Hello</div>; }
```

**Q: How can we implement `componentWillUnmount` in a function component?**
A: Use the cleanup function in `useEffect`:
```js
useEffect(() => {
  // setup
  return () => { /* cleanup */ };
}, []);
```

**Q: Explain lifecycle methods in React.**
A: Lifecycle methods are hooks into component creation, update, and destruction. Examples: `componentDidMount`, `componentDidUpdate`, `componentWillUnmount` (class); `useEffect` (function).

**Q: What is the difference between `export default` and `export` in React?**
A: `export default` allows a single export per file, imported without curly braces. `export` allows multiple named exports, imported with curly braces.

**Q: What is a portal in React?**
A: Portals let you render children into a DOM node outside the parent component hierarchy. Useful for modals, tooltips.
```js
ReactDOM.createPortal(<Modal />, document.getElementById('modal-root'));
```

**Q: What is reconciliation in React?**
A: Reconciliation is the process React uses to update the DOM by comparing the new virtual DOM with the previous one and applying minimal changes.

**Q: What is `useRef` in React?**
A: `useRef` returns a mutable ref object whose `.current` property persists across renders. Used for accessing DOM nodes or storing mutable values.

**Q: What is server-side rendering (SSR) in React?**
A: SSR renders React components on the server and sends HTML to the client, improving performance and SEO. Example: Next.js.

**Q: What is `useStrict` in React?**
A: Likely refers to `StrictMode`, a tool for highlighting potential problems in an app. Wrap components in `<React.StrictMode>` for extra checks.

**Q: What is a fragment in React?**
A: Fragments let you group multiple elements without adding extra nodes to the DOM. Example: `<></>` or `<React.Fragment></React.Fragment>`.

**Q: What is React Router?**
A: React Router is a library for routing in React apps. It enables navigation between views and supports dynamic routing.

**Q: What is a node module in React?**
A: A node module is a package installed via npm/yarn, often found in `node_modules/`. React itself is a node module.

**Q: What is the default localhost server port in React.js? How can we change it?**
A: The default port is 3000. Change it by setting the `PORT` environment variable: `PORT=4000 npm start`.

**Q: What is a higher-order component (HOC) in React?**
A: An HOC is a function that takes a component and returns a new component, often used for code reuse. Example:
```js
function withLogger(WrappedComponent) {
  return function(props) {
    console.log('Rendering');
    return <WrappedComponent {...props} />;
  };
}
```

**Q: What is a pure component in React?**
A: A pure component only re-renders if its props/state change. In class components, extend `React.PureComponent`.

**Q: What is the difference between state and props?**
A: State is local and managed within a component. Props are passed from parent to child and are read-only.

**Q: How do you optimize a React app?**
A: Use memoization (`React.memo`, `useMemo`), code splitting, lazy loading, avoid unnecessary re-renders, and use production builds.

**Q: What is the difference between React.js and Angular.js?**
A: React is a library focused on UI, uses virtual DOM, and is component-based. Angular is a full framework, uses real DOM, and has two-way data binding.

**Q: What is prop drilling and how do you overcome it?**
A: Prop drilling is passing props through many layers. Overcome it with Context API, Redux, or state management libraries.

**Q: What is the Context API in React?**
A: The Context API provides a way to share values between components without passing props manually at every level.

**Q: What are `super`, `constructor`, and `render` functions in React?**
A: In class components, `constructor` initializes state, `super` calls the parent constructor, and `render` returns JSX.

## HTML

**Q: What is `<!DOCTYPE html>` in HTML5?**
A: It is a declaration that defines the document as HTML5, helping browsers render the page correctly.

**Q: What is the difference between `<div>` and `<span>`?**
A: `<div>` is a block-level element (starts on a new line), while `<span>` is inline (does not break the flow). Use `<div>` for layout, `<span>` for styling inline text.

**Q: What are semantic and non-semantic tags?**
A: Semantic tags (e.g., `<header>`, `<main>`, `<footer>`) describe their meaning. Non-semantic tags (e.g., `<div>`, `<span>`) do not.

**Q: What is the difference between HTML and HTML5?**
A: HTML5 is the latest version, introducing new elements (like `<section>`, `<article>`), APIs (like localStorage), and better multimedia support.

**Q: What is the `<iframe>` tag in HTML5?**
A: It embeds another HTML page within the current page. Example:
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

**Q: What are block-level and inline elements?**
A: Block-level elements (e.g., `<div>`, `<p>`) start on a new line. Inline elements (e.g., `<span>`, `<a>`) do not.

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

**Q: What are the different position values in CSS?**
A: `static`, `relative`, `absolute`, `fixed`, `sticky`. Each controls how an element is positioned in the document flow.

**Q: What is the BOM in CSS?**
A: BOM usually refers to the Browser Object Model (not CSS-specific), but in CSS context, it may be a typo or confusion with DOM.

**Q: What is the difference between px, unit, em, and rem?**
A: `px` is pixels, `em` is relative to the parent font size, `rem` is relative to the root font size, and `%` is relative to the parent element.

**Q: What is Flexbox?**
A: Flexbox is a CSS layout model for arranging items in a row or column, supporting alignment, spacing, and reordering.

**Q: What are pseudo-selectors?**
A: Pseudo-selectors (e.g., `:hover`, `:first-child`) target elements in a specific state or position.

**Q: How do you make a website responsive?**
A: Use fluid layouts, media queries, flexible images, and relative units (em, rem, %).

**Q: What are breakpoints for viewport responsive devices?**
A: Common breakpoints: 320px (mobile), 768px (tablet), 1024px (desktop), but should be based on your audience/devices.

**Q: Why do we use `box-sizing` in CSS?**
A: `box-sizing: border-box` includes padding and border in an element's total width/height, making layouts easier to manage.

**Q: What are CSS-in-JS solutions? (e.g., Styled Components, Emotion)**
A: CSS-in-JS lets you write CSS in JavaScript files, enabling dynamic styling and scoped styles. Example with Styled Components:
```js
const Button = styled.button` color: red; `;
```

**Q: How do you handle animations in frontend (CSS transitions, Framer Motion, GSAP)?**
A: Use CSS transitions/animations for simple effects, or libraries like Framer Motion (React) and GSAP for complex animations.

**Q: What are the pros and cons of using CSS modules vs. global CSS?**
A: CSS modules scope styles locally, preventing conflicts. Global CSS is easier for shared styles but can cause naming collisions.

## JavaScript & TypeScript

**Q: What is ECMAScript?**
A: ECMAScript is the standard that JavaScript implements. ES6/ES2015 introduced features like `let`, `const`, arrow functions, classes.

**Q: What is the difference between `let`, `const`, and `var`?**
A: `let` and `const` are block-scoped; `var` is function-scoped. `const` cannot be reassigned.

**Q: What are the spread operator, rest operator, and default parameters?**
A: Spread (`...arr`) expands arrays/objects. Rest (`...args`) collects arguments into an array. Default parameters set fallback values in functions.
```js
function sum(a = 1, b = 2) { return a + b; }
```

**Q: What is deep copy and shallow copy?**
A: Shallow copy copies references to nested objects; deep copy duplicates all levels. Example:
```js
const shallow = [...arr];
const deep = JSON.parse(JSON.stringify(obj));
```

**Q: What are promises, callback functions, and async/await?**
A: Promises represent future values. Callbacks are functions passed as arguments. `async/await` simplifies working with promises.

**Q: What is the difference between promises and callbacks?**
A: Promises avoid callback hell and make async code easier to read and chain.

**Q: What is event bubbling and event capturing?**
A: Bubbling: event propagates from child to parent. Capturing: from parent to child. Use `event.stopPropagation()` to stop.

**Q: What is a higher-order function?**
A: A function that takes or returns another function. Example: `Array.prototype.map`.

**Q: Explain different types of functions in JavaScript.**
A: Function declarations, expressions, arrow functions, constructor functions, generator functions.

**Q: What is an arrow function?**
A: A concise function syntax: `const add = (a, b) => a + b;`. Does not have its own `this`.

**Q: Why do we use `call`, `apply`, and `bind` methods?**
A: They set the `this` context for functions. `call` and `apply` invoke immediately; `bind` returns a new function.

**Q: How many ways can you create an object in JavaScript?**
A: Object literals, constructors, `Object.create`, classes, and factory functions.

**Q: What is prototype inheritance?**
A: Objects inherit properties/methods from their prototype. Example:
```js
function Animal() {}
Animal.prototype.speak = function() { console.log('hi'); };
```

**Q: What is TypeScript?**
A: TypeScript is a superset of JavaScript that adds static typing, interfaces, and advanced tooling.

**Q: What are common array and string methods?**
A: Array: `map`, `filter`, `reduce`, `forEach`, `find`. String: `split`, `replace`, `toUpperCase`, `includes`.

**Q: What is the difference between Java and JavaScript?**
A: Java is a statically typed, compiled language. JavaScript is dynamically typed and interpreted in browsers.

**Q: What are throttling and debouncing?**
A: Throttling limits function calls to once per interval. Debouncing delays execution until a pause in events.

**Q: What is `null` and `undefined`?**
A: `null` is an assigned value meaning "no value". `undefined` means a variable has been declared but not assigned.

**Q: What are falsy values?**
A: Values that evaluate to false: `false`, `0`, `''`, `null`, `undefined`, `NaN`.

**Q: What is execution context, event loop, stack, call queue, and microtask queue?**
A: Execution context is the environment for code execution. The event loop manages the call stack and queues, handling async code.

**Q: What are `setTimeout` and `setInterval`?**
A: `setTimeout` runs code after a delay. `setInterval` runs code repeatedly at intervals.

**Q: What are `Object.seal` and `Object.freeze`?**
A: `Object.seal` prevents adding/removing properties. `Object.freeze` makes an object immutable.

**Q: What is the difference between `Map` and `Set`?**
A: `Map` stores key-value pairs. `Set` stores unique values.

**Q: What are `WeakMap` and `WeakSet`?**
A: Like `Map`/`Set`, but keys/values are weakly referenced, allowing garbage collection.

**Q: What are `sessionStorage`, `localStorage`, and cookies?**
A: All store data in the browser. `localStorage` persists, `sessionStorage` lasts per tab, cookies are sent to the server.

**Q: Write a program to sort an array.**
A:
```js
const arr = [3, 1, 2];
arr.sort((a, b) => a - b);
```

**Q: What is the use of `JSON.stringify` and `JSON.parse()`?**
A: `JSON.stringify` converts objects to JSON strings. `JSON.parse` parses JSON strings to objects.

**Q: What are `map`, `filter`, and `reduce` in JavaScript?**
A: Array methods for transforming, filtering, and reducing arrays.

**Q: What is a generator function?**
A: A function that can pause and resume execution using `function*` and `yield`.

**Q: How do you stop event propagation?**
A: Use `event.stopPropagation()` in an event handler.

**Q: What is a closure?**
A: A function that remembers its lexical scope even when called outside that scope.

**Q: What is hoisting in JavaScript?**
A: Variable and function declarations are moved to the top of their scope before code execution.

**Q: What is the temporal dead zone?**
A: The period between entering scope and variable declaration with `let`/`const` where the variable cannot be accessed.

**Q: What is function currying?**
A: Transforming a function with multiple arguments into a sequence of functions each taking a single argument.

**Q: What is a mutation observer?**
A: An API to watch for changes in the DOM tree.

**Q: What is memoization?**
A: Caching function results to optimize performance for repeated calls with the same arguments.

**Q: How do you handle browser compatibility and polyfills?**
A: Use feature detection, transpilers (Babel), and polyfills (core-js) to support older browsers.

**Q: What are web components and custom elements?**
A: Web components are reusable custom elements with encapsulated functionality, created using the Custom Elements API.

## Frontend Architecture & Design Patterns

**Q: How do you architect a micro-frontend system with independent deployments?**
A: Use separate build and deployment pipelines for each micro-frontend. Integrate them at runtime using module federation, iframes, or a shell app. Ensure clear contracts and shared dependencies are managed.

**Q: Explain the trade-offs between different state management patterns (Redux, Zustand, Context API).**
A: Redux is powerful for large apps but can be verbose. Zustand is simpler and more flexible. Context API is good for small-scale state sharing but can cause unnecessary re-renders if overused.

**Q: How do you implement a design system that scales across multiple teams?**
A: Use a component library (e.g., Storybook), document usage, enforce versioning, and provide clear contribution guidelines. Use tools like Figma for design tokens.

**Q: What's your approach to handling shared dependencies in a monorepo?**
A: Use a monorepo tool (e.g., Nx, Lerna, Turborepo) to manage packages. Deduplicate dependencies and use version constraints. Automate builds and tests.

**Q: How do micro-frontends communicate with each other?**
A: Use custom events, shared state containers, or a message bus. Avoid tight coupling by using well-defined interfaces.

**Q: How do you manage state normalization and entity management?**
A: Normalize state using libraries like normalizr or Redux Toolkit. Store entities by ID and reference them to avoid duplication and simplify updates.

## Advanced React & Performance

**Q: How do you implement server-side rendering with hydration for complex applications?**
A: Use frameworks like Next.js. Render HTML on the server, send it to the client, and hydrate with React to attach event listeners.

**Q: Explain React 18's concurrent features and how they impact application architecture.**
A: React 18 introduces concurrent rendering, allowing React to interrupt and resume rendering. Features like `startTransition` and automatic batching improve responsiveness.

**Q: How do you optimize bundle splitting for maximum performance across different routes?**
A: Use dynamic imports and React.lazy to split code by route. Tools like Webpack and Vite support code splitting out of the box.

**Q: What strategies do you use for implementing efficient data fetching patterns?**
A: Use SWR, React Query, or custom hooks for caching, deduplication, and background updates. Prefer server-side data fetching for critical data.

**Q: How do you use Lighthouse and Core Web Vitals for performance optimization?**
A: Run Lighthouse audits to identify bottlenecks. Monitor Core Web Vitals (LCP, FID, CLS) and optimize images, scripts, and rendering paths.

**Q: What are common frontend security concerns (XSS, CSRF, CSP) and how do you mitigate them?**
A: Prevent XSS by escaping user input, use CSRF tokens for forms, and set Content Security Policy headers. Validate and sanitize all inputs.

**Q: How do you use Service Workers and caching strategies for performance and offline support?**
A: Register a Service Worker to cache assets and API responses. Use strategies like cache-first for static assets and network-first for dynamic data.

**Q: What is static site generation (e.g., Next.js, Gatsby) and when would you use it?**
A: Static site generation builds HTML at compile time, serving fast, static pages. Use for blogs, docs, or sites with infrequent updates.

## Build Systems & Developer Experience

**Q: How do you design a CI/CD pipeline for frontend applications with multiple environments?**
A: Use tools like GitHub Actions, GitLab CI, or Jenkins. Automate linting, testing, building, and deployment. Use environment variables for config.

**Q: What's your approach to implementing feature flags in large frontend applications?**
A: Use a feature flag service (e.g., LaunchDarkly, Unleash) or a custom solution. Flags should be dynamic and support gradual rollouts.

**Q: How do you set up monitoring and error tracking for production frontend apps?**
A: Integrate tools like Sentry, LogRocket, or Datadog. Capture errors, performance metrics, and user sessions for debugging.

**Q: Explain your strategy for A/B testing in React applications.**
A: Use a testing platform or custom logic to split users into groups. Render different components or features and track metrics to determine effectiveness.

**Q: What are the basics of configuring Webpack, Rollup, or Vite?**
A: Define entry/output, loaders for JS/CSS/assets, plugins for optimization, and dev server settings. Vite uses native ES modules for fast builds.

**Q: How do you use and write tests with Jest, React Testing Library, or Cypress?**
A: Jest is for unit tests, React Testing Library for component tests, and Cypress for end-to-end tests. Write tests to cover logic, UI, and user flows.

**Q: How do you handle frontend logging and analytics?**
A: Use services like Google Analytics, Segment, or custom logging. Track user events, errors, and performance. Respect privacy and GDPR.

## Cross-Platform & Modern Web

**Q: How do you implement progressive web app features for better user experience?**
A: Add a manifest, register a Service Worker, enable offline support, and use HTTPS. Test with Lighthouse for PWA compliance.

**Q: What's your approach to building responsive applications that work across all devices?**
A: Use mobile-first design, flexible layouts, media queries, and test on multiple devices and browsers.

**Q: How do you handle offline functionality and data synchronization?**
A: Cache data locally (IndexedDB, localStorage), queue changes, and sync with the server when online.

**Q: Explain your strategy for implementing real-time features (WebSockets, Server-Sent Events).**
A: Use WebSockets for bidirectional communication, SSE for server-to-client updates. Manage connection state and handle reconnections.

## Team Leadership & Code Quality

**Q: How do you establish code review processes and maintain code quality standards?**
A: Use pull requests, code review checklists, and automated linting/testing. Encourage constructive feedback and knowledge sharing.

**Q: What's your approach to technical debt management in large codebases?**
A: Track debt in the backlog, prioritize fixes, and allocate time for refactoring. Use static analysis tools to identify issues.

**Q: How do you mentor junior developers and conduct technical interviews?**
A: Pair programming, regular feedback, and knowledge sharing sessions. In interviews, assess problem-solving, coding, and communication skills.

**Q: Explain your strategy for migrating legacy frontend applications to modern tech stacks.**
A: Incrementally replace old modules, use adapters, write tests, and ensure feature parity. Communicate changes and provide training.
