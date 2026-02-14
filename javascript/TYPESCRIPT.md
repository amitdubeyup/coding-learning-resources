# TypeScript Interview Questions & Answers

A comprehensive guide covering TypeScript fundamentals, advanced types, patterns, and best practices for senior-level interviews.

## Table of Contents
1. [Core Concepts](#core-concepts)
2. [Type System](#type-system)
3. [Advanced Types](#advanced-types)
4. [Generics](#generics)
5. [Classes & OOP](#classes--oop)
6. [Modules & Namespaces](#modules--namespaces)
7. [Utility Types](#utility-types)
8. [Type Guards & Narrowing](#type-guards--narrowing)
9. [Declaration Files](#declaration-files)
10. [Configuration & Tooling](#configuration--tooling)
11. [Design Patterns](#design-patterns)
12. [Best Practices](#best-practices)
13. [React with TypeScript](#react-with-typescript)
14. [Node.js with TypeScript](#nodejs-with-typescript)

---

## Core Concepts

### Q1: What is TypeScript and why use it?
**Answer:**
TypeScript is a statically typed superset of JavaScript that compiles to plain JavaScript. It adds optional type annotations, interfaces, and modern ECMAScript features.

**Benefits:**
- **Catch errors early:** Type checking at compile time
- **Better IDE support:** Autocompletion, refactoring
- **Self-documenting code:** Types serve as documentation
- **Easier refactoring:** Compiler catches breaking changes
- **Gradual adoption:** Works with existing JavaScript

```typescript
// JavaScript - runtime error
function greet(name) {
  return name.toUpperCase();
}
greet(123); // Runtime error

// TypeScript - compile-time error
function greet(name: string): string {
  return name.toUpperCase();
}
greet(123); // ❌ Error: Argument of type 'number' is not assignable
```

---

### Q2: Explain the difference between `any`, `unknown`, and `never`
**Answer:**

| Type | Description | Use Case |
|------|-------------|----------|
| `any` | Disables type checking | Migration, escape hatch (avoid) |
| `unknown` | Type-safe alternative to any | External data, needs narrowing |
| `never` | Represents impossible values | Exhaustive checks, functions that throw |

```typescript
// any - anything goes (unsafe)
let a: any = 5;
a.foo.bar; // No error (but will crash)

// unknown - must narrow before use (safe)
let b: unknown = 5;
// b.foo.bar; // ❌ Error
if (typeof b === 'string') {
  console.log(b.toUpperCase()); // ✅ OK after narrowing
}

// never - impossible values
function fail(msg: string): never {
  throw new Error(msg);
}

// Exhaustive checking
type Shape = 'circle' | 'square';
function getArea(shape: Shape): number {
  switch (shape) {
    case 'circle': return Math.PI;
    case 'square': return 1;
    default:
      const _exhaustive: never = shape; // Error if case missed
      return _exhaustive;
  }
}
```

---

### Q3: What is the difference between `interface` and `type`?
**Answer:**

| Feature | `interface` | `type` |
|---------|------------|--------|
| Object shapes | ✅ | ✅ |
| Union/intersection | ❌ | ✅ |
| Declaration merging | ✅ | ❌ |
| Extends/implements | ✅ | ✅ (via &) |
| Computed properties | ❌ | ✅ |

```typescript
// Interface - declaration merging
interface User {
  name: string;
}
interface User {
  age: number;
}
// User now has both name and age

// Type - unions and more
type Status = 'pending' | 'active' | 'completed';
type Response = User | Error;
type Nullable<T> = T | null;

// Extension
interface Admin extends User {
  role: string;
}

type AdminType = User & { role: string };

// Recommendation: Use interface for objects, type for unions/primitives
```

---

### Q4: What are literal types?
**Answer:**
Literal types represent exact values, not just types. They enable precise type definitions.

```typescript
// String literal types
type Direction = 'up' | 'down' | 'left' | 'right';

function move(direction: Direction) {
  console.log(`Moving ${direction}`);
}
move('up');    // ✅
move('north'); // ❌ Error

// Numeric literal types
type DiceRoll = 1 | 2 | 3 | 4 | 5 | 6;

// Boolean literal
type True = true;

// const assertion
const config = {
  endpoint: 'https://api.example.com',
  timeout: 3000,
} as const;
// Type: { readonly endpoint: "https://api.example.com"; readonly timeout: 3000; }

// Template literal types (TS 4.1+)
type EventName = `on${Capitalize<'click' | 'focus' | 'blur'>}`;
// Type: "onClick" | "onFocus" | "onBlur"
```

---

## Type System

### Q5: Explain structural typing vs nominal typing
**Answer:**
TypeScript uses **structural typing** (duck typing) - types are compatible if their structures match, regardless of name.

```typescript
interface Point2D {
  x: number;
  y: number;
}

interface Coordinates {
  x: number;
  y: number;
}

const point: Point2D = { x: 1, y: 2 };
const coords: Coordinates = point; // ✅ Same structure = compatible

// Extra properties are fine when assigning variables
interface Point3D {
  x: number;
  y: number;
  z: number;
}

const point3d: Point3D = { x: 1, y: 2, z: 3 };
const point2d: Point2D = point3d; // ✅ Point3D has all Point2D properties

// But not in object literals (excess property check)
const bad: Point2D = { x: 1, y: 2, z: 3 }; // ❌ Error

// Simulating nominal types with brands
type UserId = string & { readonly brand: unique symbol };
type PostId = string & { readonly brand: unique symbol };

function getUser(id: UserId) { /* ... */ }
function getPost(id: PostId) { /* ... */ }

const userId = 'u123' as UserId;
const postId = 'p456' as PostId;

getUser(userId); // ✅
getUser(postId); // ❌ Error - different brands
```

---

### Q6: What are index signatures?
**Answer:**
Index signatures define types for dynamic property access.

```typescript
// String index signature
interface Dictionary {
  [key: string]: string;
}

const dict: Dictionary = {
  hello: 'world',
  foo: 'bar',
};
dict['newKey'] = 'newValue'; // ✅

// Number index signature (for array-like objects)
interface StringArray {
  [index: number]: string;
}

// Mixed with known properties
interface User {
  name: string;
  email: string;
  [key: string]: string; // Other string properties allowed
}

// Record utility (preferred for simple cases)
type Config = Record<string, string>;

// Mapped types for more control
type Flags = {
  [K in 'darkMode' | 'notifications' | 'sound']: boolean;
};
```

---

### Q7: Explain type inference in TypeScript
**Answer:**
TypeScript infers types from values when not explicitly specified.

```typescript
// Variable inference
let name = 'John'; // infers string
const age = 30;    // infers literal 30 (const)

// Function return inference
function add(a: number, b: number) {
  return a + b;    // infers return type number
}

// Array inference
const numbers = [1, 2, 3]; // infers number[]
const mixed = [1, 'two'];  // infers (string | number)[]

// Contextual typing
const names = ['Alice', 'Bob'];
names.forEach(name => {
  console.log(name.toUpperCase()); // name inferred as string
});

// Generic inference
function identity<T>(arg: T): T {
  return arg;
}
const str = identity('hello'); // T inferred as string

// Best common type
const arr = [1, 2, null]; // infers (number | null)[]

// Control flow analysis
function process(value: string | number) {
  if (typeof value === 'string') {
    return value.toUpperCase(); // value is string here
  }
  return value.toFixed(2); // value is number here
}
```

---

## Advanced Types

### Q8: Explain union and intersection types
**Answer:**

**Union (`|`):** Value can be ANY of the types
**Intersection (`&`):** Value must satisfy ALL types

```typescript
// Union - OR
type StringOrNumber = string | number;

function process(value: StringOrNumber) {
  if (typeof value === 'string') {
    return value.toUpperCase();
  }
  return value * 2;
}

// Discriminated union (tagged union)
type Success = { status: 'success'; data: string };
type Error = { status: 'error'; message: string };
type Result = Success | Error;

function handle(result: Result) {
  if (result.status === 'success') {
    console.log(result.data);    // TypeScript knows it's Success
  } else {
    console.log(result.message); // TypeScript knows it's Error
  }
}

// Intersection - AND
type Person = { name: string };
type Employee = { employeeId: number };
type EmployeePerson = Person & Employee;

const emp: EmployeePerson = {
  name: 'John',
  employeeId: 123,
};

// Combining interfaces
interface Timestamped {
  createdAt: Date;
  updatedAt: Date;
}

interface Identifiable {
  id: string;
}

type Entity = Timestamped & Identifiable;
```

---

### Q9: What are conditional types?
**Answer:**
Conditional types select types based on conditions, enabling type-level programming.

```typescript
// Basic syntax: T extends U ? X : Y
type IsString<T> = T extends string ? true : false;

type A = IsString<string>;  // true
type B = IsString<number>;  // false

// Extract types from unions
type ExtractString<T> = T extends string ? T : never;
type Strings = ExtractString<string | number | boolean>; // string

// Infer keyword - extract type information
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;

function getString(): string { return 'hello'; }
type Result = ReturnType<typeof getString>; // string

// Extract array element type
type ArrayElement<T> = T extends (infer E)[] ? E : never;
type Elem = ArrayElement<number[]>; // number

// Distributive conditional types
type Nullable<T> = T extends any ? T | null : never;
type NullableStringOrNumber = Nullable<string | number>;
// Result: string | null | number | null

// Practical example: Unwrap Promise
type Awaited<T> = T extends Promise<infer U> ? Awaited<U> : T;
type Result1 = Awaited<Promise<string>>;              // string
type Result2 = Awaited<Promise<Promise<number>>>;     // number
```

---

### Q10: What are mapped types?
**Answer:**
Mapped types transform properties of existing types.

```typescript
// Make all properties optional
type Partial<T> = {
  [K in keyof T]?: T[K];
};

// Make all properties required
type Required<T> = {
  [K in keyof T]-?: T[K];
};

// Make all properties readonly
type Readonly<T> = {
  readonly [K in keyof T]: T[K];
};

// Remove readonly (mutable)
type Mutable<T> = {
  -readonly [K in keyof T]: T[K];
};

// Pick specific keys
type Pick<T, K extends keyof T> = {
  [P in K]: T[P];
};

// Omit keys
type Omit<T, K extends keyof any> = Pick<T, Exclude<keyof T, K>>;

// Transform property types
type Stringify<T> = {
  [K in keyof T]: string;
};

// Key remapping (TS 4.1+)
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};

interface Person {
  name: string;
  age: number;
}

type PersonGetters = Getters<Person>;
// { getName: () => string; getAge: () => number; }
```

---

## Generics

### Q11: What are generics and why use them?
**Answer:**
Generics create reusable components that work with multiple types while maintaining type safety.

```typescript
// Without generics - lose type information
function identity(arg: any): any {
  return arg;
}

// With generics - preserve type
function identity<T>(arg: T): T {
  return arg;
}

const str = identity<string>('hello'); // string
const num = identity(42);              // number (inferred)

// Multiple type parameters
function pair<K, V>(key: K, value: V): [K, V] {
  return [key, value];
}

// Generic constraints
interface HasLength {
  length: number;
}

function logLength<T extends HasLength>(arg: T): T {
  console.log(arg.length);
  return arg;
}

logLength('hello');    // ✅
logLength([1, 2, 3]);  // ✅
logLength(123);        // ❌ Error: number doesn't have length

// Default type parameters
interface Container<T = string> {
  value: T;
}

const strContainer: Container = { value: 'hello' };           // T = string
const numContainer: Container<number> = { value: 42 };        // T = number
```

---

### Q12: Explain generic constraints and keyof
**Answer:**

```typescript
// keyof - union of property names
interface User {
  name: string;
  age: number;
  email: string;
}

type UserKeys = keyof User; // "name" | "age" | "email"

// Generic constraint with keyof
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

const user: User = { name: 'John', age: 30, email: 'john@example.com' };
const name = getProperty(user, 'name');   // string
const age = getProperty(user, 'age');     // number
// getProperty(user, 'invalid');          // ❌ Error

// Constraining to specific types
function pluck<T, K extends keyof T>(objects: T[], key: K): T[K][] {
  return objects.map(obj => obj[key]);
}

const users = [
  { name: 'John', age: 30 },
  { name: 'Jane', age: 25 },
];
const names = pluck(users, 'name'); // string[]

// Multiple constraints
interface Printable {
  print(): void;
}

interface Loggable {
  log(): void;
}

function process<T extends Printable & Loggable>(item: T) {
  item.print();
  item.log();
}
```

---

### Q13: How do you use generics with classes and interfaces?
**Answer:**

```typescript
// Generic interface
interface Repository<T> {
  getById(id: string): Promise<T>;
  save(item: T): Promise<T>;
  delete(id: string): Promise<void>;
}

// Generic class
class GenericRepository<T extends { id: string }> implements Repository<T> {
  private items: Map<string, T> = new Map();

  async getById(id: string): Promise<T> {
    const item = this.items.get(id);
    if (!item) throw new Error('Not found');
    return item;
  }

  async save(item: T): Promise<T> {
    this.items.set(item.id, item);
    return item;
  }

  async delete(id: string): Promise<void> {
    this.items.delete(id);
  }
}

// Usage
interface User {
  id: string;
  name: string;
}

const userRepo = new GenericRepository<User>();

// Generic class with static members
class Container<T> {
  private static count = 0;
  private value: T;

  constructor(value: T) {
    this.value = value;
    Container.count++;
  }

  getValue(): T {
    return this.value;
  }
}

// Generic factory pattern
function createInstance<T>(
  ctor: new (...args: any[]) => T,
  ...args: any[]
): T {
  return new ctor(...args);
}
```

---

## Classes & OOP

### Q14: Explain access modifiers in TypeScript
**Answer:**

| Modifier | Class | Subclass | Outside |
|----------|-------|----------|---------|
| `public` | ✅ | ✅ | ✅ |
| `protected` | ✅ | ✅ | ❌ |
| `private` | ✅ | ❌ | ❌ |
| `#` (ES private) | ✅ | ❌ | ❌ |

```typescript
class Person {
  public name: string;           // Accessible everywhere
  protected age: number;         // Class and subclasses
  private ssn: string;           // Class only (TS compile-time)
  #bankAccount: string;          // Class only (runtime private)

  constructor(name: string, age: number, ssn: string) {
    this.name = name;
    this.age = age;
    this.ssn = ssn;
    this.#bankAccount = '****';
  }
}

class Employee extends Person {
  getAge() {
    return this.age;    // ✅ protected accessible
    // return this.ssn; // ❌ private not accessible
  }
}

const person = new Person('John', 30, '123-45-6789');
console.log(person.name);  // ✅
// console.log(person.age);  // ❌ protected
// console.log(person.ssn);  // ❌ private

// readonly modifier
class Config {
  readonly apiUrl: string;
  
  constructor(url: string) {
    this.apiUrl = url;
  }
}
```

---

### Q15: What are abstract classes and when to use them?
**Answer:**
Abstract classes are base classes that cannot be instantiated directly. They can contain abstract methods that must be implemented by subclasses.

```typescript
abstract class Shape {
  abstract getArea(): number;  // Must be implemented
  abstract getPerimeter(): number;

  // Concrete method with implementation
  describe(): string {
    return `Area: ${this.getArea()}, Perimeter: ${this.getPerimeter()}`;
  }
}

class Circle extends Shape {
  constructor(private radius: number) {
    super();
  }

  getArea(): number {
    return Math.PI * this.radius ** 2;
  }

  getPerimeter(): number {
    return 2 * Math.PI * this.radius;
  }
}

class Rectangle extends Shape {
  constructor(private width: number, private height: number) {
    super();
  }

  getArea(): number {
    return this.width * this.height;
  }

  getPerimeter(): number {
    return 2 * (this.width + this.height);
  }
}

// const shape = new Shape(); // ❌ Cannot instantiate abstract class
const circle = new Circle(5);
console.log(circle.describe());

// When to use abstract class vs interface:
// - Abstract class: shared implementation, single inheritance
// - Interface: contract definition, multiple inheritance
```

---

### Q16: How do you implement mixins in TypeScript?
**Answer:**
Mixins add functionality to classes without inheritance.

```typescript
// Mixin pattern
type Constructor<T = {}> = new (...args: any[]) => T;

function Timestamped<TBase extends Constructor>(Base: TBase) {
  return class extends Base {
    createdAt = new Date();
    updatedAt = new Date();

    touch() {
      this.updatedAt = new Date();
    }
  };
}

function Activatable<TBase extends Constructor>(Base: TBase) {
  return class extends Base {
    isActive = false;

    activate() {
      this.isActive = true;
    }

    deactivate() {
      this.isActive = false;
    }
  };
}

// Base class
class User {
  constructor(public name: string) {}
}

// Apply mixins
const TimestampedUser = Timestamped(User);
const ActivatableTimestampedUser = Activatable(TimestampedUser);

const user = new ActivatableTimestampedUser('John');
user.activate();
user.touch();
console.log(user.name, user.isActive, user.updatedAt);
```

---

## Utility Types

### Q17: Explain built-in utility types
**Answer:**

```typescript
interface User {
  id: string;
  name: string;
  email: string;
  age?: number;
}

// Partial - make all properties optional
type PartialUser = Partial<User>;
// { id?: string; name?: string; email?: string; age?: number; }

// Required - make all properties required
type RequiredUser = Required<User>;
// { id: string; name: string; email: string; age: number; }

// Readonly - make all properties readonly
type ReadonlyUser = Readonly<User>;

// Pick - select specific properties
type UserPreview = Pick<User, 'id' | 'name'>;
// { id: string; name: string; }

// Omit - exclude properties
type UserWithoutId = Omit<User, 'id'>;
// { name: string; email: string; age?: number; }

// Record - create object type with specific keys and values
type StringMap = Record<string, string>;
type UserRoles = Record<'admin' | 'user' | 'guest', string[]>;

// Exclude - exclude from union
type NonString = Exclude<string | number | boolean, string>;
// number | boolean

// Extract - extract from union
type OnlyString = Extract<string | number | boolean, string>;
// string

// NonNullable - remove null and undefined
type Defined = NonNullable<string | null | undefined>;
// string

// ReturnType - get function return type
function getUser() { return { name: 'John' }; }
type GetUserReturn = ReturnType<typeof getUser>;
// { name: string; }

// Parameters - get function parameter types
type GetUserParams = Parameters<typeof getUser>;
// []

// ConstructorParameters
class MyClass {
  constructor(name: string, age: number) {}
}
type MyClassParams = ConstructorParameters<typeof MyClass>;
// [string, number]

// Awaited - unwrap Promise
type AwaitedString = Awaited<Promise<string>>;
// string
```

---

### Q18: How do you create custom utility types?
**Answer:**

```typescript
// Make specific properties optional
type PartialBy<T, K extends keyof T> = Omit<T, K> & Partial<Pick<T, K>>;

interface User {
  id: string;
  name: string;
  email: string;
}

type UserWithOptionalEmail = PartialBy<User, 'email'>;
// { id: string; name: string; email?: string; }

// Make specific properties required
type RequiredBy<T, K extends keyof T> = T & Required<Pick<T, K>>;

// Deep Partial
type DeepPartial<T> = T extends object ? {
  [P in keyof T]?: DeepPartial<T[P]>;
} : T;

// Deep Readonly
type DeepReadonly<T> = T extends object ? {
  readonly [P in keyof T]: DeepReadonly<T[P]>;
} : T;

// Nullable
type Nullable<T> = { [P in keyof T]: T[P] | null };

// Mutable (remove readonly)
type Mutable<T> = { -readonly [P in keyof T]: T[P] };

// Get optional keys
type OptionalKeys<T> = {
  [K in keyof T]-?: {} extends Pick<T, K> ? K : never;
}[keyof T];

// Get required keys
type RequiredKeys<T> = {
  [K in keyof T]-?: {} extends Pick<T, K> ? never : K;
}[keyof T];

// Function type overload
type Overloaded = {
  (x: string): string;
  (x: number): number;
};
```

---

## Type Guards & Narrowing

### Q19: What are type guards and how do you create them?
**Answer:**
Type guards narrow types within conditional blocks.

```typescript
// typeof guard
function process(value: string | number) {
  if (typeof value === 'string') {
    return value.toUpperCase(); // value is string
  }
  return value.toFixed(2); // value is number
}

// instanceof guard
class Dog { bark() {} }
class Cat { meow() {} }

function speak(animal: Dog | Cat) {
  if (animal instanceof Dog) {
    animal.bark();
  } else {
    animal.meow();
  }
}

// in operator
interface Fish { swim(): void }
interface Bird { fly(): void }

function move(animal: Fish | Bird) {
  if ('swim' in animal) {
    animal.swim();
  } else {
    animal.fly();
  }
}

// Custom type guard (type predicate)
interface User { type: 'user'; name: string }
interface Admin { type: 'admin'; name: string; permissions: string[] }

function isAdmin(person: User | Admin): person is Admin {
  return person.type === 'admin';
}

function getPermissions(person: User | Admin) {
  if (isAdmin(person)) {
    return person.permissions; // person is Admin
  }
  return []; // person is User
}

// Assertion function
function assertIsString(value: unknown): asserts value is string {
  if (typeof value !== 'string') {
    throw new Error('Expected string');
  }
}

function process(value: unknown) {
  assertIsString(value);
  console.log(value.toUpperCase()); // value is string after assertion
}
```

---

### Q20: Explain discriminated unions
**Answer:**
Discriminated unions use a common property (discriminant) to narrow union types.

```typescript
// Network request states
interface Loading {
  state: 'loading';
}

interface Success<T> {
  state: 'success';
  data: T;
}

interface Error {
  state: 'error';
  message: string;
}

type RequestState<T> = Loading | Success<T> | Error;

function handleRequest<T>(request: RequestState<T>) {
  switch (request.state) {
    case 'loading':
      return 'Loading...';
    case 'success':
      return request.data;  // TypeScript knows it's Success<T>
    case 'error':
      return request.message; // TypeScript knows it's Error
  }
}

// Redux-style actions
type Action =
  | { type: 'INCREMENT' }
  | { type: 'DECREMENT' }
  | { type: 'SET'; payload: number };

function reducer(state: number, action: Action): number {
  switch (action.type) {
    case 'INCREMENT':
      return state + 1;
    case 'DECREMENT':
      return state - 1;
    case 'SET':
      return action.payload; // TypeScript knows payload exists
  }
}

// Exhaustive checking
function exhaustiveCheck(action: Action): number {
  switch (action.type) {
    case 'INCREMENT': return 1;
    case 'DECREMENT': return -1;
    case 'SET': return action.payload;
    default:
      const _exhaustive: never = action;
      throw new Error(`Unhandled action: ${_exhaustive}`);
  }
}
```

---

## Declaration Files

### Q21: What are declaration files (.d.ts)?
**Answer:**
Declaration files provide type information for JavaScript libraries without creating runtime code.

```typescript
// types/my-library.d.ts

// Module declaration
declare module 'my-library' {
  export function doSomething(value: string): number;
  export const VERSION: string;
  
  export interface Options {
    timeout?: number;
    retry?: boolean;
  }
  
  export class MyClass {
    constructor(options?: Options);
    process(data: string): Promise<void>;
  }
  
  export default MyClass;
}

// Global augmentation
declare global {
  interface Window {
    myGlobalVar: string;
  }
  
  interface Array<T> {
    customMethod(): T[];
  }
}

// Ambient declarations
declare const API_URL: string;
declare function legacyFunction(x: number): void;

// Module augmentation
declare module 'express' {
  interface Request {
    user?: {
      id: string;
      role: string;
    };
  }
}
```

---

### Q22: How do you create types for a JavaScript library?
**Answer:**

```typescript
// For a library like: jquery-like.js
// Expose $function and jQuery object

// types/jquery-like.d.ts

interface JQueryElement {
  html(): string;
  html(content: string): JQueryElement;
  css(property: string): string;
  css(property: string, value: string): JQueryElement;
  css(properties: Record<string, string>): JQueryElement;
  on(event: string, handler: (e: Event) => void): JQueryElement;
  addClass(className: string): JQueryElement;
  removeClass(className: string): JQueryElement;
}

interface JQueryStatic {
  (selector: string): JQueryElement;
  (element: Element): JQueryElement;
  ajax(options: AjaxOptions): Promise<any>;
  get(url: string): Promise<any>;
  post(url: string, data?: any): Promise<any>;
}

interface AjaxOptions {
  url: string;
  method?: 'GET' | 'POST' | 'PUT' | 'DELETE';
  data?: any;
  headers?: Record<string, string>;
}

declare const $: JQueryStatic;
declare const jQuery: JQueryStatic;

export = $;
export as namespace $;
```

---

## Configuration & Tooling

### Q23: Explain key tsconfig.json options
**Answer:**

```jsonc
{
  "compilerOptions": {
    // Target & Module
    "target": "ES2022",              // Output JS version
    "module": "NodeNext",            // Module system
    "moduleResolution": "NodeNext",  // How to resolve imports
    "lib": ["ES2022", "DOM"],        // Available APIs

    // Strictness (enable all for new projects)
    "strict": true,                  // Enable all strict checks
    "noImplicitAny": true,           // Error on implied 'any'
    "strictNullChecks": true,        // null/undefined are distinct
    "strictFunctionTypes": true,     // Strict function type checking
    "noUncheckedIndexedAccess": true, // Add undefined to index sigs

    // Output
    "outDir": "./dist",              // Output directory
    "rootDir": "./src",              // Source root
    "declaration": true,             // Generate .d.ts files
    "declarationMap": true,          // Source maps for .d.ts
    "sourceMap": true,               // Generate source maps

    // Module interop
    "esModuleInterop": true,         // Better CommonJS interop
    "allowSyntheticDefaultImports": true,

    // Path mapping
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@components/*": ["src/components/*"]
    },

    // Project references
    "composite": true,               // Enable project references
    "incremental": true,             // Faster rebuilds

    // Type checking
    "skipLibCheck": true,            // Skip .d.ts checking (faster)
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

---

### Q24: How do you set up TypeScript with modern tools?
**Answer:**

```jsonc
// package.json scripts
{
  "scripts": {
    "build": "tsc",
    "build:watch": "tsc --watch",
    "typecheck": "tsc --noEmit",
    "lint": "eslint . --ext .ts,.tsx"
  }
}
```

```javascript
// eslint.config.js (ESLint 9+ flat config)
import eslint from '@eslint/js';
import tseslint from 'typescript-eslint';

export default tseslint.config(
  eslint.configs.recommended,
  ...tseslint.configs.strictTypeChecked,
  {
    languageOptions: {
      parserOptions: {
        project: true,
      },
    },
    rules: {
      '@typescript-eslint/no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
      '@typescript-eslint/explicit-function-return-type': 'off',
    },
  }
);
```

```jsonc
// Vite config (vite.config.ts)
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
});
```

---

## Design Patterns

### Q25: How do you implement the Builder pattern?
**Answer:**

```typescript
class RequestBuilder {
  private url: string = '';
  private method: 'GET' | 'POST' | 'PUT' | 'DELETE' = 'GET';
  private headers: Record<string, string> = {};
  private body?: unknown;

  setUrl(url: string): this {
    this.url = url;
    return this;
  }

  setMethod(method: 'GET' | 'POST' | 'PUT' | 'DELETE'): this {
    this.method = method;
    return this;
  }

  setHeader(key: string, value: string): this {
    this.headers[key] = value;
    return this;
  }

  setBody<T>(body: T): this {
    this.body = body;
    return this;
  }

  build(): Request {
    return {
      url: this.url,
      method: this.method,
      headers: this.headers,
      body: this.body,
    };
  }
}

interface Request {
  url: string;
  method: string;
  headers: Record<string, string>;
  body?: unknown;
}

// Usage
const request = new RequestBuilder()
  .setUrl('/api/users')
  .setMethod('POST')
  .setHeader('Content-Type', 'application/json')
  .setBody({ name: 'John' })
  .build();
```

---

### Q26: How do you implement the Factory pattern?
**Answer:**

```typescript
// Abstract factory
interface Button {
  render(): string;
  onClick(handler: () => void): void;
}

interface Dialog {
  show(): void;
  close(): void;
}

interface UIFactory {
  createButton(text: string): Button;
  createDialog(title: string): Dialog;
}

// Concrete implementations
class WindowsButton implements Button {
  constructor(private text: string) {}
  render() { return `<win-button>${this.text}</win-button>`; }
  onClick(handler: () => void) { /* Windows implementation */ }
}

class MacButton implements Button {
  constructor(private text: string) {}
  render() { return `<mac-button>${this.text}</mac-button>`; }
  onClick(handler: () => void) { /* Mac implementation */ }
}

class WindowsFactory implements UIFactory {
  createButton(text: string): Button {
    return new WindowsButton(text);
  }
  createDialog(title: string): Dialog {
    return new WindowsDialog(title);
  }
}

class MacFactory implements UIFactory {
  createButton(text: string): Button {
    return new MacButton(text);
  }
  createDialog(title: string): Dialog {
    return new MacDialog(title);
  }
}

// Factory function
function createUIFactory(os: 'windows' | 'mac'): UIFactory {
  switch (os) {
    case 'windows': return new WindowsFactory();
    case 'mac': return new MacFactory();
  }
}
```

---

## Best Practices

### Q27: What are TypeScript best practices?
**Answer:**

```typescript
// 1. Enable strict mode
// tsconfig.json: "strict": true

// 2. Avoid 'any', use 'unknown' instead
function processInput(input: unknown) {
  if (typeof input === 'string') {
    return input.toUpperCase();
  }
}

// 3. Use const assertions for literals
const config = {
  api: 'https://api.example.com',
  timeout: 3000,
} as const;

// 4. Prefer interfaces for objects, types for unions
interface User {
  name: string;
  email: string;
}
type Status = 'pending' | 'active' | 'completed';

// 5. Use discriminated unions for state
type LoadingState<T> =
  | { status: 'loading' }
  | { status: 'success'; data: T }
  | { status: 'error'; error: Error };

// 6. Use type guards for type narrowing
function isUser(value: unknown): value is User {
  return typeof value === 'object' && value !== null && 'name' in value;
}

// 7. Avoid type assertions when possible
// Bad: const user = response as User;
// Good: validate and narrow

// 8. Use satisfies for type validation without widening
const routes = {
  home: '/',
  about: '/about',
} satisfies Record<string, string>;
// routes.home is still "/" literal, not string

// 9. Use explicit return types for public APIs
export function createUser(name: string): User {
  return { name, email: '' };
}

// 10. Prefer readonly for immutability
interface Config {
  readonly apiUrl: string;
  readonly items: readonly string[];
}
```

---

### Q28: How do you handle errors in TypeScript?
**Answer:**

```typescript
// Custom error classes
class AppError extends Error {
  constructor(
    message: string,
    public code: string,
    public statusCode: number = 500
  ) {
    super(message);
    this.name = 'AppError';
  }
}

class ValidationError extends AppError {
  constructor(message: string, public fields: string[]) {
    super(message, 'VALIDATION_ERROR', 400);
    this.name = 'ValidationError';
  }
}

// Result type pattern
type Result<T, E = Error> =
  | { success: true; data: T }
  | { success: false; error: E };

function divide(a: number, b: number): Result<number, string> {
  if (b === 0) {
    return { success: false, error: 'Division by zero' };
  }
  return { success: true, data: a / b };
}

const result = divide(10, 2);
if (result.success) {
  console.log(result.data);
} else {
  console.error(result.error);
}

// Type-safe try-catch
function safeJsonParse<T>(json: string): Result<T> {
  try {
    const data = JSON.parse(json) as T;
    return { success: true, data };
  } catch (error) {
    return {
      success: false,
      error: error instanceof Error ? error : new Error(String(error)),
    };
  }
}
```

---

## React with TypeScript

### Q29: How do you type React components?
**Answer:**

```typescript
import { FC, ReactNode, useState, useEffect } from 'react';

// Function component with props
interface ButtonProps {
  children: ReactNode;
  variant?: 'primary' | 'secondary';
  disabled?: boolean;
  onClick?: () => void;
}

const Button: FC<ButtonProps> = ({
  children,
  variant = 'primary',
  disabled = false,
  onClick,
}) => {
  return (
    <button
      className={`btn btn-${variant}`}
      disabled={disabled}
      onClick={onClick}
    >
      {children}
    </button>
  );
};

// Generic component
interface ListProps<T> {
  items: T[];
  renderItem: (item: T, index: number) => ReactNode;
  keyExtractor: (item: T) => string;
}

function List<T>({ items, renderItem, keyExtractor }: ListProps<T>) {
  return (
    <ul>
      {items.map((item, index) => (
        <li key={keyExtractor(item)}>{renderItem(item, index)}</li>
      ))}
    </ul>
  );
}

// Typing hooks
const [user, setUser] = useState<User | null>(null);
const [items, setItems] = useState<string[]>([]);

useEffect(() => {
  const controller = new AbortController();
  
  async function fetchData() {
    const response = await fetch('/api/user', {
      signal: controller.signal,
    });
    const data: User = await response.json();
    setUser(data);
  }
  
  fetchData();
  return () => controller.abort();
}, []);

// Event handlers
const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
  console.log(event.target.value);
};

const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
  event.preventDefault();
};
```

---

### Q30: How do you type custom hooks?
**Answer:**

```typescript
import { useState, useEffect, useCallback, useMemo } from 'react';

// Fetch hook with generics
function useFetch<T>(url: string) {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    const controller = new AbortController();
    
    setLoading(true);
    fetch(url, { signal: controller.signal })
      .then(res => res.json())
      .then((data: T) => {
        setData(data);
        setError(null);
      })
      .catch(err => {
        if (err.name !== 'AbortError') {
          setError(err);
        }
      })
      .finally(() => setLoading(false));

    return () => controller.abort();
  }, [url]);

  return { data, loading, error };
}

// Usage
const { data: users } = useFetch<User[]>('/api/users');

// Local storage hook
function useLocalStorage<T>(
  key: string,
  initialValue: T
): [T, (value: T | ((prev: T) => T)) => void] {
  const [storedValue, setStoredValue] = useState<T>(() => {
    try {
      const item = localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch {
      return initialValue;
    }
  });

  const setValue = useCallback((value: T | ((prev: T) => T)) => {
    setStoredValue(prev => {
      const valueToStore = value instanceof Function ? value(prev) : value;
      localStorage.setItem(key, JSON.stringify(valueToStore));
      return valueToStore;
    });
  }, [key]);

  return [storedValue, setValue];
}

// Debounce hook
function useDebounce<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => setDebouncedValue(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);

  return debouncedValue;
}
```

---

## Node.js with TypeScript

### Q31: How do you set up TypeScript for Node.js?
**Answer:**

```jsonc
// tsconfig.json for Node.js
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "declaration": true,
    "sourceMap": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
```

```typescript
// src/server.ts
import express, { Request, Response, NextFunction } from 'express';

// Extend Request type
declare global {
  namespace Express {
    interface Request {
      user?: { id: string; email: string };
    }
  }
}

const app = express();

// Typed middleware
const authMiddleware = (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  const token = req.headers.authorization;
  if (token) {
    req.user = { id: '1', email: 'user@example.com' };
  }
  next();
};

// Typed route handler
interface CreateUserBody {
  name: string;
  email: string;
}

app.post('/users', (
  req: Request<{}, {}, CreateUserBody>,
  res: Response
) => {
  const { name, email } = req.body;
  res.json({ id: '1', name, email });
});

// Error handling
interface AppError extends Error {
  statusCode?: number;
}

const errorHandler = (
  err: AppError,
  req: Request,
  res: Response,
  next: NextFunction
) => {
  res.status(err.statusCode || 500).json({
    error: err.message,
  });
};

app.use(errorHandler);
```

---

### Q32: How do you type environment variables?
**Answer:**

```typescript
// src/env.ts
import { z } from 'zod';

const envSchema = z.object({
  NODE_ENV: z.enum(['development', 'production', 'test']),
  PORT: z.coerce.number().default(3000),
  DATABASE_URL: z.string().url(),
  JWT_SECRET: z.string().min(32),
  REDIS_URL: z.string().optional(),
});

// Parse and validate
const parsed = envSchema.safeParse(process.env);

if (!parsed.success) {
  console.error('Invalid environment variables:', parsed.error.format());
  process.exit(1);
}

export const env = parsed.data;

// Type is inferred
// env.PORT is number
// env.NODE_ENV is 'development' | 'production' | 'test'

// Alternative: Declaration merging
declare global {
  namespace NodeJS {
    interface ProcessEnv {
      NODE_ENV: 'development' | 'production' | 'test';
      PORT: string;
      DATABASE_URL: string;
      JWT_SECRET: string;
    }
  }
}

// Now process.env is typed
const port = parseInt(process.env.PORT, 10);
```

---

## Quick Reference

### Common Patterns Cheat Sheet

```typescript
// Ensure exhaustive switch
function assertNever(x: never): never {
  throw new Error('Unexpected value: ' + x);
}

// Type-safe object keys
const keys = Object.keys(obj) as Array<keyof typeof obj>;

// Type-safe Object.entries
function entries<T extends object>(obj: T) {
  return Object.entries(obj) as Array<[keyof T, T[keyof T]]>;
}

// Readonly deeply nested
type DeepReadonly<T> = {
  readonly [P in keyof T]: T[P] extends object ? DeepReadonly<T[P]> : T[P];
};

// Make certain keys required
type WithRequired<T, K extends keyof T> = T & { [P in K]-?: T[P] };

// Branded types for type safety
type Brand<K, T> = K & { __brand: T };
type USD = Brand<number, 'USD'>;
type EUR = Brand<number, 'EUR'>;

// Discriminated union helper
type DiscriminatedUnion<K extends PropertyKey, T extends object> = {
  [P in keyof T]: { [Q in K]: P } & T[P];
}[keyof T];
```

---

*Last updated: February 2026*
