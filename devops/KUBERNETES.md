# Kubernetes Interview Questions & Answers

A comprehensive guide covering Kubernetes architecture, workloads, networking, security, and production operations.

## Table of Contents
1. [Core Concepts](#core-concepts)
2. [Architecture](#architecture)
3. [Workloads](#workloads)
4. [Networking](#networking)
5. [Storage](#storage)
6. [Configuration & Secrets](#configuration--secrets)
7. [Security](#security)
8. [Scaling & Performance](#scaling--performance)
9. [Observability](#observability)
10. [Troubleshooting](#troubleshooting)
11. [Production Operations](#production-operations)
12. [Advanced Topics](#advanced-topics)

---

## Core Concepts

### Q1: What is Kubernetes and why is it used?
**Answer:**
Kubernetes (K8s) is an open-source container orchestration platform that automates deployment, scaling, and management of containerized applications. Originally developed by Google, now maintained by CNCF.

**Key benefits:**
- **Self-healing:** Restarts failed containers, replaces pods
- **Horizontal scaling:** Scale out based on load
- **Service discovery:** DNS-based service routing
- **Rolling updates:** Zero-downtime deployments
- **Declarative configuration:** Infrastructure as code
- **Multi-cloud portability:** Runs on any cloud or on-prem

```yaml
# Simple deployment example
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
    spec:
      containers:
      - name: app
        image: nginx:latest
        ports:
        - containerPort: 80
```

---

### Q2: What are the main Kubernetes objects and their purposes?
**Answer:**

| Object | Purpose | Use Case |
|--------|---------|----------|
| **Pod** | Smallest deployable unit, 1+ containers | Running containers |
| **Deployment** | Manages ReplicaSets, handles updates | Stateless apps |
| **StatefulSet** | Ordered pods with stable identities | Databases, stateful apps |
| **DaemonSet** | One pod per node | Log collectors, monitoring |
| **Job/CronJob** | Run-to-completion tasks | Batch processing, backups |
| **Service** | Network endpoint for pods | Load balancing, discovery |
| **Ingress** | HTTP(S) routing | External access, TLS |
| **ConfigMap** | Non-sensitive configuration | Environment variables |
| **Secret** | Sensitive data | Passwords, API keys |
| **PersistentVolume** | Storage abstraction | Database storage |

---

### Q3: Explain the difference between a Pod, Deployment, and ReplicaSet
**Answer:**

**Pod:** 
- Smallest unit, one or more containers sharing network/storage
- Ephemeral, no self-healing
- Rarely created directly

**ReplicaSet:**
- Ensures N pod replicas running
- Replaces failed pods
- Rarely created directly (Deployments manage them)

**Deployment:**
- Manages ReplicaSets
- Provides rolling updates and rollbacks
- **This is what you use for stateless apps**

```yaml
# Deployment → creates ReplicaSet → creates Pods
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3                    # Desired state
  selector:
    matchLabels:
      app: my-app
  template:                      # Pod template
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: app
        image: my-app:v1
```

---

## Architecture

### Q4: Explain Kubernetes architecture and components
**Answer:**

```
┌────────────────────────────────────────────────────────────┐
│                    Control Plane (Master)                  │
│  ┌──────────────┐ ┌──────────────┐ ┌───────────────────┐  │
│  │  API Server  │ │    etcd      │ │  Controller       │  │
│  │              │ │   (store)    │ │  Manager          │  │
│  └──────────────┘ └──────────────┘ └───────────────────┘  │
│  ┌──────────────┐ ┌──────────────────────────────────────┐│
│  │  Scheduler   │ │ Cloud Controller Manager (optional)  ││
│  └──────────────┘ └──────────────────────────────────────┘│
└────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────┴─────────────────────────────┐
│                      Worker Nodes                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐       │
│  │   kubelet   │  │ kube-proxy  │  │  Container  │       │
│  │             │  │             │  │  Runtime    │       │
│  └─────────────┘  └─────────────┘  └─────────────┘       │
│  ┌───────────────────────────────────────────────┐       │
│  │                    Pods                        │       │
│  └───────────────────────────────────────────────┘       │
└───────────────────────────────────────────────────────────┘
```

**Control Plane:**
- **API Server:** Frontend, all communication goes through it
- **etcd:** Distributed key-value store for cluster state
- **Scheduler:** Assigns pods to nodes
- **Controller Manager:** Runs controllers (Deployment, Node, etc.)

**Worker Nodes:**
- **kubelet:** Agent that runs/manages pods on node
- **kube-proxy:** Network proxy, implements Services
- **Container Runtime:** Docker, containerd, CRI-O

---

### Q5: What is etcd and why is it critical?
**Answer:**
etcd is a distributed, strongly-consistent key-value store that holds all cluster state and configuration.

**Critical aspects:**
- All K8s objects stored here (deployments, secrets, etc.)
- Must be backed up for disaster recovery
- Should run in HA mode (odd number: 3, 5, 7 nodes)
- Uses Raft consensus for consistency

```bash
# Backup etcd
ETCDCTL_API=3 etcdctl snapshot save backup.db \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key

# Restore etcd
ETCDCTL_API=3 etcdctl snapshot restore backup.db \
  --data-dir /var/lib/etcd-restore

# Check cluster health
ETCDCTL_API=3 etcdctl endpoint health
```

---

### Q6: How does the Kubernetes scheduler work?
**Answer:**
The scheduler watches for unscheduled pods and assigns them to suitable nodes.

**Scheduling process:**
1. **Filtering:** Exclude nodes that can't run the pod (resources, taints, affinity)
2. **Scoring:** Rank remaining nodes by preference
3. **Binding:** Assign pod to highest-scored node

**Factors considered:**
- Resource requests/limits
- Node selectors and affinity
- Taints and tolerations
- Pod affinity/anti-affinity
- Pod topology spread constraints

```yaml
# Node affinity example
apiVersion: v1
kind: Pod
metadata:
  name: gpu-pod
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: gpu
            operator: In
            values:
            - "true"
  containers:
  - name: app
    image: gpu-app:latest
```

---

## Workloads

### Q7: When do you use StatefulSet vs Deployment?
**Answer:**

| Feature | Deployment | StatefulSet |
|---------|------------|-------------|
| Pod identity | Random names | Stable, ordered (pod-0, pod-1) |
| Scaling | Parallel | Ordered (one at a time) |
| Storage | Shared or none | Unique PVC per pod |
| Network | Random DNS | Stable DNS (pod-0.svc.ns) |
| Use case | Stateless apps | Databases, message queues |

```yaml
# StatefulSet for database
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgres
spec:
  serviceName: postgres
  replicas: 3
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
      - name: postgres
        image: postgres:16
        volumeMounts:
        - name: data
          mountPath: /var/lib/postgresql/data
  volumeClaimTemplates:        # Each pod gets its own PVC
  - metadata:
      name: data
    spec:
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 10Gi
```

---

### Q8: How do you implement rolling updates and rollbacks?
**Answer:**

```yaml
# Deployment with update strategy
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
spec:
  replicas: 4
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1         # Max pods above desired during update
      maxUnavailable: 0   # Zero downtime
  template:
    spec:
      containers:
      - name: app
        image: app:v1
        readinessProbe:   # Critical for zero-downtime
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
```

```bash
# Update image
kubectl set image deployment/web-app app=app:v2

# Check rollout status
kubectl rollout status deployment/web-app

# View history
kubectl rollout history deployment/web-app

# Rollback to previous
kubectl rollout undo deployment/web-app

# Rollback to specific revision
kubectl rollout undo deployment/web-app --to-revision=2

# Pause/resume rollout
kubectl rollout pause deployment/web-app
kubectl rollout resume deployment/web-app
```

---

### Q9: Explain DaemonSet and its use cases
**Answer:**
DaemonSet ensures one pod runs on every (or selected) node. Automatically adds pods when nodes join cluster.

**Use cases:**
- Log collectors (Fluentd, Filebeat)
- Monitoring agents (Prometheus node exporter)
- Network plugins (Calico, Cilium)
- Storage daemons (Ceph, GlusterFS)

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: log-collector
spec:
  selector:
    matchLabels:
      app: log-collector
  template:
    metadata:
      labels:
        app: log-collector
    spec:
      tolerations:
      - key: node-role.kubernetes.io/control-plane
        effect: NoSchedule    # Run on master nodes too
      containers:
      - name: fluentd
        image: fluentd:latest
        volumeMounts:
        - name: varlog
          mountPath: /var/log
          readOnly: true
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
```

---

### Q10: How do Jobs and CronJobs work?
**Answer:**

**Job:** Run-to-completion task, creates pods that terminate.
**CronJob:** Scheduled Jobs using cron syntax.

```yaml
# One-time Job
apiVersion: batch/v1
kind: Job
metadata:
  name: data-migration
spec:
  completions: 1          # Number of successful completions needed
  parallelism: 1          # Pods running in parallel
  backoffLimit: 3         # Retries before marking failed
  activeDeadlineSeconds: 3600  # Timeout
  template:
    spec:
      restartPolicy: Never   # Or OnFailure
      containers:
      - name: migrate
        image: migration:v1
        command: ["python", "migrate.py"]
---
# CronJob
apiVersion: batch/v1
kind: CronJob
metadata:
  name: backup
spec:
  schedule: "0 2 * * *"      # Daily at 2 AM
  concurrencyPolicy: Forbid  # Don't overlap runs
  successfulJobsHistoryLimit: 3
  failedJobsHistoryLimit: 1
  jobTemplate:
    spec:
      template:
        spec:
          restartPolicy: OnFailure
          containers:
          - name: backup
            image: backup:latest
```

---

## Networking

### Q11: Explain Kubernetes networking model
**Answer:**
Kubernetes networking requirements:
1. All pods can communicate without NAT
2. All nodes can communicate with all pods without NAT
3. Pod's IP is same inside and outside the pod

```
┌─────────────────────────────────────────────────────────────┐
│                     Cluster Network                          │
│                                                              │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│  │   Node 1    │    │   Node 2    │    │   Node 3    │     │
│  │ 10.0.1.0/24 │    │ 10.0.2.0/24 │    │ 10.0.3.0/24 │     │
│  │  ┌──────┐   │    │  ┌──────┐   │    │  ┌──────┐   │     │
│  │  │Pod A │   │    │  │Pod C │   │    │  │Pod E │   │     │
│  │  │.10   │───┼────┼──│.20   │───┼────┼──│.30   │   │     │
│  │  └──────┘   │    │  └──────┘   │    │  └──────┘   │     │
│  └─────────────┘    └─────────────┘    └─────────────┘     │
│                                                              │
│  Service: ClusterIP 10.96.0.1 → Pod IPs                     │
└─────────────────────────────────────────────────────────────┘
```

**CNI plugins:** Calico, Cilium, Flannel, Weave

---

### Q12: What are the different Service types?
**Answer:**

| Type | Access | Use Case |
|------|--------|----------|
| **ClusterIP** | Internal only | Default, internal communication |
| **NodePort** | Node IP:Port | Development, debugging |
| **LoadBalancer** | External LB | Cloud production exposure |
| **ExternalName** | DNS CNAME | External services |

```yaml
# ClusterIP (default)
apiVersion: v1
kind: Service
metadata:
  name: backend
spec:
  type: ClusterIP
  selector:
    app: backend
  ports:
  - port: 80
    targetPort: 8080
---
# NodePort
apiVersion: v1
kind: Service
metadata:
  name: web
spec:
  type: NodePort
  selector:
    app: web
  ports:
  - port: 80
    targetPort: 8080
    nodePort: 30080    # 30000-32767
---
# LoadBalancer
apiVersion: v1
kind: Service
metadata:
  name: api
spec:
  type: LoadBalancer
  selector:
    app: api
  ports:
  - port: 443
    targetPort: 8443
```

---

### Q13: How does Ingress work and when to use it?
**Answer:**
Ingress manages external HTTP(S) access to services with routing rules, TLS termination, and virtual hosts.

```yaml
# Ingress with multiple hosts and paths
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: main-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - api.example.com
    - web.example.com
    secretName: tls-secret
  rules:
  - host: api.example.com
    http:
      paths:
      - path: /v1
        pathType: Prefix
        backend:
          service:
            name: api-v1
            port:
              number: 80
      - path: /v2
        pathType: Prefix
        backend:
          service:
            name: api-v2
            port:
              number: 80
  - host: web.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web-frontend
            port:
              number: 80
```

**Ingress Controllers:** NGINX, Traefik, HAProxy, AWS ALB, GCE

---

### Q14: Explain Network Policies
**Answer:**
Network Policies control pod-to-pod traffic (like firewall rules). Requires CNI support (Calico, Cilium).

```yaml
# Default deny all ingress
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-ingress
spec:
  podSelector: {}    # All pods in namespace
  policyTypes:
  - Ingress
---
# Allow specific traffic
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: api-policy
spec:
  podSelector:
    matchLabels:
      app: api
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    - namespaceSelector:
        matchLabels:
          name: monitoring
    ports:
    - protocol: TCP
      port: 8080
  egress:
  - to:
    - podSelector:
        matchLabels:
          app: database
    ports:
    - protocol: TCP
      port: 5432
```

---

## Storage

### Q15: Explain PersistentVolume and PersistentVolumeClaim
**Answer:**

**PersistentVolume (PV):** Cluster-level storage resource provisioned by admin or dynamically.
**PersistentVolumeClaim (PVC):** User's request for storage.

```yaml
# StorageClass for dynamic provisioning
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-ssd
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp3
  iops: "3000"
reclaimPolicy: Retain
volumeBindingMode: WaitForFirstConsumer
---
# PVC requests storage
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: database-storage
spec:
  storageClassName: fast-ssd
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 100Gi
---
# Pod uses PVC
apiVersion: v1
kind: Pod
metadata:
  name: database
spec:
  containers:
  - name: postgres
    image: postgres:16
    volumeMounts:
    - name: data
      mountPath: /var/lib/postgresql/data
  volumes:
  - name: data
    persistentVolumeClaim:
      claimName: database-storage
```

**Access Modes:**
- **ReadWriteOnce (RWO):** Single node read-write
- **ReadOnlyMany (ROX):** Multiple nodes read-only
- **ReadWriteMany (RWX):** Multiple nodes read-write

---

## Configuration & Secrets

### Q16: How do you manage configuration in Kubernetes?
**Answer:**

```yaml
# ConfigMap for non-sensitive config
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  DATABASE_HOST: postgres.default.svc.cluster.local
  LOG_LEVEL: info
  config.yaml: |
    server:
      port: 8080
      timeout: 30s
---
# Using ConfigMap
apiVersion: v1
kind: Pod
metadata:
  name: app
spec:
  containers:
  - name: app
    image: app:latest
    # As environment variables
    envFrom:
    - configMapRef:
        name: app-config
    # Or specific keys
    env:
    - name: DB_HOST
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: DATABASE_HOST
    # As mounted file
    volumeMounts:
    - name: config
      mountPath: /etc/config
  volumes:
  - name: config
    configMap:
      name: app-config
      items:
      - key: config.yaml
        path: config.yaml
```

---

### Q17: How do you manage Secrets securely?
**Answer:**

```yaml
# Create secret
apiVersion: v1
kind: Secret
metadata:
  name: db-credentials
type: Opaque
stringData:            # Plain text (encoded on apply)
  username: admin
  password: supersecret
---
# Using secrets
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: app
    image: app:latest
    env:
    - name: DB_PASSWORD
      valueFrom:
        secretKeyRef:
          name: db-credentials
          key: password
    volumeMounts:
    - name: secrets
      mountPath: /etc/secrets
      readOnly: true
  volumes:
  - name: secrets
    secret:
      secretName: db-credentials
```

**Security best practices:**
1. **Enable encryption at rest** in etcd
2. **Use external secret stores:** HashiCorp Vault, AWS Secrets Manager
3. **RBAC:** Limit who can read secrets
4. **Avoid secrets in image or git**

```bash
# Enable encryption at rest
# /etc/kubernetes/encryption-config.yaml
apiVersion: apiserver.config.k8s.io/v1
kind: EncryptionConfiguration
resources:
  - resources:
    - secrets
    providers:
    - aescbc:
        keys:
        - name: key1
          secret: <base64-key>
    - identity: {}
```

---

## Security

### Q18: Explain RBAC in Kubernetes
**Answer:**
RBAC (Role-Based Access Control) manages who can do what in the cluster.

**Components:**
- **Role/ClusterRole:** Defines permissions (verbs on resources)
- **RoleBinding/ClusterRoleBinding:** Assigns role to users/groups/service accounts

```yaml
# Role (namespaced)
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: default
rules:
- apiGroups: [""]
  resources: ["pods", "pods/log"]
  verbs: ["get", "list", "watch"]
---
# ClusterRole (cluster-wide)
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: secret-reader
rules:
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["get", "list"]
---
# RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods
  namespace: default
subjects:
- kind: ServiceAccount
  name: my-app
  namespace: default
- kind: User
  name: jane@example.com
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

```bash
# Check permissions
kubectl auth can-i get pods --as=jane@example.com
kubectl auth can-i create deployments --as=system:serviceaccount:default:my-app
```

---

### Q19: What are Pod Security Standards?
**Answer:**
Pod Security Standards (PSS) replace PodSecurityPolicies (deprecated). They define three levels:

| Level | Description |
|-------|-------------|
| **Privileged** | Unrestricted (system pods) |
| **Baseline** | Prevents known privilege escalations |
| **Restricted** | Hardened, best practices |

```yaml
# Enforce at namespace level
apiVersion: v1
kind: Namespace
metadata:
  name: production
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/enforce-version: latest
    pod-security.kubernetes.io/warn: restricted
    pod-security.kubernetes.io/audit: restricted
---
# Restricted pod example
apiVersion: v1
kind: Pod
metadata:
  name: secure-app
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: app
    image: app:latest
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop:
        - ALL
      runAsUser: 1000
```

---

### Q20: How do you secure container images?
**Answer:**

```yaml
# Image pull policy
spec:
  containers:
  - name: app
    image: myregistry.com/app:v1.2.3@sha256:abc123...  # Use digest
    imagePullPolicy: Always
  imagePullSecrets:
  - name: registry-credentials
---
# Admission controller for image policies
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
metadata:
  name: image-policy
webhooks:
- name: image-policy.example.com
  rules:
  - operations: ["CREATE", "UPDATE"]
    resources: ["pods"]
```

**Best practices:**
1. Use specific tags or digests, never `:latest`
2. Scan images (Trivy, Snyk, Clair)
3. Use private registries with authentication
4. Sign images (Sigstore/cosign)
5. Enforce policies with admission controllers (OPA/Gatekeeper, Kyverno)

---

## Scaling & Performance

### Q21: How does Horizontal Pod Autoscaler work?
**Answer:**
HPA automatically scales pods based on metrics (CPU, memory, custom).

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: web-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web-app
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
  - type: Pods
    pods:
      metric:
        name: requests_per_second
      target:
        type: AverageValue
        averageValue: "1000"
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300  # Wait before scaling down
    scaleUp:
      stabilizationWindowSeconds: 0
```

**Requirements:**
- Pods must have resource requests defined
- Metrics Server must be installed
- For custom metrics: Prometheus Adapter

---

### Q22: Explain resource requests and limits
**Answer:**

**Requests:** Minimum guaranteed resources (used for scheduling)
**Limits:** Maximum allowed resources (enforced by kubelet)

```yaml
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: app
    image: app:latest
    resources:
      requests:
        memory: "256Mi"
        cpu: "250m"       # 0.25 CPU cores
      limits:
        memory: "512Mi"
        cpu: "1000m"      # 1 CPU core
```

**QoS Classes:**
- **Guaranteed:** requests = limits (highest priority)
- **Burstable:** requests < limits
- **BestEffort:** no requests/limits (first to be evicted)

```yaml
# LimitRange for defaults
apiVersion: v1
kind: LimitRange
metadata:
  name: default-limits
spec:
  limits:
  - default:
      cpu: "500m"
      memory: "512Mi"
    defaultRequest:
      cpu: "100m"
      memory: "128Mi"
    type: Container
---
# ResourceQuota for namespace
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-quota
spec:
  hard:
    requests.cpu: "10"
    requests.memory: "20Gi"
    limits.cpu: "20"
    limits.memory: "40Gi"
    pods: "50"
```

---

### Q23: How do you implement cluster autoscaling?
**Answer:**
Cluster Autoscaler (CA) adjusts cluster size by adding/removing nodes.

**Triggers:**
- Scale up: Pods pending due to insufficient resources
- Scale down: Nodes underutilized for extended period

```yaml
# EKS cluster autoscaler configuration
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cluster-autoscaler
  namespace: kube-system
spec:
  template:
    spec:
      containers:
      - name: cluster-autoscaler
        image: registry.k8s.io/autoscaling/cluster-autoscaler:v1.28.0
        command:
        - ./cluster-autoscaler
        - --cloud-provider=aws
        - --nodes=1:10:my-node-group  # min:max:name
        - --scale-down-delay-after-add=5m
        - --scale-down-unneeded-time=5m
        - --skip-nodes-with-local-storage=false
```

**Best practices:**
- Set appropriate min/max for node groups
- Use Pod Disruption Budgets
- Don't mix CA with manual scaling

---

## Observability

### Q24: How do you implement logging in Kubernetes?
**Answer:**

**Logging patterns:**
1. **Node-level agent (DaemonSet):** Fluentd/Fluent Bit collects from all pods
2. **Sidecar container:** Per-pod log shipping
3. **Application direct:** App sends to logging service

```yaml
# Fluent Bit DaemonSet
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluent-bit
  namespace: logging
spec:
  selector:
    matchLabels:
      app: fluent-bit
  template:
    spec:
      containers:
      - name: fluent-bit
        image: fluent/fluent-bit:latest
        volumeMounts:
        - name: varlog
          mountPath: /var/log
        - name: containers
          mountPath: /var/lib/docker/containers
          readOnly: true
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
      - name: containers
        hostPath:
          path: /var/lib/docker/containers
```

```bash
# View pod logs
kubectl logs pod-name
kubectl logs pod-name -c container-name
kubectl logs -f pod-name              # Follow
kubectl logs --previous pod-name      # Previous container instance
kubectl logs -l app=web --all-containers
```

---

### Q25: How do you monitor Kubernetes?
**Answer:**

**Components:**
- **Metrics Server:** In-cluster resource metrics (CPU, memory)
- **Prometheus:** Metrics collection and storage
- **Grafana:** Visualization
- **Alertmanager:** Alerting

```yaml
# ServiceMonitor for Prometheus
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: app-monitor
spec:
  selector:
    matchLabels:
      app: my-app
  endpoints:
  - port: metrics
    interval: 15s
    path: /metrics
---
# PrometheusRule for alerting
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: app-alerts
spec:
  groups:
  - name: app
    rules:
    - alert: HighErrorRate
      expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.1
      for: 5m
      labels:
        severity: critical
      annotations:
        summary: High error rate detected
```

**Key metrics to monitor:**
- Pod CPU/memory usage
- Container restarts
- Node resource utilization
- API server latency
- etcd health
- Network errors

---

## Troubleshooting

### Q26: How do you troubleshoot pod startup issues?
**Answer:**

```bash
# Check pod status
kubectl get pods
kubectl describe pod <pod-name>

# Common issues and fixes:

# 1. ImagePullBackOff
#    → Check image name, registry credentials
kubectl get events --field-selector involvedObject.name=<pod>

# 2. CrashLoopBackOff
#    → Check logs, command, liveness probe
kubectl logs <pod> --previous

# 3. Pending
#    → Check resources, node selectors, taints
kubectl describe pod <pod> | grep -A 10 Events

# 4. ContainerCreating
#    → Check volume mounts, secrets
kubectl get events -n <namespace>

# Debug with ephemeral container
kubectl debug -it <pod> --image=busybox --target=<container>

# Run debug pod on specific node
kubectl debug node/<node-name> -it --image=ubuntu
```

---

### Q27: How do you troubleshoot networking issues?
**Answer:**

```bash
# 1. Check Service and Endpoints
kubectl get svc <service>
kubectl get endpoints <service>
kubectl describe svc <service>

# 2. Test DNS resolution
kubectl run tmp --rm -i --restart=Never --image=busybox -- nslookup <service>

# 3. Test connectivity from another pod
kubectl run tmp --rm -i --restart=Never --image=curlimages/curl -- \
  curl -v http://<service>.<namespace>.svc.cluster.local

# 4. Check NetworkPolicies
kubectl get networkpolicies
kubectl describe networkpolicy <name>

# 5. Check pod network
kubectl exec -it <pod> -- ip addr
kubectl exec -it <pod> -- netstat -tlnp

# 6. Check kube-proxy logs
kubectl logs -n kube-system -l k8s-app=kube-proxy

# 7. Check CNI pods
kubectl get pods -n kube-system -l k8s-app=calico-node
```

---

## Production Operations

### Q28: What is your Kubernetes upgrade strategy?
**Answer:**

**Pre-upgrade:**
1. Review release notes and deprecations
2. Backup etcd and persistent data
3. Test in staging environment
4. Verify PodDisruptionBudgets exist

**Upgrade process:**
```bash
# 1. Upgrade control plane (one node at a time)
kubeadm upgrade plan
kubeadm upgrade apply v1.29.0

# 2. Drain and upgrade worker nodes
kubectl drain node1 --ignore-daemonsets --delete-emptydir-data
# Upgrade kubelet and kubectl on node
systemctl restart kubelet
kubectl uncordon node1

# 3. Verify
kubectl get nodes
kubectl get pods -A
```

**Post-upgrade:**
- Verify all workloads running
- Check deprecated API usage
- Update kubectl clients
- Document changes

---

### Q29: How do you handle disaster recovery?
**Answer:**

**Backup strategy:**
1. **etcd snapshots:** Cluster state
2. **PV backups:** Application data (Velero)
3. **GitOps:** Infrastructure as code

```bash
# Velero backup
velero backup create daily-backup \
  --include-namespaces production \
  --exclude-resources secrets \
  --ttl 720h

# Schedule backups
velero schedule create daily \
  --schedule="0 2 * * *" \
  --include-namespaces production

# Restore
velero restore create --from-backup daily-backup
```

**Recovery procedures:**
- Document runbooks
- Test restores quarterly
- Practice chaos engineering
- Multi-region considerations

---

### Q30: How do you implement GitOps with Kubernetes?
**Answer:**
GitOps uses Git as single source of truth. Changes are applied automatically via pull-based sync.

**Tools:** ArgoCD, Flux

```yaml
# ArgoCD Application
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/org/repo
    targetRevision: main
    path: k8s/production
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
    - CreateNamespace=true
---
# Kustomize support
source:
  path: k8s/overlays/production
  kustomize:
    images:
    - name: app
      newTag: v1.2.3
```

**Benefits:**
- Audit trail in git history
- Easy rollback via git revert
- Review process via PRs
- Consistent environments

---

## Advanced Topics

### Q31: How do you implement service mesh?
**Answer:**
Service mesh (Istio, Linkerd) adds observability, security, and traffic management.

```yaml
# Istio VirtualService for traffic splitting
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: my-app
spec:
  hosts:
  - my-app
  http:
  - match:
    - headers:
        x-canary:
          exact: "true"
    route:
    - destination:
        host: my-app
        subset: v2
  - route:
    - destination:
        host: my-app
        subset: v1
      weight: 90
    - destination:
        host: my-app
        subset: v2
      weight: 10
---
# Istio DestinationRule
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: my-app
spec:
  host: my-app
  subsets:
  - name: v1
    labels:
      version: v1
  - name: v2
    labels:
      version: v2
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 100
    outlierDetection:
      consecutive5xxErrors: 5
      interval: 30s
      baseEjectionTime: 30s
```

---

### Q32: How do you manage multi-cluster deployments?
**Answer:**

**Options:**
1. **Federation:** Centralized management (kubefed)
2. **GitOps:** ArgoCD ApplicationSet
3. **Service Mesh:** Istio multi-cluster

```yaml
# ArgoCD ApplicationSet for multi-cluster
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: my-app
spec:
  generators:
  - clusters:
      selector:
        matchLabels:
          env: production
  template:
    metadata:
      name: '{{name}}-app'
    spec:
      project: default
      source:
        repoURL: https://github.com/org/repo
        path: k8s/production
      destination:
        server: '{{server}}'
        namespace: production
```

**Considerations:**
- Cross-cluster networking
- Data locality
- Failover strategy
- Centralized monitoring

---

### Q33: How do operators work in Kubernetes?
**Answer:**
Operators extend Kubernetes with custom controllers that manage complex applications.

```yaml
# Custom Resource Definition
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: databases.example.com
spec:
  group: example.com
  names:
    kind: Database
    plural: databases
  scope: Namespaced
  versions:
  - name: v1
    served: true
    storage: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          spec:
            type: object
            properties:
              engine:
                type: string
              version:
                type: string
              replicas:
                type: integer
---
# Custom Resource
apiVersion: example.com/v1
kind: Database
metadata:
  name: my-db
spec:
  engine: postgresql
  version: "16"
  replicas: 3
```

**Popular Operators:**
- PostgreSQL: Crunchy, Zalando
- Redis: Spotahome
- Kafka: Strimzi
- Prometheus: kube-prometheus-stack

---

## Quick Reference

### Essential kubectl Commands
```bash
# Cluster info
kubectl cluster-info
kubectl get nodes -o wide
kubectl top nodes

# Workloads
kubectl get all -n <namespace>
kubectl describe deployment <name>
kubectl rollout history deployment <name>

# Debugging
kubectl logs -f <pod> --timestamps
kubectl exec -it <pod> -- /bin/sh
kubectl port-forward svc/<service> 8080:80

# Configuration
kubectl get configmaps,secrets
kubectl create secret generic <name> --from-literal=key=value

# Resources
kubectl api-resources
kubectl explain deployment.spec.strategy
```

### Common Issues Cheat Sheet

| Symptom | Check | Fix |
|---------|-------|-----|
| Pod Pending | `kubectl describe pod` | Check resources, node selectors |
| CrashLoopBackOff | `kubectl logs --previous` | Fix app crash, check probes |
| ImagePullBackOff | `kubectl describe pod` | Check image name, registry auth |
| Service not reachable | `kubectl get endpoints` | Check selector labels match |
| Node NotReady | `kubectl describe node` | Check kubelet, disk space |

---

*Last updated: February 2026*
