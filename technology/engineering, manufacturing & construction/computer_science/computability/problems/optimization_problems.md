# Optimization Problems - Common Algorithms


Optimization algorithms are at the core of solving real-world problems where you want to **maximize or minimize** some objective under certain constraints. These algorithms are used in fields ranging from machine learning and operations research to engineering, logistics, and economics.

---

## Categories of Optimization Algorithms

| Category                      | Purpose                                 | Example Problems                 |
| ----------------------------- | --------------------------------------- | -------------------------------- |
| **Deterministic**             | Solve exactly or converge predictably   | Linear/Quadratic Programming     |
| **Heuristic / Metaheuristic** | Approximate solutions for hard problems | TSP, scheduling, design problems |
| **Gradient-based**            | Use derivatives to find optima          | Machine Learning, NLP            |
| **Combinatorial**             | Search over discrete structures         | Routing, assignment, SAT         |

---

## 1. **Gradient-Based Optimization Algorithms**

Used in **continuous** optimization, especially in **ML, deep learning**, and scientific computing.

| Algorithm                             | Description                                   | Uses Derivatives? |
| ------------------------------------- | --------------------------------------------- | ----------------- |
| **Gradient Descent**                  | Moves in the direction of steepest descent    | ✅ Yes             |
| **Stochastic Gradient Descent (SGD)** | Uses random subsets (batches) for efficiency  | ✅ Yes             |
| **Newton’s Method**                   | Uses second-order derivatives (Hessian)       | ✅ Yes (2nd order) |
| **Conjugate Gradient**                | Efficient for large sparse linear systems     | ✅ Yes             |
| **L-BFGS**                            | Limited-memory BFGS; for large-scale problems | ✅ Yes             |
| **Adam / RMSProp**                    | Adaptive variants for neural networks         | ✅ Yes             |

> Used in: Deep learning, control systems, signal processing

---

## 2. **Combinatorial Optimization Algorithms**

Used when the problem space is **discrete**, like graphs, sets, or assignments.

| Algorithm                    | Description                                 | Problem Type       |
| ---------------------------- | ------------------------------------------- | ------------------ |
| **Dijkstra’s / A\***         | Find shortest path in a graph               | Pathfinding        |
| **Hungarian Algorithm**      | Optimal assignment in a bipartite graph     | Assignment         |
| **Branch and Bound**         | Prunes suboptimal solutions using bounds    | Knapsack, TSP      |
| **Backtracking**             | Recursive search with pruning               | Scheduling, Sudoku |
| **Integer Programming (IP)** | Linear programming with integer variables   | Routing, logistics |
| **Dynamic Programming (DP)** | Breaks problem into overlapping subproblems | Knapsack, LCS      |

> Used in: Logistics, operations research, AI planning

---

## 3. **Metaheuristic Algorithms**

Approximate global optima for hard or **NP-hard** problems. Often stochastic.

| Algorithm                       | Inspiration/Approach                      | Used In                        |
| ------------------------------- | ----------------------------------------- | ------------------------------ |
| **Simulated Annealing**         | Physics: gradual cooling                  | TSP, circuit design            |
| **Genetic Algorithms**          | Evolution: selection, mutation, crossover | Scheduling, design, ML         |
| **Ant Colony Optimization**     | Swarm behavior of ants                    | Routing problems, graphs       |
| **Particle Swarm Optimization** | Social behavior in bird flocking          | Neural network tuning, control |
| **Tabu Search**                 | Uses memory of recent moves               | Graph coloring, job scheduling |

> Used in: Optimization when exact methods fail or are too slow.

---

## 4. **Convex Optimization Algorithms**

For problems where the objective and constraints form convex sets.

| Algorithm                               | Application                       | Solves Problems Like            |
| --------------------------------------- | --------------------------------- | ------------------------------- |
| **Interior Point Methods**              | High-dimensional LP/QP            | Portfolio optimization, control |
| **Simplex Method**                      | Vertex search on LP polytope      | Linear programming              |
| **Dual Ascent / Lagrangian Relaxation** | Handle constraints with penalties | Constrained optimization        |

> Used in: Control theory, finance, signal processing

---

## 5. **Discrete Optimization**

| Algorithm                       | Description                         | Problem Domain         |
| ------------------------------- | ----------------------------------- | ---------------------- |
| **Greedy Algorithms**           | Make locally optimal choices        | Huffman coding, MST    |
| **Constraint Programming (CP)** | Declarative problem solving         | Scheduling, puzzles    |
| **SAT/SMT Solvers**             | Boolean satisfiability-based search | Verification, planning |

---

## Real-World Optimization Examples

| Problem                      | Algorithm(s) Typically Used                |
| ---------------------------- | ------------------------------------------ |
| Route planning (e.g., Uber)  | Dijkstra, A\*, Genetic Algorithms          |
| Neural network training      | SGD, Adam, RMSProp                         |
| Job shop scheduling          | Constraint Programming, Tabu Search        |
| Portfolio optimization       | Quadratic Programming, Convex Optimization |
| Knapsack problem             | Dynamic Programming, Branch and Bound      |
| Compiler register allocation | Graph coloring + heuristic search          |

---

## Summary: When to Use What

| Problem Type                | Recommended Algorithms                |
| --------------------------- | ------------------------------------- |
| Continuous & Differentiable | Gradient descent, L-BFGS, Adam        |
| Integer / Discrete          | Branch and Bound, IP, SAT solvers     |
| NP-hard or Large Search     | Metaheuristics like GA, SA, ACO       |
| Convex & Structured         | Simplex, Interior Point, Dual Methods |
| Real-time or Fast Approx.   | Greedy, Local Search, Tabu            |
