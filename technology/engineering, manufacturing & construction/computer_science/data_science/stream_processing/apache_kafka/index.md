# Apache Kafka

Apache Kafka is a platform to build real time streaming applications. Kafka was created by engineers at LinkedIn to meet demands of processing events as they occur.

- Kafka is a publish-subscribe messaging system, written in Scala and Java, that is fast, distributed and durable.
- Kafka is fault-tolerant and enables you to build distributed applications that scale on commodity hardware.

Kafka is primarily a messaging system. A messaging system is a medium that allows data transfer from one application to another so that the applications can focus on data without worrying about how to share it.

The two types of messaging patterns are:

- Point-to-Point Messaging System
- Publish-Subscribe Messaging System

Apache Kafka is a distributed publish-subscribe messaging system used for collecting and delivering high volumes of data with low latency, similar to a traditional message broker.

## Benefits of Kafka

1. Reliability: Kafka's distributed design, topic partitioning, and data replication over servers make it reliable.
2. Scalability: Kafka system exists as a cluster of brokers. The number of brokers can grow over time when more data comes. Any failure of an individual broker in a cluster is handled by the system providing uninterrupted service.
3. Durability: Disk-based data retention makes Kafka durable. Messages remain on the disk based on the retention rule configured on a per-topic basis. Even if a consumer falls backs due to any reason, the data continue to reside in the Broker till the retention period and is not lost.
4. High-Performance: All the above features make Kafka a High-Performance messaging system.

## Components of Kafka

1. Producers
2. Topics
3. Brokers
4. Consumers
5. Consumer Groups
6. Controller
7. Zookeeper
8. Streams

### Producers

Producers are systems that publish data or messages to the brokers.

### Topics

These are channels to which publishers can publish data to, and consumers can subscribe to, in order to receive data from.

It is a structured commit log.
These can have partitions. Partitioning helps scale the listener.

Data is stored as immutable ordered sequence.

Topic Replication Factor is a factor that describes the redundancy of data in topics. This should be greater than 1 everytime. In the scenario one broker goes down, the others can serve the data.

**A Kafka Broker with multiple topics and consumer groups, can have only 1 consumer per group, listening to each topic partition.**

### Brokers

Individual Nodes that host the information published by the publishers. When data  is being published, one 1 broker can be a leader. There is a leader for each topic. The other brokers, have in-sync replicas. These replicas can also be a **follower** which is tasked with becoming he leader, if the current leader fails.


### Consumers

Consumers are nodes that read information from the various topics. Consumers havve 2 important concepts : 

1. Consumer Groups : These are groups that a consumer can be assigned to, for easy subscribing to topics. Each consumer in the group is assigned one or 2 partitions to read from.
2. Consumer Offset : How much of the data in a topic has been read by a consumer. It is sort of a read head of a disk.

Consumer group concept of Kafka helps scale processing and multi-subscription.

### Controller

Controller is one of the brokers and is responsible for maintaining the leader/follower relationship for all the partitions.

### Zookeeper

Zookeeper is a distributed centralized service that coordinates/manages large sets of hosts.

Zookeeper is used to provide a configuration service, naming registry, synchronization, and group services in distributed applications.

Kafka uses Zookeeper for the following:

1. Electing a controller :
    - The controller is one among the many brokers responsible for maintaining the leader/follower relationship for all the partitions.
    - When a node crashes or shuts down, the controller tells other replicas to become partition leader replacing the one on the node, that is going away.
    - Zookeeper elects a controller, makes sure there is only one, and elects a new one it if it crashes.
2. Cluster membership: Zookeeper monitors which brokers are alive and part of the cluster.
3. Topic configuration: Zookeeper keeps track of topics, its partitions and replicas, who is the preferred leader and what configuration overrides are set for each topic.
4. Quotas: Zookeeper tracks how much data each client is allowed to read and write.
5. ACLs: Zookeeper tracks the following: Who is allowed to read and write to which topic, What are the consumer groups which exist, Who are their respective members and What is the latest offset each group received from each partition.

### Streams

A stream processor in Kafka reads streams of data from **input topics**, processes this data and produces continuous streams of data to **output topics**. For this purpose, Kafka provides a fully integrated Streams API.

This in other words is a transformer for data in a topic.

It has the following concepts : 

1. Stream - Primary abstraction in Kafka Streams, it represents an unbounded and continuously updating data set. A stream contains a sequence of immutable data records which are ordered and fault tolerant.
2. Stream processing application - Program using the Kafka Streams Library to implement its computational logic through one or more processor topologies.
3. Processor topology - Graph of stream processors (nodes) that are connected by streams (edges).
4. Stream processor - Node in the processor topology. It denotes a processing step to operate on input stream data by receiving an input record at a time from its upstream processors in the topology, applying transformations, and consequently producing output records to its downstream processors. Two special stream processors:
    - Source Processor - Does not have any upstream processors. It produces an input stream to its topology by consuming records from one or more Kafka topics and forwards it to downstream processors.
    - Sink Processor - Does not have downstream processors. It sends any received records from its upstream processors to a specified Kafka topic.

**Highlights**

- Simple, lightweight client library.
- No external dependencies on systems other than Kafka.
- Supports exactly-once processing semantics.
- Supports event-time based windowing operations.