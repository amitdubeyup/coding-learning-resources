# ReactJS Interview Guide

## Table of Contents
1. [Core Concepts](#core-concepts)
2. [Component Lifecycle](#component-lifecycle)
3. [State Management](#state-management)
4. [Hooks](#hooks)
5. [Performance Optimization](#performance-optimization)
6. [Routing](#routing)
7. [Testing](#testing)
8. [Advanced Patterns](#advanced-patterns)
9. [Best Practices](#best-practices)
10. [Common Interview Questions](#common-interview-questions)

## Core Concepts

### 1. What is React?
React is a JavaScript library for building user interfaces, particularly single-page applications. It's maintained by Facebook and a community of individual developers and companies.

### 2. JSX
JSX is a syntax extension for JavaScript that lets you write HTML-like code in your JavaScript files.

```jsx
// Example of JSX
const element = (
  <div className="greeting">
    <h1>Hello, {name}!</h1>
    <p>Welcome to React</p>
  </div>
);
```

### 3. Virtual DOM
React uses a virtual DOM to improve performance. It's a lightweight copy of the actual DOM that React uses to determine what needs to be updated.

### 4. Components
Components are the building blocks of React applications. They can be functional or class-based.

```jsx
// Functional Component
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

// Class Component
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```

## Component Lifecycle

### 5. Component Lifecycle Methods
- `constructor()`
- `render()`
- `componentDidMount()`
- `componentDidUpdate()`
- `componentWillUnmount()`

### 6. Error Boundaries
Error boundaries are React components that catch JavaScript errors anywhere in their child component tree.

```jsx
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  render() {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return this.props.children;
  }
}
```

## State Management

### 7. Local State
Using `useState` hook for local state management:

```jsx
function Counter() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

### 8. Context API
For global state management:

```jsx
const ThemeContext = React.createContext('light');

function App() {
  return (
    <ThemeContext.Provider value="dark">
      <ThemedButton />
    </ThemeContext.Provider>
  );
}
```

### 9. Redux
For complex state management:

```jsx
// Action
const increment = () => ({
  type: 'INCREMENT'
});

// Reducer
const counterReducer = (state = 0, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return state + 1;
    default:
      return state;
  }
};
```

## Hooks

### 10. useState
For managing state in functional components:

```jsx
const [state, setState] = useState(initialState);
```

### 11. useEffect
For handling side effects:

```jsx
useEffect(() => {
  // Side effect code
  return () => {
    // Cleanup code
  };
}, [dependencies]);
```

### 12. useContext
For consuming context:

```jsx
const value = useContext(MyContext);
```

### 13. useReducer
For complex state logic:

```jsx
const [state, dispatch] = useReducer(reducer, initialState);
```

### 14. useCallback
For memoizing functions:

```jsx
const memoizedCallback = useCallback(
  () => {
    doSomething(a, b);
  },
  [a, b],
);
```

### 15. useMemo
For memoizing values:

```jsx
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);
```

## Performance Optimization

### 16. React.memo
For preventing unnecessary re-renders:

```jsx
const MemoizedComponent = React.memo(function MyComponent(props) {
  return <div>{props.name}</div>;
});
```

### 17. useMemo and useCallback
For optimizing performance:

```jsx
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);
const memoizedCallback = useCallback(() => {
  doSomething(a, b);
}, [a, b]);
```

### 18. Code Splitting
Using React.lazy and Suspense:

```jsx
const LazyComponent = React.lazy(() => import('./LazyComponent'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <LazyComponent />
    </Suspense>
  );
}
```

## Routing

### 19. React Router
Basic routing setup:

```jsx
import { BrowserRouter, Route, Switch } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/about" component={About} />
        <Route path="/contact" component={Contact} />
      </Switch>
    </BrowserRouter>
  );
}
```

### 20. Protected Routes
Implementing authentication:

```jsx
function PrivateRoute({ children, ...rest }) {
  return (
    <Route
      {...rest}
      render={({ location }) =>
        isAuthenticated ? (
          children
        ) : (
          <Redirect to={{ pathname: "/login", state: { from: location } }} />
        )
      }
    />
  );
}
```

## Testing

### 21. Jest and React Testing Library
Basic test example:

```jsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
```

### 22. Snapshot Testing
```jsx
test('renders correctly', () => {
  const tree = renderer.create(<App />).toJSON();
  expect(tree).toMatchSnapshot();
});
```

## Advanced Patterns

### 23. Higher-Order Components
```jsx
function withAuth(WrappedComponent) {
  return function WithAuth(props) {
    const isAuthenticated = checkAuth();
    return isAuthenticated ? <WrappedComponent {...props} /> : <Login />;
  };
}
```

### 24. Render Props
```jsx
class Mouse extends React.Component {
  state = { x: 0, y: 0 };
  
  handleMouseMove = (event) => {
    this.setState({
      x: event.clientX,
      y: event.clientY
    });
  }

  render() {
    return (
      <div onMouseMove={this.handleMouseMove}>
        {this.props.render(this.state)}
      </div>
    );
  }
}
```

### 25. Custom Hooks
```jsx
function useWindowSize() {
  const [size, setSize] = useState({
    width: window.innerWidth,
    height: window.innerHeight
  });

  useEffect(() => {
    const handleResize = () => {
      setSize({
        width: window.innerWidth,
        height: window.innerHeight
      });
    };

    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  return size;
}
```

## Best Practices

### 26. Component Structure
- Keep components small and focused
- Use functional components with hooks
- Implement proper prop types
- Follow naming conventions

### 27. State Management
- Use local state for component-specific data
- Use context for theme/global state
- Use Redux for complex state
- Implement proper error boundaries

### 28. Performance
- Implement code splitting
- Use React.memo for expensive renders
- Optimize with useMemo and useCallback
- Implement proper loading states

### 29. Testing
- Write unit tests for components
- Implement integration tests
- Use snapshot testing
- Test error scenarios

## Common Interview Questions

### 30. What is the difference between props and state?
Props are read-only and passed from parent to child, while state is managed within the component and can be changed.

### 31. What is the Virtual DOM?
The Virtual DOM is a lightweight copy of the actual DOM that React uses to determine what needs to be updated.

### 32. What are React Hooks?
Hooks are functions that let you use state and other React features in functional components.

### 33. What is the difference between useEffect and useLayoutEffect?
useEffect runs after render, while useLayoutEffect runs synchronously after DOM mutations.

### 34. What is the purpose of keys in React?
Keys help React identify which items have changed, been added, or been removed in lists.

### 35. What is the difference between controlled and uncontrolled components?
Controlled components have their state controlled by React, while uncontrolled components maintain their own state.

### 36. What is the purpose of React.Fragment?
React.Fragment lets you group multiple elements without adding extra nodes to the DOM.

### 37. What is the difference between useCallback and useMemo?
useCallback memoizes functions, while useMemo memoizes values.

### 38. What is the purpose of React.lazy?
React.lazy lets you load components lazily, improving initial load time.

### 39. What is the difference between React.memo and useMemo?
React.memo is for components, while useMemo is for values.

### 40. What is the purpose of useRef?
useRef creates a mutable reference that persists across renders.

### 41. What is the difference between useState and useReducer?
useState is for simple state, while useReducer is for complex state logic.

### 42. What is the purpose of useContext?
useContext lets you consume context values in functional components.

### 43. What is the difference between class and functional components?
Class components use lifecycle methods, while functional components use hooks.

### 44. What is the purpose of Error Boundaries?
Error Boundaries catch JavaScript errors in their child component tree.

### 45. What is the difference between React.lazy and dynamic import?
React.lazy is specifically for React components, while dynamic import is for any module.

### 46. What is the purpose of React.Suspense?
React.Suspense lets you handle loading states for lazy-loaded components.

### 47. What is the difference between useEffect and componentDidMount?
useEffect runs after render, while componentDidMount runs after the first render.

### 48. What is the purpose of React.PureComponent?
React.PureComponent implements shouldComponentUpdate with a shallow prop and state comparison.

### 49. What is the difference between React.memo and React.PureComponent?
React.memo is for functional components, while React.PureComponent is for class components.

### 50. What is the purpose of React.forwardRef?
React.forwardRef lets you pass refs to child components.

## Resources

### Books
- Learning React (O'Reilly)
- React Design Patterns and Best Practices
- Fullstack React
- React in Action

### Online Resources
- React Documentation
- React Patterns
- React Training
- React Router Documentation

### Tools
- Create React App
- React Developer Tools
- React Testing Library
- Jest

### Communities
- React Discord
- React Reddit
- React Stack Overflow
- React GitHub Discussions
