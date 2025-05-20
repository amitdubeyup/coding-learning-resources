# Design a Real-time Chat Application

## System Requirements

### Functional Requirements
1. Real-time messaging between users
2. Support for different message types (text, images, files)
3. Group chat functionality
4. Message delivery status (sent, delivered, read)
5. Online/offline status
6. Message history and search
7. Push notifications

### Non-Functional Requirements
1. High availability (99.99%)
2. Low latency (< 100ms for message delivery)
3. Scalable to handle millions of concurrent users
4. Message persistence
5. End-to-end encryption

## Capacity Estimation

### Traffic Estimates
- Daily active users: 50 million
- Average messages per user: 100 per day
- Peak concurrent users: 1 million
- Peak messages per second: 50,000
- Total messages per day: 5 billion
- Average message size: 1 KB

### Storage Estimates
- Message data: 1 KB per message
- User data: 2 KB per user
- Chat metadata: 500 bytes per chat
- Daily storage: 5 TB
- Annual storage: ~1.8 PB
- Number of storage nodes: ~100

## System APIs

### Send Message
```
POST /api/v1/messages
Request:
{
    "chat_id": "chat123",
    "sender_id": "user123",
    "content": "Hello!",
    "type": "text",
    "metadata": {
        "reply_to": "msg123",
        "mentions": ["user456"]
    }
}
Response:
{
    "message_id": "msg123",
    "status": "sent",
    "created_at": "2024-03-20T10:00:00Z"
}
```

### Get Messages
```
GET /api/v1/chats/{chat_id}/messages
Query Parameters:
{
    "before": "msg123",
    "limit": 50,
    "type": "all"
}
Response:
{
    "messages": [
        {
            "message_id": "msg123",
            "sender_id": "user123",
            "content": "Hello!",
            "type": "text",
            "status": "delivered",
            "created_at": "2024-03-20T10:00:00Z"
        }
    ],
    "has_more": true
}
```

## Database Schema

### Messages Table
```sql
CREATE TABLE messages (
    message_id VARCHAR(36) PRIMARY KEY,
    chat_id VARCHAR(36),
    sender_id VARCHAR(36),
    content TEXT,
    type VARCHAR(20),
    status VARCHAR(20),
    metadata JSONB,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE INDEX idx_messages_chat ON messages(chat_id, created_at);
CREATE INDEX idx_messages_sender ON messages(sender_id, created_at);
```

### Chats Table
```sql
CREATE TABLE chats (
    chat_id VARCHAR(36) PRIMARY KEY,
    type VARCHAR(20),
    name VARCHAR(255),
    metadata JSONB,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE chat_participants (
    chat_id VARCHAR(36),
    user_id VARCHAR(36),
    role VARCHAR(20),
    joined_at TIMESTAMP,
    PRIMARY KEY (chat_id, user_id)
);
```

## High-Level Design

### Components
1. **Chat Service**: Core chat functionality
2. **WebSocket Service**: Real-time communication
3. **Message Service**: Message handling
4. **Presence Service**: Online status
5. **Storage Service**: Message persistence
6. **Notification Service**: Push notifications

### Message Flow
1. **Message Sending**
   - Message validation
   - Real-time delivery
   - Persistence
   - Notification

2. **Message Receiving**
   - WebSocket delivery
   - Status updates
   - History sync
   - Offline handling

## Detailed Component Design

### WebSocket Service
1. Connection management
2. Message routing
3. Heartbeat handling
4. Reconnection logic
5. Load balancing

### Message Service
1. Message validation
2. Delivery guarantees
3. Retry logic
4. Ordering
5. Deduplication

### Presence Service
1. Online status tracking
2. Last seen updates
3. Status broadcasting
4. Heartbeat monitoring
5. Cleanup handling

## Scaling Considerations

### Horizontal Scaling
1. **Service Scaling**
   - Load balancing
   - Service replication
   - Geographic distribution

2. **WebSocket Scaling**
   - Connection distribution
   - Message routing
   - State management

3. **Storage Scaling**
   - Message sharding
   - Read replicas
   - Data partitioning

### Performance Optimization
1. **Message Delivery**
   - Message batching
   - Compression
   - Caching
   - Connection pooling

2. **Storage Optimization**
   - Message archiving
   - Index optimization
   - Cache warming
   - Data cleanup

## Chat Features

1. **Message Types**
   - Text messages
   - Images
   - Files
   - Voice messages
   - Video calls

2. **Chat Types**
   - One-on-one chats
   - Group chats
   - Channels
   - Broadcast messages

3. **Message Features**
   - Read receipts
   - Typing indicators
   - Message reactions
   - Message editing
   - Message deletion

## Monitoring and Analytics

1. **Key Metrics**
   - Message latency
   - Delivery rate
   - Connection stability
   - Storage usage
   - Error rates

2. **Alerts**
   - High latency
   - Connection drops
   - Storage issues
   - Error spikes
   - Service health

## Security Considerations

1. **Message Security**
   - End-to-end encryption
   - Message signing
   - Access control
   - Content filtering

2. **Connection Security**
   - TLS encryption
   - Authentication
   - Rate limiting
   - DDoS protection

## Trade-offs and Alternatives

### Alternative Approaches
1. **WebSocket vs. Long Polling**
   - WebSocket: Better performance, more complex
   - Long Polling: Simpler, higher latency

2. **Centralized vs. Distributed**
   - Centralized: Simpler, single point of failure
   - Distributed: More complex, better scalability

### Trade-offs
1. **Consistency vs. Performance**
   - Strong consistency: Higher latency
   - Eventual consistency: Better performance

2. **Storage vs. Computation**
   - More storage: Faster retrieval
   - More computation: Lower storage cost 