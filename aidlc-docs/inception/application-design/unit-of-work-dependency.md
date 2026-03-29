# Unit of Work Dependency Matrix

This matrix defines the relationships and execution order between the Units of Work.

| Unit | Depends On | Relationship Type | Reason |
| :--- | :--- | :--- | :--- |
| **Unit 1: Data Simulator** | None | Independent | Can be developed and run locally without AWS. |
| **Unit 2: Infrastructure** | None (Structural) | Foundational | Must exist before data can be uploaded or processed in AWS. |
| **Unit 3: ETL & Governance** | Unit 1, Unit 2 | Operational | Requires raw data (Unit 1) and Glue/S3/LF environment (Unit 2) to execute. |

## Execution Sequence
1. **Unit 1 & Unit 2 (Parallelizable)**: The simulator module and the core Terraform infrastructure can be developed concurrently.
2. **Unit 3**: Depends on both foundation (Unit 2) and data (Unit 1).

## Component Map
- **Unit 2** provides the "Schema Registry" (Lake Formation/Glue) and "Storage" (S3) for **Unit 3**.
- **Unit 1** providing the "Payload" for **Unit 3**.
