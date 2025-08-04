# Theory of Computation

The Theory of Computation is the study of the mathematical foundations of computing. It asks three core questions:

1. What can computers compute? → Computability Theory
2. How efficiently can they compute it? → Complexity Theory
3. How do formal machines process input? → Automata Theory

## Breakdown

| Branch                   | Focus                                       | Key Concepts                                   |
| ------------------------ | ------------------------------------------- | ---------------------------------------------- |
| **Automata Theory**      | Abstract machines & language recognition    | Finite automata, regular languages, grammars   |
| **Computability Theory** | What problems are solvable by any algorithm | Turing machines, halting problem, decidability |
| **Complexity Theory**    | Resources needed to solve problems          | Time/space complexity, P vs NP, reductions     |

## Computability Theory

**Computability Theory** is a branch of theoretical computer science and mathematical logic that studies:

> **What problems can or cannot be solved by algorithms?**

It answers fundamental questions like:

* Is there a general algorithm to solve this problem?
* Can we determine if a program halts?
* What are the limits of what machines (or humans) can compute?

---

### Core Ideas of Computability Theory

#### 1. **Decidable vs. Undecidable Problems**

* **Decidable**: A problem for which an algorithm *always* produces a correct yes/no answer.
* **Undecidable**: No algorithm can solve it for *all* possible inputs.

Example:

* Sorting a list → ✅ Decidable
* Halting Problem → ❌ Undecidable

---

#### 2. **Turing Machines**

A Turing Machine is a simple theoretical model of a computer:

* It reads input from an infinite tape
* It can move left/right and change symbols
* It defines the **limit of algorithmic computation**

> If a problem can be solved by a Turing Machine, it is **computable**.

---

#### 3. **Church-Turing Thesis**

> Anything that is **effectively computable** can be computed by a Turing Machine.

This is not a theorem, but a foundational hypothesis accepted by most computer scientists.

---

#### 4. **Recursive and Recursively Enumerable Sets**

* **Recursive (decidable)**: There is a Turing machine that always halts and says yes/no.
* **Recursively Enumerable (RE)**: A Turing machine can *enumerate* the solutions but might run forever if the answer is no.

Example:

* All valid Python programs? ✅ RE
* All programs that never crash? ❌ Not RE

---

#### 5. **Reductions**

> We reduce one problem to another to **prove undecidability**.

If problem A is known to be undecidable and A reduces to B, then B is also undecidable.

---

#### 6. **Rice’s Theorem**

> Any non-trivial property of a program's output is **undecidable**.

This tells us you can't write a general algorithm to:

* Check if a program returns `42` for all inputs
* Decide if a function always terminates
* Detect if a program has side effects

---

### Why Computability Theory Matters

| Field                     | Use Case                                              |
| ------------------------- | ----------------------------------------------------- |
| **Programming**           | Understand which bugs can’t be detected automatically |
| **AI & ML**               | Know the boundaries of what models can reason about   |
| **Cryptography**          | Build secure systems assuming hard problems           |
| **Mathematics**           | Connects to logic, proofs, and Gödel's theorems       |
| **Software Verification** | Limits of proving program correctness                 |

---

### Summary Table

| Concept                    | Description                                                      |
| -------------------------- | ---------------------------------------------------------------- |
| **Computable Problem**     | Has a step-by-step algorithm that solves it for all inputs       |
| **Undecidable Problem**    | No algorithm exists to solve it in general                       |
| **Turing Machine**         | Abstract model of computation                                    |
| **Church-Turing Thesis**   | Anything computable by humans can be done by a Turing machine    |
| **Recursive**              | Always halts and gives a correct answer                          |
| **Recursively Enumerable** | Can list the solutions, but may not halt if input isn't accepted |
| **Rice’s Theorem**         | No general algorithm can detect non-trivial program behavior     |
| **Halting Problem**        | Classic example of undecidability                                |

---

## Complexity Theory

**Complexity Theory** is a major branch of theoretical computer science that studies:

> **How much of a computational resource (like time or memory) is needed to solve a given problem?**

It doesn’t just ask **“can a problem be solved?”** (that’s **computability theory**) — it asks:

> **“How efficiently can it be solved?”**

---

### Core Questions in Complexity Theory

1. **How many steps (time)** does it take to solve a problem?
2. **How much memory (space)** is required?
3. Can we **classify** problems based on these requirements?
4. Are there problems that are **inherently inefficient** to solve?

---

### Basic Concepts

#### 1. **Complexity Classes**

These are groups of problems based on how hard they are to solve.

| Class           | Description                                                       |
| --------------- | ----------------------------------------------------------------- |
| **P**           | Problems solvable in **polynomial time** (efficient)              |
| **NP**          | Problems **verifiable** in polynomial time                        |
| **NP-complete** | Hardest problems in NP; if any one is solved efficiently, all are |
| **PSPACE**      | Problems solvable in polynomial space                             |
| **EXP**         | Problems solvable in exponential time                             |
| **BPP / BQP**   | Problems solvable by probabilistic or quantum algorithms          |

---

#### 2. **Time Complexity**

How the **running time** of an algorithm grows with input size `n`.

Examples:

* Constant time: `O(1)`
* Linear time: `O(n)`
* Quadratic time: `O(n²)`
* Exponential time: `O(2ⁿ)`

> A problem in `P` has at least one algorithm with polynomial-time complexity.

---

#### 3. **Space Complexity**

How much **memory** is used in relation to input size.

---

#### 4. **Big-O Notation**

Describes **upper bounds** on time or space:

* `O(n)` means time grows linearly with input size
* `O(n^2)` means quadratic growth
* `O(log n)` is logarithmic (very fast)

---

### P vs NP

The most famous open problem in complexity theory:

> **Is P equal to NP?**

* `P = NP`: Every problem whose solution can be quickly **verified** can also be quickly **solved**.
* `P ≠ NP`: Some problems are easy to check but hard to solve.

Still **unsolved**, with a \$1 million prize from the Clay Mathematics Institute.

---

### Examples

| Problem                      | Complexity Class |
| ---------------------------- | ---------------- |
| Sorting a list               | `P`              |
| Sudoku (checking a solution) | `NP`             |
| Traveling Salesman Problem   | `NP-complete`    |
| Chess (generalized)          | `EXP`            |
| SAT (boolean satisfiability) | `NP-complete`    |

---

### Applications

* **Cryptography** – Relies on problems that are hard to solve (e.g. factoring)
* **Optimization** – Find efficient solutions in scheduling, logistics
* **Machine Learning** – Analyzing the tractability of model training
* **Compilers / Parsers** – Based on time/space bounds of parsing languages
* **Quantum Computing** – Challenges classical complexity assumptions

---

### Summary Table

| Concept              | Description                        |
| -------------------- | ---------------------------------- |
| **P**                | Problems solvable efficiently      |
| **NP**               | Problems verifiable efficiently    |
| **NP-complete**      | Hardest problems in NP             |
| **Time Complexity**  | Steps needed to solve a problem    |
| **Space Complexity** | Memory needed to solve a problem   |
| **Big-O Notation**   | Describes algorithm growth rate    |
| **P vs NP**          | Central open question in the field |

## Automata Theory

**Automata Theory** is a branch of theoretical computer science that studies **abstract machines** (called **automata**) and the **problems they can solve**. It forms the foundation of **language recognition**, **compiler design**, and the **limits of computation**.

---

### In Simple Terms

> **Automata Theory explores what kinds of problems can be solved by different "machines" and how those machines process input symbols.**

---

### Why It's Important

* It helps us understand how **computers, compilers, and interpreters** work at a fundamental level.
* It shows the **limits of computational models**: what *can* and *can’t* be done with limited resources like memory or time.
* It forms the basis for **regular expressions**, **parsers**, and **formal verification** tools.

---

### Core Concepts

#### 1. **Alphabet (Σ)**

* A finite set of symbols (e.g., `{0, 1}` for binary)

#### 2. **String (or Word)**

* A sequence of symbols from the alphabet (e.g., `0110`)

#### 3. **Language**

* A set of strings (e.g., all strings that start with `1`)

#### 4. **Automaton (plural: Automata)**

* An abstract machine that processes strings and decides whether they belong to a certain language.

---

### Types of Automata

| Type of Automaton            | Memory        | Recognizes                       | Power Level |
| ---------------------------- | ------------- | -------------------------------- | ----------- |
| **Finite Automaton (FA)**    | No memory     | Regular Languages                | Lowest      |
| **Pushdown Automaton (PDA)** | Stack         | Context-Free Languages           | Medium      |
| **Turing Machine (TM)**      | Infinite tape | Recursively Enumerable Languages | Highest     |

---

### Common Automata

#### **Finite Automaton (FA)**

* No memory beyond current state.
* Used in **regex engines**, **lexical analyzers**.
* Example: Accept strings with an even number of `0`s.

##### 2 types:

* DFA (Deterministic)
* NFA (Non-deterministic)

---

#### **Pushdown Automaton (PDA)**

* Like a FA but with a **stack**.
* Used for **parsing**, **syntax analysis**.
* Can recognize nested structures (e.g., matching parentheses).

---

#### **Turing Machine (TM)**

* Like a PDA but with an **infinite tape** as memory.
* Can simulate **any algorithm**.
* Foundation for **computability and complexity theory**.

---

### Language Classes (Chomsky Hierarchy)

| Language Class             | Recognized by           | Examples                              |
| -------------------------- | ----------------------- | ------------------------------------- |
| **Regular**                | Finite Automata         | `a*b*`, email matching                |
| **Context-Free**           | Pushdown Automata       | Balanced parentheses, JSON            |
| **Context-Sensitive**      | Linear Bounded Automata | Some natural languages                |
| **Recursively Enumerable** | Turing Machines         | Anything a real computer can simulate |

---

### Real-World Applications

| Area                | Role of Automata Theory                    |
| ------------------- | ------------------------------------------ |
| **Compilers**       | Lexical and syntax analysis                |
| **Regex engines**   | Pattern matching via finite automata       |
| **Protocol Design** | Communication model verification           |
| **AI/Robotics**     | State machines for behavior modeling       |
| **Cybersecurity**   | Intrusion detection rules, formal modeling |

---

### Summary Table

| Concept               | Description                                     |
| --------------------- | ----------------------------------------------- |
| **Alphabet (Σ)**      | Set of allowed input symbols                    |
| **String**            | Sequence of symbols                             |
| **Language**          | Set of strings                                  |
| **FA / DFA / NFA**    | Basic machines for pattern recognition          |
| **PDA**               | FA + stack → for parsing structured input       |
| **Turing Machine**    | Theoretical model of a general-purpose computer |
| **Chomsky Hierarchy** | Classification of languages and automata        |
