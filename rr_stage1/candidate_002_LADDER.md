# RR Stage-1 — Candidate 002 Fidelity→τ Ladder via synthEHRella: When Synthetic EHR Fidelity Preserves Methods Ranking

**Registered Report Stage 1 — Introduction + Methods (no Results)**
**OSF companion:** `osf_prereg/candidate_002_OSF_TIMESTAMPED.md` (Registration date: 2026-08-30 · Git rev 70730ae984ae0d2592c28a9d13a0179eed14e6d4 · Code archive `pilots/candidate_002/synthEHRella` @ 74aa516 · Seed 20260830)
**Checklist:** S1–S5 ladder locked, τ ≥0.7 (LB ≥0.5) on TEST_R + TEST_TRANSPORT, DCA 10% / 20%, MIMIC-III → IV transport
**Verification:** pilot exit 0 — `pilots/candidate_002/logs/pilot_002.log` (2026-08-30T10:10:11Z, Python 3.11.15), `pilots/candidate_002/outputs/pilot_002_fidelity_tau.csv`, `pilot_002_utility.csv`, `pilot_002_dca.csv`, `pilot_002_calibration_*.csv`
**Status:** RR Stage-1 submission-ready (Results TBD — registered)

---

## 1. Introduction

### 1.1 The synthetic EHR promise and the missing threshold

Synthetic electronic health records (EHRs) are promoted as privacy-safe substitutes for methods development: generate a synthetic TRAIN that mimics MIMIC-III, train competing clinical prediction methods on synthetic, and claim the winner would also win on real data. The recent scoping review by **Chen et al. JAMIA 2025 (DOI 10.1093/jamia/ocaf082)** makes this promise concrete. Chen surveyed **48 studies across 5 generation categories** (GAN, VAE, diffusion, rule-based, plasmode) and benchmarked **7 methods + 2 baselines on MIMIC-III/IV phenotype data**, scoring each generator on fidelity (MMD, RMSPE, correlation recovery, prevalence gap, discriminative AUC), utility (TSTR AUC gap, association recovery), privacy (membership/attribute disclosure), and compute — and released the open toolkit **synthEHRella** (`github.com/chenxran/synthEHRella`) with a `run_generation → run_postprocessing → run_evaluation` pipeline for MIMIC-III/IV PhecodeX. Chen's decision tree helps pick a generator, but **does not answer the instrument-validity question**: at what fidelity is synthetic good enough to **license a methods conclusion** (e.g., "GRU-D beats logistic by ΔAUC 0.03")?

The closest empirical audit of prediction-model quality underscores the risk of unverified methods claims. **Queiroz et al. BMC Endocrine Disorders 2026 (PMC13169604) audited 97 T2DM models from 65 studies (15,796 screened): only 21.6% were externally validated and 91.8% were PROBAST high risk of bias (Analysis domain 83.5%)** — a canonical example of methods ranking without credible validation. Reviews of calibration reporting (Heus et al., Wynants et al., Jin et al. Diagn Progn Res 2026 TRIPOD audit of 1,529 screens) find overall calibration is itself rarely reported, let alone stratified. If real-data methods papers already fail validity, synthetic-supported claims without a fidelity→τ threshold are doubly fragile.

Our pilot (see §1.3) shows why **fidelity without ranking preservation is non-discriminative**: the S1 (bootstrap high-fidelity) vs S5 (prevalence-random low-fidelity) 2-point ladder produced **τ = 1.0 for both** despite stark fidelity and utility gaps (MMD 0.088 vs 0.070 non-monotonic under fallback, but corr_fro 0.40 vs 4.06 and TSTR logistic AUC 0.850 vs 0.553). A naïve "high fidelity = good" rule would not have distinguished them by τ in this underpowered 2-method pilot — motivating a **calibrated fidelity→τ curve** with more methods and replicates.

### 1.2 Liu plasmode fragility — why ranking can flip

**Liu et al. arXiv 2504.11740 ("A cautionary note for plasmode simulation studies in the setting of causal inference", 55 pages, 6 tables)** demonstrates that plasmode simulation is **non-discriminative by construction choice**. Generate-Treatment (resample covariates X, overlay treatment mechanism) vs Generate-Outcome (resample X, overlay outcome mechanism) have **different statistical guarantees**: outcome-generating plasmode can make propensity-score estimators appear overly biased with under-coverage, even when they are well-calibrated on real data. In synthetic EHR terms, the **generator mechanism itself biases which method wins**. A synthetic benchmark that reports AUROC on one plasmode variant may invert the ranking on the dual variant. Any claim of "synthetic preserves methods ranking" must therefore (a) **pre-register the plasmode variant (S1 vs S1')**, (b) report both as sensitivity, and (c) demand replication on **held-out real TEST_R** and **transport TEST (MIMIC-IV)** — not just TSTR in-distribution.

Liu's warning aligns with Franklin et al. Am J Epidemiol 2014 (plasmode foundations: resample covariates from real EHR then overlay known outcome) and with the broader evaluation literature where **TSTR (train-synthetic-test-real) is reported as a utility proxy but rarely tied to ranking preservation** (Shoshan et al. ICML 2023 "Synthetic Data for Model Selection" does report rank correlation on general tabular data, but **not on EHR with Kendall τ + DCA + fidelity ladder** — the gap survives our adversarial sweep).

### 1.3 What the pilot proved (2-point ladder)

The Tier-1 **plasmode pilot** (`pilots/candidate_002/run_pilot_002.py`, `run_pilot_002.sh`) executed **exit 0 on 2026-08-30T10:10:11Z** with Python 3.11.15, `synthEHRella 1.0.0 @ 74aa516` (imports `evaluation.fidelity`, `utility`, `privacy` OK; `run_generation --help` and `run_evaluation --help` exercised). Because MIMIC-III requires PhysioNet credentialing, the pilot used an **honest synthetic fallback (5k rows, 26 columns, prevalence 0.506, train 4000 / test 1000, seed 20260830)** — explicitly logged as fallback, not real MIMIC.

| Operating point | Generator | mmd_max_gap | rmspe | corr_fro | discriminative AUC | fidelity composite |
|-----------------|-----------|-------------|-------|----------|--------------------|--------------------|
| S1 bootstrap | Bootstrap (ceiling) | 0.088 | 1.146 | 0.400 | 0.500 | 0.714 |
| S5 prevalence-random | Random floor | 0.070 | 2.180 | 4.057 | 0.508 | 0.198 |

Utility (TRTR vs TSTR):

| Train | logistic AUC | tree AUC | winner | ΔAUC |
|-------|--------------|----------|--------|------|
| TRTR (real) | 0.852 | 0.798 | logistic | 0.053 |
| TSTR S1 | 0.850 | 0.793 | logistic | 0.057 |
| TSTR S5 | 0.553 | 0.536 | logistic | 0.017 |

Both points gave **Kendall τ = 1.0, Spearman ρ = 1.0** (real_order logistic>tree vs synth_order logistic>tree) — **non-discriminative on 2 methods** despite TSTR collapse on S5. This **is the gap**: fidelity metrics and TSTR utility alone do not guarantee that the **decision** "which method is best for clinical use" is preserved. The pilot also produced **DCA net benefit at 10% and 20%**:

| Train | method | pt=0.1 NB | pt=0.2 NB |
|-------|--------|-----------|-----------|
| TRTR logistic | 0.457 | 0.411 |
| TRTR tree | 0.447 | 0.393 |
| TSTR S1 logistic | 0.456 | 0.412 |
| TSTR S1 tree | 0.443 | 0.385 |
| TSTR S5 logistic | 0.451 | 0.383 |
| TSTR S5 tree | 0.449 | 0.380 |
| treat_all | — | 0.451 | 0.383 |
| treat_none | — | 0.0 | 0.0 |

DCA ranking (logistic > tree at both thresholds on TRTR) was **preserved on S1 but compressed on S5** (logistic still > tree, but NB close to treat_all — clinically meaningless). Calibration stubs (`pilot_002_calibration_TRTR_logistic.csv`, `TSTR_S1`, `TSTR_S5`) show S5 predictions concentrate in 0.4–0.6 bins (poor calibration), previewing how **calibration at the decision threshold** (Van Calster hierarchy) mediates DCA.

**Implications for Stage-1:** (1) 2 methods are insufficient — need **4–6 methods** to make τ informative; (2) need 30–50 replicates per point for bootstrap CI; (3) need full **S1/S1′/S2-low/mid/high/S3/S4/S5 8-point ladder** to trace τ(fidelity) and locate **f* where τ ≥0.7 LB ≥0.5**.

### 1.4 Van Calster calibration hierarchy — why DCA needs calibration

**Van Calster et al. J Clin Epidemiol 2016 (DOI 10.1016/j.jclinepi.2015.12.005)** defines calibration hierarchy: mean → weak (slope/intercept) → moderate (loess vs 45°) → strong. DCA net benefit at a fixed threshold p_t = 10% or 20% (Vickers & Elkin Med Decis Making 2006 10.1177/0272989X06289078) depends on **calibration at p_t**, not just AUROC. A synthetic generator can preserve AUROC ranking while inverting calibration-slope ranking — flipping the DCA winner and recommending a harmful model at deployment. We therefore co-register **three ranking estimands**: τ_AUC, τ_ICI, τ_DCA@10%/20% — and require **τ ≥0.7 LB ≥0.5 on both TEST_R and TEST_TRANSPORT for the AUROC primary and DCA co-primary**.

---

## 2. Falsifiable Question

**Primary (registered, decision-relevant):**

> *Across the fidelity ladder S1 / S1′ / S2-low / S2-mid / S2-high / S3 / S4 / S5 (8 operating points via synthEHRella, 30–50 plasmode replicates each, seeds pinned to 20260830), does there exist a calibrated fidelity threshold **f*** such that for all f ≥ f*, synthetic-supported **methods ranking** (among logistic/Cox, GBM/XGBoost, LSTM/GRU-D, RF) agrees with real-data ranking with **Kendall τ(f) ≥0.7 and lower 95% bootstrap CI ≥0.5** on **both** held-out TEST_R (MIMIC-III 20%) and TEST_TRANSPORT (MIMIC-IV), and is this threshold preserved when evaluated on DCA net-benefit ranking at p_t = 10% and 20%?*

**Negative framing (publishable either way — see §2.1):**

- **H0 (instrument fails / cautionary, publishable negative):** Across the ladder, synthetic-supported ranking does **not** preserve real-data ranking on both tests; **τ(f) <0.5 everywhere** or τ ≥0.7 only at the near-bootstrap ceiling S4 (resample-perfect) — so **synthetic cannot license methods claims without real-data replication**. Report at which fidelity τ plateaus and whether DCA ranking decouples from AUROC ranking.
- **H1 (instrument suffices above threshold, publishable positive):** There exists **f*** such that for f ≥ f*, **τ(f) ≥0.7 LB ≥0.5** on both TEST_R and TEST_TRANSPORT (and DCA co-primary holds) — license cheap privacy-safe methods development; threshold reported as "MMD < ε* and TSTR gap < δ* and corr recovery > r* ⇒ τ ≥0.7".

**Either outcome is a decision rule** (MMD/utility thresholds + generator-choice guidance + DCA caution), not a leaderboard — useful to methodologists and IRBs evaluating compute/privacy trade-offs. The threshold is **pre-registered** to prevent HARKing.

---

## 3. Methods (Registered — Stage 1, Results TBD)

### 3.1 Data & participants — tier D (immediate, no PHI beyond de-identified)

| Source | Role | Access | Timeline |
|--------|------|--------|----------|
| **MIMIC-III v1.4** (PhysioNet DOI 10.13026/C2XW26, n~38k stays) | **TRAIN pool (80% = TRAIN_R) + TEST_R (20% hold-out, stratified by mortality, seed 20260830)** — phenotype PhecodeX via synthEHRella `run_preprocessing`; same data Chen benchmarked | Credentialed (PhysioNet, CITI + DUA) | Days–2 weeks (auto-approved) |
| **MIMIC-IV v2.2** (PhysioNet DOI 10.13026/6MM1-EK67 / 10.13026/7EBG-V124, n~65k stays) | **TEST_TRANSPORT** — schema/temporal drift stress (ICD-9→10, new hospitals, coding changes); tests whether f* transports when evaluation distribution shifts | Same PhysioNet | Same |
| **SynthEHRella-generated synthetic lake** (S1–S5, 8 operating points, 30–50 draws each, seeded) | **Synthetic TRAIN lake**, n=|TRAIN_R| per point, PhecodeX post-processed via `run_postprocessing` | Generated locally via `synthEHRella` (open) | Immediate once MIMIC obtained |
| **Synthea** (Walonoski JAMIA 2018 10.1093/jamia/ocx079) | S3 rung: rule-based, MIMIC-independent, workflow-realistic but statistics-unfaithful | Open JAR | Immediate |

**Phenotype:** same as Candidate 001 (17 time-series + 5 static, 48h window, Harutyunyan-style) for mortality/LOS; MIMIC-Extract for reproducibility. Phecodes/PhecodeX where synthEHRella pipeline requires it. **Splits locked:** `TRAIN_R` (MIMIC-III 80%) for generator training + real training; `TEST_R` (MIMIC-III 20% hold-out, never seen by generators); `TEST_TRANSPORT` (MIMIC-IV).

**No prospective Indian hospital data for v1** — Stage-2 extension (see §6).

### 3.2 Fidelity ladder S1–S5 — 8 operating points (locked)

| Point | Generator family | Fidelity expectation | Param / synthEHRella method |
|-------|------------------|---------------------|------------------------------|
| **S1** | **Plasmode Generate-Treatment** (Franklin 2014; Liu preferred) | High (causal-appropriate) | Resample X from MIMIC covariates, overlay treatment mechanism |
| **S1′** | **Plasmode Generate-Outcome** (Liu fragility) | High but different bias — sensitivity | Resample X, overlay outcome mechanism |
| **S2-low** | GAN MedGAN/CorGAN epoch 10 | Low-mid | `cor-gan` checkpoint epoch 10 |
| **S2-mid** | GAN epoch 50 | Mid | epoch 50 |
| **S2-high** | GAN epoch 200 | High-mid | epoch 200 |
| **S3** | **Synthea** rule-based | Mid-low | `synthea` config |
| **S4** | **Resample bootstrap ceiling** | Ceiling (near-perfect fidelity) | Bootstrap resample, no model |
| **S5** | **Random floor** (permuted) | Floor (zero fidelity) | `p-r-random`, permuted columns |

All generators via `synthEHRella/run_generation.py` → `evaluation/fidelity.py + utility.py + privacy.py`. Cost ceiling **~1,500 fits** (see §3.5).

### 3.3 Methods compared — ranking objects (locked)

1. **Logistic regression (L2, tabular aggregation mean+last+mask-rate, Platt-scaled)**
2. **Cox / logistic with SOFA recalibration**
3. **GBM/XGBoost** (tuned on real validation only — no synthetic tuning)
4. **LSTM (Harutyunyan 2×128) / GRU-D** (Che et al. Sci Rep 2018 10.1038/s41598-018-24271-9, 2168 cites — mandatory DL baseline for irregularity: masking + Δt)
5. Optional **Random Forest** cross-check

All methods trained **identically** on either **real TRAIN_R** or **synthetic TRAIN_S** at each ladder point, evaluated on fixed TEST_R and TEST_TRANSPORT. Ranking is per test set — **never re-estimated on TEST**.

### 3.4 Estimands

- **Primary:** Kendall **τ** between two rankings (synthetic-train vs real-train) on held-out TEST. τ ∈ [-1,1].
- **Secondaries:** Spearman ρ, pairwise concordance = (1+τ)/2, winner concordance for 2-method collapse.
- **Utility ranking:** separate τ for **AUROC ranking** (primary), **calibration ICI ranking**, **DCA net-benefit ranking at 10% and 20%** (Vickers, co-primary for clinical claim).
- **Uncertainty:** Bootstrap 95% CI for τ (B=1,000 resamples over plasmode replicates + GAN seeds); Riley 10.1136/bmj-2024-080749 intervals for calibration uncertainty on underlying risks; calibration hierarchy per Van Calster.

### 3.5 Decision rule (pre-registered)

Synthetic at fidelity level f is **valid for methods benchmarking** iff **τ_f ≥0.7 AND 95% CI lower bound ≥0.5** on **both** TEST_R and TEST_TRANSPORT. Threshold τ ≥0.7 = substantial agreement (Cohen κ analogue); LB ≥0.5 ensures moderate agreement even at lower CI limit. For DCA co-primary, same rule applied to DCA@10% and DCA@20% NB rankings.

- **f*** = smallest fidelity where rule holds **monotonically above** (isotonic regression / change-point where τ crosses 0.7 and stays above). Estimate via isotonic fit of τ vs composite fidelity (first PC of MMD⁻¹, correlation recovery, 1−TSTR gap).
- **Cautionary trigger:** If no f achieves rule except S4 (resample), report **"synthetic is cautionary — methods claims require real-data replication"** (publishable negative, Liu framing).

### 3.6 Analysis plan (pseudo-code locked, seed 20260830)

```python
# LOCKED pipeline (seed 20260830) — deterministic
# 1. Split MIMIC-III 80/20 stratified by mortality (rng 20260830)
#    TRAIN_R, TEST_R; TEST_TRANSPORT = MIMIC-IV (held-out)
# 2. For each ladder point S in [S1, S1', S2-low, S2-mid, S2-high, S3, S4, S5]:
#      Generate synthetic TRAIN_S via synthEHRella (n=|TRAIN_R|, seeds pinned)
#      For each method m in [LR, Cox, GBM, LSTM/GRU-D, RF]:
#          Train m on TRAIN_S → predict on TEST_R + TEST_TRANSPORT
#          Compute AUROC (DeLong CI), AUPRC, ICI (calibration), DCA NB@10%/20%
# 3. Per ladder point S and per metric (AUROC / ICI / DCA10 / DCA20):
#      Ranking R_real = methods ordered by metric on TRAIN_R → TEST
#      Ranking R_S    = same metric on TRAIN_S → TEST
#      tau = Kendall(R_real, R_S); bootstrap 1000x → 95% CI
# 4. Plot tau vs fidelity (x = MMD + TSTR score from synthEHRella)
#    Decision: min fidelity f* where tau >=0.7 LB>=0.5 on both tests
# 5. Sensitivity: Liu dual — compare S1 vs S1' curves; Vickers DCA thresholds 5% sensitivity
```

All seeds pinned, synthEHRella commits hashed, `seeds.log` at freeze. Code archive `pilots/candidate_002/` SHA256 archived at OSF freeze.

### 3.7 Sample size & 1,500 fits budget

| Component | Count |
|-----------|-------|
| Ladder points | 8 (S1, S1′, S2×3, S3, S4, S5) |
| Methods | 4 core × 2 trainings (real + synthetic share) |
| Replicates | 30–50 plasmode replicates per point + 3–5 GAN seeds → ~320 synthetic datasets |
| Transport | ×2 tests (TEST_R + TEST_TRANSPORT) |
| **Total fits** | **~1,500 model trainings** |

**Compute:** Single GPU (A100/4090) — LSTM 2–4h per run × ~400 fits ≈ 80–120 GPU-h; LR/GBM CPU parallel. 4 GPUs → 2–3 days wall-clock. Cost <$200 cloud. Full 16-cell sweep staged post-pilot; OSF v1 locks the 1,500-fit decision scaffold. Pilot 2-point 5k-row fallback proved the orchestration in seconds — scaling is linear.

### 3.8 Metrics (joint — not AUROC-only)

- **Discrimination:** AUROC (DeLong), AUPRC (prevalence context)
- **Calibration:** Van Calster hierarchy: mean → weak (slope 0.8–1.2, intercept |·|<0.3) → moderate (loess plot with band) → strong; Riley uncertainty bands; ICI
- **Utility:** DCA net benefit at **10% and 20%** (primary), 5% sensitivity: NB(p_t)=(TP/N)−(FP/N)·p_t/(1−p_t); ranking on NB reported separately; threshold comparison vs treat-all/treat-none (pilot: treat_all NB 0.451@10%, 0.383@20% — synthetic must beat these)
- **Privacy (reported not thresholded):** membership inference AUC + attribute disclosure per `privacy.py` (Yan Patterns 2022 framing)
- **Compute:** wall-clock + GPU-h per generator (Chen taxonomy improvement)

### 3.9 Leakage checklist — 6 items (locked, checked per phase)

- [ ] No leakage of TEST_R / TEST_TRANSPORT into synthetic generator training (TRAIN_R only)
- [ ] No tuning of generator hyper-parameters on TEST sets
- [ ] No leakage of outcome into synthetic covariate generation beyond pre-registered S1/S1′ distinction
- [ ] Missing-data handling (forward-fill + mask indicator) identical across real and synthetic training; not re-estimated on TEST
- [ ] Seeds frozen before generating ranking curves (no peeking at τ_transport to pick fidelity)
- [ ] Code/data hashes (synthetic datasets + model checkpoints) SHA256-archived at OSF freeze (`git rev 70730ae`)

### 3.10 Harmonization — ricu / METRE / YAIB

Primary `ricu 0.5.8`; METRE/YAIB exploratory. Mapping stubs shared with Candidate 001 (17 vars, z-scored, 1h grid, mask indicator). Synthetic harmonization inherits same schema — synthEHRella PhecodeX mapping where applicable.

### 3.11 TRIPOD+AI 27-item mapping

Same as Candidate 001 §8 with adaptation: Items 6–7 (outcome/predictors) refer to mortality/LOS under synthetic vs real training; Item 10 model spec notes synthetic generators as part of pipeline; Item 16 validation emphasizes two-stage TEST_R (internal) + TEST_TRANSPORT (MIMIC-IV cross-version).

---

## 4. Ethics & privacy

- **De-identified public data** under PhysioNet DUA (MIMIC-III/IV); HIPAA Safe Harbor–equivalent date shifting; no re-identification attempted; no linkage to external identifiers. Synthea carries no privacy risk.
- **Credentialing:** CITI + PhysioNet approval + signed DUA before access; restricted to listed investigators; no redistribution beyond DUA. Synthetic datasets S1–S5 are generated on-premises and shared as **aggregate metrics** (no patient-level release).
- **IRB:** Exemption / not-human-subjects determination (de-identified, publicly shared for research) — protocol filed upon credentialing; OSF declares ethics path (no prospective Indian data for v1).
- **Privacy evaluation:** `evaluation/privacy.py` (membership inference AUC, attribute inference) **characterised per rung** but not gated — privacy is reported for IRB usefulness, not as threshold.
- **Dual-use:** Synthetic below f* must not be presented as replacing clinical validation — claim is *methods benchmarking only*, not deployment readiness.

---

## 5. India relevance — geography-only v1, meaningful Stage-2

**v1: GEOGRAPHY-ONLY** (per docs/03 §6 — claiming STRESSES-ASSUMPTION without specific assumption stressed would be decoration). Core question (does synthetic preserve methods ranking? at what fidelity?) is population-agnostic and methods-forward; Indian data not needed and claiming them would be decorative.

**Meaningful Stage-2 extension (not bundled, pre-registered as future):** Test whether a generator trained on US MIMIC preserves ranking when evaluated against an **Indian hospital test distribution** (CARRS Delhi/Chennai/Karachi, ICMR-INDIAB, or Indian ICU EHR — coding prevalence, measurement frequency, formulary, documentation completeness differ). Requires Indian partner data (DUA-track UKB-SA / CARRS / ICMR-INDIAB stays staged). Lock's **MIMIC-III → IV transport check is the proxy** for this logic on public data: if τ collapses on IV (ICD-9→10 + temporal shift), threshold is distribution-specific, not universal — CF Chen's MIMIC-III→IV generator degradation. Stage-2 would write the India-stress paper without re-claiming v1.

---

## 6. Pilot verification & code archive

**Verification: pilot exit 0**

| Artifact | Path | Rows / status |
|----------|------|---------------|
| Log | `pilots/candidate_002/logs/pilot_002.log` | 106 lines, exit 0, 2026-08-30T10:10:11Z, Python 3.11.15, git synthEHRella 74aa516, pip show 1.0.0, help flags OK |
| Fidelity+τ | `pilots/candidate_002/outputs/pilot_002_fidelity_tau.csv` | 2 rows (S1 bootstrap 0.088 MMD etc. vs S5 0.070), τ=1.0 both (non-discriminative — motivates 4–6 methods) |
| Utility | `pilots/candidate_002/outputs/pilot_002_utility.csv` | TRTR 0.852/0.798 vs TSTR S1 0.850/0.793 vs S5 0.553/0.536 |
| DCA | `pilots/candidate_002/outputs/pilot_002_dca.csv` | 16 rows: TRTR/TSTR S1+S5 logistic/tree @10%/20% + treat_all/treat_none |
| Calibration | `pilots/candidate_002/outputs/pilot_002_calibration_TRTR_logistic.csv` etc. | 10-bin calibration stub per TRTR/TSTR S1/S5 |
| Code archive | `pilots/candidate_002/synthEHRella @ 74aa516` | `git rev 70730ae` (repo), `synthEHRella/build` + `synthEHRella/synthEHRella/{data/evaluation}` |
| Seed | `20260830` | `numpy.random.default_rng(20260830)` + `torch.manual_seed(20260830)` |

Honest fallback declared: MIMIC-III demo not credentialed → 5k synthetic rows; real MIMIC would be credentialed for Stage-2.

---

## 7. References (verbatim DOIs already in dossiers)

- Chen et al. JAMIA 2025 10.1093/jamia/ocaf082 — scoping review 48 studies/5 categories + synthEHRella toolkit (load-bearing)
- Liu et al. arXiv 2504.11740 — plasmode cautionary (Generate-Treatment vs Generate-Outcome, non-discriminative)
- Yan et al. Patterns 2022 10.1016/j.patter.2022.100655 — multifaceted GAN benchmarking (closed-source critique)
- Van Calster et al. J Clin Epidemiol 2016 10.1016/j.jclinepi.2015.12.005 — calibration hierarchy
- Riley et al. BMJ 2025 10.1136/bmj-2024-080749 — uncertainty of risk estimates, Riley intervals
- Vickers & Elkin Med Decis Making 2006 10.1177/0272989X06289078 (update PMC6123195) — DCA net benefit
- Walonoski et al. JAMIA 2018 10.1093/jamia/ocx079 — Synthea
- Choi et al. arXiv 1703.03427 — MedGAN
- Che et al. Sci Rep 2018 10.1038/s41598-018-24271-9 — GRU-D
- Queiroz et al. BMC Endocr Disord 2026 10.1186/s12902-026-02301-2 (PMC13169604) — 97 models, 91.8% PROBAST high risk (defeater context)
- Collins TRIPOD 2015 10.1136/bmj.g7594 → TRIPOD+AI 2024 10.1136/bmj-2023-078378
- Angelopoulos & Bates 10.1561/2200000101 — conformal baseline

---

## 8. Appendix — pilot tables (verbatim excerpts)

**A. pilot_002_fidelity_tau.csv**

```
method,mmd_max_gap,rmspe,corr_fro,discriminative_auc,synth_method,kendall_tau,spearman_rho,concordant,real_order,synth_order,mmd,fidelity_composite
S1_bootstrap,0.0879,1.146,0.400,0.500,S1_bootstrap,1.0,1.0,1,logistic>tree,logistic>tree,0.088,0.714
S5_prevalence_random,0.0704,2.180,4.057,0.508,S5_prevalence_random,1.0,1.0,1,logistic>tree,logistic>tree,0.070,0.198
```

**B. pilot_002_utility.csv**

```
train,logistic_auc,tree_auc,winner,delta_auc
TRTR,0.852,0.798,logistic,0.053
TSTR_S1,0.850,0.793,logistic,0.057
TSTR_S5,0.553,0.536,logistic,0.017
```

**C. pilot_002_dca.csv (excerpt)**

```
train,method,pt,net_benefit
TRTR,logistic,0.1,0.457
TRTR,tree,0.1,0.447
TRTR,logistic,0.2,0.411
TRTR,tree,0.2,0.393
TSTR_S1,logistic,0.1,0.456
TSTR_S5,logistic,0.2,0.383
treat_all,all,0.1,0.451
treat_none,none,0.1,0.0
```

**D. Leakage 6-item + Van Calster levels + Wilson/κ analogues** documented in OSF §9–10.

---

*End of RR Stage-1 Methods — Results section intentionally left TBD (registered). Next: execute full ladder on credentialed MIMIC-III/IV, compute τ(f) curves, locate f*, report whether synthetic is cautionary or suffices above threshold.*

