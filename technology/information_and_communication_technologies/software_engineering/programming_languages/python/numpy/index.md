# NumPy

**NumPy (Numerical Python)** is an open-source Python library for numerical computing.
It provides:

* A powerful **n-dimensional array object** (`ndarray`)
* Mathematical operations optimized for **vectorized** computation
* Tools for **linear algebra**, **Fourier transforms**, **random numbers**, and more
* Interoperability with **C/C++**, **Fortran**, and libraries like **Pandas**, **SciPy**, and **PyTorch**

It’s the *core dependency* of most scientific libraries in Python — including PyTorch, TensorFlow, Pandas, OpenCV, and Scikit-learn.

---

## 2. Key Features of NumPy

| Category                                     | Description                                                               |
| -------------------------------------------- | ------------------------------------------------------------------------- |
| **High-performance multidimensional arrays** | Core `ndarray` object with fixed-type, homogeneous elements               |
| **Vectorized operations**                    | Apply operations over entire arrays without explicit loops                |
| **Broadcasting**                             | Automatic shape expansion for arithmetic between differently sized arrays |
| **Mathematical & statistical functions**     | Mean, variance, matrix multiplication, FFTs, etc.                         |
| **Random number generation**                 | Advanced RNG via `numpy.random`                                           |
| **Linear algebra**                           | Matrix operations (`dot`, `inv`, `eig`, etc.)                             |
| **Memory-efficient**                         | Compact storage, contiguous memory layout                                 |
| **Integration**                              | Works seamlessly with Pandas, SciPy, PyTorch, etc.                        |
| **Interfacing**                              | Data sharing with C/C++ via memory buffers                                |
| **Indexing & slicing**                       | Sophisticated element access and selection tools                          |

---

## 3. Installation and Import

```bash
pip install numpy
```

Then:

```python
import numpy as np
```

---

## 4. Core Object: `ndarray`

The **`numpy.ndarray`** is a homogeneous n-dimensional array of elements.

### Creating Arrays

```python
import numpy as np

# From Python lists
arr = np.array([1, 2, 3, 4])

# 2D array
mat = np.array([[1, 2], [3, 4]])

# Arrays of zeros, ones, or uninitialized data
zeros = np.zeros((2, 3))
ones = np.ones((3, 2))
empty = np.empty((2, 2))

# Range-based arrays
a = np.arange(0, 10, 2)   # [0, 2, 4, 6, 8]
b = np.linspace(0, 1, 5)  # 5 evenly spaced points between 0 and 1
```

### Array Attributes

```python
arr.shape     # Dimensions (rows, cols)
arr.ndim      # Number of dimensions
arr.size      # Total number of elements
arr.dtype     # Data type of elements
arr.itemsize  # Size of each element in bytes
```

---

## 5. Array Operations

### Element-wise Operations

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
a + b    # [5, 7, 9]
a * b    # [4, 10, 18]
a ** 2   # [1, 4, 9]
np.sqrt(a)
np.log(b)
```

### Aggregations

```python
arr = np.arange(9).reshape(3, 3)
arr.sum()
arr.mean()
arr.min(), arr.max()
arr.std(), arr.var()
arr.sum(axis=0)  # column-wise
arr.sum(axis=1)  # row-wise
```

---

## 6. Indexing, Slicing, and Iteration

### Basic Indexing

```python
arr = np.array([[10, 20, 30], [40, 50, 60]])
arr[0, 2]   # 30
arr[:, 1]   # [20, 50]
arr[1, :]   # [40, 50, 60]
```

### Slicing

```python
a = np.arange(10)
a[2:7]        # [2, 3, 4, 5, 6]
a[:5]         # [0, 1, 2, 3, 4]
a[::2]        # every other element
```

### Boolean / Fancy Indexing

```python
arr = np.array([10, 20, 30, 40, 50])
mask = arr > 25
arr[mask]         # [30, 40, 50]

idx = [0, 2, 4]
arr[idx]          # [10, 30, 50]
```

---

## 7. Broadcasting

NumPy automatically expands arrays of different shapes for compatible operations.

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])
a + b  # b is "broadcasted" across rows
```

Rules:

* Dimensions are compared from right to left.
* Dimensions are compatible when equal or one of them is 1.

---

## 8. Linear Algebra Operations

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 3]])

np.dot(A, B)        # Matrix multiplication
A @ B               # Same as dot
np.linalg.inv(A)    # Inverse
np.linalg.det(A)    # Determinant
np.linalg.eig(A)    # Eigenvalues/vectors
```

---

## 9. Random Number Generation

Using the new RNG API (`numpy.random.default_rng`):

```python
rng = np.random.default_rng(seed=42)

rng.random((2, 3))         # Uniform [0, 1)
rng.integers(0, 10, size=5)
rng.normal(0, 1, size=(2,2))  # Gaussian
rng.choice([1, 2, 3], size=5, replace=True)
```

---

## 10. Useful Utility Functions

| Function                                 | Purpose                            |
| ---------------------------------------- | ---------------------------------- |
| `np.unique(a)`                           | Unique elements of array           |
| `np.sort(a)`                             | Sort array                         |
| `np.concatenate([a, b])`                 | Join arrays                        |
| `np.vstack([a, b])`, `np.hstack([a, b])` | Stack vertically/horizontally      |
| `np.split(a, 3)`                         | Split into sub-arrays              |
| `np.reshape(a, (m, n))`                  | Change shape                       |
| `np.ravel()` / `np.flatten()`            | Flatten an array                   |
| `np.where(a > 0, 1, 0)`                  | Conditional element-wise selection |
| `np.isnan()`, `np.isinf()`               | Check for NaN/Inf values           |

---

## 11. Memory and Performance Tips

* Prefer **vectorized** operations over Python loops.
* Use **views** instead of copies (`a.view()` vs `a.copy()`).
* Use `np.float32` or `np.int32` for memory efficiency.
* Avoid repeatedly appending to arrays — preallocate with `np.zeros`.

---

## 12. NumPy in the ML Ecosystem

| Library                  | How it uses NumPy                                          |
| ------------------------ | ---------------------------------------------------------- |
| **Pandas**               | Built on top of NumPy arrays for tabular data              |
| **Matplotlib**           | Uses NumPy arrays for plotting data                        |
| **Scikit-learn**         | Inputs/outputs are NumPy arrays                            |
| **PyTorch / TensorFlow** | Their tensor APIs are modeled on NumPy                     |
| **OpenCV**               | Image data represented as NumPy arrays                     |
| **SciPy**                | Advanced math and scientific algorithms built around NumPy |

---

## 13. Real-World Example

### Linear Regression with NumPy

```python
import numpy as np

# Generate synthetic data
X = np.random.rand(100, 1)
y = 3*X + 2 + np.random.randn(100, 1) * 0.1

# Add bias term
X_b = np.c_[np.ones((100, 1)), X]

# Compute optimal weights using normal equation
theta_best = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y

print(theta_best)  # [bias, slope]
```

---

## 14. NumPy’s Role in PyTorch and Deep Learning

* PyTorch’s `torch.Tensor` was *designed to mimic NumPy arrays*.
* NumPy arrays can easily be converted:

  ```python
  import torch
  a = np.array([1, 2, 3])
  t = torch.from_numpy(a)
  back = t.numpy()
  ```
* Many preprocessing, feature extraction, and data handling steps in ML rely on NumPy before conversion to tensors.

---


## Array Creation & Indexing

### 1.1 Creating Arrays

```python
import numpy as np

# From lists
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])

# Zeros, ones, empty
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
empty = np.empty((2, 2))  # Uninitialized

# Ranges
arr1 = np.arange(0, 10, 2)   # [0, 2, 4, 6, 8]
arr2 = np.linspace(0, 1, 5)  # [0., 0.25, 0.5, 0.75, 1.]
```

### 1.2 Array Attributes

```python
arr = np.arange(12).reshape(3, 4)
print(arr.ndim)   # Number of dimensions
print(arr.shape)  # (3,4)
print(arr.size)   # Total number of elements
print(arr.dtype)  # Data type
```

### 1.3 Indexing & Slicing

```python
arr = np.array([[10, 20, 30], [40, 50, 60]])

# Basic indexing
print(arr[0, 1])     # 20
print(arr[:, 2])     # Column 2 → [30, 60]
print(arr[1, :])     # Row 1 → [40, 50, 60]

# Slicing
a = np.arange(10)
print(a[2:7])        # [2, 3, 4, 5, 6]
print(a[::-1])       # reverse → [9,8,...,0]
```

---

### **Mini Task:**

Create a 4×4 array of numbers from 0–15 and extract:

* The 2nd row
* The 3rd column
* A subarray of shape (2×2) from the bottom-right corner

---

## Vectorized Operations

### 2.1 Arithmetic Operations

```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(x + y)  # [5, 7, 9]
print(x * y)  # [4, 10, 18]
print(x ** 2) # [1, 4, 9]
print(np.exp(x))
```

### 2.2 Comparison and Logical Operations

```python
a = np.array([1, 2, 3, 4, 5])
print(a > 3)         # [False, False, False, True, True]
print(np.any(a > 4)) # True
print(np.all(a < 10))# True
```

### 2.3 Aggregation Functions

```python
arr = np.arange(9).reshape(3, 3)

print(arr.sum())
print(arr.mean(axis=0))  # Column-wise mean
print(arr.max(axis=1))   # Row-wise max
```

---

### **Mini Task:**

Create a random 3×3 matrix and compute:

* Column-wise and row-wise mean
* Standard deviation of the entire matrix
* Normalize the matrix so all values are between 0 and 1

---

## Broadcasting

Broadcasting allows operations between arrays of **different shapes**.

```python
A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([10, 20, 30])

# B is broadcasted across rows
print(A + B)
```

### Example: Normalization using Broadcasting

```python
X = np.random.randint(1, 10, (3, 3))
X_min = X.min(axis=0)
X_max = X.max(axis=0)
X_norm = (X - X_min) / (X_max - X_min)
```

---

### **Mini Task:**

Given `arr = np.arange(12).reshape(3,4)`, subtract the mean of each column from that column (use broadcasting).

---

## Linear Algebra

### 4.1 Matrix Multiplication

```python
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print(A @ B)        # Matrix multiplication
print(np.dot(A, B)) # Same
```

### 4.2 Transpose & Inverse

```python
A = np.array([[1, 2], [3, 4]])
print(A.T)                 # Transpose
print(np.linalg.inv(A))    # Inverse
```

### 4.3 Determinant, Eigenvalues

```python
np.linalg.det(A)
eigvals, eigvecs = np.linalg.eig(A)
```

### 4.4 Solving Systems of Equations

Solving `Ax = b`

```python
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(A, b)
```

---

### **Mini Task:**

Let
[
A = \begin{bmatrix}2 & 1 \ 1 & 3\end{bmatrix}, \quad b = \begin{bmatrix}1 \ 2\end{bmatrix}
]
Find `x` using `np.linalg.solve`.

---

## Random Numbers & Statistics

### 5.1 Random Array Generation

```python
rng = np.random.default_rng(seed=42)

print(rng.random((2,3)))      # Uniform [0,1)
print(rng.integers(0, 10, 5)) # Random ints
print(rng.normal(0, 1, (2,2)))# Gaussian
```

### 5.2 Statistical Functions

```python
data = rng.normal(50, 10, 1000)
print(np.mean(data))
print(np.median(data))
print(np.std(data))
print(np.var(data))
```

### 5.3 Sampling & Permutation

```python
items = np.array([10, 20, 30, 40, 50])
print(rng.choice(items, size=3, replace=False))
```

---

### **Mini Task:**

Simulate 1,000 dice rolls using `rng.integers(1, 7, 1000)`.
Compute:

* Mean, variance, and probability of rolling a 6.

---

## Real-World Applications

### 6.1 Data Normalization

```python
data = np.random.randint(0, 255, (5, 5))
data_norm = (data - data.min()) / (data.max() - data.min())
```

### 6.2 Polynomial Fitting (Curve Fitting)

```python
x = np.linspace(0, 10, 50)
y = 3*x**2 + 2*x + 1 + np.random.randn(50) * 5

coeffs = np.polyfit(x, y, 2)
poly = np.poly1d(coeffs)

print(poly(5))  # Evaluate polynomial at x=5
```

### 6.3 Linear Regression with Normal Equation

```python
X = np.random.rand(100, 1)
y = 3*X + 2 + np.random.randn(100, 1)*0.1

# Add bias term
X_b = np.c_[np.ones((100, 1)), X]
theta_best = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
print(theta_best)
```

---

### **Mini Project Idea:**

* Generate synthetic 2D data (x, y).
* Fit a linear regression model using NumPy.
* Visualize the regression line (with `matplotlib`).
