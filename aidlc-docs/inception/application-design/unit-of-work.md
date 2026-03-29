# Unit of Work Definitions

This document defines the discrete units of work for the Construction phase, following a Technology-Based Partitioning strategy.

## Unit 1: Python Data Simulator
- **Type**: Local Module
- **Responsibilities**:
  - Generate synthetic user PII (names, SSNs, emails, countries).
  - Cross-reference with Apple Stock (AAPL) historical data.
  - Produce raw CSV/Parquet files for the `raw-zone`.
- **Primary Source Location**: `/src/simulator/`
- **Output**: Local data files to be uploaded to S3.

## Unit 2: Terraform Infrastructure
- **Type**: Infrastructure Service
- **Responsibilities**:
  - Provision S3 Buckets (`raw`, `curated`, `athena-results`).
  - Provision Glue Catalog Database and IAM Roles for personas.
  - Configure Lake Formation settings (Admins, LF-Tags taxonomy).
  - Orchestration setup (Step Functions / Glue Workflows).
- **Primary Source Location**: `/infra/terraform/`
- **Output**: Cloud environment ready for data processing and governance.

## Unit 3: PySpark ETL & Security Governance
- **Type**: ETL Service / Governance Module
- **Responsibilities**:
  - Transform raw data into Apache Iceberg format in the `curated-zone`.
  - Apply logical partitioning by year/month.
  - Self-tagging: Dynamically bind LF-Tags onto Glue tables using Boto3 within the Glue Job.
  - Implement Row-Level and Column-Level security and data masking logic.
- **Primary Source Location**: `/src/etl/`
- **Output**: Secured, queryable Iceberg tables in the Lakehouse.

## Code Organization Strategy
As a Greenfield project, the repository will follow a source-grouped structure:
- `/src/`: Contains all application logic.
  - `/src/simulator/`: Python Data Simulator scripts.
  - `/src/etl/`: PySpark Glue scripts and Boto3 security binding logic.
- `/infra/`: Contains all infrastructure definitions.
  - `/infra/terraform/`: Terraform modules and environment configurations.
- `/docs/`: MkDocs technical documentation source.
