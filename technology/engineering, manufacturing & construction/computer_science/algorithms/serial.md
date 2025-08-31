# Serial/Sequential Algorithm

A **serial algorithm** (also called a **sequential algorithm**) is an algorithm that performs its operations **one after another** in a **single sequence** — **without any parallelism or concurrency**.

## Characteristics of a Serial Algorithm:

* Executes **one instruction at a time**.
* Runs on a **single processor/core**.
* Each step **depends on the result** of the previous step.
* Easier to understand and debug.
* Used when parallelism is unnecessary or would add complexity.

## Examples of Serial Algorithms with Pseudocode

### 1. **Sum of Elements in an Array**

```ini
function sumArray(arr)
    total = 0
    for i from 0 to length of arr - 1
        total = total + arr[i]
    return total
```

* **Type:** Linear, serial
* **Time Complexity:** O(n)

### 2. **Find Maximum in an Array**

```ini
function findMax(arr)
    max = arr[0]
    for i from 1 to length of arr - 1
        if arr[i] > max
            max = arr[i]
    return max
```

* **Type:** Linear, serial
* **Time Complexity:** O(n)

### 3. **Linear Search**

```ini
function linearSearch(arr, target)
    for i from 0 to length of arr - 1
        if arr[i] == target
            return i
    return -1
```

* **Type:** Linear search, serial
* **Time Complexity:** O(n)

### 4. **Bubble Sort**

```ini
function bubbleSort(arr)
    for i from 0 to length of arr - 1
        for j from 0 to length of arr - i - 2
            if arr[j] > arr[j + 1]
                swap arr[j] and arr[j + 1]
```

* **Type:** Sorting, serial
* **Time Complexity:** O(n²)

### 5. **Counting Even Numbers**

```ini
function countEvens(arr)
    count = 0
    for i from 0 to length of arr - 1
        if arr[i] mod 2 == 0
            count = count + 1
    return count
```

* **Type:** Linear, serial
* **Time Complexity:** O(n)

## When to Use Serial Algorithms

* When the dataset is small or operations are inexpensive.
* When the problem is inherently sequential (e.g., reading a book line by line).
* When hardware only supports single-threaded execution.
