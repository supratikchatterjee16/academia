# OpenSSL

This is a utility to work with security on Linux, and also on Windows. Here, we explore some practical setups to use.


## TLS Certificates for Browsers(using EdDSA)

Perfect — if you want to use your **local Root CA + EdDSA certificates in browsers**, we need to cover a few **extra details**, because web browsers are stricter than gRPC clients:

---

### TLS Certificates for Browsers

#### Key points:

1. **Browsers require SAN (Subject Alternative Name)** → Common Name (CN) alone is ignored.

   * If your cert doesn’t have SANs, Chrome/Firefox will reject it.

2. **Root CA must be installed into the browser/OS trust store** → Otherwise you’ll see *“Your connection is not private”*.

3. **Ed25519 support in browsers**:

   * Chrome (≥ 91), Firefox (≥ 68), and recent Safari support **Ed25519 X.509 certs**.
   * Old browsers may not.

4. For **local testing**:

   * Use hostnames like `myservice.local` or `test.local`, and add them to `/etc/hosts` (Linux/macOS) or `C:\Windows\System32\drivers\etc\hosts` (Windows).
   * Browsers don’t trust raw `localhost` with self-signed certs unless SAN includes it.

---

### Generating Browser-Compatible Ed25519 Certs

Let’s automate with an **OpenSSL config**.

#### 1. Create `openssl-san.cnf`

```ini
[ req ]
default_bits        = 2048
prompt              = no
default_md          = sha256
distinguished_name  = dn
req_extensions      = req_ext

[ dn ]
C  = US
ST = Local
L  = Lab
O  = MyService
CN = myservice.local

[ req_ext ]
subjectAltName = @alt_names

[ alt_names ]
DNS.1 = myservice.local
DNS.2 = localhost
IP.1  = 127.0.0.1
```

---

#### 2. Generate Server Key (Ed25519)

```bash
openssl genpkey -algorithm Ed25519 -out server.key
```

#### 3. Generate CSR with SAN

```bash
openssl req -new -key server.key -out server.csr -config openssl-san.cnf
```

#### 4. Sign with Root CA

```bash
openssl x509 -req -in server.csr -CA rootCA.crt -CAkey rootCA.key \
  -CAcreateserial -out server.crt -days 365 -sha256 -extfile openssl-san.cnf -extensions req_ext
```

Now `server.crt` contains SANs (`myservice.local`, `localhost`, `127.0.0.1`).

---

### Installing the Root CA in Browsers

#### On Linux

* Copy `rootCA.crt` to `/usr/local/share/ca-certificates/`
* Update trust:

  ```bash
  sudo update-ca-certificates
  ```

#### On macOS

* Open **Keychain Access** → Import `rootCA.crt` → Mark as **Always Trust**.

#### On Windows

* Run `mmc` → Certificates → Trusted Root Certification Authorities → Import `rootCA.crt`.

#### On Firefox

* Firefox has its own store:
  Preferences → Privacy & Security → Certificates → Import → select `rootCA.crt`.
