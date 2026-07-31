# Design a distributed logging system

Collect logs from thousands of services, make them searchable in near real time, and
retain them affordably (think the ELK/EFK + Kafka stack). The interview is about a
**high-throughput, append-only ingestion pipeline** that never backs up into the
services producing the logs.

## 1. Requirements

**Functional:** ingest structured logs from many services; search/filter by service,
level, time, and text; aggregate and alert; retention policies. **Non-functional:**
absorb **very high write throughput** (say ~1 M events/s) with low ingest latency,
durable, cost-effective at scale, and — critically — **decoupled** so a slow storage
layer never blocks or crashes the applications logging.

## 2. The pipeline (and why each stage exists)

```
services → log agents → durable buffer (Kafka) → processors → index + tiered storage → query/alerts
```

- **Agents** (a sidecar/daemon per host) tail logs, **batch + compress**, and ship them
  — so the app just writes locally and never blocks on the network.
- **Durable buffer (Kafka)** is the keystone. It **decouples** producers from
  consumers, **absorbs spikes** (a traffic surge doesn't overwhelm storage), provides
  **replay** (reprocess if a downstream fails), and applies natural **backpressure**.
  Without it, a slow indexer would stall every service. This is the point to make first.
- **Processors** consume from Kafka to parse, extract fields, enrich (add service/user/
  **correlation IDs**), and route.
- **Index + storage** for search and retention (below).

## 3. Storage: tiered by age

Logs are write-once, read-recent, and huge — so tier by access pattern:
- **Hot** (last hours/days) → a searchable **inverted index** (Elasticsearch/OpenSearch),
  time-partitioned so old indices roll off cheaply.
- **Warm** → cheaper nodes, less RAM.
- **Cold/archive** → compressed objects in **object storage** (S3), rarely queried.
Retention deletes/rolls off by tier. Compression ratios on logs are excellent (~10:1).
Partition indices **by time** so queries prune to a range and expiry is a cheap
drop-partition.

## 4. Search & correlation

- Full-text + structured search over the hot index (same inverted-index idea as
  [`search-engine.md`](search-engine.md)).
- **Correlation IDs** propagated through requests let you stitch one request's logs
  across many services — the log system's most valuable feature for debugging, and the
  bridge to distributed tracing.

## 5. Scale realities (1 M events/s)

- **At-least-once** delivery is the practical target; dedupe on a log id if exact
  counts matter.
- **Sampling / aggregation** for ultra-high-volume debug logs — you rarely need every
  DEBUG line; pre-aggregate metrics (counts per service/level/minute) for dashboards.
- Consumers and index shards scale horizontally off Kafka partitions.

## Trade-offs to voice
- **Buffered (Kafka) vs direct-to-store ingestion** — resilience, replay, and
  backpressure vs simplicity (buffering wins at scale).
- **Real-time index vs batch/cold** — instant searchability (costly) vs cheap archival
  (slow) — hence tiering.
- **Completeness vs cost** — full retention/indexing vs sampling + aggregation.
- **Push (agents ship) vs pull (scrape)** — immediate delivery vs central control.
