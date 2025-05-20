# Design a URL Shortening Service (TinyURL)

## System Requirements

### Functional Requirements
1. Given a long URL, generate a shorter URL
2. When users access the short URL, redirect them to the original URL
3. Custom short URLs should be supported
4. URLs should expire after a certain time period
5. Analytics for URL usage should be available

### Non-Functional Requirements
1. High availability
2. Low latency
3. Scalable to handle millions of URLs
4. Secure and reliable

## Capacity Estimation

### Traffic Estimates
- Daily active users: 100 million
- Average URL creation per user: 1 per day
- Read to Write ratio: 100:1
- Total URLs per day: 100 million
- Total redirects per day: 10 billion

### Storage Estimates
- Average URL length: 100 characters
- Short URL length: 7 characters
- Storage per URL: ~200 bytes
- Total storage per year: ~7.3 TB

## System APIs

### Create URL
```
POST /api/v1/urls
Request:
{
    "long_url": "https://www.example.com/very/long/url",
    "custom_alias": "optional_custom_alias",
    "expiry_date": "2024-12-31"
}
Response:
{
    "short_url": "https://tinyurl.com/abc123",
    "expiry_date": "2024-12-31"
}
```

### Get URL
```
GET /api/v1/urls/{short_url}
Response:
{
    "long_url": "https://www.example.com/very/long/url",
    "created_at": "2024-03-20",
    "expiry_date": "2024-12-31"
}
```

## Database Schema

### URLs Table
```sql
CREATE TABLE urls (
    id BIGINT PRIMARY KEY,
    short_url VARCHAR(7) UNIQUE,
    long_url VARCHAR(2048),
    user_id BIGINT,
    created_at TIMESTAMP,
    expiry_date TIMESTAMP,
    is_custom BOOLEAN,
    clicks BIGINT DEFAULT 0
);
```

### Analytics Table
```sql
CREATE TABLE url_analytics (
    id BIGINT PRIMARY KEY,
    url_id BIGINT,
    ip_address VARCHAR(45),
    user_agent VARCHAR(512),
    referrer VARCHAR(2048),
    timestamp TIMESTAMP,
    country VARCHAR(2),
    device_type VARCHAR(20)
);
```

## High-Level Design

### Components
1. **Load Balancer**: Distributes traffic across multiple servers
2. **Application Servers**: Handle URL creation and redirection
3. **Database Servers**: Store URL mappings and analytics
4. **Cache Servers**: Cache frequently accessed URLs
5. **Analytics Servers**: Process and store analytics data

### URL Shortening Algorithm
1. **Base62 Encoding**
   - Use characters: [a-zA-Z0-9]
   - 7 characters can represent 62^7 ≈ 3.5 trillion URLs
   - Example: "abc123" represents a unique ID

2. **Custom URLs**
   - Check availability in database
   - Validate against profanity/restricted words
   - Store with is_custom flag

## Detailed Component Design

### URL Creation Service
1. Validate input URL
2. Generate short URL
3. Store in database
4. Cache the mapping
5. Return short URL

### URL Redirection Service
1. Receive request for short URL
2. Check cache for mapping
3. If not in cache, query database
4. Update analytics
5. Redirect to long URL

### Analytics Service
1. Collect click data
2. Process in real-time
3. Store in analytics database
4. Generate reports

## Scaling Considerations

### Database Scaling
1. **Sharding**
   - Shard by URL hash
   - Distribute load across multiple servers

2. **Replication**
   - Master-slave replication
   - Read replicas for analytics

### Caching Strategy
1. **Multi-level Cache**
   - In-memory cache (Redis)
   - CDN for static content
   - Browser caching

2. **Cache Invalidation**
   - TTL-based expiration
   - Write-through cache

## Security Considerations

1. **URL Validation**
   - Check for malicious URLs
   - Validate URL format
   - Prevent spam

2. **Rate Limiting**
   - Per user/IP limits
   - API rate limiting
   - DDoS protection

3. **Access Control**
   - User authentication
   - URL ownership
   - Private URLs

## Monitoring and Analytics

1. **Key Metrics**
   - Response time
   - Error rates
   - Cache hit ratio
   - Storage usage

2. **Alerts**
   - High latency
   - Error rate spikes
   - Storage thresholds
   - Security incidents

## Trade-offs and Alternatives

### Alternative Approaches
1. **Hash-based vs. Counter-based**
   - Hash-based: No collision handling needed
   - Counter-based: Sequential, predictable

2. **Database vs. NoSQL**
   - SQL: Better for analytics
   - NoSQL: Better for scaling

### Trade-offs
1. **Performance vs. Consistency**
   - Eventual consistency for better performance
   - Strong consistency for critical operations

2. **Storage vs. Computation**
   - Pre-compute vs. on-demand generation
   - Cache size vs. hit ratio 