# AI Data Engineer Handbook

**The AI Data Engineer Gita**  
A complete guide to becoming a top 1% AI Data Engineer working on AI infrastructure, LLM systems, RAG pipelines, and large scale data platforms.

---

## What This Repository Is

This repository is the **AI Data Engineer Handbook** — an open, structured curriculum and reference for **AI Data Engineering**, **LLM Infrastructure**, **RAG Systems**, **Vector Databases**, **Machine Learning Systems**, and production **Data Engineering** at scale. It covers **Spark**, **Ray**, **Airflow**, **Distributed Systems**, and related technologies used at leading AI labs and data platforms (OpenAI, Anthropic, DeepMind, Databricks, Snowflake, and more).

**Keywords:** AI Data Engineering · AI Data Engineer Roadmap · LLM Infrastructure · RAG Systems · Vector Databases · Machine Learning Systems · Data Engineering · Spark · Ray · Airflow · Distributed Systems

---

## About the Book

This repository contains the book **AI Data Engineer Gita**, a deep handbook covering everything required to become a top 1% AI Data Engineer. The book lives in the `book/` directory as a phased curriculum from Python and algorithms through SQL, data engineering systems, lakehouse storage, distributed systems, machine learning and deep learning, transformers and LLMs, embeddings and vector databases, RAG systems, AI infrastructure and inference, GPU systems, evaluation, observability, security, research and open source engineering, orchestration, CI/CD, feature stores, data catalogs, and cost management.

---

## Book Structure

The book is organized in `book/` as follows:

| Directory | Purpose |
|-----------|---------|
| `book/00_master_roadmap.md` | Master learning roadmap for the entire handbook |
| `book/01_python_programming/` … `book/27_cost_resource_management/` | Phased chapters (Python → algorithms → SQL → data engineering → lakehouse → distributed systems → ML/DL → transformers → embeddings → RAG → inference → GPU → evaluation → observability → security → research → open source → portfolio → resume → interviews → orchestration → CI/CD → feature stores → catalogs → cost management) |
| `exercises/` | Practice problems (Python, algorithms, SQL, data engineering, ML) |
| `projects/` | Full projects: vector search, RAG pipeline, distributed data pipeline, Spark query engine, LLM inference server |
| `research/` | Paper notes and references (Transformers, BERT, GPT-3, LLaMA, RAG, FAISS, HNSW) |
| `career/` | GitHub, portfolio, resume, LinkedIn, networking, interview, salary negotiation |
| `docs/` | Additional documentation |
| `notebooks/` | Jupyter notebooks for experiments |
| `benchmarks/` | Benchmark configs and results |
| `diagrams/` | Architecture and flow diagrams |
| `ci_cd_templates/` | CI/CD pipeline templates |
| `k8s_manifests/` | Kubernetes manifests for deployment |

---

## How to Use This Handbook

1. **Start with the roadmap** — Open **`book/00_master_roadmap.md`** for the full learning path and phase overview.
2. **Follow phases or jump to topics** — Work through phases in order, or go directly to a topic (e.g. RAG, orchestration, vector DBs); each phase has its own chapters where applicable.
3. **Reinforce with exercises** — Use **`exercises/`** (Python, algorithms, SQL, data engineering, ML) to practice.
4. **Build portfolio pieces** — Use **`projects/`** for end-to-end projects (vector search engine, RAG pipeline, distributed data pipeline, Spark query engine, LLM inference server).

---

## Learning Roadmap

The **AI Data Engineer Gita** roadmap in `book/00_master_roadmap.md` outlines 27 phases:

- **01–06:** Foundations (Python, algorithms, SQL & query engines, data engineering systems, data storage & lakehouse, distributed systems)
- **07–09:** ML/DL and transformers (machine learning foundations, deep learning, transformers & LLM core)
- **10–12:** AI stack (embeddings & vector databases, RAG systems, AI infrastructure & inference)
- **13–16:** Systems and quality (GPU systems, evaluation, observability, AI security & compliance)
- **17–22:** Research, open source, portfolio, resume, interviews, salary negotiation
- **23–27:** Production (orchestration & workflow ops, CI/CD & GitOps, feature stores & dataset versioning, data catalogs & governance, cost & resource management)

---

## Projects

| Project | Description |
|---------|-------------|
| [vector_search_engine](projects/vector_search_engine/) | Build a vector search engine with embeddings and ANN (e.g. FAISS, HNSW) |
| [rag_pipeline](projects/rag_pipeline/) | Document ingestion, chunking, embeddings, retrieval, and LLM generation |
| [distributed_data_pipeline](projects/distributed_data_pipeline/) | Distributed data pipeline (e.g. Spark, Kafka, Flink) |
| [spark_query_engine](projects/spark_query_engine/) | Spark SQL over lakehouse storage |
| [llm_inference_server](projects/llm_inference_server/) | LLM serving with batching, streaming, observability (e.g. vLLM, Ray Serve) |

---

## Contributing

See **[CONTRIBUTING.md](CONTRIBUTING.md)** for how to contribute (typos, new chapters, exercises, projects, research notes).

---

## License

See [LICENSE](LICENSE).

---

**Repository description (for GitHub):**  
*AI Data Engineer Handbook — The AI Data Engineer Gita. A complete roadmap for mastering AI data engineering, LLM infrastructure, RAG pipelines, vector databases, distributed systems and production AI platforms.*
