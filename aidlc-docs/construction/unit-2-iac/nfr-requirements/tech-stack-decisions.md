# Tech Stack Decisions - Unit 2 (IaC/Terraform Module)

## Core Declarative Language
- **Terraform (HCL)**: Selected natively as the core IaC provider overriding AWS CDK due to strictly mandated dynamic multi-account parameterizations seamlessly handled via Terraform Workspaces (`terraform workspace new dev`). 

## Storage & Encryption Strategy
- **Amazon S3 Standard**: Selected primarily as the transactional data ingestion landing layer (`raw`) directly receiving `pyarrow` Snappy `.parquet` output vectors.
- **SSE-S3 Native Encryption**: Selected over AWS KMS limits ensuring zero-overhead encryption without latency blockages. AWS formally encrypts S3 objects securely by default.

## Auditing Frameworks
- **AWS CloudTrail & Lake Formation Logging**: Implemented securely handling data mesh auditing without physically spinning up legacy `S3 Server Access Logging` buckets, radically reducing Terraform state scope while preserving user activity visibility natively mapping SQL queries inside internal Athena/Glue limits.
