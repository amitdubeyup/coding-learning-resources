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
