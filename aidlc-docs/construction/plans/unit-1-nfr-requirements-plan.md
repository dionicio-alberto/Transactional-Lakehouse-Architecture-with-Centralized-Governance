# NFR Requirements Plan - Unit 1 (Python Data Simulator)

## Objective
Define the Non-Functional Requirements (NFRs) including performance, scalability, security, and technology stack selection for the Python Data Simulator module.

## Execution Steps

- [x] Assess Scalability and Performance Requirements (Data generation speed)
- [x] Evaluate Security Requirements (Local file handling)
- [x] Decide Tech Stack specifics (Data processing and Parquet engines)
- [x] Establish Reliability and Logging conventions

## Clarification Questions
Before proceeding to generate the NFR documentation, please answer the following questions to finalize the system's technical profile:

**Q1: Performance & Scalability (Execution Time)**
The simulator will cross 1,000 synthetic users with 40+ years of daily Apple stock volumes to generate transactions. Do you have a strict execution time constraint for this simulation script (e.g., must complete in under 5 minutes)? Should we implement multiprocessing, or is a simpler sequential process acceptable?
`[Answer]:`  must complete in under 5 minutes 

**Q2: Tech Stack Selection (Processing Engine)**
We need to generate strictly compressed Parquet files. To process the data frames and write these files locally before uploading to AWS, do you prefer using lightweight `pandas` (with `pyarrow`) or should we use local `pyspark` to keep the ecosystem consistent with Unit 3?
`[Answer]:`using pandas

**Q3: Security Requirements (Local Data Handling)**
Although these files mock PII (SSNs, Emails), they are synthetic. Should the local raw files have any form of file-level encryption before upload, or will we rely entirely on AWS Server-Side Encryption (SSE-S3/KMS) once the files land in the `raw-zone`?
`[Answer]:`  we rely entirely on AWS Server-Side Encryption (SSE-S3/KMS) once the files land in the `raw-zone

**Q4: Reliability & Maintainability (Logging)**
How should we track the progress of the batch generations (especially distinguishing between the 20-year bulk load and the subsequent 20 incremental yearly loads)? Is standard Python console logging sufficient, or do you need a dedicated local log file/run report output?
`[Answer]:`  standard Python console logging sufficient
