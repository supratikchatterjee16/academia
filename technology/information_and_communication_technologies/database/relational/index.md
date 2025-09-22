
# Relational Database Management System

A **Relational Database Management System (RDBMS)** stores data in tables (rows & columns) and manages relationships between them using keys. RDBMSs expose a declarative query language (SQL) that lets you create, read, update and delete data while the system enforces constraints, transactions and integrity rules. Key properties you should expect from an RDBMS are **ACID** transactions (atomicity, consistency, isolation, durability), a schema (tables/columns/types), declarative querying via SQL, and support for indexes, joins and constraints.

## Comparison of 15 popular RDBMS systems

* **SQL compliance** — qualitative (High / Medium / Low) and what that means in practice (how much of modern ANSI/ISO SQL the system implements and whether it includes many proprietary extensions). This is *indicative* — exact conformance to a particular SQL standard revision varies by release.
* **ACID** — whether the product provides full ACID transactional guarantees by default (some systems provide eventual or limited guarantees in certain modes).
* **Scaling model** — common deployment/scaling pattern: vertical (scale-up), read-replica scaling, or horizontally distributed / shared-nothing.
* **Typical use** — common production scenarios.

|  # | RDBMS                           | Vendor / Org                | License                                          |                                                                                        SQL compliance (qualitative) |                                             ACID | Scaling model                                       | Typical use-case                                                                    |
| -: | ------------------------------- | --------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------: | -----------------------------------------------: | --------------------------------------------------- | ----------------------------------------------------------------------------------- |
|  1 | **Oracle Database**             | Oracle                      | Commercial (proprietary)                         |                                                   **High** — very broad SQL features + many proprietary extensions. |                                        Full ACID | Vertical + clustering (RAC)                         | Enterprise OLTP, large mixed workloads, advanced features (security, partitioning). |
|  2 | **PostgreSQL**                  | PostgreSQL Global Dev Group | Open-source (Postgres license)                   |                                            **High** — very standards-compliant, advanced SQL features & extensions. |                                        Full ACID | Vertical, read replicas, some distributed options   | General purpose, analytical + transactional, extensible apps.                       |
|  3 | **MySQL**                       | Oracle (originally Sun)     | Open-source (GPL) + commercial                   |                       **Medium** — SQL92 plus many extensions; historically lagged on newer standards but improved. |                                    ACID (InnoDB) | Vertical, read replicas; sharding via proxies       | Web apps, LAMP stacks, read-heavy workloads.                                        |
|  4 | **Microsoft SQL Server**        | Microsoft                   | Commercial (and Developer/Express free editions) |                                               **High** — strong SQL feature set, plus MS-specific T-SQL extensions. |                                        Full ACID | Vertical, Always On availability groups for scaling | Enterprise apps on Windows/.NET, analytics & OLTP.                                  |
|  5 | **SQLite**                      | D. Richard Hipp / community | Public domain / permissive                       |              **Low–Medium** — supports many SQL features but lacks full server features & extensive procedural SQL. |                        ACID (single-file engine) | Embedded / local (not for distributed scaling)      | Embedded apps, mobile, testing, small apps.                                         |
|  6 | **MariaDB**                     | MariaDB Foundation          | Open-source (GPL)                                |                                            **Medium–High** — MySQL-compatible with additional features and engines. |                        ACID (InnoDB/XtraDB etc.) | Vertical, read replicas, some clustering engines    | Drop-in MySQL replacement, web apps, forks with extra engines.                      |
|  7 | **IBM Db2**                     | IBM                         | Commercial + community editions                  |                                                          **High** — strong standards support & enterprise features. |                                        Full ACID | Vertical, clustering, federation                    | Large enterprises, mainframe/OLTP.                                                  |
|  8 | **SAP HANA**                    | SAP                         | Commercial                                       |                                                     **High** — SQL support plus in-memory extensions for analytics. |              ACID (with in-memory optimizations) | Scale-up in-memory; scale-out clusters              | Real-time analytics, mixed OLAP/OLTP.                                               |
|  9 | **Amazon Aurora**               | AWS                         | Managed service (proprietary)                    | **High (MySQL/Postgres-compatible)** — implements major features of its compatibility engine (MySQL or PostgreSQL). |                                        Full ACID | Managed horizontal storage + read replicas          | Cloud-native OLTP with high availability, MySQL/Postgres workloads.                 |
| 10 | **CockroachDB**                 | Cockroach Labs              | Open-source + commercial                         |                                             **High** — PostgreSQL-compatible SQL surface; NewSQL distributed model. | Strong ACID (distributed serializable/consensus) | Horizontally distributed (geo)                      | Global distribution, resilient OLTP, multi-region apps.                             |
| 11 | **Google Cloud Spanner**        | Google                      | Managed service (proprietary)                    |                                                **High** — ANSI-SQL-like surface (NewSQL) but with some differences. |                Strong ACID (globally consistent) | Horizontally distributed, global                    | Global-scale transactional apps needing strong consistency.                         |
| 12 | **Teradata**                    | Teradata                    | Commercial                                       |                                               **High (analytic SQL)** — strong SQL support tuned for MPP analytics. |                  ACID (for transactional layers) | MPP (massively parallel processing)                 | Data warehousing and large-scale analytics.                                         |
| 13 | **Firebird**                    | Firebird Project            | Open-source (IPL)                                |                                                               **Medium** — classic SQL support, lightweight server. |                                             ACID | Vertical, small-scale clustering options            | SMB apps, embedded to mid-size transactional apps.                                  |
| 14 | **Percona Server (MySQL fork)** | Percona                     | Open-source (GPL)                                |                                                    **Medium** — MySQL-compatible with performance/ops improvements. |                              ACID (InnoDB-based) | Vertical, replicas; Percona XtraDB Cluster for HA   | High-performance MySQL-compatible deployments.                                      |
| 15 | **Snowflake**                   | Snowflake Inc.              | Commercial (cloud service)                       |                                             **High (ANSI SQL compatible)** — SQL-oriented cloud DW with extensions. |      ACID semantics for DML in warehouse context | Cloud MPP (separate storage/compute)                | Cloud data warehouse, analytics, BI workloads.                                      |

---

### Short notes & trade-offs

* **Enterprise RDBMS (Oracle, Db2, SQL Server, SAP HANA)** tend to have the deepest feature sets, security, and vendor support but are expensive and typically scale vertically or with specialized clustering solutions.
* **Open-source systems (Postgres, MySQL/MariaDB, SQLite, Firebird)** are very popular, cost-effective and extensible. PostgreSQL is widely regarded as the most standards-compliant and feature-rich among open-source choices.
* **Cloud-managed and NewSQL (Aurora, Spanner, CockroachDB, Snowflake)** trade some traditional on-prem control for elastic scaling, managed operations and geographic distribution. They are attractive for modern cloud architectures.
* **Data warehouses (Teradata, Snowflake, Redshift — not shown above)** optimize for analytical workloads (columnar storage, MPP) and are less suited for high-frequency transactional OLTP workloads.
* **SQL compliance** is often not binary: vendors implement core ANSI/ISO SQL and then add proprietary extensions (procedural languages, windowing, JSON/JSONB, GIS, etc.). If strict standard conformance is legally or technically required, verify the exact standard revision and features on the vendor docs.

## Guidelines for true RDBMS

### Codd's Rules

Codd's twelve rules are a set of thirteen rules (numbered zero to twelve) proposed by Edgar F. Codd, a pioneer of the relational model for databases, designed to define what is required from a database management system in order for it to be considered relational, i.e., a relational database management system (RDBMS).

#### Rule 1: Information Rule

The data stored in a database, may it be user data or metadata, must be a value of some table cell. Everything in a database must be stored in a table format.

#### Rule 2: Guaranteed Access Rule

Every single data element (value) is guaranteed to be accessible logically with a combination of table-name, primary-key (row value), and attribute-name (column value). No other means, such as pointers, can be used to access data.

#### Rule 3: Systematic Treatment of NULL Values

The NULL values in a database must be given a systematic and uniform treatment. This is a very important rule because a NULL can be interpreted as one the following − data is missing, data is not known, or data is not applicable.

#### Rule 4: Active Online Catalog

The structure description of the entire database must be stored in an online catalog, known as data dictionary, which can be accessed by authorized users. Users can use the same query language to access the catalog which they use to access the database itself.

#### Rule 5: Comprehensive Data Sub-Language Rule

A database can only be accessed using a language having linear syntax that supports data definition, data manipulation, and transaction management operations. This language can be used directly or by means of some application. If the database allows access to data without any help of this language, then it is considered as a violation.

#### Rule 6: View Updating Rule

All the views of a database, which can theoretically be updated, must also be updatable by the system.

#### Rule 7: High-Level Insert, Update, and Delete Rule

A database must support high-level insertion, updation, and deletion. This must not be limited to a single row, that is, it must also support union, intersection and minus operations to yield sets of data records.

#### Rule 8: Physical Data Independence

The data stored in a database must be independent of the applications that access the database. Any change in the physical structure of a database must not have any impact on how the data is being accessed by external applications.

#### Rule 9: Logical Data Independence

The logical data in a database must be independent of its user’s view (application). Any change in logical data must not affect the applications using it. For example, if two tables are merged or one is split into two different tables, there should be no impact or change on the user application. This is one of the most difficult rule to apply.

#### Rule 10: Integrity Independence

A database must be independent of the application that uses it. All its integrity constraints can be independently modified without the need of any change in the application. This rule makes a database independent of the front-end application and its interface.

#### Rule 11: Distribution Independence

The end-user must not be able to see that the data is distributed over various locations. Users should always get the impression that the data is located at one site only. This rule has been regarded as the foundation of distributed database systems.

#### Rule 12: Non-Subversion Rule

If a system has an interface that provides access to low-level records, then the interface must not be able to subvert the system and bypass security and integrity constraints.


## Database Normalization

Database normalization is the process of structuring a relational database in accordance with a series of so-called normal forms in order to reduce data redundancy and improve data integrity. It was first proposed by Edgar F. Codd as part of his relational model.

### Objective

A basic objective of the first normal form defined by Codd in 1970 was to permit data to be queried and manipulated using a "universal data sub-language" grounded in first-order logic. An example of such language is SQL, though it is one that Codd regarded as seriously flawed.)

The objectives of normalisation beyond 1NF (first normal form) were stated as follows by Codd:

        To free the collection of relations from undesirable insertion, update and deletion dependencies.
        To reduce the need for restructuring the collection of relations, as new types of data are introduced, and thus increase the life span of application programs.
        To make the relational model more informative to users.
        To make the collection of relations neutral to the query statistics, where these statistics are liable to change as time goes by.

    — E.F. Codd, "Further Normalisation of the Data Base Relational Model"[3]

An insertion anomaly. Until the new faculty member, Dr. Newsome, is assigned to teach at least one course, their details cannot be recorded.
An update anomaly. Employee 519 is shown as having different addresses on different records.
A deletion anomaly. All information about Dr. Giddens is lost if they temporarily cease to be assigned to any courses.

When an attempt is made to modify (update, insert into, or delete from) a relation, the following undesirable side-effects may arise in relations that have not been sufficiently normalized:

**Insertion anomaly** : There are circumstances in which certain facts cannot be recorded at all. For example, each record in a "Faculty and Their Courses" relation might contain a Faculty ID, Faculty Name, Faculty Hire Date, and Course Code. Therefore, the details of any faculty member who teaches at least one course can be recorded, but a newly hired faculty member who has not yet been assigned to teach any courses cannot be recorded, except by setting the Course Code to null.

**Update anomaly** : The same information can be expressed on multiple rows; therefore updates to the relation may result in logical inconsistencies. For example, each record in an "Employees' Skills" relation might contain an Employee ID, Employee Address, and Skill; thus a change of address for a particular employee may need to be applied to multiple records (one for each skill). If the update is only partially successful – the employee's address is updated on some records but not others – then the relation is left in an inconsistent state. Specifically, the relation provides conflicting answers to the question of what this particular employee's address is.

**Deletion anomaly** : Under certain circumstances, deletion of data representing certain facts necessitates deletion of data representing completely different facts. The "Faculty and Their Courses" relation described in the previous example suffers from this type of anomaly, for if a faculty member temporarily ceases to be assigned to any courses, the last of the records on which that faculty member appears must be deleted, effectively also deleting the faculty member, unless the Course Code field is set to null.

#### Normal Forms

References : [Java T Point](https://www.javatpoint.com/dbms-normalization)
    1NF : A relation is in 1NF if it contains an atomic value.
    2NF : A relation will be in 2NF if it is in 1NF and all non-key attributes are fully functional dependent on the primary key.
    3NF : A relation will be in 3NF if it is in 2NF and no transition dependency exists.
    BCNF : A stronger definition of 3NF is known as Boyce Codd's normal form.
    4NF : A relation will be in 4NF if it is in Boyce Codd's normal form and has no multi-valued dependency.
    5NF : A relation is in 5NF. If it is in 4NF and does not contain any join dependency, joining should be lossless.
    
### Advantages of Normalization

    Normalization helps to minimize data redundancy.
    Greater overall database organization.
    Data consistency within the database.
    Much more flexible database design.
    Enforces the concept of relational integrity.

### Disadvantages of Normalization

    You cannot start building the database before knowing what the user needs.
    The performance degrades when normalizing the relations to higher normal forms, i.e., 4NF, 5NF.
    It is very time-consuming and difficult to normalize relations of a higher degree.
    Careless decomposition may lead to a bad database design, leading to serious problems.


Excellent — you’re asking for a **study-level overview of SQL** that goes beyond a quick intro. I’ll give you a structured explanation with progressively deeper layers, so you can use this as a reference.

---

## **SQL**

* **SQL (Structured Query Language)** is a **domain-specific declarative language** for interacting with relational databases.
* It lets you define, manipulate, query, and control data stored in **tables** (relations).
* Unlike imperative languages (C, Java), SQL is **set-based** and **declarative**: you state *what* result you want, not *how* to compute it.
* **Core goals of SQL:**

  * Data definition (tables, schemas)
  * Data manipulation (insert, update, delete)
  * Querying (selecting, aggregating, filtering, joining sets of data)
  * Access control and transaction management

---

### **Major SQL Versions and Key Changes**

SQL has evolved through ANSI and ISO standards. Here are the **key milestones**:

| Version      | Year | Key Additions                                                                                                     |
| ------------ | ---- | ----------------------------------------------------------------------------------------------------------------- |
| **SQL-86**   | 1986 | First ANSI standard; basic SELECT, INSERT, UPDATE, DELETE, CREATE TABLE.                                          |
| **SQL-89**   | 1989 | Minor corrections, integrity constraints (PRIMARY KEY, FOREIGN KEY).                                              |
| **SQL-92**   | 1992 | Joins, subqueries, set operations (UNION/INTERSECT), CASE expressions, more data types.                           |
| **SQL:1999** | 1999 | Object-relational features, recursive queries (WITH RECURSIVE), triggers, user-defined types, procedural SQL/PSM. |
| **SQL:2003** | 2003 | XML support, window functions, sequences, standardized MERGE statement.                                           |
| **SQL:2006** | 2006 | Native XML storage/query (XQuery).                                                                                |
| **SQL:2008** | 2008 | TRUNCATE, better MERGE, INSTEAD OF triggers.                                                                      |
| **SQL:2011** | 2011 | Temporal databases (system- and application-time).                                                                |
| **SQL:2016** | 2016 | JSON support (JSON\_TABLE, JSON functions), polymorphic tables.                                                   |
| **SQL:2019** | 2019 | More JSON extensions, enhanced polymorphism, but not universally adopted yet.                                     |

Vendors (Oracle, PostgreSQL, MySQL, SQL Server) implement subsets + proprietary extensions.

### **Core SQL Sub-Languages**

SQL is traditionally divided into **five categories**, each with **basic → intermediate → advanced** usage levels:

#### a. **DDL (Data Definition Language)**

* Defines the structure (schema) of the database.

**Basic:**

```sql
CREATE TABLE Employees (
  EmpID INT PRIMARY KEY,
  Name VARCHAR(100),
  DeptID INT
);
ALTER TABLE Employees ADD COLUMN Salary DECIMAL(10,2);
DROP TABLE TempData;
```

**Intermediate:**

* Constraints (CHECK, UNIQUE, FOREIGN KEY), schema changes, indexes.

```sql
CREATE UNIQUE INDEX idx_emp_name ON Employees(Name);
ALTER TABLE Employees ADD CONSTRAINT fk_dept FOREIGN KEY (DeptID) REFERENCES Departments(DeptID);
```

**Advanced:**

* Partitions, tablespaces, materialized views.

```sql
CREATE MATERIALIZED VIEW TopEarners AS
SELECT * FROM Employees WHERE Salary > 100000;
```

---

#### b. **DQL (Data Query Language)**

* Focused on retrieving/querying data (SELECT).

**Basic:**

```sql
SELECT Name, Salary FROM Employees WHERE DeptID = 10;
```

**Intermediate:**

* Joins, aggregates, grouping.

```sql
SELECT d.DeptName, AVG(e.Salary) AS AvgSalary
FROM Employees e
JOIN Departments d ON e.DeptID = d.DeptID
GROUP BY d.DeptName;
```

**Advanced:**

* Window functions, CTEs, recursive queries.

```sql
WITH RECURSIVE OrgChart AS (
  SELECT EmpID, ManagerID, 1 AS Level FROM Employees WHERE ManagerID IS NULL
  UNION ALL
  SELECT e.EmpID, e.ManagerID, o.Level+1
  FROM Employees e JOIN OrgChart o ON e.ManagerID = o.EmpID
)
SELECT * FROM OrgChart;
```

---

#### c. **DML (Data Manipulation Language)**

* For modifying data.

**Basic:**

```sql
INSERT INTO Employees VALUES (101, 'Alice', 10, 50000);
UPDATE Employees SET Salary = 60000 WHERE EmpID = 101;
DELETE FROM Employees WHERE EmpID = 102;
```

**Intermediate:**

* Bulk inserts, multi-row updates, subqueries in DML.

```sql
INSERT INTO HighEarners (EmpID, Name)
SELECT EmpID, Name FROM Employees WHERE Salary > 100000;
```

**Advanced:**

* MERGE/UPSERT operations.

```sql
MERGE INTO Employees e
USING NewHires n ON (e.EmpID = n.EmpID)
WHEN MATCHED THEN UPDATE SET e.Salary = n.Salary
WHEN NOT MATCHED THEN INSERT (EmpID, Name, Salary) VALUES (n.EmpID, n.Name, n.Salary);
```

---

#### d. **DCL (Data Control Language)**

* Security and permissions.

**Basic:**

```sql
GRANT SELECT ON Employees TO Analyst;
REVOKE INSERT ON Employees FROM Intern;
```

**Intermediate:**

* Roles and groups.

```sql
CREATE ROLE hr_manager;
GRANT SELECT, UPDATE ON Employees TO hr_manager;
GRANT hr_manager TO Alice;
```

**Advanced:**

* Fine-grained access (row-level security, column masking).

---

#### e. **TCL (Transaction Control Language)**

* Manages transactions.

**Basic:**

```sql
BEGIN;
UPDATE Employees SET Salary = Salary*1.1 WHERE DeptID = 20;
COMMIT;
```

**Intermediate:**

* Rollback and savepoints.

```sql
SAVEPOINT before_raise;
UPDATE Employees SET Salary = Salary*1.2 WHERE DeptID = 30;
ROLLBACK TO before_raise;
```

**Advanced:**

* Isolation levels, distributed transactions.

```sql
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

---

### **Set Theory and SQL**

SQL is fundamentally based on **relational algebra**, which itself is rooted in **set theory**.

* **Tables** → represent **relations (sets of tuples)**.
* **SELECT** → projection (choosing attributes/columns).
* **WHERE** → selection (filtering elements of a set).
* **JOIN** → Cartesian product + selection conditions.
* **UNION / INTERSECT / EXCEPT** → direct set operations.
* **GROUP BY** → partitioning sets into subsets.
* **DISTINCT** → enforces set semantics (removes duplicates).

**Example (Set operation):**

```sql
-- Employees who are also Managers
SELECT EmpID FROM Employees
INTERSECT
SELECT ManagerID FROM Employees;
```
