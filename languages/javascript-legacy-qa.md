# 200 JavaScript Interview Questions

## Table of Contents
1. [JavaScript Fundamentals](#javascript-fundamentals)
2. [Variables and Data Types](#variables-and-data-types)
3. [Operators and Expressions](#operators-and-expressions)
4. [Control Flow](#control-flow)
5. [Functions](#functions)
6. [Objects and Prototypes](#objects-and-prototypes)
7. [Arrays and Array Methods](#arrays-and-array-methods)
8. [Asynchronous JavaScript](#asynchronous-javascript)
9. [DOM Manipulation](#dom-manipulation)
10. [Error Handling](#error-handling)
11. [ES6+ Features](#es6-features)
12. [Design Patterns](#design-patterns)
13. [Testing and Debugging](#testing-and-debugging)
14. [Performance Optimization](#performance-optimization)
15. [Security](#security)

## JavaScript Fundamentals

1. **What is JavaScript?**
   - JavaScript is a high-level, interpreted programming language that conforms to the ECMAScript specification. It is a language that is also characterized as dynamic, weakly typed, prototype-based and multi-paradigm.

2. **What are the key features of JavaScript?**
   - Dynamic typing
   - Object-oriented programming
   - Functional programming
   - Prototype-based inheritance
   - First-class functions
   - Closures
   - Event-driven programming

3. **What is the difference between JavaScript and Java?**
   ```javascript
   // JavaScript
   let x = 5;
   x = "Hello"; // Valid - dynamic typing
   
   // Java
   int x = 5;
   x = "Hello"; // Invalid - static typing
   ```

4. **What is the difference between `==` and `===`?**
   ```javascript
   console.log(1 == "1");  // true (type coercion)
   console.log(1 === "1"); // false (strict equality)
   ```

5. **What is type coercion in JavaScript?**
   ```javascript
   console.log("5" + 3);    // "53" (string concatenation)
   console.log("5" - 3);    // 2 (numeric subtraction)
   console.log("5" * 3);    // 15 (numeric multiplication)
   ```

## Variables and Data Types

6. **What are the different ways to declare variables in JavaScript?**
   ```javascript
   var oldWay = "not recommended";
   let modernWay = "block scoped";
   const constant = "cannot be reassigned";
   ```

7. **What is the difference between `var`, `let`, and `const`?**
   ```javascript
   // var - function scoped
   function example() {
     var x = 1;
     if (true) {
       var x = 2; // same variable
     }
     console.log(x); // 2
   }

   // let - block scoped
   function example2() {
     let x = 1;
     if (true) {
       let x = 2; // different variable
     }
     console.log(x); // 1
   }
   ```

8. **What are the primitive data types in JavaScript?**
   ```javascript
   let string = "Hello";
   let number = 42;
   let boolean = true;
   let nullValue = null;
   let undefinedValue = undefined;
   let symbol = Symbol("description");
   let bigInt = 9007199254740991n;
   ```

9. **What is the difference between `null` and `undefined`?**
   ```javascript
   let a; // undefined
   let b = null; // null
   console.log(typeof a); // "undefined"
   console.log(typeof b); // "object"
   ```

10. **What is type conversion in JavaScript?**
    ```javascript
    // Explicit conversion
    let num = Number("123");
    let str = String(123);
    let bool = Boolean(1);

    // Implicit conversion
    let result = "5" + 3; // "53"
    ```

## Operators and Expressions

11. **What are the different types of operators in JavaScript?**
    ```javascript
    // Arithmetic
    let sum = 1 + 2;
    let diff = 5 - 3;
    let product = 4 * 2;
    let quotient = 10 / 2;
    let remainder = 10 % 3;

    // Comparison
    let isEqual = 5 === 5;
    let isGreater = 10 > 5;

    // Logical
    let and = true && false;
    let or = true || false;
    let not = !true;
    ```

12. **What is the difference between `++i` and `i++`?**
    ```javascript
    let i = 1;
    console.log(++i); // 2 (increments first, then returns)
    console.log(i++); // 2 (returns first, then increments)
    console.log(i);   // 3
    ```

13. **What is the ternary operator?**
    ```javascript
    let age = 20;
    let canVote = age >= 18 ? "Yes" : "No";
    ```

14. **What is the nullish coalescing operator (??)?**
    ```javascript
    let value = null ?? "default"; // "default"
    let value2 = 0 ?? "default";   // 0
    ```

15. **What is the optional chaining operator (?.)?**
    ```javascript
    const user = {
      address: {
        street: "Main St"
      }
    };
    console.log(user?.address?.street); // "Main St"
    console.log(user?.contact?.phone);  // undefined
    ```

## Control Flow

16. **What are the different types of loops in JavaScript?**
    ```javascript
    // for loop
    for (let i = 0; i < 5; i++) {
      console.log(i);
    }

    // while loop
    let i = 0;
    while (i < 5) {
      console.log(i);
      i++;
    }

    // do-while loop
    let j = 0;
    do {
      console.log(j);
      j++;
    } while (j < 5);

    // for...of loop
    const arr = [1, 2, 3];
    for (const item of arr) {
      console.log(item);
    }

    // for...in loop
    const obj = { a: 1, b: 2 };
    for (const key in obj) {
      console.log(key, obj[key]);
    }
    ```

17. **What is the difference between `break` and `continue`?**
    ```javascript
    // break
    for (let i = 0; i < 5; i++) {
      if (i === 3) break;
      console.log(i); // 0, 1, 2
    }

    // continue
    for (let i = 0; i < 5; i++) {
      if (i === 3) continue;
      console.log(i); // 0, 1, 2, 4
    }
    ```

18. **What is the switch statement?**
    ```javascript
    let day = "Monday";
    switch (day) {
      case "Monday":
        console.log("Start of week");
        break;
      case "Friday":
        console.log("End of week");
        break;
      default:
        console.log("Middle of week");
    }
    ```

19. **What is the difference between `if` and `switch`?**
    ```javascript
    // if statement
    if (condition1) {
      // code
    } else if (condition2) {
      // code
    } else {
      // code
    }

    // switch statement
    switch (value) {
      case 1:
        // code
        break;
      case 2:
        // code
        break;
      default:
        // code
    }
    ```

20. **What is the difference between `for...in` and `for...of`?**
    ```javascript
    const arr = [1, 2, 3];
    
    // for...in iterates over enumerable properties
    for (const index in arr) {
      console.log(index); // "0", "1", "2"
    }
    
    // for...of iterates over values
    for (const value of arr) {
      console.log(value); // 1, 2, 3
    }
    ```

## Functions

21. **What is a function in JavaScript?**
    ```javascript
    // Function declaration
    function greet(name) {
      return `Hello, ${name}!`;
    }

    // Function expression
    const greet = function(name) {
      return `Hello, ${name}!`;
    };

    // Arrow function
    const greet = (name) => `Hello, ${name}!`;
    ```

22. **What is the difference between function declaration and function expression?**
    ```javascript
    // Function declaration - hoisted
    console.log(greet("John")); // Works
    function greet(name) {
      return `Hello, ${name}!`;
    }

    // Function expression - not hoisted
    console.log(greet("John")); // Error
    const greet = function(name) {
      return `Hello, ${name}!`;
    };
    ```

23. **What is an arrow function?**
    ```javascript
    // Regular function
    function add(a, b) {
      return a + b;
    }

    // Arrow function
    const add = (a, b) => a + b;
    ```

24. **What is the difference between regular functions and arrow functions?**
    ```javascript
    const obj = {
      value: 42,
      regular: function() {
        console.log(this.value); // 42
      },
      arrow: () => {
        console.log(this.value); // undefined
      }
    };
    ```

25. **What is a callback function?**
    ```javascript
    function fetchData(callback) {
      setTimeout(() => {
        callback("Data received");
      }, 1000);
    }

    fetchData((data) => {
      console.log(data);
    });
    ```

## Objects and Prototypes

26. **What is an object in JavaScript?**
    ```javascript
    const person = {
      name: "John",
      age: 30,
      greet() {
        console.log(`Hello, I'm ${this.name}`);
      }
    };
    ```

27. **What is object destructuring?**
    ```javascript
    const person = { name: "John", age: 30 };
    const { name, age } = person;
    console.log(name); // "John"
    console.log(age);  // 30
    ```

28. **What is the difference between `Object.create()` and `new`?**
    ```javascript
    // Using new
    function Person(name) {
      this.name = name;
    }
    const person1 = new Person("John");

    // Using Object.create
    const personProto = {
      greet() {
        console.log(`Hello, I'm ${this.name}`);
      }
    };
    const person2 = Object.create(personProto);
    person2.name = "John";
    ```

29. **What is prototypal inheritance?**
    ```javascript
    function Animal(name) {
      this.name = name;
    }
    Animal.prototype.speak = function() {
      console.log(`${this.name} makes a sound.`);
    };

    function Dog(name) {
      Animal.call(this, name);
    }
    Dog.prototype = Object.create(Animal.prototype);
    Dog.prototype.constructor = Dog;

    const dog = new Dog("Rex");
    dog.speak(); // "Rex makes a sound."
    ```

30. **What is the difference between `Object.freeze()` and `Object.seal()`?**
    ```javascript
    const obj = { prop: 42 };

    // Object.seal()
    Object.seal(obj);
    obj.prop = 33; // Works
    obj.newProp = 33; // Doesn't work

    // Object.freeze()
    Object.freeze(obj);
    obj.prop = 33; // Doesn't work
    obj.newProp = 33; // Doesn't work
    ```

## Arrays and Array Methods

31. **What are the different ways to create an array?**
    ```javascript
    const arr1 = [1, 2, 3];
    const arr2 = new Array(1, 2, 3);
    const arr3 = Array.from("123");
    const arr4 = Array.of(1, 2, 3);
    ```

32. **What is the difference between `map()` and `forEach()`?**
    ```javascript
    const arr = [1, 2, 3];

    // map() returns a new array
    const doubled = arr.map(x => x * 2);
    console.log(doubled); // [2, 4, 6]

    // forEach() doesn't return anything
    arr.forEach(x => console.log(x * 2));
    ```

33. **What is the difference between `filter()` and `find()`?**
    ```javascript
    const arr = [1, 2, 3, 4, 5];

    // filter() returns all matching elements
    const even = arr.filter(x => x % 2 === 0);
    console.log(even); // [2, 4]

    // find() returns the first matching element
    const firstEven = arr.find(x => x % 2 === 0);
    console.log(firstEven); // 2
    ```

34. **What is the difference between `some()` and `every()`?**
    ```javascript
    const arr = [1, 2, 3, 4, 5];

    // some() returns true if any element matches
    console.log(arr.some(x => x > 3)); // true

    // every() returns true if all elements match
    console.log(arr.every(x => x > 3)); // false
    ```

35. **What is the difference between `reduce()` and `reduceRight()`?**
    ```javascript
    const arr = [1, 2, 3, 4];

    // reduce() goes left to right
    console.log(arr.reduce((a, b) => a + b)); // 10

    // reduceRight() goes right to left
    console.log(arr.reduceRight((a, b) => a + b)); // 10
    ```

## Asynchronous JavaScript

36. **What is asynchronous programming?**
    ```javascript
    // Synchronous
    console.log("1");
    console.log("2");
    console.log("3");

    // Asynchronous
    console.log("1");
    setTimeout(() => console.log("2"), 1000);
    console.log("3");
    ```

37. **What is a Promise?**
    ```javascript
    const promise = new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve("Success!");
      }, 1000);
    });

    promise
      .then(result => console.log(result))
      .catch(error => console.error(error));
    ```

38. **What is async/await?**
    ```javascript
    async function fetchData() {
      try {
        const response = await fetch("https://api.example.com/data");
        const data = await response.json();
        return data;
      } catch (error) {
        console.error(error);
      }
    }
    ```

39. **What is the difference between `Promise.all()` and `Promise.race()`?**
    ```javascript
    const promise1 = Promise.resolve(1);
    const promise2 = Promise.resolve(2);
    const promise3 = Promise.resolve(3);

    // Promise.all() waits for all promises to resolve
    Promise.all([promise1, promise2, promise3])
      .then(values => console.log(values)); // [1, 2, 3]

    // Promise.race() returns the first resolved promise
    Promise.race([promise1, promise2, promise3])
      .then(value => console.log(value)); // 1
    ```

40. **What is the event loop?**
    ```javascript
    console.log("1");
    setTimeout(() => console.log("2"), 0);
    Promise.resolve().then(() => console.log("3"));
    console.log("4");
    // Output: 1, 4, 3, 2
    ```

## DOM Manipulation

41. **What is the DOM?**
    ```javascript
    // Accessing elements
    const element = document.getElementById("myId");
    const elements = document.getElementsByClassName("myClass");
    const tagElements = document.getElementsByTagName("div");
    ```

42. **What is the difference between `querySelector()` and `querySelectorAll()`?**
    ```javascript
    // querySelector() returns the first matching element
    const firstElement = document.querySelector(".myClass");

    // querySelectorAll() returns all matching elements
    const allElements = document.querySelectorAll(".myClass");
    ```

43. **How do you create and add elements to the DOM?**
    ```javascript
    // Create element
    const div = document.createElement("div");
    div.textContent = "Hello World";

    // Add to DOM
    document.body.appendChild(div);
    ```

44. **What is event delegation?**
    ```javascript
    document.getElementById("parent").addEventListener("click", (e) => {
      if (e.target.matches(".child")) {
        console.log("Child clicked");
      }
    });
    ```

45. **What is the difference between `innerHTML` and `textContent`?**
    ```javascript
    const div = document.createElement("div");

    // innerHTML parses HTML
    div.innerHTML = "<span>Hello</span>";

    // textContent treats content as text
    div.textContent = "<span>Hello</span>";
    ```

## Error Handling

46. **What is the try-catch block?**
    ```javascript
    try {
      throw new Error("Something went wrong");
    } catch (error) {
      console.error(error.message);
    } finally {
      console.log("Always executed");
    }
    ```

47. **What is the difference between `throw` and `return`?**
    ```javascript
    function example() {
      throw new Error("Error"); // Stops execution
      console.log("Never reached");
    }

    function example2() {
      return "Done"; // Returns value and stops execution
      console.log("Never reached");
    }
    ```

48. **What is the difference between `Error` and `Exception`?**
    ```javascript
    // Error is a built-in object
    throw new Error("This is an error");

    // Exception is a concept, not a specific object
    try {
      // Code that might throw an exception
    } catch (exception) {
      // Handle the exception
    }
    ```

49. **What is the difference between `throw` and `reject`?**
    ```javascript
    // throw in try-catch
    try {
      throw new Error("Error");
    } catch (error) {
      console.error(error);
    }

    // reject in Promise
    new Promise((resolve, reject) => {
      reject(new Error("Error"));
    }).catch(error => console.error(error));
    ```

50. **What is error bubbling?**
    ```javascript
    function level1() {
      try {
        level2();
      } catch (error) {
        console.error("Caught in level1:", error);
      }
    }

    function level2() {
      level3();
    }

    function level3() {
      throw new Error("Error in level3");
    }
    ```

## ES6+ Features

51. **What are template literals?**
    ```javascript
    const name = "John";
    const greeting = `Hello, ${name}!`;
    ```

52. **What is the spread operator?**
    ```javascript
    const arr1 = [1, 2, 3];
    const arr2 = [...arr1, 4, 5];
    const obj1 = { foo: "bar" };
    const obj2 = { ...obj1, baz: "qux" };
    ```

53. **What is the rest parameter?**
    ```javascript
    function sum(...numbers) {
      return numbers.reduce((total, num) => total + num, 0);
    }
    console.log(sum(1, 2, 3, 4)); // 10
    ```

54. **What is destructuring?**
    ```javascript
    // Array destructuring
    const [a, b, ...rest] = [1, 2, 3, 4];
    console.log(a, b, rest); // 1, 2, [3, 4]

    // Object destructuring
    const { name, age } = { name: "John", age: 30 };
    console.log(name, age); // "John", 30
    ```

55. **What are default parameters?**
    ```javascript
    function greet(name = "Guest") {
      console.log(`Hello, ${name}!`);
    }
    greet(); // "Hello, Guest!"
    greet("John"); // "Hello, John!"
    ```

## Design Patterns

56. **What is the Singleton pattern?**
    ```javascript
    class Singleton {
      static instance;
      
      constructor() {
        if (Singleton.instance) {
          return Singleton.instance;
        }
        Singleton.instance = this;
      }
    }
    ```

57. **What is the Factory pattern?**
    ```javascript
    class Car {
      constructor(type) {
        this.type = type;
      }
    }

    class CarFactory {
      createCar(type) {
        return new Car(type);
      }
    }
    ```

58. **What is the Observer pattern?**
    ```javascript
    class Subject {
      constructor() {
        this.observers = [];
      }

      subscribe(observer) {
        this.observers.push(observer);
      }

      notify(data) {
        this.observers.forEach(observer => observer.update(data));
      }
    }
    ```

59. **What is the Module pattern?**
    ```javascript
    const Module = (function() {
      let private = "private";
      
      return {
        public: "public",
        getPrivate() {
          return private;
        }
      };
    })();
    ```

60. **What is the Prototype pattern?**
    ```javascript
    const prototype = {
      greet() {
        console.log(`Hello, ${this.name}!`);
      }
    };

    const object = Object.create(prototype);
    object.name = "John";
    object.greet(); // "Hello, John!"
    ```

## Testing and Debugging

61. **What is unit testing?**
    ```javascript
    // Using Jest
    test("adds 1 + 2 to equal 3", () => {
      expect(sum(1, 2)).toBe(3);
    });
    ```

62. **What is integration testing?**
    ```javascript
    // Testing API integration
    test("fetches user data", async () => {
      const user = await fetchUser(1);
      expect(user.name).toBe("John");
    });
    ```

63. **What is the difference between `console.log()` and `console.error()`?**
    ```javascript
    console.log("Info message");
    console.error("Error message");
    ```

64. **What is the difference between `console.warn()` and `console.error()`?**
    ```javascript
    console.warn("Warning message");
    console.error("Error message");
    ```

65. **What is the difference between `console.trace()` and `console.stack()`?**
    ```javascript
    function trace() {
      console.trace("Trace message");
    }
    trace();
    ```

## Performance Optimization

66. **What is memoization?**
    ```javascript
    function memoize(fn) {
      const cache = new Map();
      return function(...args) {
        const key = JSON.stringify(args);
        if (cache.has(key)) return cache.get(key);
        const result = fn.apply(this, args);
        cache.set(key, result);
        return result;
      };
    }
    ```

67. **What is debouncing?**
    ```javascript
    function debounce(fn, delay) {
      let timeoutId;
      return function(...args) {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => fn.apply(this, args), delay);
      };
    }
    ```

68. **What is throttling?**
    ```javascript
    function throttle(fn, delay) {
      let lastCall = 0;
      return function(...args) {
        const now = Date.now();
        if (now - lastCall >= delay) {
          lastCall = now;
          fn.apply(this, args);
        }
      };
    }
    ```

69. **What is lazy loading?**
    ```javascript
    // Lazy load images
    const images = document.querySelectorAll("img[data-src]");
    const imageObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.src = img.dataset.src;
          observer.unobserve(img);
        }
      });
    });
    ```

70. **What is code splitting?**
    ```javascript
    // Using dynamic import
    const module = await import("./module.js");
    ```

## Security

71. **What is XSS?**
    ```javascript
    // Vulnerable to XSS
    element.innerHTML = userInput;

    // Safe
    element.textContent = userInput;
    ```

72. **What is CSRF?**
    ```javascript
    // Adding CSRF token to requests
    fetch("/api/data", {
      headers: {
        "X-CSRF-Token": csrfToken
      }
    });
    ```

73. **What is CORS?**
    ```javascript
    // Server-side CORS configuration
    app.use(cors({
      origin: "https://example.com",
      methods: ["GET", "POST"]
    }));
    ```

74. **What is Content Security Policy?**
    ```html
    <meta http-equiv="Content-Security-Policy" 
          content="default-src 'self'; script-src 'self' 'unsafe-inline'">
    ```

75. **What is Same-Origin Policy?**
    ```javascript
    // Same origin
    fetch("https://example.com/api/data");

    // Different origin
    fetch("https://api.example.com/data");
    ```

## Advanced Topics

76. **What is the difference between `setTimeout()` and `setInterval()`?**
    ```javascript
    // setTimeout() runs once
    setTimeout(() => console.log("Hello"), 1000);

    // setInterval() runs repeatedly
    setInterval(() => console.log("Hello"), 1000);
    ```

77. **What is the difference between `localStorage` and `sessionStorage`?**
    ```javascript
    // localStorage persists until cleared
    localStorage.setItem("key", "value");

    // sessionStorage persists until tab is closed
    sessionStorage.setItem("key", "value");
    ```

78. **What is the difference between `JSON.stringify()` and `JSON.parse()`?**
    ```javascript
    const obj = { name: "John" };
    const str = JSON.stringify(obj);
    const parsed = JSON.parse(str);
    ```

79. **What is the difference between `encodeURI()` and `encodeURIComponent()`?**
    ```javascript
    const url = "https://example.com/path?name=John Doe";
    console.log(encodeURI(url));
    console.log(encodeURIComponent(url));
    ```

80. **What is the difference between `parseInt()` and `parseFloat()`?**
    ```javascript
    console.log(parseInt("123.45")); // 123
    console.log(parseFloat("123.45")); // 123.45
    ```

## Web APIs

81. **What is the Fetch API?**
    ```javascript
    fetch("https://api.example.com/data")
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error(error));
    ```

82. **What is the Web Storage API?**
    ```javascript
    // localStorage
    localStorage.setItem("key", "value");
    const value = localStorage.getItem("key");

    // sessionStorage
    sessionStorage.setItem("key", "value");
    const value2 = sessionStorage.getItem("key");
    ```

83. **What is the Geolocation API?**
    ```javascript
    navigator.geolocation.getCurrentPosition(
      position => console.log(position.coords),
      error => console.error(error)
    );
    ```

84. **What is the Web Workers API?**
    ```javascript
    const worker = new Worker("worker.js");
    worker.postMessage("Hello");
    worker.onmessage = event => console.log(event.data);
    ```

85. **What is the WebSocket API?**
    ```javascript
    const ws = new WebSocket("wss://example.com");
    ws.onmessage = event => console.log(event.data);
    ws.send("Hello");
    ```

## Modern JavaScript Features

86. **What are private class fields?**
    ```javascript
    class Person {
      #privateField = "private";
      static #privateStaticField = "private static";
    }
    ```

87. **What is the `at()` method?**
    ```javascript
    const arr = [1, 2, 3];
    console.log(arr.at(-1)); // 3
    ```

88. **What is the `Object.hasOwn()` method?**
    ```javascript
    const obj = { prop: "value" };
    console.log(Object.hasOwn(obj, "prop")); // true
    ```

89. **What is the `Error.cause` property?**
    ```javascript
    throw new Error("Error", { cause: "Original error" });
    ```

90. **What is the `Array.prototype.toSorted()` method?**
    ```javascript
    const arr = [3, 1, 2];
    const sorted = arr.toSorted();
    console.log(arr); // [3, 1, 2]
    console.log(sorted); // [1, 2, 3]
    ```

## Best Practices

91. **What is the difference between `const` and `let`?**
    ```javascript
    const PI = 3.14; // Cannot be reassigned
    let radius = 5;  // Can be reassigned
    ```

92. **What is the difference between `==` and `===`?**
    ```javascript
    console.log(1 == "1");  // true
    console.log(1 === "1"); // false
    ```

93. **What is the difference between `function` and `arrow function`?**
    ```javascript
    function regular() {
      console.log(this);
    }

    const arrow = () => {
      console.log(this);
    };
    ```

94. **What is the difference between `var` and `let`?**
    ```javascript
    {
      var x = 1; // Function scoped
      let y = 2; // Block scoped
    }
    console.log(x); // 1
    console.log(y); // ReferenceError
    ```

95. **What is the difference between `null` and `undefined`?**
    ```javascript
    let a; // undefined
    let b = null; // null
    ```

## Common Interview Questions

96. **What is hoisting?**
    ```javascript
    console.log(x); // undefined
    var x = 5;
    ```

97. **What is closure?**
    ```javascript
    function outer() {
      const x = 10;
      return function inner() {
        console.log(x);
      };
    }
    ```

98. **What is the difference between `call()`, `apply()`, and `bind()`?**
    ```javascript
    const obj = { value: 42 };

    function getValue() {
      return this.value;
    }

    getValue.call(obj);
    getValue.apply(obj);
    const bound = getValue.bind(obj);
    ```

99. **What is the difference between `setTimeout()` and `requestAnimationFrame()`?**
    ```javascript
    setTimeout(() => {
      // Code
    }, 1000);

    requestAnimationFrame(() => {
      // Code
    });
    ```

100. **What is the difference between `Promise` and `async/await`?**
    ```javascript
    // Promise
    fetchData()
      .then(data => console.log(data))
      .catch(error => console.error(error));

    // async/await
    async function getData() {
      try {
        const data = await fetchData();
        console.log(data);
      } catch (error) {
        console.error(error);
      }
    }
    ```

## Advanced Concepts

101. **What is the difference between `WeakMap` and `Map`?**
    ```javascript
    const map = new Map();
    const weakMap = new WeakMap();
    ```

102. **What is the difference between `WeakSet` and `Set`?**
    ```javascript
    const set = new Set();
    const weakSet = new WeakSet();
    ```

103. **What is the difference between `Symbol` and `String`?**
    ```javascript
    const sym = Symbol("description");
    const str = "description";
    ```

104. **What is the difference between `BigInt` and `Number`?**
    ```javascript
    const big = 9007199254740991n;
    const num = 9007199254740991;
    ```

105. **What is the difference between `Proxy` and `Object.defineProperty()`?**
    ```javascript
    const proxy = new Proxy(target, handler);
    Object.defineProperty(obj, "prop", descriptor);
    ```

## Performance (continued)

106. **What is the difference between `for` and `forEach` for arrays?**
    ```javascript
    const arr = [1, 2, 3];
    // for loop
    for (let i = 0; i < arr.length; i++) {
      console.log(arr[i]);
    }
    // forEach
    arr.forEach(item => console.log(item));
    // for is faster and can be broken with break/continue; forEach cannot.
    ```

107. **How do you deep clone an object?**
    ```javascript
    const obj = { a: 1, b: { c: 2 } };
    // Using JSON
    const clone = JSON.parse(JSON.stringify(obj));
    // Using structuredClone (modern)
    const clone2 = structuredClone(obj);
    ```

108. **What is tail call optimization?**
    ```javascript
    // Not all JS engines support it
    function factorial(n, acc = 1) {
      if (n <= 1) return acc;
      return factorial(n - 1, n * acc); // Tail call
    }
    ```

109. **How do you debounce a function?**
    ```javascript
    function debounce(fn, delay) {
      let timer;
      return function(...args) {
        clearTimeout(timer);
        timer = setTimeout(() => fn.apply(this, args), delay);
      };
    }
    ```

110. **How do you throttle a function?**
    ```javascript
    function throttle(fn, limit) {
      let inThrottle;
      return function(...args) {
        if (!inThrottle) {
          fn.apply(this, args);
          inThrottle = true;
          setTimeout(() => inThrottle = false, limit);
        }
      };
    }
    ```

111. **What is a memory leak and how can you prevent it?**
    - A memory leak is when memory that is no longer needed is not released. Prevent by removing event listeners, clearing timers, and dereferencing objects.

112. **How do you measure performance in JavaScript?**
    ```javascript
    const start = performance.now();
    // code
    const end = performance.now();
    console.log(`Time: ${end - start}ms`);
    ```

113. **What is the purpose of the `requestIdleCallback` API?**
    ```javascript
    requestIdleCallback(() => {
      // Perform background or low-priority work
    });
    ```

114. **How do you optimize DOM manipulation?**
    - Minimize reflows/repaints, use DocumentFragment, batch updates, and avoid layout thrashing.

115. **What is event delegation and why is it useful?**
    - Attach a single event listener to a parent instead of many children. Useful for dynamic lists.

## Patterns & Architecture

116. **What is the Observer pattern?**
    ```javascript
    class Subject {
      constructor() { this.observers = []; }
      subscribe(fn) { this.observers.push(fn); }
      notify(data) { this.observers.forEach(fn => fn(data)); }
    }
    ```

117. **What is the Module pattern?**
    ```javascript
    const Counter = (function() {
      let count = 0;
      return {
        increment() { count++; },
        getCount() { return count; }
      };
    })();
    ```

118. **What is the Revealing Module pattern?**
    ```javascript
    const MyModule = (function() {
      let privateVar = 0;
      function privateFn() { return ++privateVar; }
      return { publicFn: privateFn };
    })();
    ```

119. **What is the Factory pattern?**
    ```javascript
    function Car(type) { this.type = type; }
    function carFactory(type) { return new Car(type); }
    ```

120. **What is the Command pattern?**
    ```javascript
    class Command {
      execute() {}
    }
    class LightOnCommand extends Command {
      execute() { console.log('Light on'); }
    }
    ```

121. **What is the Proxy pattern?**
    ```javascript
    const target = { message: "Hello" };
    const handler = {
      get(obj, prop) { return prop in obj ? obj[prop] : "Not found"; }
    };
    const proxy = new Proxy(target, handler);
    ```

122. **What is the Decorator pattern?**
    ```javascript
    function addTimestamp(obj) {
      obj.timestamp = Date.now();
      return obj;
    }
    ```

123. **What is the Strategy pattern?**
    ```javascript
    function log(strategy) { strategy(); }
    log(() => console.log("Info"));
    ```

124. **What is the Chain of Responsibility pattern?**
    - Passes a request along a chain of handlers until one handles it.

125. **What is the Mediator pattern?**
    - Centralizes complex communications and control between related objects.

## Testing & Tooling

126. **What is Jest?**
    - A JavaScript testing framework for unit and integration tests.

127. **What is Mocha?**
    - A feature-rich JavaScript test framework running on Node.js.

128. **What is Chai?**
    - An assertion library for Node and browsers that can be paired with any JS testing framework.

129. **What is Sinon?**
    - A library for spies, stubs, and mocks in JavaScript.

130. **What is a mock function?**
    - A function used in testing to simulate the behavior of real functions.

131. **How do you test asynchronous code in JavaScript?**
    ```javascript
    test('async test', async () => {
      const data = await fetchData();
      expect(data).toBeDefined();
    });
    ```

132. **What is code coverage?**
    - A measure of how much code is tested by automated tests.

133. **What is TDD (Test Driven Development)?**
    - Write tests before code, then write code to pass the tests.

134. **What is BDD (Behavior Driven Development)?**
    - Write tests in a natural language style that non-programmers can read.

135. **What is snapshot testing?**
    - Testing that the output of a function/component matches a saved snapshot.

## Node.js & Backend

136. **What is Node.js?**
    - A runtime environment for executing JavaScript outside the browser.

137. **What is npm?**
    - Node Package Manager, used to install and manage packages.

138. **What is the difference between `require` and `import`?**
    - `require` is CommonJS, `import` is ES6 modules.

139. **What is the event loop in Node.js?**
    - Handles asynchronous callbacks in Node.js.

140. **What is a stream in Node.js?**
    - An abstract interface for working with streaming data.

141. **What is middleware in Express.js?**
    - Functions that execute during the request-response cycle.

142. **How do you handle file uploads in Node.js?**
    - Use packages like `multer` for handling multipart/form-data.

143. **What is process.env?**
    - An object containing the user environment.

144. **How do you read a file in Node.js?**
    ```javascript
    const fs = require('fs');
    fs.readFile('file.txt', 'utf8', (err, data) => {
      if (err) throw err;
      console.log(data);
    });
    ```

145. **How do you write a file in Node.js?**
    ```javascript
    const fs = require('fs');
    fs.writeFile('file.txt', 'Hello', err => {
      if (err) throw err;
    });
    ```

## TypeScript & Supersets

146. **What is TypeScript?**
    - A superset of JavaScript that adds static typing.

147. **What are interfaces in TypeScript?**
    ```typescript
    interface Person { name: string; age: number; }
    ```

148. **What are generics in TypeScript?**
    ```typescript
    function identity<T>(arg: T): T { return arg; }
    ```

149. **What is type inference?**
    - The compiler automatically infers the type of a variable.

150. **What is a union type?**
    ```typescript
    let value: string | number;
    ```

## Functional Programming

151. **What is a pure function?**
    - A function with no side effects and returns the same output for the same input.

152. **What is immutability?**
    - Data cannot be changed after it is created.

153. **What is a higher-order function?**
    - A function that takes another function as an argument or returns a function.

154. **What is function composition?**
    - Combining two or more functions to produce a new function.

155. **What is a monad?**
    - A design pattern used to handle program-wide concerns like state or I/O.

## Miscellaneous & Practical

156. **How do you check if a variable is an array?**
    ```javascript
    Array.isArray(arr);
    ```

157. **How do you check if a property exists in an object?**
    ```javascript
    'prop' in obj;
    obj.hasOwnProperty('prop');
    ```

158. **How do you merge two objects?**
    ```javascript
    const merged = { ...obj1, ...obj2 };
    Object.assign({}, obj1, obj2);
    ```

159. **How do you remove duplicates from an array?**
    ```javascript
    const unique = [...new Set(arr)];
    ```

160. **How do you flatten an array?**
    ```javascript
    const flat = arr.flat(Infinity);
    ```

161. **How do you shuffle an array?**
    ```javascript
    arr.sort(() => Math.random() - 0.5);
    ```

162. **How do you get the max/min value in an array?**
    ```javascript
    Math.max(...arr);
    Math.min(...arr);
    ```

163. **How do you reverse a string?**
    ```javascript
    str.split('').reverse().join('');
    ```

164. **How do you capitalize the first letter of a string?**
    ```javascript
    str.charAt(0).toUpperCase() + str.slice(1);
    ```

165. **How do you check if a string contains a substring?**
    ```javascript
    str.includes('sub');
    ```

166. **How do you pad a string?**
    ```javascript
    str.padStart(5, '0');
    str.padEnd(5, '0');
    ```

167. **How do you repeat a string?**
    ```javascript
    str.repeat(3);
    ```

168. **How do you trim whitespace from a string?**
    ```javascript
    str.trim();
    str.trimStart();
    str.trimEnd();
    ```

169. **How do you convert a string to a number?**
    ```javascript
    Number(str);
    parseInt(str);
    parseFloat(str);
    +str;
    ```

170. **How do you convert a number to a string?**
    ```javascript
    num.toString();
    String(num);
    ```

171. **How do you format a number as currency?**
    ```javascript
    num.toLocaleString('en-US', { style: 'currency', currency: 'USD' });
    ```

172. **How do you get the current date and time?**
    ```javascript
    new Date();
    Date.now();
    ```

173. **How do you format a date?**
    ```javascript
    date.toLocaleDateString();
    date.toISOString();
    ```

174. **How do you get a random number between two values?**
    ```javascript
    Math.random() * (max - min) + min;
    ```

175. **How do you generate a random integer?**
    ```javascript
    Math.floor(Math.random() * (max - min + 1)) + min;
    ```

176. **How do you debounce an input event?**
    ```javascript
    input.addEventListener('input', debounce(fn, 300));
    ```

177. **How do you copy text to the clipboard?**
    ```javascript
    navigator.clipboard.writeText('text');
    ```

178. **How do you detect the user's browser?**
    ```javascript
    navigator.userAgent;
    ```

179. **How do you detect if the user is on a mobile device?**
    ```javascript
    /Mobi|Android/i.test(navigator.userAgent);
    ```

180. **How do you check if an object is empty?**
    ```javascript
    Object.keys(obj).length === 0;
    ```

181. **How do you clone an array?**
    ```javascript
    arr.slice();
    [...arr];
    Array.from(arr);
    ```

182. **How do you get unique values from an array of objects by key?**
    ```javascript
    const unique = [...new Map(arr.map(item => [item.key, item])).values()];
    ```

183. **How do you sort an array of objects by a property?**
    ```javascript
    arr.sort((a, b) => a.prop - b.prop);
    ```

184. **How do you merge two arrays?**
    ```javascript
    arr1.concat(arr2);
    [...arr1, ...arr2];
    ```

185. **How do you remove falsy values from an array?**
    ```javascript
    arr.filter(Boolean);
    ```

186. **How do you check if two arrays are equal?**
    ```javascript
    arr1.length === arr2.length && arr1.every((v, i) => v === arr2[i]);
    ```

187. **How do you get the intersection of two arrays?**
    ```javascript
    arr1.filter(x => arr2.includes(x));
    ```

188. **How do you get the difference of two arrays?**
    ```javascript
    arr1.filter(x => !arr2.includes(x));
    ```

189. **How do you get the union of two arrays?**
    ```javascript
    [...new Set([...arr1, ...arr2])];
    ```

190. **How do you check if an array contains a value?**
    ```javascript
    arr.includes(value);
    ```

191. **How do you find the index of an element in an array?**
    ```javascript
    arr.indexOf(value);
    arr.findIndex(fn);
    ```

192. **How do you remove an element from an array by value?**
    ```javascript
    arr = arr.filter(x => x !== value);
    ```

193. **How do you remove an element from an array by index?**
    ```javascript
    arr.splice(index, 1);
    ```

194. **How do you empty an array?**
    ```javascript
    arr.length = 0;
    ```

195. **How do you check if a function is asynchronous?**
    ```javascript
    function isAsync(fn) { return fn.constructor.name === 'AsyncFunction'; }
    ```

196. **How do you convert a callback to a Promise?**
    ```javascript
    function promisify(fn) {
      return (...args) => new Promise((resolve, reject) => {
        fn(...args, (err, result) => err ? reject(err) : resolve(result));
      });
    }
    ```

197. **How do you handle uncaught exceptions in Node.js?**
    ```javascript
    process.on('uncaughtException', err => { console.error(err); });
    ```

198. **How do you handle unhandled promise rejections?**
    ```javascript
    process.on('unhandledRejection', err => { console.error(err); });
    ```

199. **How do you make an HTTP request in JavaScript?**
    ```javascript
    fetch('https://api.example.com').then(res => res.json()).then(data => console.log(data));
    ```

200. **How do you implement a simple event emitter?**
    ```javascript
    class EventEmitter {
      constructor() { this.events = {}; }
      on(event, listener) {
        (this.events[event] = this.events[event] || []).push(listener);
      }
      emit(event, ...args) {
        (this.events[event] || []).forEach(fn => fn(...args));
      }
    }
    ```

201. **What is event bubbling and event capturing in the DOM?**
    ```javascript
    // Bubbling: event propagates from child to parent
    element.addEventListener('click', handler, false); // default is bubbling

    // Capturing: event propagates from parent to child
    element.addEventListener('click', handler, true);
    ```

202. **What are WeakRefs and FinalizationRegistry?**
    ```javascript
    const obj = {};
    const weakRef = new WeakRef(obj);
    // FinalizationRegistry lets you run cleanup after GC
    const registry = new FinalizationRegistry((heldValue) => {
      console.log('Object was garbage collected:', heldValue);
    });
    registry.register(obj, 'myObject');
    ```

203. **Explain the difference between microtasks and macrotasks.**
    - Microtasks: `Promise.then`, `MutationObserver`
    - Macrotasks: `setTimeout`, `setInterval`, `setImmediate`
    ```javascript
    console.log('start');
    setTimeout(() => console.log('timeout'), 0);
    Promise.resolve().then(() => console.log('promise'));
    console.log('end');
    // Output: start, end, promise, timeout
    ```

204. **What is a Service Worker and how is it used?**
    ```javascript
    // Registering a service worker
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.register('/sw.js');
    }
    ```

205. **What is the difference between interface and type in TypeScript?**
    ```typescript
    interface A { x: number; }
    type B = { x: number; };
    // Interfaces can be extended/merged, types cannot (as easily)
    ```

206. **What is type narrowing in TypeScript?**
    ```typescript
    function printId(id: string | number) {
      if (typeof id === 'string') {
        // id is string here
      } else {
        // id is number here
      }
    }
    ```

207. **What are mapped types in TypeScript?**
    ```typescript
    type Readonly<T> = { readonly [P in keyof T]: T[P] };
    ```

208. **What is the difference between `unknown` and `any` in TypeScript?**
    - `unknown` is safer; you must check type before using.
    - `any` disables all type checking.

209. **What is a discriminated union in TypeScript?**
    ```typescript
    type Shape = { kind: 'circle', radius: number } | { kind: 'square', size: number };
    function area(shape: Shape) {
      if (shape.kind === 'circle') return Math.PI * shape.radius ** 2;
      return shape.size ** 2;
    }
    ```

210. **What is the difference between shallow and deep copy?**
    - Shallow copy: only top-level properties are copied.
    - Deep copy: all nested objects are recursively copied.

211. **What is the difference between `Object.freeze` and `const`?**
    - `const` prevents reassignment of the variable.
    - `Object.freeze` makes the object immutable (shallow).

212. **What is the difference between `setTimeout(fn, 0)` and `Promise.resolve().then(fn)`?**
    - `setTimeout` schedules a macrotask, `Promise.then` schedules a microtask (runs sooner).

213. **What is the difference between `export default` and `export` in ES modules?**
    ```javascript
    // export default: only one per file, imported without braces
    // export: named exports, imported with braces
    ```

214. **What is tree shaking?**
    - The process of removing unused code during bundling (e.g., with Webpack, Rollup).

215. **What is the difference between `Object.assign` and spread operator?**
    - Both copy properties, but spread can copy symbol properties and is more concise.

216. **What is the difference between `==` and `Object.is`?**
    ```javascript
    Object.is(NaN, NaN); // true
    NaN === NaN; // false
    ```

217. **What is the difference between `Array.prototype.find` and `Array.prototype.filter`?**
    - `find` returns the first matching element, `filter` returns all matching elements.

218. **What is the difference between `Array.prototype.map` and `Array.prototype.flatMap`?**
    ```javascript
    [1, 2, 3].map(x => [x, x * 2]); // [[1,2],[2,4],[3,6]]
    [1, 2, 3].flatMap(x => [x, x * 2]); // [1,2,2,4,3,6]
    ```

219. **What is the difference between `let`, `const`, and `var` in terms of hoisting?**
    - `var` is hoisted and initialized as `undefined`.
    - `let` and `const` are hoisted but not initialized (temporal dead zone).

220. **What is the difference between `Function.prototype.call`, `apply`, and `bind`?**
    - `call`: calls a function with a given `this` and arguments.
    - `apply`: same as `call`, but arguments are provided as an array.
    - `bind`: returns a new function with bound `this`.