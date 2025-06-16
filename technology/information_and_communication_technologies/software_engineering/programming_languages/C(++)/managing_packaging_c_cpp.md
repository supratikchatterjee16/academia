# Packaging C/C++ codebases

Attempting to develop an efficient protocol library, the code had to be structrured and atomized for transfer and delivery.
During this, the a lot of issues were encountered. To avoid said problem, the following are some key points : 

1. Header files are for the compiler
2. Object files are for the linker
3. Header files need to maintain definitions when developing member functions with templates
4. The cpp file should import it's own header at the very last
5. ```gcc -c``` compiles it and prevents linking
6. ```gcc -lstdc++``` allows compilation of C++ files
7. Maintain a ```.cpp``` and ```.h``` file for each exposed unit.


The actual structure and scoping is present in the header file. The logic, which would not affect the memory size in the calling scope, needs to be shifted to the ```.cpp```/```.c``` file.

Use a ```Makefile``` in order to smooth out the compilation process. This is especially useful when rapid compilation and subsequent
auto-deployment of embedded code to micro-controllers.

## Sample Makefile

We have a directory called ```protos``` and ```components```.
These need to compiled in a specific order, and the generated objects need to be siphoned cleanly off to a 'build' directory.

The following options are required : 

1. ```make``` makes the main logic
2. ```make all``` recompiles all related files
3. ```make run``` for quick compile and execution

The following recipes are created : 

1. ```main```
2. ```all```
3. ```build_dir```
4. ```components```
5. ```protos```
6. ```run```

The logic for it is : 

```make
BIN_NAME := ws
COMPILER ?= gcc
COMPILE_FLAGS = -lstdc++ -pthread -lssl -lcrypto

SRC_DIR = ./src
SRC = $(SRC_DIR)/main.cpp
DEST = ./build

main :
	$(COMPILER) -o $(DEST)/$(BIN_NAME).o  -c $(SRC) $(COMPILE_FLAGS)
	@echo
	$(COMPILER) -o $(DEST)/$(BIN_NAME) $(SRC) $(DEST)/protos/*.o $(DEST)/components/*.o $(COMPILE_FLAGS)
	@echo

all : build_dir components protos main

build_dir :
	mkdir -p $(DEST)

components :
	mkdir -p $(DEST)/components
	$(COMPILER) -c $(SRC_DIR)/components/server.cpp -o $(DEST)/components/server.o $(COMPILE_FLAGS)
	@echo

protos :
	mkdir -p $(DEST)/protos
	$(COMPILER) -c $(SRC_DIR)/protos/base.cpp -o $(DEST)/protos/base.o $(COMPILE_FLAGS)
	$(COMPILER) -c $(SRC_DIR)/protos/http.cpp -o $(DEST)/protos/http.o $(COMPILE_FLAGS)
	$(COMPILER) -c $(SRC_DIR)/protos/ws.cpp -o $(DEST)/protos/ws.o $(COMPILE_FLAGS)
	@echo

run : main
	$(DEST)/$(BIN_NAME)
```

The tree for the source.
No auto invocation done, as the names need to be maintained.

```
src
├── arguments.cpp
├── code.cpp
├── components
│   ├── server.cpp
│   └── server.h
├── configs.cpp
├── crypt.cpp
├── main.cpp
├── main.cpp.bak
└── protos
    ├── base.cpp
    ├── base.h
    ├── http.cpp
    ├── http.h
    ├── ws.cpp
    └── ws.h
```