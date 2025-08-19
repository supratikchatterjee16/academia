# Packaging

Programs in every programming language need a package manager, in order to manage external dependencies with versions and simplify compilation and structuring.

As such, the package managers usually have the following components:

- The manager itself
- One or more configuration files for defining the versions, and compilation recipes
- Index for external dependencies
- A prescribed folder structure to use

The following is a table of popular programming languages and their package managers:

| **Language**             | **Primary Package Manager(s)**  | **Notes**                                                                                                  |
| ------------------------ | ------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Java**                 | **Maven**, **Gradle**           | Maven uses XML (`pom.xml`), Gradle uses Groovy/Kotlin (`build.gradle`). Both handle dependencies & builds. |
| **Python**               | **pip**, **conda**              | `pip` is standard (PyPI); `conda` also manages environments and non-Python dependencies.                   |
| **JavaScript / Node.js** | **npm**, **yarn**, **pnpm**     | `npm` comes by default; `yarn` and `pnpm` improve speed and efficiency.                                    |
| **TypeScript**           | **npm**, **yarn**, **pnpm**     | Uses the same ecosystem as JavaScript.                                                                     |
| **C / C++**              | **vcpkg**, **Conan**            | `vcpkg` (by Microsoft) and `Conan` are modern dependency managers.                                         |
| **Rust**                 | **Cargo**                       | Built-in, handles packages ("crates") and builds.                                                          |
| **Go (Golang)**          | **Go Modules (go mod)**         | Built-in dependency management since Go 1.11+.                                                             |
| **Ruby**                 | **RubyGems**, **Bundler**       | `RubyGems` is the base; `Bundler` manages project dependencies.                                            |
| **PHP**                  | **Composer**                    | Standard for PHP package/dependency management.                                                            |
| **R**                    | **CRAN**, **Bioconductor**      | CRAN is main repository; Bioconductor for bioinformatics packages.                                         |
| **Perl**                 | **CPAN**                        | Longstanding Perl package ecosystem.                                                                       |
| **.NET (C#, F#)**        | **NuGet**                       | Official package manager for .NET projects.                                                                |
| **Haskell**              | **Cabal**, **Stack**            | `Cabal` is traditional; `Stack` provides reproducible builds.                                              |
| **Elixir**               | **Hex**                         | Standard package manager for Elixir/Erlang ecosystem.                                                      |
| **Erlang**               | **rebar3**, **Hex**             | `rebar3` is build tool; `Hex` for package distribution.                                                    |
| **Scala**                | **sbt**, **Maven**, **Gradle**  | `sbt` is most popular in Scala projects.                                                                   |
| **Kotlin**               | **Gradle**, **Maven**           | Gradle (Kotlin DSL) is the most common.                                                                    |
| **Swift**                | **Swift Package Manager (SPM)** | Official tool for Swift package management.                                                                |
| **Objective-C**          | **CocoaPods**, **Carthage**     | Used in iOS/macOS projects.                                                                                |
| **Julia**                | **Pkg.jl**                      | Built-in package manager.                                                                                  |
| **OCaml**                | **opam**                        | The de facto package manager for OCaml.                                                                    |
| **Dart / Flutter**       | **pub**                         | Standard dependency manager for Dart/Flutter apps.                                                         |
| **Lua**                  | **LuaRocks**                    | Standard Lua package manager.                                                                              |
