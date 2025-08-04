# Problems - Computation

In theoretical computer science and computational complexity theory, **problems are categorized** based on how difficult they are to solve or verify, using formal models like Turing machines. There’s no fixed number of categories, but here’s a structured list of the **most widely recognized problem classes**, from basic to advanced:

---

## **1. Decidable vs Undecidable Problems**

### **Decidable (Computable)**

Problems for which **an algorithm exists** that solves it in finite time.

* Example: Is a number even?
* Class: Turing-decidable

### **Undecidable**

No algorithm can solve these problems for all inputs.

* Example: Halting Problem
* Often involves self-reference or infinite loops
* Class: Not Turing-decidable

---

## **2. Within Decidable: Complexity Classes**

These are the most important **categories of decision problems** based on **time and space complexity**:

| Class              | Description                                                                        |
| ------------------ | ---------------------------------------------------------------------------------- |
| **P**              | Solvable in polynomial time (`O(n^k)`)                                             |
| **NP**             | Verifiable in polynomial time; solution may be hard to find                        |
| **co-NP**          | Complements of NP problems (e.g., "is this formula unsatisfiable?")                |
| **NP-complete**    | Hardest problems in NP; if one is in P, all NP problems are in P                   |
| **NP-hard**        | At least as hard as NP-complete but may not be in NP (e.g., optimization problems) |
| **EXP (EXPTIME)**  | Solvable in exponential time (`O(2^n)`); bigger than P or NP                       |
| **PSPACE**         | Solvable using polynomial space (regardless of time)                               |
| **EXPSPACE**       | Solvable using exponential space                                                   |
| **BPP**            | Bounded-error probabilistic polynomial time (randomized algorithms)                |
| **ZPP, RP, co-RP** | Randomized classes with different guarantees                                       |
| **L**              | Solvable in logarithmic space (very small memory)                                  |
| **NL**             | Nondeterministic log space                                                         |
| **#P**             | Counting problems (e.g., how many solutions exist to a SAT problem?)               |
| **PH**             | Polynomial hierarchy (nested levels of NP and co-NP)                               |

---

## **3. Optimization vs Decision vs Search**

| Type             | What it Asks                    | Example                    |
| ---------------- | ------------------------------- | -------------------------- |
| **Decision**     | Yes/No questions                | Is there a path < 10km?    |
| **Search**       | Find the actual solution        | What is the path < 10km?   |
| **Optimization** | Find the best possible solution | What is the shortest path? |

→ Often, **NP-complete** problems are decision versions of **NP-hard** optimization problems.

---

## **4. Semantic Categories**

| Category            | Description                                                       |
| ------------------- | ----------------------------------------------------------------- |
| **Tractable**       | Problems solvable in "reasonable" (polynomial) time               |
| **Intractable**     | Problems that require exponential or worse time                   |
| **Approximation**   | Hard to solve exactly, but can be approximated                    |
| **Parameterized**   | Complexity depends on certain input parameters                    |
| **Online problems** | Input arrives piece-by-piece; decisions must be made in real-time |

---

## **5. For Undecidable Problems**

These are usually not solvable by **any algorithm**:

| Class                           | Example Problem                                             |
| ------------------------------- | ----------------------------------------------------------- |
| **RE (Recursively Enumerable)** | You can enumerate the “yes” answers (e.g., Halting Problem) |
| **co-RE**                       | You can enumerate the “no” answers                          |
| **Not RE**                      | Even unrecognizable problems                                |

---

## Visual Hierarchy (Simplified)

```
All Problems
├── Decidable
│   ├── P
│   ├── NP
│   │   ├── NP-complete
│   ├── co-NP
│   ├── PSPACE
│   ├── EXP
│   └── ...
└── Undecidable
    ├── RE
    ├── co-RE
    └── Not RE
```

---

## Summary

| Category               | How Many? | Contains Problems Like…                 |
| ---------------------- | --------- | --------------------------------------- |
| **Basic Divide**       | 2         | Decidable, Undecidable                  |
| **Complexity Classes** | 15+       | P, NP, co-NP, NP-complete, EXP, PSPACE… |
| **Problem Types**      | 3         | Decision, Search, Optimization          |
| **Randomized**         | 4+        | BPP, RP, co-RP, ZPP                     |
| **Counting & Others**  | 5+        | #P, PH, L, NL, EXPSPACE…                |

---

## Recommended Books

* "Introduction to the Theory of Computation" by Michael Sipser
* "Computational Complexity: A Modern Approach" by Arora & Barak
