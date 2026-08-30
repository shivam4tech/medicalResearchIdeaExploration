#!/bin/bash
set -e
echo "=== Pilot 002 synthEHRella ladder ==="
echo "Date: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "Python: $(python3 --version)"
echo "Pip: $(pip --version)"
echo "Git synthEHRella log:"
git -C synthEHRella log --oneline -3 || echo "no git log"
echo "--- pip show synthEHRella ---"
pip show synthEHRella 2>&1 | head -20
echo "--- Inventory help flags (run_generation, run_evaluation) ---"
python synthEHRella/synthEHRella/run_generation.py --help
echo "---"
python synthEHRella/synthEHRella/run_evaluation.py --help
echo "---"
python synthEHRella/synthEHRella/run_postprocessing.py --help
echo "---"
# run_evaluation fidelity/utility module check
python -c "from synthEHRella.evaluation.fidelity import compute_prevalence, compute_correlation, discriminative_score; print('fidelity imports OK')"
python -c "from synthEHRella.evaluation.utility import tstr, trtr; print('utility imports OK')"
echo "=== Running synthetic fallback pilot (5k rows) ==="
python run_pilot_002.py 2>&1
echo "=== Outputs ==="
ls -lh outputs/
cat outputs/pilot_002_fidelity_tau.csv
echo "---"
cat outputs/pilot_002_dca.csv | head -20
echo "=== Done ==="
