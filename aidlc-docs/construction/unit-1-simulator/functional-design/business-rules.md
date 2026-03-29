# Unit 1: Business Rules & Constraints

## 1. Batch Constraint Rules

- **Total Historical Scope**: Approximately 40+ years of data.
- **Bulk Load Initialization**: The initial parquet file MUST contain exactly the first 20 chronological years of the dataset.
- **Incremental Distribution**: Data after the initial 20 years MUST be chunked chronologically into 20 distinct batches, representing 1 year of data each.
- **File Format**: The output format MUST be strictly compressed Parquet (e.g., using Snappy compression). CSV format is not permitted.

## 2. PII / Demographic Rules

- **User Volume Limit**: The system MUST generate exactly 1,000 distinct users.
- **Geographic Distribution Bias**:
  - The geographic assignment relies on random spreading constraints.
  - At least 30% (i.e., >= 300) of the users MUST be distinctly assigned to the following LATAM countries: Mexico (`MX`), Brazil (`BR`), Argentina (`AR`), and Colombia (`CO`).
  - This ensures that when the `LatamAnalyst` role queries the Lakehouse, a significant portion of the data is verifiable via Row-Level Security filters.
