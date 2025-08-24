# Transport Layer Security(TLS)

The TLS handshake has **two main jobs**:

1. **Authenticate** the server (and optionally client) with a certificate.
2. **Agree** on a shared session key for encryption.

That means it uses **two classes of algorithms**:

---

### 1. **Key Exchange / Key Agreement Algorithms**

These establish the **shared secret (session key)**.

* **RSA key exchange** (legacy, insecure now)

  * Client encrypts a secret with server’s RSA public key.
  * Weak against modern attacks → deprecated.

* **Diffie–Hellman (DH)**

  * Mathematical exchange of values to derive a shared key.
  * Requires large parameters; not common today.

* **Elliptic Curve Diffie–Hellman (ECDH)**

  * Same as DH, but on elliptic curves → smaller, faster, more secure.

* **Ephemeral DH / ECDH (DHE / ECDHE)**

  * “Ephemeral” = new key for every handshake.
  * Provides **forward secrecy** (past sessions safe if long-term key is stolen).
  * Today’s most common: **ECDHE**.

* **Post-Quantum (Hybrid) Key Exchange**

  * **X25519 + ML-KEM-768** (Kyber) → hybrid PQC + classical.
  * Already deployed in Chrome, Firefox, Cloudflare, etc.

---

### 2. **Authentication / Digital Signature Algorithms**

These verify the **server’s identity** (and optionally client’s).

* **RSA**

  * Most widely used in certificates.
  * Large keys, but universally supported.

* **DSA**

  * Rare today; replaced by stronger options.

* **ECDSA**

  * Preferred modern option: smaller keys, faster operations.

* **EdDSA (Ed25519/Ed448)**

  * Newer, very fast and secure.
  * Limited CA/browser adoption so far.

* **Post-Quantum Signatures (Dilithium, Falcon, SPHINCS+)**

  * Standardized by NIST.
  * Not yet supported in web PKI / browsers.

---

### 3. **Bulk Encryption Algorithms**

Once the handshake is done, the shared key secures the data stream.

* **AES-GCM** (most common today)
* **ChaCha20-Poly1305** (popular on mobile, fast without AES hardware)
* Legacy: 3DES, RC4 (deprecated, insecure).

---

### 4. **Message Authentication / Integrity**

Ensures data isn’t tampered with.

* **HMAC-SHA256 / SHA384** (common in TLS 1.2).
* **AEAD (Authenticated Encryption with Associated Data)** — in TLS 1.3 (integrity built into AES-GCM / ChaCha20-Poly1305).

---

⚡ In short:

* **Handshake = Key Exchange (ECDHE/Hybrid) + Authentication (RSA/ECDSA/EdDSA)**
* **Data Protection = AES-GCM or ChaCha20-Poly1305 with HMAC/AEAD**

---

## TLS Algorithms Across Versions

### **TLS 1.0 (1999) & TLS 1.1 (2006)**

* **Key Exchange**:

  * RSA (server sends RSA cert, client encrypts a secret with it).
  * Diffie-Hellman (DH), DHE, and ECDH/ECDHE (early support).
* **Authentication**:

  * RSA (most common in certs).
  * DSA, ECDSA (less common).
* **Encryption**:

  * Block ciphers: 3DES, AES (CBC mode).
  * Stream ciphers: RC4.
* **Integrity**:

  * HMAC with MD5 or SHA-1.
* **Issues**:

  * Vulnerable to BEAST, POODLE, RC4 biases, etc.
  * Now **deprecated**.

---

### **TLS 1.2 (2008)**

* **Key Exchange**:

  * RSA (still allowed).
  * DHE/ECDHE → widely used (enables Forward Secrecy).
* **Authentication**:

  * RSA certificates dominant.
  * ECDSA certificates widely adopted (smaller, faster).
* **Encryption**:

  * AES (CBC, then GCM later).
  * ChaCha20-Poly1305 introduced later.
* **Integrity**:

  * HMAC with SHA-256/SHA-384 (stronger than MD5/SHA-1).
  * AEAD (AES-GCM, ChaCha20-Poly1305) became preferred.
* **Strengths**:

  * Very flexible (too flexible — led to downgrade attacks).
* **Weaknesses**:

  * Complexity (too many cipher suites).
  * Vulnerable to protocol-level attacks (Lucky13, POODLE on CBC).

---

### **TLS 1.3 (2018)**

* **Key Exchange**:

  * Only ephemeral → **ECDHE** (X25519, P-256, etc.).
  * PQC hybrid → **X25519 + ML-KEM-768** (Kyber), being deployed.
* **Authentication**:

  * RSA, ECDSA certificates supported.
  * EdDSA (Ed25519/Ed448) emerging.
  * Post-Quantum (Dilithium, Falcon, SPHINCS+) not in browsers yet.
* **Encryption (only AEAD)**:

  * AES-GCM (128/256).
  * ChaCha20-Poly1305.
* **Integrity**:

  * Built into AEAD — no separate HMAC negotiation.
* **Other changes**:

  * No static RSA/DH → all handshakes are forward-secret.
  * No weak algorithms (MD5, SHA-1, 3DES, RC4).
  * Faster handshake (1-RTT, with 0-RTT option).
* **Strengths**:

  * Clean, simple, strong defaults.
  * Future-proof (PQC hybrids already included).

---

### 📊 Major Differences by Version

| **Aspect**          | **TLS 1.0/1.1**        | **TLS 1.2**                                  | **TLS 1.3**                                              |
| ------------------- | ---------------------- | -------------------------------------------- | -------------------------------------------------------- |
| **Key Exchange**    | RSA, DH, DHE, ECDH     | RSA, DHE, ECDHE                              | Only ECDHE (X25519, P-256, etc.)<br>PQC hybrids (ML-KEM) |
| **Auth (Certs)**    | RSA, DSA, ECDSA        | RSA, ECDSA                                   | RSA, ECDSA, EdDSA (future: Dilithium/Falcon)             |
| **Encryption**      | 3DES, AES-CBC, RC4     | AES (CBC, GCM), ChaCha20-Poly1305            | Only AEAD: AES-GCM, ChaCha20-Poly1305                    |
| **Integrity**       | HMAC-MD5, HMAC-SHA1    | HMAC-SHA256/384, AEAD (AES-GCM, ChaCha)      | AEAD only (built-in integrity)                           |
| **Forward Secrecy** | Optional (rarely used) | Optional (DHE/ECDHE)                         | Mandatory (ECDHE only)                                   |
| **Security**        | Weak, many attacks     | Stronger, but complex & attack-prone configs | Strong defaults, simplified, PQC-ready                   |


## Cryptographic Algorithms

| **Algorithm**                                            | **Type**                           | **Security Strength**        | **Performance**                 | **Key/Signature Size (Typical)**                 | **Pros**                                       | **Cons**                             | **Status / Usage**                      |
| -------------------------------------------------------- | ---------------------------------- | ---------------------------- | ------------------------------- | ------------------------------------------------ | ---------------------------------------------- | ------------------------------------ | --------------------------------------- |
| **RSA(Rivest-Shamir-Adleman)**                           | Asymmetric (Integer factorization) | Strong if ≥2048 bits         | Moderate                        | 2048–4096 bits                                   | Mature, widely supported                       | Large keys, slower than ECC          | Most common in TLS today                |
| **DSA(Digital Singature Algorithm)**                     | Asymmetric                         | Secure at ≥2048 bits         | Fast signing, slow verification | 1024–3072 bits                                   | Efficient signing                              | Deprecated, poor support             | Rare in TLS                             |
| **ECDSA(Elliptic Curve DSA)**                            | Elliptic Curve                     | 256-bit ≈ 3072-bit RSA       | Very fast                       | 256–521 bits                                     | Strong with small keys, efficient              | Not supported in some legacy systems | Common in modern TLS                    |
| **EdDSA(Edwards-curve DSA)** (Ed25519/Ed448)             | Elliptic Curve (Edwards)           | Strong at 256 bits           | Extremely fast                  | 256–448 bits                                     | High speed, small size, side-channel resistant | Limited CA support today             | Growing in SSH/TLS                      |
| **CRYSTALS-Dilithium**(aka ML-DSA)                       | Lattice-based (Module-LWE/LWR)     | Quantum-safe, NIST Level 1–5 | Fast signing, larger signatures | PubKey: \~1–2 KB<br>Sig: \~2–4 KB                | Standardized by NIST (2022), efficient         | Larger sizes than ECC/RSA            | PQC standard for signatures             |
| **Falcon**                                               | Lattice-based (NTRU lattice)       | Quantum-safe, NIST Level 1–5 | Compact, efficient              | PubKey: \~0.9–1.3 KB<br>Sig: \~0.7–1.3 KB        | Smaller signatures than Dilithium, efficient   | Complex math, harder to implement    | Standardized alongside Dilithium        |
| **SPHINCS+**                                             | Hash-based                         | Quantum-safe                 | Slower than lattice schemes     | PubKey: \~32–64 B<br>Sig: \~8–30 KB              | Very conservative (hash-based, no lattices)    | Very large signatures, slow          | Standardized as fallback                |
| **Kyber** (aka ML-KEM, for Key Exchange, not signatures) | Lattice-based (Module-LWE)         | Quantum-safe, NIST Level 1–5 | Fast, efficient                 | PubKey: \~800–1.5 KB<br>Ciphertext: \~700–1.5 KB | Compact, efficient, standardized for KEM       | Only for key exchange, not certs     | Will replace RSA/ECDH in TLS handshakes |
