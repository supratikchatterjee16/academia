# Search Problems - Common Algorithms

Search algorithms are methods for exploring data structures or solution spaces to **find a specific value, goal, or optimal configuration**. They're foundational in **AI, pathfinding, game theory, databases, and optimization**.

Below is a structured list of **search algorithms**, categorized by purpose and properties.

---

## 1. **Uninformed (Blind) Search Algorithms**

These algorithms don’t use any domain-specific information.

| Algorithm                      | Strategy                           | Complete?     | Optimal?             | Time Complexity        |
| ------------------------------ | ---------------------------------- | ------------- | -------------------- | ---------------------- |
| **Breadth-First Search (BFS)** | Explores neighbors level by level  | ✅ Yes         | ✅ Yes (uniform cost) | O(b<sup>d</sup>)       |
| **Depth-First Search (DFS)**   | Explores one branch deeply first   | ✅ (if finite) | ❌ No                 | O(b<sup>d</sup>)       |
| **Iterative Deepening DFS**    | DFS with increasing depth limit    | ✅ Yes         | ✅ Yes                | O(b<sup>d</sup>)       |
| **Uniform-Cost Search**        | Expands node with lowest path cost | ✅ Yes         | ✅ Yes                | O(b<sup>1+⌊C/ε⌋</sup>) |

> **b** = branching factor, **d** = depth of goal node, **C** = cost, **ε** = smallest step cost.

---

## 🔍 2. **Informed (Heuristic) Search Algorithms**

Use a heuristic function `h(n)` to guide the search. Common in **AI and robotics**.

| Algorithm                    | Description                                       | Complete? | Optimal? | Notes                               |
| ---------------------------- | ------------------------------------------------- | --------- | -------- | ----------------------------------- |
| **Greedy Best-First Search** | Chooses node with lowest `h(n)`                   | ❌         | ❌        | Fast but not always correct         |
| **A\***                      | Uses `f(n) = g(n) + h(n)` (path cost + heuristic) | ✅         | ✅        | Optimal if `h` is admissible        |
| **Beam Search**              | Keeps only best `k` nodes per level               | ❌         | ❌        | Tradeoff between speed and accuracy |
| **Iterative Deepening A\***  | A\* with depth limits                             | ✅         | ✅        | Space-efficient                     |

> A\* is widely used in **pathfinding**, e.g., GPS systems, games.

---

## 🔗 3. **Local Search Algorithms**

Focus on **improving a single solution** iteratively. Good for large state spaces.

| Algorithm               | Description                                       | Notes                           |
| ----------------------- | ------------------------------------------------- | ------------------------------- |
| **Hill Climbing**       | Moves to better neighboring states                | Can get stuck in local maxima   |
| **Simulated Annealing** | Probabilistic jumps to escape local optima        | Slower but more global          |
| **Genetic Algorithms**  | Evolves solutions through crossover and mutation  | Works on populations            |
| **Tabu Search**         | Avoids cycles by tracking recently visited states | Good for combinatorial problems |

> Useful for **optimization**, especially when the search space is vast or poorly understood.

---

## 4. **Adversarial Search (Game Trees)**

Used in **game AI** or any setting with competing agents.

| Algorithm                          | Purpose                                   | Domain                 |
| ---------------------------------- | ----------------------------------------- | ---------------------- |
| **Minimax**                        | Chooses the move that minimizes loss      | Chess, Tic-Tac-Toe     |
| **Alpha-Beta Pruning**             | Prunes Minimax branches that won't help   | More efficient Minimax |
| **Expectimax**                     | Handles stochastic outcomes               | Dice games, backgammon |
| **Monte Carlo Tree Search (MCTS)** | Simulates rollouts to estimate move value | Go, real-time strategy |

> Used in agents like **Deep Blue**, **AlphaGo**, and other game-playing AIs.

---

## 5. **Tree and Graph Traversal**

Often used in data structures, compilers, and file systems.

| Algorithm                | Structure Used             | Direction            |
| ------------------------ | -------------------------- | -------------------- |
| **In-order Traversal**   | Binary Trees               | Left → Root → Right  |
| **Pre-order Traversal**  | Binary Trees               | Root → Left → Right  |
| **Post-order Traversal** | Binary Trees               | Left → Right → Root  |
| **Topological Sort**     | DAGs                       | Sorted by dependency |
| **Dijkstra’s Algorithm** | Weighted Graphs            | Shortest path        |
| **Bellman-Ford**         | Graphs w/ negative weights | Shortest path        |

---

## 6. **Real-World & AI Search Problems**

| Problem                         | Algorithm(s) Commonly Used      |
| ------------------------------- | ------------------------------- |
| Route finding (e.g., GPS)       | A\*, Dijkstra                   |
| Puzzle solving (e.g., 8-puzzle) | A\*, IDA\*, BFS                 |
| Game playing (e.g., Chess)      | Minimax + Alpha-Beta            |
| SAT solving                     | DPLL, CDCL, WalkSAT             |
| Job scheduling                  | Tabu Search, Genetic Algorithms |
| Maze solving                    | BFS, DFS, A\*                   |
| Robot path planning             | RRT, A\*, D\*                   |

---

## Summary Table

| Algorithm Type      | Examples              | Best Used For                          |
| ------------------- | --------------------- | -------------------------------------- |
| **Uninformed**      | BFS, DFS, UCS         | General graphs, unknown domains        |
| **Informed**        | A\*, Greedy, Beam     | Pathfinding, AI                        |
| **Local**           | Hill climbing, SA, GA | Optimization, continuous problems      |
| **Adversarial**     | Minimax, MCTS         | Games, multi-agent environments        |
| **Graph traversal** | Topo Sort, DFS, BFS   | Data structures, dependency resolution |
