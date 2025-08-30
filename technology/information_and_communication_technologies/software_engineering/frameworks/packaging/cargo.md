# Cargo - Rust package Manager

* **Cargo** is the **package manager and build system** for the Rust programming language.
* It handles:

  * **Dependency management** (downloading & compiling Rust crates from [crates.io](https://crates.io))
  * **Build automation** (compiling code, running tests, creating documentation)
  * **Project organization** (standard project structure, metadata in `Cargo.toml`)
* Cargo is to **Rust** what **npm is to JavaScript**, **pip is to Python**, and **Maven is to Java**.

---

## 2. **Core Concepts**

* **Crates**

  * A Rust **crate** = a compilation unit (library or binary).
  * Crates are distributed via crates.io.

* **Workspaces**

  * Multiple related crates can be managed in a single workspace with shared configuration.

* **Cargo.toml**

  * Project manifest file, describes package metadata and dependencies.

* **Cargo.lock**

  * Lockfile ensuring reproducible builds by freezing exact versions.

* **Build Targets**

  * Cargo can build for different architectures and platforms (`--target` flag).

* **Rustup Integration**

  * Cargo works with **rustup** to manage Rust toolchains (compiler versions, cross-compilation).

---

## 3. **Important Sections / Files**

* **`Cargo.toml`** (main manifest)
  Example:

  ```toml
  [package]
  name = "my_project"
  version = "0.1.0"
  edition = "2021"

  [dependencies]
  serde = "1.0"
  tokio = { version = "1", features = ["full"] }
  ```

  Key sections:

  * `[package]`: Metadata (name, version, edition, authors).
  * `[dependencies]`: External crates required.
  * `[dev-dependencies]`: Dependencies needed only for testing.
  * `[build-dependencies]`: Dependencies needed at build time (e.g., code generators).
  * `[features]`: Optional features (enable/disable subsets of functionality).
  * `[workspace]`: Defines a multi-crate workspace.

* **`Cargo.lock`**

  * Auto-generated, records exact versions of all dependencies.
  * Should be checked in for applications, but not libraries.

* **`src/main.rs`** / **`src/lib.rs`**

  * Entry points for binary/library crates.

---

## 4. **Modern Way of Working with Cargo**

* Use **workspaces** to manage monorepos or multi-crate projects.
* Use **features** to conditionally compile optional parts of code.
* Use **edition upgrades** (2015 → 2018 → 2021 → 2024 soon) for modern language improvements.
* Prefer **semantic version ranges** (e.g., `serde = "1.0"`) for dependencies, but lock exact versions with `Cargo.lock`.
* Use **cargo install** for installing binaries from crates.io.
* Use **cargo check** for fast dev feedback (type checking without full compilation).

---

## 5. **Build Systems Cargo Integrates With**

Cargo is **more than a package manager** — it’s also the build tool. But it integrates with:

* **rustc** → The Rust compiler (Cargo orchestrates calls to it).
* **rustup** → Manages toolchains and cross-compilation.
* **Build.rs** → Custom build scripts run before compilation.
* **Bindgen / CMake** → For FFI with C/C++ code.
* **Bazel / Buck2** → Some companies integrate Rust with polyglot build systems.

## 6. **Creating Optimized Builds with Cargo**

* **Dependency Management**

  * Use `[features]` for optional dependencies to keep binaries small.
  * Avoid unnecessary dependencies (Rust encourages writing small crates).

* **Performance**

  * Use **release mode** (`cargo build --release`) for optimized binaries.
  * Use **LTO (Link-Time Optimization)**:

    ```toml
    [profile.release]
    lto = true
    opt-level = "z"   # optimize for size, or "s" for small, "3" for speed
    ```
  * Enable `strip` in release builds to reduce binary size.

* **Reproducibility**

  * Commit `Cargo.lock` for apps (not libraries).
  * Use `cargo vendor` for vendoring dependencies (offline builds, enterprise use).

* **CI/CD Integration**

  * Cache `~/.cargo` and `target/` directories in CI to speed up builds.
  * Use `cargo test --all` in CI for full coverage.

* **Cross Compilation**

  * Use `cross` (community tool) for easy Docker-based cross-compilation.

