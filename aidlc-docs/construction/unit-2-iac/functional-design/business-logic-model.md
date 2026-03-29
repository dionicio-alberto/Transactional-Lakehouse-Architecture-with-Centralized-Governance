# Business Logic Model - Unit 2 (IaC/Terraform Module)

## Logical System Architecture
While Unit 2 is inherently an Infrastructure module mapping to AWS layers, this functional design dictates the *logical business flows* required strictly from the underlying infrastructure resources without referencing code explicitly.

## 1. Batch Orchestration Logic
- **Trigger Type**: Time-based Cron Orchestration (e.g., EventBridge scheduling).
- **Frequency**: Scheduled nightly (e.g., `12:00 AM`).
- **Flow**: The orchestrator triggers dependent analytical processes downstream only after the scheduled time elapsed boundaries are met. There is no implicit event-driven trigger binding directly to physical `S3:PutObject` events on raw files.

## 2. Security Segmentation Logic
- **Identity Isolation**: Business analysts do not map implicitly to active real-world AWS federations. Instead, logically discrete mock identities must be synthesized directly. This ensures the boundaries established around the `LatamAnalyst` and `FinancialAnalyst` personas operate safely inside strict isolation models.

## 3. Storage Hierarchy Abstractions
The storage design splits cleanly across specific processing layers, explicitly prefixed under a standardized sequence identifying environmental posture: `<layer>-<region>-<account>-<typeofbucket>`
- Layer 1 (`raw`): Immutable zone acting as the landing area for local data simulator Sync uploads.
- Layer 2 (`curated`): Governed boundaries containing transformed Lake Formation objects. 
- Layer 3 (`athena`): Temporary artifact bounds strictly used to materialize ad-hoc interactive SQL queries requested by Data Analysts.
