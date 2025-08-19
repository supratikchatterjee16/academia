# Software Design Patterns

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
