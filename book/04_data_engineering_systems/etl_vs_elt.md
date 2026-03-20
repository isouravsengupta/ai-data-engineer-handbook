# ETL vs ELT

📄 File: `book/04_data_engineering_systems/etl_vs_elt.md`

This chapter covers **ETL vs ELT** — two paradigms for moving and transforming data. Critical for designing data pipelines.

---

## Study Plan (1–2 days)

* Day 1: ETL (Extract, Transform, Load)
* Day 2: ELT (Extract, Load, Transform)

---

## 1 — ETL (Traditional)

**Extract** → **Transform** → **Load**

* Transform **before** loading into warehouse
* Use separate compute (Spark, dbt, etc.)
* Schema defined before load

```mermaid
flowchart LR
    A[Source] --> B[Extract]
    B --> C[Transform]
    C --> D[Load to DW]
```

---

## 2 — ELT (Modern)

**Extract** → **Load** → **Transform**

* Load raw data first (data lake)
* Transform **inside** warehouse (Snowflake, BigQuery, etc.)
* Leverage warehouse compute

```mermaid
flowchart LR
    A[Source] --> B[Extract]
    B --> C[Load to Lake/DW]
    C --> D[Transform in DW]
```

---

## 3 — When to Use Which

| ETL | ELT |
| --- | --- |
| PII must be scrubbed before load | Raw data retention for reprocessing |
| Limited warehouse compute | Warehouse has scale |
| Legacy systems | Modern cloud warehouses |

---

## 4 — AI Data Engineering Context

* **Training data**: Often ELT — load raw, transform for features
* **RAG pipelines**: ELT — load documents, chunk/embed in pipeline
* **Real-time**: ETL-like — transform in stream (Kafka, Flink)

---

## Key Takeaways

* ETL: transform before load
* ELT: load raw, transform in warehouse
* Modern trend: ELT with cloud warehouses

---

## Next Chapter

Proceed to: **batch_processing.md**
