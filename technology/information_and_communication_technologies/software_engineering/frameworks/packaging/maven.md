# Maven - Java Package Manager

**Apache Maven** is a **build automation and project management tool** for Java (and other JVM languages).

* It helps developers **compile, test, package, and deploy** applications in a consistent, repeatable way.
* Unlike older tools (like Ant), Maven is **declarative** — you describe your project and its dependencies in a single file (`pom.xml`), and Maven handles the build steps automatically.
* It is based on the idea of **Convention over Configuration**: if you follow standard directory structures and naming, Maven can build your project with minimal configuration.

### Key Roles of Maven:

1. **Dependency Management**

   * Automatically downloads required libraries (and their sub-dependencies) from repositories.
2. **Standardized Project Structure**

   * Encourages `src/main/java` for source code, `src/test/java` for tests, etc.
3. **Build Lifecycle Management**

   * Provides predefined lifecycles (`clean`, `default`, `site`) with standard build phases.
4. **Extensibility via Plugins**

   * Tasks like compiling, testing, creating JAR/WAR files, generating reports, or deploying are all handled by plugins.
5. **Integration with Ecosystem**

   * Works smoothly with CI/CD pipelines, IDEs (Eclipse, IntelliJ), and repository managers (Nexus, Artifactory).

## 1. **History**

* **Pre-Maven Era**: Before Maven, Java projects often used **Ant** (and Makefiles earlier) for builds. These tools gave flexibility but required extensive manual configuration.
* **Problem**: Dependency management, standardization, and reproducibility were difficult — projects had custom build scripts and dependency JARs checked into version control.
* **Maven Launch**: Introduced by the **Apache Software Foundation** in **2004**, Maven aimed to provide:

  * **Convention over configuration**
  * **Dependency management via central repositories**
  * **Standard project structure**
  * **Reusable lifecycle and plugins**

---

## 2. **Core Concepts**

* **Project Object Model (POM)**: `pom.xml` defines a project’s configuration (dependencies, plugins, build lifecycle).
* **Convention over Configuration**: Follows defaults (e.g., source code in `src/main/java`, tests in `src/test/java`) to reduce boilerplate.
* **Dependency Management**:

  * Maven retrieves dependencies from **local, central, or remote repositories**.
  * Supports **transitive dependencies** (automatically pulls required sub-dependencies).
* **Lifecycle & Phases**: Defines a **build lifecycle** with standard phases (e.g., `compile`, `test`, `package`, `install`, `deploy`).
* **Plugins**: Provide actual build tasks (e.g., compiler, surefire for tests, shade for fat JARs).
* **Repositories**:

  * **Local**: `.m2/repository` on developer’s machine.
  * **Central**: Maven Central Repository (public).
  * **Remote**: Custom repositories (Nexus, Artifactory).

---

## 3. **Important POM Tags / Sections**

In `pom.xml`:

* `project`: Root element.
* `modelVersion`: POM model version (usually `4.0.0`).
* `groupId`: Unique org/project identifier.
* `artifactId`: Project’s unique name.
* `version`: Version of artifact.
* `packaging`: Type of build artifact (`jar`, `war`, `pom`).
* `dependencies`: List of required libraries.
* `dependencyManagement`: Defines versions for dependencies (helps avoid conflicts).
* `repositories`: Additional repositories beyond Maven Central.
* `build`: Custom build settings.
* `plugins`: Plugins used during build.
* `profiles`: Different build configurations (e.g., dev vs. prod).
* `properties`: Key-value pairs for reuse (e.g., Java version).
* `modules`: For multi-module projects.

---

## 4. **Build Lifecycles & Phases**

Maven has **3 built-in lifecycles**:

### (a) **default** (main build)

* `validate` → check project structure
* `compile` → compile source code
* `test` → run unit tests
* `package` → bundle artifact (JAR/WAR)
* `verify` → run integration tests
* `install` → copy artifact to local repo
* `deploy` → publish to remote repo

### (b) **clean** (cleanup)

* `pre-clean`
* `clean`
* `post-clean`

### (c) **site** (documentation)

* `pre-site`
* `site`
* `post-site`
* `site-deploy`

> Each phase triggers goals bound by plugins (e.g., `maven-compiler-plugin:compile` runs in `compile` phase).

---

## 5. **Creating Optimized Builds**

* **Dependency Management**

  * Use `<dependencyManagement>` to avoid version conflicts.
  * Prefer stable versions over SNAPSHOTs in production.
  * Exclude unnecessary transitive dependencies.

* **Build Performance**

  * Use `mvn -T 1C install` (parallel builds, 1 thread per core).
  * Use `mvn clean install -DskipTests` for faster non-test builds.
  * Use **incremental builds** with tools like [Maven Incremental Build](https://maven.apache.org/docs/3.9.0/release-notes.html).

* **Profiles & Environments**

  * Define `<profiles>` for dev/test/prod with different settings (e.g., database configs).
  * Use property filtering for environment-specific resources.

* **Shading & Minimization**

  * Use `maven-shade-plugin` to create a single executable JAR (fat JAR).
  * Minimize dependencies to reduce artifact size.

* **CI/CD Integration**

  * Cache `.m2/repository` in CI pipelines.
  * Run `mvn verify` before deployment for consistent validation.

---
