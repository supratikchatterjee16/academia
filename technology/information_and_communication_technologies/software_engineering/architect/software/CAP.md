# CAP Theorem

CAP refers to:

* **C — Consistency**
* **A — Availability**
* **P — Partition tolerance**

The theorem, in its strongest and most useful formulation, says:

> **In an asynchronous distributed system, if a network partition occurs, you cannot simultaneously guarantee both strong consistency and availability.**

The important word is **partition**.

Imagine two replicas:

```text
        Network
       /       \
      A         B
     DB        DB
      \         /
       Clients
```

Normally A and B communicate.

Now the network breaks:

```text
       X  ← network partition →  X

      A                         B
    Replica                    Replica
      ↑                           ↑
 Client 1                     Client 2
```

Both sides are still running. Clients can still reach their local replica. But **A cannot communicate with B**.

Suppose initially:

```text
x = 10
```

Client 1 writes:

```text
x = 20
```

to A.

At approximately the same time, Client 2 asks B:

```text
"What is x?"
```

B cannot determine whether A has received the write, because the network is partitioned.

Now you have a fundamental choice.

### Option 1: Preserve consistency

B refuses to answer until it can communicate with A.

```text
Client 1 → A: WRITE x=20     ✓

Client 2 → B: READ x
             ↓
           WAIT/ERROR
```

You preserve **consistency**, but lose **availability**.

That's a **CP** choice.

### Option 2: Preserve availability

B answers immediately:

```text
Client 1 → A: WRITE x=20     ✓

Client 2 → B: READ x
             ↓
            10
```

Both sides remain available, but clients can observe conflicting/stale states.

That's an **AP** choice.

And that's the heart of CAP.

---

# 2. What exactly does "Consistency" mean?

This is one of the biggest sources of confusion.

CAP's C does **not** mean:

> "Every replica eventually contains the same data."

That's **eventual consistency**, and it is different.

CAP consistency is generally **linearizability** (often called "strong consistency" in CAP discussions).

Informally:

> Every operation should appear to take effect atomically at some point between its invocation and completion, and operations should respect real-time ordering.

For example:

```text
Client 1:
    WRITE x = 20
    returns success

Client 2:
    READ x
```

If the read occurs after the successful write, a linearizable system cannot return 10.

An eventually consistent system potentially can:

```text
A: x = 20
B: x = 10

        ↓ replication

A: x = 20
B: x = 20
```

The replicas converge eventually, but during the interval they disagree.

So:

**CAP consistency ≠ eventual convergence.**

---

# 3. What exactly does "Availability" mean?

CAP availability is also stronger than merely:

> "The server is usually up."

It means, roughly:

> Every request received by a non-failing node eventually receives a response.

And importantly, the response cannot simply be:

```text
"Sorry, I can't answer because my replica
can't communicate with the other replica."
```

If you make that choice during a partition, you sacrificed CAP availability.

This is why the CAP tradeoff becomes unavoidable.

---

# 4. What is Partition Tolerance?

A partition means:

> Messages between some parts of the distributed system can be lost or delayed indefinitely.

For example:

```text
        DC1                    DC2

       Node A                 Node B
          |                     |
          |                     |
          +------ network ------+
                    X
```

The nodes themselves haven't necessarily crashed.

The communication path has failed.

And this distinction matters enormously.

CAP assumes the possibility of **arbitrary communication failures/delays**.

---

# 5. The basic proof

The proof can be surprisingly simple.

Consider two nodes:

```text
             Network
        A -------------- B
```

Initially:

```text
x = 0
```

Now the network partitions:

```text
        A        X        B
```

Client `C1` can communicate with A.

Client `C2` can communicate with B.

Now C1 performs:

```text
WRITE(x = 1)
```

Suppose the system guarantees **availability**.

A must eventually return:

```text
OK
```

But A cannot communicate with B.

Now C2 performs:

```text
READ(x)
```

Suppose the system also guarantees **availability**.

B must eventually return some answer.

There are two possibilities.

### B returns 0

```text
C1 → A: WRITE x=1 → OK

C2 → B: READ x → 0
```

The read happened after the successful write, yet returned the old value.

Therefore, **linearizability is violated**.

### B returns 1

But B has no communication with A.

If arbitrary message loss/delay is allowed, B cannot distinguish:

```text
Case 1:
A received WRITE x=1

Case 2:
A did not receive WRITE x=1
```

Therefore the algorithm cannot safely manufacture knowledge that the write happened.

The formal impossibility proof makes this argument more precise using **indistinguishable executions**: from B's perspective, two executions can have exactly the same messages/events at B even though one contains a write at A and the other doesn't. Therefore B must behave the same way in both executions, which contradicts the required consistency behavior.

Hence:

> During a partition, you cannot have both linearizability and availability.

That's CAP.

---

# 6. What assumptions does the theorem make?

This is probably the most important part if you want to understand CAP academically rather than as a database slogan.

A typical CAP model assumes:

### 1. Multiple independent nodes

You have a distributed system rather than a single machine.

### 2. Asynchronous communication

There is **no known finite upper bound** on message delivery time.

A message may be:

```text
delivered in 1 ms
```

or:

```text
delivered in 10 seconds
```

or:

```text
never delivered
```

From the algorithm's perspective, a very slow message and a lost message may be indistinguishable.

### 3. Network partitions can occur

Communication between subsets of nodes can fail indefinitely.

### 4. Nodes continue operating

The nodes may remain alive while unable to communicate.

### 5. Clients can reach different nodes

For example:

```text
Client A → Node 1

Client B → Node 2
```

### 6. Consistency means a strong consistency property

Typically **linearizability**.

### 7. Availability means operations complete

The system cannot simply stop responding to requests during a partition.

Under these assumptions:

```text
Partition
    +
Consistency
    +
Availability
```

cannot all be guaranteed.

---

# 7. So why do people say "pick two of three"?

This is the famous but somewhat misleading diagram:

```text
          C
         / \
        /   \
       /     \
      CA-----AP
       \     /
        \   /
         \ /
          P
```

People often interpret CAP as:

> Choose any two.

That's not quite right.

**Partition tolerance isn't really an optional feature for most distributed systems.**

If your system spans:

* machines,
* racks,
* availability zones,
* data centers,
* regions,

then network partitions are a fact of life.

So the practical question is usually:

> **When a partition happens, do I sacrifice consistency or availability?**

Therefore:

```text
              Partition
                 |
         +-------+-------+
         |               |
         ↓               ↓
       CP              AP
 consistency        availability
   wins              wins
```

---

# 8. What is CP?

A **CP system** sacrifices availability during partitions to preserve consistency.

Imagine a replicated key:

```text
A = leader
B = follower
C = follower
```

A write might require enough replicas to acknowledge it.

During a partition:

```text
       A       |       B
               |
      majority | minority
```

The minority side may refuse writes.

That's deliberate.

It says:

> "I'd rather reject your operation than risk giving you an incorrect answer."

Typical applications:

* financial transactions
* distributed locks
* metadata
* leader election
* configuration
* inventory where overselling is unacceptable
* systems requiring a single authoritative state

Examples of systems/protocols commonly discussed in CP terms include **etcd**, **ZooKeeper**, and many consensus-based replicated databases.

---

# 9. What is AP?

An **AP system** continues operating on both sides of a partition.

For example:

```text
       A       |       B
               |
 WRITE x=20    | READ x
     ↓         |   ↓
    OK         |  10
```

The system accepts that replicas may temporarily disagree.

Later:

```text
       partition heals
             ↓

A: x=20  → replication → B: x=20
```

This is appropriate when availability is more important than immediately agreeing on one value.

Examples include workloads such as:

* social-media feeds
* likes/reactions
* shopping carts (depending on design)
* telemetry
* some recommendation systems
* geographically distributed user-generated content

But AP doesn't mean:

> "No consistency."

AP systems often have sophisticated consistency mechanisms:

* eventual consistency
* causal consistency
* conflict-free replicated data types (CRDTs)
* version vectors
* application-level conflict resolution

They simply don't promise CAP's strong consistency during a partition.

---

# 10. What about CA?

This is another place where the terminology causes trouble.

A system can be called **CA** if it provides consistency and availability **assuming partitions don't occur**.

For example:

```text
       DB cluster

       A ←→ B
```

If communication is reliable, you can potentially have both:

```text
C + A
```

But if your distributed model allows:

```text
A    X    B
```

then CAP tells you that you cannot guarantee both C and A during that partition.

So **CA is not generally a meaningful choice for a genuinely partition-prone distributed system**.

A single-node database is sometimes informally called CA because there is no distributed network between replicas to partition.

This is why I would avoid saying:

> "My distributed database is CA."

Instead say:

> "It provides consistency and availability when there is no partition; during partitions, its behavior depends on the replication protocol."

That's much more precise.

---

# 11. How do you actually choose CP vs AP?

Don't start with:

> "Should I use CP or AP?"

Start with:

> **What must never happen?**

That's the engineering question.

### Choose CP when incorrect/stale state is unacceptable

Ask:

> "Can two clients temporarily observe contradictory facts?"

If **no**, CP is likely appropriate.

Examples:

```text
Bank balance
Account ownership
Distributed lock
Leader election
Unique username
Inventory with hard stock limits
```

Suppose there is exactly one remaining ticket:

```text
tickets_remaining = 1
```

Two geographically separated nodes both receive:

```text
BUY ticket
```

An AP design could accept both:

```text
Node A → SOLD
Node B → SOLD
```

Now you've sold two tickets.

If that's unacceptable, you probably need a consistency-first design.

---

### Choose AP when rejecting requests is worse than temporary disagreement

Consider a social network:

```text
User posts photo
```

Would you rather:

**A**

> "Sorry, your post cannot be created because the Singapore and Virginia data centers can't communicate."

or:

**B**

> "Your post is visible now and will synchronize shortly."

Usually B.

Temporary inconsistency is acceptable.

So availability wins.

---

# 12. A useful decision table

| Requirement                                   | Likely choice       |
| --------------------------------------------- | ------------------- |
| Financial ledger                              | **CP**              |
| Distributed locks                             | **CP**              |
| Leader election                               | **CP**              |
| Configuration management                      | **CP**              |
| Unique global IDs requiring strict uniqueness | **CP**              |
| Inventory with strict no-oversell guarantee   | **CP**              |
| Social-media likes                            | **AP**              |
| Analytics/telemetry ingestion                 | **AP**              |
| User activity feeds                           | **AP**              |
| Some caching systems                          | **AP**              |
| Content replication                           | **AP**              |
| Single-machine database                       | Often called **CA** |

But there's a major caveat:

**The actual architecture can mix these choices.**

A real application isn't necessarily "a CP application" or "an AP application."

---

# 13. You can even choose differently per operation

Imagine an e-commerce system.

You might want:

```text
Product description       → AP
Product reviews           → AP
Recommendations           → AP
Shopping cart             → AP-ish
Inventory reservation     → CP
Payment                   → CP
Order state               → CP
```

So the CAP decision often belongs at the **data/operation level**, not the entire application level.

---

# 14. CAP doesn't mean "latency vs consistency"

Another common misunderstanding is:

> CAP says you trade consistency against latency.

Not exactly.

CAP specifically concerns behavior **under network partition**.

There are other tradeoffs involving latency, consistency, and availability, but those aren't CAP itself.

A more useful mental model is:

```text
Normal operation:

       C + A
        ↓
   Everything works


Partition:

        P
       / \
      /   \
     C     A
     |     |
   reject  possibly
   requests stale data
```

The theorem becomes relevant specifically when communication cannot be relied upon.

---

# 15. CAP versus PACELC

If you're learning distributed systems seriously, CAP is only the beginning.

A more realistic framework is **PACELC**:

> **If there is a Partition (P), choose Availability or Consistency; Else (E), choose Latency or Consistency.**

So:

```text
             Partition?
              /     \
            YES       NO
            /          \
       A vs C        L vs C
```

CAP describes the failure case.

PACELC asks what tradeoff you make **even during normal operation**.

For example, requiring synchronous replication across regions may give you stronger consistency but increase latency.

That tradeoff exists even when there is no partition.

---

# 16. The deeper idea behind the proof

The most important conceptual insight isn't actually the C/A terminology.

It's this:

> **A distributed system cannot distinguish "the other node is dead" from "the other node is alive but the network is extremely slow."**

Suppose B hasn't heard from A.

What happened?

```text
Possibility 1:
A crashed.

Possibility 2:
Network packet is delayed.

Possibility 3:
Network partition occurred.

Possibility 4:
A is processing the request.

Possibility 5:
A replied, but the reply is delayed.
```

Under asynchronous assumptions, B cannot know which world it is in.

And that uncertainty is what makes the impossibility result possible.

This connects CAP to a much broader family of distributed-systems results, especially the **FLP impossibility result** and the theory of consensus.

---

# 17. A practical checklist

When designing a distributed system, I would ask these questions in order:

### Step 1 — What happens if communication fails?

Draw:

```text
Region A | Region B
---------X---------
```

### Step 2 — What operations must continue?

For each operation:

```text
READ
WRITE
DELETE
TRANSFER
RESERVE
```

ask whether it must work during the partition.

### Step 3 — What anomalies are acceptable?

Can you tolerate:

```text
stale reads?
duplicate writes?
lost updates?
conflicting updates?
temporary divergence?
```

### Step 4 — What must be globally unique?

Things like:

```text
account ownership
inventory
locks
resource allocation
```

usually push you toward strong coordination.

### Step 5 — What happens when you cannot coordinate?

Explicitly decide:

```text
return error?
block?
serve stale data?
accept the write?
queue the operation?
resolve conflict later?
```

### Step 6 — Make the tradeoff visible to the application

Don't hide it.

For example:

```text
Inventory:
    unavailable during partition

Product catalog:
    stale data allowed

Recommendations:
    stale data allowed

Payment:
    unavailable rather than double-charge
```

That's a much better architecture discussion than simply saying "we use CP."

---

## The mental model I'd keep

If you remember only one thing, remember this:

> **CAP says that when replicas cannot communicate, you cannot simultaneously guarantee that everyone sees one globally consistent history and that every reachable replica continues accepting/responding to requests.**

So:

```text
                 NETWORK PARTITION
                         │
              ┌──────────┴──────────┐
              │                     │
        CONSISTENCY              AVAILABILITY
        is sacred                is sacred
              │                     │
             CP                    AP
              │                     │
       "I'd rather reject"   "I'd rather respond"
```

And **CA isn't really the third practical choice** once you accept that partitions are possible.

## Key Takeaway

The CAP theorem isn't fundamentally about three database labels.

It's an information-theoretic impossibility:

> During a partition, a node cannot know what happened on the other side of the partition.

If you wait for knowledge, you sacrifice availability.

If you respond without knowledge, you may sacrifice strong consistency.