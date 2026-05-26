# Diagrams

This folder contains architecture and flow diagrams that make complex topics easy to understand visually.

## What to Add Here

- data pipeline architectures
- lakehouse table flow diagrams
- RAG request lifecycle
- model serving and inference paths
- observability and incident workflows

## Suggested Naming

- `pipeline_batch_vs_streaming.mmd`
- `rag_end_to_end.mmd`
- `inference_server_request_flow.mmd`
- `feature_store_offline_online.mmd`

## Diagram Rule

Every major project and advanced chapter should include at least one diagram showing:

1. components
2. data flow direction
3. failure/retry points
4. scaling bottlenecks

Starter diagram added:

- `rag_end_to_end.mmd`
- `batch_vs_streaming_pipeline.mmd`
- `lakehouse_data_flow.mmd`
- `inference_request_flow.mmd`

## Starter Mermaid Example

```mermaid
flowchart LR
    A[Source] --> B[Ingestion]
    B --> C[Storage]
    C --> D[Transform]
    D --> E[Serving]
    E --> F[Monitoring]
```
