# Service Layer Design

The system coordinates several AWS Managed Services organized around a central orchestration workflow.

## 1. Storage Services Layer
- **Amazon S3**: Acts as the physical storage medium, separated strictly by security zones (`raw`, `curated`).

## 2. Orchestration Services Layer
- **AWS Step Functions / AWS Glue Workflow**: Manages the ETL orchestration trigger, tracking job states, failures, and success. Initiates the PySpark ETL execution on demand.

## 3. Transformation Services Layer
- **AWS Glue**: Serverless Spark environment executing the ETL code, inferring schemas, and managing the Hive/Iceberg data catalog interactions natively.

## 4. Governance Services Layer
- **AWS Lake Formation**: Sits on top of the Glue Data Catalog intercepting all queries.
- **AWS IAM**: Provides the identity definitions for our 3 simulated personas.

## 5. Query & Validation Services Layer
- **Amazon Athena**: Serverless interactive query service where the validation screenshot queries will be executed. Athena inherently respects the Lake Formation interception layers, performing Dynamic Data Masking, RLS, and CLS automatically based on the IAM execution role invoking the query.
