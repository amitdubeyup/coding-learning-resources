# GraphQL Interview Questions & Answers

A comprehensive guide covering GraphQL fundamentals, schema design, performance optimization, and best practices for senior-level interviews.

## Table of Contents
1. [Core Concepts](#core-concepts)
2. [Schema Design](#schema-design)
3. [Queries & Mutations](#queries--mutations)
4. [Resolvers](#resolvers)
5. [Subscriptions](#subscriptions)
6. [Authentication & Authorization](#authentication--authorization)
7. [Performance Optimization](#performance-optimization)
8. [Error Handling](#error-handling)
9. [Federation & Microservices](#federation--microservices)
10. [Testing](#testing)
11. [Best Practices](#best-practices)
12. [GraphQL vs REST](#graphql-vs-rest)

---

## Core Concepts

### Q1: What is GraphQL and what problems does it solve?
**Answer:**
GraphQL is a query language for APIs and a runtime for executing those queries. Developed by Facebook in 2012, open-sourced in 2015.

**Key Problems Solved:**

| Problem | REST | GraphQL |
|---------|------|---------|
| Over-fetching | Get entire resource | Request only needed fields |
| Under-fetching | Multiple round trips | Single request for related data |
| Multiple versions | /v1, /v2 endpoints | Single evolving endpoint |
| Documentation | Separate (Swagger) | Introspective, self-documenting |
| Type safety | Optional | Required schema |

```graphql
# Query exactly what you need
query {
  user(id: "123") {
    name
    email
    posts(first: 5) {
      title
      createdAt
    }
  }
}
```

**Core Principles:**
- **Declarative data fetching:** Client specifies data needs
- **Strongly typed:** Schema defines data shape
- **Single endpoint:** POST /graphql
- **Hierarchical:** Query matches response structure

---

### Q2: Explain the GraphQL type system
**Answer:**

```graphql
# Scalar types (built-in)
type Scalars {
  id: ID!          # Unique identifier
  name: String     # UTF-8 string
  age: Int         # Signed 32-bit integer
  price: Float     # Double-precision float
  active: Boolean  # true or false
}

# Object type
type User {
  id: ID!
  name: String!
  email: String!
  posts: [Post!]!
}

# Enum type
enum Status {
  DRAFT
  PUBLISHED
  ARCHIVED
}

# Input type (for mutations)
input CreateUserInput {
  name: String!
  email: String!
  role: Role = USER
}

# Interface - abstract type
interface Node {
  id: ID!
}

type User implements Node {
  id: ID!
  name: String!
}

# Union type - one of several types
union SearchResult = User | Post | Comment

# Custom scalar
scalar DateTime
scalar JSON
scalar Upload
```

**Type Modifiers:**
- `String` - nullable string
- `String!` - non-null string
- `[String]` - nullable list of nullable strings
- `[String!]!` - non-null list of non-null strings

---

### Q3: What are the three main operations in GraphQL?
**Answer:**

```graphql
# 1. Query - Read data
query GetUser($id: ID!) {
  user(id: $id) {
    id
    name
    email
  }
}

# 2. Mutation - Write data
mutation CreateUser($input: CreateUserInput!) {
  createUser(input: $input) {
    id
    name
  }
}

# 3. Subscription - Real-time data
subscription OnMessageCreated($channelId: ID!) {
  messageCreated(channelId: $channelId) {
    id
    content
    user {
      name
    }
  }
}
```

**Query vs Mutation Execution:**
- **Queries:** Executed in parallel
- **Mutations:** Executed serially (in order)

---

## Schema Design

### Q4: How do you design a GraphQL schema?
**Answer:**

**Schema-First Design Approach:**

```graphql
# schema.graphql

# Root types
type Query {
  # By ID
  user(id: ID!): User
  post(id: ID!): Post
  
  # Lists with pagination
  users(first: Int, after: String): UserConnection!
  posts(filter: PostFilter, orderBy: PostOrderBy): PostConnection!
  
  # Search
  search(query: String!): [SearchResult!]!
  
  # Viewer pattern (current user)
  viewer: User
}

type Mutation {
  # Create
  createUser(input: CreateUserInput!): CreateUserPayload!
  createPost(input: CreatePostInput!): CreatePostPayload!
  
  # Update
  updateUser(id: ID!, input: UpdateUserInput!): UpdateUserPayload!
  
  # Delete
  deletePost(id: ID!): DeletePostPayload!
}

type Subscription {
  postCreated: Post!
  messageAdded(channelId: ID!): Message!
}

# Relay-style pagination
type UserConnection {
  edges: [UserEdge!]!
  pageInfo: PageInfo!
  totalCount: Int!
}

type UserEdge {
  cursor: String!
  node: User!
}

type PageInfo {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
  endCursor: String
}

# Payload pattern for mutations
type CreateUserPayload {
  user: User
  errors: [Error!]
}

type Error {
  field: String
  message: String!
}
```

---

### Q5: What is the Relay specification?
**Answer:**
Relay is a GraphQL client by Facebook with conventions for pagination, caching, and data fetching.

**Key Conventions:**

1. **Global Object Identification:**
```graphql
interface Node {
  id: ID!  # Globally unique, often base64(type:dbId)
}

type Query {
  node(id: ID!): Node
  nodes(ids: [ID!]!): [Node]!
}
```

2. **Connection-based Pagination:**
```graphql
type Query {
  users(
    first: Int
    after: String
    last: Int
    before: String
  ): UserConnection!
}

type UserConnection {
  edges: [UserEdge!]!
  pageInfo: PageInfo!
}

type UserEdge {
  cursor: String!  # Opaque cursor
  node: User!
}
```

3. **Mutation Input/Payload:**
```graphql
input CreateUserInput {
  name: String!
  email: String!
  clientMutationId: String  # For optimistic updates
}

type CreateUserPayload {
  user: User
  clientMutationId: String
}
```

---

### Q6: How do you handle polymorphism in GraphQL?
**Answer:**

**Using Interfaces:**
```graphql
interface Media {
  id: ID!
  title: String!
  url: String!
  createdAt: DateTime!
}

type Image implements Media {
  id: ID!
  title: String!
  url: String!
  createdAt: DateTime!
  width: Int!
  height: Int!
  altText: String
}

type Video implements Media {
  id: ID!
  title: String!
  url: String!
  createdAt: DateTime!
  duration: Int!
  thumbnail: String
}

type Query {
  media(id: ID!): Media
}
```

**Using Unions:**
```graphql
union SearchResult = User | Post | Comment | Tag

type Query {
  search(query: String!): [SearchResult!]!
}
```

**Querying Polymorphic Types:**
```graphql
query Search {
  search(query: "graphql") {
    ... on User {
      id
      name
      avatar
    }
    ... on Post {
      id
      title
      excerpt
    }
    ... on Comment {
      id
      body
    }
    __typename  # Returns the concrete type
  }
}
```

---

## Queries & Mutations

### Q7: Explain fragments and their use cases
**Answer:**
Fragments are reusable units of query logic.

```graphql
# Define fragment
fragment UserFields on User {
  id
  name
  email
  avatar
}

fragment PostPreview on Post {
  id
  title
  excerpt
  author {
    ...UserFields
  }
}

# Use in query
query GetDashboard {
  viewer {
    ...UserFields
    posts(first: 10) {
      ...PostPreview
    }
    followers(first: 5) {
      ...UserFields
    }
  }
  featuredPosts {
    ...PostPreview
  }
}

# Inline fragments for unions/interfaces
query Search {
  search(query: "graphql") {
    __typename
    ... on User {
      name
      email
    }
    ... on Post {
      title
      content
    }
  }
}
```

**Benefits:**
- DRY - Don't repeat yourself
- Colocate data requirements with components
- Type-safe with generated types

---

### Q8: How do you handle pagination?
**Answer:**

**Cursor-based Pagination (Recommended):**
```graphql
type Query {
  posts(
    first: Int
    after: String
    last: Int
    before: String
    filter: PostFilter
  ): PostConnection!
}

# Query
query GetPosts($cursor: String) {
  posts(first: 10, after: $cursor) {
    edges {
      cursor
      node {
        id
        title
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
    totalCount
  }
}
```

**Offset-based Pagination:**
```graphql
type Query {
  posts(limit: Int!, offset: Int!): PostPage!
}

type PostPage {
  items: [Post!]!
  total: Int!
  hasMore: Boolean!
}

# Query
query GetPosts {
  posts(limit: 10, offset: 20) {
    items {
      id
      title
    }
    total
    hasMore
  }
}
```

**Cursor vs Offset Comparison:**

| Feature | Cursor | Offset |
|---------|--------|--------|
| Real-time data | ✅ Stable | ❌ Duplicates/missing |
| Performance | ✅ O(1) | ❌ O(n) on large offsets |
| Random access | ❌ Sequential | ✅ Jump to page |
| Simplicity | Medium | Simple |

---

### Q9: How do you design mutations?
**Answer:**

```graphql
# Input types for complex arguments
input CreatePostInput {
  title: String!
  content: String!
  tags: [String!]
  status: PostStatus = DRAFT
}

# Payload with potential errors
type CreatePostPayload {
  post: Post
  userErrors: [UserError!]!
}

type UserError {
  field: [String!]!  # Path to field with error
  message: String!
  code: ErrorCode!
}

enum ErrorCode {
  INVALID
  REQUIRED
  DUPLICATE
  NOT_FOUND
  UNAUTHORIZED
}

type Mutation {
  createPost(input: CreatePostInput!): CreatePostPayload!
  
  # Bulk operations
  deletePosts(ids: [ID!]!): DeletePostsPayload!
  
  # Actions (not CRUD)
  publishPost(id: ID!): PublishPostPayload!
  likePost(id: ID!): LikePostPayload!
}
```

**Resolver Implementation:**
```typescript
const resolvers = {
  Mutation: {
    createPost: async (_, { input }, { user, prisma }) => {
      if (!user) {
        return {
          post: null,
          userErrors: [{
            field: [],
            message: 'Authentication required',
            code: 'UNAUTHORIZED'
          }]
        };
      }
      
      if (!input.title.trim()) {
        return {
          post: null,
          userErrors: [{
            field: ['input', 'title'],
            message: 'Title is required',
            code: 'REQUIRED'
          }]
        };
      }
      
      const post = await prisma.post.create({
        data: { ...input, authorId: user.id }
      });
      
      return { post, userErrors: [] };
    }
  }
};
```

---

## Resolvers

### Q10: How do resolvers work?
**Answer:**
Resolvers are functions that return data for each field in the schema.

```typescript
const resolvers = {
  Query: {
    user: (parent, args, context, info) => {
      // parent: Result from parent resolver (root resolvers receive undefined)
      // args: Arguments passed to the field
      // context: Shared across all resolvers (auth, DB, etc.)
      // info: Query AST and execution info
      return context.db.users.findById(args.id);
    },
    
    posts: async (_, { filter, first, after }, { db }) => {
      const cursor = after ? decodeCursor(after) : null;
      const posts = await db.posts.find({
        ...filter,
        ...(cursor && { createdAt: { $lt: cursor } })
      }).limit(first + 1);
      
      const hasNextPage = posts.length > first;
      const edges = posts.slice(0, first).map(post => ({
        cursor: encodeCursor(post.createdAt),
        node: post
      }));
      
      return {
        edges,
        pageInfo: {
          hasNextPage,
          endCursor: edges[edges.length - 1]?.cursor
        }
      };
    }
  },
  
  // Field resolvers
  User: {
    posts: (user, args, { db }) => {
      return db.posts.findByAuthorId(user.id, args);
    },
    
    fullName: (user) => {
      return `${user.firstName} ${user.lastName}`;
    }
  }
};
```

**Default Resolver:**
If no resolver is defined, GraphQL returns `parent[fieldName]`.

---

### Q11: What is the N+1 problem and how do you solve it?
**Answer:**
N+1 occurs when fetching N items triggers N additional database queries.

**Problem:**
```graphql
query {
  posts {      # 1 query for posts
    author {   # N queries for authors (one per post)
      name
    }
  }
}
```

**Solutions:**

**1. DataLoader (batching + caching):**
```typescript
import DataLoader from 'dataloader';

// Create loader per request
const createLoaders = (db) => ({
  userLoader: new DataLoader(async (ids) => {
    const users = await db.users.findByIds(ids);
    // Return in same order as requested ids
    const userMap = new Map(users.map(u => [u.id, u]));
    return ids.map(id => userMap.get(id));
  })
});

// Context
const context = ({ req }) => ({
  loaders: createLoaders(db)
});

// Resolver
const resolvers = {
  Post: {
    author: (post, _, { loaders }) => {
      return loaders.userLoader.load(post.authorId);
    }
  }
};
```

**2. Query lookahead with info:**
```typescript
import { fieldsList } from 'graphql-fields-list';

const resolvers = {
  Query: {
    posts: async (_, args, { db }, info) => {
      const fields = fieldsList(info);
      const includeAuthor = fields.includes('author');
      
      return db.posts.find({
        include: includeAuthor ? { author: true } : undefined
      });
    }
  }
};
```

**3. Join Monster (SQL-based):**
```typescript
import joinMonster from 'join-monster';

const User = {
  sqlTable: 'users',
  uniqueKey: 'id',
  fields: {
    posts: {
      sqlJoin: (userTable, postTable) =>
        `${userTable}.id = ${postTable}.author_id`
    }
  }
};
```

---

### Q12: How do you handle field-level complexity?
**Answer:**

```typescript
import { createComplexityLimitRule } from 'graphql-validation-complexity';

// Define costs in schema
const typeDefs = `
  type Query {
    users: [User!]! @complexity(value: 10)
    posts(first: Int!): [Post!]! @complexity(multipliers: ["first"])
  }
  
  type User {
    id: ID!
    name: String!
    posts: [Post!]! @complexity(value: 5)
  }
`;

// Or in code
const complexityRule = createComplexityLimitRule(1000, {
  scalarCost: 1,
  objectCost: 2,
  listFactor: 10,
  
  // Custom field costs
  fieldCost: (args, type, field) => {
    if (field.name === 'posts') {
      return args.first || 10;
    }
    return type.kind === 'OBJECT' ? 2 : 1;
  }
});

// Apply to validation
const server = new ApolloServer({
  typeDefs,
  resolvers,
  validationRules: [complexityRule]
});
```

---

## Subscriptions

### Q13: How do GraphQL subscriptions work?
**Answer:**
Subscriptions enable real-time updates via WebSocket connections.

```typescript
import { PubSub } from 'graphql-subscriptions';
import { createServer } from 'http';
import { WebSocketServer } from 'ws';
import { useServer } from 'graphql-ws/lib/use/ws';

const pubsub = new PubSub();

const typeDefs = `
  type Subscription {
    messageCreated(channelId: ID!): Message!
    userStatusChanged: UserStatus!
  }
  
  type Message {
    id: ID!
    content: String!
    user: User!
    createdAt: DateTime!
  }
`;

const resolvers = {
  Subscription: {
    messageCreated: {
      subscribe: (_, { channelId }) => {
        return pubsub.asyncIterator([`MESSAGE_CREATED_${channelId}`]);
      }
    },
    
    userStatusChanged: {
      subscribe: withFilter(
        () => pubsub.asyncIterator(['USER_STATUS']),
        (payload, variables, context) => {
          // Filter which clients receive updates
          return payload.userId !== context.userId;
        }
      )
    }
  },
  
  Mutation: {
    sendMessage: async (_, { input }, { user }) => {
      const message = await createMessage(input);
      
      // Publish event
      pubsub.publish(`MESSAGE_CREATED_${input.channelId}`, {
        messageCreated: message
      });
      
      return message;
    }
  }
};

// Setup WebSocket server
const httpServer = createServer(app);
const wsServer = new WebSocketServer({
  server: httpServer,
  path: '/graphql'
});

useServer(
  {
    schema,
    context: async (ctx) => {
      // Authenticate WebSocket connection
      const token = ctx.connectionParams?.authToken;
      const user = await validateToken(token);
      return { user, pubsub };
    }
  },
  wsServer
);
```

---

### Q14: What are the trade-offs of subscriptions vs polling?
**Answer:**

| Feature | Subscriptions | Polling |
|---------|--------------|---------|
| Latency | Real-time | Depends on interval |
| Server load | Per-connection overhead | More DB queries |
| Complexity | Higher (WebSocket) | Simple HTTP |
| Scalability | Needs Redis pub/sub | Stateless |
| Mobile | Battery impact | More control |
| Firewall | May be blocked | Always works |

**When to use subscriptions:**
- Chat applications
- Live notifications
- Collaborative editing
- Real-time dashboards
- Gaming

**When polling is better:**
- Infrequent updates
- Simple implementations
- High availability requirements
- Mobile apps (battery)

**Hybrid approach:**
```typescript
// Initial data via query
const { data } = useQuery(GET_MESSAGES);

// Real-time updates via subscription
useSubscription(MESSAGE_CREATED, {
  onData: ({ data }) => {
    // Merge with cache
    cache.modify({
      fields: {
        messages: (existing) => [...existing, data.messageCreated]
      }
    });
  }
});
```

---

## Authentication & Authorization

### Q15: How do you implement authentication in GraphQL?
**Answer:**

```typescript
import { ApolloServer } from '@apollo/server';
import jwt from 'jsonwebtoken';

// Context creation
const context = async ({ req }) => {
  const token = req.headers.authorization?.replace('Bearer ', '');
  
  let user = null;
  if (token) {
    try {
      const decoded = jwt.verify(token, process.env.JWT_SECRET);
      user = await db.users.findById(decoded.userId);
    } catch (e) {
      // Invalid token - user remains null
    }
  }
  
  return {
    user,
    db,
    loaders: createLoaders(db)
  };
};

// Auth directive
const typeDefs = `
  directive @auth(requires: Role = USER) on FIELD_DEFINITION
  
  enum Role {
    ADMIN
    USER
    GUEST
  }
  
  type Query {
    publicData: String
    userData: String @auth
    adminData: String @auth(requires: ADMIN)
  }
`;

// Directive transformer
import { mapSchema, getDirective, MapperKind } from '@graphql-tools/utils';

function authDirective(directiveName: string) {
  return (schema) => mapSchema(schema, {
    [MapperKind.OBJECT_FIELD]: (fieldConfig) => {
      const authDirective = getDirective(schema, fieldConfig, directiveName)?.[0];
      
      if (authDirective) {
        const { requires } = authDirective;
        const originalResolve = fieldConfig.resolve;
        
        fieldConfig.resolve = async (source, args, context, info) => {
          if (!context.user) {
            throw new AuthenticationError('Not authenticated');
          }
          
          if (requires && !hasRole(context.user, requires)) {
            throw new ForbiddenError('Not authorized');
          }
          
          return originalResolve(source, args, context, info);
        };
      }
      return fieldConfig;
    }
  });
}
```

---

### Q16: How do you implement field-level authorization?
**Answer:**

```typescript
// Schema with auth requirements
const typeDefs = `
  type User {
    id: ID!
    name: String!
    email: String! @auth(owner: true)
    posts: [Post!]!
    privateNotes: String @auth(requires: ADMIN)
  }
`;

// Resolver-level authorization
const resolvers = {
  User: {
    email: (user, _, { currentUser }) => {
      // Only owner or admin can see email
      if (currentUser?.id === user.id || currentUser?.role === 'ADMIN') {
        return user.email;
      }
      return null; // or throw ForbiddenError
    },
    
    privateNotes: (user, _, { currentUser }) => {
      if (currentUser?.role !== 'ADMIN') {
        throw new ForbiddenError('Admin access required');
      }
      return user.privateNotes;
    }
  },
  
  Mutation: {
    updatePost: async (_, { id, input }, { currentUser, db }) => {
      const post = await db.posts.findById(id);
      
      if (!post) {
        throw new NotFoundError('Post not found');
      }
      
      // Check ownership
      if (post.authorId !== currentUser?.id) {
        throw new ForbiddenError('Not your post');
      }
      
      return db.posts.update(id, input);
    }
  }
};

// Using graphql-shield
import { shield, rule, allow, deny } from 'graphql-shield';

const isAuthenticated = rule()((_, __, { user }) => !!user);
const isAdmin = rule()((_, __, { user }) => user?.role === 'ADMIN');
const isOwner = rule()((parent, __, { user }) => parent.userId === user?.id);

const permissions = shield({
  Query: {
    '*': allow,
    adminDashboard: isAdmin
  },
  Mutation: {
    '*': isAuthenticated,
    deleteUser: isAdmin
  },
  User: {
    email: isOwner,
    privateData: isAdmin
  }
});
```

---

## Performance Optimization

### Q17: How do you optimize GraphQL performance?
**Answer:**

**1. Query Complexity Analysis:**
```typescript
import depthLimit from 'graphql-depth-limit';
import { createComplexityLimitRule } from 'graphql-query-complexity';

const server = new ApolloServer({
  validationRules: [
    depthLimit(10),
    createComplexityLimitRule(1000)
  ]
});
```

**2. Persisted Queries:**
```typescript
// Client sends hash instead of full query
// POST /graphql
// { "extensions": { "persistedQuery": { "sha256Hash": "abc123" } } }

import { ApolloServerPluginPersistedQueries } from '@apollo/server/plugin/persistedQueries';

const server = new ApolloServer({
  plugins: [
    ApolloServerPluginPersistedQueries({
      cache: new RedisCache({ /* ... */ })
    })
  ]
});
```

**3. Caching:**
```typescript
// Field-level caching hints
const typeDefs = `
  type Post @cacheControl(maxAge: 60) {
    id: ID!
    title: String!
    author: User! @cacheControl(maxAge: 300)
    comments: [Comment!]! @cacheControl(maxAge: 30)
  }
`;

// Response cache plugin
import responseCachePlugin from '@apollo/server-plugin-response-cache';

const server = new ApolloServer({
  plugins: [
    responseCachePlugin({
      sessionId: ({ request }) => request.headers.authorization || null
    })
  ]
});
```

**4. DataLoader for batching:**
```typescript
const userLoader = new DataLoader(async (ids) => {
  const users = await db.users.findMany({ where: { id: { in: ids } } });
  return ids.map(id => users.find(u => u.id === id));
}, {
  cache: true,      // Within single request
  maxBatchSize: 100 // Batch size limit
});
```

**5. Query lookahead:**
```typescript
import graphqlFields from 'graphql-fields';

const resolvers = {
  Query: {
    posts: async (_, args, ctx, info) => {
      const fields = graphqlFields(info);
      const include = {};
      
      if (fields.author) {
        include.author = true;
      }
      if (fields.comments) {
        include.comments = { include: { user: !!fields.comments.user } };
      }
      
      return prisma.post.findMany({ include });
    }
  }
};
```

---

### Q18: How do you implement rate limiting?
**Answer:**

```typescript
import { RateLimiterRedis } from 'rate-limiter-flexible';
import Redis from 'ioredis';

const redis = new Redis();

const rateLimiter = new RateLimiterRedis({
  storeClient: redis,
  points: 100,      // requests
  duration: 60,     // per minute
  keyPrefix: 'graphql_rate_limit'
});

// Per-user rate limiting
const rateLimitPlugin = {
  async requestDidStart({ context }) {
    const key = context.user?.id || context.ip;
    
    try {
      await rateLimiter.consume(key);
    } catch (rejRes) {
      throw new RateLimitError(
        `Too many requests. Retry after ${rejRes.msBeforeNext / 1000}s`
      );
    }
  }
};

// Field-level rate limiting with directive
const typeDefs = `
  directive @rateLimit(
    max: Int!
    window: String!
    message: String
  ) on FIELD_DEFINITION
  
  type Mutation {
    sendEmail(to: String!): Boolean! @rateLimit(max: 10, window: "1h")
    createPost(input: PostInput!): Post! @rateLimit(max: 20, window: "1d")
  }
`;
```

---

## Error Handling

### Q19: How do you handle errors in GraphQL?
**Answer:**

```typescript
// Custom error classes
import { GraphQLError } from 'graphql';

class NotFoundError extends GraphQLError {
  constructor(resource: string) {
    super(`${resource} not found`, {
      extensions: {
        code: 'NOT_FOUND',
        http: { status: 404 }
      }
    });
  }
}

class ValidationError extends GraphQLError {
  constructor(message: string, field: string) {
    super(message, {
      extensions: {
        code: 'VALIDATION_ERROR',
        field,
        http: { status: 400 }
      }
    });
  }
}

// Error formatting
const server = new ApolloServer({
  formatError: (formattedError, error) => {
    // Log original error
    console.error(error);
    
    // Hide internal errors in production
    if (process.env.NODE_ENV === 'production') {
      if (formattedError.extensions?.code === 'INTERNAL_SERVER_ERROR') {
        return {
          message: 'Internal server error',
          extensions: { code: 'INTERNAL_SERVER_ERROR' }
        };
      }
    }
    
    return formattedError;
  }
});

// Mutation error pattern
type Mutation {
  createUser(input: CreateUserInput!): CreateUserPayload!
}

type CreateUserPayload {
  user: User
  errors: [MutationError!]!
}

type MutationError {
  field: String
  message: String!
  code: ErrorCode!
}

// Resolver with explicit errors
const resolvers = {
  Mutation: {
    createUser: async (_, { input }) => {
      const errors = [];
      
      if (!isValidEmail(input.email)) {
        errors.push({
          field: 'email',
          message: 'Invalid email format',
          code: 'INVALID_FORMAT'
        });
      }
      
      if (await emailExists(input.email)) {
        errors.push({
          field: 'email',
          message: 'Email already registered',
          code: 'DUPLICATE'
        });
      }
      
      if (errors.length > 0) {
        return { user: null, errors };
      }
      
      const user = await createUser(input);
      return { user, errors: [] };
    }
  }
};
```

---

## Federation & Microservices

### Q20: What is Apollo Federation?
**Answer:**
Federation allows composing multiple GraphQL services into a single graph.

**Gateway (Router):**
```yaml
# supergraph.yaml
subgraphs:
  users:
    routing_url: http://users-service:4001/graphql
    schema:
      subgraph_url: http://users-service:4001/graphql
  posts:
    routing_url: http://posts-service:4002/graphql
    schema:
      subgraph_url: http://posts-service:4002/graphql
  comments:
    routing_url: http://comments-service:4003/graphql
    schema:
      subgraph_url: http://comments-service:4003/graphql
```

**Users Subgraph:**
```graphql
extend schema @link(url: "https://specs.apollo.dev/federation/v2.0")

type User @key(fields: "id") {
  id: ID!
  name: String!
  email: String!
}

type Query {
  user(id: ID!): User
  me: User
}
```

**Posts Subgraph:**
```graphql
extend schema @link(url: "https://specs.apollo.dev/federation/v2.0")

type Post @key(fields: "id") {
  id: ID!
  title: String!
  content: String!
  author: User!  # Reference to User type
}

# Extend User from users subgraph
type User @key(fields: "id") {
  id: ID!
  posts: [Post!]!  # Add field to User
}

type Query {
  posts: [Post!]!
  post(id: ID!): Post
}
```

**Reference Resolver:**
```typescript
const resolvers = {
  User: {
    __resolveReference: async (user, { db }) => {
      // Called when another subgraph needs User data
      return db.users.findById(user.id);
    }
  }
};
```

---

### Q21: Explain Federation directives
**Answer:**

```graphql
# @key - defines entity's primary key
type User @key(fields: "id") {
  id: ID!
}

# Multiple keys
type Product @key(fields: "id") @key(fields: "sku") {
  id: ID!
  sku: String!
}

# Compound key
type Review @key(fields: "userId productId") {
  userId: ID!
  productId: ID!
}

# @shareable - field can be resolved by multiple subgraphs
type Product @key(fields: "id") {
  id: ID!
  name: String! @shareable
  price: Float! @shareable
}

# @external - field defined in another subgraph
extend type User @key(fields: "id") {
  id: ID! @external
  posts: [Post!]!  # Adds posts field to User
}

# @requires - field requires external fields
extend type User @key(fields: "id") {
  id: ID! @external
  email: String! @external
  
  # Requires email to compute
  emailDomain: String! @requires(fields: "email")
}

# @provides - hints about nested fields
type Post @key(fields: "id") {
  author: User! @provides(fields: "name")
}

# @override - takes ownership from another subgraph
type Product @key(fields: "id") {
  id: ID!
  # This subgraph now owns this field
  inStock: Boolean! @override(from: "inventory")
}
```

---

## Best Practices

### Q22: What are GraphQL schema design best practices?
**Answer:**

**1. Use meaningful names:**
```graphql
# Bad
type T1 { f1: String; f2: Int }

# Good
type User { name: String; age: Int }
```

**2. Consistent naming conventions:**
```graphql
# Types: PascalCase
type UserProfile { ... }

# Fields: camelCase
type User { firstName: String }

# Enums: SCREAMING_SNAKE_CASE
enum UserStatus { ACTIVE, INACTIVE, PENDING_VERIFICATION }

# Arguments: camelCase
type Query { user(userId: ID!): User }
```

**3. Nullable by default, require explicitly:**
```graphql
type Post {
  id: ID!           # Required
  title: String!    # Required
  subtitle: String  # Optional
  tags: [String!]!  # Required array, required items
}
```

**4. Use input types for mutations:**
```graphql
# Bad
mutation createUser(name: String!, email: String!, age: Int): User

# Good
input CreateUserInput {
  name: String!
  email: String!
  age: Int
}
mutation createUser(input: CreateUserInput!): CreateUserPayload!
```

**5. Return types for mutations:**
```graphql
# Include the modified entity and potential errors
type CreateUserPayload {
  user: User
  errors: [UserError!]!
}
```

**6. Use connections for lists:**
```graphql
type Query {
  # Bad
  posts: [Post!]!
  
  # Good
  posts(first: Int, after: String): PostConnection!
}
```

**7. Deprecation over removal:**
```graphql
type User {
  name: String! @deprecated(reason: "Use firstName and lastName")
  firstName: String!
  lastName: String!
}
```

---

### Q23: How do you version a GraphQL API?
**Answer:**

**GraphQL Best Practice: Don't version, evolve!**

**1. Add new fields (safe):**
```graphql
# v1
type User {
  name: String!
}

# v2 - just add fields
type User {
  name: String!
  firstName: String!
  lastName: String!
}
```

**2. Deprecate old fields:**
```graphql
type User {
  name: String! @deprecated(reason: "Use firstName/lastName. Will be removed 2026-01-01")
  firstName: String!
  lastName: String!
}
```

**3. Monitor deprecation usage:**
```typescript
const plugin = {
  requestDidStart() {
    return {
      didResolveOperation({ document }) {
        const deprecated = findDeprecatedFields(document);
        if (deprecated.length) {
          analytics.track('deprecated_field_usage', { fields: deprecated });
        }
      }
    };
  }
};
```

**4. Safe breaking changes with feature flags:**
```graphql
type Query {
  user(id: ID!, version: Int = 1): User
}

# Resolver
const resolvers = {
  Query: {
    user: (_, { id, version }) => {
      if (version === 2) {
        return getNewUserFormat(id);
      }
      return getLegacyUserFormat(id);
    }
  }
};
```

**5. Schema registry (Apollo):**
```bash
# Check for breaking changes before deploy
rover subgraph check my-graph --name users --schema ./schema.graphql
```

---

## GraphQL vs REST

### Q24: When to use GraphQL vs REST?
**Answer:**

| Aspect | GraphQL | REST |
|--------|---------|------|
| Data fetching | Client specifies | Server defines |
| Over/under-fetching | Minimal | Common |
| Endpoints | Single | Multiple |
| Versioning | Schema evolution | URL versioning |
| Caching | Complex (client-side) | HTTP caching |
| File uploads | Requires setup | Native |
| Learning curve | Steeper | Gentler |
| Tooling | Rich ecosystem | Mature ecosystem |
| Real-time | Native subscriptions | WebSockets separate |

**Choose GraphQL when:**
- Multiple clients (mobile, web, IoT) with different data needs
- Rapid frontend iteration
- Complex, interconnected data
- Real-time features needed
- Reducing round trips is critical

**Choose REST when:**
- Simple CRUD operations
- Heavy caching requirements
- File upload/download focus
- Public APIs with simple data
- Team unfamiliar with GraphQL

**Hybrid approach:**
```
                    ┌─────────────────┐
                    │   API Gateway   │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
       ┌──────▼──────┐ ┌─────▼─────┐ ┌──────▼──────┐
       │  GraphQL    │ │  REST     │ │  WebSocket  │
       │  (queries)  │ │  (files)  │ │  (real-time)│
       └─────────────┘ └───────────┘ └─────────────┘
```

---

## Quick Reference

### Common Patterns

```graphql
# Viewer pattern
type Query {
  viewer: User  # Current authenticated user
}

# Node interface (Relay)
interface Node {
  id: ID!
}

type Query {
  node(id: ID!): Node
}

# Connection pattern
type UserConnection {
  edges: [UserEdge!]!
  pageInfo: PageInfo!
  totalCount: Int!
}

# Payload pattern
type MutationPayload {
  success: Boolean!
  message: String
  errors: [Error!]
  record: Entity
}

# Filter input
input PostFilter {
  status: PostStatus
  authorId: ID
  createdAfter: DateTime
  search: String
}

# Order input
input PostOrder {
  field: PostOrderField!
  direction: OrderDirection!
}

enum OrderDirection {
  ASC
  DESC
}
```

### Apollo Client Setup (React)

```typescript
import { ApolloClient, InMemoryCache, ApolloProvider, gql, useQuery, useMutation } from '@apollo/client';

const client = new ApolloClient({
  uri: '/graphql',
  cache: new InMemoryCache({
    typePolicies: {
      Query: {
        fields: {
          posts: {
            keyArgs: ['filter'],
            merge(existing = { edges: [] }, incoming) {
              return {
                ...incoming,
                edges: [...existing.edges, ...incoming.edges]
              };
            }
          }
        }
      }
    }
  })
});

// Hook usage
function Posts() {
  const { data, loading, fetchMore } = useQuery(GET_POSTS);
  const [createPost] = useMutation(CREATE_POST, {
    update(cache, { data }) {
      cache.modify({
        fields: {
          posts(existing) {
            return {
              ...existing,
              edges: [{ node: data.createPost.post }, ...existing.edges]
            };
          }
        }
      });
    }
  });
}
```

---

*Last updated: February 2026*
