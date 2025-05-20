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
function Counter() {
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

### 58. How do you implement file uploads?
Using FormData and fetch:

```jsx
function FileUpload() {
  const [file, setFile] = useState(null);
  const [progress, setProgress] = useState(0);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('/upload', {
        method: 'POST',
        body: formData,
        onUploadProgress: (progressEvent) => {
          const percentCompleted = Math.round(
            (progressEvent.loaded * 100) / progressEvent.total
          );
          setProgress(percentCompleted);
        }
      });
      const data = await response.json();
      console.log('Upload successful:', data);
    } catch (error) {
      console.error('Upload failed:', error);
    }
  };

  return (
    <div>
      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />
      <button onClick={handleUpload}>Upload</button>
      {progress > 0 && <progress value={progress} max="100" />}
    </div>
  );
}
```

### 59. How do you implement pagination?
Using state and API calls:

```jsx
function PaginatedList() {
  const [items, setItems] = useState([]);
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(0);

  useEffect(() => {
    fetchItems(page).then(data => {
      setItems(data.items);
      setTotalPages(data.totalPages);
    });
  }, [page]);

  return (
    <div>
      {items.map(item => (
        <div key={item.id}>{item.name}</div>
      ))}
      <div>
        <button
          disabled={page === 1}
          onClick={() => setPage(p => p - 1)}
        >
          Previous
        </button>
        <span>Page {page} of {totalPages}</span>
        <button
          disabled={page === totalPages}
          onClick={() => setPage(p => p + 1)}
        >
          Next
        </button>
      </div>
    </div>
  );
}
```

### 60. How do you implement search with debouncing?
Using useCallback and debounce:

```jsx
function SearchComponent() {
  const [searchTerm, setSearchTerm] = useState('');
  const [results, setResults] = useState([]);

  const debouncedSearch = useCallback(
    debounce((term) => {
      searchAPI(term).then(setResults);
    }, 500),
    []
  );

  const handleSearch = (e) => {
    const value = e.target.value;
    setSearchTerm(value);
    debouncedSearch(value);
  };

  return (
    <div>
      <input
        type="text"
        value={searchTerm}
        onChange={handleSearch}
        placeholder="Search..."
      />
      <div>
        {results.map(result => (
          <div key={result.id}>{result.name}</div>
        ))}
      </div>
    </div>
  );
}
```

### 61. How do you implement a custom hook for data fetching?
Creating a reusable hook:

```jsx
function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await fetch(url);
        const json = await response.json();
        setData(json);
        setError(null);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [url]);

  return { data, loading, error };
}

// Usage
function UserProfile({ userId }) {
  const { data, loading, error } = useFetch(`/api/users/${userId}`);

  if (loading) return <Loading />;
  if (error) return <Error message={error} />;
  if (!data) return null;

  return (
    <div>
      <h1>{data.name}</h1>
      <p>{data.email}</p>
    </div>
  );
}
```

### 62. How do you implement a custom hook for local storage?
Creating a reusable hook:

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
      const valueToStore =
        value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error(error);
    }
  };

  return [storedValue, setValue];
}

// Usage
function ThemeToggle() {
  const [theme, setTheme] = useLocalStorage('theme', 'light');

  return (
    <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
      Toggle Theme
    </button>
  );
}
```

### 63. How do you implement a custom hook for window size?
Creating a reusable hook:

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

// Usage
function ResponsiveComponent() {
  const { width, height } = useWindowSize();

  return (
    <div>
      <p>Window width: {width}</p>
      <p>Window height: {height}</p>
    </div>
  );
}
```

### 64. How do you implement a custom hook for keyboard events?
Creating a reusable hook:

```jsx
function useKeyPress(targetKey) {
  const [keyPressed, setKeyPressed] = useState(false);

  useEffect(() => {
    const downHandler = ({ key }) => {
      if (key === targetKey) {
        setKeyPressed(true);
      }
    };

    const upHandler = ({ key }) => {
      if (key === targetKey) {
        setKeyPressed(false);
      }
    };

    window.addEventListener('keydown', downHandler);
    window.addEventListener('keyup', upHandler);

    return () => {
      window.removeEventListener('keydown', downHandler);
      window.removeEventListener('keyup', upHandler);
    };
  }, [targetKey]);

  return keyPressed;
}

// Usage
function KeyboardComponent() {
  const isPressed = useKeyPress('a');

  return (
    <div>
      {isPressed ? 'A key is pressed!' : 'Press A key'}
    </div>
  );
}
```

### 65. How do you implement a custom hook for mouse position?
Creating a reusable hook:

```jsx
function useMousePosition() {
  const [position, setPosition] = useState({ x: 0, y: 0 });

  useEffect(() => {
    const handleMouseMove = (event) => {
      setPosition({
        x: event.clientX,
        y: event.clientY
      });
    };

    window.addEventListener('mousemove', handleMouseMove);
    return () => window.removeEventListener('mousemove', handleMouseMove);
  }, []);

  return position;
}

// Usage
function MouseTracker() {
  const { x, y } = useMousePosition();

  return (
    <div>
      <p>Mouse X: {x}</p>
      <p>Mouse Y: {y}</p>
    </div>
  );
}
```

### 66. How do you implement a custom hook for scroll position?
```jsx
function useScrollPosition() {
  const [scrollPosition, setScrollPosition] = useState(0);

  useEffect(() => {
    const updatePosition = () => {
      setScrollPosition(window.pageYOffset);
    };

    window.addEventListener('scroll', updatePosition);
    return () => window.removeEventListener('scroll', updatePosition);
  }, []);

  return scrollPosition;
}

// Usage
function ScrollIndicator() {
  const scrollPosition = useScrollPosition();
  return <div>Scroll: {scrollPosition}px</div>;
}
```

### 67. How do you implement a custom hook for network status?
```jsx
function useNetworkStatus() {
  const [isOnline, setIsOnline] = useState(navigator.onLine);
  useEffect(() => {
    const handleOnline = () => setIsOnline(true);
    const handleOffline = () => setIsOnline(false);
    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);
    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, []);
  return isOnline;
}
// Usage
function NetworkStatus() {
  const isOnline = useNetworkStatus();
  return <div>{isOnline ? 'Online' : 'Offline'}</div>;
}
```

### 68. How do you implement a custom hook for geolocation?
```jsx
function useGeolocation() {
  const [location, setLocation] = useState({lat: null, lng: null, error: null});
  useEffect(() => {
    if (!navigator.geolocation) {
      setLocation(loc => ({...loc, error: 'Not supported'}));
      return;
    }
    navigator.geolocation.getCurrentPosition(
      pos => setLocation({lat: pos.coords.latitude, lng: pos.coords.longitude, error: null}),
      err => setLocation(loc => ({...loc, error: err.message}))
    );
  }, []);
  return location;
}
// Usage
function LocationDisplay() {
  const {lat, lng, error} = useGeolocation();
  if (error) return <div>{error}</div>;
  return <div>Lat: {lat}, Lng: {lng}</div>;
}
```

### 69. How do you implement a custom hook for clipboard operations?
```jsx
function useClipboard() {
  const [copied, setCopied] = useState(false);
  const copy = async text => {
    try {
      await navigator.clipboard.writeText(text);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {}
  };
  return {copied, copy};
}
// Usage
function CopyButton({text}) {
  const {copied, copy} = useClipboard();
  return <button onClick={() => copy(text)}>{copied ? 'Copied!' : 'Copy'}</button>;
}
```

### 70. How do you implement a custom hook for media queries?
```jsx
function useMediaQuery(query) {
  const [matches, setMatches] = useState(window.matchMedia(query).matches);
  useEffect(() => {
    const media = window.matchMedia(query);
    const listener = () => setMatches(media.matches);
    media.addEventListener('change', listener);
    return () => media.removeEventListener('change', listener);
  }, [query]);
  return matches;
}
// Usage
function Responsive() {
  const isMobile = useMediaQuery('(max-width: 600px)');
  return <div>{isMobile ? 'Mobile' : 'Desktop'}</div>;
}
```

### 71. How do you implement a custom hook for animations?
```jsx
function useAnimation(duration = 1000) {
  const [progress, setProgress] = useState(0);
  const [isAnimating, setIsAnimating] = useState(false);
  const start = useCallback(() => {
    setIsAnimating(true);
    setProgress(0);
    const startTime = performance.now();
    function animate(now) {
      const elapsed = now - startTime;
      setProgress(Math.min(elapsed / duration, 1));
      if (elapsed < duration) requestAnimationFrame(animate);
      else setIsAnimating(false);
    }
    requestAnimationFrame(animate);
  }, [duration]);
  return {progress, isAnimating, start};
}
// Usage
function AnimatedBox() {
  const {progress, isAnimating, start} = useAnimation(2000);
  return (
    <div>
      <button onClick={start} disabled={isAnimating}>Animate</button>
      <div style={{width: 100 + progress * 200, height: 50, background: 'skyblue'}} />
    </div>
  );
}
```

### 72. How do you implement a custom hook for form validation?
```jsx
function useFormValidation(value) {
  const [isValid, setIsValid] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    if (value.length < 3) {
      setIsValid(false);
      setError('Value must be at least 3 characters long');
    } else {
      setIsValid(true);
      setError('');
    }
  }, [value]);

  return {isValid, error};
}

// Usage
function Form() {
  const [username, setUsername] = useState('');
  const {isValid, error} = useFormValidation(username);

  const handleChange = (e) => {
    setUsername(e.target.value);
  };

  return (
    <div>
      <input
        type="text"
        value={username}
        onChange={handleChange}
      />
      {error && <p>{error}</p>}
    </div>
  );
}
```

### 73. How do you implement a custom hook for API polling?
```jsx
function useAPIPoll(url, interval = 5000) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await fetch(url);
        const json = await response.json();
        setData(json);
        setError(null);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();

    const timer = setInterval(fetchData, interval);
    return () => clearInterval(timer);
  }, [url, interval]);

  return {data, loading, error};
}

// Usage
function APIPollComponent() {
  const {data, loading, error} = useAPIPoll('/api/data');

  if (loading) return <Loading />;
  if (error) return <Error message={error} />;
  if (!data) return null;

  return (
    <div>
      {JSON.stringify(data)}
    </div>
  );
}
```

### 74. How do you implement a custom hook for infinite scroll?
```jsx
function useInfiniteScroll(callback) {
  const [isLoading, setIsLoading] = useState(false);
  const [hasMore, setHasMore] = useState(true);

  useEffect(() => {
    const handleScroll = async () => {
      if (isLoading || !hasMore) return;
      setIsLoading(true);
      const {scrollTop, scrollHeight, clientHeight} = document.documentElement;
      if (scrollTop + clientHeight >= scrollHeight - 100) {
        await callback();
      }
      setIsLoading(false);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, [callback, hasMore]);

  return {isLoading, hasMore};
}

// Usage
function InfiniteScrollComponent() {
  const {isLoading, hasMore} = useInfiniteScroll(async () => {
    // Fetch more items
  });

  return (
    <div>
      {isLoading ? 'Loading...' : hasMore ? 'Scroll to load more' : 'No more items'}
    </div>
  );
}
```

### 75. How do you implement a custom hook for drag and drop?
```jsx
function useDragAndDrop(accept) {
  const [isDragging, setIsDragging] = useState(false);
  const [draggedItem, setDraggedItem] = useState(null);

  const handleDragStart = (event) => {
    event.dataTransfer.setData('text', JSON.stringify(draggedItem));
    setIsDragging(true);
  };

  const handleDragOver = (event) => {
    event.preventDefault();
    event.dataTransfer.dropEffect = 'move';
  };

  const handleDrop = (event) => {
    event.preventDefault();
    const data = event.dataTransfer.getData('text');
    setDraggedItem(JSON.parse(data));
    setIsDragging(false);
  };

  return {isDragging, draggedItem, handleDragStart, handleDragOver, handleDrop};
}

// Usage
function DraggableItem({id, text}) {
  const {isDragging, handleDragStart} = useDragAndDrop('ITEM');

  return (
    <div
      draggable
      onDragStart={handleDragStart}
      style={{opacity: isDragging ? 0.5 : 1}}
    >
      {text}
    </div>
  );
}

function DroppableArea({onDrop}) {
  const {isDragging, draggedItem, handleDrop} = useDragAndDrop('ITEM');

  return (
    <div
      onDrop={handleDrop}
      onDragOver={handleDrop}
      style={{backgroundColor: isDragging ? 'lightblue' : 'white'}}
    >
      Drop here
    </div>
  );
}
```

### 76. How do you implement a custom hook for file uploads?
```jsx
function useFileUpload(url) {
  const [progress, setProgress] = useState(0);
  const [error, setError] = useState(null);

  const upload = async (file) => {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch(url, {
        method: 'POST',
        body: formData,
        onUploadProgress: (event) => {
          const percentCompleted = Math.round(
            (event.loaded * 100) / event.total
          );
          setProgress(percentCompleted);
        }
      });
      const data = await response.json();
      console.log('Upload successful:', data);
    } catch (err) {
      setError(err.message);
    }
  };

  return {progress, error, upload};
}

// Usage
function FileUploadComponent() {
  const {progress, error, upload} = useFileUpload('/api/upload');

  const handleChange = (e) => {
    const file = e.target.files[0];
    upload(file);
  };

  return (
    <div>
      <input
        type="file"
        onChange={handleChange}
      />
      {progress > 0 && <progress value={progress} max="100" />}
      {error && <p>{error}</p>}
    </div>
  );
}
```

### 77. How do you implement a custom hook for authentication?
```jsx
function useAuth() {
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

  return {user, loading, login, logout};
}

// Usage
function AuthComponent() {
  const {user, loading, login, logout} = useAuth();

  if (loading) return <Loading />;

  return (
    <div>
      {user ? (
        <button onClick={logout}>Logout</button>
      ) : (
        <button onClick={() => login({username: 'john', password: 'password'})}>Login</button>
      )}
    </div>
  );
}
```

### 78. How do you implement a custom hook for real-time updates?
```jsx
function useRealTimeUpdates(url) {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    const ws = new WebSocket(url);

    ws.onmessage = (event) => {
      const message = JSON.parse(event.data);
      setMessages(prev => [...prev, message]);
    };

    return () => {
      ws.close();
    };
  }, [url]);

  const sendMessage = (message) => {
    const ws = new WebSocket(url);
    ws.send(JSON.stringify(message));
  };

  return {messages, sendMessage};
}

// Usage
function RealTimeComponent() {
  const {messages, sendMessage} = useRealTimeUpdates('ws://your-websocket-server');

  return (
    <div>
      {messages.map(msg => (
        <div key={msg.id}>{msg.content}</div>
      ))}
      <button onClick={() => sendMessage({content: 'Hello!'})}>
        Send Message
      </button>
    </div>
  );
}
```

### 79. How do you implement a custom hook for pagination?
```jsx
function usePagination(totalItems, itemsPerPage = 10) {
  const [currentPage, setCurrentPage] = useState(1);
  const totalPages = Math.ceil(totalItems / itemsPerPage);

  const handlePageChange = (newPage) => {
    setCurrentPage(newPage);
  };

  return {currentPage, totalPages, handlePageChange};
}

// Usage
function PaginatedList() {
  const {currentPage, totalPages, handlePageChange} = usePagination(100);

  return (
    <div>
      {/* Render your list items here */}
      <div>
        <button
          disabled={currentPage === 1}
          onClick={() => handlePageChange(currentPage - 1)}
        >
          Previous
        </button>
        <span>{currentPage} of {totalPages}</span>
        <button
          disabled={currentPage === totalPages}
          onClick={() => handlePageChange(currentPage + 1)}
        >
          Next
        </button>
      </div>
    </div>
  );
}
```

### 80. How do you implement a custom hook for search?
```jsx
function useSearch(items, searchTerm) {
  const [results, setResults] = useState([]);

  useEffect(() => {
    const filteredItems = items.filter(item =>
      item.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setResults(filteredItems);
  }, [items, searchTerm]);

  return results;
}

// Usage
function SearchComponent() {
  const [searchTerm, setSearchTerm] = useState('');
  const [items, setItems] = useState([
    {id: 1, name: 'Apple'},
    {id: 2, name: 'Banana'},
    {id: 3, name: 'Cherry'},
    {id: 4, name: 'Date'},
    {id: 5, name: 'Elderberry'},
  ]);

  const results = useSearch(items, searchTerm);

  const handleSearch = (e) => {
    setSearchTerm(e.target.value);
  };

  return (
    <div>
      <input
        type="text"
        value={searchTerm}
        onChange={handleSearch}
        placeholder="Search..."
      />
      <div>
        {results.map(result => (
          <div key={result.id}>{result.name}</div>
        ))}
      </div>
    </div>
  );
}
```

### 81. How do you implement a custom hook for sorting?
```jsx
function useSort(items, sortBy) {
  const [sortedItems, setSortedItems] = useState(items);

  useEffect(() => {
    const sorted = [...items].sort((a, b) => {
      if (a[sortBy] < b[sortBy]) return -1;
      if (a[sortBy] > b[sortBy]) return 1;
      return 0;
    });
    setSortedItems(sorted);
  }, [items, sortBy]);

  return sortedItems;
}

// Usage
function SortableTable() {
  const [items, setItems] = useState([
    {id: 1, name: 'Apple', price: 1.00},
    {id: 2, name: 'Banana', price: 0.50},
    {id: 3, name: 'Cherry', price: 2.00},
  ]);
  const [sortBy, setSortBy] = useState('name');

  const sortedItems = useSort(items, sortBy);

  const handleSort = (by) => {
    setSortBy(by);
  };

  return (
    <div>
      {/* Render your table headers here */}
    </div>
  );
}
```

### 82. How do you implement a custom hook for filtering?
```jsx
function useFilter(items, filterBy) {
  const [filteredItems, setFilteredItems] = useState(items);

  useEffect(() => {
    const filtered = items.filter(item =>
      item.name.toLowerCase().includes(filterBy.toLowerCase())
    );
    setFilteredItems(filtered);
  }, [items, filterBy]);

  return filteredItems;
}

// Usage
function FilterableList() {
  const [filterBy, setFilterBy] = useState('');
  const [items, setItems] = useState([
    {id: 1, name: 'Apple'},
    {id: 2, name: 'Banana'},
    {id: 3, name: 'Cherry'},
    {id: 4, name: 'Date'},
    {id: 5, name: 'Elderberry'},
  ]);

  const filteredItems = useFilter(items, filterBy);

  const handleFilter = (e) => {
    setFilterBy(e.target.value);
  };

  return (
    <div>
      <input
        type="text"
        value={filterBy}
        onChange={handleFilter}
        placeholder="Filter..."
      />
      <div>
        {filteredItems.map(item => (
          <div key={item.id}>{item.name}</div>
        ))}
      </div>
    </div>
  );
}
```

### 83. How do you implement a custom hook for caching?
```jsx
function useCache(key, value) {
  const [cachedValue, setCachedValue] = useState(value);

  useEffect(() => {
    const cached = localStorage.getItem(key);
    if (cached) {
      setCachedValue(JSON.parse(cached));
    }
  }, [key]);

  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(cachedValue));
  }, [key, cachedValue]);

  return [cachedValue, setCachedValue];
}

// Usage
function CachedComponent() {
  const [cachedValue, setCachedValue] = useCache('cachedData', {data: 'Initial data'});

  const updateData = () => {
    setCachedValue({data: 'Updated data'});
  };

  return (
    <div>
      {cachedValue.data}
      <button onClick={updateData}>Update Data</button>
    </div>
  );
}
```

### 84. How do you implement a custom hook for error boundaries?
```jsx
function useErrorBoundary() {
  const [hasError, setHasError] = useState(false);

  useEffect(() => {
    const handleError = (event) => {
      event.preventDefault();
      setHasError(true);
    };

    window.addEventListener('error', handleError);
    window.addEventListener('unhandledrejection', handleError);

    return () => {
      window.removeEventListener('error', handleError);
      window.removeEventListener('unhandledrejection', handleError);
    };
  }, []);

  return hasError;
}

// Usage
function ErrorBoundary({children}) {
  const hasError = useErrorBoundary();

  if (hasError) {
    return <h1>Something went wrong.</h1>;
  }

  return children;
}
```

### 85. How do you implement a custom hook for loading states?
```jsx
function useLoading(asyncFunction) {
  const [isLoading, setIsLoading] = useState(false);
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setIsLoading(true);
        const result = await asyncFunction();
        setData(result);
        setError(null);
      } catch (err) {
        setError(err.message);
      } finally {
        setIsLoading(false);
      }
    };

    fetchData();
  }, [asyncFunction]);

  return {isLoading, data, error};
}

// Usage
function LoadingComponent() {
  const {isLoading, data, error} = useLoading(async () => {
    // Replace with your actual async function
  });

  if (isLoading) return <Loading />;
  if (error) return <Error message={error} />;
  if (!data) return null;

  return (
    <div>
      {/* Render your component content here */}
    </div>
  );
}
```

### 86. How do you implement a custom hook for modal dialogs?
```jsx
function useModal() {
  const [isOpen, setIsOpen] = useState(false);

  const open = () => {
    setIsOpen(true);
  };

  const close = () => {
    setIsOpen(false);
  };

  return {isOpen, open, close};
}

// Usage
function ModalComponent() {
  const {isOpen, open, close} = useModal();

  return (
    <div>
      {isOpen && (
        <div>
          {/* Modal content here */}
        </div>
      )}
      <button onClick={open}>Open Modal</button>
      <button onClick={close}>Close Modal</button>
    </div>
  );
}
```

### 87. How do you implement a custom hook for tooltips?
```jsx
function useTooltip(text) {
  const [isVisible, setIsVisible] = useState(false);

  const show = () => {
    setIsVisible(true);
  };

  const hide = () => {
    setIsVisible(false);
  };

  return {isVisible, show, hide};
}

// Usage
function TooltipComponent({text}) {
  const {isVisible, show, hide} = useTooltip(text);

  return (
    <div>
      {isVisible && (
        <div>
          {text}
        </div>
      )}
      <button onClick={show}>Show Tooltip</button>
      <button onClick={hide}>Hide Tooltip</button>
    </div>
  );
}
```

### 88. How do you implement a custom hook for dropdowns?
```jsx
function useDropdown(items) {
  const [selectedItem, setSelectedItem] = useState(null);
  const [isOpen, setIsOpen] = useState(false);

  const handleItemClick = (item) => {
    setSelectedItem(item);
    setIsOpen(false);
  };

  const toggle = () => {
    setIsOpen(!isOpen);
  };

  return {selectedItem, isOpen, handleItemClick, toggle};
}

// Usage
function DropdownComponent({items}) {
  const {selectedItem, isOpen, handleItemClick, toggle} = useDropdown(items);

  return (
    <div>
      {isOpen && (
        <div>
          {items.map(item => (
            <div key={item.id} onClick={() => handleItemClick(item)}>
              {item.name}
            </div>
          ))}
        </div>
      )}
      <button onClick={toggle}>Toggle Dropdown</button>
    </div>
  );
}
```

### 89. How do you implement a custom hook for tabs?
```jsx
function useTabs(tabs) {
  const [activeTab, setActiveTab] = useState(0);

  const handleTabClick = (index) => {
    setActiveTab(index);
  };

  return {activeTab, handleTabClick};
}

// Usage
function TabsComponent({tabs}) {
  const {activeTab, handleTabClick} = useTabs(tabs);

  return (
    <div>
      {tabs.map((tab, index) => (
        <button key={index} onClick={() => handleTabClick(index)}>
          {tab.name}
        </button>
      ))}
      {tabs[activeTab].content}
    </div>
  );
}
```

### 90. How do you implement a custom hook for accordions?
```jsx
function useAccordion(items) {
  const [activeItem, setActiveItem] = useState(null);

  const handleItemClick = (index) => {
    setActiveItem(index === activeItem ? null : index);
  };

  return {activeItem, handleItemClick};
}

// Usage
function AccordionComponent({items}) {
  const {activeItem, handleItemClick} = useAccordion(items);

  return (
    <div>
      {items.map((item, index) => (
        <div key={index}>
          <button onClick={() => handleItemClick(index)}>
            {item.name}
          </button>
          {activeItem === index && item.content}
        </div>
      ))}
    </div>
  );
}
```

### 91. How do you implement a custom hook for carousels?
```jsx
function useCarousel(items) {
  const [activeIndex, setActiveIndex] = useState(0);

  const handleNext = () => {
    setActiveIndex((activeIndex + 1) % items.length);
  };

  const handlePrev = () => {
    setActiveIndex((activeIndex - 1 + items.length) % items.length);
  };

  return {activeIndex, handleNext, handlePrev};
}

// Usage
function CarouselComponent({items}) {
  const {activeIndex, handleNext, handlePrev} = useCarousel(items);

  return (
    <div>
      {items.map((item, index) => (
        <div key={index} style={{display: index === activeIndex ? 'block' : 'none'}}>
          {item.content}
        </div>
      ))}
      <button onClick={handlePrev}>Previous</button>
      <button onClick={handleNext}>Next</button>
    </div>
  );
}
```

### 92. How do you implement a custom hook for date pickers?
```jsx
function useDatePicker(initialDate) {
  const [date, setDate] = useState(initialDate);

  const handleDateChange = (event) => {
    setDate(new Date(event.target.value));
  };

  return {date, handleDateChange};
}

// Usage
function DatePickerComponent() {
  const {date, handleDateChange} = useDatePicker(new Date());

  return (
    <div>
      <input
        type="date"
        value={date.toISOString().split('T')[0]}
        onChange={handleDateChange}
      />
    </div>
  );
}
```

### 93. How do you implement a custom hook for time pickers?
```jsx
function useTimePicker(initialTime) {
  const [time, setTime] = useState(initialTime);

  const handleTimeChange = (event) => {
    setTime(new Date(time).setHours(event.target.value));
  };

  return {time, handleTimeChange};
}

// Usage
function TimePickerComponent() {
  const {time, handleTimeChange} = useTimePicker(new Date());

  return (
    <div>
      <input
        type="time"
        value={time.toISOString().split('T')[1]}
        onChange={handleTimeChange}
      />
    </div>
  );
}
```

### 94. How do you implement a custom hook for color pickers?
```jsx
function useColorPicker(initialColor) {
  const [color, setColor] = useState(initialColor);

  const handleColorChange = (event) => {
    setColor(event.target.value);
  };

  return {color, handleColorChange};
}

// Usage
function ColorPickerComponent() {
  const {color, handleColorChange} = useColorPicker('#ff0000');

  return (
    <div>
      <input
        type="color"
        value={color}
        onChange={handleColorChange}
      />
    </div>
  );
}
```

### 95. How do you implement a custom hook for file explorers?
```jsx
function useFileExplorer(initialPath) {
  const [path, setPath] = useState(initialPath);

  const handlePathChange = (event) => {
    setPath(event.target.value);
  };

  return {path, handlePathChange};
}

// Usage
function FileExplorerComponent() {
  const {path, handlePathChange} = useFileExplorer('/');

  return (
    <div>
      {/* Render your file explorer component here */}
    </div>
  );
}
```

### 96. How do you implement a custom hook for image galleries?
```jsx
function useImageGallery(items) {
  const [activeIndex, setActiveIndex] = useState(0);

  const handleNext = () => {
    setActiveIndex((activeIndex + 1) % items.length);
  };

  const handlePrev = () => {
    setActiveIndex((activeIndex - 1 + items.length) % items.length);
  };

  return {activeIndex, handleNext, handlePrev};
}

// Usage
function ImageGalleryComponent({items}) {
  const {activeIndex, handleNext, handlePrev} = useImageGallery(items);

  return (
    <div>
      {items.map((item, index) => (
        <div key={index} style={{display: index === activeIndex ? 'block' : 'none'}}>
          {item.content}
        </div>
      ))}
      <button onClick={handlePrev}>Previous</button>
      <button onClick={handleNext}>Next</button>
    </div>
  );
}
```

### 97. How do you implement a custom hook for video players?
```jsx
function useVideoPlayer(url) {
  const [isPlaying, setIsPlaying] = useState(false);
  const [currentTime, setCurrentTime] = useState(0);
  const [duration, setDuration] = useState(0);

  const videoRef = useRef();

  useEffect(() => {
    const video = videoRef.current;
    if (video) {
      video.addEventListener('play', () => setIsPlaying(true));
      video.addEventListener('pause', () => setIsPlaying(false));
      video.addEventListener('timeupdate', () => setCurrentTime(video.currentTime));
      video.addEventListener('loadedmetadata', () => setDuration(video.duration));
    }
  }, []);

  const play = () => {
    const video = videoRef.current;
    if (video) {
      video.play();
    }
  };

  const pause = () => {
    const video = videoRef.current;
    if (video) {
      video.pause();
    }
  };

  const seek = (time) => {
    const video = videoRef.current;
    if (video) {
      video.currentTime = time;
    }
  };

  return {isPlaying, currentTime, duration, videoRef, play, pause, seek};
}

// Usage
function VideoPlayerComponent({url}) {
  const {isPlaying, currentTime, duration, videoRef, play, pause, seek} = useVideoPlayer(url);

  return (
    <div>
      {/* Render your video player component here */}
    </div>
  );
}
```

### 98. How do you implement a custom hook for audio players?
```jsx
function useAudioPlayer(url) {
  const [isPlaying, setIsPlaying] = useState(false);
  const [currentTime, setCurrentTime] = useState(0);
  const [duration, setDuration] = useState(0);

  const audioRef = useRef();

  useEffect(() => {
    const audio = audioRef.current;
    if (audio) {
      audio.addEventListener('play', () => setIsPlaying(true));
      audio.addEventListener('pause', () => setIsPlaying(false));
      audio.addEventListener('timeupdate', () => setCurrentTime(audio.currentTime));
      audio.addEventListener('loadedmetadata', () => setDuration(audio.duration));
    }
  }, []);

  const play = () => {
    const audio = audioRef.current;
    if (audio) {
      audio.play();
    }
  };

  const pause = () => {
    const audio = audioRef.current;
    if (audio) {
      audio.pause();
    }
  };

  const seek = (time) => {
    const audio = audioRef.current;
    if (audio) {
      audio.currentTime = time;
    }
  };

  return {isPlaying, currentTime, duration, audioRef, play, pause, seek};
}

// Usage
function AudioPlayerComponent({url}) {
  const {isPlaying, currentTime, duration, audioRef, play, pause, seek} = useAudioPlayer(url);

  return (
    <div>
      {/* Render your audio player component here */}
    </div>
  );
}
```

### 99. How do you implement a custom hook for charts?
```jsx
function useChart(data) {
  const [chartData, setChartData] = useState(data);

  useEffect(() => {
    // Implement chart data processing logic here
  }, [data]);

  return chartData;
}

// Usage
function ChartComponent({data}) {
  const chartData = useChart(data);

  return (
    <div>
      {/* Render your chart component here */}
    </div>
  );
}
```

### 100. How do you implement a custom hook for maps?
```jsx
function useMap(initialCenter, initialZoom) {
  const [center, setCenter] = useState(initialCenter);
  const [zoom, setZoom] = useState(initialZoom);

  const handleMapClick = (event) => {
    setCenter({
      lat: event.latlng.lat,
      lng: event.latlng.lng
    });
  };

  const handleZoomChange = (event) => {
    setZoom(event.target.getZoom());
  };

  return {center, zoom, handleMapClick, handleZoomChange};
}

// Usage
function MapComponent({initialCenter, initialZoom}) {
  const {center, zoom, handleMapClick, handleZoomChange} = useMap(initialCenter, initialZoom);

  return (
    <div>
      {/* Render your map component here */}
    </div>
  );
}
```

## Accessibility in React

Accessibility (a11y) ensures your app is usable by everyone, including people with disabilities. Use semantic HTML, ARIA attributes, and keyboard navigation. Example:

```jsx
<button aria-label="Close" onClick={onClose}>×</button>
```
- Use `<label htmlFor="id">` for form fields.
- Ensure all interactive elements are keyboard accessible.
- Use tools like [axe](https://www.deque.com/axe/) and [eslint-plugin-jsx-a11y](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y).

## TypeScript with React

TypeScript adds static typing to React, improving code quality and maintainability.

```tsx
interface Props {
  name: string;
}

const Welcome: React.FC<Props> = ({ name }) => <h1>Hello, {name}</h1>;
```
- Use `.tsx` files for components.
- Type props, state, and event handlers.
- Use `React.FC`, `React.ChangeEvent`, etc.

## Testing Best Practices (including hooks)

- Use [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/) for component tests.
- Use [@testing-library/react-hooks](https://react-hooks-testing-library.com/) for custom hooks.
- Mock API calls with [msw](https://mswjs.io/) or jest mocks.
- Test user interactions, not implementation details.

```jsx
import { renderHook, act } from '@testing-library/react-hooks';
import useCounter from './useCounter';

test('should increment counter', () => {
  const { result } = renderHook(() => useCounter());
  act(() => {
    result.current.increment();
  });
  expect(result.current.count).toBe(1);
});
```

## Common Pitfalls in React

- **Infinite loops in useEffect:** Always specify dependencies correctly.
- **Stale closures:** Use functional updates or dependencies in hooks.
- **Unnecessary re-renders:** Use React.memo, useCallback, and useMemo.
- **Direct DOM manipulation:** Avoid unless necessary; use refs.
- **Not cleaning up effects:** Always return a cleanup function in useEffect.
- **Improper key usage in lists:** Use stable, unique keys.
- **Security:** Never trust user input in `dangerouslySetInnerHTML`.

## Interview Preparation Tips

- Review React documentation and official blog.
- Practice coding: build small apps, clone UIs, or solve problems on LeetCode/CodeSandbox.
- Read and understand open-source React projects.
- Practice explaining concepts out loud.
- Mock interviews with peers or use platforms like Pramp.
- Stay updated with the latest React features.

## Expanded Best Practices

### Code Organization
- Use feature-based folder structure for scalability.
- Separate presentational and container components.
- Keep files small and focused.

### Security
- Sanitize user input, especially with `dangerouslySetInnerHTML`.
- Avoid exposing sensitive data in the frontend.
- Use HTTPS and secure cookies for authentication.

### State Management
- Lift state up only when necessary.
- Normalize state shape for complex data.
- Use Context or Redux for global state, but avoid overuse.

## React Server Components & Concurrent Features

- **React Server Components** allow you to render components on the server, reducing bundle size and improving performance. Still experimental.
- **Concurrent Features** (like `useTransition`, `Suspense` for data fetching) enable smoother user experiences by allowing React to interrupt rendering and prioritize updates.

## Clarification: Error Boundaries

> **Note:** As of now, error boundaries can only be implemented with class components. There is no hook for error boundaries yet. Use class-based error boundaries for catching errors in the component tree.

```jsx
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }
  static getDerivedStateFromError(error) {
    return { hasError: true };
  }
  componentDidCatch(error, info) {
    // Log error
  }
  render() {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return this.props.children;
  }
}
```

## Expanded Explanations for Advanced Custom Hooks (90–100)

### 90. useAccordion
**Purpose:** Manage open/close state for multiple accordion sections. Useful for FAQs, settings panels, etc.

### 91. useCarousel
**Purpose:** Manage current slide and navigation for image or content carousels. Handles next/prev logic and looping.

### 92. useDatePicker
**Purpose:** Manage selected date and handle changes. Can be integrated with calendar UIs.

### 93. useTimePicker
**Purpose:** Manage selected time and handle changes. Useful for scheduling apps.

### 94. useColorPicker
**Purpose:** Manage color selection, often used in design tools or settings.

### 95. useFileExplorer
**Purpose:** Manage navigation and selection in a file system UI. Can be extended to fetch files from APIs.

### 96. useImageGallery
**Purpose:** Manage current image and navigation in a gallery. Handles next/prev logic and looping.

### 97. useVideoPlayer
**Purpose:** Manage play/pause, seek, and time tracking for video elements. Integrate with custom controls.

### 98. useAudioPlayer
**Purpose:** Similar to useVideoPlayer, but for audio elements.

### 99. useChart
**Purpose:** Manage chart data and updates. Integrate with chart libraries like Chart.js or Recharts.

### 100. useMap
**Purpose:** Manage map center, zoom, and events. Integrate with map libraries like Leaflet or Google Maps.

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
