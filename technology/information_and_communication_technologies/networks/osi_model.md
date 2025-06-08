# OSI Model

The **OSI Model (Open Systems Interconnection Model)** is a conceptual framework used to understand and standardize how different networking protocols interact in a network communication system. It divides network communication into **seven distinct layers**, each with specific responsibilities.

---

## OSI Model: The 7 Layers

| Layer | Name         | Function                                  |
| ----- | ------------ | ----------------------------------------- |
| 7     | Application  | End-user interface & app services         |
| 6     | Presentation | Data translation, encryption, compression |
| 5     | Session      | Session control and synchronization       |
| 4     | Transport    | Reliable data transfer, segmentation      |
| 3     | Network      | Routing and logical addressing            |
| 2     | Data Link    | Physical addressing and error detection   |
| 1     | Physical     | Transmission of raw bits over media       |

---

## Detailed Breakdown of Each Layer

---

### Layer 7: Application Layer

* **Closest to the user**.
* Provides network services directly to applications (e.g., web browsers, email clients).
* **Functions**:

  * Resource sharing
  * Remote file access
  * Network management
* **Examples**:

  * HTTP, FTP, SMTP, DNS, POP3, IMAP, SNMP

---

### Layer 6: Presentation Layer

* Translates data between application and network format.
* Handles **data encoding, encryption, compression**.
* Ensures that data is in a readable format for the Application Layer.
* **Functions**:

  * Character encoding (e.g., ASCII to EBCDIC)
  * Data encryption/decryption (e.g., TLS, SSL)
  * Data compression (e.g., JPEG, MPEG)

---

### Layer 5: Session Layer

* Manages **sessions or connections** between applications.
* Responsible for:

  * Establishing, maintaining, and terminating sessions
  * Authentication and authorization
  * Synchronization checkpoints
* **Examples**:

  * NetBIOS
  * RPC (Remote Procedure Call)

---

### Layer 4: Transport Layer

* Responsible for **reliable delivery** of data.
* **Functions**:

  * Segmentation and reassembly
  * Flow control
  * Error detection and correction
* **Protocols**:

  * TCP (reliable, connection-oriented)
  * UDP (unreliable, connectionless)

---

### Layer 3: Network Layer

* Deals with **routing and logical addressing**.
* Determines **best path** for data delivery.
* **Functions**:

  * IP addressing
  * Packet forwarding and routing
* **Protocols**:

  * IP (IPv4/IPv6)
  * ICMP, ARP, RIP, OSPF, BGP

---

### Layer 2: Data Link Layer

* Provides **node-to-node** communication.
* Responsible for **framing, MAC addressing, and error detection**.
* **Sub-layers**:

  * **LLC (Logical Link Control)** – Error checking, frame synchronization
  * **MAC (Media Access Control)** – Controls how devices access the media
* **Examples**:

  * Ethernet (IEEE 802.3), Wi-Fi (IEEE 802.11)
  * Switches operate here

---

### Layer 1: Physical Layer

* Concerned with the **actual transmission of bits** over physical media.
* **Functions**:

  * Defines hardware specifications (cables, connectors)
  * Modulation and signal encoding
  * Bit rate control
* **Examples**:

  * Cables (Ethernet, fiber)
  * Radio frequencies
  * Hubs, repeaters

---

## Easy Mnemonic to Remember the Layers (Top to Bottom)

> **All People Seem To Need Data Processing**

* A – Application
* P – Presentation
* S – Session
* T – Transport
* N – Network
* D – Data Link
* P – Physical

---

## Encapsulation in the OSI Model

Each layer adds its own **header (and sometimes trailer)** to the data:

| Layer     | Data Unit Name                 |
| --------- | ------------------------------ |
| Layer 7-5 | Data                           |
| Layer 4   | Segment (TCP) / Datagram (UDP) |
| Layer 3   | Packet                         |
| Layer 2   | Frame                          |
| Layer 1   | Bits                           |

Data goes **down the stack** (encapsulation), gets transmitted, then **up the stack** (decapsulation) at the receiver.

---

## Real-World Device Mapping (Simplified)

| Layer | Devices Typically Operating Here |
| ----- | -------------------------------- |
| 7–5   | Computers, Smartphones (apps)    |
| 4     | Firewalls, Load Balancers        |
| 3     | Routers                          |
| 2     | Switches, Bridges                |
| 1     | Hubs, Repeaters, Cables          |

---
