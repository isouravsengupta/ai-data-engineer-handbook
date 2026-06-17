# AI Engineering To Do

| Day | Python & Coding (Logic) | Core Subject (DE/SQL) | Implementation & Hard Problems | Extra/System |
|---|---|---|---|---|
| 1 | Setup, Lists, Slicing, Methods | BQ Star vs Snowflake Modeling | SQL: Build star-schema view layer | Kafka vs RabbitMQ |
| 2 | Dicts, .get(), .pop() | SQL: RANK vs DENSE_RANK | Logic: Word frequency mapping | Message Queues |
| 3 | Sets, Uniqueness, Intersections | SQL: LEAD & LAG usage | Logic: Set vs List speed testing | Caching |
| 4 | List & Dict Comprehensions | BQ: Slots vs. On-demand math | Logic: Nested comprehensions | Sharding |
| 5 | Functions: *args and **kwargs | SQL: Self-Joins (Hierarchy) | Logic: Build robust API Ingestion Class with Retries | Data Modeling |
| 6 | Type Hinting (Google Standard) | BQ Partitioning vs Clustering | Logic: Type-safe function calls | API Design |
| 7 | Error Handling: try-except-finally | SQL: Running Totals (SUM OVER) | Logic: Custom Exception classes | Object Storage |
| 8 | File I/O: Generator-based reading | SQL: Recursive CTEs | Logic: csv module parsing | Consistent Hashing |
| 9 | OOP: init, self, and Methods | Architecture: OLTP vs OLAP | Logic: Create a User class | Recommendation System Infra |
| 10 | Inheritance: Super() and Mixins | DE: Idempotency logic | Logic: Admin inherits User | Prepare for System Design |
| 11 | Decorators: @timer & @retry | SQL: Gaps & Islands Part 1 | Logic: Timing function execution | Kafka |
| 12 | Generators: yield keyword | SQL: Gaps & Islands Part 2 | Logic: Memory-efficient looping | Redis |
| 13 | Context Managers: with | SQL: Median without MEDIAN() | Logic: Custom DB connection class | API Gateways |
| 14 | LC Easy: Two Sum | SQL: Complex JSON parsing | Streaming: Stream-to-Stream vs Stream-to-Static Joins | Networking Essentials |
| 15 | LC Easy: Valid Anagram | BQ Authorized Views logic | Logic: Handling Late-Arriving Data and Side-Outputs | DB Indexing |
| 16 | LC Med: Group Anagrams | SQL: Ranking without Window Func | Logic: Handling Late-Arriving Data and Side-Outputs | CAP Theorem |
| 17 | LC Med: Merge Intervals | Data Lake Partitioning Design | Python: C-API Overview | Elasticsearch |
| 18 | LC Med: Group Anagrams (Advanced Hash Map) | SQL: Date/Time (Timezones) | Logic: Rotating log file scripts | Consistent Hashing |
| 19 | Pydantic: Schema Validation | BQ Materialized Views vs Tables | Logic: Validate API JSON input | DynamoDB |
| 20 | Unit Testing: pytest & Mocks | SQL: Cumulative Percentile | Logic: Mocking a DB response | Distributed Transactions |
| 21 | Requests: API Pagination logic | API Rate Limiting logic | Logic: Fetch multi-page data | Data Structures for Big Data |
| 22 | Multiprocessing: Pool usage | Horizontal vs Vertical Scaling | Logic: Parallelize 1k tasks | Cassandra |
| 23 | Threading: I/O bound waits | Consistent Hashing Logic | Data Quality: Schema Drift & Soda Core/Great Expectations | Time Series Database |
| 24 | Regex: re.sub & re.match | PII/GDPR Masking Logic | Logic: Extract data from text | Proximity Search |
| 25 | LC Med: Max Subarray | SQL: First/Last Value in Group | Speed: Solve in < 25 mins | Design Ticketmaster |
| 26 | LC Med: Reverse Linked List | SCD Type 1 vs Type 2 Logic | Speed: Solve in < 25 mins | Design Uber |
| 27 | DuckDB: Local SQL in Python | BQ BI Engine vs MV Trade-offs | Logic: Query CSV via DuckDB | Design Dropbox or Google Drive |
| 28 | Polars: Vectorized Dataframes | Data Observability Metrics | Logic: Filter 1M rows in Polars | Design Bitly |
| 29 | Project: API-to-DB Pipeline | SQL: Handling NULLs in Joins | Logic: Pydantic + Logging | Design Twitter |
| 30 | LC Med: Longest Substring | Spark: Driver/Executor/Cores | Python: Setup Local PySpark | Design Whatsapp |
| 31 | LC Med: Container with Water | Spark: Lazy Eval & DAGs | Python: Write a .map pipeline | Design an Ad Click Aggregator |
| 32 | Python: itertools (chain/zip) | Spark: Transf. vs Actions | Python: Write a .filter job | Design YouTube |
| 33 | Python: collections (Counter) | Spark: The Shuffle Internals | Python: Write a .groupBy job | Design a Web Crawler |
| 34 | LC Med: 3Sum | Spark: repartition vs coalesce | Python: PySpark join script | Design a Distributed Rate Limiter |
| 35 | Advanced Lambda/Map | Spark: Sort-Merge Joins | Python: Multi-table join script | Design LeetCode |
| 36 | LC Med: Search in Rotated Array | Spark: Broadcast Joins | Arch: Join strategy trade-offs | Design Tinder |
| 37 | Python: Spark Data Skew logic | Spark: Salting in PySpark | Arch: Cost of Shuffle in Cloud | Design Live Comments |
| 38 | LC Med: Valid Parentheses | Spark: Window Functions | Python: PySpark Window coding | Design FB News Feed |
| 39 | Python: Spark UI Debugging | Spark: Memory Management | Logic: Fixing Spill to Disk | Top-K System Design |
| 40 | LC Med: Top K Frequent | Spark: Caching/Persist Levels | Arch: Serialization (Kryo) | Design FB Post Search |
| 41 | Iceberg: Table Snapshots | Iceberg: Hidden Partitioning | Python: Iceberg metadata script | Design an Ad Click Aggregator |
| 42 | Delta Lake: Z-Ordering script | Delta Lake: Vacuum & Optimize | Arch: Compaction strategies | LLD-Design an Elevator |
| 43 | Beam: PCollections logic | GCP: Dataflow Runner | Python: Write a Beam ParDo | Concurrency in Low-level Design |
| 44 | Beam ParDo: DoFn logic | GCP: Dataflow Side Inputs | Python: Complex transform logic | Design Amazon Locker |
| 45 | Beam Windowing: Sliding | Arch: Watermarks & Latency | Python: Script a Sliding Window | LLD-Design Connect Four |
| 46 | Beam: Allowed Lateness | Arch: Triggers & Panes | Python: Late data handling script | Design Bot Detection |
| 47 | LC Med: Number of Islands | Kafka: Topic Partitions | Arch: Consumer Group Rebalance | Design Content Moderation |
| 48 | Kafka Producer script | Arch: Exactly-Once Semantics | Python: Offset management script | Client-Server Architecture |
| 49 | Pub/Sub: Pull vs Push scripts | GCP: Dead Letter Topics | Python: Pub/Sub Async Subscriber | IP Addresses |
| 50 | BQ Search Indexing | GCP: BQ ML (Logistic Reg) | Python: Unstructured data query | Domain Name System (DNS) |
| 51 | LC Med: Course Schedule | Arch: Lambda vs Kappa | Arch: Streaming Architecture | Proxy / Reverse proxy |
| 52 | Python Profiling: cProfile | GCP: BQ Omni Multi-Cloud | Logic: Finding code bottlenecks | Latency |
| 53 | Python: BQ MV Refresh script | GCP: BI Engine Acceleration | Arch: MV Refresh Strategies | HTTP / HTTPS |
| 54 | LC Med: Subsets | Arch: Data Mesh Ownership | Arch: Decentralized Data | API's |
| 55 | Python: @dataclass usage | Arch: Metadata Management | Logic: Schema Object script | REST |
| 56 | LC Med: Word Search | Streaming: Watermarks, Event-time vs Processing-time | Logic: Cloud Billing Analysis | GraphQL |
| 57 | Phase 2 Review | Data Contracts | Logic: Re-code Skew fix | Database |
| 58 | Python: Script a Rate Limiter | SD: Design TinyURL | Arch: NoSQL vs SQL for URLs | SQL Vs NoSQL |
| 59 | Python: Script a LRU Cache | SD: Design Twitter News Feed | Arch: Fan-out on write/read | Vertical scaling |
| 60 | LC Hard: Merge K Sorted Lists | SD: Design Web Crawler | Arch: URL Frontier logic | Horizontal scaling |
| 61 | LC Hard: Trapping Rain Water | SD: Scaling Image Uploads | Arch: CDN & S3 optimization | Load balancer |
| 62 | Python: BQ Client Library | SD: YouTube View Counter | Python: BQ Dry-run Cost Script | Indexing |
| 63 | LC Med: Coin Change | SD: Ad-Click Aggregator | Arch: Real-time windowing | Replication |
| 64 | Python: Script a Bloom Filter | SD: Real-time Leaderboard | Arch: Redis Sorted Sets | Sharding |
| 65 | LC Med: Longest Increasing Sub | SD: Distributed ID Gen | Arch: Snowflake ID vs UUID | Vertical partitioning |
| 66 | Python: GCS Client Lib | SD: Data Mesh Implementation | Arch: Federated Governance | Caching |
| 67 | Python: Consistent Hashing | SD: Multi-region Replication | Arch: RPO/RTO calculation | Denormalization |
| 68 | LC Hard: Sliding Window Max | SD: Backfill Strategies | Logic: Deterministic backfills | Cap theorem |
| 69 | Python: Airflow Custom Op | SD: Schema Registry Design | Arch: Protobuf vs JSON | Blob storage |
| 70 | Python: Mocking in pytest | SD: Vector DBs for GenAI | Python: Pinecone/Milvus script | Content delivery network (CDN) |
| 71 | Python: 3.12 Typing | SD: RAG Architecture | Arch: Chunking strategies | Web sockets |
| 72 | LC Med: Subsets II | SD: Disaster Recovery | Arch: Region vs Zone failure | Web Hooks |
| 73 | BFS/DFS Logic in Python | SD: Log Aggregation (ELK) | Arch: Indexing log data | Microservices |
| 74 | LC Med: Clone Graph | SD: API Design (gRPC/REST) | Arch: Protocol Buffers internal | Message Queues |
| 75 | Bit Manipulation tricks | SD: LSM Trees vs B-Trees | Arch: Database engine write path | Rate Limiting |
| 76 | Python: heapq mastery | SD: Small File Problem | Python: File compaction script | API Gateway |
| 77 | LC Med: Pacific Atlantic | SD: CDC via Debezium | Arch: Write Ahead Log (WAL) | Idempotency |
| 78 | Timsort Logic | SD: Metrics Store (Semantic) | Arch: Looker/Tableau Logic | Prefix Sum |
| 79 | Implement Trie (Prefix Tree) | SD: Data Contract Enforcer | Python: Schema validator script | Two Pointer |
| 80 | Python: aiohttp Async | SD: Observability (SLIs/SLOs) | Arch: Distributed Tracing | Sliding Window |
| 81 | LC Hard: Median of Arrays | SD: BQ SQL Optimization | Python: BQ Cost Estimator | Fast & Slow Pointer |
| 82 | Python: Multiprocessing vs Threading for I/O bound tasks | SD: Hybrid Cloud Data Flow | Arch: Anthos / Multi-cloud | Linked List In-Place Reversal |
| 83 | LC Med: Kth Largest Element | SD: Security (IAM/KMS) | Arch: Encryption at Rest | Monotonic Stack |
| 84 | Python: BQ Dry-runs script | SD: FinOps Automation | Python: Billing Alerting script | Top 'k' Elements |
| 85 | Project: Petabyte Scale Design | SD: Whiteboard Session | Arch: Iceberg vs Delta trade-offs | Quick Select |
| 86 | Revision: Lists, Dicts, Sets | Logic: O(N) efficiency | Python: Re-write Phase 1 logic | Overlapping Intervals |
| 87 | Revision: OOP & Inheritance | Logic: Decorators & Generators | Python: Build a Framework base | Modified Binary Search |
| 88 | Revision: Spark Internals | Logic: Shuffle & Skew | Python: Re-code Salting logic | Depth-First Search (DFS) |
| 89 | Revision: Apache Beam | Logic: Windowing & Watermarks | Python: Triggering logic script | Breadth-First Search (BFS) |
| 90 | Revision: BigQuery | Logic: Slots & Partitioning | SQL: BQ Optimization techniques | Matrix Traversal |
| 91 | Data Lineage (OpenLineage/Apache Atlas) | TinyURL, Twitter, YouTube | Arch: Trade-off deep dive | Backtracking |
| 92 | SD: Security (RBAC, Row/Column Level Security, Data Masking) | Kafka, Rate Limiters, Hashing | Arch: Distributed consensus | Dynamic Programming |
| 93 | Revision: Hard SQL 1 | Recursive CTEs, Gaps/Islands | SQL: Solve 5 Hard problems |  |
| 94 | Revision: Hard SQL 2 | Window Funcs, JSON, PIVOT | SQL: Solve 5 Hard problems |  |
| 95 | Final Review: STAR Stories | Architectural Trade-offs | Final Mentality Prep |  |

---

## Refresh Instructions

To refresh this file later:

1. Read sheet tab `Data Engineering Roadmap and Tasks`.
2. Export columns `A:F`.
3. Replace the list above with the new snapshot.
