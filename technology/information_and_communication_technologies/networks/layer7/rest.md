# Representational State Transfer(REST)

## 1. Introduction

**REST**, short for **Representational State Transfer**, is an architectural style for distributed systems.

It was introduced by Roy T. Fielding in his 2000 doctoral dissertation:

> *Architectural Styles and the Design of Network-based Software Architectures*

REST was developed as a way to describe and reason about the architectural constraints that make the World Wide Web scalable, evolvable, and suitable for distributed hypermedia systems. Fielding describes REST as a set of architectural constraints emphasizing scalability, generality of interfaces, independent deployment, and the effective use of intermediaries.

The most important distinction to establish at the beginning is:

```text
REST ≠ HTTP
```

More precisely:

```text
REST
 │
 └── Architectural style

HTTP
 │
 └── Application-layer protocol
```

HTTP is one of the most important protocol implementations capable of expressing REST-style interactions, and the HTTP architecture itself was influenced by REST's constraints. However, REST is not a replacement for HTTP and is not simply a set of HTTP methods.

A useful mental model is:

```text
REST
 │
 │ defines architectural constraints
 ▼
Distributed application architecture
 │
 │ may use
 ▼
HTTP
 │
 ▼
HTTP/1.1 / HTTP/2 / HTTP/3
 │
 ▼
TCP / QUIC
 │
 ▼
IP
```

---

# 2. What Does "Representational State Transfer" Mean?

The name is deliberately precise.

Consider a resource:

```text
https://example.com/users/123
```

The resource itself is not necessarily transferred.

Instead, the server transfers a **representation** of the resource's state.

For example:

```json
{
  "id": 123,
  "name": "Alice",
  "email": "alice@example.com"
}
```

This JSON document is a representation.

The resource may exist as:

```text
Database row
        ↓
Domain object
        ↓
Resource
        ↓
JSON representation
        ↓
HTTP response
```

The client receives the representation, not the server's internal object or database row.

This separation is fundamental.

RFC 9110 uses closely related terminology: a resource is the target of an HTTP request, while a representation is information intended to reflect a past, current, or desired state of that resource.

---

# 3. REST Is an Architectural Style

An architectural style is a collection of constraints applied to a system's architecture.

REST is therefore closer to:

```text
"Rules for structuring a distributed system"
```

than:

```text
"Format of packets sent over a network"
```

For comparison:

| Concept  | What it is                 |
| -------- | -------------------------- |
| Ethernet | Link-layer protocol        |
| IP       | Network-layer protocol     |
| TCP      | Transport protocol         |
| TLS      | Security protocol          |
| HTTP     | Application-layer protocol |
| REST     | Architectural style        |
| JSON     | Data representation format |
| OpenAPI  | API description format     |

REST does not define:

* TCP packets;
* TLS handshakes;
* HTTP headers;
* JSON syntax;
* IP addresses;
* TCP ports.

Instead, REST constrains how components interact.

---

# 4. REST and OSI Layer 7

REST is normally discussed at the **application architecture/application-layer level**.

The OSI model is:

```text
7  Application
6  Presentation
5  Session
4  Transport
3  Network
2  Data Link
1  Physical
```

REST concerns the semantics and architecture of distributed application interactions.

Therefore it belongs conceptually at:

```text
OSI Layer 7
Application
```

However, there is an important qualification:

> REST is not itself an OSI Layer 7 protocol.

HTTP is an application-layer protocol.

REST is an architectural style that can be realized by application-layer protocols.

A better representation is:

```text
OSI Layer 7
┌──────────────────────────────────────────┐
│ REST architectural constraints           │
│                                          │
│ HTTP                                     │
│ JSON / XML / HTML / other representations│
└──────────────────────────────────────────┘
                     │
OSI Layer 6          │
┌────────────────────▼─────────────────────┐
│ TLS / representation encoding concepts   │
└──────────────────────────────────────────┘
                     │
OSI Layer 4          │
┌────────────────────▼─────────────────────┐
│ TCP / QUIC                               │
└──────────────────────────────────────────┘
                     │
OSI Layer 3          │
┌────────────────────▼─────────────────────┐
│ IP                                       │
└──────────────────────────────────────────┘
```

This is a conceptual mapping rather than a strict statement that modern Internet protocols map one-to-one onto OSI layers.

---

# 5. REST vs HTTP — The Fundamental Difference

This is the most important distinction in this document.

## HTTP answers:

> How are application messages exchanged?

HTTP defines:

* requests;
* responses;
* methods;
* status codes;
* headers;
* representations;
* caching semantics;
* content negotiation;
* message framing;
* connection behavior.

For example:

```http
GET /users/123 HTTP/1.1
Host: example.com
Accept: application/json
```

is an HTTP request.

---

## REST answers:

> How should a distributed application be architected so that interactions remain scalable, loosely coupled, general, and independently evolvable?

REST defines architectural constraints such as:

```text
Client-server separation
Stateless interactions
Cacheability
Uniform interface
Layered system
Code-on-demand (optional)
```

and, within the uniform interface:

```text
Resource identification
Manipulation through representations
Self-descriptive messages
Hypermedia as the engine of application state
```

Therefore:

```text
HTTP:
    Protocol

REST:
    Architectural style
```

---

# 6. HTTP Can Be Used Without REST

This is one of the easiest ways to understand the distinction.

Consider:

```http
POST /executePayment HTTP/1.1
Content-Type: application/json

{
  "account": "123",
  "amount": 1000
}
```

This is completely valid HTTP.

It can be a perfectly legitimate HTTP API.

But whether the overall system satisfies REST's architectural constraints is a separate question.

An RPC-style API might have:

```text
POST /createUser
POST /deleteUser
POST /sendEmail
POST /calculatePrice
POST /executePayment
```

It uses HTTP.

It does not automatically constitute REST.

---

# 7. REST Can Be Expressed Without HTTP

REST is not logically tied to HTTP.

The architectural constraints could theoretically be implemented over another application protocol.

For example:

```text
REST-style architecture
        │
        ├── HTTP
        │
        ├── another application protocol
        │
        └── custom protocol
```

However, HTTP is extraordinarily well suited to REST because HTTP already provides many of the mechanisms needed by REST:

```text
URI
methods
representations
status codes
caching
content negotiation
headers
conditional requests
hyperlinks
```

This is why the overwhelming majority of systems called "REST APIs" use HTTP.

---

# 8. REST Was Derived from the Web Architecture

REST did not originate as a generic CRUD API methodology.

This is a common misconception.

Fielding's work was concerned with the architecture of the Web and with identifying the constraints that enabled the Web to scale across:

```text
billions of resources
millions of clients
many independent organizations
different implementations
intermediaries
untrusted networks
independent software evolution
```

Fielding describes REST as a hybrid architectural style derived from multiple network-based architectural styles and additional constraints defining a uniform connector interface.

Therefore:

```text
REST
    ↓
Web architecture
    ↓
Distributed hypermedia
```

is historically and conceptually more accurate than:

```text
REST
    ↓
CRUD API design
```

---

# 9. The REST Constraints

REST is defined by a set of architectural constraints.

The important ones are:

```text
1. Client-server
2. Stateless
3. Cacheable
4. Uniform interface
5. Layered system
6. Code-on-demand (optional)
```

REST can be understood by progressively applying these constraints.

---

# 10. Client-Server Constraint

REST requires a separation between:

```text
Client
```

and:

```text
Server
```

The client is responsible primarily for:

* user-facing concerns;
* interaction;
* presentation;
* client-side state.

The server is responsible primarily for:

* resource management;
* persistent state;
* business logic;
* data processing.

Conceptually:

```text
Client
 │
 │ request
 ▼
Server
 │
 │ representation
 ▼
Client
```

The client does not need to know how the server stores or processes the resource.

For example:

```text
Client
    │
    │ GET /users/123
    ▼
API server
    │
    ├── PostgreSQL
    ├── Redis
    ├── microservice
    └── filesystem
```

The client only interacts with the server's interface.

---

# 11. Why Client-Server Separation Matters

Without separation, the client might need to understand server internals.

For example:

```text
Client
 │
 ├── knows database schema
 ├── knows database queries
 ├── knows business rules
 └── accesses database directly
```

This creates tight coupling.

REST instead encourages:

```text
Client
 │
 │ standardized interface
 ▼
Server
 │
 └── implementation hidden
```

The server can therefore change:

```text
MySQL
   ↓
PostgreSQL
   ↓
distributed database
```

without necessarily changing the client.

---

# 12. Statelessness

REST requires that each client request contain all information necessary for the server to understand and process it.

The server should not need to depend on hidden client session state stored between requests.

For example:

```http
GET /users/123 HTTP/1.1
Authorization: Bearer abc...
```

The request contains the authentication information necessary to identify the caller.

A subsequent request:

```http
GET /users/456 HTTP/1.1
Authorization: Bearer abc...
```

should be independently understandable.

---

# 13. REST Statelessness Does Not Mean "No State"

This is one of the most important misconceptions.

REST does **not** mean:

> The system contains no state.

A REST system can have enormous amounts of state:

```text
Users
Orders
Payments
Products
Sessions
Files
Messages
```

What REST constrains is the **interaction state between client and server**.

A useful distinction is:

```text
Resource state
    │
    └── Stored by the server

Application state
    │
    └── Progress of the client's interaction

Request state
    │
    └── Information needed to process this request
```

REST requires requests to be self-contained rather than relying on hidden conversational state on the server.

---

# 14. Stateful vs Stateless Interaction

### Stateful interaction

```text
Request 1:
"Start transaction 123"

Server:
"Okay, I'll remember transaction 123."

Request 2:
"Continue"

Server:
"Continue what?"

Server retrieves session state.
```

The meaning of Request 2 depends heavily on server-side conversational state.

---

### Stateless interaction

```text
Request 1:
POST /transactions/123/...

Request 2:
PUT /transactions/123/...
```

Each request identifies the relevant resource and provides the information required for processing.

---

# 15. Why Statelessness Improves Scalability

Consider:

```text
                 Load Balancer
                  /    |    \
                 /     |     \
              Server A Server B Server C
```

With stateless interactions:

```text
Request 1 → Server A
Request 2 → Server C
Request 3 → Server B
```

The servers do not need to share per-client conversational state.

This makes:

* load balancing easier;
* horizontal scaling easier;
* failover easier;
* caching easier;
* deployment simpler.

RFC 9110 similarly emphasizes HTTP's stateless design and notes that statelessness allows implementations to reuse proxied connections and dynamically load-balance requests.

---

# 16. Cacheability

REST requires that responses be implicitly or explicitly cacheable where appropriate.

The purpose is to allow:

```text
Client
   │
   ▼
Cache
   │
   ▼
Server
```

instead of:

```text
Client
   │
   ▼
Server
```

for every request.

This can reduce:

* latency;
* bandwidth;
* server load.

HTTP provides the actual caching mechanisms.

Important HTTP mechanisms include:

```text
Cache-Control
ETag
Last-Modified
Vary
Expires
Age
304 Not Modified
```

REST's constraint says caching should be part of the architecture.

HTTP provides the concrete protocol mechanisms.

---

# 17. REST and HTTP Caching

This is another useful example of the distinction.

REST says:

```text
Responses should be explicitly or implicitly cacheable
where appropriate.
```

HTTP defines:

```http
Cache-Control: max-age=3600
```

and:

```http
ETag: "abc123"
```

Therefore:

```text
REST
 │
 └── Architectural cacheability constraint

HTTP
 │
 └── Concrete caching protocol
```

---

# 18. Uniform Interface

The **uniform interface** is arguably the most important REST constraint.

The purpose is to reduce coupling between components.

Instead of every resource exposing a completely different RPC interface:

```text
GET /getUser
POST /executePayment
POST /deleteUser
POST /calculateInvoice
```

REST encourages a consistent interaction model based around:

```text
Resources
Representations
Standardized operations
Self-descriptive messages
Hypermedia
```

The client interacts with resources through a common interface rather than through resource-specific remote procedures.

---

# 19. Four Parts of the Uniform Interface

Fielding's REST style describes the uniform interface through four important constraints:

1. Identification of resources.
2. Manipulation of resources through representations.
3. Self-descriptive messages.
4. Hypermedia as the engine of application state.

These are central to understanding REST properly.

---

# 20. Resource Identification

Resources are identified independently of their representations.

For example:

```text
https://example.com/users/123
```

identifies a resource.

The resource could be represented as:

```json
{
  "id": 123,
  "name": "Alice"
}
```

or:

```xml
<user>
    <id>123</id>
    <name>Alice</name>
</user>
```

or HTML:

```html
<h1>Alice</h1>
```

The URI identifies the resource.

The representation describes it.

---

# 21. Resource vs Representation

This distinction is fundamental.

Suppose:

```text
Resource:
https://example.com/users/123
```

The resource might internally correspond to:

```text
Database:
users.id = 123
```

The server could produce:

```text
Representation A:
application/json
```

or:

```text
Representation B:
application/xml
```

or:

```text
Representation C:
text/html
```

The resource remains conceptually distinct from the representation.

RFC 9110 explicitly defines a representation as information intended to reflect a past, current, or desired state of a resource.

---

# 22. Why "REST" Contains the Word Representation

Consider:

```text
Resource state
      │
      ▼
Representation
      │
      ▼
HTTP message
      │
      ▼
Network
      │
      ▼
Client
```

The server does not transmit the actual resource.

It transmits information representing its state.

This is the reason for the name:

```text
Representational
       State
       Transfer
```

---

# 23. Manipulation Through Representations

Suppose the resource is:

```text
/users/123
```

The client receives:

```json
{
  "id": 123,
  "name": "Alice",
  "email": "alice@example.com"
}
```

The client wants the name changed to Bob.

It might send:

```http
PUT /users/123 HTTP/1.1
Content-Type: application/json

{
  "id": 123,
  "name": "Bob",
  "email": "alice@example.com"
}
```

The client is not directly modifying:

```text
database.users[123].name
```

It is sending a representation expressing the desired resource state.

HTTP's PUT semantics explicitly define request content as representing the desired state of the target resource after the request is successfully applied.

---

# 24. Self-Descriptive Messages

A REST message should contain enough information for the recipient to understand how to process it without relying on hidden out-of-band assumptions.

For example:

```http
Content-Type: application/json
```

tells the recipient how to interpret the content.

Likewise:

```http
Cache-Control: max-age=3600
```

communicates caching semantics.

And:

```http
Accept: application/json
```

communicates a client's representation preference.

The message should therefore carry its own semantics through standardized protocol metadata and representation formats.

---

# 25. Self-Descriptive Does Not Mean "Human Readable"

A message can be self-descriptive without being human-readable.

For example:

```text
HTTP/2 HEADERS frame
```

is binary.

The important property is that a recipient implementing the protocol can determine how the message should be interpreted.

Therefore:

```text
self-descriptive
```

means:

```text
semantically interpretable from the message and
standardized protocol context
```

not:

```text
easy for a human to read
```

---

# 26. Hypermedia as the Engine of Application State

This is the REST constraint most frequently omitted by systems calling themselves REST APIs.

The principle is commonly abbreviated:

```text
HATEOAS
```

**Hypermedia As The Engine Of Application State**

The client discovers available transitions through representations provided by the server.

For example:

```json
{
  "id": 123,
  "name": "Alice",
  "_links": {
    "self": {
      "href": "/users/123"
    },
    "orders": {
      "href": "/users/123/orders"
    },
    "delete": {
      "href": "/users/123"
    }
  }
}
```

The client does not necessarily need to hard-code:

```text
"/users/{id}/orders"
```

if the server supplies the link.

---

# 27. Why Hypermedia Matters

Consider a workflow:

```text
Order
 ↓
Payment
 ↓
Shipment
 ↓
Delivery
```

The available transitions might depend on the order state.

For example:

```json
{
  "status": "PAID",
  "_links": {
    "self": "/orders/123",
    "shipment": "/orders/123/shipment",
    "cancel": "/orders/123/cancel"
  }
}
```

After shipment:

```json
{
  "status": "SHIPPED",
  "_links": {
    "self": "/orders/123",
    "tracking": "/shipments/456"
  }
}
```

The server controls the available transitions.

The client follows them.

---

# 28. REST and HATEOAS

A system can use:

```text
HTTP
+
JSON
+
GET/POST/PUT/DELETE
```

and still not fully satisfy REST.

If the client must be programmed with every URI and every workflow transition in advance:

```text
GET /users/{id}
POST /users
GET /users/{id}/orders
POST /orders/{id}/cancel
POST /orders/{id}/pay
```

then the system is closer to an HTTP-based API using REST-inspired conventions.

A stronger REST architecture allows representations to communicate available transitions.

---

# 29. REST's Layered System Constraint

REST allows intermediary components.

For example:

```text
Client
   │
   ▼
CDN
   │
   ▼
WAF
   │
   ▼
Load Balancer
   │
   ▼
Reverse Proxy
   │
   ▼
API Gateway
   │
   ▼
Application
```

Each layer only needs to understand the interface appropriate to its role.

The client does not necessarily know whether it is communicating directly with the origin server.

---

# 30. Why Layering Matters

A CDN can cache:

```text
GET /images/logo.png
```

without understanding:

```text
Python
Java
Go
C++
PostgreSQL
```

behind the origin.

Similarly:

```text
WAF
```

can inspect HTTP requests without understanding application internals.

This is one of the major reasons REST emphasizes intermediary-friendly interactions.

---

# 31. Code-on-Demand

REST includes an optional constraint:

> Servers may extend client functionality by transferring executable code.

Historically, JavaScript downloaded by browsers is an obvious example.

Conceptually:

```text
Server
  │
  │ JavaScript
  ▼
Browser
  │
  └── executes code
```

Code-on-demand is optional.

The other REST constraints are the more fundamental architectural requirements.

---

# 32. Complete REST Constraint Model

A simplified representation is:

```text
                         REST
                          │
       ┌──────────────────┼──────────────────┐
       │                  │                  │
       ▼                  ▼                  ▼
Client-Server         Stateless          Cacheable
       │                  │                  │
       └──────────────────┼──────────────────┘
                          │
                          ▼
                  Uniform Interface
                          │
              ┌───────────┼───────────┐
              │           │           │
              ▼           ▼           ▼
        Resource       Resource     Self-
       Identification  Manipulation descriptive
                       through       messages
                    representations
                          │
                          ▼
                    HATEOAS
                          │
                          ▼
                  Layered System
                          │
                          ▼
                Code-on-Demand*
```

`*` Code-on-demand is optional.

---

# 33. REST API vs RESTful API

The terms are often used loosely.

A **REST API** usually means an API designed according to REST principles.

**RESTful** generally means:

> Conforming reasonably closely to REST's architectural constraints.

However, there is no universal certification authority that declares:

```text
"RESTful = yes"
```

or:

```text
"RESTful = no"
```

It is therefore better to evaluate an API against the actual constraints.

---

# 34. CRUD Is Not REST

A common misconception is:

```text
CRUD = REST
```

This is incorrect.

CRUD means:

```text
Create
Read
Update
Delete
```

REST is much broader.

REST is concerned with:

```text
resource identification
uniform interfaces
representations
statelessness
cacheability
self-descriptive messages
hypermedia
layering
client/server separation
```

CRUD is merely one convenient mapping onto HTTP methods.

---

# 35. CRUD-to-HTTP Mapping

A typical API might use:

| CRUD           | HTTP   |
| -------------- | ------ |
| Create         | POST   |
| Read           | GET    |
| Update/replace | PUT    |
| Partial update | PATCH  |
| Delete         | DELETE |

For example:

```http
POST /users
```

```http
GET /users/123
```

```http
PUT /users/123
```

```http
PATCH /users/123
```

```http
DELETE /users/123
```

This is useful, but it is not sufficient to make the API RESTful.

---

# 36. Resource-Oriented vs RPC-Oriented APIs

Consider:

```text
POST /createUser
POST /deleteUser
POST /sendEmail
POST /calculateInvoice
```

This resembles RPC:

```text
POST
 │
 └── invoke procedure
```

A resource-oriented design might instead expose:

```text
/users
/users/123
/orders
/orders/456
```

and use standardized method semantics.

The distinction can be summarized:

```text
RPC:
"What operation should I invoke?"

REST:
"What resource am I interacting with,
and what standardized transition am I requesting?"
```

This is a useful conceptual distinction, although real systems often contain elements of both styles.

---

# 37. HTTP Method Semantics Are Not REST Semantics

HTTP defines:

```text
GET
POST
PUT
DELETE
PATCH
HEAD
OPTIONS
...
```

REST does not invent these methods.

Instead, REST's uniform-interface constraint benefits from using standardized methods whose semantics are independent of individual resources.

RFC 9110 explicitly emphasizes that standardized HTTP methods are not resource-specific: once defined, a standardized method should have the same semantics when applied to different resources.

That property is extremely important to REST.

---

# 38. Why Uniform Methods Matter

Imagine every resource defining its own commands:

```text
User:
    retrieveUser()
    updateUser()
    deleteUser()

Order:
    fetchOrder()
    modifyOrder()
    cancelOrder()

Payment:
    getPayment()
    executePayment()
```

The client needs resource-specific knowledge.

With a uniform interface:

```text
GET
PUT
DELETE
POST
```

the client already knows the generic semantics.

This improves:

* interoperability;
* generic tooling;
* caching;
* proxies;
* observability;
* evolvability.

---

# 39. Safe Methods

HTTP defines some methods as **safe**.

Examples:

```text
GET
HEAD
OPTIONS
TRACE
```

A safe method is intended primarily for retrieval/observation rather than state-changing actions.

A REST API should respect these semantics.

For example:

```text
GET /users/123
```

should not secretly:

```text
delete the user
```

or:

```text
charge a credit card
```

because doing so violates the expectations associated with the method.

---

# 40. Idempotency

An idempotent operation can be performed multiple times with the same intended effect as performing it once.

Typical HTTP examples:

```text
GET
PUT
DELETE
```

are idempotent according to HTTP semantics.

For example:

```http
PUT /users/123
```

with the same representation repeated several times should produce the same intended resource state.

Idempotency is extremely useful for distributed systems because network failures can make it unclear whether a request was processed.

---

# 41. POST and Idempotency

POST is not inherently idempotent.

For example:

```http
POST /payments
```

could create a new payment every time.

If the client does:

```text
POST
timeout
POST retry
```

the server might receive both.

This is why application-level idempotency mechanisms are frequently used for critical operations.

---

# 42. REST and Distributed-System Failures

REST's statelessness and HTTP's method semantics are particularly valuable in unreliable networks.

Consider:

```text
Client
 │
 │ PUT
 ▼
Server
 │
 │ successfully modifies resource
 ▼
Response lost
```

The client sees:

```text
timeout
```

It does not know whether the server processed the request.

If PUT is idempotent:

```text
PUT again
```

is generally safe from the perspective of achieving the same intended resource state.

This is an important reason standardized method semantics matter.

---

# 43. Resource Naming

REST-oriented APIs generally use nouns rather than verbs in resource identifiers.

Prefer:

```text
/users
/users/123
/orders
/orders/456
/products/789
```

rather than:

```text
/getUser
/createUser
/deleteUser
/getOrder
```

The operation is conveyed primarily through the method.

---

# 44. Hierarchical Resource Relationships

Resources can be related.

For example:

```text
/users/123
/users/123/orders
/users/123/orders/456
```

This can communicate relationships.

However, URI hierarchy should not be treated as a mandatory REST rule.

REST does not require every API to use:

```text
/users/{userId}/orders/{orderId}
```

The important architectural concept is resource identification, not a particular URI naming convention.

---

# 45. URI Design

A good resource URI is:

* stable;
* meaningful;
* independently identifiable;
* not unnecessarily tied to implementation details.

Prefer:

```text
/users/123
```

over:

```text
/getUserFromPostgres?id=123
```

The second exposes implementation details and procedure semantics.

---

# 46. Resource Identity vs Database Identity

A REST resource does not have to correspond directly to a database row.

For example:

```text
/users/123
```

could represent:

```text
PostgreSQL row
+
Redis data
+
external service data
+
computed information
```

It can even represent something dynamic.

HTTP explicitly does not constrain what constitutes a resource; it provides an interface for interacting with resources.

---

# 47. A Resource Can Be Computed

For example:

```text
/weather/current
```

could represent:

```text
Current weather information
```

The server may compute it from:

```text
Sensors
Weather stations
Satellite data
Forecast models
```

There does not need to be a database row called:

```text
weather.current
```

---

# 48. A Resource Can Have Multiple Representations

Consider:

```text
/users/123
```

The client might request:

```http
Accept: application/json
```

and receive:

```json
{
  "id": 123,
  "name": "Alice"
}
```

Another client might request:

```http
Accept: text/html
```

and receive:

```html
<h1>Alice</h1>
```

Same resource:

```text
/users/123
```

Different representations.

---

# 49. Content Negotiation

HTTP provides the mechanisms used for representation negotiation.

Client:

```http
Accept: application/json
```

Server:

```http
Content-Type: application/json
```

This can be interpreted as:

```text
Resource
   │
   ├── JSON representation
   ├── HTML representation
   └── XML representation
```

The client communicates which representation it prefers.

---

# 50. REST Does Not Require JSON

This is another common misconception.

REST does not require:

```text
JSON
```

A REST system can use:

```text
JSON
XML
HTML
CSV
images
PDF
Protocol Buffers
custom media types
```

What matters is that representations are exchanged according to the architectural constraints.

JSON became extremely popular because it is convenient for modern application development.

It is not a REST requirement.

---

# 51. Media Types

A representation should have an appropriate media type.

Examples:

```http
Content-Type: application/json
```

```http
Content-Type: application/xml
```

```http
Content-Type: text/html
```

A more REST-oriented design can define custom media types.

For example:

```text
application/vnd.example.user+json
```

This allows the representation format and its semantics to evolve independently.

---

# 52. Hypermedia and Media Types

A mature REST architecture can define not just:

```text
JSON syntax
```

but also:

```text
What fields mean
What transitions exist
What links mean
What actions are permitted
```

For example:

```json
{
  "id": 123,
  "state": "pending",
  "_links": {
    "self": {
      "href": "/orders/123"
    },
    "cancel": {
      "href": "/orders/123/cancellation"
    },
    "payment": {
      "href": "/orders/123/payment"
    }
  }
}
```

The representation communicates both:

```text
current state
```

and:

```text
possible transitions
```

---

# 53. REST and Application State

The word "state" in REST is frequently misunderstood.

Consider a browser interacting with a shopping application:

```text
Browsing
   ↓
Product selected
   ↓
Cart created
   ↓
Checkout
   ↓
Payment
   ↓
Order confirmation
```

The client is moving through application state.

REST's hypermedia constraint allows representations to guide these transitions.

For example:

```text
Representation:
Order is unpaid.

Available transitions:
    pay
    cancel
    view
```

After payment:

```text
Representation:
Order is paid.

Available transitions:
    ship
    view
```

The representation therefore helps drive the client's application state.

---

# 54. REST Does Not Mean "Stateless Application"

A REST application can absolutely have:

```text
logged-in users
shopping carts
orders
payment state
workflow state
```

The important distinction is:

```text
Server-side conversational state
```

versus:

```text
Resource state and application state represented through
resources and representations
```

REST does not prohibit persistent business state.

---

# 55. REST and Sessions

Traditional server-side sessions often work like:

```text
Client
 │
 │ Cookie: session=abc
 ▼
Server
 │
 └── session[abc] = {
         user=123,
         current_step=4,
         ...
     }
```

The meaning of a request may depend on hidden server-side session state.

A RESTful design generally tries to avoid such conversational coupling.

It may instead use:

```http
Authorization: Bearer <token>
```

and explicit resource representations.

However, simply replacing a server session with a JWT does **not automatically make an application RESTful**.

The architectural constraints must still be considered as a whole.

---

# 56. REST and JWT

JWT is an authentication/token format.

REST is an architectural style.

Therefore:

```text
REST ≠ JWT
```

An API can use:

```text
REST + JWT
```

or:

```text
REST + cookie authentication
```

or:

```text
REST + HTTP Basic authentication over TLS
```

Authentication mechanism and architectural style are separate concerns.

---

# 57. REST and HTTP Status Codes

REST benefits heavily from HTTP status semantics.

For example:

```text
GET /users/123
```

might produce:

```text
200 OK
```

or:

```text
404 Not Found
```

A creation request might produce:

```text
201 Created
Location: /users/123
```

An asynchronous operation might produce:

```text
202 Accepted
```

This allows generic HTTP infrastructure and clients to understand broad outcomes without knowing application-specific details.

---

# 58. REST and `Location`

Consider:

```http
HTTP/1.1 201 Created
Location: /users/123
```

This communicates:

```text
The request created a resource.
The new resource is available at:
    /users/123
```

The client does not need to infer the URI from application-specific rules.

---

# 59. REST and Conditional Requests

REST and HTTP work particularly well together because HTTP provides conditional mechanisms.

For example:

```http
GET /users/123
If-None-Match: "abc123"
```

The server can respond:

```http
304 Not Modified
```

This enables efficient cache validation without transferring the representation again.

---

# 60. Optimistic Concurrency

Suppose:

```text
User 123
Version: 5
```

Client A retrieves it:

```http
ETag: "version-5"
```

Client B also retrieves it.

Client A updates:

```http
If-Match: "version-5"
```

The server accepts it and changes the version.

Client B then tries:

```http
If-Match: "version-5"
```

The condition fails.

The server can return:

```text
412 Precondition Failed
```

This is a powerful distributed-systems technique enabled by HTTP's conditional request semantics.

---

# 61. REST and Caching

A REST API should be designed with cacheability in mind.

For example:

```http
GET /products/123
Cache-Control: max-age=300
ETag: "abc123"
```

A CDN or intermediary can potentially serve repeated requests without contacting the origin.

This is one of the major scalability benefits of REST's architectural constraints.

---

# 62. REST and Intermediaries

Consider:

```text
Client
  │
  ▼
CDN
  │
  ▼
WAF
  │
  ▼
Load Balancer
  │
  ▼
API Gateway
  │
  ▼
Service
```

A REST-style uniform interface allows many intermediaries to operate without understanding the internal implementation of the service.

For example:

```text
CDN
```

understands caching.

```text
WAF
```

understands request filtering.

```text
Load balancer
```

understands routing.

The application itself understands:

```text
business semantics
```

---

# 63. Why RPC Can Be Harder to Interpose

An RPC system might define:

```text
ExecutePayment()
GetCustomer()
CancelOrder()
```

with application-specific semantics.

A generic intermediary needs to understand the RPC framework.

A REST-style interface instead uses standardized HTTP semantics:

```text
GET
POST
PUT
DELETE
```

and resource identifiers.

This makes generic infrastructure more useful.

---

# 64. REST and Layered Architecture

A client may not know whether:

```text
GET /users/123
```

is served by:

```text
Cache
```

or:

```text
Reverse proxy
```

or:

```text
API gateway
```

or:

```text
origin application
```

The interface remains the same.

This is precisely the kind of architectural opacity enabled by REST's layered-system constraint.

---

# 65. REST Does Not Require Microservices

REST and microservices are independent concepts.

You can have:

```text
Monolithic application
+
REST API
```

or:

```text
Microservices
+
REST APIs
```

or:

```text
Microservices
+
gRPC
```

REST is not a microservice architecture.

---

# 66. REST Does Not Require Public APIs

A REST architecture can be used internally:

```text
Service A
    │
    │ HTTP
    ▼
Service B
```

or externally:

```text
Mobile App
    │
    ▼
Public API
```

The architectural constraints do not depend on whether the API is public.

---

# 67. REST Does Not Require HTTP/1.1

REST is independent of the HTTP wire version.

The same REST-style API can operate over:

```text
HTTP/1.1
HTTP/2
HTTP/3
```

The semantics remain largely the same.

The wire representation changes.

For example:

```text
REST API
    │
    ├── HTTP/1.1
    ├── HTTP/2
    └── HTTP/3
```

This demonstrates the distinction between architecture and protocol framing.

---

# 68. REST and HTTP/2

HTTP/2 changes:

```text
wire framing
multiplexing
header compression
connection behavior
```

It does not fundamentally change the resource-oriented semantics.

A REST API can therefore move:

```text
HTTP/1.1
```

to:

```text
HTTP/2
```

without redesigning its resources.

---

# 69. REST and HTTP/3

Likewise:

```text
REST
  ↓
HTTP semantics
  ↓
HTTP/3
  ↓
QUIC
  ↓
UDP
```

The application architecture can remain RESTful while the transport changes from TCP to QUIC.

This is another strong demonstration that:

```text
REST ≠ HTTP wire protocol
```

---

# 70. A REST Request Through the Stack

Suppose the client requests:

```http
GET /users/123 HTTP/1.1
Host: api.example.com
Accept: application/json
```

The architectural interpretation is:

```text
REST:
    "Retrieve the representation of resource /users/123."
```

HTTP interprets:

```text
GET
Host
Accept
```

TCP transports the bytes.

TLS encrypts them if HTTPS is used.

IP routes the packets.

Therefore:

```text
REST semantics
       ↓
HTTP semantics
       ↓
HTTP wire representation
       ↓
TLS
       ↓
TCP
       ↓
IP
```

---

# 71. The Same REST Interaction Over HTTP/2

Conceptually:

```text
REST:
    GET resource /users/123
```

becomes HTTP/2 pseudo-fields:

```text
:method = GET
:scheme = https
:authority = api.example.com
:path = /users/123
```

These are encoded into HTTP/2 frames.

The REST architectural meaning remains unchanged.

---

# 72. The Same REST Interaction Over HTTP/3

The same semantic interaction becomes:

```text
:method = GET
:scheme = https
:authority = api.example.com
:path = /users/123
```

but is represented using HTTP/3 framing and QPACK and transported over QUIC.

Again:

```text
REST meaning
    ↓
same

HTTP wire representation
    ↓
different
```

---

# 73. REST vs HTTP Comparison

| Property                          | REST                                    | HTTP                                                |
| --------------------------------- | --------------------------------------- | --------------------------------------------------- |
| Nature                            | Architectural style                     | Application-layer protocol                          |
| Defined by                        | Fielding's architectural work           | IETF RFCs                                           |
| Main purpose                      | Structure distributed interactions      | Exchange HTTP messages                              |
| OSI relationship                  | Application architecture                | Layer 7 protocol                                    |
| Requires TCP                      | No                                      | Depends on version                                  |
| Requires HTTP                     | No                                      | Itself                                              |
| Requires JSON                     | No                                      | No                                                  |
| Defines methods                   | Architectural use of uniform operations | Yes                                                 |
| Defines status codes              | Uses protocol semantics                 | Yes                                                 |
| Defines caching                   | Architectural constraint                | Concrete mechanisms                                 |
| Defines URI use                   | Resource identification                 | Concrete URI/request semantics                      |
| Requires statelessness            | Yes                                     | HTTP itself is stateless                            |
| Requires client-server separation | Yes                                     | Not sufficient by itself                            |
| Requires uniform interface        | Yes                                     | HTTP provides mechanisms supporting it              |
| Requires HATEOAS                  | Yes, for full REST                      | No                                                  |
| Requires hypermedia               | Yes                                     | HTTP can carry hypermedia but does not require REST |
| Requires layered system           | Yes                                     | HTTP supports intermediaries                        |
| Code-on-demand                    | Optional REST constraint                | HTTP can transfer executable code                   |

---

# 74. HTTP API vs REST API

Consider this:

```http
POST /getUser
Content-Type: application/json

{
  "id": 123
}
```

It is an HTTP API.

It uses HTTP.

But it resembles RPC.

Now consider:

```http
GET /users/123
Accept: application/json
```

This is much more resource-oriented.

But even this alone does not prove that the complete system is RESTful.

We still need to examine:

```text
Client-server separation
Statelessness
Cacheability
Uniform interface
Layering
Self-descriptive messages
Hypermedia
```

---

# 75. The REST Maturity Model

A useful practical model is the **Richardson Maturity Model**.

It is not the definition of REST itself, but it provides a useful way to assess HTTP APIs.

## Level 0 — RPC over HTTP

```text
POST /api
```

Everything is essentially a command.

---

## Level 1 — Resources

Introduce resource-oriented URIs:

```text
/users/123
/orders/456
```

but still use limited HTTP semantics.

---

## Level 2 — HTTP Verbs and Status Codes

Use HTTP methods and status codes appropriately:

```text
GET
POST
PUT
DELETE
```

and:

```text
200
201
204
400
404
409
...
```

This is where many APIs commonly stop.

---

## Level 3 — Hypermedia Controls

Responses communicate available transitions:

```json
{
  "status": "pending",
  "_links": {
    "pay": {
      "href": "/payments/123"
    },
    "cancel": {
      "href": "/orders/456/cancellation"
    }
  }
}
```

This is substantially closer to the full REST architectural model.

---

# 76. Richardson Maturity Model Is Not REST Itself

This distinction matters.

The Richardson model is a useful engineering model.

REST itself comes from Fielding's architectural constraints.

Therefore:

```text
Richardson Maturity Model
        ≠
formal definition of REST
```

It is better viewed as a practical way to discuss how much an API uses HTTP's resource and hypermedia capabilities.

---

# 77. Common "REST" Misconceptions

## Misconception 1

> REST means HTTP.

False.

```text
REST = architectural style
HTTP = protocol
```

---

## Misconception 2

> REST means JSON.

False.

JSON is merely one representation format.

---

## Misconception 3

> REST means CRUD.

False.

CRUD is a common application pattern mapped onto HTTP methods.

---

## Misconception 4

> REST means use GET/POST/PUT/DELETE.

Insufficient.

Using HTTP methods correctly is important, but it does not satisfy all REST constraints.

---

## Misconception 5

> REST means stateless database.

False.

REST does not prohibit server-side resource state.

---

## Misconception 6

> REST means no sessions.

More precisely:

REST discourages hidden conversational state between requests.

Authentication/session mechanisms can still exist, but their interaction with statelessness needs to be designed carefully.

---

## Misconception 7

> REST means microservices.

False.

REST can be used in monoliths, distributed systems, internal services, and public APIs.

---

## Misconception 8

> REST requires URLs containing nouns.

Not strictly.

Resource identification is fundamental, but particular URI naming conventions are design practices rather than the entirety of REST.

---

# 78. REST Constraints vs HTTP Features

This table is useful for separating the concepts.

| REST requirement          | HTTP mechanism that helps implement it              |
| ------------------------- | --------------------------------------------------- |
| Resource identification   | URI                                                 |
| Uniform interface         | HTTP methods                                        |
| Self-descriptive messages | Headers, media types, status codes                  |
| Cacheability              | Cache-Control, ETag, validators                     |
| Stateless interactions    | Independent requests                                |
| Client-server separation  | HTTP client/server model                            |
| Layered system            | Proxies, gateways, caches                           |
| Representations           | Content-Type, content negotiation                   |
| Hypermedia                | HTML, link relations, representation-specific links |
| Code-on-demand            | HTTP-delivered executable representations           |

Notice the wording:

```text
REST requirement
       ↓
HTTP mechanism
```

not:

```text
HTTP feature
       =
REST requirement
```

---

# 79. HTTP Provides the Uniform Interface Ingredients

HTTP already provides:

```text
GET
HEAD
POST
PUT
DELETE
OPTIONS
TRACE
```

and:

```text
URI
headers
status codes
representations
caching
conditional requests
content negotiation
```

These mechanisms make HTTP particularly compatible with REST.

This is one reason REST-style API design became so strongly associated with HTTP.

---

# 80. But HTTP Alone Does Not Guarantee REST

An HTTP service could:

```text
use POST for everything
ignore caching
use server-side conversational state
return opaque commands
hard-code every workflow
expose no hypermedia
couple client and server tightly
```

and still be a valid HTTP service.

Therefore:

```text
Valid HTTP
    ≠
RESTful architecture
```

---

# 81. RESTful Design Example

Suppose we have an order system.

Resources:

```text
/orders
/orders/123
/orders/123/items
/orders/123/payment
```

Retrieve order:

```http
GET /orders/123
```

Create order:

```http
POST /orders
Content-Type: application/json

{
  "items": [
    {
      "product": "/products/10",
      "quantity": 2
    }
  ]
}
```

Response:

```http
HTTP/1.1 201 Created
Location: /orders/123
Content-Type: application/json
```

Representation:

```json
{
  "id": 123,
  "status": "pending",
  "_links": {
    "self": {
      "href": "/orders/123"
    },
    "payment": {
      "href": "/orders/123/payment"
    },
    "cancel": {
      "href": "/orders/123/cancellation"
    }
  }
}
```

The representation contains:

```text
resource state
+
available transitions
```

This is much closer to the REST architectural model.

---

# 82. RESTful Workflow

The client can follow the workflow:

```text
GET /orders/123
        │
        ▼
status = pending
        │
        ├── payment link
        │
        ▼
POST /orders/123/payment
        │
        ▼
status = paid
        │
        ├── shipment link
        │
        ▼
GET /shipments/456
```

The server provides the transitions.

The client does not necessarily need to know the entire workflow beforehand.

---

# 83. Why Hypermedia Reduces Coupling

Without hypermedia:

```text
Client
 │
 ├── knows /orders/{id}
 ├── knows /orders/{id}/payment
 ├── knows /orders/{id}/cancel
 ├── knows /shipments/{id}
 └── knows all workflow rules
```

With hypermedia:

```text
Client
 │
 └── follows links supplied by server
```

The server can change URI structures without necessarily breaking a client that understands link relations and media types.

This is one of the strongest arguments for the full REST model.

---

# 84. REST and API Versioning

REST does not mandate a particular versioning mechanism.

Possible approaches include:

```text
URI versioning
/api/v1/users
```

header-based versioning:

```http
Accept: application/vnd.example.v2+json
```

or other media-type negotiation mechanisms.

Versioning should ideally preserve the architectural separation between:

```text
resource identity
```

and:

```text
representation format
```

---

# 85. URI Versioning

Common:

```text
/api/v1/users
/api/v2/users
```

Advantages:

* obvious;
* easy to route;
* easy to debug.

Disadvantages:

* version becomes part of the URI;
* potentially duplicates resource identifiers;
* can encourage treating API versions as completely separate resources.

---

# 86. Media-Type Versioning

Example:

```http
Accept: application/vnd.example.user.v2+json
```

This treats versioning more as a representation concern.

Conceptually:

```text
Resource
   │
   ├── v1 representation
   └── v2 representation
```

This is conceptually closer to the distinction between resources and representations.

---

# 87. REST and Backward Compatibility

REST encourages independent evolution.

A server should ideally be able to evolve:

```text
Representation v1
        ↓
Representation v2
```

without requiring simultaneous replacement of every client.

Hypermedia, self-descriptive messages, optional fields, and media-type evolution can all help.

---

# 88. REST and Extensibility

A good REST interface avoids making clients depend unnecessarily on:

```text
database schema
internal class names
internal service topology
implementation-specific identifiers
```

Instead, the client depends on:

```text
resource identifiers
media types
link relations
HTTP semantics
documented application semantics
```

This reduces coupling.

---

# 89. REST and Database Design

REST does not dictate:

```text
SQL schema
NoSQL schema
database engine
ORM
```

For example:

```text
REST resource:
    /customers/123
```

could be backed by:

```text
PostgreSQL
```

or:

```text
MongoDB
```

or:

```text
Redis + PostgreSQL
```

or:

```text
several microservices
```

The representation is the interface boundary.

---

# 90. REST and Domain-Driven Design

REST can work well with domain-driven design, but they solve different problems.

DDD concerns:

```text
bounded contexts
aggregates
entities
value objects
domain services
```

REST concerns:

```text
distributed component interaction
resource identification
representations
uniform interfaces
```

A domain aggregate does not necessarily equal a REST resource.

---

# 91. REST and GraphQL

GraphQL and REST are different API architectural approaches.

REST:

```text
Resource-oriented
+
HTTP semantics
+
representations
+
standard methods
```

GraphQL:

```text
Query language
+
schema
+
single endpoint is common
+
client-specified selection
```

GraphQL can be transported over HTTP, but:

```text
GraphQL over HTTP
```

does not automatically become REST.

---

# 92. REST and gRPC

gRPC is an RPC framework.

Typical model:

```text
Client
   │
   │ ExecuteMethod()
   ▼
Server
```

REST:

```text
Client
   │
   │ manipulate resource through uniform interface
   ▼
Server
```

gRPC commonly uses:

```text
HTTP/2
Protocol Buffers
RPC semantics
```

REST commonly uses:

```text
HTTP
JSON/XML/etc.
resource semantics
```

Both are valid distributed application architectures.

They optimize for somewhat different goals.

---

# 93. REST and WebSockets

WebSockets provide a long-lived bidirectional communication channel.

REST generally uses request/response interactions.

Therefore:

```text
REST:
Client → Request → Server
Client ← Response ← Server
```

while WebSocket is:

```text
Client ←→ persistent bidirectional channel ←→ Server
```

A system can use both:

```text
REST
+
WebSocket
```

for different purposes.

For example:

```text
REST → resource management
WebSocket → real-time events
```

---

# 94. REST and Event-Driven Architecture

REST is not inherently event-driven.

REST generally uses:

```text
request
   ↓
response
```

An event-driven architecture might use:

```text
Producer
   ↓
Event broker
   ↓
Consumers
```

A system can combine them:

```text
REST API
    ↓
Command
    ↓
Event broker
    ↓
Workers
```

The external interface may be RESTful even if the internal architecture is asynchronous.

---

# 95. Asynchronous REST Operations

Suppose:

```http
POST /reports
```

starts a large report generation job.

The server can respond:

```http
HTTP/1.1 202 Accepted
Location: /reports/jobs/123
```

The client can then:

```http
GET /reports/jobs/123
```

until the operation completes.

This preserves HTTP semantics while supporting asynchronous processing.

---

# 96. REST and 202 Accepted

HTTP defines:

```text
202 Accepted
```

for a request that has been accepted for processing but is not necessarily complete.

This works naturally with resource-oriented designs.

Example:

```text
POST /video-transcodes
        │
        ▼
202 Accepted
Location: /video-transcodes/jobs/123
        │
        ▼
GET /video-transcodes/jobs/123
```

The job itself becomes a resource.

---

# 97. Resource Modeling for Commands

Some operations do not map naturally onto CRUD.

For example:

```text
"cancel order"
```

can be modeled as a resource transition:

```text
/orders/123/cancellation
```

or as a state transition:

```http
PATCH /orders/123
```

with:

```json
{
  "status": "cancelled"
}
```

The correct design depends on domain semantics.

REST does not require every operation to be forced into simplistic CRUD.

---

# 98. Resource Modeling Is a Design Exercise

The key question should be:

> What are the resources and their relationships?

rather than:

> Which controller method should I expose?

For example:

```text
Payment
Order
Customer
Shipment
Invoice
```

may all be independent resources.

Actions can then be represented through:

```text
state transitions
sub-resources
POST processing
hypermedia controls
```

---

# 99. REST and Business Actions

A common misconception is that REST prohibits actions.

It does not.

For example:

```http
POST /orders/123/payment
```

can be completely appropriate.

The question is whether the operation can be meaningfully represented as interaction with a resource and whether the interface remains uniform and self-descriptive.

REST is not:

```text
"Never use verbs anywhere."
```

It is:

```text
"Use a uniform interface around resources and representations."
```

---

# 100. REST and Error Representation

A REST API should provide useful representations of errors.

For example:

```http
HTTP/1.1 400 Bad Request
Content-Type: application/problem+json
```

with:

```json
{
  "type": "https://example.com/problems/invalid-user",
  "title": "Invalid user",
  "status": 400,
  "detail": "The email address is invalid."
}
```

RFC 9457 defines the `application/problem+json` and `application/problem+xml` problem detail formats.

This is useful because:

```text
HTTP status
    +
structured representation
```

communicates both generic protocol semantics and application-specific details.

---

# 101. REST Error Design

A good API distinguishes:

```text
HTTP semantics
```

from:

```text
application error details
```

For example:

```text
HTTP 404
```

communicates:

> The target resource was not found.

The representation can communicate:

```json
{
  "type": "...",
  "title": "User not found",
  "detail": "No user exists with ID 123."
}
```

---

# 102. REST and Security

REST does not provide security by itself.

A REST API commonly relies on:

```text
TLS
authentication
authorization
input validation
rate limiting
CSRF protection where applicable
secure cookies where applicable
request size limits
replay protection
audit logging
```

REST's statelessness can simplify some security architectures but does not automatically make an API secure.

---

# 103. Authentication vs Authorization

Authentication:

```text
Who are you?
```

Authorization:

```text
What are you allowed to do?
```

For example:

```http
Authorization: Bearer <token>
```

can establish an authenticated identity.

The server then decides:

```text
GET /users/123
```

may be allowed while:

```text
DELETE /users/123
```

may be forbidden.

---

# 104. REST and Security Boundaries

A resource-oriented API makes authorization decisions naturally expressible:

```text
Can principal P:
    GET /users/123 ?

Can principal P:
    PUT /users/123 ?

Can principal P:
    DELETE /users/123 ?
```

Authorization should be based on:

```text
identity
resource
operation
context
```

rather than solely on URI patterns.

---

# 105. REST and Rate Limiting

HTTP provides:

```text
429 Too Many Requests
```

and REST APIs commonly expose rate limits through response metadata.

For example:

```http
HTTP/1.1 429 Too Many Requests
Retry-After: 60
```

Rate limiting is an operational concern rather than a defining REST constraint.

---

# 106. REST and Observability

A uniform interface makes generic infrastructure highly effective.

A proxy can record:

```text
GET /users/123 → 200
POST /orders → 201
GET /orders/999 → 404
```

without understanding internal implementation.

Observability systems can therefore measure:

```text
latency
status distributions
request rates
cache hit rates
error rates
resource access patterns
```

using standard HTTP semantics.

---

# 107. REST and Idempotent Retry

A distributed network can fail after a server has processed a request but before the client receives the response.

For example:

```text
Client
 │
 │ PUT
 ▼
Server
 │
 │ state changed
 ▼
Network failure
```

Client:

```text
"I don't know whether it succeeded."
```

If the method is idempotent, the client can often safely retry.

This is one of the major practical benefits of HTTP's method semantics within a REST-style architecture.

---

# 108. REST and Eventual Consistency

REST does not require strong consistency.

A REST API can front:

```text
strongly consistent database
```

or:

```text
eventually consistent distributed store
```

The HTTP/REST interface does not dictate the database consistency model.

However, representations should communicate state clearly when asynchronous or eventually consistent operations are involved.

---

# 109. REST and Distributed Transactions

REST does not provide distributed transactions.

For example:

```text
Service A
Service B
Service C
```

cannot automatically participate in a REST-level ACID transaction merely because all three expose REST APIs.

Distributed transaction patterns may instead involve:

```text
Saga
outbox pattern
idempotency
compensating actions
eventual consistency
```

These are separate distributed-systems techniques.

---

# 110. REST and Caching Semantics

Caching is one of the strongest reasons REST works well for Internet-scale architectures.

Consider:

```text
10,000 clients
      │
      ▼
    CDN
      │
      └── cache
             │
             ▼
          origin
```

If:

```http
Cache-Control: max-age=3600
```

is appropriate, many requests can be served without reaching the origin.

This reduces:

```text
origin CPU
database queries
network bandwidth
latency
```

---

# 111. REST and Conditional Requests

For dynamic resources:

```http
ETag: "version-42"
```

allows clients and caches to validate existing representations.

The request:

```http
If-None-Match: "version-42"
```

can produce:

```http
304 Not Modified
```

instead of retransmitting the complete representation.

This is a direct example of HTTP mechanisms supporting REST's cacheability constraint.

---

# 112. REST and Hypermedia Formats

Hypermedia can be implemented using different formats.

HTML naturally supports links:

```html
<a href="/orders/123">Order</a>
```

JSON can use explicit links:

```json
{
  "_links": {
    "self": {
      "href": "/orders/123"
    }
  }
}
```

Standards such as:

```text
HAL
JSON:API
Siren
Collection+JSON
```

provide different approaches to hypermedia and API representation.

None of these is synonymous with REST itself.

---

# 113. REST and OpenAPI

OpenAPI describes an HTTP API.

It can describe:

```text
paths
methods
parameters
request bodies
responses
schemas
authentication
```

However:

```text
OpenAPI ≠ REST
```

An RPC-style HTTP API can have a perfectly valid OpenAPI specification.

OpenAPI describes an interface.

REST describes architectural constraints.

---

# 114. REST and JSON Schema

Likewise:

```text
JSON Schema
```

describes JSON structure.

It does not define:

```text
REST
```

A system can use:

```text
REST
+
HTTP
+
JSON
+
JSON Schema
+
OpenAPI
```

Each solves a different problem.

---

# 115. Complete Layered View

A realistic REST API stack can be represented as:

```text
┌────────────────────────────────────────────┐
│ Business domain                            │
│ Orders / Users / Payments / Products      │
├────────────────────────────────────────────┤
│ REST architectural constraints             │
│ Resources / uniform interface / HATEOAS    │
├────────────────────────────────────────────┤
│ HTTP semantics                             │
│ Methods / status / fields / caching        │
├────────────────────────────────────────────┤
│ HTTP wire protocol                         │
│ HTTP/1.1 / HTTP/2 / HTTP/3                 │
├────────────────────────────────────────────┤
│ Security / transport                       │
│ TLS / TCP / QUIC                           │
├────────────────────────────────────────────┤
│ Network                                    │
│ IP                                         │
├────────────────────────────────────────────┤
│ Link                                       │
│ Ethernet / Wi-Fi / etc.                    │
└────────────────────────────────────────────┘
```

This model makes the distinction particularly clear.

---

# 116. REST vs OSI Layer 7 — Precise Interpretation

It is tempting to say:

> "REST is a Layer 7 protocol."

That statement is technically imprecise.

A better statement is:

> REST is an application-layer architectural style that constrains the design of distributed application interactions.

HTTP is an application-layer protocol that provides concrete message semantics and wire mechanisms capable of implementing many REST constraints.

Therefore:

```text
REST
    ↓
Application architecture

HTTP
    ↓
Application-layer protocol

TCP / QUIC
    ↓
Transport

IP
    ↓
Network
```

REST participates in Layer 7 architecture but is not itself a Layer 7 wire protocol.

---

# 117. The Relationship Between REST and HTTP

The relationship can be summarized as:

```text
                    REST
                     │
          architectural constraints
                     │
                     ▼
             ┌───────────────┐
             │ Resource model│
             │ Uniform iface │
             │ Statelessness │
             │ Cacheability  │
             │ Layering      │
             │ Hypermedia    │
             └───────┬───────┘
                     │
                     ▼
                    HTTP
                     │
          concrete protocol mechanisms
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
    Methods       Headers       Status codes
       │             │             │
       └─────────────┼─────────────┘
                     ▼
              Representations
                     │
                     ▼
              HTTP/1.1 / 2 / 3
```

HTTP is therefore an excellent implementation substrate for REST.

---

# 118. What Makes an API "Truly RESTful"?

A strong REST evaluation should ask:

### 1. Are resources identifiable?

```text
/users/123
/orders/456
```

### 2. Is there a uniform interface?

```text
GET
POST
PUT
DELETE
...
```

### 3. Are HTTP method semantics respected?

For example:

```text
GET should be safe.
PUT should be idempotent.
```

### 4. Are interactions stateless?

Each request should contain the information needed to process it.

### 5. Are responses appropriately cacheable?

### 6. Are messages self-descriptive?

### 7. Can intermediaries operate without understanding implementation internals?

### 8. Are representations capable of communicating application transitions?

### 9. Is client/server separation maintained?

### 10. Is the architecture evolvable independently?

These questions are much more meaningful than:

```text
"Does the API use JSON?"
```

or:

```text
"Does it have GET/POST/PUT/DELETE?"
```

---

# 119. A Practical REST Checklist

## Resource Model

* [ ] Resources have stable identifiers.
* [ ] Resource identity is separated from representation format.
* [ ] URI design does not unnecessarily expose implementation details.
* [ ] Resource relationships are understandable.

## Uniform Interface

* [ ] HTTP methods have their standardized meanings.
* [ ] GET is safe.
* [ ] Idempotent methods remain idempotent.
* [ ] Status codes are used meaningfully.
* [ ] `Location` is used where appropriate.

## Statelessness

* [ ] Requests contain required application context.
* [ ] Server does not depend on hidden conversational state.
* [ ] Requests can be load-balanced across servers.

## Cacheability

* [ ] Cacheable responses are identified.
* [ ] `Cache-Control` is correct.
* [ ] Validators such as ETags are used where appropriate.
* [ ] `Vary` is correctly handled.

## Representations

* [ ] `Content-Type` is correct.
* [ ] Representation formats are documented.
* [ ] Content negotiation is handled where useful.
* [ ] Error representations are structured.

## Hypermedia

* [ ] Representations expose relevant links.
* [ ] Link relations are meaningful.
* [ ] Client workflows can be discovered through representations where appropriate.

## Layering

* [ ] API works correctly through proxies.
* [ ] CDN caching is possible where appropriate.
* [ ] Gateways do not require knowledge of internal implementation.

---

# 120. Common Anti-Patterns

## Everything is POST

```text
POST /getUser
POST /updateUser
POST /deleteUser
POST /calculateInvoice
```

This often indicates an RPC-oriented API rather than a resource-oriented interface.

---

## Verb-heavy URIs

```text
/getUser
/createUser
/deleteUser
/updateUser
```

Prefer resource-oriented identifiers where appropriate:

```text
/users
/users/123
```

and use HTTP method semantics.

---

## Ignoring HTTP status codes

Returning:

```http
HTTP/1.1 200 OK
```

for every application outcome and putting the actual error into JSON:

```json
{
  "success": false,
  "error": "User not found"
}
```

throws away useful protocol semantics.

A better design may use:

```http
404 Not Found
```

with a structured error representation.

---

## Server-side conversational workflow state

For example:

```text
POST /start
    ↓
server stores session step = 1

POST /continue
    ↓
server checks session step = 1

POST /continue
    ↓
server checks session step = 2
```

This creates hidden conversational coupling.

---

## Hard-coded workflows

A client containing:

```text
if pending:
    POST /orders/{id}/pay

if paid:
    POST /orders/{id}/ship

if shipped:
    GET /tracking/{id}
```

is tightly coupled to server URI structure.

A stronger hypermedia architecture can communicate available transitions through representations.

---

# 121. REST Does Not Mean "No Business Logic"

REST does not require resources to be simple database records.

A resource can represent:

```text
payment
shipment
calculation
job
report
workflow
search result
current weather
recommendation
```

The important question is how the resource is identified and interacted with through the uniform interface.

---

# 122. REST Does Not Mean "Everything Is a Noun"

REST does not require the entire domain to be expressed as simplistic nouns.

Some operations are naturally modeled as:

```text
POST /payments
```

or:

```text
POST /orders/123/cancellation
```

The goal is not grammatical purity.

The goal is a uniform, resource-oriented, self-descriptive interface.

---

# 123. REST and Search

Search can be modeled as a resource.

For example:

```http
GET /search?q=python&category=books
```

The resulting representation can itself be a resource describing the search result set.

For more complex searches:

```http
POST /searches
```

could create a persistent search resource:

```text
/searches/123
```

which can then be retrieved:

```http
GET /searches/123
```

This can be particularly useful when searches are expensive or asynchronous.

---

# 124. REST and Bulk Operations

Bulk operations require careful modeling.

Instead of:

```text
POST /bulkDelete
```

one could model a collection operation:

```http
DELETE /users?status=inactive
```

if the semantics are appropriate and safely defined.

Alternatively, create a job resource:

```http
POST /deletion-jobs
```

response:

```http
202 Accepted
Location: /deletion-jobs/123
```

Then:

```http
GET /deletion-jobs/123
```

This makes the asynchronous operation observable.

---

# 125. REST and Long-Running Operations

A long-running operation should not require a client connection to remain open indefinitely.

Instead:

```text
POST /reports
        │
        ▼
202 Accepted
Location: /reports/123
        │
        ▼
GET /reports/123
        │
        ├── processing
        │
        ├── processing
        │
        └── completed
```

This architecture works well with stateless interactions and distributed systems.

---

# 126. REST and Polling

Polling is not inherently un-RESTful.

For example:

```http
GET /jobs/123
```

can be repeated.

Caching, conditional requests, and appropriate status representations can make this efficient.

Alternatives include:

```text
WebSockets
Server-Sent Events
Webhooks
message brokers
```

but these are separate architectural mechanisms.

---

# 127. REST and Events

A REST API can expose an event collection:

```http
GET /orders/123/events
```

or an event resource:

```text
/events/456
```

The internal implementation can still use:

```text
Kafka
RabbitMQ
NATS
SQS
```

The REST interface remains independent of the internal messaging system.

---

# 128. REST and Internal Architecture

A REST API should not necessarily map one-to-one to internal services.

For example:

```text
GET /orders/123
```

could internally execute:

```text
API
 │
 ├── Order service
 ├── Customer service
 ├── Inventory service
 ├── Payment service
 └── Database
```

The client sees:

```text
one resource
```

not the internal topology.

This is another consequence of information hiding.

---

# 129. REST and Information Hiding

A major benefit of representations is that they hide implementation.

Client:

```text
GET /users/123
```

does not need to know:

```text
database table
SQL query
cache
replication topology
service topology
programming language
```

The server provides a representation through a standardized interface.

---

# 130. REST and Independent Evolution

Suppose a server changes:

```text
PostgreSQL
```

to:

```text
distributed database
```

or:

```text
monolith
```

to:

```text
microservices
```

The client should ideally continue to interact with:

```text
/users/123
```

using the same uniform interface.

This is one of REST's most important architectural goals.

---

# 131. REST and Scalability

REST's constraints support scalability through:

```text
statelessness
cacheability
uniform interfaces
intermediaries
independent deployment
```

For example:

```text
                    CDN
                     │
            ┌────────┼────────┐
            ▼        ▼        ▼
         Cache     Cache    Cache
            │        │        │
            └────────┼────────┘
                     ▼
                Load Balancer
                /     |      \
               ▼      ▼       ▼
             API A  API B   API C
```

The architecture can scale horizontally without requiring each request to reach a particular server instance.

---

# 132. REST and Reliability

Stateless interactions and standardized method semantics can improve reliability.

For example:

```text
GET
```

can usually be retried safely.

```text
PUT
```

can generally be retried because of idempotency.

```text
POST
```

may require application-level idempotency controls.

This allows clients and infrastructure to make more informed retry decisions.

---

# 133. REST and Failure Recovery

Consider:

```text
Client
 │
 │ PUT /users/123
 ▼
Server
 │
 │ update successful
 ▼
Network connection lost
```

Client:

```text
Unknown result
```

Retry:

```text
PUT /users/123
```

If the operation is idempotent, this is usually manageable.

Compare:

```text
POST /payments
```

where repeating the operation may create a second payment.

This is a fundamental distributed-systems advantage of well-defined method semantics.

---

# 134. REST and Security Through Layering

A REST system can place security mechanisms at multiple layers:

```text
TLS
 ↓
HTTP authentication
 ↓
API authorization
 ↓
resource authorization
 ↓
business rules
```

For example:

```text
TLS:
    Is the channel protected?

Authentication:
    Who is the caller?

Authorization:
    Can the caller access /users/123?

Business rule:
    Can this caller modify this particular field?
```

These are separate concerns.

---

# 135. REST and Rate Limits

A resource-oriented interface makes rate limiting naturally expressible:

```text
GET /users/123
```

versus:

```text
POST /payments
```

Different resources and methods may have different policies.

For example:

```text
GET:
    1000/minute

POST /payments:
    20/minute
```

HTTP status `429` can communicate rate-limit exhaustion.

---

# 136. REST and API Gateways

API gateways commonly provide:

```text
TLS termination
authentication
authorization
rate limiting
routing
logging
metrics
caching
request transformation
```

REST's layered architecture is highly compatible with such gateways.

The application service can remain unaware of many infrastructure details.

---

# 137. REST and CDN

REST's cacheability is particularly valuable for:

```text
GET
```

responses.

For example:

```text
GET /products/123
```

can potentially be served from:

```text
Browser cache
 ↓
CDN
 ↓
Reverse proxy
 ↓
Origin
```

This is much harder to achieve generically for arbitrary RPC commands.

---

# 138. REST and HTTP Method Semantics

The most important HTTP methods for REST-oriented design are:

```text
GET
POST
PUT
PATCH
DELETE
```

but they do not map one-to-one to:

```text
CRUD
```

A better understanding is:

```text
GET
    retrieve representation

POST
    process submitted content according to target semantics

PUT
    replace/create desired state

PATCH
    partially modify

DELETE
    remove target resource
```

These are HTTP semantics, not merely REST conventions.

---

# 139. REST and `OPTIONS`

`OPTIONS` can be useful for discovering communication capabilities.

For example:

```http
OPTIONS /users/123 HTTP/1.1
```

might produce:

```http
Allow: GET, PUT, DELETE
```

This is another example of HTTP providing a generic mechanism that can support uniform interfaces.

---

# 140. REST and `HEAD`

`HEAD` allows metadata retrieval without transferring the representation content.

For example:

```http
HEAD /large-file.iso
```

can help determine:

```text
size
type
ETag
last modification
```

before downloading.

This can be useful for efficient resource handling.

---

# 141. REST and Conditional PUT

Suppose:

```http
PUT /users/123
If-Match: "version-7"
```

The client is effectively saying:

> Replace the resource only if the representation is still version 7.

This prevents accidental overwrites.

The HTTP protocol provides the mechanism; the REST architecture benefits from it because it enables safe resource manipulation in distributed environments.

---

# 142. REST and Partial Updates

PATCH can be used when a client does not want to send the entire representation.

Example:

```http
PATCH /users/123
Content-Type: application/json

{
  "email": "new@example.com"
}
```

However, the semantics of the patch document must be defined.

Common formats include:

```text
JSON Merge Patch
JSON Patch
```

PATCH itself does not prescribe one universal patch format.

---

# 143. REST and Representation Versioning

A representation can evolve.

For example:

```json
{
  "id": 123,
  "name": "Alice"
}
```

could later become:

```json
{
  "id": 123,
  "name": "Alice",
  "display_name": "Alice Smith"
}
```

Clients should ideally tolerate compatible additions.

Strong coupling to exact representation structure reduces REST's evolvability benefits.

---

# 144. REST and Backward Compatibility

Good REST API evolution tends to favor:

```text
additive changes
optional fields
stable resource identifiers
well-defined media types
hypermedia
content negotiation
```

rather than:

```text
breaking URI changes
mandatory new fields everywhere
hidden workflow assumptions
implementation-dependent behavior
```

---

# 145. REST and Hypermedia Controls

Hypermedia controls can describe:

```text
self
related
edit
delete
next
previous
payment
cancel
tracking
```

For example:

```json
{
  "_links": {
    "self": {
      "href": "/orders/123"
    },
    "payment": {
      "href": "/orders/123/payment"
    },
    "customer": {
      "href": "/customers/42"
    }
  }
}
```

The relationship names are often more important than the exact URI.

---

# 146. Link Relations

A link should ideally communicate its semantic relationship.

For example:

```text
self
next
previous
related
collection
```

Standardized link relations can be used where applicable.

Application-specific relations can also be defined.

This allows clients to reason about links without relying exclusively on URI string patterns.

---

# 147. REST and URI Templates

A client can sometimes receive URI templates describing how to construct related resources.

For example:

```text
/search{?q,page}
```

URI templates are standardized separately from REST.

They can be useful but are not a fundamental REST requirement.

---

# 148. REST and Resource Collections

A collection can itself be a resource.

For example:

```text
/users
```

represents a collection.

A member:

```text
/users/123
```

represents one resource.

This allows:

```http
GET /users
```

to retrieve a representation of the collection.

And:

```http
POST /users
```

to request creation/processing against the collection according to its semantics.

---

# 149. REST and Pagination

Pagination can be represented through links.

For example:

```json
{
  "users": [
    ...
  ],
  "_links": {
    "self": {
      "href": "/users?page=2"
    },
    "next": {
      "href": "/users?page=3"
    },
    "previous": {
      "href": "/users?page=1"
    }
  }
}
```

This is preferable to requiring the client to infer every pagination URL convention.

---

# 150. REST and Filtering

Filtering can use query parameters:

```http
GET /users?status=active
```

The query parameters modify the retrieval of the resource/collection.

The URI still identifies a target resource.

---

# 151. REST and Sorting

For example:

```http
GET /users?sort=name
```

or:

```http
GET /products?sort=-price
```

The exact query syntax is application-specific.

REST does not prescribe a universal filtering or sorting grammar.

---

# 152. REST and Search Resources

For complex searches:

```http
POST /searches
```

could produce:

```http
201 Created
Location: /searches/abc123
```

Then:

```http
GET /searches/abc123
```

retrieves the search result.

This can be useful when:

```text
search is expensive
search is asynchronous
search state needs persistence
results need pagination
```

---

# 153. REST and Files

A file can be a resource:

```text
/files/123
```

The representation might be:

```http
Content-Type: application/pdf
```

REST does not require JSON.

The client could retrieve:

```text
PDF bytes
```

as the representation.

---

# 154. REST and Streaming

REST does not inherently prohibit streaming.

A resource representation can be streamed over HTTP.

For example:

```text
GET /large-file
```

can transfer a large representation without requiring the entire object to be held in memory.

HTTP provides the underlying streaming/framing mechanisms.

---

# 155. REST and Webhooks

Webhooks are usually:

```text
Server A
    │
    │ HTTP POST
    ▼
Server B
```

They can complement REST.

For example:

```text
REST:
    Client requests resource state

Webhook:
    Server notifies client of an event
```

The webhook itself is an HTTP interaction, but it does not automatically satisfy REST constraints merely because HTTP is involved.

---

# 156. REST and Long-Lived Connections

REST does not require each HTTP request to create a new connection.

HTTP/1.1 can use persistent connections.

HTTP/2 multiplexes requests over a connection.

HTTP/3 multiplexes requests over QUIC.

Therefore:

```text
REST statelessness
```

does not mean:

```text
TCP connection must close after every request
```

These are completely different concepts.

---

# 157. REST Statelessness vs HTTP Persistent Connections

This distinction is extremely important.

### HTTP persistent connection

```text
Same TCP/QUIC connection
    │
    ├── Request 1
    ├── Request 2
    ├── Request 3
    └── Request 4
```

### REST statelessness

```text
Request 1 can be understood independently.
Request 2 can be understood independently.
Request 3 can be understood independently.
```

Therefore:

```text
persistent transport connection
        ≠
stateful application session
```

---

# 158. REST and Load Balancing

A stateless REST architecture can use:

```text
              Load Balancer
               /    |    \
              ▼     ▼     ▼
           Server1 Server2 Server3
```

Any server can process:

```text
GET /users/123
```

because the request contains the necessary context.

This reduces the need for sticky sessions.

---

# 159. REST and Horizontal Scaling

A typical architecture:

```text
                    Internet
                       │
                       ▼
                    CDN/WAF
                       │
                       ▼
                 Load Balancer
                  /     |     \
                 ▼      ▼      ▼
              API-1   API-2   API-3
                 \      |      /
                  \     |     /
                   ▼    ▼    ▼
                    Database
```

REST's statelessness and cacheability can significantly simplify this architecture.

---

# 160. REST and Service Discovery

REST does not prescribe service discovery.

Systems may use:

```text
DNS
service registry
load balancer
API gateway
Kubernetes services
cloud discovery
```

The client-facing REST resource URI can remain stable even if internal service locations change.

---

# 161. REST and DNS

For:

```text
https://api.example.com/users/123
```

DNS maps:

```text
api.example.com
```

to network endpoints.

REST does not care whether the endpoint is:

```text
one server
```

or:

```text
100 servers
```

or:

```text
CDN → load balancer → service mesh
```

This is another example of architectural abstraction.

---

# 162. REST and Service Meshes

A service mesh may add:

```text
mTLS
service discovery
load balancing
retries
telemetry
traffic policy
```

between services.

For example:

```text
Service A
   │
   ▼
Sidecar
   │
   ▼
Sidecar
   │
   ▼
Service B
```

The application protocol can still be HTTP/REST.

REST does not prescribe whether such infrastructure exists.

---

# 163. REST and API Gateways vs REST

An API gateway is an intermediary.

REST's layered-system constraint makes such intermediaries natural.

However:

```text
API gateway
    ≠
REST
```

A gateway can front:

```text
REST
gRPC
GraphQL
SOAP
RPC
```

and therefore does not imply that the backend is RESTful.

---

# 164. REST and SOAP

SOAP is a protocol/framework for structured web-service messaging.

REST is an architectural style.

A rough comparison:

| REST                          | SOAP                                 |
| ----------------------------- | ------------------------------------ |
| Architectural style           | Protocol/messaging framework         |
| Resource-oriented             | Message/service-oriented             |
| Often HTTP                    | Can use multiple transports          |
| Uses HTTP semantics naturally | HTTP may be merely transport         |
| Hypermedia can be central     | WSDL/service contracts often central |
| Lightweight in common use     | More formal messaging infrastructure |

REST and SOAP solve overlapping but different problems.

---

# 165. REST and HTTP's Uniform Interface

One of the deepest relationships is this:

HTTP was designed around a generic interface to resources.

RFC 9110 describes HTTP as providing a uniform interface for interacting with resources by sending messages that manipulate or transfer representations.

This is closely aligned with REST's architectural model.

Therefore, modern HTTP and REST are deeply related historically and conceptually.

But they remain different abstractions.

---

# 166. Why REST Is Often Confused with HTTP

The confusion exists because the Web itself is an important example of REST architecture and HTTP is its principal application protocol.

Therefore developers often encounter:

```text
REST
+
HTTP
+
URI
+
HTML
```

as one combined system.

But they are different components:

```text
REST
    = architectural constraints

HTTP
    = communication protocol

URI
    = resource identifier syntax/semantics

HTML/JSON/XML
    = representations
```

---

# 167. The Web as a REST Example

The Web is a particularly strong example of REST principles.

Consider:

```text
Browser
   │
   │ GET /
   ▼
Web Server
   │
   ▼
HTML
   │
   ├── link → /products
   ├── link → /about
   └── link → /contact
```

The HTML representation contains hypermedia controls.

The browser follows them.

The server does not need to maintain a conversational state such as:

```text
"The browser is currently on page 7."
```

The client follows links and sends new requests.

This is a natural manifestation of REST principles.

---

# 168. Browser Navigation and REST

Suppose:

```text
GET /shop
```

returns:

```html
<a href="/products">Products</a>
<a href="/cart">Cart</a>
```

The browser can discover:

```text
/products
/cart
```

from the representation.

This is HATEOAS in a very natural form.

The browser does not need a hard-coded table saying:

```text
If on /shop, then /products is always available.
```

The representation supplies the transition.

---

# 169. Why HATEOAS Is Often Missing from APIs

Most modern APIs are consumed by software clients written specifically for that API.

Developers often write:

```python
client.get("/users/123")
client.get("/users/123/orders")
```

instead of:

```python
response = client.get("/users/123")
follow(response.links["orders"])
```

This is convenient and often practical.

But it means the client is coupled to URI structure.

The API can still be called "RESTful" informally, but it is not fully implementing REST's hypermedia constraint.

---

# 170. REST and API Documentation

A traditional API often relies heavily on:

```text
OpenAPI specification
```

to tell clients:

```text
what URI to call
what method to use
what parameters exist
what response looks like
```

A hypermedia-oriented REST architecture attempts to move more of the interaction knowledge into:

```text
representations
link relations
media types
```

This does not mean documentation becomes unnecessary.

It means the runtime representation can participate in guiding interaction.

---

# 171. REST and Discoverability

There are several levels of discoverability:

```text
Level 1:
Documentation tells you everything.

Level 2:
OpenAPI tells you everything.

Level 3:
Responses expose related resource links.

Level 4:
Representations expose state transitions and
actions through hypermedia.
```

The higher levels reduce hard-coded knowledge in clients.

---

# 172. REST and Coupling

A central architectural goal is reducing **temporal and implementation coupling**.

Bad:

```text
Client assumes:
    server implementation
    URI patterns
    workflow sequence
    database semantics
```

Better:

```text
Client depends on:
    standardized HTTP semantics
    resource identifiers
    representation semantics
    link relations
```

This permits independent evolution.

---

# 173. REST and Evolvability

Suppose:

```text
/api/users/123/orders
```

changes internally from:

```text
SQL JOIN
```

to:

```text
distributed query
```

The client does not care.

Similarly:

```text
/order/123
```

could move from:

```text
monolith
```

to:

```text
microservice
```

without changing the client-facing representation.

This is information hiding at architectural scale.

---

# 174. REST and Interoperability

A standardized interface allows generic clients and infrastructure to understand:

```text
GET
POST
PUT
DELETE
404
409
201
304
```

without understanding business implementation.

This makes it possible for:

```text
browser
curl
mobile app
CDN
proxy
crawler
monitoring system
```

to participate in the same architecture.

---

# 175. REST and Caches as Architectural Components

A cache can understand:

```text
GET /products/123
```

without knowing:

```text
how ProductService works
```

This is possible because HTTP defines standardized semantics.

The REST architecture benefits because intermediary components can operate generically.

---

# 176. REST and Generic Tooling

A REST-oriented API can be tested with:

```text
curl
browser
Postman
HTTP clients
proxies
load-testing tools
CDNs
caches
```

without custom transport infrastructure.

This is a major practical advantage.

---

# 177. REST and Performance

REST itself is not a performance protocol.

Performance depends on:

```text
HTTP version
TLS
TCP/QUIC
connection reuse
caching
payload size
compression
server processing
database latency
network latency
```

REST's architectural constraints can enable performance optimizations such as:

```text
caching
intermediaries
stateless scaling
generic infrastructure
```

but REST does not guarantee high performance.

---

# 178. REST and Payload Optimization

A REST API can optimize representations using:

```text
compression
pagination
partial representations
conditional requests
caching
range requests
content negotiation
```

For example:

```http
Accept-Encoding: br
```

can allow compressed representations.

Similarly:

```http
If-None-Match: "abc"
```

can avoid retransmitting unchanged content.

---

# 179. REST and Partial Representations

An API may support selecting fields:

```http
GET /users/123?fields=id,name
```

This is an application-specific convention.

It can reduce payload size.

However, the exact mechanism is not defined by REST.

REST constrains the architecture, not every API parameter syntax.

---

# 180. REST and Pagination Optimization

Instead of returning:

```text
1,000,000 records
```

a collection can be paginated:

```text
GET /users?page=1
```

with:

```json
{
  "items": [...],
  "_links": {
    "next": {
      "href": "/users?page=2"
    }
  }
}
```

This improves:

```text
memory usage
latency
network transfer
database workload
```

---

# 181. REST and Conditional Retrieval

A highly efficient REST interaction might be:

```text
GET /products/123
```

Response:

```http
200 OK
ETag: "abc"
Cache-Control: max-age=300
```

Later:

```http
GET /products/123
If-None-Match: "abc"
```

Response:

```text
304 Not Modified
```

No representation body needs to be transferred.

This demonstrates how REST and HTTP caching work together.

---

# 182. REST and Network Efficiency

REST does not require one HTTP connection per request.

Modern HTTP versions can use:

```text
HTTP/1.1 persistent connections
HTTP/2 multiplexing
HTTP/3 QUIC streams
```

Therefore a REST API can use efficient transport mechanisms without changing its resource architecture.

---

# 183. REST and HTTP/2 Multiplexing

Suppose the client needs:

```text
/users/123
/orders/456
/products/789
```

HTTP/2 can multiplex these requests:

```text
One connection
│
├── stream 1 → /users/123
├── stream 3 → /orders/456
└── stream 5 → /products/789
```

The REST semantics are unchanged.

---

# 184. REST and HTTP/3

Likewise:

```text
One QUIC connection
│
├── stream 0 → /users/123
├── stream 4 → /orders/456
└── stream 8 → /products/789
```

Again:

```text
REST architecture
    ↓
unchanged

transport/framing
    ↓
changed
```

---

# 185. REST and Reliability Through HTTP Semantics

REST benefits from HTTP's mature semantics for:

```text
redirection
conditional requests
caching
range requests
retries
authentication
authorization challenges
status reporting
```

These capabilities were not invented by CRUD API designers.

They are part of the broader HTTP architecture.

---

# 186. REST and Redirection

Suppose a resource moves:

```http
GET /old-users/123
```

server:

```http
301 Moved Permanently
Location: /users/123
```

A client can follow the new resource identifier.

This is another example of the protocol supporting resource-oriented evolution.

---

# 187. REST and 404

A resource-oriented API should distinguish:

```text
resource does not exist
```

from:

```text
server crashed
```

For example:

```text
404 Not Found
```

versus:

```text
500 Internal Server Error
```

This allows generic clients and infrastructure to reason about outcomes.

---

# 188. REST and 409 Conflict

Consider concurrent resource modification:

```text
Client A
    version 5

Client B
    version 5
```

Client A modifies the resource.

Client B attempts a conflicting update.

A response such as:

```text
409 Conflict
```

can communicate a state conflict.

For concurrency control, `412 Precondition Failed` with `If-Match` may be more precise when a precondition validator fails.

---

# 189. REST and 422

For syntactically valid but semantically unprocessable content:

```text
422 Unprocessable Content
```

may be appropriate.

For example:

```json
{
  "email": "not-an-email"
}
```

The JSON syntax is valid.

The domain validation fails.

---

# 190. REST and 400

`400 Bad Request` generally communicates that the request is invalid or malformed at the HTTP/request level.

An API should distinguish:

```text
malformed request
```

from:

```text
valid request but invalid domain state
```

where appropriate.

---

# 191. REST and 401 vs 403

```text
401 Unauthorized
```

generally means authentication is required or has failed.

```text
403 Forbidden
```

means the server understood the request but refuses to fulfill it.

This distinction is important for consistent API behavior.

---

# 192. REST and 429

For rate limiting:

```http
HTTP/1.1 429 Too Many Requests
Retry-After: 60
```

is more semantically meaningful than:

```http
HTTP/1.1 200 OK

{
  "error": "rate limited"
}
```

The latter discards useful HTTP semantics.

---

# 193. REST and 503

A temporarily overloaded service can use:

```text
503 Service Unavailable
```

possibly with:

```text
Retry-After
```

This allows infrastructure and clients to distinguish:

```text
temporary server unavailability
```

from:

```text
permanent application error
```

---

# 194. REST API Design Principle

A useful rule is:

> Use HTTP's semantics instead of reinventing them inside JSON whenever HTTP already provides an appropriate semantic.

Prefer:

```text
404 Not Found
```

over:

```json
{
  "status": "error",
  "errorCode": "USER_NOT_FOUND"
}
```

while still providing application-specific error details when needed.

The ideal design often uses both:

```text
HTTP status
+
structured application error representation
```

---

# 195. REST and Self-Descriptive Error Responses

For example:

```http
HTTP/1.1 409 Conflict
Content-Type: application/problem+json
```

```json
{
  "type": "https://example.com/problems/version-conflict",
  "title": "Resource conflict",
  "status": 409,
  "detail": "The resource was modified by another client."
}
```

This combines:

```text
generic protocol semantics
```

with:

```text
application-specific explanation
```

---

# 196. REST and Content Negotiation

A REST client may request:

```http
Accept: application/json
```

while another requests:

```http
Accept: application/xml
```

The resource remains:

```text
/users/123
```

while the representation varies.

This is a powerful separation:

```text
Resource identity
       ≠
Representation format
```

---

# 197. REST and Resource Identity

A resource identifier should ideally remain stable even if:

```text
representation changes
database changes
implementation changes
server cluster changes
```

For example:

```text
/users/123
```

should continue identifying the same conceptual resource even if its representation changes from:

```text
JSON v1
```

to:

```text
JSON v2
```

---

# 198. REST and URI Stability

A URI should not normally encode transient implementation details such as:

```text
database host
server instance
internal process ID
SQL query
```

Bad:

```text
/db1/query/users?id=123
```

Better:

```text
/users/123
```

The latter represents the conceptual resource rather than its implementation.

---

# 199. REST and Resource Relationships

Relationships are an important part of hypermedia.

For example:

```text
Customer
   │
   ├── orders
   │
   └── addresses

Order
   │
   ├── customer
   ├── items
   ├── payment
   └── shipment
```

These relationships can be expressed through links.

---

# 200. REST and Domain Navigation

A client can navigate:

```text
/users/123
      │
      └── orders
             │
             ▼
       /orders/456
             │
             └── shipment
                    │
                    ▼
              /shipments/789
```

This is more than simply retrieving data.

The representation describes the client's available navigation options.

---

# 201. REST as a State Machine

A useful conceptual model is:

```text
                ┌─────────────┐
                │   Resource  │
                │   State A   │
                └──────┬──────┘
                       │
                 hypermedia
                   transition
                       │
                       ▼
                ┌─────────────┐
                │   Resource  │
                │   State B   │
                └──────┬──────┘
                       │
                 hypermedia
                   transition
                       │
                       ▼
                ┌─────────────┐
                │   Resource  │
                │   State C   │
                └─────────────┘
```

The server provides representations describing current state and available transitions.

The client moves through application state by following those controls.

This is the conceptual basis for:

```text
Hypermedia As The Engine Of Application State
```

---

# 202. Why This Matters for Client Design

A tightly coupled client may contain:

```text
URI constants
workflow rules
server assumptions
```

A hypermedia-oriented client can instead understand:

```text
link relations
media types
actions
forms
state transitions
```

This permits more independent evolution.

---

# 203. REST and HTML

HTML is arguably the canonical example of a hypermedia representation.

For example:

```html
<form action="/orders/123/payment" method="post">
    <button type="submit">Pay</button>
</form>
```

The representation contains:

```text
resource state
+
transition information
```

The browser can act on that information.

This is one of the reasons the Web itself is such a useful example of REST architecture.

---

# 204. REST and JSON APIs

JSON APIs often use:

```json
{
  "id": 123,
  "name": "Alice"
}
```

but omit:

```text
links
actions
relationships
media semantics
```

This makes them easier to implement but often more tightly coupled.

A more hypermedia-oriented representation might be:

```json
{
  "id": 123,
  "name": "Alice",
  "_links": {
    "self": {
      "href": "/users/123"
    },
    "orders": {
      "href": "/users/123/orders"
    }
  }
}
```

---

# 205. REST and API Clients

A REST client should ideally understand:

```text
HTTP
media types
link relations
status codes
method semantics
```

rather than:

```text
server's database
URI implementation patterns
private workflow assumptions
```

This reduces coupling.

---

# 206. REST and Generic Clients

One of the strongest REST properties is that generic components can understand the interface.

For example:

```text
HTTP cache
HTTP proxy
HTTP crawler
browser
generic HTTP client
```

can operate without understanding application-specific business logic.

This is possible because the interface is standardized.

---

# 207. REST and Interoperability

REST is particularly useful where multiple independent implementations must communicate.

For example:

```text
Java client
        │
        ▼
REST API
        ▲
        │
Python server
```

or:

```text
Go service
        │
        ▼
REST API
        ▲
        │
Rust client
```

The participants only need to agree on:

```text
HTTP semantics
resource model
representation formats
application-specific semantics
```

---

# 208. REST and Independent Deployment

Suppose:

```text
Client v1
```

communicates with:

```text
Server v5
```

A well-designed REST interface can allow them to interoperate despite different release cycles.

This is one of the core architectural goals of REST.

---

# 209. REST and Version Compatibility

Compatibility is improved by:

```text
stable resource identifiers
standard HTTP semantics
optional fields
backward-compatible representations
hypermedia
content negotiation
```

It is harmed by:

```text
hard-coded URI structures
hidden session state
implementation-specific behavior
mandatory representation changes
```

---

# 210. REST and the Web's Scalability

Fielding's motivation for REST was strongly tied to Internet-scale distributed systems.

The Web needed:

```text
millions of independent components
many intermediaries
large numbers of clients
unreliable networks
independent deployments
caching
security boundaries
```

REST's constraints were chosen to support these properties.

---

# 211. Why Intermediaries Are So Important

REST's architecture assumes that communication may pass through:

```text
client
 ↓
proxy
 ↓
cache
 ↓
gateway
 ↓
load balancer
 ↓
origin
```

This is fundamentally different from architectures that require:

```text
client
        │
        ▼
specific server process
```

with tightly coupled state.

---

# 212. REST and Failure Domains

Layered, stateless architectures can isolate failures.

For example:

```text
CDN failure
    ↓
origin still exists

API instance failure
    ↓
load balancer routes elsewhere

cache failure
    ↓
origin handles request
```

The architectural separation reduces the blast radius of some failures.

---

# 213. REST and Availability

REST does not guarantee high availability.

However, its constraints can make high availability easier to implement through:

```text
stateless services
horizontal scaling
load balancing
caching
intermediaries
idempotent operations
```

These are architectural benefits rather than guarantees.

---

# 214. REST and CAP/Consistency

REST does not define:

```text
strong consistency
eventual consistency
linearizability
serializability
CAP tradeoffs
```

Those are distributed data-system concerns.

A REST API can expose any of these models.

---

# 215. REST and Transactions

HTTP methods should not be confused with database transactions.

For example:

```http
POST /orders
```

does not imply:

```text
ACID transaction
```

inside the server.

The server may internally use:

```text
database transaction
```

or:

```text
Saga
```

or:

```text
eventual consistency
```

independently.

---

# 216. REST and Security Tokens

Authentication tokens should be treated as application/security mechanisms.

For example:

```http
Authorization: Bearer <token>
```

does not define REST.

It simply allows the server to identify/authorize the caller.

REST's statelessness means that the request should carry whatever authentication context is required rather than relying on hidden conversational state.

---

# 217. REST and Cookies

Cookies are compatible with HTTP and can be used in REST systems.

However, a design heavily dependent on hidden server-side session state may conflict with REST's stateless interaction constraint.

The important question is not:

```text
"Does the system use cookies?"
```

but:

```text
"Does request processing depend on hidden conversational state
stored by the server?"
```

---

# 218. REST and CSRF

CSRF is primarily relevant when browsers automatically attach credentials such as cookies.

A REST API using:

```text
Authorization: Bearer ...
```

in a non-browser client has a different threat model.

REST itself does not provide CSRF protection.

Security must be designed separately.

---

# 219. REST and CORS

CORS is a browser security mechanism.

It determines whether browser JavaScript can access responses from another origin.

CORS is:

```text
browser security policy
```

not:

```text
REST
```

A REST API may need to configure CORS because browsers consume it, but CORS does not make an API RESTful.

---

# 220. REST and Same-Origin Policy

Similarly:

```text
Same-Origin Policy
```

is a browser security constraint.

It is not part of REST.

The distinction is:

```text
REST
    distributed architecture

HTTP
    application protocol

CORS/SOP
    browser security mechanisms
```

---

# 221. REST and TLS

TLS protects the communication channel.

For HTTPS:

```text
REST semantics
      ↓
HTTP
      ↓
TLS
      ↓
TCP/QUIC
```

REST does not encrypt anything.

HTTPS provides confidentiality and integrity for the HTTP exchange.

---

# 222. REST and Authorization

Authorization belongs to application/security semantics.

For example:

```text
GET /users/123
```

might be allowed for:

```text
user 123
administrator
```

but denied for:

```text
user 456
```

The HTTP method and URI identify the operation/resource.

The application authorization layer determines whether it is permitted.

---

# 223. REST and Rate Limiting

Rate limiting is not a REST constraint.

However, a REST API can use standard HTTP semantics:

```text
429 Too Many Requests
Retry-After
```

This allows generic infrastructure to understand rate-limit failures.

---

# 224. REST and Monitoring

Because REST commonly uses standardized HTTP methods and status codes, monitoring systems can classify traffic generically:

```text
GET /users
    200 → healthy

GET /users/123
    404 → expected application failure

POST /payments
    500 → server failure
```

This is one of the practical benefits of using standardized semantics.

---

# 225. REST and Testing

REST APIs can be tested at several levels.

## Protocol tests

Verify:

```text
status codes
headers
methods
content types
caching
conditional requests
```

## Resource tests

Verify:

```text
resource creation
retrieval
modification
deletion
relationships
```

## Architectural tests

Verify:

```text
statelessness
cacheability
uniform semantics
hypermedia
```

The last category is often neglected.

---

# 226. REST Contract Testing

A REST contract can describe:

```text
resource
method
request representation
response representation
status codes
headers
links
```

Tools such as OpenAPI-based contract testing can validate much of this.

However, architectural properties such as true statelessness and HATEOAS may require deeper testing.

---

# 227. REST and API Governance

For large organizations, REST governance often standardizes:

```text
URI naming
HTTP methods
status codes
error format
pagination
authentication
authorization
versioning
idempotency
caching
correlation IDs
observability
```

These are engineering conventions layered on top of REST/HTTP.

They should not be mistaken for the formal definition of REST.

---

# 228. What REST Actually Requires

A concise formulation is:

```text
REST requires the architectural constraints.
```

It does **not** require:

```text
JSON
CRUD
microservices
OpenAPI
JWT
HTTP/1.1
HTTP/2
HTTP/3
PostgreSQL
GET/POST/PUT/DELETE specifically
```

HTTP is exceptionally suitable because it already implements many of the mechanisms needed to express those constraints.

---

# 229. REST and HTTP — Final Conceptual Model

The most useful mental model is:

```text
                 REST
                  │
       architectural style
                  │
        ┌─────────┴─────────┐
        │                   │
    Constraints          Principles
        │                   │
        ▼                   ▼
Client-server          Loose coupling
Stateless              Scalability
Cacheable              Evolvability
Uniform interface      Intermediaries
Layered system         Generic tooling
Code-on-demand*       Hypermedia
        │
        ▼
      HTTP
        │
        ├── URI
        ├── Methods
        ├── Headers
        ├── Status codes
        ├── Representations
        ├── Caching
        └── Conditional requests
        │
        ▼
HTTP/1.1 / HTTP/2 / HTTP/3
        │
        ▼
TCP / QUIC
        │
        ▼
IP
```

---

# 230. The Most Important Distinctions

If only a few concepts are remembered, they should be these.

### 1. REST is not HTTP

```text
REST = architectural style
HTTP  = protocol
```

### 2. REST is not JSON

```text
JSON = representation format
```

### 3. REST is not CRUD

```text
CRUD = application operation model
```

### 4. REST is not microservices

```text
Microservices = service decomposition architecture
```

### 5. REST is not stateless data

```text
REST statelessness = stateless interaction
```

### 6. REST does not require HTTP

HTTP is simply the dominant and highly compatible protocol for implementing REST-style systems.

### 7. HTTP does not guarantee REST

An HTTP API can be RPC-oriented, stateful, tightly coupled, or non-hypermedia-driven.

### 8. HATEOAS matters

A complete REST interpretation includes hypermedia-driven application-state transitions.

---

# 231. REST vs HTTP in One Example

Consider:

```http
GET /users/123 HTTP/1.1
Host: api.example.com
Accept: application/json
```

### HTTP tells us:

```text
GET
    = method

/users/123
    = request target

HTTP/1.1
    = protocol version

Host
    = target authority

Accept
    = representation preference
```

### REST tells us:

```text
/users/123
    = identify a resource

GET
    = use the uniform interface to retrieve its representation

application/json
    = representation format

request
    = stateless interaction

response
    = potentially cacheable

representation
    = can contain links/transitions

intermediaries
    = may process the request generically
```

That is the fundamental difference.

---

# 232. Recommended Reading Order

For a serious understanding of REST, use this order.

## 1. Fielding's Dissertation

**Roy T. Fielding — Architectural Styles and the Design of Network-based Software Architectures**

Pay particular attention to:

```text
Chapter 5 — Representational State Transfer
```

This is the primary source for REST itself.

---

## 2. RFC 9110 — HTTP Semantics

This explains:

* resources;
* representations;
* methods;
* status codes;
* fields;
* content negotiation;
* conditional requests;
* HTTP's uniform interface.

It is particularly useful because HTTP's terminology overlaps heavily with REST terminology.

---

## 3. RFC 9111 — HTTP Caching

Study:

```text
freshness
validation
ETag
Cache-Control
Vary
cache reuse
```

This helps understand REST's cacheability constraint.

---

## 4. RFC 9112 — HTTP/1.1

Study:

```text
wire syntax
message framing
headers
request/response structure
```

This connects REST/HTTP semantics to actual network messages.

---

## 5. RFC 9113 — HTTP/2

Study:

```text
streams
frames
multiplexing
header compression
flow control
```

---

## 6. RFC 9114 — HTTP/3

Study:

```text
QUIC
streams
HTTP/3 framing
QPACK
```

---

# 233. Important References

## Primary REST Source

**Fielding, Roy T. — Architectural Styles and the Design of Network-based Software Architectures**

University of California, Irvine, 2000.

The dissertation introduces REST and explains the architectural constraints behind it.

---

## HTTP Semantics

**RFC 9110 — HTTP Semantics**

Defines current HTTP concepts including:

* resources;
* representations;
* methods;
* status codes;
* fields;
* request/response semantics.

---

## HTTP Caching

**RFC 9111 — HTTP Caching**

Defines current HTTP caching semantics.

---

## HTTP/1.1

**RFC 9112 — HTTP/1.1**

Defines current HTTP/1.1 message syntax and connection management.

---

## HTTP/2

**RFC 9113 — HTTP/2**

Defines current HTTP/2 framing and protocol behavior.

---

## HTTP/3

**RFC 9114 — HTTP/3**

Defines current HTTP/3 over QUIC.

---

## PATCH

**RFC 5789 — PATCH Method for HTTP**

Defines the PATCH method.

---

## Problem Details

**RFC 9457 — Problem Details for HTTP APIs**

Defines structured error representations such as:

```text
application/problem+json
```

and:

```text
application/problem+xml
```

---

# 234. Final Summary

REST is best understood as an **architectural style for distributed systems**, not as a protocol.

Its core constraints are:

```text
Client-server
Stateless
Cacheable
Uniform interface
Layered system
Code-on-demand (optional)
```

The uniform interface itself is built around:

```text
Resource identification
        +
Manipulation through representations
        +
Self-descriptive messages
        +
Hypermedia as the engine of application state
```

HTTP provides an unusually strong foundation for implementing these principles:

```text
REST
 │
 │ architectural constraints
 ▼
HTTP
 │
 ├── URI/resource identification
 ├── methods
 ├── status codes
 ├── representations
 ├── content negotiation
 ├── caching
 ├── conditional requests
 ├── hyperlinks
 └── intermediaries
```

The most important distinction is therefore:

```text
┌───────────────────────────────────────────────┐
│ REST                                          │
│                                               │
│ Architectural style                          │
│                                               │
│ Defines constraints on how distributed        │
│ components should interact.                   │
└───────────────────────┬───────────────────────┘
                        │
                        │ can be implemented using
                        ▼
┌───────────────────────────────────────────────┐
│ HTTP                                           │
│                                               │
│ Application-layer protocol                    │
│                                               │
│ Defines concrete request/response semantics,  │
│ methods, fields, status codes, caching, etc.  │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
              HTTP/1.1 / HTTP/2 / HTTP/3
                        │
                        ▼
                  TCP / QUIC
                        │
                        ▼
                       IP
```

Consequently, the statement:

> **"REST is an OSI Layer 7 protocol."**

should be refined to:

> **REST is an application-layer architectural style. HTTP is an application-layer protocol that provides a particularly suitable implementation substrate for REST.**

That distinction is fundamental. Once it is understood, the relationship between **REST, HTTP, URIs, resources, representations, HTTP methods, status codes, caching, HATEOAS, and modern HTTP/1.1/2/3** becomes considerably clearer.
