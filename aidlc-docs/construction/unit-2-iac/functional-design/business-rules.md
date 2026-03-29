# Business Rules - Unit 2 (IaC/Terraform Module)

## Rule Overview
This document lays out the explicit business constraints dictating how Unit 2's Terraform definitions establish limits securely upon the Data Lake architecture.

---

## 1. Governance Isolation Boundaries (IAM)
### Rule 1.1 - Programmatic Isolation
No production human AWS `Identity Center` federations will be dynamically mapped to analysts. Instead, the Terraform logic must natively instantiate standalone Programmatic `aws_iam_role` definitions acting as the *LatamAnalyst* and *FinancialAnalyst*, isolated securely using unique AssumeRole contexts.
### Rule 1.2 - Data Creator Exclusivity
A specific programmatic IAM Identity uniquely assigned to Unit 1 (Simulator) is physically constrained to `s3:PutObject` strictly to the `raw-zone`. Read access to downstream dependencies is blocked.

## 2. Infrastructure Taxonomy Constraints
### Rule 2.1 - Storage Identification String
S3 bucket instantiation must algorithmically match the user-defined prefix topology:
`layer` - `region` - `account` - `typeofbucket`

*Example:* `raw-us-east-1-123456789012-data`

## 3. Row & Column Security Constraints (Lake Formation)
### Rule 3.1 - Explicit Column-Level Masking
Data Analysts accessing the Curated Lakehouse layer must have explicit column-level filters (CLS) enabled for highly sensitive PII records. For example, queries accessing `users` mock properties must mask/nullify the `ssn` field depending on contextual identity tags interacting.

## 4. Workload Trigger Assertions
### Rule 4.1 - Orchestrated Batch Processing 
Data Pipeline invocations matching Lake Formation transforms are strictly event-blocked at the object level. Trigger paths logic flows exclusively rely on Nightly Schedule Boundaries (`cron(0 0 * * ? *)`) defined inside orchestration templates rather than `ON_PUT` lambdas.
