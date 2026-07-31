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

### Answers for Basic AWS Concepts

**1. What is AWS and what are its main benefits?**  
AWS (Amazon Web Services) is a comprehensive cloud computing platform provided by Amazon that offers over 200 services including computing power, storage, databases, machine learning, and more. It's the world's most comprehensive and broadly adopted cloud platform.  

**Main Benefits:**  
- **Scalability:** Pay only for what you use, scale up/down as needed  
- **Reliability:** 99.9%+ uptime SLA for most services  
- **Security:** Enterprise-grade security with compliance certifications  
- **Global Reach:** 25+ regions worldwide with 80+ availability zones  
- **Cost-Effective:** No upfront costs, pay-as-you-go pricing  
- **Innovation:** Constantly updated with new services and features  

**Example:** A startup can launch a web application using EC2, S3, and RDS without buying any hardware, scaling from 10 to 10,000 users automatically.

**2. Explain the AWS Global Infrastructure (Regions, Availability Zones, Edge Locations).**  
AWS Global Infrastructure is designed for high availability, fault tolerance, and low latency.  

- **Regions:** Geographic areas (e.g., us-east-1, eu-west-1) containing multiple data centers  
- **Availability Zones (AZs):** Isolated data centers within a region (typically 2-6 per region)  
- **Edge Locations:** CDN endpoints for CloudFront (200+ locations worldwide)  

**Example:** For high availability, deploy your application across multiple AZs in a region. If us-east-1a fails, traffic automatically routes to us-east-1b.

**3. What is the difference between IaaS, PaaS, and SaaS?**  
- **IaaS (Infrastructure as a Service):** Provides virtualized computing resources (EC2, S3, VPC)  
- **PaaS (Platform as a Service):** Provides platform for application development (Elastic Beanstalk, Lambda)  
- **SaaS (Software as a Service):** Complete software applications (WorkMail, Chime)  

**Example:** IaaS gives you a virtual server; PaaS gives you a runtime environment; SaaS gives you a ready-to-use application.

**4. How does AWS pricing work? Explain the pay-as-you-go model.**  
AWS uses a pay-as-you-go model where you only pay for what you use, with no long-term contracts or upfront costs.  

**Pricing Components:**  
- **Compute:** Per second/hour for EC2 instances  
- **Storage:** Per GB/month for S3, EBS  
- **Data Transfer:** Per GB transferred out  
- **Requests:** Per API call for many services  

**Example:** An EC2 t3.micro instance costs ~$0.0104/hour. If you run it for 100 hours in a month, you pay ~$1.04.

**5. What is the AWS Free Tier and what are its limitations?**  
AWS Free Tier provides limited usage of services at no cost for 12 months after account creation.  

**Limitations:**  
- Time-bound (12 months for most services)  
- Usage limits (e.g., 750 hours EC2 t2.micro)  
- Regional restrictions  
- Not available for all services  

**Example:** Free tier includes 5GB S3 storage, 750 hours EC2 t2.micro, and 1 million Lambda requests per month.

**6. Explain AWS Shared Responsibility Model.**  
AWS and customers share responsibility for security and compliance.  

**AWS Responsibilities:**  
- Physical security of data centers  
- Network infrastructure security  
- Hypervisor security  

**Customer Responsibilities:**  
- Data encryption  
- Access management (IAM)  
- Operating system patches  
- Application security  

**Example:** AWS secures the EC2 hypervisor; you secure your application running on EC2.

**7. What are AWS Service Level Agreements (SLAs)?**  
SLAs guarantee service availability and performance.  

**Common SLAs:**  
- EC2: 99.9% uptime  
- S3: 99.9% durability, 99.99% availability  
- RDS: 99.95% availability  

**Example:** If EC2 SLA is 99.9% and you experience downtime beyond this, you may be eligible for service credits.

**8. How do you secure your AWS account?**  
- Enable MFA for root account  
- Use IAM users instead of root  
- Implement least privilege principle  
- Enable CloudTrail for auditing  
- Use AWS Config for compliance  
- Regular security assessments  

**Example:** Create IAM users with specific permissions and assign them to groups with appropriate policies.

**9. What is AWS Organizations and when would you use it?**  
AWS Organizations helps manage multiple AWS accounts centrally.  

**Use Cases:**  
- Multi-account strategy for different environments  
- Centralized billing and cost management  
- Service Control Policies (SCPs)  
- Cross-account access management  

**Example:** Create separate accounts for dev, staging, and production environments with centralized billing.

**10. Explain AWS Resource Tags and their importance.**  
Tags are key-value pairs attached to AWS resources for organization and cost tracking.  

**Importance:**  
- Cost allocation and budgeting  
- Resource organization  
- Automation and compliance  
- Access control policies  

**Example:** Tag resources with `Environment: Production`, `Project: E-commerce`, `Owner: Team-A` for better management.

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

### Answers for EC2

**11. What is EC2 and what are its main use cases?**  
EC2 (Elastic Compute Cloud) is AWS's virtual server service that provides resizable compute capacity in the cloud.  

**Main Use Cases:**  
- Web application hosting  
- Batch processing  
- Development and testing environments  
- Big data processing  
- Machine learning workloads  

**Example:** Launch a t3.medium instance to host a Node.js web application with auto-scaling based on CPU utilization.

**12. Explain different EC2 instance types (t2, m5, c5, etc.) and their use cases.**  
EC2 instance types are optimized for different workloads:  

- **T2/T3 (Burstable):** General purpose, web servers, development environments  
- **M5/M6g (General Purpose):** Balanced compute, memory, networking  
- **C5/C6g (Compute Optimized):** High-performance computing, gaming  
- **R5/R6g (Memory Optimized):** In-memory databases, big data processing  
- **I3/I4i (Storage Optimized):** High I/O workloads, data warehousing  
- **P3/P4 (GPU Instances):** Machine learning, deep learning  

**Example:** Use C5 instances for a high-traffic web application requiring fast CPU performance.

**13. What is an AMI (Amazon Machine Image)?**  
AMI is a template that contains the software configuration needed to launch an EC2 instance. It includes:  
- Operating system  
- Application server  
- Applications  
- Custom configurations  

**Example:** Use Amazon Linux 2 AMI as base, then customize with your application and create a new AMI for consistent deployments.

**14. How do you launch an EC2 instance?**  
1. Choose AMI  
2. Select instance type  
3. Configure network settings (VPC, subnet, security groups)  
4. Add storage (EBS volumes)  
5. Configure tags  
6. Review and launch  

**Example:** Use AWS CLI: `aws ec2 run-instances --image-id ami-12345678 --instance-type t3.micro --key-name my-key`

**15. Explain EC2 Security Groups vs Network ACLs.**  
- **Security Groups:** Instance-level firewalls, stateful, allow rules only  
- **Network ACLs:** Subnet-level firewalls, stateless, allow and deny rules  

**Example:** Security Group allows inbound HTTP (port 80) from anywhere; Network ACL can deny specific IP ranges at subnet level.

**16. What is an Elastic IP and when would you use it?**  
Elastic IP is a static IPv4 address that you can allocate to your AWS account and associate with EC2 instances.  

**Use Cases:**  
- Consistent public IP for applications  
- Failover scenarios  
- Whitelisting in firewalls  

**Example:** Associate Elastic IP with EC2 instance running a web server to maintain consistent public IP during instance restarts.

**17. How do you connect to an EC2 instance?**  
- **SSH:** For Linux instances using key pairs  
- **RDP:** For Windows instances  
- **Session Manager:** AWS Systems Manager for secure access without SSH keys  
- **EC2 Instance Connect:** Browser-based SSH connection  

**Example:** `ssh -i my-key.pem ec2-user@ec2-123-456-789-0.compute-1.amazonaws.com`

**18. Explain EC2 Auto Scaling and its components.**  
Auto Scaling automatically adjusts EC2 capacity based on demand.  

**Components:**  
- **Launch Template/Configuration:** Defines instance configuration  
- **Auto Scaling Group:** Manages EC2 instances  
- **Scaling Policies:** Define when to scale (CPU > 70%, etc.)  

**Example:** Scale out when CPU > 70% for 5 minutes, scale in when CPU < 30% for 10 minutes.

**19. What is EC2 Spot Instances and when would you use them?**  
Spot Instances are unused EC2 capacity offered at up to 90% discount, but can be terminated with 2-minute notice.  

**Use Cases:**  
- Batch processing  
- CI/CD pipelines  
- Stateless web servers  
- Big data workloads  

**Example:** Use Spot Fleet for a Hadoop cluster to save costs while maintaining fault tolerance.

**20. How do you monitor EC2 instances?**  
- **CloudWatch:** Built-in metrics (CPU, network, disk)  
- **CloudWatch Agent:** Custom metrics and logs  
- **EC2 Status Checks:** Instance and system status  
- **CloudTrail:** API activity monitoring  

**Example:** Set CloudWatch alarm for CPU > 80% to trigger auto-scaling or notifications.

**21. Explain EC2 Instance Store vs EBS (Elastic Block Store).**  
- **Instance Store:** Temporary block storage, high I/O performance, data lost on termination  
- **EBS:** Persistent block storage, survives instance termination, various volume types  

**Example:** Use Instance Store for temporary data like cache; use EBS for database storage that needs persistence.

**22. What is EC2 User Data and how is it used?**  
User Data is a script that runs when an EC2 instance launches, used for:  
- Installing software  
- Configuring applications  
- Setting up environment variables  

**Example:**  
```bash
#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
```

**23. How do you create a custom AMI?**  
1. Launch and configure EC2 instance  
2. Stop the instance  
3. Create AMI from the instance  
4. Launch new instances from the custom AMI  

**Example:** Use AWS CLI: `aws ec2 create-image --instance-id i-1234567890abcdef0 --name "My Custom AMI"`

**24. Explain EC2 Placement Groups and their types.**  
Placement Groups determine how instances are placed on underlying hardware.  

**Types:**  
- **Cluster:** Low-latency, high-throughput (same AZ)  
- **Spread:** Instances on distinct hardware (different AZs)  
- **Partition:** Groups of instances on distinct hardware  

**Example:** Use Cluster placement group for HPC workloads requiring low network latency.

**25. What is EC2 Reserved Instances and Savings Plans?**  
- **Reserved Instances:** 1-3 year commitment for significant discounts (up to 75%)  
- **Savings Plans:** Flexible pricing model with 1-3 year commitment  

**Example:** Purchase Reserved Instance for steady-state workloads to save 50-70% compared to On-Demand pricing.

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

### Answers for S3

**26. What is Amazon S3 and what are its main features?**  
Amazon S3 is an object storage service that offers industry-leading scalability, data availability, security, and performance.  

**Main Features:**  
- Unlimited storage capacity  
- 99.999999999% (11 9's) durability  
- Versioning and lifecycle management  
- Cross-region replication  
- Static website hosting  
- Event-driven architectures  

**Example:** Store user-uploaded images and documents with automatic backup to another region.

**27. Explain S3 storage classes (Standard, IA, Glacier, etc.).**  
S3 offers different storage classes optimized for different access patterns:  

- **S3 Standard:** General purpose, 99.99% availability, low latency  
- **S3 Intelligent-Tiering:** Automatically moves data between tiers  
- **S3 Standard-IA:** Infrequent access, lower storage cost  
- **S3 One Zone-IA:** Single AZ, even lower cost  
- **S3 Glacier:** Archive storage, retrieval in minutes/hours/days  
- **S3 Glacier Deep Archive:** Lowest cost, retrieval in hours  

**Example:** Use S3 Standard for frequently accessed data, S3 Glacier for compliance archives.

**28. What is an S3 bucket and what are the naming conventions?**  
An S3 bucket is a container for objects stored in S3.  

**Naming Conventions:**  
- Globally unique across all AWS accounts  
- 3-63 characters long  
- Lowercase letters, numbers, hyphens only  
- Must start and end with letter or number  
- Cannot contain consecutive hyphens  

**Example:** Valid bucket name: `my-application-assets-2024`

**29. How do you secure S3 buckets?**  
- **Bucket Policies:** JSON-based access policies  
- **IAM Policies:** User/role-based permissions  
- **Access Control Lists (ACLs):** Granular permissions  
- **MFA Delete:** Require MFA for delete operations  
- **SSE Encryption:** Server-side encryption  
- **VPC Endpoints:** Private access from VPC  

**Example:** Use bucket policy to allow public read access to static website files while keeping admin access restricted.

**30. Explain S3 versioning and its benefits.**  
S3 versioning keeps multiple versions of an object in the same bucket.  

**Benefits:**  
- Accidental deletion protection  
- Rollback capability  
- Audit trail of changes  
- Compliance requirements  

**Example:** If a file is accidentally overwritten, you can restore the previous version.

**31. What is S3 Static Website Hosting?**  
S3 can host static websites without a web server, serving HTML, CSS, JS, and media files.  

**Features:**  
- Custom domain support  
- HTTPS with CloudFront  
- Redirect rules  
- Error pages  

**Example:** Host a marketing website with `index.html` and `error.html` in an S3 bucket.

**32. How do you implement S3 cross-region replication?**  
Cross-region replication automatically copies objects from one bucket to another in different regions.  

**Setup:**  
1. Enable versioning on both buckets  
2. Create replication rule  
3. Specify source and destination buckets  
4. Configure IAM role for replication  

**Example:** Replicate user uploads from us-east-1 to eu-west-1 for disaster recovery.

**33. Explain S3 lifecycle policies.**  
Lifecycle policies automatically transition objects between storage classes or delete them based on rules.  

**Example Rules:**  
- Move to IA after 30 days  
- Move to Glacier after 1 year  
- Delete after 7 years  

**Example:** Automatically move old log files to cheaper storage classes to reduce costs.

**34. What is S3 Transfer Acceleration?**  
S3 Transfer Acceleration uses CloudFront edge locations to accelerate uploads to S3 buckets.  

**Benefits:**  
- Up to 50-500% faster uploads  
- Especially beneficial for long-distance transfers  
- Uses optimized network paths  

**Example:** Accelerate large file uploads from Asia to S3 bucket in US East.

**35. How do you encrypt data in S3?**  
- **SSE-S3:** AWS manages encryption keys  
- **SSE-KMS:** AWS KMS manages keys, more control  
- **SSE-C:** Customer provides encryption keys  
- **Client-side encryption:** Encrypt before uploading  

**Example:** Use SSE-KMS for compliance requirements needing key management and audit trails.

**36. Explain S3 event notifications.**  
S3 can send notifications when certain events occur on objects.  

**Supported Events:**  
- Object creation/deletion  
- Restore completion  
- Replication events  

**Targets:**  
- SNS topics  
- SQS queues  
- Lambda functions  

**Example:** Trigger Lambda function when new image is uploaded to process it.

**37. What is S3 Select and S3 Glacier Select?**  
S3 Select allows running SQL queries directly on objects in S3 without downloading the entire file.  

**Benefits:**  
- Faster data retrieval  
- Cost-effective for partial data access  
- Supports CSV, JSON, Parquet formats  

**Example:** Query specific columns from a large CSV file without downloading the entire dataset.

**38. How do you optimize S3 performance?**  
- **Prefix Optimization:** Use random prefixes for high-throughput workloads  
- **Multipart Upload:** For large files (>100MB)  
- **S3 Transfer Acceleration:** For long-distance uploads  
- **CloudFront:** For frequently accessed content  
- **S3 Select:** For partial object retrieval  

**Example:** Use multipart upload for files >100MB to improve upload speed and reliability.

**39. Explain S3 access points.**  
S3 Access Points are unique hostnames that simplify managing access to shared datasets in S3.  

**Benefits:**  
- Simplified access management  
- Custom permissions per access point  
- VPC-only access points  
- Integration with AWS services  

**Example:** Create separate access points for different teams with specific permissions.

**40. What is S3 Batch Operations?**  
S3 Batch Operations allows performing bulk operations on objects across millions of objects.  

**Supported Operations:**  
- Copy objects  
- Replace object tags  
- Modify access controls  
- Invoke Lambda functions  
- Delete objects  

**Example:** Update encryption on millions of existing objects in a bucket.

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

### Answers for Lambda

**41. What is AWS Lambda and what are its main benefits?**  
AWS Lambda is a serverless compute service that runs code in response to events without managing servers.  

**Main Benefits:**  
- **No server management:** AWS handles infrastructure  
- **Auto-scaling:** Scales automatically based on requests  
- **Pay-per-use:** Only pay for execution time  
- **Event-driven:** Responds to various AWS events  
- **Multiple runtimes:** Supports many programming languages  

**Example:** Process S3 file uploads automatically when files are added to a bucket.

**42. Explain Lambda function lifecycle.**  
Lambda functions have a lifecycle managed by AWS:  

1. **Creation:** Upload code and configure function  
2. **Idle:** Function ready but not running  
3. **Invocation:** Function triggered and executed  
4. **Scaling:** Multiple execution environments created as needed  
5. **Cleanup:** Unused environments are cleaned up  

**Example:** First invocation may experience cold start latency, subsequent calls use warm environments.

**43. What languages does Lambda support?**  
Lambda supports multiple runtimes:  
- Node.js (14.x, 16.x, 18.x)  
- Python (3.8, 3.9, 3.10, 3.11)  
- Java (8, 11, 17)  
- .NET Core (3.1, 6.0)  
- Go (1.x)  
- Ruby (2.7, 3.2)  
- Custom runtimes via container images  

**Example:** Use Python 3.9 runtime for a data processing Lambda function.

**44. How do you trigger Lambda functions?**  
Lambda can be triggered by various sources:  

- **API Gateway:** HTTP requests  
- **S3:** Object operations  
- **DynamoDB:** Table changes  
- **SNS/SQS:** Messages  
- **CloudWatch Events:** Scheduled events  
- **Kinesis:** Stream processing  
- **Alexa:** Voice commands  

**Example:** Trigger Lambda on S3 object creation to resize images automatically.

**45. Explain Lambda layers and their use cases.**  
Lambda layers are archives containing additional code and dependencies that can be shared across functions.  

**Use Cases:**  
- Share common libraries  
- Reduce deployment package size  
- Separate business logic from dependencies  
- Version control of shared code  

**Example:** Create a layer with pandas and numpy for data processing functions.

**46. What is Lambda@Edge?**  
Lambda@Edge runs Lambda functions at CloudFront edge locations to customize content delivery.  

**Use Cases:**  
- A/B testing  
- Content personalization  
- Authentication/authorization  
- Request/response manipulation  
- Real-time image transformation  

**Example:** Use Lambda@Edge to add authentication headers to requests at edge locations.

**47. How do you monitor Lambda functions?**  
- **CloudWatch Metrics:** Invocations, duration, errors  
- **CloudWatch Logs:** Function logs  
- **X-Ray:** Distributed tracing  
- **CloudWatch Alarms:** Set alerts on metrics  

**Example:** Monitor Lambda errors and set alarm when error rate exceeds 5%.

**48. Explain Lambda cold starts and how to optimize them.**  
Cold start occurs when Lambda creates a new execution environment, causing latency.  

**Optimization Techniques:**  
- **Provisioned Concurrency:** Keep functions warm  
- **Reduce Package Size:** Smaller deployment packages  
- **Use Layers:** Separate dependencies  
- **Optimize Runtime:** Choose efficient language/runtime  
- **VPC Configuration:** Minimize ENI creation  

**Example:** Use provisioned concurrency for latency-sensitive applications.

**49. What is the maximum execution time for a Lambda function?**  
- Default: 3 seconds  
- Configurable: Up to 15 minutes (900 seconds)  
- Use Step Functions for longer workflows  

**Example:** For ETL jobs, use Lambda with Step Functions to orchestrate multiple 15-minute executions.

**50. How do you handle errors in Lambda functions?**  
- **Error Handling:** Try-catch blocks in code  
- **Dead Letter Queues:** Send failed messages to SQS/SNS  
- **Retry Logic:** Configure retry attempts  
- **Monitoring:** CloudWatch alarms on errors  
- **Custom Error Responses:** For API Gateway integration  

**Example:** Use DLQ to capture failed message processing for later analysis.

**51. Explain Lambda environment variables.**  
Environment variables are key-value pairs that can be accessed by Lambda functions.  

**Use Cases:**  
- Database connection strings  
- API keys  
- Configuration settings  
- Feature flags  

**Example:** Store database URL as environment variable: `DB_CONNECTION_STRING=postgresql://...`

**52. What is Lambda VPC configuration?**  
Lambda can access resources in VPC (RDS, ElastiCache, etc.) by configuring VPC settings.  

**Configuration:**  
- Specify VPC, subnets, security groups  
- Lambda creates ENIs in specified subnets  
- May cause cold start latency due to ENI creation  

**Example:** Configure Lambda to access RDS database in private subnet.

**53. How do you version Lambda functions?**  
Lambda supports versioning for managing function updates:  

- **$LATEST:** Working version  
- **Version Numbers:** Immutable snapshots (1, 2, 3...)  
- **Aliases:** Pointers to versions ($LATEST, prod, dev)  

**Example:** Point 'prod' alias to version 3, 'dev' alias to $LATEST.

**54. Explain Lambda aliases.**  
Aliases are pointers to specific Lambda function versions, enabling:  

- **Safe Deployments:** Update alias to new version  
- **Rollback:** Point alias back to previous version  
- **Traffic Shifting:** Gradual rollout with weighted aliases  

**Example:** Use alias 'prod' pointing to version 2, update to version 3 with 10% traffic first.

**55. What is Lambda provisioned concurrency?**  
Provisioned concurrency keeps Lambda functions initialized and ready to respond immediately.  

**Benefits:**  
- Eliminates cold starts  
- Consistent low-latency responses  
- Predictable performance  

**Example:** Enable provisioned concurrency for API endpoints requiring <100ms response times.

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

### Answers for API Gateway

**56. What is Amazon API Gateway?**  
API Gateway is a fully managed service that makes it easy to create, publish, maintain, monitor, and secure APIs at any scale.  

**Key Features:**  
- Create RESTful and WebSocket APIs  
- Serverless integration with Lambda  
- Traffic management and throttling  
- Authentication and authorization  
- Request/response transformation  

**Example:** Create a REST API that triggers Lambda functions for user registration and login.

**57. Explain API Gateway integration types.**  
- **Lambda:** Direct integration with Lambda functions  
- **HTTP:** Proxy requests to HTTP endpoints  
- **AWS Service:** Call AWS services directly  
- **Mock:** Return static responses for testing  
- **VPC Link:** Connect to private resources via VPC  

**Example:** Use Lambda integration for serverless APIs, HTTP integration for existing web services.

**58. How do you secure API Gateway?**  
- **IAM Authorization:** AWS IAM users/roles  
- **Cognito User Pools:** User authentication  
- **Lambda Authorizers:** Custom authentication logic  
- **API Keys:** Client identification  
- **Resource Policies:** IP-based restrictions  
- **SSL/TLS:** HTTPS enforcement  

**Example:** Use Cognito for user authentication and API keys for third-party access control.

**59. What is API Gateway throttling and how does it work?**  
Throttling controls the rate of requests to prevent abuse and ensure fair usage.  

**Types:**  
- **Account-level throttling:** 10,000 requests/second by default  
- **Method-level throttling:** Per API method limits  
- **Usage plans:** Client-specific limits  

**Example:** Set burst limit of 1000 requests and steady-state rate of 500 requests/second.

**60. Explain API Gateway stages and deployments.**  
- **Stages:** Named references to API deployments (dev, staging, prod)  
- **Deployments:** Snapshots of API configuration at a point in time  
- **Stage Variables:** Environment-specific configuration  

**Example:** Deploy API to 'prod' stage with production database endpoint in stage variables.

**61. How do you implement API versioning with API Gateway?**  
- **URI Versioning:** `/v1/users`, `/v2/users`  
- **Query Parameter:** `?version=1`  
- **Header Versioning:** `Accept-Version: v1`  
- **Stage-based:** Different stages for versions  

**Example:** Use URI versioning with `/api/v1/` and `/api/v2/` paths.

**62. What is API Gateway custom authorizers?**  
Custom authorizers are Lambda functions that control access to API methods.  

**Types:**  
- **Token-based:** Bearer tokens (JWT, OAuth)  
- **Request-based:** Custom headers/parameters  

**Example:** Lambda function validates JWT token and returns IAM policy for API access.

**63. Explain API Gateway WebSocket APIs.**  
WebSocket APIs enable real-time bidirectional communication between clients and servers.  

**Features:**  
- Persistent connections  
- Real-time messaging  
- Integration with Lambda and HTTP endpoints  
- Connection management  

**Example:** Build a chat application where messages are sent to connected clients via WebSocket.

**64. How do you monitor API Gateway?**  
- **CloudWatch Metrics:** Request count, latency, error rates  
- **CloudWatch Logs:** Request/response details  
- **X-Ray:** Distributed tracing  
- **Access Logs:** Detailed logging to CloudWatch/Kinesis  

**Example:** Monitor 4XX/5XX error rates and set alarms for API failures.

**65. What is API Gateway usage plans?**  
Usage plans define throttling and quota limits for API consumers.  

**Components:**  
- **Throttle limits:** Request rates  
- **Quota limits:** Monthly request limits  
- **API Keys:** Associate with usage plans  

**Example:** Create usage plan allowing 1000 requests/day for free tier users.

**66. Explain API Gateway request/response transformations.**  
API Gateway can modify requests and responses using mapping templates.  

**Use Cases:**  
- Data format conversion (XML to JSON)  
- Field mapping and filtering  
- Header manipulation  
- Content type conversion  

**Example:** Transform XML request to JSON before sending to Lambda function.

**67. How do you handle CORS in API Gateway?**  
CORS (Cross-Origin Resource Sharing) allows web applications to make requests to different domains.  

**Configuration:**  
- Enable CORS in method settings  
- Configure allowed origins, methods, headers  
- Handle preflight OPTIONS requests  

**Example:** Allow `https://myapp.com` to make POST requests to API Gateway.

**68. What is API Gateway private APIs?**  
Private APIs are only accessible from within a VPC using VPC endpoints.  

**Benefits:**  
- Enhanced security  
- No public internet exposure  
- Integration with private resources  

**Example:** Create private API for internal microservices communication.

**69. Explain API Gateway HTTP APIs vs REST APIs.**  
- **HTTP APIs:** Lower cost, faster performance, simpler features  
- **REST APIs:** Full feature set, more configuration options, higher cost  

**Example:** Use HTTP APIs for simple CRUD operations, REST APIs for complex authentication and transformations.

**70. How do you integrate API Gateway with Lambda?**  
1. Create Lambda function  
2. Create API Gateway REST API  
3. Create resource and method  
4. Configure Lambda integration  
5. Deploy API to stage  

**Example:** POST method on `/users` resource integrates with `createUser` Lambda function.

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

### Answers for DynamoDB

**71. What is Amazon DynamoDB?**  
DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability.  

**Key Features:**  
- Single-digit millisecond latency  
- Automatic scaling  
- Multi-region replication  
- Built-in security and compliance  
- Serverless architecture  

**Example:** Store user session data with automatic scaling based on traffic patterns.

**72. Explain DynamoDB tables, items, and attributes.**  
- **Table:** Top-level container for data  
- **Item:** Individual record in a table (like a row)  
- **Attribute:** Key-value pair within an item (like a column)  

**Example:** User table with items containing attributes like `userId`, `name`, `email`, `createdDate`.

**73. What is a DynamoDB partition key and sort key?**  
- **Partition Key:** Required primary key attribute that determines data distribution across partitions  
- **Sort Key:** Optional attribute that defines sort order within a partition  

**Example:** `userId` as partition key, `timestamp` as sort key for time-series user activity data.

**74. How does DynamoDB scaling work?**  
DynamoDB automatically scales based on throughput requirements:  

- **On-Demand:** Pay per request, automatic scaling  
- **Provisioned:** Set read/write capacity units, auto-scaling enabled  
- **Auto-scaling:** Automatically adjusts capacity based on usage  

**Example:** On-demand mode scales from 1 to millions of requests without capacity planning.

**75. Explain DynamoDB Local Secondary Index (LSI) vs Global Secondary Index (GSI).**  
- **LSI:** Shares partition key with base table, different sort key, same partition  
- **GSI:** Can have different partition and sort keys, spans all partitions  

**Example:** LSI for querying user orders by date, GSI for querying all orders by product category.

**76. What is DynamoDB Streams?**  
DynamoDB Streams captures item-level modifications in DynamoDB tables in near real-time.  

**Use Cases:**  
- Cross-region replication  
- Event-driven architectures  
- Data synchronization  
- Audit trails  

**Example:** Trigger Lambda function when user profile is updated to send notification email.

**77. How do you backup DynamoDB tables?**  
- **On-Demand Backup:** Manual backups with 35-day retention  
- **Point-in-Time Recovery:** Continuous backups for 35 days  
- **AWS Backup:** Centralized backup management  
- **Export to S3:** Export table data to S3  

**Example:** Enable point-in-time recovery for automatic backup every 5 minutes.

**78. Explain DynamoDB conditional writes.**  
Conditional writes only succeed if specified conditions are met, preventing concurrent modification issues.  

**Example:** Update user balance only if current balance >= withdrawal amount.

```javascript
// Conditional update example
await docClient.update({
  TableName: 'Users',
  Key: { userId: '123' },
  UpdateExpression: 'SET balance = balance - :amount',
  ConditionExpression: 'balance >= :amount',
  ExpressionAttributeValues: { ':amount': 100 }
}).promise();
```

**79. What is DynamoDB Time to Live (TTL)?**  
TTL automatically deletes items after a specified timestamp, reducing storage costs and improving performance.  

**Use Cases:**  
- Session data cleanup  
- Temporary data removal  
- Log retention policies  

**Example:** Delete user sessions older than 24 hours automatically.

**80. How do you query DynamoDB?**  
- **Query:** Retrieve items by partition key (and sort key)  
- **Scan:** Examine all items in table (expensive, avoid for large tables)  
- **GetItem:** Retrieve single item by primary key  

**Example:** Query user orders by `userId` partition key and `orderDate` sort key range.

**81. Explain DynamoDB pagination.**  
DynamoDB returns results in pages to handle large result sets efficiently.  

**Implementation:**  
- Use `LastEvaluatedKey` for next page  
- Set `Limit` parameter for page size  
- Handle pagination in application code  

**Example:** Retrieve 100 items per page with continuation token for next page.

**82. What is DynamoDB Accelerator (DAX)?**  
DAX is an in-memory cache for DynamoDB that improves read performance by up to 10x.  

**Benefits:**  
- Microsecond response times  
- Reduces DynamoDB read capacity usage  
- Compatible with existing DynamoDB APIs  

**Example:** Cache frequently accessed user profile data to reduce latency.

**83. How do you handle DynamoDB hot partitions?**  
Hot partitions occur when one partition receives too much traffic.  

**Solutions:**  
- **Randomize partition keys:** Add random suffix/prefix  
- **Use composite keys:** Combine with sort key for better distribution  
- **Implement write sharding:** Distribute writes across multiple items  

**Example:** Instead of partition key `userId`, use `userId#randomSuffix` to distribute load.

**84. Explain DynamoDB transactions.**  
DynamoDB transactions provide ACID properties for multiple item operations.  

**Types:**  
- **TransactWriteItems:** Multiple write operations  
- **TransactGetItems:** Multiple read operations  

**Example:** Transfer money between two accounts atomically.

**85. What is DynamoDB global tables?**  
Global tables replicate DynamoDB tables across multiple AWS regions for multi-region applications.  

**Benefits:**  
- Low-latency global access  
- Disaster recovery  
- Regional failover  

**Example:** Deploy application in multiple regions with automatic cross-region replication.

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

### Answers for RDS

**86. What is Amazon RDS?**  
Amazon RDS is a managed relational database service that simplifies database setup, operation, and scaling.  

**Supported Engines:**  
- MySQL, PostgreSQL, MariaDB  
- Oracle, SQL Server  
- Aurora (MySQL/PostgreSQL compatible)  

**Benefits:**  
- Automated backups and patching  
- High availability with Multi-AZ  
- Read replicas for scaling  
- Managed security and compliance  

**Example:** Deploy PostgreSQL database without managing underlying EC2 instances or storage.

**87. Explain different RDS engines (MySQL, PostgreSQL, etc.).**  
- **MySQL:** Popular open-source RDBMS, good for web applications  
- **PostgreSQL:** Advanced open-source RDBMS with JSON support  
- **MariaDB:** MySQL fork with additional features  
- **Oracle:** Enterprise RDBMS with advanced features  
- **SQL Server:** Microsoft's RDBMS for Windows applications  
- **Aurora:** AWS's high-performance MySQL/PostgreSQL-compatible engine  

**Example:** Choose PostgreSQL for applications requiring complex queries and JSON operations.

**88. How do you connect to an RDS instance?**  
- **Endpoint:** Use the RDS endpoint hostname  
- **Security Groups:** Allow inbound traffic on port 3306 (MySQL), 5432 (PostgreSQL)  
- **SSL/TLS:** Enable SSL for encrypted connections  
- **IAM Authentication:** Use IAM users instead of database users  

**Example:** Connect using: `psql -h mydb.xxxxxxx.us-east-1.rds.amazonaws.com -U admin -d mydatabase`

**89. What is RDS Multi-AZ deployment?**  
Multi-AZ deployment creates a standby replica in a different Availability Zone for high availability.  

**Benefits:**  
- Automatic failover (typically <60 seconds)  
- Data durability during AZ failures  
- No data loss during failover  

**Example:** Production database automatically fails over to standby instance if primary AZ fails.

**90. Explain RDS Read Replicas.**  
Read replicas are read-only copies of the primary database for scaling read operations.  

**Features:**  
- Asynchronous replication  
- Multiple replicas per source  
- Cross-region replication  
- Can be promoted to standalone database  

**Example:** Create 3 read replicas to handle 10x read traffic from primary database.

**91. How do you backup RDS databases?**  
- **Automated Backups:** Daily snapshots during backup window  
- **Manual Snapshots:** User-initiated backups  
- **Point-in-Time Recovery:** Restore to any point in time  
- **Cross-Region Snapshots:** Copy snapshots to other regions  

**Example:** Enable automated backups with 7-day retention and create manual snapshot before major changes.

**92. What is RDS Aurora and its benefits?**  
Aurora is AWS's high-performance relational database engine compatible with MySQL and PostgreSQL.  

**Benefits:**  
- Up to 5x better performance than standard MySQL/PostgreSQL  
- Automatic storage scaling to 128TB  
- 6-way replication across 3 AZs  
- Continuous backup to S3  
- Faster failover (<30 seconds)  

**Example:** Migrate from standard MySQL to Aurora for better performance and availability.

**93. Explain RDS parameter groups and option groups.**  
- **Parameter Groups:** Database engine configuration parameters  
- **Option Groups:** Additional features like backup compression, monitoring  

**Example:** Create parameter group to set `max_connections` and `innodb_buffer_pool_size` for MySQL.

**94. How do you monitor RDS?**  
- **CloudWatch Metrics:** CPU, memory, disk, connections  
- **Enhanced Monitoring:** OS-level metrics  
- **Performance Insights:** SQL query analysis  
- **RDS Events:** Notifications for important events  

**Example:** Monitor database connections and set alarm when >80% of max connections used.

**95. What is RDS Proxy?**  
RDS Proxy is a fully managed database proxy that improves application scalability and security.  

**Benefits:**  
- Connection pooling and multiplexing  
- Automatic failover handling  
- IAM authentication support  
- Reduced database load  

**Example:** Use RDS Proxy for Lambda functions to avoid exhausting database connections.

**96. Explain RDS storage auto-scaling.**  
Storage auto-scaling automatically increases storage capacity when needed, up to specified maximum.  

**Features:**  
- Increases in 10GB increments  
- No downtime during scaling  
- Configurable maximum storage limit  

**Example:** Set maximum storage to 1000GB with auto-scaling enabled for growing application.

**97. How do you migrate to RDS?**  
- **AWS DMS:** Database Migration Service for ongoing replication  
- **Native tools:** mysqldump, pg_dump for one-time migration  
- **AWS SCT:** Schema Conversion Tool for heterogeneous migrations  

**Example:** Use DMS to migrate from on-premises MySQL to RDS Aurora with minimal downtime.

**98. What is RDS Performance Insights?**  
Performance Insights monitors database performance and helps identify bottlenecks.  

**Features:**  
- SQL query analysis  
- Database load visualization  
- Wait event analysis  
- Historical performance data  

**Example:** Identify slow queries causing high CPU usage and optimize them.

**99. Explain RDS Serverless.**  
RDS Serverless automatically scales compute capacity based on application demand.  

**Benefits:**  
- Pay only for capacity used  
- Automatic scaling from 0.5 to 64 ACUs  
- No capacity planning required  

**Example:** Development databases that scale down to zero when not in use.

**100. How do you secure RDS?**  
- **VPC Security Groups:** Network-level access control  
- **SSL/TLS Encryption:** Encrypt data in transit  
- **Storage Encryption:** Encrypt data at rest using KMS  
- **IAM Authentication:** Database access using IAM users  
- **Database Users:** Traditional username/password  
- **RDS Proxy:** Additional security layer  

**Example:** Use SSL encryption and IAM authentication for secure database connections.

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

### Answers for VPC

**101. What is Amazon VPC?**  
Amazon VPC is a virtual network dedicated to your AWS account that provides complete control over your virtual networking environment.  

**Key Features:**  
- Custom IP address ranges  
- Subnets and routing tables  
- Network ACLs and security groups  
- VPN connections and Direct Connect  
- Multiple Availability Zones  

**Example:** Create isolated network environment for your application with custom IP ranges.

**102. Explain VPC subnets (public vs private).**  
- **Public Subnet:** Has route to Internet Gateway, instances can access internet directly  
- **Private Subnet:** No direct internet access, uses NAT Gateway for outbound traffic  

**Example:** Web servers in public subnet, database servers in private subnet for security.

**103. What is an Internet Gateway?**  
Internet Gateway enables communication between instances in VPC and the internet.  

**Functions:**  
- Provides NAT for instances with public IPs  
- Routes traffic between VPC and internet  
- Required for public subnets  

**Example:** Attach Internet Gateway to VPC to allow EC2 instances to access the internet.

**104. Explain NAT Gateway vs NAT Instance.**  
- **NAT Gateway:** Managed AWS service, highly available, automatic scaling  
- **NAT Instance:** EC2 instance configured as NAT, manual management  

**Example:** Use NAT Gateway for production workloads, NAT Instance for cost optimization in dev environments.

**105. What is a VPC Peering?**  
VPC Peering allows routing traffic between two VPCs using private IP addresses.  

**Use Cases:**  
- Cross-account resource sharing  
- Multi-region connectivity  
- Shared services architecture  

**Example:** Peer development VPC with production VPC for database access.

**106. How do you secure VPC?**  
- **Security Groups:** Instance-level firewalls  
- **Network ACLs:** Subnet-level firewalls  
- **VPC Flow Logs:** Network traffic monitoring  
- **VPC Endpoints:** Private AWS service access  
- **AWS WAF:** Web application firewall  

**Example:** Use security groups to restrict SSH access to specific IP ranges only.

**107. Explain VPC Flow Logs.**  
VPC Flow Logs capture information about IP traffic going to and from network interfaces in VPC.  

**Captured Data:**  
- Source/destination IP and port  
- Protocol, packets, bytes  
- Action (accept/reject)  
- Start/end time  

**Example:** Monitor traffic patterns and detect security threats using flow logs.

**108. What is AWS Direct Connect?**  
Direct Connect provides dedicated network connection from on-premises to AWS.  

**Benefits:**  
- Consistent network performance  
- Reduced bandwidth costs  
- Increased security  
- Lower latency than VPN  

**Example:** Connect corporate data center to AWS VPC with 1Gbps dedicated connection.

**109. Explain VPC Endpoints.**  
VPC Endpoints enable private connections to AWS services without internet access.  

**Types:**  
- **Gateway Endpoints:** For S3 and DynamoDB  
- **Interface Endpoints:** For most other AWS services  

**Example:** Use S3 gateway endpoint to access S3 buckets from private subnet without NAT.

**110. How do you design a highly available VPC?**  
- **Multi-AZ Design:** Resources across multiple AZs  
- **Redundant Components:** Multiple NAT Gateways, Internet Gateways  
- **Auto Scaling:** EC2 Auto Scaling groups  
- **Load Balancers:** ALB/NLB for traffic distribution  

**Example:** Deploy application servers in Auto Scaling group across 3 AZs with ALB.

**111. What is AWS Transit Gateway?**  
Transit Gateway connects VPCs and on-premises networks through a central hub.  

**Benefits:**  
- Simplifies network architecture  
- Centralized routing management  
- Supports thousands of VPCs  
- Integration with Direct Connect and VPN  

**Example:** Connect 50 VPCs across multiple accounts through single Transit Gateway.

**112. Explain VPC Security Groups vs Network ACLs.**  
- **Security Groups:** Stateful, instance-level, allow rules only  
- **Network ACLs:** Stateless, subnet-level, allow and deny rules  

**Example:** Security Group allows inbound HTTP, Network ACL blocks specific malicious IP addresses.

**113. How do you troubleshoot VPC connectivity issues?**  
- **VPC Reachability Analyzer:** Automated network diagnostics  
- **VPC Flow Logs:** Analyze traffic patterns  
- **Network ACLs/Security Groups:** Check rules  
- **Route Tables:** Verify routing configuration  
- **Subnet Associations:** Ensure correct subnet assignments  

**Example:** Use Reachability Analyzer to check if EC2 instance can reach RDS database.

**114. What is AWS VPN?**  
AWS VPN establishes secure connections between on-premises networks and AWS VPC.  

**Types:**  
- **Site-to-Site VPN:** Connect remote networks  
- **Client VPN:** Individual user connections  

**Example:** Connect branch office to AWS VPC using Site-to-Site VPN.

**115. Explain VPC sharing.**  
VPC sharing allows multiple AWS accounts to create resources in a shared VPC.  

**Benefits:**  
- Centralized VPC management  
- Cost optimization  
- Simplified network architecture  

**Example:** Share VPC with multiple development teams while maintaining security boundaries.

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

### Answers for IAM

**116. What is AWS IAM?**  
AWS IAM is a web service that helps you securely control access to AWS resources.  

**Key Components:**  
- Users, groups, and roles  
- Policies and permissions  
- Multi-factor authentication  
- Identity federation  

**Example:** Create IAM user for developer with permissions to launch EC2 instances but not terminate them.

**117. Explain IAM users, groups, and roles.**  
- **Users:** Individual identities with long-term credentials  
- **Groups:** Collections of users with shared permissions  
- **Roles:** Temporary permissions for AWS services or federated users  

**Example:** Create 'Developers' group with EC2 and S3 permissions, assign users to group.

**118. What is the difference between IAM policies and permissions?**  
- **Policies:** JSON documents defining permissions  
- **Permissions:** Actual access granted by policies  

**Example:** Policy document specifies "Allow" action on "s3:GetObject", granting read permission to S3.

**119. Explain IAM policy types (managed vs inline).**  
- **Managed Policies:** Standalone policies that can be attached to multiple users/groups/roles  
- **Inline Policies:** Policies embedded directly in user/group/role  

**Example:** Use managed policy for common permissions, inline policy for specific user requirements.

**120. What is IAM MFA (Multi-Factor Authentication)?**  
MFA adds extra security layer requiring second form of authentication beyond password.  

**Types:**  
- Virtual MFA devices (Google Authenticator)  
- Hardware MFA devices  
- SMS text message MFA  

**Example:** Enable MFA for root account and IAM users with high privileges.

**121. How do you implement least privilege in IAM?**  
Grant minimum permissions required for users/roles to perform their tasks.  

**Steps:**  
- Start with no permissions  
- Add permissions as needed  
- Use IAM Access Analyzer to identify unused permissions  
- Regular permission reviews  

**Example:** Developer needs only read access to S3 bucket, not write or delete permissions.

**122. Explain IAM cross-account access.**  
Allow users from one AWS account to access resources in another account.  

**Methods:**  
- IAM roles with trust policies  
- Resource-based policies  
- AWS Organizations  

**Example:** Allow development account users to access production S3 buckets for deployment.

**123. What is AWS STS (Security Token Service)?**  
STS provides temporary security credentials for AWS access.  

**Use Cases:**  
- Cross-account access  
- Federation  
- Mobile applications  
- Temporary elevated privileges  

**Example:** Generate temporary credentials for mobile app to access S3.

**124. How do you rotate IAM access keys?**  
Regularly update access keys to maintain security.  

**Process:**  
- Create new access key  
- Update applications with new key  
- Delete old access key  
- Use IAM credential reports to track usage  

**Example:** Rotate access keys every 90 days as per security policy.

**125. Explain IAM policy evaluation logic.**  
AWS evaluates all applicable policies using explicit deny overrides allow.  

**Order:**  
1. Check for explicit deny  
2. Check for explicit allow  
3. Default deny if no match  

**Example:** SCP denies all actions, IAM policy allows specific actions - result is deny.

**126. What is IAM Access Analyzer?**  
Access Analyzer helps identify resources shared with external entities.  

**Features:**  
- Find unintended access  
- Generate least-privilege policies  
- Cross-account resource sharing  

**Example:** Identify S3 buckets accessible by public or external accounts.

**127. How do you audit IAM?**  
- **CloudTrail:** Logs all IAM API calls  
- **IAM Credential Reports:** User access key usage  
- **Access Analyzer:** External access findings  
- **Config Rules:** Compliance monitoring  

**Example:** Use CloudTrail to track who created new IAM users and when.

**128. Explain IAM identity providers.**  
Identity providers enable external user authentication for AWS access.  

**Types:**  
- SAML 2.0 providers  
- OpenID Connect providers  
- Custom identity brokers  

**Example:** Configure SAML provider for corporate Active Directory integration.

**129. What is AWS Organizations SCP (Service Control Policies)?**  
SCPs set maximum permissions for accounts in AWS Organizations.  

**Features:**  
- Organization-wide guardrails  
- Cannot be overridden by IAM policies  
- Applied at account level  

**Example:** SCP prevents all accounts from using regions except us-east-1 and eu-west-1.

**130. How do you manage IAM at scale?**  
- **AWS Organizations:** Centralized account management  
- **IAM Identity Center:** Single sign-on across accounts  
- **Permission sets:** Reusable permission templates  
- **Automated provisioning:** Infrastructure as Code  

**Example:** Use Terraform to manage IAM roles and policies across multiple accounts.

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

### Answers for CloudWatch

**131. What is Amazon CloudWatch?**  
CloudWatch is a monitoring and observability service that provides data and actionable insights for AWS resources and applications.  

**Key Features:**  
- Metrics collection and monitoring  
- Log aggregation and analysis  
- Alarms and notifications  
- Dashboards and visualization  

**Example:** Monitor EC2 CPU utilization and trigger auto-scaling when >70%.

**132. Explain CloudWatch metrics, logs, and alarms.**  
- **Metrics:** Time-ordered data points (CPU usage, network traffic)  
- **Logs:** Text-based records from applications and AWS services  
- **Alarms:** Notifications based on metric thresholds  

**Example:** Metric shows CPU >80%, alarm sends SNS notification to on-call engineer.

**133. How do you create custom CloudWatch metrics?**  
Use CloudWatch API or AWS SDK to publish custom metrics.  

**Example:**  
```javascript
const AWS = require('aws-sdk');
const cloudwatch = new AWS.CloudWatch();

await cloudwatch.putMetricData({
  MetricData: [{
    MetricName: 'UserRegistrations',
    Value: 1,
    Unit: 'Count',
    Timestamp: new Date()
  }],
  Namespace: 'MyApp'
}).promise();
```

**134. What is CloudWatch Logs Insights?**  
Logs Insights enables interactive querying of log data using SQL-like syntax.  

**Features:**  
- Fast log analysis  
- Pattern discovery  
- Statistical functions  
- Visualization  

**Example:** Query: `fields @timestamp, @message | filter @message like /ERROR/ | stats count() by bin(5m)`

**135. Explain CloudWatch dashboards.**  
Dashboards provide visual representation of metrics and logs for monitoring.  

**Features:**  
- Custom widgets and graphs  
- Real-time data visualization  
- Cross-region metrics  
- Sharing capabilities  

**Example:** Create dashboard showing application performance, error rates, and infrastructure metrics.

**136. How do you set up CloudWatch alarms?**  
1. Choose metric  
2. Set threshold and comparison operator  
3. Configure evaluation period  
4. Set up notification (SNS topic)  
5. Define alarm actions  

**Example:** Alarm triggers when Lambda errors >5 in 5-minute period, sends email notification.

**137. What is CloudWatch Events (now EventBridge)?**  
EventBridge delivers real-time events from AWS services to targets like Lambda functions.  

**Components:**  
- **Events:** State changes in AWS services  
- **Rules:** Patterns to match events  
- **Targets:** Actions to take when rule matches  

**Example:** Trigger Lambda when EC2 instance state changes to 'stopped'.

**138. Explain CloudWatch agent.**  
CloudWatch agent collects system-level metrics and logs from EC2 instances.  

**Features:**  
- CPU, memory, disk metrics  
- Custom log files  
- Windows and Linux support  
- Centralized configuration  

**Example:** Install agent on EC2 to collect application logs and system metrics.

**139. How do you monitor application logs with CloudWatch?**  
- **CloudWatch Agent:** Collect logs from EC2 instances  
- **AWS SDK:** Send logs programmatically  
- **Lambda Extensions:** Send logs from Lambda  
- **Container Insights:** Monitor containerized applications  

**Example:** Configure agent to send Apache access logs to CloudWatch for analysis.

**140. What is CloudWatch Synthetics?**  
Synthetics creates canaries to monitor application endpoints and APIs.  

**Use Cases:**  
- API availability monitoring  
- Page load performance  
- Broken link detection  
- Visual regression testing  

**Example:** Create canary to check if login page loads within 3 seconds.

**141. Explain CloudWatch Application Insights.**  
Application Insights automatically detects and sets up monitoring for applications.  

**Features:**  
- Automatic metric collection  
- Problem detection and diagnosis  
- Integration with X-Ray  
- Supported for .NET and Java applications  

**Example:** Deploy .NET application and Application Insights automatically configures monitoring.

**142. How do you troubleshoot with CloudWatch?**  
- **Metrics Analysis:** Identify performance bottlenecks  
- **Log Analysis:** Search for error patterns  
- **Alarms:** Get notified of issues  
- **Dashboards:** Visualize system health  
- **Correlations:** Link metrics with logs  

**Example:** Use Logs Insights to find error spikes correlating with CPU spikes.

**143. What is CloudWatch Container Insights?**  
Container Insights provides monitoring for containerized applications on ECS and EKS.  

**Metrics Collected:**  
- CPU and memory utilization  
- Network traffic  
- Task and pod counts  
- Container restart counts  

**Example:** Monitor microservices running on ECS with detailed container metrics.

**144. Explain CloudWatch billing alerts.**  
Billing alerts notify when AWS charges exceed specified thresholds.  

**Setup:**  
- Create billing alarm  
- Set dollar threshold  
- Configure SNS notifications  

**Example:** Alert when monthly AWS bill exceeds $1000.

**145. How do you export CloudWatch logs?**  
- **CloudWatch Export:** Export logs to S3  
- **Kinesis Data Streams:** Stream logs to other services  
- **Subscription Filters:** Send logs to Lambda, Elasticsearch  

**Example:** Export VPC Flow Logs to S3 for long-term retention and analysis.

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

### Answers for CloudFormation

**146. What is AWS CloudFormation?**  
CloudFormation is an Infrastructure as Code service that allows you to model, provision, and manage AWS resources using templates.  

**Benefits:**  
- Declarative infrastructure definition  
- Automated resource provisioning  
- Version control and change management  
- Cross-region/cross-account deployment  

**Example:** Define entire application stack (VPC, EC2, RDS, Load Balancer) in YAML/JSON template.

**147. Explain CloudFormation templates and stacks.**  
- **Templates:** JSON/YAML files defining AWS resources and their configurations  
- **Stacks:** Collections of AWS resources created from templates  

**Example:** Template defines EC2 instance, stack creates actual running EC2 instance.

**148. How do you use CloudFormation parameters?**  
Parameters allow customization of templates without modifying the template itself.  

**Example:**  
```yaml
Parameters:
  InstanceType:
    Type: String
    Default: t3.micro
    AllowedValues: [t3.micro, t3.small, t3.medium]

Resources:
  MyEC2:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: !Ref InstanceType
```

**149. What is CloudFormation change sets?**  
Change sets preview modifications to stacks before applying them.  

**Benefits:**  
- See what will change before deployment  
- Prevent unintended modifications  
- Review resource additions/deletions  

**Example:** Preview adding new EC2 instance to existing stack before applying changes.

**150. Explain CloudFormation nested stacks.**  
Nested stacks allow breaking complex templates into smaller, reusable components.  

**Benefits:**  
- Template modularity  
- Reusability  
- Easier maintenance  

**Example:** Create separate stacks for network, database, and application layers.

**151. How do you handle CloudFormation rollbacks?**  
CloudFormation automatically rolls back failed deployments to previous state.  

**Configuration:**  
- `--on-failure` parameter (ROLLBACK, DELETE, DO_NOTHING)  
- Manual rollback using change sets  

**Example:** Stack creation fails due to invalid security group, CloudFormation terminates created resources.

**152. What is CloudFormation stack policies?**  
Stack policies prevent accidental updates or deletions of critical resources.  

**Example:** Prevent deletion of production RDS database while allowing EC2 updates.

**153. Explain CloudFormation custom resources.**  
Custom resources allow integration with non-AWS resources or complex logic.  

**Implementation:**  
- Lambda function handles custom resource logic  
- ServiceToken points to Lambda function  

**Example:** Custom resource to configure third-party monitoring tool during stack creation.

**154. How do you monitor CloudFormation stacks?**  
- **Stack Events:** Track resource creation/update status  
- **CloudTrail:** Audit CloudFormation API calls  
- **CloudWatch:** Monitor stack metrics  
- **Drift Detection:** Identify configuration changes  

**Example:** Monitor stack creation progress through Events tab in CloudFormation console.

**155. What is AWS CDK and how does it relate to CloudFormation?**  
AWS CDK is a software development framework for defining cloud infrastructure using programming languages.  

**Relationship:**  
- CDK generates CloudFormation templates  
- Supports TypeScript, Python, Java, .NET  
- Higher-level abstractions than raw CloudFormation  

**Example:** Write infrastructure code in TypeScript, CDK compiles to CloudFormation template.

**156. Explain CloudFormation drift detection.**  
Drift detection identifies differences between stack's expected and actual configuration.  

**Use Cases:**  
- Manual resource modifications  
- Configuration drift over time  
- Compliance monitoring  

**Example:** Detect if someone manually changed EC2 instance type outside CloudFormation.

**157. How do you version CloudFormation templates?**  
- **Git Version Control:** Store templates in Git repository  
- **S3 Versioning:** Enable versioning on S3 bucket storing templates  
- **Template Parameters:** Use version parameters for different environments  

**Example:** Tag template versions (v1.0, v1.1) and use specific version for deployments.

**158. What is CloudFormation stack sets?**  
Stack sets deploy stacks across multiple accounts and regions from single template.  

**Use Cases:**  
- Multi-account deployments  
- Cross-region redundancy  
- Centralized infrastructure management  

**Example:** Deploy VPC configuration to all accounts in AWS Organization.

**159. Explain CloudFormation intrinsic functions.**  
Intrinsic functions perform operations within CloudFormation templates.  

**Common Functions:**  
- `!Ref`: Reference resource attributes  
- `!GetAtt`: Get resource attributes  
- `!Sub`: Substitute variables in strings  
- `!Join`: Join values with delimiter  

**Example:** `!Sub "${AWS::StackName}-bucket"` creates bucket name with stack name.

**160. How do you debug CloudFormation issues?**  
- **Stack Events:** Check error messages in events  
- **CloudTrail:** Review API call details  
- **Template Validation:** Use `validate-template` command  
- **Change Sets:** Preview changes before applying  
- **Drift Detection:** Identify configuration differences  

**Example:** Use `aws cloudformation validate-template --template-body file://template.yaml` to check syntax.

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

### Answers for ECS/EKS

**161. What is Amazon ECS?**  
Amazon ECS is a fully managed container orchestration service that makes it easy to run, stop, and manage Docker containers on a cluster.  

**Key Features:**  
- Highly scalable container management  
- Integration with other AWS services  
- Support for both EC2 and Fargate launch types  

**Example:** Run microservices as Docker containers with automatic scaling and load balancing.

**162. Explain ECS clusters, services, and tasks.**  
- **Clusters:** Logical groupings of EC2 instances or Fargate tasks  
- **Services:** Maintain specified number of running tasks  
- **Tasks:** Running instances of task definitions  

**Example:** Cluster contains 3 EC2 instances, service maintains 6 running web server tasks.

**163. What is Amazon EKS?**  
Amazon EKS is a managed Kubernetes service that makes it easy to run Kubernetes on AWS.  

**Benefits:**  
- Fully managed Kubernetes control plane  
- Automatic updates and patching  
- Integration with AWS services  
- Security and compliance  

**Example:** Run Kubernetes workloads without managing the Kubernetes control plane.

**164. How do you choose between ECS and EKS?**  
- **Choose ECS if:** Simple container orchestration, AWS-native, learning curve  
- **Choose EKS if:** Need Kubernetes ecosystem, complex applications, portability  

**Example:** Use ECS for simple microservices, EKS for complex applications with existing Kubernetes expertise.

**165. Explain ECS task definitions.**  
Task definitions are JSON files that describe how to run Docker containers in ECS.  

**Components:**  
- Container definitions  
- CPU and memory requirements  
- Networking configuration  
- Environment variables  

**Example:** Define task with nginx container, 512MB memory, port 80 mapping.

**166. What is ECS Fargate?**  
Fargate is a serverless compute engine for containers that eliminates need to manage servers.  

**Benefits:**  
- No server management  
- Pay only for resources used  
- Automatic scaling  
- Security patching handled by AWS  

**Example:** Run containers without provisioning or managing EC2 instances.

**167. How do you deploy applications on ECS?**  
1. Create task definition  
2. Create service with desired count  
3. Configure load balancer (optional)  
4. Update service with new task definition  

**Example:** Blue-green deployment using CodeDeploy with ECS.

**168. Explain EKS node groups.**  
Node groups are EC2 instances that serve as worker nodes in EKS cluster.  

**Types:**  
- **Managed Node Groups:** AWS manages EC2 instances  
- **Self-Managed Node Groups:** You manage EC2 instances  
- **Fargate Profile:** Serverless pods  

**Example:** Create managed node group with 3 t3.medium instances for application workloads.

**169. What is Kubernetes and how does EKS relate?**  
Kubernetes is an open-source container orchestration platform. EKS provides managed Kubernetes service.  

**Relationship:**  
- EKS runs upstream Kubernetes  
- AWS manages control plane  
- You manage worker nodes and applications  

**Example:** Use kubectl to manage applications on EKS cluster.

**170. How do you monitor ECS/EKS?**  
- **CloudWatch Container Insights:** Detailed container metrics  
- **CloudWatch Logs:** Container logs  
- **X-Ray:** Distributed tracing  
- **Prometheus:** Custom metrics collection  

**Example:** Use Container Insights to monitor CPU/memory usage of all containers in cluster.

**171. Explain ECS service discovery.**  
Service discovery allows containers to discover and connect to each other.  

**Methods:**  
- **Service Discovery:** AWS Cloud Map integration  
- **Service Connect:** Simplified service-to-service communication  
- **Load Balancer:** External service discovery  

**Example:** Frontend service discovers backend API using service discovery name.

**172. What is AWS App Mesh?**  
App Mesh is a service mesh that provides application-level networking for microservices.  

**Features:**  
- Traffic routing and load balancing  
- Service-to-service authentication  
- Observability and tracing  

**Example:** Implement canary deployments and circuit breakers for microservices.

**173. How do you handle logging in ECS/EKS?**  
- **CloudWatch Logs:** Centralized logging  
- **Fluentd/Fluent Bit:** Log shipping  
- **ELK Stack:** Elasticsearch, Logstash, Kibana  
- **AWS FireLens:** Custom log routing  

**Example:** Configure ECS task to send application logs to CloudWatch Logs.

**174. Explain ECS capacity providers.**  
Capacity providers manage the infrastructure capacity for ECS tasks.  

**Types:**  
- **Fargate:** Serverless capacity  
- **EC2:** Auto Scaling group capacity  
- **Fargate Spot:** Cost-optimized Fargate  

**Example:** Use Fargate capacity provider for web application, EC2 for batch processing.

**175. What is AWS Copilot for ECS?**  
Copilot is a command-line tool that simplifies deploying applications to ECS.  

**Features:**  
- Environment setup  
- Application deployment  
- Service management  
- CI/CD pipeline creation  

**Example:** `copilot app init` to create ECS application with all necessary resources.

**176. How do you scale ECS services?**  
- **Service Auto Scaling:** Based on CloudWatch metrics  
- **Target Tracking:** Maintain metric at target value  
- **Step Scaling:** Scale based on alarm breaches  

**Example:** Scale web service based on CPU utilization >70%.

**177. Explain EKS add-ons.**  
EKS add-ons are software add-ons that enhance EKS cluster functionality.  

**Common Add-ons:**  
- **CoreDNS:** DNS service  
- **kube-proxy:** Network proxy  
- **EBS CSI Driver:** Persistent storage  
- **VPC CNI:** Networking  

**Example:** Install EBS CSI driver to enable persistent volumes for stateful applications.

**178. What is AWS Fargate for EKS?**  
Fargate for EKS runs Kubernetes pods without managing underlying infrastructure.  

**Benefits:**  
- No node management  
- Pod-level billing  
- Automatic scaling  
- Security isolation  

**Example:** Run individual pods on Fargate while other workloads run on EC2 nodes.

**179. How do you secure ECS/EKS?**  
- **IAM Roles:** Task execution and task roles  
- **Security Groups:** Network-level security  
- **Secrets Management:** SSM Parameter Store, Secrets Manager  
- **Image Scanning:** Amazon ECR image scanning  
- **Network Policies:** Kubernetes network policies  

**Example:** Use task IAM role to grant S3 access to ECS containers.

**180. Explain ECS task networking modes.**  
- **Bridge Mode:** Default Docker networking  
- **Host Mode:** Uses host network stack  
- **awsvpc Mode:** Each task gets ENI with security groups  

**Example:** Use awsvpc mode for fine-grained network control and security groups per task.

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

### Answers for SNS/SQS

**181. What is Amazon SNS?**  
Amazon SNS is a fully managed pub/sub messaging service for decoupling microservices and serverless applications.  

**Key Features:**  
- Publish-subscribe pattern  
- Multiple protocols (HTTP, HTTPS, Email, SMS)  
- Message filtering  
- Dead-letter queues  

**Example:** Publish order events to SNS topic, multiple services subscribe for different processing.

**182. What is Amazon SQS?**  
Amazon SQS is a fully managed message queuing service for decoupling and scaling microservices.  

**Key Features:**  
- Reliable message delivery  
- At-least-once delivery  
- Automatic scaling  
- Dead-letter queues  

**Example:** Queue user registration requests for background processing.

**183. Explain SQS queue types (standard vs FIFO).**  
- **Standard Queues:** High throughput, at-least-once delivery, best-effort ordering  
- **FIFO Queues:** Exactly-once processing, strict ordering, lower throughput  

**Example:** Use FIFO for financial transactions requiring order, standard for log processing.

**184. How do you implement fan-out pattern with SNS and SQS?**  
1. Create SNS topic  
2. Create multiple SQS queues  
3. Subscribe SQS queues to SNS topic  
4. Publish message to topic → delivered to all queues  

**Example:** Order service publishes event, inventory, shipping, and notification services process independently.

**185. What is SQS dead-letter queues?**  
DLQs store messages that can't be processed after maximum retry attempts.  

**Use Cases:**  
- Debugging failed messages  
- Preventing poison pill messages  
- Analyzing message processing failures  

**Example:** Messages failing processing 3 times move to DLQ for analysis.

**186. How do you handle message visibility in SQS?**  
Visibility timeout prevents other consumers from processing message while being processed.  

**Configuration:**  
- Default 30 seconds  
- Can be extended during processing  
- Message becomes visible again if not deleted  

**Example:** Long-running task extends visibility timeout to prevent duplicate processing.

**187. Explain SNS message filtering.**  
Message filtering allows subscribers to receive only messages matching criteria.  

**Implementation:**  
- Set filter policy on subscription  
- Use message attributes for filtering  
- Supports string, numeric, and boolean matching  

**Example:** Email service subscribes only to high-priority notifications.

**188. What is SQS long polling?**  
Long polling reduces empty responses by waiting for messages up to specified time.  

**Benefits:**  
- Reduced API calls  
- Lower costs  
- Reduced latency when messages arrive  

**Example:** Set `WaitTimeSeconds=20` to wait up to 20 seconds for messages.

**189. How do you monitor SNS/SQS?**  
- **CloudWatch Metrics:** Message counts, delivery failures  
- **SQS Console:** Queue depth, message age  
- **SNS Console:** Topic metrics  
- **CloudTrail:** API activity logging  

**Example:** Monitor `NumberOfMessagesSent` and `NumberOfMessagesReceived` metrics.

**190. Explain SQS message groups.**  
Message groups in FIFO queues ensure ordered processing within group while allowing parallel processing across groups.  

**Example:** Process orders for different customers in parallel but maintain order per customer.

**191. What is Amazon EventBridge?**  
EventBridge is a serverless event bus service for routing events between AWS services and applications.  

**Features:**  
- Event-driven architectures  
- Custom event buses  
- Integration with 90+ AWS services  
- Schema discovery  

**Example:** Route EC2 state changes to Lambda functions for automated responses.

**192. How do you secure SNS/SQS?**  
- **IAM Policies:** Control access to topics/queues  
- **VPC Endpoints:** Private access  
- **SSE:** Server-side encryption  
- **Access Policies:** Resource-based policies  

**Example:** Use SSE-KMS to encrypt messages at rest and in transit.

**193. Explain SQS batch operations.**  
Batch operations send/receive/delete multiple messages in single API call.  

**Benefits:**  
- Reduced API calls  
- Lower costs  
- Improved throughput  

**Example:** Send up to 10 messages in single `SendMessageBatch` call.

**194. What is SNS mobile push notifications?**  
SNS supports push notifications to mobile devices through platform applications.  

**Supported Platforms:**  
- Apple Push Notification Service (APNS)  
- Firebase Cloud Messaging (FCM)  
- Amazon Device Messaging (ADM)  

**Example:** Send promotional notifications to iOS and Android app users.

**195. How do you implement retry logic with SQS?**  
- **Visibility Timeout:** Automatic retry after timeout  
- **MaxReceiveCount:** Move to DLQ after max attempts  
- **Backoff Strategy:** Exponential backoff in application  

**Example:** Implement exponential backoff: 1s, 2s, 4s, 8s delays between retries.

**196. Explain SNS topic encryption.**  
SNS supports encryption of messages using AWS KMS.  

**Features:**  
- Encryption at rest  
- Customer-managed keys  
- Cross-region replication support  

**Example:** Enable encryption on SNS topic to protect sensitive notification data.

**197. What is SQS FIFO throughput limits?**  
FIFO queues have lower throughput limits compared to standard queues.  

**Limits:**  
- 300 messages/second without batching  
- 3000 messages/second with batching  
- Per message group ID  

**Example:** Use multiple message group IDs to increase FIFO queue throughput.

**198. How do you handle large messages in SQS?**  
- **S3 Integration:** Store large payload in S3, send S3 URL in message  
- **Message Size Limit:** 256KB for SQS  
- **Extended Client Library:** Automatic S3 integration  

**Example:** Use Amazon SQS Extended Client Library for messages >256KB.

**199. Explain SNS subscription confirmation.**  
SNS requires subscription confirmation to prevent spam and ensure valid endpoints.  

**Process:**  
- Subscriber receives confirmation message  
- Must confirm subscription via link or API  
- Prevents unauthorized subscriptions  

**Example:** Email subscription sends confirmation email with subscribe link.

**200. What is Amazon MQ?**  
Amazon MQ is a managed message broker service for Apache ActiveMQ and RabbitMQ.  

**Benefits:**  
- Easy migration from on-premises  
- Managed infrastructure  
- High availability  
- Integration with existing applications  

**Example:** Migrate existing ActiveMQ deployment to Amazon MQ without code changes.

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

### Answers for CodePipeline/CodeBuild

**201. What is AWS CodePipeline?**  
CodePipeline is a continuous delivery service that automates release pipelines for fast and reliable application updates.  

**Key Features:**  
- Visual workflow for CI/CD  
- Integration with multiple AWS services  
- Manual approval steps  
- Parallel execution  

**Example:** Automate build, test, and deployment of web application from GitHub to production.

**202. What is AWS CodeBuild?**  
CodeBuild is a fully managed build service that compiles source code, runs tests, and produces ready-to-deploy artifacts.  

**Key Features:**  
- Pre-configured build environments  
- Custom build environments  
- Parallel builds  
- Integration with popular tools  

**Example:** Build Docker images and run unit tests in isolated environment.

**203. How do you set up a CI/CD pipeline with CodePipeline?**  
1. Create pipeline  
2. Configure source stage (GitHub, CodeCommit)  
3. Add build stage (CodeBuild)  
4. Add deploy stage (ECS, Lambda, etc.)  
5. Configure approval gates (optional)  

**Example:** Source → Build → Test → Deploy to staging → Manual approval → Deploy to production.

**204. Explain CodeBuild build specifications.**  
Buildspec is a YAML file that defines build commands and settings for CodeBuild.  

**Sections:**  
- `version`: Buildspec version  
- `phases`: Install, pre_build, build, post_build  
- `artifacts`: Files to upload to S3  

**Example:**  
```yaml
version: 0.2
phases:
  build:
    commands:
      - npm install
      - npm run build
artifacts:
  files:
    - '**/*'
  base-directory: 'dist'
```

**205. What is AWS CodeCommit?**  
CodeCommit is a fully managed source control service that hosts Git repositories.  

**Features:**  
- Private Git repositories  
- High availability  
- Integration with AWS services  
- No repository size limits  

**Example:** Store application source code in CodeCommit repository integrated with CodePipeline.

**206. How do you integrate CodePipeline with GitHub?**  
1. Create GitHub connection using AWS CodeStar Connections  
2. Configure webhook for automatic triggers  
3. Set up source action in CodePipeline  
4. Grant necessary permissions  

**Example:** Push to GitHub main branch automatically triggers CodePipeline execution.

**207. Explain CodeBuild environments.**  
CodeBuild provides pre-configured and custom build environments.  

**Types:**  
- **Managed Images:** AWS-curated environments  
- **Custom Images:** Docker images from ECR  
- **Windows/Linux/macOS:** Different operating systems  

**Example:** Use Ubuntu 20.04 with Node.js 16 for building React application.

**208. What is AWS CodeDeploy?**  
CodeDeploy automates application deployments to EC2, Lambda, and ECS.  

**Deployment Types:**  
- **In-place:** Update existing instances  
- **Blue-green:** Create new environment  
- **Canary:** Gradual traffic shift  

**Example:** Deploy new version of application to Auto Scaling group with zero downtime.

**209. How do you handle build artifacts?**  
- **S3 Storage:** Store build outputs in S3 buckets  
- **Artifact Names:** Version artifacts for tracking  
- **Encryption:** Enable SSE for security  
- **Retention:** Configure lifecycle policies  

**Example:** Store Docker images in ECR, application bundles in S3 with versioning.

**210. Explain CodePipeline stages and actions.**  
- **Stages:** Logical divisions of pipeline (Source, Build, Deploy)  
- **Actions:** Individual tasks within stages  
- **Action Types:** Source, Build, Deploy, Test, Approval  

**Example:** Source stage with GitHub action, Build stage with CodeBuild action.

**211. What is AWS CodeStar?**  
CodeStar provides a unified user interface for managing software development activities on AWS.  

**Features:**  
- Project templates  
- Integrated CI/CD  
- Team collaboration  
- Issue tracking  

**Example:** Create Node.js web application project with pre-configured CodePipeline.

**212. How do you monitor CodePipeline/CodeBuild?**  
- **CloudWatch Metrics:** Build duration, success rates  
- **CloudWatch Logs:** Detailed build logs  
- **CodePipeline Console:** Pipeline execution status  
- **Notifications:** SNS for pipeline state changes  

**Example:** Monitor build success rate and get notified on build failures.

**213. Explain CodeBuild local builds.**  
Local builds allow testing buildspec locally before committing.  

**Setup:**  
- Install CodeBuild agent  
- Run builds locally  
- Debug build issues before CI  

**Example:** Test build process locally with `codebuild_build.sh` script.

**214. What is AWS CodeArtifact?**  
CodeArtifact is a fully managed artifact repository service for storing software packages.  

**Supported Formats:**  
- npm, PyPI, Maven  
- NuGet, RubyGems  
- Generic artifacts  

**Example:** Store private npm packages for Node.js applications.

**215. How do you secure CodePipeline?**  
- **IAM Roles:** Least privilege for pipeline execution  
- **VPC Configuration:** Run builds in private subnets  
- **Artifact Encryption:** SSE for stored artifacts  
- **Webhook Secrets:** Secure GitHub integration  

**Example:** Use IAM roles with minimal permissions for CodeBuild projects.

**216. Explain CodeBuild test reports.**  
Test reports provide detailed information about test execution in CodeBuild.  

**Formats:**  
- JUnit XML  
- Cucumber JSON  
- TestNG XML  

**Example:** Generate JUnit reports for unit tests and view results in CodeBuild console.

**217. What is AWS CodeGuru?**  
CodeGuru provides intelligent recommendations for improving code quality and performance.  

**Components:**  
- **CodeGuru Reviewer:** Code quality analysis  
- **CodeGuru Profiler:** Application performance analysis  

**Example:** CodeGuru suggests optimizing slow database queries in application.

**218. How do you implement blue-green deployments?**  
Blue-green deployment creates parallel production environment.  

**Process:**  
1. Deploy new version to green environment  
2. Test green environment  
3. Switch traffic from blue to green  
4. Keep blue as rollback option  

**Example:** Use CodeDeploy with ECS for blue-green container deployments.

**219. Explain CodePipeline approval actions.**  
Approval actions pause pipeline execution for manual review.  

**Configuration:**  
- SNS notifications  
- Custom message  
- Timeout settings  
- Approval rules  

**Example:** Require manager approval before deploying to production environment.

**220. What is AWS CodeBuild batch builds?**  
Batch builds allow running multiple builds in parallel from single source.  

**Use Cases:**  
- Multi-platform builds  
- Matrix builds  
- Parallel test execution  

**Example:** Build application for multiple architectures (x86, ARM) simultaneously.

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

### Answers for CloudFront

**221. What is Amazon CloudFront?**  
CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally.  

**Key Features:**  
- Global edge network (400+ points of presence)  
- Low latency and high transfer speeds  
- Integration with AWS services  
- DDoS protection via AWS Shield  

**Example:** Distribute static website content from S3 with global users accessing via nearest edge location.

**222. Explain CloudFront distributions.**  
Distributions define how CloudFront delivers content from origins to end users.  

**Types:**  
- **Web Distributions:** For websites and web applications  
- **RTMP Distributions:** For streaming media (deprecated)  

**Example:** Create web distribution with S3 origin for static website hosting.

**223. What is CloudFront origins?**  
Origins are the source of content that CloudFront distributes.  

**Types:**  
- **S3 Buckets:** For static content  
- **EC2 Instances:** For dynamic content  
- **Load Balancers:** For application distribution  
- **Custom Origins:** External servers  

**Example:** Use ALB as origin for dynamic web application behind CloudFront.

**224. How do you configure CloudFront behaviors?**  
Behaviors define how CloudFront processes requests for different content types.  

**Configuration:**  
- Path patterns  
- Origin selection  
- Caching policies  
- Function associations  

**Example:** Route `/api/*` to API Gateway, `/*` to S3 bucket.

**225. Explain CloudFront caching.**  
CloudFront caches content at edge locations to reduce latency and origin load.  

**Cache Control:**  
- **TTL Settings:** Time to live for cached content  
- **Cache Keys:** Determine cache uniqueness  
- **Invalidation:** Force cache refresh  

**Example:** Cache static assets for 1 year, API responses for 5 minutes.

**226. What is CloudFront Functions?**  
CloudFront Functions are lightweight functions that run at CloudFront edge locations.  

**Use Cases:**  
- URL rewrites/redirects  
- Header manipulation  
- Access control  
- A/B testing  

**Example:** Add security headers to all responses at edge.

**227. How do you secure CloudFront?**  
- **SSL/TLS:** HTTPS enforcement  
- **AWS WAF:** Web application firewall  
- **Signed URLs/Cookies:** Restrict access  
- **Origin Access Identity:** Secure S3 access  
- **Field-level Encryption:** Encrypt sensitive data  

**Example:** Use signed URLs to restrict access to premium content.

**228. Explain CloudFront signed URLs.**  
Signed URLs allow access to private content with time-limited permissions.  

**Components:**  
- Base URL  
- Policy statement (time restrictions)  
- Signature for authentication  

**Example:** Generate signed URL allowing access to private video for 24 hours.

**229. What is CloudFront Lambda@Edge?**  
Lambda@Edge runs Lambda functions at CloudFront edge locations for content customization.  

**Use Cases:**  
- Dynamic content generation  
- Real-time image processing  
- Authentication/authorization  
- A/B testing  

**Example:** Resize images dynamically based on device type at edge.

**230. How do you monitor CloudFront?**  
- **CloudWatch Metrics:** Requests, data transfer, error rates  
- **Real-time Logs:** Detailed request logs  
- **Access Logs:** To S3/Kinesis for analysis  
- **CloudFront Console:** Distribution analytics  

**Example:** Monitor cache hit ratio and 4XX/5XX error rates.

**231. Explain CloudFront price classes.**  
Price classes determine which edge locations CloudFront uses.  

**Classes:**  
- **Price Class All:** All edge locations (most expensive)  
- **Price Class 200:** Most locations except most expensive  
- **Price Class 100:** Least expensive locations only  

**Example:** Use Price Class 100 for cost optimization if users are in specific regions.

**232. What is CloudFront field-level encryption?**  
Field-level encryption protects sensitive data by encrypting specific fields in requests.  

**Process:**  
- Client encrypts sensitive fields  
- CloudFront forwards encrypted data  
- Origin decrypts using private key  

**Example:** Encrypt credit card numbers in payment form submissions.

**233. How do you invalidate CloudFront cache?**  
Cache invalidation forces CloudFront to fetch fresh content from origin.  

**Methods:**  
- **Invalidation Requests:** Specific paths or patterns  
- **Versioned Files:** Change file names  
- **Cache Behaviors:** Short TTL for dynamic content  

**Example:** Create invalidation for `/index.html` after content update.

**234. Explain CloudFront real-time logs.**  
Real-time logs provide immediate visibility into CloudFront requests.  

**Features:**  
- Sub-second delivery  
- Customizable fields  
- Integration with Kinesis  

**Example:** Monitor traffic spikes in real-time during product launches.

**235. What is AWS Global Accelerator?**  
Global Accelerator improves availability and performance of applications with global users.  

**Features:**  
- Static IP addresses  
- Automatic routing to healthy endpoints  
- TCP/UDP support  

**Example:** Accelerate gaming application with low-latency connections worldwide.

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

### Answers for Route 53

**236. What is Amazon Route 53?**  
Route 53 is a highly available and scalable Domain Name System (DNS) web service.  

**Key Features:**  
- Domain registration  
- DNS routing  
- Health checking  
- Traffic flow management  

**Example:** Register domain and route traffic to EC2 instances with automatic failover.

**237. Explain Route 53 routing policies.**  
Routing policies determine how Route 53 responds to DNS queries.  

**Types:**  
- **Simple:** Basic routing to single resource  
- **Weighted:** Distribute traffic by weights  
- **Latency-based:** Route to lowest latency region  
- **Failover:** Route to healthy resources  
- **Geolocation:** Route based on user location  

**Example:** Use weighted routing to distribute 70% traffic to us-east-1, 30% to eu-west-1.

**238. What is Route 53 health checks?**  
Health checks monitor the health of resources and route traffic accordingly.  

**Types:**  
- **Endpoint Health Checks:** HTTP/HTTPS/TCP checks  
- **Calculated Health Checks:** Combine multiple checks  
- **CloudWatch Alarm Health Checks:** Based on metrics  

**Example:** Health check pings application endpoint every 30 seconds, fails over if unhealthy.

**239. How do you configure DNS with Route 53?**  
1. Create hosted zone  
2. Add DNS records (A, CNAME, MX, etc.)  
3. Configure name servers  
4. Update domain registrar  

**Example:** Create A record pointing to ELB for load-balanced web application.

**240. Explain Route 53 hosted zones.**  
Hosted zones are containers for DNS records for specific domain.  

**Types:**  
- **Public Hosted Zones:** Internet-accessible domains  
- **Private Hosted Zones:** VPC-internal domains  

**Example:** Public hosted zone for `example.com`, private for `internal.example.com`.

**241. What is Route 53 Resolver?**  
Route 53 Resolver enables DNS resolution between VPC and on-premises networks.  

**Features:**  
- Inbound/Outbound endpoints  
- DNS forwarding rules  
- Integration with Direct Connect/VPN  

**Example:** Resolve on-premises domain names from AWS VPC.

**242. How do you implement DNS failover?**  
Use Route 53 failover routing policy with health checks.  

**Setup:**  
1. Create health checks for primary/secondary resources  
2. Configure failover routing policy  
3. Set primary and secondary records  

**Example:** Route to primary ELB, automatically failover to secondary if primary unhealthy.

**243. Explain Route 53 traffic flow.**  
Traffic flow provides visual editor for complex routing configurations.  

**Features:**  
- Visual policy creation  
- Version control  
- Reusable traffic policies  

**Example:** Create policy combining geolocation and latency-based routing.

**244. What is Route 53 domain registration?**  
Route 53 allows registering and managing domain names.  

**Features:**  
- 300+ TLD support  
- Automatic renewal  
- DNS management integration  
- WHOIS privacy protection  

**Example:** Register `myapp.com` domain and automatically configure DNS.

**245. How do you monitor Route 53?**  
- **CloudWatch Metrics:** Query counts, health check status  
- **Route 53 Console:** DNS query logs  
- **Health Check Status:** Real-time health status  

**Example:** Monitor DNS query latency and error rates.

**246. Explain Route 53 private hosted zones.**  
Private hosted zones provide DNS resolution within VPCs.  

**Features:**  
- VPC-specific DNS  
- Split-horizon DNS  
- Cross-account sharing  

**Example:** Resolve `db.internal` to RDS instance within VPC.

**247. What is Route 53 geolocation routing?**  
Geolocation routing routes traffic based on user geographic location.  

**Use Cases:**  
- Content localization  
- Legal compliance  
- Load distribution  

**Example:** Route European users to eu-west-1, Asian users to ap-southeast-1.

**248. How do you secure Route 53?**  
- **DNSSEC:** Domain Name System Security Extensions  
- **VPC Endpoints:** Private DNS queries  
- **IAM Policies:** Control access to Route 53 resources  
- **Private Hosted Zones:** Internal DNS security  

**Example:** Enable DNSSEC for domain to prevent DNS spoofing attacks.

**249. Explain Route 53 alias records.**  
Alias records route traffic to AWS resources without additional DNS queries.  

**Benefits:**  
- No additional charges  
- Automatic IP changes  
- Health-based routing  

**Example:** Alias record routes `www.example.com` to CloudFront distribution.

**250. What is AWS Certificate Manager?**  
ACM provides free SSL/TLS certificates for AWS services.  

**Features:**  
- Automatic renewal  
- Integration with ELB, CloudFront, API Gateway  
- Private CA support  

**Example:** Request SSL certificate for `api.example.com` and attach to API Gateway.

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

### Answers for KMS

**251. What is AWS KMS?**  
KMS is a managed service that makes it easy to create and control the encryption keys used to encrypt your data.  

**Key Features:**  
- Centralized key management  
- Integration with AWS services  
- Hardware security modules  
- Audit trail via CloudTrail  

**Example:** Create encryption key for S3 bucket and RDS database encryption.

**252. Explain KMS keys (customer managed vs AWS managed).**  
- **Customer Managed Keys:** You create and control, full administrative access  
- **AWS Managed Keys:** AWS creates and manages for specific service integration  

**Example:** Use customer managed key for S3 SSE-KMS, AWS managed key for RDS encryption.

**253. How do you encrypt data with KMS?**  
1. Create or use existing KMS key  
2. Use encrypt/decrypt APIs  
3. Configure service integration (S3, EBS, etc.)  

**Example:**  
```javascript
const encrypted = await kms.encrypt({
  KeyId: 'alias/my-key',
  Plaintext: Buffer.from('secret data')
}).promise();
```

**254. What is envelope encryption?**  
Envelope encryption uses two keys: data key encrypts data, master key encrypts data key.  

**Benefits:**  
- Faster encryption/decryption  
- Reduced load on master key  
- Secure key distribution  

**Example:** S3 uses envelope encryption with KMS for server-side encryption.

**255. Explain KMS key rotation.**  
Key rotation creates new version of key while preserving access to previously encrypted data.  

**Types:**  
- **Automatic Rotation:** AWS managed keys  
- **Manual Rotation:** Customer managed keys  
- **Imported Key Rotation:** Manual process  

**Example:** Enable automatic key rotation for customer managed key every 365 days.

**256. How do you use KMS with other AWS services?**  
- **S3:** SSE-KMS for bucket encryption  
- **EBS:** Encrypted volumes  
- **RDS:** Database encryption  
- **Lambda:** Environment variable encryption  
- **SNS/SQS:** Message encryption  

**Example:** Configure RDS to use KMS key for transparent data encryption.

**257. What is KMS custom key stores?**  
Custom key stores allow using your own HSMs for key storage and operations.  

**Types:**  
- **CloudHSM Key Store:** AWS CloudHSM cluster  
- **External Key Store:** On-premises HSM  

**Example:** Use CloudHSM key store for compliance requiring dedicated HSM.

**258. Explain KMS grants.**  
Grants provide temporary permissions to use KMS key without changing key policy.  

**Use Cases:**  
- Cross-account access  
- Temporary permissions  
- Service integrations  

**Example:** Grant Lambda function permission to decrypt specific data without key policy changes.

**259. How do you monitor KMS?**  
- **CloudWatch Metrics:** Key usage statistics  
- **CloudTrail:** Audit key operations  
- **KMS Console:** Key usage dashboard  

**Example:** Monitor encrypt/decrypt operations per key to detect unusual activity.

**260. What is AWS CloudHSM?**  
CloudHSM provides dedicated HSM instances in AWS cloud.  

**Features:**  
- FIPS 140-2 Level 3 compliance  
- Single-tenant HSMs  
- Integration with applications  

**Example:** Use CloudHSM for cryptographic operations requiring dedicated hardware.

**261. Explain KMS multi-region keys.**  
Multi-region keys replicate keys across multiple AWS regions.  

**Benefits:**  
- Disaster recovery  
- Low-latency access  
- Compliance requirements  

**Example:** Replicate encryption key to us-east-1 and eu-west-1 for global application.

**262. How do you secure KMS keys?**  
- **Key Policies:** Control access to keys  
- **VPC Endpoints:** Private API access  
- **CloudTrail:** Audit all key operations  
- **MFA:** Require MFA for key operations  

**Example:** Use key policy to restrict key usage to specific IAM roles only.

**263. What is KMS key policies?**  
Key policies are JSON documents that control access to KMS keys.  

**Components:**  
- Principal (who can access)  
- Actions (encrypt, decrypt, etc.)  
- Resources (specific keys)  
- Conditions (IP restrictions, etc.)  

**Example:** Allow specific IAM role to use key only from VPC.

**264. Explain KMS import key material.**  
Import your own key material into KMS for use with AWS services.  

**Process:**  
1. Generate key material  
2. Create KMS key  
3. Import key material  
4. Set expiration (optional)  

**Example:** Import key from on-premises HSM for compliance requirements.

**265. How do you audit KMS usage?**  
- **CloudTrail:** Logs all KMS API calls  
- **Key Usage Reports:** Track key operations  
- **Access Analyzer:** Identify unused permissions  

**Example:** Use CloudTrail to track who accessed specific KMS key and when.

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

### Answers for Scenario-Based Questions

**266. Your Lambda function is timing out during deployment. What could be the causes and how would you troubleshoot?**  
**Possible Causes:**  
- Function package too large  
- VPC configuration issues  
- Insufficient IAM permissions  
- Cold start problems  
- Resource constraints  

**Troubleshooting Steps:**  
1. Check CloudWatch Logs for error messages  
2. Verify function configuration (timeout, memory)  
3. Test function locally with same runtime  
4. Check VPC/security group configuration  
5. Review IAM permissions for Lambda execution role  

**267. A CloudFormation stack update failed. How do you investigate and fix it?**  
**Investigation:**  
1. Check stack events in CloudFormation console  
2. Review error messages in events  
3. Check CloudTrail for API errors  
4. Validate template syntax  

**Common Fixes:**  
- Fix template errors (invalid references, circular dependencies)  
- Resolve resource conflicts  
- Update IAM permissions  
- Use change sets for complex updates  

**268. ECS service deployment is stuck. What steps would you take to resolve it?**  
**Troubleshooting Steps:**  
1. Check ECS service events  
2. Verify task definition is valid  
3. Check cluster capacity  
4. Review CloudWatch logs for container errors  
5. Verify IAM permissions for ECS tasks  

**Resolution:**  
- Update service with force deployment  
- Scale cluster capacity  
- Fix task definition issues  
- Check load balancer target group health  

**269. CodePipeline build is failing. How do you debug the issue?**  
**Debug Steps:**  
1. Check CodePipeline execution details  
2. Review CodeBuild logs in CloudWatch  
3. Verify buildspec.yml syntax  
4. Check source code for compilation errors  
5. Validate IAM permissions  

**Common Solutions:**  
- Fix build commands in buildspec  
- Update runtime versions  
- Resolve dependency issues  
- Check artifact paths  

**270. Your application deployment to EC2 failed due to insufficient permissions. How do you fix it?**  
**Immediate Steps:**  
1. Check IAM role/instance profile permissions  
2. Review CloudTrail for access denied errors  
3. Verify security group rules  
4. Check EC2 instance state and reachability  

**Fixes:**  
- Attach proper IAM policies to EC2 instance  
- Update security groups to allow necessary traffic  
- Use AWS Systems Manager for secure access  
- Implement least privilege principle  

**271. Your S3 bucket is experiencing slow performance. What optimizations would you implement?**  
**Performance Issues:**  
- Sequential prefix access patterns  
- Small object overhead  
- High request rates  

**Optimizations:**  
- Use random prefixes for high-throughput workloads  
- Enable S3 Transfer Acceleration  
- Use multipart upload for large objects  
- Implement caching with CloudFront  
- Use S3 Select for partial object retrieval  

**272. DynamoDB table has hot partition issues. How do you resolve it?**  
**Hot Partition Causes:**  
- Uneven partition key distribution  
- High read/write rates to single partition  
- Inefficient key design  

**Solutions:**  
- Use composite partition keys with sort keys  
- Implement write sharding  
- Add random suffixes to partition keys  
- Use DAX for read-heavy workloads  
- Consider table splitting  

**273. Lambda functions are experiencing cold starts. What can you do to improve performance?**  
**Cold Start Optimizations:**  
- Increase memory allocation (reduces cold start time)  
- Use provisioned concurrency  
- Optimize package size (reduce dependencies)  
- Use layers for shared code  
- Minimize VPC usage if possible  
- Choose appropriate runtime  

**274. RDS database is running slow. How do you diagnose and optimize it?**  
**Diagnosis:**  
1. Check CloudWatch metrics (CPU, memory, IOPS)  
2. Review slow query logs  
3. Analyze Performance Insights  
4. Check connection counts  

**Optimizations:**  
- Add read replicas for read-heavy workloads  
- Optimize slow queries with indexes  
- Scale instance size  
- Use RDS Proxy for connection pooling  
- Implement query caching  

**275. CloudFront is serving stale content. How do you fix it?**  
**Cache Issues:**  
- Long TTL settings  
- Cache key mismatches  
- Origin not sending proper cache headers  

**Solutions:**  
- Create cache invalidation requests  
- Use versioned file names  
- Adjust cache behaviors  
- Set appropriate TTL values  
- Use CloudFront Functions for cache control  

**276. You suspect unauthorized access to your S3 bucket. What immediate steps would you take?**  
**Immediate Response:**  
1. Review S3 access logs and CloudTrail  
2. Check bucket policies and ACLs  
3. Enable MFA delete if not already  
4. Block public access at account level  
5. Rotate any exposed access keys  

**Prevention:**  
- Implement least privilege IAM policies  
- Use VPC endpoints for private access  
- Enable S3 server access logging  
- Set up CloudWatch alarms for suspicious activity  

**277. An IAM user was compromised. How do you contain the breach and prevent future incidents?**  
**Containment:**  
1. Disable/delete compromised access keys  
2. Detach IAM user from all groups  
3. Deactivate the IAM user  
4. Check for any resources created by compromised user  

**Prevention:**  
- Enable MFA for all users  
- Implement password policies  
- Use IAM roles instead of users where possible  
- Regular credential rotation  
- Monitor CloudTrail for suspicious activity  

**278. Your EC2 instance was hacked. What forensic steps would you take?**  
**Forensic Investigation:**  
1. Stop the instance (create AMI first for analysis)  
2. Isolate the instance in separate security group  
3. Enable VPC Flow Logs  
4. Capture memory and disk snapshots  
5. Review CloudTrail and VPC Flow Logs  

**Recovery:**  
- Launch new instance from clean AMI  
- Update security groups and NACLs  
- Rotate all credentials  
- Patch and update the application  

**279. A data breach occurred in your RDS database. How do you respond?**  
**Immediate Response:**  
1. Assess breach scope and impact  
2. Isolate affected systems  
3. Notify relevant stakeholders  
4. Preserve evidence for investigation  

**Recovery Steps:**  
- Restore from clean backup  
- Rotate database credentials  
- Update security groups  
- Implement additional monitoring  
- Review and update incident response plan  

**280. Suspicious activity detected in CloudTrail logs. How do you investigate?**  
**Investigation Process:**  
1. Filter CloudTrail events by time and user  
2. Identify unusual API calls or patterns  
3. Check source IP addresses  
4. Review resource access patterns  
5. Correlate with other logs (VPC Flow Logs, S3 access logs)  

**Actions:**  
- Disable suspicious IAM users/roles  
- Update security policies  
- Implement additional monitoring  
- Report to security team  

**281. Your primary region goes down. How do you failover to a secondary region?**  
**Failover Strategy:**  
1. Use Route 53 health checks to detect failure  
2. Configure failover routing policy  
3. Have secondary environment ready  
4. Use DynamoDB global tables for data  
5. Implement cross-region replication  

**Services to Use:**  
- Route 53 for DNS failover  
- CloudFront with multi-region origins  
- RDS read replicas in secondary region  
- S3 cross-region replication  

**282. RDS instance becomes unresponsive. How do you implement automatic failover?**  
**Multi-AZ Setup:**  
1. Enable Multi-AZ deployment  
2. Configure automatic failover  
3. Set up read replicas if needed  
4. Use RDS Proxy for connection management  

**Monitoring:**  
- Set up CloudWatch alarms  
- Configure automated notifications  
- Implement health checks  

**283. S3 bucket is accidentally deleted. How do you recover the data?**  
**Recovery Options:**  
1. Check S3 versioning (if enabled)  
2. Restore from backups  
3. Use S3 cross-region replication  
4. Check CloudTrail for deletion events  

**Prevention:**  
- Enable versioning on all buckets  
- Implement MFA delete  
- Use S3 bucket policies to prevent deletion  
- Regular backups to another region  

**284. EC2 instance in Auto Scaling group is unhealthy. How does AWS handle it?**  
**Auto Scaling Response:**  
1. Health checks detect unhealthy instance  
2. Auto Scaling terminates unhealthy instance  
3. Launches new instance to maintain desired capacity  
4. Attaches new instance to load balancer  

**Health Check Types:**  
- EC2 status checks  
- ELB health checks  
- Custom health checks  

**285. Your application needs 99.99% uptime. How do you design for high availability?**  
**Architecture Design:**  
- Multi-AZ deployment across 3 AZs  
- Auto Scaling groups  
- Load balancers (ALB/NLB)  
- RDS Multi-AZ with read replicas  
- CloudFront for global distribution  

**Additional Measures:**  
- Circuit breakers for microservices  
- Comprehensive monitoring and alerting  
- Automated failover procedures  
- Regular disaster recovery testing  

**286. Your AWS bill is unexpectedly high. How do you identify and reduce costs?**  
**Cost Analysis:**  
1. Use Cost Explorer and Cost & Usage reports  
2. Identify top cost services  
3. Check for unused resources  
4. Review Reserved Instance utilization  

**Cost Optimization:**  
- Rightsize EC2 instances  
- Use Spot Instances for non-critical workloads  
- Implement auto-scaling  
- Clean up unused EBS volumes and snapshots  
- Use S3 lifecycle policies  

**287. EC2 Reserved Instances are underutilized. What can you do?**  
**Options:**  
- Sell unused Reserved Instances on Reserved Instance Marketplace  
- Modify reservations to different instance types/families  
- Exchange for different term lengths  
- Use Savings Plans for more flexibility  

**Prevention:**  
- Better capacity planning  
- Use auto-scaling to optimize usage  
- Regular review of reservations  

**288. S3 storage costs are increasing rapidly. How do you optimize storage classes?**  
**Storage Optimization:**  
- Implement lifecycle policies to move data to cheaper classes  
- Use S3 Intelligent-Tiering for automatic optimization  
- Compress data before storage  
- Delete unnecessary objects  

**Monitoring:**  
- Use S3 Storage Lens for insights  
- Set up cost allocation tags  
- Monitor storage growth trends  

**289. Lambda functions are running longer than expected. How do you optimize costs?**  
**Optimization Strategies:**  
- Increase memory allocation (can reduce duration)  
- Optimize code and dependencies  
- Use provisioned concurrency appropriately  
- Implement caching to reduce invocations  
- Batch processing for multiple operations  

**Monitoring:**  
- Monitor duration and cost metrics  
- Set up alerts for long-running functions  

**290. Unused resources are accumulating. How do you implement cleanup?**  
**Cleanup Process:**  
- Use AWS Config and Config Rules  
- Implement automated cleanup scripts  
- Set up CloudWatch Events for scheduled cleanup  
- Use AWS Lambda for automated resource management  

**Tools:**  
- AWS Trusted Advisor  
- Cost Explorer  
- Resource Groups and Tag Editor  

**291. You need to monitor application performance across multiple services. How would you set it up?**  
**Monitoring Stack:**  
- CloudWatch for infrastructure metrics  
- X-Ray for distributed tracing  
- CloudWatch Application Insights  
- Custom dashboards  
- CloudWatch Synthetics for end-to-end monitoring  

**Implementation:**  
- Set up comprehensive logging  
- Configure alerts and notifications  
- Implement custom metrics  
- Use CloudWatch Logs Insights for analysis  

**292. Critical alert triggered but you don't know the cause. How do you investigate?**  
**Investigation Steps:**  
1. Check alert details and timeline  
2. Review CloudWatch metrics around alert time  
3. Check application logs in CloudWatch Logs  
4. Review CloudTrail for API activity  
5. Check system health and dependencies  

**Tools:**  
- CloudWatch Logs Insights  
- X-Ray for service dependencies  
- CloudWatch Metrics correlation  

**293. Log data is not appearing in CloudWatch. How do you troubleshoot?**  
**Troubleshooting:**  
1. Check IAM permissions for log delivery  
2. Verify log group and stream configuration  
3. Check CloudWatch agent status  
4. Review VPC endpoints if using private subnets  
5. Check log file permissions and paths  

**Common Issues:**  
- Incorrect log group names  
- Missing permissions  
- Network connectivity problems  
- Log file rotation issues  

**294. You need to create a dashboard for business metrics. How do you implement it?**  
**Dashboard Creation:**  
- Use CloudWatch dashboards for technical metrics  
- CloudWatch Logs Insights for log-based metrics  
- QuickSight for business intelligence  
- Custom Lambda functions for metric calculation  

**Implementation:**  
- Define key business metrics  
- Set up data collection  
- Create visualizations  
- Configure automated updates  

**295. Application errors are not being captured. How do you improve monitoring?**  
**Error Monitoring Setup:**  
- Implement structured logging  
- Use CloudWatch Logs metric filters  
- Set up CloudWatch alarms on error patterns  
- Implement distributed tracing with X-Ray  
- Use CloudWatch Application Insights  

**Best Practices:**  
- Centralized logging strategy  
- Error aggregation and analysis  
- Automated alerting  
- Error tracking and resolution workflows  

**296. EC2 instance can't connect to the internet. How do you troubleshoot?**  
**Network Troubleshooting:**  
1. Check instance security groups  
2. Verify subnet route table  
3. Check network ACLs  
4. Verify internet gateway attachment  
5. Check instance network interface  

**Tools:**  
- VPC Reachability Analyzer  
- VPC Flow Logs analysis  
- EC2 instance console connectivity tests  

**297. VPC peering connection is not working. What could be wrong?**  
**Common Issues:**  
- Overlapping CIDR blocks  
- Incorrect route table entries  
- Security group restrictions  
- DNS resolution problems  

**Resolution:**  
- Verify peering connection status  
- Check route tables in both VPCs  
- Update security groups to allow traffic  
- Test connectivity with different instance types  

**298. DNS resolution is failing. How do you diagnose Route 53 issues?**  
**DNS Troubleshooting:**  
1. Check hosted zone configuration  
2. Verify name server delegation  
3. Test DNS resolution with dig/nslookup  
4. Check Route 53 health checks  
5. Review CloudTrail for DNS changes  

**Tools:**  
- Route 53 query logging  
- DNS testing tools  
- CloudWatch metrics for DNS queries  

**299. Load balancer is not distributing traffic properly. How do you fix it?**  
**Load Balancer Issues:**  
- Unhealthy targets  
- Incorrect health check configuration  
- Security group misconfiguration  
- Cross-zone load balancing disabled  

**Resolution:**  
- Check target group health  
- Verify health check settings  
- Review security groups  
- Enable cross-zone load balancing  

**300. VPN connection is unstable. How do you improve reliability?**  
**VPN Optimization:**  
- Use AWS VPN CloudHub for multiple sites  
- Implement redundant VPN connections  
- Use Direct Connect for critical connections  
- Configure proper MTU settings  
- Monitor VPN metrics and logs  

**Monitoring:**  
- CloudWatch VPN metrics  
- VPN connection logs  
- Network latency monitoring  

**301. DynamoDB table is throttling requests. How do you handle it?**  
**Throttling Solutions:**  
- Implement exponential backoff  
- Use DynamoDB Auto Scaling  
- Distribute requests across partitions  
- Implement caching with DAX  
- Use DynamoDB Accelerator  

**Optimization:**  
- Optimize partition key design  
- Use batch operations  
- Implement request throttling in application  

**302. RDS backup failed. What are the possible causes and solutions?**  
**Common Causes:**  
- Insufficient storage space  
- Long-running transactions  
- Network connectivity issues  
- IAM permission problems  

**Solutions:**  
- Monitor free storage space  
- Schedule backups during low-activity periods  
- Check CloudWatch logs for errors  
- Verify IAM permissions for backup operations  

**303. Database connection pool is exhausted. How do you resolve it?**  
**Connection Pool Issues:**  
- Too many concurrent connections  
- Long-running queries  
- Connection leaks  
- Insufficient pool size  

**Solutions:**  
- Use RDS Proxy for connection pooling  
- Optimize query performance  
- Implement connection pooling in application  
- Monitor connection metrics  

**304. Data inconsistency between RDS read replicas. How do you fix it?**  
**Replica Lag Issues:**  
- High write load on primary  
- Network latency  
- Large transactions  
- Replica capacity constraints  

**Solutions:**  
- Monitor replica lag metrics  
- Scale replica instances  
- Use Multi-AZ for automatic failover  
- Optimize primary database performance  

**305. MongoDB on EC2 is running out of disk space. How do you handle it?**  
**Storage Management:**  
- Monitor disk usage with CloudWatch  
- Implement log rotation  
- Use MongoDB's storage optimization features  
- Scale EBS volume size  

**Solutions:**  
- Add additional EBS volumes  
- Implement data archiving  
- Use MongoDB Atlas for managed service  
- Optimize database design  

**306. Service-to-service communication is failing. How do you debug?**  
**Debugging Steps:**  
1. Check service health endpoints  
2. Review application logs  
3. Verify network connectivity  
4. Check service discovery configuration  
5. Test API endpoints directly  

**Tools:**  
- X-Ray for distributed tracing  
- CloudWatch ServiceLens  
- VPC Flow Logs  
- Application Performance Monitoring  

**307. One microservice is causing cascading failures. How do you implement circuit breaker?**  
**Circuit Breaker Implementation:**  
- Use AWS App Mesh or service mesh  
- Implement in application code  
- Use API Gateway throttling  
- Implement retry logic with exponential backoff  

**Monitoring:**  
- Monitor error rates and latency  
- Set up alerts for circuit breaker activation  
- Implement fallback mechanisms  

**308. API Gateway is rate limiting legitimate requests. How do you handle it?**  
**Rate Limiting Issues:**  
- Overly restrictive throttling  
- Burst rate too low  
- No usage plan configuration  

**Solutions:**  
- Adjust API Gateway throttling settings  
- Implement usage plans with appropriate limits  
- Use caching to reduce backend load  
- Implement request queuing  

**309. Event-driven architecture has duplicate events. How do you deduplicate?**  
**Deduplication Strategies:**  
- Use message deduplication IDs in SQS FIFO  
- Implement idempotent processing  
- Use DynamoDB for event tracking  
- Implement message filtering in SNS  

**Best Practices:**  
- Design for idempotency  
- Use appropriate queue types  
- Implement event sourcing patterns  

**310. Service discovery is not working in ECS. How do you troubleshoot?**  
**Service Discovery Issues:**  
- DNS resolution problems  
- Service registry misconfiguration  
- Network connectivity issues  
- Security group restrictions  

**Troubleshooting:**  
- Check CloudWatch logs  
- Verify service discovery configuration  
- Test DNS resolution  
- Check network ACLs and security groups  

**311. Build pipeline is slow. How do you optimize it?**  
**Pipeline Optimization:**  
- Use parallel build steps  
- Implement build caching  
- Optimize Docker layer caching  
- Use faster compute types  
- Reduce artifact sizes  

**Tools:**  
- CodeBuild local caching  
- Docker layer optimization  
- Parallel test execution  

**312. Deployment to production failed due to environment differences. How do you fix it?**  
**Environment Differences:**  
- Configuration mismatches  
- Dependency version conflicts  
- Infrastructure differences  
- Missing environment variables  

**Solutions:**  
- Use infrastructure as code  
- Implement environment-specific configurations  
- Use feature flags  
- Implement comprehensive testing  

**313. Code quality checks are failing. How do you improve them?**  
**Code Quality Improvements:**  
- Update linting rules  
- Fix identified issues  
- Implement automated code review  
- Use static analysis tools  
- Implement security scanning  

**Tools:**  
- ESLint, Prettier  
- SonarQube  
- AWS CodeGuru  
- Security scanners  

**314. Infrastructure as Code is not idempotent. How do you fix it?**  
**Idempotency Issues:**  
- Hardcoded resource names  
- State management problems  
- Dependency ordering issues  

**Solutions:**  
- Use CloudFormation change sets  
- Implement proper resource naming  
- Use Terraform state management  
- Implement dependency management  

**315. Rollback strategy failed. How do you implement better rollback mechanisms?**  
**Rollback Improvements:**  
- Implement blue-green deployments  
- Use feature flags for gradual rollouts  
- Implement automated rollback triggers  
- Maintain multiple deployment versions  

**Best Practices:**  
- Test rollback procedures  
- Implement canary deployments  
- Use automated testing in production  

**316. You need to implement zero-downtime deployments. How would you do it?**  
**Zero-Downtime Strategies:**  
- Blue-green deployments with ECS  
- Rolling updates with auto-scaling  
- Canaray deployments with traffic shifting  
- Feature flags for gradual rollouts  

**Implementation:**  
- Use CodeDeploy for blue-green  
- Implement health checks  
- Use load balancers for traffic management  
- Implement automated rollback  

**317. Application needs to handle sudden traffic spikes. How do you design auto-scaling?**  
**Auto-Scaling Design:**  
- EC2 Auto Scaling groups  
- Application Auto Scaling for ECS/EKS  
- Lambda concurrency scaling  
- DynamoDB auto-scaling  

**Configuration:**  
- Set appropriate scaling policies  
- Configure cooldown periods  
- Implement predictive scaling  
- Use CloudWatch metrics for triggers  

**318. You need to implement multi-region active-active architecture. What services would you use?**  
**Multi-Region Services:**  
- Route 53 for global DNS  
- CloudFront for global CDN  
- DynamoDB global tables  
- Aurora global database  
- S3 cross-region replication  

**Architecture:**  
- Active-active application deployment  
- Global load balancing  
- Data synchronization  
- Cross-region failover  

**319. Compliance requires data encryption at rest and in transit. How do you implement it?**  
**Encryption Implementation:**  
- S3: SSE-KMS for objects  
- EBS: Encrypted volumes with KMS  
- RDS: Transparent data encryption  
- Network: SSL/TLS for data in transit  
- API Gateway: SSL certificates  

**Key Management:**  
- AWS KMS for key management  
- Certificate Manager for SSL  
- CloudHSM for dedicated hardware  

**320. You need to implement chaos engineering in your AWS environment. How would you start?**  
**Chaos Engineering Setup:**  
1. Define steady state and hypotheses  
2. Start with non-production environments  
3. Use AWS Fault Injection Simulator  
4. Implement automated chaos experiments  

**Tools and Practices:**  
- AWS FIS for fault injection  
- Chaos Monkey alternatives  
- Monitoring and observability  
- Automated recovery testing  

**Best Practices:**  
- Start small with single services  
- Implement proper monitoring  
- Have rollback procedures ready  
- Document lessons learned

This comprehensive list covers the most important AWS services and concepts that developers encounter in modern distributed systems, microservices, and event-driven architectures. The questions progress from basic understanding to advanced implementation and troubleshooting scenarios commonly faced in interviews and real-world projects.
