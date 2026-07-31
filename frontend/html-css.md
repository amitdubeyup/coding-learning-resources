# Frontend Interview Questions & Answers

## Table of Contents
- [React.js](#reactjs)
  - [Fundamentals](#react-fundamentals)
  - [Hooks & Advanced Patterns](#react-hooks--advanced-patterns)
  - [State Management](#react-state-management)
  - [Performance & Optimization](#react-performance--optimization)
- [JavaScript & TypeScript](#javascript--typescript)
  - [Core JavaScript](#core-javascript)
  - [ES6+ Features](#es6-features)
  - [TypeScript](#typescript)
  - [Async Programming](#async-programming)
- [HTML & CSS](#html--css)
  - [HTML Fundamentals](#html-fundamentals)
  - [CSS Layout & Styling](#css-layout--styling)
  - [Responsive Design](#responsive-design)
- [Modern Frontend Ecosystem](#modern-frontend-ecosystem)
  - [Build Tools & Bundlers](#build-tools--bundlers)
  - [Testing](#testing)
  - [Performance & Optimization](#performance--optimization)
  - [Security](#security)
- [Accessibility & Internationalization](#accessibility--internationalization)
- [Team Leadership & Architecture](#team-leadership--architecture)

---

## React.js

### React Fundamentals

**Q: What is React.js and how is it different from other libraries/frameworks?**
A: React.js is a JavaScript library for building user interfaces, especially single-page applications. Key differences:
- **Component-based**: Encapsulated components that manage their own state
- **Virtual DOM**: Efficient updates through virtual representation
- **One-way data flow**: Predictable data flow from parent to child
- **Library vs Framework**: React is a library (view layer only) vs Angular (full framework)
```jsx
// React Component Example
function UserCard({ user }) {
  return (
    <div className="user-card">
      <h2>{user.name}</h2>
      <p>{user.email}</p>
    </div>
  );
}
```

**Q: What is the difference between Virtual DOM, Shadow DOM, and the real DOM?**
A: 
- **Real DOM**: Browser's actual document structure, expensive to manipulate
- **Virtual DOM**: React's lightweight JS representation, enables efficient updates
- **Shadow DOM**: Browser technology for encapsulation (Web Components)
```jsx
// Virtual DOM process:
// 1. State changes trigger virtual DOM creation
// 2. React diffs virtual DOM with previous version
// 3. Only changed elements update in real DOM
```

**Q: What are controlled and uncontrolled components?**
A: 
- **Controlled**: Form data handled by React state
- **Uncontrolled**: Form data handled by DOM itself
```jsx
// Controlled Component
function ControlledInput() {
  const [value, setValue] = useState('');
  return (
    <input 
      value={value} 
      onChange={(e) => setValue(e.target.value)} 
    />
  );
}

// Uncontrolled Component
function UncontrolledInput() {
  const inputRef = useRef();
  const handleSubmit = () => {
    console.log(inputRef.current.value);
  };
  return <input ref={inputRef} />;
}
```

**Q: What are the different types of components in React.js?**
A: 
1. **Functional Components** (preferred): Use hooks for state and lifecycle
2. **Class Components**: Use ES6 classes and lifecycle methods
```jsx
// Functional Component
function FunctionalComponent({ name }) {
  const [count, setCount] = useState(0);
  return <div>Hello {name}, Count: {count}</div>;
}

// Class Component
class ClassComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
  }
  render() {
    return <div>Hello {this.props.name}, Count: {this.state.count}</div>;
  }
}
```

### React Hooks & Advanced Patterns

**Q: What are hooks in React? List hooks you have used and explain the rules.**
A: Hooks let you use state and lifecycle features in functional components.

**Common Hooks:**
- `useState` - Local state management
- `useEffect` - Side effects and lifecycle
- `useContext` - Access context values
- `useReducer` - Complex state logic
- `useMemo` - Memoize expensive calculations
- `useCallback` - Memoize functions
- `useRef` - Mutable refs and DOM access
- `useLayoutEffect` - Synchronous effects

**Rules of Hooks:**
1. Only call hooks at the top level
2. Only call hooks from React functions
3. Use ESLint plugin to enforce rules

```jsx
// Custom Hook Example
function useCounter(initialValue = 0) {
  const [count, setCount] = useState(initialValue);
  
  const increment = useCallback(() => setCount(c => c + 1), []);
  const decrement = useCallback(() => setCount(c => c - 1), []);
  const reset = useCallback(() => setCount(initialValue), [initialValue]);
  
  return { count, increment, decrement, reset };
}

// Usage
function Counter() {
  const { count, increment, decrement, reset } = useCounter(10);
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>+</button>
      <button onClick={decrement}>-</button>
      <button onClick={reset}>Reset</button>
    </div>
  );
}
```

**Q: Explain `useEffect`, `useState`, `useMemo`, `useCallback`, and `useRef` in detail.**

**useState:**
```jsx
function UserProfile() {
  const [user, setUser] = useState({ name: '', email: '' });
  
  const updateUser = (field, value) => {
    setUser(prev => ({ ...prev, [field]: value }));
  };
  
  return (
    <form>
      <input 
        value={user.name}
        onChange={(e) => updateUser('name', e.target.value)}
        placeholder="Name"
      />
      <input 
        value={user.email}
        onChange={(e) => updateUser('email', e.target.value)}
        placeholder="Email"
      />
    </form>
  );
}
```

**useEffect:**
```jsx
function DataFetcher({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    let cancelled = false;
    
    async function fetchUser() {
      try {
        setLoading(true);
        const response = await fetch(`/api/users/${userId}`);
        const userData = await response.json();
        
        if (!cancelled) {
          setUser(userData);
        }
      } catch (error) {
        if (!cancelled) {
          console.error('Failed to fetch user:', error);
        }
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    }
    
    fetchUser();
    
    // Cleanup function
    return () => {
      cancelled = true;
    };
  }, [userId]); // Dependency array
  
  if (loading) return <div>Loading...</div>;
  if (!user) return <div>User not found</div>;
  
  return <div>Hello, {user.name}!</div>;
}
```

**useMemo & useCallback:**
```jsx
function ExpensiveComponent({ items, filter, onItemClick }) {
  // useMemo: Memoize expensive calculations
  const filteredItems = useMemo(() => {
    console.log('Filtering items...'); // Only logs when items or filter changes
    return items.filter(item => item.name.includes(filter));
  }, [items, filter]);
  
  // useCallback: Memoize functions to prevent unnecessary re-renders
  const handleItemClick = useCallback((item) => {
    onItemClick(item.id);
  }, [onItemClick]);
  
  return (
    <div>
      {filteredItems.map(item => (
        <ItemComponent 
          key={item.id} 
          item={item} 
          onClick={handleItemClick}
        />
      ))}
    </div>
  );
}

// Child component wrapped with React.memo
const ItemComponent = React.memo(({ item, onClick }) => {
  console.log('Rendering item:', item.name); // Only logs when item or onClick changes
  return (
    <div onClick={() => onClick(item)}>
      {item.name}
    </div>
  );
});
```

**useRef:**
```jsx
function FocusInput() {
  const inputRef = useRef(null);
  const renderCount = useRef(0);
  
  useEffect(() => {
    renderCount.current += 1;
  });
  
  const focusInput = () => {
    inputRef.current?.focus();
  };
  
  return (
    <div>
      <p>Render count: {renderCount.current}</p>
      <input ref={inputRef} />
      <button onClick={focusInput}>Focus Input</button>
    </div>
  );
}
```

**Q: What is the difference between useEffect and useLayoutEffect?**
A: 
- **useEffect**: Runs asynchronously after DOM paint (most common)
- **useLayoutEffect**: Runs synchronously before DOM paint (use for DOM measurements)

```jsx
function LayoutExample() {
  const [width, setWidth] = useState(0);
  const elementRef = useRef();
  
  // useLayoutEffect prevents visual flicker
  useLayoutEffect(() => {
    setWidth(elementRef.current.offsetWidth);
  }, []);
  
  return (
    <div ref={elementRef}>
      Width: {width}px
    </div>
  );
}
```

**Q: What are custom hooks and how do you create them?**
A: Custom hooks are functions that use React hooks and enable reusable stateful logic.

```jsx
// useLocalStorage custom hook
function useLocalStorage(key, initialValue) {
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error('Error reading from localStorage:', error);
      return initialValue;
    }
  });
  
  const setValue = useCallback((value) => {
    try {
      setStoredValue(value);
      window.localStorage.setItem(key, JSON.stringify(value));
    } catch (error) {
      console.error('Error writing to localStorage:', error);
    }
  }, [key]);
  
  return [storedValue, setValue];
}

// useDebounce custom hook
function useDebounce(value, delay) {
  const [debouncedValue, setDebouncedValue] = useState(value);
  
  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);
    
    return () => {
      clearTimeout(handler);
    };
  }, [value, delay]);
  
  return debouncedValue;
}

// Usage
function SearchComponent() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useLocalStorage('searchResults', []);
  const debouncedQuery = useDebounce(query, 300);
  
  useEffect(() => {
    if (debouncedQuery) {
      // Perform search
      searchAPI(debouncedQuery).then(setResults);
    }
  }, [debouncedQuery]);
  
  return (
    <div>
      <input 
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search..."
      />
      {/* Render results */}
    </div>
  );
}
```

### React State Management

**Q: What is Redux? Explain reducer, action, store, and Redux Toolkit.**
A: Redux is a predictable state container for JavaScript apps.

**Core Concepts:**
```jsx
// Action
const increment = () => ({ type: 'INCREMENT' });
const addTodo = (text) => ({ 
  type: 'ADD_TODO', 
  payload: { id: Date.now(), text, completed: false } 
});

// Reducer
function counterReducer(state = { count: 0 }, action) {
  switch (action.type) {
    case 'INCREMENT':
      return { count: state.count + 1 };
    case 'DECREMENT':
      return { count: state.count - 1 };
    default:
      return state;
  }
}

// Store
const store = createStore(counterReducer);
```

**Redux Toolkit (Modern Approach):**
```jsx
import { createSlice, configureStore } from '@reduxjs/toolkit';

// Slice
const counterSlice = createSlice({
  name: 'counter',
  initialState: { value: 0 },
  reducers: {
    increment: (state) => {
      state.value += 1; // Immer allows direct mutation
    },
    decrement: (state) => {
      state.value -= 1;
    },
    incrementByAmount: (state, action) => {
      state.value += action.payload;
    }
  }
});

export const { increment, decrement, incrementByAmount } = counterSlice.actions;

// Store
const store = configureStore({
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
      <p>{count}</p>
      <button onClick={() => dispatch(increment())}>+</button>
      <button onClick={() => dispatch(decrement())}>-</button>
    </div>
  );
}
```

**Q: What is the Context API and how does it compare to Redux?**
A: Context API provides a way to share values between components without prop drilling.

```jsx
// Context API Example
const ThemeContext = createContext();
const UserContext = createContext();

function App() {
  const [theme, setTheme] = useState('light');
  const [user, setUser] = useState(null);
  
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <UserContext.Provider value={{ user, setUser }}>
        <Header />
        <Main />
      </UserContext.Provider>
    </ThemeContext.Provider>
  );
}

// Custom hook for theme
function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within ThemeProvider');
  }
  return context;
}

// Usage
function Header() {
  const { theme, setTheme } = useTheme();
  
  return (
    <header className={`header ${theme}`}>
      <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
        Toggle Theme
      </button>
    </header>
  );
}
```

**Context API vs Redux:**
- **Context API**: Built-in, simple state sharing, good for theming/auth
- **Redux**: More powerful, time-travel debugging, middleware support, better for complex state

**Q: What are modern state management alternatives to Redux?**
A: 
1. **Zustand**: Minimal and flexible
2. **Jotai**: Atomic approach
3. **Valtio**: Proxy-based reactivity

```jsx
// Zustand Example
import { create } from 'zustand';

const useStore = create((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 })),
  decrement: () => set((state) => ({ count: state.count - 1 })),
}));

function Counter() {
  const { count, increment, decrement } = useStore();
  return (
    <div>
      <p>{count}</p>
      <button onClick={increment}>+</button>
      <button onClick={decrement}>-</button>
    </div>
  );
}

// Jotai Example
import { atom, useAtom } from 'jotai';

const countAtom = atom(0);

function Counter() {
  const [count, setCount] = useAtom(countAtom);
  return (
    <div>
      <p>{count}</p>
      <button onClick={() => setCount(c => c + 1)}>+</button>
    </div>
  );
}
```

### React Performance & Optimization

**Q: How do you optimize React app performance?**
A: Multiple strategies for optimization:

**1. Prevent Unnecessary Re-renders:**
```jsx
// React.memo for functional components
const ExpensiveComponent = React.memo(({ data, onUpdate }) => {
  return <div>{/* Complex rendering logic */}</div>;
});

// Custom comparison function
const MyComponent = React.memo(({ user, posts }) => {
  return <div>{/* Component */}</div>;
}, (prevProps, nextProps) => {
  // Return true if props are equal (skip re-render)
  return prevProps.user.id === nextProps.user.id && 
         prevProps.posts.length === nextProps.posts.length;
});
```

**2. Code Splitting & Lazy Loading:**
```jsx
import { lazy, Suspense } from 'react';

// Lazy load components
const Dashboard = lazy(() => import('./Dashboard'));
const Profile = lazy(() => import('./Profile'));

function App() {
  return (
    <Router>
      <Suspense fallback={<div>Loading...</div>}>
        <Routes>
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/profile" element={<Profile />} />
        </Routes>
      </Suspense>
    </Router>
  );
}

// Dynamic imports for other resources
const loadChartLibrary = () => import('chart.js');
```

**3. Virtualization for Large Lists:**
```jsx
import { FixedSizeList } from 'react-window';

function VirtualizedList({ items }) {
  const Row = ({ index, style }) => (
    <div style={style}>
      {items[index].name}
    </div>
  );
  
  return (
    <FixedSizeList
      height={600}
      itemCount={items.length}
      itemSize={50}
    >
      {Row}
    </FixedSizeList>
  );
}
```

**4. Optimize Heavy Computations:**
```jsx
function DataProcessor({ data, filter }) {
  // Expensive computation
  const processedData = useMemo(() => {
    return data
      .filter(item => item.category === filter)
      .map(item => ({
        ...item,
        processed: expensiveProcessing(item)
      }))
      .sort((a, b) => a.priority - b.priority);
  }, [data, filter]);
  
  return <DataVisualization data={processedData} />;
}
```

**Q: What are React DevTools and how do you use them for performance debugging?**
A: React DevTools help identify performance bottlenecks.

```jsx
// Enable Profiler in development
function App() {
  return (
    <Profiler id="App" onRender={onRenderCallback}>
      <Router>
        <Routes>
          {/* Routes */}
        </Routes>
      </Router>
    </Profiler>
  );
}

function onRenderCallback(id, phase, actualDuration, baseDuration, startTime, commitTime) {
  console.log('Component:', id);
  console.log('Phase:', phase); // "mount" or "update"
  console.log('Duration:', actualDuration);
}
```

**Performance Debugging Tips:**
1. Use Profiler tab to identify slow components
2. Look for unnecessary re-renders
3. Check component update reasons
4. Analyze bundle size with webpack-bundle-analyzer

**Q: What is React 18's Concurrent Features?**
A: React 18 introduces concurrent features for better user experience.

```jsx
// Automatic Batching
function App() {
  const [count, setCount] = useState(0);
  const [flag, setFlag] = useState(false);
  
  const handleClick = () => {
    // These updates are automatically batched
    setCount(c => c + 1);
    setFlag(f => !f);
    // Only one re-render happens
  };
  
  return <button onClick={handleClick}>Update</button>;
}

// Suspense for Data Fetching
function ProfilePage({ userId }) {
  return (
    <Suspense fallback={<ProfileSkeleton />}>
      <UserProfile userId={userId} />
      <Suspense fallback={<PostsSkeleton />}>
        <UserPosts userId={userId} />
      </Suspense>
    </Suspense>
  );
}

// useTransition for Non-urgent Updates
function SearchResults() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [isPending, startTransition] = useTransition();
  
  const handleSearch = (newQuery) => {
    setQuery(newQuery); // Urgent update
    
    startTransition(() => {
      // Non-urgent update - can be interrupted
      setResults(performExpensiveSearch(newQuery));
    });
  };
  
  return (
    <div>
      <SearchInput onChange={handleSearch} />
      {isPending ? <Spinner /> : <ResultsList results={results} />}
    </div>
  );
}
```

## Modern Frontend Ecosystem

### Build Tools & Bundlers

**Q: What is the difference between Webpack, Vite, and other modern build tools?**
A: Modern build tools have different approaches to bundling and development.

**Webpack:**
```javascript
// webpack.config.js
module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: 'babel-loader',
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html',
    }),
  ],
};
```

**Vite (Modern Alternative):**
```javascript
// vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
        },
      },
    },
  },
});
```

**Key Differences:**
- **Webpack**: Mature, extensive plugin ecosystem, slower dev server
- **Vite**: Fast dev server (ES modules), faster builds (esbuild), better DX
- **Parcel**: Zero-config, automatic optimization
- **Rollup**: Optimized for libraries, tree-shaking focused

**Q: What is TypeScript and how do you use it with React?**
A: TypeScript adds static typing to JavaScript, catching errors at compile time.

**Basic TypeScript with React:**
```typescript
// types.ts
export interface User {
  id: number;
  name: string;
  email: string;
  avatar?: string;
}

export interface UserCardProps {
  user: User;
  onEdit: (user: User) => void;
  onDelete: (id: number) => void;
}

// UserCard.tsx
import React from 'react';
import { UserCardProps } from './types';

const UserCard: React.FC<UserCardProps> = ({ user, onEdit, onDelete }) => {
  const handleEdit = () => onEdit(user);
  const handleDelete = () => onDelete(user.id);
  
  return (
    <div className="user-card">
      <img src={user.avatar || '/default-avatar.png'} alt={user.name} />
      <h3>{user.name}</h3>
      <p>{user.email}</p>
      <button onClick={handleEdit}>Edit</button>
      <button onClick={handleDelete}>Delete</button>
    </div>
  );
};

export default UserCard;
```

**Advanced TypeScript Patterns:**
```typescript
// Utility Types
type UserUpdate = Partial<Pick<User, 'name' | 'email'>>;
type UserCreate = Omit<User, 'id'>;

// Generic Components
interface ListProps<T> {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
  keyExtractor: (item: T) => string | number;
}

function List<T>({ items, renderItem, keyExtractor }: ListProps<T>) {
  return (
    <ul>
      {items.map(item => (
        <li key={keyExtractor(item)}>{renderItem(item)}</li>
      ))}
    </ul>
  );
}

// Custom Hooks with TypeScript
function useApi<T>(url: string): {
  data: T | null;
  loading: boolean;
  error: string | null;
} {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  
  useEffect(() => {
    fetch(url)
      .then(res => res.json())
      .then(setData)
      .catch(err => setError(err.message))
      .finally(() => setLoading(false));
  }, [url]);
  
  return { data, loading, error };
}

// Usage
function UserList() {
  const { data: users, loading, error } = useApi<User[]>('/api/users');
  
  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  
  return (
    <List
      items={users || []}
      renderItem={(user) => <UserCard user={user} onEdit={...} onDelete={...} />}
      keyExtractor={(user) => user.id}
    />
  );
}
```

### Testing

**Q: How do you test React components? Explain different testing strategies.**
A: Multiple testing approaches for React applications.

**Unit Testing with React Testing Library:**
```typescript
// UserCard.test.tsx
import { render, screen, fireEvent } from '@testing-library/react';
import UserCard from './UserCard';

const mockUser = {
  id: 1,
  name: 'John Doe',
  email: 'john@example.com',
};

describe('UserCard', () => {
  it('renders user information', () => {
    const onEdit = jest.fn();
    const onDelete = jest.fn();
    
    render(<UserCard user={mockUser} onEdit={onEdit} onDelete={onDelete} />);
    
    expect(screen.getByText('John Doe')).toBeInTheDocument();
    expect(screen.getByText('john@example.com')).toBeInTheDocument();
  });
  
  it('calls onEdit when edit button is clicked', () => {
    const onEdit = jest.fn();
    const onDelete = jest.fn();
    
    render(<UserCard user={mockUser} onEdit={onEdit} onDelete={onDelete} />);
    
    fireEvent.click(screen.getByText('Edit'));
    expect(onEdit).toHaveBeenCalledWith(mockUser);
  });
});
```

**Integration Testing:**
```typescript
// App.test.tsx
import { render, screen, waitFor } from '@testing-library/react';
import { rest } from 'msw';
import { setupServer } from 'msw/node';
import App from './App';

const server = setupServer(
  rest.get('/api/users', (req, res, ctx) => {
    return res(ctx.json([mockUser]));
  })
);

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

test('displays users after loading', async () => {
  render(<App />);
  
  expect(screen.getByText('Loading...')).toBeInTheDocument();
  
  await waitFor(() => {
    expect(screen.getByText('John Doe')).toBeInTheDocument();
  });
});
```

**E2E Testing with Cypress:**
```typescript
// cypress/e2e/user-management.cy.ts
describe('User Management', () => {
  beforeEach(() => {
    cy.visit('/users');
    cy.intercept('GET', '/api/users', { fixture: 'users.json' });
  });
  
  it('should display users and allow editing', () => {
    cy.get('[data-testid="user-card"]').should('have.length', 3);
    
    cy.get('[data-testid="edit-user-1"]').click();
    cy.get('[data-testid="name-input"]').clear().type('Jane Doe');
    cy.get('[data-testid="save-button"]').click();
    
    cy.get('[data-testid="user-card"]').first().should('contain', 'Jane Doe');
  });
});
```

**Custom Testing Utilities:**
```typescript
// test-utils.tsx
import { render, RenderOptions } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import { ThemeProvider } from 'styled-components';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

const AllTheProviders: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const queryClient = new QueryClient({
    defaultOptions: { queries: { retry: false } },
  });
  
  return (
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <ThemeProvider theme={mockTheme}>
          {children}
        </ThemeProvider>
      </BrowserRouter>
    </QueryClientProvider>
  );
};

const customRender = (
  ui: React.ReactElement,
  options?: Omit<RenderOptions, 'wrapper'>,
) => render(ui, { wrapper: AllTheProviders, ...options });

export * from '@testing-library/react';
export { customRender as render };
```

### Performance & Optimization

**Q: What are Core Web Vitals and how do you optimize them?**
A: Core Web Vitals are Google's metrics for user experience.

**1. Largest Contentful Paint (LCP) - Loading Performance:**
```typescript
// Image optimization
function OptimizedImage({ src, alt, ...props }) {
  return (
    <picture>
      <source srcSet={`${src}.webp`} type="image/webp" />
      <source srcSet={`${src}.avif`} type="image/avif" />
      <img 
        src={src} 
        alt={alt} 
        loading="lazy"
        decoding="async"
        {...props}
      />
    </picture>
  );
}

// Resource preloading
function App() {
  useEffect(() => {
    // Preload critical resources
    const link = document.createElement('link');
    link.rel = 'preload';
    link.href = '/critical-font.woff2';
    link.as = 'font';
    link.type = 'font/woff2';
    link.crossOrigin = 'anonymous';
    document.head.appendChild(link);
  }, []);
  
  return <div>{/* App content */}</div>;
}
```

**2. First Input Delay (FID) - Interactivity:**
```typescript
// Use React.memo to prevent unnecessary re-renders
const HeavyComponent = React.memo(({ data }) => {
  const processedData = useMemo(() => {
    return heavyDataProcessing(data);
  }, [data]);
  
  return <div>{/* Render processed data */}</div>;
});

// Code splitting for better interaction timing
const LazyDashboard = lazy(() => 
  import('./Dashboard').then(module => ({
    default: module.Dashboard
  }))
);
```

**3. Cumulative Layout Shift (CLS) - Visual Stability:**
```typescript
// Reserve space for dynamic content
function ImageWithPlaceholder({ src, alt, width, height }) {
  const [loaded, setLoaded] = useState(false);
  
  return (
    <div 
      style={{ 
        width, 
        height, 
        backgroundColor: loaded ? 'transparent' : '#f0f0f0',
        position: 'relative'
      }}
    >
      <img
        src={src}
        alt={alt}
        style={{
          width: '100%',
          height: '100%',
          opacity: loaded ? 1 : 0,
          transition: 'opacity 0.3s'
        }}
        onLoad={() => setLoaded(true)}
      />
    </div>
  );
}
```

**Performance Monitoring:**
```typescript
// Web Vitals measurement
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals';

function sendToAnalytics(metric) {
  // Send to your analytics service
  analytics.track('Web Vital', {
    name: metric.name,
    value: metric.value,
    id: metric.id,
  });
}

getCLS(sendToAnalytics);
getFID(sendToAnalytics);
getFCP(sendToAnalytics);
getLCP(sendToAnalytics);
getTTFB(sendToAnalytics);
```

### Security

**Q: What are common frontend security vulnerabilities and how do you prevent them?**
A: Multiple security concerns in frontend development.

**1. Cross-Site Scripting (XSS):**
```typescript
// BAD - Vulnerable to XSS
function UserComment({ comment }) {
  return <div dangerouslySetInnerHTML={{ __html: comment }} />;
}

// GOOD - Safe rendering
function UserComment({ comment }) {
  return <div>{comment}</div>; // React automatically escapes
}

// For rich text, use a sanitization library
import DOMPurify from 'dompurify';

function RichTextComment({ html }) {
  const sanitizedHTML = DOMPurify.sanitize(html);
  return <div dangerouslySetInnerHTML={{ __html: sanitizedHTML }} />;
}
```

**2. Content Security Policy (CSP):**
```html
<!-- Add to HTML head -->
<meta http-equiv="Content-Security-Policy" 
      content="default-src 'self'; 
               script-src 'self' 'unsafe-inline' https://trusted-cdn.com;
               style-src 'self' 'unsafe-inline';
               img-src 'self' data: https:;">
```

**3. Secure API Communication:**
```typescript
// Environment-based API configuration
const API_BASE_URL = process.env.NODE_ENV === 'production' 
  ? 'https://api.yourapp.com'
  : 'http://localhost:3001';

// Secure token handling
class AuthService {
  private static TOKEN_KEY = 'auth_token';
  
  static setToken(token: string) {
    // Use httpOnly cookies in production
    if (process.env.NODE_ENV === 'production') {
      // Set via secure API call
      this.setHttpOnlyCookie(token);
    } else {
      localStorage.setItem(this.TOKEN_KEY, token);
    }
  }
  
  static getToken(): string | null {
    return localStorage.getItem(this.TOKEN_KEY);
  }
  
  static removeToken() {
    localStorage.removeItem(this.TOKEN_KEY);
  }
}

// Secure API client
const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
});

apiClient.interceptors.request.use((config) => {
  const token = AuthService.getToken();
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});
```

**4. Input Validation & Sanitization:**
```typescript
import { z } from 'zod';

// Schema validation
const UserSchema = z.object({
  name: z.string().min(1).max(100),
  email: z.string().email(),
  age: z.number().min(0).max(120),
});

function UserForm() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    age: 0,
  });
  const [errors, setErrors] = useState({});
  
  const handleSubmit = (e) => {
    e.preventDefault();
    
    try {
      const validatedData = UserSchema.parse(formData);
      // Submit validated data
      submitUser(validatedData);
    } catch (error) {
      if (error instanceof z.ZodError) {
        setErrors(error.flatten().fieldErrors);
      }
    }
  };
  
  return (
    <form onSubmit={handleSubmit}>
      {/* Form fields with validation */}
    </form>
  );
}
```

**Q: How do you implement authentication and authorization in React?**
A: Secure authentication patterns for React applications.

```typescript
// Auth Context
interface AuthContextType {
  user: User | null;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
  loading: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    // Check for existing session
    const token = AuthService.getToken();
    if (token) {
      verifyToken(token)
        .then(setUser)
        .catch(() => AuthService.removeToken())
        .finally(() => setLoading(false));
    } else {
      setLoading(false);
    }
  }, []);
  
  const login = async (email: string, password: string) => {
    const { user, token } = await authAPI.login(email, password);
    AuthService.setToken(token);
    setUser(user);
  };
  
  const logout = () => {
    AuthService.removeToken();
    setUser(null);
  };
  
  return (
    <AuthContext.Provider value={{ user, login, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
}

// Protected Route Component
function ProtectedRoute({ children, requiredRole }: {
  children: React.ReactNode;
  requiredRole?: string;
}) {
  const { user, loading } = useAuth();
  
  if (loading) return <LoadingSpinner />;
  
  if (!user) return <Navigate to="/login" replace />;
  
  if (requiredRole && !user.roles.includes(requiredRole)) {
    return <Navigate to="/unauthorized" replace />;
  }
  
  return <>{children}</>;
}

// Usage
function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route path="/dashboard" element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          } />
          <Route path="/admin" element={
            <ProtectedRoute requiredRole="admin">
              <AdminPanel />
            </ProtectedRoute>
          } />
        </Routes>
      </Router>
    </AuthProvider>
  );
}
```

## Accessibility & Internationalization

**Q: What are accessibility (a11y) best practices in frontend development?**
A: Accessibility ensures your application is usable by everyone, including people with disabilities. Best practices include:

**1. Semantic HTML:**
```html
<!-- Good: Semantic structure -->
<header>
  <nav aria-label="Main navigation">
    <ul>
      <li><a href="/home">Home</a></li>
      <li><a href="/about">About</a></li>
    </ul>
  </nav>
</header>

<main>
  <section aria-labelledby="news-heading">
    <h1 id="news-heading">Latest News</h1>
    <article>
      <h2>Article Title</h2>
      <p>Article content...</p>
    </article>
  </section>
</main>

<!-- Bad: Non-semantic -->
<div class="header">
  <div class="nav">
    <div class="nav-item">Home</div>
  </div>
</div>
```

**2. ARIA Attributes and Focus Management:**
```jsx
function AccessibleModal({ isOpen, onClose, title, children }) {
  const modalRef = useRef(null);
  const previousFocusRef = useRef(null);
  
  useEffect(() => {
    if (isOpen) {
      previousFocusRef.current = document.activeElement;
      modalRef.current?.focus();
    } else {
      previousFocusRef.current?.focus();
    }
  }, [isOpen]);
  
  const handleKeyDown = (e) => {
    if (e.key === 'Escape') {
      onClose();
    }
  };
  
  if (!isOpen) return null;
  
  return (
    <div 
      className="modal-overlay"
      onClick={onClose}
      role="dialog"
      aria-modal="true"
      aria-labelledby="modal-title"
    >
      <div 
        ref={modalRef}
        className="modal-content"
        tabIndex={-1}
        onKeyDown={handleKeyDown}
        onClick={(e) => e.stopPropagation()}
      >
        <h2 id="modal-title">{title}</h2>
        <button 
          onClick={onClose}
          aria-label="Close modal"
          className="close-button"
        >
          ×
        </button>
        {children}
      </div>
    </div>
  );
}
```

**3. Form Accessibility:**
```jsx
function AccessibleForm() {
  const [errors, setErrors] = useState({});
  
  return (
    <form aria-labelledby="form-title">
      <h2 id="form-title">Contact Form</h2>
      
      <div className="field-group">
        <label htmlFor="name">
          Name <span aria-label="required">*</span>
        </label>
        <input
          id="name"
          type="text"
          required
          aria-describedby={errors.name ? "name-error" : undefined}
          aria-invalid={!!errors.name}
        />
        {errors.name && (
          <div id="name-error" role="alert" className="error">
            {errors.name}
          </div>
        )}
      </div>
      
      <fieldset>
        <legend>Preferred Contact Method</legend>
        <label>
          <input type="radio" name="contact" value="email" />
          Email
        </label>
        <label>
          <input type="radio" name="contact" value="phone" />
          Phone
        </label>
      </fieldset>
    </form>
  );
}
```

**Q: How do you implement internationalization (i18n) in React applications?**
A: i18n enables your app to support multiple languages and locales.

```jsx
// i18n setup with react-i18next
import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import Backend from 'i18next-http-backend';
import LanguageDetector from 'i18next-browser-languagedetector';

i18n
  .use(Backend)
  .use(LanguageDetector)
  .use(initReactI18next)
  .init({
    fallbackLng: 'en',
    interpolation: {
      escapeValue: false,
    },
    backend: {
      loadPath: '/locales/{{lng}}/{{ns}}.json',
    },
  });

// Translation files
// /public/locales/en/translation.json
{
  "welcome": "Welcome, {{name}}!",
  "navigation": {
    "home": "Home",
    "about": "About",
    "contact": "Contact"
  },
  "validation": {
    "required": "This field is required",
    "email": "Please enter a valid email"
  }
}

// /public/locales/es/translation.json
{
  "welcome": "¡Bienvenido, {{name}}!",
  "navigation": {
    "home": "Inicio",
    "about": "Acerca de",
    "contact": "Contacto"
  }
}

// React components with i18n
import { useTranslation } from 'react-i18next';

function Navigation() {
  const { t } = useTranslation();
  
  return (
    <nav>
      <a href="/">{t('navigation.home')}</a>
      <a href="/about">{t('navigation.about')}</a>
      <a href="/contact">{t('navigation.contact')}</a>
    </nav>
  );
}

function WelcomeMessage({ userName }) {
  const { t } = useTranslation();
  
  return (
    <h1>{t('welcome', { name: userName })}</h1>
  );
}

// Language switcher
function LanguageSwitcher() {
  const { i18n } = useTranslation();
  
  const changeLanguage = (lng) => {
    i18n.changeLanguage(lng);
  };
  
  return (
    <div>
      <button onClick={() => changeLanguage('en')}>English</button>
      <button onClick={() => changeLanguage('es')}>Español</button>
      <button onClick={() => changeLanguage('fr')}>Français</button>
    </div>
  );
}
```

**Advanced i18n Features:**
```jsx
// Date and number formatting
import { format } from 'date-fns';
import { enUS, es, fr } from 'date-fns/locale';

const locales = { en: enUS, es, fr };

function LocalizedDate({ date }) {
  const { i18n } = useTranslation();
  const locale = locales[i18n.language] || locales.en;
  
  return (
    <time dateTime={date.toISOString()}>
      {format(date, 'PPP', { locale })}
    </time>
  );
}

// Currency formatting
function Price({ amount, currency = 'USD' }) {
  const { i18n } = useTranslation();
  
  const formatter = new Intl.NumberFormat(i18n.language, {
    style: 'currency',
    currency,
  });
  
  return <span>{formatter.format(amount)}</span>;
}

// Pluralization
function ItemCount({ count }) {
  const { t } = useTranslation();
  
  return (
    <p>
      {t('items', { count })} {/* Uses pluralization rules */}
    </p>
  );
}

// Translation file with plurals
{
  "items_zero": "No items",
  "items_one": "{{count}} item",
  "items_other": "{{count}} items"
}
```

## JavaScript & TypeScript

### Core JavaScript

**Q: What is the difference between `let`, `const`, and `var`? Explain hoisting and scope.**
A: These keywords have different scoping rules and behaviors.

```javascript
// var: function-scoped, hoisted, can be redeclared
function varExample() {
  console.log(x); // undefined (hoisted but not initialized)
  
  if (true) {
    var x = 1;
    var x = 2; // No error, redeclaration allowed
  }
  
  console.log(x); // 2 (accessible outside block)
}

// let: block-scoped, temporal dead zone, cannot be redeclared
function letExample() {
  // console.log(y); // ReferenceError: Cannot access before initialization
  
  if (true) {
    let y = 1;
    // let y = 2; // SyntaxError: Identifier 'y' has already been declared
    y = 3; // OK, reassignment allowed
  }
  
  // console.log(y); // ReferenceError: y is not defined
}

// const: block-scoped, must be initialized, cannot be reassigned
function constExample() {
  // const z; // SyntaxError: Missing initializer
  const z = { name: 'John' };
  
  // z = {}; // TypeError: Assignment to constant variable
  z.name = 'Jane'; // OK, object mutation allowed
  
  const arr = [1, 2, 3];
  arr.push(4); // OK, array mutation allowed
  // arr = []; // TypeError: Assignment to constant variable
}
```

**Q: Explain closures with practical examples.**
A: Closures occur when a function retains access to its outer scope even after the outer function returns.

```javascript
// Basic closure
function createCounter() {
  let count = 0;
  
  return function() {
    return ++count;
  };
}

const counter1 = createCounter();
const counter2 = createCounter();

console.log(counter1()); // 1
console.log(counter1()); // 2
console.log(counter2()); // 1 (separate closure)

// Module pattern with closures
const userModule = (function() {
  let users = [];
  let currentId = 1;
  
  return {
    addUser(name, email) {
      const user = {
        id: currentId++,
        name,
        email,
        createdAt: new Date()
      };
      users.push(user);
      return user;
    },
    
    getUser(id) {
      return users.find(user => user.id === id);
    },
    
    getAllUsers() {
      return [...users]; // Return copy to prevent mutation
    },
    
    updateUser(id, updates) {
      const userIndex = users.findIndex(user => user.id === id);
      if (userIndex !== -1) {
        users[userIndex] = { ...users[userIndex], ...updates };
        return users[userIndex];
      }
      return null;
    }
  };
})();

// Event handlers with closures
function setupEventHandlers() {
  const buttons = document.querySelectorAll('.btn');
  
  for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click', function() {
      console.log(`Button ${i} clicked`); // 'i' is captured by closure
    });
  }
}
```

**Q: What is the Event Loop? Explain with examples.**
A: The Event Loop manages asynchronous operations in JavaScript's single-threaded environment.

```javascript
// Event Loop visualization
console.log('1'); // Synchronous - Call Stack

setTimeout(() => {
  console.log('2'); // Macro task - Task Queue
}, 0);

Promise.resolve().then(() => {
  console.log('3'); // Micro task - Microtask Queue
});

console.log('4'); // Synchronous - Call Stack

// Output: 1, 4, 3, 2
// Explanation:
// 1. Synchronous code executes first (1, 4)
// 2. Microtasks have priority over macrotasks (3)
// 3. Macrotasks execute last (2)

// Complex example
function eventLoopExample() {
  console.log('Start');
  
  setTimeout(() => console.log('Timeout 1'), 0);
  
  Promise.resolve()
    .then(() => console.log('Promise 1'))
    .then(() => console.log('Promise 2'));
  
  setTimeout(() => console.log('Timeout 2'), 0);
  
  Promise.resolve()
    .then(() => {
      console.log('Promise 3');
      return Promise.resolve();
    })
    .then(() => console.log('Promise 4'));
  
  console.log('End');
}

// Output: Start, End, Promise 1, Promise 3, Promise 2, Promise 4, Timeout 1, Timeout 2
```

### ES6+ Features

**Q: Explain destructuring, spread/rest operators, and template literals with examples.**
A: ES6+ introduces powerful syntax features for cleaner code.

```javascript
// Destructuring
const user = {
  id: 1,
  name: 'John Doe',
  email: 'john@example.com',
  address: {
    street: '123 Main St',
    city: 'New York'
  }
};

// Object destructuring
const { name, email } = user;
const { name: userName, email: userEmail } = user; // Rename
const { address: { city } } = user; // Nested destructuring
const { phone = 'Not provided' } = user; // Default value

// Array destructuring
const numbers = [1, 2, 3, 4, 5];
const [first, second, ...rest] = numbers;
const [, , third] = numbers; // Skip elements

// Function parameter destructuring
function createUser({ name, email, age = 18 }) {
  return {
    id: Math.random(),
    name,
    email,
    age,
    createdAt: new Date()
  };
}

// Spread operator
const originalArray = [1, 2, 3];
const newArray = [...originalArray, 4, 5]; // [1, 2, 3, 4, 5]

const originalObject = { a: 1, b: 2 };
const newObject = { ...originalObject, c: 3 }; // { a: 1, b: 2, c: 3 }

// Combining arrays
const arr1 = [1, 2];
const arr2 = [3, 4];
const combined = [...arr1, ...arr2]; // [1, 2, 3, 4]

// Rest parameters
function sum(...numbers) {
  return numbers.reduce((total, num) => total + num, 0);
}

sum(1, 2, 3, 4); // 10

// Template literals
const template = `
  <div class="user-card">
    <h2>${user.name}</h2>
    <p>Email: ${user.email}</p>
    <p>Joined: ${new Date().getFullYear()}</p>
  </div>
`;

// Tagged template literals
function highlight(strings, ...values) {
  return strings.reduce((result, string, i) => {
    const value = values[i] ? `<mark>${values[i]}</mark>` : '';
    return result + string + value;
  }, '');
}

const highlighted = highlight`Hello ${name}, you have ${5} messages`;
```

### Async Programming

**Q: Explain Promises, async/await, and error handling patterns.**
A: Modern JavaScript provides multiple ways to handle asynchronous operations.

```javascript
// Promise creation and chaining
function fetchUser(id) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (id > 0) {
        resolve({ id, name: `User ${id}`, email: `user${id}@example.com` });
      } else {
        reject(new Error('Invalid user ID'));
      }
    }, 1000);
  });
}

// Promise chaining
fetchUser(1)
  .then(user => {
    console.log('User:', user);
    return fetch(`/api/users/${user.id}/posts`);
  })
  .then(response => response.json())
  .then(posts => {
    console.log('Posts:', posts);
  })
  .catch(error => {
    console.error('Error:', error);
  })
  .finally(() => {
    console.log('Cleanup');
  });

// async/await
async function getUserData(id) {
  try {
    const user = await fetchUser(id);
    const postsResponse = await fetch(`/api/users/${user.id}/posts`);
    const posts = await postsResponse.json();
    
    return {
      user,
      posts,
      totalPosts: posts.length
    };
  } catch (error) {
    console.error('Failed to fetch user data:', error);
    throw error; // Re-throw if needed
  } finally {
    console.log('Request completed');
  }
}

// Concurrent operations
async function fetchMultipleUsers(ids) {
  try {
    // Parallel execution
    const userPromises = ids.map(id => fetchUser(id));
    const users = await Promise.all(userPromises);
    
    return users;
  } catch (error) {
    console.error('One or more requests failed:', error);
    return [];
  }
}

// Advanced Promise patterns
async function fetchWithRetry(url, maxRetries = 3) {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }
      return await response.json();
    } catch (error) {
      console.log(`Attempt ${attempt} failed:`, error.message);
      
      if (attempt === maxRetries) {
        throw error;
      }
      
      // Exponential backoff
      await new Promise(resolve => 
        setTimeout(resolve, Math.pow(2, attempt) * 1000)
      );
    }
  }
}

// Promise.allSettled for handling mixed results
async function fetchAllUserData(ids) {
  const promises = ids.map(async (id) => {
    const user = await fetchUser(id);
    const posts = await fetch(`/api/users/${id}/posts`).then(r => r.json());
    return { user, posts };
  });
  
  const results = await Promise.allSettled(promises);
  
  const successful = results
    .filter(result => result.status === 'fulfilled')
    .map(result => result.value);
    
  const failed = results
    .filter(result => result.status === 'rejected')
    .map(result => result.reason);
  
  return { successful, failed };
}
```

### TypeScript

**Q: What are TypeScript's advanced type features? Explain generics, utility types, and type guards.**
A: TypeScript provides powerful type system features for better code quality.

```typescript
// Generics
interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
}

interface User {
  id: number;
  name: string;
  email: string;
}

interface Post {
  id: number;
  title: string;
  content: string;
  authorId: number;
}

// Generic functions
async function fetchData<T>(url: string): Promise<ApiResponse<T>> {
  const response = await fetch(url);
  return response.json();
}

// Usage with type inference
const userResponse = await fetchData<User[]>('/api/users');
const postResponse = await fetchData<Post[]>('/api/posts');

// Generic constraints
interface Identifiable {
  id: number;
}

function updateEntity<T extends Identifiable>(
  entity: T, 
  updates: Partial<Omit<T, 'id'>>
): T {
  return { ...entity, ...updates };
}

// Utility Types
type UserCreate = Omit<User, 'id'>; // { name: string; email: string; }
type UserUpdate = Partial<Pick<User, 'name' | 'email'>>; // { name?: string; email?: string; }
type UserKeys = keyof User; // 'id' | 'name' | 'email'

// Advanced utility types
type NonNullable<T> = T extends null | undefined ? never : T;
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : any;

// Custom utility types
type DeepReadonly<T> = {
  readonly [P in keyof T]: T[P] extends object ? DeepReadonly<T[P]> : T[P];
};

type Optional<T, K extends keyof T> = Omit<T, K> & Partial<Pick<T, K>>;

// Type guards
function isUser(obj: any): obj is User {
  return obj && 
         typeof obj.id === 'number' && 
         typeof obj.name === 'string' && 
         typeof obj.email === 'string';
}

function isString(value: unknown): value is string {
  return typeof value === 'string';
}

// Discriminated unions
interface LoadingState {
  status: 'loading';
}

interface SuccessState {
  status: 'success';
  data: any;
}

interface ErrorState {
  status: 'error';
  error: string;
}

type AsyncState = LoadingState | SuccessState | ErrorState;

function handleState(state: AsyncState) {
  switch (state.status) {
    case 'loading':
      return <Spinner />;
    case 'success':
      return <div>{state.data}</div>; // TypeScript knows 'data' exists
    case 'error':
      return <div>Error: {state.error}</div>; // TypeScript knows 'error' exists
  }
}

// Conditional types
type ApiResult<T> = T extends string 
  ? { message: T } 
  : T extends number 
    ? { count: T } 
    : { data: T };

// Mapped types
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};

type UserGetters = Getters<User>;
// { getId: () => number; getName: () => string; getEmail: () => string; }
```

## HTML & CSS

### HTML Fundamentals

**Q: What are semantic HTML elements and why are they important?**
A: Semantic HTML provides meaning to web content, improving accessibility and SEO.

```html
<!-- Semantic HTML structure -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Blog Post - My Website</title>
  <meta name="description" content="A comprehensive guide to semantic HTML">
</head>
<body>
  <header>
    <nav aria-label="Main navigation">
      <ul>
        <li><a href="/" aria-current="page">Home</a></li>
        <li><a href="/blog">Blog</a></li>
        <li><a href="/about">About</a></li>
      </ul>
    </nav>
  </header>
  
  <main>
    <article>
      <header>
        <h1>Understanding Semantic HTML</h1>
        <p>
          Published on <time datetime="2023-12-01">December 1, 2023</time>
          by <address>John Doe</address>
        </p>
      </header>
      
      <section>
        <h2>Introduction</h2>
        <p>Semantic HTML elements clearly describe their meaning...</p>
      </section>
      
      <section>
        <h2>Benefits</h2>
        <ul>
          <li>Better accessibility</li>
          <li>Improved SEO</li>
          <li>Cleaner code structure</li>
        </ul>
      </section>
      
      <aside>
        <h3>Related Articles</h3>
        <ul>
          <li><a href="/accessibility-guide">Accessibility Guide</a></li>
          <li><a href="/seo-tips">SEO Best Practices</a></li>
        </ul>
      </aside>
    </article>
  </main>
  
  <footer>
    <p>&copy; 2023 My Website. All rights reserved.</p>
  </footer>
</body>
</html>
```

**Benefits of Semantic HTML:**
1. **Accessibility**: Screen readers understand content structure
2. **SEO**: Search engines better understand content hierarchy
3. **Maintainability**: Code is self-documenting
4. **Styling**: CSS can target semantic elements directly

### CSS Layout & Styling

**Q: Explain Flexbox and CSS Grid. When would you use each?**
A: Flexbox and Grid are powerful layout systems with different strengths.

```css
/* Flexbox - 1D layouts */
.flex-container {
  display: flex;
  flex-direction: row; /* or column */
  justify-content: space-between; /* main axis */
  align-items: center; /* cross axis */
  gap: 1rem;
  flex-wrap: wrap;
}

.flex-item {
  flex: 1; /* grow equally */
  /* flex: 0 0 200px; grow shrink basis */
}

/* Common Flexbox patterns */
.navigation {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.card-layout {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.card {
  flex: 1 1 300px; /* responsive cards */
}

.centered {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

/* CSS Grid - 2D layouts */
.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  grid-template-rows: auto 1fr auto;
  grid-template-areas:
    "header header header"
    "sidebar main aside"
    "footer footer footer";
  gap: 1rem;
  min-height: 100vh;
}

.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main { grid-area: main; }
.aside { grid-area: aside; }
.footer { grid-area: footer; }

/* Advanced Grid patterns */
.photo-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  grid-auto-rows: 200px;
  gap: 1rem;
}

.photo-gallery .featured {
  grid-column: span 2;
  grid-row: span 2;
}

/* Responsive grid */
.responsive-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr));
  gap: 1rem;
}
```

**When to use Flexbox vs Grid:**
- **Flexbox**: Navigation bars, card layouts, centering, 1D arrangements
- **Grid**: Page layouts, complex 2D arrangements, overlapping content

### Responsive Design

**Q: How do you implement responsive design? Explain mobile-first approach.**
A: Responsive design ensures your site works on all device sizes.

```css
/* Mobile-first approach */
/* Base styles (mobile) */
.container {
  padding: 1rem;
  max-width: 100%;
}

.navigation {
  flex-direction: column;
}

.grid {
  grid-template-columns: 1fr;
}

/* Tablet and up */
@media (min-width: 768px) {
  .container {
    padding: 2rem;
    max-width: 750px;
    margin: 0 auto;
  }
  
  .navigation {
    flex-direction: row;
  }
  
  .grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Desktop and up */
@media (min-width: 1024px) {
  .container {
    max-width: 1200px;
  }
  
  .grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

/* Large desktop */
@media (min-width: 1440px) {
  .container {
    max-width: 1400px;
  }
  
  .grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

/* Common responsive patterns */
.responsive-text {
  font-size: clamp(1rem, 2.5vw, 2rem);
}

.responsive-spacing {
  padding: clamp(1rem, 5vw, 3rem);
}

.responsive-image {
  width: 100%;
  height: auto;
  object-fit: cover;
}

/* Container queries (modern browsers) */
@container (min-width: 400px) {
  .card {
    display: flex;
    gap: 1rem;
  }
}

/* Responsive utilities */
.hide-mobile {
  display: none;
}

@media (min-width: 768px) {
  .hide-mobile {
    display: block;
  }
  
  .hide-desktop {
    display: none;
  }
}
```

**Responsive Design Principles:**
1. **Mobile-first**: Start with mobile, enhance for larger screens
2. **Flexible grids**: Use relative units (%, fr, em, rem)
3. **Flexible images**: Scale with container
4. **Media queries**: Apply styles based on device characteristics

## Team Leadership & Architecture

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
