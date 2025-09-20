# MongoDB Interview Questions

This document contains comprehensive MongoDB interview questions for senior full stack engineers working in cross-team, event-driven, distributed, and microservices architectures. Questions are organized from basic to advanced levels, including scenario-based questions.

## 1. Basic MongoDB Concepts

1. What is MongoDB and how does it differ from traditional relational databases?
2. Explain the concept of documents in MongoDB. How do they compare to rows in SQL?
3. What is a collection in MongoDB? How does it relate to tables in RDBMS?
4. Describe the structure of a MongoDB database. What are the key components?
5. What is BSON and why does MongoDB use it instead of JSON?
6. Explain the concept of embedded documents and references in MongoDB.
7. What are the advantages of MongoDB's schema-less design?
8. How does MongoDB handle data types? List some common BSON data types.
9. What is the ObjectId in MongoDB? How is it generated?
10. Explain the difference between MongoDB and other NoSQL databases like Cassandra or Redis.
11. What is the maximum size of a MongoDB document?
12. How does MongoDB handle large documents or files?
13. Explain the concept of capped collections in MongoDB.
14. What are database references ($ref) in MongoDB?
15. How does MongoDB ensure data consistency in a distributed environment?
16. What is the role of the MongoDB shell (mongosh)?
17. Explain the difference between MongoDB Atlas and self-hosted MongoDB.
18. What are the system collections in MongoDB?
19. How does MongoDB handle time-to-live (TTL) indexes?
20. What is the purpose of the MongoDB profiler?

### Answers for Basic MongoDB Concepts

1. **What is MongoDB and how does it differ from traditional relational databases?**  
   MongoDB is a NoSQL document database that stores data in flexible, JSON-like documents. Unlike traditional relational databases (RDBMS) that use tables with fixed schemas and SQL for queries, MongoDB uses collections of documents with dynamic schemas and a query language based on JavaScript-like syntax.  
   *Example:* In RDBMS, you'd have separate tables for users and orders with foreign keys. In MongoDB, you can embed orders directly within user documents:  
   ```json
   {
     "_id": ObjectId("507f1f77bcf86cd799439011"),
     "name": "John Doe",
     "email": "john@example.com",
     "orders": [
       {"product": "Laptop", "price": 1200, "date": "2023-01-15"},
       {"product": "Mouse", "price": 25, "date": "2023-01-20"}
     ]
   }
   ```

2. **Explain the concept of documents in MongoDB. How do they compare to rows in SQL?**  
   Documents in MongoDB are the basic unit of data, similar to rows in SQL tables, but they are JSON-like objects with key-value pairs. Unlike SQL rows with fixed columns, MongoDB documents can have different fields and structures within the same collection.  
   *Example:* A user document:  
   ```json
   {
     "_id": ObjectId("507f1f77bcf86cd799439011"),
     "name": "Alice",
     "age": 30,
     "address": {"street": "123 Main St", "city": "NYC"},
     "hobbies": ["reading", "coding"]
   }
   ```

3. **What is a collection in MongoDB? How does it relate to tables in RDBMS?**  
   A collection is a group of MongoDB documents, similar to a table in RDBMS. However, collections don't enforce a schema, allowing documents with different structures.  
   *Example:* `users` collection containing user documents.

4. **Describe the structure of a MongoDB database. What are the key components?**  
   A MongoDB database contains collections, which contain documents. Key components include: databases, collections, documents, indexes, and views. Multiple databases can exist on a single MongoDB server.

5. **What is BSON and why does MongoDB use it instead of JSON?**  
   BSON (Binary JSON) is a binary-encoded serialization of JSON-like documents. MongoDB uses BSON because it's more efficient for storage and traversal, supports additional data types (like ObjectId, Date), and is faster to encode/decode than JSON.

6. **Explain the concept of embedded documents and references in MongoDB.**  
   Embedded documents store related data within a single document, while references store relationships using ObjectIds pointing to other documents. Embedding is preferred for one-to-one or one-to-many relationships with small, frequently accessed data.  
   *Example - Embedded:*  
   ```json
   {
     "user": {
       "name": "John",
       "address": {"street": "123 Main St", "city": "NYC"}
     }
   }
   ```
   *Example - Reference:*  
   ```json
   {
     "user_id": ObjectId("507f1f77bcf86cd799439011"),
     "address_id": ObjectId("507f1f77bcf86cd799439012")
   }
   ```

7. **What are the advantages of MongoDB's schema-less design?**  
   - Flexibility to add fields without schema changes
   - Faster development and iteration
   - Better handling of polymorphic data
   - Easier data migration

8. **How does MongoDB handle data types? List some common BSON data types.**  
   MongoDB supports various BSON data types including: String, Integer, Double, Boolean, Date, ObjectId, Array, Object, Null, Binary data, Regular expression, JavaScript code.

9. **What is the ObjectId in MongoDB? How is it generated?**  
   ObjectId is a 12-byte BSON type used as the default primary key. It's generated using: 4 bytes timestamp, 5 bytes random value, 3 bytes incrementing counter.  
   *Example:* `ObjectId("507f1f77bcf86cd799439011")`

10. **Explain the difference between MongoDB and other NoSQL databases like Cassandra or Redis.**  
    MongoDB is a document database for flexible schemas and complex queries. Cassandra is a wide-column store optimized for high write throughput and linear scalability. Redis is an in-memory data structure store for caching and fast data access.

11. **What is the maximum size of a MongoDB document?**  
    16 MB per document. For larger data, use GridFS for file storage.

12. **How does MongoDB handle large documents or files?**  
    For files larger than 16MB, MongoDB uses GridFS, which splits files into chunks stored as separate documents.

13. **Explain the concept of capped collections in MongoDB.**  
    Capped collections are fixed-size collections that maintain insertion order and automatically remove oldest documents when the size limit is reached. They're useful for logging and caching.

14. **What are database references ($ref) in MongoDB?**  
    Database references are a convention for storing references to documents in other collections, using $ref, $id, and optionally $db fields.

15. **How does MongoDB ensure data consistency in a distributed environment?**  
    Through replication (replica sets) and sharding, with configurable write concerns and read preferences to balance consistency and performance.

16. **What is the role of the MongoDB shell (mongosh)?**  
    mongosh is the interactive JavaScript shell for MongoDB, used for administration, querying, and scripting database operations.

17. **Explain the difference between MongoDB Atlas and self-hosted MongoDB.**  
    MongoDB Atlas is a cloud-hosted database service with automated management, scaling, and security. Self-hosted MongoDB requires manual server management and configuration.

18. **What are the system collections in MongoDB?**  
    System collections store metadata and configuration, prefixed with `system.`, like `system.users`, `system.roles`, `system.js`.

19. **How does MongoDB handle time-to-live (TTL) indexes?**  
    TTL indexes automatically remove documents after a specified time period, useful for expiring data like session information.

20. **What is the purpose of the MongoDB profiler?**  
    The profiler captures and logs slow queries and operations, helping identify performance bottlenecks and optimization opportunities.

## 2. CRUD Operations

21. Explain the basic CRUD operations in MongoDB.
22. What is the difference between insertOne() and insertMany()?
23. How do you perform conditional queries using find()?
24. Explain the use of projection in MongoDB queries.
25. What are the different update operators in MongoDB ($set, $inc, $push, etc.)?
26. How does updateOne() differ from updateMany()?
27. Explain the difference between replaceOne() and updateOne().
28. What is the purpose of the upsert option in update operations?
29. How do you delete documents using deleteOne() and deleteMany()?
30. Explain the use of $unset operator in MongoDB.
31. How do you perform array operations like $push and $pull?
32. What is the difference between $addToSet and $push?
33. Explain the use of positional operator ($) in updates.
34. How do you perform bulk write operations in MongoDB?
35. What are the options available for find() method?

### Answers for CRUD Operations

21. **Explain the basic CRUD operations in MongoDB.**  
   CRUD stands for Create, Read, Update, Delete. In MongoDB:  
   - Create: `insertOne()`, `insertMany()`  
   - Read: `find()`, `findOne()`  
   - Update: `updateOne()`, `updateMany()`, `replaceOne()`  
   - Delete: `deleteOne()`, `deleteMany()`

22. **What is the difference between insertOne() and insertMany()?**  
   `insertOne()` inserts a single document, while `insertMany()` inserts multiple documents in a single operation.  
   *Example:*  
   ```javascript
   // insertOne
   db.users.insertOne({name: "John", age: 30})
   
   // insertMany
   db.users.insertMany([
     {name: "John", age: 30},
     {name: "Jane", age: 25}
   ])
   ```

23. **How do you perform conditional queries using find()?**  
   Use query operators in the find() method's first parameter.  
   *Example:*  
   ```javascript
   // Find users older than 25
   db.users.find({age: {$gt: 25}})
   
   // Find users with specific name
   db.users.find({name: "John"})
   ```

24. **Explain the use of projection in MongoDB queries.**  
   Projection specifies which fields to return in query results, improving performance by reducing data transfer.  
   *Example:*  
   ```javascript
   // Return only name and age fields
   db.users.find({}, {name: 1, age: 1, _id: 0})
   ```

25. **What are the different update operators in MongoDB ($set, $inc, $push, etc.)?**  
   Common update operators:  
   - `$set`: Sets field value  
   - `$inc`: Increments numeric value  
   - `$push`: Adds element to array  
   - `$pull`: Removes element from array  
   - `$unset`: Removes field  
   - `$addToSet`: Adds unique element to array

26. **How does updateOne() differ from updateMany()?**  
   `updateOne()` updates the first matching document, while `updateMany()` updates all matching documents.  
   *Example:*  
   ```javascript
   // Update first user named John
   db.users.updateOne({name: "John"}, {$set: {age: 31}})
   
   // Update all users named John
   db.users.updateMany({name: "John"}, {$set: {age: 31}})
   ```

27. **Explain the difference between replaceOne() and updateOne().**  
   `replaceOne()` replaces the entire document (except _id), while `updateOne()` modifies specific fields using update operators.  
   *Example:*  
   ```javascript
   // Replace entire document
   db.users.replaceOne({name: "John"}, {name: "John", age: 31, city: "NYC"})
   
   // Update specific fields
   db.users.updateOne({name: "John"}, {$set: {age: 31}})
   ```

28. **What is the purpose of the upsert option in update operations?**  
   Upsert (update + insert) creates a new document if no document matches the query filter.  
   *Example:*  
   ```javascript
   db.users.updateOne(
     {name: "John"},
     {$set: {age: 30}},
     {upsert: true}
   )
   ```

29. **How do you delete documents using deleteOne() and deleteMany()?**  
   `deleteOne()` deletes the first matching document, `deleteMany()` deletes all matching documents.  
   *Example:*  
   ```javascript
   // Delete one user
   db.users.deleteOne({name: "John"})
   
   // Delete all users older than 65
   db.users.deleteMany({age: {$gt: 65}})
   ```

30. **Explain the use of $unset operator in MongoDB.**  
   `$unset` removes a field from a document.  
   *Example:*  
   ```javascript
   db.users.updateOne({name: "John"}, {$unset: {temporaryField: 1}})
   ```

31. **How do you perform array operations like $push and $pull?**  
   `$push` adds elements to an array, `$pull` removes elements from an array.  
   *Example:*  
   ```javascript
   // Add hobby
   db.users.updateOne({name: "John"}, {$push: {hobbies: "reading"}})
   
   // Remove hobby
   db.users.updateOne({name: "John"}, {$pull: {hobbies: "reading"}})
   ```

32. **What is the difference between $addToSet and $push?**  
   `$addToSet` only adds elements that don't already exist in the array (prevents duplicates), while `$push` always adds elements.  
   *Example:*  
   ```javascript
   // Won't add duplicate
   db.users.updateOne({name: "John"}, {$addToSet: {hobbies: "reading"}})
   ```

33. **Explain the use of positional operator ($) in updates.**  
   The positional operator `$` updates the first element that matches the query condition in an array.  
   *Example:*  
   ```javascript
   // Update first score greater than 80
   db.students.updateOne(
     {name: "John", scores: {$gt: 80}},
     {$set: {"scores.$": 85}}
   )
   ```

34. **How do you perform bulk write operations in MongoDB?**  
   Use `bulkWrite()` method to perform multiple write operations in a single request.  
   *Example:*  
   ```javascript
   db.users.bulkWrite([
     {insertOne: {document: {name: "John", age: 30}}},
     {updateOne: {filter: {name: "Jane"}, update: {$set: {age: 31}}}},
     {deleteOne: {filter: {name: "Bob"}}}
   ])
   ```

35. **What are the options available for find() method?**  
   Common options include: limit, skip, sort, projection, and various cursor methods like count(), toArray(), forEach().

## 3. Indexing

36. What is an index in MongoDB and why is it important?
37. How do you create a single field index in MongoDB?
38. Explain compound indexes and their use cases.
39. What are the different types of indexes available in MongoDB?
40. How does a text index work in MongoDB?
41. Explain the concept of unique indexes.
42. What is a sparse index and when would you use it?
43. How do you create a geospatial index?
44. Explain the difference between foreground and background index creation.
45. What is index intersection in MongoDB?
46. How do you drop an index in MongoDB?
47. Explain the use of partial indexes.
48. What are TTL indexes and how do they work?
49. How do you analyze index usage with explain()?
50. What is the impact of indexes on write operations?

### Answers for Indexing

36. **What is an index in MongoDB and why is it important?**  
   An index is a data structure that improves query performance by allowing MongoDB to quickly locate documents. It's important for efficient queries, especially on large collections.

37. **How do you create a single field index in MongoDB?**  
   Use `createIndex()` method with the field name.  
   *Example:*  
   ```javascript
   db.users.createIndex({age: 1})  // Ascending index on age
   ```

38. **Explain compound indexes and their use cases.**  
   Compound indexes include multiple fields. They're useful for queries that filter on multiple fields.  
   *Example:*  
   ```javascript
   db.users.createIndex({age: 1, name: 1})
   ```

39. **What are the different types of indexes available in MongoDB?**  
   - Single field indexes  
   - Compound indexes  
   - Multikey indexes (for arrays)  
   - Text indexes  
   - Geospatial indexes  
   - Hashed indexes  
   - Unique indexes  
   - Sparse indexes  
   - Partial indexes

40. **How does a text index work in MongoDB?**  
   Text indexes support text search queries on string content, allowing for full-text search capabilities.  
   *Example:*  
   ```javascript
   db.articles.createIndex({content: "text"})
   db.articles.find({$text: {$search: "mongodb"}})
   ```

41. **Explain the concept of unique indexes.**  
   Unique indexes ensure that the indexed field(s) contain unique values across all documents in the collection.  
   *Example:*  
   ```javascript
   db.users.createIndex({email: 1}, {unique: true})
   ```

42. **What is a sparse index and when would you use it?**  
   Sparse indexes only include documents that contain the indexed field, saving space. Use when many documents don't have the indexed field.  
   *Example:*  
   ```javascript
   db.users.createIndex({phone: 1}, {sparse: true})
   ```

43. **How do you create a geospatial index?**  
   Use 2dsphere for GeoJSON data or 2d for legacy coordinate pairs.  
   *Example:*  
   ```javascript
   db.places.createIndex({location: "2dsphere"})
   ```

44. **Explain the difference between foreground and background index creation.**  
   Foreground index creation blocks all other operations on the database, while background index creation allows other operations to continue but takes longer.

45. **What is index intersection in MongoDB?**  
   Index intersection allows MongoDB to use multiple single-field indexes to satisfy a query, combining their benefits without requiring a compound index.

46. **How do you drop an index in MongoDB?**  
   Use `dropIndex()` method.  
   *Example:*  
   ```javascript
   db.users.dropIndex({age: 1})
   ```

47. **Explain the use of partial indexes.**  
   Partial indexes only index documents that match a specified filter expression, reducing index size and improving performance.  
   *Example:*  
   ```javascript
   db.users.createIndex(
     {age: 1},
     {partialFilterExpression: {age: {$gte: 18}}}
   )
   ```

48. **What are TTL indexes and how do they work?**  
   TTL (Time-To-Live) indexes automatically remove documents after a specified time period.  
   *Example:*  
   ```javascript
   db.sessions.createIndex(
     {createdAt: 1},
     {expireAfterSeconds: 3600}
   )
   ```

49. **How do you analyze index usage with explain()?**  
   The `explain()` method shows how MongoDB executes a query, including which indexes are used.  
   *Example:*  
   ```javascript
   db.users.find({age: {$gt: 25}}).explain("executionStats")
   ```

50. **What is the impact of indexes on write operations?**  
   Indexes improve read performance but slow down write operations because MongoDB must update indexes when documents are inserted, updated, or deleted. More indexes = slower writes.

## 4. Aggregation Framework

51. What is the MongoDB Aggregation Framework?
52. Explain the concept of aggregation pipelines.
53. What are the different stages in an aggregation pipeline?
54. How does $match stage work in aggregation?
55. Explain the use of $group stage and its operators.
56. What is the difference between $project and $addFields?
57. How do you perform joins using $lookup?
58. Explain the use of $unwind for array fields.
59. What are accumulator operators in $group stage?
60. How do you handle pagination in aggregation pipelines?
61. Explain the use of $facet for multiple aggregations.
62. What is the difference between find() and aggregate()?
63. How do you optimize aggregation pipelines?
64. Explain the use of $merge and $out stages.
65. What are the limitations of aggregation pipelines?

### Answers for Aggregation Framework

51. **What is the MongoDB Aggregation Framework?**  
   The Aggregation Framework is a powerful feature for data analysis and transformation, using pipelines of stages to process documents and return computed results.

52. **Explain the concept of aggregation pipelines.**  
   Aggregation pipelines are sequences of stages that process documents through multiple transformations, similar to a data processing pipeline.  
   *Example:*  
   ```javascript
   db.orders.aggregate([
     {$match: {status: "completed"}},
     {$group: {_id: "$customerId", total: {$sum: "$amount"}}},
     {$sort: {total: -1}}
   ])
   ```

53. **What are the different stages in an aggregation pipeline?**  
   Common stages: $match, $group, $project, $sort, $limit, $skip, $lookup, $unwind, $addFields, $facet, $merge, $out.

54. **How does $match stage work in aggregation?**  
   `$match` filters documents, similar to find() but used within aggregation pipelines. It should be placed early for performance.  
   *Example:*  
   ```javascript
   {$match: {status: "active", age: {$gte: 18}}}
   ```

55. **Explain the use of $group stage and its operators.**  
   `$group` groups documents by a specified expression and applies accumulator operators.  
   *Example:*  
   ```javascript
   {
     $group: {
       _id: "$category",
       count: {$sum: 1},
       avgPrice: {$avg: "$price"},
       maxPrice: {$max: "$price"}
     }
   }
   ```

56. **What is the difference between $project and $addFields?**  
   `$project` can include/exclude fields and reshape documents, while `$addFields` only adds new fields without removing existing ones.  
   *Example:*  
   ```javascript
   // $project
   {$project: {name: 1, age: 1, _id: 0}}
   
   // $addFields
   {$addFields: {fullName: {$concat: ["$firstName", " ", "$lastName"]}}}
   ```

57. **How do you perform joins using $lookup?**  
   `$lookup` performs left outer joins between collections.  
   *Example:*  
   ```javascript
   {
     $lookup: {
       from: "orders",
       localField: "userId",
       foreignField: "userId",
       as: "userOrders"
     }
   }
   ```

58. **Explain the use of $unwind for array fields.**  
   `$unwind` deconstructs an array field from input documents, creating a separate document for each array element.  
   *Example:*  
   ```javascript
   {$unwind: "$tags"}  // Creates separate doc for each tag
   ```

59. **What are accumulator operators in $group stage?**  
   Accumulator operators: $sum, $avg, $min, $max, $first, $last, $push, $addToSet, $stdDevPop, $stdDevSamp.

60. **How do you handle pagination in aggregation pipelines?**  
   Use `$skip` and `$limit` stages.  
   *Example:*  
   ```javascript
   [
     {$sort: {createdAt: -1}},
     {$skip: 20},
     {$limit: 10}
   ]
   ```

61. **Explain the use of $facet for multiple aggregations.**  
   `$facet` allows running multiple aggregation pipelines on the same input documents.  
   *Example:*  
   ```javascript
   {
     $facet: {
       "categorizedByTags": [
         {$unwind: "$tags"},
         {$sortByCount: "$tags"}
       ],
       "categorizedByPrice": [
         {$bucket: {groupBy: "$price", boundaries: [0, 50, 100]}}
       ],
       "brands": [{$sortByCount: "$brand"}]
     }
   }
   ```

62. **What is the difference between find() and aggregate()?**  
   `find()` is for simple queries and projections, while `aggregate()` is for complex data processing and transformations using pipelines.

63. **How do you optimize aggregation pipelines?**  
   - Place `$match` early to reduce documents  
   - Use indexes for `$match` and `$sort`  
   - Avoid unnecessary `$project` stages  
   - Use `$limit` early when possible  
   - Consider using views for frequently used pipelines

64. **Explain the use of $merge and $out stages.**  
   `$out` writes aggregation results to a new collection, `$merge` merges results into an existing collection with options for handling conflicts.  
   *Example:*  
   ```javascript
   {$merge: {into: "monthlyReports", on: "_id", whenMatched: "replace"}}
   ```

65. **What are the limitations of aggregation pipelines?**  
   - 16 MB result size limit  
   - Memory restrictions for sorting and grouping  
   - Cannot create/drop collections or indexes  
   - Read concern "snapshot" not supported  
   - Limited to 1000 operations per transaction

## 5. Replication

66. What is replication in MongoDB and why is it important?
67. Explain the concept of replica sets.
68. What are the roles of primary and secondary nodes in a replica set?
69. How does automatic failover work in MongoDB replica sets?
70. What is the oplog and how does it work?
71. Explain read preferences in MongoDB.
72. How do you configure a replica set?
73. What is an arbiter in MongoDB replication?
74. Explain the concept of write concern in replication.
75. How does MongoDB handle network partitions in replica sets?

### Answers for Replication

66. **What is replication in MongoDB and why is it important?**  
   Replication is the process of synchronizing data across multiple MongoDB servers. It's important for high availability, data redundancy, and disaster recovery.

67. **Explain the concept of replica sets.**  
   A replica set is a group of MongoDB servers that maintain the same data set, consisting of one primary node and multiple secondary nodes that replicate the primary's oplog.

68. **What are the roles of primary and secondary nodes in a replica set?**  
   - Primary: Accepts all write operations and records them in the oplog  
   - Secondary: Replicate data from primary, can serve read operations (depending on read preference)

69. **How does automatic failover work in MongoDB replica sets?**  
   When the primary becomes unavailable, an election process selects a new primary from the secondaries based on priority and recency of data.

70. **What is the oplog and how does it work?**  
   The oplog (operations log) is a capped collection that stores all write operations performed on the primary. Secondaries read from the oplog to replicate changes.

71. **Explain read preferences in MongoDB.**  
   Read preferences determine which replica set member to read from: primary (default), primaryPreferred, secondary, secondaryPreferred, nearest.  
   *Example:*  
   ```javascript
   db.collection.find().readPref("secondaryPreferred")
   ```

72. **How do you configure a replica set?**  
   Use `rs.initiate()` command with configuration document specifying members, or use `rs.add()` to add members to existing set.  
   *Example:*  
   ```javascript
   rs.initiate({
     _id: "myReplicaSet",
     members: [
       {_id: 0, host: "mongodb0.example.net:27017"},
       {_id: 1, host: "mongodb1.example.net:27017"}
     ]
   })
   ```

73. **What is an arbiter in MongoDB replication?**  
   An arbiter is a lightweight member that participates in elections but doesn't store data. Used to break ties in elections with even number of voting members.

74. **Explain the concept of write concern in replication.**  
   Write concern determines how many replica set members must acknowledge a write operation before it's considered successful.  
   *Example:*  
   ```javascript
   db.collection.insertOne(
     {name: "John"},
     {writeConcern: {w: "majority", wtimeout: 5000}}
   )
   ```

75. **How does MongoDB handle network partitions in replica sets?**  
   During network partitions, MongoDB uses its election protocol to maintain consistency. The majority side of the partition will elect a primary, while the minority side becomes read-only.

## 6. Sharding

76. What is sharding in MongoDB?
77. Explain the components of a sharded cluster.
78. What is a shard key and how do you choose one?
79. Explain the concept of chunks in MongoDB sharding.
80. What is the role of the balancer in sharding?
81. How does MongoDB handle distributed queries?
82. Explain the difference between ranged and hashed sharding.
83. What are the limitations of shard keys?
84. How do you add shards to a cluster?
85. Explain the concept of zones in MongoDB sharding.

### Answers for Sharding

76. **What is sharding in MongoDB?**  
   Sharding is MongoDB's method of distributing data across multiple machines to support deployments with very large data sets and high throughput operations.

77. **Explain the components of a sharded cluster.**  
   A sharded cluster consists of:  
   - Shard servers: Store data chunks  
   - Config servers: Store cluster metadata  
   - Mongos routers: Route queries to appropriate shards

78. **What is a shard key and how do you choose one?**  
   A shard key is an indexed field used to distribute documents across shards. Choose based on query patterns, cardinality, and write distribution.  
   *Example:*  
   ```javascript
   sh.shardCollection("database.collection", {"userId": 1})
   ```

79. **Explain the concept of chunks in MongoDB sharding.**  
   Chunks are contiguous ranges of shard key values. MongoDB automatically splits chunks when they exceed the maximum size and migrates them between shards.

80. **What is the role of the balancer in sharding?**  
   The balancer ensures even distribution of chunks across shards by automatically migrating chunks from overloaded to underloaded shards.

81. **How does MongoDB handle distributed queries?**  
   Mongos routers determine which shards contain the required data and coordinate query execution across multiple shards, then merge results.

82. **Explain the difference between ranged and hashed sharding.**  
   - Ranged sharding: Documents with close shard key values are likely to be on the same shard  
   - Hashed sharding: Documents are distributed randomly using a hash function, providing better write distribution

83. **What are the limitations of shard keys?**  
   - Cannot change shard key values after insertion  
   - Shard key fields cannot be arrays  
   - Updates to shard key require entire document replacement  
   - Some queries may require broadcasting to all shards

84. **How do you add shards to a cluster?**  
   Use `sh.addShard()` command to add new shard servers to the cluster.  
   *Example:*  
   ```javascript
   sh.addShard("shard02/mongodb0.example.net:27017")
   ```

85. **Explain the concept of zones in MongoDB sharding.**  
   Zones allow pinning data to specific shards based on shard key ranges, useful for geographic data distribution or hardware isolation.  
   *Example:*  
   ```javascript
   sh.addShardToZone("shard01", "US-West")
   sh.updateZoneKeyRange("database.collection", 
     {country: "US", state: "CA"}, 
     {country: "US", state: "CA"}, 
     "US-West")
   ```

## 7. Transactions and Concurrency

86. Does MongoDB support ACID transactions?
87. Explain multi-document transactions in MongoDB.
88. What are the limitations of transactions in MongoDB?
89. How does MongoDB handle concurrency?
90. Explain the concept of write locks in MongoDB.
91. What is optimistic concurrency control?
92. How do you handle transaction timeouts?
93. Explain the use of session in MongoDB transactions.
94. What is the difference between local and global transactions?
95. How do transactions work with sharding?

### Answers for Transactions and Concurrency

86. **Does MongoDB support ACID transactions?**  
   Yes, MongoDB supports multi-document ACID transactions since version 4.0, providing atomicity, consistency, isolation, and durability across multiple documents and collections.

87. **Explain multi-document transactions in MongoDB.**  
   Multi-document transactions allow multiple document changes to be treated as a single atomic operation, ensuring all changes succeed or all are rolled back.  
   *Example:*  
   ```javascript
   const session = db.getMongo().startSession();
   session.startTransaction();
   try {
     db.accounts.updateOne(
       {name: "Alice"}, 
       {$inc: {balance: -100}}, 
       {session}
     );
     db.accounts.updateOne(
       {name: "Bob"}, 
       {$inc: {balance: 100}}, 
       {session}
     );
     session.commitTransaction();
   } catch (error) {
     session.abortTransaction();
   }
   ```

88. **What are the limitations of transactions in MongoDB?**  
   - Transactions cannot be longer than 60 seconds (configurable)  
   - Cannot write to capped collections  
   - Cannot create/drop collections or indexes  
   - Read concern "snapshot" not supported  
   - Limited to 1000 operations per transaction

89. **How does MongoDB handle concurrency?**  
   MongoDB uses a combination of reader-writer locks, optimistic concurrency control, and document-level locking to handle concurrent operations.

90. **Explain the concept of write locks in MongoDB.**  
   MongoDB uses intent locks at database and collection levels, and exclusive locks at document level for write operations to ensure data consistency.

91. **What is optimistic concurrency control?**  
   Optimistic concurrency assumes conflicts are rare and checks for conflicts at commit time rather than locking resources preemptively.

92. **How do you handle transaction timeouts?**  
   Set `maxTransactionLockRequestTimeoutMillis` or use `maxTimeMS` in transaction options. Default transaction timeout is 60 seconds.

93. **Explain the use of session in MongoDB transactions.**  
   Sessions provide causal consistency and allow tracking operations across multiple requests. Required for multi-document transactions.  
   *Example:*  
   ```javascript
   const session = db.getMongo().startSession({causalConsistency: true});
   ```

94. **What is the difference between local and global transactions?**  
   Local transactions operate within a single replica set, while global transactions (using sessions) can span multiple operations and provide causal consistency guarantees.

95. **How do transactions work with sharding?**  
   In sharded clusters, transactions can span multiple shards but require all participating shards to be available. The transaction coordinator manages the two-phase commit protocol across shards.

## 8. Security

96. How does MongoDB handle authentication?
97. Explain role-based access control (RBAC) in MongoDB.
98. What are the built-in roles in MongoDB?
99. How do you enable encryption at rest in MongoDB?
100. Explain the use of TLS/SSL in MongoDB.

### Answers for Security

96. **How does MongoDB handle authentication?**  
   MongoDB supports multiple authentication mechanisms: SCRAM-SHA-256 (default), SCRAM-SHA-1, X.509 certificates, LDAP, and Kerberos. Authentication is configured per user and can use external systems.

97. **Explain role-based access control (RBAC) in MongoDB.**  
   RBAC assigns permissions to users through roles. Roles contain privileges (resource + actions), and users inherit permissions from assigned roles.  
   *Example:*  
   ```javascript
   db.createRole({
     role: "readWriteApp",
     privileges: [
       {resource: {db: "myapp", collection: ""}, actions: ["find", "insert", "update"]}
     ],
     roles: []
   })
   ```

98. **What are the built-in roles in MongoDB?**  
   Built-in roles include: read, readWrite, readAnyDatabase, readWriteAnyDatabase, dbAdmin, dbOwner, userAdmin, clusterAdmin, backup, restore, etc.

99. **How do you enable encryption at rest in MongoDB?**  
   Use MongoDB Enterprise's encryption at rest feature, which encrypts database files on disk. Configure with encryption key and key management service.

100. **Explain the use of TLS/SSL in MongoDB.**  
    TLS/SSL provides encrypted communication between MongoDB clients and servers, preventing eavesdropping and man-in-the-middle attacks. Configure with certificate files and enable SSL mode.

## 9. Performance and Optimization

101. How do you profile slow queries in MongoDB?
102. Explain the use of the explain() method.
103. What are the key metrics to monitor in MongoDB?
104. How do you optimize MongoDB queries?
105. Explain the concept of covered queries.
106. What is the impact of document size on performance?
107. How do you handle large collections in MongoDB?
108. Explain the use of database profiler.
109. What are the best practices for indexing?
110. How do you monitor MongoDB performance?

### Answers for Performance and Optimization

101. **How do you profile slow queries in MongoDB?**  
    Enable the database profiler to capture slow operations.  
    *Example:*  
    ```javascript
    db.setProfilingLevel(2, {slowms: 100})  // Profile all queries > 100ms
    db.system.profile.find().sort({ts: -1}).limit(5)
    ```

102. **Explain the use of the explain() method.**  
    `explain()` shows the execution plan for a query, including index usage, execution time, and optimization suggestions.  
    *Example:*  
    ```javascript
    db.users.find({age: {$gt: 25}}).explain("executionStats")
    ```

103. **What are the key metrics to monitor in MongoDB?**  
    - Operation execution times  
    - Index usage statistics  
    - Memory usage (WiredTiger cache)  
    - Connection counts  
    - Replication lag  
    - Disk I/O and space usage  
    - Lock percentages

104. **How do you optimize MongoDB queries?**  
    - Create appropriate indexes  
    - Use covered queries when possible  
    - Optimize query patterns  
    - Use projection to limit returned fields  
    - Consider query selectivity

105. **Explain the concept of covered queries.**  
    Covered queries are queries where all fields in the query and projection are covered by indexes, eliminating the need to examine the actual documents.  
    *Example:*  
    ```javascript
    // Index on {name: 1, age: 1}
    db.users.find({name: "John"}, {name: 1, age: 1, _id: 0})
    ```

106. **What is the impact of document size on performance?**  
    Larger documents increase memory usage, network transfer time, and index size. Keep documents reasonably sized and consider embedding vs. referencing.

107. **How do you handle large collections in MongoDB?**  
    - Use appropriate indexing strategies  
    - Implement data archiving/purging  
    - Consider sharding for horizontal scaling  
    - Use capped collections for time-series data  
    - Optimize query patterns

108. **Explain the use of database profiler.**  
    The profiler captures slow operations and writes them to the system.profile collection, helping identify performance bottlenecks.

109. **What are the best practices for indexing?**  
    - Index fields used in queries  
    - Use compound indexes for multi-field queries  
    - Avoid over-indexing (increases write overhead)  
    - Monitor index usage with $indexStats  
    - Use partial indexes for selective data

110. **How do you monitor MongoDB performance?**  
    Use MongoDB's built-in tools:  
    - `mongostat` and `mongotop` command-line tools  
    - Database profiler  
    - `db.serverStatus()` for detailed metrics  
    - MongoDB Atlas monitoring (for cloud deployments)  
    - Third-party monitoring tools like PMM, Zabbix

## 10. Integration and Architecture

111. How do you integrate MongoDB with microservices architecture?
112. Explain the use of MongoDB in event-driven systems.
113. What are the best practices for MongoDB in distributed systems?
114. How does MongoDB work with message queues like Kafka?
115. Explain the concept of database per service in microservices.
116. How do you handle data consistency across microservices with MongoDB?
117. What are the considerations for MongoDB in containerized environments?
118. How do you implement change data capture with MongoDB?
119. Explain the use of MongoDB Atlas in cloud-native architectures.
120. How do you handle schema evolution in microservices with MongoDB?
121. What are the patterns for implementing sagas with MongoDB?
122. How do you implement event sourcing using MongoDB?
123. Explain the use of MongoDB in CQRS architecture.
124. How do you handle cross-service queries in microservices?
125. What are the considerations for MongoDB backup and recovery in distributed systems?

### Answers for Integration and Architecture

111. **How do you integrate MongoDB with microservices architecture?**  
    Use database-per-service pattern where each microservice owns its data. Services communicate via APIs, not direct database access. Use MongoDB's replica sets for high availability and change data capture for event-driven communication.

112. **Explain the use of MongoDB in event-driven systems.**  
    MongoDB can store events in collections and use change streams to publish events to message queues. This enables event sourcing patterns where state changes are stored as immutable events.

113. **What are the best practices for MongoDB in distributed systems?**  
    - Use replica sets for high availability  
    - Implement proper sharding strategies  
    - Configure appropriate read/write concerns  
    - Use connection pooling  
    - Implement circuit breakers for resilience  
    - Monitor cross-service data consistency

114. **How does MongoDB work with message queues like Kafka?**  
    Use MongoDB change streams to capture data changes and publish them to Kafka topics. Kafka Connect MongoDB connector can also replicate data changes to Kafka for downstream processing.

115. **Explain the concept of database per service in microservices.**  
    Each microservice maintains its own database schema and data, preventing tight coupling. Services communicate through well-defined APIs, maintaining loose coupling and independent deployment.

116. **How do you handle data consistency across microservices with MongoDB?**  
    Use eventual consistency with event-driven architecture, saga patterns for distributed transactions, or implement compensating actions. For strong consistency, use MongoDB's multi-document transactions within a service boundary.

117. **What are the considerations for MongoDB in containerized environments?**  
    - Use persistent volumes for data storage  
    - Configure resource limits and requests  
    - Implement proper health checks  
    - Use Kubernetes operators like MongoDB Community Operator  
    - Consider pod anti-affinity for replica sets

118. **How do you implement change data capture with MongoDB?**  
    Use MongoDB change streams to capture real-time data changes.  
    *Example:*  
    ```javascript
    const changeStream = db.collection.watch();
    changeStream.on('change', (change) => {
      console.log('Change detected:', change);
      // Publish to message queue or trigger event
    });
    ```

119. **Explain the use of MongoDB Atlas in cloud-native architectures.**  
    MongoDB Atlas provides managed MongoDB clusters with auto-scaling, backup, and monitoring. It integrates well with Kubernetes, serverless functions, and other cloud-native services.

120. **How do you handle schema evolution in microservices with MongoDB?**  
    Use schema versioning, backward-compatible changes, and migration scripts. Implement feature flags for gradual rollouts. Consider using schema registries for API contracts.

121. **What are the patterns for implementing sagas with MongoDB?**  
    Use event sourcing with compensating actions. Store saga state in MongoDB and use change streams to trigger next steps. Implement timeout and retry mechanisms.

122. **How do you implement event sourcing using MongoDB?**  
    Store all state changes as immutable events in collections. Use aggregation pipelines to reconstruct current state from events.  
    *Example:*  
    ```javascript
    // Event document
    {
      _id: ObjectId(),
      aggregateId: "user123",
      eventType: "UserCreated",
      data: {name: "John", email: "john@example.com"},
      timestamp: ISODate()
    }
    ```

123. **Explain the use of MongoDB in CQRS architecture.**  
    Use separate MongoDB collections/databases for read and write models. Write model handles commands and generates events, read model is optimized for queries and updated via event handlers.

124. **How do you handle cross-service queries in microservices?**  
    Avoid direct cross-service queries. Use API composition, CQRS with read models, or event-driven data synchronization. Implement service meshes for cross-service communication.

125. **What are the considerations for MongoDB backup and recovery in distributed systems?**  
    - Use MongoDB Atlas automated backups or mongodump for self-hosted  
    - Implement point-in-time recovery  
    - Test backup restoration procedures  
    - Consider geo-redundant backups  
    - Implement backup encryption  
    - Monitor backup success and performance

## 11. Scenario-based Questions

126. You have a social media application with millions of users. How would you design the user profile collection and handle profile updates?
127. In an e-commerce platform, how would you model product catalogs with categories and handle inventory management?
128. Design a chat application database schema using MongoDB. How would you handle message threading and real-time updates?
129. You need to implement a logging system that can handle high write throughput. What MongoDB features would you use?
130. How would you design a multi-tenant SaaS application using MongoDB?
131. In a microservices architecture, how would you handle data synchronization between services using MongoDB?
132. Design a recommendation engine database schema. How would you store user preferences and item relationships?
133. You have a time-series data application (IoT sensors). How would you optimize MongoDB for time-series data?
134. How would you implement a shopping cart that persists across sessions in a distributed e-commerce system?
135. Design a notification system that can handle millions of notifications per day using MongoDB.
136. In a gaming application, how would you handle player statistics and leaderboards?
137. How would you implement audit logging for compliance requirements using MongoDB?
138. Design a content management system with versioning capabilities using MongoDB.
139. You need to implement a rate limiting system for API calls. How would you use MongoDB?
140. How would you handle data migration from a relational database to MongoDB in a production environment?
141. Design a job queue system using MongoDB for background processing.
142. In a distributed team collaboration tool, how would you handle document sharing and permissions?
143. How would you implement a search functionality with faceted search using MongoDB?
144. Design a financial transaction system with MongoDB, considering ACID requirements.
145. How would you handle data archiving and retention policies in MongoDB?

### Answers for Scenario-based Questions

126. **You have a social media application with millions of users. How would you design the user profile collection and handle profile updates?**  
    Design user profiles with embedded subdocuments for frequently accessed data. Use references for relationships. Implement optimistic locking for concurrent updates.  
    *Schema Design:*  
    ```javascript
    {
      _id: ObjectId(),
      username: "john_doe",
      email: "john@example.com",
      profile: {
        firstName: "John",
        lastName: "Doe",
        bio: "Software Engineer",
        avatar: "url_to_image"
      },
      settings: {
        privacy: "public",
        notifications: true
      },
      followers: [ObjectId()], // References to user IDs
      following: [ObjectId()],
      posts: [ObjectId()], // References to post IDs
      version: 1 // For optimistic locking
    }
    ```
    *Update Strategy:* Use atomic operations and version checking to prevent lost updates.

127. **In an e-commerce platform, how would you model product catalogs with categories and handle inventory management?**  
    Use a combination of embedding and referencing. Embed category information in products for fast queries, reference for complex relationships.  
    *Product Schema:*  
    ```javascript
    {
      _id: ObjectId(),
      name: "Wireless Headphones",
      sku: "WH-001",
      price: 99.99,
      category: {
        _id: ObjectId(),
        name: "Electronics",
        path: "electronics/audio"
      },
      inventory: {
        quantity: 150,
        reserved: 5,
        lowStockThreshold: 10
      },
      variants: [
        {color: "black", size: "M", sku: "WH-001-BLK"}
      ]
    }
    ```
    *Inventory Updates:* Use atomic $inc operations to prevent race conditions.

128. **Design a chat application database schema using MongoDB. How would you handle message threading and real-time updates?**  
    Use separate collections for conversations and messages. Implement change streams for real-time updates.  
    *Schema:*  
    ```javascript
    // Conversations collection
    {
      _id: ObjectId(),
      participants: [ObjectId()],
      type: "direct|group",
      lastMessage: {
        text: "Hello!",
        sender: ObjectId(),
        timestamp: ISODate()
      },
      unreadCount: {userId: 5, userId2: 2}
    }
    
    // Messages collection
    {
      _id: ObjectId(),
      conversationId: ObjectId(),
      sender: ObjectId(),
      content: {
        type: "text|image|file",
        text: "Message content",
        mediaUrl: "url_if_media"
      },
      timestamp: ISODate(),
      readBy: [ObjectId()]
    }
    ```
    *Real-time:* Use change streams to push updates to connected clients.

129. **You need to implement a logging system that can handle high write throughput. What MongoDB features would you use?**  
    Use capped collections for automatic size management and high write performance. Implement sharding for horizontal scaling.  
    *Implementation:*  
    ```javascript
    // Create capped collection
    db.createCollection("logs", {
      capped: true,
      size: 100000000, // 100MB
      max: 10000 // or max documents
    })
    
    // Sharding for high throughput
    sh.shardCollection("logs.application_logs", {"timestamp": 1})
    ```

130. **How would you design a multi-tenant SaaS application using MongoDB?**  
    Use database-per-tenant for strong isolation, or collection-per-tenant with tenantId field for cost efficiency.  
    *Database-per-tenant:*  
    ```javascript
    // Separate database for each tenant
    use tenant_companyA;
    db.users.insertOne({tenantId: "companyA", name: "John"})
    ```
    *Collection-per-tenant:*  
    ```javascript
    // Single database, tenant-specific collections
    db.companyA_users.insertOne({name: "John"})
    ```

131. **In a microservices architecture, how would you handle data synchronization between services using MongoDB?**  
    Use event-driven architecture with change streams and message queues. Implement saga pattern for distributed transactions.  
    *Pattern:*  
    ```javascript
    // Service A publishes events
    const changeStream = db.orders.watch();
    changeStream.on('change', (change) => {
      if (change.operationType === 'insert') {
        // Publish to message queue
        publishToQueue('order.created', change.fullDocument);
      }
    });
    
    // Service B consumes and updates its data
    consumeFromQueue('order.created', (order) => {
      db.inventory.updateOne(
        {productId: order.productId},
        {$inc: {quantity: -order.quantity}}
      );
    });
    ```

132. **Design a recommendation engine database schema. How would you store user preferences and item relationships?**  
    Use separate collections for users, items, and interactions. Implement collaborative filtering data structures.  
    *Schema:*  
    ```javascript
    // User preferences
    {
      userId: ObjectId(),
      preferences: {
        categories: ["electronics", "books"],
        priceRange: {min: 10, max: 500}
      },
      viewedItems: [ObjectId()],
      purchasedItems: [ObjectId()]
    }
    
    // Item relationships
    {
      itemId: ObjectId(),
      similarItems: [ObjectId()],
      alsoBought: [ObjectId()],
      category: "electronics"
    }
    ```

133. **You have a time-series data application (IoT sensors). How would you optimize MongoDB for time-series data?**  
    Use time-based sharding, TTL indexes for automatic data expiration, and clustered collections for efficient time-range queries.  
    *Optimization:*  
    ```javascript
    // Create time-series collection
    db.createCollection("sensor_data", {
      timeseries: {
        timeField: "timestamp",
        metaField: "sensorId",
        granularity: "minutes"
      }
    })
    
    // TTL index for automatic cleanup
    db.sensor_data.createIndex(
      {timestamp: 1},
      {expireAfterSeconds: 2592000} // 30 days
    )
    ```

134. **How would you implement a shopping cart that persists across sessions in a distributed e-commerce system?**  
    Store cart data in MongoDB with user sessions, implement optimistic locking for concurrent updates.  
    *Implementation:*  
    ```javascript
    {
      _id: ObjectId(),
      userId: ObjectId(),
      sessionId: "session_123",
      items: [
        {
          productId: ObjectId(),
          quantity: 2,
          price: 29.99,
          addedAt: ISODate()
        }
      ],
      expiresAt: ISODate(),
      version: 1
    }
    ```

135. **Design a notification system that can handle millions of notifications per day using MongoDB.**  
    Use sharding with time-based shard keys, implement efficient indexing, and use TTL for automatic cleanup.  
    *Design:*  
    ```javascript
    // Sharded collection
    sh.shardCollection("notifications.user_notifications", {"userId": 1, "createdAt": 1})
    
    // Notification document
    {
      _id: ObjectId(),
      userId: ObjectId(),
      type: "order_update",
      title: "Order Shipped",
      message: "Your order has been shipped",
      read: false,
      createdAt: ISODate(),
      expiresAt: ISODate() // TTL field
    }
    ```

136. **In a gaming application, how would you handle player statistics and leaderboards?**  
    Use separate collections for player stats and computed leaderboards. Update leaderboards asynchronously.  
    *Implementation:*  
    ```javascript
    // Player stats
    {
      playerId: ObjectId(),
      gameId: ObjectId(),
      stats: {
        score: 1500,
        level: 25,
        achievements: ["first_win", "speed_demon"]
      },
      lastPlayed: ISODate()
    }
    
    // Leaderboard (computed)
    {
      gameId: ObjectId(),
      period: "daily",
      rankings: [
        {playerId: ObjectId(), score: 1500, rank: 1},
        {playerId: ObjectId(), score: 1450, rank: 2}
      ]
    }
    ```

137. **How would you implement audit logging for compliance requirements using MongoDB?**  
    Use immutable collections with strict schema validation, implement comprehensive indexing for audit queries.  
    *Audit Schema:*  
    ```javascript
    {
      _id: ObjectId(),
      timestamp: ISODate(),
      userId: ObjectId(),
      action: "CREATE_USER",
      resource: "users",
      resourceId: ObjectId(),
      changes: {
        before: {},
        after: {name: "John", email: "john@example.com"}
      },
      ipAddress: "192.168.1.1",
      userAgent: "Mozilla/5.0..."
    }
    ```

138. **Design a content management system with versioning capabilities using MongoDB.**  
    Store current content separately from version history, use references for efficient querying.  
    *Schema:*  
    ```javascript
    // Current content
    {
      _id: ObjectId(),
      title: "My Article",
      content: "Article content...",
      currentVersion: 3,
      published: true
    }
    
    // Version history
    {
      contentId: ObjectId(),
      version: 3,
      title: "My Article v3",
      content: "Updated content...",
      author: ObjectId(),
      timestamp: ISODate(),
      changes: "Updated introduction"
    }
    ```

139. **You need to implement a rate limiting system for API calls. How would you use MongoDB?**  
    Use TTL collections to store request counts with automatic expiration.  
    *Implementation:*  
    ```javascript
    // Rate limit counters
    {
      _id: ObjectId(),
      userId: ObjectId(),
      endpoint: "/api/users",
      window: "2023-01-01T10:00:00Z",
      count: 45,
      expiresAt: ISODate() // TTL field
    }
    ```

140. **How would you handle data migration from a relational database to MongoDB in a production environment?**  
    Use a phased approach with minimal downtime:  
    1. Set up MongoDB alongside existing database  
    2. Implement dual-write pattern  
    3. Migrate historical data using batch processing  
    4. Switch read operations gradually  
    5. Remove old database after verification  
    *Tools:* Use mongomirror or custom ETL scripts for data transfer.

141. **Design a job queue system using MongoDB for background processing.**  
    Use capped collections for job queue, implement priority and status tracking.  
    *Job Schema:*  
    ```javascript
    {
      _id: ObjectId(),
      type: "email_send",
      payload: {to: "user@example.com", subject: "Welcome"},
      priority: 1,
      status: "pending|processing|completed|failed",
      createdAt: ISODate(),
      startedAt: ISODate(),
      completedAt: ISODate(),
      retryCount: 0,
      maxRetries: 3
    }
    ```

142. **In a distributed team collaboration tool, how would you handle document sharing and permissions?**  
    Use role-based access control with permission inheritance, implement optimistic locking for concurrent edits.  
    *Schema:*  
    ```javascript
    // Document
    {
      _id: ObjectId(),
      title: "Project Plan",
      content: "...",
      owner: ObjectId(),
      permissions: [
        {userId: ObjectId(), role: "editor"},
        {groupId: ObjectId(), role: "viewer"}
      ],
      version: 5
    }
    ```

143. **How would you implement a search functionality with faceted search using MongoDB?**  
    Use text indexes for full-text search and aggregation pipelines for faceting.  
    *Implementation:*  
    ```javascript
    // Text index
    db.products.createIndex({name: "text", description: "text"})
    
    // Faceted search
    db.products.aggregate([
      {$match: {$text: {$search: "laptop"}}},
      {$facet: {
        categories: [{$sortByCount: "$category"}],
        priceRanges: [
          {$bucket: {groupBy: "$price", boundaries: [0, 100, 500, 1000]}}
        ],
        brands: [{$sortByCount: "$brand"}]
      }}
    ])
    ```

144. **Design a financial transaction system with MongoDB, considering ACID requirements.**  
    Use multi-document transactions for consistency, implement audit trails and idempotency.  
    *Transaction Schema:*  
    ```javascript
    // Use transactions for money transfers
    const session = db.getMongo().startSession();
    session.startTransaction();
    try {
      // Debit
      db.accounts.updateOne(
        {accountId: "acc1", balance: {$gte: 100}},
        {$inc: {balance: -100}},
        {session}
      );
      // Credit
      db.accounts.updateOne(
        {accountId: "acc2"},
        {$inc: {balance: 100}},
        {session}
      );
      session.commitTransaction();
    } catch (error) {
      session.abortTransaction();
    }
    ```

145. **How would you handle data archiving and retention policies in MongoDB?**  
    Implement TTL indexes for automatic data expiration, use aggregation pipelines for archiving logic.  
    *Strategies:*  
    ```javascript
    // TTL for automatic deletion
    db.logs.createIndex({timestamp: 1}, {expireAfterSeconds: 2592000});
    
    // Archival pipeline
    db.collection.aggregate([
      {$match: {createdAt: {$lt: ISODate("2022-01-01")}}},
      {$merge: {into: "archive_collection"}}
    ]);
    
    // Then delete from main collection
    db.collection.deleteMany({createdAt: {$lt: ISODate("2022-01-01")}});
    ```
