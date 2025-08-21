# Middleware softwares

In **software engineering**, middleware is any software layer that sits **between the operating system/network and applications**, helping distributed systems communicate, integrate, and function reliably.

Here are some major **categories of middleware**:

---

### **1. Message-Oriented Middleware (MOM)**

* **Purpose:** Enables asynchronous communication between distributed applications.
* **Examples:** RabbitMQ, Apache Kafka, ActiveMQ, Redis (pub/sub).

---

### **2. Database Middleware**

* **Purpose:** Provides connectivity and abstraction for accessing databases.
* **Examples:** ODBC, JDBC, Hibernate, Entity Framework.

---

### **3. Remote Procedure Call (RPC) / Object Request Brokers (ORB)**

* **Purpose:** Allows one application to invoke procedures/methods on another system as if they were local.
* **Examples:** gRPC, Apache Thrift, CORBA, Java RMI.

---

### **4. Transaction Processing Monitors**

* **Purpose:** Manage and coordinate transactions across distributed systems to ensure consistency and reliability (ACID).
* **Examples:** IBM CICS, Tuxedo, Microsoft Transaction Server (MTS).

---

### **5. Web Middleware**

* **Purpose:** Acts as glue between web clients (browsers, APIs) and backend applications.
* **Examples:** Web servers (Apache HTTP, Nginx), application servers (Tomcat, JBoss/WildFly), middleware frameworks (Express.js, Spring Boot).

---

### **6. Integration Middleware / Enterprise Service Bus (ESB)**

* **Purpose:** Connects heterogeneous applications and services, transforming and routing data.
* **Examples:** MuleSoft, WSO2, Apache Camel, IBM Integration Bus.

---

### **7. API Gateways / Service Middleware**

* **Purpose:** Manages API traffic, authentication, routing, and observability in service-based architectures (esp. microservices).
* **Examples:** Kong, Apigee, AWS API Gateway, NGINX as API gateway.

---

### **8. Stream Processing Middleware**

* **Purpose:** Real-time data ingestion, processing, and event-driven workflows.
* **Examples:** Apache Flink, Spark Streaming, Kafka Streams, Storm.

---

### **9. Security Middleware**

* **Purpose:** Provides authentication, authorization, encryption, and policy enforcement.
* **Examples:** OAuth servers, Kerberos, Open Policy Agent (OPA).

---

### **10. Cloud & Container Middleware**

* **Purpose:** Manages orchestration, scaling, and inter-service communication in cloud-native systems.
* **Examples:** Kubernetes (service mesh via Istio or Linkerd), HashiCorp Consul, Envoy Proxy.

### **11. Service Communication Middleware(or service mesh)**

* **Purpose:** A service mesh abstracts and manages how services discover, connect, secure, and observe each other, without requiring each application to implement these features.
* **Examples:** Istio, Linkerd, Consul Connect, Kuma, AWS App Mesh