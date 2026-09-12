# Packaging in Python

## 1. Introduction

Python packaging has evolved significantly over the years. Modern Python projects generally use:

* `pyproject.toml` for project metadata and build configuration.
* A **build backend** such as Setuptools, Hatchling, Flit, PDM, Poetry, or a specialized backend.
* A **package installer/frontend**, most commonly `pip`.
* Optionally, a **dependency/project manager** such as PDM, Poetry, or `uv`.

A fundamental goal of modern packaging is to make the following command sufficient to install a project and its runtime dependencies:

```bash
python -m pip install .
```

The directory containing the project typically looks like:

```text
myproject/
├── pyproject.toml
├── README.md
├── LICENSE
├── src/
│   └── myproject/
│       ├── __init__.py
│       └── main.py
└── tests/
    └── test_main.py
```

The most important file is:

```text
pyproject.toml
```

---

## 2. The Modern Python Packaging Model

A modern `pyproject.toml` normally contains at least two important sections:

```toml
[build-system]

[project]
```

They serve different purposes.

### `[build-system]`

Defines **how the package is built**.

For example:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

### `[project]`

Defines **what the package is**, including its runtime dependencies.

For example:

```toml
[project]
name = "myproject"
version = "1.0.0"
requires-python = ">=3.10"

dependencies = [
    "requests>=2.31",
    "pydantic>=2.0"
]
```

Thus:

```text
[build-system]
        │
        └── Requirements needed to BUILD the package

[project]
        │
        └── Requirements needed to RUN the package
```

---

## 3. What Happens During `pip install .`

Suppose the project contains:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "myproject"
version = "1.0.0"

dependencies = [
    "requests>=2.31"
]
```

Running:

```bash
pip install .
```

conceptually performs the following steps:

```text
pip
 │
 ├── Read pyproject.toml
 │
 ├── Identify the build backend
 │
 ├── Create an isolated build environment
 │
 ├── Install the build backend
 │
 ├── Ask the backend to build the package
 │
 ├── Produce a wheel/sdist
 │
 ├── Read package metadata
 │
 ├── Resolve runtime dependencies
 │
 ├── Install dependencies
 │
 └── Install the package
```

The important point is that the user does **not** normally have to install the build backend manually.

The dependencies listed under:

```toml
[build-system]
requires = [...]
```

are used to bootstrap the build environment.

---

## 4. Build Backend vs Package Manager

One of the most important distinctions in Python packaging is that **`pip` and a build backend are not the same thing**.

### `pip`

`pip` is primarily a package installer and build frontend.

It can:

* install packages;
* resolve dependencies;
* install wheels;
* build/install local projects;
* invoke PEP 517 build backends.

### Build backend

The build backend is responsible for converting your source tree into a distributable package.

Examples include:

```text
setuptools
hatchling
flit_core
pdm-backend
poetry-core
uv_build
meson-python
scikit-build-core
maturin
```

The relationship can be visualized as:

```text
                 pip
                  │
                  │ PEP 517
                  ▼
          ┌─────────────────┐
          │  Build Backend  │
          └─────────────────┘
             │    │    │
             ▼    ▼    ▼
        setuptools
        hatchling
        flit
        pdm-backend
        poetry-core
        uv_build
        ...
```

---

## 5. Major Python Packaging Backends

The following are the major options worth considering.

| Backend / Tool        | `pip install .` | Dependency declaration |     Lockfile |    Native code |  Complexity | Best suited for            |
| --------------------- | --------------: | ---------------------: | -----------: | -------------: | ----------: | -------------------------- |
| **Setuptools**        |             Yes |              Excellent |           No |      Excellent | Medium–High | General-purpose Python     |
| **Hatchling**         |             Yes |              Excellent |           No |           Good |  Low–Medium | Modern Python libraries    |
| **Flit**              |             Yes |              Excellent |           No |        Limited |    Very Low | Simple Python libraries    |
| **PDM**               |             Yes |              Excellent |          Yes |      Excellent |      Medium | Applications and libraries |
| **Poetry**            |             Yes |              Excellent |          Yes | Limited–Medium |      Medium | Application development    |
| **uv / uv-build**     |             Yes |              Excellent | Yes via `uv` |         Varies |  Low–Medium | Modern Python projects     |
| **meson-python**      |             Yes |              Excellent |           No |      Excellent |        High | C/C++/Fortran              |
| **scikit-build-core** |             Yes |              Excellent |           No |      Excellent | Medium–High | CMake + Python             |
| **Maturin**           |             Yes |              Excellent |           No |           Rust |      Medium | Rust/Python                |
| **setuptools-rust**   |             Yes |              Excellent |           No |           Rust |      Medium | Rust + Setuptools          |

---

## 6. Setuptools

### Overview

Setuptools is the traditional, highly capable Python packaging backend.

It is particularly useful when a project requires:

* unusual packaging behavior;
* native extensions;
* C/C++;
* Cython;
* generated source;
* custom build steps;
* namespace packages;
* entry points;
* extensive ecosystem compatibility.

It is one of the safest choices when maximum compatibility and flexibility are important.

### Basic Configuration

```toml
[build-system]
requires = ["setuptools>=77"]
build-backend = "setuptools.build_meta"

[project]
name = "myproject"
version = "1.0.0"
description = "My Python project"
requires-python = ">=3.10"

dependencies = [
    "requests>=2.31",
    "pydantic>=2.0"
]
```

Installation:

```bash
python -m pip install .
```

### Optional Dependencies

```toml
[project.optional-dependencies]
dev = [
    "pytest",
    "ruff",
    "mypy"
]

postgres = [
    "psycopg[binary]"
]
```

Install development dependencies:

```bash
python -m pip install ".[dev]"
```

Install PostgreSQL support:

```bash
python -m pip install ".[postgres]"
```

### Strengths

#### 1. Mature

Setuptools has a very large installed base and extensive historical compatibility.

#### 2. Highly flexible

It can handle:

* pure Python;
* C extensions;
* Cython;
* generated code;
* package data;
* namespace packages;
* entry points;
* custom build commands.

#### 3. Strong native-extension support

Setuptools remains a practical option for projects involving:

```text
C
C++
Cython
Fortran
Rust
```

#### 4. Large ecosystem

Many existing Python projects and plugins understand Setuptools.

### Weaknesses

Its flexibility can also make configuration complicated.

A project may end up involving:

```text
pyproject.toml
setup.py
setup.cfg
MANIFEST.in
Setuptools plugins
custom commands
```

For a new, pure-Python project, this can be unnecessarily complicated.

### Recommendation

Use Setuptools when:

* maximum compatibility matters;
* you need unusual build behavior;
* you have native extensions;
* you are maintaining an existing Setuptools project.

---

## 7. Hatchling

Hatchling is the build backend associated with the Hatch project.

It is one of the cleaner modern choices for pure-Python packages.

### Basic Configuration

```toml
[build-system]
requires = ["hatchling>=1.27"]
build-backend = "hatchling.build"

[project]
name = "myproject"
version = "1.0.0"
description = "Example project"
requires-python = ">=3.10"

dependencies = [
    "requests>=2.31",
    "pydantic>=2.0"
]
```

Installation:

```bash
python -m pip install .
```

### Typical Layout

```text
myproject/
├── pyproject.toml
└── src/
    └── myproject/
        ├── __init__.py
        └── main.py
```

### Strengths

#### 1. Clean configuration

A modern project can often be described almost entirely by:

```text
pyproject.toml
```

#### 2. Excellent standards support

Hatchling works naturally with the standardized:

```toml
[project]
```

metadata model.

#### 3. Good developer tooling

The broader Hatch ecosystem provides:

* environments;
* scripts;
* testing matrices;
* version management;
* build workflows.

### Weaknesses

Hatchling itself is primarily a build backend rather than a complete dependency-management solution.

If you need:

* lock files;
* dependency resolution workflows;
* environment management;
* application-oriented dependency management;

then PDM, Poetry, or `uv` may be more appropriate.

### Recommendation

Hatchling is an excellent choice for:

> Modern, pure-Python libraries with relatively straightforward build requirements.

---

## 8. Flit

Flit is intentionally minimalist.

Its philosophy is that a normal Python package should not require a large amount of packaging configuration.

### Basic Configuration

```toml
[build-system]
requires = ["flit_core>=3.12,<5"]
build-backend = "flit_core.buildapi"

[project]
name = "myproject"
version = "1.0.0"
description = "A simple Python package"
requires-python = ">=3.10"

dependencies = [
    "requests>=2.31"
]
```

Installation:

```bash
python -m pip install .
```

### Typical Layout

```text
my-library/
├── pyproject.toml
└── my_library/
    ├── __init__.py
    └── utils.py
```

### Strengths

* Very simple.
* Minimal configuration.
* Good for straightforward libraries.
* Easy to understand.
* Less opportunity for configuration errors.

### Weaknesses

The simplicity is deliberate.

Flit is not the best choice for:

* complicated build pipelines;
* generated source;
* native extensions;
* unusual package layouts;
* custom build logic.

### Recommendation

Use Flit when the package is essentially:

> "Here is a normal Python package. Package it."

---

## 9. PDM

PDM is broader than a build backend.

It can function as:

```text
Dependency manager
Project manager
Build frontend
Build backend
```

Its own build backend is:

```text
pdm-backend
```

### Basic Configuration

```toml
[build-system]
requires = ["pdm-backend"]
build-backend = "pdm.backend"

[project]
name = "myproject"
version = "1.0.0"
requires-python = ">=3.10"

dependencies = [
    "fastapi>=0.115",
    "pydantic>=2.0",
    "uvicorn>=0.30"
]
```

Installation with pip:

```bash
python -m pip install .
```

### Dependency Groups

PDM supports dependency groups such as:

```toml
[dependency-groups]
test = [
    "pytest>=8"
]

lint = [
    "ruff>=0.6"
]

dev = [
    {include-group = "test"},
    {include-group = "lint"}
]
```

### Strengths

PDM provides:

* dependency resolution;
* lock files;
* virtual environments;
* dependency groups;
* project management;
* package publishing;
* build management.

It can also work with alternative build backends.

### Weaknesses

PDM is more machinery than necessary if the only objective is:

```bash
pip install .
```

For a small library, Hatchling or Flit can be simpler.

### Recommendation

PDM is particularly attractive for:

> Python applications and larger projects where dependency management is a first-class requirement.

---

## 10. Poetry

Poetry is an all-in-one Python project and dependency-management system.

Modern Poetry supports standardized `[project]` metadata.

### Basic Configuration

```toml
[build-system]
requires = ["poetry-core>=2.0"]
build-backend = "poetry.core.masonry.api"

[project]
name = "myproject"
version = "1.0.0"
description = "Example application"
requires-python = ">=3.10"

dependencies = [
    "fastapi>=0.115",
    "uvicorn>=0.30"
]
```

Installation:

```bash
python -m pip install .
```

### Legacy Poetry Configuration

Existing projects may still use:

```toml
[tool.poetry]
name = "myproject"
version = "1.0.0"

[tool.poetry.dependencies]
python = "^3.10"
fastapi = "^0.115"
```

This configuration is common in older Poetry projects.

### Strengths

Poetry is strong at:

* dependency resolution;
* lock files;
* virtual environments;
* dependency groups;
* publishing;
* version constraints;
* application workflows.

For example:

```bash
poetry add fastapi
```

can update both dependency metadata and the lock file.

### Weaknesses

Poetry is relatively opinionated.

It also introduces considerably more tooling than is necessary for a simple Python library.

It is important to distinguish:

```text
poetry
```

from:

```text
poetry-core
```

`poetry` is the project-management frontend, while `poetry-core` provides the build backend used when pip builds a Poetry-based package.

### Recommendation

Poetry is a good choice for:

> Application-oriented projects that want an integrated dependency-management workflow.

---

## 11. uv and uv-build

`uv` is a modern, high-performance Python package and project manager.

It provides functionality around:

* dependency resolution;
* virtual environments;
* lock files;
* Python versions;
* project management;
* package installation.

The ecosystem also provides:

```text
uv_build
```

as a build backend.

### Basic `uv_build` Configuration

```toml
[build-system]
requires = ["uv_build>=0.12.1,<0.13.0"]
build-backend = "uv_build"

[project]
name = "myproject"
version = "1.0.0"
requires-python = ">=3.10"

dependencies = [
    "requests>=2.31"
]
```

The resulting package can still be installed with:

```bash
python -m pip install .
```

### Strengths

The larger `uv` ecosystem provides:

* very fast dependency resolution;
* virtual environment management;
* lock files;
* reproducible environments;
* project management;
* Python version management.

For new projects, this is one of the most compelling modern workflows.

### Weaknesses

The ecosystem is newer than Setuptools.

Projects with unusual legacy packaging requirements may still be better served by Setuptools.

Also, `uv` and `uv_build` should be distinguished:

```text
uv
 │
 └── Project/dependency/environment manager

uv_build
 │
 └── PEP 517 build backend
```

### Recommendation

For a new project, consider:

```text
uv
+
pyproject.toml
+
PEP 621
```

as a modern development workflow.

---

## 12. meson-python

`meson-python` integrates Python packaging with the Meson build system.

It is particularly useful when Python packages contain significant native code.

Typical languages include:

```text
C
C++
Fortran
```

### Basic Configuration

```toml
[build-system]
requires = [
    "meson-python",
    "meson>=1.2"
]
build-backend = "mesonpy"

[project]
name = "myproject"
version = "1.0.0"
requires-python = ">=3.10"

dependencies = [
    "numpy>=2.0"
]
```

Installation:

```bash
python -m pip install .
```

### Strengths

Excellent for:

* C extensions;
* C++ extensions;
* Fortran;
* scientific Python;
* complex native build systems.

### Weaknesses

It is excessive for a pure-Python package.

A developer must understand both:

```text
Python packaging
+
Meson
```

and potentially:

```text
C/C++/Fortran toolchains
```

### Recommendation

Use `meson-python` when a project genuinely benefits from the Meson build system.

---

## 13. scikit-build-core

`scikit-build-core` is particularly useful for projects that use **CMake**.

The conceptual model is:

```text
Python packaging
        +
CMake
```

### Basic Configuration

```toml
[build-system]
requires = [
    "scikit-build-core>=0.10"
]
build-backend = "scikit_build_core.build"

[project]
name = "myproject"
version = "1.0.0"
requires-python = ">=3.10"

dependencies = [
    "numpy>=2.0"
]
```

Installation:

```bash
python -m pip install .
```

### Typical Layout

```text
myproject/
├── pyproject.toml
├── CMakeLists.txt
├── src/
│   ├── python/
│   │   └── myproject/
│   │       └── __init__.py
│   └── cpp/
│       └── bindings.cpp
└── tests/
```

### Strengths

Excellent when an organization already uses:

```text
CMake
C++
Python
```

It is particularly useful for building Python bindings around an existing C++ codebase.

### Weaknesses

CMake adds substantial complexity for pure-Python projects.

### Recommendation

If the project is fundamentally:

> C++ + Python bindings

then `scikit-build-core` should be high on the list.

---

## 14. Maturin

Maturin is designed for Rust/Python projects.

The typical technology stack is:

```text
Rust
+
PyO3
+
Maturin
+
Python packaging
```

### Basic Configuration

```toml
[build-system]
requires = ["maturin>=1.4,<2"]
build-backend = "maturin"

[project]
name = "myproject"
version = "1.0.0"
requires-python = ">=3.10"

dependencies = [
    "numpy>=2.0"
]
```

Installation:

```bash
python -m pip install .
```

Maturin builds the Rust extension and produces a Python-compatible wheel.

### Strengths

Excellent for:

* Rust extensions;
* PyO3;
* performance-critical components;
* memory-safe native code.

### Weaknesses

It introduces:

```text
Rust
Cargo
PyO3
Maturin
Python packaging
```

so it is inappropriate unless Rust is actually part of the project.

### Recommendation

For a Rust-first Python extension:

> Maturin is one of the first options to consider.

---

## 15. setuptools-rust

Another option for Rust integration is:

```text
Setuptools
+
setuptools-rust
```

A minimal build configuration might start with:

```toml
[build-system]
requires = [
    "setuptools>=77",
    "setuptools-rust"
]
build-backend = "setuptools.build_meta"
```

### Strengths

* Retains the Setuptools ecosystem.
* Useful for existing Setuptools projects.
* Allows Rust components to be integrated into a Setuptools-based build.

### Weaknesses

For a project that is primarily Rust with Python bindings, Maturin is often conceptually cleaner.

### Recommendation

Use this when:

> The project is already fundamentally Setuptools-based and Rust is an additional component.

---

## 16. Runtime Dependencies vs Build Dependencies

This distinction is critical.

Suppose an application requires:

```text
FastAPI
Pydantic
Uvicorn
```

These are runtime dependencies:

```toml
[project]
dependencies = [
    "fastapi>=0.115",
    "pydantic>=2",
    "uvicorn>=0.30"
]
```

Now suppose the package requires:

```text
Cython
setuptools
```

to build the package.

These are build dependencies:

```toml
[build-system]
requires = [
    "setuptools>=77",
    "Cython>=3"
]
```

Therefore:

```text
[build-system]
    │
    └── Dependencies needed to BUILD the package

[project]
    │
    └── Dependencies needed to RUN the package
```

These two sets should not be confused.

---

## 17. Optional Dependencies

A project can define dependencies that users install only when a particular feature is required.

For example:

```toml
[project]
name = "myproject"
version = "1.0.0"

dependencies = [
    "fastapi>=0.115"
]

[project.optional-dependencies]
dev = [
    "pytest>=8",
    "ruff>=0.6",
    "mypy>=1.10"
]

postgres = [
    "psycopg[binary]"
]
```

Normal installation:

```bash
python -m pip install .
```

installs:

```text
fastapi
myproject
```

Development installation:

```bash
python -m pip install ".[dev]"
```

installs:

```text
fastapi
pytest
ruff
mypy
myproject
```

PostgreSQL support:

```bash
python -m pip install ".[postgres]"
```

installs the PostgreSQL dependency as well.

---

## 18. Platform-Specific Dependencies

Dependencies can also be conditional.

For example:

```toml
[project]
dependencies = [
    "requests>=2.31",
    "pywin32>=306; sys_platform == 'win32'",
    "uvloop>=0.19; sys_platform != 'win32'"
]
```

On Windows, pip can install:

```text
pywin32
```

while on other platforms it can install:

```text
uvloop
```

Python version markers can also be used:

```toml
[project]
dependencies = [
    "typing-extensions>=4.10; python_version < '3.11'"
]
```

This is considerably more expressive than blindly installing a fixed `requirements.txt` on every platform.

---

## 19. `requirements.txt` vs `pyproject.toml`

These files solve related but different problems.

### `requirements.txt`

Typically answers:

> "What packages should exist in this environment?"

Example:

```text
fastapi==0.115.6
uvicorn==0.34.0
pytest==8.3.4
```

It is commonly used for environment/deployment requirements.

### `pyproject.toml`

Typically answers:

> "What does this package require?"

Example:

```toml
[project]
dependencies = [
    "fastapi>=0.115",
    "uvicorn>=0.34"
]
```

The dependency metadata becomes part of the built distribution.

If someone receives:

```text
myproject-1.0.0-py3-none-any.whl
```

pip can inspect its metadata and determine the runtime dependencies automatically.

---

## 20. `setup.py` and `setup.cfg`

Older Python projects commonly contain:

```text
setup.py
setup.cfg
```

For example:

```python
from setuptools import setup

setup(
    name="myproject",
    version="1.0.0",
)
```

Modern Python packaging generally prefers:

```text
pyproject.toml
```

with:

```toml
[build-system]
...
```

and:

```toml
[project]
...
```

For new projects, there is generally little reason to start with a `setup.py`-centric configuration.

However, `setup.py` remains relevant when maintaining legacy projects or handling specialized Setuptools workflows.

---

## 21. Package Layout

A common modern layout is the **src layout**:

```text
myproject/
├── pyproject.toml
├── README.md
├── LICENSE
├── src/
│   └── myproject/
│       ├── __init__.py
│       ├── main.py
│       └── utils.py
└── tests/
    └── test_main.py
```

An alternative is the flat layout:

```text
myproject/
├── pyproject.toml
├── myproject/
│   ├── __init__.py
│   └── main.py
└── tests/
```

The `src` layout has the advantage of making it harder to accidentally import the source tree instead of the actually installed package during development.

For libraries, the `src` layout is often a good default.

---

## 22. Complete Minimal Hatchling Example

A complete minimal project can be:

```text
myproject/
├── pyproject.toml
├── README.md
└── src/
    └── myproject/
        ├── __init__.py
        └── main.py
```

`pyproject.toml`:

```toml
[build-system]
requires = ["hatchling>=1.27"]
build-backend = "hatchling.build"

[project]
name = "myproject"
version = "1.0.0"
description = "Example Python package"
readme = "README.md"
requires-python = ">=3.10"

dependencies = [
    "requests>=2.31,<3",
    "pydantic>=2,<3"
]

[project.optional-dependencies]
dev = [
    "pytest>=8",
    "ruff>=0.6"
]
```

Installation:

```bash
python -m pip install .
```

Development installation:

```bash
python -m pip install ".[dev]"
```

---

## 23. Complete Minimal Setuptools Example

```toml
[build-system]
requires = ["setuptools>=77"]
build-backend = "setuptools.build_meta"

[project]
name = "myproject"
version = "1.0.0"
description = "Example Python package"
readme = "README.md"
requires-python = ">=3.10"

dependencies = [
    "requests>=2.31,<3",
    "pydantic>=2,<3"
]

[project.optional-dependencies]
dev = [
    "pytest>=8",
    "ruff>=0.6"
]
```

Installation:

```bash
python -m pip install .
```

---

## 24. Complete Minimal Flit Example

```toml
[build-system]
requires = ["flit_core>=3.12,<5"]
build-backend = "flit_core.buildapi"

[project]
name = "myproject"
version = "1.0.0"
description = "Example Python package"
requires-python = ">=3.10"

dependencies = [
    "requests>=2.31"
]
```

Installation:

```bash
python -m pip install .
```

---

## 25. Choosing the Appropriate Tool

### Pure Python library

Recommended order:

```text
Hatchling
    │
    ├── Simple modern configuration
    │
    └── Excellent PEP 621 support
```

or:

```text
Setuptools
    │
    └── Maximum compatibility/flexibility
```

For an extremely simple package:

```text
Flit
```

is also an excellent choice.

---

### Python application

Consider:

```text
uv
PDM
Poetry
```

because dependency management becomes much more important than merely building a wheel.

---

### C/C++ + Python

For CMake:

```text
scikit-build-core
```

For Meson:

```text
meson-python
```

For conventional native extensions:

```text
Setuptools
```

can still be appropriate.

---

### Rust + Python

Prefer:

```text
Maturin
```

when the project is fundamentally Rust-oriented.

Use:

```text
setuptools-rust
```

when the project is already fundamentally Setuptools-based.

---

## 26. Recommended Decision Matrix

| Requirement                                | Recommended choice    |
| ------------------------------------------ | --------------------- |
| Minimal pure-Python library                | **Flit**              |
| Modern pure-Python library                 | **Hatchling**         |
| Maximum compatibility                      | **Setuptools**        |
| Complicated Python build                   | **Setuptools**        |
| Python application + dependency management | **PDM**               |
| Poetry-based organization                  | **Poetry**            |
| Modern high-performance workflow           | **uv**                |
| CMake + C++                                | **scikit-build-core** |
| Meson + native code                        | **meson-python**      |
| Rust + Python                              | **Maturin**           |
| Existing Setuptools + Rust                 | **setuptools-rust**   |

---

## 27. Recommended Modern Baseline

For a normal Python library, a good baseline is:

```text
pyproject.toml
        │
        ├── PEP 621 project metadata
        │
        ├── Hatchling
        │
        └── Runtime dependencies
```

For example:

```toml
[build-system]
requires = ["hatchling>=1.27"]
build-backend = "hatchling.build"

[project]
name = "my-library"
version = "1.0.0"
description = "My Python library"
readme = "README.md"
requires-python = ">=3.10"

dependencies = [
    "requests>=2.31,<3",
    "pydantic>=2,<3"
]

[project.optional-dependencies]
dev = [
    "pytest>=8",
    "ruff>=0.6",
    "mypy>=1.10"
]
```

Then:

```bash
python -m pip install .
```

is sufficient for an ordinary user.

For development:

```bash
python -m pip install ".[dev]"
```

---

## 28. Important Packaging Concepts

A useful mental model is:

```text
                         Python Project
                               │
                               ▼
                        pyproject.toml
                               │
              ┌────────────────┴────────────────┐
              │                                 │
              ▼                                 ▼
        [project]                         [build-system]
              │                                 │
              │                                 ▼
              │                           Build backend
              │                                 │
              │                    ┌────────────┼────────────┐
              │                    │            │            │
              │               setuptools   hatchling      flit
              │                    │            │            │
              │                    └────────────┼────────────┘
              │                                 │
              │                                 ▼
              │                           Wheel / sdist
              │
              ▼
        Runtime dependencies
              │
              ▼
             pip
              │
              ▼
        Dependency resolver
              │
              ▼
       Installed environment
```

The critical concepts are therefore:

1. **`pyproject.toml`** — project configuration.
2. **PEP 621 `[project]` metadata** — standardized package metadata.
3. **PEP 517 build backend** — builds the distribution.
4. **`pip`** — installs the resulting distribution and its dependencies.
5. **Dependency groups/extras** — separate runtime, development, and optional dependencies.
6. **Lock files** — provide reproducibility when using tools such as PDM, Poetry, or `uv`.
7. **Wheels** — the preferred binary distribution format for installation.
8. **sdists** — source distributions used when a suitable wheel is unavailable.

---

## 29. Final Recommendations

If the only requirement is:

> Clone a Python project and run `pip install .`, with all runtime dependencies automatically installed.

then you do **not** need a heavyweight dependency-management system.

A clean solution is:

```text
pyproject.toml
+
PEP 621
+
a PEP 517 build backend
```

My practical recommendations are:

#### General-purpose

```text
Setuptools
```

Choose this when compatibility and flexibility are more important than minimal configuration.

#### Modern pure-Python

```text
Hatchling
```

Choose this when you want a clean, standards-oriented package with minimal configuration.

#### Very simple library

```text
Flit
```

Choose this when the package structure and build requirements are straightforward.

#### Application with dependency management

```text
uv
PDM
Poetry
```

Choose one of these when dependency resolution, lock files, environments, and development workflows are significant requirements.

#### Native extensions

```text
CMake → scikit-build-core
Meson → meson-python
Rust → Maturin
```

These specialized backends are preferable when the native build system itself is an important part of the project.

The central principle is:

```text
              pip install .
                    │
                    ▼
             pyproject.toml
                    │
          ┌─────────┴─────────┐
          │                   │
     Build backend       Project metadata
          │                   │
          ▼                   ▼
      Build package      Runtime dependencies
          │                   │
          └─────────┬─────────┘
                    ▼
              Installed package
```

For a new, ordinary Python package, **`pyproject.toml` + PEP 621 + Hatchling (or Setuptools)** is a strong default. The more specialized backends become relevant when dependency management, native compilation, Rust, CMake, or another substantial build requirement enters the picture.
