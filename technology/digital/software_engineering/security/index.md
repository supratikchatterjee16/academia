# Security in Softwares

This article explains the security considerations in place for securing an application. The security uses the [OSI Model](/technology/digital/networks/osi_model.md).

Securing each layer of the **OSI Model** involves applying different strategies, technologies, and best practices tailored to the specific function of that layer. Here's a breakdown of how to secure each layer from **Layer 1 (Physical)** up to **Layer 7 (Application)**:

---

## Securing Each Layer of the OSI Model

---

### Layer 1: Physical Layer

**What it does**: Transmits raw bits over physical media

**Security Risks**:

* Cable tapping or signal interception
* Physical device theft or tampering

**Security Measures**:

* **Physical access controls**: locks, security guards, biometrics
* **CCTV surveillance**
* **Tamper-evident seals**
* **Fiber-optic cables** (harder to tap than copper)
* **Port security**: disable unused ports on network equipment

---

### Layer 2: Data Link Layer

**What it does**: Handles MAC addresses and point-to-point connections

**Security Risks**:

* MAC spoofing
* ARP poisoning (Man-in-the-Middle attacks)
* VLAN hopping

**Security Measures**:

* **MAC address filtering** and **port security** on switches
* **Dynamic ARP Inspection (DAI)** on switches
* **802.1X (port-based network access control)**
* **Private VLANs** to isolate traffic
* **Segmentation** to contain broadcast domains

---

### Layer 3: Network Layer

**What it does**: Responsible for routing and logical addressing (IP)

**Security Risks**:

* IP spoofing
* Routing attacks (e.g., BGP hijacking)
* DoS/DDoS attacks

**Security Measures**:

* **IPsec** (encryption & authentication of IP packets)
* **Firewalls** with layer 3 rules
* **Ingress/Egress filtering** (to prevent spoofed IPs)
* **Network segmentation** with routers
* **Rate limiting** and DDoS protection tools

---

### Layer 4: Transport Layer

**What it does**: Manages end-to-end communication, ports, and reliability

**Security Risks**:

* Port scanning
* TCP SYN floods
* Session hijacking

**Security Measures**:

* **Stateful firewalls**
* **Intrusion Prevention Systems (IPS)**
* **TLS/SSL** to secure sessions
* **Rate limiting & SYN cookies** (DoS mitigation)
* **Deep Packet Inspection (DPI)**

---

### Layer 5: Session Layer

**What it does**: Manages sessions between applications

**Security Risks**:

* Session hijacking or replay
* Session fixation

**Security Measures**:

* **Session tokens** with expiration and rotation
* **Use HTTPS** to protect session data in transit
* **Logout mechanisms** and **session timeout**
* **Binding sessions to IP/device fingerprint**

---

### Layer 6: Presentation Layer

**What it does**: Translates and encrypts data

**Security Risks**:

* Weak or improper encryption
* Malformed or malicious data input

**Security Measures**:

* **Strong encryption protocols** (TLS 1.2+, AES, etc.)
* **Input validation** and sanitization
* **Use standardized data formats** (e.g., JSON, XML) securely
* **Avoid custom or obsolete encoding schemes**

---

### Layer 7: Application Layer

**What it does**: Interfaces with user applications (e.g., browsers, APIs)

**Security Risks**:

* SQL injection, XSS, CSRF
* API abuse
* Malware or phishing attacks

**Security Measures**:

* **OAuth**
* **Web Application Firewalls (WAF)**
* **Content Security Policy (CSP)**, **XSS/CSRF protections**
* **Input validation** and **output encoding**
* **Security testing** (SAST/DAST)
* **Rate limiting, CAPTCHA, and API keys**
* **Secure coding practices** and patching

---

## Summary Table: Securing the OSI Model

| Layer           | Security Tools/Techniques                         |
| --------------- | ------------------------------------------------- |
| 1. Physical     | Physical access control, CCTV, locks              |
| 2. Data Link    | MAC filtering, 802.1X, ARP inspection             |
| 3. Network      | Firewalls, IPsec, ACLs, routing hardening         |
| 4. Transport    | TLS, firewalls, rate limiting                     |
| 5. Session      | Token management, timeouts, secure cookies        |
| 6. Presentation | Encryption, input validation                      |
| 7. Application  | OAuth, WAFs, secure coding, CSP, authentication   |

---

## Further

### Digital Rights Management(DRM)

**DRM (Digital Rights Management)** is not confined to a single layer of the OSI model, but its **core functions operate primarily at the Application and Presentation Layers (Layers 6–7)**.

---

## What is DRM?

**DRM** refers to **technologies used to control access, copying, distribution, and modification of digital content**—like movies, music, ebooks, and software.

---

## DRM's Place in the OSI Model

| **OSI Layer**              | **DRM Role**                                                                                    |
| -------------------------- | ----------------------------------------------------------------------------------------------- |
| **Layer 7 – Application**  | **Main layer** for DRM policy enforcement (licenses, user rights, device checks)                |
| **Layer 6 – Presentation** | **Content encryption/decryption** (e.g., decrypting a movie stream)                             |
| **Layer 5 – Session**      | May manage secure streaming sessions (e.g., renewing keys or re-authenticating during playback) |
| **Layer 4 – Transport**    | Used indirectly via secure transport (TLS for license exchange)                                 |
| **Layer 1–3**              | Transport and network support, but not directly involved in DRM logic                           |

---

## How DRM Actually Works (Layer-by-Layer View)

### **Layer 7 – Application Layer**

* Application interprets DRM licenses and applies rules:

  * Is the user allowed to view/download?
  * Has the license expired?
  * Is the device authorized?
* Examples:

  * Adobe DRM in ebooks
  * Apple FairPlay
  * Microsoft PlayReady

### **Layer 6 – Presentation Layer**

* DRM uses **encryption** to protect media content
* Presentation layer is responsible for **decrypting** the content *only if license conditions are met*
* E.g., AES-encrypted video decrypted only after license validation

### **Layer 5 – Session Layer**

* Optional: Maintains **session state** (e.g., DRM license renewal or heartbeat for continuous access)
* Streaming DRM (like Widevine or PlayReady) might require re-authentication or token refresh mid-session

### **Lower Layers (4 and below)**

* DRM systems **rely on** secure transport:

  * **HTTPS/TLS (Layer 6)**
  * **TCP (Layer 4)**
* However, **they don't enforce content control** at these levels

---

## Real-World DRM Examples and OSI Context

| DRM System              | OSI Layers Involved              | Notes                         |
| ----------------------- | -------------------------------- | ----------------------------- |
| **Apple FairPlay**      | Layer 7 (rules), 6 (decryption)  | Used in Apple TV, iTunes      |
| **Google Widevine**     | Layer 7 (browser-based), 6 (AES) | Used in Chrome, Netflix, etc. |
| **Microsoft PlayReady** | Layer 7 and 6                    | Used in Xbox, Windows Media   |
| **Adobe DRM**           | Layer 7                          | Ebooks and PDF readers        |

---

## Summary

| **OSI Layer**    | **DRM Role**                                            |
| ---------------- | ------------------------------------------------------- |
| 7 – Application  | Interprets licenses, enforces rules                     |
| 6 – Presentation | Encrypts/decrypts media content                         |
| 5 – Session      | Manages content access sessions (in streaming DRM)      |
| 4 and below      | Provides secure transmission (HTTPS/TLS), not DRM logic |

---
