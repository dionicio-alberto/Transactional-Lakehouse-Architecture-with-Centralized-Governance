# Application Components

## 1. Data Simulator Module

- **Purpose**: Generates high-fidelity synthetic User PII and Transactional data, mocking real-world financial records.
- **Responsibilities**:
  - Creates synthetic users with assigned geographies (e.g., LATAM).
  - Crosses Apple Stock (AAPL) kaggle data with synthetic users to generate a transaction history.
  - Supports incremental batching by dividing the dataset into "charges" (e.g., temporal or size-based slices).
  - Outputs CSV/Parquet files locally, organized by batch/charge.
- **Interface**: Executed locally via CLI. Requires `python` and `faker`/`pandas`.

## 2. Infrastructure as Code (IaC) Module

- **Purpose**: Defines, provisions, and manages all AWS resources required for the Lakehouse architecture.
- **Responsibilities**:
  - Provisions S3 buckets (`raw-zone`, `curated-zone`, `athena-query-results`).
  - Provisions Glue Catalog Databases and IAM Roles.
  - Provisions Lake Formation Data Lake Settings, Permissions, and LF-Tags (taxonomy definition only).
  - Provisions AWS Step Functions / Glue Workflows for orchestration.
- **Interface**: Executed via Terraform CLI (`terraform apply`).

## 3. Data Transformation Module (ETL)

- **Purpose**: Processes raw data into optimized, partitioned Apache Iceberg tables.
- **Responsibilities**:
  - Reads data from the `raw-zone` (identifying new/incremental batches).
  - Joins and transforms user and transaction data.
  - Performs incremental updates (UPSERT/APPEND) to Apache Iceberg partitioned data in the `curated-zone`.
  - Programmatically interacts with the Boto3 Lake Formation API to dynamically bind LF-Tags and Column-Level Security configurations to the resulting schema.
- **Interface**: PySpark AWS Glue Job orchestrated via AWS Step Functions/Glue Workflow.
