# `requests`

## 1. Purpose

`requests` is a synchronous HTTP client library for Python.

Its primary purpose is to make HTTP communication straightforward:

```python
import requests

response = requests.get("https://example.com")
```

However, production use of HTTP involves considerably more than sending a URL.

A developer using `requests` effectively should understand:

* HTTP methods
* URLs and query parameters
* request headers
* request bodies
* response status codes
* response headers
* cookies
* redirects
* authentication
* TLS
* timeouts
* connection pooling
* sessions
* retries
* streaming
* multipart uploads
* proxies
* prepared requests
* transport adapters
* error handling
* resource lifecycle
* observability

The objective of this guide is to progress from:

```text
requests.get(...)
```

to:

```text
Session
    ↓
PreparedRequest
    ↓
HTTPAdapter
    ↓
urllib3 connection pool
    ↓
TCP/TLS
    ↓
HTTP server
```

---

## 2. Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

#### Linux/macOS

```bash
source .venv/bin/activate
```

#### Windows

```powershell
.venv\Scripts\activate
```

Install Requests:

```bash
python -m pip install requests
```

Check the installed version:

```bash
python -c "import requests; print(requests.__version__)"
```

The Requests documentation currently lists Python 3.10+ as officially supported.

---

## 3. The Fundamental Mental Model

An HTTP exchange is conceptually:

```text
Client
  │
  │  HTTP Request
  │
  ▼
Server
  │
  │  HTTP Response
  │
  ▼
Client
```

A request contains:

```text
Method
URL
Headers
Body
```

A response contains:

```text
Status Code
Headers
Body
```

Requests maps these concepts into Python objects.

```python
response = requests.get(url)
```

The result is a:

```python
requests.Response
```

object.

Conceptually:

```text
requests.get()
       │
       ▼
   Request
       │
       ▼
    Server
       │
       ▼
   Response
```

---

## 4. Your First Request

```python
import requests

response = requests.get("https://example.com")

print(response.status_code)
print(response.headers)
print(response.text)
```

The most important attributes are:

```python
response.status_code
response.headers
response.text
response.content
response.url
response.encoding
response.cookies
response.history
```

---

## 5. HTTP Methods

Requests provides convenience methods for the common HTTP methods.

```python
requests.get(url)
requests.post(url)
requests.put(url)
requests.patch(url)
requests.delete(url)
requests.head(url)
requests.options(url)
```

There is also the generic interface:

```python
requests.request(
    method="GET",
    url=url,
)
```

The generic method accepts the same major request parameters as the convenience functions.

---

## 6. GET Requests

Basic:

```python
response = requests.get(
    "https://example.com/users"
)
```

With query parameters:

```python
response = requests.get(
    "https://example.com/users",
    params={
        "page": 2,
        "limit": 50,
    },
)
```

Requests constructs the query string for you.

For example:

```text
?page=2&limit=50
```

You can inspect the final URL:

```python
print(response.url)
```

This is preferable to manually constructing:

```python
url = (
    "https://example.com/users"
    "?page=2&limit=50"
)
```

because Requests handles URL parameter encoding.

---

## 7. POST Requests

### Form-encoded data

```python
response = requests.post(
    "https://example.com/login",
    data={
        "username": "alice",
        "password": "secret",
    },
)
```

This normally produces:

```text
application/x-www-form-urlencoded
```

data.

---

## 8. JSON Requests

For JSON APIs, use `json=`.

```python
response = requests.post(
    "https://api.example.com/users",
    json={
        "name": "Alice",
        "email": "alice@example.com",
    },
)
```

This is preferable to manually doing:

```python
import json

requests.post(
    url,
    data=json.dumps(payload),
    headers={
        "Content-Type": "application/json"
    },
)
```

Requests handles the JSON serialization and appropriate request body handling.

---

## 9. Reading JSON Responses

```python
response = requests.get(
    "https://api.example.com/users"
)

data = response.json()
```

For example:

```python
users = response.json()

for user in users:
    print(user["name"])
```

`Response.json()` performs JSON decoding. It can fail if the response isn't valid JSON.

Therefore, don't blindly assume:

```python
data = response.json()
```

is always valid.

A more defensive approach:

```python
response.raise_for_status()

try:
    data = response.json()
except requests.JSONDecodeError as exc:
    raise RuntimeError(
        "Server returned invalid JSON"
    ) from exc
```

---

## 10. HTTP Status Codes

Never treat:

```python
response = requests.get(...)
```

as equivalent to:

```text
request succeeded
```

The network operation succeeding and the HTTP operation succeeding are different things.

For example:

```text
TCP connection succeeded
        ↓
HTTP request succeeded
        ↓
HTTP status = 404
```

The request itself was successfully delivered.

The server simply returned:

```text
404 Not Found
```

---

## 11. `raise_for_status()`

Requests provides:

```python
response.raise_for_status()
```

For successful responses it does nothing.

For unsuccessful HTTP responses it raises `HTTPError`.

Typical application code should therefore look like:

```python
response = requests.get(
    url,
    timeout=10,
)

response.raise_for_status()

data = response.json()
```

This is considerably safer than:

```python
data = requests.get(url).json()
```

---

## 12. Status Codes Should Still Be Interpreted

Sometimes a non-2xx status is part of normal application behaviour.

For example:

```python
response = requests.get(url)

if response.status_code == 404:
    return None

response.raise_for_status()
```

The rule is:

> Use `raise_for_status()` for unexpected HTTP failures, but explicitly handle statuses that are meaningful to your application's protocol.

---

## 13. Request Headers

Headers are passed using a dictionary:

```python
headers = {
    "Accept": "application/json",
    "User-Agent": "my-application/1.0",
}

response = requests.get(
    url,
    headers=headers,
)
```

Headers can also be configured at the session level.

```python
session = requests.Session()

session.headers.update({
    "Accept": "application/json",
    "User-Agent": "my-application/1.0",
})
```

---

## 14. Common HTTP Headers

Developers should understand at least:

```text
Accept
Content-Type
Authorization
User-Agent
Host
Cache-Control
If-None-Match
If-Modified-Since
ETag
Last-Modified
Location
Content-Length
Transfer-Encoding
Cookie
Set-Cookie
```

Requests does not magically interpret arbitrary custom headers as application logic. They are sent to the server as HTTP headers.

---

## 15. Response Headers

```python
content_type = response.headers.get(
    "Content-Type"
)

etag = response.headers.get(
    "ETag"
)
```

Headers behave approximately like a case-insensitive dictionary.

Prefer:

```python
response.headers.get("Content-Type")
```

over:

```python
response.headers["Content-Type"]
```

when the header may not exist.

---

## 16. Response Content

There are three commonly useful representations.

### Text

```python
response.text
```

### Bytes

```python
response.content
```

### JSON

```python
response.json()
```

Use:

```python
response.content
```

for binary data such as:

* images
* PDFs
* ZIP files
* arbitrary binary files

---

## 17. Character Encoding

Requests attempts to determine the response encoding.

```python
print(response.encoding)
```

You can inspect:

```python
response.apparent_encoding
```

and, when necessary, explicitly specify:

```python
response.encoding = "utf-8"

text = response.text
```

Do not confuse:

```text
bytes
```

with:

```text
characters
```

HTTP transports bytes.

Text requires decoding.

---

## 18. Error Model

Requests distinguishes several failure classes.

### Connection failure

```python
requests.exceptions.ConnectionError
```

Examples:

* DNS failure
* refused connection
* network failure

### Timeout

```python
requests.exceptions.Timeout
```

### HTTP error

```python
requests.exceptions.HTTPError
```

Produced by:

```python
response.raise_for_status()
```

### Redirect failure

```python
requests.exceptions.TooManyRedirects
```

All Requests-specific exceptions inherit from:

```python
requests.exceptions.RequestException
```

---

## 19. Production Error Handling

A reasonable baseline:

```python
import requests


try:
    response = requests.get(
        url,
        timeout=10,
    )

    response.raise_for_status()

except requests.Timeout:
    print("Request timed out")

except requests.ConnectionError:
    print("Could not connect to server")

except requests.HTTPError as exc:
    print(f"HTTP failure: {exc}")

except requests.RequestException as exc:
    print(f"Requests failure: {exc}")
```

Avoid:

```python
except Exception:
    pass
```

It destroys useful diagnostic information.

---

## 20. Timeouts

This is one of the most important production concepts.

Do not write:

```python
requests.get(url)
```

in production code unless you have a deliberate reason.

Requests does not impose a timeout by default. Without one, a network operation can wait indefinitely.

Use:

```python
requests.get(
    url,
    timeout=10,
)
```

---

## 21. Connect vs Read Timeout

You can specify:

```python
timeout=(3, 10)
```

meaning approximately:

```text
Connect timeout: 3 seconds
Read timeout:    10 seconds
```

This is different from:

```python
timeout=10
```

which applies the specified timeout value to the relevant connection/read operations.

Importantly, `timeout` is **not** a total request-duration limit. It controls how long Requests waits for network activity; a response download can therefore take longer overall if bytes continue arriving.

---

## 22. Timeouts Should Be Policy

Instead of scattering:

```python
timeout=10
```

throughout a codebase:

```python
DEFAULT_TIMEOUT = (3, 20)
```

then:

```python
response = session.get(
    url,
    timeout=DEFAULT_TIMEOUT,
)
```

Even better, define separate policies:

```python
CONNECT_TIMEOUT = 3
READ_TIMEOUT = 20
```

and:

```python
timeout=(
    CONNECT_TIMEOUT,
    READ_TIMEOUT,
)
```

---

## 23. Sessions

For multiple related requests, use:

```python
session = requests.Session()
```

instead of repeatedly doing:

```python
requests.get(...)
requests.get(...)
requests.post(...)
```

A Session provides:

* cookie persistence
* connection pooling
* shared configuration
* shared headers
* authentication configuration

Requests documents Sessions specifically as providing cookie persistence and connection pooling.

---

## 24. Basic Session Usage

```python
import requests

with requests.Session() as session:
    session.headers.update({
        "User-Agent": "my-client/1.0",
        "Accept": "application/json",
    })

    response = session.get(
        "https://api.example.com/users",
        timeout=10,
    )

    response.raise_for_status()
```

Using a context manager ensures the session is closed.

---

## 25. Why Sessions Matter

Consider:

```text
Request 1
    ↓
TCP connection
    ↓
TLS handshake
    ↓
HTTP request

Request 2
    ↓
TCP connection
    ↓
TLS handshake
    ↓
HTTP request
```

versus:

```text
Session
    ↓
connection pool
    ├── reusable connection
    ├── reusable connection
    └── reusable connection
```

Connection pooling reduces unnecessary connection setup.

Requests uses urllib3 underneath for connection pooling.

---

## 26. Session-Level Configuration

```python
session = requests.Session()

session.headers.update({
    "Accept": "application/json",
})

session.auth = (
    username,
    password,
)

session.params.update({
    "api_version": "2",
})
```

Requests combines session-level configuration with request-specific configuration.

Request-specific configuration can override session defaults.

---

## 27. Cookies

A Session persists cookies received from servers.

```python
with requests.Session() as session:

    session.get(
        "https://example.com/login"
    )

    response = session.get(
        "https://example.com/account"
    )
```

You can inspect:

```python
session.cookies
```

You can explicitly provide cookies:

```python
response = session.get(
    url,
    cookies={
        "session_id": "abc123"
    },
)
```

---

## 28. Authentication

### Basic Authentication

```python
response = requests.get(
    url,
    auth=("username", "password"),
)
```

Requests also provides:

```python
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth(
    "username",
    "password",
)
```

Requests supports Basic and Digest authentication directly.

Always use HTTPS when sending credentials.

---

## 29. Bearer Tokens

Many APIs use:

```http
Authorization: Bearer <token>
```

Implement:

```python
headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(
    url,
    headers=headers,
)
```

For a client making many requests, put this on the Session:

```python
session.headers.update({
    "Authorization": f"Bearer {token}"
})
```

---

## 30. Custom Authentication

Requests allows custom authentication handlers.

Subclass:

```python
requests.auth.AuthBase
```

Example:

```python
import requests


class APIKeyAuth(requests.auth.AuthBase):

    def __init__(self, api_key):
        self.api_key = api_key

    def __call__(self, request):
        request.headers["X-API-Key"] = self.api_key
        return request
```

Use:

```python
session.auth = APIKeyAuth(api_key)
```

The `AuthBase.__call__()` mechanism is the standard extension point for custom authentication.

---

## 31. Multipart File Uploads

Basic upload:

```python
with open("report.pdf", "rb") as file:
    response = requests.post(
        upload_url,
        files={
            "file": file,
        },
    )
```

Additional form data:

```python
with open("report.pdf", "rb") as file:
    response = requests.post(
        upload_url,
        data={
            "description": "Monthly report",
        },
        files={
            "file": file,
        },
    )
```

Use binary mode when uploading files. Requests explicitly recommends opening files in binary mode.

---

## 32. Multipart File Metadata

You can specify:

```python
files = {
    "file": (
        "report.pdf",
        file_object,
        "application/pdf",
    )
}
```

The tuple can also contain custom headers.

This is useful when the server requires a particular:

* filename
* MIME type
* per-part header

Requests supports 2-, 3-, and 4-element file tuples.

---

## 33. Streaming Downloads

Do not do this for a multi-gigabyte file:

```python
response = requests.get(url)

with open("large.iso", "wb") as f:
    f.write(response.content)
```

`response.content` loads the response body into memory.

Instead:

```python
with requests.get(
    url,
    stream=True,
    timeout=(5, 30),
) as response:

    response.raise_for_status()

    with open("large.iso", "wb") as file:

        for chunk in response.iter_content(
            chunk_size=1024 * 1024
        ):
            if chunk:
                file.write(chunk)
```

Requests recommends `iter_content()` for streamed downloads.

---

## 34. Why `stream=True` Matters

Without:

```python
stream=True
```

Requests downloads the response content immediately.

With:

```python
stream=True
```

the response body can be consumed incrementally.

Conceptually:

```text
Server
  │
  ├── chunk
  ├── chunk
  ├── chunk
  ├── chunk
  └── chunk
       ↓
    iter_content()
       ↓
       disk
```

This is important for:

* large downloads
* large API responses
* streaming APIs
* memory-constrained applications

---

## 35. Always Close Streamed Responses

Prefer:

```python
with requests.get(
    url,
    stream=True,
) as response:
    ...
```

rather than:

```python
response = requests.get(
    url,
    stream=True,
)
```

and relying on garbage collection.

The Session/connection pool needs the underlying connection to be released properly.

---

## 36. `iter_lines()`

For line-oriented streaming:

```python
with requests.get(
    url,
    stream=True,
) as response:

    response.raise_for_status()

    for line in response.iter_lines():
        if line:
            print(line.decode("utf-8"))
```

This is useful for:

* line-based APIs
* logs
* streaming text
* event-like protocols

---

## 37. `response.raw`

For low-level access:

```python
response = requests.get(
    url,
    stream=True,
)

raw = response.raw
```

You can read directly:

```python
data = raw.read(1024)
```

However, this is generally lower-level than necessary.

Prefer:

```python
iter_content()
```

unless you specifically need raw transport bytes.

Requests documents that `iter_content()` performs useful transfer decoding, whereas `raw` exposes the underlying raw stream.

---

## 38. Streaming Uploads

Requests can accept file-like objects:

```python
with open("large.bin", "rb") as file:

    response = requests.post(
        upload_url,
        data=file,
    )
```

This avoids first loading the entire file into a Python bytes object.

For advanced multipart streaming of very large files, the Requests documentation points to `requests-toolbelt`, because native Requests does not provide arbitrary large multipart streaming in the same way.

---

## 39. Redirects

Requests follows redirects automatically for most common request methods.

Inspect redirect history:

```python
response.history
```

For example:

```python
for redirect in response.history:
    print(
        redirect.status_code,
        redirect.url,
    )

print(response.url)
```

Disable redirects:

```python
response = requests.get(
    url,
    allow_redirects=False,
)
```

---

## 40. Redirect Security

Be particularly careful with authentication.

For example:

```text
https://trusted.example
       ↓ 302
https://untrusted.example
```

Credentials should not casually follow a redirect to an unrelated host.

Requests has redirect logic that can remove authorization when redirects move off-host.

Still, applications should not blindly trust arbitrary redirect chains.

---

## 41. TLS Verification

Requests verifies server TLS certificates by default.

```python
requests.get(
    "https://example.com",
    verify=True,
)
```

This is the correct default.

Never use:

```python
verify=False
```

as a generic solution to certificate problems.

Requests explicitly warns that disabling verification makes the connection vulnerable to man-in-the-middle attacks.

---

## 42. Custom CA Certificates

If your organization has a private CA:

```python
response = requests.get(
    url,
    verify="/path/to/ca-bundle.pem",
)
```

At the Session level:

```python
session.verify = "/path/to/ca-bundle.pem"
```

This allows proper certificate verification without disabling TLS validation.

---

## 43. Client Certificates / mTLS

For mutual TLS:

```python
response = requests.get(
    url,
    cert=(
        "/path/client.crt",
        "/path/client.key",
    ),
)
```

Or:

```python
session.cert = (
    "/path/client.crt",
    "/path/client.key",
)
```

Requests supports a client certificate file or a certificate/key pair.

---

## 44. Proxies

Requests supports HTTP and HTTPS proxy configuration.

Example:

```python
proxies = {
    "http": "http://proxy.example:8080",
    "https": "http://proxy.example:8080",
}

response = requests.get(
    url,
    proxies=proxies,
)
```

At the Session level:

```python
session.proxies.update(proxies)
```

Be aware that Requests can also obtain proxy configuration from the environment.

---

## 45. `trust_env`

A Session has:

```python
session.trust_env
```

By default this allows Requests to use relevant environment configuration, including proxy configuration and certain authentication sources.

For a controlled environment:

```python
session.trust_env = False
```

This is particularly relevant when writing software that must have deterministic network configuration.

Requests documents `trust_env` as controlling use of environment settings for proxy configuration, authentication and similar behaviour.

---

## 46. `.netrc`

Requests can use credentials from:

```text
~/.netrc
```

or equivalent platform-specific locations.

It can also use the `NETRC` environment variable.

This can be useful for command-line tooling, although applications should generally have an explicit and well-defined credential-management strategy.

Requests notes that `.netrc` credentials can take precedence over an `Authorization` header supplied through `headers=`.

---

## 47. Retries

Retries are deceptively complicated.

You should **not** simply do:

```python
for _ in range(5):
    try:
        requests.get(...)
        break
    except Exception:
        pass
```

Why?

Because not every operation is safe to retry.

Consider:

```http
POST /payments
```

If the server processed the request but the response was lost, retrying may create a second payment.

---

## 48. Idempotency

Generally safer retry candidates include operations such as:

```text
GET
HEAD
OPTIONS
```

depending on the server's semantics.

Operations such as:

```text
POST
```

may not be safely retryable unless the API provides an idempotency mechanism.

For example:

```http
Idempotency-Key: 9e6d...
```

The application must understand the server's semantics before introducing retries.

---

## 49. Retry Using `HTTPAdapter`

Requests provides transport adapters.

A common pattern is to use urllib3's `Retry`:

```python
import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


retry = Retry(
    total=3,
    backoff_factor=0.5,
    status_forcelist=[
        429,
        500,
        502,
        503,
        504,
    ],
    allowed_methods=[
        "GET",
        "HEAD",
        "OPTIONS",
    ],
)

adapter = HTTPAdapter(
    max_retries=retry
)

session = requests.Session()

session.mount(
    "https://",
    adapter,
)

session.mount(
    "http://",
    adapter,
)
```

Requests' built-in `HTTPAdapter` exposes `max_retries`, connection-pool sizing and blocking behaviour. For granular retry policies, Requests documents using urllib3's `Retry`.

---

## 50. Retry Backoff

A retry policy should generally avoid:

```text
request
retry immediately
retry immediately
retry immediately
retry immediately
```

because thousands of clients can synchronize their retries and make an overloaded server even worse.

Use backoff:

```text
Attempt 1
   ↓
wait
   ↓
Attempt 2
   ↓
longer wait
   ↓
Attempt 3
```

A production retry policy should consider:

* maximum attempts
* backoff
* jitter
* retryable status codes
* retryable methods
* `Retry-After`
* connection errors
* timeouts
* idempotency

---

## 51. Connection Pool Configuration

The default adapter can be customized:

```python
adapter = HTTPAdapter(
    pool_connections=20,
    pool_maxsize=50,
    pool_block=True,
)
```

These parameters affect connection pool caching and pool size.

`pool_block=True` causes callers to wait for an available pooled connection instead of creating behaviour outside the configured pool capacity.

This becomes relevant for high-concurrency applications.

---

## 52. Prepared Requests

Normally:

```python
response = session.get(url)
```

is enough.

But sometimes you need to inspect or modify the request immediately before transmission.

Use:

```python
from requests import Request

request = Request(
    "POST",
    url,
    json=payload,
)

prepared = session.prepare_request(request)
```

Now:

```python
prepared.method
prepared.url
prepared.headers
prepared.body
```

are available.

---

## 53. Why Prepared Requests Exist

The conceptual pipeline is:

```text
Request
   ↓
prepare
   ↓
PreparedRequest
   ↓
send
   ↓
Response
```

A `PreparedRequest` represents the final prepared HTTP request.

This is useful for:

* custom signing
* request inspection
* cryptographic signatures
* advanced authentication
* debugging
* custom request mutation

---

## 54. Sending a Prepared Request

```python
import requests

session = requests.Session()

request = requests.Request(
    "POST",
    url,
    json={"name": "Alice"},
)

prepared = session.prepare_request(request)

response = session.send(
    prepared,
    timeout=10,
)
```

---

## 55. Request Signing

A common advanced use case is:

```text
Request
   ↓
canonicalize
   ↓
hash/sign
   ↓
Authorization header
   ↓
send
```

A custom authentication object is often a cleaner abstraction:

```python
import hashlib
import hmac

from requests.auth import AuthBase


class HMACAuth(AuthBase):

    def __init__(self, secret):
        self.secret = secret.encode()

    def __call__(self, request):

        body = request.body or b""

        if isinstance(body, str):
            body = body.encode()

        signature = hmac.new(
            self.secret,
            body,
            hashlib.sha256,
        ).hexdigest()

        request.headers[
            "X-Signature"
        ] = signature

        return request
```

The real protocol would need a carefully specified canonical representation including method, path, timestamp, nonce, body digest, and other required fields.

Do not invent your own authentication protocol for production security without a proper threat model and cryptographic design.

---

## 56. Event Hooks

Requests supports response hooks.

```python
def log_response(response, *args, **kwargs):
    print(
        response.request.method,
        response.url,
        response.status_code,
    )

session = requests.Session()

session.hooks["response"].append(
    log_response
)
```

Hooks are useful for:

* instrumentation
* logging
* metrics
* diagnostics
* common response processing

Use them carefully; hidden behaviour in a shared Session can make debugging harder.

---

## 57. Request vs Response

One of the most useful things to understand is:

```python
response.request
```

This gives access to the request associated with the response.

For example:

```python
print(response.request.method)
print(response.request.url)
print(response.request.headers)
```

This is particularly useful when debugging:

* redirects
* authentication
* generated headers
* query strings
* request bodies

---

## 58. Inspecting the Prepared Request

```python
response = session.post(
    url,
    json={
        "name": "Alice"
    },
)

request = response.request

print(request.method)
print(request.url)
print(request.headers)
print(request.body)
```

This is one of the easiest ways to understand what Requests actually sent.

---

## 59. HTTP Caching

Requests itself is not a complete HTTP cache.

If an API supports:

```http
ETag: "abc123"
```

you can implement conditional requests.

First request:

```http
GET /resource
```

Response:

```http
ETag: "abc123"
```

Next request:

```http
GET /resource
If-None-Match: "abc123"
```

Server may return:

```http
304 Not Modified
```

Your application can then reuse its cached representation.

This is an excellent exercise for understanding HTTP rather than merely using Requests.

---

## 60. Pagination

Real APIs frequently paginate.

For example:

```json
{
    "items": [...],
    "next": "/users?page=2"
}
```

A simple implementation:

```python
url = first_url

while url:
    response = session.get(
        url,
        timeout=(3, 20),
    )

    response.raise_for_status()

    payload = response.json()

    for item in payload["items"]:
        process(item)

    url = payload.get("next")
```

Do not assume every API uses:

```text
?page=2
```

Common schemes include:

```text
page/limit
offset/limit
cursor
next URL
Link headers
```

---

## 61. Link Headers

Some APIs provide pagination using:

```http
Link: <https://example.com/items?page=2>; rel="next"
```

Requests exposes:

```python
response.links
```

This can simplify navigation of APIs that use standard link headers.

---

## 62. Rate Limiting

An API may return:

```http
429 Too Many Requests
```

Potentially accompanied by:

```http
Retry-After: 30
```

Your client should distinguish:

```text
429
```

from:

```text
400
```

and:

```text
401
```

A robust API client should have explicit policy for:

* rate limiting
* backoff
* `Retry-After`
* maximum retry duration
* request priority

---

## 63. API Client Architecture

Do not scatter Requests calls throughout an application.

Avoid:

```python
def create_user():
    requests.post(...)


def delete_user():
    requests.delete(...)


def get_user():
    requests.get(...)
```

through dozens of unrelated modules.

Instead:

```text
Application
     │
     ▼
API Client
     │
     ▼
Requests Session
     │
     ▼
HTTP
```

Example:

```python
class UserAPI:

    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url.rstrip("/")

    def get_user(self, user_id):

        response = self.session.get(
            f"{self.base_url}/users/{user_id}",
            timeout=(3, 20),
        )

        response.raise_for_status()

        return response.json()
```

---

## 64. Build a Reusable API Client

A better structure:

```text
myclient/
├── __init__.py
├── client.py
├── errors.py
├── models.py
├── auth.py
├── transport.py
└── cli.py
```

Conceptually:

```text
CLI
 │
 ▼
Domain API
 │
 ▼
HTTP Client
 │
 ▼
Session
 │
 ▼
HTTPAdapter
 │
 ▼
Requests
```

---

## 65. Base Client

```python
class APIClient:

    def __init__(
        self,
        base_url,
        token,
        timeout=(3, 20),
    ):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

        self.session = requests.Session()

        self.session.headers.update({
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "myclient/1.0",
        })

    def close(self):
        self.session.close()
```

Prefer:

```python
with APIClient(...) as client:
    ...
```

if you implement context-manager support.

---

## 66. Context Manager for API Clients

```python
class APIClient:

    def __enter__(self):
        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ):
        self.session.close()
```

Usage:

```python
with APIClient(
    base_url,
    token,
) as client:

    user = client.get_user(42)
```

---

## 67. Domain Errors

Don't expose raw Requests exceptions throughout a large application if you can provide a useful domain-level API.

For example:

```python
class APIError(Exception):
    pass


class AuthenticationError(APIError):
    pass


class NotFoundError(APIError):
    pass


class RateLimitError(APIError):
    pass
```

Then translate:

```python
if response.status_code == 401:
    raise AuthenticationError()

if response.status_code == 404:
    raise NotFoundError()

if response.status_code == 429:
    raise RateLimitError()
```

This keeps the rest of the application independent of HTTP implementation details.

---

## 68. Transport vs Application Errors

This distinction is essential.

### Transport failure

```text
DNS failure
TCP failure
TLS failure
timeout
```

No HTTP response may exist.

### HTTP failure

```text
401
403
404
429
500
503
```

An HTTP response exists.

### Application failure

The HTTP response may be:

```text
200 OK
```

but contain:

```json
{
    "success": false,
    "error": "..."
}
```

Your client must understand all three categories.

---

## 69. Testing Requests Code

Do not make real network calls in ordinary unit tests.

A useful architecture is:

```text
Application
     ↓
API Client
     ↓
Session
```

Inject the Session or transport boundary.

For example:

```python
class UserAPI:

    def __init__(self, session):
        self.session = session
```

Tests can then substitute a controlled client.

For more extensive HTTP mocking, dedicated libraries can intercept Requests traffic.

---

## 70. Test the Failure Cases

At minimum test:

```text
200
201
204
400
401
403
404
409
429
500
502
503
504
```

and:

```text
DNS failure
connection refused
connect timeout
read timeout
invalid JSON
unexpected content type
connection reset
malformed response
```

The exact set should depend on your API.

---

## 71. Logging

Avoid logging:

```python
print(response.request.headers)
```

in production if the headers may contain:

```text
Authorization
Cookie
API keys
session tokens
```

Instead sanitize.

For example:

```python
SENSITIVE_HEADERS = {
    "authorization",
    "cookie",
    "set-cookie",
}
```

Never treat HTTP logs as inherently safe.

---

## 72. Observability

A production API client should ideally record:

```text
request method
target host
endpoint
status code
latency
retry count
timeout
response size
request correlation ID
```

But avoid logging:

```text
passwords
tokens
API keys
cookies
sensitive request bodies
personal data
```

---

## 73. Correlation IDs

For distributed systems:

```python
headers = {
    "X-Request-ID": request_id,
}
```

or whatever correlation mechanism the service specifies.

This allows:

```text
Client
  │
  │ request-id: abc123
  ▼
API Gateway
  │
  ▼
Service A
  │
  ▼
Service B
```

to be correlated across logs.

---

## 74. Connection Pooling and Concurrency

A Session provides connection pooling.

However, you should be deliberate about sharing Sessions across threads.

A simple architecture is:

```text
Worker
   │
   └── Session
```

or a carefully designed client/transport layer with explicit concurrency requirements.

Do not assume:

> "Session has a connection pool, therefore I can freely share one Session between arbitrary concurrency models."

Test the exact usage pattern.

---

## 75. HTTPAdapter as an Extension Point

An Adapter sits approximately here:

```text
requests.Session
       │
       ▼
HTTPAdapter
       │
       ▼
urllib3
       │
       ▼
TCP/TLS
```

You can mount an adapter:

```python
session.mount(
    "https://",
    adapter,
)
```

or even by URL prefix:

```python
session.mount(
    "https://api.example.com/",
    adapter,
)
```

This allows different transport policies for different destinations.

---

## 76. Multiple Adapters

For example:

```python
session.mount(
    "https://internal.example.com/",
    internal_adapter,
)

session.mount(
    "https://",
    default_adapter,
)
```

The more specific prefix can receive specialized transport behaviour.

This is useful when different services have different:

* retry policies
* connection limits
* TLS configuration
* proxy requirements

---

## 77. Custom HTTP Adapters

You can subclass:

```python
requests.adapters.HTTPAdapter
```

and override transport behaviour.

Possible use cases include:

* custom TLS configuration
* specialized connection behaviour
* instrumentation
* custom transport integration

This is an advanced extension point.

Use it only when ordinary Session configuration is insufficient.

---

## 78. HTTP/HTTPS Is Not the Same as Requests

Requests is an HTTP client abstraction.

The stack is roughly:

```text
Your application
       │
       ▼
    Requests
       │
       ▼
    urllib3
       │
       ▼
Python socket / TLS stack
       │
       ▼
      TCP
       │
       ▼
      IP
```

Understanding this hierarchy makes advanced debugging substantially easier.

---

## 79. What Requests Does Not Provide

Requests is intentionally synchronous.

It is not an asynchronous HTTP client.

If an application requires high-volume asynchronous I/O, consider an async HTTP client such as `httpx` or `aiohttp` rather than attempting to force Requests into an asynchronous architecture.

Similarly, Requests should not be confused with:

* an API framework
* a web server
* a message queue
* a browser
* a full HTTP cache
* a distributed retry system

---

## 80. Security Checklist

For production Requests clients:

#### Always

```text
✓ HTTPS for sensitive communication
✓ TLS certificate verification
✓ explicit timeouts
✓ controlled retries
✓ validate external data
✓ handle HTTP errors
✓ protect credentials
✓ limit response sizes where appropriate
✓ sanitize logs
```

#### Avoid

```text
✗ verify=False in production
✗ unlimited retries
✗ requests without timeouts
✗ blindly following arbitrary redirects
✗ logging Authorization headers
✗ loading huge responses into memory
✗ retrying non-idempotent operations blindly
✗ trusting external JSON without validation
```

---

## 81. Production API Client Pattern

A good starting architecture is:

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def create_session(token: str) -> requests.Session:

    retry = Retry(
        total=3,
        backoff_factor=0.5,
        status_forcelist=[
            429,
            500,
            502,
            503,
            504,
        ],
        allowed_methods=[
            "GET",
            "HEAD",
            "OPTIONS",
        ],
    )

    adapter = HTTPAdapter(
        max_retries=retry,
        pool_connections=10,
        pool_maxsize=20,
        pool_block=True,
    )

    session = requests.Session()

    session.mount(
        "https://",
        adapter,
    )

    session.headers.update({
        "Accept": "application/json",
        "Authorization": f"Bearer {token}",
        "User-Agent": "myclient/1.0",
    })

    return session
```

Then:

```python
with create_session(token) as session:

    response = session.get(
        "https://api.example.com/users",
        timeout=(3, 20),
    )

    response.raise_for_status()

    users = response.json()
```

This is already substantially closer to production-quality HTTP client design than calling `requests.get()` throughout an application.

---

## 82. A Complete API Client Skeleton

```python
from __future__ import annotations

import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class APIClient:

    def __init__(
        self,
        base_url: str,
        token: str,
    ):
        self.base_url = base_url.rstrip("/")
        self.timeout = (3, 20)

        retry = Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=[
                429,
                500,
                502,
                503,
                504,
            ],
            allowed_methods=[
                "GET",
                "HEAD",
                "OPTIONS",
            ],
        )

        adapter = HTTPAdapter(
            max_retries=retry,
            pool_connections=10,
            pool_maxsize=20,
            pool_block=True,
        )

        self.session = requests.Session()

        self.session.mount(
            "https://",
            adapter,
        )

        self.session.headers.update({
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "myclient/1.0",
        })

    def get_user(self, user_id: int) -> dict:

        response = self.session.get(
            f"{self.base_url}/users/{user_id}",
            timeout=self.timeout,
        )

        response.raise_for_status()

        return response.json()

    def create_user(
        self,
        name: str,
        email: str,
    ) -> dict:

        response = self.session.post(
            f"{self.base_url}/users",
            json={
                "name": name,
                "email": email,
            },
            timeout=self.timeout,
        )

        response.raise_for_status()

        return response.json()

    def close(self) -> None:
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ):
        self.close()
```

Usage:

```python
with APIClient(
    "https://api.example.com",
    token,
) as client:

    user = client.get_user(42)

    print(user)
```

---

## 83. Progressive Exercises

The best way to learn Requests is not to read the entire API and then attempt to remember it.

Build progressively.

### Exercise 1 — GET

Write:

```text
fetch.py
```

Requirements:

* GET a URL
* print status code
* print headers
* print body

#### Learn

```text
get()
Response
status_code
headers
text
```

---

## Exercise 2 — Query Parameters

Build:

```bash
search.py --query python --page 2
```

Requirements:

* use `params=`
* print final URL
* parse JSON

#### Learn

```text
params
json()
url
```

---

## Exercise 3 — REST CRUD Client

Implement:

```text
GET
POST
PUT
PATCH
DELETE
```

#### Learn

```text
data
json
headers
status codes
raise_for_status
```

---

## Exercise 4 — Session-Based Client

Build:

```text
ApiClient
```

Requirements:

* persistent authentication
* default headers
* cookies
* connection pooling

#### Learn

```text
Session
headers
auth
cookies
```

---

## Exercise 5 — Robust Client

Add:

* timeout
* connection errors
* HTTP errors
* invalid JSON
* logging

#### Learn

```text
Timeout
ConnectionError
HTTPError
RequestException
```

---

## Exercise 6 — Retry Policy

Implement retries for:

```text
429
500
502
503
504
```

but do not automatically retry arbitrary POST requests.

#### Learn

```text
Retry
HTTPAdapter
backoff
idempotency
```

---

## Exercise 7 — Large File Downloader

Build:

```bash
download URL output.bin
```

Requirements:

* streaming
* configurable chunk size
* timeout
* progress reporting
* checksum verification

#### Learn

```text
stream=True
iter_content()
response.raw
resource management
```

---

## Exercise 8 — Multipart Uploader

Build:

```bash
upload FILE
```

Requirements:

* multipart upload
* metadata
* MIME type
* authentication
* error handling

---

## Exercise 9 — Paginated API Importer

Build:

```bash
import-users
```

Requirements:

```text
API
 ↓
pagination
 ↓
validation
 ↓
database
```

Add:

* retry
* rate limiting
* checkpointing
* idempotency

This exercise closely matches the Python project you described earlier.

---

## Exercise 10 — Production API Client

Build a reusable package:

```text
myapi/
├── client.py
├── auth.py
├── errors.py
├── models.py
├── pagination.py
├── transport.py
└── cli.py
```

It should provide:

* Session management
* authentication
* retries
* timeouts
* connection pooling
* pagination
* structured errors
* logging
* streaming
* testing
* CLI interface

At this point the learner should no longer think of Requests as:

```python
requests.get(...)
```

They should think of it as:

```text
Application
    │
    ▼
Domain API Client
    │
    ▼
Session
    │
    ├── headers
    ├── authentication
    ├── cookies
    ├── connection pool
    └── adapters
             │
             ▼
           HTTP
```

---

## 84. Requests Cheat Sheet

### Basic

```python
requests.get(url)
requests.post(url)
requests.put(url)
requests.patch(url)
requests.delete(url)
```

### Parameters

```python
params={}
data={}
json={}
headers={}
cookies={}
files={}
auth={}
timeout={}
proxies={}
verify={}
cert={}
```

### Response

```python
response.status_code
response.headers
response.text
response.content
response.json()
response.url
response.cookies
response.history
response.request
```

### Error handling

```python
response.raise_for_status()
```

```python
except requests.Timeout:
```

```python
except requests.ConnectionError:
```

```python
except requests.HTTPError:
```

```python
except requests.RequestException:
```

### Session

```python
session = requests.Session()
```

```python
session.headers.update(...)
```

```python
session.auth = ...
```

```python
session.cookies
```

```python
session.close()
```

### Streaming

```python
requests.get(
    url,
    stream=True,
)
```

```python
response.iter_content(...)
```

```python
response.iter_lines(...)
```

### TLS

```python
verify=True
```

```python
verify="/path/to/ca.pem"
```

```python
cert=(
    "client.crt",
    "client.key",
)
```

### Advanced

```python
requests.Request(...)
```

```python
session.prepare_request(...)
```

```python
session.send(...)
```

```python
HTTPAdapter(...)
```

```python
Retry(...)
```

```python
AuthBase
```

```python
session.mount(...)
```

```python
response.request
```

```python
response.links
```

---

## 85. The Mental Model to Retain

A developer who understands Requests should be able to reason about the following hierarchy:

```text
                    YOUR APPLICATION
                           │
                           ▼
                    API CLIENT CLASS
                           │
                           ▼
                    requests.Session
                           │
             ┌─────────────┼─────────────┐
             │             │             │
          Headers        Auth         Cookies
             │             │             │
             └─────────────┼─────────────┘
                           ▼
                     PreparedRequest
                           │
                           ▼
                     HTTPAdapter
                           │
                           ▼
                      urllib3
                           │
                     Connection Pool
                           │
                           ▼
                       TCP / TLS
                           │
                           ▼
                        SERVER
                           │
                           ▼
                       Response
                           │
             ┌─────────────┼──────────────┐
             │             │              │
          Status        Headers          Body
             │             │              │
             │             │       ┌──────┴──────┐
             │             │       │             │
             │             │     text         content
             │             │       │             │
             │             │      JSON         bytes
             │             │
             └─────────────┴──────────────┐
                                          ▼
                                  Application Logic
```

Once this model is understood, most of the Requests API becomes fairly intuitive.

The important progression is:

```text
requests.get()
      ↓
Request / Response
      ↓
timeouts + errors
      ↓
Session
      ↓
streaming
      ↓
authentication + TLS
      ↓
retries
      ↓
connection pooling
      ↓
PreparedRequest
      ↓
HTTPAdapter
      ↓
production API client
```

That is the level of progression I would expect for an engineer moving from **basic Python HTTP usage to competent production use of Requests**.

### Primary reference

The authoritative Requests documentation is the best reference for exact API behaviour, particularly for Sessions, adapters, prepared requests, TLS, streaming, authentication and exceptions.

[Requests documentation](https://requests.readthedocs.io/en/latest/?utm_source=chatgpt.com)
