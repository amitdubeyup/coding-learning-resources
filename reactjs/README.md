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

### 10. Core Hooks
- `useState`: For managing state in functional components
- `useEffect`: For handling side effects
- `useContext`: For consuming context
- `useReducer`: For complex state logic
- `useCallback`: For memoizing functions
- `useMemo`: For memoizing values

### 11. Custom Hooks
Common custom hooks for:
- Data fetching
- Local storage
- Window size
- Keyboard events
- Mouse position
- Scroll position
- Network status
- Geolocation
- Clipboard operations
- Media queries

## Performance Optimization

### 12. React.memo
For preventing unnecessary re-renders:

```jsx
const MemoizedComponent = React.memo(function MyComponent(props) {
  return <div>{props.name}</div>;
});
```

### 13. Code Splitting
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

### 14. React Router
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

### 15. Protected Routes
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

### 16. Jest and React Testing Library
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

## Advanced Patterns

### 17. Higher-Order Components
```jsx
function withAuth(WrappedComponent) {
  return function WithAuth(props) {
    const isAuthenticated = checkAuth();
    return isAuthenticated ? <WrappedComponent {...props} /> : <Login />;
  };
}
```

### 18. Render Props
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

## Best Practices

### 19. Component Structure
- Keep components small and focused
- Use functional components with hooks
- Implement proper prop types
- Follow naming conventions

### 20. State Management
- Use local state for component-specific data
- Use context for theme/global state
- Use Redux for complex state
- Implement proper error boundaries

### 21. Performance
- Implement code splitting
- Use React.memo for expensive renders
- Optimize with useMemo and useCallback
- Implement proper loading states

### 22. Testing
- Write unit tests for components
- Implement integration tests
- Use snapshot testing
- Test error scenarios

## Common Interview Questions

### 23. Core Concepts
1. What is the difference between props and state?
2. What is the Virtual DOM?
3. What are React Hooks?
4. What is the difference between useEffect and useLayoutEffect?
5. What is the purpose of keys in React?

### 24. Component Lifecycle
1. What is the difference between controlled and uncontrolled components?
2. What is the purpose of React.Fragment?
3. What is the difference between useCallback and useMemo?
4. What is the purpose of React.lazy?
5. What is the difference between React.memo and useMemo?

### 25. State Management
1. What is the purpose of useRef?
2. What is the difference between useState and useReducer?
3. What is the purpose of useContext?
4. What is the difference between class and functional components?
5. What is the purpose of Error Boundaries?

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