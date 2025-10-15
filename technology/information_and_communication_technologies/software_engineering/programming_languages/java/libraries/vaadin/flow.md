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


## Notes from courses

> Note: Hilla is TS based development, as compared to Flow, which is Java Based.

A Simple hello World Program in Vaadin Flow:

```java
@Route(value = "")
public class helloWorldView extends VerticalLayout{
    public HelloWorldView(){
        Button sayHello = new Button("Say Hello");
        sayHello.addClickListener(e -> {
            Notification.show("Hello World!");
        });
        add(sayHello);
    }
}
```


Can be run via:

- Running main method of `Application.java`
- `mvn spring-boot:run`

### Components

- Form Inputs
    - Checkbox
    - Combo Box
    - Text Field
    - Date Picker
    - Password Field
    - Upload
    - Email Field
    - Custom field
    - Date Time Picker
    - List Box
    - Number Field
    - Mult-Select combo Box
    - Rich Text Editor
    - Select
    - Text Area
    - Time Picker
- Data Visualizations and interaction
    - Button
    - Dialog
    - Grid
    - Icons(600 icons)
    - Progress Bars
    - Tabs
    - Accordion
    - Avatar
    - Badge
    - Charts
    - Confirm Dialog
    - Context Menu
    - Cookie Consent
    - CRUD
    - Details
    - Grid Pro
    - Map
    - Menu Bar
    - Message List
    - Notification
    - Scroll Bar
    - Virtual List
- Layouts
    - Basic
    - App
    - Board
    - Form
    - Login
    - Split
- HTML Components
    - HTML5 components


### Layouts

Example code for Layouts:

```java
HorizontalLayout layout = new HorizontalLayout();
// or VerticalLayout

layout.add(new DatePicker("DatePicker"));
layout.add(new TextField("TextField"));
layout.add(new ComboBox("ComboBox"));
```

Padding can be set via:

`layout.setPadding(boolean)`

Margins can be set via similar method. `layout.setMethod(boolean)`

Theming controls the margins and padding, to ensure consistent theming.

Default, both are enabled.

#### FlexBox and FlexLayouts

Main and Cross Axes for FlexBoxes are the components render axis, and the axis perpendicular to it respectively.

Flex direction can be set via:

`flexLayout.setFlexDirection(FlexDirection.[What we need])`

Alignment can be set by `justify-content`.

- flex-start
- flex-end
- center
- space-between
- space-around
- space-evenly

Set via `layout.setJustifyContentMode(FlexComponent.JustifyContentMode.[Whichever is required])`.

Alignment is set by `align-items`, this is set to the parent, and is applied to it's children as well.

Set via `layout.setAlignItems(FlexComponent.Alignment.[Some option])`.

There is a `LumoUtility` for providing multiple options.

For sizing, there are some convenient functions available.

When sizing, take into consideration `flex-shrink` and `flex-grow`.

`layout.setFlexGrow(1, item)` for setting flex grow/shrink properties.

Wrapping items can be done via `layout.setFlexWrap(FlexLayout.FlexWrap.[Some Option])`.

#### Responsiveness

Example code for setting responsive steps:

```java
fl.setResponsiveSteps(
    new ResponsiveStep("0", 1, LabelsPosition.TOP),
    new ResponsiveStep("20em", 1),
    new ResponsiveStep("50em", 2)
);
```

`setColspan` can be used a field to cover multiple columns.

#### Board Layout

> Commercial Component. Requires License

Example code:

```java
Board board = new Board();
Component a = createComponent("A");
Component b = createComponent("B");
Component c = createComponent("C");
Component d = createComponent("D");

Row row1 = board.addRow(a, b);// can contain upto 4 components
row1.setComponentSpan(a, 2);//for covering multiple columns

board.addRow(row1);
```

#### AppLayout

Contains 3 sections:

- Nav Bar
- Drawer
- Content

### Forms

`Field` is a Vaadin component that holds a value.

Example:

`class TextField extends Component implements HasValue`

What is `HasValue`?

This indicates that the field holds a value.

Properties are used for getting and setting the values.

Example:

```java
public class User extends AbstractEntity{
    private String email;

    public String getEmail(){return email;}
    public void setEmail(String email){this.email = email;}
}
```

All fields implement `HasValue<E, V>`, where `V` is the data type, and `E` is the value change event.

3 functions provided:

- `getValue`
- `setValue`
- `addValueChangeListener`

#### Binder

`Binder` is used for data binding.

- handles data conversions and validation
- like `HasValue`, Binder is always typed to the Backing Bean.

Example:

- `Binder<person> binder = new Binder<>()` - doesn't support binding with property names
- `Binder<Person> biner = new Binder<>(Person.class);` - supports binding with with property names

Example:

```java
Binder<Person> binder = new Binder<>();

Textfield titleField = new TextField();
IntegerField brithYearField = new IntegerField();

binder.forField(titleField).bind(Person::getTitle, Person::setTitle);
binder.forField(brithYearField);
```

Example, bindings with property name:

```java
Binder<Person> binder = new Binder<>(Person.class);

Textfield titleField = new TextField();

// can use the shorthand mechanism, for cases without extra config
binder.bind(titleField, Person::getTitle, Person::setTitle);

// or with property name
binder.bind(titleField, "title");

// Also can use lambda expressions, or a ValueProvider/Setter based anonymous class.
```

Automated Binding example, for an entire form:

```java
public class MyForm{

    private TextField name = new TextField();

    @PropertyId("email")
    private TextField emailField = new TextField();

    public MyForm() {
        Binder<Person> binder = new Binder<>(Person.class);
        binder.bindInstanceFields(this);
    }
}
```

> Note: No null-safe implementation as Vaadin doesn't know how it needs to be handled, as it depends on business logic

`Binder` has a `readBean`, to read values from a bean to an input form.
It has the `writeBean` to write the values to a bean.
Also, has `writeBeanAsDraft`, write even without validations passing.

Resetting can be done, via calling the `readBean`, prior to setting properties via `writeBean`.

> `Validator` can be used with `Binder` for adding validations

`BeanValidationBinder` can also be used.

#### Converter API

For custom data types being used in a POJO with Binder, you will require a coverter(or even, when string is received for Integer).
Binders have a `withConverter` function wrapper for converting.

There are some Automatic conversion features as well, which utilizes the internal classes, if the conversion isn't explicitly mentioned.

#### Custom Field

We can use custom fields, and leverage third party library components. To do this we do the following:

- Use `npm i --save @somecompany/library`. This adds the library to the `node_modules` list
- Then create a custom class. Example below, for using `@polymer/paper-toggle-button`

```java
@JsModule("@polymer/paper-toggle-button/paper-toggle-button.js")
@Tag("paper-toggle-button")
public class ToggleButton extends AbstractSinglePropertyField<ToggleButton, Boolean>{

    public ToggleButton(){
        super("checked", false, false);// property name, default value, accept null values
    }
}
```

`CustomField` is a wrapper of components to be used as a regular field. 
They have a validation error message and a required indicator. This is another way of implementing 
components from external libraries.

Example:

```java
public class MyCustomField extends CustomField<Boolean> {
    private ToggleButton tb = new ToggleButton();
    public MyCustomField(){
        add(tb);
    }

    @Override
    protected Boolean generateModelValue(){
        return tb.getValue();
    }

    @Override
    protected void setPresentationValue(Boolean newValue){
        tb.setValue(newValue);
    }
}
```

You can also use some of the other components with `CustomField` to add more functionalities,
for instead creating the `UploadField` such that it works with `Binder`.

### Grid Components

`Grid<Person> grid = new Grid<>(Person.class);`

This automatically add the columns automatically.

Columns can be added as:

`grid.addColumn(Person::getFirstName)` if, no class reference is passed.

There are multiple renderes that Vaadin has, that can be used for rendering column values:

- TextRenderer - default
- ComponentRenderer - renders using a Vaadin component
- LocalDateRenderer
- NativeButtonRenderer
- IconRenderer
- LitRenderer - provides option for rendering HTML with properties
- ColumnPathRenderer
- EditorRenderer

You can add a different header name, via:

`grid.addColumn(Person::getLastName).setHeader("Last Name");`

Footers also can be added via:

`grid.addColumn(Person::getLastName).setHeader("Total: " + personList.size() +" people");`

Sorting can be enabled via:

`Column::setSortable(Boolean)`.

Comparators can be set by:

```java
Grid<Person> grid = new Grid<>(Person.class);

grid.getColumnByKey("firstName").setComparator(Comparator.comparing(Person::getAge));
```

> This only applies to in-memory data

Multi sorting can be done by:

`grid.setMultiSort(true)`.

There are some prioritizations available.

To set all rows as visible:

`grid.setAllRowsVisible(true)`. This makes all rows visible, without a scroll bar.

Selection modes:

- Single select: `grid.setSelectionMode(Grid.SelectionMode.SINGLE)`
- Multi select: `grid.setSelectionMode(Grid.SelectionMode.MULTI)`

Programatical selection:

```java
grid.select();
grid.asSingleSelect().asValue()
grid.asMultiSelect().asValue()
```

To obtain the selected values we can use `grid.getSelectedItems()`. This provides a `Set<T>`, for us to use.

To use with `Binder` as a `Field`:

```java
SingleSelect<Grid<Person>, Person> selected = grid.asSingleSelect(); 
// or
// MultiSelect<Grid<Person>, Person> selected = grid.asMultiSelect();

binder.forField(selected).bind(...);
```

Click listener implementation:

```java
grid.addItemClickListener(e -> {
    Grid.Column<Person> column = e.getColumn(); // to get column
    Person item = e.getItem();// to get the row
});

grid.addItemDoubleClickListener(); // for using the double click event.
```

ContextMenu and ToolTips are also enabled by the Grid component.

Item details can also be produced via `grid.setItemdetailsRenderer`.

There are multiple themes for grid. This can be used with the enum `GridVariant`.

There is a special grid called `TreeGrid`. This allows setting children for each item, 
but otherwise behaves exactly like `Grid`.

In-line editing can also be achieved in the Grid component. This can be done via `grid.getEditor`.
The component for editing needs to be provided by the following:

```java
TextField field = new TextField();
nameColumn.setEditorComponent(field);

Checkbox checkbox = new CheckBox();
subscriberColumn.setEditorComponent(checkbox);

// bind the data
Binder<Person> binder = new Binder<>(Person.class);
grid.getEditor().setBinder(binder);
binder.bind(field, "firstName");
binder.bind(checkbox, "subscriber");
```

For save/cancel functionality `grid.getEditor().setBuffered(true)`.

#### DataProviders - advanced mechanism for providing data

When `grid.setItems(items)` is called, it instead calls to `grid.setItems(DataProvider.ofCollection(items))`.

The `DataProvider` has in-memory and lazy loading variants.

It provides the ability to sort a `Grid` and a `Chart` using the same `DataProvider`.

Example to compare using the bean:

```java
// override previously set comparator
InMemoryDataProvider#setSortComparator(SerializableComparator<T> comparator);
// or adding a new one
InMemoryDataProvider#addSortComparator(SerializableComparator<T> comparator);

// This is used like the following
dataProvider.setSortComparator(Comparator.comparing(Person::getName)::compare);
// The ::compare is required to obtain a SerializableComparator
```

`DataProvider` also provides the ability to set sort orders using
- `setSortOrder(ValueProvider<T, V>, SortDirection)`
- `addSortOrder(ValueProvider<T, V>, SortDirection)`

`SortDirection` is an enum.

`DataView` is another mechanism to manipulate data in a `Grid`.
`Grid.setItems` methods all return an implementation of the DataView interface.
The `DataView` allows you to set an identifier provider, do the `refreshItem`/`refreshAll` requests
and  fetch an item at a specific index. Concrete implementation classes such as `GridLazyDataView`
and `GridListDataView` offer more methods for accessing and modifying the data.

Example implementation:

```java
List<Person> allPersons = repo.findAll();
GridListDataView<Person> gridDataView = grid.setItems(allPersons);

Button selectNext = new Button("Next", e -> {
    grid.asSingleSelect().getOptionalValue().ifPresent(p -> {
        gridDataView.getNextItem(p).ifPresent(next -> grid.select(next));
    });
});
```

#### LazyProvider

A `Query` object is provided with information needed for lazy loading. The class looks as the following:


```java
public class Query<VALUETYPE, FILTERTYPE>{
    public int getLimit();
    public int getOffset();
    public List<QuerySortOrder> getSortOrders();
    public Optional<FILTERTYPE> getFilter();
}
```

A `FetchCallback` object, is used for lazy loading, and is passed instead of data to the `DataProvider`
directly. This allows for fetching a stream of items based on a query. It allows for keeping the memory
free.

The API looks like the following:

```java
public interface FetchCallback<VALUETYPE, FILTERTYPE> {
    Stream<VALUETYPE> fetch(Query<VALUETYPE, FITLERTYPE> query);
}

// Example usage:
FetchCallback<Person, Void> fetchCallback = query -> service.getPersons(query.getOffset(), query.getLimit());
```

There is another API called `CountCallback`, which is to be used in-tandem with `FetchCallback`.

This allows counting of number of items in the backend, and is required for being able to render the scrollbar properly.

The API looks similar to `FetchCallback`:

```java
public interface FetchCallback<VALUETYPE, FILTERTYPE> extends Serializable{
    int count(Query<VALUETYPE, FITLERTYPE> query);
}

// Example usage:
CountCallback<Person, Void> count = query -> backend.countPersons();
```

To create a `DataProvider` implementation, we extend the `AbstractBackendDataProvider`,
overriding the signatures:
- `protected Stream<Person> fetchFromBackEnd(Query<T, Q>)`
- `protected int sizeInBackEnd(Query<T, Q>)`

Lazy data loading can also be done compactly via:

```java
DataProvider.fromCallbacks(
    FetchCallback<T, Void> fetchCallback,
    CountCallback<T, Void> countCallback
    );

// Example
CallbackDataProvider<Person, Void> dataProvider = DataProvider.fromCallbacks(
    query -> backend.getPersons(query.getOffset(), query.getLimits()),
    query -> backend.countPersons()
);
```

Filtering can be done via using `DataProvider.fromFilteringCallbacks`.

Sorting is done by the backend, and hence only `setSortProperty` allows for us to do that.

Paging, has a few helper functions such as:

- `VaadinSpringDataHelpers.fromPagingRepository(personRepo)`
- `query.getPage()`, `query.getPageSize()`

For Hierarchical Lazy Data, we have the `AbstractBackEndHierarchicalDataProvider<T, Q>`,
where the following needs to be overridden:

- `protected Stream<T> fetchChildrenFromBackEnd(HierarchicalQuery<T, Q>)`
- `public int getChildCount(HierarchicalQuery<T, Q>)`
- `public boolean hasChildren(T item)`

`HierarchicalQuery` is similar to `Query`, but has an extra method called `public T getParent()`.

Grid Pro allows inline editing, with some shortcuts to edit more efficiently.

### Routing

- `@Route` annotation for specifying routing path
- `@RouteAlias` can be used if the same view has to be used for multiple paths
- `HasUrlParameter` interface to work with path params, but using the parameter becomes required.
- `@OptionalParameter` for specifying that the parameter is optional
- `@WildcardParameter` for specifying type of parameter
- Most specific path is matched.
- Dynamic routes are of 2 types
    - Session based route(imports application scope routes)
        - `RouteConfiguration.forSessionScope()`
        - Use `.getUrl(SomeComponent.class)` on this object to obtain the dynamic URL to the component
        - This can work with most components, but there is `HasUrlParameter` interface, that can be used to create paths for a component
    - Application scope routes
        - `RouteConfiguration.forApplicationScope()`
- To get where application is hosted `VaadinServletRequest.getCurrent().getRequestURL()`
- Routing does not impact query parameters.
- `@PageTitle` can be used to change the static page titles
- `RouterLink` to provide links to different views, while also passing params.
- `button.getUI().ifPresent(ui -> ui.navigate(SomeView.class))` allows for programmatically navigating
- When only a part of the UI is to be updated, specify a parent layout when specifying `@Route` for a component
- `@Route(value="company", layout=MainLayout.class)` specifies, that on `/company` redirect to this component, with `MainLayout` as the parent.
- Parent Layouts can implement the RouterLayout.
- Nesting  can be done in various ways, but in general, every end node should sepcify a parent layout, and every parent layout should implement `RouterLayout`.
- Navigation Lifecycle has 3 events that are fired and can be acted upon
    - BeforeEnterEvent can be acted on by BeforeEnterObserver
        - Check Login
        - Handle errors
        - Typically useful for authenticated page visits
    - BeforeLeaveEvent can be acted on by BeforeLeaveObserver
        - Typically for cleaning up views
        - Or for confirmation with the user, if the state of a submission needs to be maintained
    - AfterNvigationEvent can be acted on by AfterNavigationObserver
        - This is fired when navigation happens, and there are no further redirects
    - Series of events: `HasUrlParameter -> BeforeEnter -> Attached -> AfterNavigation -> ... -> BeforeLeave`

### Themeing

- Order of styling techniques to try should be the following:
    - Theme variants
    - Lumo CSS variables customization
    - Styling using component parts and state selectors
    - Applying styles to elements using `LumoUtility` predefined classes
    - Styling using custom CSS classes and variables(`addClassName(s)()` method)
    - Styling using directly setting style on an element(`getStyle().set()` method)
- Vaadin provides an official Figma Library
- Theme Variants
    - Primary
    - Secondary
    - Tertiary
    - Large
    - Normal
    - Small
- CSS variables:
    - Defining: `--app-font-color : #fcf`
    - using: `color: var(--app-font-color)`
    - This can be used in the CSS files
- There are some Lumo Variables to use, Ex: `--lumo-border-radius`. Refer [Lumo Style Properties](https://vaadin.com/docs/latest/styling/lumo/lumo-style-properties)
- A part name can be mentioned to customize an element(this is standard HTML). This is core for the "Shadow DOM"
- `@Theme` annotation allows for defining the component theme
- `@NoTheme` annotation allows stripping the entire theme.
- folder structure for custom theme(to be used with `@Theme`):
    - `frontend -> themes -> my-theme -> [theme.json, styles.css]`
- Lazy loading of stylesheets can be done using `@StyleSheet` to load in CSS after page is loaded(as opposed to `@import` in CSS)
- In Grids, Part Name Generators can be used for custom styling
    - Ex: `grid.setPartNameGenerator(product -> product.isAvailable()? "": "unavailable")`



### Exercise

Create a data model explorer.

- Download some data sets from Kaggle
- Create a Vaadin project
- Use SQLite as the DB
- Implement a Signup & Login logic
- Implement a theme switcher
- Create views for each data set
- Use `Grid` and `HierarchicalGrid` as required
- Implement paging for loading/viewing the data sets
- Vaadin provides a `RouterLink` component that allows users to navigate to different views

For generating URLs programmatically, we can use `RouteConfiguration.forSessionScope().getUrl(PathComponent.class)`.

However, this only provides the current page. To have the full URL, we use `VaadinServletRequest.getCurrent().getRequestURL()`.

Passing data between views in Java:
- Call the following on an event `getUI().navigate(UserEditor.class).ifPresent(editor -> editor.editUser(user))`
