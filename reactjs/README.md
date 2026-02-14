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
9. [Modern React Features](#modern-react-features)
10. [TypeScript Integration](#typescript-integration)
11. [Build Tools](#build-tools)
12. [React Best Practices](#react-best-practices)
13. [Rendering Strategies (SSR, CSR, SSG, ISR)](#rendering-strategies)
14. [React Interview Essentials](#react-interview-essentials)
15. [Additional Resources](#additional-resources)

## Core Concepts

### 1. What is React?
React is an open-source JavaScript library for building user interfaces, particularly single-page applications. Originally created by Facebook (now Meta), it's maintained by Meta and a large community. React uses a component-based architecture and a virtual DOM for efficient rendering. As of 2026, React is the most widely used frontend library in the industry.

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
React uses a virtual DOM to improve performance. The Virtual DOM is a lightweight JavaScript object representation of the actual DOM. When state changes, React creates a new virtual DOM tree and uses a **reconciliation algorithm** (diffing) to compare it with the previous tree. Only the changed nodes are updated in the real DOM (a process called **"committing"**). This batched, minimal update approach is much faster than directly manipulating the DOM. React Fiber (introduced in React 16) further optimizes this with incremental rendering and priority-based scheduling.

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
Class component lifecycle methods (in order of execution):
- **Mounting:** `constructor()` → `render()` → `componentDidMount()`
- **Updating:** `render()` → `componentDidUpdate(prevProps, prevState)`
- **Unmounting:** `componentWillUnmount()`
- **Error handling:** `static getDerivedStateFromError()` → `componentDidCatch()`

**Modern equivalent with Hooks:**
- `componentDidMount` → `useEffect(() => { ... }, [])`
- `componentDidUpdate` → `useEffect(() => { ... }, [deps])`
- `componentWillUnmount` → `useEffect(() => { return () => { cleanup } }, [])`

> **Industry note:** Functional components with Hooks are the standard in modern React. Class components are still supported but considered legacy for new code.

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
For complex state management. **Redux Toolkit (RTK)** is now the official, recommended way to write Redux logic:

```jsx
// Modern Redux with Redux Toolkit
import { configureStore, createSlice } from '@reduxjs/toolkit';

const counterSlice = createSlice({
  name: 'counter',
  initialState: { value: 0 },
  reducers: {
    increment: state => { state.value += 1; },
    decrement: state => { state.value -= 1; },
    incrementByAmount: (state, action) => { state.value += action.payload; }
  }
});

export const { increment, decrement, incrementByAmount } = counterSlice.actions;
export const store = configureStore({ reducer: { counter: counterSlice.reducer } });
```

<details>
<summary>Legacy Redux syntax (for reference)</summary>

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
</details>

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
Basic routing setup (React Router v6+):

```jsx
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/users/:id" element={<UserProfile />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}
```

> **Note:** React Router v6 replaced `Switch` with `Routes`, `component` prop with `element`, and removed the need for `exact` on parent routes.

### 20. Protected Routes
Implementing authentication (React Router v6):

```jsx
import { Navigate, useLocation } from 'react-router-dom';

function ProtectedRoute({ children }) {
  const { user } = useAuth();
  const location = useLocation();

  if (!user) {
    return <Navigate to="/login" state={{ from: location }} replace />;
  }

  return children;
}

// Usage in Routes
<Route
  path="/dashboard"
  element={
    <ProtectedRoute>
      <Dashboard />
    </ProtectedRoute>
  }
/>
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

### 26. What is the difference between useCallback and useMemo?
useCallback memoizes functions, while useMemo memoizes values. useCallback is useful when passing callbacks to optimized child components, while useMemo is useful for expensive calculations.

### 27. What is the purpose of React.lazy?
React.lazy lets you load components lazily, improving initial load time. It's used with Suspense to handle loading states.

### 28. What is the difference between React.memo and useMemo?
React.memo is for components, while useMemo is for values. React.memo prevents unnecessary re-renders of components, while useMemo prevents unnecessary recalculations of values.

### 29. What is the purpose of useRef?
useRef creates a mutable reference that persists across renders. It's useful for accessing DOM elements, storing previous values, and maintaining values that don't trigger re-renders.

### 30. What is the difference between props and state?
Props are read-only and passed from parent to child, while state is managed within the component and can be changed.

### 31. What is the Virtual DOM?
The Virtual DOM is a lightweight JavaScript representation of the real DOM. React maintains two virtual DOM trees — when state changes, React creates a new tree and **diffs** it against the previous one (reconciliation). Only the minimal set of changes are applied to the real DOM. This approach is faster than direct DOM manipulation because DOM operations are expensive while JavaScript object comparisons are cheap. React Fiber (the reconciliation engine since React 16) can also split rendering work into chunks and prioritize updates.

### 32. What are React Hooks?
Hooks are functions that let you use state and other React features in functional components.

### 33. What is the difference between useEffect and useLayoutEffect?
useEffect runs after render, while useLayoutEffect runs synchronously after DOM mutations.

### 34. What is the purpose of keys in React?
Keys help React identify which items have changed, been added, or been removed in lists.

### 35. What is the difference between controlled and uncontrolled components?
Controlled components have their state controlled by React, while uncontrolled components maintain their own state.

### 36. What is the purpose of React.Fragment?
React.Fragment lets you group multiple elements without adding extra nodes to the DOM. You can also use the shorthand syntax `<>...</>`.

### 41. What is the difference between useState and useReducer?
useState is for simple state, while useReducer is for complex state logic.

### 42. What is the purpose of useContext?
useContext lets you consume context values in functional components.

### 43. What is the difference between class and functional components?
Class components use lifecycle methods and `this.state`/`this.setState`, while functional components use Hooks (`useState`, `useEffect`, etc.). **Functional components are the modern standard** — they are simpler, easier to test, and support all React features including Hooks. Class components are still supported but are no longer recommended for new code in the industry.

### 44. What is the purpose of Error Boundaries?
Error Boundaries catch JavaScript errors in their child component tree.

### 45. What is the difference between React.lazy and dynamic import?
React.lazy is specifically for React components, while dynamic import is for any module.

### 46. What is the purpose of React.Suspense?
React.Suspense lets you handle loading states for lazy-loaded components.

### 47. What is the difference between useEffect and componentDidMount?
`useEffect(() => { ... }, [])` is the functional equivalent of `componentDidMount`, but there's a subtle difference: `componentDidMount` fires synchronously after the DOM is painted, while `useEffect` fires asynchronously after paint. If you need synchronous DOM measurement before paint, use `useLayoutEffect`. Additionally, `useEffect` can return a cleanup function (similar to `componentWillUnmount`), and with dependencies, it replaces `componentDidUpdate` as well — making it a more unified side-effect API.

### 48. What is the purpose of React.PureComponent?
React.PureComponent implements shouldComponentUpdate with a shallow prop and state comparison.

### 49. What is the difference between React.memo and React.PureComponent?
React.memo is for functional components, while React.PureComponent is for class components.

### 50. What is the purpose of React.forwardRef?
React.forwardRef lets you pass refs to child components.

### 51. What is the purpose of React.StrictMode?
React.StrictMode helps identify potential problems in your application by enabling additional checks and warnings.

```jsx
function App() {
  return (
    <React.StrictMode>
      <div>
        <ComponentOne />
        <ComponentTwo />
      </div>
    </React.StrictMode>
  );
}
```

### 52. How do you handle forms in React?
Using controlled components with form state:

```jsx
function Form() {
  const [formData, setFormData] = useState({
    username: '',
    email: ''
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        name="username"
        value={formData.username}
        onChange={handleChange}
      />
      <input
        name="email"
        value={formData.email}
        onChange={handleChange}
      />
      <button type="submit">Submit</button>
    </form>
  );
}
```

### 53. What is the difference between useRef and useState?
useRef doesn't trigger re-renders, while useState does:

```jsx
function RefVsState() {
  const [count, setCount] = useState(0);
  const countRef = useRef(0);

  const handleClick = () => {
    countRef.current += 1; // No re-render
    setCount(count + 1); // Triggers re-render
  };

  return (
    <div>
      <p>State: {count}</p>
      <p>Ref: {countRef.current}</p>
      <button onClick={handleClick}>Increment</button>
    </div>
  );
}
```

### 54. How do you implement infinite scrolling?
Using Intersection Observer API:

```jsx
function InfiniteScroll() {
  const [items, setItems] = useState([]);
  const [page, setPage] = useState(1);
  const observer = useRef();

  const lastElementRef = useCallback(node => {
    if (observer.current) observer.current.disconnect();
    observer.current = new IntersectionObserver(entries => {
      if (entries[0].isIntersecting) {
        setPage(prevPage => prevPage + 1);
      }
    });
    if (node) observer.current.observe(node);
  }, []);

  useEffect(() => {
    // Fetch more items when page changes
    fetchItems(page).then(newItems => {
      setItems(prevItems => [...prevItems, ...newItems]);
    });
  }, [page]);

  return (
    <div>
      {items.map((item, index) => (
        <div
          ref={index === items.length - 1 ? lastElementRef : null}
          key={item.id}
        >
          {item.content}
        </div>
      ))}
    </div>
  );
}
```

### 55. How do you implement drag and drop?
Using react-dnd (v16+ API):

```jsx
import { DndProvider, useDrag, useDrop } from 'react-dnd';
import { HTML5Backend } from 'react-dnd-html5-backend';

function DraggableItem({ id, text }) {
  const [{ isDragging }, drag] = useDrag(() => ({
    type: 'ITEM',
    item: { id },
    collect: monitor => ({
      isDragging: monitor.isDragging()
    })
  }), [id]);

  return (
    <div
      ref={drag}
      style={{ opacity: isDragging ? 0.5 : 1, cursor: 'grab' }}
    >
      {text}
    </div>
  );
}

function DroppableArea({ onDrop }) {
  const [{ isOver }, drop] = useDrop(() => ({
    accept: 'ITEM',
    drop: item => onDrop(item.id),
    collect: monitor => ({
      isOver: monitor.isOver()
    })
  }), [onDrop]);

  return (
    <div
      ref={drop}
      style={{ backgroundColor: isOver ? 'lightblue' : 'white', padding: 20 }}
    >
      Drop here
    </div>
  );
}

// Wrap your app with DndProvider
function App() {
  return (
    <DndProvider backend={HTML5Backend}>
      <DraggableItem id="1" text="Drag me" />
      <DroppableArea onDrop={id => console.log('Dropped:', id)} />
    </DndProvider>
  );
}
```

### 56. How do you implement authentication in React?
Using context and protected routes:

```jsx
const AuthContext = React.createContext(null);

function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Check if user is logged in
    checkAuth().then(user => {
      setUser(user);
      setLoading(false);
    });
  }, []);

  const login = async (credentials) => {
    const user = await loginUser(credentials);
    setUser(user);
  };

  const logout = () => {
    setUser(null);
  };

  if (loading) return <Loading />;

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

function useAuth() {
  return useContext(AuthContext);
}
```

### 57. How do you implement real-time updates?
Using WebSocket:

```jsx
function RealTimeComponent() {
  const [messages, setMessages] = useState([]);
  const ws = useRef(null);

  useEffect(() => {
    ws.current = new WebSocket('ws://your-websocket-server');

    ws.current.onmessage = (event) => {
      const message = JSON.parse(event.data);
      setMessages(prev => [...prev, message]);
    };

    return () => {
      ws.current.close();
    };
  }, []);

  const sendMessage = (message) => {
    ws.current.send(JSON.stringify(message));
  };

  return (
    <div>
      {messages.map(msg => (
        <div key={msg.id}>{msg.content}</div>
      ))}
      <button onClick={() => sendMessage({ content: 'Hello!' })}>
        Send Message
      </button>
    </div>
  );
}
```

### 58. How do you implement a custom hook for real-time updates?
Using WebSocket:

```jsx
function useRealTimeUpdates() {
  const [messages, setMessages] = useState([]);
  const ws = useRef(null);

  useEffect(() => {
    ws.current = new WebSocket('ws://your-websocket-server');

    ws.current.onmessage = (event) => {
      const message = JSON.parse(event.data);
      setMessages(prev => [...prev, message]);
    };

    return () => {
      ws.current.close();
    };
  }, []);

  const sendMessage = (message) => {
    ws.current.send(JSON.stringify(message));
  };

  return { messages, sendMessage };
}
```

### 59. How do you implement a portal in React?
React Portals provide a way to render children into a DOM node that exists outside the parent component's DOM hierarchy. This is useful for modals, tooltips, and dropdowns.

```jsx
import { createPortal } from 'react-dom';

function Modal({ children, isOpen, onClose }) {
  if (!isOpen) return null;

  return createPortal(
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={e => e.stopPropagation()}>
        {children}
        <button onClick={onClose}>Close</button>
      </div>
    </div>,
    document.getElementById('modal-root')
  );
}

// Usage
function App() {
  const [isOpen, setIsOpen] = useState(false);
  return (
    <div>
      <button onClick={() => setIsOpen(true)}>Open Modal</button>
      <Modal isOpen={isOpen} onClose={() => setIsOpen(false)}>
        <h2>Modal Content</h2>
        <p>This renders outside the parent DOM hierarchy</p>
      </Modal>
    </div>
  );
}
```

### 60. How do you implement a higher-order component?
```jsx
// HOC for authentication
function withAuth(WrappedComponent) {
  return function WithAuth(props) {
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    
    useEffect(() => {
      checkAuth().then(result => setIsAuthenticated(result));
    }, []);
    
    if (!isAuthenticated) {
      return <div>Please log in</div>;
    }
    
    return <WrappedComponent {...props} />;
  };
}

// Usage
const ProtectedComponent = withAuth(function MyComponent() {
  return <div>Protected Content</div>;
});
```

### 61. How do you implement a render prop pattern?
```jsx
class MouseTracker extends React.Component {
  state = { x: 0, y: 0 };
  
  handleMouseMove = (event) => {
    this.setState({
      x: event.clientX,
      y: event.clientY
    });
  };
  
  render() {
    return (
      <div onMouseMove={this.handleMouseMove}>
        {this.props.render(this.state)}
      </div>
    );
  }
}

// Usage
function App() {
  return (
    <MouseTracker
      render={({ x, y }) => (
        <div>
          Mouse position: {x}, {y}
        </div>
      )}
    />
  );
}
```

### 62. How do you implement a compound component pattern?
```jsx
const Tabs = ({ children }) => {
  const [activeTab, setActiveTab] = useState(0);
  
  return (
    <TabsContext.Provider value={{ activeTab, setActiveTab }}>
      {children}
    </TabsContext.Provider>
  );
};

Tabs.Tab = function Tab({ index, children }) {
  const { activeTab, setActiveTab } = useContext(TabsContext);
  
  return (
    <button
      onClick={() => setActiveTab(index)}
      className={activeTab === index ? 'active' : ''}
    >
      {children}
    </button>
  );
};

Tabs.Panel = function Panel({ index, children }) {
  const { activeTab } = useContext(TabsContext);
  
  return activeTab === index ? <div>{children}</div> : null;
};

// Usage
function App() {
  return (
    <Tabs>
      <Tabs.Tab index={0}>Tab 1</Tabs.Tab>
      <Tabs.Tab index={1}>Tab 2</Tabs.Tab>
      <Tabs.Panel index={0}>Content 1</Tabs.Panel>
      <Tabs.Panel index={1}>Content 2</Tabs.Panel>
    </Tabs>
  );
}
```

### 63. How do you implement a custom hook for data fetching?
```jsx
function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(url);
        const json = await response.json();
        setData(json);
        setLoading(false);
      } catch (error) {
        setError(error);
        setLoading(false);
      }
    };

    fetchData();
  }, [url]);

  return { data, loading, error };
}

// Usage
function DataComponent() {
  const { data, loading, error } = useFetch('https://api.example.com/data');
  
  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  
  return <div>{JSON.stringify(data)}</div>;
}
```

### 64. How do you implement a custom hook for form handling?
```jsx
function useForm(initialValues) {
  const [values, setValues] = useState(initialValues);
  const [errors, setErrors] = useState({});
  const [touched, setTouched] = useState({});

  const handleChange = (e) => {
    const { name, value } = e.target;
    setValues(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleBlur = (e) => {
    const { name } = e.target;
    setTouched(prev => ({
      ...prev,
      [name]: true
    }));
  };

  const handleSubmit = (onSubmit) => (e) => {
    e.preventDefault();
    onSubmit(values);
  };

  return {
    values,
    errors,
    touched,
    handleChange,
    handleBlur,
    handleSubmit
  };
}

// Usage
function FormComponent() {
  const { values, handleChange, handleBlur, handleSubmit } = useForm({
    username: '',
    email: ''
  });

  const onSubmit = (values) => {
    console.log('Form submitted:', values);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input
        name="username"
        value={values.username}
        onChange={handleChange}
        onBlur={handleBlur}
      />
      <input
        name="email"
        value={values.email}
        onChange={handleChange}
        onBlur={handleBlur}
      />
      <button type="submit">Submit</button>
    </form>
  );
}
```

### 65. How do you implement a custom hook for local storage?
```jsx
function useLocalStorage(key, initialValue) {
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error(error);
      return initialValue;
    }
  });

  const setValue = (value) => {
    try {
      const valueToStore = value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error(error);
    }
  };

  return [storedValue, setValue];
}

// Usage
function LocalStorageComponent() {
  const [name, setName] = useLocalStorage('name', '');
  
  return (
    <input
      value={name}
      onChange={e => setName(e.target.value)}
      placeholder="Enter your name"
    />
  );
}
```

### 66. How do you implement a custom hook for media queries?
```jsx
function useMediaQuery(query) {
  const [matches, setMatches] = useState(false);

  useEffect(() => {
    const media = window.matchMedia(query);
    if (media.matches !== matches) {
      setMatches(media.matches);
    }
    
    const listener = (e) => setMatches(e.matches);
    media.addEventListener('change', listener);
    
    return () => media.removeEventListener('change', listener);
  }, [matches, query]);

  return matches;
}

// Usage
function ResponsiveComponent() {
  const isMobile = useMediaQuery('(max-width: 768px)');
  
  return (
    <div>
      {isMobile ? 'Mobile View' : 'Desktop View'}
    </div>
  );
}
```

### 67. How do you test React components?
```jsx
// Using React Testing Library
import { render, screen, fireEvent } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

// Component to test
function Counter() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}

// Test
test('increments counter when button is clicked', () => {
  render(<Counter />);
  
  const button = screen.getByText('Increment');
  const count = screen.getByText(/count: 0/i);
  
  fireEvent.click(button);
  
  expect(screen.getByText(/count: 1/i)).toBeInTheDocument();
});
```

### 68. How do you implement error boundaries?
```jsx
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Error:', error);
    console.error('Error Info:', errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div>
          <h1>Something went wrong.</h1>
          <details>
            <summary>Error Details</summary>
            <pre>{this.state.error?.toString()}</pre>
          </details>
        </div>
      );
    }

    return this.props.children;
  }
}

// Usage
function App() {
  return (
    <ErrorBoundary>
      <MyComponent />
    </ErrorBoundary>
  );
}
```

### 69. How do you implement loading states?
```jsx
function useLoadingState() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const withLoading = async (fn) => {
    try {
      setLoading(true);
      setError(null);
      await fn();
    } catch (err) {
      setError(err);
    } finally {
      setLoading(false);
    }
  };

  return { loading, error, withLoading };
}

// Usage
function DataFetcher() {
  const { loading, error, withLoading } = useLoadingState();
  const [data, setData] = useState(null);

  const fetchData = async () => {
    await withLoading(async () => {
      const response = await fetch('https://api.example.com/data');
      const json = await response.json();
      setData(json);
    });
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  if (!data) return <button onClick={fetchData}>Fetch Data</button>;

  return <div>{JSON.stringify(data)}</div>;
}
```

### 70. How do you implement optimistic updates?
```jsx
function OptimisticList() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(false);

  const addItem = async (newItem) => {
    // Optimistically add item
    const tempId = Date.now();
    setItems(prev => [...prev, { ...newItem, id: tempId }]);

    try {
      // Make API call
      const response = await fetch('/api/items', {
        method: 'POST',
        body: JSON.stringify(newItem)
      });
      const savedItem = await response.json();

      // Update with real data
      setItems(prev => 
        prev.map(item => 
          item.id === tempId ? savedItem : item
        )
      );
    } catch (error) {
      // Revert on error
      setItems(prev => 
        prev.filter(item => item.id !== tempId)
      );
      alert('Failed to add item');
    }
  };

  return (
    <div>
      {items.map(item => (
        <div key={item.id}>{item.name}</div>
      ))}
      <button 
        onClick={() => addItem({ name: 'New Item' })}
        disabled={loading}
      >
        Add Item
      </button>
    </div>
  );
}
```

### 71. How do you implement infinite scrolling with loading states?
```jsx
function InfiniteScroll() {
  const [items, setItems] = useState([]);
  const [page, setPage] = useState(1);
  const [loading, setLoading] = useState(false);
  const [hasMore, setHasMore] = useState(true);
  const observer = useRef();

  const lastElementRef = useCallback(node => {
    if (loading) return;
    if (observer.current) observer.current.disconnect();
    
    observer.current = new IntersectionObserver(entries => {
      if (entries[0].isIntersecting && hasMore) {
        setPage(prevPage => prevPage + 1);
      }
    });
    
    if (node) observer.current.observe(node);
  }, [loading, hasMore]);

  useEffect(() => {
    const fetchItems = async () => {
      setLoading(true);
      try {
        const response = await fetch(`/api/items?page=${page}`);
        const newItems = await response.json();
        
        setItems(prev => [...prev, ...newItems]);
        setHasMore(newItems.length > 0);
      } catch (error) {
        console.error('Error fetching items:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchItems();
  }, [page]);

  return (
    <div>
      {items.map((item, index) => (
        <div
          ref={index === items.length - 1 ? lastElementRef : null}
          key={item.id}
        >
          {item.content}
        </div>
      ))}
      {loading && <div>Loading...</div>}
      {!hasMore && <div>No more items</div>}
    </div>
  );
}
```

### 72. How do you implement a custom hook for API calls?
```jsx
function useApi(endpoint) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchData = async (options = {}) => {
    setLoading(true);
    setError(null);
    
    try {
      const response = await fetch(endpoint, {
        method: options.method || 'GET',
        headers: {
          'Content-Type': 'application/json',
          ...options.headers
        },
        body: options.body ? JSON.stringify(options.body) : undefined
      });
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const result = await response.json();
      setData(result);
      return result;
    } catch (err) {
      setError(err);
      throw err;
    } finally {
      setLoading(false);
    }
  };

  return { data, loading, error, fetchData };
}

// Usage
function UserProfile() {
  const { data, loading, error, fetchData } = useApi('/api/user');
  
  useEffect(() => {
    fetchData();
  }, []);
  
  const updateProfile = async (newData) => {
    await fetchData({
      method: 'PUT',
      body: newData
    });
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  if (!data) return null;

  return (
    <div>
      <h1>{data.name}</h1>
      <button onClick={() => updateProfile({ name: 'New Name' })}>
        Update Name
      </button>
    </div>
  );
}
```

### 73. How do you implement a custom hook for animations?
```jsx
function useAnimation(duration = 1000) {
  const [isAnimating, setIsAnimating] = useState(false);
  const [progress, setProgress] = useState(0);
  const animationRef = useRef();

  const startAnimation = useCallback(() => {
    setIsAnimating(true);
    setProgress(0);
    
    const startTime = performance.now();
    
    const animate = (currentTime) => {
      const elapsed = currentTime - startTime;
      const newProgress = Math.min(elapsed / duration, 1);
      
      setProgress(newProgress);
      
      if (newProgress < 1) {
        animationRef.current = requestAnimationFrame(animate);
      } else {
        setIsAnimating(false);
      }
    };
    
    animationRef.current = requestAnimationFrame(animate);
  }, [duration]);

  useEffect(() => {
    return () => {
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current);
      }
    };
  }, []);

  return { isAnimating, progress, startAnimation };
}

// Usage
function AnimatedComponent() {
  const { isAnimating, progress, startAnimation } = useAnimation();
  
  return (
    <div>
      <div
        style={{
          width: `${progress * 100}%`,
          height: '20px',
          backgroundColor: 'blue',
          transition: 'width 0.1s linear'
        }}
      />
      <button onClick={startAnimation} disabled={isAnimating}>
        Animate
      </button>
    </div>
  );
}
```

### 74. How do you implement a custom hook for keyboard shortcuts?
```jsx
function useKeyboardShortcut(key, callback) {
  useEffect(() => {
    const handleKeyPress = (event) => {
      if (event.key === key) {
        callback();
      }
    };

    window.addEventListener('keydown', handleKeyPress);
    return () => window.removeEventListener('keydown', handleKeyPress);
  }, [key, callback]);
}

// Usage
function ShortcutComponent() {
  const [count, setCount] = useState(0);
  
  useKeyboardShortcut('a', () => {
    setCount(prev => prev + 1);
  });
  
  return (
    <div>
      <p>Press 'a' to increment: {count}</p>
    </div>
  );
}
```

### 75. How do you implement a custom hook for drag and drop?
```jsx
function useDragAndDrop() {
  const [isDragging, setIsDragging] = useState(false);
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const [offset, setOffset] = useState({ x: 0, y: 0 });

  const handleDragStart = (e) => {
    setIsDragging(true);
    setOffset({
      x: e.clientX - position.x,
      y: e.clientY - position.y
    });
  };

  const handleDrag = (e) => {
    if (isDragging) {
      setPosition({
        x: e.clientX - offset.x,
        y: e.clientY - offset.y
      });
    }
  };

  const handleDragEnd = () => {
    setIsDragging(false);
  };

  useEffect(() => {
    if (isDragging) {
      window.addEventListener('mousemove', handleDrag);
      window.addEventListener('mouseup', handleDragEnd);
    }
    return () => {
      window.removeEventListener('mousemove', handleDrag);
      window.removeEventListener('mouseup', handleDragEnd);
    };
  }, [isDragging]);

  return {
    isDragging,
    position,
    handleDragStart
  };
}

// Usage
function DraggableComponent() {
  const { isDragging, position, handleDragStart } = useDragAndDrop();
  
  return (
    <div
      style={{
        position: 'absolute',
        left: position.x,
        top: position.y,
        cursor: isDragging ? 'grabbing' : 'grab'
      }}
      onMouseDown={handleDragStart}
    >
      Drag me!
    </div>
  );
}
```

### 76. How do you implement a custom hook for form validation?
```jsx
function useFormValidation(initialValues, validationRules) {
  const [values, setValues] = useState(initialValues);
  const [errors, setErrors] = useState({});
  const [touched, setTouched] = useState({});

  const validate = (fieldValues = values) => {
    const newErrors = {};
    
    Object.keys(validationRules).forEach(field => {
      const value = fieldValues[field];
      const rules = validationRules[field];
      
      if (rules.required && !value) {
        newErrors[field] = 'This field is required';
      }
      
      if (rules.pattern && !rules.pattern.test(value)) {
        newErrors[field] = rules.message || 'Invalid format';
      }
      
      if (rules.minLength && value.length < rules.minLength) {
        newErrors[field] = `Minimum length is ${rules.minLength}`;
      }
    });
    
    return newErrors;
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setValues(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleBlur = (e) => {
    const { name } = e.target;
    setTouched(prev => ({
      ...prev,
      [name]: true
    }));
    setErrors(validate());
  };

  const handleSubmit = (onSubmit) => (e) => {
    e.preventDefault();
    const newErrors = validate();
    setErrors(newErrors);
    
    if (Object.keys(newErrors).length === 0) {
      onSubmit(values);
    }
  };

  return {
    values,
    errors,
    touched,
    handleChange,
    handleBlur,
    handleSubmit
  };
}

// Usage
function FormComponent() {
  const { values, errors, touched, handleChange, handleBlur, handleSubmit } = useFormValidation(
    { email: '', password: '' },
    {
      email: {
        required: true,
        pattern: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
        message: 'Invalid email address'
      },
      password: {
        required: true,
        minLength: 6
      }
    }
  );

  const onSubmit = (values) => {
    console.log('Form submitted:', values);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div>
        <input
          name="email"
          value={values.email}
          onChange={handleChange}
          onBlur={handleBlur}
        />
        {touched.email && errors.email && <span>{errors.email}</span>}
      </div>
      <div>
        <input
          name="password"
          type="password"
          value={values.password}
          onChange={handleChange}
          onBlur={handleBlur}
        />
        {touched.password && errors.password && <span>{errors.password}</span>}
      </div>
      <button type="submit">Submit</button>
    </form>
  );
}
```

### 77. How do you implement a custom hook for pagination?
```jsx
function usePagination(items, itemsPerPage = 10) {
  const [currentPage, setCurrentPage] = useState(1);
  
  const totalPages = Math.ceil(items.length / itemsPerPage);
  
  const currentItems = items.slice(
    (currentPage - 1) * itemsPerPage,
    currentPage * itemsPerPage
  );
  
  const goToPage = (page) => {
    setCurrentPage(Math.min(Math.max(1, page), totalPages));
  };
  
  const nextPage = () => {
    goToPage(currentPage + 1);
  };
  
  const previousPage = () => {
    goToPage(currentPage - 1);
  };
  
  return {
    currentPage,
    totalPages,
    currentItems,
    goToPage,
    nextPage,
    previousPage
  };
}

// Usage
function PaginatedList() {
  const items = Array.from({ length: 100 }, (_, i) => ({
    id: i + 1,
    content: `Item ${i + 1}`
  }));
  
  const {
    currentPage,
    totalPages,
    currentItems,
    nextPage,
    previousPage
  } = usePagination(items);
  
  return (
    <div>
      {currentItems.map(item => (
        <div key={item.id}>{item.content}</div>
      ))}
      <div>
        <button onClick={previousPage} disabled={currentPage === 1}>
          Previous
        </button>
        <span>
          Page {currentPage} of {totalPages}
        </span>
        <button onClick={nextPage} disabled={currentPage === totalPages}>
          Next
        </button>
      </div>
    </div>
  );
}
```

### 78. How do you implement a custom hook for sorting?
```jsx
function useSort(items, initialSort = { key: null, direction: 'asc' }) {
  const [sort, setSort] = useState(initialSort);
  
  const sortedItems = useMemo(() => {
    if (!sort.key) return items;
    
    return [...items].sort((a, b) => {
      const aValue = a[sort.key];
      const bValue = b[sort.key];
      
      if (sort.direction === 'asc') {
        return aValue > bValue ? 1 : -1;
      } else {
        return aValue < bValue ? 1 : -1;
      }
    });
  }, [items, sort]);
  
  const handleSort = (key) => {
    setSort(prev => ({
      key,
      direction: prev.key === key && prev.direction === 'asc' ? 'desc' : 'asc'
    }));
  };
  
  return {
    sortedItems,
    sort,
    handleSort
  };
}

// Usage
function SortableTable() {
  const items = [
    { id: 1, name: 'John', age: 30 },
    { id: 2, name: 'Alice', age: 25 },
    { id: 3, name: 'Bob', age: 35 }
  ];
  
  const { sortedItems, sort, handleSort } = useSort(items);
  
  return (
    <table>
      <thead>
        <tr>
          <th onClick={() => handleSort('name')}>
            Name {sort.key === 'name' && (sort.direction === 'asc' ? '↑' : '↓')}
          </th>
          <th onClick={() => handleSort('age')}>
            Age {sort.key === 'age' && (sort.direction === 'asc' ? '↑' : '↓')}
          </th>
        </tr>
      </thead>
      <tbody>
        {sortedItems.map(item => (
          <tr key={item.id}>
            <td>{item.name}</td>
            <td>{item.age}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
```

### 79. How do you implement a custom hook for filtering?
```jsx
function useFilter(items, initialFilters = {}) {
  const [filters, setFilters] = useState(initialFilters);
  
  const filteredItems = useMemo(() => {
    return items.filter(item => {
      return Object.entries(filters).every(([key, value]) => {
        if (!value) return true;
        return item[key].toLowerCase().includes(value.toLowerCase());
      });
    });
  }, [items, filters]);
  
  const handleFilterChange = (key, value) => {
    setFilters(prev => ({
      ...prev,
      [key]: value
    }));
  };
  
  const clearFilters = () => {
    setFilters(initialFilters);
  };
  
  return {
    filteredItems,
    filters,
    handleFilterChange,
    clearFilters
  };
}

// Usage
function FilterableList() {
  const items = [
    { id: 1, name: 'Apple', category: 'Fruit' },
    { id: 2, name: 'Carrot', category: 'Vegetable' },
    { id: 3, name: 'Banana', category: 'Fruit' }
  ];
  
  const {
    filteredItems,
    filters,
    handleFilterChange,
    clearFilters
  } = useFilter(items);
  
  return (
    <div>
      <div>
        <input
          placeholder="Filter by name"
          value={filters.name || ''}
          onChange={e => handleFilterChange('name', e.target.value)}
        />
        <input
          placeholder="Filter by category"
          value={filters.category || ''}
          onChange={e => handleFilterChange('category', e.target.value)}
        />
        <button onClick={clearFilters}>Clear Filters</button>
      </div>
      <ul>
        {filteredItems.map(item => (
          <li key={item.id}>
            {item.name} - {item.category}
          </li>
        ))}
      </ul>
    </div>
  );
}
```

### 80. How do you implement a custom hook for debouncing?
```jsx
function useDebounce(value, delay) {
  const [debouncedValue, setDebouncedValue] = useState(value);
  
  useEffect(() => {
    const timer = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);
    
    return () => {
      clearTimeout(timer);
    };
  }, [value, delay]);
  
  return debouncedValue;
}

// Usage
function SearchComponent() {
  const [searchTerm, setSearchTerm] = useState('');
  const debouncedSearchTerm = useDebounce(searchTerm, 500);
  
  useEffect(() => {
    if (debouncedSearchTerm) {
      // Perform search
      console.log('Searching for:', debouncedSearchTerm);
    }
  }, [debouncedSearchTerm]);
  
  return (
    <input
      value={searchTerm}
      onChange={e => setSearchTerm(e.target.value)}
      placeholder="Search..."
    />
  );
}
```

### 81. How do you implement a custom hook for throttling?
```jsx
function useThrottle(callback, delay) {
  const lastRun = useRef(Date.now());
  const timeout = useRef();

  return useCallback((...args) => {
    if (Date.now() - lastRun.current >= delay) {
      callback(...args);
      lastRun.current = Date.now();
    } else {
      clearTimeout(timeout.current);
      timeout.current = setTimeout(() => {
        callback(...args);
        lastRun.current = Date.now();
      }, delay);
    }
  }, [callback, delay]);
}

// Usage
function ThrottledComponent() {
  const [count, setCount] = useState(0);
  
  const handleScroll = useThrottle(() => {
    setCount(prev => prev + 1);
  }, 1000);
  
  useEffect(() => {
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, [handleScroll]);
  
  return <div>Scroll count: {count}</div>;
}
```

### 82. How do you implement a custom hook for localStorage with type safety?
```jsx
function useLocalStorage<T>(key: string, initialValue: T) {
  const [storedValue, setStoredValue] = useState<T>(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error(error);
      return initialValue;
    }
  });

  const setValue = (value: T | ((val: T) => T)) => {
    try {
      const valueToStore = value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error(error);
    }
  };

  return [storedValue, setValue] as const;
}

// Usage
function TypedStorageComponent() {
  const [user, setUser] = useLocalStorage<{ name: string; age: number }>('user', {
    name: '',
    age: 0
  });
  
  return (
    <div>
      <input
        value={user.name}
        onChange={e => setUser(prev => ({ ...prev, name: e.target.value }))}
      />
      <input
        type="number"
        value={user.age}
        onChange={e => setUser(prev => ({ ...prev, age: Number(e.target.value) }))}
      />
    </div>
  );
}
```

### 83. How do you implement a custom hook for handling API errors?
```jsx
function useApiError() {
  const [error, setError] = useState(null);
  const [isError, setIsError] = useState(false);

  const handleError = (error) => {
    setError(error);
    setIsError(true);
    
    // Log error to monitoring service
    console.error('API Error:', error);
    
    // Show error notification
    // notification.error(error.message);
  };

  const clearError = () => {
    setError(null);
    setIsError(false);
  };

  return {
    error,
    isError,
    handleError,
    clearError
  };
}

// Usage
function ApiComponent() {
  const { error, isError, handleError, clearError } = useApiError();
  
  const fetchData = async () => {
    try {
      const response = await fetch('https://api.example.com/data');
      if (!response.ok) {
        throw new Error('API request failed');
      }
      const data = await response.json();
      return data;
    } catch (error) {
      handleError(error);
    }
  };
  
  if (isError) {
    return (
      <div>
        <p>Error: {error.message}</p>
        <button onClick={clearError}>Try Again</button>
      </div>
    );
  }
  
  return <button onClick={fetchData}>Fetch Data</button>;
}
```

### 84. How do you implement a custom hook for handling API caching?
```jsx
function useApiCache() {
  const cache = useRef(new Map());
  
  const getCachedData = (key) => {
    const cachedItem = cache.current.get(key);
    if (cachedItem && Date.now() - cachedItem.timestamp < cachedItem.expiry) {
      return cachedItem.data;
    }
    return null;
  };

  const setCachedData = (key, data) => {
    cache.current.set(key, { data, timestamp: Date.now() });
  };

  const invalidateCache = () => {
    cache.current.clear();
  };

  const invalidateKey = (key) => {
    cache.current.delete(key);
  };

  return {
    getCachedData,
    setCachedData,
    invalidateCache,
    invalidateKey,
    invalidationKey
  };
}

// Usage
function CacheComponent() {
  const {
    getCachedData,
    setCachedData,
    invalidateCache,
    invalidateKey
  } = useApiCache();
  
  const [data, setData] = useState(null);
  
  const fetchData = async (id) => {
    const cachedData = getCachedData(`user-${id}`);
    if (cachedData) {
      setData(cachedData);
      return;
    }
    
    const response = await fetch(`https://api.example.com/users/${id}`);
    const newData = await response.json();
    setCachedData(`user-${id}`, newData);
    setData(newData);
  };
  
  return (
    <div>
      {data ? (
        <div>{JSON.stringify(data)}</div>
      ) : (
        <button onClick={() => fetchData(1)}>Load User</button>
      )}
    </div>
  );
}
```

### 85. How do you implement a custom hook for handling API retries?
```jsx
function useApiRetry(fetchFn, maxRetries = 3, delay = 1000) {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const retryCount = useRef(0);

  const execute = async (...args) => {
    setLoading(true);
    setError(null);
    
    try {
      const result = await fetchFn(...args);
      setData(result);
      retryCount.current = 0;
    } catch (error) {
      if (retryCount.current < maxRetries) {
        retryCount.current += 1;
        await new Promise(resolve => setTimeout(resolve, delay));
        return execute(...args);
      }
      setError(error);
    } finally {
      setLoading(false);
    }
  };

  return { data, error, loading, execute };
}

// Usage
function RetryComponent() {
  const { data, error, loading, execute } = useApiRetry(
    async (id) => {
      const response = await fetch(`https://api.example.com/data/${id}`);
      if (!response.ok) throw new Error('Failed to fetch');
      return response.json();
    }
  );
  
  return (
    <div>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error.message}</div>}
      {data && <div>{JSON.stringify(data)}</div>}
      <button onClick={() => execute(1)}>Fetch Data</button>
    </div>
  );
}
```

### 86. How do you implement a custom hook for handling API polling?
```jsx
function usePolling(fetchFn, interval = 5000) {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const pollingRef = useRef();

  const startPolling = useCallback(async (...args) => {
    const poll = async () => {
      setLoading(true);
      try {
        const result = await fetchFn(...args);
        setData(result);
        setError(null);
      } catch (error) {
        setError(error);
      } finally {
        setLoading(false);
      }
    };

    await poll();
    pollingRef.current = setInterval(poll, interval);
  }, [fetchFn, interval]);

  const stopPolling = useCallback(() => {
    if (pollingRef.current) {
      clearInterval(pollingRef.current);
    }
  }, []);

  useEffect(() => {
    return () => stopPolling();
  }, [stopPolling]);

  return { data, error, loading, startPolling, stopPolling };
}

// Usage
function PollingComponent() {
  const { data, error, loading, startPolling, stopPolling } = usePolling(
    async () => {
      const response = await fetch('https://api.example.com/status');
      return response.json();
    }
  );
  
  return (
    <div>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error.message}</div>}
      {data && <div>{JSON.stringify(data)}</div>}
      <button onClick={() => startPolling()}>Start Polling</button>
      <button onClick={stopPolling}>Stop Polling</button>
    </div>
  );
}
```

### 87. How do you implement a custom hook for handling API queuing?
```jsx
function useApiQueue() {
  const queue = useRef([]);
  const processing = useRef(false);
  const [results, setResults] = useState([]);

  const processQueue = async () => {
    if (processing.current || queue.current.length === 0) return;
    
    processing.current = true;
    const { request, resolve, reject } = queue.current[0];
    
    try {
      const result = await request();
      setResults(prev => [...prev, result]);
      resolve(result);
    } catch (error) {
      reject(error);
    } finally {
      queue.current.shift();
      processing.current = false;
      processQueue();
    }
  };

  const enqueue = (request) => {
    return new Promise((resolve, reject) => {
      queue.current.push({ request, resolve, reject });
      processQueue();
    });
  };

  return { enqueue, results };
}

// Usage
function QueueComponent() {
  const { enqueue, results } = useApiQueue();
  
  const handleClick = async () => {
    try {
      await enqueue(async () => {
        const response = await fetch('https://api.example.com/data');
        return response.json();
      });
    } catch (error) {
      console.error('Queue error:', error);
    }
  };
  
  return (
    <div>
      <button onClick={handleClick}>Add to Queue</button>
      <ul>
        {results.map((result, index) => (
          <li key={index}>{JSON.stringify(result)}</li>
        ))}
      </ul>
    </div>
  );
}
```

### 88. How do you implement a custom hook for handling API batching?
```jsx
function useApiBatch(batchSize = 5, delay = 1000) {
  const batch = useRef([]);
  const timeout = useRef();
  const [results, setResults] = useState([]);

  const addToBatch = (request) => {
    return new Promise((resolve, reject) => {
      batch.current.push({ request, resolve, reject });
      
      if (batch.current.length >= batchSize) {
        processBatch();
      } else if (!timeout.current) {
        timeout.current = setTimeout(processBatch, delay);
      }
    });
  };

  const processBatch = async () => {
    if (timeout.current) {
      clearTimeout(timeout.current);
      timeout.current = null;
    }
    
    if (batch.current.length === 0) return;
    
    const currentBatch = [...batch.current];
    batch.current = [];
    
    try {
      const results = await Promise.all(
        currentBatch.map(({ request }) => request())
      );
      
      setResults(prev => [...prev, ...results]);
      currentBatch.forEach(({ resolve }, index) => resolve(results[index]));
    } catch (error) {
      currentBatch.forEach(({ reject }) => reject(error));
    }
  };

  return { addToBatch, results };
}

// Usage
function BatchComponent() {
  const { addToBatch, results } = useApiBatch();
  
  const handleClick = async () => {
    try {
      await addToBatch(async () => {
        const response = await fetch('https://api.example.com/data');
        return response.json();
      });
    } catch (error) {
      console.error('Batch error:', error);
    }
  };
  
  return (
    <div>
      <button onClick={handleClick}>Add to Batch</button>
      <ul>
        {results.map((result, index) => (
          <li key={index}>{JSON.stringify(result)}</li>
        ))}
      </ul>
    </div>
  );
}
```

### 89. How do you implement a custom hook for handling API caching with invalidation?
```jsx
function useApiCacheWithInvalidation() {
  const cache = useRef(new Map());
  const [invalidationKey, setInvalidationKey] = useState(0);

  const getCachedData = (key) => {
    return cache.current.get(key);
  };

  const setCachedData = (key, data) => {
    cache.current.set(key, data);
  };

  const invalidateCache = () => {
    cache.current.clear();
    setInvalidationKey(prev => prev + 1);
  };

  const invalidateKey = (key) => {
    cache.current.delete(key);
    setInvalidationKey(prev => prev + 1);
  };

  return {
    getCachedData,
    setCachedData,
    invalidateCache,
    invalidateKey,
    invalidationKey
  };
}

// Usage
function CacheComponent() {
  const {
    getCachedData,
    setCachedData,
    invalidateCache,
    invalidateKey
  } = useApiCacheWithInvalidation();
  
  const [data, setData] = useState(null);
  
  const fetchData = async (id) => {
    const cachedData = getCachedData(`user-${id}`);
    if (cachedData) {
      setData(cachedData);
      return;
    }
    
    const response = await fetch(`https://api.example.com/users/${id}`);
    const newData = await response.json();
    setCachedData(`user-${id}`, newData);
    setData(newData);
  };
  
  return (
    <div>
      {data ? (
        <div>
          {JSON.stringify(data)}
          <button onClick={() => invalidateKey(`user-${data.id}`)}>
            Invalidate Cache
          </button>
        </div>
      ) : (
        <button onClick={() => fetchData(1)}>Load User</button>
      )}
      <button onClick={invalidateCache}>Clear All Cache</button>
    </div>
  );
}
```

### 90. How do you implement a custom hook for handling API caching with stale-while-revalidate?
```jsx
function useStaleWhileRevalidate(fetchFn, key, staleTime = 5000) {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const lastFetch = useRef(0);

  const fetchData = async () => {
    const now = Date.now();
    const isStale = now - lastFetch.current > staleTime;
    
    if (!isStale && data) {
      return data;
    }
    
    setLoading(true);
    try {
      const result = await fetchFn();
      setData(result);
      lastFetch.current = now;
      return result;
    } catch (error) {
      setError(error);
      throw error;
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, [key]);

  return { data, error, loading, refetch: fetchData };
}

// Usage
function StaleComponent() {
  const { data, error, loading, refetch } = useStaleWhileRevalidate(
    async () => {
      const response = await fetch('https://api.example.com/data');
      return response.json();
    },
    'data-key'
  );
  
  return (
    <div>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error.message}</div>}
      {data && <div>{JSON.stringify(data)}</div>}
      <button onClick={refetch}>Refresh</button>
    </div>
  );
}
```

### 91. How do you implement a custom hook for handling API caching with optimistic updates?
```jsx
function useOptimisticUpdate(fetchFn, updateFn) {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const update = async (optimisticData) => {
    // Optimistically update the UI
    setData(optimisticData);
    
    try {
      // Make the actual API call
      const result = await updateFn(optimisticData);
      setData(result);
    } catch (error) {
      // Revert on error
      setData(data);
      setError(error);
      throw error;
    }
  };

  useEffect(() => {
    const loadData = async () => {
      setLoading(true);
      try {
        const result = await fetchFn();
        setData(result);
      } catch (error) {
        setError(error);
      } finally {
        setLoading(false);
      }
    };
    
    loadData();
  }, []);

  return { data, error, loading, update };
}

// Usage
function OptimisticComponent() {
  const { data, error, loading, update } = useOptimisticUpdate(
    async () => {
      const response = await fetch('https://api.example.com/todos');
      return response.json();
    },
    async (newTodo) => {
      const response = await fetch('https://api.example.com/todos', {
        method: 'POST',
        body: JSON.stringify(newTodo)
      });
      return response.json();
    }
  );
  
  const handleAddTodo = async () => {
    const newTodo = { id: Date.now(), text: 'New Todo', completed: false };
    try {
      await update(newTodo);
    } catch (error) {
      console.error('Failed to add todo:', error);
    }
  };
  
  return (
    <div>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error.message}</div>}
      {data && (
        <ul>
          {data.map(todo => (
            <li key={todo.id}>{todo.text}</li>
          ))}
        </ul>
      )}
      <button onClick={handleAddTodo}>Add Todo</button>
    </div>
  );
}
```

### 92. How do you implement a custom hook for handling API caching with background updates?
```jsx
function useBackgroundUpdate(fetchFn, key, updateInterval = 30000) {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const [lastUpdate, setLastUpdate] = useState(null);

  const fetchData = async (showLoading = true) => {
    if (showLoading) setLoading(true);
    try {
      const result = await fetchFn();
      setData(result);
      setLastUpdate(new Date());
      return result;
    } catch (error) {
      setError(error);
      throw error;
    } finally {
      if (showLoading) setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
    
    const interval = setInterval(() => {
      fetchData(false);
    }, updateInterval);
    
    return () => clearInterval(interval);
  }, [key]);

  return { data, error, loading, lastUpdate, refetch: () => fetchData(true) };
}

// Usage
function BackgroundUpdateComponent() {
  const { data, error, loading, lastUpdate, refetch } = useBackgroundUpdate(
    async () => {
      const response = await fetch('https://api.example.com/data');
      return response.json();
    },
    'data-key'
  );
  
  return (
    <div>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error.message}</div>}
      {data && (
        <div>
          <div>{JSON.stringify(data)}</div>
          <div>Last updated: {lastUpdate?.toLocaleTimeString()}</div>
        </div>
      )}
      <button onClick={refetch}>Refresh Now</button>
    </div>
  );
}
```

### 93. How do you implement a custom hook for handling API caching with prefetching?
```jsx
function usePrefetch(fetchFn, prefetchKeys) {
  const cache = useRef(new Map());
  const [loading, setLoading] = useState(false);

  const prefetch = async (key) => {
    if (cache.current.has(key)) return;
    
    try {
      const result = await fetchFn(key);
      cache.current.set(key, result);
    } catch (error) {
      console.error('Prefetch error:', error);
    }
  };

  const getData = async (key) => {
    if (cache.current.has(key)) {
      return cache.current.get(key);
    }
    
    setLoading(true);
    try {
      const result = await fetchFn(key);
      cache.current.set(key, result);
      return result;
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    prefetchKeys.forEach(key => prefetch(key));
  }, [prefetchKeys]);

  return { getData, loading };
}

// Usage
function PrefetchComponent() {
  const { getData, loading } = usePrefetch(
    async (id) => {
      const response = await fetch(`https://api.example.com/users/${id}`);
      return response.json();
    },
    [1, 2, 3] // Prefetch these IDs
  );
  
  const [selectedUser, setSelectedUser] = useState(null);
  
  const handleSelect = async (id) => {
    const user = await getData(id);
    setSelectedUser(user);
  };
  
  return (
    <div>
      {loading && <div>Loading...</div>}
      {selectedUser && <div>{JSON.stringify(selectedUser)}</div>}
      <button onClick={() => handleSelect(1)}>User 1</button>
      <button onClick={() => handleSelect(2)}>User 2</button>
      <button onClick={() => handleSelect(3)}>User 3</button>
    </div>
  );
}
```

### 94. How do you implement a custom hook for handling API caching with selective updates?
```jsx
function useSelectiveUpdate(fetchFn, updateFn) {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const [updating, setUpdating] = useState(new Set());

  const update = async (id, updateData) => {
    setUpdating(prev => new Set(prev).add(id));
    
    try {
      const result = await updateFn(id, updateData);
      setData(prev => 
        prev.map(item => 
          item.id === id ? result : item
        )
      );
    } catch (error) {
      setError(error);
      throw error;
    } finally {
      setUpdating(prev => {
        const next = new Set(prev);
        next.delete(id);
        return next;
      });
    }
  };

  useEffect(() => {
    const loadData = async () => {
      setLoading(true);
      try {
        const result = await fetchFn();
        setData(result);
      } catch (error) {
        setError(error);
      } finally {
        setLoading(false);
      }
    };
    
    loadData();
  }, []);

  return { data, error, loading, updating, update };
}

// Usage
function SelectiveUpdateComponent() {
  const { data, error, loading, updating, update } = useSelectiveUpdate(
    async () => {
      const response = await fetch('https://api.example.com/todos');
      return response.json();
    },
    async (id, data) => {
      const response = await fetch(`https://api.example.com/todos/${id}`, {
        method: 'PUT',
        body: JSON.stringify(data)
      });
      return response.json();
    }
  );
  
  const handleToggle = async (id, completed) => {
    try {
      await update(id, { completed });
    } catch (error) {
      console.error('Failed to update todo:', error);
    }
  };
  
  return (
    <div>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error.message}</div>}
      {data && (
        <ul>
          {data.map(todo => (
            <li key={todo.id}>
              <input
                type="checkbox"
                checked={todo.completed}
                onChange={e => handleToggle(todo.id, e.target.checked)}
                disabled={updating.has(todo.id)}
              />
              {todo.text}
              {updating.has(todo.id) && ' (updating...)'}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
```

### 95. How do you implement a custom hook for handling API caching with offline support?
```jsx
function useOfflineCache(fetchFn, key) {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const [isOnline, setIsOnline] = useState(navigator.onLine);
  const queue = useRef([]);

  const updateData = async (newData) => {
    if (isOnline) {
      try {
        await fetchFn(newData);
        setData(newData);
      } catch (error) {
        setError(error);
        throw error;
      }
    } else {
      queue.current.push(newData);
      setData(newData);
    }
  };

  useEffect(() => {
    const handleOnline = () => {
      setIsOnline(true);
      // Process queued updates
      queue.current.forEach(async (queuedData) => {
        try {
          await fetchFn(queuedData);
        } catch (error) {
          console.error('Failed to sync queued update:', error);
        }
      });
      queue.current = [];
    };

    const handleOffline = () => {
      setIsOnline(false);
    };

    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);

    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, []);

  useEffect(() => {
    const loadData = async () => {
      setLoading(true);
      try {
        const result = await fetchFn();
        setData(result);
      } catch (error) {
        setError(error);
      } finally {
        setLoading(false);
      }
    };
    
    loadData();
  }, [key]);

  return { data, error, loading, isOnline, update: updateData };
}

// Usage
function OfflineComponent() {
  const { data, error, loading, isOnline, update } = useOfflineCache(
    async (newData) => {
      const response = await fetch('https://api.example.com/data', {
        method: 'PUT',
        body: JSON.stringify(newData)
      });
      return response.json();
    },
    'data-key'
  );
  
  const handleUpdate = async () => {
    try {
      await update({ ...data, updated: true });
    } catch (error) {
      console.error('Failed to update:', error);
    }
  };
  
  return (
    <div>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error.message}</div>}
      {data && (
        <div>
          <div>{JSON.stringify(data)}</div>
          <div>Status: {isOnline ? 'Online' : 'Offline'}</div>
          <button onClick={handleUpdate}>Update</button>
        </div>
      )}
    </div>
  );
}
```

### 96. How do you implement a custom hook for handling API caching with versioning?
```jsx
function useVersionedCache(fetchFn, key, version) {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const cache = useRef(new Map());

  const getCachedData = () => {
    const cached = cache.current.get(key);
    if (cached && cached.version === version) {
      return cached.data;
    }
    return null;
  };

  const setCachedData = (data) => {
    cache.current.set(key, data);
  };

  const fetchData = async () => {
    const cached = getCachedData();
    if (cached) {
      setData(cached);
      return;
    }
    
    setLoading(true);
    try {
      const result = await fetchFn();
      setCachedData(result);
      setData(result);
    } catch (error) {
      setError(error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, [key, version]);

  return { data, error, loading, refetch: fetchData };
}

// Usage
function VersionedComponent() {
  const [version, setVersion] = useState(1);
  const { data, error, loading, refetch } = useVersionedCache(
    async () => {
      const response = await fetch('https://api.example.com/data');
      return response.json();
    },
    'data-key',
    version
  );
  
  return (
    <div>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error.message}</div>}
      {data && <div>{JSON.stringify(data)}</div>}
      <button onClick={() => setVersion(prev => prev + 1)}>
        Invalidate Cache
      </button>
    </div>
  );
}
```

### 97. How do you implement a custom hook for handling API caching with time-based invalidation?
```jsx
function useTimeBasedCache(fetchFn, key, ttl = 5 * 60 * 1000) {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const cache = useRef(new Map());

  const getCachedData = () => {
    const cached = cache.current.get(key);
    if (cached && Date.now() - cached.timestamp < ttl) {
      return cached.data;
    }
    return null;
  };

  const setCachedData = (data) => {
    cache.current.set(key, { data, timestamp: Date.now() });
  };

  const fetchData = async () => {
    const cached = getCachedData();
    if (cached) {
      setData(cached);
      return;
    }
    
    setLoading(true);
    try {
      const result = await fetchFn();
      setCachedData(result);
      setData(result);
    } catch (error) {
      setError(error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
    
    const interval = setInterval(() => {
      const cached = getCachedData();
      if (!cached) {
        fetchData();
      }
    }, ttl);
    
    return () => clearInterval(interval);
  }, [key]);

  return { data, error, loading, refetch: fetchData };
}

// Usage
function TimeBasedComponent() {
  const { data, error, loading, refetch } = useTimeBasedCache(
    async () => {
      const response = await fetch('https://api.example.com/data');
      return response.json();
    },
    'data-key',
    30000 // 30 seconds TTL
  );
  
  return (
    <div>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error.message}</div>}
      {data && <div>{JSON.stringify(data)}</div>}
      <button onClick={refetch}>Refresh Now</button>
    </div>
  );
}
```

### 98. How do you implement a custom hook for handling API caching with dependency-based invalidation?
```jsx
function useDependencyCache(fetchFn, key, dependencies = []) {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const cache = useRef(new Map());

  const getCacheKey = () => {
    return `${key}-${dependencies.join('-')}`;
  };

  const getCachedData = () => {
    return cache.current.get(getCacheKey());
  };

  const setCachedData = (data) => {
    cache.current.set(getCacheKey(), data);
  };

  const fetchData = async () => {
    const cached = getCachedData();
    if (cached) {
      setData(cached);
      return;
    }
    
    setLoading(true);
    try {
      const result = await fetchFn();
      setCachedData(result);
      setData(result);
    } catch (error) {
      setError(error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, [key, ...dependencies]);

  return { data, error, loading, refetch: fetchData };
}

// Usage
function DependencyComponent() {
  const [userId, setUserId] = useState(1);
  const [filter, setFilter] = useState('all');
  
  const { data, error, loading, refetch } = useDependencyCache(
    async () => {
      const response = await fetch(
        `https://api.example.com/users/${userId}/todos?filter=${filter}`
      );
      return response.json();
    },
    'todos',
    [userId, filter]
  );
  
  return (
    <div>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error.message}</div>}
      {data && <div>{JSON.stringify(data)}</div>}
      <button onClick={() => setUserId(prev => prev + 1)}>
        Next User
      </button>
      <button onClick={() => setFilter('completed')}>
        Show Completed
      </button>
    </div>
  );
}
```

### 99. How do you implement a custom hook for handling API caching with priority-based invalidation?
```jsx
function usePriorityCache(fetchFn, key, priority = 'low') {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const cache = useRef(new Map());
  const priorities = {
    low: 5 * 60 * 1000,    // 5 minutes
    medium: 60 * 1000,     // 1 minute
    high: 10 * 1000        // 10 seconds
  };

  const getCachedData = () => {
    const cached = cache.current.get(key);
    if (cached && Date.now() - cached.timestamp < priorities[priority]) {
      return cached.data;
    }
    return null;
  };

  const setCachedData = (data) => {
    cache.current.set(key, data);
  };

  const fetchData = async () => {
    const cached = getCachedData();
    if (cached) {
      setData(cached);
      return;
    }
    
    setLoading(true);
    try {
      const result = await fetchFn();
      setCachedData(result);
      setData(result);
    } catch (error) {
      setError(error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
    
    const interval = setInterval(() => {
      const cached = getCachedData();
      if (!cached) {
        fetchData();
      }
    }, priorities[priority]);
    
    return () => clearInterval(interval);
  }, [key, priority]);

  return { data, error, loading, refetch: fetchData };
}

// Usage
function PriorityComponent() {
  const [priority, setPriority] = useState('low');
  const { data, error, loading, refetch } = usePriorityCache(
    async () => {
      const response = await fetch('https://api.example.com/data');
      return response.json();
    },
    'data-key',
    priority
  );
  
  return (
    <div>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error.message}</div>}
      {data && <div>{JSON.stringify(data)}</div>}
      <select value={priority} onChange={e => setPriority(e.target.value)}>
        <option value="low">Low Priority</option>
        <option value="medium">Medium Priority</option>
        <option value="high">High Priority</option>
      </select>
      <button onClick={refetch}>Refresh Now</button>
    </div>
  );
}
```

### 100. How do you implement a custom hook for handling API caching with adaptive invalidation?
```jsx
function useAdaptiveCache(fetchFn, key) {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const cache = useRef(new Map());
  const lastUpdate = useRef(Date.now());
  const updateInterval = useRef(5 * 60 * 1000); // Start with 5 minutes

  const getCachedData = () => {
    const cached = cache.current.get(key);
    if (cached && Date.now() - cached.timestamp < updateInterval.current) {
      return cached.data;
    }
    return null;
  };

  const setCachedData = (data) => {
    cache.current.set(key, data);
  };

  const adjustInterval = (newData) => {
    const now = Date.now();
    const timeSinceLastUpdate = now - lastUpdate.current;
    
    // If data changed, decrease interval
    if (JSON.stringify(data) !== JSON.stringify(newData)) {
      updateInterval.current = Math.max(
        10 * 1000, // Minimum 10 seconds
        updateInterval.current * 0.8 // Reduce by 20%
      );
    } else {
      // If data didn't change, increase interval
      updateInterval.current = Math.min(
        30 * 60 * 1000, // Maximum 30 minutes
        updateInterval.current * 1.2 // Increase by 20%
      );
    }
    
    lastUpdate.current = now;
  };

  const fetchData = async () => {
    const cached = getCachedData();
    if (cached) {
      setData(cached);
      return;
    }
    
    setLoading(true);
    try {
      const result = await fetchFn();
      adjustInterval(result);
      setCachedData(result);
      setData(result);
    } catch (error) {
      setError(error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
    
    const interval = setInterval(() => {
      const cached = getCachedData();
      if (!cached) {
        fetchData();
      }
    }, updateInterval.current);
    
    return () => clearInterval(interval);
  }, [key]);

  return { data, error, loading, refetch: fetchData };
}

// Usage
function AdaptiveComponent() {
  const { data, error, loading, refetch } = useAdaptiveCache(
    async () => {
      const response = await fetch('https://api.example.com/data');
      return response.json();
    },
    'data-key'
  );
  
  return (
    <div>
      {loading && <div>Loading...</div>}
      {error && <div>Error: {error.message}</div>}
      {data && <div>{JSON.stringify(data)}</div>}
      <button onClick={refetch}>Refresh Now</button>
    </div>
  );
}
```

## Modern React Features

### React Server Components
React Server Components (RSC) is a paradigm that allows components to run on the server, reducing the JavaScript bundle size sent to the client. They are a core feature of Next.js 13+ App Router.

**Key rules:**
- Server Components can `async/await` data fetching directly
- Server Components cannot use state, effects, or browser-only APIs
- Client Components must be marked with `'use client'`
- Server Components can import Client Components, but not vice versa

```jsx
// Server Component
async function UserProfile({ userId }) {
  const user = await fetchUser(userId); // Runs on server
  
  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </div>
  );
}

// Client Component
'use client';
function UserActions({ userId }) {
  const [liked, setLiked] = useState(false);
  
  return (
    <button onClick={() => setLiked(!liked)}>
      {liked ? 'Unlike' : 'Like'}
    </button>
  );
}
```

### Suspense and Concurrent Features
React Suspense allows components to "wait" for something before rendering, improving the user experience.

```jsx
function App() {
  return (
    <Suspense fallback={<Loading />}>
      <UserProfile />
    </Suspense>
  );
}

// Using concurrent features
function ConcurrentComponent() {
  const [isPending, startTransition] = useTransition();
  
  const handleClick = () => {
    startTransition(() => {
      // Non-urgent updates
      setCount(c => c + 1);
    });
  };
  
  return (
    <div>
      {isPending ? <Spinner /> : null}
      <button onClick={handleClick}>Increment</button>
    </div>
  );
}
```

### React Query/SWR
Modern data fetching libraries that handle caching, revalidation, and state management.

```jsx
// Using TanStack Query (React Query v5)
import { useQuery, QueryClient, QueryClientProvider } from '@tanstack/react-query';

const queryClient = new QueryClient();

function UserProfile() {
  const { data, isLoading, error } = useQuery({
    queryKey: ['user'],
    queryFn: fetchUser,
    staleTime: 5 * 60 * 1000, // 5 minutes
  });

  if (isLoading) return <Loading />;
  if (error) return <Error message={error.message} />;

  return <div>{data.name}</div>;
}

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <UserProfile />
    </QueryClientProvider>
  );
}
```

```jsx
// Using SWR
import useSWR from 'swr';

function UserProfile() {
  const { data, error, isLoading } = useSWR('/api/user', fetcher);

  if (error) return <Error />;
  if (isLoading) return <Loading />;

  return <div>{data.name}</div>;
}
```

### React 18 Features
React 18 introduces new features for concurrent rendering and automatic batching.

```jsx
// Automatic batching (React 18 batches ALL state updates, even in async code)
function BatchExample() {
  const [count, setCount] = useState(0);
  const [flag, setFlag] = useState(false);
  
  async function handleClick() {
    // In React 17, these would cause 2 re-renders in async callbacks
    // In React 18, these are automatically batched into 1 re-render
    setCount(c => c + 1);
    setFlag(f => !f);
  }
  
  return <button onClick={handleClick}>Click</button>;
}

// Using createRoot (required for React 18 features)
import { createRoot } from 'react-dom/client';

const root = createRoot(document.getElementById('root'));
root.render(<App />);

// useId - generates unique IDs for accessibility
function FormField() {
  const id = useId();
  return (
    <div>
      <label htmlFor={id}>Name</label>
      <input id={id} />
    </div>
  );
}

// useDeferredValue - defers updating a value for smoother UI
function SearchResults({ query }) {
  const deferredQuery = useDeferredValue(query);
  const results = useMemo(() => filterResults(deferredQuery), [deferredQuery]);
  return <ResultsList results={results} />;
}
```

### React 19 Features (2024+)
React 19 introduces significant improvements for data handling and forms.

```jsx
// use() hook - read resources (promises, context) during render
function UserProfile({ userPromise }) {
  const user = use(userPromise); // Suspends until resolved
  return <div>{user.name}</div>;
}

// Server Actions with forms
async function submitForm(formData) {
  'use server';
  const name = formData.get('name');
  await saveToDatabase(name);
}

function SignupForm() {
  return (
    <form action={submitForm}>
      <input name="name" />
      <button type="submit">Submit</button>
    </form>
  );
}

// useFormStatus - get pending state of parent form
import { useFormStatus } from 'react-dom';

function SubmitButton() {
  const { pending } = useFormStatus();
  return <button disabled={pending}>{pending ? 'Submitting...' : 'Submit'}</button>;
}

// useActionState - manage form action state (replaces useFormState)
import { useActionState } from 'react';

function AddToCart({ itemId }) {
  const [message, formAction, isPending] = useActionState(addToCartAction, null);
  return (
    <form action={formAction}>
      <input type="hidden" name="itemId" value={itemId} />
      <button type="submit" disabled={isPending}>Add to Cart</button>
      {message && <p>{message}</p>}
    </form>
  );
}

// useOptimistic - optimistic UI updates
import { useOptimistic } from 'react';

function TodoList({ todos, addTodoAction }) {
  const [optimisticTodos, addOptimisticTodo] = useOptimistic(
    todos,
    (state, newTodo) => [...state, { ...newTodo, sending: true }]
  );

  return (
    <form action={async (formData) => {
      addOptimisticTodo({ text: formData.get('text') });
      await addTodoAction(formData);
    }}>
      <input name="text" />
      <button type="submit">Add</button>
      <ul>
        {optimisticTodos.map(todo => (
          <li key={todo.id} style={{ opacity: todo.sending ? 0.5 : 1 }}>
            {todo.text}
          </li>
        ))}
      </ul>
    </form>
  );
}
```

> **Other React 19 improvements:** `ref` as a prop (no more `forwardRef`), `<Context>` as a provider (no more `<Context.Provider>`), cleanup functions in `ref` callbacks, document metadata support (`<title>`, `<meta>` in components), and native stylesheet/script support.

## TypeScript Integration

### TypeScript with React
TypeScript provides type safety and better developer experience in React applications.

```tsx
// Props interface
interface ButtonProps {
  text: string;
  onClick: () => void;
  variant?: 'primary' | 'secondary';
}

// Typed component
const Button: React.FC<ButtonProps> = ({ text, onClick, variant = 'primary' }) => {
  return (
    <button 
      className={`btn-${variant}`}
      onClick={onClick}
    >
      {text}
    </button>
  );
};

// Using the component
<Button 
  text="Click me"
  onClick={() => console.log('clicked')}
  variant="secondary"
/>
```

### Type Definitions for Props and State
Proper type definitions improve code quality and catch errors early.

```tsx
// State types
interface UserState {
  id: number;
  name: string;
  email: string;
  preferences: {
    theme: 'light' | 'dark';
    notifications: boolean;
  };
}

function UserProfile() {
  const [user, setUser] = useState<UserState | null>(null);
  
  // TypeScript will ensure type safety
  const updateUser = (updates: Partial<UserState>) => {
    setUser(prev => prev ? { ...prev, ...updates } : null);
  };
  
  return (
    <div>
      {user ? (
        <div>
          <h1>{user.name}</h1>
          <p>{user.email}</p>
        </div>
      ) : (
        <Loading />
      )}
    </div>
  );
}
```

### Generic Components
Generic components provide type safety while maintaining flexibility.

```tsx
interface ListProps<T> {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
}

function List<T>({ items, renderItem }: ListProps<T>) {
  return (
    <ul>
      {items.map((item, index) => (
        <li key={index}>{renderItem(item)}</li>
      ))}
    </ul>
  );
}

// Usage
interface User {
  id: number;
  name: string;
}

function UserList() {
  const users: User[] = [
    { id: 1, name: 'John' },
    { id: 2, name: 'Jane' }
  ];
  
  return (
    <List
      items={users}
      renderItem={(user) => <div>{user.name}</div>}
    />
  );
}
```

### Type-Safe Hooks
Creating type-safe custom hooks ensures proper usage and error prevention.

```tsx
function useLocalStorage<T>(key: string, initialValue: T) {
  const [storedValue, setStoredValue] = useState<T>(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error(error);
      return initialValue;
    }
  });

  const setValue = (value: T | ((val: T) => T)) => {
    try {
      const valueToStore = value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error(error);
    }
  };

  return [storedValue, setValue] as const;
}

// Usage
function UserSettings() {
  const [settings, setSettings] = useLocalStorage<{
    theme: 'light' | 'dark';
    fontSize: number;
  }>('settings', {
    theme: 'light',
    fontSize: 16
  });
  
  return (
    <div>
      <select
        value={settings.theme}
        onChange={e => setSettings(prev => ({
          ...prev,
          theme: e.target.value as 'light' | 'dark'
        }))}
      >
        <option value="light">Light</option>
        <option value="dark">Dark</option>
      </select>
    </div>
  );
}
```

## Testing

### Jest and React Testing Library
Modern testing approaches focus on user behavior rather than implementation details.

```tsx
import { render, screen, fireEvent } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

function Counter() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(c => c + 1)}>Increment</button>
    </div>
  );
}

describe('Counter', () => {
  test('increments count when button is clicked', async () => {
    render(<Counter />);
    
    const button = screen.getByRole('button', { name: /increment/i });
    const count = screen.getByText(/count: 0/i);
    
    await userEvent.click(button);
    
    expect(screen.getByText(/count: 1/i)).toBeInTheDocument();
  });
});
```

### Component Testing
Testing individual components in isolation.

```tsx
function UserCard({ user, onEdit }) {
  return (
    <div className="user-card">
      <h2>{user.name}</h2>
      <p>{user.email}</p>
      <button onClick={() => onEdit(user)}>Edit</button>
    </div>
  );
}

describe('UserCard', () => {
  const mockUser = {
    id: 1,
    name: 'John Doe',
    email: 'john@example.com'
  };
  
  const mockOnEdit = jest.fn();
  
  test('renders user information correctly', () => {
    render(<UserCard user={mockUser} onEdit={mockOnEdit} />);
    
    expect(screen.getByText(mockUser.name)).toBeInTheDocument();
    expect(screen.getByText(mockUser.email)).toBeInTheDocument();
  });
  
  test('calls onEdit when edit button is clicked', async () => {
    render(<UserCard user={mockUser} onEdit={mockOnEdit} />);
    
    const editButton = screen.getByRole('button', { name: /edit/i });
    await userEvent.click(editButton);
    
    expect(mockOnEdit).toHaveBeenCalledWith(mockUser);
  });
});
```

### Integration Testing
Testing how components work together.

```tsx
function UserList() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    fetchUsers().then(data => {
      setUsers(data);
      setLoading(false);
    });
  }, []);
  
  if (loading) return <Loading />;
  
  return (
    <div>
      {users.map(user => (
        <UserCard key={user.id} user={user} />
      ))}
    </div>
  );
}

describe('UserList Integration', () => {
  test('loads and displays users', async () => {
    const mockUsers = [
      { id: 1, name: 'John' },
      { id: 2, name: 'Jane' }
    ];
    
    global.fetch = jest.fn().mockResolvedValue({
      json: () => Promise.resolve(mockUsers)
    });
    
    render(<UserList />);
    
    expect(screen.getByText(/loading/i)).toBeInTheDocument();
    
    const userCards = await screen.findAllByRole('heading');
    expect(userCards).toHaveLength(2);
    expect(userCards[0]).toHaveTextContent('John');
    expect(userCards[1]).toHaveTextContent('Jane');
  });
});
```

### E2E Testing with Cypress
End-to-end testing ensures the entire application works as expected.

```tsx
// cypress/integration/user-flow.spec.ts
describe('User Flow', () => {
  beforeEach(() => {
    cy.visit('/');
  });
  
  it('completes user registration', () => {
    cy.get('[data-testid="register-button"]').click();
    
    cy.get('[data-testid="name-input"]').type('John Doe');
    cy.get('[data-testid="email-input"]').type('john@example.com');
    cy.get('[data-testid="password-input"]').type('password123');
    
    cy.get('[data-testid="submit-button"]').click();
    
    cy.url().should('include', '/dashboard');
    cy.get('[data-testid="welcome-message"]')
      .should('contain', 'Welcome, John Doe');
  });
  
  it('handles login and profile update', () => {
    cy.get('[data-testid="login-button"]').click();
    
    cy.get('[data-testid="email-input"]').type('john@example.com');
    cy.get('[data-testid="password-input"]').type('password123');
    
    cy.get('[data-testid="submit-button"]').click();
    
    cy.get('[data-testid="profile-link"]').click();
    cy.get('[data-testid="edit-profile"]').click();
    
    cy.get('[data-testid="bio-input"]')
      .type('Software Developer');
    
    cy.get('[data-testid="save-button"]').click();
    
    cy.get('[data-testid="bio"]')
      .should('contain', 'Software Developer');
  });
});
```

## Performance Optimization

### Code Splitting Strategies
Implementing efficient code splitting to reduce initial bundle size.

```tsx
// Route-based code splitting
import { lazy, Suspense } from 'react';
import { Routes, Route } from 'react-router-dom';

const Home = lazy(() => import('./pages/Home'));
const About = lazy(() => import('./pages/About'));
const Contact = lazy(() => import('./pages/Contact'));

function App() {
  return (
    <Suspense fallback={<Loading />}>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </Suspense>
  );
}

// Component-based code splitting
const HeavyComponent = lazy(() => import('./HeavyComponent'));

function ParentComponent() {
  const [showHeavy, setShowHeavy] = useState(false);
  
  return (
    <div>
      <button onClick={() => setShowHeavy(true)}>
        Load Heavy Component
      </button>
      
      {showHeavy && (
        <Suspense fallback={<Loading />}>
          <HeavyComponent />
        </Suspense>
      )}
    </div>
  );
}
```

### Bundle Optimization
Techniques to optimize the JavaScript bundle size.

```tsx
// Tree shaking friendly exports
export const Button = ({ children, ...props }) => (
  <button {...props}>{children}</button>
);

export const Input = ({ ...props }) => (
  <input {...props} />
);

// Dynamic imports with webpack
const loadComponent = () => import('./HeavyComponent');

// Using webpack magic comments
const Component = lazy(() => import(
  /* webpackChunkName: "component" */
  /* webpackPrefetch: true */
  './Component'
));
```

### Memory Leak Prevention
Preventing memory leaks in React applications.

```tsx
function DataFetcher() {
  const [data, setData] = useState(null);
  
  useEffect(() => {
    let isMounted = true;
    
    const fetchData = async () => {
      try {
        const result = await api.getData();
        if (isMounted) {
          setData(result);
        }
      } catch (error) {
        if (isMounted) {
          console.error(error);
        }
      }
    };
    
    fetchData();
    
    return () => {
      isMounted = false;
    };
  }, []);
  
  return <div>{data ? JSON.stringify(data) : 'Loading...'}</div>;
}

// Using AbortController
function SearchComponent() {
  const [results, setResults] = useState([]);
  
  useEffect(() => {
    const controller = new AbortController();
    
    const search = async (query) => {
      try {
        const response = await fetch(
          `/api/search?q=${query}`,
          { signal: controller.signal }
        );
        const data = await response.json();
        setResults(data);
      } catch (error) {
        if (error.name === 'AbortError') {
          console.log('Search aborted');
        }
      }
    };
    
    search('react');
    
    return () => {
      controller.abort();
    };
  }, []);
  
  return <div>{/* render results */}</div>;
}
```

### Performance Monitoring
Implementing performance monitoring in React applications.

```tsx
// Using React Profiler
function ProfilerExample() {
  const handleRender = (
    id,
    phase,
    actualDuration,
    baseDuration,
    startTime,
    commitTime
  ) => {
    console.log({
      id,
      phase,
      actualDuration,
      baseDuration,
      startTime,
      commitTime
    });
  };
  
  return (
    <Profiler id="app" onRender={handleRender}>
      <App />
    </Profiler>
  );
}

// Custom performance hook
function usePerformanceMonitor(componentName) {
  useEffect(() => {
    const startTime = performance.now();
    
    return () => {
      const endTime = performance.now();
      const duration = endTime - startTime;
      
      console.log(`${componentName} mounted for ${duration}ms`);
    };
  }, [componentName]);
}

// Usage
function MonitoredComponent() {
  usePerformanceMonitor('MonitoredComponent');
  
  return <div>Content</div>;
}
```

## State Management

### Redux Toolkit
Modern Redux with simplified setup and best practices.

```tsx
// store.ts
import { configureStore, createSlice } from '@reduxjs/toolkit';

const counterSlice = createSlice({
  name: 'counter',
  initialState: { value: 0 },
  reducers: {
    increment: state => {
      state.value += 1;
    },
    decrement: state => {
      state.value -= 1;
    }
  }
});

export const { increment, decrement } = counterSlice.actions;

export const store = configureStore({
  reducer: {
    counter: counterSlice.reducer
  }
});

// Component
function Counter() {
  const count = useSelector(state => state.counter.value);
  const dispatch = useDispatch();
  
  return (
    <div>
      <button onClick={() => dispatch(decrement())}>-</button>
      <span>{count}</span>
      <button onClick={() => dispatch(increment())}>+</button>
    </div>
  );
}
```

### Zustand
Lightweight state management with hooks.

```tsx
import create from 'zustand';

const useStore = create((set) => ({
  bears: 0,
  increasePopulation: () => set((state) => ({ bears: state.bears + 1 })),
  removeAllBears: () => set({ bears: 0 })
}));

function BearCounter() {
  const bears = useStore((state) => state.bears);
  const increasePopulation = useStore((state) => state.increasePopulation);
  
  return (
    <div>
      <h1>{bears} bears around here...</h1>
      <button onClick={increasePopulation}>one up</button>
    </div>
  );
}
```

### Jotai
Atomic state management for React.

```tsx
import { atom, useAtom } from 'jotai';

const countAtom = atom(0);
const doubleAtom = atom((get) => get(countAtom) * 2);

function Counter() {
  const [count, setCount] = useAtom(countAtom);
  const [doubled] = useAtom(doubleAtom);
  
  return (
    <div>
      <p>Count: {count}</p>
      <p>Doubled: {doubled}</p>
      <button onClick={() => setCount(c => c + 1)}>Increment</button>
    </div>
  );
}
```

### Recoil
Facebook's experimental state management library.

```tsx
import { atom, selector, useRecoilState, useRecoilValue } from 'recoil';

const countState = atom({
  key: 'countState',
  default: 0
});

const doubleCountState = selector({
  key: 'doubleCountState',
  get: ({get}) => {
    const count = get(countState);
    return count * 2;
  }
});

function Counter() {
  const [count, setCount] = useRecoilState(countState);
  const doubledCount = useRecoilValue(doubleCountState);
  
  return (
    <div>
      <p>Count: {count}</p>
      <p>Doubled: {doubledCount}</p>
      <button onClick={() => setCount(c => c + 1)}>Increment</button>
    </div>
  );
}
```

## Build Tools

### Vite
Next-generation frontend tooling.

```tsx
// vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist',
    sourcemap: true,
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
          utils: ['./src/utils']
        }
      }
    }
  }
});
```

### Next.js
React framework for production with both Pages Router and App Router.

```tsx
// App Router (Next.js 13+, recommended)
// app/users/page.tsx - Server Component by default
async function UsersPage() {
  const users = await fetch('https://api.example.com/users').then(r => r.json());
  return (
    <div>
      <h1>Users</h1>
      {users.map(user => <div key={user.id}>{user.name}</div>)}
    </div>
  );
}

export default UsersPage;

// app/users/[id]/page.tsx - Dynamic route
async function UserPage({ params }: { params: { id: string } }) {
  const user = await fetch(`https://api.example.com/users/${params.id}`).then(r => r.json());
  return <h1>{user.name}</h1>;
}

export default UserPage;
```

```tsx
// Pages Router (legacy but still supported)
// pages/index.tsx
import { GetServerSideProps } from 'next';

export const getServerSideProps: GetServerSideProps = async () => {
  const data = await fetchData();
  return {
    props: { data }
  };
};

function HomePage({ data }) {
  return (
    <div>
      <h1>Welcome to Next.js</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default HomePage;
```

### Remix
Full stack web framework.

```tsx
// app/routes/index.tsx
import { json } from '@remix-run/node';
import { useLoaderData } from '@remix-run/react';

export async function loader() {
  const data = await fetchData();
  return json({ data });
}

export default function Index() {
  const { data } = useLoaderData();
  
  return (
    <div>
      <h1>Welcome to Remix</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
```

## React Best Practices

### Component Composition Patterns
Effective patterns for component composition.

```tsx
// Compound Components
const Tabs = ({ children }) => {
  const [activeTab, setActiveTab] = useState(0);
  
  return (
    <TabsContext.Provider value={{ activeTab, setActiveTab }}>
      {children}
    </TabsContext.Provider>
  );
};

Tabs.List = function TabsList({ children }) {
  return <div className="tabs-list">{children}</div>;
};

Tabs.Tab = function Tab({ index, children }) {
  const { activeTab, setActiveTab } = useContext(TabsContext);
  
  return (
    <button
      className={activeTab === index ? 'active' : ''}
      onClick={() => setActiveTab(index)}
    >
      {children}
    </button>
  );
};

Tabs.Panel = function Panel({ index, children }) {
  const { activeTab } = useContext(TabsContext);
  
  return activeTab === index ? <div>{children}</div> : null;
};

// Usage
function App() {
  return (
    <Tabs>
      <Tabs.List>
        <Tabs.Tab index={0}>Tab 1</Tabs.Tab>
        <Tabs.Tab index={1}>Tab 2</Tabs.Tab>
      </Tabs.List>
      <Tabs.Panel index={0}>Content 1</Tabs.Panel>
      <Tabs.Panel index={1}>Content 2</Tabs.Panel>
    </Tabs>
  );
}
```

### Error Boundary Implementation
Proper error handling with error boundaries.

```tsx
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    // Log error to service
    console.error('Error:', error);
    console.error('Error Info:', errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="error-boundary">
          <h1>Something went wrong</h1>
          <details>
            <summary>Error Details</summary>
            <pre>{this.state.error?.toString()}</pre>
          </details>
          <button onClick={() => this.setState({ hasError: false })}>
            Try Again
          </button>
        </div>
      );
    }

    return this.props.children;
  }
}

// Usage
function App() {
  return (
    <ErrorBoundary>
      <MyComponent />
    </ErrorBoundary>
  );
}
```

### Performance Optimization Techniques
Advanced performance optimization strategies.

```tsx
// Memoization
const MemoizedComponent = React.memo(function MyComponent({ data }) {
  return <div>{data.map(item => <Item key={item.id} {...item} />)}</div>;
});

// useMemo for expensive calculations
function ExpensiveComponent({ items }) {
  const sortedItems = useMemo(() => {
    return items.sort((a, b) => a.value - b.value);
  }, [items]);
  
  return <div>{sortedItems.map(item => <Item key={item.id} {...item} />)}</div>;
}

// useCallback for stable function references
function ParentComponent() {
  const [count, setCount] = useState(0);
  
  const handleClick = useCallback(() => {
    setCount(c => c + 1);
  }, []);
  
  return <ChildComponent onClick={handleClick} />;
}
```

### Security Considerations
Implementing security best practices in React applications.

```tsx
// XSS Prevention
function SafeComponent({ userInput }) {
  // Don't do this
  // return <div>{userInput}</div>;
  
  // Do this instead
  return <div>{escapeHtml(userInput)}</div>;
}

// Use DOMPurify for sanitizing HTML
import DOMPurify from 'dompurify';
function SafeHtml({ html }) {
  return <div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(html) }} />;
}

// CSRF Protection
function SecureForm() {
  const [csrfToken, setCsrfToken] = useState('');
  
  useEffect(() => {
    // Fetch CSRF token from server
    fetch('/api/csrf-token')
      .then(res => res.json())
      .then(data => setCsrfToken(data.token));
  }, []);
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    
    await fetch('/api/submit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRF-Token': csrfToken
      },
      body: JSON.stringify(formData)
    });
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <input type="hidden" name="csrf-token" value={csrfToken} />
      {/* form fields */}
    </form>
  );
}

// Authentication & Authorization
// Use secure cookies (httpOnly, secure, sameSite)
// Store secrets in environment variables, not in code
// Always use HTTPS in production
// Audit dependencies for vulnerabilities (e.g., npm audit)
```

**Recommended Libraries:**
- [DOMPurify](https://github.com/cure53/DOMPurify) for sanitizing HTML
- [Helmet](https://helmetjs.github.io/) for setting HTTP headers (server-side)
- [jsonwebtoken](https://github.com/auth0/node-jsonwebtoken) for JWT handling
- [OWASP Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/React_Security_Cheat_Sheet.html)

### Accessibility Guidelines
Implementing accessibility features in React components.

```tsx
// Accessible Button
function AccessibleButton({ onClick, children }) {
  return (
    <button
      onClick={onClick}
      role="button"
      tabIndex={0}
      aria-pressed="false"
      onKeyPress={(e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          onClick();
        }
      }}
    >
      {children}
    </button>
  );
}

// Accessible Form
function AccessibleForm() {
  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="username">Username:</label>
      <input
        id="username"
        name="username"
        aria-required="true"
        aria-describedby="username-error"
      />
      <span id="username-error" role="alert">
        {errors.username}
      </span>
      <button type="submit">Submit</button>
    </form>
  );
}

// Accessible Modal
function AccessibleModal({ isOpen, onClose, children }) {
  const modalRef = useRef();
  
  useEffect(() => {
    if (isOpen) {
      modalRef.current?.focus();
    }
  }, [isOpen]);
  
  if (!isOpen) return null;
  
  return (
    <div
      role="dialog"
      aria-modal="true"
      aria-labelledby="modal-title"
      ref={modalRef}
      tabIndex={-1}
    >
      <h2 id="modal-title">Modal Title</h2>
      {children}
      <button onClick={onClose}>Close</button>
    </div>
  );
}
```

**Advanced Accessibility Topics:**
- Use proper ARIA roles and attributes
- Ensure keyboard navigation for all interactive elements
- Maintain sufficient color contrast (use tools like [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/))
- Test with screen readers (NVDA, VoiceOver)
- Use automated tools like [axe](https://www.deque.com/axe/) and [Lighthouse](https://developers.google.com/web/tools/lighthouse)

### Code Organization and Structure
Best practices for organizing React code.

```tsx
// Feature-based organization
src/
  features/
    auth/
      components/
      hooks/
      api/
      types/
    users/
      components/
      hooks/
      api/
      types/
  shared/
    components/
    hooks/
    utils/
    types/

// Component structure
// UserCard.tsx
import { UserCardProps } from './types';
import { useUser } from './hooks';
import { formatDate } from './utils';
import styles from './UserCard.module.css';

export function UserCard({ userId }: UserCardProps) {
  const { user, loading, error } = useUser(userId);
  
  if (loading) return <Loading />;
  if (error) return <Error error={error} />;
  
  return (
    <div className={styles.card}>
      <h2>{user.name}</h2>
      <p>Joined: {formatDate(user.joinDate)}</p>
    </div>
  );
}

// Types
// types.ts
export interface UserCardProps {
  userId: string;
}

export interface User {
  id: string;
  name: string;
  joinDate: string;
}

// Hooks
// hooks.ts
export function useUser(userId: string) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);
  
  useEffect(() => {
    fetchUser(userId)
      .then(setUser)
      .catch(setError)
      .finally(() => setLoading(false));
  }, [userId]);
  
  return { user, loading, error };
}
```

### Design Systems and Component Libraries

Design systems help maintain consistency and scalability in UI development. Popular component libraries include Material-UI, Chakra UI, and Ant Design.

```js
// Using Material-UI
import Button from '@mui/material/Button';
function MyButton() {
  return <Button variant="contained">Material UI Button</Button>;
}
```

**Resources:**
- [Material-UI](https://mui.com/)
- [Chakra UI](https://chakra-ui.com/)
- [Ant Design](https://ant.design/)

### Error Monitoring & Logging

Integrate tools like Sentry or LogRocket to monitor errors and user sessions in production.

```js
// Example: Sentry integration
import * as Sentry from '@sentry/react';
Sentry.init({ dsn: 'YOUR_SENTRY_DSN' });
```

**Resources:**
- [Sentry](https://sentry.io/)
- [LogRocket](https://logrocket.com/)

### DevTools & Debugging

Use React DevTools for inspecting component trees and profiling performance. Chrome DevTools and Redux DevTools are also valuable.

**Resources:**
- [React DevTools](https://react.dev/tools)
- [Redux DevTools](https://github.com/reduxjs/redux-devtools)

### Micro-frontends

Micro-frontends is an architectural style where independently deliverable frontend applications are composed into a greater whole.

- Use Module Federation (Webpack 5) or native federation (Vite) to share code between apps.
- Each micro-frontend can be developed and deployed independently.

**Resources:**
- [Micro-Frontends.org](https://micro-frontends.org/)
- [Webpack Module Federation](https://webpack.js.org/concepts/module-federation/)

### React Compiler (React Forget)

The React Compiler is an experimental build-time tool that automatically optimizes React components by inserting memoization. It aims to eliminate the need for manual `useMemo`, `useCallback`, and `React.memo` in most cases.

**Key points:**
- Analyzes your components at build time and adds memoization automatically
- Works with React 19+ and can be adopted incrementally
- Follows the "Rules of React" (pure rendering, no side effects during render)
- Reduces the cognitive overhead of performance optimization

```jsx
// Before: manual memoization
function TodoList({ todos, filter }) {
  const filteredTodos = useMemo(() => 
    todos.filter(t => t.status === filter), [todos, filter]
  );
  const handleClick = useCallback(() => { ... }, []);
  return <List items={filteredTodos} onClick={handleClick} />;
}

// After: React Compiler handles this automatically
function TodoList({ todos, filter }) {
  const filteredTodos = todos.filter(t => t.status === filter);
  const handleClick = () => { ... };
  return <List items={filteredTodos} onClick={handleClick} />;
}
```

**Resources:**
- [React Compiler Docs](https://react.dev/learn/react-compiler)

## Additional Resources

### Official React Documentation
- [React Documentation](https://react.dev/)
- [React Hooks Reference](https://react.dev/reference/react)
- [React Router Documentation](https://reactrouter.com/)

### React Community Resources
- [React GitHub Repository](https://github.com/facebook/react)
- [Reactiflux Discord](https://www.reactiflux.com/)
- [React Stack Overflow](https://stackoverflow.com/questions/tagged/reactjs)

### Recommended Books and Courses
- "Learning React" by Alex Banks and Eve Porcello
- "Fullstack React" by Anthony Accomazzo
- "React Design Patterns and Best Practices" by Carlos Santana Roldán

### Useful React Libraries
- [TanStack Query (React Query)](https://tanstack.com/query/latest)
- [React Hook Form](https://react-hook-form.com/)
- [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
- [React Router](https://reactrouter.com/)
- [Redux Toolkit](https://redux-toolkit.js.org/)
- [Zustand](https://github.com/pmndrs/zustand)
- [Zod](https://zod.dev/) (schema validation, commonly used with React forms)

### React Conferences and Events
- React Conf
- React Summit
- React Native EU
- React Advanced London

## React Native Integration

### What is React Native?
React Native is a framework for building native mobile applications using React. It allows you to use React concepts to build apps for iOS and Android with a single codebase.

### Sharing Logic Between React and React Native
You can share business logic, hooks, and state management between web and mobile apps by extracting them into shared modules.

```js
// shared/useCounter.js
import { useState } from 'react';
export function useCounter() {
  const [count, setCount] = useState(0);
  const increment = () => setCount(c => c + 1);
  return { count, increment };
}
```

**Usage in React Web:**
```js
import { useCounter } from './shared/useCounter';
function WebCounter() {
  const { count, increment } = useCounter();
  return <button onClick={increment}>Web Count: {count}</button>;
}
```

**Usage in React Native:**
```js
import { useCounter } from './shared/useCounter';
import { Button, Text, View } from 'react-native';
function NativeCounter() {
  const { count, increment } = useCounter();
  return (
    <View>
      <Text>Native Count: {count}</Text>
      <Button title="Increment" onPress={increment} />
    </View>
  );
}
```

**Resources:**
- [React Native Docs](https://reactnative.dev/)
- [React Native for Web](https://necolas.github.io/react-native-web/)

## Internationalization (i18n)

Internationalization (i18n) is the process of designing your app so it can be adapted to various languages and regions.

### Using react-i18next

```js
import { useTranslation } from 'react-i18next';

function MyComponent() {
  const { t, i18n } = useTranslation();
  return (
    <div>
      <p>{t('welcome_message')}</p>
      <button onClick={() => i18n.changeLanguage('fr')}>Français</button>
      <button onClick={() => i18n.changeLanguage('en')}>English</button>
    </div>
  );
}
```

**Resources:**
- [react-i18next](https://react.i18next.com/)
- [FormatJS](https://formatjs.io/)
- [MDN: Internationalization](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl)

## GraphQL with React

GraphQL is a query language for APIs and a runtime for executing those queries. React integrates well with GraphQL using libraries like Apollo Client and Relay.

### Using Apollo Client

```js
import { ApolloClient, InMemoryCache, ApolloProvider, useQuery, gql } from '@apollo/client';

const client = new ApolloClient({
  uri: 'https://example.com/graphql',
  cache: new InMemoryCache(),
});

const GET_USERS = gql`
  query GetUsers {
    users {
      id
      name
    }
  }
`;

function Users() {
  const { loading, error, data } = useQuery(GET_USERS);
  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error :(</p>;
  return (
    <ul>
      {data.users.map(user => <li key={user.id}>{user.name}</li>)}
    </ul>
  );
}

function App() {
  return (
    <ApolloProvider client={client}>
      <Users />
    </ApolloProvider>
  );
}
```

**Resources:**
- [Apollo Client](https://www.apollographql.com/docs/react/)
- [Relay](https://relay.dev/)
- [GraphQL.org](https://graphql.org/)

## Animation in React

React supports animation via CSS, React Transition Group, and powerful libraries like Framer Motion and React Spring.

### Using Framer Motion
```js
import { motion } from 'framer-motion';
function FadeIn() {
  return <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }}>Hello!</motion.div>;
}
```

### Using React Spring
```js
import { useSpring, animated } from 'react-spring';
function SpringComponent() {
  const props = useSpring({ opacity: 1, from: { opacity: 0 } });
  return <animated.div style={props}>Hello Spring!</animated.div>;
}
```

**Resources:**
- [Framer Motion](https://www.framer.com/motion/)
- [React Spring](https://react-spring.dev/)
- [React Transition Group](https://reactcommunity.org/react-transition-group/)

## Rendering Strategies

This is one of the most frequently asked topics in React interviews, especially for mid-to-senior roles.

### SSR vs CSR vs SSG vs ISR — What's the Difference?

| Strategy | Full Name | When HTML is Generated | Best For |
|---|---|---|---|
| **CSR** | Client-Side Rendering | In the browser at runtime | SPAs, dashboards, internal tools |
| **SSR** | Server-Side Rendering | On the server per request | Dynamic pages needing SEO (e-commerce, news) |
| **SSG** | Static Site Generation | At build time | Blog posts, docs, marketing pages |
| **ISR** | Incremental Static Regeneration | At build time + revalidated periodically | Pages that are mostly static but need occasional updates |

**CSR (Client-Side Rendering):**
```jsx
// Standard React SPA — browser downloads JS bundle, renders everything client-side
import { createRoot } from 'react-dom/client';
const root = createRoot(document.getElementById('root'));
root.render(<App />);
// Pros: Rich interactivity, fast page transitions
// Cons: Slow initial load, poor SEO (empty HTML until JS executes)
```

**SSR (Server-Side Rendering):**
```jsx
// Next.js example
export async function getServerSideProps(context) {
  const res = await fetch('https://api.example.com/products');
  const products = await res.json();
  return { props: { products } };
}

function ProductsPage({ products }) {
  return (
    <div>
      {products.map(p => <ProductCard key={p.id} product={p} />)}
    </div>
  );
}
// Pros: Good SEO, fast first contentful paint
// Cons: Server load per request, slower TTFB than SSG
```

**SSG (Static Site Generation):**
```jsx
// Next.js example — HTML generated at build time
export async function getStaticProps() {
  const posts = await fetchBlogPosts();
  return { props: { posts } };
}

export async function getStaticPaths() {
  const posts = await fetchBlogPosts();
  return {
    paths: posts.map(p => ({ params: { slug: p.slug } })),
    fallback: false,
  };
}
// Pros: Fastest load times, can be served from CDN
// Cons: Stale data until next build
```

**ISR (Incremental Static Regeneration):**
```jsx
// Next.js example — static + revalidation
export async function getStaticProps() {
  const data = await fetchData();
  return {
    props: { data },
    revalidate: 60, // Regenerate page every 60 seconds
  };
}
// Pros: CDN speed + fresh data, no full rebuild needed
// Cons: Next.js-specific, slight complexity
```

**Industry tip:** In Next.js App Router (13+), these are replaced by React Server Components with `fetch` caching options:
```jsx
// SSR equivalent
const data = await fetch(url, { cache: 'no-store' });

// SSG equivalent
const data = await fetch(url, { cache: 'force-cache' });

// ISR equivalent
const data = await fetch(url, { next: { revalidate: 60 } });
```

### What is React Hydration?

Hydration is the process where React attaches event handlers and makes server-rendered HTML interactive on the client. After SSR sends static HTML to the browser, React "hydrates" it by:

1. Downloading the JavaScript bundle
2. Reconciling the server-rendered DOM with the React component tree
3. Attaching event listeners

```jsx
// Server: renders HTML string
import { renderToString } from 'react-dom/server';
const html = renderToString(<App />);

// Client: hydrates the existing HTML instead of replacing it
import { hydrateRoot } from 'react-dom/client';
hydrateRoot(document.getElementById('root'), <App />);
```

**Common hydration errors:**
- Server and client render different content (e.g., using `Date.now()` or `window` in render)
- Missing or extra DOM nodes between server and client

**React 18 Selective Hydration:** React 18 hydrates components lazily/on-demand with `<Suspense>`, so interactive parts hydrate first:
```jsx
<Suspense fallback={<Spinner />}>
  <Comments /> {/* Hydrates independently, won't block other parts */}
</Suspense>
```

### SEO Considerations in React

SPAs (CSR) have inherent SEO challenges because search engines may not execute JavaScript. Solutions:

1. **Use SSR/SSG** (Next.js, Remix) — best approach for SEO-critical pages
2. **React Helmet / next/head** — manage `<title>`, `<meta>` tags dynamically
3. **Structured data** — JSON-LD for rich search results
4. **Sitemap and robots.txt** — ensure crawlability
5. **Open Graph tags** — for social media previews

```jsx
// Using next/head in Next.js
import Head from 'next/head';

function ProductPage({ product }) {
  return (
    <>
      <Head>
        <title>{product.name} | My Store</title>
        <meta name="description" content={product.description} />
        <meta property="og:title" content={product.name} />
        <meta property="og:image" content={product.image} />
        <script type="application/ld+json">
          {JSON.stringify({
            '@context': 'https://schema.org',
            '@type': 'Product',
            name: product.name,
            description: product.description,
          })}
        </script>
      </Head>
      <ProductDetails product={product} />
    </>
  );
}
```

### Core Web Vitals in React

Google uses Core Web Vitals as ranking signals. The three key metrics:

| Metric | What It Measures | Good Threshold |
|---|---|---|
| **LCP** (Largest Contentful Paint) | Loading performance — time for largest visible content | < 2.5s |
| **INP** (Interaction to Next Paint) | Responsiveness — delay from user input to visual update | < 200ms |
| **CLS** (Cumulative Layout Shift) | Visual stability — unexpected layout shifts | < 0.1 |

**React optimization strategies:**
```jsx
// 1. Reduce LCP — lazy load below-fold images, preload critical assets
import Image from 'next/image';
<Image src="/hero.jpg" priority /> {/* Preloads hero image for LCP */}

// 2. Improve INP — avoid blocking the main thread
import { useTransition } from 'react';
function SearchResults() {
  const [isPending, startTransition] = useTransition();
  const handleChange = (e) => {
    startTransition(() => {
      setFilter(e.target.value); // Non-urgent update, won't block input
    });
  };
}

// 3. Prevent CLS — always set dimensions on images/videos
<Image src="/photo.jpg" width={800} height={600} alt="Photo" />
// Reserve space for dynamic content
<div style={{ minHeight: '200px' }}>{isLoading ? <Skeleton /> : <Content />}</div>
```

**Measuring Core Web Vitals:**
```jsx
import { onLCP, onINP, onCLS } from 'web-vitals';
onLCP(console.log);
onINP(console.log);
onCLS(console.log);
```

## React Interview Essentials

These are frequently asked conceptual questions in React interviews at all levels.

### What are Synthetic Events in React?

React wraps the browser's native events in a cross-browser wrapper called `SyntheticEvent`. This provides a consistent API across all browsers.

```jsx
function Form() {
  const handleSubmit = (e) => {
    e.preventDefault(); // Works the same in all browsers
    console.log(e.nativeEvent); // Access the underlying native event if needed
  };

  const handleChange = (e) => {
    // e is a SyntheticEvent, not a native Event
    console.log(e.target.value);

    // In React 17+, events are NOT pooled (no need for e.persist())
    setTimeout(() => console.log(e.target.value), 100); // Works fine
  };

  return (
    <form onSubmit={handleSubmit}>
      <input onChange={handleChange} />
    </form>
  );
}
```

**Key points:**
- React 17+ attaches events to the root DOM node (not `document`), enabling multiple React roots
- Event pooling was removed in React 17 — `SyntheticEvent` objects are no longer reused
- Use `e.nativeEvent` to access the underlying browser event when needed

### What is Prop Drilling and How Do You Solve It?

Prop drilling is when you pass props through many intermediate components that don't need them, just to reach a deeply nested child.

```jsx
// ❌ Prop drilling — theme passed through 3 components unnecessarily
function App() {
  const [theme, setTheme] = useState('dark');
  return <Layout theme={theme} />;
}
function Layout({ theme }) {
  return <Sidebar theme={theme} />;
}
function Sidebar({ theme }) {
  return <NavItem theme={theme} />;
}
function NavItem({ theme }) {
  return <span className={theme}>Home</span>;
}
```

**Solutions (from simple to complex):**

1. **Component Composition** — restructure to pass components instead of data:
```jsx
function App() {
  const [theme, setTheme] = useState('dark');
  return (
    <Layout>
      <Sidebar>
        <NavItem theme={theme} />
      </Sidebar>
    </Layout>
  );
}
```

2. **Context API** — for global/shared state:
```jsx
const ThemeContext = createContext('light');

function App() {
  return (
    <ThemeContext.Provider value="dark">
      <Layout />
    </ThemeContext.Provider>
  );
}

function NavItem() {
  const theme = useContext(ThemeContext); // Direct access, no drilling
  return <span className={theme}>Home</span>;
}
```

3. **State Management Libraries** — Zustand, Redux Toolkit, Jotai for complex cases.

### What is `useImperativeHandle`?

Allows a child component to expose specific methods to a parent via `ref`. Used with `forwardRef` to customize the ref value.

```jsx
import { useRef, useImperativeHandle, forwardRef } from 'react';

const FancyInput = forwardRef((props, ref) => {
  const inputRef = useRef();

  useImperativeHandle(ref, () => ({
    focus: () => inputRef.current.focus(),
    clear: () => { inputRef.current.value = ''; },
    getValue: () => inputRef.current.value,
  }));

  return <input ref={inputRef} {...props} />;
});

// Parent component
function Form() {
  const inputRef = useRef();
  return (
    <>
      <FancyInput ref={inputRef} />
      <button onClick={() => inputRef.current.focus()}>Focus</button>
      <button onClick={() => inputRef.current.clear()}>Clear</button>
    </>
  );
}
```

**When to use:** Exposing imperative APIs (focus, scroll, play/pause) from child components. Rare but important for libraries and reusable components.

### What is `useSyncExternalStore`?

A React 18 hook for subscribing to external stores (state management outside React). It ensures consistent reads during concurrent rendering.

```jsx
import { useSyncExternalStore } from 'react';

// External store (e.g., a simple pub/sub)
const store = {
  state: { count: 0 },
  listeners: new Set(),
  subscribe(listener) {
    store.listeners.add(listener);
    return () => store.listeners.delete(listener);
  },
  getSnapshot() {
    return store.state;
  },
  increment() {
    store.state = { ...store.state, count: store.state.count + 1 };
    store.listeners.forEach(l => l());
  },
};

function Counter() {
  const { count } = useSyncExternalStore(
    store.subscribe,
    store.getSnapshot
  );
  return <button onClick={store.increment}>Count: {count}</button>;
}
```

**When to use:** Library authors building state management, subscribing to browser APIs (e.g., `navigator.onLine`, `matchMedia`), integrating non-React state.

### What is "Lifting State Up"?

A pattern where you move shared state to the nearest common parent of the components that need it. This is a core React principle.

```jsx
// ❌ Problem: Two components need to share state
function TemperatureInput({ scale }) {
  const [value, setValue] = useState(''); // Each has its own state
  return <input value={value} onChange={e => setValue(e.target.value)} />;
}

// ✅ Solution: Lift state up to the parent
function TemperatureCalculator() {
  const [celsius, setCelsius] = useState('');

  const fahrenheit = celsius ? ((parseFloat(celsius) * 9/5) + 32).toString() : '';

  return (
    <>
      <label>Celsius:</label>
      <input value={celsius} onChange={e => setCelsius(e.target.value)} />

      <label>Fahrenheit:</label>
      <input value={fahrenheit} readOnly />
    </>
  );
}
```

**Rule of thumb:** If two sibling components need the same state → lift it to their parent. If many distant components need it → consider Context or a state management library.

### What is the Difference Between Controlled and Uncontrolled Components? (In-Depth)

| Aspect | Controlled | Uncontrolled |
|---|---|---|
| Data source | React state | DOM (ref) |
| Value access | `value` prop + `onChange` | `ref.current.value` |
| Validation | Real-time (on every keystroke) | On submit |
| Performance | Re-renders on each change | Fewer re-renders |
| Use case | Most forms, complex validation | Simple forms, file inputs |

```jsx
// Controlled — React drives the input value
function ControlledForm() {
  const [email, setEmail] = useState('');
  const isValid = email.includes('@');
  return (
    <form>
      <input value={email} onChange={e => setEmail(e.target.value)} />
      {!isValid && <span>Invalid email</span>}
    </form>
  );
}

// Uncontrolled — DOM holds the value, accessed via ref
function UncontrolledForm() {
  const emailRef = useRef();
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(emailRef.current.value); // Read value on submit
  };
  return (
    <form onSubmit={handleSubmit}>
      <input ref={emailRef} defaultValue="" />
      <button type="submit">Submit</button>
    </form>
  );
}
```

**Industry recommendation:** Use controlled components for most cases. Libraries like React Hook Form use uncontrolled components internally for better performance.

### What is `React.Children` and When Do You Use It?

`React.Children` provides utilities for working with the `props.children` opaque data structure.

```jsx
import { Children, cloneElement } from 'react';

function Tabs({ children, activeIndex }) {
  return (
    <div>
      {Children.map(children, (child, index) =>
        cloneElement(child, { isActive: index === activeIndex })
      )}
    </div>
  );
}

function Tab({ isActive, children }) {
  return <div className={isActive ? 'active' : ''}>{children}</div>;
}

// Usage
<Tabs activeIndex={0}>
  <Tab>Tab 1 Content</Tab>
  <Tab>Tab 2 Content</Tab>
</Tabs>
```

**Methods:** `Children.map()`, `Children.forEach()`, `Children.count()`, `Children.only()`, `Children.toArray()`

**Modern alternative:** In newer React patterns, the **compound component pattern** with Context is generally preferred over `React.Children` manipulation.
