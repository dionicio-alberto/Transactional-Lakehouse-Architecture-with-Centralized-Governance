# Unit Test Execution - Unit 1 (Simulator)

## Run Unit Tests
Unit tests in Unit 1 apply **Property-Based Testing (PBT)** utilizing `hypothesis` and `pytest`.

### 1. Execute All Unit Tests
```bash
cd src/simulator
source venv/bin/activate
python -m pytest tests/
```

### 2. Review Test Results
- **Expected**: 2 tests pass, 0 failures.
- **Coverage Strategy**: Focus is purely on verifying `Mock_Engine` isolation bounds and random property permutations (Faker bounds, >30% Geo LATAM targets).
- **Test Report Location**: Stdout terminal logging natively attached to the process.

### 3. Fix Failing Tests
If tests fail:
1. Examine explicit warnings (e.g., `hypothesis` often marks FailedHealthChecks if memory or fixtures drop data contexts).
2. Adjust `suppress_health_check` in `test_generator.py` if testing on heavily delayed IO virtual terminals.
