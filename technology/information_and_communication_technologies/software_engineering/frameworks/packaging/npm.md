# NPM - Package Manager for NodeJS

## 1. **What is npm?**

* **npm** = **Node Package Manager**.
* It is the **default package manager for Node.js**, used to install, share, and manage JavaScript/TypeScript libraries and tools.
* npm is both:

  1. A **command-line tool** (`npm install`, `npm run`)
  2. An **online registry** ([npmjs.com](https://www.npmjs.com)) hosting millions of open-source packages.

---

## 2. **Core Concepts**

* **Packages & Modules**

  * Reusable code distributed via npm registry.
  * Each package includes a `package.json` manifest file.

* **Dependencies**

  * **Dependencies**: Required to run the app.
  * **DevDependencies**: Needed only for development (e.g., testing tools, bundlers).
  * **PeerDependencies**: Packages expected to be provided by the consuming project.

* **Semantic Versioning (SemVer)**

  * `^1.2.3` → compatible with patch & minor updates.
  * `~1.2.3` → compatible with patch updates only.
  * Exact `1.2.3` → fully pinned version.

* **node\_modules**

  * Local folder storing installed packages (with nested sub-dependencies).

* **Lockfiles**

  * `package-lock.json` (npm) or `yarn.lock`/`pnpm-lock.yaml` — ensure reproducible installs.

---

## 3. **Important Sections / Files**

* **`package.json`** (the core manifest file)
  Key sections:

  * `"name"` / `"version"`: Package identity.
  * `"dependencies"`: Runtime deps.
  * `"devDependencies"`: Development deps.
  * `"scripts"`: Custom CLI commands (e.g., `"start": "node server.js"`).
  * `"engines"`: Required Node.js/npm versions.
  * `"main"` / `"exports"`: Entry points.
  * `"peerDependencies"`: Dependencies expected from user.

* **`package-lock.json`**

  * Auto-generated.
  * Locks exact dependency versions for reproducible installs.

* **`.npmrc`**

  * Config file for registry URLs, authentication, caching, etc.

---

## 4. **Modern Way of Working with npm**

* Use **lockfiles** (`package-lock.json`) for reproducibility.
* Prefer `npx` (runs a package without installing globally).
* Use **workspaces** (`"workspaces": ["packages/*"]`) for multi-package monorepos.
* Use **ESM (`"type": "module"`)** instead of CommonJS when possible.
* Alternative package managers:

  * **Yarn** → Faster, better dependency resolution (Plug’n’Play).
  * **pnpm** → Efficient storage (single copy of packages, symlinks into projects).
  * **bun** (emerging) → All-in-one runtime, package manager, bundler.

---

## 5. **Build Systems npm Integrates With**

npm is a **package manager**, but integrates with JavaScript build tools:

* **webpack** → Bundler (packages JS, CSS, assets into bundles).
* **Rollup** → Optimized for libraries & tree-shaking.
* **Parcel / Vite** → Fast, zero-config bundlers/dev servers.
* **esbuild / swc** → Next-gen compilers (written in Go/Rust for speed).

### Comparison of Package Managers

| Feature              | npm                         | Yarn (Berry)       | pnpm                       |
| -------------------- | --------------------------- | ------------------ | -------------------------- |
| Lockfile             | `package-lock.json`         | `yarn.lock`        | `pnpm-lock.yaml`           |
| Speed (Cold Install) | Moderate                    | Faster             | Very fast                  |
| Disk Usage           | High (`node_modules` bloat) | Lower (PnP option) | Very low (symlinked store) |
| Monorepo Support     | Workspaces                  | Workspaces         | Workspaces                 |
| Adoption             | Very high                   | Medium             | Growing fast               |

---

## 6. **Creating Optimized Builds with npm**

* **Dependency Management**

  * Pin versions (`"dependencies": {"lib": "1.2.3"}`) for stability.
  * Use lockfiles in version control.
  * Remove unused packages (`npm prune`, `depcheck`).

* **Performance**

  * Use `npm ci` (clean install from lockfile) in CI/CD for speed & reproducibility.
  * Cache `~/.npm` in CI pipelines.
  * Prefer `--production` flag to skip devDependencies in production builds.

* **Security**

  * Run `npm audit` to check vulnerabilities.
  * Use `npm audit fix` or manually patch versions.

* **Optimized Bundling**

  * Use tree-shaking bundlers (webpack, Rollup, Vite).
  * Split code into chunks for faster load times.
  * Minify and compress assets (Terser, esbuild).

* **Monorepo Optimization**

  * Use **npm workspaces** or switch to **pnpm**/**Yarn** for large-scale projects.
