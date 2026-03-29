#!/bin/bash
set -e

# Target Setup Directory
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$BASE_DIR"

echo "[Simulator Init] Transitioning to local bounds: $BASE_DIR"

if [ ! -d "venv" ]; then
    echo "[VENV Check] Python Virtual Environment missed. Creating..."
    python3 -m venv venv
else
    echo "[VENV Check] Validated existing 'venv' layer."
fi

# Load Execution Boundaries
echo "[Pip Ensure] Bootstrapping simulation definitions via requirements.txt..."
source venv/bin/activate
pip install -r requirements.txt --quiet

# Pre-Validate target destinations
mkdir -p data/staged/users
mkdir -p data/staged/transactions

echo "[System Complete] The Python execution boundary is verified. Virtualization initialized successfully."
echo "Execute: 'source src/simulator/venv/bin/activate' && 'python src/simulator/main.py'."
exit 0
