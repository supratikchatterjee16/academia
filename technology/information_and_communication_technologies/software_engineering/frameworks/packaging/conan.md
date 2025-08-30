# Conan - C/C++ Package Manager

**Conan** is a **package manager for C and C++**. It helps developers **manage dependencies, build configurations, and package binaries** in a reproducible way. Since C++ has no single standardized build or package system (unlike Java with Maven or Rust with Cargo), Conan fills that gap. Works across operating systems, compilers (GCC, Clang, MSVC), and build systems (CMake, Meson, Autotools, etc.).

---

## 2. **Core Concepts**

* **Packages & Recipes**

  * A Conan package = a binary or source distribution of a C/C++ library.
  * Defined by a `conanfile.py` or `conanfile.txt` (recipe).

* **Conan Center**

  * The central repository hosting popular C++ packages.

* **Profiles**

  * Define build settings (compiler, version, build type, architecture).
  * Example: `default` profile for dev, `release` profile for production.

* **Settings & Options**

  * Settings: compiler, OS, architecture.
  * Options: package-specific toggles (e.g., enable/disable SSL support).

* **Remotes**

  * Repositories (ConanCenter, Artifactory, custom remotes).

* **Lockfiles**

  * Ensure reproducible dependency resolution.

---

## 3. **Important Sections / Files**

* **`conanfile.txt`** (simpler, dependency list)

  ```ini
  [requires]
  fmt/9.1.0
  spdlog/1.11.0

  [generators]
  cmake
  ```

* **`conanfile.py`** (full recipe)

  ```python
  from conan import ConanFile

  class HelloConan(ConanFile):
      name = "hello"
      version = "0.1"
      settings = "os", "compiler", "build_type", "arch"
      requires = "fmt/9.1.0"
      generators = "CMakeDeps"
  ```

* **`conan.lock`**

  * Lockfile for reproducibility (pinned versions + options).

* **Profiles (`~/.conan2/profiles/`)**

  * Example:

    ```ini
    [settings]
    os=Linux
    compiler=gcc
    compiler.version=11
    build_type=Release
    arch=x86_64
    ```

---

## 4. **Modern Way of Working with Conan (v2)**

* Use **Conan 2.x** (released 2023) — major redesign for clarity and consistency.
* Use **CMakeDeps** + **CMakeToolchain** generators instead of legacy ones.
* Prefer **lockfiles** for reproducible builds.
* Use **profiles** to separate build configs (debug/release, cross-compilation).
* Integrate Conan with CI/CD (GitHub Actions, GitLab CI, Jenkins).
* Upload custom packages to **Artifactory** or private remotes.

---

## 5. **Build Systems Conan Integrates With**

Conan is not itself a build system (like Cargo) but integrates tightly with many:

* **CMake** → Primary build system integration (`CMakeDeps`, `CMakeToolchain`).
* **Meson** → Supported via generators.
* **Autotools / Makefiles** → Supported.
* **Bazel** → Third-party integrations.
* **Visual Studio / Xcode** → Integration via toolchains.

---

## 6. **Creating Optimized Builds with Conan**

* **Dependency Management**

  * Use version ranges (`fmt/[>=9.0 <10.0]`) for flexibility.
  * Use lockfiles for reproducibility.
  * Vendor private packages into your own Artifactory.

* **Profiles & Multi-Config**

  * Define profiles for Debug/Release/Cross-compilation.
  * Example: cross-compiling to ARM with a separate profile.

* **Performance**

  * Use prebuilt binaries (Conan caches them).
  * Build once, deploy everywhere (avoids per-developer builds).

* **Reproducibility**

  * Always commit lockfiles for applications.
  * Use `conan create` + `conan upload` for distributing consistent binaries.

* **CI/CD Optimization**

  * Cache `~/.conan2` in pipelines.
  * Use profiles per environment (Linux, Windows, macOS).
  * Automate package uploads after successful builds.
