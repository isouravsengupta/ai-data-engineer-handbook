# DuckDB

📄 File: `book/03_sql_query_engines/duckdb.md`

This chapter covers **DuckDB** — in-process analytical SQL. Perfect for local analytics, Python embeddings, and AI data pipelines.

---

## Study Plan (2–3 days)

* Day 1: Install, basic queries
* Day 2: Parquet, Python API
* Day 3: Extensions, exercises

---

## 1 — What is DuckDB?

DuckDB is an **in-process** analytical database. No server — runs inside your app.

```mermaid
flowchart LR
    A[Python / App] --> B[DuckDB]
    B --> C[Parquet / CSV]
```

---

## 2 — Basic Usage

```python
import duckdb

# In-memory or file
con = duckdb.connect(':memory:')

# Query Parquet directly
con.execute("SELECT * FROM 'data.parquet' WHERE date > '2025-01-01'").fetchdf()

# Query from Python
con.execute("SELECT * FROM df WHERE x > 10", [df]).fetchall()
```

---

## 3 — Query Parquet

```python
# No import needed - query files directly
result = duckdb.query("""
    SELECT user_id, SUM(amount) as total
    FROM 'sales/*.parquet'
    GROUP BY user_id
""").df()
```

---

## 4 — Python Integration

```python
import pandas as pd
import duckdb

df = pd.DataFrame({'a': [1,2,3], 'b': [4,5,6]})
result = duckdb.query("SELECT a, b FROM df WHERE a > 1").df()
```

---

## 5 — Why DuckDB for AI Data Engineering?

* **Local analytics**: No cluster needed
* **Parquet-native**: Query files directly
* **Fast**: Columnar, vectorized
* **Embedded**: Use from Python, no server

---

## Key Takeaways

* DuckDB = in-process analytical SQL
* Query Parquet/CSV directly
* Great for Python data pipelines

---

## Next Chapter

Proceed to: **trino.md**
