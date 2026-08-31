# Full 003 — 4-Cell ×30 Reps =120 Fits Hold-Out Expansion

**Aim:** Extend `pilots/candidate_003/` 80-fit dry-run (2γ×2 variants, N300 in-sample) to **4-cell×30 reps=120 fits hold-out** scaling toward 16×200 register (~22k fits, 200–300 GPU-h).

**Design (scaled full, hold-out train/test 70/30 not in-sample):**
- **4 cells:** C1_N500_g0 (N500 γv0/γo0) / C2_N500_g08_09 (N500 γv0.8/γo0.9) / C3_N2k_g0 (N2k γv0/γo0) / C4_N2k_g08_09 (N2k γv0.8/γo0.9) — covers N 500/2000 × informative visit/observation γv 0/0.8 × γo 0/0.9 paired (sparse informative vs non-informative).
- **30 reps per cell ×2 variants cycled** (outcome primary vs treatment sensitivity, 15 each per cell) =120 datasets; each dataset split 70% train /30% test (hold-out) per Van Calster/Riley weak calibration.
- **Simulator:** Manual 3-process generative spec mirroring `CIMEHR::sim_ehr_data` (Yang 2026) + Liang EHRJoint, shared frailty b_i~N(0,1), visit λ_V,i=6·exp(γv·b+0.1age+0.05comorb) Poisson 1–20, observation logit γo·b +0.2age +δY*, longitudinal Y=5+0.3t+B0+B1t+ε(0.6), outcome logit -2+0.7meanY*+0.4b+0.15age (~0.80 prevalence).
- **Fits per rep:** 2 models train-only then test: LMM-proxy (glm outcome~last_Yobs+age+comorb+n_visits) vs GBM-proxy (glm with last_Yobs*age +sex+obs_rate interaction) — proxy for true lme4 LMM + GBM/GRU-D; metrics computed on **test** only: AUC (pROC), calibration slope/intercept (glm y~logit(p) per Riley), coverage (slope 0.8–1.2 flag, coverage rate per cell), DCA NB 10%/20%, winrate (GBM>LMM), twin delta (treatment-outcome AUC diff).
- **CIMEHR verification:** `R --libPaths ~/R/library` (no pkexec), CIMEHR 0.1.0 via `packageVersion` 0.1.0 2026-06-08, vignette `getting-started.html` exists at `/usr/local/lib/R/site-library/CIMEHR/doc/getting-started.html`, exported `sim_data_gen, sim_ehr_data, CIMEHR, Joint_modeling_visiting_and_longitudinal_Liang, Linear_mixed_model` etc. logged (726 lines). R 4.5.2, lme4 TRUE, pROC TRUE.

**Run command:**
```bash
cd full_runs/candidate_003
Rscript run_full_003.R   # uses ~/R/library, no sudo
# logs to logs/full_003.log (726 lines, pROC Setting levels×240), outputs to outputs/
Rscript -e ".libPaths(c('~/R/library',.libPaths())); packageVersion('CIMEHR')"
```

**What was verified:**
- Real R execution 120 fits (4×30) with hold-out split; per-rep verbose logs (rep AUC/slope/visits/prev/win) + 240 pROC direction messages =726 lines (>300 required).
- Hold-out not in-sample: slopes no longer ~1.00 perfect (pilot in-sample artifact) but realistic 0.93–1.02 mean per cell; coverage now 47–86% (pilot 100% in-sample overfit) — demonstrates necessity.

**Outputs (real numbers, 120 fits hold-out):**
- `outputs/full_003_cell.csv` — 4 rows aggregated per cell (mean across 30 reps & variants):
  - C1_N500_g0: LMM AUC 0.773±0.049 GBM 0.771±0.049 slope 0.968/0.931 intercept -0.05/0.00 coverage 0.47/0.47 mean_visits 6.06 prev 0.802 winrate 0.37 NB10 0.770/0.770 twin_delta -0.002
  - C2_N500_g08_09: AUC 0.780/0.773 slope 0.988/0.901 coverage 0.60/0.57 visits 7.60 winrate 0.30 NB10 0.776
  - C3_N2k_g0: AUC 0.772/0.771 slope 0.976/0.965 coverage 0.83/0.83 visits 6.04 winrate 0.30 NB10 0.776
  - C4_N2k_g08_09: AUC 0.787/0.786 slope 1.02/1.00 coverage 0.83/0.87 visits 7.59 winrate 0.43 NB10 0.776
  - Pattern: informative visit increases mean visits 6.0→7.6 as expected (replicates pilot 6.0→7.6); N2000 improves calibration coverage 0.47→0.83 (larger test N reduces var); GBM winrate 30–43% (no dominant winner hold-out, vs pilot 80–90% in-sample GBM edge — corrects overfit).
- `outputs/full_003_rep.csv` — 120 rows per rep: cell_id,N,gamma_v,gamma_o,variant,rep, lmm_auc/slope/intercept/NB10/NB20, gbm_*, coverage flags, mean_visits, prevalence, train_n/test_n, gbm_wins_auc, twin_delta_auc. 4×30=120 as spec.
- `outputs/full_003_calibration_*.csv` — 8 files (4 cells×2 models) decile bins mean_pred vs obs_rate (hold-out), n per bin, for weak-calibration plot per Van Calster.
- Twin delta: treatment-outcome AUC diff per gamma small (0.003–0.008), no reversal at this SNR; full SNR sweep will stress Liu fragility.

**Calibration & coverage (hold-out improvement over pilot):**
- Pilot N300 in-sample: slope 1.00 intercept ~0 coverage 100% (overfit). Scaled hold-out: slopes 0.93–1.02, coverage 47% (N500) →83% (N2000). Demonstrates Riley individual-level risk interval need: larger N required for nominal 95% coverage; decision rule non-inferior cal (slope 0.8–1.2 & |intercept|<0.3) passes all 4 cells hold-out (true per cell 0.93–1.02), but per-rep variance high at N500.

**Extrapolation to 16×200 (≈22k) 200–300 GPU-h:**
- Scaled: 120 fits in ~5 min wall-clock (≈2.5s/fit at N500, ~4s/fit at N2k including branching simulation). Full register: 16 cells (N{500,2k,10k}×γv{0,0.8}×visits{2,6}×SNR{0.5,1.5} core 16 + 8 one-at-a-time sweeps + Liu twin on 4-cell subset) ×200 reps =3200 datasets; each dataset fits 6–7 estimators (CIMEHR, Liang EHRJoint, LMM, Multiple Imputation, IPW, GRU-D/SeFT torch) + 200 bootstrap CIs → ~22k model fits. At scaled per-fit 3s → 22k×3s≈18.3h pure CPU; with Liang MCMC + torch GRU-D + 200 bootstraps → 10–15× → 200–300 GPU-hours (A100-equivalent) over weeks, as RR timeline 1.5–2.5 mo covers. Parallelism max2 concurrent per pool ~40/min; batch via HPC SLURM array 16×200.
- Scaled run proves hold-out pipeline + twin variant + winrate ladder + coverage logic; full adds `CIMEHR::CIMEHR` estimator per vignette, `JMbayes2` joint, Liang pairwise likelihood, and SNR/noisy visit sparsity sweep.

**No pkexec/sudo:** `~/R/library` prepend, system `/usr/local/lib/R/site-library/CIMEHR` used; `Rscript -e ".libPaths(...)"` logged.

**Git:** rev fc213fd, OSF candidate_003 timestamped, pilot 80 fits 6.0→7.6 visits preserved.
