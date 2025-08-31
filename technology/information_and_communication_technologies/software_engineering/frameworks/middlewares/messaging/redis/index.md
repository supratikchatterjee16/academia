# Redis

Perfect — Redis is one of those tools that looks simple at first (a “fast in-memory key-value store”) but has **many core concepts**. Let’s go through them in detail, and then cover **security best practices** for a Redis node.

---

# **Core Concepts of Redis**

### 1. **In-Memory Data Store**

* Redis = **REmote DIctionary Server**.
* Stores all data in RAM (extremely fast), with optional persistence to disk.
* Used as: cache, database, or message broker.

---

### 2. **Data Structures**

Unlike simple key-value stores, Redis supports rich data types:

* **Strings** → simplest form, can store text, numbers, or binary.
* **Lists** → ordered sequence of values (push/pop operations).
* **Sets** → unordered collection of unique values.
* **Sorted Sets (Zsets)** → sets ordered by a score (leaderboards, rankings).
* **Hashes** → maps/dictionaries (good for objects).
* **Streams** → append-only log for event streaming.
* **HyperLogLog** → probabilistic data structure for counting unique items.
* **Bitmaps & Bitfields** → compact data manipulation at the bit level.

---

### 3. **Persistence**

Redis is in-memory but offers persistence:

* **RDB snapshots** → periodic dumps of the dataset to disk.
* **AOF (Append Only File)** → logs every write operation for durability.
* **Hybrid mode** → use both RDB + AOF.

---

### 4. **Replication**

* **Primary-Replica** architecture.
* Data from a primary (master) is replicated to replicas (slaves).
* Used for scaling reads and redundancy.

---

### 5. **High Availability (Redis Sentinel)**

* **Redis Sentinel** monitors primary and replica nodes.
* Provides **automatic failover** if the primary goes down.
* Sentinel also handles discovery (apps don’t need to know which is the current primary).

---

### 6. **Sharding / Clustering**

* **Redis Cluster** distributes data across multiple nodes (horizontal scaling).
* Supports partitioning (sharding) by hash slots.
* Ensures automatic rebalancing and partial fault tolerance.

---

### 7. **Pub/Sub (Messaging)**

* Redis supports **publish/subscribe messaging**.
* Producers publish messages to channels, subscribers receive them in real time.
* Useful for lightweight messaging, but not durable (no message persistence unless using Streams).

---

### 8. **Transactions & Lua Scripting**

* Supports **multi-command transactions** (with `MULTI` / `EXEC`).
* Atomic execution of commands.
* **Lua scripting** allows complex logic to run inside Redis.

---

### 9. **Performance Features**

* **Pipeline** → batch multiple commands in one network roundtrip.
* **Eviction policies** (LRU, LFU, TTL) → for cache use cases.
* **Key expiration** → set TTLs for automatic deletion.

---

# **Securing a Redis Node**

By default, Redis is **not secure out of the box** (it trusts localhost connections). In production, you must harden it:

---

### 1. **Network Security**

* **Bind to localhost** (default):

  ```ini
  bind 127.0.0.1
  ```
* Or, restrict to a private network (VPC, internal subnet).
* **Firewall rules (iptables / security groups):**

  * Only allow trusted IPs to connect on port `6379`.
  * Block public internet access.

---

### 2. **Authentication**

* Redis has **password-based authentication**. In `redis.conf`:

  ```ini
  requirepass strong_password_here
  ```
* Or in Redis 6+, use **ACLs (Access Control Lists):**

  ```ini
  user app1 on >strongpassword ~* +@all
  user readonly on >readonlypass ~* +@read
  ```
* This allows different users with different permissions.

---

### 3. **TLS/SSL Encryption**

* Redis 6+ supports TLS natively.
* In `redis.conf`:

  ```ini
  tls-port 6379
  port 0
  tls-cert-file /etc/ssl/redis.crt
  tls-key-file /etc/ssl/redis.key
  tls-ca-cert-file /etc/ssl/ca.crt
  ```
* Ensures traffic is encrypted in transit.

---

### 4. **Disable Dangerous Commands**

* Some commands (like `FLUSHALL`, `CONFIG`, `SHUTDOWN`) can be abused.
* Disable them in `redis.conf`:

  ```ini
  rename-command FLUSHALL ""
  rename-command FLUSHDB ""
  rename-command CONFIG ""
  ```
* This prevents accidental or malicious misuse.

---

### 5. **System Hardening**

* Run Redis as a **non-root user**.
* Use **chroot jail** or Docker/Kubernetes isolation.
* Keep Redis updated (security patches).

---

### 6. **Monitoring & Logging**

* Monitor with **Prometheus + Grafana**, or **RedisInsight**.
* Enable logging in `redis.conf`:

  ```ini
  logfile /var/log/redis/redis-server.log
  ```

---

## Sample secure Redis Configuration

```ini
########################################
# NETWORK SECURITY
########################################

# Only listen on localhost or private network interface
bind 127.0.0.1 ::1

# Disable non-TLS port (force encrypted connections)
port 0

# Enable TLS port
tls-port 6379
tls-cert-file /etc/ssl/redis/redis.crt
tls-key-file /etc/ssl/redis/redis.key
tls-ca-cert-file /etc/ssl/redis/ca.crt

########################################
# SECURITY & AUTHENTICATION
########################################

# Require a strong password for clients
requirepass STRONG_PASSWORD_HERE

# Redis 6+ ACLs (example: full user + readonly user)
# user admin on >ADMIN_PASSWORD ~* +@all
# user readonly on >READONLY_PASSWORD ~* +@read

########################################
# PROTECTION AGAINST DANGEROUS COMMANDS
########################################

# Disable risky commands
rename-command FLUSHALL ""
rename-command FLUSHDB ""
rename-command CONFIG ""
rename-command SHUTDOWN ""
rename-command DEBUG ""

########################################
# GENERAL SETTINGS
########################################

# Run as a non-root user
supervised systemd

# Log file
logfile /var/log/redis/redis-server.log
loglevel notice

# Database files (persistence)
dir /var/lib/redis/

########################################
# PERSISTENCE
########################################

# Snapshotting (RDB persistence)
save 900 1    # Save if at least 1 key changes in 900 seconds
save 300 10   # Save if at least 10 keys change in 300 seconds
save 60 10000 # Save if at least 10,000 keys change in 60 seconds

# Append Only File (AOF) for durability
appendonly yes
appendfsync everysec

########################################
# PERFORMANCE & SECURITY
########################################

# Limit clients per IP (basic DoS protection)
maxclients 10000

# Max memory usage (example: 2GB)
maxmemory 2gb
maxmemory-policy allkeys-lru

# TCP keepalive
tcp-keepalive 300

```