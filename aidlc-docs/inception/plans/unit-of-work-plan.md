# Unit of Work Plan

## Phase 1: Planning and Context
- [ ] Present this plan and gather answers to the decomposition questions.
- [ ] Analyze answers for ambiguity.

## Phase 2: Generation
- [ ] Generate `aidlc-docs/inception/application-design/unit-of-work.md` with unit definitions, responsibilities, and code organization strategy.
- [ ] Generate `aidlc-docs/inception/application-design/unit-of-work-dependency.md` displaying the dependency matrix between these units.
- [ ] Generate `aidlc-docs/inception/application-design/unit-of-work-story-map.md` mapping the existing 5 user stories to their executing units.

---

# Clarification Questions

Please answer the following questions to outline how we will break this project down for the Construction (Coding) phase.

## Question 1: Unit of Work Boundary Strategy
How should we group the application components into distinct Units of Work? Each unit will be designed and built sequentially in the Construction phase.

A) Technology-Based Partitioning: 
   - Unit 1: Python Data Simulator (Local)
   - Unit 2: Terraform Infrastructure provisioning
   - Unit 3: PySpark ETL & Security tags

B) Feature-Based Partitioning: 
   - Unit 1: Data Ingestion Pipeline (Simulator + S3 IaC)
   - Unit 2: ETL Transformation (Glue IaC + PySpark)
   - Unit 3: Centralized Governance (Lake Formation/IAM IaC + Boto3 tag bindings)

X) Other (please specify after [Answer]: tag)

[Answer]: A

## Question 2: Code Organization Strategy
Since this is a Greenfield project, how should we layout the code repository physically for these units?

A) Monorepo with isolated top-level directories: `/simulator`, `/terraform`, `/etl`.
B) Source-grouped structure: `/src` (for both Simulator and PySpark scripts), `/infra` (for Terraform modules).
X) Other (please specify)

[Answer]: B
