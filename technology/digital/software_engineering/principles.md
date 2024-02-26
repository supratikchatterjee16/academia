# Principles in Software Engineering

## SOLID

Acronym for :

1. Single responsibility : Classes should have a single resposibility
2. Open/Close : Open for extension, closed for modifications
3. Liskov Subsitution : References to base classes should be able to use child classes
4. Interface Segregation : Clients should not be forced to depend on interfaces they do not use
5. Depedency Inversion : High level modules should not depend on low level modules. Abstractions should not depend on details, but details should depend on Abstractions.

## General Responsibilities Assignment Software Pattern(GRASP)

9 key principles :

1. Information Expert : Give responsibility to the class that has the information needed to fulfill
2. Creator : Who is responsible for creating objects. It focuses on the has-a relationship. It creates objects for components it "has" in itself. Example : A car has wheels, engine, seats, and should be responsible for creation of instances
3. Low Coupling : Amount of information known between 2 classes should be minimal to promote re-use and dependency, so as to reduce the scope of changes required
4. High Cohesion : Low Coupling results in High Cohesion. Assigning responsibilities to specific objects, to prevent increase coupling.
5. Controller : Divide work between UI classes and non-UI classes, by creating controllers to redirect the work
6. Polymorphism : 
7. Pure Fabrication : When we have operations that do not belong to any particular object, we create a "fake" class, in order to separate the logic.
8. Indirection : Create intermediary between classes to reduce direct coupling. 
9. Protected Variations : Reduce impact of changes of some object on others, by making use of interfaces.
