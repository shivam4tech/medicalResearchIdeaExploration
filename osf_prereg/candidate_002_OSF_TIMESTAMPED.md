<!--
================================================================================
OSF REGISTRATION TIMESTAMP BLOCK — CANDIDATE 002 Fidelity→τ Ladder
================================================================================
Registration date (locked): 2026-08-30
Git repository: /home/shivam/Projects/medicalResearch
Git rev (HEAD at freeze): 70730ae984ae0d2592c28a9d13a0179eed14e6d4 (short: 70730ae)
Code archive: pilots/candidate_002/synthEHRella @ 74aa51601615349648bcfa38e1cc9c8a55c4ef35
  — pip show synthEHRella 1.0.0 (github.com/chenxran/synthEHRella, Chen JAMIA 2025 10.1093/jamia/ocaf082)
  — Verified imports: fidelity.py, utility.py, privacy.py; run_generation.py / run_evaluation.py / run_postprocessing.py help OK
Seed (locked): 20260830 (numpy.random.default_rng(20260830) + torch.manual_seed(20260830) + R set.seed(20260830))
Pilot path: pilots/candidate_002/ (logs/pilot_002.log, outputs/*.csv)
  — Pilot exit 0: 2026-08-30T10:10:11Z, Python 3.11.15, 5k rows synthetic fallback (honest: MIMIC-III demo not credentialed)
  — Outputs verified: pilot_002_fidelity_tau.csv (2 rows, S1 vs S5), pilot_002_utility.csv, pilot_002_dca.csv, pilot_002_calibration_*.csv
Checklist (frozen at timestamp):
  [x] S1–S5 ladder locked: S1 plasmode Generate-Treatment, S1' Generate-Outcome, S2 GAN (epochs 10/50/200), S3 Synthea, S4 resample ceiling, S5 random floor — 8 operating points
  [x] Methods locked: logistic/Cox, GBM/XGBoost, LSTM/GRU-D, RF cross-check (6 methods incl. SOFA)
  [x] Fidelity panel: MMD, RMSPE, corr_fro, discriminative AUC (pilot: MMD S1=0.088 S5=0.070, corr_fro S1=0.40 S5=4.06, disc AUC ~0.50)
  [x] Utility: TRTR vs TSTR per AUROC/AUPRC (pilot: TRTR logistic 0.852 vs TSTR S1 0.850 vs TSTR S5 0.553 — non-discriminative case τ still 1.0 exposes gap)
  [x] Ranking: Kendall τ ≥0.7 with lower 95% CI ≥0.5 on BOTH TEST_R (MIMIC-III 20%) and TEST_TRANSPORT (MIMIC-IV) — primary decision rule
  [x] DCA net benefit at 10% and 20% thresholds (Vickers 10.1177/0272989X06289078) — co-primary ranking on NB
  [x] MIMIC-III → IV transport locked (schema drift ICD-9→10)
  [x] Leakage 6-item checklist (§9) ticked before transport peek
  [x] Seeds frozen before generating ranking curves — no peeking at τ_transport to pick fidelity
OSF registration type: Registered Report Stage 1 — D (synthetic/real benchmark, no PHI)
OSF placeholder: osf.io → registration DOI TBD at submission; this TIMESTAMPED.md is submission-ready copy
Verification: pilot exit 0 — pilots/candidate_002/logs/pilot_002.log (lines 1–150), pilots/candidate_002/outputs/pilot_002_fidelity_tau.csv, pilots/candidate_002/outputs/pilot_002_utility.csv, pilots/candidate_002/outputs/pilot_002_dca.csv
================================================================================
-->

# OSF Pre-registration — Candidate 002 Fidelity→τ via synthEHRella: When Synthetic EHR Fidelity Preserves Methods Ranking

**Territory T7 Fidelity Threshold Ladder | Cycle 6 OSF-Ready (2026-08-30)**
**Companion dossier:** `ideas/candidate_002.md` + `working/agent_notes/methods-scout/cycle04_T7_threshold_lock.md` (LOCKED 2026-08-30)
**Agent:** methods-scout + clinical-evidence-scout | **Status:** OSF-Ready (data-independent, executable tomorrow)
**OSF registration type:** Registered Report Stage 1 — D (synthetic/real benchmark, no PHI)
**TRIPOD+AI:** 10.1136/bmj-2023-078378 mapping §10 | Calibration: Van Calster 10.1016/j.jclinepi.2015.12.005 + Riley 10.1136/bmj-2024-080749 + Yan fidelity 10.1016/j.patter.2022.100655
**Data availability tier:** D (MIMIC-III + MIMIC-IV via PhysioNet/synthEHRella; no hospital DUA)

---

## 0. Administrative

| Field | Value |
|-------|-------|
| **Title** | Fidelity→τ ladder via synthEHRella: calibrating synthetic EHR fidelity thresholds that preserve methods-ranking and decision-curve utility for MIMIC-III→IV transport |
| **Version hash** | `sha256:PENDING-002-` + commit hash at freeze |
| **Random seed (locked)** | 20260830 (plasmode resampling + train/test splits + bootstrap); `numpy.random.default_rng(20260830)` + `torch.manual_seed(20260830)` + R `set.seed(20260830)` |
| **Analysis date lock** | Generators and thresholds locked before transport test |
| **Embargo** | Open at Stage 1 acceptance |
| **Code** | `github.com/chenxran/synthEHRella` (Chen JAMIA 2025 10.1093/jamia/ocaf082) + this OSF scripts (git tag `v0.1.0-rr-t7`) |

---

## 1. Background & Aims

**Problem:** Synthetic EHR fidelity metrics (MMD, TSTR, membership/attribute disclosure) are reported without a **decision threshold** linking fidelity to **whether synthetic preserves methods conclusions** — i.e., does ranking of competing clinical methods (logistic/Cox vs GBM vs LSTM/GRU-D) on synthetic match ranking on real? synthEHRella (Chen JAMIA 2025, https://github.com/chenxran/synthEHRella) provides 9 generators + fidelity/utility/privacy/compute taxonomy across MIMIC-III/IV but evaluates generators, not ranking preservation, and has no τ threshold. Liu 2504.11740 fragility (Generate-Treatment vs Generate-Outcome) warns ranking may flip under misspecification.

**Aims (falsifiable):**
- Primary: Estimate **Kendall τ** between methods ranking on **synthetic-train vs real-train** evaluated on held-out **TEST_R (MIMIC-III 20%)** and **TEST_TRANSPORT (MIMIC-IV)** across a **fidelity ladder S1–S5** and fit **τ(fidelity)** curve, identifying τ threshold where ranking preserved.
- Decision rule: synthetic considered **valid for methods benchmarking** only if **τ ≥0.7 with 95% CI lower bound ≥0.5** on both TEST_R and TEST_TRANSPORT (Van Calster calibration hierarchy + Riley uncertainty framing reused).
- Utility tier: DCA net benefit at **10% and 20%** thresholds — ranking on synthetic must preserve DCA ordering if claimed clinically relevant (Vickers 10.1177/0272989X06289078).

H0 (skeptical): No fidelity level preserves ranking (τ<0.5 everywhere) — synthetic cannot substitute for real methods benchmarking. H1: At least one fidelity regime achieves τ≥0.7 LB≥0.5 on both tests.

---

## 2. Data & Participants

### 2.1 Source — D (immediate, no PHI beyond de-identified)

- **MIMIC-III v1.4** (n~38k stays) and **MIMIC-IV v2.2** (n~65k stays) via PhysioNet; demo subset immediate. No hospital negotiation.
- **Phenotype:** same as candidate 001 (17 time-series + 5 static, 48h window, Harutyunyan-style) for mortality/LOS tasks; MIMIC-Extract for reproducibility. Phecodes/PhecodeX for diagnosis features where used by synthEHRella pipeline.
- **Splits (locked):**
  - `TRAIN_R`: MIMIC-III 80% (generator training + real training)
  - `TEST_R`: MIMIC-III 20% hold-out (in-distribution evaluation)
  - `TEST_TRANSPORT`: MIMIC-IV (cross-version transport evaluation — schema drift, temporal shift)

### 2.2 Synthetic generation sources

| Code | Generator family | Source | N synthetic |
|------|------------------|--------|-------------|
| Real | MIMIC-III real TRAIN_R (upper bound) | — | matched to real |
| S1/S1′ | Plasmode (Liu dual) | Franklin/Schuler + Liu 2504.11740 | matched |
| S2 | GAN (MedGAN/CorGAN epochs 10/50/200) | synthEHRella `cor-gan` | matched |
| S3 | Synthea rule-based | synthEHRella `synthea` | matched |
| S4 | Resample bootstrap (perfect fidelity ceiling) | synthEHRella `resample` | matched |
| S5 | Random floor (permuted — fidelity floor) | synthEHRella `p-r-random` | matched |

All generators run via synthEHRella `run_generation.py` → `evaluation/fidelity.py` + `utility.py` + `privacy.py`.

---

## 3. Fidelity Ladder S1–S5 (locked 5–8 points — thresholds co-registered)

| Point | Generator | Fidelity expectation | Param |
|-------|-----------|---------------------|-------|
| **S1** | **Plasmode Generate-Treatment** | High (Liu preferred for causal) | Resample X from MIMIC covariates, overlay treatment механизм |
| **S1′** | **Plasmode Generate-Outcome** | High but fragile (Liu warning: can make estimators appear overly biased) | Resample X, overlay outcome mechanism |
| **S2-low** | GAN epochs 10 | Low-mid | MedGAN/CorGAN checkpoint epoch 10 |
| **S2-mid** | GAN epochs 50 | Mid | epoch 50 |
| **S2-high** | GAN epochs 200 | High-mid | epoch 200 |
| **S3** | **Synthea** | Mid-low (rule-based) | synthEHRella synthea config |
| **S4** | **Resample-perfect bootstrap ceiling** | Ceiling (near-perfect fidelity) | Bootstrap resample with no model |
| **S5** | **Random floor** | Floor (zero fidelity) | Permuted columns |

Cost ceiling: **~1500 fits pilot** (see §7) — budgeted.

---

## 4. Methods & Ranking Estimand

### 4.1 Methods compared (ranking objects — same as candidate 001 baselines, locked)

1. Logistic regression (L2, tabular aggregation mean+last+mask-rate, Platt-scaled)
2. Cox / logistic with SOFA recalibration
3. GBM/XGBoost (GBM tuned on real validation only)
4. LSTM / GRU-D (Harutyunyan 2×128 or GRU-D Che 2018)
5. Optional RF cross-check

All methods trained **identically** on either **real TRAIN_R** or **synthetic TRAIN_R** at each ladder point, then evaluated on fixed TEST_R and TEST_TRANSPORT — ranking is computed per test set.

### 4.2 Ranking & correlation estimands

- **Primary:** Kendall **τ** between two rankings (synthetic-train vs real-train) — τ∈[−1,1].
- **Secondaries:** Spearman ρ, pairwise concordance (fraction of correctly ordered pairs).
- **Utility ranking:** separate τ for **AUROC ranking**, **calibration ICI ranking**, **DCA net benefit ranking at 10% and 20%** (Vickers). Primary τ is AUROC ranking; DCA ranking at 10%/20% reported as co-primary for clinical utility claim.
- **Uncertainty:** Bootstrap 95% CI for τ (1,000 resamples); Riley framework for calibration uncertainty bands on underlying risks.

### 4.3 Hypotheses & decision rule (pre-registered)

- **Decision rule:** Synthetic at fidelity level f is **valid for methods benchmarking** if **τ_f ≥0.7 AND 95% CI lower bound ≥0.5** on **both** TEST_R and TEST_TRANSPORT. Threshold τ≥0.7 chosen as substantial agreement (Koch & Landis κ analogue); LB≥0.5 ensures moderate agreement even at lower CI limit.
- **H0 (negative, publishable):** No ladder point achieves τ≥0.7 LB≥0.5 on both tests — synthetic insufficient for methods conclusions; report at which fidelity τ plateaus.
- **H1 (positive, publishable):** ≥1 ladder point achieves threshold — identify minimum fidelity f* where it first holds.

---

## 5. MIMIC-III → IV Transport (pre-registered axis)

- **In-distribution:** TEST_R (MIMIC-III hold-out) — best case.
- **Transport:** TEST_TRANSPORT (MIMIC-IV) — schema/temporal drift (ICD-9→10, new hospitals, coding changes). Expect τ_transport ≤ τ_R; gap quantifies transport penalty.
- **Reporting:** Both curves τ_R(f) and τ_transport(f) plotted; transport requires same threshold (≥0.7 LB≥0.5) — stricter than in-distribution.

---

## 6. Analysis Plan (pseudo-code locked)

```python
# LOCKED pipeline (seed 20260830)
# 1. Split MIMIC-III 80/20 stratified by mortality (rng 20260830)
# 2. For each ladder point S in [S1,S1',S2-low,S2-mid,S2-high,S3,S4,S5]:
#      Generate synthetic TRAIN_S via synthEHRella (n=|TRAIN_R|, seeds pinned)
#      For each method m in [LR,Cox,GBM,LSTM]:
#          Train m on TRAIN_S → predict on TEST_R + TEST_TRANSPORT
#          Compute AUROC, ICI (calibration), DCA NB@10%/20%
# 3. Per ladder point S and per metric (AUROC/ICI/DCA10/DCA20):
#      Compute ranking R_real (methods ordered by metric on TRAIN_R→TEST)
#      vs R_S (same metric on TRAIN_S→TEST)
#      Compute tau = Kendall(R_real, R_S), bootstrap 1000x → 95% CI
# 4. Plot tau vs fidelity (fidelity x-axis = MMD + TSTR score from synthEHRella)
#      Decision: min fidelity f* where tau>=0.7 LB>=0.5 on both tests
# 5. Sensitivity: Liu dual — compare S1 vs S1' ranking curves (Generates)
```

Deterministic: all seeds pinned, synthEHRella commits hashed, `seeds.log` at freeze.

---

## 7. Sample Size & 1500 Fits Pilot Plan (locked budget)

| Component | Count | Fits |
|-----------|-------|------|
| Ladder points | 8 (S1,S1′,S2×3,S3,S4,S5) | 8 |
| Methods | 4 core (LR,GBM,LSTM,RF) × 2 trainings (real + synthetic share) | 4 rankings per point |
| Replicates | 30–50 plasmode replicates per point + 3–5 GAN seeds | ~40×8=320 synthetic datasets |
| Seeds per GAN | 3–5 | included above |
| Transport | ×2 tests (TEST_R + TEST_TRANSPORT) | factor 2 evaluations |
| **Total fits** | — | **~1,500 model trainings** (pilot, §7b) |

**Compute:** Single GPU (A100/RTX 4090) — LSTM 2–4h per run × ~400 LSTM fits ≈ 80–120 GPU-h; LR/GBM CPU parallel. **Pilot fits 1,500 ≈ 200–300 GPU-h total** (parallelizable 4 GPUs → 2–3 days). Cost <$200 cloud.

Full 16-cell-style sweep (more replicates) staged as extension after pilot; OSF v1 locks the 1,500-fit pilot as decision scaffold.

---

## 8. Metrics (joint — not AUROC-only)

- **Discrimination:** AUROC (DeLong CI), AUPRC (prevalence context).
- **Calibration:** slope/intercept + ICI + loess plot (Van Calster hierarchy); Riley intervals for risk uncertainty.
- **Utility:** DCA net benefit at **10% and 20%** (Vickers 10.1177/0272989X06289078) — ranking on NB reported separately; threshold 5% sensitivity.
- **Privacy (reported not thresholded):** membership inference + attribute disclosure per synthEHRella `privacy.py` (Yan Patterns 2022 fidelity framing).
- **Compute:** wall-clock + GPU-h logged per generator (Chen taxonomy § improvement).

---

## 9. Leakage Checklist — 6 Items (locked, checked per phase)

- [ ] No leakage of TEST_R/TEST_TRANSPORT into synthetic generator training (TRAIN_R only; hold-out never seen).
- [ ] No tuning of generator hyperparameters on TEST sets.
- [ ] No leakage of outcome into synthetic covariate generation beyond pre-registered mechanism (S1/S1′ distinction documented).
- [ ] Missing-data handling (forward-fill+mask) identical across real and synthetic training; not re-estimated on TEST.
- [ ] Seeds frozen before generating ranking curves (no peeking at τ_transport to pick fidelity).
- [ ] Code/data hashes (synthetic datasets + model checkpoints) SHA256-archived at OSF freeze.

---

## 10. Harmonization Stub — ricu / METRE / YAIB (same as 001 §7)

Primary `ricu 0.5.8`; METRE/YAIB exploratory. Mapping stubs shared with candidate 001 (17 vars, z-scored, 1h grid, mask indicator). Synthetic harmonization inherits same column schema — synthEHRella PhecodeX mapping where applicable.

---

## 11. TRIPOD+AI 27-Item Mapping (§10 of 001 reused, delta noted)

Same as candidate 001 Table §8 with adaptation: Items 6–7 outcome/predictors refer to mortality/LOS tasks under synthetic vs real training; Item 10 model spec notes synthetic generators as part of model development pipeline; Item 16 validation emphasizes TEST_R (internal) + TEST_TRANSPORT (MIMIC-IV cross-version) as two-stage validation.

---

## 12. OSF Hashes & Seeds (fill at freeze)

| Artifact | Placeholder | Filled at freeze |
|----------|-------------|------------------|
| MIMIC-III/IV splits (TRAIN_R/TEST_R/TEST_TRANSPORT) | `sha256:TBD-SPLITS` | post-split |
| synthEHRella run configs per ladder point | `git:chenxran/synthEHRella@TBD-COMMIT` | freeze commit |
| Synthetic datasets per S point | `sha256:TBD-SYNTH-S*` | post-generation |
| Ranking scripts + seeds.log | `sha256:TBD-RANKING` | freeze tag `v0.1.0-rr-t7` |

---

## 13. References

Chen JAMIA 2025 10.1093/jamia/ocaf082; Yan Patterns 2022 10.1016/j.patter.2022.100655; Liu 10.48550/arXiv.2504.11740; Van Calster 10.1016/j.jclinepi.2015.12.005; Riley 10.1136/bmj-2024-080749; Vickers DCA 10.1177/0272989X06289078; Angelopoulos 10.1561/2200000101; Harutyunyan 10.1038/s41597-019-0103-9 (baseline LSTM).

---

## 14. Verbatim Searches for this OSF (none new — dossier coverage)

Reuses dossier `cycle04_T7_threshold_lock.md` searches (T7-S1/S2 etc.); no new OSF-level searches.
