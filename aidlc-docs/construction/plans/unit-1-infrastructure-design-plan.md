# Infrastructure Design Plan - Unit 1 (Python Data Simulator)

## Objective
Map the logical and NFR components of the Data Simulator to actual execution environments and AWS infrastructure integration points (S3 bucket, IAM roles).

## Execution Steps

- [x] Map Compute Infrastructure (where the simulator runs)
- [x] Map Storage Integration (how files are moved to S3)
- [x] Map IAM & Authentication (how the simulator authorizes against AWS)

## Clarification Questions
Before generating the Infrastructure Design documentation, please answer the following questions to solidify the integration with AWS:

**Q1: Compute Environment (Execution context)**
Unit 1 is a Python script that writes Parquet files to `data/staged/`. In the final state, is this script intended to just run locally on your developer machine (to bootstrap the Lakehouse once), or should it be deployed to an AWS compute service (e.g., an EC2 instance, AWS Lambda, or Jenkins/GitHub Actions runner) to run repeatedly?
`[Answer]:` local machinne 

**Q2: Storage Infrastructure (Target AWS S3)**
Once the script generates the incremental Parquet batches in `data/staged/`, how should they interact with the AWS `raw-zone`? Should the Python script natively include a `boto3.client('s3').upload_file()` step to automatically push them, or will you just use `aws s3 sync` via terminal outside of the script's boundaries?
`[Answer]:` manually via terminal

**Q3: IAM Authentication Strategy**
For the script (or CLI sync) to successfully deposit files into the `raw-zone` S3 bucket, it needs AWS permissions. Should we assume it will run using an existing configured `AWS_PROFILE` on the host machine, or should the Terraform architecture (Unit 2) explicitly create a dedicated IAM User/Role containing strictly locked `s3:PutObject` permissions for the simulator?
`[Answer]:` using terraform architecture
