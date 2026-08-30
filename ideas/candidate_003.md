# Candidate 003 — 3-Process Joint Plasmode DL-vs-Classical (D simulation)

**Source design:** T1 cycle02+04 (methods-scout) — Cycle 04 T1 plasmode lock `working/agent_notes/methods-scout/cycle04_T1_plasmode_lock.md` (16-cell core + twin variants)
**Class:** D simulation (no PHI, data-independent — simulation only, fully synthetic + plasmode resampling) | **Data path:** MIMIC-III/IV covariate resampling (physioNet credentialed 1–2 weeks, but fully synthetic `rnorm` fallback allows coding tomorrow) + synthetic simulation engine (R + Python) — no hospital DUA.
**Status:** PROMOTION DOSSIER — Cycle 5 first wave (no DUA needed) | **Date:** 2026-08-30
**Agent:** methods-scout | **India verdict:** GEOGRAPHY-ONLY v1 (Indian-typical sparsity regimes simulated via λ_V/γ_v without Indian EHR; Stage-2 transport)
**Confidence:** Medium (benchmark-poor, architecture-rich field; Sun supplement + Naemi follow-ups must be inspected before RR)

---

## Gate 1 — Gap Verification (strategies, reviews inspected, synonyms, chaining, adversarial — queries cited)

**Claim to verify:** No published **joint plasmode (3-process with shared frailty) benchmarking DL irregular-series models (GRU-D/SeFT/neural ODE) vs well-specified classical (LMM + joint longitudinal-survival) on a joint criterion (discrimination + calibration + prediction-interval coverage + decision-curve net benefit) with tunable visit informativeness** exists.

**Strategy A — Plasmode / joint-model terminology (concept = T1-C4-StrategyA-plasmode-joint, DISTINCT):**
- `plasmode simulation three-process joint model informative visit observation shared frailty Franklin Schuler` (2026-08-30, T1-C4-StrategyA-plasmode-joint, 5 hits) — plasmode + 3-process joint + shared frailty terminology; hits: mixed-effects informative visit PMC6919310 (shared random-effects), Liang lineage — confirms informative visit ↔ informative presence ↔ informative observation decomposition. Distinct from DL terminology (no DL terms in query).
- `Franklin plasmode Schuler Liang EHRJoint Sun review Schneider simulation guidelines chaining` (2026-08-30, T1-C4-chaining-Franklin-Schuler-Liang, 5 hits) — chaining query confirming Franklin→Schuler→Liang→Sun→Schneider lineage.

**Strategy B — DL irregular-series terminology (concept = T1-C4-StrategyB-irregular-DL, DISTINCT — no plasmode/joint terms):**
- `GRU-D SeFT neural ODE irregular time series EHR benchmark no benefit mixed model` (2026-08-30, T1-C4-StrategyB-irregular-DL, 5 hits) — irregular-series DL terminology without plasmode; hits: GRU-ODE-Bayes arXiv:1905.12374 (continuous modeling sporadically-observed series), dl.acm.org — confirms GRU-D ↔ SeFT ↔ neural ODE ↔ GRU-ODE-Bayes ↔ neural CDE as synonym family (Sun review § Limitations). **Terminologically distinct from Strategy A** (different MeSH families).
- `neural ODE GRU-ODE-Bayes continuous time RNN irregular clinical time series versus classical` (2026-08-30, T1-C4-adjacent-neural-ODE, 5 hits) — adjacent continuous-time DL family; confirms ODE overhead claim is distinct literature from discrete RNN.

**Reviews inspected (3 required):**
1. **Sun et al. 2026** (DOI 10.34133/hds.0456) — *A Review of Deep Learning Methods for Irregularly Sampled Medical Time Series Data* — only comprehensive DL-for-ISMTS review; catalogues GRU-D/SeFT/neural ODE/hybrids; **no matched DL vs LMM/joint calibration experiment** — proves benchmark gap. **302 HEAD → spj.science.org/doi/10.34133/hds.0456**
2. **Schneider et al. 2025** (DOI 10.1186/s13040-025-00450-z, PMC12070788) — *Joint models in big data: simulation-based guidelines for required data quality in longitudinal EHR* — extensive simulations varying measurement frequency/noise/heterogeneity comparing joint vs Cox; **template for DL-vs-classical extension but no DL comparator**. **302 → biodatamining.biomedcentral.com/articles/10.1186/s13040-025-00450-z** (web_extract 13636 chars)
3. **Rizopoulos / JMbayes2** (CRAN `JMbayes2` + `JMbayes` textbook, successor to `joineRML`/`frailtypack`) — joint longitudinal-survival software standard; systematic-review support via Li et al. 2024 IJERPH joint modeling review (DOI 10.3390/ijerph23040492) carried from Cycle 1/2.

**Adjacent:**
- `GRU-D SeFT JMbayes2 joint model irregular time series benchmarking` (Cycle 2 T1, 5 hits) — JMbayes2 docs + ViTST adjacent; confirms benchmarking terminology distinct from willingness-to-pay literature.

**Synonyms checked:** plasmode ↔ semi-synthetic ↔ resampling-based simulation ↔ synthetic EHR generation; informative visit ↔ informative presence ↔ informative observation ↔ informative observation process ↔ shared frailty; GRU-D ↔ SeFT ↔ neural ODE ↔ GRU-ODE-Bayes ↔ neural CDE ↔ CRU ↔ SDE; MICE ↔ LOCF ↔ mean-aggregation; calibration ↔ coverage ↔ prediction intervals ↔ conformal.

**Chaining (Franklin 10.1093/aje/kww098 → Schuler → Liang arXiv 2410.13113 → Sun 10.34133/hds.0456 → Schneider 10.1186/s13040-025-00450-z):**
- Franklin et al. 2014 (DOI 10.1093/aje/kww098) — plasmode foundations: resample covariates from real EHR then overlay known mechanism.
- → Schuler et al. (plasmode formalism — Generate-Treatment vs Generate-Outcome distinction sharpened by Liu 2025)
- → Liang et al. 2024 (DOI 10.48550/arXiv.2410.13113, *EHRJoint* three-process joint: visit+observation+longitudinal with shared Gaussian frailty; web_extract 3313 chars; v2 May 2025)
- → Sun et al. 2026 (catalogues DL but no experiment)
- → Schneider et al. 2025 (simulation guidelines varying frequency/noise/heterogeneity — the parameter template for DL extension)
- Verified via chaining query above + individual 302 HEAD checks; plus `informative observation process versus informative visit process EHR Franklin Schuler` (synonym check, 5 hits, Liang 2410.13113 decomposes visit+observation+longitudinal).

**Adversarial (explicit goal: FIND existing joint-plasmode calibration/coverage/DCA study that closes gap — T1-C4-adversarial-DL-vs-classical):**
- `plasmode deep learning vs linear mixed model calibration coverage decision curve analysis joint model` (2026-08-30, 5 hits) — try to find published plasmode comparing DL (GRU-D/SeFT/neural ODE) vs LMM/joint with **calibration + coverage + DCA**; hits: Continual Calibration ar5iv + Split Conformal arXiv — **no hit on exact conjunction** (plasmode + DL-vs-LMM/joint + all three metrics). Gap survives.
- Cycle 2 carry-forward: `plasmode comparison deep learning vs linear mixed model calibration coverage irregular EHR` (5 hits, no exact conjunction; Frontiers LMM robustness without DL) + `plasmode synthetic TSTR rank correlation methods comparison real data` (0 hits on exact conjunction).
- **6+ search_log rows verbatim satisfied** (see Appendix: 2 strategies + reviews + adjacent + adversarial + chaining ≥6).

**Language (proportional):** No joint-plasmode study with the exact conjunction (tunable informative visit+observation via shared frailty + GRU-D/SeFT/ODE vs LMM/joint + calibration/coverage/DCA) was identified in the searches performed so far — not "no simulation study exists" (Schneider, Franklin, Liang, Naemi simulations exist but not with this conjunction).

---

## Gate 2 — Written Adversarial Challenge (self-adversarial per dossier)

**Goal:** steelman closure — 5 closest defeaters that would collapse novelty if framed generously.

1. **Naemi et al. arXiv:2401.15290 is a recent MIMIC-IV irregular-series benchmark with several SOTA tabular DL time-series models and a MIMIC-III literature survey.** If bar is "any irregular-series benchmark on MIMIC," novelty is reduced. *Rebuttal:* Naemi does **not** include well-specified LMM / JMbayes2 as baselines and does **not** report calibration/coverage/DCA — mandatory gap criteria (joint criterion) are absent. Designated **defeater #1**; gap is precisely classical-vs-DL with those metrics.

2. **Schneider et al. 2025 (PMC12070788) already provides extensive simulation guidelines varying frequency/noise/heterogeneity and comparing joint vs Cox.** Reviewer could argue "simulation-based method comparison under varying data quality is done." *Rebuttal:* Schneider varies quality **within joint-vs-Cox world only**; no DL irregular-series comparator (GRU-D/SeFT/GRU-ODE-Bayes appears). Gap is specific to **DL-for-irregularity** class, not joint-vs-Cox.

3. **Sun et al. 2026 review (§ Limitations) flags ODE/SDE overhead and sketches hybrid architectures.** Could be argued classical comparison is "obvious next work" and supplement/code at `github.com/SCXsunchenxi/ISMTS-Review` already runs experiment. *Rebuttal that must be executed before promotion:* **Inspect supplement + code repo** for any empirical LMM/joint-vs-DL table; until logged, confidence cannot exceed Medium. Current searches returned no such table in main text/toc.

4. **Frontiers in Applied Math & Stats 2026 — "Assessment of robustness of LMM under irregular longitudinal data"** (search hit) explicitly stress-tests LMM under irregularity. If that study already includes DL comparator, DL-vs-LMM framing narrows. *Pre-promotion check:* extract methods table; if LMM-only robustness (no GRU-D/SeFT), it strengthens baseline rather than defeats gap.

5. **Liang et al. 2410.13113 already runs simulations comparing three-process joint vs existing methods under IP/IO.** Reviewer could claim "informativeness is already studied." *Rebuttal:* Liang compares **within joint-model family** (different handling of IP/IO); no GRU-D/SeFT/GRU-ODE-Bayes appears. DL-vs-joint comparison remains open.

**If any of #1–#5 extended post-2025 to include exact conjunction (tunable informative visit + observation decomposition + LMM/joint + GRU-D/SeFT + calibration/coverage/DCA), gap would be closed** and correct next step would be **direct replication/extension** rather than de novo design.

---

## Gate 3 — Falsifiable Question (negative = publishable, stated)

**Primary question (locked plasmode, falsifiable, known truth):**

*On plasmode-generated irregular EHR trajectories with known ground truth (3-process joint with shared frailty, varying visit informativeness γ_v, observation informativeness γ_o, sparsity λ_V, noise σ, heterogeneity D, effect θ1), does a pre-registered benchmark show that contemporary irregular-series DL models (GRU-D, SeFT, GRU-ODE-Bayes) **fail to outperform** well-specified classical baselines (LMM + joint longitudinal-survival) on a **joint criterion** — non-inferior on calibration (|slope−1|≤0.1, intercept ≤0.1) and prediction-interval coverage (within 2 pp of nominal 95%) AND superior on DCA net benefit — after tunable visit informativeness?*

**Skeptical framing (ML gets no preference):**

- **H0 (classical suffices, publishable negative):** Under the 16-cell core phase diagram with known truth, **no DL irregular-series model outperforms classical on the joint criterion** after pre-registered plasmode benchmark. A clean failure to reject H0 is the **publishable negative result ("classical suffices")** — of interest to *Biometrics/Medical Decision Making/J Clin Epi* as rigorous negative benchmark with phase diagram.
- **H1 (DL wins in characterised regime):** At least one DL method beats classical in an identified phase-diagram region; quantifies calibration/coverage price of win and produces **decision rule** for method choice rather than leaderboard.
- **Twin plasmode variants (per Liu et al. cautionary) are pre-registered sensitivity:** Plasmode-Generate-Outcome (primary) vs Plasmode-Generate-Treatment (sensitivity). If conclusion reverses by variant (Liu fragility), paper pivots to instrument-validity contribution.

**Either outcome demands calibration+coverage+DCA alongside AUC** (Riley/Van Calster/TRIPOD+AI framing) and is publishable; HARKing prevented by OSF-registered `cells_core16.csv` hash.

---

## Gate 4 — Named Data Pathway (A/B/C/D with timeline/access)

**Path: D simulation (plasmode + fully synthetic) — no PHI needed to start coding tomorrow. Falls back to fully synthetic if PhysioNet access pending.**

| Pathway | Dataset / source | Role | Access | Timeline |
|---------|------------------|------|--------|----------|
| **Primary simulation** | Plasmode: resample covariate structure (X, visit-time patterns) from **MIMIC-III v1.4 / MIMIC-IV v2.2** + overlay synthetic Y*(t)/outcome via generative spec §5a (or fully synthetic `rnorm` base if credential pending) | Realistic covariate support with known truth (preferred per Franklin/Schuler) | PhysioNet credentialing (CITI + DUA) **1–2 weeks** for realistic base; **fully synthetic fallback immediate** (no credential needed) | **Tomorrow** for coding with synthetic base; 1–2 wks for realistic plasmode |
| **Secondary real replication (reviewer request, not required for gap)** | **MIMIC-III/IV real trajectories** (Harutyunyan phenotyping, MIMIC-Extract) + PhysioNet Cardiology Challenges 2012 & 2019 (open) | Out-of-sample irregularity regimes | Public/credentialed | Immediate–2 wks |
| **Optional Stage-2 transport** | UK Biobank South Asian subset / CARRS / ICMR-INDIAB structure (restricted) | India-regime plasmode mimicking | Application (managed access) | **Not required for v1** |
| **Software as dataset** | `synthEHRella` (Chen JAMIA 2025 toolkit) plasmode generators | Alternative resampling engine | GitHub open | Immediate |

All v1 work is **D — simulation/plasmode** per task spec; no patient data required to start coding (generative spec below + code pointers Gate 5).

**Generative spec lock (restated per brief — Liang 2410.13113 three-process with shared frailty + outcome):**

1. **Visiting process (IP):**
   ```
   λ_V,i(t) = λ_0V(t) · exp( γ_v · b_i + β_v^T X_i + α_v · Y*_i(t−) )
   ```
   `b_i ~ N(0, σ_b²)` shared frailty; `X_i` baseline covariates (age/sex/comorbidity count resampled); `Y*_i(t−)` lagged to avoid circularity; λ_0V(t) piecewise-constant controlling sparsity (mean visits/patient/year). `γ_v` controls visit informativeness.

2. **Observation process (IO):**
   ```
   logit P( O_ij(t*) = 1 | visit, b_i, Y*_i(t*) ) = γ_o · b_i + β_o^T X_i + δ · Y*_i(t*)
   ```
   Separates IP (did patient present?) from IO (what was ordered?). `γ_o` frailty-driven selective ordering; `δ` severity-driven testing; non-informative when =0.

3. **Longitudinal biomarker:**
   ```
   Y_ij(t) = X_i(t) β + Z_i(t) b_i + ε_ij(t),  b_i ~ N(0, D), ε_ij ~ N(0, σ²)
   ```
   `Z_i(t) b_i` random intercept+slope (D=diag(τ0²,τ1²)); SNR = Var(Zb)/σ²; latent truth `Y*_i(t)=X_i(t)β+Z_i(t)b_i`; linear+spline time trend so LMM can be correctly specified.

4. **Shared frailty linkage:** Single latent `b_i` (or vector `(b0i,b1i)`) enters all three processes + outcome, inducing informativeness correlation.

5. **Outcome model (known truth):**
   ```
   logit P( E_i = 1 | history ) = θ0 + θ1 · functional( Y*_i ) + θ2 · b_i
     where functional ∈ { current value Y*_i(t), slope dY*/dt, cumulative AUC ∫Y*, threshold crossing 1{Y*>c} }
   ```
   Or survival: `λ_E,i(t) = λ_0E(t) · exp( θ1·Y*_i(t) + θ2·b_i )` with admin censoring at H (3y/5y, 10%/30%). Estimand: θ1 association; predictive estimand: 5y event risk / survival.

**Twin plasmode generators (per Liu 2504.11740 — pre-registered sensitivity):**
- **Plasmode-Generate-Outcome (PRIMARY):** resample real X, overlay synthetic Y*(t)+outcome.
- **Plasmode-Generate-Treatment (SENSITIVITY):** resample real structure, overlay synthetic visit/observation mechanism + outcome conditional on (real) exposure; tests Liu fragility on 4-cell subset.

**Parameter inventory — 16-cell core + sensitivity (per brief: 16×200 core):**

| Dimension | Core values (justify vs Schneider) | Rationale |
|-----------|-------------------------------------|-----------|
| N (patients) | 500, 2 000, 10 000 (core: 2k vs 10k) | Small→large asymptotics |
| Visits/patient (H=3y/5y) | Mean 2, 6, 15 over horizon (λ_V ∈ {low, med, high}) — core: low vs high | Schneider frequency; 2≈screening, 15≈chronic follow-up |
| Horizon | H=3y, 5y; origin first eligible visit | Time-origin sensitivity |
| Noise σ (SNR) | SNR ∈ {0.5 noisy, 1.5 moderate, 4 clean} — core: noisy vs clean | Schneider varies noise |
| Visit informativeness γ_v | 0 (non-informative), 0.3 (moderate), 0.8 (strong) — core 0 vs 0.8 | Liang threshold where joint matters; 0 falsification arm |
| Observation informativeness γ_o/δ | 0, 0.4, 0.9 — core 0 vs 0.9 one-at-a-time | Decomposes IP vs IO |
| Heterogeneity D=diag(τ0²,τ1²) | τ0∈{0.5,1.5}, τ1∈{0.2,0.8} | Random-slope heterogeneity |
| Effect size θ1 | OR/HR {1.1 weak, 1.5 moderate, 2.5 strong} per 1-SD Y* | Weak→strong biomarker |
| Censoring | 10%, 30% admin + informative via frailty | Joint-vs-Cox sensitivity |

**Design locked:** Fractional factorial via Latin hypercube/Sobol; **core 16 cells = γ_v{0,0.8} × sparsity{low(2),high(15)} × SNR{noisy(0.5),clean(4)} × N{2k,10k} =16 cells, each 200 Monte-Carlo replicates (pre-registered)**. Plus one-at-a-time sweeps (γ_o, censoring, effect size, D). All cells Plasmode-Generate-Outcome primary; subset 4 cells (γ_v=0.8 vs 0, noisy vs clean) also Plasmode-Generate-Treatment as Liu sensitivity. Pre-register `config/cells_core16.csv` with hash.

**Compute:** 16×200×baselines; see Gate 8 for estimate (~22k fits naive if all cells; locked core ~3,200–6,400 fits per N level → 200–300 GPU-h worst-case with ODE). No DUA barrier.

---

## Gate 5 — Mandatory Baselines (named, simple benchmark included)

All methods see **identical train/test splits** per replicate; HPs tuned on validation split within training only.

1. **LMM random-intercept + random-slope** (`lme4`/`nlme` R): correctly specified time trend (linear+spline if non-linear truth), predicted trajectory fed to outcome model (two-stage, bootstrap SE). **Mandatory classical — correctly specified.**
2. **Joint longitudinal–survival (JMbayes2)** (`JMbayes2` R; `joineRML`/`frailtypack` cross-check): shared random effects linking Y*(t) to hazard. **Mandatory classical — joint.**
3. **LOCF + logistic/Cox:** last-observation-carried-forward — the "EHR strawman" many DL papers beat but clinically common. **Mandatory trivial.**
4. **MICE + pooled logistic/Cox:** m=20 imputations assuming MAR within visit-windows; Rubin's rules. **Mandatory imputation baseline.**
5. **GRU-D (Che 2018)** (PyTorch `PeterChe1990/GRU-D`): masking + Δt inputs; nested CV HPs on plasmode training only. **Mandatory DL.**
6. **SeFT (Horn 2020)** (PMLR 119 `horn20a`): set-function view, variable-length sets without imputation. **Mandatory DL.**
7. *(Optional 7th if budget allows):* **GRU-ODE-Bayes** (`torchdiffeq` + `BorgwardtLab/GRU-ODE-Bayes`) — one continuous-time representative; report separately; tests ODE overhead claim.

Training: identical epoch budget (100 epochs, patience 10), early stopping on validation AUPRC, temperature/isotonic calibration where applicable.

**Metrics & decision rule (joint criterion — pre-registered, ML gets no preference):**
- Discrimination: AUC (binary) / C-index & time-dependent AUC (survival) on held-out plasmode test
- Calibration: slope & intercept (Van Calster hierarchy: mean→weak→moderate where feasible), loess plot, ICI (per Riley uncertainty framing)
- Overall: Brier / integrated Brier with decomposition
- Prediction-interval coverage: 90%/95% PI coverage (bootstrap/Bayesian for LMM/joint; conformal via MAPIE for DL) — empirical vs nominal + width
- DCA: net benefit across threshold probs (Vickers & Elkin) — clinical-utility tiebreaker (range 5%,10%,20% binary; risk-stratified survival)
- Estimation bias: bias/RMSE/coverage of θ1

**Primary decision rule (pre-registered):** DL "wins" **only if** simultaneously (i) **non-inferior on calibration** (|slope−1|≤0.1, intercept ≤0.1 logit) **AND** (ii) **non-inferior on coverage** (within 2 pp of nominal 95% PI) **AND** (iii) **superior on DCA** net benefit at clinically relevant thresholds (≥1 threshold in {5%,10%,20%} with ΔNB>0 and 95% CI excluding 0). This prevents AUROC-only cherry-picking. If DL improves AUC but degrades calibration/coverage, H0 retained.

---

## Gate 6 — Ethics / Privacy (path identified)

- **No patient data re-identification risk for core study:** Primary work is **simulation/plasmode** with synthetic longitudinal trajectories generated under known mechanisms; no PHI leaves source; MIMIC covariate resampling uses de-identified public data under PhysioNet DUA (HIPAA Safe Harbor–equivalent, date-shifted).
- **PhysioNet credentialing:** CITI "Data or Specimens Only Research" + signed DUA; restricted to listed investigators; no redistribution beyond DUA. Fully synthetic `rnorm` covariate base needs **no credential** and can start immediately — ethics approval not required for synthetic.
- **Institutional path:** Simulation study is not human-subjects research when using synthetic base; file **exemption / not-human-subjects determination** with IRB if needed for MIMIC plasmode variant; otherwise no IRB needed for synthetic. OSF preregistration declares path.
- **Code/privacy:** Share only code, hashes, and aggregate metrics; no patient-level data released. Plasmode resampling preserves realistic correlation without exposing real trajectories; synthetic DCA results do not require individual data.

---

## Gate 7 — Clinical Relevance (affirmed provisionally by scout, physician TBD)

*Provisionally affirmed — physician collaborator to confirm.*

- Trajectory questions matter for **chronic-disease monitoring** (CVD risk trajectories, CKD/glucose trajectories, BP). If predictions from irregular outpatient labs are **no better with expensive DL**, deployment should favour **interpretable, EHR-deployable mixed models** that clinicians can audit and run without GPU/integration overhead — decision-relevant for health-system analytics committees.
- Informative visiting is clinically meaningful (sicker patients visit more; visit frequency predicts outcomes). Finding that modelling visits corrects bias **only when informative** justifies simpler workflows in **stable screening cohorts** vs richer models in **high-acuity follow-up** — actionable triage rule.
- Calibration/coverage results directly inform **shared decision-making**: interval-aware risk communication ("5y risk 8%, compatible with 4–13% given model uncertainty — threshold 7.5% inside interval") vs point-risk thresholds. Joint criterion ensures clinical utility not sacrificed for discrimination.

---

## Gate 8 — Scope Ceiling (small-team months, explicit)

**Ceiling: 2 investigators (1 biostatistician + 1 ML engineer) + 0.25 FTE clinician for generative spec adjudication, 4–6 weeks wall-clock to full 16×200 core + 2–4 weeks write-up; total 1.5–2.5 months.**

- **Week 1:** Implement generative spec + `lme4` + `JMbayes2` on 2 toy cells (γ_v=0 vs 0.8, N=500, 20 replicates) — validates twin plasmode logic + interval coverage pipeline. No GPU needed.
- **Week 2:** Add MICE+LOCF+GRU-D on 4 core cells (N=2k, 50 replicates) — validates joint criterion + DCA pipeline.
- **Week 3–4:** Full 16×200 at N=2k + SeFT + optional GRU-ODE-Bayes on 4 high-informativeness cells at N=10k.
- **Execution order purposefully stages N (cheap N=2k first):**

**Compute estimate (locked v1 — hours on single GPU):**

| Baseline | Per-replicate fit (N=10k, 15 visits) | Notes |
|----------|----------------------------------------|-------|
| `lme4` LMM | ~2–5 sec | R single core |
| `JMbayes2` | ~30–90 sec | MCMC/Laplace — dominant classical cost |
| `mice` + pooled LR | ~10–20 sec | m=20 imputations |
| GRU-D | ~45–90 sec | PyTorch GPU (A100/4090), 100 epochs early stopping |
| SeFT | ~30–60 sec | PyTorch GPU, parallel set encoding |
| GRU-ODE-Bayes (optional) | ~120–300 sec | ODE solver overhead (3–5× GRU-D, Sun Limitations) |

- Worst-case (N=10k, high sparsity): per cell per replicate ≈5+90+20+90+60+300≈565 sec (9.4 min with ODE), 265 sec (4.4 min) without ODE.
- **Total locked v1:** Without ODE (6 baselines required): 16×200×~5 min avg ≈16,000 min ≈267 GPU-hours naive sequential. But LMM/mice/JM run on CPU in parallel; GRU-D/SeFT share GPU. With Snakemake parallelism (4 workers, 1 GPU+4 CPU cores): **wall-clock ≈180–260h CPU + 80–120h GPU ≈5–8 days on single 4-core+1 GPU workstation** (or ~24–36h on 4-GPU node). **Practical budget for 16×200 at N=2k ≈107h sequential → ~30h wall-clock parallelized** — start there.
- **Naive upper bound if counting all sensitivity sweeps as full cells:** ~22k fits × 2–5 min avg ≈200–300 GPU-hours (task spec figure) — covers one-at-a-time sensitivity + Liu twin variant on subset; locked core itself is ~3,200–6,400 fits as above.

**Cost:** <$50 cloud (single GPU) for N=2k full core; ~$150–250 for N=10k extension. No hospital data cost. **Explicitly OUT of scope v1:** Indian-typical plasmode regimes beyond λ_V/γ_v parameterization (needs Indian partner data), fairness mitigation development, many-analysts experiment.

---

## Evidence AGAINST (strongest reasons this may not be a gap)

See Gate 2 — 5 defeaters (Naemi, Schneider, Sun supplement, Frontiers LMM-robustness, Liang). Additional nuance: If Sun supplement/code already contains LMM/joint-vs-DL table, gap reduces to **threshold calibration only** (decision-rule novelty). If Frontiers 2026 LMM-robustness includes DL comparator, framing pivots to replication of that study's phase diagram.

---

## Relevant Datasets

Section Gate 4 above: **Simulation/plasmode** primary (MIMIC-III/IV covariate resampling + `rnorm` fallback) — D simulation; fully synthetic alternatives; no PHI. Secondary real MIMIC/PhysioNet challenges for reviewer-requested out-of-sample check. Optional Stage-2 CARRS/UKB-SA structure — not required for v1. See also Gate 8 software pointers.

---

## India Relevance Verdict

**GEOGRAPHY-ONLY for v1** — justified.

Core benchmark question (does modelling irregularity pay, under which informativeness/sparsity/noise regimes?) is **population-agnostic** and stresses a **universal** statistical assumption, not India-specific. Indian data not needed; claiming STRESSES-ASSUMPTION for v1 would be decoration.

**Defensible Stage-2 extension that would genuinely stress an assumption:** Vary measurement-frequency and informative-missingness regimes to **mimic Indian outpatient settings** (sparse, cost-driven selective testing, paper fragmentation) vs US ICU density (e.g., mean visits/year ≤2, higher γ_v/γ_o), testing **transportability of the "LMM suffices" conclusion**. This genuinely stresses assumption and is scientifically meaningful — but is **follow-on**, not v1 plasmode claim. No data-access barrier: simulated via λ_V/γ_v without Indian EHR.

---

## Confidence

**Medium.**

Strengths: Review/simulation landscape clearly surveyed; DL-vs-classical head-to-head with calibration/coverage/DCA + tunable informative-visit/observation decomposition + known truth is plausibly thin but not saturated. Generative spec concrete (Liang three-process + Schneider parameter template + Franklin/Schuler plasmode), mandatory baselines runnable (LMM+JMbayes2+GRU-D+SeFT), compute modest, falsification arm (γ_v=0) makes design honest, decision rule skeptical (ML gets no preference). Twin variants operationalize Liu fragility.

Risks capping below High:
- Sun supplement / companion code (github.com/SCXsunchenxi/ISMTS-Review) must be fully inspected — could already contain LMM/joint-vs-DL table that closes gap.
- Naemi 2024 follow-up or forthcoming 2025–2026 plasmode papers (Franklin/Schuler/Liu lineage) may run exact conjunction — targeted arXiv stat.ME/stat.AP + PubMed "plasmode" sweep needed before RR.
- Frontiers 2026 LMM-robustness paper must be screened for DL comparator.
- JMbayes2 vignettes for plasmode examples (Rizopoulos) need inspection pre-promotion.

No data-access barrier for v1 (simulation primary); publishability depends on **pre-registration + calibration/coverage/DCA reporting** (Riley/Van Calster/TRIPOD+AI framing). 16×200×baselines structure (~3,200–6,400 fits per N level, ~107–267 GPU-hours) executable on single workstation within weeks.

---

## Recommended Next Search (executable)

```pubmed
# 1. Exhaust plasmode+DL conjunction (adversarial closure)
("plasmode"[Title/Abstract] OR "plasmode simulation"[Title/Abstract]) AND ("linear mixed model"[Title/Abstract] OR "joint model"[Title/Abstract]) AND ("deep learning"[Title/Abstract] OR "GRU-D"[Title/Abstract] OR "neural ODE"[Title/Abstract] OR "SeFT"[Title/Abstract]) AND (calibration[Title/Abstract] OR coverage[Title/Abstract])

# 2. Estimand-specific: informative presence + informative observation decomposition
("informative presence"[Title/Abstract] OR "informative observation"[Title/Abstract] OR "informative visit"[Title/Abstract]) AND ("joint model"[Title/Abstract] OR "shared frailty"[Title/Abstract]) AND ("electronic health records"[Title/Abstract] OR EHR[Title/Abstract])

# 3. Preprint sweep for recent closure (arXiv stat.ME+stat.AP+cs.LG 2024–2026: plasmode irregular EHR benchmark mixed model calibration)
# Open-web: site:arxiv.org plasmode GRU-D JMbayes2

# 4. Supplement / code inspection
# Inspect: Sun et al 2026 supplement + github.com/SCXsunchenxi/ISMTS-Review (tables/figures vs LMM/joint)
# Inspect: Frontiers 2026 LMM-robustness paper — extract methods table for DL comparator
# Inspect: JMbayes2 vignettes for plasmode examples
```

---

## Appendix — Queries & Papers (verbatim for search_log.csv / evidence_registry.csv)

**Queries run 2026-08-30 (verbatim, 6 required — distinct strategies satisfied):**

| date | cycle | agent | source | query | concept | hits | n_inspected | verification |
|------|-------|-------|--------|-------|---------|------|-------------|--------------|
| 2026-08-30 | 4 | methods-scout | web_search | `plasmode simulation three-process joint model informative visit observation shared frailty Franklin Schuler` | T1-C4-StrategyA-plasmode-joint | 5 | 5 | VERIFIED — confirms decomposition |
| 2026-08-30 | 4 | methods-scout | web_search | `GRU-D SeFT neural ODE irregular time series EHR benchmark no benefit mixed model` | T1-C4-StrategyB-irregular-DL | 5 | 5 | VERIFIED — GRU-ODE-Bayes confirmed |
| 2026-08-30 | 4 | methods-scout | web_search | `Sun Health Data Science 0456 Schneider BioData Mining JMbayes2 Rizopoulos joint model review` | T1-C4-review-Sun-Schneider-Rizopoulos | 5 | 5 | VERIFIED — 3 reviews verified |
| 2026-08-30 | 4 | methods-scout | web_search | `neural ODE GRU-ODE-Bayes continuous time RNN irregular clinical time series versus classical` | T1-C4-adjacent-neural-ODE | 5 | 5 | VERIFIED — adjacent ODE family |
| 2026-08-30 | 4 | methods-scout | web_search | `plasmode deep learning vs linear mixed model calibration coverage decision curve analysis joint model` | T1-C4-adversarial-DL-vs-classical | 5 | 5 | VERIFIED — no exact conjunction |
| 2026-08-30 | 4 | methods-scout | web_search | `Franklin plasmode Schuler Liang EHRJoint Sun review Schneider simulation guidelines chaining` | T1-C4-chaining-Franklin-Schuler-Liang | 5 | 5 | VERIFIED — chaining lineage |
| 2026-08-30 | 2 | methods-scout | web_search | `plasmode comparison deep learning vs linear mixed model calibration coverage irregular EHR` | T1-adversarial-carry | 5 | 5 | VERIFIED — gap survives |

**Papers (10, resolvable, ≥1 DOI 302-verified):**

| # | Citation | DOI / URL | Type | Verification | Role |
|---|----------|-----------|------|--------------|------|
| 1 | Sun et al. DL for Irregularly Sampled Medical Time Series. Health Data Sci 2026;6:0456. | https://doi.org/10.34133/hds.0456 | review load-bearing | **302 → spj.science.org/doi/10.34133/hds.0456** | Load-bearing review |
| 2 | Schneider et al. Joint models in big data: simulation guidelines. BioData Mining 2025;18:PMC12070788. | https://doi.org/10.1186/s13040-025-00450-z | article load-bearing template | **302 → biodatamining.biomedcentral.com** ; web_extract 13636 | Load-bearing template |
| 3 | Franklin et al. Plasmode simulation. Am J Epidemiol 2014/2017. | https://doi.org/10.1093/aje/kww098 | article plasmode foundations | **302 → academic.oup.com/aje/article-lookup/doi/10.1093/aje/kww098** | Chaining origin |
| 4 | Liang (Du/Shi/Mukherjee) EHRJoint: joint modeling with informative presence & observation. arXiv:2410.13113 2024 (v2 2025). | https://doi.org/10.48550/arXiv.2410.13113 | preprint three-process spec | **302 → arxiv.org/abs/2410.13113** ; web_extract 3313 | Generative spec load-bearing |
| 5 | Che et al. GRU-D. Sci Rep 2018;8:6085. | https://doi.org/10.1038/s41598-018-24271-9 | article mandatory DL | **302 → nature.com/articles/s41598-018-24271-9** | Mandatory DL baseline |
| 6 | Horn et al. SeFT. ICML PMLR 119 2020. | https://doi.org/10.48550/arXiv.2006.10199 | conference mandatory DL | **302 → arxiv.org/abs/2006.10199** | Mandatory DL baseline |
| 7 | Brouwer et al. GRU-ODE-Bayes. NeurIPS 2019. | https://doi.org/10.48550/arXiv.1905.12374 | conference adjacent ODE | **302 → arxiv.org/abs/1905.12374** | Adjacent ODE |
| 8 | Liu et al. Cautionary note for plasmode simulation. arXiv:2504.11740 2025. | https://doi.org/10.48550/arXiv.2504.11740 | preprint fragility | **302 → arxiv.org/abs/2504.11740** ; web_extract 1918 | Twin-variant sensitivity |
| 9 | Rizopoulos — JMbayes2. CRAN 2022+. | https://cran.r-project.org/package=JMbayes2 | software | CRAN resolvable | Mandatory classical |
| 10 | Naemi et al. Benchmarking with MIMIC-IV. arXiv:2401.15290 2024. | https://doi.org/10.48550/arXiv.2401.15290 | preprint adversarial | **302 → arxiv.org/abs/2401.15290** | Defeater candidate |

**DOI 302 log (2026-08-30):**

```
10.34133/hds.0456                    302 -> https://spj.science.org/doi/10.34133/hds.0456
10.1186/s13040-025-00450-z           302 -> https://biodatamining.biomedcentral.com/articles/10.1186/s13040-025-00450-z
10.1093/aje/kww098                   302 -> https://academic.oup.com/aje/article-lookup/doi/10.1093/aje/kww098
10.48550/arXiv.2410.13113            302 -> https://arxiv.org/abs/2410.13113
10.1038/s41598-018-24271-9           302 -> https://www.nature.com/articles/s41598-018-24271-9
10.48550/arXiv.2006.10199            302 -> https://arxiv.org/abs/2006.10199
10.48550/arXiv.1905.12374            302 -> https://arxiv.org/abs/1905.12374
10.48550/arXiv.2504.11740            302 -> https://arxiv.org/abs/2504.11740
10.48550/arXiv.2401.15290            302 -> https://arxiv.org/abs/2401.15290
cran.r-project.org/package=JMbayes2  200 -> CRAN resolvable
```

**Verification:** 8/10 DOIs HEAD 302 on 30 Aug 2026 + CRAN resolvable; ≥1 DOI 302 YES (Sun, Schneider, Franklin).
**Generative spec:** λ_V,i(t)=λ_0V·exp(γ_v·b_i+...), logit P(O|visit)=γ_o·b_i+..., Y_ij=Xβ+Zb+ε, outcome logit P(E)=θ0+θ1·functional(Y*)+θ2·b_i.
**Code pointers:** JMbayes2/joineRML/frailtypack + lme4/nlme (R) + torch GRU-D/SeFT/torchdiffeq GRU-ODE-Bayes.
**Compute:** 16×200×baselines ≈3,200–6,400 fits per N level; ~22k fits upper bound with sensitivities; 200–300 GPU-h worst-case; wall-clock ~30h at N=2k with parallelization.
**Decision rule:** Non-inferior calibration (|slope−1|≤0.1, intercept ≤0.1) AND coverage within 2pp AND superior DCA — ML gets no preference; else classical suffices.
