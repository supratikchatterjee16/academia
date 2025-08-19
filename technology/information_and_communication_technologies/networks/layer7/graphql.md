# GraphQL

It is a data query and manipulation language that allows specifying what data is to be retrieved or modified. This is a control/signalling plane technology developed by Facebook in 2012 and open sourced in 2015, and is now maintained by the GraphQL foundation, hosted by the non-profit Linux foundation.

GraphQL is a query language for APIs that lets clients request exactly the data they need. Unlike REST, it avoids over-fetching/under-fetching and exposes a single endpoint.

Core concepts:

1. Operations - Query, Mutation, Subscription
2. Schemas - Define types, queries, mutations, and relationships. Acts as contract between server and client
3. Resolvers - Functions for fetching data for a field
4. Introspection - Ability to query the schema itself via `__schema` and `__type`
5. Fragments
6. Error handling
7. Variables
8. Directives

Implementation concepts:

1. Authentication
2. Batching and Batching utilities(DataLoader)
3. Federation(see Apollo Federation)
4. Subscriptions usage(WebSockets)
5. Query complexity limits using `cost`
6. Union vs Interface
7. Caching
8. Persisted Queries
9. Securing
10. File Uploads(see Apollo Upload Server)

## Operations

1. Query for reading
2. Mutation for modifying(create, delete, update)
3. Subscription for real time updates

