# Interview Q&A for Amit Dubey

## Introductions

### 1. Tell me about yourself (including brief self-introduction or introduction).
Hello, I'm **Amit Dubey**, a passionate and experienced **Senior Software Engineer** with over 8 years in the tech industry, specializing in building robust, scalable full-stack applications for dynamic sectors like fintech, logistics, and SaaS.

- **Career Journey**: Started with a B.Tech in Computer Science from Rajasthan Technical University, evolving from junior developer to team lead.
- **Key Achievements**: Contributed to projects handling millions of transactions and searches, e.g., loan systems processing ₹50Cr+ monthly and recruitment platforms serving 100+ enterprise clients.
- **Technical Expertise**:
  - **Frontend**: React, Vue.js, Angular, TypeScript.
  - **Backend**: Node.js, Express, Python, FastAPI.
  - **Databases**: MongoDB, PostgreSQL, Redis, Elasticsearch.
  - **Cloud & Tools**: AWS (EC2, S3, Lambda, RDS), microservices, event-driven architectures, CI/CD with Jenkins, AI integrations (LangChain, OpenAI APIs).
- **Leadership**: Mentored teams, conducted interviews, drove decisions improving performance by up to 70%.
- **Education**: Pursuing M.Tech in AI & Data Science at IIT Dhanbad.
- **Personal**: Enjoy coding challenges (LeetCode), swimming, and staying updated with trends.
- **Motivation**: Excited to leverage skills in innovative projects for real impact.

### 2. Introduce yourself.
Hi, my name is **Amit Dubey**. I'm a **Senior Software Engineer** with 8+ years of hands-on experience in full-stack development for fintech, logistics, and SaaS.

- **Career Path**: Began at NSGA (transport platforms), progressed through HostBooks, Simplilearn, Shypmax, Arthmate, to HireEZ (handling 500K+ learners to 1M+ searches).
- **Skills**:
  - Frontend: React, Vue.js.
  - Backend: Node.js, Python.
  - Databases: MongoDB, PostgreSQL.
  - Cloud: AWS deployments.
- **Highlights**: Implemented AI features, optimized APIs to sub-10ms latencies, migrated to microservices.
- **Education**: B.Tech from RTU, M.Tech in AI & Data Science at IIT Dhanbad.
- **Strengths**: Problem-solving, collaboration, quality assurance, compliance (e.g., RBI standards).
- **Interests**: Coding, swimming, exploring technologies.
- **Aspiration**: Bring experience to new challenges in innovative teams.

## Project Overview

### 3. Describe your last/recent/most recent/previous project.
My most recent project at **HireEZ** is the **Company Intelligence module**, revolutionizing recruitment with deep hiring insights.

- **Overview**: Aggregates data from 10+ sources (Glassdoor, LinkedIn, Crunchbase) via ETL pipelines.
- **Key Features**:
  - **Data Ingestion**: Python scripts with Pandas for transformation, validation, deduplication.
  - **Talent Pool Management**: 100K+ profiles with filters/tags, using MongoDB and Elasticsearch.
  - **AI Sourcing**: LangChain + OpenAI for boolean searches, job analysis, predictive analytics.
  - **Real-Time Updates**: Event-driven with Redis Streams.
  - **Security**: RBAC with JWT, granular permissions.
  - **Reporting**: Automated PDFs/Excel with Puppeteer/ExcelJS.
  - **Insights**: AI-powered predictions, trends, benchmarks.
- **Scalability**: Optimized for 1M+ searches with caching, horizontal scaling on AWS.
- **Impact**: Reduced sourcing time by 40%, increased client satisfaction.

### 4. Discussion on the most recent project undertaken in the previous organization.
At **Arthmate**, I developed a **Loan Origination System (LOS)** streamlining lending for financial institutions.

- **Scale**: Processed 10K+ applications daily, ₹50Cr+ monthly transactions.
- **Features**:
  - Co-lending integrations with 8+ banks.
  - Bureau checks (CIBIL, Experian, CRIF) with error handling.
  - Loan management: Schedules, EMI, penalties, settlements in PostgreSQL.
  - Underwriting: 50+ rules, 70% manual reduction.
  - Payments: Razorpay/Cashfree integrations.
- **Security**: PII encryption, audit trails for RBI compliance.
- **Architecture**: Migrated to microservices.
- **Monitoring**: Grafana dashboards for KPIs (approval rates, TAT, NPA).
- **Leadership**: Led 5 engineers, daily standups, reviews.

### 5. Explain your recent/current/most recent project (including architecture and tech stack).
**HireEZ** is an intelligent recruitment platform using **microservices architecture** for modularity and scalability.

- **Architecture**:
  - Services: Data aggregation, AI processing, user management, reporting.
  - Containers: Docker on AWS EC2/Lambda.
  - Communication: Event-driven with Kafka, Redis pub-sub.
- **Tech Stack**:
  - **APIs**: Node.js (Express), Python (FastAPI) with async/await.
  - **Data**: MongoDB (flexible), PostgreSQL (transactions), Redis (caching), Elasticsearch (search).
  - **Frontend**: React + TypeScript, Redux, Axios.
  - **AI**: LangChain + OpenAI for generative tasks.
  - **Deployment**: CI/CD with Jenkins, blue-green deployments.
  - **Security**: JWT, OAuth, RBAC, encryption.
  - **Monitoring**: ELK, Prometheus, Grafana.
- **Scalability**: Load balancers, auto-scaling for 1M+ searches.

### 6. About recent challenging project.
The **multi-carrier shipping platform** at **Shypmax** was highly challenging, integrating 15+ couriers.

- **Challenges**:
  - Diverse APIs (SOAP/REST, poor docs), handled with adapter patterns and middleware.
  - Real-time tracking for 10K+ users: WebSockets + Redis, reduced load by 50%.
  - Rate comparisons: Algorithms saving 20% costs.
  - NDR automation: Retry logic, escalations.
  - Peak loads: Event-driven with Kafka, zero message loss.
- **Improvements**: Vue.js migration boosted performance 60%, conversion 25%.
- **Monitoring**: ELK + Grafana for SLAs.
- **Leadership**: Mentored 3 juniors, collaborated with teams.
- **Outcome**: Scalable foundation for millions in transactions.

## Roles and Responsibilities

### 7. What were your roles and responsibilities in your last/current/most recent project?
At **HireEZ**, my roles include:

- **Leadership**: Lead modules, manage 4 engineers, conduct standups/reviews.
- **Technical**: Architect event-driven systems (Redis/Kafka), implement AI (LangChain/OpenAI), optimize for 1M+ searches.
- **Collaboration**: Gather requirements, present demos, resolve blockers.
- **Security/Compliance**: Implement RBAC, encryption.
- **Mentoring**: Guide juniors, conduct interviews.

### 8. Role and responsibility in the project.
Across projects, my roles encompass:

- **Development**: Full-stack APIs, databases, integrations.
- **Optimization**: Performance tuning, migrations to microservices.
- **Leadership**: Mentoring, conflict resolution, compliance.
- **Lifecycle**: Analysis, coding, testing, deployment, support.

### 9. Roles and responsibilities handled.
- **End-to-End**: From ideation to maintenance.
- **Team**: Management, collaboration.
- **Quality**: Testing, reviews.
- **Compliance**: Security, audits.

## Architecture and Design

### 10. What was the architecture of the project?
**HireEZ** uses **microservices architecture**:

- Independent services for scalability.
- Event-driven (Redis/Kafka).
- Containerized (Docker), deployed on AWS.
- API gateways for routing.
- Polyglot databases, ELK monitoring.

### 11. Explain your project architecture and design.
For large projects like **Arthmate**:

- **Microservices**: Domain-specific, RESTful APIs, message queues.
- **Data**: PostgreSQL (ACID), MongoDB (flexible).
- **Security**: JWT, RBAC, encryption.
- **Monitoring**: Grafana.
- **Principles**: SOLID, DDD, CI/CD.

### 12. How would you design for a large project?
- **Architecture**: Microservices, event-driven.
- **Tools**: Kubernetes, Kafka.
- **Data**: Polyglot, caching.
- **Frontend**: React, Redux.
- **Security**: OWASP.
- **Process**: Agile, CI/CD, monitoring.

### 13. How would you design and implement global state management for a large project?
- **Frontend**: Redux Toolkit.
- **Server**: Redis, event sourcing.
- **Distributed**: Sagas, consistency patterns.

### 14. Architecture of the project and deployment.
- **Architecture**: Microservices on AWS.
- **Deployment**: Jenkins CI/CD, Docker, load balancers, monitoring.

## Technical Choices

### 15. Why did you choose PHP for your project?
In legacy projects like **HostBooks**, PHP for simplicity and LAMP. Now prefer Node.js/Python for scalability.

### 16. Why was PHP chosen for the project?
Ease, community, quick MVPs. Modern: async languages.

## Data Flow and Backend Basics

### 17. How does an API work?
- Defines endpoints for HTTP methods.
- Processes requests, queries DB, returns JSON.
- Example: HireEZ fetches data from MongoDB.

### 18. What's the flow of data from frontend to backend and database?
- Frontend → API gateway → Backend validation → DB query → Response.
- Example: Search → Elasticsearch → Results.

## Authentication, Authorization, Security

### 19. How did you handle authentication?
- JWT for sessions, OAuth for enterprises, MFA in Arthmate.

### 20. What is Authentication and Authorization and their differences and types?
- **Auth**: Verifies identity (passwords, JWT, MFA).
- **Authz**: Controls access (RBAC, ABAC).
- Types: Basic, token, etc.

## Database and Indexing

### 21. Explain the difference between MySQL and MongoDB.
- **MySQL**: Relational, ACID, SQL, joins.
- **MongoDB**: NoSQL, flexible, scaling.

### 22. What is Indexing and its types? How indexing works (in depth)?
- Creates structures (B-trees) for fast lookup.
- Types: Clustered, non-clustered, unique, composite.
- Works: Maps keys to locations, O(log n) vs. O(n).

### 23. Types of indexing.
- Primary, secondary, unique, composite, full-text, spatial, hash, bitmap.

### 24. Explain indexing in a database.
- Speeds queries via sorted indexes, binary search.

### 25. When performing multi-column/composite indexing, do you have any priority? Does the order matter?
- Order matters: Selective columns first.
- Priority: High-cardinality, frequent queries.

### 26. Query optimization and indexing: what happens without indexes inside databases?
- Full scans, slow, high I/O.

## Performance and Optimization

### 27. How do you optimize queries?
- Indexes, EXPLAIN, joins, pagination, caching.

### 28. Query optimization: what will you do when a query is stuck?
- Analyze plan, add indexes, rewrite, denormalize.

### 29. How have you optimized an API?
In my experience, particularly at Arthmate's Loan Origination System, I've optimized APIs through several key strategies:

- **Caching Mechanisms**: Implemented Redis for in-memory caching to reduce database load, achieving sub-10ms response times for frequently accessed endpoints.
- **Pagination and Data Chunking**: Used cursor-based pagination to efficiently handle large datasets, preventing memory overload and improving user experience.
- **Asynchronous Processing**: Leveraged async/await in Node.js and Python backends to handle concurrent requests without blocking threads, increasing throughput.
- **Database Indexing**: Added composite indexes on high-cardinality fields in PostgreSQL to speed up queries.
- **Query Optimization**: Utilized EXPLAIN plans to identify bottlenecks and rewrote complex joins or denormalized data where necessary.
- **CDN Integration**: Employed AWS CloudFront for static assets and API responses to reduce latency globally.

These optimizations resulted in significant performance improvements, such as reducing API latency from 1000ms to 10-20ms in some cases.

### 30. Pagination, infinite scroll, lazy loading.
- **Pagination**: Divides large datasets into smaller, manageable pages (e.g., 10-50 items per page) to improve load times and user navigation. Implemented in APIs using offset or cursor-based methods.
- **Infinite Scroll**: Loads content dynamically as the user scrolls, providing a seamless experience for large lists without page breaks. Useful for social media feeds, but can impact performance if not optimized.
- **Lazy Loading**: Defers loading of non-critical resources (images, components) until they are needed, reducing initial page load time and bandwidth usage. Commonly used in React with libraries like react-lazyload.

### 31. If there are around 10k records, how will you send the data to the API — all together or in chunks?
Sending all 10k records at once would overwhelm the client and server, leading to slow response times, high memory usage, and poor user experience. Instead, send data in chunks using pagination (e.g., 100 records per page) to allow efficient loading, caching, and navigation.

### 32. How did you achieve 10–20 ms latency when it was 1000 ms?
By implementing multi-layered optimizations: added Redis caching for frequent queries, created database indexes on key fields, and integrated CDNs like CloudFront to serve content closer to users, reducing network latency significantly.

### 33. Which pagination techniques are known? How is pagination implemented in live systems?
Common techniques include:
- **Offset-based**: Uses LIMIT and OFFSET (e.g., SQL), simple but slow for large datasets.
- **Cursor-based**: Uses a unique identifier (cursor) from the last item, efficient for large scales.
- **Keyset Pagination**: Similar to cursor, based on sortable keys.
In live systems like HireEZ, cursor-based pagination is preferred for scalability, especially with real-time data.

### 34. Drawbacks of limit/offset pagination and why it doesn't scale for infinite scroll/real-time feeds.
Offset-based pagination requires skipping rows (e.g., OFFSET 10000), which is slow on large tables as the database must scan all preceding rows. It also leads to inconsistent results if new items are inserted, causing duplicates or misses. For infinite scroll or real-time feeds, it doesn't scale well because it can't handle dynamic updates efficiently; cursor-based methods are better for maintaining order and performance.

## Algorithms and Data Structures

### 35. Find the second largest number in an array and explain time and space complexity.
- Iterate, track max/second. **Time**: O(n), **Space**: O(1).

### 36. Explain why sorting is less efficient for finding the second largest number in the array.
- Sorting: O(n log n) vs. Linear: O(n).

### 37. Algorithm: finding second largest element.
- Initialize, update in loop.

### 38. Approach to find the second largest element/second highest number in an array; explain time and space complexity and edge cases.
- Linear pass. **Time**: O(n), **Space**: O(1). **Edge cases**: <2 elements, all equal.

### 39. Why is a sorting-based method less optimal for second largest; compare approaches including different sorting options.
- Sorting overkill; linear direct.

### 40. Algorithm: palindrome (string/number) with time and space complexity.
- Reverse compare. **Time**: O(n), **Space**: O(n) or O(1) in-place.

### 41. Explain palindrome checking for strings (including special characters) with time and space complexity.
- Two pointers, skip specials. **Time**: O(n), **Space**: O(1).

### 42. Explain palindrome logic for numbers/strings with complexity.
- Reverse compare. Numbers: O(d).

### 43. String palindrome using different approaches and complexities.
- Iterative: O(n) O(1); Recursive: O(n) O(n); Reverse: O(n) O(n).

### 44. How do you access a binary tree?
- Traversals: inorder, preorder, postorder, level-order.

### 45. Difference between a tree and a graph.
- Tree: Acyclic connected; Graph: Cycles possible.

### 46. How do you do DFS in a binary tree — time and space complexity for best and worst case?
- Recursive. **Time**: O(n), **Space**: O(h) best, O(n) worst.

### 47. Binary tree: explain BFS and DFS with time and space complexity; include queue size in BFS.
- **BFS**: Queue, O(n) time, O(w) space.
- **DFS**: Stack, O(n) time, O(h) space.

### 48. What is BFS? Provide algorithm of BFS on a binary tree.
- Level-order: Queue, enqueue root, process children.

### 49. What is DFS? Provide algorithmic explanation.
- Depth-first: Stack/recursion, explore deep.

### 50. Sorting algorithms (bubble, insertion, etc.): which is more optimal with time and space complexity and why certain complexities are vs?
- **Merge sort**: O(n log n) time, O(n) space, stable. Bubble/insertion: O(n^2) worst.

### 51. Given two sorted arrays of sizes m and n−m, how to merge into a single sorted array; provide time and space complexity.
- Two pointers. **Time**: O(m+n), **Space**: O(m+n).

### 52. Merge two arrays; discuss time and space complexity.
- Same.

### 53. Explain second-highest number using different approaches and complexities.
- Linear: O(n) O(1); Sort: O(n log n); Heap: O(n log k).

## Spring/Java Specifics

### 54. Does Spring Boot support asynchronous processing?
Yes, Spring Boot supports asynchronous processing through the @Async annotation for methods and CompletableFuture for reactive programming, allowing non-blocking operations to improve concurrency and responsiveness.

### 55. How do we do caching in Spring Boot for local caching — what does the cache support?
Use the @Cacheable annotation on methods to cache results. Supports providers like EhCache or Caffeine for local caching, with features like TTL (time-to-live), eviction policies (LRU, LFU), and cache size limits to manage memory.

### 56. What challenges have been faced working with Java, Spring Boot, and Hibernate JPA?
Common challenges include N+1 query problems (excessive DB calls), managing lazy loading to avoid session issues, and handling transactions for data consistency. Resolved by using fetch joins, @Transactional, and profiling with tools like Hibernate Statistics.

### 57. What are string literals in Java, and how is memory managed for them?
String literals are immutable objects created in the string pool (heap). Memory is managed by the JVM's garbage collector; duplicates are reused from the pool to save space.

### 58. Difference between StringBuffer and StringBuilder.
StringBuffer is thread-safe (synchronized) but slower due to locks. StringBuilder is faster and non-synchronized, suitable for single-threaded scenarios.

### 59. What is synchronization in Java, and why is it used?
Synchronization ensures thread safety by allowing only one thread to access a critical section at a time, using locks to prevent race conditions and data corruption.

### 60. What is asynchronous programming, and how has it been implemented in projects?
Asynchronous programming allows tasks to run without blocking the main thread, improving performance. In projects, implemented using async/await in Node.js, promises in JavaScript, and @Async in Spring Boot for concurrent operations.

### 61. How are other threads notified when an asynchronous task completes?
Through callbacks (functions executed on completion), events (publish-subscribe), or futures/promises that resolve with results.

## Frontend and State Management

### 62. Which is more comfortable: Frontend or Backend?
Both, but I lean towards backend for complex logic, data processing, and scalability, while frontend for user experience. Full-stack experience allows balancing both.

### 63. Have you used any third-party library?
Yes, libraries like Axios for HTTP requests, Lodash for utility functions, and Chart.js for data visualization to enhance functionality and reduce development time.

### 64. Issues faced in state management; how was it handled?
Faced prop drilling in React, leading to complex component trees. Handled by implementing Redux for centralized state management, improving maintainability.

### 65. How to do state management in React?
Use useState for local component state, Context API for prop drilling avoidance, and Redux Toolkit for global, complex state with actions and reducers.

### 66. Components re-rendering solution.
Prevent unnecessary re-renders using React.memo for components, useMemo for expensive computations, and useCallback for stable function references.

## Challenges, Issues, and Production Handling

### 67. Describe some challenges faced in your project and how they were overcome.
Challenges included integrating diverse APIs with varying standards; overcome by building adapter patterns and middleware. Performance bottlenecks were addressed through caching, indexing, and code profiling.

### 68. What were the biggest challenges in the previous/current project?
Scaling the Loan Origination System at Arthmate to handle 10K+ daily applications; overcome by migrating to microservices architecture for better decoupling and horizontal scaling.

### 69. What challenges did you face in your last/current project and how did you resolve them (Backend and Frontend)?
Backend: Handling large datasets with ETL pipelines for data processing. Frontend: Managing complex state with Redux to avoid prop drilling and improve performance.

### 70. Share 2–3 challenges faced, followed by handling counter-questions.
1. Implementing real-time features; used WebSockets for bidirectional communication.
2. Third-party integrations; developed middleware for standardization.
3. Ensuring security; applied encryption and RBAC.

### 71. Production issue handling: how did you resolve production issues?
Monitored logs (ELK stack), reproduced issues in staging, applied fixes, and deployed via CI/CD with rollback plans.

### 72. How do you debug an issue? Steps for debugging an API issue.
1. Reproduce the issue in a controlled environment.
2. Check logs and error messages.
3. Use breakpoints or profilers to inspect code flow.
4. Test fixes incrementally.

### 73. How were backend errors viewed/logged when they occurred?
Used ELK stack for centralized logging and visualization, and Winston logger in Node.js for structured error logging.

### 74. How would you resolve a client issue where recent deployment changes are not reflecting only on the client machine?
Clear browser cache, check CDN invalidation, or advise hard refresh. If persistent, investigate network issues or deployment inconsistencies.

### 75. Tell something worked on in backend and challenges faced.
Developed loan approval workflows in the backend; faced concurrency issues with multiple users, resolved using database transactions and optimistic locking.

### 76. How to approach production bugs?
Gather details from users/logs, reproduce in dev/staging, debug, implement fix, test, and deploy with monitoring.

### 77. In past experience where a problem was identified and debugged independently, how was it fixed?
Identified a GST calculation bug in HostBooks; debugged by reviewing logs and code, fixed by correcting the formula and adding unit tests.

### 78. Production issues and how they were resolved.
Handled downtime by implementing failover to backup servers and load balancers, then root-caused and patched the issue.

### 79. What would be done if a bug is discovered just before launch?
Assess severity and impact; if critical, fix immediately and re-test; otherwise, delay launch or deploy a hotfix post-launch.

## PR, Collaboration, and Team

### 80. What are PR merging strategies?
Merge: Keeps full history. Squash: Combines commits into one. Rebase: Linear history by replaying commits.

### 81. How do you collaborate with team members?
Through daily standups, Jira for task tracking, code reviews, and pair programming to ensure quality and alignment.

### 82. How did you resolve conflicts between teams? Provide scenarios.
Used data-driven discussions; e.g., in a feature prioritization conflict, presented metrics on user impact to reach consensus.

### 83. How were conflicts solved with teammates without arguments?
By listening actively, focusing on facts and shared goals, and finding compromises.

### 84. How will conflicts within team members be handled?
Through open dialogue, mediation if needed, and focusing on solutions rather than blame.

### 85. Business model and how teams communicate.
Followed Agile methodology; teams communicate via Slack for instant messaging, Jira for tasks, and weekly syncs.

### 86. If a conflict arises with product owner and technical lead over an implementation decision, how would it be handled?
Discuss trade-offs in terms of time, cost, and quality; involve stakeholders and decide based on business priorities.

## Decision-Making and Prioritization

### 87. Describe a situation where something was achieved; explain the approach.
Optimized a slow query at Arthmate by profiling with EXPLAIN, adding indexes, and rewriting joins, reducing execution time by 70%.

### 88. Can you describe a scenario where two options had to be chosen and the decision criteria used?
Chose PostgreSQL over MongoDB for transactional data at Arthmate based on ACID compliance and scalability needs.

### 89. Suppose multiple tasks are all priority before a deadline — what procedure is followed to handle that?
Use MoSCoW method: Must-have, Should-have, Could-have, Won't-have to prioritize based on impact.

### 90. How do you prioritize 20 tasks?
Use Eisenhower matrix: Urgent/Important to categorize and focus on high-impact tasks first.

## Responsibilities and Contributions

### 91. What was the contribution in the project?
Led development of key modules, optimized performance, and mentored junior developers.

### 92. Tell about a task completed that evoked pride; challenges faced and how they were overcome.
Migrated monolithic app to microservices at Arthmate; overcame data consistency challenges with event sourcing.

### 93. Tell a project worked on in the last 6–12 months, challenges faced, and how they were resolved; strengths in coding, testing, or debugging.
Worked on HireEZ's AI sourcing module; integrated LangChain with OpenAI, resolved API rate limits with caching; strengths in debugging complex integrations.

## Feature and Modules

### 94. What features were implemented on this project?
Company intelligence aggregation, AI-powered sourcing, and RBAC for security.

### 95. Microservice concepts and module-specific work.
Yes, worked on decoupled services for data ingestion and AI processing, ensuring scalability.

### 96. Cloud platform worked on.
Primarily AWS, using EC2, S3, Lambda, RDS for deployments.

## Scenario-Based and Follow-Ups

### 97. Follow-up questions on the project explained.
Ensured data privacy with encryption and compliance with regulations like GDPR.

### 98. Follow-up on challenges and project-related questions.
Monitored KPIs like response times and maintained SLAs through optimizations.

### 99. Scenario-based questions related to real-time project experiences.
Handled traffic spikes by auto-scaling on AWS and optimizing queries.

### 100. Project-related follow-up questions.
Implemented security measures and conducted regular audits.

### 101. Cross questions on the related project/tech stack.
Node.js for its event-driven nature, enabling high scalability.

## Miscellaneous

### 102. What would be done if assigned work that is not liked?
Discuss with manager to understand value, seek alternatives, or accept for team growth.

### 103. Did any third-party plugins or APIs get used? If yes, explain.
Yes, payment gateways like Razorpay and external APIs for data enrichment.

### 104. How to gather requirements from a client?
Through client meetings, user stories, and prototypes to clarify needs.

### 105. How are requirements gathered and what is the approach to system design and decision-making?
Gathered via Agile ceremonies; designed with docs, considering scalability and maintainability.

### 108. Miscellaneous practice prompts.
- Practice STAR (Situation, Task, Action, Result) for behavioral questions.
- Mock interviews: Time yourself, record responses.
- Focus on metrics, challenges, resolutions.

