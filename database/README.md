# Database Interview Questions & Solutions

This repository contains commonly asked database interview questions and their solutions, covering various types of databases including SQL, NoSQL, and real-time databases. These questions are curated based on FAANG-level interviews and real-world scenarios.

## Table of Contents
- [SQL Database Questions](#sql-database-questions)
- [NoSQL Database Questions](#nosql-database-questions)
- [Real-time Database Questions](#real-time-database-questions)
- [System Design Questions](#system-design-questions)
- [Performance & Optimization](#performance--optimization)

## SQL Database Questions

### 1. ACID Properties
**Q: Explain ACID properties in detail and why they are important.**
**Solution:**
- **Atomicity**: All operations in a transaction succeed or all fail
- **Consistency**: Database remains in a valid state before and after transaction
- **Isolation**: Concurrent transactions don't interfere with each other
- **Durability**: Once a transaction is committed, it remains committed

**Example Transaction:**
```sql
BEGIN TRANSACTION;
    -- Atomicity: All or nothing
    UPDATE accounts SET balance = balance - 100 WHERE account_id = 'A123';
    UPDATE accounts SET balance = balance + 100 WHERE account_id = 'B456';
    -- If any statement fails, the entire transaction is rolled back
COMMIT;
```

### 2. Indexing
**Q: How do indexes work in SQL databases? When should you use them?**
**Solution:**
- Indexes are data structures that improve data retrieval speed
- Types: B-tree, Hash, Bitmap
- Use cases:
  - Frequently queried columns
  - Columns used in WHERE clauses
  - Columns used in JOIN conditions
- Trade-offs: Faster reads vs. slower writes and additional storage

**Example Index Creation:**
```sql
-- Single column index
CREATE INDEX idx_user_email ON users(email);

-- Composite index
CREATE INDEX idx_order_date_status ON orders(order_date, status);

-- Partial index (PostgreSQL)
CREATE INDEX idx_active_users ON users(email) WHERE status = 'active';

-- Covering index
CREATE INDEX idx_user_details ON users(email, name, status);
```

### 3. Normalization
**Q: Explain database normalization and its different forms.**
**Solution:**
- 1NF: Eliminate repeating groups
- 2NF: Remove partial dependencies
- 3NF: Remove transitive dependencies
- BCNF: Stricter version of 3NF
- 4NF: Remove multi-valued dependencies
- 5NF: Remove join dependencies

**Example: Denormalized to Normalized**
```sql
-- Denormalized table
CREATE TABLE orders (
    order_id INT,
    customer_name VARCHAR(100),
    customer_email VARCHAR(100),
    product_name VARCHAR(100),
    product_price DECIMAL(10,2)
);

-- Normalized tables
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

## NoSQL Database Questions

### 1. CAP Theorem
**Q: Explain CAP theorem and how it affects database design choices.**
**Solution:**
- **Consistency**: All nodes see the same data at the same time
- **Availability**: Every request receives a response
- **Partition Tolerance**: System continues to operate despite network failures
- You can only guarantee two of these properties at once

### 2. Document vs Key-Value Stores
**Q: Compare and contrast document and key-value stores. When would you choose one over the other?**
**Solution:**
- Document stores (MongoDB):
  - Schema-flexible
  - Better for complex queries
  - Good for hierarchical data
- Key-value stores (Redis):
  - Simple data model
  - Extremely fast
  - Good for caching and session storage

### 3. Sharding Strategies
**Q: Explain different sharding strategies and their trade-offs.**
**Solution:**
- Range-based sharding
- Hash-based sharding
- Directory-based sharding
- Considerations:
  - Data distribution
  - Query patterns
  - Scaling requirements
  - Rebalancing complexity

## Real-time Database Questions

### 1. Eventual Consistency
**Q: What is eventual consistency? How do you handle it in real-time applications?**
**Solution:**
- Data will eventually be consistent across all nodes
- Strategies:
  - Conflict resolution
  - Version vectors
  - Last-write-wins
  - CRDTs (Conflict-free Replicated Data Types)

### 2. Real-time Sync
**Q: How do you implement real-time synchronization in a distributed database?**
**Solution:**
- WebSocket connections
- Change Data Capture (CDC)
- Event sourcing
- Message queues
- Pub/sub patterns

## System Design Questions

### 1. Database Scaling
**Q: How would you scale a database system to handle millions of users?**
**Solution:**
- Horizontal vs Vertical scaling
- Read replicas
- Caching strategies
- Database sharding
- Load balancing
- Connection pooling

### 2. High Availability
**Q: Design a highly available database system.**
**Solution:**
- Master-slave replication
- Failover mechanisms
- Data redundancy
- Geographic distribution
- Monitoring and alerting
- Backup strategies

## Performance & Optimization

### 1. Query Optimization
**Q: How do you optimize slow database queries?**
**Solution:**
- Query analysis and profiling
- Index optimization
- Query rewriting
- Table partitioning
- Materialized views
- Denormalization when appropriate

**Example: Optimizing a Slow Query**
```sql
-- Original slow query
SELECT * FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id
WHERE o.order_date > '2023-01-01'
AND c.status = 'active'
ORDER BY o.order_date DESC;

-- Optimized query
SELECT o.order_id, o.order_date, c.name, p.name
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN products p ON o.product_id = p.product_id
WHERE o.order_date > '2023-01-01'
AND c.status = 'active'
ORDER BY o.order_date DESC
LIMIT 1000;
```

### 2. Caching Strategies
**Q: Explain different caching strategies and when to use them.**
**Solution:**
- Application-level caching
- Database query cache
- Distributed caching
- Cache invalidation strategies
- Cache consistency
- Cache size management

## Advanced Topics

### 1. Distributed Transactions
**Q: How do you handle distributed transactions across multiple databases?**
**Solution:**
- Two-phase commit
- Saga pattern
- Eventual consistency
- Compensation transactions
- Idempotency

### 2. Data Warehousing
**Q: Explain the architecture of a data warehouse and its components.**
**Solution:**
- ETL processes
- Star schema
- Snowflake schema
- OLAP vs OLTP
- Data marts
- Data lakes

### 3. Database Security
**Q: How do you ensure database security in a production environment?**
**Solution:**
- Authentication and Authorization
  - Role-based access control (RBAC)
  - Principle of least privilege
  - Multi-factor authentication
- Data Encryption
  - At-rest encryption
  - In-transit encryption (TLS/SSL)
  - Column-level encryption
- Security Best Practices
  - Regular security audits
  - SQL injection prevention
  - Input validation
  - Audit logging
  - Regular security patches

### 4. Database Migration
**Q: How would you handle a database migration with zero downtime?**
**Solution:**
- Blue-Green Deployment
- Database Replication
- Change Data Capture (CDC)
- Dual-Write Pattern
- Feature Flags
- Rollback Strategy
- Monitoring and Validation

### 5. Time-Series Databases
**Q: When would you choose a time-series database over a traditional database?**
**Solution:**
- Use Cases:
  - IoT data
  - Financial market data
  - Application metrics
  - System monitoring
- Key Features:
  - Efficient time-based queries
  - Data retention policies
  - Downsampling
  - Aggregation functions
- Popular Options:
  - InfluxDB
  - TimescaleDB
  - Prometheus

### 6. Graph Databases
**Q: Explain the use cases and advantages of graph databases.**
**Solution:**
- Use Cases:
  - Social networks
  - Recommendation engines
  - Fraud detection
  - Knowledge graphs
- Advantages:
  - Efficient relationship traversal
  - Flexible schema
  - Complex pattern matching
- Popular Options:
  - Neo4j
  - Amazon Neptune
  - JanusGraph

### 7. Database Consistency Models
**Q: Explain different consistency models and their trade-offs in distributed databases.**
**Solution:**
- Strong Consistency
  - Linearizability
  - Sequential consistency
  - Causal consistency
- Eventual Consistency
  - Read-your-writes
  - Monotonic reads
  - Monotonic writes
- Consistency vs Performance Trade-offs
  - Latency considerations
  - Network partition handling
  - Conflict resolution strategies

### 8. Database Partitioning
**Q: How would you partition a database that's growing beyond its capacity?**
**Solution:**
- Partitioning Strategies:
  - Range partitioning
  - Hash partitioning
  - List partitioning
  - Composite partitioning
- Considerations:
  - Data distribution
  - Query patterns
  - Join operations
  - Hot spots
  - Rebalancing
  - Cross-partition queries

### 9. Database Monitoring and Observability
**Q: How would you monitor and maintain a large-scale database system?**
**Solution:**
- Key Metrics:
  - Query performance
  - Resource utilization
  - Connection pool stats
  - Cache hit rates
  - Replication lag
  - Disk I/O
- Tools and Practices:
  - APM solutions
  - Query analysis
  - Slow query logging
  - Resource monitoring
  - Alerting systems
  - Capacity planning

## Modern Database Challenges

### 1. Multi-Region Database Design
**Q: Design a database system that spans multiple regions with minimal latency.**
**Solution:**
- Architecture:
  - Active-Active setup
  - Regional replication
  - Data locality
  - Conflict resolution
- Considerations:
  - Network latency
  - Data consistency
  - Failover strategy
  - Cost optimization
  - Compliance requirements

**Example: Cross-Region Replication Setup (AWS)**
```sql
-- Primary region
CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    email VARCHAR(255),
    region VARCHAR(50),
    created_at TIMESTAMP
);

-- Replication configuration (AWS)
CREATE REPLICATION GROUP my_replication_group
    WITH REPLICATION GROUP ID 'my-replication-group'
    REPLICATION GROUP CLASS 'db.r5.large'
    REPLICATION GROUP INSTANCE 'primary-instance'
    REPLICATION GROUP INSTANCE 'secondary-instance'
    REPLICATION GROUP INSTANCE 'tertiary-instance';
```

### 2. Database as a Service (DBaaS)
**Q: Compare self-hosted databases vs DBaaS solutions. When would you choose each?**
**Solution:**
- DBaaS Advantages:
  - Managed operations
  - Automatic scaling
  - Built-in monitoring
  - Regular updates
  - High availability
- Self-hosted Advantages:
  - Full control
  - Cost optimization
  - Custom configurations
  - Compliance requirements
  - Specialized workloads

**Example: Cloud Database Configuration (AWS RDS)**
```sql
-- Parameter group configuration
{
    "max_connections": 1000,
    "shared_buffers": "4GB",
    "work_mem": "64MB",
    "maintenance_work_mem": "256MB",
    "effective_cache_size": "12GB"
}

-- Connection string example
postgresql://user:password@my-instance.xxxxx.region.rds.amazonaws.com:5432/mydb
```

### 3. Database Performance Tuning
**Q: How would you optimize a database system experiencing performance issues?**
**Solution:**
- Analysis:
  - Query profiling
  - Resource monitoring
  - Bottleneck identification
  - Workload patterns
- Optimization Techniques:
  - Query rewriting
  - Index optimization
  - Configuration tuning
  - Hardware scaling
  - Caching strategy
  - Connection pooling

## System Design Deep Dives

### 1. Real-time Analytics Database
**Q: Design a database system for real-time analytics with sub-second query response.**
**Solution:**
- Architecture:
  - Columnar storage
  - In-memory processing
  - Materialized views
  - Pre-aggregation
- Considerations:
  - Data ingestion rate
  - Query patterns
  - Storage requirements
  - Cost optimization
  - Data freshness

**Example: Time-Series Data Schema (InfluxDB)**
```sql
-- Measurement definition
measurement: server_metrics
tags:
    - host
    - region
    - environment
fields:
    - cpu_usage
    - memory_usage
    - disk_io
    - network_traffic
timestamp: 2023-03-15T10:00:00Z

-- Query example
SELECT mean("cpu_usage") 
FROM "server_metrics" 
WHERE time >= now() - 1h 
GROUP BY time(5m), "host"
```

### 2. Multi-tenant Database
**Q: Design a database system supporting multiple tenants with data isolation.**
**Solution:**
- Approaches:
  - Separate databases
  - Shared database, separate schemas
  - Shared database, shared schema
- Considerations:
  - Data isolation
  - Resource allocation
  - Backup strategy
  - Scaling approach
  - Cost model

**Example: Multi-tenant Schema Design**
```sql
-- Approach 1: Separate Schemas
CREATE SCHEMA tenant_1;
CREATE SCHEMA tenant_2;

-- Approach 2: Shared Schema with Tenant ID
CREATE TABLE users (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL,
    email VARCHAR(255),
    created_at TIMESTAMP,
    CONSTRAINT fk_tenant FOREIGN KEY (tenant_id) REFERENCES tenants(id)
);

-- Row Level Security (PostgreSQL)
ALTER TABLE users ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation_policy ON users
    FOR ALL
    USING (tenant_id = current_setting('app.current_tenant')::uuid);
```

## Database Operations

### 1. Disaster Recovery
**Q: Design a comprehensive disaster recovery strategy for a critical database system.**
**Solution:**
- Components:
  - Backup strategy
  - Recovery procedures
  - Failover testing
  - Documentation
  - Team training
- Considerations:
  - RPO (Recovery Point Objective)
  - RTO (Recovery Time Objective)
  - Data integrity
  - Cost implications
  - Compliance requirements

**Example: Backup and Restore Commands**
```sql
-- PostgreSQL backup
pg_dump -U username -d database_name -F c -f backup.dump

-- PostgreSQL restore
pg_restore -U username -d database_name backup.dump

-- MySQL backup
mysqldump -u username -p database_name > backup.sql

-- MySQL restore
mysql -u username -p database_name < backup.sql
```

### 2. Database Maintenance
**Q: What are the key maintenance tasks for ensuring database health?**
**Solution:**
- Regular Tasks:
  - Index maintenance
  - Statistics updates
  - Vacuum operations
  - Log rotation
  - Backup verification
- Monitoring:
  - Performance metrics
  - Resource utilization
  - Error rates
  - Security alerts
  - Capacity planning

**Example: Maintenance Queries**
```sql
-- Index maintenance (PostgreSQL)
REINDEX TABLE users;
ANALYZE users;

-- Statistics update
ANALYZE VERBOSE users;

-- Vacuum operation
VACUUM FULL users;

-- Log rotation configuration (PostgreSQL)
log_rotation_age = 1d
log_rotation_size = 100MB
```

## Interview Preparation Tips

1. **System Design Approach**
   - Start with requirements
   - Consider scale
   - Discuss trade-offs
   - Mention monitoring
   - Include security
   - Plan for failures

2. **Technical Deep Dives**
   - Understand internals
   - Know performance characteristics
   - Be ready for trade-offs
   - Consider real-world constraints
   - Think about maintenance

3. **Problem-Solving Framework**
   - Clarify requirements
   - Propose solutions
   - Discuss alternatives
   - Consider edge cases
   - Plan for scale

## Additional Resources

- [Database Internals](https://www.example.com)
- [Distributed Systems Patterns](https://www.example.com)
- [Database Performance Tuning](https://www.example.com)
- [Cloud Database Services](https://www.example.com)
- [Database Security Best Practices](https://www.example.com)
- [Database Scalability Patterns](https://www.example.com)
- [Cloud Database Architectures](https://www.example.com)
- [Database Performance Engineering](https://www.example.com)
- [Distributed Database Systems](https://www.example.com)
- [Database Security Patterns](https://www.example.com)

---

*Note: This is a living document. Feel free to contribute more questions and solutions.*

*Last updated: [Current Date]*
