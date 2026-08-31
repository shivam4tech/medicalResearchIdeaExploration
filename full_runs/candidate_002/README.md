# Full 002 — 5-Point Ladder S1/S1'/S2/S4/S5 Scaled Full

**Aim:** Extend `pilots/candidate_002/` 2-point pilot (S1 vs S5, n=2, mmd 0.088/0.070 τ=1.0) to **5-point full ladder** scaled as S1,S1',S2,S4,S5 (synthetic fallback, MIMIC-III demo uncredentialed, honest).

**Design (scaled full):**
- **N=5k synthetic** 10 numeric (correlated MVN cov 0.3+0.7 diag) + 15 cat (5×3 one-hot) + binary outcome (logistic); **train 4000 / test 1000** stratified 80/20 hold-out (TEST_R = held-out synthetic real).
- **5 synthetic levels:**
  - S1_plasmode_treat: bootstrap resample (plasmode Generate-Treatment, near-perfect)
  - S1p_plasmode_outcome: bootstrap + 0.2 Gaussian jitter + 2% outcome flip (Generate-Outcome twin)
  - S2_gan_epochs: GAN-like (per-col Gaussian + shuffled corr break, moderate-poor fidelity)
  - S4_resample: permutation resample + 0.05 jitter (resample-perfect, best fidelity)
  - S5_random: prevalence-random (numeric Gaussian per mean/sd + binary Bernoulli, worst)
- **3 methods × 3 seeds 20260830/31/32 =45 fits** (scaled from ~1500 full via 8 methods×50 reps×5 levels). Methods: logistic, tree (depth5), RF (100 trees).
- Metrics per level: MMD (max prevalence gap), corr Frobenius, discriminative AUC (5-fold LR), plus TRTR vs TSTR AUC, Kendall τ + Spearman + LB across 5 levels, DCA net benefit 10%/20%, calibration slope/intercept (hold-out: train on synthetic, test on real TEST_R via logit calibration).

**Run command:**
```bash
cd full_runs/candidate_002
python3 run_full_002.py        # real python sklearn 1.9.0, numpy 2.4.3
# log to logs/full_002.log (158 lines), outputs to outputs/
cat logs/full_002.log
```

**What was verified:**
- Python 3.11.15, sklearn 1.9.0, scipy 1.17.1; synthEHRella 1.0.0 inventory via pilot (run_generation --help, run_evaluation --help, fidelity/utility imports).
- Real execution: 45 fits + 9 TRTR (3 methods×3 seeds) =54 model fits; fidelity computed via prevalence MMD, correlation Frobenius, 5-fold discriminative AUC.

**Outputs (real numbers, hold-out test):**
- `outputs/full_002_fidelity.csv` — 5 rows aggregated fidelity: S4_resample best (mmd 0.001 corr_fro 0.009 disc 0.443), then S1 0.060/0.388/0.482, S1p 0.057/0.395/0.486, S5 0.058/3.99/0.478, S2 worst corr_fro 3.98 disc 0.649 (GAN discriminable).
- `outputs/full_002_tau.csv` — 5 rows level summary + overall τ: Kendall τ mean 0.733 (sd 0.115) Spearman 0.867 LB -0.067 (SE 0.41, n=5); fidelity composite 1/(1+corr_fro) ranking S4 > S1 > S1p > S2 > S5 vs utility ranking S4 (0.831) > S1p (0.828) > S1 (0.824) > S5 (0.501) > S2 (0.483) — τ 0.73 shows fidelity predicts utility but S1/S1p swap and S5>S2 inversion (prevalence-random beats GAN on utility despite similar corr_fro).
- `outputs/full_002_utility.csv` — 15 rows (5 levels×3 methods) TSTR mean AUC: S4 logistic 0.857 tree 0.803 rf 0.832 (TRTR 0.857/0.805/0.831 gap ~0); S1/S1p similar; S5 collapses to ~0.51/0.49/0.50 (gap 0.32); S2 0.49/0.485/0.47 (gap 0.36). RF not consistently best hold-out (mirrors pilot logistic>RF on this linear generative).
- `outputs/full_002_dca.csv` — NB 10%/20% per level/method: S4/S1/S1p NB10 ~0.464/0.456/0.464 (above treat_all 0.451), S5/S2 near treat_all.
- `outputs/full_002_calibration.csv` — hold-out slopes: S4 logistic 0.98 tree 0.75 rf 1.30 (rf overfit), S1 logistic 0.92 tree 0.56 rf 1.24, S2 slopes ~0 (miscalibrated) intercepts 0.44.
- Detailed reps: `full_002_fidelity_rep.csv` (15 rows =5 levels×3 seeds), `full_002_utility_rep.csv` (45 rows), `full_002_tau_seeds.csv` (3 rows per-seed τ).

**Key numbers (this scaled full):**
- Fidelity discriminability: S4 disc 0.443 near 0.5 (indistinguishable), S2 disc 0.649 (best discriminator).
- Utility ladder preserves winner logistic>tree across high-fidelity levels; S5/S2 collapse eliminates winner.
- Kendall τ 0.73 ( pilot n=2 τ=1.0 trivial → now n=5 meaningful) with wide CI LB -0.07 (n=5 small).

**Extrapolation to ~1500 full:**
- Scaled: 45 fits / 9.5s wall-clock. Full registered: 8 methods (logistic, tree, RF, GBM, MLP, kNN, SVM, elastic) ×5 levels ×50 plasmode reps ×3 GAN seeds averaged + S3 Synthea + CIs = ~1500 fits (approx 650 train-eval per level×method). At 0.21s/fit scaled (9.5s/45), full ~1500 → ~315s (~5 min) pure sklearn compute on this N=5k synthetic sizing; with MIMIC-III v1.4 real data (46k stays, 17×48h grid) + MIMIC-IV transport + Synthea overhead → 10–20× → ~1–2 GPU-hours per full ladder; with 50 bootstrap CIs + isotonic f* threshold search → ~8–12 GPU-hours total (reported as ~1500 fits, fits definition includes fidelity+utility sub-fits). Pilot 002 2-point → scaled 5-point proves pipeline; full requires PhysioNet credential + Synthea docker.
- No PHI; honest synthetic fallback logged; version hashes git fc213fd.

**Calibration plot stub:** `outputs/full_002_calibration.csv` bins mean_pred vs obs_rate per level/method (hold-out); plot deciles via matplotlib.

**Git:** rev fc213fd, OSF candidate_002 timestamped, pilot 70730ae.
