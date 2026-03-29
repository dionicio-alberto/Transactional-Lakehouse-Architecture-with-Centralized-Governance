# Business Logic Summary - Unit 1 (Simulator)

## Architecture Overview
The simulator employs exclusively native Pandas vectorizations to generate robust testing boundaries mapped upon physical Kaggle CSV transaction values. No `for-loops` are enacted over large data rows.

- **Orchestration**: `main.py` explicitly cycles a historical back-fill (1980 - 2000), followed iteratively by single-year increments down to 2026. Explicit Garbage Collection boundaries execute tightly tied to these discrete steps.
- **Generator Core**: `generator.py` utilizes PyArrow to bind Snappy Parquet compression to disk paths enforcing explicit local limits (`data/staged/*.parquet`). Geo-mapping uses weighted Faker assignments to rigorously ensure the exact >30% LATAM geo-requirements.

## Testing Integrity
All Python bindings were secured leveraging **Property-Based Testing**. The custom `test_generator.py` implementation iterates random target bounds testing execution limits (e.g. integer 100 up to integer 5000 random generation targets) and independently verifies if array schemas or geographic thresholds falter underneath unexpected permutations logic vectors.
