# Unit 1: NFR Requirements

## 1. Performance and Scalability

- **Execution Time Bound**: The complete execution of the 40+ year simulation (identifying 1,000 users across daily AAPL stock values, chunking into the 20-year bulk batch and 20 subsequent incremental yearly batches) **MUST** complete in under 5 minutes.
- **Scalability Strategy**: Since execution time is strictly bound to under 5 minutes, in-memory vectorization using the selected tech stack is required. Sequential processing is acceptable only if the 5-minute threshold is strictly met; otherwise, basic Python `multiprocessing` must be engaged to divide the historical years.

## 2. Security and Data Protection

- **Data Sensitivity**: The simulated PII data (Names, SSNs, Emails) is synthetic.
- **Encryption at Rest (Local)**: No file-level encryption is required locally before upload.
- **Encryption at Rest (Remote)**: The architecture explicitly delegates encryption responsibilities to AWS Server-Side Encryption (SSE-S3 with AWS KMS) once the raw Parquet batches are deposited into the `raw-zone` S3 bucket.

## 3. Reliability and Maintainability

- **Monitoring Strategy**: The execution flow will utilize standard Python console logging (`logging` module configured to `INFO` level).
- **Log Structure**: The logs must explicitly indicate the start and end of the initialization (20-year bulk load), followed by distinct markers for each of the 20 incremental year loops ensuring progress is easily tracked by a human operator in standard output. Dedicated log files on disk are out of scope.
