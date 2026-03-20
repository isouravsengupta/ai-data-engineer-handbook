# Advanced SQL

📄 File: `book/03_sql_query_engines/advanced_sql.md`

This chapter covers **advanced SQL** — CTEs, CASE, EXISTS, UNION. Essential for complex analytics pipelines.

---

## Study Plan (3–4 days)

* Day 1: CTEs (WITH)
* Day 2: CASE, COALESCE, NULL handling
* Day 3: EXISTS, UNION, EXCEPT
* Day 4: Exercises

---

## 1 — CTEs (Common Table Expressions)

```sql
-- WITH: define reusable subqueries
WITH active_users AS (
    SELECT * FROM users WHERE status = 'active'
),
recent_orders AS (
    SELECT * FROM orders WHERE created_at > '2025-01-01'
)
SELECT u.name, COUNT(o.id) AS order_count
FROM active_users u
LEFT JOIN recent_orders o ON u.id = o.user_id
GROUP BY u.name;
```

---

## Diagram — CTE Flow

```mermaid
flowchart LR
    A[WITH cte AS] --> B[SELECT from cte]
    B --> C[Main query]
```

---

## 2 — CASE Expression

```sql
SELECT
    name,
    CASE
        WHEN age < 18 THEN 'minor'
        WHEN age < 65 THEN 'adult'
        ELSE 'senior'
    END AS age_group
FROM users;
```

---

## 3 — COALESCE and NULLIF

```sql
-- COALESCE: first non-NULL
SELECT COALESCE(middle_name, '') FROM users;

-- NULLIF: NULL if equal
SELECT NULLIF(column, 0) FROM table;
```

---

## 4 — EXISTS (Often faster than IN for large sets)

```sql
SELECT * FROM users u
WHERE EXISTS (
    SELECT 1 FROM orders o
    WHERE o.user_id = u.id AND o.amount > 100
);
```

---

## 5 — UNION vs UNION ALL

```sql
-- UNION: distinct rows
SELECT name FROM users
UNION
SELECT name FROM admins;

-- UNION ALL: keep duplicates (faster)
SELECT name FROM users
UNION ALL
SELECT name FROM admins;
```

---

## Interview Questions

1. CTE vs subquery — when to use which?
2. EXISTS vs IN — performance?
3. UNION vs UNION ALL?

---

## Key Takeaways

* CTEs improve readability
* CASE for conditional logic
* EXISTS for correlated subqueries
* UNION removes duplicates, UNION ALL does not

---

## Next Chapter

Proceed to: **window_functions.md**
