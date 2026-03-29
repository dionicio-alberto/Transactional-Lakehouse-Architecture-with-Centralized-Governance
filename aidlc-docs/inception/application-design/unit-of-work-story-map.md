# Unit of Work Story Map

This document maps the project user stories to the specific units of work responsible for their implementation.

| Story ID | Story Title | Primary Unit | Supporting Unit |
| :--- | :--- | :--- | :--- |
| **Story 1** | DataAdmin Unrestricted Oversight | **Unit 2 (IAM/LF)** | **Unit 3 (Tagging)** |
| **Story 2** | FinancialAnalyst Data Masking | **Unit 3 (ETL/Tagging)** | **Unit 2 (LF Policies)** |
| **Story 3** | LatamAnalyst Row/Column Security | **Unit 3 (ETL/Tagging)** | **Unit 2 (LF Policies)** |
| **Story 4** | Automated Data Ingestion | **Unit 1 (Simulator)** | **Unit 2 (S3)** |
| **Story 5** | Iceberg Transformation ETL | **Unit 3 (PySpark)** | **Unit 2 (Glue/S3)** |

## Coverage Verification
- [x] All stories from `stories.md` are mapped.
- [x] Security-specific persona requirements are covered by Unit 2 and Unit 3.
- [x] Data processing requirements are covered by Unit 1 and Unit 3.
