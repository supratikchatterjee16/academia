# Google RPC(gRPC)

* **gRPC** stands for **Google Remote Procedure Call**.
* It’s an **open-source RPC framework** developed by Google in 2015.
* Built on top of **HTTP/2**, it allows efficient client-server communication.
* Uses **Protocol Buffers (Protobuf)** as the default serialization mechanism.
* Supports **bi-directional streaming**, **authentication**, **load balancing**, and **multi-language compatibility**.

---

## History

* RPC (Remote Procedure Call) dates back to the 1980s as a way to make remote systems interact like local function calls.
* Google internally used **Stubby**, a proprietary RPC framework, for years.
* In 2015, Google open-sourced **gRPC**, influenced by Stubby but designed for public adoption.
* gRPC quickly became popular for **microservices** and **cloud-native architectures** because of its speed and compatibility.

---

## Core Concepts

1. **Service Definition**

   * Defined using `.proto` files (Protocol Buffers).
   * Specifies available methods and message formats.

2. **Protocol Buffers (Protobuf)**

   * A language-neutral, platform-neutral, extensible way of serializing structured data.
   * Much faster and smaller than JSON or XML.

3. **HTTP/2 Transport**

   * Provides multiplexing, header compression, and bidirectional streaming.

4. **Client & Server Stubs**

   * Protobuf compiler generates code (stubs) for clients and servers in multiple languages.

5. **Streaming Types**

   * Unary RPC → One request, one response.
   * Server streaming → One request, multiple responses.
   * Client streaming → Multiple requests, one response.
   * Bidirectional streaming → Both client and server stream messages.

---

## Simple Code Setup

### Python

#### 1. Install gRPC

```bash
pip install grpcio grpcio-tools
```

#### 2. Define a `.proto` file (hello.proto)

```proto
syntax = "proto3";

service Greeter {
  rpc SayHello (HelloRequest) returns (HelloReply);
}

message HelloRequest {
  string name = 1;
}

message HelloReply {
  string message = 1;
}
```

#### 3. Generate gRPC Code

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. hello.proto
```

This generates:

* `hello_pb2.py` (messages)
* `hello_pb2_grpc.py` (service stubs)

#### 4. Implement Server (`server.py`)

```python
import grpc
from concurrent import futures
import hello_pb2
import hello_pb2_grpc

class Greeter(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return hello_pb2.HelloReply(message=f"Hello, {request.name}!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
```

#### 5. Implement Client (`client.py`)

```python
import grpc
import hello_pb2
import hello_pb2_grpc

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(hello_pb2.HelloRequest(name="Alice"))
    print("Greeter client received:", response.message)

if __name__ == "__main__":
    run()
```

#### 6. Run It

1. Start server:

   ```bash
   python server.py
   ```
2. In another terminal, run client:

   ```bash
   python client.py
   ```

Output:

```
Greeter client received: Hello, Alice!
```

### C/C++

gRPC was originally written in **C** and provides **first-class support for C++**. In fact, many performance-critical systems at Google use gRPC in C++.

#### 1. Install gRPC & Protobuf

You’ll need **CMake**, **gRPC**, and **Protocol Buffers**.

On Linux/macOS (example using git + cmake):

```bash
# Clone gRPC (includes Protobuf as a submodule)
git clone --recurse-submodules -b v1.68.0 https://github.com/grpc/grpc
cd grpc

# Build and install
mkdir -p cmake-build
cd cmake-build
cmake .. -DgRPC_INSTALL=ON -DgRPC_BUILD_TESTS=OFF -DCMAKE_BUILD_TYPE=Release
make -j
sudo make install
```

This installs both **gRPC** and **Protobuf** system-wide.

---

#### 2. Define a `.proto` File (`hello.proto`)

```proto
syntax = "proto3";

service Greeter {
  rpc SayHello (HelloRequest) returns (HelloReply);
}

message HelloRequest {
  string name = 1;
}

message HelloReply {
  string message = 1;
}
```

---

#### 3. Generate C++ Code

Use `protoc` to generate C++ bindings:

```bash
protoc -I=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_cpp_plugin` hello.proto
protoc -I=. --cpp_out=. hello.proto
```

This generates:

* `hello.pb.h` / `hello.pb.cc` (messages)
* `hello.grpc.pb.h` / `hello.grpc.pb.cc` (service stubs)

---

#### 4. Implement the Server (`server.cpp`)

```cpp
#include <iostream>
#include <memory>
#include <string>

#include <grpcpp/grpcpp.h>
#include "hello.grpc.pb.h"

using grpc::Server;
using grpc::ServerBuilder;
using grpc::ServerContext;
using grpc::Status;
using hello::Greeter;
using hello::HelloRequest;
using hello::HelloReply;

class GreeterServiceImpl final : public Greeter::Service {
    Status SayHello(ServerContext* context, const HelloRequest* request,
                    HelloReply* reply) override {
        std::string prefix("Hello, ");
        reply->set_message(prefix + request->name());
        return Status::OK;
    }
};

void RunServer() {
    std::string server_address("0.0.0.0:50051");
    GreeterServiceImpl service;

    ServerBuilder builder;
    builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
    builder.RegisterService(&service);

    std::unique_ptr<Server> server(builder.BuildAndStart());
    std::cout << "Server listening on " << server_address << std::endl;
    server->Wait();
}

int main(int argc, char** argv) {
    RunServer();
    return 0;
}
```

---

#### 5. Implement the Client (`client.cpp`)

```cpp
#include <iostream>
#include <memory>
#include <string>

#include <grpcpp/grpcpp.h>
#include "hello.grpc.pb.h"

using grpc::Channel;
using grpc::ClientContext;
using grpc::Status;
using hello::Greeter;
using hello::HelloRequest;
using hello::HelloReply;

class GreeterClient {
public:
    GreeterClient(std::shared_ptr<Channel> channel)
        : stub_(Greeter::NewStub(channel)) {}

    std::string SayHello(const std::string& user) {
        HelloRequest request;
        request.set_name(user);

        HelloReply reply;
        ClientContext context;

        Status status = stub_->SayHello(&context, request, &reply);

        if (status.ok()) {
            return reply.message();
        } else {
            return "RPC failed";
        }
    }

private:
    std::unique_ptr<Greeter::Stub> stub_;
};

int main(int argc, char** argv) {
    GreeterClient greeter(grpc::CreateChannel("localhost:50051",
                                              grpc::InsecureChannelCredentials()));
    std::string user("Alice");
    std::string reply = greeter.SayHello(user);
    std::cout << "Greeter received: " << reply << std::endl;
    return 0;
}
```

---

#### 6. Build with CMake (`CMakeLists.txt`)

```cmake
cmake_minimum_required(VERSION 3.5)
project(hello_grpc)

find_package(Protobuf REQUIRED)
find_package(gRPC REQUIRED)

add_executable(server server.cpp hello.pb.cc hello.grpc.pb.cc)
target_link_libraries(server gRPC::grpc++ protobuf::libprotobuf)

add_executable(client client.cpp hello.pb.cc hello.grpc.pb.cc)
target_link_libraries(client gRPC::grpc++ protobuf::libprotobuf)
```

Build:

```bash
mkdir build && cd build
cmake ..
make
```

---

#### 7. Run It

1. Start the server:

   ```bash
   ./server
   ```
2. In another terminal, run the client:

   ```bash
   ./client
   ```

Output:

```
Greeter received: Hello, Alice
```
