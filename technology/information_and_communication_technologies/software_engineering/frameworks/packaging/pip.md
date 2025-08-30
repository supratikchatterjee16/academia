# Pip - Python Package Manager

**pip** (short for *“Pip Installs Packages”*) is the **default package installer for Python**. It allows developers to **install, upgrade, and manage Python packages** from the [Python Package Index (PyPI)](https://pypi.org). pip is to Python what **Maven is to Java**: it standardizes package management, dependency handling, and reproducibility across projects.

---

## **Core Concepts**

* **Packages & Modules**

  * A package = a distribution of Python code (libraries, frameworks, or tools).
  * Stored in **PyPI** or other custom indexes.

* **Virtual Environments**

  * pip works best inside a **virtual environment** (e.g., `venv`, `virtualenv`, `conda`) to isolate dependencies per project.

* **Dependency Resolution**

  * Modern pip resolves transitive dependencies (since pip 20.3, using a backtracking resolver).

* **Requirements Files**

  * `requirements.txt` lists project dependencies for reproducibility (`pip install -r requirements.txt`).

* **Metadata (PEP 517/518)**

  * Build configuration is now handled by `pyproject.toml`, not just `setup.py`.
  * pip understands modern packaging standards (PEP 517 for build systems, PEP 518 for dependencies).

---

## **Important Sections / Files**

* **`requirements.txt`**

  * Explicit list of pinned dependencies.
  * Often generated with `pip freeze > requirements.txt`.

* **`pyproject.toml`** (modern standard)

  * Defines build system requirements (e.g., setuptools, poetry, flit).
  * Replaces older reliance on `setup.py` alone.
  * Example:

    ```toml
    [build-system]
    requires = ["setuptools>=42", "wheel"]
    build-backend = "setuptools.build_meta"
    ```

* **`setup.py`** (legacy, still widely used)

  * Script for setuptools packaging. Being replaced by `pyproject.toml`.

---

## **Modern Way of Working with pip**

* Use **virtual environments** (`python -m venv .venv && source .venv/bin/activate`).
* Use **`pyproject.toml`** instead of raw `setup.py`.
* Prefer **dependency managers/wrappers**:

  * **pip-tools** → `pip-compile` for locked requirements.
  * **Poetry** → dependency + environment + build manager.
  * **PDM** → PEP 582 compliant, lightweight alternative.

---

## **Build Systems pip Works With**

pip itself is an **installer**, not a build system — but it integrates with:

* **setuptools + wheel (traditional)**

  * Most common, but verbose and older.
  * Good for compatibility, less modern dependency handling.

* **Poetry (modern)**

  * Manages dependencies, environments, and builds.
  * Uses `pyproject.toml` exclusively.
  * Simpler than setuptools.

* **Flit**

  * Lightweight packaging tool.
  * Great for pure Python packages.

* **PDM**

  * Similar to Poetry, but with PEP 582 support (no venvs needed).

### Comparison

| Feature          | setuptools/wheel | Poetry        | Flit       | PDM         |
| ---------------- | ---------------- | ------------- | ---------- | ----------- |
| Legacy Support   | ✅ High           | ⚠️ Limited    | ❌ Minimal  | ❌ Minimal   |
| Dependency Mgmt  | ❌ Manual         | ✅ Automatic   | ⚠️ Limited | ✅ Automatic |
| `pyproject.toml` | ✅ Supported      | ✅ Native      | ✅ Native   | ✅ Native    |
| Virtual Env Mgmt | ❌ External       | ✅ Built-in    | ❌ External | ✅ Optional  |
| Best For         | Backward compat  | Full projects | Small libs | Modern apps |

---

## **Creating Optimized Builds with pip**

* **Dependency Control**

  * Pin dependencies (`package==1.2.3`) in `requirements.txt` or lockfiles.
  * Use `pip-tools` for **deterministic builds** (`pip-compile`).

* **Performance**

  * Use `pip install --no-cache-dir` in CI/CD to avoid caching issues.
  * Use **wheels** instead of source distributions (`pip install somepkg --prefer-binary`).
  * Pre-build wheels for internal use (via `pip wheel`).

* **Environment Management**

  * Use `.venv` per project, or containerize builds (Docker).
  * Cache `.venv` or wheels in CI/CD pipelines for faster builds.

* **Security & Reproducibility**

  * Use `pip-audit` to check vulnerabilities.
  * Use `hash-checking mode` (`--require-hashes` in requirements) to prevent tampering.
