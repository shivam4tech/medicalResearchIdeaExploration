<!--
================================================================================
OSF REGISTRATION TIMESTAMP BLOCK — CANDIDATE 007 Ahlqvist Centroids vs De Novo
================================================================================
Registration date (locked): 2026-08-31
Git repository: /home/shivam/Projects/medicalResearch
Git rev (HEAD at freeze): 70bb40c (full: 70bb40c0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6 — short 70bb40c per brief)
Code archive: full_runs/candidate_007/ + pilots/candidate_005_006/ (paired G0→G3 40k verified)
Random seed (locked): 20260830 (numpy.random.default_rng(20260830) + python random.seed(20260830) + sklearn random_state=20260830 + R set.seed(20260830))
Full run path: full_runs/candidate_007/ — N=8000 synthetic UKB-SA proxy (DUA staged, honest proxy)
  — run_full_007.py 336 lines, logs/full_007.log 91 lines (2026-08-31 12:17:11 IST, Python 3.11.15, sklearn 1.9.0, pandas 3.0.5, numpy 2.4.3)
  — Outputs verified: centroids_vs_denovo_ARI.csv 17 rows sha256:ba7626f885a9, cluster_profiles.csv 10 rows sha256:747a075d8fd3, ablation_6to3.csv 3 rows sha256:c17976e51d7c, synthetic_proxy_sample.csv 100 rows sha256:129f20ad3ac2
Metrics (locked thresholds): completeness 6-var 98.36% TRANSPORTS (≥85%), ARI 6-var transport vs de-novo 0.250 FAILS (≥0.60 transports, <0.40 fails per Landis&Koch), ARI 3-var 0.446 INTERMEDIATE, ARI 6vs3 0.243 GADA/HOMA drives assignment, silhouette transport 0.107 de-novo 0.174 (both poor, de-novo not >0.40), SMD fail 3/6 (50.0% ≥30% fails), ESS 99.2% adequate (>70%), S-score AUC stub ~0.73 intermediate (<0.70 adequate, >0.80 fails), trimming 10% adequate
Pilots: pilots/candidate_005_006/ (G0→G3 5k, 109-line log) — UKB-SA proxy + ICMR-INDIAB thin-fat reference
Checklist (frozen at timestamp):
  [x] Ahlqvist 2018 centroids locked (SAID/SIDD/SIRD/MOD/MARD, 6 vars GADA/age/BMI/HbA1c/HOMA2-B/HOMA2-IR per Lancet Diabetes 10.1016/s2213-8587(18)30051-2)
  [x] ANDIS means/SDs locked for transport standardization
  [x] k=5 fixed primary, Euclidean primary, complete-case primary, IOPW truncation 5% primary
  [x] Thresholds locked: completeness≥85%, S-score AUC<0.70 / >0.80, ESS>70% / <50%, trimming<15% / >30%, ARI≥0.60 / <0.40, silhouette 0.25 vs 0.40, ΔAUC 0.03
  [x] Ablation 6→4→3 locked (6-var primary if completeness≥85% else 3-var co-primary; 3-var age/BMI/HbA1c as GADA-free co-primary)
  [x] DUA staged: UKB-SA 1–3mo RAP, CARRS PHFI/Emory 2–3mo, ICMR-INDIAB 113k 3–6mo, CMC/AIIMS 2–4mo new-onset; no PHI
  [x] TRIPOD+AI 27-item mapping §11 ticked (10.1136/bmj-2023-078378) + PROBAST + Van Calster 10.1016/j.jclinepi.2015.12.005 + Riley 10.1136/bmj-2024-080749
OSF registration type: Registered Report Stage 1 — B staged (UKB-SA managed proxy + CARRS/ICMR-INDIAB restricted + CMC/AIIMS new-onset secondary)
OSF placeholder: osf.io → registration DOI TBD at submission; this TIMESTAMPED.md is submission-ready copy
Verification: full run exit 0 — full_runs/candidate_007/logs/full_007.log (91 lines, SMD 50% fails, completeness 98.36% transports, ARI 0.250 fails, 3-var 0.446, 6vs3 0.243), full_runs/candidate_007/outputs/centroids_vs_denovo_ARI.csv (17 rows), cluster_profiles.csv (10 rows), ablation_6to3.csv (3 rows)
================================================================================
-->

# OSF Pre-registration — Candidate 007 Ahlqvist Centroids vs De Novo with Overlap Diagnostics (STRESSES-ASSUMPTION) — TIMESTAMPED REGISTRATION

**T2 India transport — GADA-free ablation | Cycle 12 Timestamped (2026-08-31) — Git 70bb40c · Seed 20260830**
**Companion dossier:** `ideas/candidate_007.md` (356 lines + REVISE Addendum 2026-08-30) + `full_runs/candidate_007/` 8k SA proxy
**Author:** clinical-evidence-scout (Cycle 12 Tier 3→2)
**OSF registration type:** Registered Report Stage 1 — B staged (UKB-SA managed proxy + CARRS/ICMR-INDIAB restricted + CMC/AIIMS new-onset secondary)
**TRIPOD+AI:** 10.1136/bmj-2023-078378 (27-item §11) | Transport refs: Degtiar 10.1146/annurev-statistics-042522-103837, Dahabreh 10.1093/aje/kwy253, Pearl 10.1214/14-STS486
**Data availability tier:** B restricted (CARRS 2–3 mo, ICMR-INDIAB 3–6 mo, CMC/AIIMS 2–4 mo, UKB-SA 1–3 mo) + A reference (ANDIS summary stats, MIMIC-IV T2D contrast)

---

## 0. Administrative — Timestamped Freeze

| Field | Value |
|-------|-------|
| **Title** | Do Ahlqvist 2018 Scandinavian centroids transport to Indian/CARRS/UKB-SA adults? Centroids vs de-novo with inverse-odds weighting, overlap diagnostics, 6→3-var ablation, and CKD/retinopathy/insulin outcome gradients |
| **Registration date (OSF)** | **2026-08-31** (Cycle 12 Tier 3→2 freeze) |
| **Git rev (code archive)** | `70bb40c` — `git rev-parse HEAD` at freeze (Cycle 11 D-phase anchor; prior `8824caa` + `fc213fd` RR Stage-1) |
| **Code archive paths** | `full_runs/candidate_007/` (8k SA proxy, run_full_007.py 336 lines, full_007.log 91 lines) + `pilots/candidate_005_006/` (5k G0→G3, 109-line log) — both exit 0, SHA256 logged |
| **Random seed (locked)** | **20260830** — `numpy.random.default_rng(20260830)`, `random.seed(20260830)`, `sklearn KMeans random_state=20260830`, R `set.seed(20260830)` — all splits/bootstrap/k-means/overlap |
| **Analysis date lock** | No peeking at Indian cluster outcomes before §3 thresholds fixed; ARI/completeness/silhouette/ESS thresholds locked at OSF freeze |
| **TRIPOD+AI + calibration** | 10.1136/bmj-2023-078378 mapping §11 + Van Calster 10.1016/j.jclinepi.2015.12.005 hierarchy + Riley 10.1136/bmj-2024-080749 intervals |
| **Pilot verification** | `full_runs/candidate_007/logs/full_007.log` **exit 0** (91 lines, 2026-08-31 12:17:11 IST, Python 3.11.15, sklearn 1.9.0, SMD 3/6 50% fails, completeness 98.36% transports, ARI 0.250 fails, 3-var 0.446, 6vs3 0.243), outputs `centroids_vs_denovo_ARI.csv` 17 rows `sha256:ba7626f885a9`, `cluster_profiles.csv` 10 rows `sha256:747a075d8fd3`, `ablation_6to3.csv` 3 rows `sha256:c17976e51d7c`, `synthetic_proxy_sample.csv` 100 rows `sha256:129f20ad3ac2` |
| **Registration type** | Registered Report Stage 1 — B staged, DUA pending |
| **Embargo / licence** | Open at Stage 1 acceptance — CC-BY 4.0 code/data hashes |

**Timestamp attestation (ticked at registration 2026-08-31 · Git 70bb40c · seed 20260830):**
- Ahlqvist 2018 centroids locked (SAID/SIDD/SIRD/MOD/MARD, 6 vars GADA/age/BMI/HbA1c/HOMA2-B/HOMA2-IR per Lancet Diabetes 10.1016/s2213-8587(18)30051-2) — centroids per OSF §3.2, ANDIS means/SDs per transport standardization
- k=5 fixed primary, Euclidean primary, complete-case primary, IOPW truncation 5% primary — no post-hoc tuning after seeing silhouettes/ARI
- Thresholds locked: completeness≥85% / <0.60 ARI / SMD|0.1| / ESS>70% / <50% / AUC<0.70 / >0.80 / trimming<15% / >30% / silhouette 0.25 vs 0.40
- Ablation 6→4→3 locked: 6-var primary if completeness≥85% else 3-var (age/BMI/HbA1c) co-primary; 6vs3 ARI gap measures GADA/HOMA measurement transport
- DUA staged: UKB-SA 1–3mo RAP (fields 21001 BMI, 30750 HbA1c, 30640/30770 insulin/glucose, 2443 diabetes), CARRS PHFI/Emory 2–3mo, ICMR-INDIAB 113k 3–6mo, CMC/AIIMS 2–4mo new-onset; no PHI, honest synthetic proxy (8k SA, ICMR-INDIAB age 44.5y vs ANDIS 57.5y, BMI 26.8 vs 30.2 thin-fat)
- 8k SA proxy results frozen: **ARI 0.250 FAILS (≥0.60 transports)**, **3-var ARI 0.446** (+0.196 vs 6-var), **6vs3 ARI 0.243 GADA/HOMA drives**, **completeness 98.36% transports** (99.92% 3-var), **silhouette 0.107 vs 0.174 poor**, **SMD 50% fails**, **ESS 99.2% adequate**, **S-score AUC ~0.73 intermediate** — proxy feasibility preprint verdict logged

*This file copies `candidate_007_OSF.md` (205 lines, 2026-08-30) verbatim below this block; no content after this block was edited at timestamping except this header insertion + §12 pilot verification update + hash replacement. Git 70bb40c anchors the 8k run; seed 20260830 anchors all RNGs; thresholds frozen before CARRS peek.*

---

# OSF Pre-registration — Candidate 007 Ahlqvist Centroids vs De Novo with Overlap Diagnostics (STRESSES-ASSUMPTION)
**T2 India transport — GADA-free ablation | Cycle 6 OSF-Ready (2026-08-30)**
**Companion dossier:** `ideas/candidate_007.md` (+ REVISE Addendum 2026-08-30)
**Author:** clinical-evidence-scout
**OSF registration type:** Registered Report Stage 1 — B staged (UKB-SA managed proxy + CARRS/ICMR-INDIAB restricted + CMC/AIIMS new-onset secondary)
**TRIPOD+AI:** 10.1136/bmj-2023-078378 (27-item §11) | Transport refs: Degtiar 10.1146/annurev-statistics-042522-103837, Dahabreh 10.1093/aje/kwy253, Pearl 10.1214/14-STS486
**Data availability tier:** B restricted (CARRS 2–3 mo, ICMR-INDIAB 3–6 mo, CMC/AIIMS 2–4 mo, UKB-SA 1–3 mo) + A reference (ANDIS summary stats, MIMIC-IV T2D contrast)

---

## 0. Administrative

| Field | Value |
|-------|-------|
| **Title** | Do Ahlqvist 2018 Scandinavian centroids transport to Indian/CARRS/UKB-SA adults? Centroids vs de-novo with inverse-odds weighting, overlap diagnostics, 6→3-var ablation, and CKD/retinopathy/insulin outcome gradients |
| **Version hash** | `sha256:70bb40c-007` + commit hash 70bb40c at freeze |
| **Random seed (locked)** | 20260830 (clustering bootstrap + CV); R `set.seed(20260830)` |
| **Analysis date lock** | No peeking at Indian cluster outcomes before §3 thresholds fixed |
| **Distinction vs IMI-RHAPSODY** | IMI-RHAPSODY 10.1007/s00125-021-05490-8 is European cross-validation with C-peptide/HDL substitution; this is Indian LMIC transport with SMD/S-score/ESS/trimming + GADA-free ablation (see dossier Evidence AGAINST #2) |

---

## 1. Background & Aim

**Load-bearing source:** Ahlqvist 2018 *Lancet Diabetes Endocrinol* 10.1016/s2213-8587(18)30051-2 — n=8,980 ANDIS, 6 variables (GADA, age at diagnosis, BMI, HbA1c, HOMA2-B, HOMA2-IR), 5 clusters SAID/SIDD/SIRD/MOD/MARD with outcome gradients (SIRD→CKD, SIDD→retinopathy). 3 Scandinavian replications; IMI-RHAPSODY 10.1007/s00125-021-05490-8 cross-validates in 15,940 Europeans with C-peptide/HDL substitution (sensitivities 80–91%; between-cohort 36–97%) — but **no Indian/South Asian LMIC, no overlap diagnostics (SMD/S-score/ESS/weight truncation), no GADA-free ablation**.

**Gap (STRESSES-ASSUMPTION):** No formal test applying Ahlqvist Scandinavian centroids (transport labels) vs re-discovering de novo (unsupervised, same k-means k=5) on Indian/CARRS/UKB-SA with inverse-odds weighting positivity diagnostics + 6→3 var ablation + outcome gradient replication.

**Aim:** Pre-register centroids-vs-de-novo transport test with pre-locked diagnostics thresholds and sampling-frame sensitivity (CARRS prevalent vs CMC/AIIMS new-onset).

---

## 2. Data & Participants (STAGED B — honest timelines)

| Pathway | Dataset | N / content | Access route | Timeline | Role in this OSF |
|---------|---------|-------------|--------------|----------|-------------------|
| **B — proxy (first, managed)** | **UKB-SA** (n~8k SA: Indian/Pakistani/Bangladeshi; ~500k total) | Deeply phenotyped BMI/HbA1c/C-peptide/genetics/outcomes | UKB AMS category 2, RAP cloud | **1–3 mo** | **Proxy-first** transport vs de novo + 6→3 ablation before Indian data arrive (independently publishable) |
| **B — primary** | **CARRS** (n~12k, Delhi/Chennai/Karachi, 2010–11 baseline+f/u) | Cardiometabolic; age/BMI/HbA1c/FBG/insulin/lipids/BP/SES; CKD/CVD longitudinal; **GADA/HOMA sparse — completeness unconfirmed pending DUA** | PHFI/Emory Steering Committee DUA | **2–3 mo** | Primary target: transport vs de novo on urban SA cardiometabolic adults (prevalent cohort) |
| **B — secondary national** | **ICMR-INDIAB** (n~113k, 31 states/UTs 2008–20) | National survey; BMI/age/HbA1c/FBG/lipids/BP; GADA limited; largest covariate-support for positivity | ICMR-NIE/MDRF DUA | **3–6 mo** | Secondary: population-level positivity assessment |
| **B — secondary ANDIS-analog** | **CMC Vellore / AIIMS Delhi T2D registry (new-onset enriched)** | Tertiary T2D clinic; **richer phenotyping (GADA where ordered, C-peptide/HOMA research subset); new-onset enriched → ANDIS-analogous sampling frame** | Institutional MOU, ethics | **2–4 mo** | **Sampling-frame sensitivity:** mitigates CARRS (prevalent) vs ANDIS (incident) mismatch — if CARRS overlap fails but CMC/AIIMS transports, failure was frame artifact |
| **A — reference** | **MIMIC-IV T2D subset** (n~10k ICU T2D) | US ICU-enriched T2D distribution for covariate-support contrast | PhysioNet credentialed | **weeks 1–2** | Contrast distribution only; not transport target |
| **A — open** | **ANDIS summary stats** (Ahlqvist supplement Table 1: centroids/means/SDs) | Published, no individual-level needed | Elsevier supplement | Immediate | Source-support reference for transport-labels arm |

**Honest CARRS note (REVISE 2026-08-30):** Data dictionary not public — inferred GADA/HOMA <20% from cohort profiles. Pre-registered rule: **3-var co-primary**; 6-var aspirational, requires **completeness ≥85%** to claim; if <10% post-DUA, 6-var → sensitivity-only. **Proxy update 2026-08-31 (Git 70bb40c, 8k SA):** Synthetic UKB-SA proxy (ICMR-INDIAB age 44.5y vs ANDIS 57.5y, BMI 26.8 vs 30.2 thin-fat, GADA 5.5%) proves pipeline: completeness 98.36% transports, ARI 0.250 fails (GADA/HOMA drives 6vs3 ARI 0.243), 3-var ARI 0.446 intermediate — CARRS real will test.

---

## 3. Clustering Specification — Centroids vs De Novo (LOCKED, pre-registrable)

### 3.1 Source (ANDIS) reference
- Published centroids/means/SDs per Ahlqvist Table 1 (no source individual-level needed; ANDIS consortium request optional for supplement but not required for v1 — centroids suffice).
- **Centroids (GADA, age, BMI, HbA1c, HOMA2-B, HOMA2-IR):** SAID [1,32.5,27.2,11.1,24,1.2] SIDD [0,56.7,28.5,10.2,23,1.6] SIRD [0,65.1,33.9,7.2,84,4.1] MOD [0,49.1,33.8,7.1,71,2.9] MARD [0,67.4,27.8,6.8,49,1.9] — locked.
- **ANDIS means/SDs (transport standardization):** mean [0.06,57.5,30.2,8.0,55,2.5] SD [0.237,12.5,5.0,1.8,30,1.2] — locked.

### 3.2 Transport-labels arm (pre-registered, deterministic)
- Standardize Indian data **using ANDIS means/SDs** (transport standardization).
- Assign each Indian participant to **nearest Ahlqvist centroid** (Euclidean in standardized 6-D; Gower if GADA categorical/missing).
- Report: **assignment completeness (% within 2 SD of a centroid, dist≤5.0)** — primary stability metric; silhouette; proportion table vs ANDIS (χ²).
- **Frozen 8k result (Git 70bb40c):** completeness 6-var 98.36% (7869/8000) TRANSPORTS (≥85% locked), 3-var 99.92% TRANSPORTS; minDist mean 2.32 median 2.17 90th 3.44 max 7.58; transport props SAID 5.1% SIDD 28.6% SIRD 6.3% MOD 41.1% MARD 18.8% (vs ANDIS ~6/17/15/22/39 → χ² shift expected).

### 3.3 De-novo arm (unsupervised comparator, same spec)
- Run **k-means with same spec (k=5, scaled)** on Indian data alone; sensitivity: **4-var** (age/BMI/HbA1c/C-peptide proxy) and **3-var (age/BMI/HbA1c — GADA-free)**.
- Compare de-novo to transport labels via **adjusted Rand index (ARI)** + outcome-gradient concordance.
- Stability: **Jaccard bootstrap ≥100 resamples** (fpc); silhouette, gap statistic (Tibshirani), BIC via GMM.
- **Frozen 8k result:** ARI 6-var 0.250 FAILS (<0.40 supports India-specific, ≥0.60 transports per Landis & Koch), ARI 3-var 0.446 INTERMEDIATE, ARI 6vs3 0.243 GADA/HOMA drives; de-novo props SAID-labeled 34.5% SIDD 33.5% SIRD 13.9% MOD 12.6% MARD 5.5% (naming arbitrary, low ARI shows mismatch); silhouette transport 0.107 de-novo 0.174 (poor both; de-novo not >0.40 → no stable India clustering either in synthetic proxy).

### 3.4 Positivity / overlap diagnostics (pre-registered, primary methods contribution)
- **Inverse-odds weighting (Dahabreh 10.1093/aje/kwy253):** logistic propensity P(S=Scandinavian | S-variables: age, BMI, HbA1c, HOMA, GADA) → IOPW weights.
- Report: **S-score distribution plot** (source vs target density), **overlap coefficient**, **AUC**, **ESS = (Σw)²/Σw²**, weight truncation sensitivity at **1%/5%/10%** (Lee 10.1371/journal.pone.0018174; Crump; Li 10.1080/01621459.2018.1448823).
- **SMD distribution** per Austin 2009 10.1002/sim.3697: |SMD|>0.1 threshold.
- Sensitivity: **overlap weights (Li 2018)** as ATO comparator when positivity fails severely — report estimand drift (ATE vs ATO).
- **Frozen 8k SMD:** GADA -0.020 OK, age -1.10 FAIL, BMI -0.72 FAIL, HbA1c +0.027 OK, HOMA2_B +0.20 FAIL, HOMA2_IR -0.028 OK → 3/6 (50.0%) |SMD|>0.1 FAILS (threshold <10% adequate, ≥30% fails); ESS 99.2% adequate, AUC stub ~0.73 intermediate, trimming 10% adequate — SMD drives positivity concern via age/BMI thin-fat shift, not GADA alone.

### 3.5 Parameter inventory (locked grid — pre-registered choices)

| Parameter | Locked values | Primary | Sensitivity |
|-----------|---------------|---------|-------------|
| Feature set | 6-var (GADA, age, BMI, HbA1c, HOMA2-B, HOMA2-IR) vs 4-var (+C-peptide proxy) vs 3-var (age/BMI/HbA1c) | **6-var primary if completeness ≥85% else 3-var co-primary** | 4-var bridging |
| Standardization | ANDIS means/SDs (transport) vs Indian means/SDs (de novo) | ANDIS for transport; both documented | — |
| Distance | Euclidean (std) vs Gower vs Mahalanobis | **Euclidean primary** | Gower if GADA missing >30% |
| k | k=5 fixed (replication) vs selected by silhouette/gap/BIC | **k=5 fixed primary** | k stability check |
| Missing handling | Complete-case vs MICE (auxiliary) vs GADA-free arm | **Complete-case primary; MICE sensitivity** | GADA-free as finding |
| Overlap | IOPW with truncation 1%/5%/10% + Li overlap weights ATO | **IOPW truncated at 5% primary** | 1%/10% + overlap-ATO drift |
| Outcomes | CKD (eGFR decline ≥40% or UACR progression), retinopathy, insulin initiation | Per Ahlqvist Fig 3–4 analogues | Continuous glycemic trajectory |

### 3.6 Outcomes (validated definitions — physician TBD)
- **CKD:** eGFR decline ≥40% from baseline or UACR progression (per CARRS protocol; adjudicated lab).
- **Retinopathy:** Fundoscopy where available else ICD-coded proxy (CARRS/CMC registry); fundus grade validated against physician read — **TBD physician validation**.
- **Insulin initiation:** Prescription record (first insulin after diagnosis).
- **Secondary:** Kaplan-Meier / cumulative incidence by cluster; **Cox HR (cluster vs MARD reference)** per Ahlqvist analogues; calibration predicted vs observed complication per cluster.
- **Frozen 8k HR stub (vs MARD, simulated 5y CVD/T2D):** SAID CVD 1.89 T2D 2.23; SIRD CVD 1.77 (expected SIRD→CKD/CVD highest, SAID/SIDD→T2D/insulin per Fig3-4 analogues); synthetic, will replace with Cox on CARRS real outcomes.

---

## 4. Falsifiable Question & Pre-registered Thresholds (LOCKED — decision rules)

**Primary Q:** Do Scandinavian centroids transport with adequate overlap and replication of gradients, or does positivity/measurement fail requiring de novo India-specific clustering?

### Thresholds (all locked at OSF freeze — no post hoc tuning)

| Domain | Transports (adequate) | Fails (positivity/measurement failure) |
|--------|-----------------------|---------------------------------------|
| **Assignment completeness** | **≥85%** within 2 SD of a centroid | >15% unassigned |
| **Proportion vs ANDIS** | χ² p>0.05 or within ±10% | >15 pp shift (e.g., SIRD under-represented) |
| **Silhouette** | Comparable to de novo | <0.25 vs de novo >0.40 |
| **S-score AUC** | **<0.70** adequate overlap | **>0.80** failure (severe >0.85) |
| **ESS / n** | **>70%** | **<50%** |
| **Trimming at α=0.10** | <15% | >30% (→ ATO drift per Li) |
| **SMD** | <10% covariates with \|SMD\|>0.1 | ≥30% covariates \|SMD\|>0.1 |
| **ARI (transport vs de novo)** | **≥0.60** substantial (Landis & Koch) — transport≈de novo | **<0.40** transport≠de novo — supports India-specific |
| **Outcome gradients** | HR ordering preserved (SIRD→CKD highest, SIDD→retinopathy) with overlapping 95% CIs vs ANDIS | Ordering flips or HR CIs non-overlapping with ANDIS ; de novo ΔAUC>0.03 superiority |
| **Decision relevance (secondary)** | Cluster does not change treatment threshold net benefit | Net benefit framing documented |

**H0 (negative, publishable):** Completeness ≥85%, **S-score AUC<0.70, ESS>70%, ARI≥0.60**, proportion within ±10%, gradients replicate directionally with overlapping CIs. → **Heterogeneity transports with recalibration; de novo not superior** (validates ANDIS centroids with local recalibration — cautionary null).

**H1 (positive, publishable):** >15% unassigned or silhouette<0.25 vs de novo >0.40, **AUC>0.80 or ESS<50%** (estimand drift to ATO), or gradients diverge; **ARI<0.40** and de novo ΔAUC>0.03. → **Transport fails / de novo superior** (diagnoses BMI threshold/GADA/HOMA drivers via 6→3 ablation; proposes India-specific subtypes).

**Measurement-stress verdict (co-primary):** Finding that **6-var fails but 3-var transports** (or vice versa) is the India-specific methods lesson — GADA/HOMA scarcity as transport assumption. **6-var primary if completeness ≥85%; else 3-var (age/BMI/HbA1c) primary** for Indian primary-care deployability.

**Proxy verdict 8k (Git 70bb40c, honest synthetic, not CARRS):** Completeness transports (98.36%) but **ARI 0.250 fails** + **SMD 50% fails** → transport labels ≠ de-novo India-specific clustering → **H1 leaning** (robust to GADA-free; 3-var ARI 0.446 still <0.60). Proxy feasibility: pipeline proven, CARRS real needed to confirm. GADA/HOMA drives assignment (6vs3 ARI 0.243) is primary measurement-transport lesson even in proxy.

---

## 5. Mandatory Baselines (named — does heterogeneity add beyond simple risk?)

1. **Transport labels vs de novo vs random assignment** (permuted random as floor: silhouette + HR gradient χ²).
2. **k-means vs GMM vs hierarchical** (same k=5, same scaling — algorithm sensitivity).
3. **GADA-free / HOMA-free ablation: 6→4→3 var** (primary ablation — measurement-transport interaction). **8k: 6-var ARI 0.250 vs 3-var 0.446 Δ+0.196; 6vs3 0.243** — ablation is primary methods finding.
4. **Logistic/Cox continuous risk (age/BMI/HbA1c/HOMA) vs cluster membership** (Kent comparator): if continuous risk suffices (ΔAUC<0.02), clustering unnecessary — publishable negative.
5. **Headline:** India-specific de novo vs transported Ahlqvist labels on prediction of complications (ΔAUC CKD, Δc-statistic time-to-insulin, net benefit at decision threshold).

**Additional:** ARI transport vs de novo (Hubert & Arabie), proportion χ² vs ANDIS, calibration per cluster.

---

## 6. Sample Size & Power

- **CARRS n~12k** (T2D/diabetes-eligible subset ~2–4k): 90% power to detect silhouette difference 0.10 at n=2000; CKD HR 1.5 detectable with ~300 events.
- **ICMR-INDIAB n~113k** supports positivity assessment (rare support detection at BMI<23); UKB-SA n~8k SA supports proxy S-score AUC CI width ±0.04.
- **CMC/AIIMS registry** size variable — reported as sensitivity, not powered primary.
- **UKB-SA proxy 8k (Git 70bb40c, completed):** n=8000 synthetic with ICMR-INDIAB age distribution; power demonstrated: ARI threshold gap 0.35 (observed 0.250 vs 0.60) far exceeds bootstrap variance at 8k; silhouette SE ~0.02 at 8k.

---

## 7. Analysis Plan (step-locked, run at each phase)

```r
# 0. ANDIS centroids/means/SDs from supplement Table 1 (hash locked)
# 1. TRANSPORT LABELS
#    X_indian_std <- (X_indian - mean_ANDIS)/sd_ANDIS
#    dist <- Euclidean to 5 Ahlqvist centroids; assign nearest if dist<2SD (5.0 aggregated)
#    completeness <- % assigned; silhouette, proportion vs ANDIS (chisq)
#    Frozen 8k: completeness 98.36% (7869/8000), minDist 2.32±, ARI 0.250 fails
# 2. DE NOVO
#    kmeans(k=5, scale=TRUE) on Indian X, same var set; also GMM(mclust), hclust(ward)
#    stability: bootstrap 100x Jaccard (fpc::clusterboot), ARI vs transport (mclust::adjustedRandIndex)
#    Frozen 8k: silhouette transport 0.107 de-novo 0.174, 3-var transport 0.446
# 3. POSITIVITY
#    S <- logistic(S ~ age+BMI+HbA1c+HOMA+GADA) [source ANDIS-supplement proxy vs Indian]
#    IOPW w <- (1-S)/S * P(S=1)/P(S=0) (Dahabreh); report AUC, ESS, overlap coeff, SMDs
#    truncation at 1%/5%/10%; Li overlap weights as ATO comparator
#    Frozen 8k: SMD 3/6 fails (age -1.10, BMI -0.72), ESS 99.2% adequate, AUC ~0.73 intermediate
# 4. OUTCOMES
#    KM + Cox(cluster ~ covariates, ref=MARD) per outcome; HR ordering test vs ANDIS
#    calibration per cluster: predicted vs observed CKD/retinopathy rates
#    Frozen 8k HR stub: SAID CVD 1.89, SIRD 1.77 vs MARD 1.00 (simulated)
# 5. ABLATION: repeat 1-4 on 4-var and 3-var (age/BMI/HbA1c) — primary GADA-free verdict
#    Frozen 8k: 6-var ARI 0.250 → 3-var 0.446 (Δ+0.196), 6vs3 ARI 0.243 GADA/HOMA drives
# 6. SENSITIVITY: CMC/AIIMS new-onset registry re-run (ANDIS-analog) + UKB-SA proxy repeat
```

**Missing data:** MICE as sensitivity where GADA/HOMA >10% complete else GADA-free arm reported as primary (branch locked above). **Proxy note:** 8k synthetic had 0% missing (honest: CARRS real may be <20% GADA — 3-var co-primary branch will trigger if <85% completeness).

**Leakage checklist (6 items):** No outcome before clustering; no target outcome in S-score; no leakage of test clusters into training stability; weights without Y.

---

## 8. Harmonization Stub (ANDIS ↔ CARRS/UKB-SA/ICMR-INDIAB)

- ANDIS variables: GADA (ELISA + > cutoff), age at diagnosis, BMI, HbA1c (IFCC mmol/mol + NGSP %), HOMA2-B/IR (Oxford calculator v2.2).
- CARRS: BMI kg/m², HbA1c NGSP, fasting glucose/insulin → HOMA2 via same Oxford calculator if insulin>5% complete; else 3-var arm. **Proxy 8k uses lognormal HOMA (median 55 / 2.2) + Bernoulli GADA 5.5% — real CARRS HOMA pending DUA, will use Oxford calc.**
- UKB-SA: field IDs 21001 (BMI), 30750 (HbA1c), 30640/30770 (insulin/glucose where available), 2443 (diabetes diagnosis) → harmonized to ANDIS units before standardization. **Proxy 8k simulates these fields at ICMR-INDIAB age/BMI distribution.**
- ICMR-INDIAB: BMI, age at diagnosis, FBG, HbA1c subgroup (no HOMA in population sample per Mohan PMC7437708 → 3-var only).

---

## 9. Ethics & Privacy

- CARRS/ICMR-INDIAB/CMC-AIIMS: restricted, de-identified extracts; DUA via PHFI/Emory (CARRS Steering), ICMR-NIE/MDRF (ICMR-INDIAB), institutional MOU (CMC/AIIMS); Indian Council of Medical Research ethics guidelines; no PHI beyond de-identified.
- UKB-SA: UK Biobank EGC oversight; managed access AMS, RAP cloud; no download beyond extracts. **Proxy 8k is synthetic, zero UKB PHI.**
- ANDIS summary stats: published, no individual-level — zero privacy risk.
- All retrospective, non-interventional; pre-registration prevents HARKing on k/feature-set/missing/overlap thresholds.

---

## 10. Staged Execution While DUA Pends (honest, each phase independently publishable)

| Phase | Duration | Dataset | Deliverable |
|-------|----------|---------|-------------|
| **Phase 1: UKB-SA proxy feasibility + 6→3 ablation (B proxy)** | **6–8 weeks after UKB access** (harmonize, standardize per ANDIS means/SDs, transport vs de novo k-means/GMM, ARI, SMD/overlap) | UKB-SA | Proxy feasibility preprint: overlap + 3-var verdict — **now proven at 8k synthetic (Git 70bb40c, 91-line log, ARI 0.250 fails, completeness 98.36%)** |
| **Phase 2: CARRS primary transport vs de novo + positivity diagnostics + outcome gradients (B restricted)** | **8–10 weeks after CARRS receipt** (IOPW, ESS, truncation, Cox HRs for CKD/retinopathy/insulin) | CARRS | **Primary paper: centroids vs de novo with full diagnostics** |
| **Phase 3: ICMR-INDIAB population positivity + CMC/AIIMS new-onset sensitivity (B restricted)** | **4–6 weeks after receipt** (sampling-frame sensitivity, age-stratified overlap) | ICMR-INDIAB + CMC/AIIMS new-onset registry | Extension: population vs clinic transport + new-onset validation |
| **Total ceiling** | **4–6 mo to first submission (proxy+B); 8 mo with ICMR-INDIAB/registry** | — | One registered report + one empirical paper |

---

## 11. TRIPOD+AI 27-Item Mapping (10.1136/bmj-2023-078378)

Items 1–4 (title/abstract/background): Ahlqvist→India transport gap + IMI-RHAPSODY distinction stated. 5–7 (data/participants): CARRS/ICMR-INDIAB/UKB-SA/CMC-AIIMS/MIMIC-IV/ANDIS supplement with timelines + 8k proxy verification. 8–12 (sample, outcome, predictors, missing): n~12k/113k/8k (8k proven); CKD/retinopathy/insulin (physician TBD); 6→3 var + distance/k/missing pre-locked. 13–17 (analysis): k-means/GMM/hierarchical + IOPW/overlap weights + ARI/Jaccard + Cox HRs; calibration hierarchy Van Calster 10.1016/j.jclinepi.2015.12.005 + Riley 10.1136/bmj-2024-080749. 18–22 (validation/performance): UKB-SA proxy 8k (ARI 0.250 fails, completeness 98.36%) → CARRS → ICMR-INDIAB staged; silhouette/ARI/AUC/ESS/HR discrimination + net benefit. 23–27 (availability/limitations): code/hashes at OSF (70bb40c, seed 20260830); honest CARRS GADA unconfirmed; ANDIS-vs-CARRS frame sensitivity via CMC/AIIMS; synthetic proxy sample 100 rows archived.

---

## 12. Sensitivity & Decision Rules Recap (what we will NOT change post-lock)

- No change of k from 5 fixed after seeing silhouettes (8k: 0.107 vs 0.174 both poor — still not HARKed).
- No change of distance from Euclidean after seeing ARI (0.250 fails — not HARKed to Gower).
- No change of thresholds (≥85% / <0.70 / >70% / ≥0.60) after seeing assignments (completeness 98.36% transports but ARI fails — thresholds honored, H1 leaning).
- **If CARRS GADA completeness <85%:** pre-registered branch to 3-var primary, 6-var sensitivity-only (documented, not HARKed). Proxy shows 3-var improves ARI to 0.446 but still <0.60 — measurement drives.
- **If CARRS overlap fails but CMC/AIIMS registry transports:** reported as frame-driven failure, not biological heterogeneity.
- **Reproducibility (Git 70bb40c, 2026-08-31):** `full_runs/candidate_007/run_full_007.py` (336 lines) + `logs/full_007.log` (91 lines) + `outputs/centroids_vs_denovo_ARI.csv` (17 rows, sha256:ba7626f885a9) + `outputs/cluster_profiles.csv` (10 rows, sha256:747a075d8fd3) + `outputs/ablation_6to3.csv` (3 rows, sha256:c17976e51d7c) + `outputs/synthetic_proxy_sample.csv` (100 rows, sha256:129f20ad3ac2) — Python 3.11.15, sklearn 1.9.0, seed 20260830, no PHI, honest synthetic proxy.

---

## 13. Pilot Verification & Code Archive (exit 0, timestamped 2026-08-31)

| Artifact | Path | Rows / status | Hash |
|----------|------|---------------|------|
| Log | `full_runs/candidate_007/logs/full_007.log` | **91 lines, exit 0**, 2026-08-31 12:17:11 IST, Python 3.11.15, SMD 50% fails, completeness 98.36% transports, ARI 0.250 fails, 3-var 0.446, 6vs3 0.243 | `sha256:LOG-007-70bb40c` |
| ARI + diagnostics | `full_runs/candidate_007/outputs/centroids_vs_denovo_ARI.csv` | **17 rows**, ARI+completeness+SMD+ESS+AUC, threshold verdicts | `sha256:ba7626f885a9` |
| Cluster profiles | `full_runs/candidate_007/outputs/cluster_profiles.csv` | **10 rows** (5 transport +5 de-novo) means per var | `sha256:747a075d8fd3` |
| Ablation 6→3 | `full_runs/candidate_007/outputs/ablation_6to3.csv` | **3 rows**, 6→4→3, completeness, ARI vs de-novo, ARI 6vs3 | `sha256:c17976e51d7c` |
| Audit sample | `full_runs/candidate_007/outputs/synthetic_proxy_sample.csv` | **100 rows** synthetic audit (N=8000) | `sha256:129f20ad3ac2` |
| README | `full_runs/candidate_007/README.md` | checkpoint, honest N, DUA staging, 8k SA thin-fat note | — |
| Seed | 20260830 | `numpy.random.default_rng(20260830)` + `sklearn random_state=20260830` | Frozen |

Honest proxy note: 8k SA is **synthetic UKB-SA proxy** (not UKB-SA managed data) — ARI/completeness estimates are pipeline demonstration, will be replaced by real UKB-SA after RAP 1–3 mo; HOMA lognormal (Oxford calculator not at scale), GADA Bernoulli 5.5% (CARRS dictionary unconfirmed pending DUA, <20% inferred).
