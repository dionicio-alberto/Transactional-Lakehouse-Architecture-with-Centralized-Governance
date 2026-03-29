# Code Generation Plan - Unit 1 (Data Simulator)

## Context
- **Unit**: Unit 1 (Data Simulator)
- **Target Location**: `src/simulator/`
- **Stories**: Story 4 (Automated Data Ingestion)
- **Dependencies**: Kaggle Raw Data (`data/raw/`), Python 3 `venv`
- **Extensions**: Security Baseline (Active), Property-Based Testing (Active)

## Execution Sequence

- [x] **Step 1: Project Structure Setup**
  - Create `src/simulator/` directory structure.
  - Create `src/simulator/requirements.txt` (`pandas`, `faker`, `pyarrow`, `pytest`, `hypothesis`).

- [x] **Step 2: Business Logic Generation**
  - Implement `src/simulator/generator.py`: Core logic for Faker generation, vectorization with Kaggle data (Open/High/Low/Close/Volume).
  - Implement `src/simulator/main.py`: Orchestrator for "chunk-and-flush", generating the initial 20-year block and 20 yearly chunks.

- [x] **Step 3: Business Logic Unit Testing**
  - Implement `src/simulator/tests/test_generator.py`: Use `hypothesis` for Property-Based Testing (PBT) verifying constraints (e.g., Exactly 1000 users, >30% LATAM geo distribution).

- [x] **Step 4: Business Logic Summary**
  - Update `aidlc-docs/construction/unit-1-simulator/code/business-logic-summary.md`.

- [x] **Step 5: Documentation Generation**
  - Create `src/simulator/README.md` defining setup (`python -m venv venv`), execution, and local staging directory `data/staged/`.

- [x] **Step 6: Deployment Artifacts Generation**
  - Create `src/simulator/bootstrap.sh` script to automate venv setup, dependency installation, and directory initialization.

