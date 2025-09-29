# Frameworks & Tools for Python to C/C++ Integration

---

## 1. **Python C API (Lowest-level, Official)**

* **What it is:** Official API provided by CPython for writing C extensions.
* **How it works:** Write C code that directly interacts with Python objects and runtime.
* **Pros:** Maximum control, fastest possible performance.
* **Cons:** Verbose, error-prone, requires deep knowledge of CPython internals.
* **Use case:** Performance-critical extensions (e.g., NumPy core).
* **Example:**

  ```c
  #include <Python.h>
  static PyObject* say_hello(PyObject* self, PyObject* args) {
      const char* name;
      if (!PyArg_ParseTuple(args, "s", &name))
          return NULL;
      printf("Hello, %s!\n", name);
      Py_RETURN_NONE;
  }
  ```

---

## 2. **Cython**

* **What it is:** Superset of Python with optional C type annotations, compiled to C extensions.
* **Pros:** Easiest way to speed up Python code with minimal changes, supports mixing Python and C.
* **Cons:** Generates C code, so a compilation step is required.
* **Use case:** Scientific computing (SciPy, pandas, scikit-learn use it heavily).
* **Example:**

  ```python
  def add(int a, int b):
      return a + b
  ```

---

## 3. **SWIG (Simplified Wrapper and Interface Generator)**

* **What it is:** Generates Python bindings automatically from C/C++ header files.
* **Pros:** Automates wrapping of large C/C++ libraries, widely used.
* **Cons:** Generated code can be less Pythonic; harder to fine-tune.
* **Use case:** Wrapping existing large C/C++ projects (e.g., OpenCV used SWIG early on).
* **Workflow:** Write `.i` interface file → SWIG → auto-generate wrapper code.

---

## 4. **pybind11**

* **What it is:** Modern C++11 header-only library to expose C++ classes and functions to Python.
* **Pros:** Very clean, modern C++ syntax; integrates naturally with Python.
* **Cons:** Requires C++11 or newer; a bit more verbose than Cython for small functions.
* **Use case:** C++ heavy libraries (TensorFlow, PyTorch, etc. rely on this style).
* **Example:**

  ```cpp
  #include <pybind11/pybind11.h>
  int add(int i, int j) { return i + j; }
  PYBIND11_MODULE(example, m) {
      m.def("add", &add, "A function that adds two numbers");
  }
  ```

---

## 5. **Boost.Python**

* **What it is:** Part of the Boost C++ libraries for binding C++ with Python.
* **Pros:** Rich features, well-tested.
* **Cons:** Heavier dependency than pybind11, slower compile times.
* **Use case:** Legacy projects (before pybind11 became popular).
* **Note:** Pybind11 was actually inspired by Boost.Python but lighter.

---

## 6. **cffi (C Foreign Function Interface)**

* **What it is:** Pure Python module to call C functions directly from shared libraries.
* **Pros:** No compilation step if using ABI mode, simple FFI interface.
* **Cons:** Best for calling C functions, not full C++ classes.
* **Use case:** When you already have a C shared library (`.so`/`.dll`) and just need Python hooks.
* **Example:**

  ```python
  from cffi import FFI
  ffi = FFI()
  ffi.cdef("int add(int, int);")
  lib = ffi.dlopen("./libadd.so")
  print(lib.add(2, 3))
  ```

---

## 7. **ctypes (Standard Library)**

* **What it is:** Python built-in library to load and call C functions from DLLs/shared objects.
* **Pros:** No extra install; very lightweight.
* **Cons:** Manual, lower-level than `cffi`; doesn’t handle C++ well.
* **Use case:** Simple use cases where you just want to call a few C functions.
* **Example:**

  ```python
  import ctypes
  lib = ctypes.CDLL("./libadd.so")
  print(lib.add(2, 3))
  ```

---

## 8. **Numba (Alternative Approach)**

* **What it is:** JIT compiler (LLVM-based) for Python, not direct binding to C/C++.
* **Pros:** Speed without leaving Python, auto-compiles to native machine code.
* **Cons:** Less flexible for direct C++ integration.
* **Use case:** Speed up Python numeric/scientific code without C++ glue.

---

## Quick Comparison

| Tool         | Language | Level | Best for                            |
| ------------ | -------- | ----- | ----------------------------------- |
| Python C API | C        | Low   | Maximum control, CPython extensions |
| Cython       | Py + C   | Mid   | Speeding up Python code             |
| SWIG         | C/C++    | Auto  | Large legacy C++ codebases          |
| pybind11     | C++11+   | High  | Modern, clean C++ integration       |
| Boost.Python | C++      | High  | Legacy C++ projects                 |
| cffi         | C        | Mid   | Calling existing C libraries        |
| ctypes       | C        | Low   | Quick bindings, built-in            |
| Numba        | Python   | High  | JIT speedups without C++            |

---

In modern projects:

* **For C++ → Python:** `pybind11` is the most popular.
* **For Python with C speedups:** `Cython` or `Numba`.
* **For calling C libraries:** `cffi` (preferred over `ctypes`).
