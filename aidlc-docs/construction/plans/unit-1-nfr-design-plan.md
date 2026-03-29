# NFR Design Plan - Unit 1 (Python Data Simulator)

## Objective
Translate the Non-Functional Requirements (NFRs) into concrete design patterns and logical components for the Data Simulator. This ensures the script is performant, resilient against memory limits, and structured correctly for local staging.

## Execution Steps

- [x] Define Performance Optimization Patterns (Vectorization vs Parallelism)
- [x] Define Resilience Patterns (Memory management and bulk chunking)
- [x] Define Logical Components (Local directory handling and data flow)

## Clarification Questions
Before generating the NFR design documentation, please answer the following questions to confirm the tactical patterns:

**Q1: Performance Patterns (Execution Paradigm)**
To guarantee the `< 5 minutes` execution constraint in Pandas, should the primary optimization strategy heavily rely on Pandas/Numpy **vectorized operations** (avoiding `for-loops` entirely during the trade assignments), or should it utilize Python's **`multiprocessing.Pool`** to parallelize the processing of the 20 batch years?
`[Answer]:` the primary optimization strategy heavily rely on Pandas/Numpy **vectorized operations** (avoiding `for-loops` entirely during the trade assignments)

**Q2: Resilience Patterns (Memory Management)**
Simulating 40+ years of transactional data can cause memory bloat. Do you approve a "chunk-and-flush" pattern where the script processes one chronological batch in memory completely, writes it to Parquet, and then calls explicit garbage collection (`del df`, `gc.collect()`) before moving to the next batch to permanently avoid Out-Of-Memory (OOM) errors?
`[Answer]:` yes, i approved it

**Q3: Logical Components (Local Staging Directory)**
The parquet files must be written locally before any AWS upload. Should the design enforce a specific local directory structure like `data/staged/user_batch.parquet` and `data/staged/transactions/batch_YYYY.parquet`?
`[Answer]:` data/staged/transactions/batch_YYYY.parquet`
