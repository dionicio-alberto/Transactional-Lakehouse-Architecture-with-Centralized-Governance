# NFR Requirements Plan - Unit 2 (IaC/Terraform Module)

## Execution Sequence
- [x] **Step 1: Scalability & Storage Performance**
  - Define S3 lifecycle rules and scale vectors.
- [x] **Step 2: Availability & Threat Modeling**
  - Define replication requirements and disaster recovery posture.
- [x] **Step 3: Security & Encryption**
  - Define KMS boundaries and Access Logging logic.

## Clarification Questions
> Please answer the following NFR business questions to finalize the architectural constraints.

**Q1. For Scalability, should the IaC be designed to support multi-account deployments (e.g., using Terraform workspaces for dev/prod scaling) or is this strictly a single-account greenfield setup?** 
[Answer]: multiaccount 

**Q2. For Storage Performance, does the S3 configuration require explicit lifecycle expiration rules to save storage costs (e.g., delete raw objects after 90 days), or will raw data persist indefinitely?**
[Answer]: raw data persist indefinitely

**Q3. For Availability, should the S3 buckets enforce Cross-Region Replication for disaster recovery, or is standard Single-Region durability sufficient?**
[Answer]: standard Single-Region durability sufficient


**Q4. For Security/Encryption, do we require AWS KMS Customer Managed Keys (CMK) for absolute dataset encryption, or is the free SSE-S3 default encryption acceptable?**
[Answer]: sse-s3 

**Q5. For Security/Audit, do the S3 buckets require exact Server Access Logging enabled and forwarded to a distinct centralized audit bucket?**
[Answer]: no
