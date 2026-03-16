# AI Data Engineer Gita (2026 Edition)

The **AI Data Engineer Gita** is a living handbook and roadmap for engineers who want to reach the **top 1% of AI Data Engineering and AI Infrastructure roles**.

This guide is designed to help engineers build the skills required to work on large‑scale AI systems at companies such as:

- Salesforce
- OpenAI
- Anthropic
- DeepMind
- Databricks
- Snowflake
- NVIDIA
- Stripe

The goal is not just learning theory, but building the ability to:

- design AI data platforms
- scale machine learning systems
- build RAG pipelines
- run distributed data infrastructure
- understand research papers
- pass elite engineering interviews

This handbook is meant to be used alongside **coding practice, experiments, and real projects**.

---


# How To Use The Gita

Each chapter in the Gita follows the same structure:

1. Concept
2. Internal Implementation
3. Why It Matters In Real Systems
4. Code Examples
5. Interview Questions
6. Practice Problems
7. Mini Project
8. Mastery Task

You should study every topic using the following cycle:

Learn → Implement → Experiment → Document → Publish

Your GitHub repository becomes both:

- a **study log**
- a **portfolio of engineering capability**

---

# The Master Roadmap

Becoming a top AI data engineer requires understanding the **entire AI systems stack**.

Modern AI platforms are composed of multiple layers. Mastery requires understanding how each layer interacts with the others.

The Gita organizes learning into **system layers** rather than random tools.

---

# Layer 1 — Programming Foundations

Everything begins with strong programming fundamentals.

Topics:

- Python internals
- data structures
- algorithms
- concurrency
- memory management
- performance optimization

Key technologies:

- Python
- Numba
- C extensions

These skills allow you to write efficient data and AI infrastructure code.

---

# Layer 2 — Algorithms and Data Structures

AI engineers must be able to solve complex problems and pass technical interviews.

Topics:

- arrays
- hash maps
- trees
- graphs
- heaps
- dynamic programming
- sliding window
- two pointer techniques

Goal:

Solve **300+ algorithm problems** with a focus on medium and hard problems.

---

# Layer 3 — SQL and Query Engines

Large scale AI systems depend heavily on structured data systems.

Topics:

- advanced SQL
- query optimization
- window functions
- indexing
- query planning

Query engines to understand:

- DuckDB
- Trino
- Presto
- Spark SQL

These engines power analytics pipelines and dataset preparation.

---

# Layer 4 — Data Engineering Systems

AI systems rely on reliable pipelines to move and transform data.

Topics:

- ETL vs ELT
- batch pipelines
- streaming pipelines
- data quality

Important tools:

- Apache Spark
- Apache Kafka
- Apache Flink
- dbt

These systems process large scale training and analytics datasets.

---

# Layer 5 — Data Storage and Lakehouse Architecture

AI training datasets often reach petabyte scale.

Topics:

- columnar storage
- object storage
- data lakehouses

Technologies:

- Parquet
- Delta Lake
- Apache Iceberg
- Apache Hudi

These systems enable scalable dataset management.

---

# Layer 6 — Distributed Systems

Most large scale AI infrastructure runs on distributed clusters.

Topics:

- CAP theorem
- replication
- partitioning
- consensus algorithms
- distributed logs

Understanding distributed systems enables engineers to design scalable platforms.

---

# Layer 7 — Machine Learning Foundations

AI infrastructure engineers must understand the models their systems support.

Topics:

- regression
- classification
- clustering
- dimensionality reduction

Math foundations:

- linear algebra
- probability
- optimization

This knowledge helps engineers reason about models and training pipelines.

---

# Layer 8 — Deep Learning Systems

Modern AI relies heavily on neural networks.

Topics:

- neural networks
- backpropagation
- training loops
- PyTorch fundamentals

Understanding these systems helps engineers support training pipelines.

---

# Layer 9 — Transformers and LLM Internals

Large language models dominate modern AI systems.

Topics:

- attention mechanism
- transformer architecture
- positional encoding
- tokenization
- scaling laws

These concepts explain how modern LLMs operate internally.

---

# Layer 10 — Embeddings and Vector Databases

Many AI applications rely on vector similarity search.

Topics:

- embeddings
- cosine similarity
- approximate nearest neighbors

Technologies:

- FAISS
- Milvus
- Qdrant
- pgvector

These systems enable semantic search and knowledge retrieval.

---

# Layer 11 — Retrieval Augmented Generation (RAG)

RAG pipelines combine LLMs with external knowledge.

Topics:

- document chunking
- hybrid search
- retrieval strategies
- agentic RAG

These systems power many modern AI products.

---

# Layer 12 — AI Infrastructure and Inference

Serving models efficiently is critical for production systems.

Topics:

- LLM inference
- batching
- KV cache
- token streaming

Tools:

- vLLM
- Triton Inference Server
- Ray Serve

These systems enable scalable AI services.

---

# Layer 13 — GPU Systems

Modern AI training and inference run on GPUs.

Topics:

- GPU architecture
- CUDA basics
- GPU memory hierarchy
- tensor cores

Understanding GPU systems helps optimize AI workloads.

---

# Layer 14 — Evaluation Frameworks

AI systems must be measurable to improve.

Topics:

- RAG evaluation
- benchmark datasets
- A/B testing

Tools:

- RAGAS

Evaluation ensures AI systems produce reliable outputs.

---

# Layer 15 — Observability and Monitoring

Production AI systems require monitoring and tracing.

Topics:

- prompt tracing
- latency metrics
- token usage

Tools:

- Langfuse
- Arize
- OpenTelemetry

Observability helps detect issues in AI pipelines.

---

# Layer 16 — AI Security and Compliance

AI systems introduce new security challenges.

Topics:

- prompt injection
- jailbreak attacks
- data leakage
- PII protection

Security becomes critical when deploying AI at scale.

---

# Layer 17 — Research Engineering

Top AI labs rely heavily on research engineering.

Topics:

- reading research papers
- implementing papers
- benchmarking experiments

This skill allows engineers to translate research into production systems.

---

# Layer 18 — Open Source Engineering

Contributing to open source builds credibility.

Topics:

- Git workflows
- writing pull requests
- contributing to major projects

Example projects:

- Spark
- Ray
- DuckDB
- Airflow

---

# Layer 19 — Portfolio Projects

A strong engineering portfolio proves capability.

Example projects:

- vector search engine
- RAG pipeline
- distributed data pipeline
- LLM inference server

These projects demonstrate real engineering ability.

---

# Layer 20 — Career Engineering

Reaching top roles requires more than technical skill.

Topics:

- GitHub portfolio strategy
- resume writing
- LinkedIn optimization
- interview preparation
- salary negotiation

The combination of **skills + visibility + proof of work** leads to top opportunities.

---

# Study Strategy

Recommended weekly schedule:

Weekdays

- 2 hours study
- 1 hour coding

Weekends

- 4–6 hours project work

The goal is to continuously:

- learn
- build
- document

---

# The Philosophy of the Gita

The purpose of this handbook is not simply to list technologies.

Instead, it aims to build **deep systems thinking**.

Top engineers are not defined by how many tools they know, but by their ability to:

- understand systems deeply
- learn new technologies quickly
- build reliable infrastructure

By mastering the layers of the AI systems stack, engineers can adapt to new tools and technologies throughout their careers.

---

# Next Step

The first section of the Gita begins with:

**Python Programming Foundations**.

Understanding Python internals forms the basis for building scalable AI infrastructure.

The next chapter begins with:

**Python Basics and Data Structures.**

---

# Phase Index and Navigation

This document is the single source of truth for the learning path from fundamentals to top 1% AI Data Engineer. The roadmap is organized into **phases**; detail for each phase lives in the corresponding `book/XX_*/` directory.

| Phase | Topic | Focus |
|-------|--------|--------|
| 01 | Python Programming | Core language, concurrency, profiling, C extensions |
| 02 | Algorithms & Data Structures | Arrays, hashes, trees, graphs, DP, heaps, tries |
| 03 | SQL & Query Engines | SQL, window functions, DuckDB, Trino, Presto, Spark SQL |
| 04 | Data Engineering Systems | ETL/ELT, batch/stream, Spark, Kafka, Flink, dbt, data quality |
| 05 | Data Storage & Lakehouse | Parquet, Arrow, Delta, Iceberg, Hudi, LakeFS |
| 06 | Distributed Systems | CAP, replication, partitioning, consensus, scaling |
| 07 | Machine Learning Foundations | Regression, classification, clustering, PCA, evaluation |
| 08 | Deep Learning | Neural nets, backprop, PyTorch basics |
| 09 | Transformers & LLM Core | Attention, tokenization, scaling laws |
| 10 | Embeddings & Vector DBs | Embeddings, ANN, FAISS, Milvus, Qdrant, pgvector |
| 11 | RAG Systems | RAG architecture, chunking, hybrid search, agentic RAG |
| 12 | AI Infrastructure & Inference | LLM inference, KV cache, vLLM, Triton, Ray Serve |
| 13 | GPU Systems | GPU architecture, CUDA, distributed training |
| 14 | Evaluation Frameworks | RAG eval, RAGAS, benchmarks, A/B testing |
| 15 | Observability & Monitoring | Tracing, latency, Langfuse, OpenTelemetry, Prometheus |
| 16 | AI Security & Compliance | Prompt injection, PII, encryption, audit |
| 17 | Research Engineering | Reading/implementing papers, experiments, benchmarking |
| 18 | Open Source Engineering | Git, contributions, PRs, maintaining projects |
| 19 | Portfolio Projects | End-to-end project ideas |
| 20 | Resume & LinkedIn | Templates and optimization |
| 21 | Interview Preparation | Strategy and practice |
| 22 | Salary Negotiation | Tactics and frameworks |
| 23 | Orchestration & Workflow Ops | Airflow, Dagster, Prefect, Argo, Kubeflow |
| 24 | CI/CD & GitOps | GitHub Actions, Argo CD, Flux, ML pipelines |
| 25 | Feature Stores & Dataset Versioning | Feast, Tecton, DVC, LakeFS, data contracts |
| 26 | Data Catalogs & Governance | Amundsen, DataHub, OpenMetadata |
| 27 | Cost & Resource Management | FinOps, resource optimization |

**How to use this roadmap**

1. **Sequential path** — Follow phases 01–27 in order for a full curriculum.
2. **Target roles** — For “AI Data Engineer at a lab,” emphasize 01–06, 09–12, 15, 23–24, 25–27.
3. **Fill gaps** — Use the phase index in each `book/XX_*/` folder to see which chapters you need.

---

# Automation & Daily Checklist

You can absolutely keep the **Daily Checklist** inside the repo and wire it to Cursor so that updating Canvas → syncing → local push becomes a one-small-prompt flow.

Below are two clean approaches. Pick the one you prefer and I will give you the exact files and Cursor prompt to create them automatically.

## Daily checklist (copy into repo as `.cursor/checklist.md`)

```
Daily Checklist — AI Data Engineer Gita

1. Edit Canvas (add/update chapter)
2. Run Cursor sync prompt to export Canvas -> repo (updates /book/*.md)
3. git pull origin main locally; run tests/notebooks/sanity checks
4. Make any local fixes, commit: git commit -m "chore: refine chapter" && git push
5. Post a short progress update on LinkedIn/X (optional)
```

### Option 1 — One‑click via Cursor (recommended)

I will provide a Cursor prompt (below) that:
- creates `.cursor/checklist.md` in the repo with the content above
- creates a lightweight helper script `scripts/run_checklist.sh` that prints the checklist and opens the Canvas doc link (if available)
- commits and pushes both files to `origin/main` so they exist in the repo

**Cursor prompt to run (paste into Cursor)**

```
Create two files in the repository ai-data-engineer-handbook:

1) .cursor/checklist.md with the following content:

---
Daily Checklist — AI Data Engineer Gita

1. Edit Canvas (add/update chapter)
2. Run Cursor sync prompt to export Canvas -> repo (updates /book/*.md)
3. git pull origin main locally; run tests/notebooks/sanity checks
4. Make any local fixes, commit: git commit -m "chore: refine chapter" && git push
5. Post a short progress update on LinkedIn/X (optional)
---

2) scripts/run_checklist.sh which prints the checklist and exits. The file should be executable.

Content of scripts/run_checklist.sh:

#!/usr/bin/env bash
cat .cursor/checklist.md
exit 0

Commit with message: "chore: add cursor checklist and helper script" and push to origin/main. Confirm when done and show the created file paths.
```

This gives you a single Cursor action to create the checklist inside the repo.

### Option 2 — Auto‑reminder (GitHub Action)

If you want the checklist to run or remind you automatically, we can add a GitHub Action that sends a daily Slack/X/Email reminder or creates a GitHub Issue with the checklist. I can generate that workflow file as well.

---

If you'd like, I will now (1) add `.cursor/checklist.md` and `scripts/run_checklist.sh` into the repo by giving you the Cursor prompt above, or (2) also generate the optional GitHub Action that creates a daily issue containing the checklist. Which would you like me to do now?
