# ReactJS Interview Guide

## Table of Contents
1. [Core Concepts](#core-concepts)
2. [Component Lifecycle](#component-lifecycle)
3. [State Management](#state-management)
4. [Hooks](#hooks)
5. [Performance Optimization](#performance-optimization)
6. [Routing](#routing)
8. [Advanced Patterns](#advanced-patterns)

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

## React Interview Questions with Practical Examples

### 1. What is React and why use it?
React is a JavaScript library for building user interfaces. It's component-based, declarative, and efficient.

```jsx
// Example of a simple React component
function Welcome() {
  return <h1>Welcome to React!</h1>;
}
```

### 2. What are the key features of React?
- Virtual DOM
- JSX
- Component-based architecture
- One-way data flow
- React Hooks

### 3. What is JSX and how does it work?
JSX is a syntax extension for JavaScript that lets you write HTML-like code in JavaScript.

```jsx
// JSX Example
const element = (
  <div>
    <h1>Hello, {name}</h1>
    <p>Welcome to {props.website}</p>
  </div>
);

// Compiled JavaScript
const element = React.createElement(
  'div',
  null,
  React.createElement('h1', null, 'Hello, ', name),
  React.createElement('p', null, 'Welcome to ', props.website)
);
```

### 4. What is the difference between state and props?
Props are read-only and passed from parent to child, while state is managed within the component.

```jsx
// Props Example
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

// State Example
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

### 5. What are React Hooks and why use them?
Hooks are functions that let you use state and other React features in functional components.

```jsx
// useState Hook
function Counter() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}

// useEffect Hook
function DataFetcher() {
  const [data, setData] = useState(null);
  
  useEffect(() => {
    fetch('https://api.example.com/data')
      .then(response => response.json())
      .then(data => setData(data));
  }, []);

  return <div>{data ? data.title : 'Loading...'}</div>;
}
```

### 6. What is the Virtual DOM and how does it work?
The Virtual DOM is a lightweight copy of the actual DOM that React uses to improve performance.

```jsx
// Example showing Virtual DOM updates
function TodoList() {
  const [todos, setTodos] = useState([]);
  
  const addTodo = (text) => {
    setTodos([...todos, { id: Date.now(), text }]);
  };

  return (
    <div>
      {todos.map(todo => (
        <div key={todo.id}>{todo.text}</div>
      ))}
      <button onClick={() => addTodo('New Todo')}>Add Todo</button>
    </div>
  );
}
```

### 7. What are controlled and uncontrolled components?
Controlled components have their state controlled by React, while uncontrolled components maintain their own state.

```jsx
// Controlled Component
function ControlledForm() {
  const [value, setValue] = useState('');
  
  return (
    <input
      value={value}
      onChange={(e) => setValue(e.target.value)}
    />
  );
}

// Uncontrolled Component
function UncontrolledForm() {
  const inputRef = useRef();
  
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(inputRef.current.value);
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <input ref={inputRef} />
      <button type="submit">Submit</button>
    </form>
  );
}
```

### 8. What is the Context API and when to use it?
Context API provides a way to pass data through the component tree without prop drilling.

```jsx
// Context Example
const ThemeContext = React.createContext('light');

function App() {
  return (
    <ThemeContext.Provider value="dark">
      <ThemedButton />
    </ThemeContext.Provider>
  );
}

function ThemedButton() {
  const theme = useContext(ThemeContext);
  return <button className={theme}>Themed Button</button>;
}
```

### 9. What is Redux and when to use it?
Redux is a state management library for complex applications.

```jsx
// Redux Example
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

### 10. What is React Router and how to use it?
React Router is a library for handling routing in React applications.

```jsx
// React Router Example
function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/about" component={About} />
        <Route path="/users/:id" component={UserProfile} />
      </Switch>
    </Router>
  );
}

// Navigation
function Navigation() {
  return (
    <nav>
      <Link to="/">Home</Link>
      <Link to="/about">About</Link>
    </nav>
  );
}
```

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
Using react-dnd:

```jsx
import { DndProvider, useDrag, useDrop } from 'react-dnd';

function DraggableItem({ id, text }) {
  const [{ isDragging }, drag] = useDrag({
    item: { type: 'ITEM', id },
    collect: monitor => ({
      isDragging: monitor.isDragging()
    })
  });

  return (
    <div
      ref={drag}
      style={{ opacity: isDragging ? 0.5 : 1 }}
    >
      {text}
    </div>
  );
}

function DroppableArea({ onDrop }) {
  const [{ isOver }, drop] = useDrop({
    accept: 'ITEM',
    drop: item => onDrop(item.id),
    collect: monitor => ({
      isOver: monitor.isOver()
    })
  });

  return (
    <div
      ref={drop}
      style={{ backgroundColor: isOver ? 'lightblue' : 'white' }}
    >
      Drop here
    </div>
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

### 59. How do you implement a custom hook?
```jsx
// Custom hook for window size
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

// Usage
function ResponsiveComponent() {
  const { width, height } = useWindowSize();
  return <div>Window size: {width}x{height}</div>;
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
    
    const listener = () => setMatches(media.matches);
    media.addListener(listener);
    
    return () => media.removeListener(listener);
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
