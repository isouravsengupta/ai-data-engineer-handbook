# Garbage Collection (Deep Dive)

📄 File: `book/01_python_programming/09_garbage_collection.md`

This chapter explains **how Python reclaims memory** — reference counting, cycle detection, and when to care.

---

## Study Plan (2 days)

* Day 1: Reference counting, cycles
* Day 2: gc module, tuning, implications

---

## 1 — Two Mechanisms

Python uses **two** garbage collection mechanisms:

```mermaid
flowchart TD
    A[Garbage Collection] --> B[Reference Counting]
    A --> C[Cycle Detector]
    B --> D[Immediate: ref count → 0]
    C --> E[Periodic: find cycles]
```

---

## 2 — Reference Counting (Primary)

Every object has a `ob_refcnt`. When it reaches 0, memory is freed immediately.

```python
x = [1, 2, 3]   # refcnt = 1
y = x           # refcnt = 2
del x           # refcnt = 1
del y           # refcnt = 0 → freed
```

---

## Diagram — Reference Counting

```mermaid
flowchart LR
    A[Object] --> B["refcnt = 2"]
    B --> C[x]
    B --> D[y]
    C --> E[del x]
    E --> F["refcnt = 1"]
    D --> G[del y]
    G --> H["refcnt = 0"]
    H --> I[Freed]
```

---

## 3 — Reference Cycles (Problem)

Reference counting **cannot** free cycles:

```python
a = []
a.append(a)   # a references itself!
# refcnt of list = 1, never 0
del a         # No more references from outside, but list still exists
```

---

## Diagram — Reference Cycle

```mermaid
flowchart LR
    A[List] --> B[Element 0]
    B --> A
    C[No external refs] -.-> D[Cycle detector finds it]
```

---

## 4 — Cycle Detector (Generational GC)

Python's `gc` module runs a **generational** garbage collector:

* **Generation 0**: New objects
* **Generation 1**: Survived one collection
* **Generation 2**: Long-lived

```python
import gc

# Manually trigger collection
gc.collect()

# Get counts per generation
print(gc.get_count())   # (gen0, gen1, gen2)
```

---

## Diagram — Generational GC

```mermaid
flowchart TD
    A[New Objects] --> B[Gen 0]
    B --> C{Survived?}
    C -->|Yes| D[Gen 1]
    C -->|No| E[Freed]
    D --> F{Survived?}
    F -->|Yes| G[Gen 2]
    F -->|No| E
```

---

## 5 — When to Disable GC

For **short-lived, batch jobs** (e.g., ETL), you might disable GC to avoid pause times:

```python
import gc

gc.disable()   # No automatic GC
# ... run heavy batch ...
gc.enable()    # Re-enable
gc.collect()   # Manual cleanup
```

⚠️ Use only when you understand memory usage.

---

## 6 — Weak References (Advanced)

For caches, use `weakref` to avoid keeping objects alive:

```python
import weakref

obj = SomeClass()
ref = weakref.ref(obj)
ref()   # Returns obj if still alive, else None
del obj
ref()   # None - object was freed
```

---

## 7 — Why This Matters for Data Engineering

* **Large data processing**: Temporary objects → GC pressure
* **Streaming**: Avoid cycles in pipeline objects
* **Caching**: Use weakref for cache that shouldn't prevent GC

---

## Interview Questions

1. How does Python's garbage collection work?
2. What is a reference cycle?
3. When might you disable GC?

---

## Key Takeaways

* Reference counting: immediate free when refcnt=0
* Cycle detector: handles circular references
* Generational GC: reduces pause times
* Disable GC only for controlled batch jobs

👉 Understanding GC helps **tune memory** in data pipelines.

---

## Next Chapter

Proceed to: **10_concurrency.md**
