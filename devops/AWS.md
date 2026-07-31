# AWS

Cloud interviews test breadth (know the service categories and pick the right one),
core primitives (compute, storage, networking, IAM), and the design instincts from
the Well-Architected Framework. You don't need every service — you need the map.

## The service map (know one per category)

| Need | Service(s) | One-liner |
|---|---|---|
| VMs | **EC2** | resizable virtual servers |
| Serverless functions | **Lambda** | run code on events, no servers, pay per ms |
| Containers | **ECS / EKS / Fargate** | run containers (EKS = managed K8s; Fargate = serverless containers) |
| Object storage | **S3** | durable, cheap, infinite blob storage |
| Block storage | **EBS** | disks attached to EC2 |
| Relational DB | **RDS / Aurora** | managed SQL |
| NoSQL | **DynamoDB** | managed key-value/document, single-digit-ms |
| Cache | **ElastiCache** | managed Redis/Memcached |
| Networking | **VPC** | your private network; subnets, route tables, gateways |
| CDN | **CloudFront** | edge caching of content/APIs |
| Identity | **IAM** | who can do what to which resource |
| Queue / events | **SQS / SNS / EventBridge** | decoupling and async messaging |
| Monitoring | **CloudWatch** | metrics, logs, alarms |

## Compute: how to choose

- **EC2** — max control, you manage the OS/scaling. Legacy/lift-and-shift or special
  needs.
- **Containers (ECS/EKS)** — portable, orchestrated; EKS if you want Kubernetes,
  Fargate if you don't want to manage nodes.
- **Lambda** — event-driven, spiky, or glue workloads; scales to zero, pay per
  invocation. Watch cold starts, the 15-min limit, and statelessness.

The senior answer maps workload shape (steady vs spiky, stateful vs stateless,
ops appetite) to the option — not "Lambda is always best."

## S3 (the most-asked service)

- **11 nines of durability**, effectively unlimited, cheap. Backups, static assets,
  data lakes, logs.
- **Storage classes** trade cost for retrieval speed (Standard → Infrequent Access →
  Glacier). Use **lifecycle policies** to tier automatically.
- Secure by default: block public access, use bucket policies/IAM, enable encryption
  (SSE), and versioning for recovery.

## IAM (security fundamentals)

- **Principle of least privilege** — grant the minimum permissions needed.
- **Roles over long-lived keys** — EC2/Lambda assume roles for temporary credentials;
  never bake access keys into code or images (this repo's own history is a cautionary
  tale — see `SECURITY.md`).
- Policies are JSON: principal, action, resource, condition.

## Networking (VPC) in brief

- A **VPC** is your isolated network; split into **public subnets** (internet-facing,
  via an Internet Gateway) and **private subnets** (backend/DB, egress via NAT).
- **Security groups** (stateful, instance-level) vs **NACLs** (stateless,
  subnet-level) — know the difference.
- Put databases in private subnets; expose only load balancers publicly.

## High availability & scaling

- Deploy across **multiple Availability Zones**; use an **Auto Scaling Group** behind
  an **Elastic Load Balancer**.
- Multi-AZ RDS for DB failover; read replicas for read scaling.
- Design stateless app tiers so any instance can serve any request.

## Well-Architected Framework (name-drop the pillars)

Operational Excellence, Security, Reliability, Performance Efficiency, Cost
Optimization, Sustainability. A great way to structure any "design on AWS" answer:
walk the pillars.

## Cost instincts

Right-size instances, use auto-scaling and spot for interruptible work, tier S3 with
lifecycle rules, and set **billing alarms**. "How would you cut this bill?" is a
common scenario — lead with measuring usage, then right-sizing and tiering.

## Common questions

- **EC2 vs Lambda vs containers?** Control/steady vs event-driven/spiky vs
  portable/orchestrated.
- **Make an app highly available?** Multi-AZ, ASG + load balancer, stateless tier,
  managed multi-AZ DB.
- **Secure secrets on AWS?** IAM roles + Secrets Manager/Parameter Store; never
  hard-code credentials.
- **S3 vs EBS vs EFS?** Object vs block (single EC2) vs shared file system.
- **Reduce latency globally?** CloudFront + edge + regional replicas.

*Deep legacy Q&A: [`aws-legacy-qa.md`](aws-legacy-qa.md).*
