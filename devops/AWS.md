# AWS Interview Questions for Developers

This document contains over 100 AWS interview questions, focusing on services commonly used by developers in microservices, event-driven, and distributed architectures. Questions range from basic to advanced, including scenario-based problems.

## Table of Contents
1. [Basic AWS Concepts](#1-basic-aws-concepts)
2. [EC2 (Elastic Compute Cloud)](#2-ec2-elastic-compute-cloud)
3. [S3 (Simple Storage Service)](#3-s3-simple-storage-service)
4. [Lambda](#4-lambda)
5. [API Gateway](#5-api-gateway)
6. [DynamoDB](#6-dynamodb)
7. [RDS (Relational Database Service)](#7-rds-relational-database-service)
8. [VPC (Virtual Private Cloud)](#8-vpc-virtual-private-cloud)
9. [IAM (Identity and Access Management)](#9-iam-identity-and-access-management)
10. [CloudWatch](#10-cloudwatch)
11. [CloudFormation](#11-cloudformation)
12. [ECS/EKS](#12-ecseks)
13. [SNS/SQS](#13-snssqs)
14. [CodePipeline/CodeBuild](#14-codepipelinecodebuild)
15. [CloudFront](#15-cloudfront)
16. [Route 53](#16-route-53)
17. [KMS (Key Management Service)](#17-kms-key-management-service)
18. [Scenario-Based Questions](#18-scenario-based-questions)

## 1. Basic AWS Concepts

1. What is AWS and what are its main benefits?
2. Explain the AWS Global Infrastructure (Regions, Availability Zones, Edge Locations).
3. What is the difference between IaaS, PaaS, and SaaS?
4. How does AWS pricing work? Explain the pay-as-you-go model.
5. What is the AWS Free Tier and what are its limitations?
6. Explain AWS Shared Responsibility Model.
7. What are AWS Service Level Agreements (SLAs)?
8. How do you secure your AWS account?
9. What is AWS Organizations and when would you use it?
10. Explain AWS Resource Tags and their importance.

## 2. EC2 (Elastic Compute Cloud)

11. What is EC2 and what are its main use cases?
12. Explain different EC2 instance types (t2, m5, c5, etc.) and their use cases.
13. What is an AMI (Amazon Machine Image)?
14. How do you launch an EC2 instance?
15. Explain EC2 Security Groups vs Network ACLs.
16. What is an Elastic IP and when would you use it?
17. How do you connect to an EC2 instance?
18. Explain EC2 Auto Scaling and its components.
19. What is EC2 Spot Instances and when would you use them?
20. How do you monitor EC2 instances?
21. Explain EC2 Instance Store vs EBS (Elastic Block Store).
22. What is EC2 User Data and how is it used?
23. How do you create a custom AMI?
24. Explain EC2 Placement Groups and their types.
25. What is EC2 Reserved Instances and Savings Plans?

## 3. S3 (Simple Storage Service)

26. What is Amazon S3 and what are its main features?
27. Explain S3 storage classes (Standard, IA, Glacier, etc.).
28. What is an S3 bucket and what are the naming conventions?
29. How do you secure S3 buckets?
30. Explain S3 versioning and its benefits.
31. What is S3 Static Website Hosting?
32. How do you implement S3 cross-region replication?
33. Explain S3 lifecycle policies.
34. What is S3 Transfer Acceleration?
35. How do you encrypt data in S3?
36. Explain S3 event notifications.
37. What is S3 Select and S3 Glacier Select?
38. How do you optimize S3 performance?
39. Explain S3 access points.
40. What is S3 Batch Operations?

## 4. Lambda

41. What is AWS Lambda and what are its main benefits?
42. Explain Lambda function lifecycle.
43. What languages does Lambda support?
44. How do you trigger Lambda functions?
45. Explain Lambda layers and their use cases.
46. What is Lambda@Edge?
47. How do you monitor Lambda functions?
48. Explain Lambda cold starts and how to optimize them.
49. What is the maximum execution time for a Lambda function?
50. How do you handle errors in Lambda functions?
51. Explain Lambda environment variables.
52. What is Lambda VPC configuration?
53. How do you version Lambda functions?
54. Explain Lambda aliases.
55. What is Lambda provisioned concurrency?

## 5. API Gateway

56. What is Amazon API Gateway?
57. Explain API Gateway integration types.
58. How do you secure API Gateway?
59. What is API Gateway throttling and how does it work?
60. Explain API Gateway stages and deployments.
61. How do you implement API versioning with API Gateway?
62. What is API Gateway custom authorizers?
63. Explain API Gateway WebSocket APIs.
64. How do you monitor API Gateway?
65. What is API Gateway usage plans?
66. Explain API Gateway request/response transformations.
67. How do you handle CORS in API Gateway?
68. What is API Gateway private APIs?
69. Explain API Gateway HTTP APIs vs REST APIs.
70. How do you integrate API Gateway with Lambda?

## 6. DynamoDB

71. What is Amazon DynamoDB?
72. Explain DynamoDB tables, items, and attributes.
73. What is a DynamoDB partition key and sort key?
74. How does DynamoDB scaling work?
75. Explain DynamoDB Local Secondary Index (LSI) vs Global Secondary Index (GSI).
76. What is DynamoDB Streams?
77. How do you backup DynamoDB tables?
78. Explain DynamoDB conditional writes.
79. What is DynamoDB Time to Live (TTL)?
80. How do you query DynamoDB?
81. Explain DynamoDB pagination.
82. What is DynamoDB Accelerator (DAX)?
83. How do you handle DynamoDB hot partitions?
84. Explain DynamoDB transactions.
85. What is DynamoDB global tables?

## 7. RDS (Relational Database Service)

86. What is Amazon RDS?
87. Explain different RDS engines (MySQL, PostgreSQL, etc.).
88. How do you connect to an RDS instance?
89. What is RDS Multi-AZ deployment?
90. Explain RDS Read Replicas.
91. How do you backup RDS databases?
92. What is RDS Aurora and its benefits?
93. Explain RDS parameter groups and option groups.
94. How do you monitor RDS?
95. What is RDS Proxy?
96. Explain RDS storage auto-scaling.
97. How do you migrate to RDS?
98. What is RDS Performance Insights?
99. Explain RDS Serverless.
100. How do you secure RDS?

## 8. VPC (Virtual Private Cloud)

101. What is Amazon VPC?
102. Explain VPC subnets (public vs private).
103. What is an Internet Gateway?
104. Explain NAT Gateway vs NAT Instance.
105. What is a VPC Peering?
106. How do you secure VPC?
107. Explain VPC Flow Logs.
108. What is AWS Direct Connect?
109. Explain VPC Endpoints.
110. How do you design a highly available VPC?
111. What is AWS Transit Gateway?
112. Explain VPC Security Groups vs Network ACLs.
113. How do you troubleshoot VPC connectivity issues?
114. What is AWS VPN?
115. Explain VPC sharing.

## 9. IAM (Identity and Access Management)

116. What is AWS IAM?
117. Explain IAM users, groups, and roles.
118. What is the difference between IAM policies and permissions?
119. Explain IAM policy types (managed vs inline).
120. What is IAM MFA (Multi-Factor Authentication)?
121. How do you implement least privilege in IAM?
122. Explain IAM cross-account access.
123. What is AWS STS (Security Token Service)?
124. How do you rotate IAM access keys?
125. Explain IAM policy evaluation logic.
126. What is IAM Access Analyzer?
127. How do you audit IAM?
128. Explain IAM identity providers.
129. What is AWS Organizations SCP (Service Control Policies)?
130. How do you manage IAM at scale?

## 10. CloudWatch

131. What is Amazon CloudWatch?
132. Explain CloudWatch metrics, logs, and alarms.
133. How do you create custom CloudWatch metrics?
134. What is CloudWatch Logs Insights?
135. Explain CloudWatch dashboards.
136. How do you set up CloudWatch alarms?
137. What is CloudWatch Events (now EventBridge)?
138. Explain CloudWatch agent.
139. How do you monitor application logs with CloudWatch?
140. What is CloudWatch Synthetics?
141. Explain CloudWatch Application Insights.
142. How do you troubleshoot with CloudWatch?
143. What is CloudWatch Container Insights?
144. Explain CloudWatch billing alerts.
145. How do you export CloudWatch logs?

## 11. CloudFormation

146. What is AWS CloudFormation?
147. Explain CloudFormation templates and stacks.
148. How do you use CloudFormation parameters?
149. What is CloudFormation change sets?
150. Explain CloudFormation nested stacks.
151. How do you handle CloudFormation rollbacks?
152. What is CloudFormation stack policies?
153. Explain CloudFormation custom resources.
154. How do you monitor CloudFormation stacks?
155. What is AWS CDK and how does it relate to CloudFormation?
156. Explain CloudFormation drift detection.
157. How do you version CloudFormation templates?
158. What is CloudFormation stack sets?
159. Explain CloudFormation intrinsic functions.
160. How do you debug CloudFormation issues?

## 12. ECS/EKS

161. What is Amazon ECS?
162. Explain ECS clusters, services, and tasks.
163. What is Amazon EKS?
164. How do you choose between ECS and EKS?
165. Explain ECS task definitions.
166. What is ECS Fargate?
167. How do you deploy applications on ECS?
168. Explain EKS node groups.
169. What is Kubernetes and how does EKS relate?
170. How do you monitor ECS/EKS?
171. Explain ECS service discovery.
172. What is AWS App Mesh?
173. How do you handle logging in ECS/EKS?
174. Explain ECS capacity providers.
175. What is AWS Copilot for ECS?
176. How do you scale ECS services?
177. Explain EKS add-ons.
178. What is AWS Fargate for EKS?
179. How do you secure ECS/EKS?
180. Explain ECS task networking modes.

## 13. SNS/SQS

181. What is Amazon SNS?
182. What is Amazon SQS?
183. Explain SQS queue types (standard vs FIFO).
184. How do you implement fan-out pattern with SNS and SQS?
185. What is SQS dead-letter queues?
186. How do you handle message visibility in SQS?
187. Explain SNS message filtering.
188. What is SQS long polling?
189. How do you monitor SNS/SQS?
190. Explain SQS message groups.
191. What is Amazon EventBridge?
192. How do you secure SNS/SQS?
193. Explain SQS batch operations.
194. What is SNS mobile push notifications?
195. How do you implement retry logic with SQS?
196. Explain SNS topic encryption.
197. What is SQS FIFO throughput limits?
198. How do you handle large messages in SQS?
199. Explain SNS subscription confirmation.
200. What is Amazon MQ?

## 14. CodePipeline/CodeBuild

201. What is AWS CodePipeline?
202. What is AWS CodeBuild?
203. How do you set up a CI/CD pipeline with CodePipeline?
204. Explain CodeBuild build specifications.
205. What is AWS CodeCommit?
206. How do you integrate CodePipeline with GitHub?
207. Explain CodeBuild environments.
208. What is AWS CodeDeploy?
209. How do you handle build artifacts?
210. Explain CodePipeline stages and actions.
211. What is AWS CodeStar?
212. How do you monitor CodePipeline/CodeBuild?
213. Explain CodeBuild local builds.
214. What is AWS CodeArtifact?
215. How do you secure CodePipeline?
216. Explain CodeBuild test reports.
217. What is AWS CodeGuru?
218. How do you implement blue-green deployments?
219. Explain CodePipeline approval actions.
220. What is AWS CodeBuild batch builds?

## 15. CloudFront

221. What is Amazon CloudFront?
222. Explain CloudFront distributions.
223. What is CloudFront origins?
224. How do you configure CloudFront behaviors?
225. Explain CloudFront caching.
226. What is CloudFront Functions?
227. How do you secure CloudFront?
228. Explain CloudFront signed URLs.
229. What is CloudFront Lambda@Edge?
230. How do you monitor CloudFront?
231. Explain CloudFront price classes.
232. What is CloudFront field-level encryption?
233. How do you invalidate CloudFront cache?
234. Explain CloudFront real-time logs.
235. What is AWS Global Accelerator?

## 16. Route 53

236. What is Amazon Route 53?
237. Explain Route 53 routing policies.
238. What is Route 53 health checks?
239. How do you configure DNS with Route 53?
240. Explain Route 53 hosted zones.
241. What is Route 53 Resolver?
242. How do you implement DNS failover?
243. Explain Route 53 traffic flow.
244. What is Route 53 domain registration?
245. How do you monitor Route 53?
246. Explain Route 53 private hosted zones.
247. What is Route 53 geolocation routing?
248. How do you secure Route 53?
249. Explain Route 53 alias records.
250. What is AWS Certificate Manager?

## 17. KMS (Key Management Service)

251. What is AWS KMS?
252. Explain KMS keys (customer managed vs AWS managed).
253. How do you encrypt data with KMS?
254. What is envelope encryption?
255. Explain KMS key rotation.
256. How do you use KMS with other AWS services?
257. What is KMS custom key stores?
258. Explain KMS grants.
259. How do you monitor KMS?
260. What is AWS CloudHSM?
261. Explain KMS multi-region keys.
262. How do you secure KMS keys?
263. What is KMS key policies?
264. Explain KMS import key material.
265. How do you audit KMS usage?

## 18. Scenario-Based Questions

### Deployment Failures
266. Your Lambda function is timing out during deployment. What could be the causes and how would you troubleshoot?
267. A CloudFormation stack update failed. How do you investigate and fix it?
268. ECS service deployment is stuck. What steps would you take to resolve it?
269. CodePipeline build is failing. How do you debug the issue?
270. Your application deployment to EC2 failed due to insufficient permissions. How do you fix it?

### Performance Issues
271. Your S3 bucket is experiencing slow performance. What optimizations would you implement?
272. DynamoDB table has hot partition issues. How do you resolve it?
273. Lambda functions are experiencing cold starts. What can you do to improve performance?
274. RDS database is running slow. How do you diagnose and optimize it?
275. CloudFront is serving stale content. How do you fix it?

### Security Incidents
276. You suspect unauthorized access to your S3 bucket. What immediate steps would you take?
277. An IAM user was compromised. How do you contain the breach and prevent future incidents?
278. Your EC2 instance was hacked. What forensic steps would you take?
279. A data breach occurred in your RDS database. How do you respond?
280. Suspicious activity detected in CloudTrail logs. How do you investigate?

### High Availability and Disaster Recovery
281. Your primary region goes down. How do you failover to a secondary region?
282. RDS instance becomes unresponsive. How do you implement automatic failover?
283. S3 bucket is accidentally deleted. How do you recover the data?
284. EC2 instance in Auto Scaling group is unhealthy. How does AWS handle it?
285. Your application needs 99.99% uptime. How do you design for high availability?

### Cost Optimization
286. Your AWS bill is unexpectedly high. How do you identify and reduce costs?
287. EC2 Reserved Instances are underutilized. What can you do?
288. S3 storage costs are increasing rapidly. How do you optimize storage classes?
289. Lambda functions are running longer than expected. How do you optimize costs?
290. Unused resources are accumulating. How do you implement cleanup?

### Monitoring and Alerting
291. You need to monitor application performance across multiple services. How would you set it up?
292. Critical alert triggered but you don't know the cause. How do you investigate?
293. Log data is not appearing in CloudWatch. How do you troubleshoot?
294. You need to create a dashboard for business metrics. How do you implement it?
295. Application errors are not being captured. How do you improve monitoring?

### Networking Issues
296. EC2 instance can't connect to the internet. How do you troubleshoot?
297. VPC peering connection is not working. What could be wrong?
298. DNS resolution is failing. How do you diagnose Route 53 issues?
299. Load balancer is not distributing traffic properly. How do you fix it?
300. VPN connection is unstable. How do you improve reliability?

### Database Problems
301. DynamoDB table is throttling requests. How do you handle it?
302. RDS backup failed. What are the possible causes and solutions?
303. Database connection pool is exhausted. How do you resolve it?
304. Data inconsistency between RDS read replicas. How do you fix it?
305. MongoDB on EC2 is running out of disk space. How do you handle it?

### Microservices Architecture
306. Service-to-service communication is failing. How do you debug?
307. One microservice is causing cascading failures. How do you implement circuit breaker?
308. API Gateway is rate limiting legitimate requests. How do you handle it?
309. Event-driven architecture has duplicate events. How do you deduplicate?
310. Service discovery is not working in ECS. How do you troubleshoot?

### DevOps and CI/CD
311. Build pipeline is slow. How do you optimize it?
312. Deployment to production failed due to environment differences. How do you fix it?
313. Code quality checks are failing. How do you improve them?
314. Infrastructure as Code is not idempotent. How do you fix it?
315. Rollback strategy failed. How do you implement better rollback mechanisms?

### Advanced Scenarios
316. You need to implement zero-downtime deployments. How would you do it?
317. Application needs to handle sudden traffic spikes. How do you design auto-scaling?
318. You need to implement multi-region active-active architecture. What services would you use?
319. Compliance requires data encryption at rest and in transit. How do you implement it?
320. You need to implement chaos engineering in your AWS environment. How would you start?

This comprehensive list covers the most important AWS services and concepts that developers encounter in modern distributed systems, microservices, and event-driven architectures. The questions progress from basic understanding to advanced implementation and troubleshooting scenarios commonly faced in interviews and real-world projects.
