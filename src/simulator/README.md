# Transactional Lakehouse - Python Data Simulator (Unit 1)

## Overview
This purely local Python application strictly simulates 40+ years of daily historical Apple (AAPL) transactional trading volume across 1,000 distinct dynamically generated users. To comply with performance demands and strict 5-minute time guarantees, the application leverages Pandas native block-vectorization schemas rather than iterations, mapping historical Open/Close/Volume ranges onto pseudo-randomly assigned UUIDs.

## Output Structure
Simulation data is written natively into Parquet formatting encoded with Snappy compression logic.
- `data/staged/users.parquet` (1,000 PII distinct records > 30% LATAM geo-mapped).
- `data/staged/transactions/batch_*.parquet` (Time-partitioned historical chunking).

## Setup & Execution
The application acts entirely decoupled from the AWS API (`boto3`). An associated `bootstrap.sh` automates the virtualization boundary.

1. Init virtual boundary:
```bash
sh src/simulator/bootstrap.sh
```

2. Execute simulation orchestration:
```bash
cd src/simulator/
source venv/bin/activate
python main.py
```

### Next Steps (Post-Execution)
Following a successful terminal execution, standard stdout logs will assert completion. Proceed to utilize `aws s3 sync data/staged/ s3://[raw-zone-bucket]/` utilizing your dynamically provisioned Terraform User access keys.
