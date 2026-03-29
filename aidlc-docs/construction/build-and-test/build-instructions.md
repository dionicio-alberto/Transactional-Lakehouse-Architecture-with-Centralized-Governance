# Build Instructions - Unit 1 (Simulator)

## Prerequisites
- **Build Tool**: Python 3.9+ / Virtual Environment (`venv`) / Bash
- **Dependencies**: `pandas`, `pyarrow`, `faker`
- **Environment Variables**: None explicitly required for build. 
- **System Requirements**: Minimal Local Linux/macOS host. Parquet generation relies natively on local disk I/O.

## Build Steps

### 1. Install Dependencies & Configure Environment
Because the simulator dictates exact execution parameters, we use an automated bash execution:
```bash
cd src/simulator/
chmod +x bootstrap.sh
./bootstrap.sh
```

### 2. Verify Build Success
- **Expected Output**: `[System Complete] The Python execution boundary is verified. Virtualization initialized successfully.`
- **Build Artifacts**: The target local directories `data/staged/` and the underlying `venv/` subdirectories exist. 
- **Common Warnings**: `pip` upgrade warnings are entirely acceptable and don't break the build boundary.

## Troubleshooting

### Build Fails with Dependency Errors
- **Cause**: PyArrow/Pandas often fail compiling C-extensions locally if Python headers are missing.
- **Solution**: Upgrade pip explicitly or use a pre-compiled wheel via Conda.
