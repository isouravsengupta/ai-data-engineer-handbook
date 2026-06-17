# AI Engineering To Do

This file contains an in-repo snapshot of the roadmap in a tabular format.

- Sheet tab mirrored: `Data Engineering Roadmap and Tasks`
- Columns: `Day | 1: Python & Coding (Logic) | 2: Core Subject (DE/SQL) | 3: Implementation & Hard Problems | Status | Casual`

## Roadmap Entries (Tabular Snapshot)

| Day | Python & Coding (Logic) | Core Subject (DE/SQL) | Implementation & Hard Problems | Status | Casual |
|---|---|---|---|---|---|
| Day 1 | Setup, Lists, Slicing, Methods | BQ Star vs Snowflake Modeling | SQL: Build star-schema view layer | Not Completed | Kafka vs RabbitMQ |
| Day 2 | Dicts, .get(), .pop() | SQL: RANK vs DENSE_RANK | Logic: Word frequency mapping | Not Completed | Message Queues |
| Day 3 | Sets, Uniqueness, Intersections | SQL: LEAD & LAG usage | Logic: Set vs List speed testing | Not Completed | Caching |
| Day 4 | List & Dict Comprehensions | BQ: Slots vs. On-demand math | Logic: Nested comprehensions | Not Completed | Sharding |
| Day 5 | Functions: *args and **kwargs | SQL: Self-Joins (Hierarchy) | Logic: Build robust API Ingestion Class with Retries | Not Completed | Data Modeling |
| Day 6 | Type Hinting (Google Standard) | BQ Partitioning vs Clustering | Logic: Type-safe function calls | Not Completed | API Design |
| Day 7 | Error Handling: try-except-finally | SQL: Running Totals (SUM OVER) | Logic: Custom Exception classes | Not Completed | Object Storage |
| Day 8 | File I/O: Generator-based reading | SQL: Recursive CTEs | Logic: csv module parsing | Not Completed | Consistent Hashing |
| Day 9 | OOP: init, self, and Methods | Architecture: OLTP vs OLAP | Logic: Create a User class | Not Completed | Recommendation System Infra |
| Day 10 | Inheritance: Super() and Mixins | DE: Idempotency logic | Logic: Admin inherits User | Not Completed | Prepare for System Design |
| Day 11 | Decorators: @timer & @retry | SQL: Gaps & Islands Part 1 | Logic: Timing function execution | Not Completed | Kafka |
| Day 12 | Generators: yield keyword | SQL: Gaps & Islands Part 2 | Logic: Memory-efficient looping | Not Completed | Redis |
| Day 13 | Context Managers: with | SQL: Median without MEDIAN() | Logic: Custom DB connection class | Not Completed | API Gateways |
| Day 14 | LC Easy: Two Sum | SQL: Complex JSON parsing | Streaming: Stream-to-Stream vs Stream-to-Static Joins | Not Completed | Networking Essentials |
| Day 15 | LC Easy: Valid Anagram | BQ Authorized Views logic | Logic: Handling Late-Arriving Data and Side-Outputs | Not Completed | DB Indexing |
| Day 16 | LC Med: Group Anagrams | SQL: Ranking without Window Func | Logic: Handling Late-Arriving Data and Side-Outputs | Not Completed | CAP Theorem |
| Day 17 | LC Med: Merge Intervals | Data Lake Partitioning Design | Python: C-API Overview | Not Completed | Elasticsearch |
| Day 18 | LC Med: Group Anagrams (Advanced Hash Map) | SQL: Date/Time (Timezones) | Logic: Rotating log file scripts | Not Completed | Consistent Hashing |
| Day 19 | Pydantic: Schema Validation | BQ Materialized Views vs Tables | Logic: Validate API JSON input | Not Completed | DynamoDB |
| Day 20 | Unit Testing: pytest & Mocks | SQL: Cumulative Percentile | Logic: Mocking a DB response | Not Completed | Distributed Transactions |
| Day 21 | Requests: API Pagination logic | API Rate Limiting logic | Logic: Fetch multi-page data | Not Completed | Data Structures for Big Data |
| Day 22 | Multiprocessing: Pool usage | Horizontal vs Vertical Scaling | Logic: Parallelize 1k tasks | Not Completed | Cassandra |
| Day 23 | Threading: I/O bound waits | Consistent Hashing Logic | Data Quality: Schema Drift & Soda Core/Great Expectations | Not Completed | Time Series Database |
| Day 24 | Regex: re.sub & re.match | PII/GDPR Masking Logic | Logic: Extract data from text | Not Completed | Proximity Search |
| Day 25 | LC Med: Max Subarray | SQL: First/Last Value in Group | Speed: Solve in < 25 mins | Not Completed | Design Ticketmaster |
| Day 26 | LC Med: Reverse Linked List | SCD Type 1 vs Type 2 Logic | Speed: Solve in < 25 mins | Not Completed | Design Uber |
| Day 27 | DuckDB: Local SQL in Python | BQ BI Engine vs MV Trade-offs | Logic: Query CSV via DuckDB | Not Completed | Design Dropbox or Google Drive |
| Day 28 | Polars: Vectorized Dataframes | Data Observability Metrics | Logic: Filter 1M rows in Polars | Not Completed | Design Bitly |
| Day 29 | Project: API-to-DB Pipeline | SQL: Handling NULLs in Joins | Logic: Pydantic + Logging | Not Completed | Design Twitter |
| Day 30 | LC Med: Longest Substring | Spark: Driver/Executor/Cores | Python: Setup Local PySpark | Not Completed | Design Whatsapp |
| Day 31 | LC Med: Container with Water | Spark: Lazy Eval & DAGs | Python: Write a .map pipeline | Not Completed | Design an Ad Click Aggregator |
| Day 32 | Python: itertools (chain/zip) | Spark: Transf. vs Actions | Python: Write a .filter job | Not Completed | Design YouTube |
| Day 33 | Python: collections (Counter) | Spark: The Shuffle Internals | Python: Write a .groupBy job | Not Completed | Design a Web Crawler |
| Day 34 | LC Med: 3Sum | Spark: repartition vs coalesce | Python: PySpark join script | Not Completed | Design a Distributed Rate Limiter |
| Day 35 | Advanced Lambda/Map | Spark: Sort-Merge Joins | Python: Multi-table join script | Not Completed | Design LeetCode |
| Day 36 | LC Med: Search in Rotated Array | Spark: Broadcast Joins | Arch: Join strategy trade-offs | Not Completed | Design Tinder |
| Day 37 | Python: Spark Data Skew logic | Spark: Salting in PySpark | Arch: Cost of Shuffle in Cloud | Not Completed | Design Live Comments |
| Day 38 | LC Med: Valid Parentheses | Spark: Window Functions | Python: PySpark Window coding | Not Completed | Design FB News Feed |
| Day 39 | Python: Spark UI Debugging | Spark: Memory Management | Logic: Fixing Spill to Disk | Not Completed | Top-K System Design |
| Day 40 | LC Med: Top K Frequent | Spark: Caching/Persist Levels | Arch: Serialization (Kryo) | Not Completed | Design FB Post Search |
| Day 41 | Iceberg: Table Snapshots | Iceberg: Hidden Partitioning | Python: Iceberg metadata script | Not Completed | Design an Ad Click Aggregator |
| Day 42 | Delta Lake: Z-Ordering script | Delta Lake: Vacuum & Optimize | Arch: Compaction strategies | Not Completed | LLD-Design an Elevator |
| Day 43 | Beam: PCollections logic | GCP: Dataflow Runner | Python: Write a Beam ParDo | Not Completed | Concurrency in Low-level Design |
| Day 44 | Beam ParDo: DoFn logic | GCP: Dataflow Side Inputs | Python: Complex transform logic | Not Completed | Design Amazon Locker |
| Day 45 | Beam Windowing: Sliding | Arch: Watermarks & Latency | Python: Script a Sliding Window | Not Completed | LLD-Design Connect Four |
| Day 46 | Beam: Allowed Lateness | Arch: Triggers & Panes | Python: Late data handling script | Not Completed | Design Bot Detection |
| Day 47 | LC Med: Number of Islands | Kafka: Topic Partitions | Arch: Consumer Group Rebalance | Not Completed | Design Content Moderation |
| Day 48 | Kafka Producer script | Arch: Exactly-Once Semantics | Python: Offset management script | Not Completed | Client-Server Architecture |
| Day 49 | Pub/Sub: Pull vs Push scripts | GCP: Dead Letter Topics | Python: Pub/Sub Async Subscriber | Not Completed | IP Addresses |
| Day 50 | BQ Search Indexing | GCP: BQ ML (Logistic Reg) | Python: Unstructured data query | Not Completed | Domain Name System (DNS) |
| Day 51 | LC Med: Course Schedule | Arch: Lambda vs Kappa | Arch: Streaming Architecture | Not Completed | Proxy / Reverse proxy |
| Day 52 | Python Profiling: cProfile | GCP: BQ Omni Multi-Cloud | Logic: Finding code bottlenecks | Not Completed | Latency |
| Day 53 | Python: BQ MV Refresh script | GCP: BI Engine Acceleration | Arch: MV Refresh Strategies | Not Completed | HTTP / HTTPS |
| Day 54 | LC Med: Subsets | Arch: Data Mesh Ownership | Arch: Decentralized Data | Not Completed | API's |
| Day 55 | Python: @dataclass usage | Arch: Metadata Management | Logic: Schema Object script | Not Completed | REST |
| Day 56 | LC Med: Word Search | Streaming: Watermarks, Event-time vs Processing-time | Logic: Cloud Billing Analysis | Not Completed | GraphQL |
| Day 57 | Phase 2 Review | Data Contracts | Logic: Re-code Skew fix | Not Completed | Database |
| Day 58 | Python: Script a Rate Limiter | SD: Design TinyURL | Arch: NoSQL vs SQL for URLs | Not Completed | SQL Vs NoSQL |
| Day 59 | Python: Script a LRU Cache | SD: Design Twitter News Feed | Arch: Fan-out on write/read | Not Completed | Vertical scaling |
| Day 60 | LC Hard: Merge K Sorted Lists | SD: Design Web Crawler | Arch: URL Frontier logic | Not Completed | Horizontal scaling |
| Day 61 | LC Hard: Trapping Rain Water | SD: Scaling Image Uploads | Arch: CDN & S3 optimization | Not Completed | Load balancer |
| Day 62 | Python: BQ Client Library | SD: YouTube View Counter | Python: BQ Dry-run Cost Script | Not Completed | Indexing |
| Day 63 | LC Med: Coin Change | SD: Ad-Click Aggregator | Arch: Real-time windowing | Not Completed | Replication |
| Day 64 | Python: Script a Bloom Filter | SD: Real-time Leaderboard | Arch: Redis Sorted Sets | Not Completed | Sharding |
| Day 65 | LC Med: Longest Increasing Sub | SD: Distributed ID Gen | Arch: Snowflake ID vs UUID | Not Completed | Vertical partitioning |
| Day 66 | Python: GCS Client Lib | SD: Data Mesh Implementation | Arch: Federated Governance | Not Completed | Caching |
| Day 67 | Python: Consistent Hashing | SD: Multi-region Replication | Arch: RPO/RTO calculation | Not Completed | Denormalization |
| Day 68 | LC Hard: Sliding Window Max | SD: Backfill Strategies | Logic: Deterministic backfills | Not Completed | Cap theorem |
| Day 69 | Python: Airflow Custom Op | SD: Schema Registry Design | Arch: Protobuf vs JSON | Not Completed | Blob storage |
| Day 70 | Python: Mocking in pytest | SD: Vector DBs for GenAI | Python: Pinecone/Milvus script | Not Completed | Content delivery network (CDN) |
| Day 71 | Python: 3.12 Typing | SD: RAG Architecture | Arch: Chunking strategies | Not Completed | Web sockets |
| Day 72 | LC Med: Subsets II | SD: Disaster Recovery | Arch: Region vs Zone failure | Not Completed | Web Hooks |
| Day 73 | BFS/DFS Logic in Python | SD: Log Aggregation (ELK) | Arch: Indexing log data | Not Completed | Microservices |
| Day 74 | LC Med: Clone Graph | SD: API Design (gRPC/REST) | Arch: Protocol Buffers internal | Not Completed | Message Queues |
| Day 75 | Bit Manipulation tricks | SD: LSM Trees vs B-Trees | Arch: Database engine write path | Not Completed | Rate Limiting |
| Day 76 | Python: heapq mastery | SD: Small File Problem | Python: File compaction script | Not Completed | API Gateway |
| Day 77 | LC Med: Pacific Atlantic | SD: CDC via Debezium | Arch: Write Ahead Log (WAL) | Not Completed | Idempotency |
| Day 78 | Timsort Logic | SD: Metrics Store (Semantic) | Arch: Looker/Tableau Logic | Not Completed | Prefix Sum |
| Day 79 | Implement Trie (Prefix Tree) | SD: Data Contract Enforcer | Python: Schema validator script | Not Completed | Two Pointer |
| Day 80 | Python: aiohttp Async | SD: Observability (SLIs/SLOs) | Arch: Distributed Tracing | Not Completed | Sliding Window |
| Day 81 | LC Hard: Median of Arrays | SD: BQ SQL Optimization | Python: BQ Cost Estimator | Not Completed | Fast & Slow Pointer |
| Day 82 | Python: Multiprocessing vs Threading for I/O bound tasks | SD: Hybrid Cloud Data Flow | Arch: Anthos / Multi-cloud | Not Completed | Linked List In-Place Reversal |
| Day 83 | LC Med: Kth Largest Element | SD: Security (IAM/KMS) | Arch: Encryption at Rest | Not Completed | Monotonic Stack |
| Day 84 | Python: BQ Dry-runs script | SD: FinOps Automation | Python: Billing Alerting script | Not Completed | Top 'k' Elements |
| Day 85 | Project: Petabyte Scale Design | SD: Whiteboard Session | Arch: Iceberg vs Delta trade-offs | Not Completed | Quick Select |
| Day 86 | Revision: Lists, Dicts, Sets | Logic: O(N) efficiency | Python: Re-write Phase 1 logic | Not Completed | Overlapping Intervals |
| Day 87 | Revision: OOP & Inheritance | Logic: Decorators & Generators | Python: Build a Framework base | Not Completed | Modified Binary Search |
| Day 88 | Revision: Spark Internals | Logic: Shuffle & Skew | Python: Re-code Salting logic | Not Completed | Depth-First Search (DFS) |
| Day 89 | Revision: Apache Beam | Logic: Windowing & Watermarks | Python: Triggering logic script | Not Completed | Breadth-First Search (BFS) |
| Day 90 | Revision: BigQuery | Logic: Slots & Partitioning | SQL: BQ Optimization techniques | Not Completed | Matrix Traversal |
| Day 91 | Data Lineage (OpenLineage/Apache Atlas) | TinyURL, Twitter, YouTube | Arch: Trade-off deep dive | Not Completed | Backtracking |
| Day 92 | SD: Security (RBAC, Row/Column Level Security, Data Masking) | Kafka, Rate Limiters, Hashing | Arch: Distributed consensus | Not Completed | Dynamic Programming |
| Day 93 | Revision: Hard SQL 1 | Recursive CTEs, Gaps/Islands | SQL: Solve 5 Hard problems | Not Completed |  |
| Day 94 | Revision: Hard SQL 2 | Window Funcs, JSON, PIVOT | SQL: Solve 5 Hard problems | Not Completed |  |
| Day 95 | Final Review: STAR Stories | Architectural Trade-offs | Final Mentality Prep | Not Completed |  |

---

## Refresh Instructions

To refresh this file later:

1. Read sheet tab `Data Engineering Roadmap and Tasks`.
2. Export columns `A:F`.
3. Replace the list above with the new snapshot.
