# Batch Processing (Deep Dive)

📄 File: `book/04_data_engineering_systems/batch_processing.md`

This chapter covers **batch processing** — processing data in large chunks. Foundation for ETL, training data preparation, and analytics.

---

## Study Plan (2–3 days)

* Day 1: Batch vs streaming, patterns
* Day 2: Spark batch, partitioning
* Day 3: Idempotency, backfills

---

## 1 — What is Batch Processing?

Process **finite** datasets in **scheduled** jobs. Opposite of streaming (continuous, unbounded).

```mermaid
flowchart LR
    A[Data Lake] --> B[Batch Job]
    B --> C[Transform]
    C --> D[Output]
    D --> E[Warehouse / Lake]
```

---

## 2 — Batch vs Streaming

| Batch | Streaming |
| ----- | --------- |
| Finite data | Unbounded stream |
| Scheduled (hourly, daily) | Continuous |
| High throughput | Low latency |
| Spark, Hive | Kafka, Flink |

---

## 3 — Batch Pipeline Pattern

```python
# 1. Read: load data from source (e.g., Parquet)
df = spark.read.parquet("s3://bucket/raw/date=2025-01-01/")

# 2. Transform: clean, aggregate, join
cleaned = df.filter(df["amount"].isNotNull())
agg = cleaned.groupBy("user_id").agg(
    F.sum("amount").alias("total"),
    F.count("*").alias("count"),
)

# 3. Write: save to destination (overwrite or append)
agg.write.mode("overwrite").parquet("s3://bucket/processed/date=2025-01-01/")
```

---

## Diagram — Batch Job Lifecycle

```mermaid
flowchart TD
    A[Trigger] --> B[Read Source]
    B --> C[Transform]
    C --> D[Write Sink]
    D --> E[Complete]
```

---

## 4 — Partitioning for Batch

* **Input partitioning**: Read only needed partitions (e.g., date)
* **Output partitioning**: Write by partition key for efficient reads

```python
# Read only specific partition
df = spark.read.parquet("s3://bucket/raw/").filter("date = '2025-01-01'")

# Write partitioned
df.write.partitionBy("date").parquet("s3://bucket/out/")
```

---

## 5 — Idempotency (Critical)

* Running job twice = same result
* Use overwrite by partition, or upsert with dedup keys

```mermaid
flowchart LR
    A[Run 1] --> B[Output]
    A[Run 2] --> B
    B --> C[Same result]
```

---

## 6 — Why Batch for AI Data Engineering?

* **Training data**: Daily batch of features, labels
* **Embeddings**: Batch embed documents for RAG index
* **Analytics**: Aggregate metrics for dashboards

---

## Interview Questions with In-Depth Answers

### Q1: Batch vs streaming — when to use which?

**Answer**:

* **Batch**: Use when data is **finite** (e.g., daily dump, historical backfill) and **latency** is acceptable (minutes to hours). Batch is simpler to operate, easier to debug, and typically higher throughput. Examples: nightly ETL, training data preparation, analytics aggregations.
* **Streaming**: Use when data is **unbounded** (e.g., clickstream, logs) and you need **low latency** (seconds). Streaming is more complex (event time, watermarks, exactly-once) but enables real-time dashboards, fraud detection, and live feature updates. Hybrid approach: batch for bulk, streaming for real-time — e.g., Lambda architecture or Kappa with batch backfill.

---

### Q2: How to achieve idempotency?

**Answer**:

**Idempotency** means running the job multiple times produces the same result. Strategies: (1) **Overwrite by partition**: Write to `path/date=2025-01-01/` and use `mode("overwrite")` for that partition only — re-running overwrites the same partition. (2) **Upsert with unique key**: Use Delta/Iceberg/Hudi merge; deduplicate by business key (e.g., `event_id`) so duplicates are collapsed. (3) **Append with dedup in read**: Append new data, but when reading apply `distinct` or window to pick latest per key. (4) **Transactional writes**: Use formats that support ACID (Delta, Iceberg) so partial writes are not visible.

---

### Q3: How to handle late-arriving data?

**Answer**:

**Late data** arrives after the batch window (e.g., event at 23:59 arrives at 02:00 next day). Strategies: (1) **Delayed processing**: Run the batch for `date=D` at `D+1` or `D+2` to allow late arrivals. (2) **Reconciliation job**: Run a separate "catch-up" job that processes late data and merges into the main table (e.g., Delta merge). (3) **Watermarks in streaming**: In Flink/Spark Streaming, use event-time watermarks — data after watermark can be dropped or sent to a side output for batch backfill. (4) **Hybrid**: Streaming for real-time; daily batch to correct for late data.

---

## Key Takeaways

* Batch = finite, scheduled
* Partition for efficiency
* Idempotency for reliability

---

## Next Chapter

Proceed to: **apache_hadoop.md** (foundational big data) or **apache_spark.md** (modern batch engine)
