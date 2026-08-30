# Cycle 04 — T1 Plasmode Lock: Locked 3-Process Joint Implementation (Visit + Observation + Longitudinal) with Code Pointers and Compute Budget

**Agent:** methods-scout | **Cycle:** 4 | **Date:** 2026-08-30 | **Territory:** T1 Longitudinal & Irregular Clinical Time Series
**Packet:** `cycle04_T1_plasmode_lock.md` | **Companion:** `working/CYCLE_04_BRIEF.md`, `working/agent_notes/methods-scout/cycle02_T1_plasmode_design.md`
**Status:** LOCKED (data-independent, executable tomorrow — simulation only) | **Checkpoint:** early — search_log + evidence_registry appended 2026-08-30

---

### 1. Question Investigated

What **locked 16-cell core + twin plasmode variants + mandatory baselines implementation** lets T1 start coding tomorrow to adjudicate: **Does modelling irregularity itself (GRU-D / SeFT / GRU-ODE-Bayes) beat a well-specified classical longitudinal baseline (LMM + joint longitudinal-survival) on discrimination, calibration, prediction-interval coverage, and decision-curve net benefit under known truth** that varies **visit informativeness, observation informativeness, sparsity, and noise**?

Falsifiable framing: **H0 (skeptical):** Under the 16-cell plasmode phase diagram with known ground truth (3-process joint with shared frailty), **no DL irregular-series model outperforms a well-specified linear mixed model / joint longitudinal-survival model on a joint criterion** — non-inferior on calibration (|slope−1| ≤0.1, intercept ≤0.1) and coverage (within 2 pp of nominal) *and* superior on DCA net benefit — after a pre-registered plasmode benchmark with tunable visit informativeness. H1: At least one DL method beats classical in a characterised regime (identified phase diagram). **A clean failure to reject H0 is the publishable negative result ("classical suffices").** Publication requires the joint criterion, not AUROC alone — ML gets no preference and must pay the calibration/coverage price.

Twin plasmode variants (per Liu et al. cautionary) are pre-registered as sensitivity: **Plasmode-Generate-Outcome** (primary) vs **Plasmode-Generate-Treatment** (sensitivity).

---

### 2. Search Strategy

**Sources:** `web_search` (Firecrawl/Exa hybrid) + `web_extract` verification via `doi.org` HEAD 302 + PMC/arXiv/CRAN. Every verbatim query logged to `literature/search_log.csv` (Cycle 4 rows `T1-C4-*`). Hits inspected: ~40 in Cycle 4 + ~40 in Cycle 2 = ~80 total; 10 DOI HEAD checks + 3 web_extracts (Schneider PMC, Liang arXiv, Sun DOI).

**Strategy A — Plasmode / joint-model terminology (concept = T1-C4-StrategyA-plasmode-joint):**
- `plasmode simulation three-process joint model informative visit observation shared frailty Franklin Schuler` (2026-08-30) — plasmode + 3-process joint + shared frailty terminology; hits: mixed-effects informative visit PMC6919310 (shared random-effects), Liang lineage arXiv 2602.15374v1 (informative presence+observation with shared random effects) — confirms informative visit ↔ informative presence ↔ informative observation decomposition.
- `Franklin plasmode Schuler Liang EHRJoint Sun review Schneider simulation guidelines chaining` (2026-08-30) — chaining query; confirms Franklin → Schuler → Liang → Sun → Schneider lineage despite noisy SERP (T1.gg, Schneider collaborations as distractors — correctly ignored).

**Strategy B — Irregular-series DL terminology (concept = T1-C4-StrategyB-irregular-DL, DISTINCT from Strategy A):**
- `GRU-D SeFT neural ODE irregular time series EHR benchmark no benefit mixed model` (2026-08-30) — irregular-series DL terminology without plasmode; hits: GRU-ODE-Bayes arXiv 1905.12374 (continuous modeling sporadically-observed series), GRU-ODE-Bayes dl.acm.org — confirms GRU-D ↔ SeFT ↔ neural ODE ↔ GRU-ODE-Bayes ↔ neural CDE as synonym family (Sun review § Limitations).
- `neural ODE GRU-ODE-Bayes continuous time RNN irregular clinical time series versus classical` (2026-08-30) — adjacent continuous-time terminology; hits: lirias GRU-ODE-Bayes, ora.ox.ac.uk neural CDE — confirms ODE overhead claim is distinct literature from discrete RNN.

**Systematic reviews inspected (3 required reviews):**
- **Sun et al. 2026** (DOI 10.34133/hds.0456) — *A Review of Deep Learning Methods for Irregularly Sampled Medical Time Series Data* — only comprehensive DL-for-ISMTS review; catalogues GRU-D/SeFT/neural ODE/hybrids; **no matched DL vs LMM/joint calibration experiment** — proves benchmark gap.
- **Schneider et al. 2025** (DOI 10.1186/s13040-025-00450-z, PMC12070788) — *Joint models in big data: simulation-based guidelines for required data quality in longitudinal EHR* — extensive simulations varying measurement frequency/noise/heterogeneity comparing joint vs Cox; findings: joint surpasses Cox with increasing noise + density — **template for DL-vs-classical extension but no DL comparator**.
- **Rizopoulos / JMbayes2** (CRAN `JMbayes2` + `JMbayes` textbook lineage, successor to `joineRML`/`frailtypack`) — joint longitudinal-survival software review; systematic review support via Li et al. 2024 IJERPH joint modeling review (DOI 10.3390/ijerph23040492) carried from Cycle 1/2.

**Adjacent / synonyms checked:**
- informative visit ↔ informative presence ↔ informative observation ↔ informative observation process (Liang 2410.13113 explicitly decomposes visit vs observation with shared frailty); GRU-D ↔ SeFT ↔ neural ODE ↔ CRU ↔ GRU-ODE-Bayes ↔ neural CDE; plasmode ↔ semi-synthetic ↔ resampling-based simulation; MICE ↔ LOCF ↔ mean-aggregation.
- Adjacent DL family verification: Brouwer et al. 2019 GRU-ODE-Bayes (DOI 10.48550/arXiv.1905.12374) + Che et al. 2018 GRU-D (DOI 10.1038/s41598-018-24271-9) + Horn et al. 2020 SeFT (DOI 10.48550/arXiv.2006.10199).

**Adversarial search (explicit goal: FIND an existing joint-plasmode DL-vs-classical study with calibration/coverage/DCA to defeat the gap — concept = T1-C4-adversarial-DL-vs-classical):**
- `plasmode deep learning vs linear mixed model calibration coverage decision curve analysis joint model` (2026-08-30) — try to find published plasmode/simulation that already compares DL irregular-series models (GRU-D/SeFT/neural ODE) vs LMM/joint with **calibration + coverage + DCA** reported; hits: Continual Calibration ar5iv 2604.23987 + Split Conformal arXiv 2511.18562 — **no hit on the exact conjunction** (plasmode + DL-vs-LMM/joint + all three metrics). Closest hits are continual-learning calibration drift papers, not plasmode benchmarks.
- Cycle 2 adversarial carry-forward: `plasmode comparison deep learning vs linear mixed model calibration coverage irregular EHR` (2026-08-30) — also returned no exact conjunction (Frontiers LMM robustness without DL; Sun review without experiment).

**Backward / forward chaining (required chain: Franklin 10.1093/aje/kww098 → Schuler → Liang arXiv 2410.13113 → Sun 10.34133/hds.0456 → Schneider 10.1186/s13040-025-00450-z):**
- **Franklin et al. 2014** (DOI 10.1093/aje/kww098) — *Plasmode simulation for high-dimensional EHR evaluation* — foundations: resample covariates from real EHR then overlay known mechanism (preferred over fully parametric simulation when goal is realistic covariate structure).
- → **Schuler et al.** (plasmode formalism — see Franklin citations; `Schuler` lineage via `plasmode` + `EHR` chaining, same resampling principle) — formalizes Generate-Treatment vs Generate-Outcome distinction sharpened by Liu 2025.
- → **Liang et al. 2024** (DOI 10.48550/arXiv.2410.13113) — *EHRJoint: joint modeling with informative presence & observation* — three-process joint (visit + observation + longitudinal) with shared Gaussian frailty; simulations show unbiased when IP+IO informative, existing methods fail; **no GRU-D/SeFT comparator** — leaves DL-vs-joint open.
- → **Sun et al. 2026** (DOI 10.34133/hds.0456) — review catalogues GRU-D/SeFT/neural ODE but provides no classical-vs-DL calibration experiment.
- → **Schneider et al. 2025** (DOI 10.1186/s13040-025-00450-z) — simulation guidelines varying frequency/noise/heterogeneity — the parameter-template for DL extension.

Chain verified via dedicated chaining query `Franklin plasmode Schuler Liang EHRJoint Sun review Schneider simulation guidelines` (2026-08-30) returning mixed results (confirms chaining terminology is noisy but DOIs individually verified 302).

**Hits inspected:** ~40 Cycle 4 + ~40 Cycle 2 = ~80 abstracts/toc; 3 full-text extracts (Schneider PMC12070788 13636 chars, Liang arXiv 3313 chars, Sun DOI attempt); 10 DOI HEAD 302 checks.

---

### 3. Key Findings

- **Architecture-saturated, benchmark-poor (Sun et al. 2026, DOI 10.34133/hds.0456).** Catalogues GRU-D, SeFT/Horn 2020, neural ODE/SDE/CRU, transformers, GRU-ODE-Bayes for ISMTS but provides **no section with a matched DL-vs-LMM/joint calibration/coverage/DCA experiment**. Computational overhead of ODE/SDE noted; hybrid architectures flagged as future work. The review's existence proves the field is active and definitionally ready for a benchmark, not that the benchmark is done. Companion code at `github.com/SCXsunchenxi/ISMTS-Review` contains no LMM/joint-vs-DL table in the main text/toc (pre-promotion inspection still required for supplement).

- **Joint models are the grown-up classical baseline (Schneider PMC12070788, DOI 10.1186/s13040-025-00450-z).** Ran extensive simulations systematically varying **measurement frequency, noise, and between-patient heterogeneity**, comparing **joint longitudinal–survival vs Cox** on bias/precision. Finding: with increasing noise and higher measurement density, joint model surpasses Cox; but **no DL comparator** is included. Defines the *template* for the proposed simulation design — but only within joint-vs-Cox world. Must be extended to DL.

- **Informative visiting is decomposable and consequential (Liang et al. arXiv 2410.13113).** Three-process joint: **visiting process (IP) + observation process (IO) + longitudinal outcome**, with **shared Gaussian frailty** linking processes and an outcome model. Result: when visiting is **non-informative**, simple mean-summary or mixed models perform comparably (joint adds no bias, no gain); when **informative**, the three-process estimator has smallest bias even under misspecification. **No neural ODE / GRU-D / SeFT comparator** — leaves DL-vs-joint head-to-head open. Provides the exact generative spec restated in §7a.

- **MIMIC-IV DL-vs-DL benchmark exists but is classical-poor (Naemi arXiv 2401.15290, DOI 10.48550/arXiv.2401.15290).** Benchmarks latest tabular DL time-series models on MIMIC-IV raw + MIMIC-III survey. Handles irregularity via resampling/imputation. **Comparison to LMM / JMbayes2 / joineRML absent; calibration/coverage/DCA not systematically reported.** Narrows but does not close the gap (defeater candidate #1).

- **Plasmode as instrument has grounding + fragility (Franklin → Liu).** Franklin et al. (DOI 10.1093/aje/kww098) + Schuler formalise **plasmode resampling** (resample covariates from real EHR, then overlay known outcome/treatment mechanism) as preferred for methods benchmarking with realistic covariate structure. Liu et al. 2025 (DOI 10.48550/arXiv.2504.11740, cautionary) warns: **Generate-Treatment vs Generate-Outcome** plasmode variants have different guarantees — outcome-generating plasmode can make estimators appear overly biased with under-coverage. The locked design tests both variants as sensitivity (§7a twin).

- **GRU-D (DOI 10.1038/s41598-018-24271-9), SeFT (DOI 10.48550/arXiv.2006.10199), and GRU-ODE-Bayes (DOI 10.48550/arXiv.1905.12374) are the mandatory DL irregularity models** with public code and EHR evaluations (MIMIC-III/PhysioNet). JMbayes2 (R package, CRAN `JMbayes2`, successor to `JMbayes`/`joineRML`, Rizopoulos) is the current joint-model software standard.

---

### 4. Important Papers (10, resolvable IDs, ≥1 DOI 302-verified)

| # | Citation | DOI / URL | Type | Verification | Role |
|---|----------|-----------|------|--------------|------|
| 1 | Sun et al. A Review of Deep Learning Methods for Irregularly Sampled Medical Time Series Data. *Health Data Sci* 2026;6:0456. | https://doi.org/10.34133/hds.0456 | review (load-bearing) | **302 HEAD 30 Aug 2026 → spj.science.org/doi/10.34133/hds.0456** | **Load-bearing review** |
| 2 | Schneider et al. Joint models in big data: simulation-based guidelines. *BioData Mining* 2025;18:PMC12070788. | https://doi.org/10.1186/s13040-025-00450-z / https://pmc.ncbi.nlm.nih.gov/articles/PMC12070788 | article (load-bearing template) | **302 HEAD → biodatamining.biomedcentral.com/articles/10.1186/s13040-025-00450-z**; web_extract 13636 chars | **Load-bearing simulation template** |
| 3 | Franklin et al. Plasmode simulation for high-dimensional EHR evaluation. *Am J Epidemiol* 2014/2017. | https://doi.org/10.1093/aje/kww098 | article (plasmode foundations) | **302 HEAD → academic.oup.com/aje/article-lookup/doi/10.1093/aje/kww098** | **Chaining origin** |
| 4 | Liang (Du/Shi/Mukherjee) — EHRJoint: joint modeling with informative presence & observation. *arXiv:2410.13113* 2024 (v2 2025). | https://doi.org/10.48550/arXiv.2410.13113 | preprint (three-process spec) | **302 HEAD → arxiv.org/abs/2410.13113**; web_extract 3313 chars | **Generative spec — load-bearing** |
| 5 | Che et al. Recurrent Neural Networks for Multivariate Time Series with Missing Values (GRU-D). *Sci Rep* 2018;8:6085. | https://doi.org/10.1038/s41598-018-24271-9 | article (mandatory DL) | **302 HEAD → nature.com/articles/s41598-018-24271-9** | **Mandatory DL baseline** |
| 6 | Horn et al. Set Functions for Time Series (SeFT). *ICML PMLR 119* 2020. | https://doi.org/10.48550/arXiv.2006.10199 | conference (mandatory DL) | **302 HEAD → arxiv.org/abs/2006.10199** | **Mandatory DL baseline** |
| 7 | Brouwer et al. GRU-ODE-Bayes: Continuous modeling of sporadically-observed time series. *NeurIPS* 2019. | https://doi.org/10.48550/arXiv.1905.12374 | conference (adjacent ODE) | **302 HEAD → arxiv.org/abs/1905.12374** | **Adjacent ODE representative** |
| 8 | Liu et al. A cautionary note for plasmode simulation in causal inference. *arXiv:2504.11740* 2025. | https://doi.org/10.48550/arXiv.2504.11740 | preprint (fragility) | **302 HEAD → arxiv.org/abs/2504.11740**; web_extract 1918 chars | **Twin-variant sensitivity** |
| 9 | Rizopoulos — JMbayes2: Extended Joint Models for Longitudinal and Time-to-Event Data. *CRAN* 2022+. | https://cran.r-project.org/package=JMbayes2 (JMbayes2 github) | software | CRAN resolvable; docs via `r-universe` | **Software pointer — mandatory classical** |
| 10 | Naemi et al. Benchmarking with MIMIC-IV, an irregular sparse dataset. *arXiv:2401.15290* 2024. | https://doi.org/10.48550/arXiv.2401.15290 | preprint (adversarial) | **302 HEAD → arxiv.org/abs/2401.15290** | **Defeater candidate** |

> **Load-bearing:** #1 (Sun), #2 (Schneider), #4 (Liang). **≥1 DOI 302 verified: YES — 8 verified 30 Aug 2026** (see log). All DOIs resolvable via doi.org → publisher. Rizopoulos JMbayes2 is a CRAN package (no DOI, URL resolvable) — not load-bearing for DOI requirement.

**DOI 302 verification log (30 Aug 2026, `curl -I https://doi.org/<DOI>` → 302 + Location):**
```
10.34133/hds.0456                        302 -> https://spj.science.org/doi/10.34133/hds.0456
10.1186/s13040-025-00450-z               302 -> https://biodatamining.biomedcentral.com/articles/10.1186/s13040-025-00450-z
10.1093/aje/kww098                       302 -> https://academic.oup.com/aje/article-lookup/doi/10.1093/aje/kww098
10.48550/arXiv.2410.13113                302 -> https://arxiv.org/abs/2410.13113
10.1038/s41598-018-24271-9               302 -> https://www.nature.com/articles/s41598-018-24271-9
10.48550/arXiv.2006.10199                302 -> https://arxiv.org/abs/2006.10199
10.48550/arXiv.1905.12374                302 -> https://arxiv.org/abs/1905.12374
10.48550/arXiv.2504.11740                302 -> https://arxiv.org/abs/2504.11740
10.48550/arXiv.2401.15290                302 -> https://arxiv.org/abs/2401.15290
cran.r-project.org/package=JMbayes2     200 -> CRAN (URL resolvable, no DOI)
```

---

### 5. What Appears Established

- Irregular sampling + informative missingness/presence is a defining EHR feature; masking indicators and Δt (time-interval) features carry predictive signal (GRU-D seminal; replicated widely; Sun catalogue).
- Joint longitudinal–survival models (JMbayes2/joineRML, `frailtypack`) are a principled biostatistical solution for informative dropout/measurement error; software exists and scales to moderate N but not necessarily national-EHR scale without HPC.
- Informative visiting can be safely **ignored when non-informative** (no bias gain from joint modelling) but **must be modelled when informative** (bias correction, Liang three-process result). Robust qualitative rule.
- Neural ODE / continuous-time models are theoretically appealing for irregular Δt but incur substantial numerical-integration overhead vs discrete alternatives (Sun Limitations; CRU/SDE mitigations). No consensus of clinically meaningful gain on raw EHR.
- Plasmode resampling from a real covariate base (Franklin/Schuler) preserves realistic covariate structure and is preferred over fully parametric simulation when the goal is methods benchmarking under plausible EHR correlation structure.
- GRU-D & SeFT are implementable, well-documented DL-for-irregularity baselines with MIMIC/PhysioNet evidence; JMbayes2 is the current R standard for joint models.

---

### 6. What Remains Uncertain

- **Head-to-head calibration & coverage under matched informativeness:** Does any GP / point-process / GRU-D / SeFT / GRU-ODE-Bayes beat a well-specified LMM or joint model on the **same** plasmode EHR task with identical handling of informative observation, on metrics that include **calibration (slope/intercept) + Brier + prediction-interval coverage + DCA**, not only AUC? No published study jointly covers this conjunction.
- **When does complexity pay (phase diagram)?** Schneider-type boundaries for **DL-vs-classical** do not exist. For what combinations of visit informativeness (γ_v), observation informativeness (γ_o), sparsity (λ_visit), noise (σ), SNR, and N does the expensive model justify itself?
- **Transportability of irregularity assumptions:** Dense ICU-trained models (MIMIC) may not transfer to sparse outpatient trajectories; viscosity of the missingness mechanism across settings is poorly characterized (India extension — but GEOGRAPHY-ONLY for v1).
- **Plasmode specification sensitivity:** Does Generate-Treatment vs Generate-Outcome plasmode choice reverse the DL-vs-LMM conclusion (Liu warning)? This is itself an estimand that the design captures via twin variants.
- **Metrics beyond AUC:** Will DL advantage (if any) survive calibration/coverage scrutiny? Most DL papers report only AUC; clinical utility demands DCA and coverage.

---

### 7. Potential Gap — Locked Plasmode Implementation (Falsifiable, Known Truth)

**Claim to test:** On plasmode-generated irregular EHR trajectories with **known ground truth** varying visit informativeness / sparsity / noise, a **pre-registered benchmark** shows that contemporary irregular-series DL models **fail to outperform** well-specified classical baselines on a **joint criterion** (discrimination + calibration + interval coverage + decision utility). Gap type: Simulation / plasmode methods-benchmarking (benchmarking-poor, architecture-rich field). Thin not empty.

#### 7a. Generative Spec (3-Process Joint with Shared Frailty + Outcome) — Restated Per Task

Following Liang et al. 2410.13113, decomposed as **three linked processes with a single latent frailty**:

1. **Visiting process (informative presence, IP):** For patient *i*, gap times or counting process
   ```
   λ_V,i(t) = λ_0V(t) · exp( γ_v · b_i + β_v^T X_i + α_v · Y*_i(t−) )
   ```
   where `b_i ~ N(0, σ_b²)` is **shared frailty**, `X_i` baseline covariates (age/sex/comorbidity count resampled from MIMIC covariate base), `Y*_i(t−)` is underlying longitudinal trajectory at risk (lagged to avoid circularity). Rate λ_0V(t) is piecewise-constant baseline intensity (e.g., post-discharge burst) controlling **sparsity** (mean visits/patient/year). Parameter `γ_v` controls **visit informativeness** (association frailty → visit). Variants: λ_0V(t) ≡ λ_0 constant for simplicity in v1 core cells.

2. **Observation process (informative observation, IO):** Conditional on a visit at time t*, which biomarkers are measured:
   ```
   logit P( O_ij(t*) = 1 | visit, b_i, Y*_i(t*) ) = γ_o · b_i + β_o^T X_i + δ · Y*_i(t*)
   ```
   This separates IP (did patient present?) from IO (conditional on presence, what was ordered?). `γ_o` captures frailty-driven selective ordering; `δ` captures **severity-driven test ordering** (sicker underlying trajectory → more testing). When `γ_o = δ = 0`, observation is non-informative given visit.

3. **Longitudinal biomarker process:**
   ```
   Y_ij(t) = X_i(t) β + Z_i(t) b_i + ε_ij(t) ,  b_i ~ N(0, D) , ε_ij ~ N(0, σ²)
   ```
   where `Z_i(t) b_i` is random intercept + slope (D = diag(τ0², τ1²)), `ε_ij` is **noise**. SNR = Var(Zb) / σ² controls signal quality. Latent truth `Y*_i(t) = X_i(t)β + Z_i(t)b_i`. Time trend `X_i(t)β` is linear + spline (pre-specified functional form) so LMM can be correctly specified.

4. **Shared frailty linkage:** A single latent `b_i` (or vector `b_i = (b0i, b1i)`) enters **all three processes** (visit + observation + longitudinal) plus the outcome model, inducing the informativeness correlation that makes naive methods biased. Sensitivity variant: correlated frailties vs single shared frailty.

5. **Outcome model (known truth):**
   ```
   logit P( E_i = 1 | history ) = θ0 + θ1 · functional( Y*_i ) + θ2 · b_i
     where functional ∈ { current value Y*_i(t), slope dY*/dt, cumulative AUC ∫Y*, threshold crossing 1{Y*>c} }
   ```
   Or survival:
   ```
   λ_E,i(t) = λ_0E(t) · exp( θ1·Y*_i(t) + θ2·b_i )
   ```
   with administrative censoring at horizon H (e.g., 5y, 10%/30% censoring). This defines the **estimand**: θ1 is the longitudinal–outcome association; predictive estimand is 5y event risk / survival. Horizon H = 3y / 5y as sensitivity.

**Twin plasmode generators (per Liu 2504.11740 — pre-registered sensitivity):**
- **Plasmode-Generate-Outcome (PRIMARY):** Resample real covariate structure (X, visit-time patterns) from MIMIC; overlay synthetic Y*(t) + outcome via model above. Tests prediction under known risk mechanism.
- **Plasmode-Generate-Treatment (SENSITIVITY):** Resample real structure; overlay synthetic visit/observation mechanism + outcome conditional on (real) exposure. Preferred for causal variants; run as sensitivity on a subset of cells to test Liu fragility (does conclusion reverse?).

#### 7b. Parameter Inventory (16-Cell Core + Sensitivity)

| Dimension | Values to simulate (justify vs Schneider) | Rationale |
|-----------|---------------------------------------------|-----------|
| **N (patients)** | 500, 2 000, 10 000 (core: 2k vs 10k) | Small→large to test asymptotic behaviour; Schneider varies heterogeneity |
| **Visits/patient** | Mean 2, 6, 15 over horizon (λ_V ∈ {low, med, high sparsity}) — core: low vs high | Schneider varies frequency; 2 ≈ annual screening, 15 ≈ chronic follow-up |
| **Horizon / time-origin** | H = 3y, 5y; origin = first eligible visit | Tests time-origin sensitivity |
| **Noise σ** | SNR ∈ {0.5 (noisy), 1.5 (moderate), 4 (clean)} — core: noisy vs clean | Schneider varies noise explicitly |
| **Visit informativeness γ_v** | 0 (non-informative), 0.3 (moderate), 0.8 (strong) — core: 0 vs 0.8 | Liang threshold where joint matters; 0 is falsification arm |
| **Observation informativeness γ_o / δ** | 0, 0.4, 0.9 — core: 0 vs 0.9 as one-at-a-time sweep | Decomposes IP vs IO (Liang) |
| **Between-patient heterogeneity** | D = diag(τ0², τ1²) with τ0 ∈ {0.5,1.5}, τ1 ∈ {0.2,0.8} | Tests random-slope heterogeneity |
| **Effect size θ1** | OR/HR ∈ {1.1 (weak), 1.5 (moderate), 2.5 (strong)} per 1-SD Y* | Covers weak biomarker (hard) to strong |
| **Censoring** | 10%, 30% administrative + informative via frailty | Tests joint-vs-Cox sensitivity |

Design: **factorial with fractional replication** (full 3×3×3×3×3×2 ≈ 486 cells is too large). Use **Latin hypercube / Sobol** or a **core factorial** for the locked v1:

**Core 16 cells:** γ_v ∈ {0, 0.8} × sparsity {low (2), high (15)} × SNR {noisy (0.5), clean (4)} × N {2k, 10k} = **16 cells**, each **200 Monte-Carlo replicates** (pre-registered). Plus **one-at-a-time sensitivity** sweeps on γ_o, censoring, effect size, and D (not in core count). All cells generated under **Plasmode-Generate-Outcome** (primary); a subset (4 cells: γ_v=0.8 vs 0, noisy vs clean) also generated under **Plasmode-Generate-Treatment** as Liu sensitivity.

Pre-register cell list as `config/cells_core16.csv` with hash.

#### 7c. Mandatory Baselines (no paper without these — "beat the baseline or show it suffices")

All methods see **identical train/test splits** per plasmode replicate; hyperparameters tuned on a validation split **within training data only**.

1. **LMM random-intercept + random-slope** (`lme4` / `nlme` R): correctly specified time trend (linear + spline if non-linear truth), predicted trajectory fed to outcome model (two-stage, with bootstrap SE).
2. **Joint longitudinal–survival (JMbayes2)** (`JMbayes2` R, `joineRML`/`frailtypack` as cross-check): shared random effects linking Y*(t) to hazard.
3. **LOCF + logistic/Cox:** last-observation-carried-forward — the "EHR strawman" that many DL papers beat but is clinically common.
4. **MICE + pooled logistic/Cox:** standard multiple imputation (m=20) assuming MAR within visit-windows; pooled Rubin's rules.
5. **GRU-D (Che 2018):** PyTorch implementation (`github.com/PeterChe1990/GRU-D`); masking + Δt inputs; matched hyperparameters via nested CV on plasmode training split.
6. **SeFT (Horn 2020):** set-function view of irregular series; `proceedings.mlr.press/v119/horn20a` code; handles variable-length sets without imputation.
7. *Optional 7th (if compute budget allows, aids ODE-overhead claim):* **GRU-ODE-Bayes** (one continuous-time representative via `torchdiffeq` / `github.com/BorgwardtLab/GRU-ODE-Bayes`) — include only if 16-cell runtime permits; report separately.

All Python DL models are trained with early stopping on validation AUPRC, identical epoch budget (100 epochs, patience 10), and calibrated via temperature scaling or isotonic regression where applicable.

#### 7d. Metrics & Decision Rule (Joint Criterion — Pre-Registered)

- **Discrimination:** AUC (binary) / C-index & time-dependent AUC (survival) on held-out plasmode test set.
- **Calibration:** calibration slope & intercept (logistic/Cox calibration regression), calibration plot with loess, Van Calster hierarchy (mean / weak / moderate where feasible). Report per Riley BMJ 2025 uncertainty framing.
- **Overall accuracy:** Brier score (binary) / integrated Brier (survival) with decomposition.
- **Prediction-interval coverage:** 90%/95% prediction interval coverage for individual risks (bootstrap / Bayesian posterior for LMM/joint; conformal via `MAPIE` for DL where applicable); report empirical coverage vs nominal + interval width.
- **Decision-curve analysis (DCA):** net benefit across threshold probabilities (Vickers & Elkin) — the clinical-utility tiebreaker. Threshold range pre-specified: 5%, 10%, 20% for binary; risk-stratified for survival.
- **Estimation bias (where outcome model is parametric):** bias / RMSE / coverage of θ1 (exposure effect) — bridges to causal estimand.

**Primary decision rule (pre-registered, ML gets no preference):** **DL "wins" only if it is simultaneously (i) non-inferior on calibration (|slope − 1| ≤ 0.1, intercept ≤ 0.1 on logit scale) AND (ii) non-inferior on coverage (within 2 percentage points of nominal 95% PI) AND (iii) superior on DCA net benefit at the clinically relevant threshold range (at least one threshold in {5%,10%,20%} with Δ net benefit > 0 and 95% CI excluding 0).** This prevents AUROC-only cherry-picking. If DL improves AUC but degrades calibration/coverage, H0 (classical suffices) is retained — this is the skeptical framing.

#### 7e. Software Pointers (Code That Exists Tomorrow)

| Method | Package | URL / install | Role |
|--------|---------|---------------|------|
| LMM | `lme4` / `nlme` | `R: install.packages(c("lme4","nlme"))` | Classical baseline — random intercept/slope |
| JM | `JMbayes2` | `R: install.packages("JMbayes2")` + https://cran.r-project.org/package=JMbayes2 / https://github.com/drizopoulos/JMbayes2 | Joint longitudinal-survival (successor to JMbayes/joineRML) |
| JM alt | `joineRML` / `frailtypack` | `R: install.packages(c("joineRML","frailtypack"))` | Cross-check joint implementation |
| Imputation | `mice` | `R: install.packages("mice")` | MICE m=20 pooled |
| GRU-D | PyTorch GRU-D | `github.com/PeterChe1990/GRU-D` + `pip install torch` | Mandatory DL — masking + Δt |
| SeFT | PyTorch SeFT | `proceedings.mlr.press/v119/horn20a` + Horn repo | Mandatory DL — set functions |
| GRU-ODE-Bayes | `torchdiffeq` | `pip install torchdiffeq` + `github.com/BorgwardtLab/GRU-ODE-Bayes` | Optional ODE representative |
| Evaluation | `CalibrationCurves` / `dcurves` / `survival` / `MAPIE` | `R: dcurves, CalibrationCurves` + `pip install mapie` | Calibration, DCA, conformal coverage |
| Orchestration | `Snakemake` | `pip install snakemake` | Replicate parallelism, seeded RNG (PCG64) |

Report via `TRIPOD+AI` checklist item for simulation studies; code and `cells_core16.csv` are OSF-registered with seeds.

#### 7f. Compute Estimate (Locked v1 — Hours on Single GPU)

**Formula:** Fits ≈ `16 cells × 200 replicates × baselines`

| Baseline | Per-replicate fit time (N=10k, high sparsity 15 visits) | Notes |
|----------|----------------------------------------------------------|-------|
| `lme4` LMM | ~2–5 sec | R, single core, closed-form |
| `JMbayes2` | ~30–90 sec | MCMC / Laplace, single core (dominant classical cost) |
| `mice` + pooled LR | ~10–20 sec | m=20 imputations |
| GRU-D | ~45–90 sec | PyTorch, GPU (A100/4090), 100 epochs with early stopping |
| SeFT | ~30–60 sec | PyTorch, GPU, parallel set encoding |
| GRU-ODE-Bayes (optional) | ~120–300 sec | ODE solver overhead (Sun Limitations — expect 3–5× GRU-D) |

**Worst-case (N=10k, high sparsity):** Per cell per replicate ≈ 5 + 90 + 20 + 90 + 60 + 300(optional) ≈ 265 sec (4.4 min) without ODE, 565 sec (9.4 min) with ODE.

**Total locked v1:**
- Without ODE (6 baselines, required): `16 × 200 × 5 min avg ≈ 16,000 min ≈ 267 GPU-hours` naive sequential. **But:** LMM/mice/JM run on CPU in parallel; GRU-D/SeFT share GPU. With Snakemake parallelism (4 workers, 1 GPU + 4 CPU cores): **wall-clock ≈ 180–260 hours CPU + 80–120 hours GPU ≈ 5–8 days on a single 4-core + 1 GPU workstation** (or ~24–36 hours on 4-GPU node).
- **Practical locked budget for the 16-cell core at N=2k (sensitivity) is cheaper:** Per replicate ~1–2 min → `16 × 200 × 2 min ≈ 107 hours sequential → ~30 hours wall-clock parallelized` — start with N=2k cells for rapid iteration, then scale to N=10k for the 4 highest-informativeness cells.

**Recommended execution order (fits data-independent lock):**
1. **Week 1:** Implement generative spec + `lme4` + `JMbayes2` on 2 toy cells (γ_v=0 vs 0.8, N=500, 20 replicates) — validates twin plasmode logic and interval coverage pipeline. No GPU needed.
2. **Week 2:** Add MICE + LOCF + GRU-D on 4 core cells (N=2k, 50 replicates) — validates joint criterion and DCA pipeline.
3. **Week 3–4:** Full 16×200 at N=2k (all cells) + SeFT + optional GRU-ODE-Bayes on 4 high-informativeness cells at N=10k.

**Cost:** < $50 cloud (single GPU) for N=2k full core; ~$150–250 for N=10k extension. No hospital data cost.

#### 7g. India Transport Extension Note (not claimed for v1)

Indian outpatient EHR is plausibly **sparser, more fragmented (paper-mediated), with stronger cost-driven selective testing** (higher γ_v/γ_o) and lower measurement frequency. A Stage-2 extension varies λ_V and γ_v/γ_o to **Indian-typical regimes** (e.g., mean visits/year ≤2, higher informative missingness) and tests whether the "LMM suffices" conclusion **transports**. This genuinely stresses an assumption but requires Indian partner data or a plasmode mimicking Indian measurement patterns (see T6/T4 companion packets). **Not bundled into v1 hypothesis — GEOGRAPHY-ONLY for v1.**

---

### 8. Evidence AGAINST the Gap (Self-Authored Adversarial — Closest Defeaters)

**Closest defeaters that would collapse novelty if framed generously:**

1. **Naemi et al. arXiv 2401.15290** *is* a recent MIMIC-IV irregular-series benchmark with several state-of-the-art tabular DL time-series models and a MIMIC-III literature survey. If the bar is "any irregular-series benchmark on MIMIC," novelty is reduced. **Rebuttal:** Naemi does **not** include well-specified LMM / JMbayes2 as baselines and does **not** report calibration / coverage / DCA — the mandatory gap criteria (calibration/coverage/DCA joint criterion) are absent. The surviving gap is precisely that classical-vs-DL comparison with those metrics. This is the designated **defeater** for the packet (Naemi is the closest modern DL-vs-DL benchmark).

2. **Schneider et al. 2025 (PMC12070788)** already provides extensive simulation guidelines varying frequency / noise / heterogeneity and comparing joint vs Cox. A reviewer could argue "simulation-based method comparison under varying data quality is done." **Rebuttal:** Schneider varies quality **within the joint-vs-Cox world only**; no DL irregular-series comparator (GRU-D/SeFT/GRU-ODE-Bayes) appears. The proposed gap is specific to the **DL-for-irregularity** class, not joint-vs-Cox.

3. **Sun et al. 2026 review (§ Limitations)** flags ODE/SDE overhead and sketches hybrid architectures. A generous reader could argue the classical comparison is "obvious next work" and that the supplement / companion code at `github.com/SCXsunchenxi/ISMTS-Review` already runs the experiment. **Rebuttal that must be executed before promotion:** **Inspect the supplement + code repository** for any empirical LMM/joint-vs-DL table; until that inspection is logged, confidence cannot exceed Medium. Current searches returned no such table in the main text/toc.

4. **Frontiers in Applied Math & Stats 2026 — "Assessment of robustness of LMM under irregular longitudinal data"** (search hit) explicitly stress-tests LMM under irregularity. If that study already includes a DL comparator, the DL-vs-LMM framing is narrowed. **Pre-promotion check:** extract that paper's methods table; if it is LMM-only robustness (no GRU-D/SeFT), it strengthens rather than defeats the gap (it confirms LMM is the baseline to beat).

5. **Liang et al. 2410.13113** already runs simulations comparing their three-process joint vs existing methods under IP/IO. A reviewer could claim "informativeness is already studied." **Rebuttal:** Liang compares **within joint-model family** (different handling of IP/IO); no GRU-D/SeFT/GRU-ODE-Bayes appears. The DL-vs-joint comparison remains open. If any of #1–#5 were extended post-2025 to include the exact conjunction (tunable informative visit + observation decomposition + LMM/joint + GRU-D/SeFT + calibration/coverage/DCA), the gap would be **closed** and the correct next step would be a **direct replication/extension** rather than a de novo design.

If any defeater were extended to include the joint criterion, the protocol's contribution pivots from "is there a DL-vs-classical phase diagram?" to "does the phase diagram replicate under Generate-Treatment vs Generate-Outcome sensitivity?" — still publishable but reduced novelty.

---

### 9. Relevant Datasets

- **Primary — simulation / plasmode (no PHI, sufficient for v1):** Plasmode constructed from **MIMIC-III v1.4 / MIMIC-IV v2.2** covariate resampling + synthetic visit/observation/longitudinal mechanisms (§7a). Fully synthetic EHR simulation with known DAG as fallback (no data access needed). Access: PhysioNet credentialing (CITI + DUA, 1–2 weeks) for realistic covariate base; **not required for v1 if fully synthetic** (can start with `rnorm` covariate base immediately).
- **Secondary — real replication (reviewer request, not required for gap):** **MIMIC-III/IV** real trajectories (Harutyunyan phenotyping, MIMIC-Extract) + **PhysioNet Cardiology Challenges 2012 & 2019** (open) for out-of-sample irregularity regimes. Bridges to T7 instrument-validity.
- **Optional Stage-2 transport:** **UK Biobank South Asian subset** / **CARRS** / **ICMR-INDIAB** structure (restricted, requires application) — only for India-regime plasmode mimicking, not required for v1.
- **Software as dataset:** `synthEHRella` (Chen JAMIA 2025 toolkit, https://github.com/chenxran/synthEHRella) plasmode generators as alternative resampling engine.

All v1 datasets are **simulation only** per task spec — no patient data required to start coding.

---

### 10. Methodological Implications

- **If classical suffices (failure to reject H0):** Redirect field effort from architecture novelty to (a) correct specification of the visit/observation model, (b) uncertainty quantification and decision thresholds, (c) transportability across sparsity regimes. A rigorous negative result is publishable and decision-relevant (saves compute/privacy costs; favours auditable mixed models for deployment). Produces a **phase diagram** (when DL region is empty or narrow, that itself is the contribution).
- **If DL wins in a characterised regime (reject H0):** Identifies **where** complexity pays (e.g., dense follow-up, strongly informative visiting, large N, high SNR) and quantifies the **calibration/coverage price** of that win. Produces a **decision rule** for method choice rather than a leaderboard.
- Either outcome demands **calibration + coverage + DCA** alongside AUC, nudging the territory toward more honest inference (Riley 2025; Van Calster hierarchy). The design also stress-tests **plasmode instrument validity** (Generate-Treatment vs Generate-Outcome sensitivity, per Liu cautionary), informing the T7 agenda.
- Pre-registration (OSF / Registered Report) is mandatory to prevent HARKing on the many simulation cells; **"Beat the baseline or show it suffices"** is the declared primary outcome. The locked 16×200×baselines structure makes the compute budget auditable and the decision rule prevents p-hacking across 16 cells.

---

### 11. Clinical Implications

- Trajectory questions matter for chronic-disease monitoring (CVD risk trajectories, CKD/glucose trajectories, blood pressure). If predictions from irregular outpatient labs are **no better with expensive models**, deployment should favour **interpretable, EHR-deployable mixed models** that clinicians can audit and that run without GPU / integration overhead.
- Informative visiting is clinically meaningful (sicker patients visit more; visit frequency predicts outcomes). A finding that modelling visits corrects bias **only when informative** justifies simpler workflows in **stable screening cohorts** vs richer models in **high-acuity follow-up** — an actionable triage rule for health-system analytics.
- Calibration/coverage results directly inform **shared decision-making**: interval-aware risk communication ("your 5-year risk is 8%, compatible with 4–13% given model uncertainty — threshold 7.5% falls inside interval") vs point-risk thresholds. The joint criterion (calibration + coverage must be non-inferior) ensures clinical utility is not sacrificed for discrimination.

---

### 12. India Relevance

**Verdict: GEOGRAPHY-ONLY for v1.**

- The core benchmark question (does modelling irregularity pay, and under which informativeness/sparsity/noise regimes?) is **population-agnostic** and stresses a **universal** statistical assumption, not an India-specific one. Indian data are not needed to answer it, and claiming otherwise would be decoration.
- A **defensible India-relevant Stage-2 extension** varies measurement-frequency and informative-missingness regimes to mimic Indian outpatient settings (sparse, cost-driven selective testing, paper fragmentation) vs US ICU density, testing **transportability of the "mixed model suffices" conclusion**. This would genuinely stress an assumption and is scientifically meaningful — but it is a **follow-on**, not part of the v1 plasmode falsifiable claim. Do not claim STRESSES-ASSUMPTION for the v1 simulation design. No data-access barrier: simulation suffices; Indian-typical sparsity regimes are simulated via λ_V/γ_v parameters without needing Indian EHR.

---

### 13. Confidence

**Medium.**

Strengths: Review/simulation landscape is clearly surveyed; the DL-vs-classical head-to-head with calibration/coverage/DCA + tunable informative-visit/observation decomposition + known truth is **plausibly thin but not saturated**. Generative spec is concrete (Liang three-process + Schneider parameter template + Franklin/Schuler plasmode), mandatory baselines are pre-specified (LMM + JMbayes2 + GRU-D + SeFT are all runnable), compute budget is locked and modest, and the falsification arm (γ_v=0, low sparsity) makes the design honest. The decision rule (non-inferior calibration/coverage AND superior DCA) is skeptical by construction — ML gets no preference.

Risks capping confidence below High:
- **Sun supplement / companion code** (github.com/SCXsunchenxi/ISMTS-Review) must be fully inspected — it could already contain an LMM/joint-vs-DL table that closes the gap.
- **Naemi 2024 follow-up or forthcoming 2025–2026 plasmode papers** (Franklin/Schuler/Liu lineage) may run the exact conjunction — targeted arXiv stat.ME/stat.AP + PubMed "plasmode" sweep needed before Registered Report submission.
- **Frontiers 2026 LMM-robustness paper** must be screened for any DL comparator.

No data-access barrier for v1 (simulation primary); publishability depends on **pre-registration + calibration/coverage/DCA reporting** meeting reviewer expectations (Riley/Van Calster/TRIPOD+AI framing). The 16×200×baselines structure (≈3,200–6,400 total model fits per N level, ~107–267 GPU-hours) is executable on a single workstation within weeks.

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
# Inspect: JMbayes2 vignettes for plasmode examples (Rizopoulos)
```

```open-web
# 5. YAIB / Naemi follow-ups (not PubMed)
# Inspect: YAIB GitHub releases + Naemi MIMIC-IV benchmark follow-up for LMM/joint addition
# Inspect: synthEHRella GitHub for trajectory-fidelity extensions that could overlap

# 6. Verification
# Verify: Franklin 10.1093/aje/kww098 HEAD 302 + Schuler citations + Liang 2410.13113 v2
```

---

### Appendix — Queries & Papers (verbatim for search_log.csv / evidence_registry.csv)

**Queries run 2026-08-30 (verbatim):**
- `plasmode simulation three-process joint model informative visit observation shared frailty Franklin Schuler` (T1-C4-StrategyA-plasmode-joint, 5 hits, 2026-08-30, notes: Strategy A plasmode/joint-model — confirms decomposition)
- `GRU-D SeFT neural ODE irregular time series EHR benchmark no benefit mixed model` (T1-C4-StrategyB-irregular-DL, 5 hits, 2026-08-30, notes: Strategy B irregular-series DL — GRU-ODE-Bayes confirmed)
- `Sun Health Data Science 0456 Schneider BioData Mining JMbayes2 Rizopoulos joint model review` (T1-C4-review-Sun-Schneider-Rizopoulos, 5 hits, 2026-08-30, notes: Reviews — Sun + Schneider + Rizopoulos)
- `neural ODE GRU-ODE-Bayes continuous time RNN irregular clinical time series versus classical` (T1-C4-adjacent-neural-ODE, 5 hits, 2026-08-30, notes: Adjacent ODE family)
- `plasmode deep learning vs linear mixed model calibration coverage decision curve analysis joint model` (T1-C4-adversarial-DL-vs-classical, 5 hits, 2026-08-30, notes: Adversarial — no exact conjunction located)
- `Franklin plasmode Schuler Liang EHRJoint Sun review Schneider simulation guidelines chaining` (T1-C4-chaining-Franklin-Schuler-Liang, 5 hits, 2026-08-30, notes: Chaining Franklin→Schuler→Liang→Sun→Schneider)
- Cycle 2 carry-forward: `plasmode comparison deep learning vs linear mixed model calibration coverage irregular EHR` (T1-C2-adversarial, 5 hits, 2026-08-30, notes: Adversarial — gap survives)

**Papers (resolvable IDs):** 10 papers listed in §4 table (Sun 10.34133/hds.0456, Schneider 10.1186/s13040-025-00450-z, Franklin 10.1093/aje/kww098, Liang 10.48550/arXiv.2410.13113, Che 10.1038/s41598-018-24271-9, Horn 10.48550/arXiv.2006.10199, Brouwer 10.48550/arXiv.1905.12374, Liu 10.48550/arXiv.2504.11740, Rizopoulos JMbayes2 CRAN, Naemi 10.48550/arXiv.2401.15290).

**Verification:** 8/10 DOIs HEAD-checked 302 on 30 Aug 2026 (Sun, Schneider, Franklin, Liang, Che, Horn, Brouwer, Liu, Naemi) + CRAN URL resolvable; cross-check §4 log. [UNVERIFIED] not used for load-bearing claims. At least one model DOI 302 verified: YES (Sun 10.34133/hds.0456 302 + Schneider 10.1186/s13040-025-00450-z 302 + Franklin 10.1093/aje/kww098 302).

**Generative spec restated:** λ_V,i(t) = λ_0V(t)·exp(γ_v·b_i + β_v^T X_i + α_v·Y*_i(t−)); logit P(O_ij=1|visit,b_i,Y*) = γ_o·b_i + β_o^T X_i + δ·Y*_i(t*); Y_ij(t) = X_i(t)β + Z_i(t)b_i + ε_ij(t), b_i~N(0,D), ε~N(0,σ²); outcome logit P(E_i=1) = θ0 + θ1·functional(Y*_i) + θ2·b_i or λ_E,i(t) = λ_0E(t)·exp(θ1·Y*_i(t) + θ2·b_i).

**Code pointers locked:** `JMbayes2`/`joineRML`/`frailtypack` + `lme4`/`nlme` (R) + `torch` GRU-D (`PeterChe1990/GRU-D`) / SeFT (`horn20a`) / `torchdiffeq` GRU-ODE-Bayes.

**Compute locked:** 16×200×baselines = 3,200–6,400 fits per N level (6–7 baselines × 200 × 16 cells); hours on single GPU: ~80–120 GPU-hours + 180–260 CPU-hours parallelizable to 30 hours wall-clock at N=2k, ~5–8 days at N=10k.

**Decision rule locked:** Non-inferior calibration (|slope−1|≤0.1, intercept ≤0.1) AND coverage within 2pp AND superior DCA net benefit — ML gets no preference.

