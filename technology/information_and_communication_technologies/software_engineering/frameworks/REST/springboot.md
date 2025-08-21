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

Spring Core provides Inversion of Control and Dependency Injection via annotations. These are majorly done via annotations. Some of the important annotations are listed here:

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

## ORM



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

