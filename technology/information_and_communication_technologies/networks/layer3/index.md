# Network Layer(OSI Layer 3)

The **Network Layer** is responsible for **logical addressing, routing, and forwarding of data** across interconnected networks. While the Data Link Layer (Layer 2) handles communication on the same local network (or link), the Network Layer ensures data can **travel across different networks** to reach its final destination.

---

## Key Responsibilities

### 1. **Logical Addressing**

* Assigns **IP addresses** to identify each device uniquely across networks.
* Unlike MAC addresses (which are physical), IP addresses are **logical** and can change.
* Supports both **IPv4 (e.g., 192.168.1.1)** and **IPv6 (e.g., 2001:0db8::1)**.

### 2. **Routing**

* Determines the **best path** for data to travel from source to destination across networks.
* Uses **routing tables** and **algorithms** like OSPF, BGP, and RIP.

### 3. **Packet Forwarding**

* Moves packets from one network to another, based on IP addresses.
* Involves **encapsulation** of Layer 4 segments into **Layer 3 packets**.

### 4. **Fragmentation and Reassembly**

* Breaks large packets into smaller ones if a network's MTU (Maximum Transmission Unit) is too small.
* Reassembles them at the destination.
* Important in **IPv4** (optional in IPv6, which relies on endpoints to do it).

### 5. **Error Handling and Diagnostics**

* Provides **ICMP (Internet Control Message Protocol)** for error messages (e.g., "host unreachable", "TTL expired").
* Used in tools like **ping** and **traceroute**.

---

## Network Layer Data Unit

* The basic data unit is called a **packet**.

---

## Key Protocols in Layer 3

| Protocol                                     | Function                                                                    |
| -------------------------------------------- | --------------------------------------------------------------------------- |
| **IP (Internet Protocol)**                   | Logical addressing and packet forwarding.                                   |
| **ICMP (Internet Control Message Protocol)** | Sends error and control messages.                                           |
| **ARP (Address Resolution Protocol)**        | Maps IP addresses to MAC addresses (technically between Layer 2 and 3).     |
| **RARP (Reverse ARP)**                       | Finds IP address from a known MAC address (obsolete).                       |
| **OSPF (Open Shortest Path First)**          | Dynamic link-state routing.                                                 |
| **BGP (Border Gateway Protocol)**            | Core routing protocol of the Internet.                                      |
| **RIP (Routing Information Protocol)**       | Distance-vector routing protocol.                                           |
| **IPSec**                                    | Provides security features at the IP layer (authentication and encryption). |

---

## Devices Operating at Layer 3

* **Routers** (primary devices at this layer)
* **Layer 3 Switches** (hybrid devices capable of both switching and routing)
* **Firewalls** (operate across layers, but inspect Layer 3 addresses for rules)

---

## Common Fields in an IP Packet (IPv4)

| Field              | Description                                  |
| ------------------ | -------------------------------------------- |
| Version            | IP version (IPv4 or IPv6)                    |
| Source IP          | Sender's IP address                          |
| Destination IP     | Receiver's IP address                        |
| TTL (Time to Live) | Prevents packets from circulating forever    |
| Protocol           | Indicates the upper-layer protocol (TCP/UDP) |
| Header Checksum    | Error-checking of the IP header              |

---

## Real-World Example

Let’s say you want to visit `www.example.com`:

1. Your device uses DNS to resolve the domain to an IP address.
2. Layer 3 creates an IP packet with:

   * **Your IP** as source.
   * **Server's IP** as destination.
3. The packet is routed across multiple networks using Layer 3 routers.
4. Each router looks only at the **destination IP address** and forwards the packet accordingly.

---

## Comparison with Neighboring Layers

| OSI Layer             | Description                                                 |
| --------------------- | ----------------------------------------------------------- |
| Layer 2 (Data Link)   | Local delivery of frames via MAC addresses.                 |
| **Layer 3 (Network)** | End-to-end delivery across networks using IP addresses.     |
| Layer 4 (Transport)   | Reliable delivery (TCP) or fast delivery (UDP) of segments. |

---

## IPv4 vs. IPv6 (Layer 3 evolution)

| Feature           | IPv4                        | IPv6                             |
| ----------------- | --------------------------- | -------------------------------- |
| Address size      | 32-bit                      | 128-bit                          |
| Address format    | Decimal (e.g., 192.168.1.1) | Hexadecimal (e.g., 2001:0db8::1) |
| Header complexity | Simpler                     | More extensible                  |
| NAT support       | Common                      | Generally not used               |
| Security          | Optional (IPSec)            | Built-in                         |

---

## Packet Structures

### IPv4

```text
  0                   1                   2                   3
  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 |Version|  IHL  |Type of Service|          Total Length         |
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 |         Identification        |Flags|     Fragment Offset     |
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 |  Time to Live |   Protocol    |       Header Checksum         |
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 |                       Source IP Address                       |
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 |                    Destination IP Address                     |
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 |                    (Options if IHL > 5)                       |
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 |                          Data (Payload)                       |
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```
Fields description:

| Field                      | Size     | Description                                                            |
| -------------------------- | -------- | ---------------------------------------------------------------------- |
| **Version**                | 4 bits   | IP version (should be `4` for IPv4).                                   |
| **IHL** (Header Length)    | 4 bits   | Number of 32-bit words in the header (minimum is 5 = 20 bytes).        |
| **Type of Service (ToS)**  | 8 bits   | Used for QoS (Quality of Service) to prioritize packets.               |
| **Total Length**           | 16 bits  | Entire packet size (header + data) in bytes.                           |
| **Identification**         | 16 bits  | Used for uniquely identifying fragments of an original IP packet.      |
| **Flags**                  | 3 bits   | Control flags for fragmentation (e.g., Don't Fragment bit).            |
| **Fragment Offset**        | 13 bits  | Position of a fragment in the original packet.                         |
| **Time to Live (TTL)**     | 8 bits   | Limits packet lifetime (decreases by 1 at each hop).                   |
| **Protocol**               | 8 bits   | Indicates the protocol in the payload (e.g., TCP=6, UDP=17, ICMP=1).   |
| **Header Checksum**        | 16 bits  | Verifies integrity of the IP header.                                   |
| **Source IP Address**      | 32 bits  | IP address of the sender.                                              |
| **Destination IP Address** | 32 bits  | IP address of the receiver.                                            |
| **Options (Optional)**     | Variable | Rarely used; allows additional features like timestamping.             |
| **Data (Payload)**         | Variable | The actual data passed from Layer 4 (e.g., TCP segment, UDP datagram). |

### IPv6

```text
  0                   1                   2                   3
  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 |Version| Traffic Class |           Flow Label                  |
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 |      Payload Length           |  Next Header  |   Hop Limit   |
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 |                                                               |
 +                         Source Address                        +
 |                                                               |
 +                                                               +
 |                                                               |
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 |                                                               |
 +                      Destination Address                      +
 |                                                               |
 +                                                               +
 |                                                               |
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

Field Descriptions:

| Field                   | Size     | Description                                                                      |
| ----------------------- | -------- | -------------------------------------------------------------------------------- |
| **Version**             | 4 bits   | IP version (`6` for IPv6).                                                       |
| **Traffic Class**       | 8 bits   | Like Type of Service (ToS) in IPv4; used for QoS.                                |
| **Flow Label**          | 20 bits  | Identifies packet flows requiring special handling (e.g., real-time traffic).    |
| **Payload Length**      | 16 bits  | Size of the payload (excluding header), in bytes.                                |
| **Next Header**         | 8 bits   | Identifies the type of the next header (e.g., TCP, UDP, or an extension header). |
| **Hop Limit**           | 8 bits   | Replaces IPv4’s TTL; decrements by 1 at each hop.                                |
| **Source Address**      | 128 bits | IPv6 address of sender.                                                          |
| **Destination Address** | 128 bits | IPv6 address of recipient.                                                       |

Notable Ommissions:

| Feature                           | IPv4        | IPv6                                        |
| --------------------------------- | ----------- | ------------------------------------------- |
| Header Checksum                   | Present   | Removed (upper layers like TCP handle it) |
| NAT (Network Address Translation) | Common    | Avoided (end-to-end addressing preferred) |
| Broadcast                         | Supported | Replaced with multicast and anycast       |

### IPv4 vs IPv6

| Feature           | **IPv4**                           | **IPv6**                            |
| ----------------- | ---------------------------------- | ----------------------------------- |
| Address size      | 32 bits                            | 128 bits                            |
| Header size       | Variable (20–60 bytes)             | Fixed (40 bytes)                    |
| Header complexity | More complex, many optional fields | Simplified, with extension headers  |
| Fragmentation     | Done by routers or hosts           | Done only by sending hosts          |
| Checksum          | Present                            | Removed (handled by upper layers)   |
| Options           | Built-in                           | Replaced with **extension headers** |
| Security support  | Optional (IPSec)                   | Mandatory support for IPSec         |

## Comprehensive list of Layer 3 protocols

```
Layer 3 Protocols (Network Layer)
├── 1. IP Protocols
│   ├── IPv4
│   ├── IPv6
│   └── CLNP (OSI)
│
├── 2. Routing Protocols
│   ├── OSPF
│   ├── RIP
│   ├── BGP
│   ├── EIGRP
│   ├── IS-IS
│   └── IGRP (deprecated)
│
├── 3. Messaging & Diagnostics
│   ├── ICMP
│   ├── ICMPv6
│   └── Traceroute/Ping (use ICMP)
│
├── 4. Address Resolution
│   ├── ARP
│   ├── RARP (obsolete)
│   ├── NDP (IPv6)
│   └── DHCP (Layer 3/4 hybrid)
│
├── 5. Multicast Management
│   ├── IGMP (IPv4)
│   └── MLD (IPv6)
│
├── 6. Tunneling & Security
│   ├── IPSec
│   ├── GRE
│   ├── MPLS (Layer 2.5)
│   ├── L2TP
│   ├── 6to4 / Teredo / ISATAP
│   └── DS-Lite
│
└── 7. Legacy & Vendor-Specific
    ├── IPX (Novell)
    ├── AppleTalk DDP
    ├── DECnet
    └── X.25
```
## Example: Operation of a Router

Absolutely! Let’s walk through a **real-world example** of how a **router** operates in a network, step-by-step. This will help you understand how it uses **Layer 3 protocols (like IP and routing protocols)** to forward data across networks.

---

### Scenario: Home Network Accessing a Website

#### Setup:

* You have a **laptop** at home.
* Your **home router** connects to the **Internet** via your **ISP**.
* You want to visit `https://example.com`, which is hosted on a server in another country.

---

### Step-by-Step: How the Router Works

#### 1. **Your Device Sends a Request**

* You open a browser and type `https://example.com`.
* Your laptop:

  * Resolves the **domain** using **DNS** (a Layer 7 application-layer service).
  * Gets the IP address of the website (e.g., `93.184.216.34`).
  * Forms a **TCP/IP packet** (Layer 4 and 3):

    * Source IP: `192.168.1.10` (your laptop)
    * Destination IP: `93.184.216.34`

---

#### 2. **IP Packet is Delivered to the Router**

* Your laptop checks its **routing table**:

  * Destination IP is not local → send to **default gateway** (your router, IP `192.168.1.1`).
* The laptop uses **ARP** to get the router's MAC address.
* It sends the packet to the router via Ethernet (Layer 2).

---

#### 3. **Router Processes the Packet (Layer 3)**

* Your **home router** receives the packet.
* It examines the **IP header**:

  * Sees destination IP is **external** (not in local 192.168.1.0/24 range).
* It performs **NAT (Network Address Translation)**:

  * Changes the source IP from `192.168.1.10` to your public IP, e.g., `203.0.113.42`.
  * Records the mapping in its **NAT table**.

---

#### 4. **Router Forwards the Packet to the ISP**

* The router consults its **routing table**.
* It forwards the packet to the **ISP's router** (next hop).

---

#### 5. **Routers on the Internet Forward the Packet**

* The packet travels through **multiple routers** on the Internet:

  * Each router examines the **destination IP**.
  * Uses routing protocols like **BGP** to decide the next hop.
* The **TTL** field in the IP header decreases by 1 at each hop to prevent loops.

---

#### 6. **Packet Reaches Destination Server**

* The server receives the packet, sees:

  * Destination IP = its own.
  * Source IP = your router’s public IP (`203.0.113.42`).
* It sends a **response** back to that IP.

---

#### 7. **Return Path**

* The response packet travels **back** across the Internet.
* Your **home router** receives it and:

  * Checks the **NAT table**.
  * Maps it back to your laptop’s private IP (`192.168.1.10`).
* Forwards the packet to your laptop.

---

### What the Router Does at Layer 3

| Task                            | Detail                                                         |
| ------------------------------- | -------------------------------------------------------------- |
| **Packet forwarding**           | Based on destination IP and routing table.                     |
| **NAT**                         | Translates private IP to public IP and vice versa.             |
| **TTL decrement**               | Prevents endless routing loops.                                |
| **Routing decisions**           | May use static routes or dynamic protocols (like OSPF, BGP).   |
| **Encapsulation/Decapsulation** | Strips and re-encapsulates data-link layer frames at each hop. |

---


## Packet Capture(as one may see on Wireshark)

### Scenario:

You visit `https://example.com` from a home laptop.

---

### **Step 1: DNS Resolution**

```
Frame 1: 74 bytes
Ethernet II
Internet Protocol Version 4
User Datagram Protocol (UDP)
Domain Name System (query)
    Source Port: 53627
    Destination Port: 53
    Query: example.com A
```

```
Frame 2: 90 bytes
Ethernet II
Internet Protocol Version 4
User Datagram Protocol (UDP)
Domain Name System (response)
    Answer: example.com A 93.184.216.34
```

**Note**: *Your laptop asks a DNS server for the IP of `example.com`.*

---

### **Step 2: TCP 3-Way Handshake to the Web Server**

```
Frame 3: 74 bytes
Ethernet II
IP: 192.168.1.10 → 93.184.216.34
TCP: 49876 → 443 [SYN]

Frame 4: 74 bytes
Ethernet II
IP: 93.184.216.34 → 203.0.113.42
TCP: 443 → 49876 [SYN, ACK]

Frame 5: 66 bytes
Ethernet II
IP: 192.168.1.10 → 93.184.216.34
TCP: 49876 → 443 [ACK]
```

**Note**: 
- *The TCP handshake establishes a secure connection to port 443 (HTTPS) of the web server.*
- *You might see `192.168.1.10` locally, but in the public Internet, the IP is your router’s NAT address (e.g. `203.0.113.42`).*

---

### **Step 3: HTTPS GET Request**

```
Frame 6: 600 bytes
Ethernet II
IP: 192.168.1.10 → 93.184.216.34
TCP: 49876 → 443
TLSv1.3: Client Hello

Frame 7: 1514 bytes
Ethernet II
IP: 93.184.216.34 → 192.168.1.10
TCP: 443 → 49876
TLSv1.3: Server Hello, Certificate, Server Finished
```

**Note**: *This is the start of the TLS handshake. It's encrypted because it's HTTPS.*

---

### How You’d See This in Wireshark

Filter examples:

* `dns` — to view only DNS queries
* `ip.addr == 93.184.216.34` — to isolate traffic to the web server
* `tcp.port == 443` — to see encrypted HTTPS traffic
* `tcp.flags.syn == 1` — to catch SYN packets in TCP handshakes

---

### Layer Involvement

| Layer                 | What It Does in the Capture                   |
| --------------------- | --------------------------------------------- |
| Layer 2 (Data Link)   | Ethernet headers (MAC addresses)              |
| Layer 3 (Network)     | IP addresses (routing logic)                  |
| Layer 4 (Transport)   | TCP/UDP ports (443 for HTTPS, 53 for DNS)     |
| Layer 7 (Application) | DNS, TLS handshake, and HTTP (if unencrypted) |

---

### Want to Try It Yourself?

You can capture this flow using **Wireshark**:

1. Install and launch Wireshark.
2. Start capturing on your active network interface.
3. Visit a website like `https://example.com`.
4. Use filters like `ip.addr == x.x.x.x` to isolate traffic.
5. Right-click a packet → “Follow TCP stream” for full context.
