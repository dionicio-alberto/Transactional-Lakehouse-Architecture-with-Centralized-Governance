# Unit 1: Tech Stack Decisions

## 1. Local Processing Engine

- **Technology**: Python with `pandas` and `pyarrow`
- **Rationale**: The user explicitly selected `pandas` over local `pyspark`. It is superior for rapid prototyping, lightweight single-machine data frame operations, and efficient memory management (especially when combined with PyArrow). `pandas` avoids the JVM overhead of PySpark while still fulfilling the requirement to output strictly compressed Parquet files natively.

## 2. File Format & Compression

- **Technology**: Apache Parquet (Snappy Compression)
- **Rationale**: The raw-zone will accept serialized columnar Parquet files generated locally via `pandas.to_parquet(engine='pyarrow', compression='snappy')`. This is aligned with the data lake architectural goals of lowering storage size and increasing query speed compared to CSV data dumps.

## 3. Mock Data Generator

- **Technology**: `Faker` (Python Library)
- **Rationale**: Required for high-fidelity synthetic data generation corresponding to Names, ISO Country Codes, SSNs, and Emails for the predefined 1,000 user volume ceiling.

## 4. Execution Modality

- **Technology**: Sequential or `multiprocessing` standard library (Python).
- **Rationale**: Standard library multiprocessing may be utilized explicitly to satisfy the `< 5 minutes` NFR constraint regarding generating and correlating 40+ years of daily stock prices across 1,000 distinct user profiles.
