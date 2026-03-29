# Component Methods (High-Level)

## 1. Data Simulator Module
### `generate_users_dataset(output_path, num_users)`
- **Purpose**: Generates synthetic PII strings.
- **Output**: Writes `users.csv` to disk.

### `generate_transactions_dataset(stock_data_path, users_path)`
- **Purpose**: Joins random user IDs with parsed AAPL stock data.
- **Output**: Writes `transactions.csv` to disk.

## 2. IaC Security Binding Methods (Terraform)
### `aws_lakeformation_lf_tag`
- **Purpose**: Defines the ontology of tags (e.g., `Category: Confidential`, `Geography: LATAM`).

### `aws_lakeformation_permissions`
- **Purpose**: Maps DataAdmin, FinancialAnalyst, and LatamAnalyst IAM Roles to the LF-Tags.

## 3. Data Transformation Module (PySpark)
### `process_lakehouse_data(glueContext, raw_s3_path, curated_s3_path)`
- **Purpose**: Reads disparate raw files, casts schema properly, and writes the PySpark DynamicFrame explicitly to an Iceberg target.

### `apply_lf_tags_to_tables(glue_client, database_name, table_name, tags_dict)`
- **Purpose**: Uses Boto3 AWS API calls immediately following the Spark write to automatically bind LF-Tags directly onto the resulting Data Catalog tables, fulfilling the "Self-Tagging" routing strategy.
