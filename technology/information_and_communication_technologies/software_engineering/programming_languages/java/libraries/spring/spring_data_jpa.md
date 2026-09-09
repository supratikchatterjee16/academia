# Spring JPA / Spring Data JPA

> **Scope:** A structured reference for Jakarta Persistence (JPA), Spring Data JPA, Spring transactions, and commonly encountered Hibernate extensions.
>
> **Modern package note:** Modern Spring Boot applications use `jakarta.persistence.*`. Older applications may use `javax.persistence.*`.

---

## Menu

* [1. JPA, Spring Data JPA, and Hibernate](#1-jpa-spring-data-jpa-and-hibernate)
* [2. Entity Mapping](#2-entity-mapping)

  * [`@Entity`](#entity)
  * [`@Table`](#table)
  * [`@Column`](#column)
  * [`@Basic`](#basic)
  * [`@Transient`](#transient)
  * [`@Lob`](#lob)
* [3. Primary Keys](#3-primary-keys)

  * [`@Id`](#id)
  * [`@GeneratedValue`](#generatedvalue)
  * [`@SequenceGenerator`](#sequencegenerator)
  * [`@TableGenerator`](#tablegenerator)
* [4. Relationships](#4-relationships)

  * [`@OneToOne`](#onetoone)
  * [`@ManyToOne`](#manytoone)
  * [`@OneToMany`](#onetomany)
  * [`@ManyToMany`](#manytomany)
  * [`@JoinColumn`](#joincolumn)
  * [`@JoinColumns`](#joincolumns)
  * [`@JoinTable`](#jointable)
  * [Owning vs Inverse Side](#owning-vs-inverse-side)
  * [`cascade`](#cascade)
  * [`fetch`](#fetch)
  * [`orphanRemoval`](#orphanremoval)
* [5. Value Objects / Embedded Types](#5-value-objects--embedded-types)

  * [`@Embeddable`](#embeddable)
  * [`@Embedded`](#embedded)
  * [`@AttributeOverride`](#attributeoverride)
  * [`@AssociationOverride`](#associationoverride)
* [6. Enums and Custom Types](#6-enums-and-custom-types)

  * [`@Enumerated`](#enumerated)
  * [`@Converter`](#converter)
  * [`@Convert`](#convert)
  * [`AttributeConverter`](#attributeconverter)
* [7. Inheritance and Discriminators](#7-inheritance-and-discriminators)

  * [`@Inheritance`](#inheritance)
  * `SINGLE_TABLE`
  * [`@DiscriminatorColumn`](#discriminatorcolumn)
  * [`@DiscriminatorValue`](#discriminatorvalue)
  * `JOINED`
  * `TABLE_PER_CLASS`
  * [`@MappedSuperclass`](#mappedsuperclass)
* [8. Concurrency and Locking](#8-concurrency-and-locking)

  * [`@Version`](#version)
  * [`@Lock`](#lock)
* [9. Transactions](#9-transactions)

  * [`@Transactional`](#transactional)
  * [Propagation](#propagation)
  * [Isolation](#isolation)
  * [Rollback Rules](#rollback-rules)
  * [Transaction Boundaries](#transaction-boundaries)
* [10. Spring Data JPA Repositories](#10-spring-data-jpa-repositories)

  * [`JpaRepository`](#jparepository)
  * [Derived Queries](#derived-queries)
  * [`@Query`](#query)
  * [`@Modifying`](#modifying)
  * [`@EntityGraph`](#entitygraph)
  * [`@Procedure`](#procedure)
* [11. Querying](#11-querying)

  * [JPQL](#jpql)
  * [Native SQL](#native-sql)
  * [Specifications](#specifications)
  * [Criteria API](#criteria-api)
  * [Projections](#projections)
* [12. Fetching and Performance](#12-fetching-and-performance)

  * [LAZY vs EAGER](#lazy-vs-eager)
  * [N+1 Query Problem](#n1-query-problem)
  * [Fetch Joins](#fetch-joins)
  * [Entity Graphs](#entity-graphs)
  * [Batch Fetching](#batch-fetching)
* [13. Entity Lifecycle and Callbacks](#13-entity-lifecycle-and-callbacks)

  * [`@PrePersist`](#prepersist)
  * [`@PostPersist`](#postpersist)
  * [`@PreUpdate`](#preupdate)
  * [`@PostUpdate`](#postupdate)
  * [`@PreRemove`](#preremove)
  * [`@PostRemove`](#postremove)
* [14. Spring Data JPA Auditing](#14-spring-data-jpa-auditing)

  * [`@CreatedDate`](#createddate)
  * [`@LastModifiedDate`](#lastmodifieddate)
  * [`@CreatedBy`](#createdby)
  * [`@LastModifiedBy`](#lastmodifiedby)
* [15. Common Hibernate Extensions](#15-common-hibernate-extensions)
* [16. Quick Annotation Map](#16-quick-annotation-map)
* [17. Recommended Learning Order](#17-recommended-learning-order)

---

# 1. JPA, Spring Data JPA, and Hibernate

One of the most important things to understand is that **JPA, Hibernate, Spring Data JPA, and Spring Framework are different layers**.

```text
Your Application
       |
       v
Spring Data JPA
       |
       v
Jakarta Persistence (JPA)
       |
       v
Hibernate
       |
       v
JDBC
       |
       v
Database
```

## Jakarta Persistence / JPA

JPA is the standard persistence API/specification.

Modern applications use:

```java
import jakarta.persistence.*;
```

It defines annotations such as:

```text
@Entity
@Id
@OneToMany
@ManyToOne
@OneToOne
@ManyToMany
@Enumerated
@Convert
@Inheritance
@Version
```

JPA defines **what persistence behavior means**, but it does not itself execute SQL.

---

## Hibernate

Hibernate is a **JPA provider / implementation**.

It performs the actual ORM work:

```text
Java Object
     |
     v
Hibernate
     |
     v
SQL
     |
     v
Database
```

Hibernate also provides features beyond standard JPA.

For example:

```text
@BatchSize
@Formula
@CreationTimestamp
@UpdateTimestamp
@JdbcTypeCode
```

These are Hibernate-specific.

---

## Spring Data JPA

Spring Data JPA builds a repository abstraction on top of JPA.

For example:

```java
public interface UserRepository
        extends JpaRepository<User, Long> {
}
```

Instead of implementing standard CRUD operations yourself, Spring Data generates the repository implementation.

It also provides:

```text
Derived queries
@Query
@Modifying
@EntityGraph
Specifications
Projections
```

---

## Spring Framework

Spring Framework provides application infrastructure around the persistence layer.

For example:

```java
@Transactional
```

comes from Spring Framework:

```java
org.springframework.transaction.annotation.Transactional
```

not from JPA.

---

# 2. Entity Mapping

Entity mapping describes how Java classes and attributes correspond to persistent database structures.

---

## `@Entity`

Marks a Java class as a persistent entity.

```java
@Entity
public class Employee {

    @Id
    private Long id;

    private String name;
}
```

The entity has persistent identity, normally represented by its primary key.

Typical requirements include:

* A primary key.
* A no-argument constructor with at least `protected` visibility.
* A class that can be proxied/enhanced by the provider in normal Hibernate usage.
* Persistent fields/properties accessible according to the chosen access strategy.

---

## `@Table`

Controls the table mapping.

```java
@Entity
@Table(
    name = "employees",
    schema = "hr"
)
public class Employee {
}
```

### Important attributes

| Attribute           | Purpose                        |
| ------------------- | ------------------------------ |
| `name`              | Table name                     |
| `schema`            | Database schema                |
| `catalog`           | Database catalog               |
| `uniqueConstraints` | Table-level unique constraints |
| `indexes`           | Index definitions              |

Example:

```java
@Table(
    name = "employees",
    uniqueConstraints = {
        @UniqueConstraint(
            name = "uk_employee_email",
            columnNames = "email"
        )
    }
)
```

---

## `@Column`

Controls how an attribute maps to a column.

```java
@Column(
    name = "first_name",
    nullable = false,
    length = 100,
    unique = true
)
private String firstName;
```

### Important attributes

| Attribute          | Purpose                                         |
| ------------------ | ----------------------------------------------- |
| `name`             | Column name                                     |
| `nullable`         | Whether the column permits NULL                 |
| `unique`           | Requests a unique constraint                    |
| `length`           | String length                                   |
| `precision`        | Decimal precision                               |
| `scale`            | Decimal scale                                   |
| `insertable`       | Whether included in generated INSERT statements |
| `updatable`        | Whether included in generated UPDATE statements |
| `columnDefinition` | Explicit SQL definition                         |
| `table`            | Secondary table                                 |

A useful pattern:

```java
@Column(
    name = "created_at",
    insertable = false,
    updatable = false
)
private Instant createdAt;
```

This makes the attribute effectively read-only from the JPA-generated INSERT/UPDATE perspective.

---

## `@Basic`

Represents a basic persistent attribute.

```java
@Basic(
    optional = false,
    fetch = FetchType.LAZY
)
private String name;
```

In ordinary cases, it can be omitted:

```java
private String name;
```

### Attributes

```text
optional
fetch
```

`fetch` can be:

```text
FetchType.EAGER
FetchType.LAZY
```

> `@Basic(fetch = LAZY)` has provider-dependent behavior for some basic attribute types. Do not assume that every basic field will behave like a lazy association.

---

## `@Transient`

Marks a field/property as non-persistent.

```java
@Transient
private String fullName;
```

The field exists in Java but isn't mapped to a database column.

### Important distinction

These are different:

```java
jakarta.persistence.Transient
```

and:

```java
transient
```

The first is a JPA mapping annotation. The second is a Java language keyword related to Java serialization.

---

## `@Lob`

Used for large object data.

```java
@Lob
private String document;

@Lob
private byte[] image;
```

Typical database representations include:

```text
String / character data -> CLOB-like type
byte[] / binary data    -> BLOB-like type
```

Exact SQL types depend on the database and provider.

---

# 3. Primary Keys

---

## `@Id`

Marks the primary-key attribute.

```java
@Id
private Long id;
```

---

## `@GeneratedValue`

Specifies how the primary key is generated.

```java
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Long id;
```

### Strategies

```text
AUTO
IDENTITY
SEQUENCE
TABLE
```

### `IDENTITY`

The database generates the ID during insertion.

```text
INSERT
   |
   v
Database
   |
   v
Generated ID
```

Common with databases that provide identity/auto-increment columns.

---

### `SEQUENCE`

Uses a database sequence.

```text
Database Sequence
       |
       v
Next ID
       |
       v
Entity
```

Common with PostgreSQL, Oracle, etc.

---

### `TABLE`

Uses a database table to maintain generated ID values.

Less common in modern applications.

---

### `AUTO`

Allows the persistence provider to select the strategy.

---

## `@SequenceGenerator`

Defines a sequence generator.

```java
@Id
@GeneratedValue(
    strategy = GenerationType.SEQUENCE,
    generator = "employee_seq"
)
@SequenceGenerator(
    name = "employee_seq",
    sequenceName = "employee_sequence",
    allocationSize = 50
)
private Long id;
```

### Important attributes

| Attribute        | Purpose                 |
| ---------------- | ----------------------- |
| `name`           | Generator name          |
| `sequenceName`   | Database sequence name  |
| `initialValue`   | Initial value           |
| `allocationSize` | IDs allocated per block |

### `allocationSize`

This can improve performance by allowing the provider to reserve ID ranges.

However, it also means generated IDs may have gaps.

> **Do not use database-generated primary keys as gap-free business sequence numbers.**

---

## `@TableGenerator`

Defines a table-based generator.

```java
@TableGenerator(
    name = "employee_generator",
    table = "id_generator",
    pkColumnName = "entity",
    valueColumnName = "next_id"
)
```

This is less common than `SEQUENCE` or `IDENTITY`.

---

# 4. Relationships

The four fundamental relationship annotations are:

```text
@OneToOne
@OneToMany
@ManyToOne
@ManyToMany
```

Understanding these properly requires understanding:

```text
Owning side
Inverse side
mappedBy
Foreign key
Join table
Cascade
Fetch
Orphan removal
```

---

## `@OneToOne`

One entity is associated with one other entity.

```text
Employee 1 -------- 1 Passport
```

Example:

```java
@Entity
public class Employee {

    @OneToOne
    @JoinColumn(name = "passport_id")
    private Passport passport;
}
```

### Attributes

```java
@OneToOne(
    targetEntity = Passport.class,
    cascade = CascadeType.ALL,
    fetch = FetchType.LAZY,
    optional = false,
    mappedBy = "...",
    orphanRemoval = true
)
```

| Attribute       | Purpose                           |
| --------------- | --------------------------------- |
| `targetEntity`  | Target entity type                |
| `cascade`       | Propagated entity operations      |
| `fetch`         | Loading strategy                  |
| `optional`      | Whether association may be absent |
| `mappedBy`      | Inverse-side mapping              |
| `orphanRemoval` | Delete orphaned child             |

Usually `targetEntity` can be omitted because Java's type provides it:

```java
@OneToOne
private Passport passport;
```

---

## `@ManyToOne`

Many entities refer to one entity.

```text
Employee * -------- 1 Department
```

```java
@ManyToOne(fetch = FetchType.LAZY)
@JoinColumn(name = "department_id")
private Department department;
```

Common attributes:

```text
targetEntity
cascade
fetch
optional
```

The foreign-key relationship is normally represented on this side.

---

## `@OneToMany`

One entity has many related entities.

```text
Department 1 -------- * Employee
```

```java
@OneToMany(
    mappedBy = "department",
    cascade = CascadeType.ALL,
    orphanRemoval = true
)
private List<Employee> employees;
```

Common attributes:

```text
targetEntity
cascade
fetch
mappedBy
orphanRemoval
```

---

## `@ManyToMany`

Many entities can relate to many entities.

```text
Student * -------- * Course
```

Usually represented through a join table.

```java
@ManyToMany
@JoinTable(
    name = "student_course",
    joinColumns = @JoinColumn(name = "student_id"),
    inverseJoinColumns = @JoinColumn(name = "course_id")
)
private Set<Course> courses;
```

Common attributes:

```text
targetEntity
cascade
fetch
mappedBy
```

---

## `@JoinColumn`

Specifies the foreign-key column.

```java
@ManyToOne
@JoinColumn(
    name = "department_id",
    referencedColumnName = "id",
    nullable = false
)
private Department department;
```

### Important attributes

| Attribute              | Purpose              |
| ---------------------- | -------------------- |
| `name`                 | FK column            |
| `referencedColumnName` | Target column        |
| `nullable`             | NULL allowed?        |
| `unique`               | Unique constraint    |
| `insertable`           | Included in INSERT   |
| `updatable`            | Included in UPDATE   |
| `table`                | Secondary table      |
| `foreignKey`           | Foreign-key metadata |

---

## `@JoinColumns`

Used when multiple columns participate in a relationship.

```java
@JoinColumns({
    @JoinColumn(
        name = "country_code",
        referencedColumnName = "country_code"
    ),
    @JoinColumn(
        name = "account_number",
        referencedColumnName = "account_number"
    )
})
```

This is particularly relevant with composite keys.

---

## `@JoinTable`

Defines an intermediate table.

```java
@ManyToMany
@JoinTable(
    name = "student_course",
    joinColumns = @JoinColumn(name = "student_id"),
    inverseJoinColumns = @JoinColumn(name = "course_id")
)
private Set<Course> courses;
```

Database:

```text
student
   |
   | student_id
   v
student_course
   |
   | course_id
   v
course
```

---

## Owning vs Inverse Side

This is one of the **most important concepts in JPA**.

Consider:

```java
@Entity
public class Employee {

    @ManyToOne
    @JoinColumn(name = "department_id")
    private Department department;
}
```

and:

```java
@Entity
public class Department {

    @OneToMany(mappedBy = "department")
    private List<Employee> employees;
}
```

The owning side is:

```text
Employee.department
```

The inverse side is:

```text
Department.employees
```

### Why?

Because:

```java
@JoinColumn(name = "department_id")
```

is on the `Employee` side.

The inverse side says:

```java
mappedBy = "department"
```

---

## What does `mappedBy` mean?

```java
@OneToMany(mappedBy = "department")
```

means:

> "This relationship is mapped by the `department` attribute on Employee."

It refers to a **Java attribute**, not the database column.

Incorrect mental model:

```text
mappedBy = database column
```

Correct:

```text
mappedBy = Java relationship attribute
```

---

## Cascade

Cascade controls which JPA entity lifecycle operations propagate to related entities.

```java
@OneToMany(cascade = CascadeType.ALL)
private List<OrderLine> lines;
```

### Cascade types

```text
PERSIST
MERGE
REMOVE
REFRESH
DETACH
ALL
```

For example:

```java
cascade = CascadeType.PERSIST
```

means:

```text
persist(Order)
       |
       +---- persist(OrderLine)
```

### `CascadeType.ALL`

Equivalent to:

```text
PERSIST
MERGE
REMOVE
REFRESH
DETACH
```

### Important distinction

```text
JPA Cascade
     !=
Database ON DELETE CASCADE
```

JPA cascade is about entity operations through the persistence context.

---

## Fetch

The standard fetch types are:

```text
FetchType.LAZY
FetchType.EAGER
```

### LAZY

The association is intended to be loaded when needed.

```java
@ManyToOne(fetch = FetchType.LAZY)
private Department department;
```

### EAGER

The association is intended to be available eagerly.

```java
@ManyToOne(fetch = FetchType.EAGER)
private Department department;
```

### Practical recommendation

Do not use EAGER simply because a relationship is frequently needed.

Instead, make fetching explicit through:

```text
Fetch join
EntityGraph
Projection
Specific query
```

This gives you more control over SQL and performance.

---

## `orphanRemoval`

Example:

```java
@OneToMany(
    mappedBy = "order",
    orphanRemoval = true
)
private List<OrderLine> lines;
```

If the child is removed from the parent's collection:

```java
order.getLines().remove(line);
```

JPA can remove that child entity from the database.

Potential SQL:

```sql
DELETE FROM order_line
WHERE id = ?
```

### Difference from cascade remove

Think of:

```text
Cascade REMOVE
```

as:

> "When the parent is removed, remove the related entity."

Whereas:

```text
orphanRemoval = true
```

is about:

> "When a privately owned child is removed from the relationship, remove that child."

Use it where the child has a strong lifecycle dependency on the parent.

---

# 5. Value Objects / Embedded Types

---

## `@Embeddable`

Defines a reusable value type.

```java
@Embeddable
public class Address {

    private String street;
    private String city;
    private String zipCode;
}
```

---

## `@Embedded`

Embeds the value into an entity.

```java
@Entity
public class Employee {

    @Embedded
    private Address address;
}
```

The fields can be stored directly in the employee table:

```text
employee
------------------
id
street
city
zip_code
```

There is no required `address` table.

### Mental model

```text
@Entity
    = entity with identity

@Embeddable
    = value object embedded into another entity
```

---

## `@AttributeOverride`

Changes the mapping of an embedded attribute.

```java
@Embedded
@AttributeOverrides({
    @AttributeOverride(
        name = "city",
        column = @Column(name = "home_city")
    )
})
private Address homeAddress;
```

---

## `@AssociationOverride`

Used when an embeddable contains an association and the containing entity needs to override that association's mapping.

---

# 6. Enums and Custom Types

---

## `@Enumerated`

Maps Java enums to database values.

```java
public enum Status {
    ACTIVE,
    INACTIVE,
    BLOCKED
}
```

Recommended:

```java
@Enumerated(EnumType.STRING)
private Status status;
```

### `EnumType.STRING`

Database:

```text
ACTIVE
INACTIVE
BLOCKED
```

### `EnumType.ORDINAL`

Database:

```text
0
1
2
```

### Why STRING is generally preferable

Suppose:

```java
enum Status {
    ACTIVE,
    INACTIVE,
    BLOCKED
}
```

With ordinal:

```text
ACTIVE   = 0
INACTIVE = 1
BLOCKED  = 2
```

If you later change it:

```java
enum Status {
    ACTIVE,
    PENDING,
    INACTIVE,
    BLOCKED
}
```

then:

```text
ACTIVE   = 0
PENDING  = 1
INACTIVE = 2
BLOCKED  = 3
```

Old database value:

```text
1
```

used to mean:

```text
INACTIVE
```

but now means:

```text
PENDING
```

Therefore:

```java
@Enumerated(EnumType.STRING)
```

is usually safer for persisted business enums.

---

## `@Converter`

Registers a custom JPA attribute converter.

Example:

```java
@Converter
public class StatusConverter
        implements AttributeConverter<Status, String> {

    @Override
    public String convertToDatabaseColumn(Status status) {
        if (status == null) {
            return null;
        }

        return status == Status.ACTIVE
                ? "A"
                : "I";
    }

    @Override
    public Status convertToEntityAttribute(String value) {
        if (value == null) {
            return null;
        }

        return "A".equals(value)
                ? Status.ACTIVE
                : Status.INACTIVE;
    }
}
```

---

## `@Convert`

Applies a converter to an attribute.

```java
@Convert(converter = StatusConverter.class)
private Status status;
```

Conceptually:

```text
Java                        Database

Status.ACTIVE   --------->  "A"
Status.INACTIVE --------->  "I"

Status.ACTIVE   <---------  "A"
Status.INACTIVE <---------  "I"
```

---

## `AttributeConverter`

The interface is:

```java
AttributeConverter<X, Y>
```

where:

```text
X = Java/entity attribute type
Y = database representation
```

Methods:

```java
Y convertToDatabaseColumn(X attribute);

X convertToEntityAttribute(Y dbData);
```

This is useful when the Java representation and database representation differ.

Examples:

```text
Java enum       <-> VARCHAR code
Money object    <-> DECIMAL
Custom ID       <-> VARCHAR
Boolean         <-> Y/N
Encrypted value <-> database string
```

---

## `@Converter(autoApply = true)`

```java
@Converter(autoApply = true)
public class StatusConverter
        implements AttributeConverter<Status, String> {
}
```

This allows the converter to be automatically applied to compatible attributes.

Use it when the conversion should consistently apply to that Java type.

---

## `@Convert(disableConversion = true)`

Can explicitly disable an otherwise applicable converter for a particular mapping.

Useful when an auto-applied converter should not apply to one attribute.

---

# 7. Inheritance and Discriminators

JPA supports inheritance between entity classes.

Example:

```text
Payment
   |
   +---- CreditCardPayment
   |
   +---- UpiPayment
```

The main annotations are:

```text
@Inheritance
@DiscriminatorColumn
@DiscriminatorValue
@MappedSuperclass
```

---

## `@Inheritance`

Defines the database inheritance strategy.

```java
@Inheritance(strategy = InheritanceType.SINGLE_TABLE)
```

Three standard strategies exist:

```text
SINGLE_TABLE
JOINED
TABLE_PER_CLASS
```

---

## `SINGLE_TABLE`

All classes use one table.

```java
@Entity
@Inheritance(strategy = InheritanceType.SINGLE_TABLE)
@DiscriminatorColumn(name = "payment_type")
public class Payment {
}
```

Subclass:

```java
@Entity
@DiscriminatorValue("CARD")
public class CreditCardPayment extends Payment {
}
```

Another:

```java
@Entity
@DiscriminatorValue("UPI")
public class UpiPayment extends Payment {
}
```

Database:

```text
payment
--------------------------------------------------
id | payment_type | card_number | upi_id
--------------------------------------------------
1  | CARD         | 1234        | NULL
2  | UPI          | NULL        | abc@upi
```

When Hibernate reads:

```text
payment_type = CARD
```

it knows the row represents:

```text
CreditCardPayment
```

When it reads:

```text
payment_type = UPI
```

it knows:

```text
UpiPayment
```

This is **discriminator-based polymorphic loading**.

---

## `@DiscriminatorColumn`

Defines the discriminator column.

```java
@DiscriminatorColumn(
    name = "payment_type",
    discriminatorType = DiscriminatorType.STRING,
    length = 20
)
```

### Important attributes

| Attribute           | Purpose                        |
| ------------------- | ------------------------------ |
| `name`              | Discriminator column           |
| `discriminatorType` | `STRING`, `CHAR`, or `INTEGER` |
| `columnDefinition`  | SQL definition                 |
| `length`            | String length                  |

---

## `@DiscriminatorValue`

Defines the value identifying an entity class.

```java
@Entity
@DiscriminatorValue("CARD")
public class CreditCardPayment extends Payment {
}
```

Mapping:

```text
CARD -> CreditCardPayment
UPI  -> UpiPayment
```

---

## `JOINED`

Parent and child classes have separate tables.

```text
payment
-----------------
id
common fields


credit_card_payment
-------------------
id
card_number


upi_payment
----------------
id
upi_id
```

The subclass table joins to the parent table using the primary key.

### Advantages

* Normalized structure.
* Avoids many nullable subclass-specific columns.

### Trade-offs

* More joins.
* Polymorphic queries can be more expensive.

---

## `TABLE_PER_CLASS`

Each concrete class has its own table.

```text
credit_card_payment
-------------------
id
common fields
card_number


upi_payment
----------------
id
common fields
upi_id
```

Common fields are repeated.

Polymorphic queries can require unions or equivalent provider-generated SQL.

---

## `@MappedSuperclass`

A `@MappedSuperclass` provides persistent fields to subclasses but is not itself an entity/table.

```java
@MappedSuperclass
public abstract class BaseEntity {

    @Id
    private Long id;

    private Instant createdAt;
}
```

Then:

```java
@Entity
public class Employee extends BaseEntity {
}
```

```java
@Entity
public class Department extends BaseEntity {
}
```

Conceptually:

```text
BaseEntity
   |
   +-- id
   +-- createdAt
        |
        +---- Employee table
        |
        +---- Department table
```

There is no `BaseEntity` table.

### Important distinction

```text
@MappedSuperclass
    = reuse mappings

@Inheritance
    = entity inheritance / polymorphism
```

---

# 8. Concurrency and Locking

---

## `@Version`

Enables optimistic locking.

```java
@Version
private Long version;
```

Suppose two transactions read the same entity:

```text
Transaction A -> version 5
Transaction B -> version 5
```

A updates it:

```text
5 -> 6
```

B then attempts an update based on version 5.

Conceptually:

```sql
UPDATE account
SET balance = ?,
    version = 6
WHERE id = ?
  AND version = 5;
```

If the update affects zero rows, the provider detects the optimistic locking conflict.

### Why?

To prevent:

```text
Transaction A changes data
       +
Transaction B silently overwrites A
```

This is the **lost update** problem.

---

## `@Lock`

Spring Data JPA provides:

```java
@Lock(LockModeType.PESSIMISTIC_WRITE)
Optional<Account> findById(Long id);
```

This allows repository methods to request a JPA lock mode.

### Two broad strategies

```text
Optimistic locking
       |
       +-- @Version

Pessimistic locking
       |
       +-- @Lock
```

---

# 9. Transactions

## `@Transactional`

`@Transactional` is primarily a **Spring Framework** annotation.

Typical import:

```java
import org.springframework.transaction.annotation.Transactional;
```

Example:

```java
@Service
public class TransferService {

    @Transactional
    public void transfer(
            Long source,
            Long destination,
            BigDecimal amount) {

        debit(source, amount);
        credit(destination, amount);
    }
}
```

Conceptually:

```text
BEGIN
   |
   +-- debit()
   |
   +-- credit()
   |
COMMIT
```

If rollback conditions occur:

```text
BEGIN
   |
   +-- debit()
   |
   +-- credit()
   |
   X exception
   |
ROLLBACK
```

---

## Important `@Transactional` attributes

```java
@Transactional(
    propagation = Propagation.REQUIRED,
    isolation = Isolation.DEFAULT,
    timeout = 30,
    readOnly = false,
    rollbackFor = Exception.class,
    noRollbackFor = SomeException.class
)
```

---

## Propagation

Controls how the method participates in an existing transaction.

Important values:

```text
REQUIRED
REQUIRES_NEW
SUPPORTS
MANDATORY
NOT_SUPPORTED
NEVER
NESTED
```

---

## `REQUIRED`

Default propagation in Spring.

```text
Existing transaction?
       |
   +---+---+
   |       |
  yes      no
   |       |
 join    create
```

If a transaction already exists:

```text
join existing transaction
```

Otherwise:

```text
create new transaction
```

---

## `REQUIRES_NEW`

Suspends the existing transaction and starts a new one.

```text
Transaction A
     |
   suspend
     |
Transaction B
     |
   complete
     |
resume A
```

Useful when an operation needs its own independent transaction.

Example use case:

```text
Business transaction
        |
        +---- audit operation in independent transaction
```

Be careful: `REQUIRES_NEW` can require another database connection and therefore has connection-pool implications.

---

## `SUPPORTS`

```text
Existing transaction?
   |
  yes -> use it
   |
  no  -> execute without transaction
```

---

## `MANDATORY`

Requires an existing transaction.

If none exists, the call fails.

---

## `NOT_SUPPORTED`

Suspends an existing transaction and runs without one.

---

## `NEVER`

Fails if a transaction already exists.

---

## `NESTED`

Creates a nested transaction-like scope using savepoints where supported by the transaction manager/resource.

Do not confuse it with `REQUIRES_NEW`:

```text
REQUIRES_NEW
    = independent transaction

NESTED
    = nested/savepoint-based behavior
```

---

## Isolation

Controls how transactions observe concurrent changes.

Common levels:

```text
DEFAULT
READ_UNCOMMITTED
READ_COMMITTED
REPEATABLE_READ
SERIALIZABLE
```

Actual behavior depends on the database and transaction manager.

Typical anomalies discussed with isolation are:

```text
Dirty read
Non-repeatable read
Phantom read
Lost update
```

---

## `readOnly`

```java
@Transactional(readOnly = true)
```

Expresses that the transaction is intended for reads.

It can enable optimizations in Spring/provider integrations.

However:

> `readOnly = true` should not be treated as a universal guarantee that a write is impossible.

---

## `timeout`

```java
@Transactional(timeout = 30)
```

Specifies the transaction timeout in seconds.

---

## Rollback Rules

For example:

```java
@Transactional(
    rollbackFor = IOException.class
)
```

can configure rollback for an exception type.

You can also specify:

```java
noRollbackFor = SomeException.class
```

to prevent rollback for particular exception types.

### Default rule

Spring's default rollback behavior is primarily based on unchecked exceptions and errors. Checked exceptions generally require explicit rollback configuration when rollback is desired.

---

## Transaction Boundaries

A common architecture is:

```text
Controller
    |
    v
Service       <-- transaction boundary
    |
    v
Repository
    |
    v
Database
```

Example:

```java
@Service
public class OrderService {

    @Transactional
    public void createOrder(...) {
        ...
    }
}
```

The service method represents the **unit of work**.

---

# 10. Spring Data JPA Repositories

---

## `JpaRepository`

Example:

```java
public interface UserRepository
        extends JpaRepository<User, Long> {
}
```

Provides common repository operations such as:

```text
save()
findById()
findAll()
existsById()
deleteById()
count()
```

The exact inherited API depends on the Spring Data version.

---

## Derived Queries

Spring Data can derive queries from method names.

```java
List<User> findByLastName(String lastName);
```

```java
Optional<User> findByEmail(String email);
```

```java
List<Order> findByStatusAndCreatedAtAfter(
    Status status,
    Instant timestamp
);
```

Spring Data parses the method name and creates the appropriate query.

Examples of common keywords:

```text
And
Or
Between
LessThan
GreaterThan
Like
Containing
StartingWith
EndingWith
In
IsNull
IsNotNull
True
False
OrderBy
```

---

## `@Query`

Defines an explicit query.

```java
@Query("""
    SELECT u
    FROM User u
    WHERE u.email = :email
""")
Optional<User> findByEmail(
    @Param("email") String email
);
```

This is JPQL.

---

## Native SQL with `@Query`

```java
@Query(
    value = """
        SELECT *
        FROM users
        WHERE email = :email
    """,
    nativeQuery = true
)
Optional<User> findByEmail(String email);
```

Use native SQL when you genuinely need database-specific SQL or capabilities.

---

## `@Modifying`

Used for update/delete queries.

```java
@Modifying
@Query("""
    UPDATE User u
    SET u.active = false
    WHERE u.lastLogin < :date
""")
int deactivateUsers(Instant date);
```

Usually used within a transaction:

```java
@Modifying
@Transactional
```

### Important caveat

Bulk JPQL updates/deletes operate directly against the database.

Entities already loaded in the persistence context may therefore contain stale state.

Spring Data provides options such as:

```java
@Modifying(clearAutomatically = true)
```

when clearing the persistence context after a modifying query is appropriate.

---

## `@EntityGraph`

Controls fetching of relationships for a repository operation.

```java
@EntityGraph(attributePaths = {"orders"})
Optional<Customer> findById(Long id);
```

Useful for avoiding unnecessary lazy-loading queries and addressing N+1 situations.

---

## `@Procedure`

Maps a repository method to a database stored procedure.

Use this when the application intentionally relies on stored procedures.

---

# 11. Querying

---

## JPQL

JPQL operates on the **entity model**.

```java
@Query("""
    SELECT e
    FROM Employee e
    WHERE e.department.name = :department
""")
List<Employee> findEmployees(String department);
```

Notice:

```text
Employee
e.department.name
```

rather than:

```text
employee_table
department_table
```

JPQL is entity-oriented.

---

## Native SQL

Native queries use actual database SQL.

```java
@Query(
    value = """
        SELECT *
        FROM employees
        WHERE department_id = :departmentId
    """,
    nativeQuery = true
)
List<Employee> findEmployees(Long departmentId);
```

### Advantages

* Database-specific features.
* Full SQL control.
* Useful for existing SQL.
* Useful for advanced database functionality.

### Trade-offs

* Less database portability.
* More coupling to the database schema/vendor.

---

## Specifications

Spring Data JPA Specifications provide composable dynamic predicates.

Conceptually:

```text
Specification A
       AND
Specification B
       AND
Specification C
```

Repository:

```java
public interface EmployeeRepository
        extends JpaRepository<Employee, Long>,
                JpaSpecificationExecutor<Employee> {
}
```

Useful for search screens with many optional filters.

---

## Criteria API

The JPA Criteria API constructs queries programmatically.

Conceptually:

```text
CriteriaBuilder
      |
      v
CriteriaQuery
      |
      v
Predicates
      |
      v
Typed query
```

It is powerful for dynamic queries but verbose.

---

## Projections

Projections retrieve only the data required.

### Interface projection

```java
public interface UserSummary {

    String getName();

    String getEmail();
}
```

Repository:

```java
List<UserSummary> findByActiveTrue();
```

This can be preferable to loading complete entities when only a subset of data is required.

### DTO projection

JPQL can construct DTOs:

```java
@Query("""
    SELECT new com.example.UserSummaryDto(
        u.name,
        u.email
    )
    FROM User u
""")
List<UserSummaryDto> findSummaries();
```

---

# 12. Fetching and Performance

---

## LAZY vs EAGER

Associations have fetch semantics.

```java
@ManyToOne(fetch = FetchType.LAZY)
private Department department;
```

and:

```java
@OneToMany(fetch = FetchType.LAZY)
private List<Employee> employees;
```

### LAZY

Load the relationship when it is accessed, subject to provider behavior.

### EAGER

The relationship is intended to be loaded eagerly.

### Practical rule

Prefer deliberate fetching.

Instead of:

```textEAGER everything
```

use:

```textSpecific query
     |
     +-- fetch join
     +-- EntityGraph
     +-- projection
```

This makes SQL behavior more predictable.

---

## N+1 Query Problem

Suppose:

```java
List<Order> orders = orderRepository.findAll();
```

Then:

```java
for (Order order : orders) {
    order.getCustomer().getName();
}
```

Potential SQL:

```text
Query 1:
SELECT * FROM orders;

Query 2:
SELECT * FROM customer WHERE id = ?;

Query 3:
SELECT * FROM customer WHERE id = ?;

Query 4:
SELECT * FROM customer WHERE id = ?;

...
```

Total:

```text
1 + N queries
```

This is the **N+1 query problem**.

---

## Fetch Joins

JPQL can fetch relationships as part of the query.

```java
@Query("""
    SELECT o
    FROM Order o
    JOIN FETCH o.customer
""")
List<Order> findOrdersWithCustomers();
```

Conceptually:

```text
Order
  |
  +---- Customer
```

are loaded through one query.

### Caution

Collection fetch joins require care with:

* Pagination.
* Duplicate parent rows.
* Multiple collection fetches.
* Result cardinality.

---

## Entity Graphs

Alternative approach:

```java
@EntityGraph(attributePaths = {"customer"})
List<Order> findAll();
```

This separates the fetching plan from the query definition.

---

## Batch Fetching

Hibernate can batch lazy association loading.

Without batching:

```text
SELECT customer WHERE id = 1
SELECT customer WHERE id = 2
SELECT customer WHERE id = 3
```

With batching, the provider may issue something like:

```sql
SELECT *
FROM customer
WHERE id IN (1, 2, 3);
```

Hibernate provides provider-specific mechanisms such as:

```java
@BatchSize(size = 50)
```

and configuration properties for batch fetching.

---

# 13. Entity Lifecycle and Callbacks

JPA entities move through lifecycle states.

A simplified model:

```text
             persist()
 New --------------------> Managed
                              |
                              | remove()
                              v
                           Removed

Managed
   |
   | detach()
   v
Detached
```

Common callback annotations:

```text
@PrePersist
@PostPersist
@PreUpdate
@PostUpdate
@PreRemove
@PostRemove
```

---

## `@PrePersist`

Runs before persistence.

```java
@PrePersist
void beforeInsert() {
    createdAt = Instant.now();
}
```

---

## `@PostPersist`

Runs after the entity has been persisted.

---

## `@PreUpdate`

Runs before an update operation.

```java
@PreUpdate
void beforeUpdate() {
    updatedAt = Instant.now();
}
```

---

## `@PostUpdate`

Runs after an update operation.

---

## `@PreRemove`

Runs before removal.

---

## `@PostRemove`

Runs after removal.

---

## Entity Listeners

Callbacks can be moved to a separate listener class.

```java
@Entity
@EntityListeners(AuditListener.class)
public class Employee {
}
```

This is useful when lifecycle logic should be shared across multiple entities.

---

# 14. Spring Data JPA Auditing

Spring Data JPA provides auditing support.

---

## `@CreatedDate`

```java
@CreatedDate
private Instant createdAt;
```

Records creation time.

---

## `@LastModifiedDate`

```java
@LastModifiedDate
private Instant updatedAt;
```

Records modification time.

---

## `@CreatedBy`

```java
@CreatedBy
private String createdBy;
```

Records the creator.

---

## `@LastModifiedBy`

```java
@LastModifiedBy
private String modifiedBy;
```

Records the last modifying user.

---

## Example

```java
@Entity
@EntityListeners(AuditingEntityListener.class)
public class Order {

    @CreatedDate
    private Instant createdAt;

    @LastModifiedDate
    private Instant updatedAt;

    @CreatedBy
    private String createdBy;

    @LastModifiedBy
    private String modifiedBy;
}
```

Enable auditing:

```java
@Configuration
@EnableJpaAuditing
public class JpaConfig {
}
```

For:

```java
@CreatedBy
@LastModifiedBy
```

Spring Data needs an `AuditorAware<T>` implementation to determine the current auditor.

---

# 15. Common Hibernate Extensions

Hibernate is a common JPA provider used with Spring Boot.

The following are **Hibernate-specific**, not portable JPA annotations:

```text
@BatchSize
@Fetch
@JdbcTypeCode
@SQLRestriction
@CreationTimestamp
@UpdateTimestamp
@DynamicInsert
@DynamicUpdate
@Formula
@NaturalId
@Immutable
```

Use them when Hibernate-specific behavior is justified.

### Layer distinction

```text
Jakarta Persistence
        |
        +-- Portable JPA standard

Hibernate
        |
        +-- JPA provider
        +-- Hibernate-specific extensions

Spring Data JPA
        |
        +-- Repository/query abstraction

Spring Framework
        |
        +-- Transactions
        +-- Dependency Injection
        +-- Application infrastructure
```

---

# 16. Quick Annotation Map

| Area                 | Important annotations                                                                   |
| -------------------- | --------------------------------------------------------------------------------------- |
| Entity               | `@Entity`, `@Table`                                                                     |
| Columns              | `@Column`, `@Basic`, `@Transient`, `@Lob`                                               |
| IDs                  | `@Id`, `@GeneratedValue`, `@SequenceGenerator`, `@TableGenerator`                       |
| One-to-one           | `@OneToOne`                                                                             |
| Many-to-one          | `@ManyToOne`                                                                            |
| One-to-many          | `@OneToMany`                                                                            |
| Many-to-many         | `@ManyToMany`                                                                           |
| Join mappings        | `@JoinColumn`, `@JoinColumns`, `@JoinTable`                                             |
| Embedded types       | `@Embeddable`, `@Embedded`                                                              |
| Overrides            | `@AttributeOverride`, `@AssociationOverride`                                            |
| Enums                | `@Enumerated`                                                                           |
| Custom conversion    | `@Converter`, `@Convert`                                                                |
| Inheritance          | `@Inheritance`, `@MappedSuperclass`                                                     |
| Discriminator        | `@DiscriminatorColumn`, `@DiscriminatorValue`                                           |
| Locking              | `@Version`, Spring Data `@Lock`                                                         |
| Transactions         | Spring `@Transactional`                                                                 |
| Queries              | Spring Data `@Query`, `@Modifying`                                                      |
| Fetching             | `@EntityGraph`                                                                          |
| Stored procedures    | `@Procedure`                                                                            |
| Lifecycle            | `@PrePersist`, `@PostPersist`, `@PreUpdate`, `@PostUpdate`, `@PreRemove`, `@PostRemove` |
| Auditing             | `@CreatedDate`, `@LastModifiedDate`, `@CreatedBy`, `@LastModifiedBy`                    |
| Hibernate extensions | `@BatchSize`, `@Fetch`, `@Formula`, `@JdbcTypeCode`, etc.                               |

---

# 17. Recommended Learning Order

Do not try to memorize every annotation simultaneously.

A better progression is:

```text
1. JPA Fundamentals
       |
       +-- Entity
       +-- Persistence Context
       +-- EntityManager
       +-- Entity lifecycle
       |
2. Basic Mapping
       |
       +-- @Entity
       +-- @Table
       +-- @Column
       +-- @Id
       +-- @GeneratedValue
       |
3. Relationships
       |
       +-- @ManyToOne
       +-- @OneToMany
       +-- @OneToOne
       +-- @ManyToMany
       +-- owning side
       +-- mappedBy
       +-- JoinColumn
       +-- JoinTable
       +-- cascade
       +-- orphanRemoval
       |
4. Transactions
       |
       +-- @Transactional
       +-- propagation
       +-- isolation
       +-- rollback
       |
5. Spring Data JPA
       |
       +-- JpaRepository
       +-- derived queries
       +-- @Query
       +-- @Modifying
       +-- projections
       |
6. Fetching
       |
       +-- LAZY
       +-- EAGER
       +-- N+1
       +-- fetch joins
       +-- @EntityGraph
       |
7. Advanced Mapping
       |
       +-- @Embeddable
       +-- @Embedded
       +-- @Enumerated
       +-- @Converter
       |
8. Inheritance
       |
       +-- @Inheritance
       +-- SINGLE_TABLE
       +-- JOINED
       +-- TABLE_PER_CLASS
       +-- discriminators
       +-- @MappedSuperclass
       |
9. Concurrency
       |
       +-- @Version
       +-- optimistic locking
       +-- pessimistic locking
       +-- @Lock
       |
10. Advanced Querying
       |
       +-- Specifications
       +-- Criteria
       +-- projections
       +-- native queries
       |
11. Hibernate-specific Features
       |
       +-- batching
       +-- custom SQL
       +-- JDBC types
       +-- provider-specific optimizations
```

## Final Mental Model

Keep these layers separate:

```text
                    Your Application
                           |
                           v
                  Spring Data JPA
                  repositories/query
                           |
                           v
                Jakarta Persistence
                 entity/relationship
                    specification
                           |
                           v
                      Hibernate
                    JPA provider
                           |
                           v
                        JDBC
                           |
                           v
                       Database
```

And separately:

```text
Spring Framework
      |
      +---- Dependency Injection
      +---- @Transactional
      +---- Transaction management
      +---- Application infrastructure
```

The key distinction is:

> **JPA defines the persistence model, Hibernate implements that model, Spring Data JPA simplifies repository/query development, and Spring Framework provides application infrastructure such as transactions and dependency injection.**
