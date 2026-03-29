# Unit 1: Deployment Architecture

## 1. Deployment Model

- **Classification**: Local Node Scripting.
- **Deployment Mechanics**: The physical code will reside within the Git repository structure under `src/simulator/`. Deployment simply requires a `git clone` to the host execution machine followed by Python `venv` initialization.

## 2. Interaction Topology

The physical interaction map connecting local infrastructure to the Cloud boundary:

1. `Host Memory [Pandas/Faker]` → Generates Batches
2. `Host Disk [Local File System]` → Stores `data/staged/*.parquet`
3. `Host Terminal [AWS CLI]` → Invokes `s3 sync` utilizing Terraform-injected IAM Keys.
4. `AWS Edge [IAM/S3]` → Authenticates identity and drops Parquet files into the target Raw Lakehouse zone.

