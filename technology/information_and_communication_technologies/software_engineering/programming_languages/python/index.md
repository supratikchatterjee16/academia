# Python

Python is a **high-level, interpreted, general-purpose programming language** known for its simplicity, readability, and versatility. It supports multiple paradigms, including **object-oriented, procedural, and functional programming**. Because of its clean syntax and rich ecosystem, Python is widely used in web development, data science, artificial intelligence, automation, and more.

## History of Python

* **Late 1980s** – Developed by **Guido van Rossum** at **Centrum Wiskunde & Informatica (CWI), Netherlands**.
* **1991** – First public release: **Python 0.9.0**, which already included modules, exceptions, functions, and core data types (str, list, dict).
* Named after the British comedy series **“Monty Python’s Flying Circus”**, not the snake.

## Major Python Versions & Key Features

### **Python 1.x (1991 – 2000)**

* First stable release: **Python 1.0 (1994)**.
* Key features: functions, exceptions, core data types, and modules.
* Early focus on extensibility and portability.

### **Python 2.x (2000 – 2020)**

* Released in **2000** with many improvements, but also some design flaws.
* Major features:

  * **List comprehensions**.
  * **Garbage collection via reference counting & cycles**.
  * **Unicode support** (limited in 2.x).
* **Python 2.7 (2010)** became the last release in the 2.x line.
* Official support ended on **January 1, 2020**.

### **Python 3.x (2008 – present)**

* Released in **2008**, not backward-compatible with Python 2.
* Major features and changes:

  * **print() function** replaces `print` statement.
  * **Unicode by default** (all strings are Unicode).
  * **Integer division change**: `/` gives float, `//` gives integer.
  * **Function annotations** for better readability and typing support.
  * **Async/await** keywords (introduced in Python 3.5).
  * **F-strings** (formatted string literals, introduced in 3.6).
  * **Type hinting improvements** (gradually added).
  * **Pattern matching** (introduced in 3.10).
  * **Performance optimizations** (especially in Python 3.11+).

## Features

### 1. **Print as a Function**

```python
# Python 3
print("Hello, World!")

# Python 2 (invalid in Python 3)
# print "Hello, World!"
```

### 2. **Unicode by Default**

```python
text = "こんにちは"  # Japanese for "Hello"
print(text)  # Strings are Unicode by default in Python 3
```

### 3. **Integer Division Change**

```python
print(5 / 2)   # 2.5  (float division)
print(5 // 2)  # 2    (integer division)
```

### 4. **Function Annotations / Type Hints**

```python
def greet(name: str, age: int) -> str:
    return f"Hello, {name}. You are {age} years old."

print(greet("Alice", 25))
```

### 5. **Generators with `yield`**

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i  # Produces values one at a time
        i += 1

for number in count_up_to(5):
    print(number)
```

### 6. **Async / Await (Asynchronous Programming)**

```python
import asyncio

async def say_hello():
    await asyncio.sleep(1)
    print("Hello after 1 second")

asyncio.run(say_hello())
```

### 7. **F-Strings (Formatted String Literals)**

```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
```

### 8. **Improved Iteration with `enumerate` and `zip`**

```python
fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)

colors = ["red", "yellow", "purple"]
for fruit, color in zip(fruits, colors):
    print(f"{fruit} is {color}")
```

### 9. **Unpacking in Assignments**

```python
a, b, *rest = [1, 2, 3, 4, 5]
print(a, b, rest)  # 1 2 [3, 4, 5]
```

### 10. **Pattern Matching (Python 3.10+)**

```python
def match_example(value):
    match value:
        case 0:
            return "Zero"
        case 1 | 2:
            return "One or Two"
        case _:
            return "Something else"

print(match_example(2))   # One or Two
```

### 11. **Walrus Operator (`:=`, Python 3.8+)**

```python
# Assignment inside expression
if (n := len("Python")) > 3:
    print(f"Length is {n}")
```

### 12. **Dictionary Comprehensions**

```python
squares = {x: x*x for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### 13. **Set Comprehensions**

```python
unique = {x for x in "banana"}
print(unique)  # {'a', 'n', 'b'}
```

### 14. **Context Managers (`with`)**

```python
with open("example.txt", "w") as f:
    f.write("Hello, file!")
```

### 15. **Exception Handling with `as`**

```python
try:
    1 / 0
except ZeroDivisionError as e:
    print("Error:", e)
```

### 16. **Extended Iterable Unpacking (PEP 3132)**

```python
first, *middle, last = [1, 2, 3, 4, 5]
print(first, middle, last)  # 1 [2, 3, 4] 5
```

### 17. **Named Expressions in Loops**

```python
data = ["apple", "banana", "cherry"]
while (item := data.pop(0)) != "cherry":
    print(item)
```

### 18. **Improved Performance in Recent Versions (3.11+)**

Try running the following with older versions and with versions with 3.11+:

```
import time

# Example 1: Function calls (faster in 3.11+)
def add(a, b):
    return a + b

def benchmark_func_calls(n=10_000_00):
    for _ in range(n):
        add(1, 2)

# Example 2: Exception handling (optimized in 3.11+)
def benchmark_exceptions(n=100_000):
    for _ in range(n):
        try:
            raise ValueError("test")
        except ValueError:
            pass

# Example 3: Nested loops (general interpreter speedup)
def benchmark_loops(n=1_000_000):
    s = 0
    for i in range(n):
        s += i
    return s

# Run benchmarks
start = time.time()
benchmark_func_calls()
print("Function calls:", time.time() - start, "seconds")

start = time.time()
benchmark_exceptions()
print("Exceptions:", time.time() - start, "seconds")

start = time.time()
benchmark_loops()
print("Loops:", time.time() - start, "seconds")
```

### List comprehensions

#### 1. Square numbers

```python
squares = [x*x for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

---

#### 2. Filtering with a condition

```python
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]
```

---

#### 3. Applying a function

```python
words = ["hello", "world", "python"]
uppercased = [w.upper() for w in words]
print(uppercased)  # ['HELLO', 'WORLD', 'PYTHON']
```

#### 4. Cartesian product

```python
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(pairs)  # [(1, 3), (1, 4), (2, 3), (2, 4)]
```

---

#### 5. Flatten a matrix

```python
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6]
```

#### 6. Inline if-else

```python
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)  # ['even', 'odd', 'even', 'odd', 'even']
```

---

#### 7. Remove vowels from a string

```python
text = "comprehension"
no_vowels = [ch for ch in text if ch not in "aeiou"]
print(no_vowels)  # ['c', 'm', 'p', 'r', 'h', 'n', 's', 'n']
```

---

#### 8. Transpose a matrix

```python
matrix = [[1, 2, 3], [4, 5, 6]]
transpose = [[row[i] for row in matrix] for i in range(3)]
print(transpose)  # [[1, 4], [2, 5], [3, 6]]
```

---

#### 9. Set and Dictionary Comprehensions (related feature)

```python
# Set comprehension
unique = {x % 3 for x in range(10)}
print(unique)  # {0, 1, 2}

# Dict comprehension
squares_dict = {x: x*x for x in range(5)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

## Advanced Features

### 1. **Decorators** (Functions that modify other functions/classes)

```python
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@debug
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))
```

### 2. **Generators and `yield`** (Lazy evaluation, efficient iteration)

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(10)))
```

### 3. **Context Managers (`with`) & `__enter__` / `__exit__`**

```python
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, "w")
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with ManagedFile("test.txt") as f:
    f.write("Hello, world!")
```

### 4. **Metaclasses** (Classes that create classes)

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass
```

### 5. **Descriptors** (Custom attribute access)

```python
class Celsius:
    def __get__(self, instance, owner):
        return instance._celsius
    def __set__(self, instance, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        instance._celsius = value

class Temperature:
    celsius = Celsius()

t = Temperature()
t.celsius = 25
print(t.celsius)  # 25
```

### 6. **Coroutines (`async` / `await`)**

```python
import asyncio

async def main():
    await asyncio.sleep(1)
    print("Done after 1 second")

asyncio.run(main())
```

### 7. **Pattern Matching (Python 3.10+)**

```python
def handle(data):
    match data:
        case {"type": "error", "msg": msg}:
            print(f"Error: {msg}")
        case {"type": "success", "value": v}:
            print(f"Success: {v}")
        case _:
            print("Unknown")

handle({"type": "error", "msg": "File not found"})
```

### 8. **Multiple Inheritance & MRO (Method Resolution Order)**

```python
class A: 
    def hello(self): print("A")
class B(A): 
    def hello(self): print("B")
class C(A): 
    def hello(self): print("C")
class D(B, C): 
    pass

D().hello()        # B (follows MRO: D → B → C → A)
print(D.mro())     # Method Resolution Order
```

### 9. **Dynamic Code Execution (`eval`, `exec`)**

```python
code = "x = 5\ny = 10\nprint(x + y)"
exec(code)   # Runs dynamically
```

### 10. **Property Decorator (`@property`)**

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def area(self):
        return 3.14 * self._radius ** 2

c = Circle(5)
print(c.area)  # 78.5
```

### 11. **Monkey Patching (Changing behavior at runtime)**

```python
class Person:
    def say_hello(self):
        print("Hello!")

def new_hello(self):
    print("Hi there!")

Person.say_hello = new_hello
p = Person()
p.say_hello()  # Hi there!
```

### 12. **Closures (Functions inside functions)**

```python
def multiplier(factor):
    def inner(x):
        return x * factor
    return inner

double = multiplier(2)
print(double(5))  # 10
```

### 13. **Slots (`__slots__`) for Memory Optimization**

```python
class Point:
    __slots__ = ("x", "y")  # Prevents dict overhead
    def __init__(self, x, y):
        self.x, self.y = x, y

p = Point(1, 2)
print(p.x, p.y)
```

### 14. **Operator Overloading (`__add__`, `__str__`, etc.)**

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # (4, 6)
```
