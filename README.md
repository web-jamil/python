JavaScrip Cheatsheet 


Here is a more comprehensive guide to JavaScript, including advanced topics, detailed examples, and syntaxes. It's divided into categories for easier navigation.


# **1. JavaScript Basics**
### Declaring Variables
 **`let`**: Block-scoped (preferred for mutable variables).
 **`const`**: Block-scoped, immutable.
 **`var`**: Function-scoped (use is discouraged).

```javascript
let a = 10;
const b = 20;
var c = 30;
```

### Data Types
1. **Primitive**: `string`, `number`, `boolean`, `undefined`, `null`, `symbol`, `bigint`.
2. **Non-Primitive**: Objects, arrays, functions.

---

# **2. Operators**
### Arithmetic Operators
```javascript
let x = 10, y = 3;
console.log(x + y); // 13
console.log(x - y); // 7
console.log(x * y); // 30
console.log(x / y); // 3.33
console.log(x % y); // 1
console.log(x ** y); // 1000

### Logical Operators
- `&&`: Logical AND
- `||`: Logical OR
- `!`: Logical NOT

```javascript
console.log(true && false); // false
console.log(true || false); // true
console.log(!true);         // false
```

---

# **3. Control Flow**
### If-Else Statements
```javascript
let age = 20;

if (age >= 18) {
  console.log("Adult");
} else {
  console.log("Minor");
}
```

### Switch Statement
```javascript
let day = "Monday";

switch (day) {
  case "Monday":
    console.log("Start of the week");
    break;
  case "Friday":
    console.log("Weekend is near");
    break;
  default:
    console.log("Regular day");
}
```


# **4. Loops**
### For Loop
```javascript
for (let i = 0; i < 5; i++) {
  console.log(i);
}
```

### While Loop
```javascript
let count = 0;
while (count < 5) {
  console.log(count);
  count++;
}
```

### Do-While Loop
```javascript
let count = 0;
do {
  console.log(count);
  count++;
} while (count < 5);
```

### Iteration (For...of and For...in)
```javascript
let arr = [10, 20, 30];
for (let value of arr) {
  console.log(value); // 10, 20, 30
}

let obj = { name: "Alice", age: 25 };
for (let key in obj) {
  console.log(key, obj[key]); // name: Alice, age: 25
}
```

---

# **5. Functions**
### Function Declaration
```javascript
function add(a, b) {
  return a + b;
}
console.log(add(5, 10)); // 15
```

### Function Expression
```javascript
const multiply = function (a, b) {
  return a * b;
};
console.log(multiply(5, 10)); // 50
```

### Arrow Functions
```javascript
const greet = (name) => `Hello, ${name}!`;
console.log(greet("Alice"));
```

### Default Parameters
```javascript
function greet(name = "Guest") {
  return `Hello, ${name}!`;
}
```


6. Arrays
### Creating Arrays
```javascript
let arr = [1, 2, 3, 4];
```

### Array Methods
- `push()`: Add to the end.
- `pop()`: Remove last element.
- `shift()`: Remove first element.
- `unshift()`: Add to the start.
- `splice()`: Add/remove elements.
- `slice()`: Extract subarray.

```javascript
let arr = [1, 2, 3];
arr.push(4);         // [1, 2, 3, 4]
arr.pop();           // [1, 2, 3]
let subArr = arr.slice(0, 2); // [1, 2]
```

### Higher-Order Methods
```javascript
let arr = [1, 2, 3];

arr.forEach((val) => console.log(val)); // Iterates through the array
let doubled = arr.map((val) => val * 2); // [2, 4, 6]
let even = arr.filter((val) => val % 2 === 0); // [2]
let total = arr.reduce((sum, val) => sum + val, 0); // 6
```


# **7. Objects**
### Creating Objects
```javascript
let person = {
  name: "Alice",
  age: 25,
  greet() {
    console.log(`Hello, my name is ${this.name}`);
  },
};

### Destructuring Objects
```javascript
let { name, age } = person;
console.log(name, age);
```


# **8. Classes**
### Class Declaration
```javascript
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log(`Hello, my name is ${this.name}`);
  }
}

let alice = new Person("Alice", 25);
alice.greet();
```

# **9. Promises and Async**
### Promises
```javascript
let promise = new Promise((resolve, reject) => {
  let success = true;
  if (success) resolve("Success!");
  else reject("Error!");
});

promise
  .then((message) => console.log(message))
  .catch((error) => console.error(error));
```

### Async/Await
```javascript
async function fetchData() {
  try {
    let response = await fetch("https://api.example.com/data");
    let data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}
```


# **10. DOM Manipulation**
### Selecting Elements
```javascript
let element = document.getElementById("myElement");
let elements = document.querySelectorAll(".myClass");
```

### Modifying Elements
```javascript
element.textContent = "New Text";
element.style.color = "blue";
```

### Event Handling
```javascript
element.addEventListener("click", () => {
  console.log("Element clicked!");
});
```


# **11. ES6+ Features**
### Spread and Rest Operators
```javascript
let arr = [1, 2, 3];
let newArr = [...arr, 4]; // [1, 2, 3, 4]

function sum(...nums) {
  return nums.reduce((total, n) => total + n);
}
console.log(sum(1, 2, 3)); // 6
```

### Modules
**Export**
```javascript
export const greet = (name) => `Hello, ${name}`;
```

**Import**
```javascript
import { greet } from "./module.js";
```

# **12. Advanced Topics**
### Closures
```javascript
function outerFunction(outerVar) {
  return function innerFunction(innerVar) {
    console.log(`Outer: ${outerVar}, Inner: ${innerVar}`);
  };
}

let closure = outerFunction("outside");
closure("inside");
```

### Async Iteration
```javascript
async function* asyncGenerator() {
  yield "First";
  yield "Second";
}

for await (let value of asyncGenerator()) {
  console.log(value);
}
```

### Error Handling
```javascript
try {
  throw new Error("Something went wrong!");
} catch (error) {
  console.error(error.message);
}
```

## **1. Closures**
A closure is when a function "remembers" the variables from its lexical scope even when it is executed outside that scope.

```javascript
function outerFunction(outerVar) {
  return function innerFunction(innerVar) {
    console.log(`Outer: ${outerVar}, Inner: ${innerVar}`);
  };
}

const closure = outerFunction("outside");
closure("inside"); // Output: Outer: outside, Inner: inside
```

**Use Cases:**
- Data hiding
- Function factories
- Maintaining state in asynchronous operations

---

## **2. Prototypal Inheritance**
Objects in JavaScript can inherit from other objects via the prototype chain.

```javascript
function Person(name) {
  this.name = name;
}

Person.prototype.greet = function () {
  console.log(`Hello, my name is ${this.name}`);
};

const alice = new Person("Alice");
alice.greet(); // Output: Hello, my name is Alice
```

**Modern Approach:**
Using `class` syntax for inheritance.
```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    console.log(`${this.name} makes a noise.`);
  }
}

class Dog extends Animal {
  speak() {
    console.log(`${this.name} barks.`);
  }
}

const dog = new Dog("Rex");
dog.speak(); // Rex barks.
```

---

## **3. Currying**
Transforming a function that takes multiple arguments into a series of functions that each take one argument.

```javascript
function add(a) {
  return function (b) {
    return function (c) {
      return a + b + c;
    };
  };
}

console.log(add(1)(2)(3)); // Output: 6
```

**Use Cases:**
1.Function composition
2. Delayed execution
3.Partial application


## **4. Event Loop & Asynchronous JavaScript**
JavaScript uses a single-threaded event loop to handle asynchronous operations like `setTimeout`, `fetch`, or promises.

```javascript
console.log("Start");

setTimeout(() => console.log("Timeout"), 0);

Promise.resolve().then(() => console.log("Promise"));

console.log("End");

// Output:
// Start
// End
// Promise
// Timeout
```

**Key Concepts:**
- Call Stack
- Web APIs (like `setTimeout`)
- Task Queue (Macrotasks)
- Microtasks (Promises, Mutation Observers)


## **5. Higher-Order Functions**
Functions that accept other functions as arguments or return a function.

```javascript
function withLogging(fn) {
  return function (...args) {
    console.log(`Calling function with args: ${args}`);
    return fn(...args);
  };
}

const add = (a, b) => a + b;
const loggedAdd = withLogging(add);

console.log(loggedAdd(2, 3)); // Logs args, then Output: 5
```

**Common Examples:**
- `map()`, `filter()`, `reduce()` in arrays.

---

## **6. Async/Await and Promises**
### Promises
```javascript
const fetchData = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => resolve("Data fetched!"), 1000);
  });
};

fetchData()
  .then((data) => console.log(data))
  .catch((error) => console.error(error));
```

### Async/Await
```javascript
async function fetchData() {
  try {
    const data = await fetch("https://api.example.com/data");
    const json = await data.json();
    console.log(json);
  } catch (error) {
    console.error(error);
  }
}
fetchData();
```


## **7. Module System**
### ES6 Modules
**Exporting**
```javascript
export const greet = (name) => `Hello, ${name}`;
```

**Importing**
```javascript
import { greet } from './module.js';
console.log(greet("Alice"));
```

### CommonJS (Node.js)
```javascript
// Export
module.exports = {
  greet: (name) => `Hello, ${name}`,
};

// Import
const { greet } = require('./module');
console.log(greet("Alice"));
```


## **8. Debouncing and Throttling**
### Debouncing
Ensures a function runs only after a certain period of inactivity.

```javascript
function debounce(fn, delay) {
  let timeout;
  return function (...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => fn(...args), delay);
  };
}

const debouncedFunction = debounce(() => console.log("Debounced!"), 300);
window.addEventListener("resize", debouncedFunction);
```

### Throttling
Ensures a function runs at most once in a specified time interval.

```javascript
function throttle(fn, limit) {
  let lastCall = 0;
  return function (...args) {
    const now = Date.now();
    if (now - lastCall >= limit) {
      lastCall = now;
      fn(...args);
    }
  };
}

const throttledFunction = throttle(() => console.log("Throttled!"), 300);
window.addEventListener("scroll", throttledFunction);
```

## **9. Generators**
A generator is a special function that can pause and resume its execution.

```javascript
function* numberGenerator() {
  yield 1;
  yield 2;
  yield 3;
}

const gen = numberGenerator();
console.log(gen.next().value); // 1
console.log(gen.next().value); // 2
console.log(gen.next().value); // 3
```

**Use Case:** Infinite sequences, asynchronous iterations.

---

## **10. Proxy**
Intercepts and customizes operations on objects.

```javascript
const person = { name: "Alice", age: 25 };

const proxy = new Proxy(person, {
  get(target, prop) {
    return prop in target ? target[prop] : "Property not found";
  },
  set(target, prop, value) {
    if (prop === "age" && typeof value !== "number") {
      throw new TypeError("Age must be a number");
    }
    target[prop] = value;
    return true;
  },
});

console.log(proxy.name); // Alice
console.log(proxy.gender); // Property not found
proxy.age = 30; // Works
proxy.age = "thirty"; // Throws TypeError
```


## **11. Memory Management**
JavaScript has automatic garbage collection but understanding memory allocation and leaks is important.

### Common Causes of Memory Leaks
- **Global Variables:** Variables declared without `let`, `const`, or `var`.
- **Event Listeners:** Forgotten `removeEventListener`.
- **Closures:** Retaining unused variables in closures.

### Avoiding Leaks
- Use `WeakMap` and `WeakSet` for objects that can be garbage-collected.
- Clean up event listeners and intervals.


## **12. Symbols**
Unique, immutable property keys.

```javascript
const sym1 = Symbol("description");
const sym2 = Symbol("description");

console.log(sym1 === sym2); // false

const obj = {
  [sym1]: "value1",
};

console.log(obj[sym1]); // value1
```


## **13. Functional Programming Concepts**
### Immutability
```javascript
const obj = { a: 1 };
const newObj = { ...obj, b: 2 };
```

### Pure Functions
A function that doesn’t modify external state and always returns the same result for the same input.

```javascript
const add = (a, b) => a + b;
```

### Composition
Combining functions to build more complex ones.

```javascript
const add = (x) => x + 2;
const multiply = (x) => x * 3;

const compose = (...fns) => (x) => fns.reduceRight((acc, fn) => fn(acc), x);

const combined = compose(multiply, add);
console.log(combined(2)); // Output: 12
```

