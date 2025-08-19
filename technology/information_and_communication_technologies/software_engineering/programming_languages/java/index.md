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

### Functional Interface

In Java, a functional interface is an interface with:

- Exactly one abstract method
- Annotated with `@FunctionalInterface` annotation(this is optional, but recommended)
- Can have default and static methods

### Core Functional Interfaces

The functional interfaces provided by Java are(Abbrevation to remember **PFCSO**):

- Predicate - return boolean values
    - `Predicate<T>`
    - `BiPredicate<T, U>`(takes 2 inputs)
    - abstract function: `boolean test(T t, U... u)`, here `...` is used as standin for "also"
- Function - Take an input, and provide a definite replicable output based on it. Return type needs to be specified.
    - `Function<T, R>`, R is the return type, and T is the input type
    - `BiFunction<T, U, R>`, U is the second input type
    - abstract function: `T apply(T t, U... u)`
- Consumer - Take input, without any outputs.
    - `Consumer<T>`
    - `BiConsumer<T, U>`
    - abstract function: `void accept(T t, U... u)`
- Supplier - Provide output
    - `Supplier<T>`
    - abstract function: `T get()`
- Operator - Operate on the same datatype, providing an output of the same type
    - `UnaryOperator<T>`
    - `BinaryOperator<T>`
    - abstract function: `T apply(T t1, T... t2)`

To avoid boxing/unboxing overhead:
- IntFunction, LongFunction, DoubleFunction
- ToIntFunction<T>, ToLongFunction<T>, ToDoubleFunction<T>
- IntPredicate, LongPredicate, DoublePredicate
- IntConsumer, LongConsumer, DoubleConsumer
- IntSupplier, LongSupplier, DoubleSupplier
- IntUnaryOperator, IntBinaryOperator (and for Long/Double)


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
