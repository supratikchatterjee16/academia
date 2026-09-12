# Simple Object Access Protocol(SOAP)

## 1. Introduction

**SOAP** is a protocol for exchanging structured information between distributed software systems.

Unlike REST, which is an architectural style, SOAP is an actual **messaging protocol** with a formally defined message structure, processing model, extensibility mechanism, and protocol-binding framework.

SOAP is strongly associated with:

* XML
* WSDL
* [HTTP](./http.md)
* RPC-style service invocation
* enterprise web services
* strongly typed contracts
* XML Schema
* SOAP Headers
* SOAP Faults
* WS-Security
* WS-Addressing
* WS-ReliableMessaging
* WS-Policy
* MTOM
* other WS-* specifications

A useful first approximation is:

```text
SOAP
  = structured message protocol
  + XML-based message format
  + processing model
  + extensibility mechanism
  + protocol binding model
```

However, SOAP itself does **not** define everything normally associated with an enterprise web service.

For example:

```text
SOAP
  does not inherently define:
      authentication
      authorization
      encryption
      reliable delivery
      transactions
      service discovery
      routing
      business semantics

Those capabilities can be added through
separate specifications and SOAP modules/extensions.
```

This separation is one of the most important characteristics of SOAP.

---

# 2. SOAP in the Protocol Stack

A common misconception is that SOAP and HTTP are competing protocols.

They are not.

A typical SOAP-over-HTTP deployment looks approximately like:

```text
+--------------------------------------------------+
| Application semantics                            |
|                                                  |
| "CreateCustomer", "GetAccount", etc.            |
+--------------------------------------------------+
| SOAP message                                     |
|                                                  |
| Envelope                                         |
|   Header                                         |
|   Body                                           |
|   Fault                                          |
+--------------------------------------------------+
| HTTP                                              |
|                                                  |
| POST /CustomerService HTTP/1.1                   |
| Content-Type: application/soap+xml               |
| Content-Length: ...                              |
+--------------------------------------------------+
| TCP                                               |
+--------------------------------------------------+
| IP                                                |
+--------------------------------------------------+
| Ethernet / Wi-Fi / etc.                          |
+--------------------------------------------------+
```

The important distinction is:

```text
HTTP = transport/application protocol carrying the message

SOAP = message protocol carried by that transport
```

SOAP 1.2 was specifically designed around a **protocol-binding framework**, allowing SOAP messages to be exchanged using different underlying protocols. HTTP is simply the most historically common binding.

Therefore:

```text
SOAP over HTTP
SOAP over SMTP
SOAP over other transports
```

are conceptually possible.

The SOAP message itself does not fundamentally depend on HTTP.

---

# 3. Is SOAP an OSI Layer 7 Protocol?

This requires more careful terminology than simply saying:

> SOAP is Layer 7.

SOAP is an **application-layer protocol**.

Therefore it can reasonably be discussed at the OSI Layer 7 level.

A simplified stack is:

```text
OSI Layer 7
    SOAP
    HTTP
    DNS
    SMTP
    etc.

OSI Layer 4
    TCP
    UDP
    QUIC

OSI Layer 3
    IP

OSI Layer 2
    Ethernet / Wi-Fi
```

But the OSI model is conceptual, and modern Internet protocols do not always map cleanly onto individual OSI layers.

More importantly:

```text
REST ≠ protocol
SOAP = protocol
HTTP = protocol
```

REST is an architectural style.

SOAP is a defined messaging protocol.

HTTP is a defined application protocol.

---

# 4. Historical Background

SOAP emerged during the late 1990s as an attempt to standardize structured communication between distributed applications.

SOAP 1.1 was published in 2000.

The original SOAP 1.1 specification described SOAP as an XML-based mechanism for exchanging structured and typed information and included:

1. an envelope
2. encoding rules
3. RPC conventions
4. HTTP bindings

SOAP 1.2 subsequently became a W3C Recommendation in 2007.

SOAP 1.2 significantly clarified and formalized the architecture around:

* message processing
* extensibility
* protocol bindings
* message constructs
* message exchange patterns

SOAP 1.2 also explicitly stopped treating "SOAP" as an acronym.

Therefore:

```text
SOAP 1.1:
    Simple Object Access Protocol

SOAP 1.2:
    SOAP is simply the name of the protocol
```

SOAP 1.1 remains extremely important historically because many enterprise systems and libraries still use it.

---

# 5. SOAP 1.1 vs SOAP 1.2

The two versions are similar conceptually but differ in several important protocol details.

| Feature           | SOAP 1.1                                    | SOAP 1.2                                  |
| ----------------- | ------------------------------------------- | ----------------------------------------- |
| Status            | W3C Note                                    | W3C Recommendation                        |
| Namespace         | `http://schemas.xmlsoap.org/soap/envelope/` | `http://www.w3.org/2003/05/soap-envelope` |
| HTTP Content-Type | commonly `text/xml`                         | `application/soap+xml`                    |
| Action indication | `SOAPAction` HTTP header                    | `action` parameter of Content-Type        |
| Fault model       | older fault vocabulary                      | redesigned fault model                    |
| Processing model  | less formally separated                     | explicitly defined                        |
| Protocol bindings | more HTTP-oriented                          | generalized binding framework             |
| Encoding          | SOAP encoding commonly associated           | encoding separated from core framework    |

For interoperability work, **SOAP version matters**.

A SOAP 1.1 endpoint and SOAP 1.2 endpoint are not simply interchangeable because the envelope namespace and HTTP binding semantics differ.

---

# 6. The SOAP Message

At the core of SOAP is the **SOAP message**.

A SOAP 1.2 message is an XML document whose root element is:

```xml
<env:Envelope>
```

A simplified structure is:

```xml
<env:Envelope>
    <env:Header>
        ...
    </env:Header>

    <env:Body>
        ...
    </env:Body>
</env:Envelope>
```

The fundamental structure is:

```text
Envelope
├── Header       optional
└── Body         required
```

The Header can contain zero or more header blocks.

The Body contains information intended for the ultimate receiver.

A Fault is represented inside the Body.

---

# 7. SOAP 1.2 Envelope

A typical SOAP 1.2 request might look like:

```xml
<?xml version="1.0" encoding="UTF-8"?>

<soap:Envelope
    xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
    xmlns:m="http://example.com/customer">

    <soap:Header>
        ...
    </soap:Header>

    <soap:Body>

        <m:GetCustomer>
            <m:customerId>12345</m:customerId>
        </m:GetCustomer>

    </soap:Body>

</soap:Envelope>
```

The namespace prefix `soap` has no special meaning.

This:

```xml
<soap:Envelope>
```

and this:

```xml
<s:Envelope>
```

are equivalent if the prefixes resolve to the same namespace URI.

For example:

```xml
xmlns:s="http://www.w3.org/2003/05/soap-envelope"
```

is perfectly valid.

The **namespace URI**, not the prefix, identifies the SOAP vocabulary.

---

# 8. SOAP Envelope Rules

The Envelope:

* must exist
* must be the root XML element
* identifies the SOAP version through its namespace
* contains the optional Header
* contains the mandatory Body

Conceptually:

```text
XML Document
     |
     v
 SOAP Envelope
     |
     +------ Header (optional)
     |
     +------ Body (required)
```

The Body follows the Header if a Header exists.

---

# 9. SOAP Header

The SOAP Header is one of SOAP's most important architectural features.

It provides a standardized location for **message-level extensions**.

Example:

```xml
<soap:Header>

    <auth:Authentication
        xmlns:auth="http://example.com/auth">

        <auth:Username>alice</auth:Username>
        <auth:Token>...</auth:Token>

    </auth:Authentication>

</soap:Header>
```

The application payload remains in the Body.

This creates a separation:

```text
Header
    protocol/service metadata

Body
    application message
```

Examples of information that may appear in SOAP headers include:

* security credentials
* digital signatures
* encryption metadata
* message IDs
* correlation IDs
* routing information
* transaction information
* reliability information
* policy-related metadata

This extensibility model is fundamental to the later WS-* ecosystem.

---

# 10. Header Blocks

A SOAP Header can contain multiple independent blocks.

Conceptually:

```xml
<soap:Header>

    <A>...</A>

    <B>...</B>

    <C>...</C>

</soap:Header>
```

Each header block can have its own semantics.

This makes SOAP capable of supporting intermediary processing.

For example:

```text
Client
  |
  | SOAP message
  v
Security Gateway
  |
  | process security header
  v
Message Router
  |
  | process routing header
  v
Application Server
  |
  | process application body
  v
Service
```

The SOAP processing model therefore isn't simply:

```text
sender -> final application
```

It can be:

```text
sender
  |
  v
intermediary
  |
  v
intermediary
  |
  v
ultimate receiver
```

---

# 11. `mustUnderstand`

One of SOAP's important header-processing mechanisms is:

```xml
soap:mustUnderstand
```

The idea is:

> If a receiver cannot understand a mandatory header block, it must not silently ignore it.

For example:

```xml
<sec:Security
    soap:mustUnderstand="true">
    ...
</sec:Security>
```

The exact lexical representation depends on the SOAP version and schema.

The semantic purpose is more important:

```text
Header says:
    "You MUST understand/process this."

Receiver says:
    "I don't understand it."

Result:
    SOAP processing fault.
```

This prevents silent interoperability failures.

Without such a mechanism, a sender could believe:

```text
"Security policy was applied."
```

while the receiver actually did:

```text
"Security header ignored."
```

That would be dangerous.

---

# 12. SOAP Intermediaries

SOAP explicitly supports message paths containing intermediaries.

Consider:

```text
Client
  |
  v
+----------------+
| Security Node  |
+----------------+
  |
  v
+----------------+
| Router         |
+----------------+
  |
  v
+----------------+
| Service        |
+----------------+
```

Different SOAP header blocks can be intended for different nodes.

Therefore SOAP can carry both:

```text
end-to-end information
```

and

```text
hop-specific information
```

This is one reason SOAP's message model is more sophisticated than simply:

```text
HTTP POST + XML
```

---

# 13. SOAP Body

The SOAP Body contains the main message payload.

Example:

```xml
<soap:Body>

    <m:GetCustomer>
        <m:customerId>12345</m:customerId>
    </m:GetCustomer>

</soap:Body>
```

The Body can represent:

* an RPC invocation
* a document
* application data
* a response
* a fault

SOAP itself does not require every Body to represent a method invocation.

This distinction is important.

---

# 14. RPC Style

Historically, SOAP was heavily associated with RPC.

For example:

```text
GetCustomer(12345)
```

can conceptually become:

```xml
<soap:Body>

    <m:GetCustomer>
        <m:customerId>12345</m:customerId>
    </m:GetCustomer>

</soap:Body>
```

The response might be:

```xml
<soap:Body>

    <m:GetCustomerResponse>
        <m:customer>
            <m:id>12345</m:id>
            <m:name>Alice</m:name>
        </m:customer>
    </m:GetCustomerResponse>

</soap:Body>
```

This looks similar to calling a local function.

However:

```text
SOAP ≠ RPC
```

SOAP can also be used for document-oriented messaging.

---

# 15. Document Style

A document-oriented SOAP message treats the Body as a business document rather than an RPC invocation.

For example:

```xml
<soap:Body>

    <PurchaseOrder
        xmlns="http://example.com/purchase">

        <OrderId>PO-1001</OrderId>

        <Customer>
            <Id>123</Id>
        </Customer>

        <Items>
            ...
        </Items>

    </PurchaseOrder>

</soap:Body>
```

The distinction is:

```text
RPC style

    invoke operation
        |
        +-- parameters


Document style

    exchange business document
        |
        +-- document schema
```

Enterprise SOAP systems frequently use document-oriented contracts.

---

# 16. Literal vs Encoded SOAP

SOAP historically defined encoding rules.

The important distinction is:

```text
encoded
```

versus

```text
literal
```

### SOAP Encoding

SOAP encoding attempts to describe how application data structures are represented in XML.

It historically supported concepts such as:

* arrays
* compound values
* references
* polymorphic values
* typed values

### Literal

Literal means the XML representation follows an XML Schema-defined representation rather than SOAP's own encoding rules.

In modern interoperable enterprise SOAP systems, you will commonly encounter:

```text
document/literal
```

especially:

```text
document/literal wrapped
```

This is important when working with WSDL and interoperability profiles.

---

# 17. SOAP over HTTP

SOAP is frequently transported over HTTP.

A SOAP 1.1 request might look approximately like:

```http
POST /CustomerService HTTP/1.1
Host: api.example.com
Content-Type: text/xml; charset=utf-8
SOAPAction: "GetCustomer"
Content-Length: 512

<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:m="http://example.com/customer">

    <soap:Body>
        <m:GetCustomer>
            <m:customerId>12345</m:customerId>
        </m:GetCustomer>
    </soap:Body>

</soap:Envelope>
```

The HTTP layer sees:

```text
POST
URI
HTTP headers
HTTP body
```

The SOAP layer sees:

```text
Envelope
Header
Body
application message
```

These are different protocol layers.

---

# 18. SOAP 1.1 `SOAPAction`

SOAP 1.1 commonly uses:

```http
SOAPAction: "GetCustomer"
```

This HTTP header is associated with the intended SOAP action.

For example:

```http
POST /CustomerService HTTP/1.1
Content-Type: text/xml; charset=utf-8
SOAPAction: "http://example.com/GetCustomer"
```

This led to a common implementation pattern:

```text
HTTP request
      |
      +-- URI
      |
      +-- SOAPAction
      |
      +-- SOAP XML body
```

The HTTP server/framework can use `SOAPAction` to select the operation.

---

# 19. SOAP 1.2 Action

SOAP 1.2 changes the mechanism.

A SOAP 1.2 request commonly uses:

```http
Content-Type: application/soap+xml;
              charset=utf-8;
              action="http://example.com/GetCustomer"
```

Therefore:

```text
SOAP 1.1

SOAPAction:
    HTTP header


SOAP 1.2

action:
    parameter associated with application/soap+xml
```

This is an important practical interoperability distinction.

---

# 20. HTTP Status Codes vs SOAP Faults

SOAP introduces another layer of error semantics.

Suppose a SOAP service encounters:

```text
Customer does not exist.
```

That may be represented as a SOAP Fault.

HTTP also has status codes:

```http
HTTP/1.1 500 Internal Server Error
```

Therefore there can be two semantic layers:

```text
HTTP
    transport/protocol outcome

SOAP
    message/application processing outcome
```

Do not automatically equate:

```text
HTTP 500
```

with:

```text
business failure
```

or assume every SOAP error is represented only by HTTP status.

SOAP's own fault model must be considered.

---

# 21. SOAP Fault

A SOAP Fault is a standardized representation of a SOAP processing failure.

SOAP 1.2 has a structured fault model.

Conceptually:

```xml
<soap:Body>

    <soap:Fault>

        <soap:Code>
            ...
        </soap:Code>

        <soap:Reason>
            ...
        </soap:Reason>

        <soap:Node>
            ...
        </soap:Node>

        <soap:Role>
            ...
        </soap:Role>

        <soap:Detail>
            ...
        </soap:Detail>

    </soap:Fault>

</soap:Body>
```

The exact elements and semantics matter.

---

# 22. SOAP 1.2 Fault Structure

The major SOAP 1.2 Fault components are:

```text
Fault
├── Code
│   └── Value
│       └── optional Subcode
│
├── Reason
│
├── Node
│
├── Role
│
└── Detail
```

### Code

Identifies the class of failure.

Examples include:

```text
VersionMismatch
MustUnderstand
DataEncodingUnknown
Sender
Receiver
```

### Reason

Human-readable explanation.

### Node

Identifies the SOAP node that generated the fault.

### Role

Identifies the role being played by that node.

### Detail

Application-specific fault information.

---

# 23. Example SOAP 1.2 Fault

```xml
<soap:Fault>

    <soap:Code>
        <soap:Value>
            soap:Sender
        </soap:Value>
    </soap:Code>

    <soap:Reason>
        <soap:Text xml:lang="en">
            Customer ID is invalid.
        </soap:Text>
    </soap:Reason>

    <soap:Detail>

        <m:InvalidCustomerId
            xmlns:m="http://example.com/customer">

            <m:id>-1</m:id>
            <m:message>Customer ID must be positive.</m:message>

        </m:InvalidCustomerId>

    </soap:Detail>

</soap:Fault>
```

The important architectural distinction is:

```text
SOAP fault structure
        +
application-specific Detail
```

The SOAP layer provides the common fault envelope while the application can define domain-specific error information.

---

# 24. SOAP Message Exchange Patterns

SOAP messages are fundamentally one-way transmissions:

```text
Sender
  |
  | SOAP message
  v
Receiver
```

A request/response interaction is constructed from multiple message transmissions:

```text
Client
  |
  | Request
  v
Server
  |
  | Response
  v
Client
```

SOAP 1.2 defines the concept of **Message Exchange Patterns (MEPs)**.

Examples include:

```text
Request-Response
One-Way
```

Extensions can define additional patterns.

This is an important conceptual distinction:

```text
SOAP message
```

is not inherently synonymous with:

```text
HTTP request
```

or:

```text
RPC call
```

---

# 25. SOAP Protocol Binding

SOAP separates:

```text
SOAP message model
```

from:

```text
underlying transport
```

The binding defines how SOAP interacts with another protocol.

Conceptually:

```text
              SOAP
               |
       +-------+-------+
       |       |       |
      HTTP    SMTP    ...
```

A binding specifies how SOAP concepts map onto the underlying protocol.

For example:

```text
SOAP Message
     |
     v
HTTP Binding
     |
     v
HTTP Request / Response
```

This architectural separation is one of the major improvements in SOAP 1.2.

---

# 26. SOAP and XML

SOAP uses XML technologies.

A SOAP message therefore has several nested levels:

```text
Bytes
 |
 v
XML serialization
 |
 v
SOAP XML document
 |
 v
Envelope
 |
 +-- Header
 |
 +-- Body
       |
       +-- application XML
```

The application payload itself may use XML Schema-defined types.

For example:

```xml
<customer>
    <id>123</id>
    <name>Alice</name>
</customer>
```

can be constrained using XML Schema.

---

# 27. XML Schema

SOAP systems frequently rely heavily on:

**XML Schema (XSD)**.

XSD can define:

```text
elements
attributes
simple types
complex types
enumerations
restrictions
extensions
cardinality
required/optional fields
```

For example:

```xml
<xs:complexType name="Customer">
    <xs:sequence>

        <xs:element
            name="id"
            type="xs:int"/>

        <xs:element
            name="name"
            type="xs:string"/>

    </xs:sequence>
</xs:complexType>
```

This provides strong structural typing.

---

# 28. Why XML Schema Matters to SOAP

Consider a service operation:

```text
CreateCustomer(Customer)
```

Without a formal contract, the client needs to know:

```text
What fields?
What types?
Which fields are mandatory?
What order?
What response?
What faults?
What endpoint?
What binding?
```

A SOAP ecosystem can formalize these through:

```text
XSD
+
WSDL
+
SOAP
+
WS-* specifications
```

This leads directly to WSDL.

---

# 29. WSDL

**WSDL = Web Services Description Language**

WSDL describes a web service contract.

It answers questions such as:

```text
What operations exist?

What messages are exchanged?

What XML types are used?

What protocol binding is used?

Where is the service available?
```

The important conceptual distinction is:

```text
SOAP
    defines how SOAP messages work

WSDL
    describes a service contract
```

SOAP does not require WSDL.

Similarly:

```text
WSDL does not itself equal SOAP.
```

WSDL can describe services using different bindings.

---

# 30. WSDL as a Contract

A useful conceptual model is:

```text
                    WSDL
                     |
       +-------------+-------------+
       |             |             |
     Types        Operations     Binding
       |             |             |
       +-------------+-------------+
                     |
                   Endpoint
```

The client can use the WSDL to determine how to communicate with the service.

This is why SOAP systems are often called:

```text
contract-first
```

systems.

---

# 31. WSDL 1.1 Structure

WSDL 1.1 commonly uses the following major constructs:

```text
definitions
│
├── types
│
├── message
│
├── portType
│
├── binding
│
└── service
    └── port
```

These are worth understanding individually.

---

# 32. WSDL `types`

The `types` section contains data type definitions.

Typically:

```xml
<wsdl:types>

    <xsd:schema
        targetNamespace="http://example.com/customer">

        ...

    </xsd:schema>

</wsdl:types>
```

The types are usually expressed using XML Schema.

Conceptually:

```text
WSDL
 |
 +-- types
       |
       +-- XSD
             |
             +-- Customer
             +-- Address
             +-- Order
```

---

# 33. WSDL `message`

A WSDL 1.1 `message` describes a logical message.

For example:

```xml
<wsdl:message name="GetCustomerRequest">

    <wsdl:part
        name="parameters"
        element="tns:GetCustomer"/>

</wsdl:message>
```

The response may be:

```xml
<wsdl:message name="GetCustomerResponse">

    <wsdl:part
        name="parameters"
        element="tns:GetCustomerResponse"/>

</wsdl:message>
```

Think of:

```text
message
```

as describing the data exchanged for an operation.

---

# 34. WSDL `portType`

The WSDL 1.1 `portType` represents the abstract interface.

Example:

```xml
<wsdl:portType name="CustomerPortType">

    <wsdl:operation name="GetCustomer">

        <wsdl:input
            message="tns:GetCustomerRequest"/>

        <wsdl:output
            message="tns:GetCustomerResponse"/>

    </wsdl:operation>

</wsdl:portType>
```

Conceptually:

```text
portType
    |
    +-- operation
          |
          +-- input
          |
          +-- output
          |
          +-- fault
```

This is similar to an interface definition in programming.

---

# 35. WSDL `binding`

The abstract interface does not necessarily specify the concrete wire details.

The `binding` supplies those details.

For example:

```xml
<wsdl:binding
    name="CustomerSoapBinding"
    type="tns:CustomerPortType">

    ...

</wsdl:binding>
```

The binding can describe:

```text
SOAP version
style
encoding
operation mapping
transport
wire-level details
```

Conceptually:

```text
Abstract interface
       |
       v
    Binding
       |
       v
Concrete protocol representation
```

---

# 36. WSDL `service`

A WSDL service associates a service with concrete endpoints.

Example:

```xml
<wsdl:service name="CustomerService">

    <wsdl:port
        name="CustomerPort"
        binding="tns:CustomerSoapBinding">

        <soap:address
            location="https://api.example.com/customer"/>

    </wsdl:port>

</wsdl:service>
```

Conceptually:

```text
Service
   |
   +-- Port
         |
         +-- Binding
         |
         +-- Address
```

---

# 37. WSDL 1.1: Complete Conceptual Model

A useful way to remember WSDL 1.1 is:

```text
types
    What data exists?

message
    What data crosses the boundary?

portType
    What operations exist?

binding
    How are those operations represented on the wire?

service
    Where can I access them?

port
    Which endpoint implements which binding?
```

Therefore:

```text
XSD
 |
 v
Types
 |
 v
Messages
 |
 v
PortType
 |
 v
Binding
 |
 v
Service / Port
 |
 v
Endpoint
```

---

# 38. WSDL 2.0

WSDL 2.0 reorganized the conceptual model.

The major constructs are:

```text
Description
│
├── Types
│
├── Interface
│
├── Binding
│
└── Service
    └── Endpoint
```

The important conceptual mapping is roughly:

```text
WSDL 1.1       WSDL 2.0

portType   ->   interface

port        ->   endpoint

service     ->   service

binding     ->   binding
```

WSDL 2.0 explicitly separates abstract service functionality from concrete details such as binding and endpoint address.

---

# 39. WSDL 1.1 vs WSDL 2.0

| Concept             | WSDL 1.1    | WSDL 2.0                                     |
| ------------------- | ----------- | -------------------------------------------- |
| Abstract interface  | `portType`  | `interface`                                  |
| Operation           | `operation` | `operation`                                  |
| Message             | `message`   | modeled through interface/message references |
| Concrete protocol   | `binding`   | `binding`                                    |
| Endpoint            | `port`      | `endpoint`                                   |
| Service             | `service`   | `service`                                    |
| XML Schema          | Common      | Common                                       |
| Industry prevalence | Very high   | Lower historically                           |

In practical enterprise environments, **WSDL 1.1 remains extremely important** despite WSDL 2.0 being the newer W3C specification.

---

# 40. Example WSDL 1.1

A simplified WSDL might look like:

```xml
<?xml version="1.0"?>

<wsdl:definitions
    xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
    xmlns:tns="http://example.com/customer"
    targetNamespace="http://example.com/customer">

    <wsdl:types>

        <xsd:schema
            targetNamespace="http://example.com/customer">

            <xsd:element
                name="GetCustomer">
                ...
            </xsd:element>

        </xsd:schema>

    </wsdl:types>


    <wsdl:message name="GetCustomerRequest">
        ...
    </wsdl:message>


    <wsdl:message name="GetCustomerResponse">
        ...
    </wsdl:message>


    <wsdl:portType name="CustomerPortType">

        <wsdl:operation name="GetCustomer">

            <wsdl:input
                message="tns:GetCustomerRequest"/>

            <wsdl:output
                message="tns:GetCustomerResponse"/>

        </wsdl:operation>

    </wsdl:portType>


    <wsdl:binding
        name="CustomerSoapBinding"
        type="tns:CustomerPortType">

        ...

    </wsdl:binding>


    <wsdl:service name="CustomerService">

        <wsdl:port
            name="CustomerPort"
            binding="tns:CustomerSoapBinding">

            <soap:address
                location="https://api.example.com/customer"/>

        </wsdl:port>

    </wsdl:service>

</wsdl:definitions>
```

The actual WSDL can be considerably more complicated because of imported schemas, policies, WS-Addressing, security requirements, multiple bindings, and faults.

---

# 41. Contract-First Development

A major SOAP development model is:

```text
WSDL
 |
 v
Generate client/server artifacts
 |
 v
Implement business logic
```

For example:

```text
customer.wsdl
      |
      v
WSDL compiler
      |
      +----> client proxy
      |
      +----> server skeleton
      |
      +----> XML types
      |
      +----> service interfaces
```

The generated proxy might allow code such as:

```java
Customer customer =
    customerClient.getCustomer(12345);
```

while the framework handles:

```text
Java object
   |
   v
XML serialization
   |
   v
SOAP Envelope
   |
   v
HTTP
```

This is one reason SOAP can appear to behave like local procedure calls.

---

# 42. Generated Client Proxies

A SOAP client often consists of:

```text
Application
     |
     v
Generated Proxy
     |
     v
SOAP Runtime
     |
     v
HTTP Client
     |
     v
Network
```

The programmer may only see:

```text
client.getCustomer(12345)
```

while underneath:

```text
object
  -> XML
  -> SOAP
  -> HTTP
  -> TCP
  -> server
```

The server reverses this:

```text
HTTP
  -> SOAP
  -> XML parsing
  -> deserialization
  -> dispatch
  -> service method
```

---

# 43. SOAP Processing Model

A SOAP node processes a SOAP message.

Conceptually:

```text
Receive bytes
      |
      v
Parse XML
      |
      v
Identify SOAP version
      |
      v
Process Envelope
      |
      v
Identify applicable headers
      |
      v
Process mandatory headers
      |
      v
Process Body
      |
      v
Invoke application processing
```

An intermediary may process only the headers intended for its role and forward the message.

---

# 44. SOAP Node Roles

SOAP defines concepts around message-processing nodes.

A simplified model:

```text
Initial Sender
       |
       v
Intermediary
       |
       v
Ultimate Receiver
```

The ultimate receiver is the final intended SOAP node.

Intermediaries can perform functions such as:

```text
routing
security processing
logging
validation
reliability
transaction processing
```

These are generally implemented through SOAP modules/specifications rather than being hard-coded into the SOAP core.

---

# 45. SOAP Extensibility

One of SOAP's strongest characteristics is extensibility.

The core SOAP framework intentionally does not try to solve every distributed-systems problem.

Instead:

```text
SOAP Core
    |
    +-- Security
    |
    +-- Addressing
    |
    +-- Reliability
    |
    +-- Transactions
    |
    +-- Policy
    |
    +-- Attachments
    |
    +-- Other features
```

This resulted in the large family commonly called:

```text
WS-*
```

---

# 46. The WS-* Ecosystem

"WS-*" is not one specification.

It is a family of related specifications.

Some historically important members include:

```text
WS-Security
WS-Addressing
WS-ReliableMessaging
WS-Policy
WS-Coordination
WS-AtomicTransaction
WS-Trust
WS-SecureConversation
WS-Notification
```

Not every SOAP deployment uses all of these.

A better mental model is:

```text
SOAP
 |
 +-- optional feature specifications
       |
       +-- security
       +-- addressing
       +-- reliability
       +-- policy
       +-- transactions
       +-- etc.
```

---

# 47. WS-Security

**WS-Security** provides SOAP-level mechanisms for message security.

It addresses concerns such as:

* message integrity
* message confidentiality
* security tokens
* signatures
* encryption

This is fundamentally different from simply using TLS.

---

# 48. TLS vs WS-Security

Suppose:

```text
Client
   |
   | TLS
   v
Gateway
   |
   | internal network
   v
Service
```

TLS protects the communication channel.

The gateway terminates TLS:

```text
Client ==TLS==> Gateway
Gateway -------=> Service
```

The original end-to-end message may no longer have transport-level protection.

WS-Security can instead protect portions of the SOAP message itself.

Conceptually:

```text
SOAP Envelope
   |
   +-- Security Header
   |      |
   |      +-- Signature
   |      +-- Encryption
   |      +-- Token
   |
   +-- Body
```

Therefore:

```text
TLS

protects:
    connection/channel


WS-Security

protects:
    SOAP message/content
```

The two can be used together.

---

# 49. Digital Signatures

A SOAP message can carry XML Signature information.

Conceptually:

```text
SOAP Body
    |
    v
Canonicalization
    |
    v
Digest
    |
    v
Digital Signature
```

A receiver can verify:

```text
Was the message modified?

Who signed it?

Which parts were signed?
```

This is particularly useful in multi-hop systems.

---

# 50. Message-Level Encryption

WS-Security can also support XML encryption.

Conceptually:

```text
SOAP Envelope
 |
 +-- Header
 |
 +-- Body
      |
      +-- encrypted content
```

This can allow only selected portions of the message to be encrypted.

That is fundamentally different from transport encryption:

```text
TLS:
    encrypt network connection

Message-level encryption:
    encrypt message content
```

---

# 51. Security Tokens

WS-Security supports mechanisms for carrying security credentials.

Examples include:

```text
UsernameToken
X.509 certificates
SAML assertions
Kerberos-related tokens
```

The exact mechanism depends on the profile and deployment.

This enables a message to carry security context along with the message itself.

---

# 52. WS-Addressing

HTTP already provides an address:

```http
POST /CustomerService
Host: api.example.com
```

But distributed messaging can require more than a transport-level URI.

**WS-Addressing** introduces message-level addressing concepts.

For example:

```xml
<wsa:MessageID>
    uuid:...
</wsa:MessageID>

<wsa:To>
    https://api.example.com/customer
</wsa:To>

<wsa:Action>
    http://example.com/GetCustomer
</wsa:Action>

<wsa:ReplyTo>
    ...
</wsa:ReplyTo>
```

These allow message addressing information to be represented independently of the underlying transport.

---

# 53. Why Message-Level Addressing Matters

Suppose:

```text
Client
   |
   v
Message Queue
   |
   v
Router
   |
   v
Service
```

The original message may not have a direct HTTP connection to the ultimate recipient.

WS-Addressing allows the message itself to contain information such as:

```text
Message ID
Destination
Action
Reply endpoint
Fault endpoint
Relationship
```

This makes the messaging model less dependent on HTTP.

---

# 54. WS-ReliableMessaging

Network communication can fail.

For example:

```text
Client
  |
  | message
  v
Network
  X
```

The sender needs to know:

```text
Was it delivered?
Was it duplicated?
Was it delivered in order?
```

**WS-ReliableMessaging** provides a protocol for reliable message transfer across failures, including mechanisms for identifying and managing message sequences. It is designed to be transport-independent and includes a SOAP binding.

This can address requirements such as:

```text
reliable delivery
duplicate detection
message ordering
```

---

# 55. Why HTTP/TCP Reliability Is Not Enough

TCP provides:

```text
ordered byte stream
retransmission
connection reliability
```

But TCP does not tell an application:

```text
"Your business message was processed exactly once."
```

Consider:

```text
Client
  |
  | CreatePayment
  v
Server
  |
  | processes payment
  |
  X response lost
  |
Client timeout
```

The client cannot automatically know whether:

```text
payment failed
```

or:

```text
payment succeeded but response was lost
```

Application-level reliable messaging and idempotency are therefore different from TCP reliability.

---

# 56. WS-Policy

WS-Policy allows services to express requirements and capabilities.

Conceptually:

```text
Service policy:

    Must use WS-Security

    Must sign SOAP Body

    Must encrypt specific elements

    Must use a particular token

    Must support a particular binding
```

A client can use the policy to determine how it must interact with the service.

Therefore:

```text
WSDL
    describes service interface

WS-Policy
    describes applicable requirements/capabilities
```

They can be combined.

---

# 57. WS-Transaction Specifications

Enterprise systems sometimes need distributed transaction semantics.

The WS-* ecosystem historically included specifications such as:

```text
WS-Coordination
WS-AtomicTransaction
WS-BusinessActivity
```

These address distributed coordination and transaction scenarios.

They should not be confused with database transactions.

A database transaction might be:

```text
BEGIN
UPDATE A
UPDATE B
COMMIT
```

A distributed transaction can involve:

```text
Service A
     |
     +---- Service B
     |
     +---- Service C
```

and therefore requires coordination across distributed participants.

---

# 58. Attachments

XML is inefficient for some binary payloads.

Suppose a SOAP operation needs to transfer:

```text
PDF
image
video
large binary document
```

Base64 encoding can represent binary data inside XML:

```xml
<document>
    JVBERi0xLjQK...
</document>
```

but increases size and requires XML processing.

SOAP systems therefore developed attachment mechanisms.

---

# 59. MTOM

**MTOM = Message Transmission Optimization Mechanism**

MTOM allows binary data to be transmitted efficiently while still being represented logically as part of the SOAP message.

Conceptually:

```text
SOAP XML
   |
   +-- logical reference to binary content
   |
   +----------------------+
                          |
                          v
                    Binary attachment
```

The binary data does not need to be base64-encoded directly into the XML representation.

MTOM is particularly important when SOAP services exchange:

```text
large documents
images
files
binary business data
```

---

# 60. SOAP Message Structure with WS-* Extensions

A realistic enterprise SOAP message may look conceptually like:

```xml
<soap:Envelope>

    <soap:Header>

        <!-- WS-Addressing -->
        <wsa:MessageID>
            uuid:...
        </wsa:MessageID>

        <wsa:To>
            ...
        </wsa:To>

        <wsa:Action>
            ...
        </wsa:Action>

        <!-- WS-Security -->
        <wsse:Security>
            ...
        </wsse:Security>

        <!-- Reliability -->
        <wsrm:Sequence>
            ...
        </wsrm:Sequence>

    </soap:Header>

    <soap:Body>

        <m:GetCustomer>
            ...
        </m:GetCustomer>

    </soap:Body>

</soap:Envelope>
```

This illustrates the fundamental SOAP design:

```text
Core SOAP
    +
modular extensions
```

---

# 61. SOAP vs HTTP

This distinction is essential.

| SOAP                                 | HTTP                               |
| ------------------------------------ | ---------------------------------- |
| Message protocol                     | Application protocol               |
| XML message model                    | HTTP message model                 |
| Envelope/Header/Body                 | Start-line/fields/content          |
| SOAP Fault                           | HTTP status code                   |
| SOAP headers                         | HTTP headers                       |
| Can be bound to HTTP                 | Can carry many payload types       |
| Defines processing model             | Defines request/response semantics |
| Supports SOAP-specific extensions    | Supports HTTP extensions           |
| Can theoretically use other bindings | Not dependent on SOAP              |

Example:

```http
POST /customer HTTP/1.1
Content-Type: application/soap+xml
```

The above is an HTTP request.

Its body may contain:

```xml
<soap:Envelope>
    ...
</soap:Envelope>
```

That XML is the SOAP message.

---

# 62. SOAP vs REST

The distinction is even more important.

```text
REST
    architectural style

SOAP
    protocol
```

REST commonly uses:

```text
HTTP
```

SOAP can use:

```text
HTTP
```

Therefore:

```text
REST over HTTP

and

SOAP over HTTP
```

are completely different architectural/protocol approaches.

---

# 63. REST Resource Model vs SOAP Operation Model

REST generally starts with:

```text
Resource
```

For example:

```text
/customer/123
```

Operations are expressed using HTTP methods:

```http
GET /customer/123
PUT /customer/123
DELETE /customer/123
```

SOAP commonly starts with:

```text
Service operation
```

For example:

```text
GetCustomer
CreateCustomer
UpdateCustomer
DeleteCustomer
```

The request may be:

```xml
<GetCustomer>
    <customerId>123</customerId>
</GetCustomer>
```

Therefore:

```text
REST:

resource-oriented


SOAP:

service/operation-oriented
```

This is a simplification, because SOAP can also be document-oriented rather than RPC-oriented.

---

# 64. REST and SOAP Are Not Opposite Protocol Versions

It is incorrect to think:

```text
HTTP  -> REST
HTTP  -> SOAP
```

as though REST and SOAP were competing versions of HTTP.

A better model is:

```text
              Application architecture
                       |
             +---------+---------+
             |                   |
           REST                Other
             |
             v
            HTTP
```

and independently:

```text
            SOAP
             |
             v
       protocol binding
             |
             v
            HTTP
```

Therefore HTTP can participate in both.

---

# 65. SOAP and REST: Detailed Comparison

| Property                | REST                          | SOAP                           |
| ----------------------- | ----------------------------- | ------------------------------ |
| Nature                  | Architectural style           | Protocol                       |
| Core abstraction        | Resource                      | Message / operation / document |
| Typical transport       | HTTP                          | HTTP, potentially others       |
| Typical format          | JSON, XML, etc.               | XML                            |
| Contract                | Optional                      | Often WSDL                     |
| Interface style         | Uniform interface             | Explicit operations            |
| Errors                  | HTTP status + representation  | SOAP Fault + transport status  |
| Security                | Usually TLS + HTTP mechanisms | TLS and/or WS-Security         |
| Reliability             | Application design            | WS-ReliableMessaging etc.      |
| Addressing              | HTTP URI                      | URI + optional WS-Addressing   |
| Binary data             | HTTP mechanisms               | MTOM/SWA etc.                  |
| Extensibility           | HTTP/media type mechanisms    | SOAP headers/modules/WS-*      |
| Hypermedia              | REST constraint               | Not intrinsic                  |
| Strong schema contracts | Optional                      | Common                         |
| Generated clients       | Optional                      | Very common                    |
| Enterprise WS-* stack   | No                            | Yes                            |

---

# 66. SOAP Is Not "Just XML over HTTP"

This statement is common but incomplete.

A very simple SOAP deployment may look like:

```text
HTTP
 +
XML
```

but SOAP defines significantly more:

```text
SOAP
 |
 +-- Envelope
 |
 +-- Header processing
 |
 +-- Body
 |
 +-- Faults
 |
 +-- Processing model
 |
 +-- Message Exchange Patterns
 |
 +-- Protocol binding framework
 |
 +-- Extensibility model
```

Furthermore, enterprise SOAP commonly incorporates:

```text
WSDL
XML Schema
WS-Security
WS-Addressing
WS-ReliableMessaging
WS-Policy
MTOM
etc.
```

Therefore:

```text
XML over HTTP
```

is not necessarily SOAP.

For example:

```http
POST /api HTTP/1.1
Content-Type: application/xml
```

with arbitrary XML in the body does not automatically constitute SOAP.

---

# 67. SOAP Request Processing — End to End

Consider:

```text
Application
    |
    | getCustomer(123)
    v
Generated Proxy
    |
    | serialize parameters
    v
SOAP Runtime
    |
    | create Envelope
    | create Headers
    | create Body
    v
XML Serializer
    |
    v
HTTP Client
    |
    v
TCP / TLS
    |
    v
Network
```

At the server:

```text
Network
    |
    v
TLS
    |
    v
HTTP Server
    |
    v
SOAP Runtime
    |
    +-- parse Envelope
    |
    +-- process Headers
    |
    +-- verify security
    |
    +-- verify addressing
    |
    +-- verify reliability
    |
    +-- deserialize Body
    |
    v
Service Dispatch
    |
    v
Business Logic
```

The response reverses the process.

---

# 68. Byte-Level View of SOAP over HTTP

At the wire, SOAP over HTTP still consists of HTTP bytes.

For example:

```text
50 4F 53 54 20 2F 63 75 73 74 6F 6D 65 72 ...
```

which begins:

```text
POST /customer ...
```

The HTTP body then contains bytes representing XML.

For example:

```text
3C 73 6F 61 70 3A 45 6E 76 65 6C 6F 70 65 ...
```

which corresponds to:

```xml
<soap:Envelope...
```

Thus:

```text
HTTP
    sees:
        byte sequence

SOAP
    interprets:
        XML SOAP message
```

SOAP does not replace HTTP's byte transport.

It defines the semantics of the payload and message processing.

---

# 69. SOAP over HTTP/1.1

Conceptually:

```text
HTTP/1.1 message
│
├── Request line
├── HTTP headers
├── blank line
└── SOAP XML bytes
```

For example:

```http
POST /service HTTP/1.1
Host: example.com
Content-Type: application/soap+xml
Content-Length: 800

<soap:Envelope>
    ...
</soap:Envelope>
```

The HTTP parser stops interpreting at the HTTP message boundary.

The SOAP implementation then receives the entity/content bytes.

---

# 70. SOAP over HTTP/2

SOAP is not intrinsically tied to HTTP/1.1.

SOAP can be transported using HTTP/2 infrastructure when the relevant binding and implementation support it.

The conceptual layers remain:

```text
SOAP XML message
       |
       v
HTTP/2
       |
       v
TLS
       |
       v
TCP
```

HTTP/2 changes the HTTP wire framing:

```text
HTTP/1.1
    text-oriented message syntax


HTTP/2
    binary frames
    streams
    multiplexing
    HPACK
```

but does not fundamentally change the SOAP envelope.

---

# 71. SOAP and HTTP/3

The same conceptual separation applies to HTTP/3:

```text
SOAP
  |
  v
HTTP/3
  |
  v
QUIC
  |
  v
UDP
  |
  v
IP
```

The SOAP message model does not become an HTTP/3 protocol.

HTTP/3 changes the transport/application framing beneath the SOAP interaction.

---

# 72. SOAP and Stateful Applications

SOAP itself does not make an application stateless.

For example:

```text
SOAP request
    |
    v
Server session
    |
    +-- server-side state
```

can exist.

SOAP can carry:

```text
session ID
correlation ID
security context
transaction context
```

through headers or application data.

This differs from REST's formal stateless architectural constraint.

---

# 73. SOAP and Idempotency

SOAP does not automatically make operations idempotent.

Consider:

```text
CreatePayment()
```

If the client retries:

```text
CreatePayment()
```

the operation might execute twice.

Enterprise SOAP systems can address this using:

```text
message identifiers
reliable messaging
application-level idempotency keys
transaction mechanisms
```

The important principle is:

```text
transport reliability
    ≠
business operation idempotency
```

---

# 74. SOAP and Transactions

SOAP itself does not automatically provide ACID transactions.

A distributed transaction requires additional mechanisms.

Conceptually:

```text
SOAP
 |
 +-- transaction-related WS-* specifications
```

rather than:

```text
SOAP = transaction protocol
```

This distinction is important when reading enterprise architecture diagrams.

---

# 75. SOAP and Service Discovery

SOAP does not inherently define:

```text
Where can I discover services?
```

Historically, SOAP ecosystems included technologies such as:

```text
UDDI
```

for service discovery.

In modern deployments, service locations are more commonly supplied through:

```text
WSDL
configuration
service registries
DNS
API gateways
enterprise service infrastructure
```

Discovery is therefore separate from the core SOAP message protocol.

---

# 76. SOAP and RESTful HTTP Semantics

SOAP often uses:

```http
POST
```

for many operations.

For example:

```http
POST /CustomerService
```

could carry:

```xml
<GetCustomer>
```

or:

```xml
<DeleteCustomer>
```

or:

```xml
<CreateCustomer>
```

The operation is represented in the SOAP message.

REST instead attempts to exploit HTTP's standardized method semantics:

```http
GET
POST
PUT
PATCH
DELETE
```

Therefore:

```text
SOAP:
    operation semantics inside SOAP message


REST:
    operation semantics strongly tied to HTTP method semantics
```

---

# 77. SOAP and HTTP Caching

HTTP provides caching semantics.

SOAP messages are generally much less naturally cacheable because many SOAP operations are:

```text
POST
```

and may represent commands or RPC operations.

For example:

```text
POST /CustomerService
<GetCustomer/>
```

does not automatically provide the same cache semantics as:

```http
GET /customers/123
```

This is one reason REST's use of HTTP semantics can be advantageous for cacheable resource retrieval.

---

# 78. SOAP and Content Negotiation

REST commonly uses HTTP content negotiation:

```http
Accept: application/json
```

SOAP generally has a more strongly defined XML contract through:

```text
WSDL
+
XML Schema
+
SOAP binding
```

SOAP 1.2 normally uses:

```http
Content-Type: application/soap+xml
```

The message's XML schema determines the structure of the payload.

---

# 79. SOAP Namespaces

Namespaces are essential to SOAP.

For example:

```xml
xmlns:soap=
    "http://www.w3.org/2003/05/soap-envelope"
```

and:

```xml
xmlns:m=
    "http://example.com/customer"
```

allow the document to distinguish:

```text
SOAP vocabulary
```

from:

```text
application vocabulary
```

The namespace URI is the identifier.

The prefix is merely syntactic shorthand.

Therefore:

```xml
<s:Envelope>
```

and:

```xml
<soap:Envelope>
```

can mean exactly the same thing.

---

# 80. SOAP Version Identification

SOAP version is determined by the envelope namespace.

SOAP 1.1:

```text
http://schemas.xmlsoap.org/soap/envelope/
```

SOAP 1.2:

```text
http://www.w3.org/2003/05/soap-envelope
```

Therefore a SOAP processor can identify the SOAP version from the envelope namespace.

This is analogous to protocol version identifiers elsewhere in network protocols.

---

# 81. SOAP Message Processing Errors

A SOAP processor may fail before application business logic executes.

For example:

```text
Malformed XML
     |
     v
XML parsing failure

Unknown mandatory header
     |
     v
MustUnderstand failure

Wrong SOAP namespace
     |
     v
VersionMismatch

Invalid message structure
     |
     v
SOAP processing failure
```

Only after SOAP processing succeeds does the application operation necessarily execute.

This creates a useful conceptual pipeline:

```text
Transport validation
        |
        v
XML validation/parsing
        |
        v
SOAP processing
        |
        v
SOAP extension processing
        |
        v
Application processing
```

---

# 82. SOAP Fault vs Business Error

Consider:

```text
GetCustomer(123)
```

and suppose customer 123 does not exist.

There are several possible designs.

### SOAP Fault

```text
SOAP processing result:
    Fault
        Detail:
            CustomerNotFound
```

### Successful SOAP response carrying a business result

```text
<GetCustomerResponse>
    <status>NOT_FOUND</status>
</GetCustomerResponse>
```

The appropriate design depends on the contract.

A fault generally represents an error condition at the SOAP/service contract level, while application-specific result structures can represent ordinary business outcomes.

---

# 83. WSDL Faults

WSDL can formally describe operation faults.

Conceptually:

```xml
<wsdl:operation name="GetCustomer">

    <wsdl:input
        message="tns:GetCustomerRequest"/>

    <wsdl:output
        message="tns:GetCustomerResponse"/>

    <wsdl:fault
        name="CustomerNotFound"
        message="tns:CustomerNotFoundFault"/>

</wsdl:operation>
```

This lets generated client libraries potentially expose typed exceptions.

For example:

```java
try {
    client.getCustomer(123);
}
catch (CustomerNotFoundException e) {
    ...
}
```

The exact programming-language representation depends on the SOAP toolchain.

---

# 84. Strong Contract Typing

A typical SOAP contract can define:

```text
Operation
    |
    +-- input message
    |
    +-- output message
    |
    +-- fault messages
```

and:

```text
Message
    |
    +-- XML elements
    |
    +-- XML Schema types
```

This creates a strongly described interface:

```text
WSDL
 +
XSD
 =
formal service contract
```

This is one of the biggest reasons SOAP became important in large enterprise environments.

---

# 85. Stub Generation

Given:

```text
service.wsdl
```

a tool can generate:

```text
Client
    |
    +-- Proxy
    +-- Request types
    +-- Response types
    +-- Fault types
```

and potentially:

```text
Server
    |
    +-- Interface
    +-- Request deserializers
    +-- Response serializers
```

This dramatically reduces manual protocol implementation.

---

# 86. Why SOAP Can Be Attractive in Large Enterprises

SOAP is particularly strong when an organization needs:

```text
formal contracts
strong XML schemas
generated clients
message-level security
standardized headers
reliable messaging
formal policies
transaction coordination
intermediaries
complex enterprise integration
```

The trade-off is complexity.

A simple service may become:

```text
WSDL
+
XSD
+
SOAP
+
WS-Security
+
WS-Addressing
+
WS-Policy
+
WS-ReliableMessaging
```

This is powerful but significantly more complicated than:

```text
HTTP
+
JSON
```

---

# 87. SOAP Complexity

SOAP's architecture can become layered:

```text
                   Application
                       |
                       v
                      WSDL
                       |
             +---------+---------+
             |                   |
           SOAP                XSD
             |
       +-----+-----+
       |     |     |
    Security Addr Reliability
       |     |     |
       +-----+-----+
             |
             v
            HTTP
             |
             v
            TLS
             |
             v
            TCP
```

This is both SOAP's strength and weakness.

You can compose sophisticated capabilities.

But every additional specification introduces:

```text
more metadata
more processing
more configuration
more interoperability considerations
more failure modes
```

---

# 88. SOAP Performance Considerations

SOAP's main performance costs traditionally come from:

```text
XML verbosity
XML parsing
schema validation
serialization/deserialization
namespace processing
security processing
signature generation
encryption
large message envelopes
```

For example:

```json
{"id":123,"name":"Alice"}
```

is considerably smaller than a deeply namespaced XML document representing the same logical data.

This does not mean SOAP is inherently slow.

A SOAP service can be highly performant.

It means:

```text
SOAP optimizes for standardized enterprise messaging features,
not minimum message size.
```

---

# 89. XML Parsing Security

SOAP applications must consider XML-specific security risks.

Important categories include:

```text
XXE
XML entity expansion
XML bombs
oversized messages
deeply nested XML
signature wrapping attacks
parser resource exhaustion
```

Modern parsers and SOAP frameworks generally provide defenses, but secure configuration remains important.

---

# 90. XML Signature Wrapping

SOAP's extensibility and XML signature model introduce specialized security concerns.

A simplified attack pattern is:

```text
Signed SOAP element
       |
       +---- attacker moves/copies element
       |
       v
Application processes a different element
```

The cryptographic signature may still validate against the original signed element while application logic processes attacker-controlled content.

Therefore:

```text
"Signature validates"
```

does not automatically imply:

```text
"Application processed exactly the intended element."
```

SOAP security implementations need correct signature-reference and processing semantics.

---

# 91. WS-Security vs OAuth

These technologies operate at different architectural levels.

OAuth is primarily an authorization framework.

WS-Security is a SOAP message-security framework.

They are not direct substitutes.

A SOAP enterprise system may use:

```text
TLS
+
WS-Security
+
SAML
```

while a modern HTTP API might use:

```text
TLS
+
OAuth 2.0
+
JWT
```

The choice depends on architecture and trust boundaries.

---

# 92. SOAP and Microservices

SOAP predates the modern microservices movement.

It can technically be used in microservice architectures:

```text
Service A
    |
    | SOAP
    v
Service B
```

but its ecosystem is more commonly associated with:

```text
enterprise integration
SOA
legacy enterprise applications
B2B systems
financial systems
telecommunications
government systems
```

The protocol itself does not require a particular deployment architecture.

---

# 93. SOAP and Service-Oriented Architecture

SOAP and SOA are frequently conflated.

They are not equivalent.

```text
SOA
    architectural approach

SOAP
    messaging protocol
```

SOA can use SOAP.

SOAP can be used without implementing a complete SOA architecture.

Similarly:

```text
REST ≠ SOA
SOAP ≠ SOA
```

They exist at different conceptual levels.

---

# 94. SOAP and RPC

RPC means:

```text
Remote Procedure Call
```

SOAP can encode RPC-style interactions.

For example:

```text
GetCustomer(123)
```

can be represented as a SOAP message.

But:

```text
SOAP ≠ RPC
```

SOAP can carry document-oriented messages and arbitrary structured information.

---

# 95. SOAP and gRPC

SOAP and gRPC have some conceptual similarities:

```text
formal contracts
generated clients
generated servers
strongly defined messages
RPC-style operations
```

but their protocol stacks are very different.

Typical gRPC:

```text
Protocol Buffers
+
HTTP/2
+
gRPC semantics
```

Typical SOAP:

```text
XML Schema
+
WSDL
+
SOAP
+
HTTP
+
WS-* extensions
```

gRPC generally emphasizes:

```text
compact binary serialization
high-performance RPC
modern service-to-service communication
```

SOAP emphasizes:

```text
formal XML contracts
extensible message headers
enterprise WS-* specifications
interoperable message-level features
```

---

# 96. SOAP and GraphQL

GraphQL is also not simply an alternative version of SOAP.

GraphQL provides:

```text
query language
schema
execution model
```

A typical GraphQL request is:

```graphql
query {
    customer(id: 123) {
        id
        name
    }
}
```

SOAP instead typically uses:

```text
operation
+
strong XML message schema
+
WSDL contract
```

They solve different problems.

---

# 97. SOAP and WebSockets

WebSockets provide:

```text
persistent bidirectional communication
```

SOAP primarily provides:

```text
structured message exchange
```

A SOAP system does not inherently provide a WebSocket-style full-duplex channel.

Again:

```text
SOAP
    message protocol


WebSocket
    communication protocol
```

They can theoretically be combined through appropriate bindings or application frameworks, but they address different concerns.

---

# 98. SOAP and JSON

SOAP's canonical representation is XML.

For example:

```xml
<soap:Envelope>
    <soap:Body>
        ...
    </soap:Body>
</soap:Envelope>
```

JSON is not the normal SOAP message representation.

Therefore:

```text
REST API
    commonly:
        JSON


SOAP service
    normally:
        XML
```

The distinction is not merely stylistic.

SOAP's XML representation supports:

```text
namespaces
XML Schema
XML Signature
XML Encryption
structured headers
formal XML contracts
```

which form a large part of the SOAP ecosystem.

---

# 99. SOAP and HTTP Methods

SOAP-over-HTTP commonly uses:

```http
POST
```

The actual operation is usually represented inside the SOAP message.

For example:

```http
POST /CustomerService
```

with:

```xml
<GetCustomer>
```

inside the SOAP Body.

This differs from REST:

```http
GET /customers/123
```

where the HTTP method itself carries standardized semantics.

---

# 100. SOAP URI vs REST URI

In REST:

```text
/customers/123
```

is normally interpreted as identifying a resource.

In SOAP:

```text
/CustomerService
```

may identify a service endpoint.

The operation can then be:

```xml
<GetCustomer>
```

inside the SOAP message.

Therefore:

```text
REST URI:
    commonly resource-oriented


SOAP endpoint:
    commonly service-oriented
```

---

# 101. A Complete SOAP Request

Consider:

```http
POST /CustomerService HTTP/1.1
Host: api.example.com
Content-Type: application/soap+xml; charset=utf-8
Content-Length: 1000
```

Body:

```xml
<?xml version="1.0" encoding="UTF-8"?>

<soap:Envelope
    xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
    xmlns:wsa="http://www.w3.org/2005/08/addressing"
    xmlns:wsse="http://docs.oasis-open.org/wss/..."
    xmlns:m="http://example.com/customer">

    <soap:Header>

        <wsa:MessageID>
            uuid:12345678
        </wsa:MessageID>

        <wsa:To>
            https://api.example.com/CustomerService
        </wsa:To>

        <wsa:Action>
            http://example.com/customer/GetCustomer
        </wsa:Action>

        <wsse:Security>
            ...
        </wsse:Security>

    </soap:Header>

    <soap:Body>

        <m:GetCustomer>
            <m:customerId>12345</m:customerId>
        </m:GetCustomer>

    </soap:Body>

</soap:Envelope>
```

This one message can therefore contain:

```text
HTTP
    transport/application protocol

SOAP
    messaging framework

WS-Addressing
    message addressing

WS-Security
    message security

Application XML
    business request
```

This layered composition is central to SOAP.

---

# 102. A Complete SOAP Response

Conceptually:

```http
HTTP/1.1 200 OK
Content-Type: application/soap+xml; charset=utf-8
```

Body:

```xml
<soap:Envelope
    xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
    xmlns:m="http://example.com/customer">

    <soap:Header>
        ...
    </soap:Header>

    <soap:Body>

        <m:GetCustomerResponse>

            <m:customer>

                <m:id>12345</m:id>

                <m:name>Alice</m:name>

                <m:email>
                    alice@example.com
                </m:email>

            </m:customer>

        </m:GetCustomerResponse>

    </soap:Body>

</soap:Envelope>
```

The SOAP response remains an XML document with the same envelope structure.

---

# 103. SOAP Fault Response

An error could instead result in:

```http
HTTP/1.1 500 Internal Server Error
Content-Type: application/soap+xml
```

Body:

```xml
<soap:Envelope
    xmlns:soap="http://www.w3.org/2003/05/soap-envelope">

    <soap:Body>

        <soap:Fault>

            <soap:Code>
                <soap:Value>
                    soap:Sender
                </soap:Value>
            </soap:Code>

            <soap:Reason>
                <soap:Text xml:lang="en">
                    Invalid customer ID.
                </soap:Text>
            </soap:Reason>

            <soap:Detail>
                ...
            </soap:Detail>

        </soap:Fault>

    </soap:Body>

</soap:Envelope>
```

This demonstrates the two-level model:

```text
HTTP:
    500

SOAP:
    Fault
```

---

# 104. SOAP Message Anatomy

A useful mental model is:

```text
                 SOAP Message
                      |
               +------+------+
               |             |
            Header          Body
               |             |
       +-------+------+      |
       |       |      |      |
   Security Address Reliability
                             |
                             v
                      Application Data
                             |
                 +-----------+-----------+
                 |                       |
               Request                Response
                 |
                 +-- or Fault
```

---

# 105. SOAP Core vs WS-* Stack

Keep these layers separate.

```text
+----------------------------------------+
| Application                            |
+----------------------------------------+
| WSDL / XSD                             |
+----------------------------------------+
| WS-Security / WS-Addressing / etc.     |
+----------------------------------------+
| SOAP                                   |
+----------------------------------------+
| HTTP                                   |
+----------------------------------------+
| TLS                                    |
+----------------------------------------+
| TCP / QUIC                             |
+----------------------------------------+
| IP                                     |
+----------------------------------------+
```

Not every deployment contains every layer.

For example:

```text
SOAP
  +
HTTP
```

is a valid simple deployment.

Another might be:

```text
SOAP
  +
WS-Security
  +
WS-Addressing
  +
WS-ReliableMessaging
  +
WS-Policy
  +
HTTP
  +
TLS
```

---

# 106. Important Terminology

## SOAP Node

A participant that processes SOAP messages.

## SOAP Message

A message conforming to the SOAP messaging framework.

## Envelope

The outermost SOAP XML element.

## Header

Optional SOAP metadata containing header blocks.

## Body

Required SOAP element containing the primary message content.

## Fault

SOAP-defined representation of a processing failure.

## SOAP Module

An extension defining syntax and semantics for SOAP header blocks and processing behavior.

## Binding

Specification of how SOAP messages are exchanged using an underlying protocol.

## Message Exchange Pattern

A defined pattern for exchanging SOAP messages.

## WSDL

A formal description of a web service interface and concrete deployment information.

## XML Schema

The type system commonly used to define SOAP payload structures.

---

# 107. Common Misconceptions

## "SOAP is XML."

Incorrect.

SOAP uses XML, but SOAP is a protocol and processing model.

---

## "SOAP is HTTP."

Incorrect.

HTTP is commonly used as a transport/application protocol binding for SOAP.

---

## "SOAP requires HTTP."

Incorrect.

SOAP 1.2 explicitly defines a protocol-binding framework intended to support underlying protocols other than HTTP.

---

## "SOAP is always RPC."

Incorrect.

SOAP supports RPC-style and document-oriented messaging.

---

## "SOAP automatically provides security."

Incorrect.

SOAP's core messaging framework does not itself provide complete confidentiality, integrity, authentication, or authorization.

WS-Security and transport security can provide those capabilities.

---

## "WSDL is SOAP."

Incorrect.

WSDL describes services.

SOAP defines a message protocol.

---

## "WSDL is required by SOAP."

Incorrect.

SOAP messages can exist without WSDL.

WSDL is commonly used to describe SOAP-based services.

---

## "SOAP and REST are competing versions of HTTP."

Incorrect.

REST is an architectural style.

SOAP is a protocol.

Both can use HTTP.

---

## "SOAP is inherently stateful."

Incorrect.

SOAP does not require stateful applications.

---

## "SOAP is inherently unreliable."

Incorrect.

The base SOAP framework does not guarantee reliable business message delivery, but WS-ReliableMessaging and application mechanisms can provide stronger guarantees.

---

# 108. SOAP's Architectural Philosophy

SOAP's design can be summarized as:

```text
Keep the core messaging framework relatively small.

Add advanced capabilities through extensions/modules.
```

Therefore:

```text
SOAP Core
    |
    +-- addressing
    +-- security
    +-- reliability
    +-- transactions
    +-- policy
    +-- attachments
    +-- other features
```

This is conceptually similar to a modular protocol architecture.

---

# 109. Why the WS-* Ecosystem Became Large

Enterprise systems have requirements that ordinary HTTP request/response semantics do not directly solve.

For example:

```text
How do I sign one XML element?

How do I encrypt only part of a message?

How do I route a message through intermediaries?

How do I identify the ultimate destination?

How do I correlate messages?

How do I guarantee message delivery?

How do I detect duplicates?

How do I express service security requirements?

How do I coordinate distributed transactions?
```

Instead of modifying SOAP itself for every problem, specifications were built around the SOAP extension model.

That produced the WS-* ecosystem.

---

# 110. SOAP as a Message-Oriented Architecture

A useful way to think about SOAP is:

```text
SOAP is not fundamentally an RPC framework.

SOAP is a structured message framework
that can support RPC and document messaging.
```

The message is primary.

RPC is one possible interpretation of the message.

This distinction becomes especially important when studying:

```text
WS-Addressing
WS-ReliableMessaging
WS-Security
intermediaries
asynchronous messaging
```

---

# 111. Synchronous vs Asynchronous SOAP

SOAP does not fundamentally require synchronous communication.

### Synchronous

```text
Client
  |
  | Request
  v
Server
  |
  | Response
  v
Client
```

### Asynchronous

```text
Client
  |
  | Message
  v
Queue / intermediary
  |
  v
Service
  |
  | later response
  v
Callback endpoint
```

WS-Addressing can be useful in such architectures because the response destination can be represented as message-level metadata.

---

# 112. Correlation

Distributed systems often require:

```text
Request A
    |
    v
Response A

Request B
    |
    v
Response B
```

A message ID can be used to correlate messages.

Conceptually:

```text
MessageID:
    123

Reply:
    relatesTo = 123
```

This becomes particularly useful when:

```text
responses are asynchronous
multiple messages are in flight
intermediaries exist
transport connections are not persistent
```

---

# 113. SOAP and Intermediaries — Practical Example

Consider:

```text
Client
   |
   v
Internet Gateway
   |
   v
Security Service
   |
   v
Message Router
   |
   v
Business Service
```

A SOAP message could contain:

```text
Security Header
    -> processed by security node

Routing Header
    -> processed by router

Application Body
    -> processed by business service
```

This is a much richer model than:

```text
HTTP request -> application
```

---

# 114. SOAP and Enterprise Integration

SOAP is particularly useful when several organizations need a formally specified interface.

For example:

```text
Bank
   |
   | SOAP
   v
Insurance company
```

Both sides can agree on:

```text
WSDL
XSD
security policy
message structure
fault contract
addressing
reliability
```

The implementation languages can differ:

```text
Java
C#
C++
Python
COBOL
etc.
```

provided they correctly implement the agreed contract.

This language-neutral contract was one of SOAP's major selling points.

---

# 115. SOAP Interoperability

Theoretically:

```text
Java SOAP client
        |
        v
C# SOAP service
```

can interoperate.

But interoperability is not guaranteed merely because both systems say "SOAP."

Potential incompatibilities include:

```text
SOAP 1.1 vs SOAP 1.2
document vs RPC
literal vs encoded
different XSD interpretations
WS-* version differences
WS-Addressing differences
WS-Security profile differences
namespace mismatches
binding differences
fault differences
```

This is why interoperability profiles and standardized contracts matter.

---

# 116. Contract Compatibility

Changing a SOAP service contract can break clients.

For example:

```xml
<customerId>
```

changing to:

```xml
<customerID>
```

may break schema validation.

Likewise:

```text
int
```

changing to:

```text
string
```

can alter generated client types.

SOAP systems therefore place considerable emphasis on:

```text
schema compatibility
WSDL compatibility
versioning
namespace management
```

---

# 117. XML Namespace Versioning

A common strategy is to use namespaces to distinguish versions.

For example:

```text
http://example.com/customer/v1
```

and:

```text
http://example.com/customer/v2
```

This allows a service to maintain separate contracts.

Conceptually:

```text
v1 client
    |
    +----> v1 namespace

v2 client
    |
    +----> v2 namespace
```

Namespaces therefore become part of service versioning strategy.

---

# 118. SOAP and API Gateways

A SOAP deployment may contain:

```text
Client
   |
   v
API Gateway
   |
   v
SOAP Service
```

The gateway can perform:

```text
TLS termination
authentication
authorization
rate limiting
logging
routing
schema validation
message transformation
```

SOAP's header model can integrate with intermediary processing.

---

# 119. SOAP and Message Transformation

An intermediary might transform:

```text
SOAP v1.1
```

into:

```text
SOAP v1.2
```

or transform:

```text
SOAP
```

into:

```text
internal application protocol
```

or:

```text
SOAP/XML
```

into:

```text
REST/JSON
```

This is common in modernization architectures.

For example:

```text
Legacy SOAP
     |
     v
Integration Gateway
     |
     v
Modern REST API
     |
     v
Microservice
```

The gateway acts as a protocol translation boundary.

---

# 120. SOAP-to-REST Migration

A common modernization pattern is:

```text
Legacy SOAP
      |
      v
Adapter
      |
      v
REST API
      |
      v
Modern service
```

The adapter may translate:

```text
SOAP Envelope
      |
      v
SOAP Body
      |
      v
REST JSON
```

and responses in the opposite direction.

However, the transformation is not always one-to-one because SOAP may contain:

```text
WS-Security
WS-Addressing
WS-ReliableMessaging
typed faults
headers
complex XML schemas
```

that have no direct HTTP/JSON equivalent.

---

# 121. SOAP vs REST — Architectural Trade-Off

A simplified comparison:

```text
SOAP

Strengths:
    formal contracts
    rich extensibility
    message-level security
    enterprise standards
    strong schemas
    generated clients
    sophisticated messaging

Costs:
    XML verbosity
    complexity
    larger toolchain
    difficult debugging
    substantial standards ecosystem
```

```text
REST/HTTP

Strengths:
    simpler
    HTTP-native
    cache-friendly
    broadly supported
    easy browser/tool integration
    JSON-friendly
    simple operational model

Costs:
    fewer standardized enterprise message extensions
    contracts often less formal
    advanced messaging features require additional design
```

Neither is universally superior.

The correct choice depends on system requirements.

---

# 122. A Useful Layered Mental Model

When studying SOAP, keep these layers separate:

```text
Layer 1 — Business contract
    What does the service actually do?

Layer 2 — WSDL
    What operations/messages/types exist?

Layer 3 — XML Schema
    What does the data look like?

Layer 4 — SOAP
    How is the message packaged and processed?

Layer 5 — WS-* modules
    How are security/addressing/reliability/etc. added?

Layer 6 — Binding
    How does SOAP travel over a protocol?

Layer 7 — HTTP
    How are bytes transported/application messages exchanged?

Layer 8 — TLS
    How is the communication channel protected?

Layer 9 — TCP/QUIC
    How are bytes transported?

Layer 10 — IP
    How are packets routed?
```

The exact OSI mapping should not be interpreted literally, but the separation of concerns is useful.

---

# 123. SOAP in One Diagram

```text
                         BUSINESS LOGIC
                              |
                              v
                         WSDL CONTRACT
                              |
                 +------------+------------+
                 |                         |
               XML Schema              Operations
                 |                         |
                 +------------+------------+
                              |
                              v
                       SOAP MESSAGE
                              |
                +-------------+-------------+
                |                           |
              Header                       Body
                |                           |
        +-------+-------+                   |
        |       |       |                   |
    Security Address Reliability            |
                                            |
                                            v
                                   Application XML
                             
                              |
                              v
                      SOAP HTTP Binding
                              |
                              v
                            HTTP
                              |
                              v
                             TLS
                              |
                              v
                        TCP / QUIC
                              |
                              v
                             IP
```

---

# 124. What You Should Memorize

For an in-depth understanding, the following distinctions are fundamental.

### SOAP

```text
Protocol / messaging framework
```

### HTTP

```text
Application protocol commonly carrying SOAP
```

### REST

```text
Architectural style
```

### XML

```text
Markup/data representation technology used by SOAP
```

### XML Schema

```text
Type/schema system commonly used to define SOAP data
```

### WSDL

```text
Formal service description/contract
```

### WS-Security

```text
SOAP message security extensions
```

### WS-Addressing

```text
Message-level addressing
```

### WS-ReliableMessaging

```text
Reliable message-transfer protocol
```

### WS-Policy

```text
Policy/capability expression
```

### MTOM

```text
Optimized binary-data transmission for SOAP
```

---

# 125. Standards Worth Knowing

For serious SOAP work, these are the most useful specifications to understand.

## Core SOAP

### SOAP 1.1

**W3C Note, 2000**

Important for understanding legacy SOAP implementations.

### SOAP 1.2 Part 1

**W3C Recommendation**

Defines:

* processing model
* extensibility model
* protocol binding framework
* message construct

### SOAP 1.2 Part 2

Defines additional SOAP adjuncts, including mechanisms related to encoding and RPC conventions.

---

## Service Description

### WSDL 1.1

Extremely important historically and in deployed enterprise systems.

Understand:

```text
types
message
portType
binding
service
port
```

### WSDL 2.0

Understand:

```text
types
interface
binding
service
endpoint
```

---

## XML

Understand:

```text
XML Namespaces
XML Schema
XML Infoset
XML Signature
XML Encryption
```

---

## SOAP Extensions

Understand conceptually:

```text
WS-Security
WS-Addressing
WS-ReliableMessaging
WS-Policy
WS-Coordination
WS-AtomicTransaction
MTOM
```

You do not need to memorize every WS-* specification.

Understand **why each exists and which problem it solves**.

---

# 126. Recommended Learning Order

For an in-depth understanding, study SOAP in this order:

```text
1. XML
       |
       v
2. XML Namespaces
       |
       v
3. XML Schema
       |
       v
4. SOAP Envelope
       |
       v
5. SOAP Header / Body
       |
       v
6. SOAP Processing Model
       |
       v
7. SOAP Faults
       |
       v
8. SOAP HTTP Binding
       |
       v
9. SOAP 1.1 vs SOAP 1.2
       |
       v
10. WSDL 1.1
       |
       v
11. WSDL 2.0
       |
       v
12. Document vs RPC
       |
       v
13. Literal vs Encoded
       |
       v
14. WS-Addressing
       |
       v
15. WS-Security
       |
       v
16. WS-ReliableMessaging
       |
       v
17. WS-Policy
       |
       v
18. MTOM
       |
       v
19. Enterprise interoperability
       |
       v
20. SOAP vs REST
```

This order is preferable to starting with WSDL because WSDL becomes considerably easier to understand once the underlying SOAP message is familiar.

---

# 127. Final Conceptual Model

The most useful way to think about SOAP is:

```text
SOAP is a standardized message-processing framework
for exchanging structured information between distributed nodes.
```

It provides:

```text
Envelope
Header
Body
Fault
Processing model
Extensibility model
Protocol-binding model
```

WSDL then provides:

```text
Service contract
```

XML Schema provides:

```text
Data model
```

WS-* specifications add:

```text
Security
Addressing
Reliability
Policy
Transactions
Other enterprise messaging capabilities
```

HTTP commonly provides:

```text
The protocol binding carrying SOAP
```

TLS can provide:

```text
Channel security
```

And TCP/QUIC provides:

```text
Underlying transport
```

The complete conceptual stack is therefore:

```text
                    BUSINESS SERVICE
                           |
                           v
                         WSDL
                           |
                           v
                    XML Schema / XSD
                           |
                           v
                    SOAP Message
                           |
             +-------------+-------------+
             |             |             |
          Security      Addressing   Reliability
             |             |             |
             +-------------+-------------+
                           |
                           v
                     SOAP Binding
                           |
                           v
                         HTTP
                           |
                           v
                          TLS
                           |
                           v
                       TCP / QUIC
                           |
                           v
                          IP
```

And the most important distinction from the previous REST discussion is:

```text
REST:
    architectural constraints applied to
    distributed application architecture


SOAP:
    protocol defining a structured
    message-processing framework
```

while:

```text
HTTP:
    application protocol that can carry
    either REST-oriented interactions,
    SOAP messages, or arbitrary other
    application data.
```

That distinction prevents most of the common conceptual confusion surrounding REST, SOAP, and HTTP.

---

# 128. Primary References

The following specifications are the most important references for deeper study.

1. **W3C — SOAP 1.1**

   * W3C Note, 8 May 2000
   * Understand the original envelope, header, body, fault, encoding, RPC, and HTTP binding model.

2. **W3C — SOAP Version 1.2 Part 1: Messaging Framework**

   * W3C Recommendation, Second Edition, 27 April 2007
   * The primary specification for the SOAP 1.2 messaging framework.

3. **W3C — SOAP Version 1.2 Part 2**

   * SOAP adjuncts including encoding/RPC-related mechanisms.

4. **W3C — Web Services Description Language 1.1**

   * Important for understanding the historically dominant WSDL model.

5. **W3C — Web Services Description Language 2.0 Part 1: Core Language**

   * Modernized WSDL component model.

6. **OASIS — Web Services Security**

   * SOAP message security and security-token mechanisms.

7. **W3C — Web Services Addressing**

   * Message-level addressing and endpoint references.

8. **OASIS — WS-ReliableMessaging**

   * Reliable message transfer, sequencing, and related mechanisms.

9. **W3C — MTOM**

   * Optimized binary transmission for SOAP messages.

10. **XML Schema**

    * Fundamental to understanding typed SOAP/WSDL contracts.

---

# 129. Short Version

If the entire document had to be reduced to one diagram:

```text
REST
    = architectural style

SOAP
    = messaging protocol

WSDL
    = service contract

XSD
    = data/schema definition

WS-Security
    = message security

WS-Addressing
    = message addressing

WS-ReliableMessaging
    = reliable message transfer

HTTP
    = common SOAP binding / application protocol

TLS
    = channel security

TCP/QUIC
    = transport
```

And:

```text
                    SOAP ECOSYSTEM

                 +-------------------+
                 |   Application     |
                 +-------------------+
                          |
                 +-------------------+
                 |      WSDL         |
                 |     + XSD         |
                 +-------------------+
                          |
       +------------------+------------------+
       |                  |                  |
   WS-Security      WS-Addressing    WS-ReliableMessaging
       |                  |                  |
       +------------------+------------------+
                          |
                 +-------------------+
                 |       SOAP        |
                 | Envelope/Header   |
                 | Body/Fault        |
                 +-------------------+
                          |
                 +-------------------+
                 |       HTTP        |
                 +-------------------+
                          |
                 +-------------------+
                 |    TLS / TCP      |
                 +-------------------+
                          |
                 +-------------------+
                 |       IP          |
                 +-------------------+
```

That is the conceptual model to retain.
