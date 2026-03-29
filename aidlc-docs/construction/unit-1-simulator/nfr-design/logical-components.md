# Unit 1: Logical Components

## 1. Local Staging Storage Component

- **Purpose**: Serve as a temporary intermediary persistence layer before pushing raw files securely to AWS S3.
- **Directory Enforcement**: The system architecture enforces strict adherence to a standard local path schema.
- **Paths**:
  - Base Staging Zone: `data/staged/`
  - User PII Output: `data/staged/users.parquet`
  - Historical Chunk Output: `data/staged/transactions/batch_initial_20_years.parquet`
  - Incremental Output: `data/staged/transactions/batch_YYYY.parquet`

## 2. Generator Logic Component

- **Dependencies**: Exclusively isolates its dependency onto the Python `faker` library and local mock logic.
- **Coupling Rules**: Sits entirely separate from the AWS SDK (`boto3`). The generator component only interacts with the Local Staging Component. This prevents tight coupling and ensures data generation execution doesn't fail due to temporary network or IAM irregularities.

## 3. Local Environment Component

- **Purpose**: Isolate the Python dependencies from the global system to ensure reproducibility and prevent version conflicts.
- **Implementation**: The implementation **MUST** include the creation of a dedicated Python virtual environment (e.g., `python3 -m venv venv`). All dependencies (`pandas`, `pyarrow`, `faker`) must be pinned in a `requirements.txt` file, and the simulator script must execute exclusively within this activated environment.
