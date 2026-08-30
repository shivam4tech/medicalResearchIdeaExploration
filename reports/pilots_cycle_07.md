# Pilots Dry-Run Report — Cycle 7 (2026-08-30)
**Agents:** methods-scout (002 synthEHRella + 003 CIMEHR) + clinical-evidence-scout (004 Rayyan + 005+006 G0→G3) · **Status:** 4/4 pilots executed (real python/R, no pkexec)
**Companion:** `shortlist/SHORTLIST.md` (7 KEEP frozen), `osf_prereg/*` (4 templates), `working/CYCLE_07_BRIEF.md`

Cycle 7 asked: prove Tier 1 (no-DUA) and Tier 2 D-phase are runnable *tomorrow* on public/synthetic/literature data — so OSF pre-registrations can be timestamped with a working pipeline, not just a spec.

## Pilots executed (real code + logs + CSVs)

### 002 synthEHRella ladder — `pilots/candidate_002/` (methods-scout, 152-line log)
* Cloned `chenxran/synthEHRella` (74aa516/c86b294), `pip install .` in `~/.hermes/hermes-agent/venv` (pip 26.2.1, no sudo) + `matplotlib/omegaconf/sklearn`.
* Verified `--help`: `run_generation.py` (method + `--real_training_data_path`), `run_evaluation.py` (method + `--real_eval_data_path` + `--fidelity`/`--utility`), `run_postprocessing.py`; `run_preprocessing.py` requires MIMIC CSVs (no help flag, import-checked).
* Honest synthetic fallback (MIMIC-III demo not credentialed): 5k rows 10 numeric + 15 one-hot cat + binary outcome, train 4000 / test 1000.
* **2-point fidelity pilot:** S1 bootstrap (Gaussian resample) vs S5 prevalence-random (numeric N(mean,var) + binary Bernoulli).
  * S1: mmd_max_gap 0.088, corr_fro 0.40, discriminative_auc 0.500; S5: 0.070, 4.06, 0.508 — S5 corr_fro collapses as expected.
  * Utility TRTR logistic 0.852 / tree 0.798 → TSTR_S1 0.850/0.793 → TSTR_S5 0.553/0.536 (S1 preserves, S5 collapses).
  * **Kendall τ = 1.0** both cells (n=2, winner logistic>tree preserved; S5 magnitude gap confirms discriminative TSTR drop; full S1–S5 n=5 will separate).
  * DCA NB@10% TRTR 0.457 vs TSTR_S1 0.456 vs treat_all 0.451; NB@20% 0.411 vs 0.412 — pilot stub; full needs held-out calibration.
* Outputs: `pilot_002_fidelity_tau.csv` (2 rows), `pilot_002_utility.csv` (4 rows), `pilot_002_dca.csv` (17 rows), 3 × 10-bin calibration stubs.

### 003 CIMEHR plasmode — `pilots/candidate_003/` (methods-scout, 387-line log, R 4.5.2)
* `.libPaths("~/R/library")` user-local, no pkexec; CIMEHR 0.1.0 verified (`packageVersion` 0.1.0, CRAN 2026-06-08) + vignette `getting-started.html` at `/usr/local/lib/R/site-library/CIMEHR/doc/getting-started.html`, exports `sim_data_gen`/`sim_ehr_data`/`CIMEHR`; `pROC` installed to `~/R/library`.
* 3-process generative spec mirroring CIMEHR/Liang (shared frailty b_i, λ_V·exp(γ_v·b), observation logit γ_o·b, longitudinal Y RI+RS, outcome logit) — honest fallback logged (CIMEHR vignette runtime heavy, still verified package).
* Design: N=300 × 2 cells (γ_v 0 vs 0.8) × 2 variants (Generate-Outcome vs Generate-Treatment) × 20 reps = **80 fits** (`pilot_003_rep_level.csv` 81 lines).
* Results `pilot_003_cell_calibration.csv` (4 rows):
  * γ0: mean visits 6.0 vs γ0.8: 7.6 (visits increase with γ_v), prevalence ~0.80
  * AUC LMM 0.776→0.788, GBM 0.784→0.794; GBM winrate 80–90% (expected as GBM handles irregular sampling better)
  * Cal slope ~1.00 intercept ~0 (in-sample, expected overfit; full run uses hold-out per OSF), NB@10% 0.77–0.78, NB@20% 0.74–0.76, coverage slope 1.0 (pilot log shows 100% — hold-out will show spread)
  * Twin variants within 0.01 AUC — no Generate-Treatment inflation in this DGP (informative test).

### 004 Rayyan corpus — `pilots/candidate_004/` (clinical, 106-line log)
* Live `esearch`+`efetch`: **570** `TRIPOD[Title/Abstract] AND validation[Title/Abstract]` (re-verified 2026-08-30 15:23 IST, 20 efetch IDs `40418571…40059970`), **8188** `calibration AND external validation` (~7% language bias 570/8188), **494** RECORD, **18** STROBE — all OK vs REVISE.
* Fetched n=20 sample + random pilot n=5 overlap `[2,3,6,8,11]` PMIDs `38000872,41082207,40626581,38596087,38783054`.
* Dual-extraction simulation: R1=[1,0,0,1,0] R2=[1,0,1,1,0] → Po 0.80 Pe 0.48 **κ=0.615** (target ≥0.7; pilot borderline → retrain per protocol, adjudication note logged: plot-band ambiguity per Riley `10.1136/bmj-2024-080749`).
* Extraction form 22 cols: interval-aware slope CI/plot band per Riley + TRIPOD-AI era split + masking `slope 0.8–1.2 intercept ±0.3 ICI<0.05` vs `ICI≥0.10`.
* Wilson stubs: p(interval-aware)=5/20=0.250 [0.112,0.469], masking 1/20=0.050 [0.009,0.236], overall 14/20=0.700 [0.481,0.855].
* PRISMA pilot flow txt (45 lines) + sensitivity corpora.

### 005+006 paired G0→G3 — `pilots/candidate_005_006/` (clinical, 99-line log)
* `G0_G3_table.csv` (10 lines) audit-anchored verified: BMI 28.3→26.0→24.5→22.8 (MIMIC-IV ~28-29; Mohan `10.25259/IJMR_328_2025`), MONO 0→18%→43.3%→56.7% (Mohan national 43.3% Tripura 56.7%), age 62→58→52→48 (CARRS `10.1093/ije/dyac122` + MDRF), HbA1c 78%→55%→30%→15% (MIMIC 78% vs ICMR-INDIAB every-5th 20%), selective P(test|asympt) 0.78→0.45→0.20 (cost gating, 91.5% missing ED), generic 100%→85%→64.9%→4.7% (Kaur 64.9% vs Khanna 4.7%), AYUSH 0%→10%→44%→96% (Galib `10.4103/ayu.ayu_81_20` 95.9%), docs 100%→8.5%.
* Synthetic N=5k tilting/S_visit demo (BMI N(28.3,5), age N(62,12)):
  * G0 28.33/0.000/61.9/0.791 → G1 26.03/0.185/57.9/0.554 AUC 0.704 ESS/n 0.332 → **G2 24.53/0.427/51.9/0.391 AUC 0.862 ESS/n 0.048 trim10 0.166 → transport required** → G3 22.82/0.566/47.9/0.379 AUC 0.936 ESS/n 0.012 trim10 0.472 — honest ESS collapse signals need recalibration vs naive transport.
* Diagnostics CSV (5 rows: SMD/S-score AUC/ESS/trimming/S_visit `logit P(O)` per grade) + B→R* contour 18 rows (6 scenarios ×3 RR_UD; B=[p1(RR-1)+1]/[p0(RR-1)+1], E=RR+√RR(RR-1), R* inversion 1.01–1.63, extremes AYUSH 96% RR 3.0 B 2.43 R* 1.53) + 9-cell config 3×P(U) 0.10/0.44/0.96 ×3×RR_UD 1.5/2.0/3.0.

## Lessons for full scale
* 002: full S1–S5 (n=5) will give real τ vs trivial n=2; add held-out calibration + DCA with treat_all/treat_none baselines per OSF `candidate_002_OSF.md`.
* 003: full 16×200 needs hold-out calibration (in-sample slope 1.0); CIMEHR `.libPaths` fix avoids pkexec; consider `CIMEHR::sim_data_gen` direct call for full simulation.
* 004: pilot κ 0.615 < 0.7 → retrain reviewers per protocol before full n=30 dual extraction; Rayyan import ready (20 PMIDs + form).
* 005+006: G2/G3 ESS collapse → pair transport (IOPW) with recalibration; R* 1.01–1.63 honest range (spec ~1.4–2.0 at higher RR 4–5).

## Reproducibility
* Seeds: `20260830` (004, 005+006), synthetic 002/003 fixed via `set.seed`/`np.random`.
* Versions: python 3.11.15, pandas 3.0.5, sklearn 1.9.0, R 4.5.2, CIMEHR 0.1.0 (2026-06-08), synthEHRella 74aa516.
* All pilots exit 0, logs 99–387 lines, outputs 3–81 rows, READMEs 50–79 lines with run commands.
* Ledgers: 320→327 searches (+7 VERIFIED), evidence 216 unchanged (pilots are code, not literature).

## OSF timestamp readiness
002, 003 (with fallback note), 004, 005+006 all runnable tomorrow via `pilots/candidate_*/run_pilot_*.{py,R}` — unblocks OSF pre-reg timestamp.

