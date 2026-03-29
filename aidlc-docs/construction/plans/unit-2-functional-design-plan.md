# Functional Design Plan - Unit 2 (IaC/Terraform Module)

## Purpose
This defines the domain mapping, business workflows, and logical abstractions for Unit 2: the Data Lake infrastructure provisioning. Although Infrastructure is usually technical, the Functional Design stage establishes the *business rules, permissions, taxonomies, and access parameters* that the IaC will ultimately enforce.

---

## Execution Sequence

- [ ] **Step 1: Domain Mapping**
  - Define logical boundaries for `raw-zone`, `curated-zone`, and the metadata catalogs.
- [ ] **Step 2: Taxonomy & Security Rules (Lake Formation)**
  - Map explicit Business Personas to Data Access boundaries.
  - Define logical Tagging schemas (e.g., `classification: pii`, `geography: latam`).
- [ ] **Step 3: Workflow Mapping**
  - Define orchestration rules connecting S3 ingestion to ETL triggers.

---

## Clarification Questions
> Please answer the following functional business questions to finalize the design constraints.

**Q1. What is the explicit naming convention policy for the core logical business buckets (Raw, Curated, Athena)? Do they require a prefix aligned to a specific business unit or environment?**
[Answer]: 

**Q2. Our User Stories identified an `LatamAnalyst` and a `FinancialAnalyst`. Do these personas map directly to existing AWS IAM SSO Identity Center Roles, or should the design create localized programmatic IAM logical definitions?**
[Answer]: 

**Q3. For the Lake Formation taxonomy, should we functionally segment the tables strictly by Geography (i.e., ROW-Level Security), or do we also need explicit Column-Level Security (e.g., masking the synthetic `ssn` field we created in Unit 1)?**
[Answer]: 

**Q4. Does the business logic dictate that raw data landing in S3 automatically triggers the ETL PySpark jobs, or is it a scheduled batch orchestration (e.g., Nightly at 12:00 AM)?**
[Answer]: 
