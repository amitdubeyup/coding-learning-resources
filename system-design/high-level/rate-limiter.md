# Design a Rate Limiter

## System Requirements

### Functional Requirements
1. Support multiple rate limiting algorithms (Token Bucket, Leaky Bucket)
2. Configurable rate limits per user/service
3. Distributed rate limiting
4. Rate limit headers in responses
5. Rate limit bypass for critical services
6. Rate limit analytics and monitoring
7. Rate limit configuration management

### Non-Functional Requirements
1. High availability (99.99%)
2. Low latency (< 10ms for rate limit checks)
3. Scalable to handle millions of requests per second
4. Consistent rate limiting across distributed systems
5. Minimal memory footprint

## Capacity Estimation

### Traffic Estimates
- Daily active users: 10 million
- Average requests per user: 1000 per day
- Peak RPS: 100,000
- Total requests per day: 10 billion
- Average rate limit rules: 5 per user
- Total rate limit rules: 50 million

### Storage Estimates
- Rate limit data: 100 bytes per rule
- User data: 1 KB per user
- Analytics data: 1 KB per request
- Daily storage: 10 GB
- Annual storage: ~3.6 TB
- Number of storage nodes: ~5

## System APIs

### Check Rate Limit
```
GET /api/v1/rate-limit
Request Headers:
{
    "X-API-Key": "key123",
    "X-User-ID": "user123"
}
Response:
{
    "allowed": true,
    "limit": 100,
    "remaining": 95,
    "reset": 1616248800
}
Response Headers:
{
    "X-RateLimit-Limit": "100",
    "X-RateLimit-Remaining": "95",
    "X-RateLimit-Reset": "1616248800"
}
```

### Configure Rate Limit
```
POST /api/v1/rate-limit/config
Request:
{
    "user_id": "user123",
    "rules": [
        {
            "endpoint": "/api/v1/users",
            "method": "GET",
            "limit": 100,
            "window": 3600,
            "algorithm": "token_bucket"
        }
    ]
}
Response:
{
    "status": "success",
    "config_id": "config123"
}
```

## Database Schema

### Rate Limit Rules
```sql
CREATE TABLE rate_limit_rules (
    rule_id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36),
    endpoint VARCHAR(255),
    method VARCHAR(10),
    limit INT,
    window INT,
    algorithm VARCHAR(20),
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    status VARCHAR(20)
);

CREATE INDEX idx_rules_user ON rate_limit_rules(user_id);
CREATE INDEX idx_rules_endpoint ON rate_limit_rules(endpoint, method);
```

### Rate Limit Counters
```sql
CREATE TABLE rate_limit_counters (
    counter_id VARCHAR(36) PRIMARY KEY,
    rule_id VARCHAR(36),
    user_id VARCHAR(36),
    count INT,
    reset_at TIMESTAMP,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE INDEX idx_counters_rule ON rate_limit_counters(rule_id, user_id);
CREATE INDEX idx_counters_reset ON rate_limit_counters(reset_at);
```

## High-Level Design

### Components
1. **Rate Limit Service**: Core rate limiting logic
2. **Counter Service**: Rate limit tracking
3. **Config Service**: Rule management
4. **Analytics Service**: Usage tracking
5. **Cache Service**: Counter caching
6. **Bypass Service**: Critical service handling

### Rate Limiting Flow
1. **Request Processing**
   - Request validation
   - Rule lookup
   - Counter check
   - Response generation

2. **Counter Management**
   - Counter increment
   - Window management
   - Cleanup handling
   - Analytics collection

## Detailed Component Design

### Rate Limit Service
1. Algorithm implementation
2. Rule evaluation
3. Counter management
4. Response generation
5. Error handling

### Counter Service
1. Counter operations
2. Window management
3. Cleanup handling
4. Consistency management
5. Performance optimization

### Config Service
1. Rule management
2. Configuration validation
3. Rule distribution
4. Version control
5. Audit logging

## Scaling Considerations

### Horizontal Scaling
1. **Service Scaling**
   - Load balancing
   - Service replication
   - Geographic distribution

2. **Counter Scaling**
   - Counter sharding
   - Replica distribution
   - Cache distribution

3. **Storage Scaling**
   - Data sharding
   - Read replicas
   - Cache distribution

### Performance Optimization
1. **Counter Optimization**
   - Counter batching
   - Cache warming
   - Lazy cleanup
   - Memory optimization

2. **Rule Optimization**
   - Rule caching
   - Rule compilation
   - Rule distribution
   - Rule validation

## Rate Limiting Features

1. **Algorithms**
   - Token Bucket
   - Leaky Bucket
   - Fixed Window
   - Sliding Window
   - Adaptive Rate Limiting

2. **Rule Types**
   - User-based limits
   - IP-based limits
   - Endpoint limits
   - Service limits
   - Custom limits

3. **Bypass Features**
   - Critical service bypass
   - Emergency bypass
   - VIP user bypass
   - Service bypass
   - Time-based bypass

## Monitoring and Analytics

1. **Key Metrics**
   - Rate limit hits
   - Bypass usage
   - Rule effectiveness
   - Counter accuracy
   - Error rates

2. **Alerts**
   - High bypass rate
   - Rule conflicts
   - Counter issues
   - Storage issues
   - Service health

## Security Considerations

1. **Rate Limit Security**
   - Bypass protection
   - Rule validation
   - Counter protection
   - Access control
   - Audit logging

2. **Configuration Security**
   - Rule validation
   - Access control
   - Change tracking
   - Version control
   - Rollback capability

## Implementation Details

### Token Bucket Algorithm
```python
class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_refill = time.time()

    def consume(self, tokens=1):
        self.refill()
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False

    def refill(self):
        now = time.time()
        time_passed = now - self.last_refill
        new_tokens = time_passed * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + new_tokens)
        self.last_refill = now
```

### Distributed Rate Limiting
```python
class DistributedRateLimiter:
    def __init__(self, redis_client):
        self.redis = redis_client

    def is_allowed(self, key, limit, window):
        current = self.redis.get(key)
        if current is None:
            self.redis.setex(key, window, 1)
            return True
        if int(current) < limit:
            self.redis.incr(key)
            return True
        return False
```

## Trade-offs and Alternatives

### Alternative Approaches
1. **Local vs. Distributed**
   - Local: Better performance, inconsistent
   - Distributed: More complex, consistent

2. **Algorithm Choice**
   - Token Bucket: Better burst handling
   - Leaky Bucket: Better rate smoothing

### Trade-offs
1. **Accuracy vs. Performance**
   - More accurate: Higher latency
   - Better performance: Less accurate

2. **Storage vs. Computation**
   - More storage: Better history
   - More computation: Better adaptation 