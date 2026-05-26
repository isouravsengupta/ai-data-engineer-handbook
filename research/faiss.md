# FAISS

## Why It Matters

FAISS is a core library for efficient nearest-neighbor search on large embedding datasets.

## Core Ideas

- vector indexing strategies (flat, IVF, PQ, HNSW variants)
- approximate nearest-neighbor search
- CPU/GPU acceleration

## Engineering Takeaways

- choose index type by recall/latency/memory needs
- benchmark with real embedding distributions
- critical for semantic search and RAG retrieval layers
