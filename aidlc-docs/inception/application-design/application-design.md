# Application Design Master Document

Contains the complete boundary mapping for the Data Simulation, Transformation, and Governance components.

## 📌 Application Components
Refer to [components.md](./components.md) for full mapping. The Core boundary consists of:
- **Data Simulator Module** (Python CLI)
- **Infrastructure as Code (IaC) Module** (Terraform)
- **Data Transformation Module** (PySpark & Boto3 LF-Tagging)

## 📌 Service Layer
Refer to [services.md](./services.md) for full mapping.
- Orchestration: Step Functions
- Storage: Amazon S3
- Governance: Lake Formation + IAM
- Transformation: AWS Glue Spark Serverless
- Query Layer: Athena

## 📌 Methods & Signatures
Refer to [component-methods.md](./component-methods.md) for full mapping.

## 📌 Provisioning Flow
Refer to [component-dependency.md](./component-dependency.md) for full mapping. Critical focus on provisioning IAM and LF-Tags *prior* to Catalog Database assignments via Terraform dependency graph (`depends_on`).
