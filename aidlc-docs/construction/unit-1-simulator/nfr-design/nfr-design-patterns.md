# Unit 1: NFR Design Patterns

## 1. Performance Optimization Patterns

- **Vectorization over Iteration**: To guarantee execution within the tight 5-minute constraint for 40 years of daily data coupled to 1,000 distinct users, the design strictly bans standard Python `for-loops` for trade assignment.
- **Implementation**: The script leverages Pandas and Numpy native vectorized functions (e.g., `pd.merge()`, `np.random.choice`, `df.apply()`) to execute transformations and join operations simultaneously across the entire array structure in C-optimized memory.

## 2. Resilience and Memory Management Patterns

- **Chunk-And-Flush Pattern**: 40+ years of dense financial transactions expanded across dummy users introduces severe memory scaling risks (bloat).
- **Implementation**: The simulation is chronologically partitioned into explicit loops (an initial 20-year chunk, followed by 20 subsequent incremental yearly chunks). During each loop cycle, the memory array is processed, immediately written to the disk as Parquet, and then forcibly purged from RAM using explicit Garbage Collection hooks (`del batch_df`, `gc.collect()`). This guarantees the memory profile stays flat and eliminates Out-Of-Memory (OOM) failures entirely.
