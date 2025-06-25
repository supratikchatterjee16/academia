# Parallel Algorithms

A **parallel algorithm** is an algorithm that splits a problem into **independent subtasks** that can be **executed simultaneously**, typically on multiple processors or cores.

## Characteristics of a Parallel Algorithm:

* Tasks are **executed concurrently**.
* Aims to **reduce total execution time**.
* Requires **synchronization** or **coordination** between parallel tasks.
* Designed for **multi-core CPUs**, **GPUs**, or **distributed systems**.
* May involve **communication overhead**.

## Key Concepts
| Concept             | Description                                                               |
| ------------------- | ------------------------------------------------------------------------- |
| **Task**            | A unit of work to be done (could be a loop iteration or a function call). |
| **Parallelism**     | Performing multiple tasks at the same time.                               |
| **Synchronization** | Making sure tasks finish in the correct order when needed.                |
| **Speedup**         | The performance gain over a serial version.                               |

## Examples of Parallel Algorithms with Pseudocode

(Note: Pseudocode includes `parallel for`, which assumes independent iterations can run at the same time.)

### 1. **Parallel Sum of Array Elements**

```pseudocode
function parallelSum(arr)
    n = length of arr
    total = 0
    parallel for i from 0 to n - 1
        atomic total = total + arr[i]
    return total
```

* **Note:** `atomic` ensures that `total` is safely updated from multiple threads.
* **Speedup:** Depends on number of threads; ideal is O(n/p)

### 2. **Parallel Maximum in Array**

```pseudocode
function parallelMax(arr)
    maxVal = -∞
    parallel for i from 0 to length of arr - 1
        atomic maxVal = max(maxVal, arr[i])
    return maxVal
```

* Uses parallel comparison, needs atomic or reduction operation.

### 3. **Parallel Matrix Addition**

```pseudocode
function addMatrices(A, B)
    rows = number of rows in A
    cols = number of columns in A
    result = matrix of same size
    parallel for i from 0 to rows - 1
        parallel for j from 0 to cols - 1
            result[i][j] = A[i][j] + B[i][j]
    return result
```

* Perfect for grid-like problems (image processing, matrix math).

### 4. **Parallel Merge Sort (Divide and Conquer)**

```pseudocode
function parallelMergeSort(arr)
    if length of arr ≤ 1
        return arr
    mid = length of arr / 2
    parallel:
        left = parallelMergeSort(arr[0..mid-1])
        right = parallelMergeSort(arr[mid..end])
    return merge(left, right)
```

* Recursive parallelism.
* **Time Complexity:** O(log² n) with enough processors.

## When to Use Parallel Algorithms

* When the problem has **independent subparts** (no data dependencies).
* When **performance/scalability** is critical.
* In **scientific computing, machine learning, image processing**, etc.

### Challenges

* **Race conditions** (multiple threads writing to same data)
* **Load balancing** (not all threads have equal work)
* **Overhead** of creating and managing threads
