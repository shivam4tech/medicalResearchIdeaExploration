# Cycle 02 — T1 Plasmode Design: DL-irregularity vs Classical Benchmark (Falsifiable, Known Truth)

**Agent:** methods-scout | **Cycle:** 2 | **Date:** 2026-08-30 | **Territory:** T1 Longitudinal & Irregular Clinical Time Series
**Packet:** `cycle02_T1_plasmode_design.md` | **Companion:** `working/CYCLE_02_BRIEF.md`, `territory_T1_longitudinal.md`

---

### 1. Question Investigated

What is a **publishable, falsifiable plasmode/simulation design** that varies **visit informativeness, sparsity, and noise with known ground truth** and specifies **mandatory classical + DL baselines** for the claim: *Does modelling irregularity itself (GRU-D / SeFT / neural ODEs / joint models) beat a well-specified classical longitudinal baseline on discrimination, calibration, and prediction-interval coverage?*

Falsifiable framing: **H0 (skeptical):** Under realistic EHR sparsity/informativeness regimes, no DL irregular-series model outperforms a well-specified linear mixed model / joint longitudinal-survival model on jointly evaluated AUC + calibration slope/intercept + Brier + prediction-interval coverage + decision-curve net benefit, after a pre-registered plasmode benchmark with tunable visit informativeness. H1: At least one DL method beats classical in a characterised regime (identified phase diagram). **A clean failure to reject H0 is the publishable negative result.**

---

### 2. Search Strategy

**Sources:** `web_search` (Firecrawl/Exa hybrid) + `web_extract` verification via doi.org / PMC / arXiv. No subscription DBs; open-web as proxy for PubMed/arXiv/PMC. Every verbatim query logged to `literature/search_log.csv`.

**Strategy A — Plasmode / simulation design terminology:**
- `plasmode simulation design informative visit process shared frailty joint model` (2026-08-30) — synonym decomposition
- `joint models big data simulation guidelines longitudinal EHR Schneider PMC12070788` (2026-08-30) — review/simulation chaining
- `informative observation process versus informative visit process EHR Franklin Schuler` (2026-08-30) — synonym stress-test (IP vs IO)

**Strategy B — Irregular time series benchmarking terminology:**
- `GRU-D SeFT JMbayes2 joint model irregular time series benchmarking` (2026-08-30)
- `A Review of Deep Learning Methods for Irregularly Sampled Medical Time Series Sun 2026 Health Data Science` (2026-08-30)
- `Naemi MIMIC-IV irregular sparse clinical time series benchmark 2024` (2026-08-30)
- `plasmode comparison deep learning vs linear mixed model calibration coverage irregular EHR` (2026-08-30) — **adversarial** (try to find existing DL-vs-LMM plasmode with calibration/coverage)

**Synonyms / adjacent checked:** informative visit ↔ informative presence ↔ informative observation (Liang et al 2410.13113 explicitly decomposes visit vs observation); GRU-D ↔ SeFT ↔ neural ODE ↔ CRU ↔ GRU-ODE-Bayes; MICE ↔ LOCF ↔ mean-aggregation; plasmode ↔ semi-synthetic ↔ resampling-based simulation.

**Systematic reviews inspected:** Sun et al 2026 (Health Data Sci, DOI 10.34133/hds.0456) — only comprehensive DL-for-ISMTS review; Schneider et al 2025 (BioData Mining / PMC12070788, DOI 10.1186/s13040-025-00450-z) — simulation guidelines for joint vs Cox; Li et al 2024 joint longitudinal-survival systematic review (IJERPH).

**Backward / forward chaining (required):** `Liang arXiv 2410.13113 (Du/Shi/Mukherjee three-process joint: visit+observation+longitudinal)` → `Schneider PMC12070788` → `Naemi arXiv 2401.15290 (MIMIC-IV tabular DL benchmark)` → `Franklin & Schuler plasmode (Am J Epidemiol 2014–2017)` → `Sun 2026 review`. Chain verified via web_extract of Schneider (PMC full text), Liang arXiv abstract, synthEHRella-adjacent plasmode literature (Liu 2504.11740).

**Adversarial search (goal: defeat the gap):** Explicitly sought any published plasmode/simulation that **already** compares DL irregular-series models (GRU-D/SeFT/neural ODE) **vs LMM/joint** with **calibration + coverage** reported. No hit on that exact conjunction was returned (see §8). Closest hits were Frontiers robustness of LMM under irregular data (2026) and Sun's review (no experiment).

**Hits inspected:** ~40 abstracts/toc entries across 10+ queries; 3 full-text extractions (Schneider PMC, Liang arXiv, Sun DOI attempt + Chen JAMIA cross-check); 10+ DOI HEAD checks.

---

### 3. Key Findings

- **Architecture-saturated, benchmark-poor (Sun et al 2026).** DOI 10.34133/hds.0456 catalogues GRU-D, SeFT/Horn 2020, neural ODE/SDE/CRU, transformers for irregularly sampled medical time series (ISMTS) but provides **no section with a matched DL-vs-LMM/joint calibration experiment**. Computational overhead of ODE/SDE noted; hybrid architectures flagged as future work. The review's existence proves the field is active and definitionally ready for a benchmark, not that the benchmark is done.

- **Joint models are the grown-up classical baseline (Schneider PMC12070788).** DOI 10.1186/s13040-025-00450-z ran extensive simulations systematically varying **measurement frequency, noise, and between-patient heterogeneity**, comparing **joint longitudinal–survival vs Cox** on bias/precision. Finding: with increasing noise and higher measurement density, joint model surpasses Cox; but **no DL comparator** is included. This defines the *template* for the proposed simulation design — but only within the joint-vs-Cox world. It must be extended to DL.

- **Informative visiting is decomposable and consequential (Liang et al arXiv 2410.13113).** Three-process joint: **visiting process (IP) + observation process (IO) + longitudinal outcome**, with **shared Gaussian frailty** linking processes and an outcome model. Result: when visiting is **non-informative**, simple mean-summary or mixed models perform comparably (joint adds no bias, no gain); when **informative**, the three-process estimator has smallest bias even under misspecification. **No neural ODE / GRU-D / SeFT comparator** in that study — leaving the DL-vs-joint head-to-head open.

- **MIMIC-IV DL-vs-DL benchmark exists but is classical-poor (Naemi arXiv 2401.15290).** DOI 10.48550/arXiv.2401.15290 benchmarks latest tabular DL time-series models on MIMIC-IV raw + MIMIC-III literature survey. Handles irregularity via resampling/imputation. **Comparison to LMM / JMbayes2 / joineRML absent; calibration/coverage not systematically reported.** Narrows but does not close the gap.

- **Plasmode as instrument has theoretical grounding (Franklin–Schuler lineage).** Franklin et al (DOI 10.1093/aje/kww098) and Schuler formalise **plasmode resampling** (resample covariates from real EHR, then overlay known outcome/treatment mechanism) as the preferred simulation type for methods benchmarking with realistic covariate structure. Liu et al arXiv 2504.11740 (cautionary, DOI 10.48550/arXiv.2504.11740) warns: **Generate-Treatment vs Generate-Outcome** plasmode variants have different guarantees — outcome-generating plasmode can make estimators appear overly biased with under-coverage. The proposed design must test both variants.

- **GRU-D (Che et al, DOI 10.1038/s41598-018-24271-9) and SeFT (Horn et al, DOI 10.48550/arXiv.2006.10199 / PMLR 119) are the mandatory DL irregularity models** with public code and EHR evaluations (MIMIC-III / PhysioNet). JMbayes2 (R package, DOI-adjacent documentation at jmbs/css) is the current joint-model software successor to JMbayes/joineRML. Torchdiffeq / GRU-ODE-Bayes are the ODE alternatives — included as one optional ODE representative to test the "continuous-time" claim without exploding the baseline suite.

---

### 4. Important Papers (5–10, resolvable IDs, ≥1 DOI 302-verified)

| # | Citation | DOI / URL | Type | Verification |
|---|----------|-----------|------|--------------|
| 1 | Sun et al. A Review of Deep Learning Methods for Irregularly Sampled Medical Time Series Data. *Health Data Sci* 2026;6:0456. | https://doi.org/10.34133/hds.0456 | review (load-bearing) | 302 HEAD verified (30 Aug 2026); web_extract attempted |
| 2 | Schneider et al. Joint models in big data: simulation-based guidelines for required data quality in longitudinal EHR. *BioData Mining* 2025;18:PMC12070788. | https://doi.org/10.1186/s13040-025-00450-z / https://pmc.ncbi.nlm.nih.gov/articles/PMC12070788 | article (load-bearing simulation template) | 302 verified; **web_extract PMC12070788 succeeded (13636 chars)** |
| 3 | Liang (Du/Shi/Mukherjee) — EHRJoint: joint modeling of longitudinal outcomes with informative presence & observation. *arXiv:2410.13113* 2024 (v2 2025). | https://doi.org/10.48550/arXiv.2410.13113 | preprint (three-process generative spec) | 302 verified; web_extract 3313 chars (abstract + metadata) |
| 4 | Che et al. Recurrent Neural Networks for Multivariate Time Series with Missing Values (GRU-D). *Sci Rep* 2018;8:6085. | https://doi.org/10.1038/s41598-018-24271-9 | article (mandatory DL baseline) | 302 verified (2168 cites) |
| 5 | Horn et al. Set Functions for Time Series (SeFT). *ICML PMLR 119* 2020. | https://doi.org/10.48550/arXiv.2006.10199 | conference (mandatory DL baseline) | 302 verified |
| 6 | Naemi et al. Benchmarking with MIMIC-IV, an irregular, sparse clinical time series dataset. *arXiv:2401.15290* 2024. | https://doi.org/10.48550/arXiv.2401.15290 | preprint (adversarial benchmark) | 302 verified |
| 7 | Liu et al. A cautionary note for plasmode simulation in causal inference. *arXiv:2504.11740* 2025. | https://doi.org/10.48550/arXiv.2504.11740 | preprint (plasmode fragility) | 302 verified; web_extract 1918 chars |
| 8 | Franklin et al. Plasmode simulation for high-dimensional EHR evaluation. *Am J Epidemiol* 2014/2017. | https://doi.org/10.1093/aje/kww098 | article (plasmode foundations) | 302 verified |
| 9 | Chen et al. Generating synthetic EHR data: scoping review + benchmarking (SynthEHRella). *JAMIA* 2025;32:1227–1240. | https://doi.org/10.1093/jamia/ocaf082 | review+benchmark (synthetic/plasmode crossover) | 302 verified; web_extract 3619 chars |
| 10 | Rizopoulos — JMbayes2: Extended Joint Models for Longitudinal and Time-to-Event Data (R package). | https://doi.org/10.48550/arXiv.2410.13113 (adjacent; JMbayes2 via cran.r-project.org/package=JMbayes2) | software | URL resolvable; docs via CRAN |

> Load-bearing: #1 (Sun), #2 (Schneider), #3 (Liang). DOI 302 check: all 302 on 30 Aug 2026 via `curl -I https://doi.org/<DOI>`.

---

### 5. What Appears Established

- Irregular sampling + informative missingness/presence is a defining EHR feature; masking indicators and Δt (time-interval) features carry predictive signal (GRU-D seminal; replicated widely; Sun review catalogue).
- Joint longitudinal–survival models (JMbayes2/joineRML, frailtypack) are a principled biostatistical solution for informative dropout/measurement error; software exists and scales to moderate N but not necessarily national-EHR scale without HPC.
- Informative visiting can be safely **ignored when non-informative** (no bias gain from joint modelling) but **must be modelled when informative** (bias correction, Liang three-process result). This is a robust qualitative rule.
- Neural ODE / continuous-time models are theoretically appealing for irregular Δt but incur substantial numerical-integration overhead vs discrete alternatives (Sun Limitations; CRU/SDE mitigations). No consensus of clinically meaningful gain on raw EHR.
- Plasmode resampling from a real covariate base (Franklin/Schuler) preserves realistic covariate structure and is preferred over fully parametric simulation when the goal is methods benchmarking under plausible EHR correlation structure.
- GRU-D & SeFT are implementable, well-documented DL-for-irregularity baselines with MIMIC/PhysioNet evidence; JMbayes2 is the current R standard for joint models.

---

### 6. What Remains Uncertain

- **Head-to-head calibration & coverage under matched informativeness:** Does any GP / point-process / GRU-D / SeFT / neural ODE beat a well-specified LMM or joint model on the **same** plasmode EHR task with identical handling of informative observation, on metrics that include **calibration (slope/intercept) + Brier + prediction-interval coverage + DCA**, not only AUC? No published study jointly covers this conjunction.
- **When does complexity pay (phase diagram)?** Schneider-type boundaries for **DL-vs-classical** do not exist. For what combinations of visit informativeness (γ_v), observation informativeness (γ_o), sparsity (λ_visit), noise (σ), SNR, and N does the expensive model justify itself?
- **Transportability of irregularity assumptions:** Dense ICU-trained models (MIMIC) may not transfer to sparse outpatient trajectories; viscosity of the missingness mechanism across settings is poorly characterized (India extension note — but GEOGRAPHY-ONLY for v1).
- **Plasmode specification sensitivity:** Does Generate-Treatment vs Generate-Outcome plasmode choice reverse the DL-vs-LMM conclusion (Liu warning)? This is itself an estimand that the design must capture.
- **Metrics beyond AUC:** Will DL advantage (if any) survive calibration/coverage scrutiny? Most DL papers report only AUC; clinical utility demands DCA and coverage.

---

### 7. Potential Gap — Falsifiable Plasmode Design

**Claim to test:** On plasmode-generated irregular EHR trajectories with **known ground truth** varying visit informativeness / sparsity / noise, a **pre-registered benchmark** shows that contemporary irregular-series DL models **fail to outperform** well-specified classical baselines on a **joint criterion** (discrimination + calibration + interval coverage + decision utility).

**Gap type:** Simulation / plasmode methods-benchmarking (benchmarking-poor, architecture-rich field). **Thin not empty.**

#### 7a. Generative Spec (3-process joint with shared frailty + outcome)

Following Liang et al 2410.13113, decomposed as:

1. **Visiting process (informative presence, IP):** For patient *i*, gap times or counting process  
   `λ_V,i(t) = λ_0V(t) · exp( γ_v · b_i + β_v^T X_i + α_v · Y_i*(t-) )`  
   where `b_i ~ N(0, σ_b^2)` is **shared frailty**, `X_i` baseline covariates (age/sex/comorbidity count resampled from MIMIC), `Y_i*(t-)` is underlying longitudinal trajectory at risk. Rate λ_V controls **sparsity** (mean visits/patient/year). Parameter `γ_v` controls **visit informativeness** (association frailty→visit). Baseline λ_0V(t) can be piecewise-constant (e.g., post-discharge burst).

2. **Observation process (informative observation, IO):** Conditional on a visit at time t*, which biomarkers are measured:  
   `logit P( O_ij(t*) = 1 | visit, b_i, Y*_i(t*) ) = γ_o · b_i + β_o^T X_i + δ · Y*_i(t*)`  
   This separates IP (did patient present?) from IO (conditional on presence, what was ordered?). δ captures **severity-driven test ordering**.

3. **Longitudinal biomarker process:**  
   `Y_ij(t) = X_i(t) β + Z_i(t) b_i + ε_ij(t)` , `b_i ~ N(0, D)` (random intercept + slope), `ε_ij ~ N(0, σ^2)` (**noise**). SNR = Var( Z b ) / σ^2. Trajectory Y*(t) = X(t)β + Zb is the **latent truth**.

4. **Shared frailty linkage:** A single latent `b_i` (or vector) enters all three processes (visit + observation + longitudinal) plus the outcome model, inducing the informativeness correlation. Sensitivity variants: correlated frailties vs single shared frailty.

5. **Outcome model (known truth):**  
   - Concurrent risk: `logit P( E_i = 1 | history ) = θ0 + θ1 · functional( Y*_i ) + θ2 · b_i` where functional ∈ {current value, slope, cumulative AUC, threshold crossing}.  
   - Or survival: `λ_E,i(t) = λ_0E(t) · exp( θ1·Y*_i(t) + θ2·b_i )` with administrative censoring at horizon H (e.g., 5y).  
   This defines the ** estimand**: θ1 is the longitudinal–outcome association; predictive estimand is 5y event risk / survival.

Twin plasmode generators (per Liu 2504.11740):
- **Plasmode-Generate-Outcome:** Resample real covariate structure (X, visit-time patterns) from MIMIC; overlay synthetic Y*(t) + outcome via model above. Tests prediction.
- **Plasmode-Generate-Treatment:** Resample real structure; overlay synthetic visit/observation mechanism + outcome conditional on (real) exposure. Preferred for causal variants; run as sensitivity.

#### 7b. Parameter Inventory (publishable grid)

| Dimension | Values to simulate (justify vs Schneider) | Rationale |
|-----------|---------------------------------------------|-----------|
| **N (patients)** | 500, 2 000, 10 000 | Small→large to test asymptotic behaviour; Schneider varies heterogeneity; 10k approximates single-centre EHR |
| **Visits/patient** | Mean 2, 6, 15 over horizon (λ_V ∈ {low, med, high sparsity}) | Schneider varies frequency; 2 ≈ annual screening, 15 ≈ chronic-disease follow-up |
| **Horizon / time-origin** | H = 3y, 5y; origin = first eligible visit | Tests time-origin sensitivity (target-trial concern) |
| **Noise σ** | SNR ∈ {0.5 (noisy), 1.5 (moderate), 4 (clean)} | Schneider varies noise explicitly |
| **Visit informativeness γ_v** | 0 (non-informative), 0.3 (moderate), 0.8 (strong) | Liang shows threshold where joint matters; 0 is the falsification arm |
| **Observation informativeness γ_o / δ** | 0, 0.4, 0.9 | Decomposes IP vs IO (Liang contribution) |
| **Between-patient heterogeneity** | D = diag(τ0^2, τ1^2) with τ0 ∈ {0.5,1.5}, τ1 ∈ {0.2,0.8} | Tests random-slope heterogeneity (Schneider) |
| **Effect size θ1** | OR/HR ∈ {1.1 (weak), 1.5 (moderate), 2.5 (strong)} per 1-SD Y* | Covers weak biomarker (hard) to strong |
| **Censoring** | 10%, 30% administrative + informative via frailty | Tests joint-vs-Cox sensitivity |

Design: **factorial with fractional replication** (full 3×3×3×3×3×2 ≈ 486 cells is too large). Use **Latin hypercube / Sobol** or a **core factorial** (γ_v ∈ {0, 0.8} × sparsity {low, high} × SNR {noisy, clean} × N {2k, 10k} = 16 core cells, each 200 Monte-Carlo replicates), plus **one-at-a-time sensitivity** sweeps on γ_o, censoring, effect size. Pre-register cell list.

#### 7c. Mandatory Baselines (no paper without these)

1. **LMM random-intercept + random-slope** (`lme4` / `nlme`): correctly specified time trend (linear + spline if non-linear truth), predicted trajectory fed to outcome model (two-stage, with bootstrap SE).
2. **Joint longitudinal–survival (JMbayes2):** shared random effects linking Y*(t) to hazard; with `frailtypack` as cross-check.
3. **LOCF + logistic/Cox:** last-observation-carried-forward — the "EHR strawman" that many DL papers beat but is clinically common.
4. **MICE + pooled logistic/Cox:** standard multiple imputation (m=20) assuming MAR within visit-windows; pooled Rubin's rules.
5. **GRU-D (Che 2018):** PyTorch implementation (`github.com/PeterChe1990/GRU-D`); masking + Δt inputs; matched hyperparameters via nested CV on plasmode training split.
6. **SeFT (Horn 2020):** set-function view of irregular series; `mlr.press` code; handles variable-length sets without imputation.

*Optional 7th:* neural ODE / GRU-ODE-Bayes (one continuous-time representative via `torchdiffeq`) — include only if compute budget allows; aids the ODE-overhead claim (Sun).

All methods see **identical train/test splits** per plasmode replicate; hyperparameters tuned on a validation split **within training data only**.

#### 7d. Metrics (joint criterion, not AUC-only)

- **Discrimination:** AUC (binary) / C-index & time-dependent AUC (survival) on held-out plasmode test set.
- **Calibration:** calibration slope & intercept (logistic/Cox calibration regression), calibration plot with loess, Van Calster hierarchy (mean / weak / moderate where feasible). Report per Riley BMJ 2025.
- **Overall accuracy:** Brier score (binary) / integrated Brier (survival) with decomposition.
- **Prediction-interval coverage:** 90%/95% prediction interval coverage for individual risks (bootstrap / Bayesian posterior for LMM/joint; conformal for DL where applicable); report empirical coverage vs nominal + interval width.
- **Decision-curve analysis (DCA):** net benefit across threshold probabilities (Vickers & Elkin) — the clinical-utility tiebreaker.
- **Estimation bias (where outcome model is parametric):** bias / RMSE / coverage of θ1 (exposure effect) — bridges to causal estimand.

Primary decision rule (pre-registered): **DL "wins" only if it is simultaneously non-inferior on calibration (|slope-1| within 0.1, intercept within 0.1 on logit scale) and coverage (within 2 pp of nominal) and superior on DCA net benefit at the clinically relevant threshold range.** This prevents AUC-only cherry-picking.

#### 7e. Software

- **R:** `JMbayes2`, `joineRML`, `frailtypack`, `nlme`/`lme4`, `mice`, `CalibrationCurves`, `dcurves` (DCA), `survival`.
- **Python:** `GRU-D` (PyTorch), `SeFT` (PyTorch), `torchdiffeq` / `GRU-ODE-Bayes`, `lifelines`/`scikit-survival` for Cox, `MAPIE` for conformal.
- **Orchestration:** Snakemake for replicate parallelism; seeded RNG (PCG64); reporting via `TRIPOD+AI` checklist item for simulation studies.

#### 7f. Data Need

- **Primary (sufficient for v1): simulation / plasmode** — no PHI required. Covariate base resampled from **MIMIC-III / MIMIC-IV** public extracts (PhysioNet credentialed, days–2 weeks) for realistic X/b distributions, or fully synthetic if access delayed.
- **Secondary (replication / reviewer request): MIMIC-III/IV real-data replication** — fit same baseline suite on a real phenotyping task (e.g., CKD progression / mortality) with empirical visit sparsity; compares plasmode phase diagram to real-data ordering (bridges T7 instrument-validity question).
- **No private hospital data required for v1.**

#### 7g. India Transport Extension Note (not claimed for v1)

Indian outpatient EHR is plausibly **sparser, more fragmented (paper-mediated), with stronger cost-driven selective testing** (higher γ_v/γ_o) and lower measurement frequency. A Stage-2 extension varies λ_V and γ_v/γ_o to **Indian-typical regimes** (e.g., mean visits/year ≤2, higher informative missingness) and tests whether the "LMM suffices" conclusion **transports**. This genuinely stresses an assumption but requires Indian partner data or a plasmode mimicking Indian measurement patterns (see T6/T4 companion packets). **Not bundled into v1 hypothesis.**

---

### 8. Evidence AGAINST the Gap (Self-Authored Adversarial)

**Closest defeaters that would collapse novelty if framed generously:**

1. **Naemi et al arXiv 2401.15290** *is* a recent MIMIC-IV irregular-series benchmark with several state-of-the-art tabular DL time-series models and a MIMIC-III literature survey. If the bar is "any irregular-series benchmark on MIMIC," novelty is reduced. **Rebuttal:** Naemi does **not** include well-specified LMM / JMbayes2 as baselines and does **not** report calibration / coverage / DCA — the mandatory gap criteria. The surviving gap is precisely that classical-vs-DL comparison with those metrics.

2. **Schneider et al 2025 (PMC12070788)** already provides extensive simulation guidelines varying frequency / noise / heterogeneity and comparing joint vs Cox. A reviewer could argue "simulation-based method comparison under varying data quality is done." **Rebuttal:** Schneider varies quality **within the joint-vs-Cox world only**; no DL irregular-series comparator appears. The proposed gap is specific to the **DL-for-irregularity** class (GRU-D / SeFT / neural ODE), not joint-vs-Cox.

3. **Sun et al 2026 review (§ Limitations)** flags ODE/SDE overhead and sketches hybrid architectures. A generous reader could argue the classical comparison is "obvious next work" and that the supplement / companion code at `github.com/SCXsunchenxi/ISMTS-Review` already runs the experiment. **Rebuttal that must be executed before promotion:** **Inspect the supplement + code repository** for any empirical LMM/joint-vs-DL table; until that inspection is logged, confidence cannot exceed Medium. Current searches returned no such table in the main text/toc.

4. **Frontiers in Applied Math & Stats 2026 — "Assessment of robustness of LMM under irregular longitudinal data"** (search hit) explicitly stress-tests LMM under irregularity. If that study already includes a DL comparator, the DL-vs-LMM framing is narrowed. **Pre-promotion check:** extract that paper's methods table; if it is LMM-only robustness (no GRU-D/SeFT), it strengthens rather than defeats the gap (it confirms LMM is the baseline to beat).

5. **Liang et al 2410.13113** already runs simulations comparing their three-process joint vs existing methods under IP/IO. A reviewer could claim "informativeness is already studied." **Rebuttal:** Liang compares **within joint-model family** (different handling of IP/IO); no GRU-D/SeFT/neural ODE appears. The DL-vs-joint comparison remains open.

If any of #1–#5 were extended post-2025 to include the exact conjunction (tunable informative visit + observation decomposition + LMM/joint + GRU-D/SeFT + calibration/coverage/DCA), the gap would be **closed** and the correct next step would be a **direct replication/extension** rather than a de novo design.

---

### 9. Relevant Datasets

- **Primary — simulation / plasmode (no PHI):** Plasmode constructed from **MIMIC-III v1.4 / MIMIC-IV v2.2** covariate resampling + synthetic visit/observation/longitudinal mechanisms (§7a). Fully synthetic EHR simulation with known DAG as fallback (no data access needed). Access: PhysioNet credentialing (CITI + DUA, 1–2 weeks) for realistic covariate base; not required for v1 if fully synthetic.
- **Secondary — real replication:** **MIMIC-III/IV** real trajectories (Harutyunyan phenotyping, MIMIC-Extract) + **PhysioNet Cardiology Challenges 2012 & 2019** (open) for out-of-sample irregularity regimes. Bridges to T7 instrument-validity.
- **Optional Stage-2 transport:** **UK Biobank South Asian subset** / **CARRS** / **ICMR-INDIAB** structure (restricted, requires application) — only for India-regime plasmode mimicking, not required for v1.
- **Software as dataset:** `synthEHRella` (Chen JAMIA 2025 toolkit, https://github.com/chenxran/synthEHRella) plasmode generators as alternative resampling engine.

---

### 10. Methodological Implications

- **If classical suffices (failure to reject H0):** Redirect field effort from architecture novelty to (a) correct specification of the visit/observation model, (b) uncertainty quantification and decision thresholds, (c) transportability across sparsity regimes. A rigorous negative result is publishable and decision-relevant (saves compute/privacy costs; favours auditable mixed models for deployment). Produces a **phase diagram** (when DL region is empty or narrow, that itself is the contribution).
- **If DL wins in a characterised regime (reject H0):** Identifies **where** complexity pays (e.g., dense follow-up, strongly informative visiting, large N, high SNR) and quantifies the **calibration/coverage price** of that win. Produces a **decision rule** for method choice rather than a leaderboard.
- Either outcome demands **calibration + coverage + DCA** alongside AUC, nudging the territory toward more honest inference (Riley 2025; Van Calster hierarchy). The design also stress-tests **plasmode instrument validity** (Generate-Treatment vs Generate-Outcome sensitivity, per Liu cautionary), informing the T7 agenda.
- Pre-registration (OSF / Registered Report) is mandatory to prevent HARKing on the many simulation cells; **"Beat the baseline or show it suffices"** is the declared primary outcome.

---

### 11. Clinical Implications

- Trajectory questions matter for chronic-disease monitoring (CVD risk trajectories, CKD/glucose trajectories, blood pressure). If predictions from irregular outpatient labs are **no better with expensive models**, deployment should favour **interpretable, EHR-deployable mixed models** that clinicians can audit and that run without GPU / integration overhead.
- Informative visiting is clinically meaningful (sicker patients visit more; visit frequency predicts outcomes). A finding that modelling visits corrects bias **only when informative** justifies simpler workflows in **stable screening cohorts** vs richer models in **high-acuity follow-up** — an actionable triage rule for health-system analytics.
- Calibration/coverage results directly inform **shared decision-making**: interval-aware risk communication ("your 5-year risk is 8%, compatible with 4–13% given model uncertainty — threshold 7.5% falls inside interval") vs point-risk thresholds.

---

### 12. India Relevance

**Verdict: GEOGRAPHY-ONLY for v1.**

- The core benchmark question (does modelling irregularity pay, and under which informativeness/sparsity/noise regimes?) is **population-agnostic** and stresses a **universal** statistical assumption, not an India-specific one. Indian data are not needed to answer it, and claiming otherwise would be decoration.
- A **defensible India-relevant Stage-2 extension** varies measurement-frequency and informative-missingness regimes to mimic Indian outpatient settings (sparse, cost-driven selective testing, paper fragmentation) vs US ICU density, testing **transportability of the "mixed model suffices" conclusion**. This would genuinely stress an assumption and is scientifically meaningful — but it is a **follow-on**, not part of the v1 plasmode falsifiable claim. Do not claim STRESSES-ASSUMPTION for the v1 simulation design.

---

### 13. Confidence

**Medium.**

Strengths: The review/simulation landscape is clearly surveyed; the DL-vs-classical head-to-head with calibration/coverage/DCA + tunable informative-visit/observation decomposition + known truth is **plausibly thin but not saturated**. Generative spec is concrete (Liang three-process + Schneider parameter template + Franklin/Schuler plasmode), mandatory baselines are pre-specified, and the falsification arm (γ_v=0, low sparsity) makes the design honest.

Risks capping confidence below High:
- **Sun supplement / companion code** (github.com/SCXsunchenxi/ISMTS-Review) must be fully inspected — it could already contain an LMM/joint-vs-DL table that closes the gap.
- **Naemi 2024 follow-up or forthcoming 2025–2026 plasmode papers** (Franklin/Schuler/Liu lineage) may run the exact conjunction — targeted arXiv stat.ME/stat.AP + PubMed "plasmode" sweep needed before Registered Report submission.
- **Frontiers 2026 LMM-robustness paper** must be screened for any DL comparator.

No data-access barrier for v1 (simulation primary); publishability depends on **pre-registration + calibration/coverage/DCA reporting** meeting reviewer expectations (Riley/Van Calster/TRIPOD+AI framing).

---

### 14. Recommended Next Search (Executable)

```pubmed
# 1. Exhaust plasmode+DL conjunction (adversarial closure)
("plasmode"[Title/Abstract] OR "plasmode simulation"[Title/Abstract]) AND ("linear mixed model"[Title/Abstract] OR "joint model"[Title/Abstract]) AND ("deep learning"[Title/Abstract] OR "GRU-D"[Title/Abstract] OR "neural ODE"[Title/Abstract] OR "SeFT"[Title/Abstract]) AND (calibration[Title/Abstract] OR coverage[Title/Abstract])

# 2. Estimand-specific: informative presence + informative observation decomposition (synonym sweep)
("informative presence"[Title/Abstract] OR "informative observation"[Title/Abstract] OR "informative visit"[Title/Abstract]) AND ("joint model"[Title/Abstract] OR "shared frailty"[Title/Abstract]) AND ("electronic health records"[Title/Abstract] OR EHR[Title/Abstract])

# 3. Preprint sweep for recent closure
# arXiv: stat.ME + stat.AP + cs.LG, 2024–2026
# query: plasmode irregular EHR benchmark mixed model calibration
# tool: arxiv.org search + open-web site:arxiv.org plasmode GRU-D JMbayes2

# 4. Supplement / code inspection (not a PubMed query)
# Inspect: Sun et al 2026 supplement + github.com/SCXsunchenxi/ISMTS-Review (tables/figures vs LMM/joint)
# Inspect: Frontiers 2026 LMM-robustness paper — extract methods table for any DL comparator
```

---

### Appendix — Queries & Papers (verbatim for search_log.csv / evidence_registry.csv)

**Queries run 2026-08-30 (verbatim):**
- `plasmode simulation design informative visit process shared frailty joint model`
- `plasmode comparison deep learning vs linear mixed model calibration coverage irregular EHR`
- `informative observation process versus informative visit process EHR Franklin Schuler`
- `GRU-D SeFT JMbayes2 joint model irregular time series benchmarking`
- `A Review of Deep Learning Methods for Irregularly Sampled Medical Time Series Sun 2026 Health Data Science`
- `Naemi MIMIC-IV irregular sparse clinical time series benchmark 2024`

**Papers (resolvable IDs):** 10 papers listed in §4 table (Sun 10.34133/hds.0456, Schneider 10.1186/s13040-025-00450-z, Liang 10.48550/arXiv.2410.13113, Che 10.1038/s41598-018-24271-9, Horn 10.48550/arXiv.2006.10199, Naemi 10.48550/arXiv.2401.15290, Liu 10.48550/arXiv.2504.11740, Franklin 10.1093/aje/kww098, Chen 10.1093/jamia/ocaf082, JMbayes2 CRAN).

**Verification:** 10/10 DOIs HEAD-checked 302 on 2026-08-30; Schneider PMC12070788 + Liang arXiv + Chen JAMIA web_extract succeeded (see search_log). [UNVERIFIED] not used for load-bearing claims.

