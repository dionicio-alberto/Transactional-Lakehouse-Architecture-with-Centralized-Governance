# Performance Test Instructions - Unit 1

## Purpose
Validate Python Pandas logic vectorizations keep total chronological executions tightly mapped beneath the explicit constraints (< 5 minutes total run-time).

## Performance Requirements
- **Execution Target Time**: `< 300` seconds for an entire 1980 - 2026 backfill cycle.
- **Memory Consumption Constraint**: `< 1.2` Gigabytes peak resident RAM (achieved exclusively via the chunk-and-flush execution mapped onto 20 partition arrays).
- **Throughput Bounds**: ~N interactions matched smoothly onto Kaggle dataset matrices.

## Setup & Execution
1. Purge `venv` and re-init cleanly.
2. Ensure you invoke Unix `time` wrapper or equivalent bash memory tracers on execution:
```bash
time python src/simulator/main.py
```
3. Read the STDOUT wall clock timestamp. If > 5m, Python generation has missed execution parameters.
