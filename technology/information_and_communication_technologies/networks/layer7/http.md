# HTTP

## 1. Introduction

[**HTTP (Hypertext Transfer Protocol)**](./http.md) is a stateless, application-layer request/response protocol used for communication between clients, servers, proxies, gateways, caches, and other intermediaries.

HTTP provides a uniform interface for interacting with resources without requiring the client to know how those resources are implemented.

At a conceptual level:

```text
Client
  │
  │ HTTP Request
  ▼
Server
  │
  │ HTTP Response
  ▼
Client
```

A more realistic deployment can contain several intermediaries:

```text
Client
   │
   ▼
Forward Proxy
   │
   ▼
CDN / Cache
   │
   ▼
Reverse Proxy / Load Balancer
   │
   ▼
Application Server
   │
   ▼
Database / Other Services
```

HTTP is specifically designed to operate through such intermediaries.

The current HTTP specifications separate:

* **HTTP semantics**
* **HTTP caching**
* **HTTP/1.1 message syntax**
* **HTTP/2 framing**
* **HTTP/3 framing and transport**

This separation is important because HTTP/1.1, HTTP/2, and HTTP/3 generally implement the same HTTP semantics while using substantially different wire formats.

The principal current standards are:

| Area           |          RFC | Current status |
| -------------- | -----------: | -------------- |
| HTTP Semantics | **RFC 9110** | Current        |
| HTTP Caching   | **RFC 9111** | Current        |
| HTTP/1.1       | **RFC 9112** | Current        |
| HTTP/2         | **RFC 9113** | Current        |
| HTTP/3         | **RFC 9114** | Current        |

RFC 9110 is particularly important because it defines the common semantics shared across HTTP versions. RFC 9112 then defines the HTTP/1.1 message syntax and connection management, while RFCs 9113 and 9114 define the HTTP/2 and HTTP/3 mappings respectively.

---

# 2. What HTTP Actually Provides

HTTP defines a uniform interface consisting primarily of:

```text
Methods
Resources
Target URIs
Request fields
Response fields
Status codes
Representations
Content negotiation
Caching
Conditional requests
Range requests
Authentication
Redirection
Connection semantics
Intermediary behavior
```

HTTP does **not** inherently define:

* JSON;
* REST;
* HTML;
* XML;
* GraphQL;
* databases;
* application business logic.

For example:

```http
GET /users/123 HTTP/1.1
Host: example.com
Accept: application/json
```

is HTTP.

The JSON representation returned by the server is an application-level representation carried by HTTP.

---

# 3. HTTP Is Stateless

HTTP is fundamentally stateless.

A request can be understood independently:

```text
Request 1:
GET /users/123

Request 2:
GET /users/456
```

HTTP itself does not require the server to remember that Request 1 happened before Request 2.

State can nevertheless be implemented using mechanisms such as:

* cookies;
* authorization credentials;
* bearer tokens;
* server-side sessions;
* application-level identifiers.

For example:

```http
Cookie: session_id=abc123
```

provides application state, but the concept of a session is not fundamental to HTTP itself.

---

# 4. HTTP and REST Are Not the Same Thing

HTTP is a protocol.

REST is an architectural style.

A REST-oriented API commonly uses HTTP concepts such as:

```text
GET     retrieve
POST    create/process
PUT     replace
PATCH   partially modify
DELETE  remove
```

but an HTTP API does not automatically become REST merely because it uses these methods.

For example:

```http
POST /executePayment
```

is perfectly valid HTTP but may not represent a strongly resource-oriented REST design.

---

# 5. HTTP Protocol Evolution

A simplified history is:

```text
1990
 │
 └── Early HTTP / HTTP/0.9
       │
       ▼
1996/1997
 │
 └── HTTP/1.0
       RFC 1945
       │
       ▼
1997
 │
 └── HTTP/1.1
       RFC 2068
       │
       ▼
1999
 │
 └── HTTP/1.1 revision
       RFC 2616
       │
       ▼
2014
 │
 └── HTTP/1.1 modularized
       RFC 7230–7235
       │
       ▼
2015
 │
 └── HTTP/2
       RFC 7540
       │
       ▼
2022
 │
 ├── RFC 9110 — HTTP Semantics
 ├── RFC 9111 — HTTP Caching
 ├── RFC 9112 — HTTP/1.1
 ├── RFC 9113 — HTTP/2
 └── RFC 9114 — HTTP/3
```

---

# 6. HTTP/0.9

HTTP/0.9 was extremely simple.

A request was essentially:

```text
GET /index.html
```

The server returned the document directly.

There were:

* no HTTP headers;
* no status line;
* no request headers;
* no response headers;
* no explicit HTTP version in the request;
* no content type mechanism;
* no status codes.

Conceptually:

```text
Client → GET /index.html → Server

Server → <document bytes> → Client
```

The end of the underlying connection indicated the end of the response.

HTTP/0.9 is primarily historically significant today.

RFC 1945 formally documents HTTP/1.0 and also specifies compatibility with the HTTP/0.9 request/response format.

---

# 7. HTTP/1.0

HTTP/1.0 was defined by:

**RFC 1945 — Hypertext Transfer Protocol — HTTP/1.0**

It introduced the basic message model that most developers recognize as "HTTP":

```text
Request line
Headers
Blank line
Body
```

and:

```text
Status line
Headers
Blank line
Body
```

Example:

```http
GET /index.html HTTP/1.0
Host: example.com

```

Response:

```http
HTTP/1.0 200 OK
Content-Type: text/html
Content-Length: 1234

<html>...</html>
```

Important capabilities included:

* HTTP version identification;
* request headers;
* response headers;
* status codes;
* content metadata;
* `Content-Length`;
* basic caching controls;
* conditional requests;
* authentication mechanisms.

However, HTTP/1.0 generally treated each request/response exchange as associated with a connection that was closed afterward.

That created considerable overhead:

```text
TCP connection
     ↓
HTTP request
     ↓
HTTP response
     ↓
TCP connection closed
```

For many objects:

```text
HTML
 ├── CSS
 ├── JavaScript
 ├── image 1
 ├── image 2
 ├── image 3
 └── ...
```

many separate connections could be required.

---

# 8. HTTP/1.1

HTTP/1.1 was originally specified by:

* RFC 2068 — 1997
* RFC 2616 — 1999
* RFC 7230–7235 — 2014

The 2014 specifications split the HTTP/1.1 specification into several documents.

The current HTTP/1.1 specification is:

**RFC 9112 — HTTP/1.1**

RFC 9112 obsoletes RFC 7230.

Important HTTP/1.1 improvements included:

* persistent connections;
* `Host`;
* chunked transfer coding;
* stronger message framing;
* improved caching;
* conditional requests;
* range requests;
* content negotiation;
* improved proxy support;
* virtual hosting;
* better connection reuse.

---

# 9. HTTP/1.1 Persistent Connections

Instead of:

```text
TCP
 │
 ├── Request
 ├── Response
 └── CLOSE
```

HTTP/1.1 can use:

```text
TCP
 │
 ├── Request 1
 ├── Response 1
 ├── Request 2
 ├── Response 2
 ├── Request 3
 ├── Response 3
 └── ...
```

This reduces:

* TCP handshake overhead;
* TLS handshake overhead;
* latency;
* connection establishment cost.

HTTP/1.1 therefore introduced a much more efficient model for web workloads.

---

# 10. HTTP/2

HTTP/2 was originally specified by:

**RFC 7540 — Hypertext Transfer Protocol Version 2**

The current specification is:

**RFC 9113 — HTTP/2**

RFC 9113 obsoletes RFC 7540 and RFC 8740.

HTTP/2 retains HTTP semantics but fundamentally changes the wire representation.

HTTP/1.1:

```text
Text-oriented message syntax
```

HTTP/2:

```text
Binary framing
+
Multiplexed streams
+
Compressed header fields
```

Major features include:

* binary framing;
* multiplexing;
* stream identifiers;
* concurrent requests/responses;
* HPACK header compression;
* flow control;
* stream prioritization mechanisms;
* server push in the original specification.

---

# 11. HTTP/2 Multiplexing

HTTP/1.1 commonly looks like:

```text
Connection
│
├── Request A
│   └── Response A
│
├── Request B
│   └── Response B
│
└── Request C
    └── Response C
```

HTTP/2 can interleave frames from multiple streams:

```text
TCP connection
│
├── Stream 1 frame
├── Stream 3 frame
├── Stream 1 frame
├── Stream 5 frame
├── Stream 3 frame
├── Stream 5 frame
└── ...
```

This allows multiple HTTP exchanges to share a single TCP connection.

However, HTTP/2 still runs over TCP.

Therefore, if TCP loses a packet, TCP-level retransmission can block delivery of subsequent TCP data even if that data belongs to another HTTP/2 stream.

This is **TCP head-of-line blocking**.

HTTP/3 addresses this at the transport architecture level.

---

# 12. HTTP/2 Binary Framing

An HTTP/2 message is divided into frames.

The basic frame header is 9 octets:

```text
  0                   1                   2                   3
  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7
 +-------------------------------+---------------+---------------+
 | Length (24)                    | Type (8)      | Flags (8)     |
 +---------------+---------------+-------------------------------+
 |R| Stream Identifier (31)                                       |
 +---------------------------------------------------------------+
 | Frame Payload ...                                              |
 +---------------------------------------------------------------+
```

Fields:

| Field             |     Size |
| ----------------- | -------: |
| Length            |  24 bits |
| Type              |   8 bits |
| Flags             |   8 bits |
| Stream Identifier |  31 bits |
| Reserved bit      |    1 bit |
| Payload           | Variable |

The frame payload length is therefore explicitly encoded.

Common frame types include:

```text
0x0  DATA
0x1  HEADERS
0x2  PRIORITY
0x3  RST_STREAM
0x4  SETTINGS
0x5  PUSH_PROMISE
0x6  PING
0x7  GOAWAY
0x8  WINDOW_UPDATE
0x9  CONTINUATION
```

RFC 9113 defines the current HTTP/2 framing model.

---

# 13. HTTP/2 Connection Preface

An HTTP/2 client begins a connection with a connection preface containing the following ASCII sequence:

```text
PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n
```

In hexadecimal:

```text
50 52 49 20 2A 20 48 54 54 50 2F 32 2E 30
0D 0A 0D 0A 53 4D 0D 0A 0D 0A
```

This is followed by a SETTINGS frame.

The preface helps distinguish HTTP/2 from other protocols when negotiating or establishing the connection.

---

# 14. HPACK

HTTP/2 uses **HPACK** for HTTP field compression.

HPACK was defined by:

**RFC 7541 — HPACK: Header Compression for HTTP/2**

HTTP headers tend to be repetitive.

For example:

```http
Host: example.com
User-Agent: ...
Accept: application/json
Authorization: Bearer ...
```

may appear repeatedly.

Sending all of those bytes literally for every request is wasteful.

HPACK uses:

* indexed fields;
* static tables;
* dynamic tables;
* Huffman encoding.

The result is substantially smaller header blocks.

---

# 15. HTTP/3

HTTP/3 is defined by:

**RFC 9114 — HTTP/3**

HTTP/3 retains HTTP semantics but maps them onto **QUIC** rather than TCP.

Conceptually:

```text
HTTP/1.1
    │
    ▼
   TCP
    │
    ▼
   IP
```

```text
HTTP/2
    │
    ▼
   TCP
    │
    ▼
   IP
```

```text
HTTP/3
    │
    ▼
   QUIC
    │
    ▼
   UDP
    │
    ▼
   IP
```

QUIC provides:

* encrypted transport;
* independent streams;
* stream-level loss recovery;
* connection migration;
* integrated TLS 1.3 handshake.

HTTP/3 therefore avoids the TCP-level head-of-line blocking problem affecting HTTP/2.

---

# 16. QUIC and HTTP/3

HTTP/3 does not mean:

```text
HTTP over ordinary UDP
```

It means:

```text
HTTP
  ↓
HTTP/3
  ↓
QUIC
  ↓
UDP
```

QUIC itself provides reliable, ordered delivery **within individual streams**.

Different streams can progress independently.

For example:

```text
QUIC Connection
│
├── Stream 0
│
├── Stream 4
│
├── Stream 8
│
├── Stream 12
│
└── ...
```

Loss on Stream 4 does not inherently prevent Stream 8 from progressing.

---

# 17. QPACK

HTTP/3 uses **QPACK** instead of HPACK.

QPACK is specified by:

**RFC 9204 — QPACK: Field Compression for HTTP/3**

The reason for using a different compression design is that HTTP/3's underlying QUIC transport has different ordering properties from TCP.

HPACK's assumptions about ordered delivery can create undesirable blocking behavior when mapped onto HTTP/3.

QPACK therefore separates encoder/decoder state handling in a way appropriate for QUIC.

---

# 18. HTTP Version Comparison

| Feature                         | HTTP/0.9   | HTTP/1.0 | HTTP/1.1 | HTTP/2         | HTTP/3            |
| ------------------------------- | ---------- | -------- | -------- | -------------- | ----------------- |
| Headers                         | No         | Yes      | Yes      | Yes            | Yes               |
| Status codes                    | No         | Yes      | Yes      | Yes            | Yes               |
| Text message syntax             | Yes        | Yes      | Yes      | No             | No                |
| Binary framing                  | No         | No       | No       | Yes            | Yes               |
| Persistent connections          | No         | Limited  | Yes      | Yes            | Yes               |
| Multiplexing                    | No         | No       | No       | Yes            | Yes               |
| Header compression              | No         | No       | No       | HPACK          | QPACK             |
| Transport                       | TCP-era    | TCP      | TCP      | TCP            | QUIC/UDP          |
| Stream independence             | No         | No       | No       | Limited by TCP | Yes               |
| Encryption inherent to protocol | No         | No       | No       | Commonly TLS   | QUIC includes TLS |
| Current RFC                     | Historical | RFC 1945 | RFC 9112 | RFC 9113       | RFC 9114          |

---

# 19. HTTP/1.1 at the Byte Level

HTTP/1.1 is particularly important to understand at the byte level because it is a text-oriented protocol.

An HTTP/1.1 message is:

```text
start-line
CRLF
zero or more field-lines
CRLF
optional message body
```

RFC 9112 defines the grammar approximately as:

```text
HTTP-message =
    start-line CRLF
    *( field-line CRLF )
    CRLF
    [ message-body ]
```

This means the actual wire representation is a sequence of **octets**, not Unicode characters.

---

# 20. Octets vs Characters

HTTP/1.1 must be parsed as a sequence of octets.

An octet is 8 bits:

```text
1 octet = 8 bits
```

For example:

```text
A
```

in ASCII/UTF-8 is:

```text
0x41
```

The space character:

```text
0x20
```

Carriage Return:

```text
CR = 0x0D
```

Line Feed:

```text
LF = 0x0A
```

Colon:

```text
: = 0x3A
```

The HTTP parser therefore operates on bytes before higher-level character decoding takes place.

This distinction is important for security.

---

# 21. CRLF

HTTP/1.1 uses:

```text
CRLF
```

as the normal line terminator.

The bytes are:

```text
CR = 0x0D
LF = 0x0A
```

Therefore:

```text
CRLF = 0D 0A
```

For example:

```http
GET / HTTP/1.1
Host: example.com

```

is approximately:

```text
47 45 54 20 2F 20 48 54 54 50 2F 31 2E 31 0D 0A
48 6F 73 74 3A 20 65 78 61 6D 70 6C 65 2E 63 6F 6D 0D 0A
0D 0A
```

The final:

```text
0D 0A
```

marks the end of the header section.

---

# 22. HTTP/1.1 Request Format

The request grammar is:

```text
request-line
*(header-field CRLF)
CRLF
[message-body]
```

The request line is:

```text
method SP request-target SP HTTP-version CRLF
```

Example:

```http
GET /hello HTTP/1.1\r\n
Host: example.com\r\n
Accept: application/json\r\n
\r\n
```

---

# 23. Request Line at the Byte Level

Consider:

```http
GET /hello HTTP/1.1\r\n
```

The bytes are:

```text
47 45 54
20
2F 68 65 6C 6C 6F
20
48 54 54 50 2F 31 2E 31
0D 0A
```

Breaking that down:

```text
47 45 54                 GET
20                       SP
2F 68 65 6C 6C 6F        /hello
20                       SP
48 54 54 50 2F 31 2E 31  HTTP/1.1
0D 0A                     CRLF
```

---

# 24. HTTP Header Fields

A field line has the general structure:

```text
field-name ":" OWS field-value OWS
```

Example:

```http
Content-Type: application/json
```

Byte representation:

```text
43 6F 6E 74 65 6E 74 2D 54 79 70 65
3A
20
61 70 70 6C 69 63 61 74 69 6F 6E 2F 6A 73 6F 6E
```

The field name is case-insensitive.

Therefore:

```text
Content-Type
content-type
CONTENT-TYPE
CoNtEnT-TyPe
```

represent the same field name.

The field value semantics are field-specific.

---

# 25. Header Termination

Consider:

```http
Host: example.com\r\n
Accept: application/json\r\n
\r\n
```

The first CRLF terminates the `Host` field.

The second CRLF terminates the `Accept` field.

The third sequence:

```text
\r\n
```

with no preceding field indicates the end of the header section.

Therefore:

```text
Headers
   │
   ▼
CRLF
   │
   ▼
Body
```

---

# 26. HTTP Message Body

The body is an arbitrary sequence of octets:

```text
message-body = *OCTET
```

The HTTP protocol does not require the body to be text.

It can contain:

```text
JSON
XML
HTML
JPEG
PNG
PDF
ZIP
Protocol Buffers
application/octet-stream
compressed data
encrypted application data
```

For example:

```http
Content-Type: application/json
Content-Length: 17

{"name":"Alice"}
```

The body bytes are interpreted according to the representation metadata and application protocol.

---

# 27. Content-Type

`Content-Type` describes the media type of the representation.

Examples:

```http
Content-Type: application/json
```

```http
Content-Type: text/html; charset=utf-8
```

```http
Content-Type: image/jpeg
```

```http
Content-Type: application/octet-stream
```

The media type is not the same thing as the transport framing.

For example:

```text
Content-Type: application/json
```

says:

> Interpret these bytes as JSON.

It does not say:

> The message is 1024 bytes long.

That is the job of message framing.

---

# 28. Content-Length

Example:

```http
Content-Length: 13
```

means the message content contains 13 octets.

For:

```text
Hello, world!
```

the ASCII/UTF-8 byte count is:

```text
13
```

It is important that `Content-Length` counts **bytes**, not characters.

For example:

```text
é
```

is one Unicode character but commonly occupies two UTF-8 bytes:

```text
C3 A9
```

Therefore:

```text
character count ≠ byte count
```

when non-ASCII encodings are involved.

---

# 29. Transfer-Encoding: chunked

HTTP/1.1 can transmit content without knowing its total size in advance.

Example:

```http
Transfer-Encoding: chunked
```

The body is then encoded as:

```text
chunk-size CRLF
chunk-data CRLF
chunk-size CRLF
chunk-data CRLF
0 CRLF
CRLF
```

Example:

```text
5\r\n
Hello\r\n
6\r\n
 World\r\n
0\r\n
\r\n
```

Byte representation:

```text
35 0D 0A
48 65 6C 6C 6F
0D 0A

36 0D 0A
20 57 6F 72 6C 64
0D 0A

30 0D 0A
0D 0A
```

The chunk sizes are hexadecimal.

For example:

```text
5
```

means:

```text
5 octets
```

and:

```text
A
```

means:

```text
10 octets
```

---

# 30. Why Chunked Transfer Exists

Imagine a server generates data dynamically:

```text
database query
      ↓
application
      ↓
JSON serialization
      ↓
HTTP response
```

The server may not know the final size before it begins sending.

Without chunked transfer, it might need to:

```text
generate entire response
      ↓
calculate length
      ↓
send response
```

With chunked transfer:

```text
generate data
      ↓
send chunk
      ↓
generate more data
      ↓
send chunk
      ↓
...
```

This allows streaming.

Note that HTTP/2 and HTTP/3 use their own framing and do not use HTTP/1.1 chunked transfer coding.

---

# 31. Message Framing vs Representation

This distinction is essential.

Suppose:

```http
Content-Type: application/json
Content-Length: 25
```

There are two different questions:

### What is the data?

```text
JSON
```

### How many bytes belong to this message?

```text
25 octets
```

Therefore:

```text
Representation semantics
        │
        └── Content-Type

Message framing
        │
        └── Content-Length / Transfer-Encoding /
            protocol-specific framing
```

HTTP/2 and HTTP/3 make this distinction even more obvious because the HTTP message is carried inside binary frames.

---

# 32. Request Methods

HTTP defines methods with specific semantics.

Common methods include:

| Method  | Typical purpose              | Safe |     Idempotent |
| ------- | ---------------------------- | ---: | -------------: |
| GET     | Retrieve                     |  Yes |            Yes |
| HEAD    | Retrieve metadata            |  Yes |            Yes |
| OPTIONS | Discover capabilities        |  Yes |            Yes |
| TRACE   | Diagnostic loop-back         |  Yes |            Yes |
| POST    | Create/process               |   No |             No |
| PUT     | Replace/create at target URI |   No |            Yes |
| PATCH   | Partial modification         |   No | Not inherently |
| DELETE  | Delete                       |   No |            Yes |
| CONNECT | Establish tunnel             |   No |             No |

"Safe" and "idempotent" are semantic properties, not indications that a method is inherently harmless in every application.

---

# 33. GET

GET requests a representation of a target resource.

Example:

```http
GET /users/123 HTTP/1.1
Host: api.example.com
Accept: application/json
```

Typical response:

```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 42

{"id":123,"name":"Alice"}
```

GET responses are commonly cacheable.

---

# 34. HEAD

HEAD is similar to GET but requests response metadata without the response content.

Example:

```http
HEAD /large.iso HTTP/1.1
Host: example.com
```

Useful for determining:

```text
Content-Length
Content-Type
ETag
Last-Modified
Accept-Ranges
```

without transferring the entire representation.

---

# 35. POST

POST asks the target resource to process the enclosed content according to the resource's semantics.

Example:

```http
POST /users HTTP/1.1
Host: api.example.com
Content-Type: application/json
Content-Length: 27

{"name":"Alice","age":30}
```

POST is not inherently "create".

It can represent:

* creation;
* commands;
* processing;
* form submission;
* non-idempotent operations.

---

# 36. PUT

PUT requests that the target resource's state be replaced or created according to the semantics defined by the target URI.

Example:

```http
PUT /users/123 HTTP/1.1
Host: api.example.com
Content-Type: application/json

{"id":123,"name":"Alice"}
```

PUT is idempotent by HTTP semantics.

Repeating the same request should have the same intended effect as making it once, although server-side side effects can still exist outside the requested resource state.

---

# 37. PATCH

PATCH performs a partial modification.

A PATCH request might contain:

```http
PATCH /users/123 HTTP/1.1
Content-Type: application/json

{"name":"Bob"}
```

PATCH is not inherently idempotent.

Whether a particular PATCH operation is idempotent depends on the patch semantics.

PATCH was standardized by RFC 5789.

---

# 38. DELETE

DELETE requests removal of the target resource's association with its functionality.

Example:

```http
DELETE /users/123 HTTP/1.1
Host: api.example.com
```

DELETE is idempotent in the HTTP semantic sense.

A second DELETE can still produce a different status code, such as:

```text
404 Not Found
```

while remaining idempotent with respect to the desired resource state.

---

# 39. URI Structure

A typical HTTP URI is:

```text
https://example.com:443/users/123?active=true#fragment
```

Conceptually:

```text
scheme://authority/path?query#fragment
```

For HTTP:

```text
scheme      = https
host        = example.com
port        = 443
path        = /users/123
query       = active=true
fragment    = #fragment
```

The fragment is generally not sent to the HTTP server.

It is interpreted by the client.

---

# 40. Host and Authority

For HTTP/1.1:

```http
Host: example.com
```

identifies the host targeted by the request.

This is essential for virtual hosting.

One IP address can serve:

```text
example.com
api.example.com
static.example.com
```

and the HTTP `Host` value allows the server or intermediary to select the appropriate virtual host.

HTTP/2 and HTTP/3 represent this information through the `:authority` pseudo-header.

---

# 41. HTTP/2 Pseudo-Headers

HTTP/2 does not send an HTTP/1.1 request line.

Instead, request control information is represented through pseudo-header fields such as:

```text
:method
:scheme
:authority
:path
```

An HTTP/1.1 request:

```http
GET /users HTTP/1.1
Host: example.com
```

is conceptually mapped to:

```text
:method = GET
:scheme = https
:authority = example.com
:path = /users
```

The actual HTTP/2 representation is binary and HPACK-encoded.

---

# 42. HTTP/3 Pseudo-Headers

HTTP/3 uses the same general semantic model as HTTP/2:

```text
:method
:scheme
:authority
:path
```

but the field section is encoded using QPACK.

---

# 43. HTTP Status Codes

HTTP status codes consist of three decimal digits.

The first digit identifies the broad class:

```text
1xx  Informational
2xx  Successful
3xx  Redirection
4xx  Client Error
5xx  Server Error
```

---

# 44. 1xx Informational

## 100 Continue

The server indicates that it has received the request headers and the client should proceed with sending the request content.

Commonly used with:

```http
Expect: 100-continue
```

This can prevent sending a large body when the server is likely to reject the request based only on headers.

---

## 101 Switching Protocols

Used when switching protocols using the HTTP upgrade mechanism.

Historically important for mechanisms such as WebSocket establishment.

---

## 102 Processing

Defined by WebDAV.

Indicates that the server has received and is processing the request but has not completed it.

---

## 103 Early Hints

Defined by RFC 8297.

Allows a server to send preliminary response headers, commonly for link/preload-related hints, before the final response.

---

# 45. 2xx Success

## 200 OK

Generic successful response.

```http
HTTP/1.1 200 OK
```

---

## 201 Created

Indicates successful creation of a resource.

Often accompanied by:

```http
Location: /users/123
```

---

## 202 Accepted

The request has been accepted for processing but has not necessarily completed.

Common for asynchronous operations.

---

## 203 Non-Authoritative Information

The response contains modified or transformed metadata from an intermediary.

---

## 204 No Content

The request succeeded but there is no content in the response.

Common after operations where a response body is unnecessary.

---

## 205 Reset Content

Requests the user agent to reset the document/view.

Less commonly used.

---

## 206 Partial Content

Used for range responses.

Example:

```http
Range: bytes=0-999
```

Response:

```http
HTTP/1.1 206 Partial Content
Content-Range: bytes 0-999/50000
```

Useful for:

* large downloads;
* media streaming;
* resumable downloads.

---

## 207 Multi-Status

Defined by WebDAV.

Allows multiple status results in one response.

---

## 208 Already Reported

Defined by WebDAV.

---

## 226 IM Used

Defined for instance manipulation.

Rare in ordinary HTTP APIs.

---

# 46. 3xx Redirection

## 300 Multiple Choices

Multiple representations/resources may satisfy the request.

---

## 301 Moved Permanently

The resource has a new permanent URI.

```http
Location: https://example.com/new
```

---

## 302 Found

Historically ambiguous and widely implemented as a temporary redirect.

Clients and servers need to understand the method-preservation implications.

---

## 303 See Other

The response directs the client to another URI, commonly using GET to retrieve the result.

---

## 304 Not Modified

Extremely important for caching.

Example:

```http
If-None-Match: "abc123"
```

Server:

```http
HTTP/1.1 304 Not Modified
```

This means the cached representation can be reused.

No response content is sent.

---

## 305 Use Proxy

Obsolete.

---

## 306

Unused/reserved.

---

## 307 Temporary Redirect

Temporary redirect while preserving the request method and request content.

---

## 308 Permanent Redirect

Permanent redirect while preserving the request method and request content.

Defined originally by RFC 7538 and incorporated into current HTTP semantics by RFC 9110.

---

# 47. 4xx Client Errors

## 400 Bad Request

The server considers the request malformed or invalid.

Examples:

* malformed syntax;
* invalid framing;
* invalid request target;
* malformed fields.

---

## 401 Unauthorized

Despite the name, this means that authentication is required or has failed.

Typically accompanied by:

```http
WWW-Authenticate: ...
```

---

## 402 Payment Required

Reserved for future use, although some APIs use it for application-specific payment-related semantics.

---

## 403 Forbidden

The server understood the request but refuses to fulfill it.

---

## 404 Not Found

The target resource was not found or the server does not wish to disclose its existence.

---

## 405 Method Not Allowed

The target resource does not support the requested method.

The response should normally include:

```http
Allow: GET, HEAD, OPTIONS
```

---

## 406 Not Acceptable

The server cannot produce a representation satisfying the client's content negotiation requirements.

---

## 407 Proxy Authentication Required

The client must authenticate with a proxy.

---

## 408 Request Timeout

The server did not receive a complete request within the time it was prepared to wait.

---

## 409 Conflict

The request conflicts with the current state of the target resource.

Common in APIs involving:

* version conflicts;
* concurrent modifications;
* state transitions.

---

## 410 Gone

The resource is intentionally and permanently unavailable.

---

## 411 Length Required

The request requires a defined content length.

---

## 412 Precondition Failed

A request condition was not satisfied.

For example:

```http
If-Match: "version-123"
```

does not match the current representation.

---

## 413 Content Too Large

The request content is larger than the server is willing or able to process.

---

## 414 URI Too Long

The target URI is longer than the server is willing to interpret.

---

## 415 Unsupported Media Type

The request content format is not supported.

Example:

```http
Content-Type: application/xml
```

when the endpoint only accepts:

```text
application/json
```

---

## 416 Range Not Satisfiable

The requested byte range cannot be satisfied.

---

## 417 Expectation Failed

The expectation specified by the request's `Expect` field could not be met.

---

## 418 I'm a teapot

Originally specified by RFC 2324 as an April Fools' joke.

It is historically notable but should not normally be used for production semantics.

---

## 421 Misdirected Request

The request was directed at a server that cannot produce a response for the requested target.

Particularly relevant in HTTP/2 and HTTP/3 deployments involving connection coalescing and multiple origins.

---

## 422 Unprocessable Content

The server understands the content type and syntax but cannot process the contained instructions.

Originally associated with WebDAV and later generalized.

---

## 423 Locked

WebDAV.

---

## 424 Failed Dependency

WebDAV.

---

## 425 Too Early

Defined by RFC 8470.

Used to indicate that the server is unwilling to risk processing a request that may have been replayed when sent using early data.

---

## 426 Upgrade Required

The client should use another protocol.

---

## 428 Precondition Required

The origin server requires the request to be conditional.

---

## 429 Too Many Requests

The client has sent too many requests within a given period.

Often associated with:

```http
Retry-After: 60
```

This is one of the most important HTTP status codes for rate limiting.

---

## 431 Request Header Fields Too Large

The request header fields are too large.

---

## 451 Unavailable For Legal Reasons

The requested resource is unavailable because of legal demands or restrictions.

---

# 48. 5xx Server Errors

## 500 Internal Server Error

Generic server-side failure.

---

## 501 Not Implemented

The server does not support the functionality required to fulfill the request.

---

## 502 Bad Gateway

A gateway/proxy received an invalid response from an upstream server.

Typical topology:

```text
Client
  ↓
Reverse Proxy
  ↓
Application Server
```

If the application server produces an invalid upstream response:

```text
Reverse Proxy → 502
```

---

## 503 Service Unavailable

The server is temporarily unable to handle the request.

Common causes:

* overload;
* maintenance;
* dependency failure;
* insufficient capacity.

May include:

```http
Retry-After: 120
```

---

## 504 Gateway Timeout

A gateway or proxy did not receive a timely response from an upstream server.

---

## 505 HTTP Version Not Supported

The server does not support the HTTP version used in the request.

---

## 506 Variant Also Negotiates

Content negotiation configuration error.

---

## 507 Insufficient Storage

WebDAV.

---

## 508 Loop Detected

WebDAV.

---

## 510 Not Extended

Obsoleted/experimental extension mechanism.

---

## 511 Network Authentication Required

Used by some networks to indicate that network-level authentication is required.

---

# 49. Status Code Classes

A useful mental model:

```text
1xx
 │
 └── "Continue / information"

2xx
 │
 └── "Your request succeeded"

3xx
 │
 └── "Look elsewhere / use cached result / redirect"

4xx
 │
 └── "The request cannot be fulfilled as submitted"

5xx
 │
 └── "The server-side processing failed"
```

A client should generally make decisions based on the numeric status code and defined semantics, not the textual reason phrase.

---

# 50. Reason Phrases

HTTP/1.1 historically uses:

```http
HTTP/1.1 404 Not Found
```

The text:

```text
Not Found
```

is the reason phrase.

Modern clients should not depend on it.

For example:

```http
HTTP/1.1 404 Resource Missing
```

can still represent status code 404.

The numeric status code carries the protocol semantics.

HTTP/2 and HTTP/3 do not use the HTTP/1.1 textual status-line representation.

---

# 51. Headers

HTTP fields communicate:

```text
routing information
authentication
content metadata
caching instructions
conditional requests
client capabilities
server capabilities
security policy
cookies
range requests
compression
connection behavior
```

Important fields include:

```text
Host
Content-Type
Content-Length
Accept
Accept-Encoding
Authorization
Cookie
Set-Cookie
Cache-Control
ETag
If-Match
If-None-Match
If-Modified-Since
Last-Modified
Location
Range
Content-Range
Vary
User-Agent
Server
Date
Retry-After
```

---

# 52. Accept

`Accept` communicates which response media types the client prefers.

Example:

```http
Accept: application/json
```

Multiple alternatives:

```http
Accept: application/json, text/plain;q=0.8, */*;q=0.5
```

The `q` parameter expresses relative preference.

---

# 53. Accept-Encoding

Example:

```http
Accept-Encoding: gzip, br, zstd
```

This indicates acceptable content codings.

The server might respond with:

```http
Content-Encoding: br
```

The distinction is important:

```text
Content-Type
    ↓
What the representation is

Content-Encoding
    ↓
How the representation is encoded
```

---

# 54. Content-Encoding

Example:

```http
Content-Encoding: gzip
```

The representation is compressed.

Conceptually:

```text
Application representation
        ↓
       gzip
        ↓
HTTP content
```

The client reverses the encoding:

```text
HTTP content
        ↓
      gunzip
        ↓
Application representation
```

---

# 55. Transfer-Encoding vs Content-Encoding

These are fundamentally different.

### Content-Encoding

Describes representation encoding:

```http
Content-Encoding: gzip
```

### Transfer-Encoding

Describes HTTP/1.1 transfer coding:

```http
Transfer-Encoding: chunked
```

Conceptually:

```text
Application representation
       │
       ▼
Content-Encoding
       │
       ▼
HTTP content
       │
       ▼
Transfer framing
       │
       ▼
Network
```

HTTP/2 and HTTP/3 do not use HTTP/1.1 `chunked` transfer coding.

---

# 56. Cookies

Cookies are defined by the HTTP State Management Mechanism.

A server sends:

```http
Set-Cookie: session=abc123; Secure; HttpOnly
```

The client subsequently sends:

```http
Cookie: session=abc123
```

Cookies therefore introduce state into an otherwise stateless protocol interaction.

Important attributes include:

```text
Secure
HttpOnly
SameSite
Domain
Path
Max-Age
Expires
```

---

# 57. Authentication

HTTP authentication is distinct from application authorization.

Common authentication schemes include:

```text
Basic
Bearer
Digest
Negotiate
```

Example:

```http
Authorization: Bearer eyJhbGciOi...
```

The server may respond:

```http
WWW-Authenticate: Bearer
```

Authentication and authorization should be conceptually separated:

```text
Authentication
    ↓
Who are you?

Authorization
    ↓
Are you allowed to perform this operation?
```

---

# 58. Conditional Requests

Conditional requests allow a client to ask:

> "Perform this operation only if the resource is still in the state I expect."

Important fields include:

```text
If-Match
If-None-Match
If-Modified-Since
If-Unmodified-Since
If-Range
```

These are extremely important for:

* caching;
* optimistic concurrency;
* avoiding unnecessary transfers.

---

# 59. ETag

An ETag identifies a representation version.

Example:

```http
ETag: "abc123"
```

Client:

```http
If-None-Match: "abc123"
```

If unchanged:

```http
HTTP/1.1 304 Not Modified
```

If changed:

```http
HTTP/1.1 200 OK
```

with the new representation.

---

# 60. Strong vs Weak ETags

Example strong validator:

```http
ETag: "abc123"
```

Example weak validator:

```http
ETag: W/"abc123"
```

A weak validator indicates semantic equivalence rather than byte-for-byte identity.

This distinction matters for conditional requests and cache validation.

---

# 61. Last-Modified

A server may provide:

```http
Last-Modified: Wed, 10 Sep 2026 12:00:00 GMT
```

A client can subsequently send:

```http
If-Modified-Since: Wed, 10 Sep 2026 12:00:00 GMT
```

If the resource has not changed, the server can return:

```http
304 Not Modified
```

---

# 62. HTTP Caching

HTTP caching is defined by:

**RFC 9111 — HTTP Caching**

A cache stores previous responses and can reuse them when appropriate.

Conceptually:

```text
Client
  │
  ▼
Cache
  │
  ├── HIT ──→ Response
  │
  └── MISS
       │
       ▼
     Server
```

Caching can reduce:

* latency;
* bandwidth;
* server load.

---

# 63. Cache-Control

Example:

```http
Cache-Control: max-age=3600
```

means that the response can generally be considered fresh for 3600 seconds subject to the complete caching rules.

Other important directives include:

```text
no-cache
no-store
private
public
must-revalidate
immutable
max-age
s-maxage
stale-while-revalidate
stale-if-error
```

---

# 64. `no-cache` vs `no-store`

These are frequently confused.

### `no-store`

Means:

> Do not store this response.

### `no-cache`

Does **not** mean "do not cache".

It means the stored response must generally be validated before reuse.

Therefore:

```text
no-store
    ≈ don't store

no-cache
    ≈ may store, but revalidate before reuse
```

---

# 65. Vary

Consider:

```http
Vary: Accept-Encoding
```

A cache cannot blindly reuse a response for every request.

It must consider the relevant request fields named by `Vary`.

For example:

```text
Request A
Accept-Encoding: gzip

Request B
Accept-Encoding: br
```

may result in different cached representations.

---

# 66. Range Requests

Range requests allow partial retrieval.

Example:

```http
Range: bytes=1000-1999
```

The server may respond:

```http
HTTP/1.1 206 Partial Content
Content-Range: bytes 1000-1999/10000
```

This is useful for:

* resumable downloads;
* media playback;
* large objects;
* random-access retrieval.

---

# 67. Content Negotiation

HTTP can negotiate representations.

The client may send:

```http
Accept: application/json
Accept-Language: en-US
Accept-Encoding: br, gzip
```

The server selects an appropriate representation.

Relevant concepts include:

```text
media type
language
content coding
charset
Vary
```

---

# 68. HTTP Connection Architecture

A typical HTTPS request involves several layers:

```text
Application
    │
HTTP
    │
TLS
    │
TCP
    │
IP
    │
Ethernet/Wi-Fi
```

For HTTP/3:

```text
Application
    │
HTTP/3
    │
QUIC
    │
UDP
    │
IP
    │
Ethernet/Wi-Fi
```

This distinction is important when debugging latency.

---

# 69. HTTPS

HTTPS is HTTP transported over TLS.

Historically:

```text
HTTP
  ↓
TLS
  ↓
TCP
```

The security properties include:

* confidentiality;
* integrity;
* server authentication;
* optionally client authentication.

HTTP itself does not provide encryption.

TLS does.

---

# 70. TLS Handshake

For TLS 1.3, conceptually:

```text
Client
   │
   │ ClientHello
   ▼
Server
   │
   │ ServerHello
   │ Certificate
   │ Finished
   ▼
Client
   │
   │ Finished
   ▼
Encrypted application data
```

HTTP requests are carried after the TLS handshake establishes the secure channel.

With HTTP/2, TLS is commonly used.

With HTTP/3, QUIC incorporates TLS 1.3 into the transport handshake.

---

# 71. ALPN

ALPN allows the TLS handshake to negotiate the application protocol.

Examples:

```text
h2
```

for HTTP/2.

```text
h3
```

is associated with HTTP/3 protocol negotiation mechanisms, though HTTP/3 itself uses QUIC's TLS integration rather than ordinary TCP-based TLS.

Conceptually:

```text
Client:
"I support HTTP/2."

Server:
"I select HTTP/2."

        ↓

HTTP/2 communication
```

---

# 72. HTTP Intermediaries

HTTP commonly passes through intermediaries.

## Proxy

A forward proxy operates on behalf of the client.

```text
Client
  ↓
Proxy
  ↓
Internet
```

## Reverse Proxy

A reverse proxy operates in front of servers.

```text
Client
  ↓
Reverse Proxy
  ↓
Application
```

Examples of reverse-proxy responsibilities include:

* TLS termination;
* load balancing;
* caching;
* authentication;
* routing;
* rate limiting;
* compression;
* observability.

---

# 73. Gateway

A gateway can translate between protocols or systems.

For example:

```text
HTTP
 ↓
API Gateway
 ↓
gRPC
 ↓
Internal Service
```

The gateway can expose an HTTP interface while using another protocol internally.

---

# 74. CDN

A CDN is effectively a distributed set of intermediaries/caches.

Conceptually:

```text
Client
   │
   ▼
Nearest CDN edge
   │
   ├── Cache HIT
   │
   └── Cache MISS
          │
          ▼
       Origin
```

The primary performance benefit is moving frequently accessed representations closer to users.

---

# 75. HTTP Request Lifecycle

A typical HTTPS request can involve:

```text
1. DNS resolution
       ↓
2. TCP connection
       ↓
3. TLS handshake
       ↓
4. HTTP protocol negotiation
       ↓
5. HTTP request
       ↓
6. Server processing
       ↓
7. HTTP response
       ↓
8. Response decoding
       ↓
9. Connection reuse
```

For HTTP/2:

```text
DNS
 ↓
TCP
 ↓
TLS
 ↓
ALPN
 ↓
HTTP/2
```

For HTTP/3:

```text
DNS / service discovery
 ↓
QUIC
 ↓
TLS 1.3 within QUIC
 ↓
HTTP/3
```

---

# 76. HTTP Latency Components

A request's latency can be divided into:

```text
DNS lookup
+
Connection establishment
+
TLS handshake
+
Request transmission
+
Server queueing
+
Application processing
+
Database/dependency latency
+
Response transmission
+
Client processing
```

Therefore:

```text
HTTP latency ≠ application latency
```

When optimizing HTTP clients, all of these components need to be considered.

---

# 77. Connection Reuse

Connection reuse is one of the simplest HTTP optimizations.

Without reuse:

```text
Request
 ↓
Connect
 ↓
TLS
 ↓
HTTP
 ↓
Close
```

Repeated many times.

With reuse:

```text
Connect
 ↓
TLS
 ↓
HTTP request 1
HTTP request 2
HTTP request 3
HTTP request 4
...
```

This is particularly important when:

* latency is high;
* TLS handshakes are expensive;
* many requests target the same origin.

---

# 78. HTTP/1.1 Pipelining

HTTP/1.1 historically defined pipelining:

```text
Request 1
Request 2
Request 3
```

could be sent without waiting for the response to each request.

However, deployment problems and head-of-line blocking made it unattractive.

HTTP/2's multiplexing provides a much better solution.

---

# 79. HTTP/2 Stream Multiplexing

Instead of:

```text
Connection A → Request A
Connection B → Request B
Connection C → Request C
```

HTTP/2 can do:

```text
Single TCP connection

Stream 1 → Request A
Stream 3 → Request B
Stream 5 → Request C
```

This reduces the need for multiple TCP connections.

---

# 80. HTTP/3 Stream Independence

HTTP/3 goes further:

```text
QUIC connection

Stream 1
Stream 2
Stream 3
Stream 4
```

Loss on Stream 2 does not inherently block delivery of data on Stream 3.

This is one of the fundamental architectural differences between HTTP/2 and HTTP/3.

---

# 81. Flow Control

HTTP/2 and HTTP/3 need mechanisms to prevent a sender from overwhelming a receiver.

Flow control exists at multiple levels.

Conceptually:

```text
Sender
  │
  │ DATA DATA DATA DATA
  ▼
Receiver
  │
  └── "Window remaining: N"
```

HTTP/2 uses `WINDOW_UPDATE`.

HTTP/3 uses QUIC flow-control mechanisms.

---

# 82. HTTP/2 SETTINGS

HTTP/2 peers exchange settings that control protocol behavior.

The SETTINGS frame can communicate values such as:

```text
header table size
maximum concurrent streams
initial flow-control window
maximum frame size
maximum header list size
```

These parameters allow peers to adapt behavior to their capabilities.

---

# 83. HTTP/2 GOAWAY

A peer can use `GOAWAY` to indicate that it is shutting down the connection or will not accept new streams.

Conceptually:

```text
Existing streams
      │
      ├── complete
      ├── complete
      └── complete

New streams
      │
      └── rejected
```

This permits graceful connection shutdown.

---

# 84. HTTP/2 RST_STREAM

`RST_STREAM` terminates an individual stream.

This is different from closing the entire connection.

```text
HTTP/2 connection
│
├── Stream 1 → active
├── Stream 3 → RST_STREAM
├── Stream 5 → active
└── Stream 7 → active
```

Only Stream 3 is terminated.

---

# 85. HTTP/2 PING

PING is used to test connection liveness and measure round-trip behavior.

It operates at the HTTP/2 connection level.

---

# 86. HTTP/3 Connection Migration

QUIC supports connection migration.

This is useful for clients whose network path changes.

For example:

```text
Wi-Fi
  │
  ▼
QUIC connection
  │
  ▼
Mobile network
```

The connection can potentially continue without reconstructing the entire application-level connection.

This is particularly relevant for mobile devices.

---

# 87. Request and Response Bodies Are Byte Streams

An HTTP body should conceptually be treated as:

```text
byte stream
```

not:

```text
string
```

For example:

```text
00 FF 12 84 A1 00 7E ...
```

is perfectly valid HTTP content if the associated media type and application semantics permit it.

HTTP does not require the body to be human-readable.

---

# 88. Unicode and HTTP

HTTP's wire framing is fundamentally based on octets.

Unicode becomes relevant when interpreting content.

For example, UTF-8 encoding:

```text
A
```

is:

```text
41
```

while:

```text
€
```

is:

```text
E2 82 AC
```

Therefore:

```text
1 Unicode character
=
possibly multiple bytes
```

This is why protocol framing must happen before application-level character decoding.

---

# 89. HTTP Header Size

HTTP does not define one universal small maximum header size.

Implementations impose limits for practical and security reasons.

Examples include:

```text
maximum request-line size
maximum header-field size
maximum total header size
maximum header-list size
```

HTTP/2 and HTTP/3 have protocol mechanisms related to header-list sizing.

Servers such as:

```text
nginx
Apache HTTP Server
Envoy
HAProxy
```

may impose additional implementation-specific limits.

---

# 90. Request Smuggling

HTTP request smuggling is a security class involving inconsistent interpretation of message boundaries by different HTTP components.

For example:

```text
Client
  ↓
Proxy
  ↓
Backend
```

If the proxy interprets message framing differently from the backend, an attacker may cause one request to be interpreted as multiple requests.

Historically important mechanisms include conflicts involving:

```text
Content-Length
Transfer-Encoding
```

This is one reason HTTP message parsing must be strict and consistent.

RFC 9112 explicitly discusses request smuggling and dangerous parsing differences.

---

# 91. Response Splitting

Response splitting exploits incorrect handling of CRLF sequences in response fields.

An attacker may attempt to inject:

```text
CRLF
```

into data that becomes an HTTP header.

Because:

```text
CRLF CRLF
```

can terminate the header section, this can alter HTTP message boundaries.

Therefore applications must never blindly insert untrusted data into HTTP fields.

---

# 92. CRLF Injection

The dangerous bytes are:

```text
CR = 0x0D
LF = 0x0A
```

An attacker attempting to inject a new HTTP field might attempt:

```text
%0D%0A
```

depending on the context.

Modern HTTP implementations reject or sanitize invalid field values.

Application frameworks should not manually construct HTTP headers from untrusted input.

---

# 93. HTTP Desynchronization

A broader class of vulnerabilities occurs when:

```text
Frontend parser
```

and:

```text
Backend parser
```

disagree about:

```text
where a request ends
where a request begins
which header has precedence
how whitespace is interpreted
```

This is especially dangerous in architectures containing:

```text
CDN
 ↓
WAF
 ↓
Reverse proxy
 ↓
Application server
```

Every component must interpret HTTP framing consistently.

---

# 94. HTTP Header Injection

Never construct:

```http
X-Custom-Header: <untrusted user input>
```

without appropriate validation.

An attacker-controlled CRLF could historically transform:

```text
Header: attacker
```

into:

```text
Header: attacker
Injected: malicious
```

Modern frameworks generally prevent this, but application developers should still treat header values as structured protocol data rather than arbitrary strings.

---

# 95. HTTP Cache Poisoning

A cache can become dangerous if it stores a response under the wrong cache key or ignores request properties that affect the response.

Important concepts include:

```text
Cache-Control
Vary
Host
request target
authorization
cookies
content negotiation
```

A cache must not reuse a response when the semantics require a different response.

---

# 96. HTTP Authentication and TLS Are Different

TLS can authenticate the server:

```text
Client
  │
  │ TLS
  ▼
Server identity verified
```

HTTP authentication can authenticate the application user:

```text
HTTP
 │
 └── Authorization: Bearer ...
```

Therefore:

```text
TLS authentication
    ≠
HTTP authentication
```

They operate at different layers.

---

# 97. Idempotency and Retries

A client may need to retry requests after network failures.

This is dangerous for non-idempotent operations.

For example:

```http
POST /payments
```

may have reached the server even though the client never received the response.

If the client blindly retries:

```text
POST /payments
POST /payments
```

the payment could potentially be processed twice.

Application-level idempotency keys can help:

```http
Idempotency-Key: 7f5e...
```

This is commonly used by payment APIs, although the specific header is an application convention rather than a universal HTTP semantic requirement.

---

# 98. `Retry-After`

Servers can indicate when a client should retry.

Example:

```http
HTTP/1.1 503 Service Unavailable
Retry-After: 60
```

The value can indicate either:

```text
seconds
```

or an HTTP date.

Clients should respect server-provided retry guidance where appropriate.

---

# 99. HTTP Timeouts

A robust HTTP client should generally have explicit timeouts.

Conceptually:

```text
connect timeout
+
TLS timeout
+
request/write timeout
+
response/read timeout
+
overall deadline
```

A timeout is not an HTTP protocol status code.

For example:

```text
HTTP request
    ↓
TCP connection attempt
    ↓
TIMEOUT
```

may result in a client-side exception without any HTTP response being received.

Therefore:

```text
HTTP 504
```

and:

```text
client-side timeout
```

are not equivalent.

---

# 100. HTTP Error vs Transport Error

This distinction is extremely important.

## HTTP error

The server successfully communicated using HTTP:

```http
HTTP/1.1 404 Not Found
```

The client received a valid HTTP response.

## Transport error

No valid HTTP response was received.

Examples:

```text
DNS failure
TCP connection refused
TLS handshake failure
connection reset
timeout
QUIC failure
```

A client library may expose these as exceptions rather than HTTP status codes.

---

# 101. HTTP/1.1 Wire Example

Consider:

```http
POST /api/users HTTP/1.1
Host: example.com
Content-Type: application/json
Content-Length: 27
Accept: application/json

{"name":"Alice","age":30}
```

The logical structure is:

```text
┌─────────────────────────────────────────┐
│ Request-Line                            │
├─────────────────────────────────────────┤
│ Host field                              │
├─────────────────────────────────────────┤
│ Content-Type field                      │
├─────────────────────────────────────────┤
│ Content-Length field                    │
├─────────────────────────────────────────┤
│ Accept field                            │
├─────────────────────────────────────────┤
│ CRLF                                    │
├─────────────────────────────────────────┤
│ Message Body                            │
└─────────────────────────────────────────┘
```

The header/body separator is:

```text
0D 0A 0D 0A
```

---

# 102. HTTP/1.1 Parser Model

A robust parser can conceptually perform:

```text
Receive octets
      │
      ▼
Find request-line CRLF
      │
      ▼
Parse method
      │
      ▼
Parse request-target
      │
      ▼
Parse HTTP version
      │
      ▼
Parse field lines
      │
      ▼
Detect empty CRLF
      │
      ▼
Determine message-body length
      │
      ▼
Read exact body bytes
```

Only after this framing step should application-level interpretation occur.

---

# 103. Why Byte-Level Parsing Matters

Consider these bytes:

```text
41 0D 0A 42
```

As bytes:

```text
A
CR
LF
B
```

If the parser treats `0D 0A` as a protocol line terminator, it may interpret the bytes differently depending on whether they occur inside:

```text
request-line
header field
body
```

The parser must therefore know exactly which grammar it is currently parsing.

This is why HTTP parsing is fundamentally a protocol parsing problem, not merely string manipulation.

---

# 104. HTTP/2 Does Not Send HTTP/1.1 Lines

This is a common misconception.

HTTP/2 does **not** simply take:

```http
GET / HTTP/1.1
Host: example.com
```

and compress the text.

Instead, it maps the semantic information into binary frames.

There is no HTTP/1.1-style:

```text
GET / HTTP/1.1\r\n
Host: example.com\r\n
\r\n
```

on an HTTP/2 wire.

---

# 105. HTTP/3 Does Not Send HTTP/2 Frames Over UDP

Likewise:

```text
HTTP/3 ≠ HTTP/2 frames over UDP
```

HTTP/3 has its own framing defined by RFC 9114 and operates over QUIC.

The stack is:

```text
HTTP semantics
      ↓
HTTP/3 framing
      ↓
QUIC streams/packets
      ↓
UDP datagrams
```

---

# 106. HTTP/2 vs HTTP/3

| Feature               | HTTP/2            | HTTP/3                       |
| --------------------- | ----------------- | ---------------------------- |
| Application semantics | HTTP              | HTTP                         |
| Framing               | Binary            | Binary                       |
| Multiplexing          | Yes               | Yes                          |
| Transport             | TCP               | QUIC                         |
| Network protocol      | TCP               | UDP                          |
| TLS                   | TLS commonly used | TLS 1.3 integrated into QUIC |
| Header compression    | HPACK             | QPACK                        |
| TCP HOL blocking      | Yes               | No                           |
| Connection migration  | Limited           | QUIC supports it             |
| Main RFC              | 9113              | 9114                         |

---

# 107. Important RFC Map

## Core HTTP

### RFC 9110

**HTTP Semantics**

Defines:

* methods;
* status codes;
* URI semantics;
* fields;
* representations;
* content negotiation;
* authentication framework;
* conditional requests;
* ranges;
* message abstraction;
* HTTP architecture.

---

### RFC 9111

**HTTP Caching**

Defines:

* cache behavior;
* freshness;
* validation;
* cache directives;
* cache keys;
* `Vary`;
* reuse of responses.

---

### RFC 9112

**HTTP/1.1**

Defines:

* HTTP/1.1 syntax;
* request lines;
* status lines;
* fields;
* CRLF framing;
* message-body framing;
* connection management;
* chunked transfer coding;
* HTTP/1.1 security considerations.

---

### RFC 9113

**HTTP/2**

Defines:

* binary framing;
* streams;
* frames;
* SETTINGS;
* flow control;
* multiplexing;
* HTTP/2 error handling;
* mapping HTTP semantics to HTTP/2.

---

### RFC 9114

**HTTP/3**

Defines:

* HTTP over QUIC;
* HTTP/3 streams;
* HTTP/3 frames;
* control streams;
* QPACK integration;
* HTTP/3-specific error handling.

---

# 108. Important Historical RFCs

| RFC      | Topic                                                                    |
| -------- | ------------------------------------------------------------------------ |
| RFC 1945 | HTTP/1.0                                                                 |
| RFC 2068 | Early HTTP/1.1                                                           |
| RFC 2616 | HTTP/1.1, later obsoleted                                                |
| RFC 7230 | HTTP/1.1 message syntax, obsolete                                        |
| RFC 7231 | HTTP semantics/content, obsolete                                         |
| RFC 7232 | Conditional requests, obsolete                                           |
| RFC 7233 | Range requests, obsolete                                                 |
| RFC 7234 | HTTP caching, obsolete                                                   |
| RFC 7235 | HTTP authentication, obsolete                                            |
| RFC 7540 | HTTP/2, obsolete                                                         |
| RFC 7541 | HPACK                                                                    |
| RFC 7538 | HTTP 308 Permanent Redirect                                              |
| RFC 5789 | PATCH method                                                             |
| RFC 6265 | Cookies                                                                  |
| RFC 6585 | Additional HTTP status codes                                             |
| RFC 8297 | 103 Early Hints                                                          |
| RFC 8470 | 425 Too Early                                                            |
| RFC 8740 | HTTP/2 TLS/ALPN update                                                   |
| RFC 9110 | HTTP Semantics                                                           |
| RFC 9111 | HTTP Caching                                                             |
| RFC 9112 | HTTP/1.1                                                                 |
| RFC 9113 | HTTP/2                                                                   |
| RFC 9114 | HTTP/3                                                                   |
| RFC 9204 | QPACK                                                                    |
| RFC 9218 | Extensible Prioritization Scheme for HTTP                                |
| RFC 9297 | HTTP Datagrams                                                           |
| RFC 9292 | Binary Representation of HTTP Messages / Capsule-related HTTP mechanisms |

---

# 109. RFC 7230–7235 and RFC 9110–9114

It is important not to treat the older RFCs as the current HTTP specification.

The transition is roughly:

```text
RFC 7230
   ↓
RFC 9112

RFC 7231
   ↓
RFC 9110

RFC 7232
   ↓
RFC 9110

RFC 7233
   ↓
RFC 9110

RFC 7234
   ↓
RFC 9111

RFC 7235
   ↓
RFC 9110

RFC 7540
   ↓
RFC 9113
```

The older RFCs remain extremely useful for historical understanding and for interpreting older implementations, but the RFC 9110-series documents should be treated as the current baseline.

---

# 110. HTTP Extensions

HTTP is intentionally extensible.

New methods, fields, status codes, and mechanisms can be defined without creating an entirely new version.

This is an important design principle.

For example:

```text
HTTP/1.1
```

does not need to become:

```text
HTTP/1.2
```

every time a new header field is introduced.

Instead, extension mechanisms can define new semantics.

---

# 111. HTTP Version Numbers

HTTP version numbers indicate compatibility with the wire protocol.

A major version change generally corresponds to incompatible message syntax.

This explains:

```text
HTTP/1.x
```

versus:

```text
HTTP/2
```

and:

```text
HTTP/3
```

HTTP/2 and HTTP/3 do not merely represent incremental changes to HTTP/1.1's textual wire format; they use fundamentally different framing.

---

# 112. The HTTP Message Abstraction

RFC 9110 defines an abstract HTTP message model:

```text
Message
├── Control data
├── Header fields
├── Content
└── Trailers
```

The actual wire representation depends on the HTTP version.

HTTP/1.1:

```text
Start line
Headers
CRLF
Content
```

HTTP/2:

```text
HEADERS frames
DATA frames
```

HTTP/3:

```text
HEADERS frames
DATA frames
```

This abstraction allows the semantics to remain consistent while the wire format evolves.

---

# 113. Trailers

HTTP can provide metadata after the content.

HTTP/1.1 chunked encoding historically supports trailers:

```http
Transfer-Encoding: chunked
Trailer: Digest
```

followed later by:

```text
0\r\n
Digest: ...\r\n
\r\n
```

HTTP/2 and HTTP/3 represent trailing fields using header blocks associated with the end of a stream.

Trailers are useful when metadata cannot be known until the content has been generated.

---

# 114. Content Digest and Integrity

HTTP representations can be protected with integrity metadata.

Depending on the mechanism and deployment, a digest can allow the recipient to verify that the received representation matches the expected content.

This is especially useful for:

* large downloads;
* content distribution;
* integrity-sensitive applications.

HTTP integrity mechanisms have evolved over time, so current implementations should consult the applicable current RFCs rather than relying solely on historical `Digest` behavior.

---

# 115. HTTP Priorities

Modern HTTP has an extensible priority model.

RFC 9218 defines:

**Extensible Prioritization Scheme for HTTP**

Priorities can help communicate which responses are more important.

For example:

```text
HTML document
   ↑
highest priority

CSS
   ↑

JavaScript
   ↑

Images
   ↑
lower priority
```

Actual scheduling is ultimately controlled by the implementation.

A priority signal is not a guarantee that a particular resource will be transmitted first.

---

# 116. Server Push

HTTP/2 originally included server push.

Conceptually:

```text
Client requests:
GET /index.html

Server:
"I know you will need style.css."

Server → style.css
Server → index.html
```

In practice, deployment experience showed that server push had significant complexity and limited usefulness.

HTTP/3 does not retain the HTTP/2 server push mechanism in the same way.

Modern applications commonly use other techniques such as:

```text
preload
103 Early Hints
application-aware prefetching
CDN caching
```

---

# 117. HTTP/2 Connection Coalescing

HTTP/2 can sometimes reuse one secure connection for multiple origins when the certificate and protocol conditions permit.

For example:

```text
Connection
     │
     ├── example.com
     └── api.example.com
```

This can reduce connection establishment overhead.

However, the security and authority requirements are strict, and a client must not assume arbitrary origins can share a connection.

---

# 118. DNS and HTTP

HTTP normally depends on name resolution.

For:

```text
https://api.example.com/users
```

the client may need to resolve:

```text
api.example.com
```

to an IP address.

DNS therefore participates in HTTP latency even though DNS itself is not part of HTTP.

Modern HTTP/3 deployments may also use mechanisms such as:

```text
HTTPS DNS records
Alt-Svc
```

to advertise protocol and service information.

---

# 119. Alt-Svc

The `Alt-Svc` mechanism allows a server to advertise an alternative service.

For example, a server can communicate that an HTTP service is also available through another endpoint/protocol.

This is particularly relevant to HTTP/3 deployment.

A client may initially connect using HTTP/2 and subsequently learn that HTTP/3 is available.

---

# 120. HTTP Observability

For debugging HTTP, capture at least:

```text
DNS time
TCP connect time
TLS handshake time
protocol negotiated
request headers
request body size
response status
response headers
response body size
TTFB
total duration
connection reuse
```

For HTTP/2/HTTP/3 additionally consider:

```text
stream ID
frame behavior
flow-control stalls
connection errors
QUIC packet loss
stream resets
```

---

# 121. Useful Diagnostic Tools

Common tools include:

```text
curl
openssl
tcpdump
Wireshark
nghttp2
nghttp
h2load
qlog
browser DevTools
```

For example:

```bash
curl -v https://example.com/
```

can expose:

```text
DNS/connection details
TLS negotiation
request headers
response headers
redirects
```

For TLS inspection:

```bash
openssl s_client -connect example.com:443
```

Network-level inspection can be performed with:

```bash
tcpdump
```

or Wireshark.

---

# 122. `curl` and Raw HTTP

A simple request:

```bash
curl -v http://example.com/
```

may reveal something conceptually similar to:

```http
GET / HTTP/1.1
Host: example.com
User-Agent: curl/...
Accept: */*
```

The actual bytes sent over the connection include CRLF delimiters.

This makes `curl` useful for learning HTTP semantics, although it abstracts away much of the wire protocol.

---

# 123. Raw HTTP over TCP

For an HTTP/1.1 server on a suitable plaintext endpoint, a raw TCP client can conceptually send:

```text
GET / HTTP/1.1\r\n
Host: example.com\r\n
Connection: close\r\n
\r\n
```

At the byte level:

```text
GET / HTTP/1.1
     ↓
47 45 54 20 2F 20 48 54 54 50 2F 31 2E 31

Host: example.com
     ↓
48 6F 73 74 3A 20 65 78 61 6D 70 6C 65 2E 63 6F 6D

CRLF:
0D 0A

Final CRLF:
0D 0A
```

The server then parses the bytes according to HTTP/1.1 grammar.

---

# 124. A Complete Mental Model

A useful layered model is:

```text
┌─────────────────────────────────────┐
│ Application semantics               │
│ JSON / HTML / XML / binary data     │
├─────────────────────────────────────┤
│ HTTP semantics                      │
│ methods / status / headers / cache  │
├─────────────────────────────────────┤
│ HTTP version framing                │
│ HTTP/1.1 / HTTP/2 / HTTP/3          │
├─────────────────────────────────────┤
│ Transport                           │
│ TCP / QUIC                          │
├─────────────────────────────────────┤
│ Security                            │
│ TLS / QUIC TLS                      │
├─────────────────────────────────────┤
│ Network                             │
│ IP                                  │
├─────────────────────────────────────┤
│ Link                                │
│ Ethernet / Wi-Fi / etc.             │
└─────────────────────────────────────┘
```

The precise placement of TLS differs for HTTP/3 because QUIC incorporates TLS 1.3 into the transport handshake.

---

# 125. The Most Important Distinctions

For an in-depth understanding of HTTP, the following distinctions should be kept separate.

## HTTP semantics vs wire syntax

```text
GET means "retrieve"
```

is semantics.

```text
GET / HTTP/1.1\r\n
```

is HTTP/1.1 wire syntax.

---

## Representation vs message framing

```text
JSON
```

is representation semantics.

```text
Content-Length: 123
```

helps delimit the content in HTTP/1.1.

---

## HTTP vs TLS

```text
HTTP
```

defines application protocol semantics.

```text
TLS
```

provides secure transport properties.

---

## HTTP error vs transport error

```text
404
```

is an HTTP response.

```text
connection reset
```

is a transport failure.

---

## HTTP/1.1 vs HTTP/2 vs HTTP/3

They largely share HTTP semantics but differ substantially in wire representation and transport.

```text
HTTP/1.1 → textual syntax over TCP
HTTP/2   → binary frames over TCP
HTTP/3   → binary frames over QUIC/UDP
```

---

# 126. Recommended RFC Reading Order

For a serious understanding of HTTP, read the specifications in this order.

## Level 1 — Semantics

### RFC 9110

Start here.

Understand:

* resources;
* representations;
* methods;
* status codes;
* fields;
* content negotiation;
* conditional requests;
* ranges;
* authentication;
* message abstraction.

---

## Level 2 — HTTP/1.1 Wire Protocol

### RFC 9112

Study:

* ABNF;
* request line;
* status line;
* field syntax;
* CRLF;
* message-body framing;
* `Content-Length`;
* `Transfer-Encoding`;
* chunked encoding;
* connection management.

This is the best specification for understanding HTTP at the raw-byte level.

---

## Level 3 — Caching

### RFC 9111

Study:

* freshness;
* validation;
* cache keys;
* `Cache-Control`;
* `Vary`;
* revalidation;
* cache invalidation behavior.

---

## Level 4 — HTTP/2

### RFC 9113

Study:

* connection preface;
* frames;
* streams;
* SETTINGS;
* flow control;
* HEADERS;
* DATA;
* RST_STREAM;
* GOAWAY;
* multiplexing.

Then read:

### RFC 7541

for HPACK.

---

## Level 5 — HTTP/3

### RFC 9114

Study:

* HTTP/3 streams;
* control streams;
* frames;
* pseudo-headers;
* QUIC integration;
* HTTP/3 errors.

Then read:

### RFC 9204

for QPACK.

---

# 127. Core RFC Reference Table

| RFC          | Subject                     | Importance                          |
| ------------ | --------------------------- | ----------------------------------- |
| **RFC 1945** | HTTP/1.0                    | Historical foundation               |
| **RFC 2068** | HTTP/1.1                    | Historical                          |
| **RFC 2616** | HTTP/1.1                    | Historical; obsolete                |
| **RFC 7230** | HTTP/1.1 syntax             | Historical; obsolete                |
| **RFC 7231** | HTTP semantics              | Historical; obsolete                |
| **RFC 7232** | Conditional requests        | Historical; obsolete                |
| **RFC 7233** | Range requests              | Historical; obsolete                |
| **RFC 7234** | HTTP caching                | Historical; obsolete                |
| **RFC 7235** | HTTP authentication         | Historical; obsolete                |
| **RFC 7540** | HTTP/2                      | Obsolete; replaced by RFC 9113      |
| **RFC 7541** | HPACK                       | Important for HTTP/2                |
| **RFC 7538** | HTTP 308                    | Incorporated into current semantics |
| **RFC 5789** | PATCH                       | Important method extension          |
| **RFC 6265** | Cookies                     | Important state mechanism           |
| **RFC 6585** | Additional status codes     | Important                           |
| **RFC 8297** | 103 Early Hints             | Modern optimization                 |
| **RFC 8470** | 425 Too Early               | Replay/early-data protection        |
| **RFC 9110** | HTTP Semantics              | **Core current specification**      |
| **RFC 9111** | HTTP Caching                | **Core current specification**      |
| **RFC 9112** | HTTP/1.1                    | **Core current specification**      |
| **RFC 9113** | HTTP/2                      | **Core current specification**      |
| **RFC 9114** | HTTP/3                      | **Core current specification**      |
| **RFC 9204** | QPACK                       | HTTP/3 header compression           |
| **RFC 9218** | HTTP priorities             | Modern prioritization               |
| **RFC 9297** | HTTP Datagrams              | HTTP extension                      |
| **RFC 8441** | Extended CONNECT for HTTP/2 | WebSocket-related                   |
| **RFC 7838** | HTTP Alternative Services   | Protocol/service discovery          |

---

# 128. Final Summary

HTTP is best understood as a collection of related concepts rather than simply:

```text
GET URL
```

At the semantic level:

```text
HTTP
├── Resources
├── Methods
├── Representations
├── Fields
├── Status codes
├── Caching
├── Conditional requests
├── Content negotiation
├── Authentication
├── Redirection
└── Intermediaries
```

At the wire level:

```text
HTTP/1.1
├── Start line
├── CRLF
├── Fields
├── CRLF
└── Content
```

HTTP/2 changes that to:

```text
HTTP/2
├── Connection
├── Streams
├── Frames
│   ├── HEADERS
│   ├── DATA
│   ├── SETTINGS
│   ├── WINDOW_UPDATE
│   ├── RST_STREAM
│   ├── GOAWAY
│   └── ...
└── HPACK
```

HTTP/3 changes the transport architecture:

```text
HTTP/3
├── HTTP semantics
├── HTTP/3 frames
├── QUIC streams
├── QUIC transport
├── QPACK
└── UDP
```

The central architectural evolution is therefore:

```text
HTTP/0.9
    │
    │ extremely simple text request
    ▼
HTTP/1.0
    │
    │ headers + status + body
    ▼
HTTP/1.1
    │
    │ persistent connections + robust framing
    ▼
HTTP/2
    │
    │ binary frames + multiplexed streams
    ▼
HTTP/3
    │
    │ HTTP semantics + QUIC
    ▼
Modern HTTP
```

The most important specifications to understand are:

```text
RFC 9110  → What HTTP means
RFC 9111  → How HTTP caching works
RFC 9112  → How HTTP/1.1 is encoded on the wire
RFC 9113  → How HTTP/2 is framed
RFC 9114  → How HTTP/3 is framed over QUIC
RFC 7541  → HPACK
RFC 9204  → QPACK
```

For practical protocol engineering, **RFC 9110 + RFC 9112** provide the most important foundation. Once the HTTP/1.1 byte-level model is understood, HTTP/2 and HTTP/3 become easier to understand because they can be viewed as different, more efficient mappings of substantially the same HTTP semantics onto different framing and transport architectures.

## Primary References

The authoritative source for the standards in this document is the **RFC Editor / IETF RFC archive**.

Key references:

* RFC 1945 — *Hypertext Transfer Protocol — HTTP/1.0*
* RFC 2068 — *HTTP/1.1*
* RFC 2616 — *Hypertext Transfer Protocol — HTTP/1.1*
* RFC 7230 — *HTTP/1.1: Message Syntax and Routing*
* RFC 7231 — *HTTP/1.1: Semantics and Content*
* RFC 7232 — *HTTP/1.1: Conditional Requests*
* RFC 7233 — *HTTP/1.1: Range Requests*
* RFC 7234 — *HTTP/1.1: Caching*
* RFC 7235 — *HTTP/1.1: Authentication*
* RFC 7540 — *Hypertext Transfer Protocol Version 2*
* RFC 7541 — *HPACK: Header Compression for HTTP/2*
* RFC 9110 — *HTTP Semantics*
* RFC 9111 — *HTTP Caching*
* RFC 9112 — *HTTP/1.1*
* RFC 9113 — *HTTP/2*
* RFC 9114 — *HTTP/3*
* RFC 9204 — *QPACK: Field Compression for HTTP/3*
* RFC 9218 — *Extensible Prioritization Scheme for HTTP*
* RFC 5789 — *PATCH Method for HTTP*
* RFC 6265 — *HTTP State Management Mechanism*
* RFC 8297 — *An HTTP Status Code for Indicating Hints*
* RFC 8470 — *Using Early Data in HTTP*
* RFC 7838 — *HTTP Alternative Services*
* RFC 8441 — *Bootstrapping WebSockets with HTTP/2*
