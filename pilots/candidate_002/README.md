# Pilot 002 — synthEHRella S1–S5 Ladder 2-Point Pilot

**Aim:** Prove the fidelity→τ pipeline (synthEHRella S1 bootstrap vs S5 prevalence-random) is runnable before full 5–8 point ladder. Synthetic fallback used honestly (MIMIC-III demo not credentialed).

**Data:**
- Synthetic fallback: 5000 rows, 10 numeric (correlated MVN, cov 0.3+0.7 diag) + 5 categorical (3 levels, one-hot →15 cols) + binary outcome (logistic of X). Total feature dim 26 (10 num +15 oh +1 y). N=5000, prevalence 0.506.
- Split: stratified 80/20 train 4000 / test 1000 (TEST_R = held-out synthetic real, since no MIMIC).
- Generators: S1 bootstrap (resample with replacement from real_train), S5 prevalence-random (numeric ~ N(mean,sd) per col + binary Bernoulli per prevalence).
- Seed 20260830.

**Run command:**
```bash
cd pilots/candidate_002
pip install .  # synthEHRella 1.0.0 (requires matplotlib, omegaconf, sklearn)
python synthEHRella/synthEHRella/run_generation.py --help
python synthEHRella/synthEHRella/run_evaluation.py --help
# fidelity/utility module import check + pilot
bash run_pilot_002.sh   # wraps help flags + python run_pilot_002.py
# or directly:
python run_pilot_002.py
```

**What was verified (inventory):**
- `run_generation.py --help` → method + --real_training_data_path + --ckpt_dir + --num_gen_samples + --params
- `run_evaluation.py --help` → method + --output_dir + --real_eval_data_path + --synthetic_data_path + --fidelity/utility/privacy
- `run_postprocessing.py --help` → method + --data_path + --output_path
- `evaluation/fidelity.py`: compute_prevalence, compute_correlation, discriminative_score, MMD/RMSPE/corr Fro
- `evaluation/utility.py`: tstr/trtr/tsrtr
- `version`: synthEHRella 1.0.0, git log 74aa516 / c86b294 / c54b261, pip show, Python 3.11.15

**Outputs (real numbers, synthetic fallback):**
- `outputs/pilot_002_fidelity_tau.csv` — 2 rows S1 vs S5: mmd, rmspe, corr_fro, discriminative_auc, Kendall tau, Spearman, composite
- `outputs/pilot_002_dca.csv` — net benefit at pt 10%/20% per train (TRTR/TSTR_S1/TSTR_S5) vs treat_all/none
- `outputs/pilot_002_utility.csv` — AUC per method + winner
- `outputs/pilot_002_calibration_*.csv` — 10-bin calibration stub (mean_pred vs obs_rate)

Key numbers (this pilot):
- Fidelity S1: mmd 0.088, corr_fro 0.40, disc_auc 0.500; S5: mmd 0.070, corr_fro 4.06, disc_auc 0.508
- Utility TRTR logistic 0.852 tree 0.798; TSTR S1 logistic 0.850 tree 0.793 (gap ~0.002); TSTR S5 logistic 0.553 tree 0.536 (gap 0.30)
- Kendall tau S1=1.0, S5=1.0 (both preserve winner logistic>tree; n=2 methods — trivial; full ladder needs ≥4 methods for meaningful τ)
- DCA NB 10%: TRTR logistic 0.457 vs tree 0.447; TSTR_S1 logistic 0.456; treat_all 0.451 — S1 preserves DCA winner, S5 collapses toward treat_all

**Verification:**
- Calibration plot stub: `pilot_002_calibration_*.csv` (10 bins, n per bin). Plot with `matplotlib` using bins.
- No PHI. Honest synthetic fallback logged.

**Full scale adds:**
- Replace synthetic fallback with MIMIC-III v1.4 TRAIN/TEST_R + MIMIC-IV TEST_TRANSPORT (PhysioNet credentialed)
- Expand to S1/S1′/S2(MedGAN/CorGAN)/S3(Synthea)/S4(resample-perfect)/S5 + sweep seeds (30–50 plasmode reps, 3–5 GAN seeds, ~1500 fits)
- Kendall τ curve vs fidelity composite (MMD⁻¹, corr, TSTR gap PC1) + isotonic f* threshold, DCA 10/20% ranking
