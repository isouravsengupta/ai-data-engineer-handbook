# RAG Pipeline

End-to-end project: document ingestion, chunking, embeddings, retrieval, and LLM generation.

## Variants

1. **Minimal (custom)** — Build from scratch with raw OpenAI API, embeddings, and a vector store. Best for understanding internals.
2. **LangChain** — Use `create_retrieval_chain` and LCEL. See `book/11_rag_systems/orchestration_frameworks.md`.
3. **LlamaIndex** — Use `VectorStoreIndex` and `as_query_engine`. See `book/11_rag_systems/orchestration_frameworks.md`.

## Theory

* `book/11_rag_systems/` — RAG architecture, chunking, hybrid search, agentic RAG
* `book/11_rag_systems/orchestration_frameworks.md` — LangChain vs LlamaIndex vs custom
