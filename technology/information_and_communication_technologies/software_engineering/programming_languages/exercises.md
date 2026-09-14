# Progressive Programming Language Exercises

## Curriculum Philosophy

The purpose of these exercises is not to teach language syntax in isolation.

Each project should force the learner to encounter the constructs that are commonly required when building real software:

* data modelling
* control flow
* functions and modularity
* collections
* error handling
* file I/O
* resource management
* abstraction
* serialization
* networking
* concurrency
* testing
* packaging
* process management
* performance
* failure handling

### General rules

1. **Use the language's standard library initially.**
2. **Do not introduce a framework merely to avoid implementing something.**
3. Each exercise should begin with a minimal implementation.
4. Subsequent milestones add requirements rather than replacing the original implementation.
5. The learner should write tests as soon as the program becomes non-trivial.
6. Error paths are part of the exercise, not optional polish.
7. The learner should be able to explain why a particular language construct was used.
8. Avoid giving learners the implementation architecture upfront. Give them requirements and let the architecture emerge.

---

## 1. C

C should primarily teach the learner to reason about:

> memory, representation, pointers, resources, processes, and the operating system.

---

### Exercise 1 — Binary File Inspector

#### Objective

Build a command-line program capable of inspecting arbitrary files.

#### Command

```bash
bininspect <file>
```

Example:

```text
File: example.bin
Size: 182734 bytes
Printable ASCII: 63.4%
Zero bytes: 12483
Unique byte values: 247
```

#### Milestone 1 — Basic File Reading

Implement:

* command-line argument parsing
* file opening
* file reading
* file size calculation
* error reporting

#### Milestone 2 — Byte Analysis

Calculate:

* frequency of every byte value
* number of zero bytes
* number of printable characters
* minimum/maximum byte value

#### Milestone 3 — Hex Dump

Implement:

```bash
bininspect --hex example.bin
```

Output:

```text
00000000  48 65 6c 6c 6f 20 57 6f  72 6c 64
0000000b  ...
```

#### Milestone 4 — String Extraction

Implement:

```bash
bininspect --strings example.bin
```

Extract printable character sequences.

#### Concepts deliberately encountered

* primitive types
* arrays
* pointers
* pointer arithmetic
* `char`
* `unsigned char`
* `size_t`
* structs
* functions
* command-line arguments
* file descriptors / `FILE *`
* `fopen`
* `fread`
* `fseek`
* `malloc`
* `free`
* header files
* compilation and linking

#### Completion criterion

The learner should be able to explain:

* why binary data should generally be treated as `unsigned char`
* why `sizeof` is preferable to assumptions about type sizes
* who owns dynamically allocated memory
* what happens when `fread()` fails

---

### Exercise 2 — Generic Data Structure Library

Build a small reusable collection library.

Implement:

```text
vector
linked_list
hash_map
string
```

#### Example API

```c
vector_t *vector_create(size_t element_size);

int vector_push(
    vector_t *vector,
    const void *element
);

void *vector_get(
    vector_t *vector,
    size_t index
);

void vector_destroy(vector_t *vector);
```

#### Milestone 1

Implement a dynamic vector.

Requirements:

* automatic growth
* indexed access
* insertion
* removal
* destruction

#### Milestone 2

Make the vector generic.

It must support:

```c
int
double
struct User
struct Packet
```

without duplicating the implementation.

#### Milestone 3

Add callbacks for:

* comparison
* destruction
* iteration

#### Milestone 4

Build a hash map.

```text
key → value
```

#### Concepts deliberately encountered

* pointers
* pointer-to-pointer
* dynamic allocation
* ownership
* opaque structures
* header/source separation
* function pointers
* callbacks
* `const`
* `static`
* macros
* generic programming using `void *`
* memory layout

#### Completion criterion

The learner should be able to answer:

> What exactly is stored in memory when a `vector_t` contains 100 structures?

---

### Exercise 3 — Mini Unix Shell

Build:

```bash
myshell
```

Initial commands:

```bash
$ pwd
$ cd /tmp
$ echo hello
$ cat file.txt
$ ./program argument
```

#### Milestone 1

Implement:

* command parsing
* argument parsing
* built-in `cd`
* built-in `exit`
* external program execution

#### Milestone 2

Add:

```bash
program > output.txt
program < input.txt
```

#### Milestone 3

Add pipelines:

```bash
cat file.txt | grep hello
```

#### Milestone 4

Add background execution:

```bash
long-running-program &
```

#### Milestone 5

Add signal handling.

#### Concepts

* `fork`
* `exec`
* `wait`
* processes
* process IDs
* file descriptors
* pipes
* signals
* environment variables
* process lifecycle
* parsing
* memory management

#### Completion criterion

The learner should be able to describe the lifecycle of:

```bash
ls | grep foo > output.txt
```

from shell input to process termination.

---

## 2. C++

C++ should teach:

> abstraction + resource ownership + generic programming + concurrency.

---

### Exercise 1 — In-Memory Database

Build:

```bash
dbcli
```

Support:

```text
CREATE USER
INSERT USER 42 Alice
GET USER 42
DELETE USER 42
LIST USERS
```

#### Milestone 1

Implement classes representing:

```text
User
Database
Command
```

#### Milestone 2

Use STL containers.

#### Milestone 3

Add validation and exceptions.

#### Milestone 4

Add multiple entity types.

```text
User
Order
Product
```

#### Concepts

* classes
* constructors
* destructors
* methods
* references
* `const`
* `std::string`
* `std::vector`
* `std::unordered_map`
* enums
* namespaces
* exceptions
* iterators
* algorithms

---

### Exercise 2 — Persistent Database

Extend the database to persist data.

```text
dbcli
   ↓
Database
   ↓
Storage
   ↓
database.db
```

#### Milestone 1

Binary serialization.

#### Milestone 2

Deserialization.

#### Milestone 3

Crash-safe writes.

#### Milestone 4

Add an index.

#### Milestone 5

Add transactions:

```text
BEGIN
INSERT ...
UPDATE ...
COMMIT
ROLLBACK
```

#### Concepts

* RAII
* smart pointers
* `std::unique_ptr`
* `std::shared_ptr`
* move semantics
* copy semantics
* move constructors
* templates
* serialization
* filesystem
* exception safety
* resource ownership

---

### Exercise 3 — HTTP Server

Build:

```bash
cpphttp --port 8080 --root ./www
```

#### Milestone 1

Implement TCP connection handling.

#### Milestone 2

Parse:

```http
GET /index.html HTTP/1.1
```

#### Milestone 3

Generate HTTP responses.

#### Milestone 4

Serve static files.

#### Milestone 5

Implement routing.

```text
GET /users
GET /users/42
POST /users
```

#### Milestone 6

Implement concurrency.

First:

```text
one thread / connection
```

Then:

```text
thread pool
```

#### Milestone 7

Implement graceful shutdown.

#### Concepts

* sockets
* STL
* RAII
* smart pointers
* move semantics
* lambdas
* threads
* mutexes
* condition variables
* atomics
* filesystem
* error handling
* HTTP

#### Intermediate checkpoint

The learner should understand why RAII is particularly useful for:

```text
socket
file
mutex
connection
memory
```

---

## 3. Rust

Rust should deliberately force learners to understand:

> ownership, borrowing, lifetimes, algebraic data types, traits, error handling, and safe concurrency.

---

### Exercise 1 — Text Statistics

Build:

```bash
textstat file.txt
```

Output:

```text
Lines:        1432
Words:        21894
Characters:   127331
Unique words: 4821
```

#### Milestone 1

Basic file reading.

#### Milestone 2

Word counting.

#### Milestone 3

Frequency table.

#### Milestone 4

Add:

```bash
textstat --top 20 file.txt
```

#### Milestone 5

Process multiple files.

#### Concepts

* variables
* mutability
* primitive types
* `String`
* `&str`
* slices
* `Vec<T>`
* `HashMap`
* functions
* modules
* iterators
* `Option`
* `Result`
* pattern matching
* ownership
* borrowing

#### Critical exercise

Rewrite the program so that it does **not** load the entire input file into memory.

The learner should discover streaming and borrowing naturally.

---

### Exercise 2 — Log Processing Engine

Input:

```text
2026-09-14T10:32:11 GET /api/users 200 421
2026-09-14T10:32:12 GET /api/users 200 391
2026-09-14T10:32:13 POST /api/users 500 128
```

Build:

```bash
logproc access.log
```

Output:

```text
Requests:       100023
Successful:      99431
Errors:            592
Average latency: 31ms
P95 latency:     112ms
```

#### Milestone 1

Define:

```rust
struct LogEntry {
    ...
}
```

#### Milestone 2

Introduce:

```rust
enum ParseError {
    ...
}
```

#### Milestone 3

Implement filtering.

#### Milestone 4

Implement streaming processing.

#### Milestone 5

Add unit tests.

#### Milestone 6

Implement configurable output.

#### Milestone 7

Investigate zero-copy parsing.

#### Concepts

* structs
* enums
* `impl`
* methods
* traits
* generic functions
* iterators
* closures
* pattern matching
* `Result<T, E>`
* `Option<T>`
* `?`
* custom errors
* lifetimes
* borrowing
* zero-copy data

---

### Exercise 3 — Concurrent TCP Server

Build:

```bash
kvserver 127.0.0.1:9000
```

Protocol:

```text
SET name Alice
GET name
DELETE name
```

#### Milestone 1

TCP server.

#### Milestone 2

Request parser.

#### Milestone 3

Key-value store.

#### Milestone 4

Multiple clients.

#### Milestone 5

Shared state.

#### Milestone 6

Worker pool.

#### Milestone 7

Graceful shutdown.

#### Concepts

* `TcpListener`
* `TcpStream`
* threads
* channels
* `Arc`
* `Mutex`
* `Send`
* `Sync`
* ownership across threads
* synchronization
* `Drop`
* error propagation

#### Intermediate checkpoint

The learner should be able to explain why Rust rejects data races at compile time rather than relying solely on runtime discipline.

---

## 4. Java

### Exercise 1 — File-Backed CLI

Build:

```bash
notes add "Learn Java"
notes list
notes delete 3
```

#### Milestone 1

In-memory implementation.

#### Milestone 2

File persistence.

#### Milestone 3

Introduce interfaces.

```text
NoteRepository
FileNoteRepository
```

#### Milestone 4

Add validation and error handling.

#### Milestone 5

Add tests.

#### Concepts

* classes
* objects
* constructors
* methods
* interfaces
* inheritance
* polymorphism
* collections
* generics
* enums
* exceptions
* streams
* file I/O
* Maven

---

### Exercise 2 — HTTP Server Using Sockets

Build an HTTP server using:

```java
ServerSocket
Socket
InputStream
OutputStream
```

Do not use a servlet container.

#### Milestone 1

Accept a TCP connection.

#### Milestone 2

Parse an HTTP request.

#### Milestone 3

Return:

```http
HTTP/1.1 200 OK
```

#### Milestone 4

Implement routing.

```text
GET /
GET /users
GET /users/42
```

#### Milestone 5

Implement POST bodies.

#### Milestone 6

Implement error responses.

```text
400
404
405
500
```

#### Milestone 7

Add concurrent connections.

#### Concepts

* networking
* byte streams
* character encoding
* interfaces
* classes
* collections
* exceptions
* threads
* `ExecutorService`
* HTTP
* Maven

---

### Exercise 3 — Dynamic WAR/Application Loader

Extend the HTTP server so that applications can be loaded dynamically.

Directory:

```text
server/
applications/
    application-a.war
    application-b.war
```

#### Milestone 1

Read a WAR file as an archive.

#### Milestone 2

Discover application metadata.

#### Milestone 3

Load classes dynamically.

#### Milestone 4

Define an application interface.

```java
interface WebApplication {
    Response handle(Request request);
}
```

#### Milestone 5

Use separate class loaders.

#### Milestone 6

Implement application lifecycle.

```text
load
start
handle
stop
unload
```

#### Concepts

* JAR/WAR structure
* class loaders
* reflection
* interfaces
* dynamic class loading
* lifecycle management
* resource management
* concurrency
* Maven

#### Intermediate checkpoint

The learner should understand the distinction between:

```text
Java language
JVM
class loading
application framework
application server
```

rather than treating them as one system.

---

## 5. Python

Python should expose:

> dynamic data modelling, modules, exceptions, iterators, generators, packaging, external APIs, persistence, and concurrency.

---

### Exercise 1 — CSV Data Processor

Build:

```bash
csvtool data.csv
```

Support:

```bash
csvtool --count data.csv
csvtool --filter country=IN data.csv
csvtool --sort age data.csv
csvtool --group country data.csv
```

#### Milestone 1

Read CSV.

#### Milestone 2

Represent records using dictionaries.

#### Milestone 3

Implement filtering.

#### Milestone 4

Implement sorting.

#### Milestone 5

Implement grouping.

#### Milestone 6

Add `argparse`.

#### Milestone 7

Add generators so large files can be processed without loading everything into memory.

#### Concepts

* variables
* lists
* dictionaries
* tuples
* sets
* functions
* comprehensions
* modules
* exceptions
* iterators
* generators
* `argparse`
* file I/O

---

### Exercise 2 — REST Data Importer

Build:

```text
REST API
    ↓
requests
    ↓
validation
    ↓
SQLAlchemy
    ↓
database
    ↓
CLI
```

#### Milestone 1

Retrieve JSON from an API.

#### Milestone 2

Parse the response.

#### Milestone 3

Create SQLAlchemy models using `declarative_base`.

#### Milestone 4

Persist the records.

#### Milestone 5

Handle:

* pagination
* timeouts
* retries
* HTTP errors
* malformed responses

#### Milestone 6

Make imports idempotent.

Running:

```bash
mytool import
mytool import
```

should not create duplicates.

#### Milestone 7

Package it.

```bash
pip install mytool
```

#### Milestone 8

Provide:

```bash
mytool import
mytool list
mytool report
```

#### Concepts

* external packages
* virtual environments
* modules
* packages
* classes
* exceptions
* decorators
* context managers
* type hints
* HTTP
* SQLAlchemy
* CLI design
* packaging

---

### Exercise 3 — Concurrent Job Runner

Build:

```bash
jobrunner jobs.yaml
```

Example:

```yaml
jobs:
  - name: download
    command: download.py

  - name: process
    command: process.py
    depends_on:
      - download

  - name: report
    command: report.py
    depends_on:
      - process
```

#### Milestone 1

Sequential execution.

#### Milestone 2

Dependency handling.

#### Milestone 3

Parallel execution of independent jobs.

#### Milestone 4

Retries.

#### Milestone 5

Timeouts.

#### Milestone 6

Cancellation.

#### Milestone 7

Persistent job state.

#### Concepts

* `threading`
* `multiprocessing`
* `asyncio`
* queues
* futures
* subprocesses
* context managers
* decorators
* type hints
* serialization
* concurrency models

#### Intermediate checkpoint

The learner should be able to explain when to use:

```text
threading
multiprocessing
asyncio
```

and why.

---

## 6. TypeScript + Node.js

The distinction here is important:

> Teach TypeScript as a language and Node.js as a runtime.

Do not start with Express.

---

### Exercise 1 — Typed CLI Application

Build:

```bash
todo add "Learn TypeScript"
todo list
todo done 4
todo remove 4
```

Persist to JSON.

#### Milestone 1

In-memory implementation.

#### Milestone 2

Define interfaces/types.

```typescript
interface Todo {
    id: number;
    text: string;
    completed: boolean;
}
```

#### Milestone 3

Persistence.

#### Milestone 4

Error handling.

#### Milestone 5

Async file operations.

#### Milestone 6

Unit tests.

#### Concepts

* primitive types
* interfaces
* type aliases
* unions
* arrays
* objects
* functions
* optional properties
* generics
* modules
* promises
* `async/await`
* Node filesystem APIs

---

### Exercise 2 — REST Synchronizer

Build:

```text
REST API
    ↓
HTTP client
    ↓
unknown JSON
    ↓
validation
    ↓
domain model
    ↓
database
```

#### Milestone 1

Retrieve remote JSON.

#### Milestone 2

Treat external input as:

```typescript
unknown
```

rather than:

```typescript
any
```

#### Milestone 3

Validate the response.

#### Milestone 4

Map API DTOs into domain objects.

#### Milestone 5

Persist locally.

#### Milestone 6

Implement retries and timeouts.

#### Milestone 7

Handle pagination.

#### Milestone 8

Build a CLI.

#### Concepts

* interfaces
* type aliases
* generics
* discriminated unions
* type narrowing
* `unknown`
* `never`
* promises
* async/await
* modules
* error handling
* runtime validation
* Node APIs

#### Critical lesson

The learner must explicitly understand:

```text
TypeScript types
        ≠
runtime validation
```

External JSON is untrusted runtime data regardless of its declared TypeScript type.

---

### Exercise 3 — HTTP Server Without Express

Build:

```typescript
http.createServer(...)
```

#### Milestone 1

Return:

```text
Hello World
```

#### Milestone 2

Parse HTTP requests.

#### Milestone 3

Implement routing.

```text
GET /
GET /users
GET /users/:id
```

#### Milestone 4

Implement POST.

#### Milestone 5

Implement middleware.

```text
request
   ↓
logging middleware
   ↓
authentication middleware
   ↓
router
   ↓
handler
```

#### Milestone 6

Implement streaming responses.

#### Milestone 7

Implement graceful shutdown.

#### Milestone 8

Investigate backpressure.

#### Concepts

* Node event loop
* callbacks
* promises
* async/await
* events
* streams
* buffers
* backpressure
* closures
* higher-order functions
* generics
* discriminated unions
* module architecture

#### Intermediate checkpoint

The learner should understand why Node can handle many concurrent I/O operations without creating one OS thread per request.

---

## 7. POSIX Shell

The purpose of shell exercises is not to turn the learner into a shell-language programmer.

It is to teach:

> Unix processes + pipelines + file descriptors + exit status + orchestration.

---

### Exercise 1 — Backup Utility

Build:

```bash
backup source destination
```

Example:

```bash
backup ~/documents /backup
```

Produce:

```text
/backup/documents-2026-09-14.tar.gz
```

#### Milestone 1

Copy files.

#### Milestone 2

Recursive directory handling.

#### Milestone 3

Compression.

#### Milestone 4

Checksums.

#### Milestone 5

Dry-run mode.

```bash
backup --dry-run ...
```

#### Milestone 6

Logging.

#### Concepts

* variables
* quoting
* command substitution
* positional parameters
* exit codes
* pipelines
* redirection
* globbing
* `find`
* `tar`
* compression
* checksums

---

### Exercise 2 — Deployment Pipeline

Build:

```bash
deploy.sh
```

Pipeline:

```text
validate
   ↓
build
   ↓
test
   ↓
package
   ↓
deploy
   ↓
health check
```

#### Requirement

If any step fails, subsequent steps must not execute.

#### Add

```bash
deploy.sh --dry-run
deploy.sh --rollback
deploy.sh --verbose
```

#### Concepts

* exit status
* command chaining
* environment variables
* temporary files
* traps
* signals
* atomic operations
* pipeline failure
* process orchestration

#### Critical checkpoint

The learner must understand why:

```bash
A | B
```

does not necessarily propagate the failure of `A` in every shell configuration.

---

## 8. Bash

After the POSIX exercise, move to Bash-specific functionality.

---

### Exercise 1 — System Information Utility

Build:

```bash
sysinfo
```

Output:

```text
Hostname:
Kernel:
Architecture:
CPU:
Memory:
Disk:
Uptime:
Processes:
```

#### Milestone 1

Collect information.

#### Milestone 2

Format it.

#### Milestone 3

Add options.

```bash
sysinfo --cpu
sysinfo --memory
sysinfo --disk
sysinfo --json
```

#### Concepts

* variables
* functions
* `case`
* parameter expansion
* command substitution
* arrays
* loops
* exit status
* functions

---

### Exercise 2 — Deployment Pipeline

Repeat the POSIX deployment exercise, but this time require Bash-specific constructs.

Implement:

```bash
deploy.sh
```

with:

* functions
* arrays
* configuration variables
* `trap`
* cleanup
* logging
* rollback

#### Concepts

* Bash arrays
* associative arrays
* `local`
* `[[ ]]`
* parameter expansion
* functions
* traps
* subshells
* file descriptors

---

### Exercise 3 — Parallel Job Executor

Build:

```bash
batchrun -j 4 jobs.txt
```

Input:

```text
./job1.sh
./job2.sh
./job3.sh
./job4.sh
./job5.sh
```

At most four jobs may execute simultaneously.

Output:

```text
job1   SUCCESS   12.3s
job2   FAILED     4.2s
job3   SUCCESS    8.1s
job4   SUCCESS    9.7s
job5   SUCCESS    2.4s
```

#### Milestone 1

Sequential execution.

#### Milestone 2

Background processes.

#### Milestone 3

Limit concurrency.

#### Milestone 4

Collect exit codes.

#### Milestone 5

Capture stdout/stderr.

#### Milestone 6

Handle `SIGINT`.

#### Milestone 7

Clean up child processes.

#### Concepts

* background processes
* `&`
* `wait`
* `$!`
* arrays
* associative arrays
* traps
* signals
* process groups
* file descriptors
* exit status
* concurrency

#### Intermediate checkpoint

The learner should understand that Bash concurrency is fundamentally **process orchestration**, not language-level multithreading.

---

## 9. Cross-Language Capstone

Once a learner completes the three projects for their chosen language, give them the same final specification.

### Capstone — Minimal HTTP File Server

#### Objective

Build a minimal HTTP/1.1 server without an HTTP framework.

#### Required functionality

```text
GET /
GET /index.html
GET /file.txt
404
400
405
```

#### Phase 1 — TCP

Accept connections.

```text
TCP connection
    ↓
read bytes
    ↓
close
```

#### Phase 2 — HTTP

Parse:

```http
GET /index.html HTTP/1.1
Host: localhost
```

#### Phase 3 — Response

Return:

```http
HTTP/1.1 200 OK
Content-Length: 123
Content-Type: text/html

...
```

#### Phase 4 — Routing

Implement:

```text
/
 /index.html
 /about.html
```

#### Phase 5 — Static Files

Map URLs to files.

#### Phase 6 — Security

Prevent:

```text
GET /../../../etc/passwd
```

from escaping the document root.

#### Phase 7 — Concurrency

Support multiple simultaneous clients.

#### Phase 8 — Operational Behaviour

Implement:

* configuration
* logging
* graceful shutdown
* connection limits
* malformed-request handling
* timeouts

#### Phase 9 — Testing

Create tests for:

* valid requests
* malformed requests
* missing files
* traversal attempts
* large files
* concurrent clients
* client disconnects

#### Phase 10 — Benchmarking

Measure:

```text
requests/sec
latency
memory consumption
CPU utilization
```

---

## 10. Language-Specific Learning Outcomes

After completing the curriculum, the learner should have encountered approximately the following.

| Concept                    |               C |          C++ |      Rust |    Java |        Python | TypeScript | Shell/Bash |
| -------------------------- | --------------: | -----------: | --------: | ------: | ------------: | ---------: | ---------: |
| Variables/control flow     |               ✓ |            ✓ |         ✓ |       ✓ |             ✓ |          ✓ |          ✓ |
| Functions                  |               ✓ |            ✓ |         ✓ |       ✓ |             ✓ |          ✓ |          ✓ |
| Collections                |               ✓ |            ✓ |         ✓ |       ✓ |             ✓ |          ✓ |          ✓ |
| Structs/classes            |               ✓ |            ✓ |         ✓ |       ✓ |             ✓ |          ✓ |            |
| Interfaces/traits          |                 |            ✓ |         ✓ |       ✓ |             ✓ |          ✓ |            |
| Generics                   |                 |            ✓ |         ✓ |       ✓ |               |          ✓ |            |
| Error handling             |               ✓ |            ✓ |         ✓ |       ✓ |             ✓ |          ✓ |          ✓ |
| File I/O                   |               ✓ |            ✓ |         ✓ |       ✓ |             ✓ |          ✓ |          ✓ |
| Resource management        |               ✓ |            ✓ |         ✓ |       ✓ |             ✓ |          ✓ |          ✓ |
| Memory management          |               ✓ |            ✓ |         ✓ |         |               |            |            |
| Ownership                  |          manual |         RAII | ownership |      GC |            GC |         GC |            |
| Networking                 |               ✓ |            ✓ |         ✓ |       ✓ |             ✓ |          ✓ |          ✓ |
| Concurrency                |       processes |      threads |   threads | threads | threads/async |      async |  processes |
| Packaging                  | compiler/linker | build system |     Cargo |   Maven |           pip |        npm |    scripts |
| Reflection/dynamic loading |                 |              |           |       ✓ |             ✓ |            |            |
| Type system depth          |             low |         high | very high |    high |       dynamic |       high |        low |
| OS/process model           |              ✓✓ |           ✓✓ |         ✓ |       ✓ |             ✓ |          ✓ |         ✓✓ |

---

## 11. Recommended Completion Gates

A learner should **not** advance merely because the program "works."

Use these gates.

### Beginner → Competent

The learner can:

* build the program independently
* explain the major data structures
* handle normal errors
* split code into modules
* write basic tests
* use the compiler/build system independently
* read standard-library documentation

---

### Competent → Intermediate

The learner can:

* redesign part of the application
* identify ownership/resource boundaries
* handle malformed input
* reason about failure
* introduce concurrency
* diagnose race/resource issues
* write meaningful tests
* package the program
* measure basic performance
* explain trade-offs in their implementation

---

## 12. Suggested Evaluation Rubric

Each project can be evaluated out of 100.

| Area                         | Points |
| ---------------------------- | -----: |
| Correct functionality        |     25 |
| Error handling               |     15 |
| Code organisation            |     10 |
| Language idioms              |     15 |
| Tests                        |     10 |
| Resource management          |     10 |
| Documentation                |      5 |
| Performance                  |      5 |
| Debugging/diagnostic quality |      5 |

The **language idioms** category is particularly important.

A program that works but looks like C written in C++, Java written in Python, or JavaScript written in TypeScript should not receive full credit.

---

## 13. Recommended "No Framework" Rule

For the first three exercises in each language:

| Language    | Permitted                                                    |
| ----------- | ------------------------------------------------------------ |
| C           | C standard library + OS APIs                                 |
| C++         | C++ standard library + OS APIs                               |
| Rust        | `std` + Cargo                                                |
| Java        | JDK + Maven                                                  |
| Python      | Python stdlib initially; `requests`/SQLAlchemy in Exercise 2 |
| TypeScript  | TypeScript + Node.js standard APIs                           |
| POSIX Shell | POSIX utilities                                              |
| Bash        | Bash + standard Unix utilities                               |

Only after the learner completes the framework-free implementations should they be allowed to replace portions with mature libraries.

For example:

```text
Raw Node HTTP server
        ↓
understand HTTP
        ↓
Express/Fastify

Raw Java ServerSocket
        ↓
understand HTTP + concurrency
        ↓
Spring/Netty

Raw Rust TCP
        ↓
understand ownership/concurrency/networking
        ↓
Tokio/Axum/Actix

Raw C++ sockets
        ↓
understand resource management/concurrency
        ↓
Asio/Boost/etc.
```

This creates a useful mental model:

> **Frameworks become abstractions that the learner understands, rather than magic that the learner memorises.**

---

## 14. Final Curriculum Map

```text
C
├── Binary File Inspector
│   └── memory / pointers / I/O
├── Generic Data Structure Library
│   └── allocation / callbacks / abstraction
└── Unix Shell
    └── processes / pipes / signals / file descriptors

C++
├── In-Memory Database
│   └── classes / STL / exceptions
├── Persistent Database
│   └── RAII / smart pointers / move semantics / templates
└── HTTP Server
    └── sockets / threads / synchronization / RAII

Rust
├── Text Statistics
│   └── ownership / borrowing / Result / iterators
├── Log Processing Engine
│   └── structs / enums / traits / lifetimes
└── Concurrent TCP Server
    └── Arc / Mutex / channels / Send / Sync

Java
├── File-Backed CLI
│   └── classes / interfaces / collections / Maven
├── Socket HTTP Server
│   └── networking / streams / concurrency
└── Dynamic WAR Loader
    └── reflection / class loaders / dynamic loading

Python
├── CSV Processor
│   └── collections / functions / generators
├── REST → SQLAlchemy → CLI
│   └── packages / HTTP / ORM / argparse
└── Concurrent Job Runner
    └── subprocess / threads / multiprocessing / asyncio

TypeScript + Node
├── Typed CLI
│   └── types / interfaces / modules / async
├── REST Synchronizer
│   └── unknown / validation / generics / promises
└── HTTP Server
    └── event loop / streams / backpressure / async

POSIX Shell
├── Backup Utility
│   └── commands / pipelines / exit codes
└── Deployment Pipeline
    └── orchestration / traps / failure handling

Bash
├── System Information Utility
│   └── Bash language features
├── Deployment Pipeline
│   └── arrays / functions / traps
└── Parallel Job Executor
    └── processes / wait / signals / concurrency
```
