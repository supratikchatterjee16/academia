# IFPUG - FPA

How do we estimate using IFPUG?

1. Type of Count
2. Identify Counting Scope and Application Boundary
3. Count Data Function Point
4. Count Trasnaction Function Point
5. Determine Unadjusted Function Point
6. Determine Value Adjustment Factor
7. Calculate Adjusted Function Point Count

## Types of FP count

1. Development Project Count
    - Measures functions provided to user on first installation of product
2. Enhancement Project Count
    - Measures the modifications to the existing application that add, change or delete user functions delivered when the project is complete
    - When an enhancement project is intalled, the application function point count must be updated to reflect changes in the application's functionality
3. Application Count
    - Provides a measure of the current functions the application provides to the user
    - Comonly referred to as the Baseline or Installed Function Point Count
    - Initialized when the development project function point count is completed
    - Updated every time completion of an enhancement project alters the application's functions


## Input Documentation for FP Count

1. Requirements Document
2. Data Flow Diagrams
3. Data Models
4. Entity relationship Diagrams
5. Flow Charts
6. Interface Descriptions
7. Reports Layouts
8. File Layouts
9. Screen Layouts
10. User Manual/Guide
11. Tutorial Documentation

## Data Function

Data Function in FP parlance is the functionality which satisfies the functional user requirements(obtained from customer) to store and/or reference data. Typically, it signifies the contribution of application business data to the overall size of the application.

There are 2 types of Data Functions :

1. Internal Logical File
    - It is a user identifiable group of logicallu related data or control information maintained within the boundary of the application.(Ex : employee Info, Leave Records Information)
2. External Interface file
    - An EIF is a user identifiable group of logically related data or control information refrenced by the application, but maintained outside the boundary of the application.

**Note : Master table containing data that is not changed frequently are not counted as ILF or EIFs.**

### Complexity of Data Functions

2 parameters are utilized for this : 

1. Data Element Type
    - Unique user recognizable non-repeatable field, either maintained in an ILF or retreived from an ILF/EIF.
2. Record Element Type
    - User Recognizable sub-group of data elements within an ILF/EIF

Attributes of a table or file are counted as DETs.  
Subgroup of data wihtin a table/file, which can not exist independently are counted as RETs.  
Default value of a RET is 1.  
Repeated fields(identical in format and meaning) are counted as single DET.  
Fields created for internal calculations are not counted.

Example : 

Employee info table containing : 

1. Name
2. Qualification
3. Email
4. Phone number
5. Dependent Name
6. Dependent DOB
7. Relationship
8. ID

All of the above each are DETs. However, there are 2 RETs.

RET 1 contains : 

1. Name
2. Qualification
3. Email
4. Phone number
5. ID

RET 2 contains : 

1. Dependent Name
2. Dependent DOB
3. Relationship

## Transaction Functions

These are the functionalities that satisfy the functional user requirements to process application data. Transaction functions indicate the contribution of the application features and functionalities in the overall application size.

Important points :

1. It is the smallest unit of activity meaningful to the user.
2. It must be self-contained and leave the business of the application in a consistent state
3. They are of 3 types :
    - External Input,
    - External Output
    - External Query

## ILF/EIF Complexity

|         | DET(1-19) | DET(20-50) | DET(>50) |
| :-----: | :-------: | :--------: | :------: |
| RET 1   | Low       | Low        | Average  |
| RET 2-5 | Low       | Average    | High     |
| RET >5  | Average   | High       | High     |

## EI Complexity Table

|         | DET(1-5)  | DET(6-19)  | DET(>19) |
| :-----: | :-------: | :--------: | :------: |
| FTR 0-1 | Low       | Low        | Average  |
| FTR 2-3 | Low       | Average    | High     |
| FTR >3  | Average   | High       | High     |

## UFP Configuration Table

|         | ILF | EIF | EI | EO | EQ |
| :-----: | :--: | :--: | :--: | :--: | :--: |
| Low     |  7  |  5  |  3 | 4  | 3  |
| Average | 10  |  7  |  4 | 5  | 4  |
| High    | 15  | 10  |  6 | 7  | 6  |



## Adjusted Function Points

AFP is the Final FP count over the UFP. It contains the contribution of the 14 idenfied general system characters(GSC) of the application being counted. Based on the presence/absence of these GSCs, the UFP is multiplies with an adjustment factor(VAF) to obtain AFP. AFP ensure that the impact of certain technicalities impacting the functionalities are considered in the final count. AFP lies withing +35% range of the UFP.

VAF can vary between 0.65(TDI = 14 x 0 = 0) and 1.35(TDI = 14 x 5 = 70).

TDI is total degrees of influence.

Types of GSCs : 

1. Data Communication
2. Distributed Data Processing
3. Performance Objectives
4. Heavily Used Configuration
5. Transaction Rate
6. On-line Data Entry
7. End-User Efficiency
8. On-Line Update
9. Complex Processing
10. Reusability
11. Installation Ease
12. Operational Ease
13. Multiple Sites
14. Facilitate Change

Values they can have :

1. 0 - Not present/No Influence
2. 1 - Incidental influence
3. 2 - Moderate Influence
4. 3 - Average influence
5. 4 - Significant
6. 5 - Strong

TDI = $\sum_{1}^{14}[GSC Values]$

## Process Flow

1. Understand requirements, determine type of count, define system boundaryy, identify elementary processes
2. Identify ILF, EIFs
3. Determine EIF/ILF complexity(based on RET and DET)
4. Determine EI, EO, EQ
5. Determine ILF, EIF complexity(Based on FTR and DET)
6. Calculate UFP using UFP translation table
7. Calculate total UFP
8. Determine TDI of 14 GSCs
9. Calculate adjusted FP

## Development Project Function Point Count

DFP = ADD * AF

ADD is UFP developed for the application, evaluated as they are expected to be at the completion of the project

AF is VAF of the application after the development is completed.

## Enhancement Project function Point Count

EFP = (ADD + CHGa) * AFa + (DELb * AFb)

Here ADD is the same as above.  
CHGa is Functionality Changed A  
AFa is adjustment factor for A  
DELb is deleted functionality B  
ADb is adjustment factor for B

## Application function Point Count

AFP = VAF * [(UFPb + ADD + CHGa) - (CHGb + DEL)]

VAF is Value Adjustment Factor...the meaning of the rest is identifiable.

## Example of Sizing

Given a program of size 500 FP, the following changes are made :

1. Functionality Added = 50 FP
2. Functionality Changed = 24 FP(Originally 20)
3. Functionality deleted = 36 FP

Size of enhancement project :

50 + 24 + 36 = 110 FP

Application size after re-baseline : 

500 + 50 + (24 - 20) - 36 = 518 FP

## Special Notes

**Elementary Process** - A proces that constitutes a complete transaction, meaningful to the user, that is self contained and leaves the business of the application being counted in a consistent state.

**VAF = (TDI * 0.01) + 0.65**

