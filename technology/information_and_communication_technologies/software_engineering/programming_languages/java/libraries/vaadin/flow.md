# Vaadin Flow

> Short summary: **Vaadin Flow** is the server-side Java framework in the Vaadin platform that lets you build web UIs using Java components that are rendered to the browser as Web Components. The runtime keeps UI state on the server and synchronizes updates to the client. ([Vaadin][1])

## 1) Version / release history — major Flow / platform changes (high level)

I'll list major Flow / platform releases and the most notable changes per release family. For full, line-by-line changelogs check the Flow and Platform GitHub releases and Vaadin release notes (links in sources).

**Notes on mapping:** Vaadin Flow is shipped as part of Vaadin **Platform** releases (e.g., Vaadin 14, 23, 24) and also has independent Flow GitHub releases (nightlies, alphas for Vaadin 25). Use platform release notes for the combined picture. ([GitHub][2])

### Vaadin 14 (LTS) — (classic LTS series)

* **When / context:** Long term support for Java 8 users; last non-Jakarta LTS before the newer release model.
* **Major changes:** Stable server-side bootstrapping and Flow 14 API; incremental component improvements and bugfixes. (Recommended if you need Java 8 / legacy compatibility.) ([Vaadin][3])

### Vaadin 23 → 24 (modernized, client-side bootstrapping + Jakarta)

* **Vaadin 23 → 24** introduced client-side bootstrapping (moving some annotations and app shell responsibilities) and aligned the stack with newer servlet/Java requirements. Vaadin 24 became the primary stable stream in the new simplified release model. Changes included modernization of bootstrapping (AppShellConfigurator), tooling updates, and new component versions. See upgrade docs for recommended code changes. ([Vaadin][4])

### Vaadin 24.x (current stable family; LTS for 24.x variants)

* Ongoing 24.x maintenance releases add Flow improvements, component updates, tooling refinements, and design system features. Example: 24.7/24.9 maintenance releases continue improving Flow plus Hilla/TypeScript tooling. Check blog/release posts for specific minor changes. ([GitHub][2])

### Vaadin 25 (developer channel / alphas)

* **Status:** Vaadin Flow 25 appears in alpha / pre-release on GitHub; these releases iterate API changes and new features (e.g., experimental theme or component changes) before the stable 25 platform. Use GitHub releases to track breaking changes and migration notes. ([GitHub][5])

> If you need a strict, version-by-version diff for *every* Flow release, the canonical resource is the **Flow GitHub releases** (tags) and the Vaadin Platform release notes — I included both sources above. For implementation planning, prioritise the platform LTS notes (14/24) and GitHub releases for alpha/beta work. ([GitHub][5])

---

## 2) Design & architecture (how Flow works, recommended architecture patterns)

### Core runtime model

* **Server-driven UI**: UI classes (Views / Components) are Java objects on the server. Vaadin serializes a component tree to the browser and updates it incrementally over a WebSocket or HTTP channel. Application state and UI event handling remain server-side. This gives safety (no client-exposed internals) and simplifies Java devs’ work. ([Vaadin][1])

### Architectural patterns supported / suggested

* **Not prescriptive MVC/MVVM strictly**: Flow is component-based and doesn’t enforce a single architectural pattern. In practice you’ll typically implement a **layered architecture**:

  * **View layer**: Vaadin Flow Views and Components (server-side UI).
  * **Service layer**: Spring services / business logic.
  * **Persistence layer**: Repositories (Spring Data / JPA).
  * **API layer** (optional): GraphQL or REST for integration / microservices.
* **Common patterns**:

  * **MVC-like**: Views (Vaadin) → Controllers / Services → Repositories.
  * **MVVM-ish**: Use binder / data binding to separate data models from UI components (Vaadin `Binder` helps with two-way binding & validation).
  * **Microservices**: Vaadin apps usually sit at the edge (server-side UI) and call microservices / GraphQL for data aggregation (Vaadin itself is not microservices framework but coexists with microservices). Vaadin recommends using GraphQL / REST for backend integrations to scale and decouple business logic. ([Vaadin][1])

### Security considerations

* Because state & logic are on the server, Vaadin Flow apps have a smaller browser attack surface; still follow server-side validation and standard auth (Spring Security). See Vaadin docs on security architecture. ([Vaadin][6])

---

## 3) Implementation guide — quick start, Spring Boot integration, example view, lifecycle

### Quick start (Maven + Spring Boot)

1. Create a Spring Boot project (Java 17+ for modern platform; adjust for LTS requirements).
2. Add Vaadin Spring Boot starter dependency (platform aligned to chosen Vaadin version). Example `pom.xml` snippet (conceptual):

```xml
<dependencyManagement>
  <!-- Vaadin platform BOM -->
</dependencyManagement>

<dependencies>
  <dependency>
    <groupId>com.vaadin</groupId>
    <artifactId>vaadin-spring-boot-starter</artifactId>
    <version>24.x.y</version>  <!-- pick platform version -->
  </dependency>
</dependencies>
```

(Use Vaadin start or the official docs to generate a bootstrapped project.) ([Vaadin][1])

### Example Flow View (Hello button)

```java
@Route("")                 // root view
public class MainView extends VerticalLayout {

    public MainView() {
        Button btn = new Button("Say hello", e -> Notification.show("Hello from Vaadin Flow"));
        add(btn);
    }
}
```

* `@Route` registers the view; the UI is server-driven and synchronized to client. ([Vaadin][7])

### Data binding with `Binder`

* Use `Binder<T>` to bind form fields to a Java bean, include validation, and commit data to service layer.

```java
Binder<Person> binder = new Binder<>(Person.class);
TextField name = new TextField("Name");
binder.bind(name, Person::getName, Person::setName);
```

### Lifecycle / Push

* Flow supports server push via WebSockets (enabling server → client updates). You can enable `@Push` and use `UI.access()` for thread-safe UI updates.

---

## 4) UI components — categorized catalog (Flow components)

Vaadin exposes a large set of components. Below are categories and the most commonly used components in each category (Flow wrappers available for these Web Components). For the authoritative and exhaustive list, see Vaadin Components docs. ([Vaadin][8])

### Layouts / Structure

* `VerticalLayout`, `HorizontalLayout`
* `FlexLayout` (flexbox layout)
* `Div` (generic container)
* `FormLayout`
* `AppLayout` (header + drawer)
* `SplitterLayout`, `Tabs`, `Accordion`
* `DrawerToggle`, `MenuBar`, `ContextMenu`

### Data display / Grids / Lists

* `Grid` (data grid with sorting, filtering, lazy loading, item details, inline editing)
* `ListBox`
* `TreeGrid`

### Inputs / Form controls

* `TextField`, `TextArea`
* `NumberField`, `IntegerField`
* `DatePicker`, `DateTimePicker`
* `ComboBox`, `MultiSelectComboBox`
* `Checkbox`, `RadioButtonGroup`
* `Select`
* `Upload`

### Navigation / Routing components

* `Tabs`, `RouterLink`, `AppLayout`, `DrawerToggle`

### Feedback / Overlay / Dialogs

* `Dialog`, `Notification`, `ProgressBar`, `Tooltip` (via addon)

### Media / Visuals / Icons

* `Icon`, `Avatar`, `Image`, `Chart` (commercial), `TimePicker` etc.

### Advanced / Enterprise components (some are part of commercial add-ons)

* Spreadsheet, Rich text editor, TreeTable, Advanced charts (Vaadin Charts is commercial), PDF viewer.

> **Grid** is heavily featured (sorting, lazy loading, pagination, renderers, selection, drag & drop, inline editing) and often the central complex component in data apps. ([Vaadin][9])

---

## 5) Styling & attribute classes — Flow API examples

Vaadin Flow exposes CSS styling helpers and several layout-specific enums/classes. Examples:

### FlexLayout + `FlexDirection`

* `FlexLayout` is a Java wrapper around a flexbox container. Use `FlexLayout.FlexDirection` to set orientation:

```java
FlexLayout layout = new FlexLayout();
layout.setFlexDirection(FlexLayout.FlexDirection.COLUMN);
```

There’s also `Style.FlexDirection` enum available in the Flow DOM API. See the API docs for the exact enum names. ([Vaadin][10])

### Inline style editing (component.getElement().getStyle())

```java
button.getElement().getStyle().set("margin", "10px");
```

### CSS / Theming

* Vaadin supports theming using CSS and the Design System. For app shell changes (PWA, meta), move to `AppShellConfigurator` in newer versions. You can also create theme overlays and use CSS variables with the design system. See theming docs for details. ([Vaadin][4])

---

## 6) Querying data — databases (JPA / Spring Data) and GraphQL

### A — Database access (Spring Data JPA + Vaadin Flow)

* Pattern: Use **Spring Data repositories** + services, and call those services from Vaadin views. Vaadin docs include a tutorial showing `JpaRepository` usage, `@Query`, and integration into the view via services. Typical flow:

1. **Entity**:

```java
@Entity
public class Person { @Id Long id; String firstName; String lastName; /* getters/setters */ }
```

2. **Repository**:

```java
public interface PersonRepository extends JpaRepository<Person, Long> {
    List<Person> findByLastNameIgnoreCase(String lastName);
}
```

3. **Service**:

```java
@Service
public class PersonService {
    @Autowired PersonRepository repo;
    public List<Person> findAll() { return repo.findAll(); }
}
```

4. **View**:

```java
Grid<Person> grid = new Grid<>(Person.class);
grid.setItems(personService.findAll());
add(grid);
```

Vaadin docs provide a step-by-step tutorial for database access with Flow and Spring Boot. Use `Binder` for forms and transactions in the service layer as needed. ([Vaadin][11])

### B — GraphQL integration (Vaadin client/server calling GraphQL)

* **Approach 1 — Server side fetch** (recommended for server-driven apps): Vaadin Flow server classes call GraphQL endpoints (using `graphql-java`, `Spring GraphQL`, or an HTTP GraphQL client). The view gets DTOs from your service; UI stays server-side. Benefits: centralized security, fewer CORS / auth issues, caching. See Vaadin blog recommending GraphQL at the API gateway level for UI consumption. ([Vaadin][12])

* **Approach 2 — Client side (Fusion / TS) direct GraphQL calls**: If using a client-side approach or Hilla (TypeScript endpoints), you may call GraphQL directly from the browser. For Flow (server UI) this is less common; server side calls are easier to manage.

**Example (server-side using Spring GraphQL / WebClient):**

```java
// pseudo-code: use WebClient or GraphQL client to POST { query: "...", variables: {...} }
GraphQLResponse resp = webClient.post()
    .uri(graphqlUrl)
    .bodyValue(requestPayload)
    .retrieve()
    .bodyToMono(GraphQLResponse.class)
    .block();
```

Then convert response data into view models for `Grid` / forms.

**GraphQL best practice:** use GraphQL as an aggregator/API gateway so the Vaadin app receives exactly the shape it needs rather than multiple REST calls. ([Vaadin][12])

---

## 7) Other relevant Flow APIs & tooling

* **TypeScript generator**: If you expose endpoints to TypeScript or Hilla, Vaadin can generate typed clients. (Useful when mixing client-side UIs.) ([Vaadin][1])
* **Designer**: visual drag-and-drop UI editor (IDE plugins).
* **TestBench**: commercial UI test automation tool (Selenium based).
* **Push**: `@Push` annotation enables server push (WebSocket) for real-time UIs.

---

## 8) Best practices and pitfalls (implementation advice)

### Best practices

* **Keep heavy processing off the UI thread** — use services / async processing; use `UI.access()` to update UI from background threads.
* **Reuse connections / channels**: If calling remote APIs (DB/GraphQL), use connection pooling and reactive clients when possible.
* **Prefer server-side GraphQL calls** for Flow apps to centralize auth/caching. ([Vaadin][12])
* **Use `Binder` for complex forms**; it centralizes binding and validation.
* **Use `Grid` lazy loading** (`DataProvider`) for large datasets to avoid memory blowup. ([Vaadin][9])
* **Make queues/limits**: don’t let queues or live data sets accumulate without bounds — prefer pagination / lazy fetching.

### Common pitfalls

* **Treating Vaadin like a pure client framework**: remember it is server-driven — pushing large amounts of UI state to the client can cause scalability issues. ([Vaadin][1])
* **Forgetting to tune `Grid` / pagination** → memory and responsiveness problems. ([Vaadin][9])
* **Improper theming / migration mistakes**: when upgrading between major versions watch bootstrap and `AppShellConfigurator` changes (Vaadin 23→23+ migration notes). ([Vaadin][4])
* **Expecting identical patterns to client SPA frameworks**: Vaadin hides HTML/JS but you still need to know web constraints (network latency, push scalability).

---

## 9) Quick recipe — create a Flow app that reads DB + GraphQL and shows a Grid

1. **Create Spring Boot + Vaadin starter** (platform 24.x).
2. **Add Spring Data JPA** + DB driver (Postgres) and `application.properties` datasource.
3. **Create Entities + Repositories** for directly owned data.
4. **Create a service** that (a) fetches from JPA and (b) calls GraphQL aggregator for remote data (use WebClient / Spring GraphQL).
5. **Create a Flow view** with a `Grid` and set `DataProvider` that queries the service lazily. Use `Binder` for editing.
6. **Enable security** using Spring Security; protect GraphQL credentials on server side.
7. **Test & profile**: measure response times (server push and heavy grids can cause concurrent sessions to grow memory usage).

---

## 10) Useful links / authoritative sources (quick jump)

* **How Vaadin Flow works** (Flow docs) — overview & guides. ([Vaadin][1])
* **Vaadin Components (catalog + categories)** — components list & docs. ([Vaadin][8])
* **Grid component page** (features like lazy loading, editing). ([Vaadin][9])
* **FlexLayout & FlexDirection API** (styling enums). ([Vaadin][10])
* **Database access tutorial (Flow + Spring JPA)**. ([Vaadin][11])
* **Vaadin blog on consuming GraphQL** (recommended pattern for GraphQL with Vaadin). ([Vaadin][12])
* **Vaadin Flow GitHub releases** (full per-release changelogs). ([GitHub][5])

[1]: https://vaadin.com/docs/latest/flow/what-is-flow?utm_source=chatgpt.com "How Vaadin Flow works"
[2]: https://github.com/vaadin/platform/releases?utm_source=chatgpt.com "Releases · vaadin/platform"
[3]: https://vaadin.com/roadmap?utm_source=chatgpt.com "Vaadin releases & roadmap"
[4]: https://vaadin.com/docs/v23/upgrading/recommended-changes?utm_source=chatgpt.com "Recommended Changes | Upgrading | Vaadin Docs"
[5]: https://github.com/vaadin/flow/releases?utm_source=chatgpt.com "Releases · vaadin/flow"
[6]: https://vaadin.com/docs/latest/flow/security/advanced-topics/architecture?utm_source=chatgpt.com "Security architecture best practices for ..."
[7]: https://vaadin.com/docs/v14/flow/tutorial/components-and-layouts?utm_source=chatgpt.com "Creating a Vaadin Flow View With Components"
[8]: https://vaadin.com/docs/latest/components?utm_source=chatgpt.com "How to use Components"
[9]: https://vaadin.com/docs/latest/components/grid?utm_source=chatgpt.com "Grid component"
[10]: https://vaadin.com/api/platform/current/com/vaadin/flow/component/orderedlayout/FlexLayout.html?utm_source=chatgpt.com "Class FlexLayout"
[11]: https://vaadin.com/docs/v23/tutorial/database-access?utm_source=chatgpt.com "Tutorial: Accessing the database from a Vaadin Flow view"
[12]: https://vaadin.com/blog/consuming-graphql-apis-from-java-applications?utm_source=chatgpt.com "Consuming GraphQL APIs from Java applications"
