# JavaScript

JavaScript (JS) is a **high-level, interpreted programming language** originally designed for adding interactivity to web pages. Today, it is a **multi-paradigm language** used across web development, backend services, mobile apps, and even desktop applications.

---

## 1. Brief History of JavaScript

* **1995** – Brendan Eich at Netscape created JavaScript in just **10 days**, originally named **Mocha**, later renamed **LiveScript**, and finally **JavaScript** (partly for marketing, to ride on Java’s popularity).
* **1996** – Microsoft introduced **JScript** (their implementation for IE 3).
* **1997** – Standardized as **ECMAScript (ES)** by **ECMA International** (ECMA-262 spec).
* **2009** – **Node.js** brought JS to the server.
* **2015 onwards** – ES6 (aka ES2015) revolutionized JS with modern features.

---

## 2. Major ECMAScript (ES) Version Updates

| Year  | Version          | Key Features                                                                                               |   |                                                                            |
| ----- | ---------------- | ---------------------------------------------------------------------------------------------------------- | - | -------------------------------------------------------------------------- |
| 1997  | ES1              | First edition                                                                                              |   |                                                                            |
| 1998  | ES2              | Minor changes                                                                                              |   |                                                                            |
| 1999  | ES3              | Regular expressions, better error handling                                                                 |   |                                                                            |
| 2009  | ES5              | Strict mode, JSON support, `Array.forEach`, getters/setters                                                |   |                                                                            |
| 2015  | **ES6 (ES2015)** | `let`, `const`, classes, modules, template literals, arrow functions, promises, default/rest/spread params |   |                                                                            |
| 2016  | ES7              | `Array.includes`, exponentiation (`**`)                                                                    |   |                                                                            |
| 2017  | ES8              | `async/await`, `Object.entries`, `Object.values`                                                           |   |                                                                            |
| 2018  | ES9              | Rest/spread in objects, async iterators                                                                    |   |                                                                            |
| 2019  | ES10             | `Array.flat`, `Object.fromEntries`, optional `catch` binding                                               |   |                                                                            |
| 2020  | ES11             | Optional chaining (`?.`), nullish coalescing (`??`), dynamic `import()`                                    |   |                                                                            |
| 2021+ | ES12+            | Logical assignment (\`                                                                                     |   | =`, `??=`), `String.replaceAll`, top-level `await\`, weak references, etc. |

---

## 3. JavaScript Features with Examples

### A. Basic Features

1. **Variables**

```js
var x = 5;   // function-scoped
let y = 10;  // block-scoped
const z = 15; // immutable
```

2. **Data Types**

```js
let num = 42;        // number
let str = "Hello";   // string
let bool = true;     // boolean
let obj = {a:1};     // object
let arr = [1,2,3];   // array
let n = null;        // null
let u;               // undefined
```

3. **Functions**

```js
function add(a, b) {
  return a + b;
}
console.log(add(2,3));
```

4. **Control Flow**

```js
for (let i=0; i<3; i++) console.log(i);

if (true) console.log("Yes");
```

---

### B. Intermediate Features

1. **Arrow Functions**

```js
const multiply = (a, b) => a * b;
```

2. **Template Literals**

```js
let name = "Alice";
console.log(`Hello, ${name}!`);
```

3. **Destructuring**

```js
const [a,b] = [1,2];
const {x, y} = {x:10, y:20};
```

4. **Spread / Rest**

```js
let nums = [1,2,3];
let more = [...nums, 4,5];

function sum(...args) {
  return args.reduce((a,b)=>a+b, 0);
}
```

5. **Classes**

```js
class Person {
  constructor(name) { this.name = name; }
  greet() { console.log(`Hi, I'm ${this.name}`); }
}
```

6. **Modules (ES6)**

```js
// file: math.js
export const add = (a,b) => a+b;

// file: app.js
import { add } from './math.js';
```

---

### C. Advanced Features

1. **Promises & Async/Await**

```js
function fetchData() {
  return new Promise(resolve => setTimeout(()=>resolve("Done"), 1000));
}

async function run() {
  let result = await fetchData();
  console.log(result);
}
run();
```

2. **Generators**

```js
function* numbers() {
  yield 1;
  yield 2;
  yield 3;
}
for (let n of numbers()) console.log(n);
```

3. **Optional Chaining**

```js
let user = {profile: {name: "Alice"}};
console.log(user.profile?.name); // Alice
console.log(user.settings?.theme); // undefined
```

4. **Nullish Coalescing**

```js
let x = null ?? "default"; // "default"
```

5. **Proxies**

```js
let obj = {a:1};
let proxy = new Proxy(obj, {
  get: (target, prop) => prop in target ? target[prop] : "Not found"
});
console.log(proxy.a, proxy.b);
```

6. **Symbols & Iterators**

```js
const sym = Symbol("id");
let obj2 = {[sym]: 123};
console.log(obj2[sym]);
```

---

## 4. Flavours of JavaScript Implementations

JavaScript isn’t just one runtime—it has **multiple implementations**:

| Implementation           | Environment                                                                            | Highlights                                         |
| ------------------------ | -------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **Browser JS**           | Runs inside browsers (V8 in Chrome, SpiderMonkey in Firefox, JavaScriptCore in Safari) | DOM manipulation, events, APIs                     |
| **Node.js**              | Server-side runtime (uses V8)                                                          | File system, networking, backend services          |
| **Deno**                 | Secure JS/TS runtime by Node’s creator                                                 | Built-in TypeScript, secure by default, ES modules |
| **Bun**                  | New runtime (powered by Zig & JavaScriptCore)                                          | Very fast, built-in bundler, test runner           |
| **Nashorn/GraalJS**      | Java-based implementations                                                             | Running JS on JVM                                  |
| **Adobe’s ExtendScript** | Adobe apps scripting                                                                   | Automates Photoshop/Illustrator                    |

---

**Summary:**

* JS started in 1995, standardized as ECMAScript.
* ES6 (2015) was the biggest leap with modern syntax.
* Features range from basics (variables, functions) → intermediate (classes, modules) → advanced (async/await, proxies, generators).
* Multiple runtimes exist: browsers, Node.js, Deno, Bun, etc.
