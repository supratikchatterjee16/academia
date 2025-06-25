# Recursion Algorithms

A recursion algorithm is an algorithm that solves a problem by calling itself with a smaller or simpler version of the original problem. This process continues until it reaches a base case — a condition that stops the recursion.

## Examples

### 1. **Factorial of a Number**

**Problem:** Compute `n!` (n factorial)

**Pseudocode:**

```pseudocode
function factorial(n)
    if n == 0 or n == 1
        return 1
    else
        return n * factorial(n - 1)
```

---

### 2. **Fibonacci Sequence**

**Problem:** Return the nth Fibonacci number.

**Pseudocode:**

```pseudocode
function fibonacci(n)
    if n == 0
        return 0
    else if n == 1
        return 1
    else
        return fibonacci(n - 1) + fibonacci(n - 2)
```

---

### 3. **Sum of Elements in an Array**

**Problem:** Return the sum of all elements in an array `arr` of size `n`.

**Pseudocode:**

```pseudocode
function sumArray(arr, n)
    if n == 0
        return 0
    else
        return arr[n - 1] + sumArray(arr, n - 1)
```

---

### 4. **Reverse a String**

**Problem:** Reverse a string using recursion.

**Pseudocode:**

```pseudocode
function reverseString(s)
    if length of s <= 1
        return s
    else
        return reverseString(s[1:]) + s[0]
```

---

### 5. **Binary Search**

**Problem:** Search for a target value in a sorted array using recursion.

**Pseudocode:**

```pseudocode
function binarySearch(arr, target, left, right)
    if left > right
        return -1
    mid = (left + right) / 2
    if arr[mid] == target
        return mid
    else if target < arr[mid]
        return binarySearch(arr, target, left, mid - 1)
    else
        return binarySearch(arr, target, mid + 1, right)
```

---

### 6. **Tower of Hanoi**

**Problem:** Move `n` disks from source rod to destination rod using an auxiliary rod.

**Pseudocode:**

```pseudocode
function towerOfHanoi(n, source, destination, auxiliary)
    if n == 1
        print "Move disk 1 from " + source + " to " + destination
        return
    towerOfHanoi(n - 1, source, auxiliary, destination)
    print "Move disk " + n + " from " + source + " to " + destination
    towerOfHanoi(n - 1, auxiliary, destination, source)
```
