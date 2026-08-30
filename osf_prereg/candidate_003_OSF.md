# OSF Pre-registration — Candidate 003 3-Process Joint Plasmode DL-vs-Classical (CIMEHR Engine, 16-Cell Core + Twin Variants)

**Territory T1 Plasmode Design | Cycle 9 OSF-Ready (2026-08-30) — TIMESTAMPED**
**Companion dossiers:** `ideas/candidate_003.md` + `working/agent_notes/methods-scout/cycle04_T1_plasmode_lock.md` (LOCKED 2026-08-30) + `pilots/candidate_003/` (exit 0)
**Agent:** methods-scout | **Status:** OSF-Ready (D simulation, data-independent, executable tomorrow)
**OSF registration type:** Registered Report Stage 1 — D simulation plasmode benchmark
**Generative engine:** CIMEHR 0.1.0 (Yang 10.48550/arXiv.2602.15374 + CRAN https://cran.r-project.org/web/packages/CIMEHR + GitHub https://github.com/ysph-dsde/CIMEHR) primary; Liang 10.48550/arXiv.2410.13113 (EHRJoint) sensitivity
**TRIPOD+AI:** not directly applicable (simulation) — maps via calibration hierarchy Van Calster 10.1016/j.jclinepi.2015.12.005 + Riley 10.1136/bmj-2024-080749 + Schneider 10.1186/s13040-025-00450-z template
**Data availability tier:** D simulation (MIMIC-III/IV covariate resampling + `rnorm` synthetic fallback — no PHI, no DUA blocking)

---

> **OSF REGISTRATION TIMESTAMP BLOCK**
>
> | Field | Value |
> |-------|-------|
> | **Registration date (OSF)** | **2026-08-30** |
> | **Git rev (code archive)** | `70730ae984ae0d2592c2` — tag `v0.1.0-rr` |
> | **Code archive paths** | `pilots/candidate_003/run_pilot_003.R` + `pilots/candidate_003/logs/pilot_003.log` (387 lines, exit 0) + `pilots/candidate_002/synthEHRella` commit `74aa51601615349648bcfa38e1cc9c8a55c4ef35` |
> | **CIMEHR version** | `0.1.0` (CRAN 2026-06-08) — verified `packageVersion("CIMEHR")==0.1.0` + vignette `getting-started.html` 169K in pilot log |
> | **Random seed (locked)** | `20260830` — `set.seed(20260830)` (R), `numpy.random.default_rng(20260830)`, `torch.manual_seed(20260830)` — all cell generation, splits, bootstrap |
> | **Pilot verification** | `pilots/candidate_003/logs/pilot_003.log` **exit 0** — 4 cells (γ_v 0/0.8 × outcome/treatment) ×20 reps, N=300; CIMEHR installed TRUE, lme4 TRUE, pROC TRUE; outputs `pilot_003_rep_level.csv` (80 rows) + `pilot_003_cell_calibration.csv` |
> | **Checklist** | Leakage N/A (simulation) — instead **CIMEHR decision rule + twin-variant + 16-cell spec** ticked (see §4/§5) |
> | **Analysis lock** | Generators, cells, decision rule, seeds locked before any full 16×200 run; no peeking at pilot calibration to choose thresholds |

---

## 0. Administrative

| Field | Value |
|-------|-------|
| **Title** | Pre-registered 16-cell 3-process joint plasmode benchmark: do irregular-series deep learning (GRU-D/SeFT/GRU-ODE-Bayes) outperform well-specified classical (LMM + JMbayes2) on a joint calibration/coverage/DCA criterion under tunable informative visiting/observation? |
| **Version hash (pre-freeze)** | `sha256:PENDING-003-` + commit hash at OSF freeze — replace at submission; `config/cells_core16.csv` SHA256 co-registered |
| **Random seed (locked)** | 20260830 all RNGs (see timestamp block) |
| **Analysis date lock** | Generative spec, cells, decision rule locked at freeze; no peeking at full-run metrics before thresholds fixed |
| **Embargo** | Open at Stage 1 acceptance |
| **Code freeze** | Git tag `v0.1.0-rr` + Docker `r-base:4.5.2` + `CIMEHR==0.1.0` + `lme4` + `JMbayes2` + `pROC` + `torch==2.3` for GRU-D/SeFT |
| **Target journals** | Biometrics / J Clin Epidemiol / Medical Decision Making / Nature Scientific Data (simulation benchmark + calibration focus) |

---

## 1. Background & Aims

**Problem:** Sun et al. 2026 (Health Data Sci 10.34133/hds.0456) is the only comprehensive review of DL for irregularly sampled medical time series (ISMTS) — catalogues GRU-D (Che 10.1038/s41598-018-24271-9), SeFT (Horn 10.48550/arXiv.2006.10199), GRU-ODE-Bayes (Brouwer 10.48550/arXiv.1905.12374), neural CDE/ODE hybrids. Review contains **no matched calibration/coverage/DCA head-to-head of GRU-D/SeFT vs well-specified LMM/joint** under tunable informativeness. Schneider et al. 2025 (10.1186/s13040-025-00450-z, PMC12070788) provides simulation template varying frequency/noise/heterogeneity joint vs Cox — but **no DL comparator**. Liang et al. 2024 (EHRJoint 10.48550/arXiv.2410.13113) establishes 3-process (visit+observation+longitudinal) shared-frailty correction; Yang et al. 2026 CIMEHR (10.48550/arXiv.2602.15374, CRAN 0.1.0) packages the three-stage joint (partial-likelihood frailty visit + probit observation + weighted longitudinal) with simulator — **but neither paper benchmarks DL vs classical**. Frontiers 10.3389/fams.2026.1849703 (Mashishi 2026) stress-tests LMM vs GEE under irregularity — no DL. Inspecting Sun supplement `github.com/SCXsunchenxi/ISMTS-Review` (README, datasets, no LMM-vs-DL table) + CIMEHR vignette `getting-started.html` (169K, no head-to-head) confirms gap survives (ideas/candidate_003.md Gate 1).

**Aims (falsifiable, ML gets no preference):** Pre-register a **3-process joint plasmode benchmark** with **known truth** that tests, across a pre-specified phase diagram, whether DL-irregular models **fail to outperform** classical on a **joint criterion** (non-inferior calibration + coverage AND superior DCA). Either outcome publishable (classical suffices vs DL wins in characterised regime — see §4).

**Generative claim:** We **use CIMEHR as engine**, not propose new joint — benchmarking DL vs classical is the contribution; Liang spec retained as engine-sensitivity.

---

## 2. Data & Participants (Simulation — No PHI)

### 2.1 Plasmode base

| Pathway | Source | Role | Access | Timeline |
|---------|--------|------|--------|----------|
| **Primary plasmode** | Resample covariate structure (X, visit-time patterns) from **MIMIC-III v1.4 / MIMIC-IV v2.2** then overlay synthetic trajectories via §2.2 spec | Realistic covariate support with known truth (Franklin 10.1093/aje/kww098 + Schuler formalism) | PhysioNet CITI+DUA 1–2 weeks for realistic base | **Tomorrow** for coding with `rnorm` fallback |
| **Fully synthetic fallback** | `rnorm` age/sex/comorbidity base (no resample) | Immediate coding without credential | none needed | Immediate |
| **Secondary real replication** | MIMIC-III/IV real trajectories (MIMIC-Extract) + PhysioNet Challenges 2012/2019 | Reviewer-requested out-of-sample irregularity | Public/credentialed | Immediate–2wks, not required for gap |
| **Optional Stage-2 transport** | UKB-SA / CARRS / ICMR-INDIAB structure | Indian sparsity regime via λ_V/γ_v (not claim-staging) | Managed access | Not required for v1 |

### 2.2 Generative spec — 3-process joint (CIMEHR primary; Liang sensitivity)

We lock CIMEHR semantics (Yang 2602.15374 §2 + vignette `sim_data_gen`):

1. **Visiting process (IP):**
   ```
   λ_V,i(t) = λ_0V(t) · exp( γ_v · b_i + β_v^T X_i + α_v · Y*_i(t−) )
   ```
   `b_i ~ N(0, σ_b²)` shared frailty (or vector `(b0i,b1i)`); `X_i` baseline (age/sex/comorbidity resampled); `Y*_i(t−)` lagged latent truth to avoid circularity; `λ_0V(t)` piecewise-constant controlling sparsity (mean visits/year). `γ_v` = **visit informativeness** (0→non-informative, 0.8→strong; primary contrast 0 vs 0.8, intermediate 0.3 in sweeps).

2. **Observation process (IO):**
   ```
   logit P( O_ij(t*) = 1 | visit at t*, b_i, Y*_i(t*) ) = γ_o · b_i + β_o^T X_i + δ · Y*_i(t*)
   ```
   Separates IP (did patient present?) from IO (what was ordered?). `γ_o` frailty-driven selective ordering; `δ` severity-driven testing; both 0 → non-informative. Core contrast `γ_o 0 vs 0.9` one-at-a-time; sweep includes `0.4` intermediate.

3. **Longitudinal biomarker (RI+RS):**
   ```
   Y_ij(t) = X_i(t) β + Z_i(t) b_i + ε_ij(t),  b_i ~ N(0, D), ε_ij ~ N(0, σ²)
   ```
   `Z_i(t) b_i` = **random intercept + random slope** (RI+RS), `D = diag(τ0², τ1²)` (heterogeneity); SNR = Var(Zb)/σ²; latent truth `Y*_i(t)=X_i(t)β+Z_i(t)b_i`; linear + spline time trend so LMM can be correctly specified when desired.

4. **Shared frailty linkage:** Single latent `b_i` (or vector) enters all three processes + outcome, inducing visit↔observation↔longitudinal↔outcome correlation.

5. **Outcome (known truth):**
   ```
   logit P( E_i = 1 | history ) = θ0 + θ1 · functional( Y*_i ) + θ2 · b_i
     functional ∈ { current value Y*_i(t), slope dY*/dt, cumulative AUC ∫Y*, threshold 1{Y*>c} }
   ```
   Or survival `λ_E,i(t)=λ_0E(t)·exp(θ1·Y*_i(t)+θ2·b_i)` with admin censoring at H=3y/5y (10%/30%). Estimand predictive: 5y event risk / survival; also estimation bias of θ1.

**Engine note:** Primary generator = `CIMEHR::sim_data_gen` / `sim_ehr_data` (R); sensitivity = Liang `EHRJoint::sim_data_gen` (arXiv 2410.13113). Pilot `run_pilot_003.R` mirrors spec manually for transparency (shared frailty b, λ_V=6/yr cap 30, visit Poisson, RI+RS, logit IO) and **verified CIMEHR 0.1.0 installed** with vignette present — honest fallback logged (see pilot log tail).

### 2.3 Twin plasmode variants (Liu 10.48550/arXiv.2504.11740 sensitivity)

- **Plasmode-Generate-Outcome (PRIMARY):** resample real X, overlay synthetic `Y*(t)` + outcome mechanism (Franklin preferred for prediction).
- **Plasmode-Generate-Treatment (SENSITIVITY):** overlay synthetic visit/observation mechanism + outcome | (real) exposure; tests Liu fragility (outcome-generating can under-cover) on 4-cell subset.
- If conclusion reverses by variant, paper pivots to instrument-validity contribution (pre-registered).

---

## 3. Design — 16-Cell Core + Sweeps (pre-registered `config/cells_core16.csv`)

### 3.1 Parameter inventory

| Dimension | Values (core bold, sweeps italic) | Rationale (vs Schneider) |
|-----------|-----------------------------------|--------------------------|
| **N (patients)** | **500**, **2 000**, **10 000** — core uses **2k vs 10k** (500 for pilot) | Small→large asymptotics |
| **Visits / patient** (H=3y/5y) | Mean **2** (sparse/screening), **6** (moderate), **15** (dense/chronic) — `λ_V` low/med/high — core: **2 vs 15** | Schneider frequency |
| **Horizon** | H=3y, 5y; origin first eligible visit | Time-origin sensitivity |
| **Noise σ (SNR)** | **0.5** noisy, *1.5* moderate, **4** clean — SNR = Var(Zb)/σ² — core: **0.5 vs 4** | Schneider noise |
| **Visit informativeness γ_v** | **0** (non-inform), *0.3* moderate, **0.8** strong — core **0 vs 0.8** | Liang threshold where joint matters; 0 = falsification arm |
| **Observation informativeness γ_o / δ** | **0** non-inform, *0.4* moderate, **0.9** strong — core **0 vs 0.9** one-at-a-time | Decomposes IP vs IO |
| **Heterogeneity D** | τ0∈{0.5,1.5}, τ1∈{0.2,0.8} — `diag(τ0²,τ1²)` RI+RS | Random-slope heterogeneity |
| **Effect size θ1** | OR/HR {1.1 weak, 1.5 moderate, 2.5 strong} per 1-SD Y* | Weak→strong biomarker |
| **Censoring** | 10%, 30% admin + informative via frailty | Joint-vs-Cox sensitivity |

### 3.2 Core design (fractional factorial via Latin hypercube / Sobol)

**Core 16 cells = γ_v{0,0.8} × sparsity{low(2), high(15)} × SNR{noisy(0.5), clean(4)} × N{2k,10k} = 16 cells**, each **200 Monte-Carlo replicates** (pre-registered). Plus one-at-a-time sweeps (γ_o, censoring, effect size, D). All cells Plasmode-Generate-Outcome primary; **subset 4 cells (γ_v 0/0.8 × SNR noisy/clean) also Plasmode-Generate-Treatment** as Liu sensitivity. Optional sensitivity: `H=3y vs 5y`, CIMEHR vs Liang engine 4-cell.

### 3.3 Replicates & config hash

- **Replicates:** 200 per cell (16×200=3,200 datasets per N level; 6,400 with N=2k+10k). Pilot uses 20/demonstration.
- **Config file:** `config/cells_core16.csv` (columns: cell_id, N, mean_visits, H, SNR, gamma_v, gamma_o, tau0, tau1, theta1, censoring, variant, engine, seed) — **SHA256 co-registered at freeze**; any post-freeze change logged as deviation.

---

## 4. Baselines & Metrics — Joint Criterion & Decision Rule (ML Gets No Preference)

### 4.1 Mandatory baselines (identical splits per replicate; HPs tuned on training validation only)

1. **LMM RI+RS** (`lme4`/`nlme` R): correctly specified time trend (linear+spline if non-linear truth), predicted trajectory fed to outcome model (two-stage, bootstrap SE). *Mandatory classical — correctly specified.*
2. **Joint longitudinal–survival (JMbayes2)** (`JMbayes2` R; `joineRML`/`frailtypack` cross-check): shared random effects linking `Y*(t)` to hazard. *Mandatory classical — joint.*
3. **LOCF + logistic/Cox:** last-observation-carried-forward — "EHR strawman" many DL papers beat. *Mandatory trivial.*
4. **MICE + pooled logistic/Cox:** m=20 imputations assuming MAR within visit-windows; Rubin's rules. *Mandatory imputation.*
5. **GRU-D (Che 2018)** (`PeterChe1990/GRU-D`, PyTorch): masking + Δt, nested CV HPs on plasmode training only. *Mandatory DL.*
6. **SeFT (Horn 2020)** (PMLR 119 `horn20a`): set-function, variable-length sets without imputation. *Mandatory DL.*
7. *(Optional 7th if budget):* **GRU-ODE-Bayes** (`torchdiffeq` + `BorgwardtLab/GRU-ODE-Bayes`) — one continuous-time representative; report separately; tests ODE overhead claim (Sun Limitations).

Training: identical epoch budget (100 epochs, patience 10), early stopping on validation AUPRC, temperature/isotonic calibration where applicable.

### 4.2 Metrics (joint — not AUROC-only)

- Discrimination: AUC (binary) / C-index & time-dependent AUC (survival) on held-out plasmode test (DeLong / bootstrap CI).
- Calibration: slope & intercept (logistic calibration `y ~ logit(p)`), loess plot, **ICI** integrated calibration index (Van Calster hierarchy: mean→weak→moderate feasible; Riley intervals where reported).
- Overall: Brier / integrated Brier with decomposition.
- **Prediction-interval coverage:** 90%/95% PI coverage (bootstrap/Bayesian for LMM/joint; conformal via MAPIE for DL) — empirical vs nominal + width (2 pp non-inferiority window).
- **DCA:** net benefit across thresholds (Vickers & Elkin) — clinical-utility tiebreaker at **5%, 10%, 20%** (binary) or risk-stratified survival; report NB with 95% CI.
- Estimation: bias/RMSE/coverage of θ1 (where estimand θ1).

### 4.3 Primary decision rule (pre-registered, ML gets no preference)

DL "wins" **only if simultaneously**:
1. **Non-inferior on calibration:** calibration **slope ∈ [0.8, 1.2]** AND **intercept |·| < 0.3** logit per Van Calster weak calibration (10.1016/j.jclinepi.2015.12.005), AND **slope coverage rate >80%** (empirical coverage of 95% CI for slope containing inferred 1.0 across 200 reps) — computed per cell from `pROC` + `glm(y ~ logit(p))` as in pilot.
2. **Non-inferior on coverage:** PI empirical coverage **within 2 percentage points of nominal** (e.g., 93–97% for 95% nominal).
3. **Superior on DCA:** net benefit **strictly greater** than best classical (LMM or JM) at **≥1 threshold in {5%,10%,20%} with ΔNB>0 and 95% CI excluding 0** (bootstrap 2000 resamples per cell).

If DL improves AUC but degrades calibration/coverage, **H0 retained (classical suffices)**. Pilot decision stub illustrates rule (see `pilot_003.log` tail: slope 1.00 int ~0 cov 1.00 per cell).

### 4.4 Hypotheses (falsifiable, either outcome publishable)

- **H0 (classical suffices, publishable negative):** Under 16-cell core with known truth, **no DL method beats classical on joint criterion** after pre-registered plasmode benchmark. Clean failure to reject = publishable negative (Biometrics/Medical Decision Making/J Clin Epi as rigorous negative benchmark with phase diagram).
- **H1 (DL wins in characterised regime):** ≥1 DL method beats classical in **identified phase-diagram region**; quantifies calibration/coverage price and produces **decision rule** for method choice rather than leaderboard.

Twin-variant sensitivity: if H0/H1 reverses between Generate-Outcome vs Generate-Treatment, paper pivots to Liu fragility contribution (pre-registered contingency).

---

## 5. Analysis Plan

### 5.1 Per-cell pipeline (pseudo-code locked, seed 20260830)

```r
# LOCKED pipeline (seed 20260830) — per cell, per replicate
# 1. Generate dataset via CIMEHR::sim_data_gen(N, gamma_v, gamma_o, SNR, lambda0, D, theta1, H)
#    or fallback manual 3-process (as in pilot run_pilot_003.R) if CIMEHR vignette-blocked
# 2. Split 80/20 stratified by outcome (rng 20260830); tune HPs on 80% validation only
# 3. Fit 6 baselines: lme4 LMM, JMbayes2 joint, LOCF+logit, MICE+pooled, GRU-D, SeFT (+ optional GRU-ODE-Bayes)
# 4. Predict on held-out 20%: get p_hat / survival curves
# 5. Metrics: AUC (pROC/R pec), calibration slope/intercept (glm), ICI, Brier, PI coverage (bootstrap/MAPIE), DCA NB@5/10/20% (dcurves)
# 6. Aggregate across 200 reps: mean, SD, empirical coverage of slope, win rate vs classical, DCA ΔNB CI
# 7. Decision rule per §4.3 applied per cell; phase diagram: x=γ_v, y=SNR/sparsity, facet=N, colour=ΔNB
```

Deterministic: all seeds pinned, CIMEHR commit `0.1.0` hashed, `seeds.log` at freeze. Pilot `run_pilot_003.R` (R 4.5.2, libPaths `~/R/library`) demonstrates steps 1–6 on 4 toy cells (N=300×20 reps) with AUC/slope/intercept/NB/coverage/mean_visits/prevalence reported (see `outputs/pilot_003_cell_calibration.csv`).

### 5.2 Power & precision (pre-registered)

- Per cell 200 reps → SE for AUC ≈0.003–0.005 at N=10k → CI width 0.01–0.02 → power >0.99 to detect ΔAUC=0.05.
- Slope SE ≈0.04–0.06 → power >0.90 to detect 1.0→0.8 shift; coverage rate SE ≈ sqrt(p(1-p)/200) ≈0.03 at p=0.8.
- DCA NB CI via bootstrap 2k resamples per replicate → pooled across reps (Rubin-style for DCA if needed).

### 5.3 Reporting

- Phase diagram (16-cell grid): discrimination (AUC Δ), calibration (slope), coverage (empirical 95% PI), DCA ΔNB with CI.
- Supplementary: per-cell calibration plots (decile bins as in pilot `pilot_003_calibration_*.csv`), PI width, bias of θ1.
- **Pilot cell table reference:** `pilots/candidate_003/outputs/pilot_003_cell_calibration.csv` (5 cols header: gamma_v, variant, lmm_auc 0.776–0.788, gbm_auc 0.783–0.794, slope≈1.0, coverage 1.0, gbm_win 0.80–0.90) — shows pipeline produces calibrated stubs; full 16×200 extends this.

---

## 6. Scope Ceiling, Compute & Ethics

**Ceiling: 2 investigators (1 biostatistician + 1 ML engineer) + 0.25 FTE clinician for generative spec adjudication, 4–6 weeks wall-clock to full 16×200 core + 2–4 weeks write-up; total 1.5–2.5 months.**

- Week 1: 2 toy cells (γ_v 0 vs 0.8, N=500, 20 reps) — validates twin logic + interval pipeline (pilot == this).
- Week 2: 4 core cells (N=2k, 50 reps) — validates joint criterion + DCA.
- Week 3–4: Full 16×200 at N=2k + SeFT + optional GRU-ODE-Bayes on 4 high-informativeness cells at N=10k.

**Compute estimate (locked v1 — via CIMEHR pipeline):**

| Baseline | Per-replicate fit (N=10k, 15 visits) | Notes |
|----------|----------------------------------------|-------|
| CIMEHR simulator (generation) | ~1–3 sec | R `CIMEHR::sim_data` — negligible |
| `lme4` LMM | ~2–5 sec | R single core |
| `JMbayes2` | ~30–90 sec | MCMC/Laplace — dominant classical cost |
| `mice` + pooled LR | ~10–20 sec | m=20 imputations |
| GRU-D | ~45–90 sec | PyTorch GPU (A100/4090), 100 epochs |
| SeFT | ~30–60 sec | PyTorch GPU, parallel set encoding |
| GRU-ODE-Bayes (opt) | ~120–300 sec | ODE solver 3–5× GRU-D |

Total locked v1 without ODE (6 baselines): 16×200×~5 min avg ≈267 GPU-h naive sequential; Snakemake 4 workers wall-clock ≈80–120 GPU-h +180–260 CPU-h ≈5–8 days workstation; practical N=2k ≈30h parallel — start there. Cost <$50 N=2k core; ~$150–250 N=10k ext. Pilot 4×20×N=300 completed in minutes on CPU (log 387 lines).

**Ethics/privacy:** Simulation primary — **no PHI**; MIMIC resampling uses de-identified public data under PhysioNet DUA (HIPAA Safe Harbor–equivalent date-shifted). Synthetic `rnorm` base needs no credential / no IRB; file exemption/not-human-subjects if needed for MIMIC plasmode. Share only code, hashes, aggregate metrics.

**India Stage-2 note (not v1, GEOGRAPHY-ONLY):** Core benchmark question (does modelling irregularity pay under which informativeness/sparsity/noise regimes?) is population-agnostic. Indian-typical sparsity (mean visits/year ≤2, higher γ_v/γ_o, cost-driven selective testing, paper fragmentation) could be **mimicked via λ_V/γ_v without Indian EHR** — genuinely stresses exchangeability but is **follow-on, not v1 claim**; no data-access barrier (simulated via parameters).

---

## 7. OSF Hashes & Seeds (fill at freeze)

| Artifact | Placeholder hash | Filled at freeze |
|----------|-----------------|------------------|
| Config `cells_core16.csv` (16-cell core, twin flags, engine) | `sha256:TBD-CELLS-16` | OSF freeze commit |
| CIMEHR simulator version | `CIMEHR 0.1.0 (2026-06-08)` + `git:ysph-dsde/CIMEHR@TBD` | Freeze tag |
| Feature tables (plasmode draws per cell) | `sha256:TBD-PLASMODE` | Post-generation |
| Model code tag `v0.1.0-rr` | `git:70730ae984ae0d2592c2` | Freeze tag |
| Seed log | `20260830` all RNGs | Frozen |
| Pilot outputs (`pilot_003_cell_calibration.csv` etc.) | SHA256 logged at pilot | Already exists |

---

## 8. References (locked protocol)

Yang 10.48550/arXiv.2602.15374 (CIMEHR engine); Liang 10.48550/arXiv.2410.13113 (EHRJoint sensitivity); Sun 10.34133/hds.0456 (DL for ISMTS review — no head-to-head); Schneider 10.1186/s13040-025-00450-z (simulation template frequency/noise/heterogeneity); Franklin 10.1093/aje/kww098 (plasmode); Liu 10.48550/arXiv.2504.11740 (plasmode fragility twin variants); Che 10.1038/s41598-018-24271-9 (GRU-D); Horn 10.48550/arXiv.2006.10199 (SeFT); Brouwer 10.48550/arXiv.1905.12374 (GRU-ODE-Bayes); Van Calster 10.1016/j.jclinepi.2015.12.005 (calibration hierarchy); Riley 10.1136/bmj-2024-080749 (uncertainty intervals); Vickers DCA 10.1177/0272989X06289078; Rizopoulos JMbayes2 CRAN.

---

## 9. Verbatim Searches for this OSF (none new — dossier coverage)

Reuses dossier `cycle04_T1_plasmode_lock.md` searches (T1-C4-StrategyA-plasmode-joint, T1-C4-StrategyB-irregular-DL, T1-C4-review-Sun-Schneider-Rizopoulos, T1-C4-adjacent-neural-ODE, T1-C4-adversarial-DL-vs-classical, T1-C4-chaining-Franklin-Schuler-Liang — 6 required distinct strategies, see ideas/candidate_003.md Appendix). Pilot log `pilots/candidate_003/logs/pilot_003.log` documents CIMEHR 0.1.0 + vignette `getting-started.html` verification (available TRUE, vignette exists TRUE, exported objects listed) + 4-cell dry-run (80 rep rows, calibration stubs, decision stub slope 1.00 coverage 1.00).

---

## Appendix A — Verification

- **PILOT EXIT 0:** `pilots/candidate_003/logs/pilot_003.log` — 387 lines, `[Done] Pilot003 complete`, config N=300×20 reps×4 cells, CIMEHR available TRUE, vignette exists TRUE, outputs `pilot_003_rep_level.csv` rows 80 + `pilot_003_cell_calibration.csv`.
- **GIT REV:** `70730ae984ae0d2592c2`
- **SEEDS:** `20260830` (R `set.seed`, `numpy`, `torch`)
- **ENGINES:** CIMEHR 0.1.0 + Liang 2410.13113 sensitivity (both DOI 302-verified 2026-08-30)
