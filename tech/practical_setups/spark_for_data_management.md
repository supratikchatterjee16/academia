# Apache Spark for Data Management

Apache Spark is a framework that aims to provide a unified engine for large scale Data Analytics.

This sits on top of cluster managers to be able to arrange data and provide the information at
high speeds, while making sure that high availability is not compromised.

It supports 3 Cluster Managers :

1. [Standalone](https://spark.apache.org/docs/2.1.1/spark-standalone.html) cluster manager that ships with Apache Spark
2. [Apache Mesos](http://mesos.apache.org/), which abstracts CPU, memory, storage, and other compute resources.
3. [Apache Hadoop YARN](https://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-site/YARN.html) which is a resource management and job scheduling technology

The core construct of Apache Spark is the RDD, which was data represented as a Java Object, when it initially began. A brief history about the concept is :

    Spark 1.0 to 1.3: It started with RDD’s where data is represented as Java Objects.
    Spark 1.4 to 1.6: Deprioritised Java objects. DataSet and DataFrame evolved where data is stored in row-based format.
    Spark 2.x: Support for Vectorized Parquet which is columnar in-memory data is added.

So why was RDD removed? It was removed to accommodate Dataframes, which is a row-based data format, that has lesser need for Java serialization and has lesser overhead than Java objects.

Now even though RDD is not used as a structure in the backend, for the interface, for backward compatibility, the structure is maintained.

## Resilient Distributed Dataset


    Resilient because RDDs are immutable(can’t be modified once created) and fault tolerant
    Distributed because it is distributed across cluster
    Dataset because it holds data.

This is the primary structure in use for the transactions to and from the PySpark endpoint.

### Partitions

RDDs are divided into smaller chunks called Partitions, and when you execute some action, a task is launched per partition. So it means, the more the number of partitions, the more the parallelism. Spark automatically decides the number of partitions that an RDD has to be divided into but you can also specify the number of partitions when creating an RDD. These partitions of an RDD is distributed across all the nodes in the network.

### Some basic operations

#### Create an RDD

Creating an RDD is easy, it can be created either from an external file or by parallelizing collections in your driver. For example,

```
val rdd = sc.textFile("/some_file",3)  
val lines = sc.parallelize(List("this is","an example"))
```

The first line creates an RDD from an external file, and the second line creates an RDD from a list of Strings. Note that the argument ‘3’ in the method call sc.textFile() specifies the number of partitions that has to be created. If you don’t want to specify the number of partitions, then you can simply call sc.textFile(“some_file”).

#### Actions/Transformations

There are two types of operations that you can perform on an RDD- Transformations and Actions. Transformation applies some function on a RDD and creates a new RDD, it does not modify the RDD that you apply the function on.(Remember that RDDs are resilient/immutable).

    **The new RDD keeps a pointer to it’s parent RDD.**

When you call a transformation, Spark does not execute it immediately, instead it creates a lineage. A lineage keeps track of what all transformations has to be applied on that RDD, including from where it has to read the data.

```
val rdd = sc.textFile("spam.txt")
val filtered = rdd.filter(line => line.contains("money"))
filtered.count()
```

sc.textFile() and rdd.filter() do not get executed immediately, it will only get executed once you call an Action on the RDD - here filtered.count(). An Action is used to either save result to some location or to display it. You can also print the RDD lineage information by using the command filtered.toDebugString(filtered is the RDD here).

    RDDs can also be thought of as a set of instructions that has to be executed, first instruction being the load instruction.

#### Caching

You can cache an RDD in memory by calling rdd.cache(). When you cache an RDD, it’s Partitions are loaded into memory of the nodes that hold it.

Caching can improve the performance of your application to a great extent. In the previous section you saw that when an action is performed on a RDD, it executes it’s entire lineage. Now imagine you are going to perform an action multiple times on the same RDD which has a long lineage, this will cause an increase in execution time. Caching stores the computed result of the RDD in the memory thereby eliminating the need to recompute it every time. You can think of caching as if it is breaking the lineage, but it does remember the lineage so that it can be recomputed in case of a node failure.

#### Persistence

 If there is not enough memory in the cluster, you can tell spark to use disk also for saving the RDD by using the method persist().

```
rdd.persist(StorageLevel.MEMORY_AND_DISK)
```

n fact Caching is a type of persistence with StorageLevel -MEMORY_ONLY. If you use MEMORY_ONLY as the Storage Level and if there is not enough memory in your cluster to hold the entire RDD, then some partitions of the RDD cannot be stored in memory and will have to be recomputed every time it is needed. If you don’t want this to happen, you can use the StorageLevel - MEMORY_AND_DISK in which if an RDD does not fit in memory, the partitions that do not fit are saved to disk.

#### Broadcast variables

A broadcast variable, is a type of shared variable, used for broadcasting data across the cluster. Hadoop MapReduce users can relate this to distributed cache. Let us first understand why we need a broadcast variable. Take a look at the below example, where names is joined with addresses.

```
val names = sc.textFile("/names").map(line => (line.split(",")(3),line))
val addresses = sc.textFile("/address").map(line=>(line.split(",")(0),line))
names.join(addresses)
```

Here, both names and addresses will be shuffled over the network for performing the join which is not efficient since any data transfer over the network will reduce the execution speed.

Another approach is, if one of the RDDs is small in size, we can choose to send it along with each task. Consider the below example :

```
val names = sc.textFile("/names").map(line => (line.split(",")(3),line))
val addresses = sc.textFile("/address").map(line=>(line.split(",")(0),line))
val addressesMap = addresses.collect().toMap
val joined = names.map(v=>(v._2,(addressesMap(v._1))))
```

This is also inefficient since we are sending sizable amount of data over the network for each task. So how do we overcome this problem? By means of broadcast variables.

```
val names = sc.textFile("/names").map(line => (line.split(",")(3),line))
val addresses = sc.textFile("/address").map(line=>(line.split(",")(0),line))
val addressesMap = addresses.collect().toMap
val broadcast = sc.broadcast(addressesMap)
val joined = names.map(v=>(v._2,(broadcast.value(v._1))))
```

#### Accumulators

Accumulators, as the name suggests accumulates data during execution. This is similar to Counters in Hadoop MapReduce. An accumulator is initialized at the driver and is then modified (added) by each executors. Finally all these values are aggregated back at the driver.

```
val names = sc.textFile("/names").map(line => (line.split(",")(3),line))
val addresses = sc.textFile("/address").map(line=>(line.split(",")(0),line))
val addressesMap = addresses.collect().toMap
val broadcast = sc.broadcast(addressesMap)
val joined = names.map(v=>(v._2,(broadcast.value(v._1))))

val accum = sc.accumulator(0,"india_counter")
joined.foreach(v=> if (v._2.contains("india")) accum += 1)

//we cannot do below operations on accumulators of the type Int
//joined.foreach(v=> if (v._2.contains("india")) accum -= 1)
//joined.foreach(v=> if (v._2.contains("india")) accum *= 1)
//error: value *= is not a member of org.apache.spark.Accumulator[Int]
```
