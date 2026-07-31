# Design a distributed file system

Store petabytes across commodity machines that individually fail, while presenting one
reliable file system (the GFS/HDFS model). The interview centers on **splitting files
into replicated blocks** and **separating the metadata plane from the data plane** so a
central coordinator never becomes the bottleneck.

## 1. Requirements

**Functional:** store/retrieve large files, directory hierarchy, permissions,
replication. **Non-functional:** scale to **petabytes / billions of files**, **durable**
despite constant hardware failure, high read throughput, and available. Assume large
files and read/append-heavy workloads (the GFS design point) rather than tiny-file
random writes.

## 2. The core architecture: blocks + two planes

- **Chunk the file.** Split each file into large fixed-size **blocks** (e.g. 64–128 MB)
  and scatter blocks across many **data nodes**. Large files become sets of blocks that
  read in parallel from many machines.
- **Replicate each block** (typically **factor 3**) across different nodes (and racks) —
  the primary durability mechanism on unreliable hardware.
- **Separate control from data:**
  - **Metadata plane — the name node:** holds the directory tree, permissions, and the
    map of *file → blocks → which data nodes hold them*.
  - **Data plane — data nodes:** store and serve the actual block bytes.

**The key move:** a client asks the **name node** only for *where* a file's blocks live,
then reads/writes the bytes **directly from the data nodes**. The name node stays out of
the data path, so it doesn't bottleneck on bandwidth — it only handles lightweight
metadata. Say this explicitly.

## 3. Durability & failure handling

- **Heartbeats:** data nodes heartbeat to the name node. Missed heartbeats → node
  presumed dead → the name node **re-replicates** its blocks elsewhere to restore the
  replication factor. Self-healing.
- **Checksums** per block detect corruption (bit rot); a bad replica is repaired from a
  good one.
- **Rack-aware placement:** spread replicas across racks so a rack/switch failure
  doesn't take out all copies.

## 4. Why large blocks

64–128 MB blocks (vs KB filesystem blocks) **amortize metadata and seek overhead** and
suit large sequential reads — fewer blocks per file means the name node's metadata map
stays small enough to keep in memory. The cost: **small files waste a block's worth of
metadata** and pack poorly — this design is for big files, not billions of tiny ones.

## 5. The name node as a single point of failure

Centralized metadata is the classic weak point. Mitigations:
- **HA standby** name node with a shared/replicated edit log; automatic failover.
- **Federation/sharding** of the namespace across multiple name nodes when metadata
  outgrows one machine.
Naming the SPOF and how you'd remove it is expected at senior level.

## 6. Consistency model

GFS/HDFS relax POSIX semantics for scale — they favor **append** and are optimized for
throughput over low-latency random writes. Reads see committed data; concurrent-write
semantics are deliberately simple. The trade is **scalability/throughput over strict
consistency and arbitrary random writes**.

## Trade-offs to voice
- **Block size** — large blocks → throughput + small metadata, but wasteful for tiny
  files.
- **Replication factor** — higher durability/read parallelism vs storage cost (3× is
  the usual sweet spot).
- **Central metadata** — simple, fast lookups vs a SPOF/scaling limit (fix with HA +
  federation).
- **Consistency vs throughput** — relaxed append-oriented semantics buy petabyte scale.
- **Replication vs erasure coding** — 3× replicas (simple, fast recovery) vs erasure
  coding (far less storage overhead, costlier reconstruction) for colder data.
