# Distributed Algorithm

A **distributed algorithm** is an algorithm designed to **run across multiple computers (nodes or processes)** connected by a network, where each node has **limited knowledge** and communicates with others by **sending and receiving messages**.

## Key Characteristics of Distributed Algorithms:

| Feature             | Description                                                                         |
| ------------------- | ----------------------------------------------------------------------------------- |
| **Multiple nodes**  | Algorithm runs on multiple machines, each with its own local memory and processing. |
| **Communication**   | Nodes communicate via messages (not shared memory).                                 |
| **Concurrency**     | Nodes operate concurrently and independently.                                       |
| **Fault tolerance** | Must handle node failures, network delays, or message loss.                         |
| **No global clock** | Nodes operate asynchronously or with partial time sync.                             |

## Common Use Cases

* **Leader election** (e.g., choosing a master node)
* **Consensus** (e.g., Paxos, Raft)
* **Distributed data structures**
* **Mutual exclusion** in distributed systems
* **Broadcasting and synchronization**

## Example 1: Leader Election in a Ring Network (Simplified)

Each node has a unique ID and is connected in a ring. Goal: elect the node with the highest ID.

```ini
function onStart(node)
    sendMessageToNext({type: "election", id: node.id})

function onReceive(message)
    if message.type == "election"
        if message.id > node.id
            sendMessageToNext(message)
        else if message.id < node.id
            // Discard smaller ID, start election with own
            sendMessageToNext({type: "election", id: node.id})
        else
            // Message came back to origin: I’m the leader
            broadcast({type: "leader", id: node.id})

function onReceive(message)
    if message.type == "leader"
        node.leaderId = message.id
```

* **Time Complexity:** O(n), where *n* is the number of nodes.
* **Assumptions:** Synchronous ring, unique IDs, reliable messages.

## Example 2: Distributed Mutual Exclusion (Ricart-Agrawala Algorithm)

Each node wants exclusive access to a shared resource.

```ini
onRequestCS()
    timestamp = current time
    requestQueue.add(self)
    broadcast({type: "request", from: self.id, time: timestamp})

onReceiveRequest(message)
    reply immediately if:
        - not in critical section AND
        - (no pending request OR message.timestamp < my.timestamp)
    else
        queue message

onReceiveReply()
    mark reply received from sender
    if replies received from all nodes
        enterCriticalSection()

onExitCS()
    for each queued request
        send reply
```

* **Message complexity:** O(n) per request.
* Ensures mutual exclusion without a central coordinator.

## Example 3: Gossip (Rumor Spreading / Epidemic Protocol)

Used for broadcasting or synchronization.

```ini
every T seconds:
    if node knows rumor
        select random neighbor
        send rumor to neighbor

onReceiveRumor(rumor)
    if not known
        store rumor
        gossip = true
```

* **Fast convergence** with probabilistic guarantees.
* Used in systems like Cassandra and Dynamo.

## Summary: When to Use Distributed Algorithms

* You have a **network of independent machines**.
* Shared memory is **not possible**.
* Fault-tolerance and scalability are critical.
* You’re building systems like databases, blockchains, cloud infrastructure, etc.
