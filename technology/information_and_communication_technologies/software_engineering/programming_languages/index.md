# Introduction to Programming Languages

A **programming language** is a **formal language** used to communicate instructions to a computer.

It defines a **syntax** (structure) and **semantics** (meaning) for writing programs that can:

* Control hardware
* Process data
* Build applications
* Automate tasks

In simple terms: A programming language is the bridge between **human thought** and **machine execution**.

---

## Why Do We Need Programming Languages?

Computers operate using **binary (0s and 1s)**. Writing in machine code is error-prone and tedious.
Programming languages:

* Provide **abstraction** (hide low-level details).
* Make code more **readable and maintainable**.
* Enable **portability** across different hardware.
* Facilitate **problem-solving** using higher-level concepts.

---

## Categories of Programming Languages

Programming languages are often classified by **level of abstraction** or **paradigm**:

### 1. **By Level of Abstraction**

* **Low-level languages:**

  * **Machine Language:** Direct 0s and 1s, hardware-specific.
  * **Assembly Language:** Human-readable mnemonics (MOV, ADD).

* **High-level languages:**

  * **Procedural:** C, Pascal
  * **Object-Oriented:** Java, C++, Python
  * **Functional:** Haskell, Lisp, F#
  * **Scripting:** JavaScript, PHP, Ruby

* **Very High-level (Domain-specific):** SQL, HTML, MATLAB.

---

### 2. **By Programming Paradigm**

* **Imperative:** Step-by-step instructions (C, Python).
* **Declarative:** State *what* to do, not *how* (SQL, Prolog).
* **Object-Oriented (OOP):** Based on objects and classes (Java, C++, Python).
* **Functional:** Treats computation as function evaluation (Haskell, Scala).
* **Procedural:** Organized as functions and procedures (C, Pascal).
* **Logic-based:** Uses rules and inference (Prolog).
* **Multi-paradigm:** Most modern languages (Python, Scala, JavaScript).

---

## What Programming Languages Encompass

A programming language typically provides:

1. **Syntax** → grammar rules (keywords, operators, structure).
2. **Semantics** → meaning of valid constructs.
3. **Primitives** → basic data types (int, float, string).
4. **Control Structures** → loops, conditionals.
5. **Abstractions** → functions, objects, modules.
6. **Standard Library** → built-in tools for I/O, networking, etc.
7. **Execution Model** → compiled (C, Rust) vs. interpreted (Python, JavaScript) vs. hybrid (Java).

---

## Evolution of Programming Languages

* **1940s–50s:** Machine code, Assembly.
* **1950s–60s:** FORTRAN (scientific), COBOL (business).
* **1970s–80s:** C, Pascal, Smalltalk (rise of OOP).
* **1990s–2000s:** Java, Python, PHP, JavaScript (web + enterprise).
* **2010s–now:** Rust, Go, Kotlin, TypeScript (safety, concurrency, web-scale).

---

## Core Principles in Programming Languages

1. **Abstraction:** Hide hardware details (variables instead of registers).
2. **Expressiveness:** Ability to express ideas clearly.
3. **Simplicity:** Minimize complexity (Python).
4. **Safety:** Prevent errors (Rust’s ownership system).
5. **Efficiency:** Optimize performance (C, C++).
6. **Portability:** Run across systems (Java, Python).
7. **Tooling & Ecosystem:** IDEs, compilers, libraries, frameworks.

---

## Programming Languages vs. Software Engineering

| Programming Languages                                 | Software Engineering                                                       |
| ----------------------------------------------------- | -------------------------------------------------------------------------- |
| Concerned with **how to express solutions**           | Concerned with **how to build software systems**                           |
| Focus on **syntax, semantics, paradigms**             | Focus on **process, lifecycle, methodology**                               |
| Example: “How do I implement this sorting algorithm?” | Example: “How do we design, test, and deliver a system that uses sorting?” |
| Tool                                                  | Discipline                                                                 |

---

## In Short

* **Programming languages = the vocabulary and grammar for telling computers what to do.**
* They range from **low-level (machine/assembly)** to **high-level (Python, Java)**.
* Classified by **paradigm (OOP, functional, declarative, etc.)**.
* Evolved alongside hardware and software needs.
* They are the **primary tools of software engineering**.

---

## Compilers vs Interpreters vs Hybrid

| Aspect               | **Compiler**                                                      | **Interpreter**                                        | **Hybrid (VM-based)**                                        |
| -------------------- | ----------------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------ |
| **Definition**       | Translates entire source code into machine code before execution. | Executes code line-by-line, translating on the fly.    | Compiles to intermediate bytecode, then executed by a VM.    |
| **Execution Speed**  | Fast (once compiled).                                             | Slower (line-by-line).                                 | Medium (JIT can optimize).                                   |
| **Translation Time** | Longer upfront (compile step).                                    | No upfront time, immediate execution.                  | Moderate (compile to bytecode + runtime interpretation/JIT). |
| **Error Detection**  | Errors caught at compile-time.                                    | Errors caught at runtime.                              | Both compile-time (bytecode check) & runtime.                |
| **Examples**         | C, C++, Rust, Go.                                                 | Python (CPython), JavaScript (Node.js, older engines). | Java (JVM), C# (.NET CLR), Kotlin.                           |
| **Portability**      | Platform-dependent binaries.                                      | Platform-independent (needs interpreter).              | High portability (VM runs on many platforms).                |
| **Use Cases**        | System software, performance-critical apps.                       | Rapid prototyping, scripting.                          | Enterprise, cross-platform apps.                             |


## Comparison of popular languages in 2025

| Language       | Paradigm(s)                                  | Execution Model                    | Strengths                                    | Typical Use Cases                               |
| -------------- | -------------------------------------------- | ---------------------------------- | -------------------------------------------- | ----------------------------------------------- |
| **C**          | Procedural, low-level                        | Compiled (native)                  | Fast, close to hardware, portable            | OS, embedded systems, performance-critical apps |
| **C++**        | OOP + Procedural                             | Compiled (native)                  | High performance, rich features, STL         | Games, real-time systems, high-performance apps |
| **Java**       | OOP, Multi-paradigm                          | Hybrid (JVM bytecode + JIT)        | Platform-independent, mature ecosystem       | Enterprise apps, Android, web backends          |
| **Python**     | Multi-paradigm (OOP, Functional, Procedural) | Interpreted (bytecode + VM)        | Simple, readable, large libraries            | AI/ML, scripting, web, data science             |
| **JavaScript** | Multi-paradigm (Functional + OOP)            | Interpreted/JIT (V8, SpiderMonkey) | Ubiquitous, async support, huge ecosystem    | Web apps (frontend & backend with Node.js)      |
| **C#**         | OOP, Multi-paradigm                          | Hybrid (.NET CLR + JIT)            | Strong tooling, enterprise-ready             | Windows apps, enterprise, game dev (Unity)      |
| **Go**         | Procedural, Concurrent                       | Compiled (native)                  | Simple, fast, great concurrency (goroutines) | Cloud services, networking, distributed systems |
| **Rust**       | Systems, Functional, OOP                     | Compiled (native)                  | Memory safety without GC, performance        | Systems programming, safe concurrency           |
| **Kotlin**     | OOP + Functional                             | Hybrid (JVM/Native)                | Modern, concise, interoperable with Java     | Android, enterprise, multiplatform              |
| **SQL**        | Declarative                                  | Interpreted by DB engine           | Simple, powerful queries                     | Database management                             |
