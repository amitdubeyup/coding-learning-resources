# PostgreSQL Interview Questions & Answers

A comprehensive guide covering PostgreSQL internals, advanced features, pgvector for AI/ML, and production best practices.

## Table of Contents
1. [Architecture & Internals](#architecture--internals)
2. [Data Types](#data-types)
3. [Indexing Strategies](#indexing-strategies)
4. [Query Optimization](#query-optimization)
5. [Advanced SQL Features](#advanced-sql-features)
6. [Partitioning](#partitioning)
7. [Stored Procedures & Functions](#stored-procedures--functions)
8. [pgvector for AI/ML](#pgvector-for-aiml)
9. [Replication & High Availability](#replication--high-availability)
10. [Performance Tuning](#performance-tuning)
11. [Security](#security)
12. [Monitoring & Maintenance](#monitoring--maintenance)
13. [Production Best Practices](#production-best-practices)

---

## Architecture & Internals

### Q1: Explain PostgreSQL's architecture and key processes
**Answer:**
PostgreSQL uses a multi-process architecture with:

- **Postmaster:** Main process that spawns others, handles connections
- **Backend processes:** One per client connection, executes queries
- **Background workers:** Autovacuum, WAL writer, checkpointer, stats collector
- **Shared memory:** Shared buffers, WAL buffers, lock tables

```
                    ┌─────────────────────────────────────┐
                    │           Shared Memory             │
                    │  ┌─────────────┐ ┌──────────────┐  │
                    │  │Shared Buffer│ │  WAL Buffer  │  │
                    │  └─────────────┘ └──────────────┘  │
                    └─────────────────────────────────────┘
                                      │
        ┌─────────┬─────────┬────────┼────────┬─────────┐
        ▼         ▼         ▼        ▼        ▼         ▼
   ┌─────────┐┌─────────┐┌─────────┐┌─────────┐┌─────────┐
   │Backend 1││Backend 2││Autovacuum│WAL Writer│Checkpointer
   └─────────┘└─────────┘└─────────┘└─────────┘└─────────┘
```

**Key takeaway:** Understanding this helps debug connection issues and tune shared memory settings.

---

### Q2: What is MVCC and how does PostgreSQL implement it?
**Answer:**
MVCC (Multi-Version Concurrency Control) allows readers and writers to not block each other by maintaining multiple versions of data rows.

**Implementation:**
- Each row has `xmin` (creating transaction ID) and `xmax` (deleting transaction ID)
- Transactions see a snapshot based on their start time
- Dead tuples (old versions) are cleaned by VACUUM

```sql
-- View transaction IDs on a row
SELECT xmin, xmax, * FROM users WHERE id = 1;

-- See current transaction ID
SELECT txid_current();

-- Check row visibility
SELECT ctid, xmin, xmax, name 
FROM users 
WHERE id = 1;
```

**Trade-offs:**
- **Pros:** High concurrency, consistent reads without locks
- **Cons:** Table bloat from dead tuples, requires VACUUM

---

### Q3: Explain Write-Ahead Logging (WAL) in PostgreSQL
**Answer:**
WAL ensures durability by writing changes to a log before applying to data files. If crash occurs, WAL is replayed to recover.

**Key concepts:**
- **WAL segments:** 16MB files in `pg_wal/` directory
- **Checkpoint:** Flushes dirty buffers to disk, advances recovery point
- **LSN (Log Sequence Number):** Position in WAL stream

```sql
-- Check current WAL position
SELECT pg_current_wal_lsn();

-- WAL statistics
SELECT * FROM pg_stat_wal;

-- Force checkpoint
CHECKPOINT;

-- View WAL settings
SHOW wal_level;
SHOW max_wal_size;
SHOW checkpoint_completion_target;
```

**Configuration tuning:**
```ini
# postgresql.conf
wal_level = replica              # minimal, replica, or logical
max_wal_size = 2GB               # Trigger checkpoint when reached
min_wal_size = 1GB               # Keep at least this much WAL
checkpoint_completion_target = 0.9  # Spread I/O over checkpoint interval
```

---

### Q4: How does VACUUM work and why is it important?
**Answer:**
VACUUM reclaims storage from dead tuples created by MVCC. Without it, tables bloat indefinitely.

**Types:**
- **VACUUM:** Marks space reusable, doesn't return to OS
- **VACUUM FULL:** Rewrites table, returns space to OS (heavy lock)
- **Autovacuum:** Background automatic vacuuming

```sql
-- Manual vacuum
VACUUM VERBOSE users;

-- Vacuum with analyze (update statistics)
VACUUM ANALYZE users;

-- Check table bloat
SELECT 
    relname,
    n_dead_tup,
    n_live_tup,
    round(n_dead_tup * 100.0 / nullif(n_live_tup + n_dead_tup, 0), 2) as dead_pct
FROM pg_stat_user_tables
ORDER BY n_dead_tup DESC;

-- Check autovacuum settings
SELECT name, setting 
FROM pg_settings 
WHERE name LIKE 'autovacuum%';
```

**Autovacuum tuning:**
```ini
autovacuum_vacuum_threshold = 50
autovacuum_vacuum_scale_factor = 0.1  # Vacuum when 10% dead tuples
autovacuum_analyze_threshold = 50
autovacuum_analyze_scale_factor = 0.05
```

---

## Data Types

### Q5: When should you use JSONB vs JSON vs relational columns?
**Answer:**

| Feature | JSON | JSONB | Relational |
|---------|------|-------|------------|
| Storage | Text (as-is) | Binary (parsed) | Native types |
| Indexing | No | Yes (GIN) | Yes (B-tree, etc.) |
| Query speed | Slow | Fast | Fastest |
| Schema flexibility | High | High | Low |
| Disk space | Less | More | Least |

**Use JSONB when:**
- Schema varies per row
- You need flexible attributes
- You want to avoid frequent migrations

**Use relational when:**
- Fixed schema, high query volume
- Need foreign keys and constraints
- Maximum performance required

```sql
-- JSONB column with indexing
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    attributes JSONB
);

-- GIN index for JSONB
CREATE INDEX idx_products_attrs ON products USING GIN (attributes);

-- Querying JSONB
SELECT * FROM products WHERE attributes->>'color' = 'red';
SELECT * FROM products WHERE attributes @> '{"size": "large"}';

-- JSONB operators
SELECT 
    attributes->'specs'->>'weight' as weight,      -- Extract as text
    (attributes->'price')::numeric as price        -- Cast to numeric
FROM products;
```

---

### Q6: Explain PostgreSQL array types and their use cases
**Answer:**
Arrays store multiple values of the same type in a single column. Useful for tags, categories, or denormalized data.

```sql
-- Create table with array
CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    title TEXT,
    tags TEXT[]
);

-- Insert with array
INSERT INTO articles (title, tags) VALUES 
    ('PostgreSQL Tips', ARRAY['database', 'sql', 'postgresql']),
    ('Python Guide', '{"python", "programming"}');  -- Alternative syntax

-- Query arrays
SELECT * FROM articles WHERE 'sql' = ANY(tags);
SELECT * FROM articles WHERE tags @> ARRAY['database'];
SELECT * FROM articles WHERE tags && ARRAY['python', 'sql'];  -- Overlap

-- GIN index for arrays
CREATE INDEX idx_articles_tags ON articles USING GIN (tags);

-- Array functions
SELECT 
    array_length(tags, 1) as tag_count,
    array_to_string(tags, ', ') as tags_str,
    unnest(tags) as individual_tag  -- Expands to rows
FROM articles;
```

---

## Indexing Strategies

### Q7: Compare different PostgreSQL index types
**Answer:**

| Index Type | Best For | Operators | Use Case |
|------------|----------|-----------|----------|
| **B-tree** | Equality, range | =, <, >, BETWEEN | Default, most queries |
| **Hash** | Equality only | = | Simple lookups (rare) |
| **GIN** | Contains, arrays, JSONB | @>, ?, &&, @@ | Full-text, JSONB, arrays |
| **GiST** | Geometric, range types | &&, @>, <@ | PostGIS, ranges, fuzzy |
| **BRIN** | Large sequential data | <, >, = | Time-series, logs |
| **SP-GiST** | Non-balanced structures | Various | IP ranges, phone numbers |

```sql
-- B-tree (default)
CREATE INDEX idx_users_email ON users(email);

-- Partial index (smaller, faster)
CREATE INDEX idx_active_users ON users(email) WHERE status = 'active';

-- Covering index (includes extra columns)
CREATE INDEX idx_users_covering ON users(email) INCLUDE (name, created_at);

-- GIN for JSONB
CREATE INDEX idx_data_gin ON documents USING GIN (data);

-- GIN for full-text search
CREATE INDEX idx_content_fts ON articles USING GIN (to_tsvector('english', content));

-- BRIN for time-series (very small index)
CREATE INDEX idx_logs_created ON logs USING BRIN (created_at);

-- Composite index
CREATE INDEX idx_orders_user_date ON orders(user_id, order_date DESC);
```

---

### Q8: What are partial indexes and when should you use them?
**Answer:**
Partial indexes only index rows matching a WHERE condition. They're smaller and faster for specific query patterns.

```sql
-- Only index active users (common query pattern)
CREATE INDEX idx_active_users ON users(email) 
WHERE status = 'active';

-- Only index unprocessed orders
CREATE INDEX idx_pending_orders ON orders(created_at) 
WHERE processed = false;

-- Only index recent data
CREATE INDEX idx_recent_logs ON logs(level, message) 
WHERE created_at > '2026-01-01';

-- Check index size comparison
SELECT 
    indexrelname,
    pg_size_pretty(pg_relation_size(indexrelid)) as index_size
FROM pg_stat_user_indexes
WHERE relname = 'users';
```

**Benefits:**
- Smaller index size → fits in memory
- Faster index maintenance on writes
- More efficient for known query patterns

---

### Q9: How do you identify and fix missing indexes?
**Answer:**
Use `pg_stat_user_tables` and `EXPLAIN ANALYZE` to find missing indexes.

```sql
-- Find tables with sequential scans (potential missing indexes)
SELECT 
    schemaname,
    relname,
    seq_scan,
    seq_tup_read,
    idx_scan,
    idx_tup_fetch,
    round(seq_tup_read::numeric / nullif(seq_scan, 0), 0) as avg_seq_rows
FROM pg_stat_user_tables
WHERE seq_scan > 100
ORDER BY seq_tup_read DESC;

-- Find unused indexes (candidates for removal)
SELECT 
    indexrelname,
    idx_scan,
    pg_size_pretty(pg_relation_size(indexrelid)) as size
FROM pg_stat_user_indexes
WHERE idx_scan = 0
    AND indexrelname NOT LIKE '%_pkey'
ORDER BY pg_relation_size(indexrelid) DESC;

-- Analyze query plan
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT * FROM orders WHERE user_id = 123 AND status = 'pending';

-- Create index based on findings
CREATE INDEX CONCURRENTLY idx_orders_user_status 
ON orders(user_id, status);
```

---

## Query Optimization

### Q10: How do you read and interpret EXPLAIN ANALYZE output?
**Answer:**
EXPLAIN shows the query plan; ANALYZE actually runs it with timing.

```sql
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT u.name, COUNT(o.id) as order_count
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE o.created_at > '2026-01-01'
GROUP BY u.id, u.name
ORDER BY order_count DESC
LIMIT 10;
```

**Key metrics to look for:**

| Metric | Meaning | Warning Signs |
|--------|---------|---------------|
| **Seq Scan** | Full table scan | Large tables without filter |
| **actual time** | Real execution time | High values |
| **rows** | Estimated vs actual | Large differences = stale stats |
| **Buffers: shared hit** | Cache hits | Low hit rate |
| **Buffers: shared read** | Disk reads | High values = slow |
| **Sort Method: external merge** | Disk sort | Increase work_mem |

**Common optimizations:**
```sql
-- Force index hint (not recommended, fix query instead)
SET enable_seqscan = off;

-- Update statistics
ANALYZE orders;

-- Check if stats are up to date
SELECT 
    relname,
    last_analyze,
    last_autoanalyze,
    n_live_tup,
    n_dead_tup
FROM pg_stat_user_tables
WHERE relname = 'orders';
```

---

### Q11: What are common query anti-patterns and how to fix them?
**Answer:**

**1. SELECT * (fetching unnecessary columns)**
```sql
-- Bad
SELECT * FROM users WHERE id = 1;

-- Good
SELECT id, name, email FROM users WHERE id = 1;
```

**2. NOT IN with subquery (can be slow with NULLs)**
```sql
-- Bad
SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM banned_users);

-- Good
SELECT u.* FROM users u
LEFT JOIN banned_users b ON u.id = b.user_id
WHERE b.user_id IS NULL;

-- Or use NOT EXISTS
SELECT * FROM users u
WHERE NOT EXISTS (SELECT 1 FROM banned_users b WHERE b.user_id = u.id);
```

**3. Functions on indexed columns**
```sql
-- Bad (can't use index)
SELECT * FROM users WHERE LOWER(email) = 'john@example.com';

-- Good (create functional index or store normalized)
CREATE INDEX idx_users_email_lower ON users(LOWER(email));
-- Or
SELECT * FROM users WHERE email = 'john@example.com';  -- case-insensitive collation
```

**4. OR conditions (can prevent index use)**
```sql
-- Bad
SELECT * FROM orders WHERE user_id = 1 OR status = 'pending';

-- Good (if you need this often)
SELECT * FROM orders WHERE user_id = 1
UNION ALL
SELECT * FROM orders WHERE status = 'pending' AND user_id != 1;
```

---

## Advanced SQL Features

### Q12: Explain window functions with examples
**Answer:**
Window functions perform calculations across rows related to current row without grouping.

```sql
-- Running total
SELECT 
    order_date,
    amount,
    SUM(amount) OVER (ORDER BY order_date) as running_total
FROM orders;

-- Rank within groups
SELECT 
    user_id,
    product_name,
    amount,
    RANK() OVER (PARTITION BY user_id ORDER BY amount DESC) as rank
FROM orders;

-- Moving average (last 7 rows)
SELECT 
    date,
    value,
    AVG(value) OVER (
        ORDER BY date 
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) as moving_avg_7
FROM daily_metrics;

-- Lead/Lag for comparing with adjacent rows
SELECT 
    order_date,
    amount,
    LAG(amount) OVER (ORDER BY order_date) as prev_amount,
    amount - LAG(amount) OVER (ORDER BY order_date) as diff
FROM orders;

-- First/Last value in window
SELECT 
    user_id,
    order_date,
    amount,
    FIRST_VALUE(amount) OVER (
        PARTITION BY user_id ORDER BY order_date
    ) as first_order_amount,
    LAST_VALUE(amount) OVER (
        PARTITION BY user_id 
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) as last_order_amount
FROM orders;
```

---

### Q13: How do you use CTEs (Common Table Expressions)?
**Answer:**
CTEs create named temporary result sets for complex queries. They improve readability and enable recursion.

```sql
-- Basic CTE
WITH active_users AS (
    SELECT id, name, email
    FROM users
    WHERE status = 'active'
),
user_orders AS (
    SELECT user_id, COUNT(*) as order_count
    FROM orders
    GROUP BY user_id
)
SELECT u.name, COALESCE(o.order_count, 0) as orders
FROM active_users u
LEFT JOIN user_orders o ON u.id = o.user_id;

-- Recursive CTE (organizational hierarchy)
WITH RECURSIVE org_hierarchy AS (
    -- Base case: top-level managers
    SELECT id, name, manager_id, 1 as level
    FROM employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    -- Recursive case: reports
    SELECT e.id, e.name, e.manager_id, h.level + 1
    FROM employees e
    JOIN org_hierarchy h ON e.manager_id = h.id
)
SELECT * FROM org_hierarchy ORDER BY level, name;

-- Recursive CTE for paths (graph traversal)
WITH RECURSIVE path_finder AS (
    SELECT id, name, ARRAY[id] as path, 0 as depth
    FROM nodes
    WHERE id = 1  -- Start node
    
    UNION ALL
    
    SELECT n.id, n.name, p.path || n.id, p.depth + 1
    FROM nodes n
    JOIN edges e ON n.id = e.target_id
    JOIN path_finder p ON e.source_id = p.id
    WHERE NOT n.id = ANY(p.path)  -- Prevent cycles
      AND p.depth < 10  -- Limit depth
)
SELECT * FROM path_finder;
```

---

## Partitioning

### Q14: Explain PostgreSQL table partitioning strategies
**Answer:**
Partitioning splits large tables into smaller physical pieces for better performance and maintenance.

**Types:**
- **Range:** By date ranges, numeric ranges
- **List:** By discrete values (region, category)
- **Hash:** Even distribution across N partitions

```sql
-- Range partitioning (by date - most common)
CREATE TABLE orders (
    id SERIAL,
    user_id INT,
    order_date DATE NOT NULL,
    amount DECIMAL(10,2),
    PRIMARY KEY (id, order_date)
) PARTITION BY RANGE (order_date);

-- Create partitions
CREATE TABLE orders_2025 PARTITION OF orders
    FOR VALUES FROM ('2025-01-01') TO ('2026-01-01');

CREATE TABLE orders_2026 PARTITION OF orders
    FOR VALUES FROM ('2026-01-01') TO ('2027-01-01');

-- Default partition for unmatched rows
CREATE TABLE orders_default PARTITION OF orders DEFAULT;

-- List partitioning (by region)
CREATE TABLE customers (
    id SERIAL,
    name VARCHAR(100),
    region VARCHAR(20) NOT NULL,
    PRIMARY KEY (id, region)
) PARTITION BY LIST (region);

CREATE TABLE customers_us PARTITION OF customers
    FOR VALUES IN ('us-east', 'us-west');
    
CREATE TABLE customers_eu PARTITION OF customers
    FOR VALUES IN ('eu-west', 'eu-central');

-- Hash partitioning (even distribution)
CREATE TABLE events (
    id SERIAL,
    user_id INT NOT NULL,
    event_type VARCHAR(50),
    PRIMARY KEY (id, user_id)
) PARTITION BY HASH (user_id);

CREATE TABLE events_p0 PARTITION OF events
    FOR VALUES WITH (MODULUS 4, REMAINDER 0);
CREATE TABLE events_p1 PARTITION OF events
    FOR VALUES WITH (MODULUS 4, REMAINDER 1);
-- ... create p2, p3
```

---

### Q15: How do you manage partitions in production?
**Answer:**

```sql
-- Attach existing table as partition
ALTER TABLE orders ATTACH PARTITION orders_2024
    FOR VALUES FROM ('2024-01-01') TO ('2025-01-01');

-- Detach partition (for archival)
ALTER TABLE orders DETACH PARTITION orders_2024;

-- Drop old partition
DROP TABLE orders_2023;

-- Check partition info
SELECT 
    parent.relname as parent,
    child.relname as partition,
    pg_get_expr(child.relpartbound, child.oid) as bounds
FROM pg_inherits
JOIN pg_class parent ON pg_inherits.inhparent = parent.oid
JOIN pg_class child ON pg_inherits.inhrelid = child.oid
WHERE parent.relname = 'orders';

-- Automate partition creation with pg_partman
CREATE EXTENSION pg_partman;

SELECT partman.create_parent(
    p_parent_table := 'public.orders',
    p_control := 'order_date',
    p_type := 'native',
    p_interval := '1 month',
    p_premake := 3
);
```

**Best practices:**
- Create partitions ahead of time (premake)
- Index each partition (inherited automatically in PG 11+)
- Use partition pruning (enabled by default)
- Archive/drop old partitions regularly

---

## Stored Procedures & Functions

### Q16: What's the difference between functions and procedures in PostgreSQL?
**Answer:**

| Feature | Function | Procedure (PG 11+) |
|---------|----------|-------------------|
| Return value | Required | Optional |
| Transaction control | No | Yes (COMMIT/ROLLBACK) |
| Call syntax | SELECT func() | CALL proc() |
| Use in expressions | Yes | No |

```sql
-- Function (returns a value)
CREATE OR REPLACE FUNCTION get_user_orders(p_user_id INT)
RETURNS TABLE (order_id INT, amount DECIMAL, order_date DATE)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT id, amount, order_date
    FROM orders
    WHERE user_id = p_user_id
    ORDER BY order_date DESC;
END;
$$;

-- Usage
SELECT * FROM get_user_orders(123);

-- Procedure (can control transactions)
CREATE OR REPLACE PROCEDURE transfer_funds(
    p_from_account INT,
    p_to_account INT,
    p_amount DECIMAL
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Debit
    UPDATE accounts SET balance = balance - p_amount
    WHERE id = p_from_account;
    
    -- Credit  
    UPDATE accounts SET balance = balance + p_amount
    WHERE id = p_to_account;
    
    -- Commit this transaction
    COMMIT;
END;
$$;

-- Usage
CALL transfer_funds(1, 2, 100.00);
```

---

### Q17: How do you create triggers in PostgreSQL?
**Answer:**

```sql
-- Audit trigger function
CREATE OR REPLACE FUNCTION audit_changes()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        INSERT INTO audit_log (table_name, operation, new_data, changed_at)
        VALUES (TG_TABLE_NAME, 'INSERT', row_to_json(NEW), NOW());
        RETURN NEW;
    ELSIF TG_OP = 'UPDATE' THEN
        INSERT INTO audit_log (table_name, operation, old_data, new_data, changed_at)
        VALUES (TG_TABLE_NAME, 'UPDATE', row_to_json(OLD), row_to_json(NEW), NOW());
        RETURN NEW;
    ELSIF TG_OP = 'DELETE' THEN
        INSERT INTO audit_log (table_name, operation, old_data, changed_at)
        VALUES (TG_TABLE_NAME, 'DELETE', row_to_json(OLD), NOW());
        RETURN OLD;
    END IF;
END;
$$;

-- Attach trigger
CREATE TRIGGER users_audit_trigger
AFTER INSERT OR UPDATE OR DELETE ON users
FOR EACH ROW EXECUTE FUNCTION audit_changes();

-- Trigger for updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$;

CREATE TRIGGER set_timestamp
BEFORE UPDATE ON users
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```

---

## pgvector for AI/ML

### Q18: How do you set up pgvector for vector similarity search?
**Answer:**
pgvector adds vector data type and similarity operators for AI/ML embeddings.

```sql
-- Install extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Create table with vector column
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    content TEXT,
    metadata JSONB,
    embedding vector(1536)  -- OpenAI ada-002 dimension
);

-- Insert embeddings
INSERT INTO documents (content, embedding) VALUES
    ('PostgreSQL is a database', '[0.1, 0.2, 0.3, ...]'),
    ('Vectors enable similarity search', '[0.2, 0.3, 0.4, ...]');

-- Similarity search (cosine distance)
SELECT id, content, 1 - (embedding <=> query_embedding) as similarity
FROM documents
ORDER BY embedding <=> query_embedding  -- <=> is cosine distance
LIMIT 5;

-- Other distance operators
-- <->  L2 distance (Euclidean)
-- <#>  Inner product (negative, for max inner product use ORDER BY ... DESC)
-- <=>  Cosine distance
```

---

### Q19: What pgvector index types are available and when to use each?
**Answer:**

| Index Type | Best For | Trade-off |
|------------|----------|-----------|
| **IVFFlat** | Medium datasets (<1M vectors) | Fast build, good recall |
| **HNSW** | Large datasets, high recall | Slower build, excellent recall |
| **(none)** | Small datasets (<10K) | Exact search, no approximation |

```sql
-- IVFFlat index (faster to build)
CREATE INDEX idx_docs_ivfflat ON documents 
USING ivfflat (embedding vector_cosine_ops)
WITH (lists = 100);  -- sqrt(n) to n/1000 lists

-- Set probes for search accuracy vs speed
SET ivfflat.probes = 10;  -- Search 10 lists (default 1)

-- HNSW index (better recall, slower build)
CREATE INDEX idx_docs_hnsw ON documents
USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);

-- Set search parameter
SET hnsw.ef_search = 100;  -- Higher = better recall, slower

-- Check index size
SELECT pg_size_pretty(pg_relation_size('idx_docs_hnsw'));
```

**Guidelines:**
- **< 10K vectors:** No index needed
- **10K - 1M vectors:** IVFFlat with lists = sqrt(n)
- **> 1M vectors:** HNSW for better recall

---

### Q20: How do you integrate pgvector with Python and LangChain?
**Answer:**

```python
# Using psycopg with pgvector
import psycopg
from pgvector.psycopg import register_vector

conn = psycopg.connect("postgresql://user:pass@localhost/db")
register_vector(conn)

# Insert embedding
embedding = [0.1, 0.2, 0.3]  # Your embedding
conn.execute(
    "INSERT INTO documents (content, embedding) VALUES (%s, %s)",
    ("Hello world", embedding)
)

# Similarity search
query_embedding = [0.1, 0.2, 0.3]
results = conn.execute(
    """
    SELECT id, content, 1 - (embedding <=> %s) as similarity
    FROM documents
    ORDER BY embedding <=> %s
    LIMIT 5
    """,
    (query_embedding, query_embedding)
).fetchall()
```

```python
# LangChain integration (2026 API)
from langchain_postgres import PGVector
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vectorstore = PGVector(
    embeddings=embeddings,
    collection_name="my_docs",
    connection="postgresql://user:pass@localhost/db",
    use_jsonb=True,
)

# Add documents
vectorstore.add_texts(
    texts=["Document 1", "Document 2"],
    metadatas=[{"source": "file1"}, {"source": "file2"}]
)

# Search
docs = vectorstore.similarity_search("query text", k=5)

# Search with score
docs_with_scores = vectorstore.similarity_search_with_score("query", k=5)
for doc, score in docs_with_scores:
    print(f"Score: {score:.4f}, Content: {doc.page_content}")
```

---

### Q21: How do you combine vector search with traditional filters?
**Answer:**
Hybrid search combines semantic similarity with metadata filtering.

```sql
-- Filtered vector search
SELECT id, content, 1 - (embedding <=> query_vec) as similarity
FROM documents
WHERE metadata->>'category' = 'tech'  -- Filter first
  AND metadata->>'date' > '2026-01-01'
ORDER BY embedding <=> query_vec
LIMIT 10;

-- Create composite index for filtered search
CREATE INDEX idx_docs_category_embedding ON documents
USING ivfflat ((embedding) vector_cosine_ops)
WHERE metadata->>'category' IS NOT NULL;

-- Or use partial HNSW index
CREATE INDEX idx_docs_tech ON documents
USING hnsw (embedding vector_cosine_ops)
WHERE metadata->>'category' = 'tech';

-- Hybrid: BM25 + vector (using pg_search or ts_rank)
WITH semantic AS (
    SELECT id, 1 - (embedding <=> query_vec) as semantic_score
    FROM documents
    ORDER BY embedding <=> query_vec
    LIMIT 100
),
keyword AS (
    SELECT id, ts_rank(content_tsv, query) as keyword_score
    FROM documents
    WHERE content_tsv @@ query
    LIMIT 100
)
SELECT 
    COALESCE(s.id, k.id) as id,
    COALESCE(s.semantic_score, 0) * 0.7 + 
    COALESCE(k.keyword_score, 0) * 0.3 as combined_score
FROM semantic s
FULL OUTER JOIN keyword k ON s.id = k.id
ORDER BY combined_score DESC
LIMIT 10;
```

---

## Replication & High Availability

### Q22: Explain PostgreSQL streaming replication
**Answer:**
Streaming replication sends WAL records to standby servers in real-time for high availability.

```ini
# Primary postgresql.conf
wal_level = replica
max_wal_senders = 5
wal_keep_size = 1GB

# Primary pg_hba.conf
host replication replicator standby_ip/32 scram-sha-256
```

```bash
# On standby: Create base backup
pg_basebackup -h primary_host -D /var/lib/postgresql/data \
    -U replicator -P -R --slot=standby1

# The -R flag creates standby.signal and postgresql.auto.conf
```

```sql
-- Check replication status on primary
SELECT client_addr, state, sent_lsn, write_lsn, flush_lsn, replay_lsn,
       pg_wal_lsn_diff(sent_lsn, replay_lsn) as lag_bytes
FROM pg_stat_replication;

-- Check on standby
SELECT pg_is_in_recovery();
SELECT pg_last_wal_receive_lsn(), pg_last_wal_replay_lsn();
```

---

### Q23: What is logical replication and when to use it?
**Answer:**
Logical replication replicates changes at the row level, allowing selective table replication and cross-version replication.

**Use cases:**
- Replicate subset of tables
- Replicate between different PG versions
- Consolidate data from multiple databases
- Zero-downtime upgrades

```sql
-- On publisher
CREATE PUBLICATION my_pub FOR TABLE users, orders;
-- Or all tables
CREATE PUBLICATION all_tables FOR ALL TABLES;

-- On subscriber
CREATE SUBSCRIPTION my_sub
    CONNECTION 'host=publisher_host dbname=mydb user=replicator'
    PUBLICATION my_pub;

-- Check status
SELECT * FROM pg_stat_subscription;
SELECT * FROM pg_publication_tables;
```

---

### Q24: How do you set up high availability with Patroni?
**Answer:**
Patroni manages PostgreSQL HA clusters with automatic failover using a distributed consensus store (etcd/Consul/ZooKeeper).

```yaml
# patroni.yml
scope: postgres-cluster
name: node1

restapi:
  listen: 0.0.0.0:8008
  connect_address: node1:8008

etcd:
  hosts: etcd1:2379,etcd2:2379,etcd3:2379

bootstrap:
  dcs:
    ttl: 30
    loop_wait: 10
    retry_timeout: 10
    maximum_lag_on_failover: 1048576
    postgresql:
      use_pg_rewind: true
      parameters:
        max_connections: 200
        shared_buffers: 2GB

  pg_hba:
    - host replication replicator 0.0.0.0/0 scram-sha-256
    - host all all 0.0.0.0/0 scram-sha-256

postgresql:
  listen: 0.0.0.0:5432
  connect_address: node1:5432
  data_dir: /var/lib/postgresql/data
  authentication:
    replication:
      username: replicator
      password: secret
    superuser:
      username: postgres
      password: secret
```

```bash
# Check cluster status
patronictl list

# Manual switchover
patronictl switchover --master node1 --candidate node2

# Failover (when master is down)
patronictl failover
```

---

## Performance Tuning

### Q25: What are the key PostgreSQL configuration parameters for performance?
**Answer:**

```ini
# Memory settings
shared_buffers = 4GB                 # 25% of RAM for dedicated DB server
effective_cache_size = 12GB          # 75% of RAM (estimate of OS cache)
work_mem = 64MB                      # Per-operation memory (careful with many connections)
maintenance_work_mem = 1GB           # For VACUUM, CREATE INDEX

# Write performance
wal_buffers = 64MB                   # WAL buffer size
checkpoint_completion_target = 0.9   # Spread checkpoint I/O
max_wal_size = 4GB                   # Checkpoint trigger threshold

# Query planner
random_page_cost = 1.1               # SSD (default 4.0 for HDD)
effective_io_concurrency = 200       # SSD (default 1)

# Connection handling
max_connections = 200                # Or use connection pooling
```

**Checking current settings:**
```sql
-- All settings
SELECT name, setting, unit, context
FROM pg_settings
WHERE name IN ('shared_buffers', 'work_mem', 'effective_cache_size');

-- Memory usage
SELECT 
    sum(heap_blks_hit) / sum(heap_blks_hit + heap_blks_read) as cache_hit_ratio
FROM pg_statio_user_tables;
```

---

### Q26: How do you use connection pooling with PgBouncer?
**Answer:**
PgBouncer pools connections to handle thousands of clients with fewer backend connections.

```ini
# pgbouncer.ini
[databases]
mydb = host=localhost port=5432 dbname=mydb

[pgbouncer]
listen_addr = 0.0.0.0
listen_port = 6432
auth_type = scram-sha-256
auth_file = /etc/pgbouncer/userlist.txt

# Pool settings
pool_mode = transaction     # transaction, session, or statement
max_client_conn = 1000      # Max client connections
default_pool_size = 25      # Connections per pool
min_pool_size = 5
reserve_pool_size = 5

# Timeouts
server_idle_timeout = 600
client_idle_timeout = 0
```

**Pool modes:**
- **session:** Connection held until client disconnects (like no pooling)
- **transaction:** Connection returned after each transaction (recommended)
- **statement:** Connection returned after each statement (limited use)

```sql
-- Monitor PgBouncer
SHOW STATS;
SHOW POOLS;
SHOW CLIENTS;
```

---

## Security

### Q27: How do you implement row-level security (RLS) in PostgreSQL?
**Answer:**
RLS restricts which rows users can access based on policies.

```sql
-- Enable RLS on table
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;

-- Policy for users to see only their orders
CREATE POLICY user_orders_policy ON orders
    FOR ALL
    USING (user_id = current_setting('app.current_user_id')::int);

-- Policy for admins to see all
CREATE POLICY admin_all_orders ON orders
    FOR ALL
    TO admin_role
    USING (true);

-- Set user context in application
SET app.current_user_id = '123';
SELECT * FROM orders;  -- Only sees user 123's orders

-- Multi-tenant RLS
CREATE POLICY tenant_isolation ON data
    FOR ALL
    USING (tenant_id = current_setting('app.tenant_id')::uuid);

-- Bypass RLS for superuser/owner (optional)
ALTER TABLE orders FORCE ROW LEVEL SECURITY;  -- Apply to owner too
```

---

### Q28: What are PostgreSQL security best practices?
**Answer:**

```sql
-- 1. Use roles with least privilege
CREATE ROLE app_readonly;
GRANT CONNECT ON DATABASE mydb TO app_readonly;
GRANT USAGE ON SCHEMA public TO app_readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO app_readonly;

CREATE ROLE app_readwrite;
GRANT app_readonly TO app_readwrite;
GRANT INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_readwrite;

-- 2. Revoke public permissions
REVOKE ALL ON DATABASE mydb FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM PUBLIC;

-- 3. Use SCRAM-SHA-256 authentication
-- pg_hba.conf
host all all 0.0.0.0/0 scram-sha-256

-- 4. Enable SSL
-- postgresql.conf
ssl = on
ssl_cert_file = '/path/to/server.crt'
ssl_key_file = '/path/to/server.key'

-- Force SSL in pg_hba.conf
hostssl all all 0.0.0.0/0 scram-sha-256

-- 5. Audit logging
CREATE EXTENSION pgaudit;
-- postgresql.conf
pgaudit.log = 'write, ddl'

-- 6. Encrypt sensitive columns
CREATE EXTENSION pgcrypto;
INSERT INTO users (email, password_hash) VALUES
    ('user@example.com', crypt('password', gen_salt('bf')));
```

---

## Monitoring & Maintenance

### Q29: What pg_stat views should you monitor?
**Answer:**

```sql
-- Table statistics
SELECT 
    relname,
    seq_scan, seq_tup_read,      -- Sequential scans
    idx_scan, idx_tup_fetch,     -- Index scans
    n_tup_ins, n_tup_upd, n_tup_del,  -- Writes
    n_live_tup, n_dead_tup       -- Tuple counts
FROM pg_stat_user_tables
ORDER BY seq_tup_read DESC;

-- Index usage
SELECT 
    indexrelname,
    idx_scan,
    idx_tup_read,
    idx_tup_fetch
FROM pg_stat_user_indexes
ORDER BY idx_scan DESC;

-- Slow queries (requires pg_stat_statements)
CREATE EXTENSION pg_stat_statements;

SELECT 
    calls,
    total_exec_time / 1000 as total_seconds,
    mean_exec_time as avg_ms,
    rows,
    query
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 20;

-- Connection stats
SELECT * FROM pg_stat_activity
WHERE state = 'active';

-- Replication lag
SELECT 
    client_addr,
    state,
    pg_wal_lsn_diff(pg_current_wal_lsn(), replay_lsn) as lag_bytes
FROM pg_stat_replication;

-- Lock monitoring
SELECT 
    blocked.pid as blocked_pid,
    blocked.query as blocked_query,
    blocking.pid as blocking_pid,
    blocking.query as blocking_query
FROM pg_stat_activity blocked
JOIN pg_locks blocked_locks ON blocked.pid = blocked_locks.pid
JOIN pg_locks blocking_locks ON blocked_locks.locktype = blocking_locks.locktype
    AND blocked_locks.relation = blocking_locks.relation
    AND blocked_locks.pid != blocking_locks.pid
JOIN pg_stat_activity blocking ON blocking_locks.pid = blocking.pid
WHERE NOT blocked_locks.granted;
```

---

### Q30: How do you perform backup and recovery?
**Answer:**

```bash
# Logical backup (pg_dump)
pg_dump -U postgres -Fc mydb > backup.dump    # Custom format (compressed)
pg_dump -U postgres -Fp mydb > backup.sql     # Plain SQL

# Restore
pg_restore -U postgres -d mydb backup.dump
psql -U postgres -d mydb < backup.sql

# Parallel dump/restore for large DBs
pg_dump -U postgres -Fc -j 4 mydb > backup.dump
pg_restore -U postgres -d mydb -j 4 backup.dump

# Physical backup (pg_basebackup)
pg_basebackup -h localhost -U replicator -D /backup/base -Fp -Xs -P

# Point-in-time recovery (PITR)
# 1. Enable WAL archiving
archive_mode = on
archive_command = 'cp %p /archive/%f'

# 2. After restoring base backup, create recovery.signal
touch /var/lib/postgresql/data/recovery.signal

# 3. Configure recovery target in postgresql.conf
restore_command = 'cp /archive/%f %p'
recovery_target_time = '2026-02-14 10:00:00'
recovery_target_action = 'promote'
```

---

## Production Best Practices

### Q31: What's your PostgreSQL production deployment checklist?
**Answer:**

**Before Go-Live:**
```sql
-- 1. Verify indexes exist for foreign keys
SELECT 
    conrelid::regclass as table_name,
    conname as constraint_name,
    a.attname as column_name
FROM pg_constraint c
JOIN pg_attribute a ON a.attnum = ANY(c.conkey) AND a.attrelid = c.conrelid
WHERE c.contype = 'f'
AND NOT EXISTS (
    SELECT 1 FROM pg_index i
    WHERE i.indrelid = c.conrelid
    AND a.attnum = ANY(i.indkey)
);

-- 2. Check for missing primary keys
SELECT table_name 
FROM information_schema.tables t
WHERE table_schema = 'public' 
AND table_type = 'BASE TABLE'
AND NOT EXISTS (
    SELECT 1 FROM information_schema.table_constraints c
    WHERE c.table_name = t.table_name 
    AND c.constraint_type = 'PRIMARY KEY'
);

-- 3. Analyze all tables
ANALYZE VERBOSE;

-- 4. Verify connection settings
SHOW max_connections;
SHOW shared_buffers;
```

**Ongoing:**
- Monitor slow queries with pg_stat_statements
- Set up automated backups with verification
- Configure alerting for replication lag, connection saturation
- Regular VACUUM ANALYZE
- Review and rotate logs
- Test disaster recovery quarterly

---

### Q32: How do you handle schema migrations safely?
**Answer:**

```sql
-- 1. Use transactions for rollback
BEGIN;
ALTER TABLE users ADD COLUMN status VARCHAR(20) DEFAULT 'active';
-- Test
ROLLBACK;  -- Or COMMIT;

-- 2. Add columns as nullable first
ALTER TABLE users ADD COLUMN email_verified BOOLEAN;
-- Later, backfill and add constraint
UPDATE users SET email_verified = false WHERE email_verified IS NULL;
ALTER TABLE users ALTER COLUMN email_verified SET NOT NULL;

-- 3. Create indexes concurrently (no lock)
CREATE INDEX CONCURRENTLY idx_users_email ON users(email);

-- 4. Use pg_repack for table rewrites without locks
-- Instead of:
-- ALTER TABLE big_table ALTER COLUMN id TYPE bigint;  -- LOCKS TABLE
-- Use pg_repack:
pg_repack --table big_table --no-order

-- 5. Add constraints without validation first
ALTER TABLE orders ADD CONSTRAINT fk_user 
    FOREIGN KEY (user_id) REFERENCES users(id) NOT VALID;
-- Then validate separately
ALTER TABLE orders VALIDATE CONSTRAINT fk_user;
```

**Migration tools:**
- Alembic (Python)
- Flyway (Java)
- golang-migrate
- Sqitch

---

## Additional Advanced Topics

### Q33: How do you use Foreign Data Wrappers (FDW)?
**Answer:**
FDW lets you query external data sources as if they were local tables.

```sql
-- PostgreSQL to PostgreSQL
CREATE EXTENSION postgres_fdw;

CREATE SERVER remote_server
    FOREIGN DATA WRAPPER postgres_fdw
    OPTIONS (host 'remote-host', dbname 'remotedb', port '5432');

CREATE USER MAPPING FOR local_user
    SERVER remote_server
    OPTIONS (user 'remote_user', password 'secret');

-- Import all tables from remote schema
IMPORT FOREIGN SCHEMA public
    FROM SERVER remote_server
    INTO local_schema;

-- Or create single foreign table
CREATE FOREIGN TABLE remote_users (
    id INT,
    name VARCHAR(100),
    email VARCHAR(255)
) SERVER remote_server OPTIONS (table_name 'users');

-- Query like normal
SELECT * FROM remote_users WHERE id = 1;

-- Join local and remote
SELECT l.*, r.extra_data
FROM local_users l
JOIN remote_users r ON l.id = r.id;
```

---

### Q34: How do you implement full-text search in PostgreSQL?
**Answer:**

```sql
-- Add tsvector column
ALTER TABLE articles ADD COLUMN content_tsv tsvector;

-- Populate and index
UPDATE articles SET content_tsv = to_tsvector('english', title || ' ' || content);
CREATE INDEX idx_articles_fts ON articles USING GIN (content_tsv);

-- Auto-update with trigger
CREATE FUNCTION update_tsv() RETURNS TRIGGER AS $$
BEGIN
    NEW.content_tsv := to_tsvector('english', NEW.title || ' ' || NEW.content);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER articles_tsv_update
    BEFORE INSERT OR UPDATE ON articles
    FOR EACH ROW EXECUTE FUNCTION update_tsv();

-- Search with ranking
SELECT 
    id, title,
    ts_rank(content_tsv, query) as rank,
    ts_headline('english', content, query) as snippet
FROM articles, to_tsquery('english', 'postgresql & performance') query
WHERE content_tsv @@ query
ORDER BY rank DESC
LIMIT 10;

-- Phrase search
SELECT * FROM articles
WHERE content_tsv @@ phraseto_tsquery('english', 'database performance');
```

---

## Summary

### Key Takeaways for PostgreSQL Interviews

1. **Architecture:** Understand MVCC, WAL, vacuum, and process model
2. **Indexing:** Know when to use B-tree vs GIN vs BRIN; partial and covering indexes
3. **Query optimization:** Read EXPLAIN ANALYZE, identify anti-patterns
4. **pgvector:** Critical for AI/ML; know HNSW vs IVFFlat trade-offs
5. **High availability:** Streaming replication, Patroni, connection pooling
6. **Security:** RLS, encryption, least privilege
7. **Performance:** Configuration tuning, monitoring with pg_stat views
8. **Operations:** Backup/recovery, safe migrations, maintenance

### Quick Reference

| Task | Key Command/Setting |
|------|---------------------|
| Check slow queries | `pg_stat_statements` |
| Monitor connections | `pg_stat_activity` |
| Check replication | `pg_stat_replication` |
| Find bloat | `pg_stat_user_tables.n_dead_tup` |
| Index health | `pg_stat_user_indexes` |
| Memory tuning | `shared_buffers`, `work_mem` |
| Disk I/O tuning | `random_page_cost`, `effective_io_concurrency` |

---

*Last updated: February 2026*
