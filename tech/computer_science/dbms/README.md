# Database Management Systems

In computing, a database is an organized collection of data stored and accessed electronically. Small databases can be stored on a file system, while large databases are hosted on computer clusters or cloud storage. The design of databases spans formal techniques and practical considerations, including data modeling, efficient data representation and storage, query languages, security and privacy of sensitive data, and distributed computing issues, including supporting concurrent access and fault tolerance. 

Database management systems are developed over storage solutions. Some basics of storage systems are as the following : 

### Types of Storages

1. Magnetic Storage(affected by Karlqvist gap)
 - Disk Storage(HDDs, Floppy)
 - Tape storage
2. Solid - state storage
 - Random Access Memory
 - Solid - State Drive(made up of RAM units) 
 - Flash Memory Devices(NOR flash and NAND flash)

While Random Access Memory types do not require a scheudling algorithm as a sinple address points the required location for information retrieval. Magnetic Storages require scheduling algorithms for various purposes.

#### Disk Storage Schduling Algorithms

Referred from : [work@tech](https://workat.tech/core - cs/tutorial/disk - scheduling - algorithms - in - operating - system - os - ope5ahnn6mhh)(article by Ujjwal Abhishek)

Important Terms related to Disk Scheduling Algorithms

1. Seek Time - It is the time taken by the disk arm to locate the desired track.
2. Rotational Latency - The time taken by a desired sector of the disk to rotate itself to the position where it can access the Read/Write heads is called Rotational Latency.
3. Transfer Time - It is the time taken to transfer the data requested by the processes.
4. Disk Access Time - Disk Access time is the sum of the Seek Time, Rotational Latency, and Transfer Time. 

##### First Come First Serve (FCFS) 

In this algorithm, the requests are served in the order they come. Those who come first are served first. This is the simplest algorithm.

Eg. Suppose the order of requests are 70, 140, 50, 125, 30, 25, 160 and the initial position of the Read - Write head is 60.
Seek Time = Distance Moved by the disk arm = (140 - 70) + (140 - 50) + (125 - 50) + (125 - 30) + (30 - 25) + (160 - 25) = 480

##### Shortest Seek Time First (SSTF)

In this algorithm, the shortest seek time is checked from the current position and those requests which have the shortest seek time is served first. In simple words, the closest request from the disk arm is served first.

Eg. Suppose the order of requests are 70, 140, 50, 125, 30, 25, 160 and the initial position of the Read - Write head is 60.

Seek Time = Distance Moved by the disk arm = (60 - 50) + (50 - 30) + (30 - 25) + (70 - 25) + (125 - 70) + (140 - 125) + (160 - 125) = 270

##### SCAN 

In this algorithm, the disk arm moves in a particular direction till the end and serves all the requests in its path, then it returns to the opposite direction and moves till the last request is found in that direction and serves all of them.

Eg. Suppose the order of requests are 70, 140, 50, 125, 30, 25, 160 and the initial position of the Read - Write head is 60. And it is given that the disk arm should move towards the larger value.

Seek Time = Distance Moved by the disk arm = (170 - 60) + (170 - 25) = 255

##### LOOK

In this algorithm, the disk arm moves in a particular direction till the last request is found in that direction and serves all of them found in the path, and then reverses its direction and serves the requests found in the path again up to the last request found. The only difference between SCAN and LOOK is, it doesn't go to the end it only moves up to which the request is found.

Eg. Suppose the order of requests are 70, 140, 50, 125, 30, 25, 160 and the initial position of the Read - Write head is 60. And it is given that the disk arm should move towards the larger value.

Seek Time = Distance Moved by the disk arm = (170 - 60) + (170 - 25) = 235

##### C-SCAN 

This algorithm is the same as the SCAN algorithm. The only difference between SCAN and C - SCAN is, it moves in a particular direction till the last and serves the requests in its path. Then, it returns in the opposite direction till the end and doesn't serve the request while returning. Then, again reverses the direction and serves the requests found in the path. It moves circularly.

Eg. Suppose the order of requests are 70, 140, 50, 125, 30, 25, 160 and the initial position of the Read - Write head is 60. And it is given that the disk arm should move towards the larger value.

Seek Time = Distance Moved by the disk arm = (170 - 60) + (170 - 0) + (50 - 0) = 330

##### C-LOOK 

This algorithm is also the same as the LOOK algorithm. The only difference between LOOK and C - LOOK is, it moves in a particular direction till the last request is found and serves the requests in its path. Then, it returns in the opposite direction till the last request is found in that direction and doesn't serve the request while returning. Then, again reverses the direction and serves the requests found in the path. It also moves circularly.

Eg. Suppose the order of requests are 70, 140, 50, 125, 30, 25, 160 and the initial position of the Read - Write head is 60. And it is given that the disk arm should move towards the larger value.

Seek Time = Distance Moved by the disk arm = (160 - 60) + (160 - 25) + (50 - 25) = 260

### RAID

Referred from [Wikipedia](https://en.wikipedia.org/wiki/RAID)

Virtualization is required to use each storage effectively. This is applied through **RAID** which stands for "redundant array of inexpensive disks" or "redundant array of independent disks". It combines multiple physical disk drive components into one or more logical units for the purposes of data redundancy, performance improvement, or both. This was in contrast to the previous concept of highly reliable mainframe disk drives referred to as "single large expensive disk" (SLED).

Data is distributed across the drives in one of several ways, referred to as RAID levels, depending on the required level of redundancy and performance. The different schemes, or data distribution layouts, are named by the word "RAID" followed by a number, for example RAID 0 or RAID 1. Each scheme, or RAID level, provides a different balance among the key goals: reliability, availability, performance, and capacity. RAID levels greater than RAID 0 provide protection against unrecoverable sector read errors, as well as against failures of whole physical drives. 

#### Standard Levels

Originally, there were five standard levels of RAID, but many variations have evolved, including several nested levels and many non-standard levels (mostly proprietary). RAID levels and their associated data formats are standardized by the Storage Networking Industry Association (SNIA) in the Common RAID Disk Drive Format (DDF) standard:

1. RAID 0 consists of striping, but no mirroring or parity. Compared to a spanned volume, the capacity of a RAID 0 volume is the same; it is the sum of the capacities of the drives in the set. But because striping distributes the contents of each file among all drives in the set, the failure of any drive causes the entire RAID 0 volume and all files to be lost. In comparison, a spanned volume preserves the files on the unfailing drives. The benefit of RAID 0 is that the throughput of read and write operations to any file is multiplied by the number of drives because, unlike spanned volumes, reads and writes are done concurrently. The cost is increased vulnerability to drive failures—since any drive in a RAID 0 setup failing causes the entire volume to be lost, the average failure rate of the volume rises with the number of attached drives.
2. RAID 1 consists of data mirroring, without parity or striping. Data is written identically to two or more drives, thereby producing a "mirrored set" of drives. Thus, any read request can be serviced by any drive in the set. If a request is broadcast to every drive in the set, it can be serviced by the drive that accesses the data first (depending on its seek time and rotational latency), improving performance. Sustained read throughput, if the controller or software is optimized for it, approaches the sum of throughputs of every drive in the set, just as for RAID 0. Actual read throughput of most RAID 1 implementations is slower than the fastest drive. Write throughput is always slower because every drive must be updated, and the slowest drive limits the write performance. The array continues to operate as long as at least one drive is functioning.
3. RAID 2 consists of bit-level striping with dedicated Hamming-code parity. All disk spindle rotation is synchronized and data is striped such that each sequential bit is on a different drive. Hamming-code parity is calculated across corresponding bits and stored on at least one parity drive. This level is of historical significance only; although it was used on some early machines (for example, the Thinking Machines CM-2), as of 2014 it is not used by any commercially available system.
4. RAID 3 consists of byte-level striping with dedicated parity. All disk spindle rotation is synchronized and data is striped such that each sequential byte is on a different drive. Parity is calculated across corresponding bytes and stored on a dedicated parity drive. Although implementations exist, RAID 3 is not commonly used in practice.
5. RAID 4 consists of block-level striping with dedicated parity. This level was previously used by NetApp, but has now been largely replaced by a proprietary implementation of RAID 4 with two parity disks, called RAID-DP. The main advantage of RAID 4 over RAID 2 and 3 is I/O parallelism: in RAID 2 and 3, a single read I/O operation requires reading the whole group of data drives, while in RAID 4 one I/O read operation does not have to spread across all data drives. As a result, more I/O operations can be executed in parallel, improving the performance of small transfers.
6. RAID 5 consists of block-level striping with distributed parity. Unlike RAID 4, parity information is distributed among the drives, requiring all drives but one to be present to operate. Upon failure of a single drive, subsequent reads can be calculated from the distributed parity such that no data is lost. RAID 5 requires at least three disks. Like all single-parity concepts, large RAID 5 implementations are susceptible to system failures because of trends regarding array rebuild time and the chance of drive failure during rebuild (see "Increasing rebuild time and failure probability" section, below). Rebuilding an array requires reading all data from all disks, opening a chance for a second drive failure and the loss of the entire array.
7. RAID 6 consists of block-level striping with double distributed parity. Double parity provides fault tolerance up to two failed drives. This makes larger RAID groups more practical, especially for high-availability systems, as large-capacity drives take longer to restore. RAID 6 requires a minimum of four disks. As with RAID 5, a single drive failure results in reduced performance of the entire array until the failed drive has been replaced. With a RAID 6 array, using drives from multiple sources and manufacturers, it is possible to mitigate most of the problems associated with RAID 5. The larger the drive capacities and the larger the array size, the more important it becomes to choose RAID 6 instead of RAID 5. RAID 10 also minimizes these problems.

#### Nested RAID

In what was originally termed hybrid RAID, many storage controllers allow RAID levels to be nested. The elements of a RAID may be either individual drives or arrays themselves. Arrays are rarely nested more than one level deep.

The final array is known as the top array. When the top array is RAID 0 (such as in RAID 1+0 and RAID 5+0), most vendors omit the "+" (yielding RAID 10 and RAID 50, respectively).

#### Non-Standard levels

* Linux MD RAID 10
* Hadoop
* BeeGFS
* Declustered RAID

## Database Management Systems

Adapted from [Wikipedia](https://en.wikipedia.org/wiki/Database)

In computing, a database is an organized collection of data stored and accessed electronically. Small databases can be stored on a file system, while large databases are hosted on computer clusters or cloud storage. The design of databases spans formal techniques and practical considerations, including data modeling, efficient data representation and storage, query languages, security and privacy of sensitive data, and distributed computing issues, including supporting concurrent access and fault tolerance.

A database management system (DBMS) is the software that interacts with end users, applications, and the database itself to capture and analyze the data. The DBMS software additionally encompasses the core facilities provided to administer the database. The sum total of the database, the DBMS and the associated applications can be referred to as a database system. Often the term "database" is also used loosely to refer to any of the DBMS, the database system or an application associated with the database.

The interactions are done through various means such as : 

1. SQL(Structured Query Language, Oracle DB, PostgreSQL)
2. Spreadsheets(dBase, MS Excel, OpenOffice Calc)
3. Object Oriented(ORM like abstraction for DBs)
4. NoSQL(MongoDB, Redis)
5. NewSQL

Brief on NewSQL : NewSQL is a class of relational database management systems that seek to provide the scalability of NoSQL systems for online transaction processing (OLTP) workloads while maintaining the ACID guarantees of a traditional database system. Many enterprise systems that handle high-profile data (e.g., financial and order processing systems) are too large for conventional relational databases, but have transactional and consistency requirements that are not practical for NoSQL systems. The only options previously available for these organizations were to either purchase more powerful computers or to develop custom middleware that distributes requests over conventional DBMS. Both approaches feature high infrastructure costs and/or development costs. NewSQL systems attempt to reconcile the conflicts. Ex : Apache Trafodion, Clustrix, CockroachDB, Couchbase, Google Spanner, NuoDB, Pivotal GemFire XD, SingleStore was formerly known as MemSQL., TIBCO Active Spaces, TiDB, TokuDB, TransLattice Elastic Database, VoltDB, YugabyteDB.

### Properties of database transactions

Adapted from [Wikipedia](https://en.wikipedia.org/wiki/ACID)

ACID, BASE(not referred here to avoid ambiguity) & CAP

#### Atomicity

Transactions are often composed of multiple statements. Atomicity guarantees that each transaction is treated as a single "unit", which either succeeds completely or fails completely: if any of the statements constituting a transaction fails to complete, the entire transaction fails and the database is left unchanged. An atomic system must guarantee atomicity in each and every situation, including power failures, errors, and crashes. A guarantee of atomicity prevents updates to the database from occurring only partially, which can cause greater problems than rejecting the whole series outright. As a consequence, the transaction cannot be observed to be in progress by another database client. At one moment in time, it has not yet happened, and at the next, it has already occurred in whole (or nothing happened if the transaction was canceled in progress).

An example of an atomic transaction is a monetary transfer from bank account A to account B. It consists of two operations, withdrawing the money from account A and saving it to account B. Performing these operations in an atomic transaction ensures that the database remains in a consistent state, that is, money is neither debited nor credited if either of those two operations fails.

#### Consistency (Correctness)

Consistency ensures that a transaction can only bring the database from one valid state to another, maintaining database invariants: any data written to the database must be valid according to all defined rules, including constraints, cascades, triggers, and any combination thereof. This prevents database corruption by an illegal transaction, but does not guarantee that a transaction is correct. Referential integrity guarantees the primary key – foreign key relationship.

#### Isolation

Transactions are often executed concurrently (e.g., multiple transactions reading and writing to a table at the same time). Isolation ensures that concurrent execution of transactions leaves the database in the same state that would have been obtained if the transactions were executed sequentially. Isolation is the main goal of concurrency control; depending on the method used, the effects of an incomplete transaction might not even be visible to other transactions.

#### Durability

Durability guarantees that once a transaction has been committed, it will remain committed even in the case of a system failure (e.g., power outage or crash). This usually means that completed transactions (or their effects) are recorded in non-volatile memory.

#### CAP Theorem

In theoretical computer science, the CAP theorem, also named Brewer's theorem after computer scientist Eric Brewer, states that any distributed data store can provide only two of the following three guarantees:

1. Consistency : Every read receives the most recent write or an error.
2. Availability : Every request receives a (non-error) response, without the guarantee that it contains the most recent write.
3. Partition tolerance : The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes.

When a network partition failure happens, it must be decided whether to

1. cancel the operation and thus decrease the availability but ensure consistency or to
2. proceed with the operation and thus provide availability but risk inconsistency.

### Relational Database Management System

Codd's twelve rules are a set of thirteen rules (numbered zero to twelve) proposed by Edgar F. Codd, a pioneer of the relational model for databases, designed to define what is required from a database management system in order for it to be considered relational, i.e., a relational database management system (RDBMS).

#### Rule 1: Information Rule

The data stored in a database, may it be user data or metadata, must be a value of some table cell. Everything in a database must be stored in a table format.

#### Rule 2: Guaranteed Access Rule

Every single data element (value) is guaranteed to be accessible logically with a combination of table-name, primary-key (row value), and attribute-name (column value). No other means, such as pointers, can be used to access data.

#### Rule 3: Systematic Treatment of NULL Values

The NULL values in a database must be given a systematic and uniform treatment. This is a very important rule because a NULL can be interpreted as one the following − data is missing, data is not known, or data is not applicable.

#### Rule 4: Active Online Catalog

The structure description of the entire database must be stored in an online catalog, known as data dictionary, which can be accessed by authorized users. Users can use the same query language to access the catalog which they use to access the database itself.

#### Rule 5: Comprehensive Data Sub-Language Rule

A database can only be accessed using a language having linear syntax that supports data definition, data manipulation, and transaction management operations. This language can be used directly or by means of some application. If the database allows access to data without any help of this language, then it is considered as a violation.

#### Rule 6: View Updating Rule

All the views of a database, which can theoretically be updated, must also be updatable by the system.

#### Rule 7: High-Level Insert, Update, and Delete Rule

A database must support high-level insertion, updation, and deletion. This must not be limited to a single row, that is, it must also support union, intersection and minus operations to yield sets of data records.

#### Rule 8: Physical Data Independence

The data stored in a database must be independent of the applications that access the database. Any change in the physical structure of a database must not have any impact on how the data is being accessed by external applications.

#### Rule 9: Logical Data Independence

The logical data in a database must be independent of its user’s view (application). Any change in logical data must not affect the applications using it. For example, if two tables are merged or one is split into two different tables, there should be no impact or change on the user application. This is one of the most difficult rule to apply.

#### Rule 10: Integrity Independence

A database must be independent of the application that uses it. All its integrity constraints can be independently modified without the need of any change in the application. This rule makes a database independent of the front-end application and its interface.

#### Rule 11: Distribution Independence

The end-user must not be able to see that the data is distributed over various locations. Users should always get the impression that the data is located at one site only. This rule has been regarded as the foundation of distributed database systems.

#### Rule 12: Non-Subversion Rule

If a system has an interface that provides access to low-level records, then the interface must not be able to subvert the system and bypass security and integrity constraints.


#### Database Normalization

Database normalization is the process of structuring a relational database in accordance with a series of so-called normal forms in order to reduce data redundancy and improve data integrity. It was first proposed by Edgar F. Codd as part of his relational model.

##### Objective

A basic objective of the first normal form defined by Codd in 1970 was to permit data to be queried and manipulated using a "universal data sub-language" grounded in first-order logic. An example of such language is SQL, though it is one that Codd regarded as seriously flawed.)

The objectives of normalisation beyond 1NF (first normal form) were stated as follows by Codd:

        To free the collection of relations from undesirable insertion, update and deletion dependencies.
        To reduce the need for restructuring the collection of relations, as new types of data are introduced, and thus increase the life span of application programs.
        To make the relational model more informative to users.
        To make the collection of relations neutral to the query statistics, where these statistics are liable to change as time goes by.

    — E.F. Codd, "Further Normalisation of the Data Base Relational Model"[3]

An insertion anomaly. Until the new faculty member, Dr. Newsome, is assigned to teach at least one course, their details cannot be recorded.
An update anomaly. Employee 519 is shown as having different addresses on different records.
A deletion anomaly. All information about Dr. Giddens is lost if they temporarily cease to be assigned to any courses.

When an attempt is made to modify (update, insert into, or delete from) a relation, the following undesirable side-effects may arise in relations that have not been sufficiently normalized:

**Insertion anomaly** : There are circumstances in which certain facts cannot be recorded at all. For example, each record in a "Faculty and Their Courses" relation might contain a Faculty ID, Faculty Name, Faculty Hire Date, and Course Code. Therefore, the details of any faculty member who teaches at least one course can be recorded, but a newly hired faculty member who has not yet been assigned to teach any courses cannot be recorded, except by setting the Course Code to null.

**Update anomaly** : The same information can be expressed on multiple rows; therefore updates to the relation may result in logical inconsistencies. For example, each record in an "Employees' Skills" relation might contain an Employee ID, Employee Address, and Skill; thus a change of address for a particular employee may need to be applied to multiple records (one for each skill). If the update is only partially successful – the employee's address is updated on some records but not others – then the relation is left in an inconsistent state. Specifically, the relation provides conflicting answers to the question of what this particular employee's address is.

**Deletion anomaly** : Under certain circumstances, deletion of data representing certain facts necessitates deletion of data representing completely different facts. The "Faculty and Their Courses" relation described in the previous example suffers from this type of anomaly, for if a faculty member temporarily ceases to be assigned to any courses, the last of the records on which that faculty member appears must be deleted, effectively also deleting the faculty member, unless the Course Code field is set to null.

###### Normal Forms

References : [Java T Point](https://www.javatpoint.com/dbms-normalization)
    1NF : A relation is in 1NF if it contains an atomic value.
    2NF : A relation will be in 2NF if it is in 1NF and all non-key attributes are fully functional dependent on the primary key.
    3NF : A relation will be in 3NF if it is in 2NF and no transition dependency exists.
    BCNF : A stronger definition of 3NF is known as Boyce Codd's normal form.
    4NF : A relation will be in 4NF if it is in Boyce Codd's normal form and has no multi-valued dependency.
    5NF : A relation is in 5NF. If it is in 4NF and does not contain any join dependency, joining should be lossless.
    
##### Advantages of Normalization

    Normalization helps to minimize data redundancy.
    Greater overall database organization.
    Data consistency within the database.
    Much more flexible database design.
    Enforces the concept of relational integrity.

##### Disadvantages of Normalization

    You cannot start building the database before knowing what the user needs.
    The performance degrades when normalizing the relations to higher normal forms, i.e., 4NF, 5NF.
    It is very time-consuming and difficult to normalize relations of a higher degree.
    Careless decomposition may lead to a bad database design, leading to serious problems.
