# NFR Requirements - Unit 2 (IaC/Terraform Module)

## 1. Scalability Requirements
### 1.1 Multi-Account Deployments
The Terraform definitions **must** utilize decoupled architecture patterns (e.g., Terraform Workspaces or parameterized variable blocks) to fully support dynamic multi-account deployments natively (e.g., spinning up isolated `dev` vs `prod` accounts). Greenfield single-account lock-in is strictly rejected.

## 2. Storage & Performance
### 2.1 Object Persistence
The S3 data storage layer will strictly avoid automated deletion bounds. Implicit logical requirements specify that raw transaction payloads dropped by the Unit 1 batch simulator MUST persist indefinitely with zero explicit AWS S3 Lifecycle pruning configurations enabled. 

## 3. Availability Requirements 
### 3.1 Durability Bounds
Disaster recovery capabilities are restricted securely to standard AWS S3 Single-Region durability bounds (99.999999999%). Strict avoidance of explicit Cross-Region Replication (CRR). The S3 provisioning patterns will not define dual-region disaster synchronization.

## 4. Security & Compliance
### 4.1 Encryption Methodology
Absolute underlying storage protection will utilize standard SSE-S3 default object methodologies. External KMS Key (CMK) provisioning modules and complex key-rotation logic are intentionally rejected from the Terraform boundary to optimize latency overhead.
### 4.2 Logging Audits
Extraneous S3 Server Access Logging and downstream central audit bucket orchestration is intentionally disabled off the `raw` and `curated` buckets based strictly on threat model simplifications. Lake Formation audit trails alone handle data mesh observability.
