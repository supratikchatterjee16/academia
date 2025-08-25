# Design Patterns(software)

In software engineering, a design pattern represents a general, reusable solution to a commonly occurring problem within a specific context during software design. It is not a finished design that can be directly converted into code, but rather a template or blueprint that can be adapted to solve particular design problems in a structured and efficient way.

The following is a table, with some of the common design patterns across programming paradigms:

| **Pattern**                             | **Paradigm**      | **Category**     | **Core Idea / Use Case**                                         |
| --------------------------------------- | ----------------- | ---------------- | ---------------------------------------------------------------- |
| **Factory Method**                      | OO                | Creational       | Subclasses decide which concrete class to instantiate.           |
| **Abstract Factory**                    | OO                | Creational       | Families of related objects without specifying concrete classes. |
| **Builder**                             | OO                | Creational       | Step-by-step construction of complex objects.                    |
| **Prototype**                           | OO                | Creational       | Clone existing objects.                                          |
| **Singleton**                           | OO                | Creational       | Ensure only one instance globally.                               |
| **Adapter (Wrapper)**                   | OO                | Structural       | Convert one interface to another.                                |
| **Bridge**                              | OO                | Structural       | Decouple abstraction from implementation.                        |
| **Composite**                           | OO                | Structural       | Treat individual + composite objects uniformly (trees).          |
| **Decorator**                           | OO                | Structural       | Add responsibilities dynamically.                                |
| **Facade**                              | OO                | Structural       | Provide a simple interface to a complex subsystem.               |
| **Flyweight**                           | OO                | Structural       | Reuse shared objects to save memory.                             |
| **Proxy**                               | OO                | Structural       | Surrogate that controls access to another object.                |
| **Chain of Responsibility**             | OO                | Behavioral       | Pass requests along chain until handled.                         |
| **Command**                             | OO                | Behavioral       | Encapsulate requests as objects (undo, logging).                 |
| **Interpreter**                         | OO                | Behavioral       | Define grammar + interpret sentences.                            |
| **Iterator**                            | OO                | Behavioral       | Sequentially access collection elements.                         |
| **Mediator**                            | OO                | Behavioral       | Encapsulate interactions between objects.                        |
| **Memento**                             | OO                | Behavioral       | Save and restore state.                                          |
| **Observer (Pub-Sub)**                  | OO/Procedural     | Behavioral       | Notify dependents when state changes.                            |
| **State**                               | OO                | Behavioral       | Change behavior when internal state changes.                     |
| **Strategy**                            | OO/Procedural     | Behavioral       | Swap algorithms interchangeably.                                 |
| **Template Method**                     | OO                | Behavioral       | Skeleton algorithm, steps overridden by subclasses.              |
| **Visitor**                             | OO                | Behavioral       | Add operations without changing object structure.                |
| **Active Object**                       | OO                | Concurrency      | Async method calls via queue + scheduler.                        |
| **Thread Pool**                         | OO/Procedural     | Concurrency      | Reuse worker threads for efficiency.                             |
| **Double-Checked Locking**              | OO/Procedural     | Concurrency      | Optimize lazy initialization with minimal locking.               |
| **Producer-Consumer**                   | OO/Procedural     | Concurrency      | Decouple work production and consumption.                        |
| **Reader-Writer Lock**                  | OO/Procedural     | Concurrency      | Allow many reads, exclusive writes.                              |
| **Monitor Object**                      | OO                | Concurrency      | Encapsulate synchronization with monitor.                        |
| **Scheduler / Dispatcher**              | OO/Procedural     | Concurrency      | Central dispatcher controls task execution.                      |
| **Half-Sync/Half-Async**                | OO/Procedural     | Concurrency      | Layer sync & async processing with queues.                       |
| **Leader-Follower**                     | OO/Procedural     | Concurrency      | Thread pool where threads take turns leading event wait.         |
| **Module Initialization**               | Procedural        | Creational       | Setup/teardown for modules.                                      |
| **Factory Functions**                   | Procedural        | Creational       | Functions return pre-configured structures.                      |
| **RAII-like Init/Free**                 | Procedural        | Resource Mgmt    | Lifecycle mgmt (`init/free`).                                    |
| **Handle / Opaque Pointer**             | Procedural        | Structural       | Hide implementation via indirection.                             |
| **Table-Driven Methods**                | Procedural        | Structural       | Replace conditionals with lookup tables.                         |
| **Callback Functions**                  | Procedural        | Behavioral       | Register function handlers for events.                           |
| **Finite State Machine (FSM)**          | Procedural        | Behavioral       | Switch-based state transitions.                                  |
| **Main Loop (Event Loop)**              | Procedural        | Control          | Central dispatcher loop.                                         |
| **Reactor Pattern**                     | Procedural        | Concurrency      | Event demux (select/poll/epoll).                                 |
| **Pipe and Filter**                     | Procedural        | Data Flow        | Sequential transformation stages.                                |
| **Polling / Interrupt Handling**        | Procedural        | Control          | Low-level event handling.                                        |
| **Error Codes & Sentinels**             | Procedural        | Error Handling   | Numeric codes for errors.                                        |
| **Setjmp/Longjmp Exceptions**           | Procedural        | Error Handling   | Simulated exceptions in C.                                       |
| **Shared Memory + Locks**               | Procedural        | Concurrency      | Synchronization primitives.                                      |
| **Message Passing (IPC)**               | Procedural        | Concurrency      | Processes communicate via messages.                              |
| **Worker Pools (Fork/Join)**            | Procedural        | Concurrency      | Parallel divide-and-conquer.                                     |
| **Dependency Injection (DI)**           | OO (Advanced)     | Structural       | Inject dependencies externally.                                  |
| **Service Locator**                     | OO (Advanced)     | Architectural    | Central registry for dependencies.                               |
| **Lazy Initialization**                 | OO (Advanced)     | Structural       | Create objects only when needed.                                 |
| **Null Object**                         | OO (Advanced)     | Behavioral       | No-op implementation to avoid `null`.                            |
| **Extension Object**                    | OO (Advanced)     | Structural       | Dynamically add new behavior.                                    |
| **Specification Pattern**               | OO (Advanced)     | Behavioral       | Encapsulate and compose business rules.                          |
| **Repository Pattern**                  | OO (Advanced)     | Data Access      | Abstract persistence behind repo.                                |
| **Unit of Work**                        | OO (Advanced)     | Data Mgmt        | Track changes, commit in one transaction.                        |
| **Aggregator / Composite Service**      | OO (Advanced)     | Service-Oriented | Combine multiple services into one response.                     |
| **CQRS**                                | OO (Advanced)     | Architectural    | Separate reads from writes.                                      |
| **Event Sourcing**                      | OO (Advanced)     | Architectural    | Store events, rebuild state later.                               |
| **Domain Model**                        | OO (Advanced)     | Modeling/DDD     | Rich object model for business domain.                           |
| **Policy Pattern**                      | OO (Advanced)     | Behavioral       | Rules encapsulated as objects.                                   |
| **Active Record**                       | OO (Advanced)     | Data Access      | ORM-like object + persistence.                                   |
| **Interceptor / Middleware**            | OO (Advanced)     | Structural       | Cross-cutting logic insertion.                                   |
| **Microkernel (Plug-in)**               | OO/Architectural  | Advanced Arch    | Minimal core + plug-ins for extensibility.                       |
| **Hexagonal (Ports & Adapters)**        | OO/Architectural  | Advanced Arch    | Business logic isolated from external systems.                   |
| **Saga**                                | Distributed/OO    | Advanced         | Long transactions split into steps + compensations.              |
| **Event-Carried State Transfer (ECST)** | Distributed       | Advanced         | Events carry full state to consumers.                            |
| **Aggregator / Scatter-Gather**         | Distributed       | Advanced         | Split requests into parallel calls, combine results.             |
| **Blackboard Pattern**                  | AI/Advanced       | Problem-Solving  | Shared knowledge base for multiple subsystems.                   |
| **Immutable Snapshot / Copy-on-Write**  | OO/Procedural     | Concurrency      | Readers use immutable copies, writers update.                    |
| **Self-Healing / Adaptive System**      | Distributed/Cloud | Resilience       | Detect failures, auto-recover.                                   |
| **Double Dispatch / Multi-Dispatch**    | OO                | Behavioral       | Different execution based on multiple types.                     |
| **Aspect-Oriented Patterns**            | OO/Architectural  | Cross-Cutting    | Separate logging, security, metrics.                             |
| **Model-Driven (DSL + Interpreter)**    | OO/Frameworks     | Advanced         | Declarative configs interpreted at runtime.                      |

## Creational Design Patterns

* **Abstract Factory** – create families of related objects without specifying their concrete classes.
* **Builder** – construct complex objects step by step; same construction, different representations.
* **Factory Method** – let subclasses decide which class to instantiate.
* **Prototype** – clone existing objects instead of creating from scratch.
* **Singleton** – ensure a class has only one instance and provide a global access point.

Below are tight summaries and clean Java examples (OOP-friendly). Each snippet is self-contained.

---

### 1) Abstract Factory

**Intent:** Provide an interface for creating related objects (a “family”) without exposing concrete classes.
**Use when:** You have multiple product families (e.g., Win/Mac widgets) and want to switch families easily.

**Key idea:** Client depends on abstract factories & products; swap the factory to change the family.

```java
// Products (abstract)
interface Button { void render(); }
interface Checkbox { void toggle(); }

// Concrete Products: Family A
class WinButton implements Button { public void render() { System.out.println("WinButton"); } }
class WinCheckbox implements Checkbox { public void toggle() { System.out.println("WinCheckbox"); } }

// Concrete Products: Family B
class MacButton implements Button { public void render() { System.out.println("MacButton"); } }
class MacCheckbox implements Checkbox { public void toggle() { System.out.println("MacCheckbox"); } }

// Abstract Factory
interface GUIFactory {
    Button createButton();
    Checkbox createCheckbox();
}

// Concrete Factories
class WinFactory implements GUIFactory {
    public Button createButton() { return new WinButton(); }
    public Checkbox createCheckbox() { return new WinCheckbox(); }
}

class MacFactory implements GUIFactory {
    public Button createButton() { return new MacButton(); }
    public Checkbox createCheckbox() { return new MacCheckbox(); }
}

// Client
class Application {
    private final Button button;
    private final Checkbox checkbox;

    Application(GUIFactory factory) {
        this.button = factory.createButton();
        this.checkbox = factory.createCheckbox();
    }
    void draw() { button.render(); checkbox.toggle(); }
}

public class Demo {
    public static void main(String[] args) {
        GUIFactory factory = System.getProperty("os.name").startsWith("Windows")
                ? new WinFactory() : new MacFactory();
        new Application(factory).draw();
    }
}
```

**Pros:** Swap product families at runtime; enforces family consistency.
**Cons:** Many classes; adding a new product type touches all factories.

---

### 2) Builder

**Intent:** Separate construction of a complex object from its representation.
**Use when:** Object has many optional/complex parts or different representations.

```java
// Product
class House {
    boolean hasBasement, hasGarden; int floors;
    public String toString() { return "House{floors=" + floors + ", basement=" + hasBasement + ", garden=" + hasGarden + "}"; }
}

// Builder
interface HouseBuilder {
    HouseBuilder floors(int n);
    HouseBuilder basement(boolean b);
    HouseBuilder garden(boolean g);
    House build();
}

// Concrete Builder
class ConcreteHouseBuilder implements HouseBuilder {
    private final House h = new House();
    public HouseBuilder floors(int n) { h.floors = n; return this; }
    public HouseBuilder basement(boolean b) { h.hasBasement = b; return this; }
    public HouseBuilder garden(boolean g) { h.hasGarden = g; return this; }
    public House build() { return h; }
}

// Optional Director
class Architect {
    House luxuryVilla(HouseBuilder b) {
        return b.floors(2).basement(true).garden(true).build();
    }
}

public class Demo {
    public static void main(String[] args) {
        House custom = new ConcreteHouseBuilder().floors(3).garden(true).build();
        House preset = new Architect().luxuryVilla(new ConcreteHouseBuilder());
        System.out.println(custom);
        System.out.println(preset);
    }
}
```

**Pros:** Readable object creation; different “recipes.”
**Cons:** More classes/indirection; not ideal for simple objects.

---

### 3) Factory Method

**Intent:** Define an interface for creating an object, but let subclasses choose the class to instantiate.
**Use when:** A class can’t anticipate which specific subclass to create.

```java
// Product
interface Document { void open(); }

// Concrete Products
class WordDoc implements Document { public void open() { System.out.println("Opening WordDoc"); } }
class PdfDoc  implements Document { public void open() { System.out.println("Opening PdfDoc"); } }

// Creator
abstract class Application {
    // Factory Method
    protected abstract Document createDocument();
    public void newDocument() {
        Document doc = createDocument();
        doc.open();
    }
}

// Concrete Creators
class WordApp extends Application {
    protected Document createDocument() { return new WordDoc(); }
}
class PdfApp extends Application {
    protected Document createDocument() { return new PdfDoc(); }
}

public class Demo {
    public static void main(String[] args) {
        Application app = args.length > 0 && args[0].equals("pdf") ? new PdfApp() : new WordApp();
        app.newDocument();
    }
}
```

**Pros:** Open/closed for new products; moves creation to subclasses.
**Cons:** Class proliferation; still tied to inheritance.

---

### 4) Prototype

**Intent:** Create new objects by copying an existing instance (a prototype).
**Use when:** Object creation is expensive or you need to avoid subclass explosions and use runtime configuration.

```java
import java.util.HashMap;
import java.util.Map;

// Prototype
interface Shape extends Cloneable {
    Shape clone();
    void draw();
}

// Concrete Prototypes
class Circle implements Shape {
    int radius; String color;
    Circle(int r, String c) { radius = r; color = c; }
    public void draw() { System.out.println("Circle r=" + radius + " c=" + color); }
    public Circle clone() { return new Circle(this.radius, this.color); } // deep copy if needed
}
class Rectangle implements Shape {
    int w, h; String color;
    Rectangle(int w, int h, String c) { this.w = w; this.h = h; color = c; }
    public void draw() { System.out.println("Rectangle " + w + "x" + h + " c=" + color); }
    public Rectangle clone() { return new Rectangle(this.w, this.h, this.color); }
}

// Prototype Registry
class ShapeRegistry {
    private final Map<String, Shape> cache = new HashMap<>();
    void register(String key, Shape proto) { cache.put(key, proto); }
    Shape create(String key) { return cache.get(key).clone(); }
}

public class Demo {
    public static void main(String[] args) {
        ShapeRegistry reg = new ShapeRegistry();
        reg.register("bigRedCircle", new Circle(50, "red"));
        reg.register("card", new Rectangle(90, 60, "white"));

        Shape s1 = reg.create("bigRedCircle"); s1.draw();
        Shape s2 = reg.create("card"); s2.draw();
    }
}
```

**Pros:** Avoids costly re-creation; convenient runtime composition.
**Cons:** Cloning complexity (deep vs. shallow, circular refs, immutable fields).

---

### 5) Singleton

**Intent:** Ensure a class has a single instance and provide global access.
**Use when:** Exactly one instance must coordinate actions (e.g., config, logging).
**Note:** Use sparingly; can hinder testing and introduce hidden coupling.

```java
// Thread-safe, lazy-loaded Singleton with double-checked locking
class Config {
    private static volatile Config INSTANCE;
    private Config() { /* load settings */ }
    public static Config getInstance() {
        Config result = INSTANCE;
        if (result == null) {
            synchronized (Config.class) {
                result = INSTANCE;
                if (result == null) INSTANCE = result = new Config();
            }
        }
        return result;
    }
    public String get(String key) { return "value-for-" + key; }
}

public class Demo {
    public static void main(String[] args) {
        Config a = Config.getInstance();
        Config b = Config.getInstance();
        System.out.println(a == b); // true
    }
}
```

**Alternatives (Java):**

* **Enum Singleton** (simple & serialization-safe):

  ```java
  public enum Registry { INSTANCE; public String get(String k){return "v";} }
  ```
* **Dependency Injection** frameworks often replace singletons.

---

### Quick When-to-Use Cheat Sheet

* **Abstract Factory:** Need to switch *families* of related products.
* **Builder:** Many optional parts / construction steps.
* **Factory Method:** Creator defers exact product to subclasses.
* **Prototype:** New objects are copies of configured exemplars.
* **Singleton:** Exactly one instance; global access required.

---

## Structural Design Patterns (GoF)

* **Adapter** – make incompatible interfaces work together.
* **Bridge** – decouple abstraction from implementation.
* **Composite** – tree structures of objects, treat part/whole uniformly.
* **Decorator** – add responsibilities dynamically.
* **Facade** – unified simplified interface to a subsystem.
* **Flyweight** – efficient sharing of many fine-grained objects.
* **Proxy** – placeholder for another object to control access.

---

### 1) Adapter

**Intent:** Convert one interface into another that clients expect.
**Use when:** You want to use a class but its interface is incompatible.

```java
// Target
interface MediaPlayer { void play(String file); }

// Adaptee (incompatible interface)
class LegacyPlayer {
    void playFile(String filename) { System.out.println("Playing " + filename); }
}

// Adapter
class MediaAdapter implements MediaPlayer {
    private final LegacyPlayer legacy;
    MediaAdapter(LegacyPlayer l) { this.legacy = l; }
    public void play(String file) { legacy.playFile(file); }
}

// Client
public class Demo {
    public static void main(String[] args) {
        MediaPlayer player = new MediaAdapter(new LegacyPlayer());
        player.play("song.mp3");
    }
}
```

---

### 2) Bridge

**Intent:** Separate abstraction from implementation, letting them vary independently.
**Use when:** You have multiple dimensions of variation (e.g., Shapes & Colors).

```java
// Implementor
interface Color { String fill(); }
class Red implements Color { public String fill() { return "Red"; } }
class Blue implements Color { public String fill() { return "Blue"; } }

// Abstraction
abstract class Shape {
    protected Color color;
    Shape(Color c) { color = c; }
    abstract void draw();
}

// Refined Abstraction
class Circle extends Shape {
    Circle(Color c) { super(c); }
    void draw() { System.out.println("Circle filled with " + color.fill()); }
}
class Square extends Shape {
    Square(Color c) { super(c); }
    void draw() { System.out.println("Square filled with " + color.fill()); }
}

public class Demo {
    public static void main(String[] args) {
        Shape s1 = new Circle(new Red());
        Shape s2 = new Square(new Blue());
        s1.draw(); s2.draw();
    }
}
```

---

### 3) Composite

**Intent:** Compose objects into tree structures; treat individual and composite uniformly.
**Use when:** Represent hierarchies (menus, directories, GUI).

```java
import java.util.*;

// Component
interface Graphic { void draw(); }

// Leaf
class Line implements Graphic {
    public void draw() { System.out.println("Line"); }
}
class Circle implements Graphic {
    public void draw() { System.out.println("Circle"); }
}

// Composite
class Picture implements Graphic {
    private final List<Graphic> children = new ArrayList<>();
    public void add(Graphic g) { children.add(g); }
    public void draw() {
        System.out.println("Picture:");
        for (Graphic g : children) g.draw();
    }
}

public class Demo {
    public static void main(String[] args) {
        Picture pic = new Picture();
        pic.add(new Line());
        pic.add(new Circle());
        pic.draw();
    }
}
```

---

### 4) Decorator

**Intent:** Attach new behavior to objects dynamically without subclassing.
**Use when:** You want to extend functionality at runtime.

```java
// Component
interface Coffee { String getDescription(); double cost(); }

// Concrete Component
class SimpleCoffee implements Coffee {
    public String getDescription() { return "Simple Coffee"; }
    public double cost() { return 2.0; }
}

// Decorator
abstract class CoffeeDecorator implements Coffee {
    protected final Coffee decorated;
    CoffeeDecorator(Coffee c) { decorated = c; }
    public String getDescription() { return decorated.getDescription(); }
    public double cost() { return decorated.cost(); }
}

// Concrete Decorators
class Milk extends CoffeeDecorator {
    Milk(Coffee c) { super(c); }
    public String getDescription() { return super.getDescription() + ", Milk"; }
    public double cost() { return super.cost() + 0.5; }
}
class Sugar extends CoffeeDecorator {
    Sugar(Coffee c) { super(c); }
    public String getDescription() { return super.getDescription() + ", Sugar"; }
    public double cost() { return super.cost() + 0.2; }
}

public class Demo {
    public static void main(String[] args) {
        Coffee coffee = new Sugar(new Milk(new SimpleCoffee()));
        System.out.println(coffee.getDescription() + " $" + coffee.cost());
    }
}
```

---

### 5) Facade

**Intent:** Provide a simple interface to a complex subsystem.
**Use when:** You want to simplify client usage.

```java
// Subsystem
class CPU { void start() { System.out.println("CPU start"); } }
class Memory { void load() { System.out.println("Memory load"); } }
class Disk { void read() { System.out.println("Disk read"); } }

// Facade
class Computer {
    private final CPU cpu = new CPU();
    private final Memory mem = new Memory();
    private final Disk disk = new Disk();
    void start() {
        cpu.start(); mem.load(); disk.read();
        System.out.println("Computer ready!");
    }
}

// Client
public class Demo {
    public static void main(String[] args) {
        new Computer().start();
    }
}
```

---

### 6) Flyweight

**Intent:** Use sharing to support large numbers of fine-grained objects efficiently.
**Use when:** Too many similar objects (e.g., characters in a text editor).

```java
import java.util.*;

// Flyweight
interface Glyph { void draw(int x, int y); }

// Concrete Flyweight
class CharacterGlyph implements Glyph {
    private final char symbol; // intrinsic state
    CharacterGlyph(char c) { symbol = c; }
    public void draw(int x, int y) { // extrinsic state
        System.out.println("Draw " + symbol + " at (" + x + "," + y + ")");
    }
}

// Flyweight Factory
class GlyphFactory {
    private final Map<Character, Glyph> pool = new HashMap<>();
    Glyph get(char c) {
        return pool.computeIfAbsent(c, CharacterGlyph::new);
    }
}

// Client
public class Demo {
    public static void main(String[] args) {
        GlyphFactory f = new GlyphFactory();
        String text = "abba";
        for (int i = 0; i < text.length(); i++) {
            f.get(text.charAt(i)).draw(i, 0);
        }
    }
}
```

---

### 7) Proxy

**Intent:** Provide a placeholder to control access to another object.
**Variants:** Virtual Proxy (lazy loading), Protection Proxy (access control), Remote Proxy.

```java
// Subject
interface Image { void display(); }

// Real Subject
class RealImage implements Image {
    private final String filename;
    RealImage(String f) { this.filename = f; load(); }
    private void load() { System.out.println("Loading " + filename); }
    public void display() { System.out.println("Displaying " + filename); }
}

// Proxy
class ProxyImage implements Image {
    private final String filename;
    private RealImage real;
    ProxyImage(String f) { filename = f; }
    public void display() {
        if (real == null) real = new RealImage(filename);
        real.display();
    }
}

// Client
public class Demo {
    public static void main(String[] args) {
        Image img = new ProxyImage("photo.png");
        img.display(); // loads + displays
        img.display(); // only displays
    }
}
```

---

### Quick Cheat Sheet: When to Use

* **Adapter:** Incompatible interfaces.
* **Bridge:** Two independent dimensions of variation.
* **Composite:** Tree structures, uniform treatment.
* **Decorator:** Add/remove responsibilities at runtime.
* **Facade:** Simplify a complex subsystem.
* **Flyweight:** Lots of similar fine-grained objects.
* **Proxy:** Control, cache, or defer access to real object.

Got it ✅ — you’d like a **broader set of behavioral patterns**, not just the 11 GoF ones.
So I’ll include the **classic GoF behavioral patterns** *plus* a few **commonly recognized ones outside GoF** (e.g., Null Object, Specification, etc.).

These patterns all deal with **object interaction, communication, and responsibility distribution**.

---

## Behavioral Design Patterns

### 1) **Chain of Responsibility**

**Intent:** Pass requests along a chain until handled.
**Use when:** Multiple handlers may process a request, but the client shouldn’t know which one.

```java
// Handler
abstract class Handler {
    protected Handler next;
    public Handler setNext(Handler h) { next = h; return h; }
    abstract void handle(String request);
}

// Concrete Handlers
class AuthHandler extends Handler {
    void handle(String request) {
        if ("auth".equals(request)) System.out.println("Auth handled");
        else if (next != null) next.handle(request);
    }
}
class LogHandler extends Handler {
    void handle(String request) {
        if ("log".equals(request)) System.out.println("Log handled");
        else if (next != null) next.handle(request);
    }
}

public class Demo {
    public static void main(String[] args) {
        Handler h = new AuthHandler();
        h.setNext(new LogHandler());
        h.handle("log");
    }
}
```

---

### 2) **Command**

**Intent:** Encapsulate a request as an object.
**Use when:** Undo/redo, logging, macro commands.

```java
// Command
interface Command { void execute(); }

// Receiver
class Light { void on() { System.out.println("Light on"); } void off() { System.out.println("Light off"); } }

// Concrete Commands
class LightOn implements Command { private final Light light; LightOn(Light l){light=l;} public void execute(){light.on();} }
class LightOff implements Command { private final Light light; LightOff(Light l){light=l;} public void execute(){light.off();} }

// Invoker
class Remote {
    private Command slot;
    void setCommand(Command c){ slot = c; }
    void press(){ slot.execute(); }
}

public class Demo {
    public static void main(String[] args) {
        Light l = new Light();
        Remote r = new Remote();
        r.setCommand(new LightOn(l)); r.press();
        r.setCommand(new LightOff(l)); r.press();
    }
}
```

---

### 3) **Interpreter**

**Intent:** Define a grammar and interpret sentences in it.
**Use when:** DSLs, configuration languages.

```java
// Expression
interface Expression { boolean interpret(String ctx); }

// Terminal Expressions
class Terminal implements Expression {
    private final String word;
    Terminal(String w){word=w;}
    public boolean interpret(String ctx){ return ctx.contains(word); }
}

// Non-terminal
class Or implements Expression {
    private final Expression a, b;
    Or(Expression a, Expression b){this.a=a;this.b=b;}
    public boolean interpret(String ctx){ return a.interpret(ctx) || b.interpret(ctx); }
}

public class Demo {
    public static void main(String[] args) {
        Expression expr = new Or(new Terminal("dog"), new Terminal("cat"));
        System.out.println(expr.interpret("I love dogs")); // true
    }
}
```

---

### 4) **Iterator**

**Intent:** Sequentially access elements without exposing representation.

```java
import java.util.Iterator;
import java.util.NoSuchElementException;

class MyCollection implements Iterable<String> {
    private final String[] data = {"a","b","c"};
    public Iterator<String> iterator() {
        return new Iterator<>() {
            int idx=0;
            public boolean hasNext(){ return idx < data.length; }
            public String next(){ if(!hasNext()) throw new NoSuchElementException(); return data[idx++]; }
        };
    }
}

public class Demo {
    public static void main(String[] args) {
        for(String s : new MyCollection()) System.out.println(s);
    }
}
```

---

### 5) **Mediator**

**Intent:** Centralize communication between objects.

```java
import java.util.*;

interface ChatMediator { void send(String msg, User u); }
class ChatRoom implements ChatMediator {
    private final List<User> users = new ArrayList<>();
    void add(User u){ users.add(u); }
    public void send(String msg, User u){ for(User x: users) if(x!=u) x.receive(msg); }
}

abstract class User {
    protected ChatMediator mediator; protected String name;
    User(ChatMediator m, String n){ mediator=m; name=n; }
    void send(String msg){ mediator.send(msg,this); }
    abstract void receive(String msg);
}

class ChatUser extends User {
    ChatUser(ChatMediator m, String n){ super(m,n); }
    void receive(String msg){ System.out.println(name+" got: "+msg); }
}

public class Demo {
    public static void main(String[] args) {
        ChatRoom room = new ChatRoom();
        User a = new ChatUser(room,"Alice"); User b = new ChatUser(room,"Bob");
        room.add(a); room.add(b);
        a.send("Hi Bob!");
    }
}
```

---

### 6) **Memento**

**Intent:** Capture object state without exposing internals (undo/rollback).

```java
// Memento
class Memento { private final String state; Memento(String s){state=s;} String get(){return state;} }

// Originator
class Editor {
    private String text="";
    void setText(String t){ text=t; }
    String getText(){ return text; }
    Memento save(){ return new Memento(text); }
    void restore(Memento m){ text = m.get(); }
}

// Caretaker
public class Demo {
    public static void main(String[] args) {
        Editor e = new Editor();
        e.setText("v1"); Memento m = e.save();
        e.setText("v2");
        e.restore(m);
        System.out.println(e.getText()); // v1
    }
}
```

---

### 7) **Observer (Publish-Subscribe)**

**Intent:** Notify dependents automatically when subject changes.

```java
import java.util.*;

interface Observer { void update(int s); }
class Subject {
    private final List<Observer> obs = new ArrayList<>(); private int state;
    void attach(Observer o){ obs.add(o); }
    void setState(int s){ state=s; for(Observer o: obs) o.update(state); }
}

class ConsoleObserver implements Observer {
    private final String name;
    ConsoleObserver(String n){name=n;}
    public void update(int s){ System.out.println(name+" sees state="+s); }
}

public class Demo {
    public static void main(String[] args) {
        Subject sub = new Subject();
        sub.attach(new ConsoleObserver("A"));
        sub.attach(new ConsoleObserver("B"));
        sub.setState(5);
    }
}
```

---

### 8) **State**

**Intent:** Change object behavior when its internal state changes.

```java
// State
interface State { void handle(Context c); }

class On implements State {
    public void handle(Context c){ System.out.println("Turning Off"); c.set(new Off()); }
}
class Off implements State {
    public void handle(Context c){ System.out.println("Turning On"); c.set(new On()); }
}

// Context
class Context {
    private State state;
    Context(State s){ state=s; }
    void set(State s){ state=s; }
    void request(){ state.handle(this); }
}

public class Demo {
    public static void main(String[] args) {
        Context ctx = new Context(new Off());
        ctx.request(); ctx.request(); ctx.request();
    }
}
```

---

### 9) **Strategy**

**Intent:** Define family of algorithms, make them interchangeable.

```java
// Strategy
interface SortStrategy { void sort(int[] arr); }

// Concrete Strategies
class BubbleSort implements SortStrategy { public void sort(int[] arr){ System.out.println("Bubble sort"); } }
class QuickSort implements SortStrategy { public void sort(int[] arr){ System.out.println("Quick sort"); } }

// Context
class Sorter {
    private SortStrategy strategy;
    Sorter(SortStrategy s){ strategy=s; }
    void setStrategy(SortStrategy s){ strategy=s; }
    void sort(int[] arr){ strategy.sort(arr); }
}

public class Demo {
    public static void main(String[] args) {
        Sorter s = new Sorter(new BubbleSort());
        s.sort(new int[]{1,2,3});
        s.setStrategy(new QuickSort());
        s.sort(new int[]{1,2,3});
    }
}
```

---

### 10) **Template Method**

**Intent:** Skeleton of algorithm with steps deferred to subclasses.

```java
abstract class Game {
    abstract void init(); abstract void play(); abstract void end();
    public final void run(){ init(); play(); end(); }
}
class Chess extends Game {
    void init(){System.out.println("Chess init");}
    void play(){System.out.println("Chess playing");}
    void end(){System.out.println("Chess end");}
}
public class Demo {
    public static void main(String[] args) {
        new Chess().run();
    }
}
```

---

### 11) **Visitor**

**Intent:** Add new operations without changing object classes.

```java
// Visitor
interface Visitor { void visit(Book b); void visit(CD c); }

// Element
interface Item { void accept(Visitor v); }

// Concrete Elements
class Book implements Item { public void accept(Visitor v){ v.visit(this); } }
class CD implements Item { public void accept(Visitor v){ v.visit(this); } }

// Concrete Visitor
class PriceCalculator implements Visitor {
    public void visit(Book b){ System.out.println("Book $10"); }
    public void visit(CD c){ System.out.println("CD $5"); }
}

public class Demo {
    public static void main(String[] args) {
        Item[] cart = { new Book(), new CD() };
        Visitor v = new PriceCalculator();
        for(Item i: cart) i.accept(v);
    }
}
```

---

### 12) **Null Object**

Provide a “do-nothing” object instead of `null` checks.

```java
interface Logger { void log(String msg); }
class ConsoleLogger implements Logger { public void log(String msg){ System.out.println(msg); } }
class NullLogger implements Logger { public void log(String msg){ /* do nothing */ } }

public class Demo {
    public static void main(String[] args) {
        Logger log = new NullLogger();
        log.log("This won’t print");
    }
}
```

---

### 13) **Specification**

Encapsulate business rules as composable predicates.

```java
interface Spec<T>{ boolean isSatisfiedBy(T t); default Spec<T> and(Spec<T> other){ return t -> this.isSatisfiedBy(t)&&other.isSatisfiedBy(t); } }

class EvenSpec implements Spec<Integer>{ public boolean isSatisfiedBy(Integer t){ return t%2==0; } }
class PositiveSpec implements Spec<Integer>{ public boolean isSatisfiedBy(Integer t){ return t>0; } }

public class Demo {
    public static void main(String[] args) {
        Spec<Integer> spec = new EvenSpec().and(new PositiveSpec());
        System.out.println(spec.isSatisfiedBy(4)); // true
    }
}
```

---

### 14) **Blackboard**

Useful in AI systems: multiple knowledge sources contribute to a central “blackboard.”

```java
// Simplified
class Blackboard {
    private final List<String> knowledge = new ArrayList<>();
    void add(String fact){ knowledge.add(fact); }
    List<String> facts(){ return knowledge; }
}
```

---

## Concurrency Design Patterns

### 1) **Active Object**

**Intent:** Decouple method execution from method invocation. Methods run asynchronously in their own thread.
**Use when:** You want objects to look synchronous, but actually run in the background.

```java
import java.util.concurrent.*;

class ActiveObject {
    private final ExecutorService executor = Executors.newSingleThreadExecutor();
    public Future<Integer> compute(int x) {
        return executor.submit(() -> {
            Thread.sleep(500);
            return x * x;
        });
    }
}
public class Demo {
    public static void main(String[] args) throws Exception {
        ActiveObject ao = new ActiveObject();
        Future<Integer> f = ao.compute(5);
        System.out.println("Doing other work...");
        System.out.println("Result = " + f.get());
    }
}
```

---

### 2) **Balking**

**Intent:** Execute an action only if the object is in a particular state. Otherwise, do nothing.
**Use when:** Prevent unsafe concurrent state transitions.

```java
class Printer {
    private boolean busy = false;
    synchronized void print(String msg) {
        if (busy) return; // balk
        busy = true;
        System.out.println("Printing: " + msg);
        busy = false;
    }
}
```

---

### 3) **Double-Checked Locking**

**Intent:** Reduce synchronization overhead in lazy initialization.
**Use when:** Singleton or resource that is expensive to create.

(We already saw this in **Singleton** example earlier.)

---

### 4) **Guarded Suspension**

**Intent:** A method waits (suspends) until a precondition is true.
**Use when:** Threads must wait for a resource to become available.

```java
class Shared {
    private String data;
    synchronized String take() throws InterruptedException {
        while (data == null) wait();
        String d = data; data = null;
        return d;
    }
    synchronized void put(String d) {
        data = d;
        notifyAll();
    }
}
```

---

### 5) **Scheduler (Thread Pool / Executor)**

**Intent:** Manage and schedule concurrent tasks without creating threads manually.
**Use when:** Many short-lived tasks → use pooled workers.

```java
import java.util.concurrent.*;

public class Demo {
    public static void main(String[] args) {
        ExecutorService pool = Executors.newFixedThreadPool(3);
        for(int i=0;i<5;i++){
            final int id=i;
            pool.submit(() -> System.out.println("Task "+id+" run by "+Thread.currentThread().getName()));
        }
        pool.shutdown();
    }
}
```

---

### 6) **Producer–Consumer (Bounded Buffer)**

**Intent:** Decouple producing from consuming with a buffer.
**Use when:** Workload balancing between producers and consumers.

```java
import java.util.concurrent.*;

class Demo {
    public static void main(String[] args) {
        BlockingQueue<Integer> queue = new ArrayBlockingQueue<>(5);
        new Thread(() -> { try { for(int i=0;i<10;i++){ queue.put(i); System.out.println("Produced "+i); } } catch(Exception e){} }).start();
        new Thread(() -> { try { while(true) System.out.println("Consumed "+queue.take()); } catch(Exception e){} }).start();
    }
}
```

---

### 7) **Reader–Writer Lock**

**Intent:** Allow multiple readers or one writer.
**Use when:** Reads are frequent, writes are rare.

```java
import java.util.concurrent.locks.*;

class RWData {
    private final ReadWriteLock lock = new ReentrantReadWriteLock();
    private int value;
    void write(int v){ lock.writeLock().lock(); try{ value=v; } finally{ lock.writeLock().unlock(); } }
    int read(){ lock.readLock().lock(); try{ return value; } finally{ lock.readLock().unlock(); } }
}
```

---

### 8) **Thread-Per-Message**

**Intent:** Each request is handled by a separate thread.
**Use when:** Requests are independent, and blocking the caller is undesirable.

```java
class Service {
    void handle(String msg){
        new Thread(() -> System.out.println("Handling "+msg)).start();
    }
}
```

---

### 9) **Work Stealing**

**Intent:** Workers steal tasks from each other’s queues to balance load.
**Use when:** Fork-Join parallelism.

(Java 7+ `ForkJoinPool` implements this.)

---

### 10) **Future / Promise**

**Intent:** Represent the result of an async computation.
**Use when:** Asynchronous workflows.

```java
import java.util.concurrent.*;
public class Demo {
    public static void main(String[] args) throws Exception {
        CompletableFuture<String> f = CompletableFuture.supplyAsync(() -> "Hello");
        System.out.println(f.get());
    }
}
```

---

### 11) **Reactor**

**Intent:** Handle service requests concurrently using non-blocking I/O and an event loop.
**Use when:** Servers (like Netty, Node.js).

---

### 12) **Half-Sync/Half-Async**

**Intent:** Split into async event handling and sync processing layers.
**Use when:** Systems need concurrency but simplified sync logic (e.g., web servers).

---

### 13) **Monitor Object**

**Intent:** Encapsulate synchronization inside an object; only one method executes at a time.

```java
class SafeCounter {
    private int count=0;
    public synchronized void inc(){ count++; }
    public synchronized int get(){ return count; }
}
```

---

### 14) **Barrier / Phaser**

**Intent:** Multiple threads must wait at a barrier until all have reached it.

```java
import java.util.concurrent.*;

public class Demo {
    public static void main(String[] args) {
        CyclicBarrier barrier = new CyclicBarrier(3, () -> System.out.println("All reached barrier"));
        for(int i=0;i<3;i++){
            new Thread(() -> {
                try { Thread.sleep((int)(Math.random()*1000)); barrier.await(); }
                catch(Exception e){}
            }).start();
        }
    }
}
```

---

### Cheat Sheet: When to Use Concurrency Patterns

| Pattern                     | When to Use                                       |
| --------------------------- | ------------------------------------------------- |
| **Active Object**           | Asynchronous methods with synchronous-looking API |
| **Balking**                 | Action only if in safe state                      |
| **Double-Checked Locking**  | Efficient lazy init (Singletons, caches)          |
| **Guarded Suspension**      | Wait until condition true (e.g., data available)  |
| **Thread Pool / Scheduler** | Many small tasks, manage thread lifecycle         |
| **Producer–Consumer**       | Decouple producers and consumers, buffering       |
| **Reader–Writer Lock**      | Frequent reads, rare writes                       |
| **Thread-per-Message**      | Independent, short-lived tasks                    |
| **Work Stealing**           | Dynamic load balancing in parallel tasks          |
| **Future / Promise**        | Asynchronous result representation                |
| **Reactor**                 | Event-driven, non-blocking server I/O             |
| **Half-Sync/Half-Async**    | Separate async I/O from sync processing           |
| **Monitor Object**          | Encapsulate synchronization inside object         |
| **Barrier / Phaser**        | Multiple threads must sync at a point             |

---

These concurrency patterns are complementary:

* For **async APIs** → use **Active Object**, **Future/Promise**.
* For **task scheduling** → **Thread Pool**, **Work Stealing**.
* For **resource sharing** → **Guarded Suspension**, **Reader-Writer Lock**, **Monitor**.
* For **coordination** → **Barrier**, **Half-Sync/Async**, **Reactor**.

---

## Distributed Design Patterns

### 1) **Broker**

**Intent:** Decouple clients and servers via a broker that handles communication, requests, and responses.
**Use when:** Service invocations need location transparency (e.g., CORBA, gRPC).

---

### 2) **Client–Server**

**Intent:** Split responsibilities between service provider (server) and consumer (client).
**Use when:** Centralized service model (web apps, APIs).

---

### 3) **Peer-to-Peer**

**Intent:** Every node acts as both client and server.
**Use when:** Decentralized networks (BitTorrent, blockchain).

---

### 4) **Remote Proxy**

**Intent:** Provide a local representative for a remote object.
**Use when:** Clients should use remote services transparently.
*(e.g., Java RMI stub, REST API client stubs)*

---

### 5) **Messaging / Message Queue**

**Intent:** Use messages for async communication.
**Use when:** Decouple sender and receiver (RabbitMQ, Kafka).

```java
// Simplified producer-consumer via queue
BlockingQueue<String> mq = new LinkedBlockingQueue<>();
new Thread(() -> { try{ mq.put("msg"); }catch(Exception e){} }).start();
new Thread(() -> { try{ System.out.println("Got "+mq.take()); }catch(Exception e){} }).start();
```

---

### 6) **Publish–Subscribe**

**Intent:** Subscribers register interest; publishers broadcast events.
**Use when:** Event-driven architecture.

---

### 7) **Leader Election**

**Intent:** Elect a leader among nodes for coordination.
**Use when:** Distributed consensus is required.
*(Used in ZooKeeper, Raft, Paxos.)*

---

### 8) **Replication**

**Intent:** Replicate data/services across nodes.
**Types:**

* **Active replication:** all replicas process requests.
* **Passive replication:** primary-backup.
  **Use when:** Fault tolerance, high availability.

---

### 9) **Sharding / Partitioning**

**Intent:** Split data across nodes by key/range.
**Use when:** Scalability of data stores.

---

### 10) **MapReduce**

**Intent:** Divide data-processing into map (parallel tasks) + reduce (aggregation).
**Use when:** Large-scale distributed data processing (Hadoop, Spark).

---

### 11) **Service Registry & Discovery**

**Intent:** Services register with a registry; clients discover them dynamically.
**Use when:** Microservices with dynamic scaling (Eureka, Consul).

---

### 12) **Circuit Breaker**

**Intent:** Prevent cascading failures by cutting off calls to failing services.
**Use when:** Resilient service-to-service calls (Netflix Hystrix).

---

### 13) **Bulkhead**

**Intent:** Isolate resources so failure in one part doesn’t sink the system.
**Use when:** Microservices resilience.

---

### 14) **Saga**

**Intent:** Manage long-running distributed transactions via compensating actions.
**Use when:** Business workflows across services.

#### Choreography (Event-driven)

- Each service listens for events, performs work, and publishes new events.
- No central coordinator.
- Simpler, scalable, but harder to track/monitor.

Example:

- Order Service → “OrderCreated” event.
- Payment Service → “PaymentProcessed” → emits “PaymentConfirmed”.
- Shipping Service → “ShipmentScheduled”.
- If Payment fails → emit “PaymentFailed” → Order Service compensates (cancel order).

#### Orchestration (Central Coordinator)

- A central saga orchestrator commands services to execute steps and compensations.
- Easier to reason about, but adds coupling and single-point control.

Pros:

- Avoids global locks (better than 2PC).
- Works in microservices, cloud-native systems.
- Supports long-running business processes.

Cons:

- Eventual consistency (not strong atomicity).
- Complexity: need compensation logic for every step.
- Choreography: harder to debug. Orchestration: potential bottleneck.

Used in: Microservices (e.g., ecommerce order workflows), distributed business logic.

---

### 15) **CQRS (Command Query Responsibility Segregation)**

**Intent:** Separate read and write models.
**Use when:** Complex systems with high read/write loads.

Split read and write models into separate systems.

- Commands → change state.
- Queries → read state.

Workflow:

- Commands go through a write model (strict validation, business rules).
- Queries use a read model (denormalized, optimized for fast lookups).
- Event sourcing often complements CQRS (writes generate events → update read projections).

Pros:

- Scalability: write and read can be scaled independently.
- Optimized for performance: queries can be denormalized.
- Easier to handle complex business rules on write side.

Cons:

- Complexity: requires eventual consistency between read/write.
- Infrastructure overhead (projections, messaging).
- Harder debugging due to async updates.

Used in: High-traffic apps, financial systems, e-commerce order tracking, microservices.

---

### 16) **Event Sourcing**

**Intent:** Store state as a sequence of events.
**Use when:** Auditing, replay, temporal queries.

---

### 17) **Two-Phase Commit (2PC)**

**Intent:** Ensure all participants in a transaction commit or rollback together.
**Use when:** Distributed database transactions.

Workflow:

Prepare Phase (Voting): Coordinator asks all participants: “Can you commit?”

Each participant locks resources, logs state, replies YES/NO.

Commit Phase:

- If all say YES → send COMMIT.
- If any says NO → send ROLLBACK.

Pros:

- Strong consistency (atomic commit).
- Simple, widely implemented (databases, XA transactions).

Cons:

- Blocking: if coordinator crashes after prepare, participants may wait indefinitely.
- Performance overhead: lots of locking and synchronous waiting.
- Not fault-tolerant in network partitions.

Used in: Classic RDBMS, XA transactions, financial systems.

---

### 18) **Three-Phase Commit**

**Intent:** Extension of 2PC to reduce blocking.
**Use when:** Coordinating commits in unreliable networks.

Workflow: Adds an extra phase (Pre-Commit).

- CanCommit: Coordinator asks participants if they can commit.
- PreCommit: If all YES, coordinator sends PREPARE TO COMMIT → participants log "ready" (but not final).
- DoCommit: Coordinator finally sends COMMIT.

Pros:

- Non-blocking in certain crash scenarios (participants can decide if no coordinator).
- Better failure handling than 2PC.

Cons:

- Still vulnerable to network partitions (split brain).
- More overhead (extra round-trip).
- Rarely implemented in practice (too complex).

Used in: Mostly academic/research. Industry uses Raft/Paxos instead.

---

### 19) **Cache Aside / Distributed Cache**

**Intent:** Application loads data into cache on demand.
**Use when:** Improve performance and reduce DB load (Redis, Memcached).

---

### 20) **Load Balancer**

**Intent:** Distribute requests among multiple servers.
**Use when:** Scale services horizontally.

Types:

- Round Robin: simple cycling.
- Least Connections: pick server with fewest active connections.
- IP Hash / Consistent Hashing: map client to server deterministically.
- Layer 4 (Transport): TCP/UDP routing.
- Layer 7 (Application): HTTP header, URL-aware routing.

Pros:

- Improves availability and fault tolerance.
- Scales horizontally (add more servers).
- Can provide SSL termination, caching, health checks.

Cons:

- Can become a single point of failure (unless itself replicated).
- Requires session persistence (“sticky sessions”) if stateful.
- Adds latency hop.

Used in: Nginx, HAProxy, AWS ELB, Kubernetes Services, Cloudflare.

---

### 21) **Gossip / Epidemic Protocol**

**Intent:** Spread information probabilistically like a virus.
**Use when:** Scalable membership, failure detection (Cassandra, DynamoDB).

Workflow:

- Each node periodically picks random peers and exchanges state.
- Over time, all nodes converge to the same state (eventual consistency).

Types of Gossip:

- Epidemic broadcast: spread messages.
- Failure detection: nodes gossip about suspected failures.
- Anti-entropy: sync state databases.

Pros:

- Scales to 1000s of nodes.
- No single point of failure.
- Naturally fault-tolerant, resilient to partitions.

Cons:

- Eventual consistency (not immediate).
- Redundant message passing (network overhead).
- Hard to guarantee strict ordering.

Used in: Cassandra, DynamoDB, Akka Cluster, Consul, Kubernetes node health.

---

### 22) **Quorum**

**Intent:** Require majority agreement before proceeding. Ensure consistency in distributed systems by requiring a minimum number of nodes to agree before committing.
**Use when:** Strong consistency guarantees (distributed DBs).

Workflow (common in distributed databases):

- R = Read quorum (# of replicas that must respond to a read).
- W = Write quorum (# of replicas that must acknowledge a write).
- With N replicas total, if R + W > N, strong consistency is guaranteed.

Pros:

- Balance between availability and consistency.
- Tunable consistency model.
- Works well with replication.

Cons:

- Higher latency for strict quorum.
- Tradeoff: stronger consistency reduces availability.
- Network partitions → may reduce progress.

Used in: Cassandra, DynamoDB, Riak, quorum-based replication systems.

---

### 23) **Vector Clocks / Lamport Clocks**

**Intent:** Track causality in distributed systems.
**Use when:** Versioning and conflict resolution in eventually consistent DBs.

Workflow:

- Each node keeps a vector `[n1, n2, …, nk]` (counters per node).
- On local event: increment own counter.
- On message: send vector; receiver merges by taking max per element.
- Comparison:
    - A → B (causal order): all elements in A ≤ B, and at least one <.
    - Concurrent: neither dominates (conflict).

Pros:

- Captures causality and concurrency precisely.
- Helps resolve conflicts (e.g., last-write-wins not needed).

Cons:

- Overhead: vector grows with number of nodes.
- Complex conflict resolution logic still needed.
- Not suitable for very large dynamic systems.

Used in: Amazon Dynamo, Riak, CRDTs, versioning in eventually consistent stores.

---

### 24) **Strangler Fig**

**Intent:** Gradually replace legacy systems by routing traffic incrementally to new services.
**Use when:** Migration from monolith to microservices.

Workflow:

- Add a facade/proxy layer in front of legacy system.
- Route new functionality to new services.
- Gradually migrate old features behind proxy.
- Legacy system “strangled” and eventually retired.

Pros:

- Smooth migration, no big-bang rewrite.
- Reduces risk: legacy and new coexist.
- Enables continuous delivery.

Cons:

- Requires proxy layer and routing.
- Can increase temporary system complexity.
- Migration can be slow if not managed properly.

Used in: Monolith → Microservices migration, cloud modernization, API upgrades.

---

### Cheat Sheet – When to Use What (Distributed)

| Pattern                        | When to Use                                 |
| ------------------------------ | ------------------------------------------- |
| **Broker**                     | Transparent remote service invocation       |
| **Client–Server**              | Centralized service model                   |
| **Peer-to-Peer**               | Decentralized systems (no central server)   |
| **Remote Proxy**               | Transparent remote calls                    |
| **Message Queue**              | Async communication, decoupling             |
| **Publish–Subscribe**          | Event-driven architecture                   |
| **Leader Election**            | Consensus, coordination                     |
| **Replication**                | High availability, fault tolerance          |
| **Sharding**                   | Scaling databases horizontally              |
| **MapReduce**                  | Parallel big data processing                |
| **Service Registry/Discovery** | Microservices dynamic lookup                |
| **Circuit Breaker**            | Fault tolerance, prevent cascading failures |
| **Bulkhead**                   | Failure isolation                           |
| **Saga**                       | Distributed transaction workflows           |
| **CQRS**                       | Separate read/write scalability             |
| **Event Sourcing**             | Event-driven state, auditing                |
| **2PC/3PC**                    | Strongly consistent distributed commits     |
| **Cache Aside**                | Improve performance with caching            |
| **Load Balancer**              | Scale horizontally, distribute load         |
| **Gossip**                     | Membership, eventual consistency            |
| **Quorum**                     | Strong consistency requirement              |
| **Vector/Lamport Clocks**      | Causal ordering of events                   |
| **Strangler Fig**              | Gradual migration from monolith             |

---

## Advanced Design Patterns

### 1) **Microkernel (Plug-in / Plugin)**

**Intent:** Separate a minimal core system from extensible plug-ins.
**Use when:** You need a small stable core but lots of extensibility (OS kernels, Eclipse, IDEs).

* **Core System:** Manages lifecycle, communication, resource access.
* **Plug-ins:** Add features, loaded dynamically.

```java
// Core
interface Plugin { void execute(); }
class Microkernel {
    private final List<Plugin> plugins = new ArrayList<>();
    void register(Plugin p){ plugins.add(p); }
    void run(){ for(Plugin p: plugins) p.execute(); }
}

// Plugin
class LoggingPlugin implements Plugin {
    public void execute(){ System.out.println("Logging..."); }
}

public class Demo {
    public static void main(String[] args){
        Microkernel kernel = new Microkernel();
        kernel.register(new LoggingPlugin());
        kernel.run();
    }
}
```

**Examples:** Eclipse IDE, OS kernels, web servers with modules.

---

### 2) **Entity–Component–System (ECS / ECST)**

**Intent:** Separate data (entities), behavior (systems), and attributes (components).
**Use when:** Highly dynamic composition of game/real-time simulation objects.

* **Entity:** Just an ID.
* **Component:** Data (e.g., Position, Velocity).
* **System:** Processes entities with matching components.

```java
class Entity { final int id; Entity(int id){ this.id=id; } }

class Position { int x,y; }
class Velocity { int dx,dy; }

class MovementSystem {
    void update(Map<Integer, Position> pos, Map<Integer, Velocity> vel){
        for(var id: vel.keySet()){
            Position p = pos.get(id); Velocity v = vel.get(id);
            if(p!=null) { p.x+=v.dx; p.y+=v.dy; }
        }
    }
}

public class Demo {
    public static void main(String[] args){
        Map<Integer, Position> pos = new HashMap<>();
        Map<Integer, Velocity> vel = new HashMap<>();
        pos.put(1,new Position()); vel.put(1,new Velocity(){ {dx=1; dy=2;} });
        new MovementSystem().update(pos,vel);
        System.out.println("Entity 1 at ("+pos.get(1).x+","+pos.get(1).y+")");
    }
}
```

**Examples:** Unity, Unreal Engine, simulation frameworks.

---

### 3) **Adaptive System Pattern**

**Intent:** Systems adjust behavior in response to changing environments or requirements.
**Use when:** Self-optimizing, self-healing, or context-aware software is needed.

Key mechanisms:

* **Monitoring** (collect metrics).
* **Analyzing** (detect conditions).
* **Planning** (decide adaptation).
* **Execution** (apply change).

*(Also called **MAPE loop** in autonomic computing.)*

```java
interface Strategy { void execute(); }

class HighLoadStrategy implements Strategy { public void execute(){ System.out.println("Scaling up resources"); } }
class LowLoadStrategy implements Strategy { public void execute(){ System.out.println("Scaling down resources"); } }

class AdaptiveSystem {
    void adapt(int load){
        Strategy s = (load > 70) ? new HighLoadStrategy() : new LowLoadStrategy();
        s.execute();
    }
}

public class Demo {
    public static void main(String[] args){
        AdaptiveSystem sys = new AdaptiveSystem();
        sys.adapt(80); // scale up
        sys.adapt(20); // scale down
    }
}
```

**Examples:** Cloud auto-scaling, adaptive UI, self-healing systems.

---

### 4) **Model-Driven Architecture (MDA) / Model-Driven Pattern**

**Intent:** Use high-level abstract models (platform-independent) that can be transformed into executable code (platform-specific).
**Use when:** Large systems where abstractions should outlive underlying tech stacks.

* **PIM (Platform Independent Model)**: high-level UML or DSL.
* **PSM (Platform Specific Model)**: generated model for Java, .NET, etc.
* **Transformations**: map PIM → PSM → Code.

```java
// Pseudo Example
abstract class WorkflowModel { abstract void generateCode(); }

class OrderWorkflow extends WorkflowModel {
    void generateCode(){ System.out.println("Generating Java code for Order Processing"); }
}

public class Demo {
    public static void main(String[] args){
        WorkflowModel model = new OrderWorkflow();
        model.generateCode(); // simulate MDA transformation
    }
}
```

**Examples:** OMG’s MDA, Eclipse Modeling Framework (EMF), domain-specific languages.

---

### 5) **Reflection / Meta-Architecture Pattern**

**Intent:** A system can modify its own structure/behavior at runtime.
**Use when:** Need highly dynamic adaptation (e.g., ORMs, middleware).

```java
class Reflective {
    void invokeMethod(Object obj, String method) throws Exception {
        obj.getClass().getMethod(method).invoke(obj);
    }
}

class Service { public void sayHi(){ System.out.println("Hello!"); } }

public class Demo {
    public static void main(String[] args) throws Exception {
        new Reflective().invokeMethod(new Service(), "sayHi");
    }
}
```

**Examples:** Java Reflection API, Hibernate, Spring Framework.

---

### 6) **Layered System (a.k.a. Hexagonal / Onion variants)**

**Intent:** Organize system into hierarchical layers with strict dependencies.
**Use when:** Separation of concerns, portability.

---

### 7) **Blackboard (Extended from Behavioral)**

**Intent:** Multiple specialized subsystems contribute incrementally to solve a problem via a common “blackboard.”
**Use when:** Problem-solving with incomplete knowledge (speech recognition, AI).

---

### Cheat Sheet – Advanced Patterns

| Pattern                           | When to Use                                             |
| --------------------------------- | ------------------------------------------------------- |
| **Microkernel**                   | Stable core, extensible plugins (OS, IDEs, servers)     |
| **ECS (Entity-Component-System)** | Game dev, simulations, highly composable objects        |
| **Adaptive System**               | Self-healing, auto-scaling, runtime adaptation          |
| **Model-Driven**                  | Generate code from abstract models, portability         |
| **Reflection/Meta-Arch**          | Runtime adaptability, frameworks, ORMs                  |
| **Layered/Hexagonal**             | Clear separation of concerns, testability               |
| **Blackboard**                    | Complex problem solving from multiple knowledge sources |

---
