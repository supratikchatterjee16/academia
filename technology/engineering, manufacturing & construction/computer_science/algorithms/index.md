# Algorithms

In maths and computer science, algorithm is a finite sequence of mathematically rigorous instructions, typically used to solve a class of specific problems or to perform a computation.

In Computer Science, algorithms can be classified by implementation, design paradigm, and optimization:

1. Implementation
	- [recursion](./recursion.md) - invoke itself recursively. (Ex: Tower of Hanoi)
	- [Serial](./serial.md), [parallel](./parallel.md), or [distributed](./distributed.md)
	- Deterministic or non-deterministic - solve a problem with exact decision
	- Exact or approximate - Approximation algorithms seek an approximation that is close to the the solution
	- Quantum Algorithm - Algorithms run on a realistic model of quantum computation
2. By design paradigm
	- Brute force or exhaustive search
	- divide and conquer
	- search and enumeration - Includes search, branch and bound and backtracking algorithms(Ex: Chess, Graph Exploration Algorithm, etc.)
	- Randomized algorithm - Algorithms that make choices randomly(Ex: Monte Carlo algorithm, Las Vegas algo)
	- Reduction of complexity - This technique transforms difficult problems into better-known problems solvable with (hopefully) asymptotically optimal algorithms.
	- Back tracking - Multiple solutions are built incrementally and abandoned when it is determined that they cannot lead to a valid full solution
3. Optimization problems
	- Linear programming - When searching for optimal solutions to a linear function bound by linear equality and inequality constraints, the constraints can be used directly to produce optimal solutions.
	- Dynamic Programming - When a problem shows optimal substructures—meaning the optimal solution can be constructed from optimal solutions to subproblems—and overlapping subproblems, meaning the same subproblems are used to solve many different problem instances, a quicker approach called dynamic programming avoids recomputing solutions. 
	- Greedy method - Greedy algorithms, similarly to a dynamic programming, work by examining substructures, in this case not of the problem but of a given solution.
	- Heuristic method - In optimization problems, heuristic algorithms find solutions close to the optimal solution when finding the optimal solution is impractical.
