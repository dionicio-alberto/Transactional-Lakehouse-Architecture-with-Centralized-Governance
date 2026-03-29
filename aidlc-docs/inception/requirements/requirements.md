# Requirements Document

## Intent Analysis Summary

- **User Request**: "Transactional Lakehouse Architecture with Centralized Governance (AWS & Apache Iceberg)"
- **Request Type**: New Project (Greenfield)
- **Scope Estimate**: System-wide
- **Complexity Estimate**: Complex

## Project Overview

Design and implement a secure, scalable data lakehouse to centralize the financial and transactional history of a simulated investment platform. The system guarantees ACID transactions, data versioning (time travel), and strict regulatory compliance through granular security policies using AWS and Apache Iceberg.

## Target Audience / Users (Simulated Personas)

- DataAdmin
- FinancialAnalyst
- LatamAnalyst

## Technology Stack

- Python
- PySpark
- Terraform (IaC)
- AWS (S3, Glue, Lake Formation, Athena, IAM)
- Apache Iceberg
- GitHub Actions & MkDocs

## Functional Requirements

1. **Data Simulation (Incremental)**: Generate initial and incremental batches of Users (synthetic PII) and Transactions datasets, dividing the 40+ years of Kaggle Apple Stock Dataset (AAPL) into periodic slices (e.g., Annual/Monthly) to simulate realistic ETL loads.
2. **Storage Strategy**: Data must traverse three Amazon S3 layers: `raw-zone`, `curated-zone`, and `athena-query-results`.
3. **ETL Processing (Incremental)**: Use AWS Glue job and PySpark to process raw dataset batches incrementally into Apache Iceberg format using `MERGE INTO` or ACID appends. Data must reside in the curated-zone with logical partitioning (e.g., year/month).
4. **Continuous Deployment & Documentation**: Publish technical documentation via CI/CD using MkDocs and GitHub Actions to the `gh-pages` branch.
5. **Validation Testing**: Execute queries via Athena to validate row/column-level and masked data visualizations.

## Non-Functional Requirements & Extensions

- **Infrastructure as Code**: The entire architecture must be deployed using Terraform.
- **Performance**: Use Apache Iceberg logical partitioning to optimize Athena query performance.
- **Security Baseline (Enforced)**: Strict adherence to SECURITY-01 through SECURITY-15.
- **Property-Based Testing (Enforced)**: Strict adherence to PBT-01 through PBT-10.
- **Centralized Governance & Least Privilege**:
  - Implement LF-Tags representing ontology-based security.
  - Revoke default IAM public access in Lake Formation.
  - Set Least Privilege IAM roles (DataAdmin, FinancialAnalyst, LatamAnalyst).
- **Data Filtering & Masking Policies**:
  - Dynamic Data Masking (FinancialAnalyst): Mask SSNs.
  - Row-Level Security (LatamAnalyst): Only query LATAM country transactions.
  - Column-Level Security: Restrict non-privileged access to the Email column.
