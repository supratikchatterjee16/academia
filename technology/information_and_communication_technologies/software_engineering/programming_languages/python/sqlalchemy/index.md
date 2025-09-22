# SQLAlchemy

## 1. Introduction: What is an ORM?

* **ORM (Object Relational Mapper)** is a programming technique that allows you to interact with a database using **objects and classes**, instead of raw SQL queries.
* SQLAlchemy provides:

  * A **Core (SQL Expression Language)** → closer to SQL, for those who want fine-grained control.
  * An **ORM Layer** → allows defining Python classes mapped to database tables.

With ORM, instead of writing:

```sql
SELECT * FROM users WHERE id = 1;
```

You can write:

```python
session.query(User).filter_by(id=1).first()
```

---

## 2. Supported Databases

SQLAlchemy supports a wide variety of databases. Some are **officially supported**, while others are **community-maintained**.

### Officially Supported (via `dialects`)

* **PostgreSQL**: `psycopg2`, `asyncpg`, `pg8000`
* **MySQL / MariaDB**: `mysqlclient` (MySQL-Python), `PyMySQL`, `asyncmy`
* **SQLite**: Built-in Python `sqlite3` (no extra install needed)
* **Oracle**: `cx_Oracle` (11+)
* **Microsoft SQL Server**: `pyodbc`, `mssql+pyodbc`, `mssql+pymssql`

### Community / Third-Party Supported

* **CockroachDB** (via PostgreSQL dialect, needs tweaks)
* **Amazon Aurora** (compatible with MySQL/PostgreSQL drivers)
* **Redshift** (uses `sqlalchemy-redshift`)
* **Snowflake** (via `snowflake-sqlalchemy`)
* **Google BigQuery** (via `pybigquery`)
* **ClickHouse** (via `sqlalchemy-clickhouse`)

**Requirements to work well:**

* Each DB dialect requires a **DB driver library** (example: PostgreSQL → `psycopg2`).
* For async support: `asyncpg`, `aiomysql`, `aioodbc`, etc.
* Some databases (like Redshift, BigQuery, Snowflake) require external **SQLAlchemy plugins**.

---

## 3. Core Concepts

### Engine

* Central object that manages the **connection pool** and database **dialect**.
* Created with `create_engine()`.

```python
from sqlalchemy import create_engine
engine = create_engine("postgresql+psycopg2://user:pass@localhost/dbname")
```

### Connection

* A **single connection** to the DB (managed by the engine).
* Used for executing **SQL expressions** directly.

```python
with engine.connect() as conn:
    result = conn.execute("SELECT 1")
```

### Session

* ORM construct that manages **conversations with the DB**.
* Handles transactions, object states, and queries.
* Created using `sessionmaker`.

```python
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
```

**Flow:**
**Engine → Connection → Session → ORM objects**

---

## 4. Normal Method (SQL Expression Language)

Without ORM classes, using SQLAlchemy Core:

```python
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

engine = create_engine("sqlite:///:memory:")
metadata = MetaData()

# Define table
users = Table("users", metadata,
              Column("id", Integer, primary_key=True),
              Column("name", String))

metadata.create_all(engine)

# Insert data
with engine.connect() as conn:
    conn.execute(users.insert().values(name="Alice"))

# Query
with engine.connect() as conn:
    result = conn.execute(users.select())
    for row in result:
        print(row)
```

---

## 5. Using ORM with Declarative Base

Declarative mapping allows defining tables as Python classes.

```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Base class for models
Base = declarative_base()

# Define ORM model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Engine and Session
engine = create_engine("sqlite:///example.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Insert record
new_user = User(name="Alice")
session.add(new_user)
session.commit()

# Query records
users = session.query(User).all()
for user in users:
    print(user.id, user.name)
```

---

## Quick Comparison: Core vs ORM (Declarative)

| Feature     | SQLAlchemy Core (Normal)                      | ORM (Declarative)         |
| ----------- | --------------------------------------------- | ------------------------- |
| Abstraction | Tables & Columns                              | Classes & Objects         |
| Syntax      | SQL-like, explicit                            | Pythonic OOP              |
| Use case    | Lightweight scripts, fine-grained SQL control | Full-fledged applications |
| Example     | `users.insert()`                              | `session.add(User(...))`  |
