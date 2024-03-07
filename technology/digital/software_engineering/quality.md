# Quality Models

3 Quality models:

1. McCall's
2. Boehm's
3. GQM

## McCall's Qualty Model

1. Product Operation :
It includes five software quality factors, which are related with the requirements that directly affect the operation of the software such as operational performance, convenience, ease of usage and its correctness. These factors help in providing a better user experience.

    Correctness –
    The extent to which a software meets its requirements specification.
    Efficiency –
    The amount of hardware resources and code the software, needs to perform a function.
    Integrity –
    The extent to which the software can control an unauthorized person from the accessing the data or software.
    Reliability –
    The extent to which a software performs its intended functions without failure.
    Usability –
    The extent of effort required to learn, operate and understand the functions of the software.


2. Product Revision :
It includes three software quality factors, which are required for testing and maintenance of the software. They provide ease of maintenance, flexibility and testing effort to support the software to be functional according to the needs and requirements of the user in the future.

    Maintainability –
    The effort required to detect and correct an error during maintenance phase.
    Flexibility –
    The effort needed to improve an operational software program.
    Testability –
    The effort required to verify a software to ensure that it meets the specified requirements.


3. Product Transition :
It includes three software quality factors, that allows the software to adapt to the change of environments in the new platform or technology from the previous.

    Portability –
    The effort required to transfer a program from one platform to another.
    Re-usability –
    The extent to which the program’s code can be reused in other applications.
    Interoperability –
    The effort required to integrate two systems with one another.
    
## Boehm's Quality Model

The highest level of Boehm’s model has following three primary uses stated as below –

    As is utility –
    Extent to which, we can use software as-is.
    Maintainability –
    Effort required to detect and fix an error during maintenance.
    Portability –
    Effort required to change software to fit in a new environment.

The next level of Boehm’s hierarchical model consists of seven quality factors associated with three primary uses, stated as below –

    Portability –
    Effort required to change software to fit in a new environment.
    Reliability –
    Extent to which software performs according to requirements.
    Efficiency –
    Amount of hardware resources and code required to execute a function.
    Usability (Human Engineering) –
    Extent of effort required to learn, operate and understand functions of the software.
    Testability –
    Effort required to verify that software performs its intended functions.
    Understandability –
    Effort required for a user to recognize logical concept and its applicability.
    Modifiability –
    Effort required to modify a software during maintenance phase.

Boehm further classified characteristics into Primitive constructs as follows- device independence, accuracy, completeness, consistency, device efficiency, accessibility, communicativeness, self-descriptiveness, legibility, structuredness, conciseness, augment-ability. For example- Testability is broken down into:- accessibility, communicativeness, structuredness and self descriptiveness.

Advantages :

    It focuses and tries to satisfy the needs of the user.
    It focuses on software maintenance cost effectiveness.

Disadvantages :

    It doesn’t suggest, how to measure the quality characteristics.
    It is difficult to evaluate the quality of software using the top-down approach.

## GQM Method

The Goal/Question/Metric (GQM) method is a proven technique used for goal oriented measures. It consists of the following 3 basis elements:

    Goal
    Question
    Metric

In GQM method, measurement is goal-oriented. firstly, the goals need to be described clearly so that it can be measured during the software development.

In this method goals are defined which transforms into questions and metrics. Then the questions are answered and it is checked whether these answers satisfy goals or not. Hence, this method follows a top-down approach through division of goals and then mapping of goals into questions and then these questions are transformed into metrics, and method also follows bottom-up approach by analyzing measurement and checking whether goals are satisfied or not.



Steps in GQM Method

    Goals are defined and described clearly.
    Conversion of goals into appropriate questions.
    Questions are transformed into mertics.


Phases of GQM Method :

    Planning:
    In the first phase, Project plan is prepared by identifying the basic requirements.
    Definition:
    In the second phase Description of goals, question and metric takes place.These three are clearly defined.
    Data collection:
    In this phase, collection of actual data takes place.
    Interpretation:
    It is the final phase in which answers to the questions asked in previous phases are provided and the goal’s achievement is verified.

## Code Optimization

Categorized into : 

1. Platform Independent
    - using loop rolling
    - reducing function calls 
    - using memory efficient routines
    - reducing the number of conditions
2. Patform Dependent
    - Instructional level parallelism
    - Data level parallelism
    - Cache Optimization techniques

Compiler based optimization. Good compilers do the following : 

1. Data Alignment
2. Proper Loop Nesting
3. Procedure Inlining
4. Loop Unrolling
5. Loop Blocking(Tiling)
6. Local Optimization

**Note** : Loop Unrolling is bringing out looping statements to prevent conditional checks if unrequired.

Trade off : Caching data can increase performance, but it increases the memory consumption.

Fixing bottlenecks can be achieved by leveraging the Pareto Priciple and the 90/10 rule.

Pareto Principle : 80% of issues, problems or effects are produced by 20% of causes or defects.  
90/10 law : 90% of execution time is taken for executing 10% of the code.

## Software Quality Tools

There are 4 categories :

1. Software Quality Tools for developers
2. Software Quality tools for general overview
3. Static Program Assessment Tool
4. Dynamic Program Analysis Tools

They cover 7 categories of code quality :

1. Duplicated Codes
2. Coding Standards
3. Unit Tests
4. Complex Code
5. potantial Bugs
6. Comments
7. Design and Architecture

Some tools in the market :

### SAP Code quality tools

1. Accenture Code Review Tool for SAP
2. Quality Inspector for SAP
3. Accenture Security  Workbench for SAP

### Java Code Quality Tools

1. Sonar
2. checkstyle
3. PMD
4. FindBugs
5. JDepend
6. Architecture Rules

### Microsoft .NET Quality Tools

1. MS Visual Studio - Static Code Analysis

### Oracle PL/SQL quality tools

1. PL/SQL Code review tool(Accenture Oracle e-Business suite automation)
2. Sonar
3. Toad CodeXPert

### Mainframe COBOL quality tools

1. Standalone development environment
2. Downsizing Development Environment
3. IBM Rational Asset Analyzer

## Review Process

1. Plan for a review
2. Prepare for a review 
3. Conduct a review
4. Resolve review points
5. Validate resolutions
6. Baseline a software work product

## Testing Metrics

1. Defect Desity : $$Number of confirmed defects(in a specific testing phase) / Size of component(in terms of man-days, functional points or LOC)$$
2. Defect Injection rate : $$Number of injected defects in a specific amount of time.$$
3. Defect removal efficiency : $$Number of defects found in internal tests * 100 / Total number of defect$$

## Code Quality Metrics

The following are required coding quality measures :

1. Duplicated Code Identification
2. Coding Standards
3. Automated Test Units
4. Complexity
5. Comments
6. Design and Architecture

