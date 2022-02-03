# Contracts Management Project

## Requirement

To maintain a view of the ledger that is currently maintained in Excel sheets.
1. Invoice payment tracking and fast summarization of statuses
2. Alerts for notifying the people invovled, when payment is due
3. Alerts for notifying Finance team about the Invoices Closed.

Each of the points is a deliverable.  
Point 1 is a mandatory deliverable.  
Points 2 and 3 are required good to haves.

## Target Audience

PMO, Delivery Head, ISU Head

PMO to have CRUD access.
Delivery head and ISU head has Read Access.

## Entitites 

1. Account/Entity(Ex : LOIPL, LSIPL)
2. Contract
3. Milestone
4. Projects
5. Users
6. Invoice
7. Payment Advice
8. Alerts(Emails)
9. External Users(Information regarding finance team and )

## Concept

An Invoice has no independent meaning. It's meaning depends on SOW milestones.

Actions for a PMO : 

1. Create the SOW/Contract with information on the invoices(draft)
2. Updates status of Contracts manually
3. Updates the invoice status manually

Deletion almost never happens.

Actions for Sub-ISU head :

1. Checks the status of the Invoices 

Actions for Delivery Head : 

1. Checks the status of the invoices


## Contracts Lifecycle

1. Contract Creation(Draft)
2. Contract Confirmation(Confirmed)
3. TCS Legal Approval(Legal Approved)
4. Business Finance Management Approval(Finance Approved)
5. Signature of BU Head(Sumanta)(TCS Signed)
6. Client signed(Counter signed)

Countersigned copy to be uploaded to CMS

1 contract - multiple milestones

Can have the following statuses :

1. Draft
2. Confirmed
3. Legal approved
4. Finance approved
5. TCS signed
6. Counter signed 

## Milestones Status

This is tracked through Invoice status.
1 milestone - 1 invoice

Invoice statuses : Generated, Submitted, Payment Received, Closed

## Projects status

Projects are made with Change Requests(CR).  
Which are presented in a contract(SOW).  
This can have multiple invoices against it.  
Projects are usually billed against UAT(90% of total) + Production(10%).

### Payment models(Projects)

1. Fixed Bid :  effort estimate + time period + payment against it = contract
2. Per-Person Payment : Monthly Payment * #People = contract. May contain milestones abstracting and dividing this

## Invoice

Generated on SOW creation.
Each Invoice has a billed date and a due date.
Each invoice has a bill to entity.


## Informations Unstructured

Statement of Work(SOW)
CR to the SOW are developed
Project start and end date
Master service agreement is the SOW, aka Contracts.

1 payment advice - multiple invoice
1 project will have 1 contract. CRs are generated against it, which would contain the milestones for the project.

Invoice and Advices

## Reference

1. Sameera Akula(on Contracts Management in TCS for LSIPL/LOIPL walkthrough)