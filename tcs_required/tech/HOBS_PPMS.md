HOBS is an end-to-end OSS and BSS system
developed by TCS to support any subscription based system.

The Enterprise Catalogue, aka **Product Portfolio Management System(PPMS)**
is one component of HOBS.

Roadmap : 

TCS HOBS Product Catalogue
Product Config
Price Config
Offerability Config
Release Roll Out
PPM Schema Info

TCS HOBS Product Catalogue

Product Catalogue Management System
Sample Use-case - Product Modelling
How Product Catalogue works
Making changes in Product Catalogue

PPMS has 3 components : 

1. Product Catalogue UI
2. TIBPCServices
3. Spring-Boot Microservices for DB

It is used for product modelling :

1. Initiate Release
2. Create Products
3. Define service and Product Attribs
4. Define Package
5. Define Biling charges
6. Define Offerability
7. Rollout release

Process:

1. Initiate a release
2. Make required changes in Product Catalogue -> This gets saved in Audit Tables
3. Roll Out the release -> Commits to Master table

Product Configuration

1. Creating Products
2. Creating Service Attribs
3. Creating Packages
4. Adding Products to a Package

Create a random product - > Make a Bundle Definition(Bundle Type, Package Category ID,  Package ID, Package Name, Start and End dates, some description, package label)
-> Generay Product Definition(Category, Type, Name, Product Label, Product ID, Start and Ed date, cost range, description)
-> Tag resources in bundle
-> Create Attribute(Attrib name, Allowed Values, Default Values, Group Name, Value Type, Identifier, Type(of data), Group Name)

Price Configuration

2 types 

1. Recurring
2. Non-Recurring

Offerability

Define the conditions for which the plan will be offerable to customers

Parametric based offerabilities. in Offerability section

Rollout Release

Why to create a release
How to rollout a release
Why should we rollout a release
How to clear cache

Release creation is for : 

1. Adding/Modifying should not impact others
2. Adding/Modifying should not incur a down time
3. Only new changes should be deployed
4. Update the master data without impacting pre-existent product catalogue

Clear Ref Values, Service Cache, DAO Cache

TIBTCARE_PPM Schema

1. Master Tables
2. Audit Tables

| Type | Audit tables | Master Tables |
| --- | --- | --- |
| Product | TCARE_PPM_PRODUCT_AUD | TCARE_PPM_PRODUCT |
| Packages/Bundles | TCARE_PPM_PACKAGE_AUD/TCARE_PPM_PCAT_INFO_AUD | TCARE_PPM_PACKAGE/TCARE_PPM_PCAT_INFO |
| Release Info |  | RELASE_ENTITY_INST_MAP |

Product-Package Mapping : 

1. Audit : PPM_PACKAGE_PROD_MAP_AUD
2. Master : TCARE_PPM_PACKAGE_PRODUCT_MAP

Note : add AUD for audit schema for the following sections

Package Creation/Update

1. TCARE_PPM_PACKAGE
2. TCARE_PPM_PRODUCT
3. TCARE_PPM_PCAT_INFO
4. TCARE_PPM_PACKAGE_PRODUCT_MAP

Product Creation : 

1. TCARE_PPM_PRODUCT
2. TCARE_PPM_PCAT_INFO

Package Products : 

1. TCARE_PPM_PACKAGE_PRODUCT_MAP

Product Attributes : 

1. TCARE_PPM_PRODUCT_ATTRIBUTES
2. PPM_PRODUCT_ATRIBUTE_GROUPS

Package Pricing : 

1. TCARE_PPM_PRODUCT_COMPONENTS
2. COMPONENT_DEFINITION
3. BAL_RESOURCE_MAP
4. COMPONENT_BAL_GROUP
5. COMPONENT_BALANCE_MAP
6. COMPONENT_RESOURCE
7. PPM_PRODUCT_COMPONENT_REF_MAP

Package Offerability : 

1. TCARE_PPM_OFFERABILITY_RULE





