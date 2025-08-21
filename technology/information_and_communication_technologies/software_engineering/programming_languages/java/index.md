# Java

## History of Java

* **Early 1990s** – James Gosling and his team at Sun Microsystems began the **“Green Project”**, creating a language called **Oak** for interactive TV and embedded devices.
* **1995** – Oak was renamed **Java** and officially released by Sun Microsystems.
* **1996** – Java 1.0 was released, with the slogan *“Write Once, Run Anywhere” (WORA)* thanks to the **Java Virtual Machine (JVM)**.
* **2009** – Sun Microsystems was acquired by **Oracle Corporation**, which has maintained Java since.
* Today, Java remains one of the most widely used programming languages for enterprise software, Android apps, cloud computing, and more.

---

## Java Versions (Major Releases)

Here’s a **timeline of major Java versions** and key features:

1. **JDK 1.0 (1996)** – Initial release, applets, AWT.
2. **JDK 1.1 (1997)** – Inner classes, JDBC, RMI.
3. **J2SE 1.2 (1998)** – Swing, Collections Framework.
4. **J2SE 1.3 (2000)** – HotSpot JVM, JavaSound.
5. **J2SE 1.4 (2002)** – assert, NIO, logging API.
6. **J2SE 5.0 (2004)** – Generics, Annotations, Enum, Autoboxing, varargs, enhanced for-loop.
7. **Java SE 6 (2006)** – Scripting, Compiler API, improvements in GUI & Web services.
8. **Java SE 7 (2011)** – try-with-resources, diamond operator, NIO.2.
9. **Java SE 8 (2014)** – **Biggest update**: Lambda expressions, Streams API, Default methods in interfaces, Functional interfaces, Optional, Date & Time API.
10. **Java SE 9 (2017)** – Module System (Project Jigsaw), JShell (REPL).
11. **Java SE 10 (2018)** – `var` keyword (local variable type inference).
12. **Java SE 11 (2018, LTS)** – New string methods, HTTP client API, long-term support.
13. **Java SE 12–15 (2019–2020)** – Switch expressions, Text blocks, Records (preview), Pattern matching.
14. **Java SE 17 (2021, LTS)** – Sealed classes, Pattern matching, Strong encapsulation, LTS release.
15. **Java SE 18–20 (2022–2023)** – Simple web server, switch pattern matching, record patterns, virtual threads (preview).
16. **Java SE 21 (2023, LTS)** – Virtual threads (Project Loom), String templates, Sequenced collections.

## Object Oriented Programming with Java

This is the core paradigm in Java.

Short form to remember core structures - **EAPI**

### 1. Encapsulation

**Definition:**
Encapsulation is the process of bundling **data (fields)** and **methods** that operate on the data into a single unit (a class), while restricting direct access to some components. It hides the internal state and allows controlled access through **getters and setters**.

**How Java does it:**

* Use **private** variables to restrict direct access.
* Use **public getter and setter methods** to provide controlled access.

**Example:**

```java
class Person {
    private String name;  // private field (hidden from outside)

    // Getter
    public String getName() {
        return name;
    }

    // Setter
    public void setName(String name) {
        this.name = name;
    }
}

public class Main {
    public static void main(String[] args) {
        Person p = new Person();
        p.setName("Alice");  // controlled access
        System.out.println(p.getName());
    }
}
```

---

### 2. Abstraction

**Definition:**
Abstraction is the process of **hiding implementation details** and showing only the **essential features** of an object.

**How Java does it:**

* With **abstract classes** (can have abstract and concrete methods).
* With **interfaces** (specify behavior but don’t provide implementation).

**Example using abstract class:**

```java
abstract class Animal {
    abstract void makeSound();  // abstract method (no implementation)

    public void sleep() {
        System.out.println("Sleeping...");
    }
}

class Dog extends Animal {
    public void makeSound() {
        System.out.println("Bark");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal a = new Dog();  // abstraction
        a.makeSound();         // Bark
        a.sleep();             // Sleeping...
    }
}
```

---

### 3. Polymorphism

**Definition:**
Polymorphism means **"many forms"** — the ability of an object to take different forms.
Java supports:

* **Compile-time polymorphism (Method Overloading)**
* **Runtime polymorphism (Method Overriding)**

**Example (Overriding – runtime polymorphism):**

```java
class Animal {
    void makeSound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    void makeSound() {
        System.out.println("Dog barks");
    }
}

class Cat extends Animal {
    void makeSound() {
        System.out.println("Cat meows");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal a1 = new Dog();
        Animal a2 = new Cat();

        a1.makeSound();  // Dog barks
        a2.makeSound();  // Cat meows
    }
}
```

---

### 4. Inheritance

**Definition:**
Inheritance is the mechanism where one class (child) **acquires properties and behaviors** of another class (parent).

**How Java does it:**

* Use the `extends` keyword for classes.
* Use the `implements` keyword for interfaces.

**Example:**

```java
class Vehicle {
    String brand = "Ford";
    
    void honk() {
        System.out.println("Beep beep!");
    }
}

class Car extends Vehicle {  // Car inherits from Vehicle
    String model = "Mustang";
}

public class Main {
    public static void main(String[] args) {
        Car c = new Car();
        c.honk(); // Inherited from Vehicle
        System.out.println(c.brand + " " + c.model);
    }
}
```

---

## Functional Programming with Java

### The Type of a Lambda Expression

A lambda expression in Java is a concise way to represent an implementation of a functional interface (an interface with a single abstract method) using an inline block of code.

It uses the notations:
```java
(parameters) -> expression
(parameters) -> { statements }
```

This can take the following forms:
| Notation                         | Example                                      | Meaning                                      |
| -------------------------------- | -------------------------------------------- | -------------------------------------------- |
| **No parameters**                | `() -> 42`                                   | A function that takes nothing, returns `42`. |
| **Single parameter (no type)**   | `x -> x * 2`                                 | Takes one parameter `x`, returns `x * 2`.    |
| **Single parameter (with type)** | `(int x) -> x * 2`                           | Explicitly declares type.                    |
| **Multiple parameters**          | `(a, b) -> a + b`                            | Takes two parameters, returns sum.           |
| **With multiple statements**     | `(x, y) -> { int sum = x + y; return sum; }` | Block body, must use `return`.               |
| **Void body**                    | `(s) -> System.out.println(s)`               | Performs action, returns nothing.            |

In Java, a **lambda expression itself does not have a concrete type like `class` or `interface`**.
Instead, its type is inferred from the **context** in which it is used.

Specifically:
👉 A lambda expression’s type is a **functional interface** (an interface with exactly one abstract method, marked by `@FunctionalInterface`).

---

#### Example

```java
Runnable r = () -> System.out.println("Hello");
```

* Here, `() -> System.out.println("Hello")` is a **lambda expression**.
* Its type is inferred as `Runnable` because `Runnable` has exactly one abstract method:

  ```java
  void run();
  ```

---

```java
Comparator<String> cmp = (a, b) -> a.length() - b.length();
```

* Type of `(a, b) -> a.length() - b.length()` is `Comparator<String>`,
  because `Comparator` has a single abstract method:

  ```java
  int compare(T o1, T o2);
  ```

---

#### Generic Lambdas

```java
Function<Integer, String> f = i -> "Value: " + i;
```

* Here, the lambda type is `Function<Integer, String>`.
* The compiler ensures the parameter type (`Integer`) and return type (`String`) match the `apply` method of `Function<T,R>`.

---

#### Key Point

* Lambda expressions in Java are **not objects of their own class**.
* They are **compiled to instances of functional interfaces**, often implemented via invokedynamic (JVM-level optimization).

---

#### Summary Table

| Example                          | Functional Interface Type                                   |
| -------------------------------- | ----------------------------------------------------------- |
| `() -> System.out.println("Hi")` | `Runnable`                                                  |
| `(a, b) -> a + b`                | `BinaryOperator<T>` or `Comparator<T>` depending on context |
| `s -> s.length()`                | `Function<String, Integer>`                                 |
| `x -> x > 10`                    | `Predicate<Integer>`                                        |
| `() -> 42`                       | `Supplier<Integer>`                                         |

### Functional Interface

In Java, a functional interface is an interface with:

- Exactly one abstract method
- Annotated with `@FunctionalInterface` annotation(this is optional, but recommended)
- Can have default and static methods

### Core Functional Interfaces

The functional interfaces provided by Java are(Abbrevation to remember **PFCSO**):

- Predicate - return boolean values
    - `Predicate&ltT&gt`
    - `BiPredicate&ltT, U&gt`(takes 2 inputs)
    - abstract function: `boolean test(T t, U... u)`, here `...` is used as standin for "also"
- Function - Take an input, and provide a definite replicable output based on it. Return type needs to be specified.
    - `Function&ltT, R&gt`, R is the return type, and T is the input type
    - `BiFunction&ltT, U, R&gt`, U is the second input type
    - abstract function: `T apply(T t, U... u)`
- Consumer - Take input, without any outputs.
    - `Consumer&ltT&gt`
    - `BiConsumer&ltT, U&gt`
    - abstract function: `void accept(T t, U... u)`
- Supplier - Provide output
    - `Supplier&ltT&gt`
    - abstract function: `T get()`
- Operator - Operate on the same datatype, providing an output of the same type
    - `UnaryOperator&ltT&gt`
    - `BinaryOperator&ltT&gt`
    - abstract function: `T apply(T t1, T... t2)`

To avoid boxing/unboxing overhead:
- IntFunction, LongFunction, DoubleFunction
- ToIntFunction&ltT&gt, ToLongFunction&ltT&gt, ToDoubleFunction&ltT&gt
- IntPredicate, LongPredicate, DoublePredicate
- IntConsumer, LongConsumer, DoubleConsumer
- IntSupplier, LongSupplier, DoubleSupplier
- IntUnaryOperator, IntBinaryOperator (and for Long/Double)

### Streams API

The Java Streams API, utilizes functional programming heavily.

Here’s a structured guide you can use as a reference:

### 1. Creating Streams

| Source                                      | How to Get Stream                                                           | Notes                                                       |
| ------------------------------------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------- |
| `Collection` (`List`, `Set`, `Queue`, etc.) | `collection.stream()` or `collection.parallelStream()`                      | All **collections** support `.stream()` (since Java 8).     |
| `Map<K,V>`                                  | `map.entrySet().stream()`, `map.keySet().stream()`, `map.values().stream()` | `Map` itself has no `.stream()`, but its views do.          |
| Arrays                                      | `Arrays.stream(array)` or `Stream.of(array)`                                | For primitives: `IntStream.of()`, `DoubleStream.of()`, etc. |
| Stream factory                              | `Stream.of(...)`, `Stream.generate(...)`, `Stream.iterate(...)`             | Useful for programmatic generation.                         |
| Files / I/O                                 | `Files.lines(Path)`, `BufferedReader.lines()`                               | Returns `Stream<String>`.                                   |
| Primitive streams                           | `IntStream.range()`, `LongStream.rangeClosed()`                             | Specialized for primitives (avoid boxing overhead).         |

---

### 2. Stream Operations Categories

#### A) **Intermediate Operations** (return a `Stream` — lazy)

| Operation                          | Accepted Types          | Return Type    | Purpose                                           |
| ---------------------------------- | ----------------------- | -------------- | ------------------------------------------------- |
| `filter(Predicate<T>)`             | `Predicate<T>`          | `Stream<T>`    | Keep elements matching condition.                 |
| `map(Function<T,R>)`               | `Function<T,R>`         | `Stream<R>`    | Transform elements.                               |
| `mapToInt(ToIntFunction<T>)`       | `ToIntFunction<T>`      | `IntStream`    | Map to primitive int stream.                      |
| `mapToLong(ToLongFunction<T>)`     | `ToLongFunction<T>`     | `LongStream`   | Map to primitive long stream.                     |
| `mapToDouble(ToDoubleFunction<T>)` | `ToDoubleFunction<T>`   | `DoubleStream` | Map to primitive double stream.                   |
| `flatMap(Function<T,Stream<R>>)`   | `Function<T,Stream<R>>` | `Stream<R>`    | Flatten nested streams.                           |
| `distinct()`                       | –                       | `Stream<T>`    | Remove duplicates (uses `equals()`/`hashCode()`). |
| `sorted()`                         | –                       | `Stream<T>`    | Natural order sort.                               |
| `sorted(Comparator<T>)`            | `Comparator<T>`         | `Stream<T>`    | Custom order sort.                                |
| `peek(Consumer<T>)`                | `Consumer<T>`           | `Stream<T>`    | Debug/log elements, does not modify stream.       |
| `limit(long n)`                    | –                       | `Stream<T>`    | Take first `n` elements.                          |
| `skip(long n)`                     | –                       | `Stream<T>`    | Skip first `n` elements.                          |

---

#### B) **Terminal Operations** (consumes stream)

| Operation                                                          | Accepted Types         | Return Type   | Purpose                                     |
| ------------------------------------------------------------------ | ---------------------- | ------------- | ------------------------------------------- |
| `forEach(Consumer<T>)`                                             | `Consumer<T>`          | `void`        | Perform action on each element.             |
| `forEachOrdered(Consumer<T>)`                                      | `Consumer<T>`          | `void`        | Respect encounter order (parallel streams). |
| `toArray()`                                                        | –                      | `Object[]`    | Collect to array.                           |
| `toArray(IntFunction<A[]>)`                                        | Array constructor      | `A[]`         | Collect to typed array.                     |
| `reduce(BinaryOperator<T>)`                                        | `BinaryOperator<T>`    | `Optional<T>` | Reduce elements to one.                     |
| `reduce(T identity, BinaryOperator<T>)`                            | Identity + op          | `T`           | Reduce with identity.                       |
| `reduce(U identity, BiFunction<U,? super T,U>, BinaryOperator<U>)` | Accumulator + combiner | `U`           | Mutable reduction.                          |
| `collect(Collector<T,A,R>)`                                        | `Collector`            | `R`           | Collect to container (List, Set, Map, etc). |
| `min(Comparator<T>)`                                               | `Comparator<T>`        | `Optional<T>` | Minimum element.                            |
| `max(Comparator<T>)`                                               | `Comparator<T>`        | `Optional<T>` | Maximum element.                            |
| `count()`                                                          | –                      | `long`        | Number of elements.                         |
| `anyMatch(Predicate<T>)`                                           | `Predicate<T>`         | `boolean`     | Any element matches.                        |
| `allMatch(Predicate<T>)`                                           | `Predicate<T>`         | `boolean`     | All elements match.                         |
| `noneMatch(Predicate<T>)`                                          | `Predicate<T>`         | `boolean`     | No element matches.                         |
| `findFirst()`                                                      | –                      | `Optional<T>` | First element (encounter order).            |
| `findAny()`                                                        | –                      | `Optional<T>` | Any element (esp. parallel streams).        |

---

#### C) **Short-Circuiting Operations**

(Special subset of terminal ops that may stop early)

| Operation     | Return Type   | Example                 |
| ------------- | ------------- | ----------------------- |
| `findFirst()` | `Optional<T>` | Stop after first match. |
| `findAny()`   | `Optional<T>` | Stop after any match.   |
| `anyMatch()`  | `boolean`     | Stop after finding one. |
| `allMatch()`  | `boolean`     | Stop after failure.     |
| `noneMatch()` | `boolean`     | Stop after success.     |
| `limit(n)`    | `Stream<T>`   | Restricts traversal.    |

---

### 3. Collectors (via `collect()`)

| Collector                                        | Return Type            | Purpose                    |
| ------------------------------------------------ | ---------------------- | -------------------------- |
| `Collectors.toList()`                            | `List<T>`              | Collect into `List`.       |
| `Collectors.toSet()`                             | `Set<T>`               | Collect into `Set`.        |
| `Collectors.toMap(Function<T,K>, Function<T,V>)` | `Map<K,V>`             | Collect into map.          |
| `Collectors.groupingBy(Function<T,K>)`           | `Map<K,List<T>>`       | Group by classifier.       |
| `Collectors.partitioningBy(Predicate<T>)`        | `Map<Boolean,List<T>>` | Partition true/false.      |
| `Collectors.joining(CharSequence)`               | `String`               | Concatenate strings.       |
| `Collectors.summarizingInt(ToIntFunction<T>)`    | `IntSummaryStatistics` | Count, min, max, sum, avg. |
| `Collectors.counting()`                          | `Long`                 | Count elements.            |
| `Collectors.reducing(...)`                       | `Optional<T>`/`T`      | General reduction.         |

---

### 4. Which Collections Need `.stream()`?

| Collection Type                             | `.stream()` Support | Notes                                                         |
| ------------------------------------------- | ------------------- | ------------------------------------------------------------- |
| `Collection` (`List`, `Set`, `Queue`, etc.) | ✅ Yes               | Direct `.stream()` available.                                 |
| `Map`                                       | ❌ No                | Must use `map.entrySet()`, `map.keySet()`, or `map.values()`. |
| Arrays                                      | ❌ No                | Use `Arrays.stream(array)` or `Stream.of(array)`.             |
| Primitive arrays (`int[]`, etc.)            | ❌ No                | Use `Arrays.stream(int[])` → `IntStream`.                     |

---

### 5. Example End-to-End

```java
List<String> names = List.of("Alice", "Bob", "Charlie", "David");

Map<Integer, List<String>> grouped = names.stream()
    .filter(n -> n.length() > 3)                // intermediate
    .map(String::toUpperCase)                   // intermediate
    .sorted()                                   // intermediate
    .collect(Collectors.groupingBy(String::length)); // terminal

System.out.println(grouped);
```


## Concurrency Patterns

Java provides a **rich set of features and APIs** to implement concurrency patterns, enabling programs to perform multiple tasks **simultaneously** while handling synchronization, scalability, and performance. Here’s a detailed breakdown:

---

## **1. Threads and Runnable**

* **Basic concurrency building blocks**.
* `Thread` class: Represents an independent path of execution.
* `Runnable` interface: Encapsulates a task to be executed by a thread.

**Example:**

```java
class MyTask implements Runnable {
    public void run() {
        System.out.println("Task running in " + Thread.currentThread().getName());
    }
}

public class Main {
    public static void main(String[] args) {
        Thread t = new Thread(new MyTask());
        t.start();  // starts a new thread
    }
}
```

---

## **2. Executor Framework**

* Provides **thread pools** to manage and reuse threads efficiently.
* **Interfaces/classes:** `Executor`, `ExecutorService`, `ScheduledExecutorService`.

**Example:**

```java
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) throws Exception {
        ExecutorService executor = Executors.newFixedThreadPool(2);
        executor.submit(() -> System.out.println("Task executed by thread pool"));
        executor.shutdown();
    }
}
```

* **Advantages:** avoids creating too many threads, improves performance, and simplifies task submission.

---

## **3. Synchronization & Locks**

* Java provides **intrinsic locks** (`synchronized`) and **explicit locks** (`ReentrantLock`) to coordinate access to shared resources.

**Example:**

```java
class Counter {
    private int count = 0;

    public synchronized void increment() {
        count++;
    }

    public int getCount() {
        return count;
    }
}
```

* `synchronized` ensures **mutual exclusion**, preventing race conditions.

---

## **4. Concurrent Collections**

* **Thread-safe collections** in `java.util.concurrent` package:

  * `ConcurrentHashMap`
  * `CopyOnWriteArrayList`
  * `BlockingQueue` (like `ArrayBlockingQueue`, `LinkedBlockingQueue`)

**Example:**

```java
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) {
        BlockingQueue<String> queue = new LinkedBlockingQueue<>();
        queue.add("Hello");
    }
}
```

---

## **5. Atomic Variables**

* **Lock-free thread-safe operations** for single variables.
* Classes in `java.util.concurrent.atomic`:

  * `AtomicInteger`, `AtomicBoolean`, `AtomicReference`

**Example:**

```java
import java.util.concurrent.atomic.AtomicInteger;

AtomicInteger counter = new AtomicInteger(0);
counter.incrementAndGet();  // thread-safe increment
```

---

## **6. Fork/Join Framework**

* Designed for **divide-and-conquer algorithms**.
* Breaks tasks into smaller subtasks and processes them in parallel.

**Example:**

```java
import java.util.concurrent.*;

class MyTask extends RecursiveTask<Integer> {
    int n;
    MyTask(int n) { this.n = n; }
    protected Integer compute() {
        if (n <= 1) return n;
        MyTask t1 = new MyTask(n-1);
        t1.fork(); // asynchronously
        return n + t1.join(); // wait for result
    }
}

ForkJoinPool pool = new ForkJoinPool();
int result = pool.invoke(new MyTask(5));
```

---

## **7. Modern Concurrency Features (Java 21 and recent versions)**

* **Virtual Threads (Project Loom)**:

  * Lightweight threads that allow millions of concurrent tasks.
  * Easier to write concurrent code like sequential code.
* **Structured Concurrency** (preview in recent versions): groups multiple tasks to manage them as a unit.

**Example (virtual thread):**

```java
Thread.startVirtualThread(() -> System.out.println("Virtual thread running"));
```

---

### ✅ **Summary of Java Concurrency Patterns**

| Pattern/Feature           | Purpose                                        |
| ------------------------- | ---------------------------------------------- |
| Thread & Runnable         | Basic task execution                           |
| Executor Framework        | Thread pools, task management                  |
| Synchronization / Locks   | Safe access to shared resources                |
| Concurrent Collections    | Thread-safe collections                        |
| Atomic Variables          | Lock-free updates                              |
| Fork/Join Framework       | Parallel divide-and-conquer tasks              |
| Virtual Threads (Java 21) | Lightweight, scalable concurrency              |
| Structured Concurrency    | Grouping tasks for easier management (preview) |
