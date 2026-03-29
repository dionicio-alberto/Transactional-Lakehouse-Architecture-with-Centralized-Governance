# User Stories

## Epic 1: Centralized Governance & Data Access (Persona-Based)

These stories are organized primarily by the personas and reflect the high-level security constraints (Row-Level Security, Column-Level Security, Dynamic Data Masking) defined by Lake Formation.

### Story 1: DataAdmin Unrestricted Oversight
**As the DataAdmin**, I need unrestricted access to all tables in the lakehouse **so that** I can configure, audit, and troubleshoot the data platform without artificial limitations.

**Acceptance Criteria**:
- Given the DataAdmin role is active, when they query the `Users` or `Transactions` table, they can see all columns and all rows unmodified.

### Story 2: FinancialAnalyst Data Masking
**As the FinancialAnalyst**, I need access to all transactional and user records while protecting sensitive PII **so that** I can perform comprehensive financial analysis globally without violating privacy laws.

**Acceptance Criteria**:
- Given the FinancialAnalyst role is active, when they query the `Users` table, the SSN column is masked (e.g., `XXX-XX-####`).
- The role must be able to view all rows (no Row-Level Security applied).

### Story 3: LatamAnalyst Regional Row & Column Security
**As the LatamAnalyst**, I need to view transaction details strictly for my geographic region, and I must not see extraneous private details like emails **so that** my reporting complies with regional data sovereignty and "least privilege" principles.

**Acceptance Criteria**:
- Given the LatamAnalyst role is active, when they query the joined `Users` and `Transactions` table, they only see rows where the user country belongs to Latin America (Row-Level Security).
- When they attempt to select the `email` column, it returns null or throws a permission error (Column-Level Security).

---

## Epic 2: Data Pipeline & Processing Operations

### Story 4: Automated Data Ingestion
**As the DataAdmin**, I need the capability to systematically ingest real stock data and synthetic PII into the `raw-zone` bucket **so that** there is a reliable dataset ready for the ETL pipeline.

**Acceptance Criteria**:
- A script provisions random PII (Names, SSN, Emails, Country) crossing it against Apple Stock historical facts.
- The datasets successfully reside in S3 `raw-zone`.

### Story 5: Iceberg Transformation ETL
**As the DataAdmin**, I need a PySpark Glue Job to transform the raw ingested data into the Apache Iceberg format in the `curated-zone` **so that** it benefits from ACID transactions, logical partitioning by year/month, and rapid scan times in S3.

**Acceptance Criteria**:
- A Glue 4.0+ job runs successfully.
- The output in the `curated-zone` is registered in the Glue Data Catalog as Iceberg tables and partitioned by year/month.
