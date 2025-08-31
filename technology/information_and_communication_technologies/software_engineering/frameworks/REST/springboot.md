# REST using Spring Boot

Spring Boot 

Dependencies required:

1. spring-boot-starter-parent
2. spring-boot-starter-web

Core Concepts:

- Dependency Injection
- Exception Handling
- ORM
- Spring Expression Language
- Spring AOP
- Securing
- Fault tolerance(Resilience4J)

These core concepts will be touched upon in their own segments, or will be amalgamated when going through certain features.

## Important Annotations

Spring Core provides Inversion of Control and Dependency Injection via annotations. Some of the important annotations are listed here:

### `@SpringBootApplication`

This is used to indicate a **configuration** class that declares one or more beans and triggers auto-configuration and component scanning. This is euivalent to declaring the following 3 annotations:

- `@SpringBootConfiguration`
- `@EnableAutoConfiguration`
- `@ComponentScan`

These 3 will be covered in subsequent sections. In the standard use case, this is used to indicate the entry point of the application.

### `@SpringBootConfiguration`

This is a specialized `@Configuration` class(described later), but with the semantic meaning that "This is the primary configuration class for a Spring Boot Application".

### `@EnableAutoConfiguration`

This does exactly what it's name suggests. Configuration can also be controlled manually, as the program defines.

### `@ComponentScan`

This tells the framework where to look for the beans(classes annotated as `@Components`, and it's subsequent derivatives). Default is the package of the class where it is declared and all it's sub-packages. This allows a few customization options to define which directories to actually scan.

Example: `@ComponentScan(basePackages = {"com.example.demo.services", "com.example.shared"})`

This also allows filtering, to include/exclude specific beans:

```java
@ComponentScan(
    basePackages = "com.example.demo",
    includeFilters = @ComponentScan.Filter(type = FilterType.ANNOTATION, classes = MyCustomAnnotation.class),
    excludeFilters = @ComponentScan.Filter(type = FilterType.ASSIGNABLE_TYPE, classes = UnwantedService.class)
)
```

This also enables taregtting multiple subpackages in the following way:

```java
@SpringBootApplication
@ComponentScan(basePackages = "com.example.module1")
class Module1App {}

@SpringBootApplication
@ComponentScan(basePackages = "com.example.module2")
class Module2App {}
```

Entrypoint:
```java
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(Module1App.class, args);
        SpringApplication.run(Module2App.class, args);
    }
}
```

This is useful for multi-tenancy, and plugins-based architectures, migrations, running multiple web servers in the same JVM, if running directly, and Testing modules. 

### `@Component`

This is the most generic stereotype annotation, and this marks a class as a Spring-managed component. This is use for classes that do not fit into specialized roles.

Specializations of this annotation are:

| Category                    | Annotation                            | Specializes / Meta-annotated With                                          | Purpose                                                                                             |
| --------------------------- | ------------------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Core Stereotype**         | `@Component`                          | —                                                                          | Generic Spring-managed bean. Catch-all stereotype.                                                  |
|                             | `@Repository`                         | `@Component`                                                               | Persistence/DAO beans; adds exception translation (`PersistenceException` → `DataAccessException`). |
|                             | `@Service`                            | `@Component`                                                               | Business/service layer beans; semantic marker (no extra behavior).                                  |
|                             | `@Controller`                         | `@Component`                                                               | MVC controller for handling web requests (returns views/templates).                                 |
| **REST/Web**                | `@RestController`                     | `@Controller` + `@ResponseBody`                                            | REST controller; shorthand for JSON/XML APIs.                                                       |
|                             | `@ControllerAdvice`                   | `@Component`                                                               | Global advice for controllers (exception handling, data binding, etc.).                             |
|                             | `@RestControllerAdvice`               | `@ControllerAdvice` + `@ResponseBody`                                      | REST-specific global advice (JSON/XML responses).                                                   |
| **Configuration**           | `@Configuration`                      | `@Component`                                                               | Defines Spring configuration classes; holds `@Bean` methods.                                        |
|                             | `@SpringBootConfiguration`            | `@Configuration`                                                           | Specialized configuration for Spring Boot apps.                                                     |
|                             | `@SpringBootApplication`              | `@SpringBootConfiguration` + `@EnableAutoConfiguration` + `@ComponentScan` | Bootstrapping entry point for Spring Boot.                                                          |
| **Messaging / Integration** | `@MessageEndpoint`                    | `@Component`                                                               | Spring Integration: defines a message-driven endpoint.                                              |
|                             | `@Endpoint` (Spring WS)               | `@Component`                                                               | Web Services endpoint (SOAP).                                                                       |
|                             | `@JmsListener`\*                      | Often combined with `@Component`                                           | Marks a method to consume JMS messages (not itself a stereotype, but works in `@Component` beans).  |
|                             | `@KafkaListener`\*                    | Often combined with `@Component`                                           | Marks a method to consume Kafka messages.                                                           |
| **Other Specializations**   | `@Indexed` (Spring Data)              | `@Component`                                                               | Adds Spring Data repository index hints for classpath scanning.                                     |
|                             | `@GraphQlController` (Spring GraphQL) | `@Controller`                                                              | GraphQL controllers for queries/mutations.                                                          |
|                             | `@Endpoint` (Spring Actuator)         | `@Component`                                                               | Defines Actuator endpoints.                                                                         |


### `@Service`

This indicates business logic/service layer class, and is a specialization of `@Component`. Extra features may be applies such as transaction boundaries, and AOP proxies by Spring when applicable.

### `@Repository`

This indicates a DAO/persistence layer, and is a specialization of `@Component`. Catches persistence exceptions and rethrows them as Spring's DataAccessException hierarchy.

### `@Configuration`

This indicates a class as a source of bean definitions, and is a specialization of `@Component`. Spring treats these specially in the following ways:

- Methods inside an annotated class with the annotation `@Bean` return objects registered as beans.
- By default, Spring ensures singleton semantics.

### `@Controller`

Indicates an MVC controller, and is a specialization of `@Component`. This is used with Spring MVC's view resolution(Thymeleaf, JSP, etc.), and returns view names instead of raw data.

### `@RestController`

A specialization of `@Controller`, that combines `@Controller` and `@ResponseBody`. Every method's return value is automatically serialized. Removes the need to put `@ResponseBody` on each method.

### `@Bean`

A method-level annotation used inside a `@Configuration` class, to declare and return a bean that will be managed by the Spring container. This is recognized as a dependency, in other classes declaring this as `@Autowired` or on their constructors, if it is annotated, with `@Component` or some specialization of it. Default bean name is the function name. It allows for using lifecycle methods, by specifying the `initMethod` and `destroyMethod` params.

In case of 2 beans with the same return type
- a `@Qualifier("beanName/functionName")` can be used to explicitly usage.
- Using `@Primary` can also, mark a bean to be used as default unless mentioned otherwise via `@Qualifier`
- Multiple beans of the same type can be utilized, if loaded as a `List`

Example: Multiple implementations of the same interface:

```java
public interface PaymentProcessor {
    void process();
}
// You may have different strategies for the same business logic
@Bean
public PaymentProcessor paypalProcessor() { return new PaypalProcessor(); }

@Bean
public PaymentProcessor stripeProcessor() { return new StripeProcessor(); }
```

Usage:
```java
@Service
public class CheckoutService {
    private final Map<String, PaymentProcessor> processors;

    public CheckoutService(Map<String, PaymentProcessor> processors) {
        this.processors = processors;
    }

    public void checkout(String method) {
        processors.get(method).process();
    }
}
```

Example: Environment specific bean(using the `@Profile` annotation).
```java
@Bean
@Profile("dev")
public DataSource devDataSource() { ... }

@Bean
@Profile("prod")
public DataSource prodDataSource() { ... }
```

Example: Composing functionality with multiple beans. Use case: Logging filters.

```java
@Bean
public Filter authFilter() { return new AuthFilter(); }

@Bean
public Filter metricsFilter() { return new MetricsFilter(); }
```

Then inject them all as:
```java
@Bean
public FilterChain filterChain(List<Filter> filters) {
    return new FilterChain(filters);
}
```

Example: Versioning/Features toggle

```java
@Bean
@Qualifier("v1")
public PricingService pricingServiceV1() { return new PricingServiceV1(); }

@Bean
@Qualifier("v2")
public PricingService pricingServiceV2() { return new PricingServiceV2(); }
```

The select based on config:
```java
public PricingController(@Qualifier("${pricing.version}") PricingService service) {
    this.service = service;
}
```
## Exception Handling

Spring Boot gives a full stack for turning Java exceptions into clean, consistent HTTP errors. Here’s a **comprehensive, practical guide** you can use as a blueprint.

### 1) The moving parts (how exceptions become HTTP responses)

Spring MVC resolves exceptions through a **chain of `HandlerExceptionResolver`s** (in order):

1. `ExceptionHandlerExceptionResolver`

   * Calls your `@ExceptionHandler` methods (local or in `@ControllerAdvice`/`@RestControllerAdvice`).
2. `ResponseStatusExceptionResolver`

   * Applies `@ResponseStatus` on exceptions **or** `ResponseStatusException`.
3. `DefaultHandlerExceptionResolver`

   * Translates common framework exceptions (e.g., `HttpRequestMethodNotSupportedException` → 405).
4. If still unhandled, **BasicErrorController** handles `/error` using **ErrorAttributes**.

### 2) Core ways to shape error responses

#### A) Local `@ExceptionHandler` (controller-specific)

```java
@RestController
@RequestMapping("/orders")
class OrderController {

  @GetMapping("/{id}")
  Order get(@PathVariable long id) { ... }

  @ExceptionHandler(OrderNotFoundException.class)
  ResponseEntity<ProblemDetail> notFound(OrderNotFoundException ex) {
    var pd = ProblemDetail.forStatus(HttpStatus.NOT_FOUND);
    pd.setDetail(ex.getMessage());
    pd.setProperty("errorCode", "ORDER_NOT_FOUND");
    return ResponseEntity.status(HttpStatus.NOT_FOUND).body(pd);
  }
}
```

#### B) Global `@RestControllerAdvice`

*(recommended for consistency across the app)*

```java
@RestControllerAdvice
class GlobalExceptionHandler {

  @ExceptionHandler(MethodArgumentNotValidException.class)
  ResponseEntity<ProblemDetail> validation(MethodArgumentNotValidException ex) {
    var pd = ProblemDetail.forStatus(HttpStatus.BAD_REQUEST);
    pd.setTitle("Validation failed");
    pd.setProperty("errors", ex.getBindingResult()
        .getFieldErrors()
        .stream()
        .map(fe -> Map.of("field", fe.getField(), "message", fe.getDefaultMessage()))
        .toList());
    return ResponseEntity.badRequest().body(pd);
  }

  @ExceptionHandler(ConstraintViolationException.class)
  ResponseEntity<ProblemDetail> constraint(ConstraintViolationException ex) {
    var pd = ProblemDetail.forStatus(HttpStatus.BAD_REQUEST);
    pd.setTitle("Constraint violation");
    pd.setProperty("errors", ex.getConstraintViolations()
        .stream()
        .map(v -> Map.of("path", v.getPropertyPath().toString(), "message", v.getMessage()))
        .toList());
    return ResponseEntity.badRequest().body(pd);
  }

  @ExceptionHandler(ResponseStatusException.class)
  ResponseEntity<ProblemDetail> rse(ResponseStatusException ex) {
    var pd = ProblemDetail.forStatusAndDetail(ex.getStatusCode(), ex.getReason());
    return ResponseEntity.status(ex.getStatusCode()).body(pd);
  }

  @ExceptionHandler(Exception.class)
  ResponseEntity<ProblemDetail> fallback(Exception ex) {
    var pd = ProblemDetail.forStatus(HttpStatus.INTERNAL_SERVER_ERROR);
    pd.setTitle("Unexpected error");
    // Avoid leaking internals in prod:
    // pd.setDetail(ex.getMessage()); // optional (omit in prod)
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(pd);
  }
}
```

> `ProblemDetail` (Spring 6 / Boot 3) implements RFC 7807 “problem+json”. Prefer it for modern APIs.

#### C) `@ResponseStatus` on exceptions (simple mapping)

```java
@ResponseStatus(HttpStatus.NOT_FOUND)
class OrderNotFoundException extends RuntimeException {
  public OrderNotFoundException(long id) { super("Order %d not found".formatted(id)); }
}
```

* Lightweight, but less flexible than explicit handlers.

#### D) Throw `ResponseStatusException` on the fly

```java
if (invalid) {
  throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "Invalid state");
}
```

### 3) Validation errors (the ones you see most)

* **Request body** validation (`@Valid` on `@RequestBody`) → `MethodArgumentNotValidException`.
* **Path/query/header** validation (`@Validated` + constraint annotations on method params) → `ConstraintViolationException`.

Example:

```java
@RestController
@Validated
class UserController {
  @GetMapping("/users")
  List<User> list(@RequestParam @Min(1) int page) { ... }

  @PostMapping("/users")
  User create(@Valid @RequestBody CreateUserDto dto) { ... }
}
```

Handle both in your `@RestControllerAdvice` (see above).

### 4) Customize the default `/error` response

**BasicErrorController** uses **ErrorAttributes** to render `/error`. You can tune exposure via properties:

```yaml
server:
  error:
    include-message: never   # always|on_param|never
    include-binding-errors: never
    include-exception: false
    include-stacktrace: never
```

For deeper control, implement a custom `ErrorAttributes` or extend `DefaultErrorAttributes` to add correlation IDs, error codes, etc.

### 5) Consistency via a simple error model (if not using ProblemDetail)

If you aren’t on Spring 6 / ProblemDetail, standardize this shape:

```json
{
  "timestamp": "2025-08-22T16:00:00Z",
  "status": 404,
  "error": "Not Found",
  "code": "ORDER_NOT_FOUND",
  "message": "Order 123 not found",
  "path": "/orders/123",
  "traceId": "b1d2..."
}
```

Return it from your `@ExceptionHandler`s using a DTO and `ResponseEntity`.

### 6) Transactional rollback and exceptions

* By default, `@Transactional` rolls back on **unchecked** (`RuntimeException`, `Error`).
* If you want rollback on a checked exception:

  ```java
  @Transactional(rollbackFor = MyCheckedException.class)
  public void doWork() { ... }
  ```

### 7) Filters, Security, and async edges

* **Filters** (`OncePerRequestFilter`) wrap the whole servlet chain; you can translate low-level exceptions to API errors there (e.g., mapping deserialization failures before they reach MVC).
* **Spring Security**:

  * Auth failures → `AuthenticationEntryPoint`.
  * Access denials → `AccessDeniedHandler`.
    Configure these to align with your API error format.
* **Async / `@Async`**: exceptions return via `AsyncUncaughtExceptionHandler` for `void` methods, or inside `Future/CompletableFuture` for async return types — handle or map them accordingly.

### 8) Logging & observability

* Log **once** at the edge (your global handler). Avoid duplicate logs.
* Add a **correlation/trace ID** (e.g., from Sleuth / Micrometer / OpenTelemetry) to both logs and error body.
* Log at appropriate levels:

  * 4xx → `WARN` (client issue)
  * 5xx → `ERROR` (server issue)

### 9) Testing your error handling

Using MockMvc:

```java
@WebMvcTest(controllers = OrderController.class)
class OrderControllerAdviceTest {

  @Autowired MockMvc mvc;

  @Test
  void notFound_isMapped() throws Exception {
    mvc.perform(get("/orders/999"))
       .andExpect(status().isNotFound())
       .andExpect(jsonPath("$.code").value("ORDER_NOT_FOUND"));
  }
}
```

### 10) Performance & startup considerations

* Prefer **centralized** global advice over many scattered local handlers.
* Keep handlers lightweight (no I/O).
* If using `ProblemDetail`, avoid expensive stack captures unless needed.

---

#### Quick checklist (copy/paste)

* [ ] Use **`@RestControllerAdvice` + `@ExceptionHandler`** for a single, consistent error policy.
* [ ] Use **`ProblemDetail`** (Boot 3 / Spring 6) for RFC 7807 responses.
* [ ] Map validation exceptions (`MethodArgumentNotValidException`, `ConstraintViolationException`).
* [ ] Create **domain exceptions** (e.g., `OrderNotFoundException`) and map them to 4xx with stable `code`s.
* [ ] Set `server.error.include-*` properties appropriately (no stack traces in prod).
* [ ] Align **Spring Security** handlers with your JSON shape.
* [ ] Add **trace/correlation ID** to responses and logs.
* [ ] Write MockMvc tests for representative errors.
* [ ] Configure **transaction rollback** rules where needed.
* [ ] Don’t leak internals (SQL, stack traces) in messages.

## Repositories(including ORM)

### **RDBMS Repositories in Spring Boot**

Spring Boot uses **Spring Data JPA** for interacting with relational databases. Here’s a detailed setup:

#### **Step 1: Dependencies**

In `pom.xml`:

```xml
<dependencies>
    <!-- Spring Boot Starter Data JPA -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jpa</artifactId>
    </dependency>

    <!-- H2 Database for testing (replace with MySQL/PostgreSQL in prod) -->
    <dependency>
        <groupId>com.h2database</groupId>
        <artifactId>h2</artifactId>
        <scope>runtime</scope>
    </dependency>

    <!-- Optional: Spring Boot Starter Web -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
</dependencies>
```

---

#### **Step 2: Configuration**

`application.properties` (or `application.yml`):

```properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
```

This sets up an in-memory H2 database for testing.

---

#### **Step 3: Entity Definition**

```java
import jakarta.persistence.*;

@Entity
@Table(name = "users")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true)
    private String username;

    private String email;

    // Constructors, getters, setters
    public User() {}

    public User(String username, String email) {
        this.username = username;
        this.email = email;
    }

    // Getters and setters
}
```

---

#### **Step 4: Repository Interface**

Spring Data JPA automatically provides **CRUD operations**, and you can also define **custom queries**.

```java
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import java.util.List;

public interface UserRepository extends JpaRepository<User, Long> {

    // Derived query method
    List<User> findByUsername(String username);

    // Custom query using JPQL
    @Query("SELECT u FROM User u WHERE u.email LIKE %:domain%")
    List<User> findByEmailDomain(@Param("domain") String domain);
}
```

**Default methods available** include: `save()`, `findById()`, `findAll()`, `deleteById()`, etc.

---

#### **Step 5: Service and Usage Example**

```java
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class UserService {

    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public User createUser(String username, String email) {
        return userRepository.save(new User(username, email));
    }

    public List<User> getUsersByDomain(String domain) {
        return userRepository.findByEmailDomain(domain);
    }
}
```

---

### **File Repositories with External Storage**

Spring Boot can work with **external file repositories** like **Amazon S3, Google Cloud Storage, or other file servers**. Unlike storing in the local filesystem, you interact via APIs.

Here’s an example with **Amazon S3**:

---

#### **Step 1: Dependencies**

```xml
<dependency>
    <groupId>software.amazon.awssdk</groupId>
    <artifactId>s3</artifactId>
</dependency>
```

---

#### **Step 2: Configuration**

`application.properties`:

```properties
aws.accessKeyId=YOUR_ACCESS_KEY
aws.secretAccessKey=YOUR_SECRET_KEY
aws.region=us-east-1
aws.s3.bucketName=my-bucket
```

---

#### **Step 3: File Repository Service**

```java
import org.springframework.stereotype.Repository;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.*;

import java.io.InputStream;
import java.util.List;
import java.util.stream.Collectors;

@Repository
public class FileRepository {

    private final S3Client s3Client;
    private final String bucketName = "my-bucket";

    public FileRepository(S3Client s3Client) {
        this.s3Client = s3Client;
    }

    // "Create" / "Save"
    public void save(String key, InputStream inputStream, long contentLength) {
        PutObjectRequest putObjectRequest = PutObjectRequest.builder()
                .bucket(bucketName)
                .key(key)
                .build();
        s3Client.putObject(putObjectRequest, software.amazon.awssdk.core.sync.RequestBody.fromInputStream(inputStream, contentLength));
    }

    // "Read"
    public InputStream findByKey(String key) {
        GetObjectRequest getObjectRequest = GetObjectRequest.builder()
                .bucket(bucketName)
                .key(key)
                .build();
        return s3Client.getObject(getObjectRequest);
    }

    // "Delete"
    public void deleteByKey(String key) {
        DeleteObjectRequest deleteObjectRequest = DeleteObjectRequest.builder()
                .bucket(bucketName)
                .key(key)
                .build();
        s3Client.deleteObject(deleteObjectRequest);
    }

    // List files (like "findAll")
    public List<String> findAllKeys() {
        ListObjectsV2Request listObjectsRequest = ListObjectsV2Request.builder()
                .bucket(bucketName)
                .build();
        return s3Client.listObjectsV2(listObjectsRequest)
                .contents()
                .stream()
                .map(S3Object::key)
                .collect(Collectors.toList());
    }
}
```

---

#### **Key Differences:**

| Feature   | RDBMS Repositories       | File Repositories (S3)           |
| --------- | ------------------------ | -------------------------------- |
| Data type | Structured data (tables) | Files (binary or text)           |
| Storage   | DB (SQL)                 | External storage (S3, GCS, etc.) |
| Access    | JPA repositories         | SDK/API calls                    |
| Queries   | SQL/JPQL                 | File paths and keys              |

---

### Transaction Managers

In **Spring Boot**, a **Transaction Manager** is the component responsible for managing **transactions** (begin, commit, rollback) in a consistent way across different resources like databases, JMS, JPA, etc.

Spring provides a unified abstraction:

```java
org.springframework.transaction.PlatformTransactionManager
```

All transaction managers implement this interface.

Transactions ensure the **ACID properties** (Atomicity, Consistency, Isolation, Durability).

---

#### Common Transaction Managers in Spring Boot

Depending on the persistence technology, Spring Boot auto-configures the right `PlatformTransactionManager`.

* **DataSourceTransactionManager** → for **JDBC** (plain SQL).
* **JpaTransactionManager** → for **JPA/Hibernate**.
* **HibernateTransactionManager** → for **native Hibernate** usage.
* **JtaTransactionManager** → for **distributed transactions** (across multiple DBs, JMS, etc.).
* **ReactiveTransactionManager** → for **reactive drivers** (R2DBC, MongoDB reactive).

---

#### How They’re Used

There are **two main ways** to use them in Spring Boot:

###### 1. **Declarative Transactions (Recommended)**

Use the `@Transactional` annotation.

Example with JPA:

```java
@Service
public class OrderService {

    @Autowired
    private OrderRepository orderRepository;

    @Transactional
    public void placeOrder(Order order) {
        orderRepository.save(order);
        // If any RuntimeException is thrown, transaction rolls back automatically
    }
}
```

* By default, `@Transactional` rolls back on `RuntimeException` and `Error`.
* You can configure rollback rules:

  ```java
  @Transactional(rollbackFor = Exception.class)
  ```

Spring Boot automatically wires the right `TransactionManager` (e.g., `JpaTransactionManager` if using Spring Data JPA).

---

###### 2. **Programmatic Transactions**

Use `PlatformTransactionManager` directly.

Example:

```java
@Service
public class PaymentService {

    @Autowired
    private PlatformTransactionManager transactionManager;

    public void processPayment() {
        TransactionDefinition def = new DefaultTransactionDefinition();
        TransactionStatus status = transactionManager.getTransaction(def);

        try {
            // perform DB operations
            transactionManager.commit(status);
        } catch (Exception e) {
            transactionManager.rollback(status);
            throw e;
        }
    }
}
```

This gives more control but is rarely needed — mostly used for custom transaction handling.

---

#### Example: Multiple Transaction Managers

If you have multiple datasources, you may need multiple transaction managers:

```java
@Bean
public PlatformTransactionManager primaryTxManager(
        @Qualifier("primaryDataSource") DataSource dataSource) {
    return new DataSourceTransactionManager(dataSource);
}

@Bean
public PlatformTransactionManager secondaryTxManager(
        @Qualifier("secondaryDataSource") DataSource dataSource) {
    return new DataSourceTransactionManager(dataSource);
}
```

Then in service code:

```java
@Transactional("primaryTxManager")
public void doSomethingInPrimaryDb() { ... }

@Transactional("secondaryTxManager")
public void doSomethingInSecondaryDb() { ... }
```

---

#### Key Benefits

* Consistent transaction management across JDBC, JPA, JMS, etc.
* Eliminates boilerplate commit/rollback code.
* Integrates with Spring Data repositories.
* Supports both **local transactions** and **global/distributed transactions**.

---
#### Details of Declarative Transaction(`@Transactional`)

Parameters accepted by the annotation are:

```java
@Transactional(
    propagation = Propagation.REQUIRES_NEW,
    isolation = Isolation.SERIALIZABLE,
    timeout = 30,
    readOnly = false,
    rollbackFor = {IOException.class, SQLException.class},
    noRollbackFor = IllegalArgumentException.class
)
public void performDatabaseOperation() {
    // business logic
}
```

##### Propagation Types

| Propagation            | Behavior                          | Example Use Case             |
| ---------------------- | --------------------------------- | ---------------------------- |
| **REQUIRED** (default) | Join existing, else create new    | General business logic       |
| **REQUIRES\_NEW**      | Always start new, suspend current | Logging, auditing            |
| **NESTED**             | Savepoints, rollback only inner   | Batch jobs, partial rollback |
| **SUPPORTS**           | Join if exists, else run non-tx   | Read-only queries            |
| **MANDATORY**          | Must join existing, else error    | DAO layer                    |
| **NOT\_SUPPORTED**     | Suspend transaction, run non-tx   | Long-running ops             |
| **NEVER**              | Must run non-tx, else error       | Health checks                |

##### Isolation Types

| **Isolation Type**     | **Behavior**                                                                                                                                         | **Example Use Case**                                                                             |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **`DEFAULT`**          | Uses the **default isolation** of the underlying database (varies by DBMS, e.g., most use `READ_COMMITTED`).                                         | When you don’t need to enforce a stricter level and are okay with DB defaults.                   |
| **`READ_UNCOMMITTED`** | Allows **dirty reads** (reading uncommitted changes from other transactions), non-repeatable reads, phantom reads. Fastest but least safe.           | Rarely used. Possible in reporting queries where stale/dirty data is acceptable.                 |
| **`READ_COMMITTED`**   | Prevents **dirty reads**. Still allows **non-repeatable reads** (a row may change between reads) and **phantom reads** (new rows may appear).        | Most common default (e.g., Oracle, SQL Server). Suitable for general OLTP systems.               |
| **`REPEATABLE_READ`**  | Prevents **dirty reads** and **non-repeatable reads**. Still allows **phantom reads** (new rows may appear when scanning ranges).                    | When you need stable row-level reads but can tolerate phantom rows (e.g., MySQL InnoDB default). |
| **`SERIALIZABLE`**     | Strictest level. Prevents **dirty reads, non-repeatable reads, and phantom reads**. Transactions execute as if sequential (serial order). Very slow. | Financial systems, critical operations where correctness > performance.                          |

## Misc

Sample project setup using Maven:
```
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">

    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>hello-spring</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.3.1</version> <!-- use latest -->
    </parent>

    <dependencies>
        <!-- Web starter -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <!-- For unit tests -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
```

