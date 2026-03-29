# Unit 1: Infrastructure Design mapping

## 1. Compute Infrastructure

- **Environment Setting**: Developer Workstation / Local Machine.
- **Provider Map**: N/A (No AWS Compute instantiated).
- **Execution Strategy**: The Python simulation script will execute ad-hoc on the developer machine to bootstrap the Lakehouse architecture. There will be no continuous integration runner or EC2 deployment bound to the generator logic.

## 2. Storage Integration (AWS S3)

- **Interaction Pattern**: Out-Of-Band (OOB).
- **Tooling Selection**: `aws s3 sync data/staged/ s3://[raw-zone-bucket]/`
- **Design Rationale**: The simulator Python code will be kept completely decoupled from the AWS API (`boto3`). Data is explicitly dumped to the `data/staged` drive sector natively. Transfer execution to the `raw-zone` bucket is abstracted to a terminal level user interaction.

## 3. IAM and Access Control

- **Identity Provisioning Unit**: The IAM scaffolding will be deferred entirely to **Unit 2 (Terraform)**.
- **Security Posture**: The user running the `aws s3 sync` CLI command MUST use short-lived credentials or Access Keys tied to a dedicated programmatic IAM User generated explicitly by Terraform for this purpose. The IAM Policy mapped to this role restricts access solely to `s3:PutObject` bounds mapped to the exact Data Lake raw-zone bucket ARN.
