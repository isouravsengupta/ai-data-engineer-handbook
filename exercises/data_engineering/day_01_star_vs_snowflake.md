# Day 01 - Star vs Snowflake Modeling

## Goal

Explain and compare Star vs Snowflake schema for analytics use-cases as if in an interview.

## Deliverable (30-40 min)

Write a one-page answer including:

- business scenario (example: e-commerce orders analytics)
- fact table and dimension tables
- Star model design and why
- Snowflake model design and why
- query performance trade-offs
- storage and maintainability trade-offs
- when you would choose each in BigQuery

## Interview Prompt

"You have to design a data model for an enterprise reporting system with high query volume. Would you choose Star or Snowflake and why?"

Answer framework:

1. Clarify workload (BI dashboards vs ad hoc exploration)
2. Explain both options
3. Pick one with trade-offs
4. Mention partitioning/clustering impacts
5. Mention cost/performance in cloud warehouse context
