# Java - Remote Method Invocation

## 1. Historical Background

* **Early Distributed Systems (1980s–1990s):** As distributed computing grew in importance, developers sought ways to allow programs on different machines to communicate. Technologies like **CORBA (Common Object Request Broker Architecture)** and **DCOM (Distributed Component Object Model)** emerged.
* **Java Emergence (mid-1990s):** With Java’s popularity, Sun Microsystems introduced **Java RMI** in **JDK 1.1 (1997)** as a simpler, Java-centric alternative for distributed object communication.
* **Key Differentiator:** Unlike CORBA (multi-language, complex), RMI was **Java-only** but tightly integrated with the language’s object model, making distributed programming more natural for Java developers.
* **Evolution:**

  * Early RMI used **JRMP (Java Remote Method Protocol)** (Java-specific).
  * Later versions introduced **RMI-IIOP** for CORBA interoperability.
  * With Java 2, RMI gained **dynamic class loading** and **serialization support**.

---

## 2. Core Concepts of Java RMI

At its heart, RMI allows an object running in one Java Virtual Machine (JVM) to **invoke methods on an object running in another JVM**, potentially across a network.

### Key Components:

1. **Remote Interface**

   * Defines the methods that can be invoked remotely.
   * Must extend `java.rmi.Remote`.
   * Each method must declare `throws RemoteException`.

2. **Remote Object (Server Implementation)**

   * A class that implements the remote interface.
   * Usually extends `UnicastRemoteObject` (to support RMI networking).

3. **Stub and Skeleton**

   * *Stub*: Acts as a client-side proxy for the remote object.
   * *Skeleton*: (in older versions) handled server-side communication. Since Java 2, skeletons are generated dynamically.

4. **RMI Registry**

   * A simple naming service where servers register remote objects so clients can look them up by name.

5. **Communication Layer**

   * Uses **JRMP** by default for communication.
   * Handles marshalling (serializing arguments) and unmarshalling (deserializing results).

---

## 3. How to Use Java RMI

Here’s a **step-by-step example** of a simple RMI application.

### (A) Define a Remote Interface

```java
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface HelloService extends Remote {
    String sayHello(String name) throws RemoteException;
}
```

### (B) Implement the Remote Interface

```java
import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;

public class HelloServiceImpl extends UnicastRemoteObject implements HelloService {
    protected HelloServiceImpl() throws RemoteException {
        super();
    }

    @Override
    public String sayHello(String name) throws RemoteException {
        return "Hello, " + name + "!";
    }
}
```

### (C) Create the Server

```java
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class HelloServer {
    public static void main(String[] args) {
        try {
            HelloService service = new HelloServiceImpl();
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("HelloService", service);
            System.out.println("Server started, waiting for clients...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### (D) Create the Client

```java
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class HelloClient {
    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            HelloService service = (HelloService) registry.lookup("HelloService");
            String response = service.sayHello("Alice");
            System.out.println("Response: " + response);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

---

## 4. Running the Application

1. **Compile all classes**

   ```bash
   javac *.java
   ```
2. **Start the server**

   ```bash
   java HelloServer
   ```
3. **Run the client** (in another terminal)

   ```bash
   java HelloClient
   ```

---

## 5. Strengths & Limitations

**Strengths:**

* Seamless integration with Java’s object model.
* Transparent remote calls (looks like local method calls).
* Built-in security (via Java Security Manager).

**Limitations:**

* Java-only (less suitable for heterogeneous systems).
* Legacy technology—modern systems often prefer **REST, gRPC, or messaging frameworks** for distributed applications.
