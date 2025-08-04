# Decision Problems - Common Algorithms

**Decision algorithms** are algorithms that solve **decision problems** — problems with **yes/no** answers. These are core to computer science, especially in **complexity theory**, **formal languages**, **logic**, and **computational geometry**.

Below is a categorized list of common **decision algorithms**, organized by domain and difficulty.

---

## Basic Decision Algorithms (Polynomial Time)

These are efficient (in **P**) and foundational in computer science.

| Algorithm                             | Problem Decided                                       | Time Complexity   |
| ------------------------------------- | ----------------------------------------------------- | ----------------- |
| **Primality Test (AKS)**              | Is `n` a prime number?                                | Polynomial        |
| **DFS/BFS**                           | Is there a path between nodes `u` and `v` in a graph? | Linear (`O(V+E)`) |
| **Dijkstra’s Algorithm**              | Is the shortest path from `A` to `B` less than `K`?   | `O(V + E log V)`  |
| **Regular Expression Matching (DFA)** | Does a string match a regular expression?             | Linear            |
| **Balanced Parentheses**              | Is a string of parentheses balanced?                  | Linear            |
| **String Matching (KMP)**             | Does string `P` occur in text `T`?                    | Linear            |
| **Union-Find**                        | Are `x` and `y` in the same set? (after unions)       | Near-constant     |

---

## Intermediate Decision Algorithms (NP-complete, verifiable quickly)

These problems are **easy to verify**, but **hard to solve** (no known polynomial-time algorithm).

| Problem                          | Decision Question                                       | Common Algorithm Used             |
| -------------------------------- | ------------------------------------------------------- | --------------------------------- |
| **SAT (Boolean Satisfiability)** | Is there an assignment that satisfies a formula?        | DPLL, CDCL, or WalkSAT solvers    |
| **3-COLORING**                   | Can a graph be colored with 3 colors without conflict?  | Backtracking, CSP search          |
| **Hamiltonian Cycle**            | Does a graph contain a Hamiltonian cycle?               | Backtracking, Dynamic Programming |
| **Subset Sum**                   | Is there a subset of numbers summing to `T`?            | Meet-in-the-middle, DP            |
| **Knapsack (0/1)**               | Is there a subset that fits capacity and reaches value? | Branch and bound, DP              |
| **Traveling Salesman (TSP)**     | Is there a tour shorter than `K`?                       | Branch and bound, Held-Karp       |

---

## Advanced or Specialized Decision Algorithms

| Algorithm                          | Problem                                           | Complexity                        |
| ---------------------------------- | ------------------------------------------------- | --------------------------------- |
| **Presburger Arithmetic Decision** | Is a given integer formula valid?                 | Non-elementary                    |
| **First-order Logic Validity**     | Is this FOL formula valid in all models?          | Undecidable in general            |
| **Model Checking (CTL, LTL)**      | Does a system satisfy a temporal logic property?  | PSPACE-complete                   |
| **SAT modulo Theories (SMT)**      | Is this logic formula satisfiable under a theory? | Depends on theory                 |
| **Ellipsoid Method**               | Is a linear system feasible?                      | Polynomial (theoretical)          |
| **Linear Programming (LP)**        | Is there a feasible solution meeting constraints? | Polynomial (e.g., interior point) |

---

## Decision vs Search vs Optimization

* **Decision**: Does a solution exist? (`YES/NO`)
* **Search**: What is the solution?
* **Optimization**: What is the *best* solution?

💡 Often, **decision problems** are used to study complexity, while **search/optimization** are more practical.

---

## Tools Used to Build Decision Algorithms

* **Greedy algorithms** (e.g., for shortest path, matching)
* **Dynamic programming** (e.g., subset sum, Knapsack)
* **Backtracking / DFS** (e.g., SAT, 3-coloring)
* **Constraint satisfaction** (CSP solvers)
* **Automata theory** (DFA/NFA for regex matching)
* **Linear programming** (LP feasibility)

---
