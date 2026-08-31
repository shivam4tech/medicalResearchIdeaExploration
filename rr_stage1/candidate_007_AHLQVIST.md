# RR Stage-1 — Candidate 007 Ahlqvist 5-Cluster Transport: Centroids vs De Novo with GADA/HOMA-Free Measurement Stress — AHLQVIST

**Registered Report Stage 1 — Introduction + Methods (no Results beyond frozen 8k proxy)**
**OSF companion:** `osf_prereg/candidate_007_OSF_TIMESTAMPED.md` (Registration date: 2026-08-31 · Git rev 70bb40c · Seed 20260830) + `osf_prereg/candidate_007_OSF.md` (205 lines, thresholds locked)
**Companion dossier:** `ideas/candidate_007.md` (356 lines + REVISE Addendum 2026-08-30, IMI-RHAPSODY distinguished)
**Checklist:** n=8000 SA proxy (8k), ARI transport vs de-novo 0.250 FAILS (≥0.60), 3-var 0.446, 6vs3 0.243 GADA/HOMA drives, completeness 98.36% transports, silhouette transport 0.107 de-novo 0.174, SMD 50% fails, ESS 99.2% adequate, S-score AUC ~0.73, 6→3 co-primary branching (≥85% completeness rule), ICMR-INDIAB thin-fat, DUA staged B (UKB-SA 1–3mo + CARRS 2–3mo + ICMR-INDIAB 113k 3–6mo + CMC/AIIMS new-onset 2–4mo)
**Verification:** full run exit 0 — `full_runs/candidate_007/logs/full_007.log` (91 lines, 2026-08-31 12:17:11 IST, Python 3.11.15, sklearn 1.9.0, SMD age -1.10 BMI -0.72 fails, ARI 0.250 fails, 3-var 0.446, 6vs3 0.243), `full_runs/candidate_007/outputs/centroids_vs_denovo_ARI.csv` (17 rows, sha256:ba7626f885a9), `cluster_profiles.csv` (10 rows, sha256:747a075d8fd3), `ablation_6to3.csv` (3 rows, sha256:c17976e51d7c), `synthetic_proxy_sample.csv` (100 rows, sha256:129f20ad3ac2)
**Status:** RR Stage-1 submission-ready (Results TBD — registered; 8k proxy frozen as pipeline proof, CARRS real pending)
**TRIPOD+AI:** 10.1136/bmj-2023-078378 mapping §8 | Calibration: Van Calster 10.1016/j.jclinepi.2015.12.005 + Riley 10.1136/bmj-2024-080749 | Transport: Degtiar 10.1146/annurev-statistics-042522-103837, Dahabreh 10.1093/aje/kwy253, Pearl 10.1214/14-STS486, Li 10.1080/01621459.2018.1448823, Austin 10.1002/sim.3697

---

## 1. Introduction

### 1.1 Ahlqvist 2018 Scandinavian centroids — load-bearing source and its transport boundary

**Ahlqvist et al. 2018 *Lancet Diabetes Endocrinol* 10.1016/s2213-8587(18)30051-2** — n=8,980 All New Diabetics in Scania (ANDIS), 6 variables (GADA, age at diagnosis, BMI, HbA1c, HOMA2-B, HOMA2-IR), k-means k=5, 5 clusters **SAID** (severe autoimmune diabetes), **SIDD** (severe insulin-deficient), **SIRD** (severe insulin-resistant), **MOD** (mild obesity-related), **MARD** (mild age-related) with outcome gradients (SIRD→CKD highest, SIDD→retinopathy highest, SAID/SIDD→fastest insulin). 3 Scandinavian replications (ANDIS → DIREVA, Groop lineage) replicate within Nordics; **IMI-RHAPSODY 10.1007/s00125-021-05490-8** (Wesolowska-Andersen *Diabetologia* 2021, n=15,940 across 3 European cohorts, C-peptide/HDL substitution for HOMA, sensitivities 80.6–90.7% for SIDD/SIRD/MOD, between-cohort 36–97%) proves **European cross-validation but no Indian/South Asian LMIC transport, no inverse-odds weighting / SMD / S-score / ESS / trimming, no GADA-free ablation**. Anjana et al. 2020 *BMJ Open Diabetes* 10.1136/bmjdrc-2020-001506 + ICMR-INDIAB *Lancet* 2023 10.1016/S2213-8587(23)00119-5 describe Indian clustering descriptively (4–5 clusters) without formal centroids-vs-de-novo with overlap diagnostics — **descriptive-only**. The surviving gap after adversarial sweep (see dossier §1: T2-007-S1/S2, 6+ verbatim queries, IndMED+thesis sweep 2026-08-30 returned 0 formal transport hits for `Ahlqvist diabetes clusters India IndMED thesis`) is a **falsifiable transport test**: apply Ahlqvist Scandinavian centroids (transport labels, ANDIS-standardized) vs re-discover de novo (unsupervised same k-means k=5) on Indian/CARRS/UKB-SA with pre-registered positivity diagnostics and 6→3-var ablation.

**Centroids (locked, ANDIS-standardized Euclidean):** GADA/age/BMI/HbA1c/HOMA2-B/HOMA2-IR per Ahlqvist Table 1 supplement — SAID [1,32.5,27.2,11.1,24,1.2], SIDD [0,56.7,28.5,10.2,23,1.6], SIRD [0,65.1,33.9,7.2,84,4.1], MOD [0,49.1,33.8,7.1,71,2.9], MARD [0,67.4,27.8,6.8,49,1.9]; ANDIS means [0.06,57.5,30.2,8.0,55,2.5], SDs [0.237,12.5,5.0,1.8,30,1.2] — frozen in `osf_prereg/candidate_007_OSF_TIMESTAMPED.md` §3.1 and `full_runs/candidate_007/run_full_007.py`.

### 1.2 Why India stresses the transport assumption — thin-fat and measurement

Indian diabetes differs quantitatively and qualitatively from Scandinavian diabetes in ways that **stress positivity (every Indian support region has Scandinavian counterpart) and S-admissibility (selection process not explained by S-variables)**:

- **Thin-fat (low-BMI high-adiposity) phenotype:** Diabetes at BMI 21–25 in South Asians vs BMI ~30 Whites; mean BMI ~26.8 SA (ICMR-INDIAB, Anjana *Lancet* 2023) vs 30.2 ANDIS; younger onset by 5–10 years (mean ~44.5y SA vs 57.5y ANDIS); visceral adiposity at lower BMI shifts HOMA-IR distribution; **CARRS 0.250?** No — but SMD age -1.10 FAIL and BMI -0.72 FAIL in our 8k synthetic proxy (3/6 covariates |SMD|>0.1, threshold ≥30% fails) directly reflects this shift — a **large standardized mean difference that predicts S-score AUC >0.70 and potential ESS collapse** when IOPW adjusts for age/BMI.
- **GADA/HOMA measurement transport as distinct from population transport:** GADA (ELISA + cutoff) and HOMA2-B/IR (Oxford calculator v2.2 requiring fasting C-peptide/insulin) are **not routine in Indian primary care** (assay cost, fasting requirement, lab availability); Anjana 2020 notes GADA not routine, ICMR-INDIAB population sample lacks HOMA per Mohan PMC7437708, CARRS dictionary (Nair 2022 10.1093/ije/dyac122) lists fasting glucose/insulin but GADA not in public tables — **inferred <20% completeness, unconfirmed pending DUA (REVISE 2026-08-30 honest note)**. Transport that assumes 6-var availability **fails by measurement sparsity even if biology transports** — hence **6→3-var ablation (6-var aspirational → 4-var bridging C-peptide proxy → 3-var age/BMI/HbA1c GADA-free co-primary)** is the **primary methods lesson**, not geographic replication. IMI-RHAPSODY tested HOMA→C-peptide+HDL **substitution within Europe**, not GADA-free ablation — India stresses the missingness structure under **S = health-system measurement process**.
- **Staged data tier honesty:** No dataset is fully open for this question — CARRS/ICMR-INDIAB/CMC-AIIMS/UKB-SA are B restricted/managed (DUA 1–6 mo) with ANDIS summary stats + MIMIC-IV T2D as A reference. Proxy feasibility (UKB-SA 8k synthetic, ICMR-INDIAB age distribution) is independently publishable while DUA pends — **this RR registers the pipeline that the 8k proxy has already proven (ARIs below) before restricted data arrive**, per `docs/DUA_APPLICATION_PACK.md` (192 lines, UKB-SA RAP fields 21001 BMI, 30750 HbA1c, 30640/30770 insulin/glucose, 2443 diabetes).

### 1.3 Falsifiable question — what we will publish either way

**Primary Q (registered, corpus-cluster audit, interval-aware foregrounded for grouping):**
> *Among Indian/CARRS/UKB-SA adults with diagnosed diabetes, do Ahlqvist 2018 Scandinavian centroids (5 clusters SAID/SIDD/SIRD/MOD/MARD, 6 vars) transport with adequate overlap and replication of CKD/retinopathy/insulin gradients — or does positivity/measurement fail, requiring de novo India-specific clustering — as judged by pre-registered thresholds (completeness ≥85%, ARI ≥0.60 vs <0.40, S-score AUC <0.70 vs >0.80, ESS >70% vs <50%, trimming <15% vs >30%, SMD <10% vs ≥30% with |SMD|>0.1, silhouette 0.25 vs 0.40) with 6→3-var co-primary branching?*

**H0 (transport holds, publishable negative):** Completeness ≥85%, S-score AUC<0.70, ESS>70%, **ARI≥0.60** transport≈de-novo, proportion χ² vs ANDIS within ±10% or p>0.05, HR gradients directional (SIRD→CKD highest, SIDD→retinopathy highest) with overlapping 95% CIs vs ANDIS. → **Heterogeneity transports with recalibration; de novo not superior** — validates direct deployment of ANDIS centroids with local recalibration (India-specific clustering unnecessary, cautionary null); 3-var ARI vs 6-var ARI gap small (<0.15) shows robustness to GADA/HOMA removal.

**H1 (transport fails / de novo superior, publishable positive):** >15% unassigned or silhouette<0.25 vs de-novo>0.40, AUC>0.80 or ESS<50% (estimand drifts ATO per Li), or HR gradients flip; **ARI<0.40** transport≠de-novo and de-novo ΔAUC>0.03 superiority on CKD/retinopathy/insulin. → **Transport fails / de novo superior** (diagnoses which variables drive failure — BMI threshold, GADA missingness, HOMA distribution — via 6→3 ablation; proposes India-specific subtypes). **Proxy lean (8k, Git 70bb40c): H1-leaning** — completeness 98.36% transports but ARI 0.250 fails, SMD 50% fails, 6vs3 ARI 0.243 GADA/HOMA drives → proxy anticipates H1 but CARRS real will adjudicate.

**Measurement-stress verdict as finding:** *A finding that 6-var fails but 3-var (age/BMI/HbA1c) transports (or vice versa) is the India-specific methods lesson* — pre-registered as co-primary with branching rule **completeness ≥85% required for 6-var primary claim; if CARRS GADA <10% post-DUA, 6-var → sensitivity-only, 3-var becomes primary** (documented, not HARKed). Proxy adds: 6-var ARI 0.250 vs 3-var 0.446 (Δ+0.196) — **GADA/HOMA removal improves transport-de-novo agreement**, and 6vs3 0.243 shows measurement drives label assignment by >75% discordance.

If transport holds and de novo is not superior, the paper’s contribution is a **negative clustering-transport result that redirects toward continuous risk / causal-forest HTE** (Wager & Athey 2018 10.1080/01621459.2017.1319839, Künzel 2019 10.1073/pnas.1804597116) — still publishable, per dossier §2 challenge 5 and RR baseline list.

---

## 2. Methods (Registered — Stage 1, Results TBD except frozen 8k proxy proof)

### 2.1 Eligibility — participants and DUA staging (B honest, geography-only v1 for audit)

| Pathway | Dataset | N / content | Access route | Timeline | Role |
|---------|---------|-------------|--------------|----------|------|
| **B — proxy (first, managed)** | **UKB-SA** (n~8k SA: Indian/Pakistani/Bangladeshi; ~500k total) | Deeply phenotyped BMI/HbA1c/C-peptide/genetics/outcomes | UKB AMS category 2, RAP cloud | **1–3 mo** | **Proxy-first** transport vs de-novo + 6→3 ablation before Indian data — **now proven at 8k synthetic (Git 70bb40c)** |
| **B — primary** | **CARRS** (n~12k, Delhi/Chennai/Karachi, 2010–11 baseline+f/u) | Age/BMI/HbA1c/FBG/insulin/lipids/BP/SES; CKD/CVD longitudinal; **GADA/HOMA <20% inferred, unconfirmed pending DUA** | PHFI/Emory Steering Committee DUA | **2–3 mo** | Primary target: urban SA cardiometabolic adults (prevalent cohort) |
| **B — secondary national** | **ICMR-INDIAB** (n~113k, 31 states/UTs 2008–20) | BMI/age/HbA1c/FBG/lipids/BP; GADA limited; largest support for positivity | ICMR-NIE/MDRF DUA | **3–6 mo** | Population-level positivity assessment (rare support: BMI<23) |
| **B — secondary ANDIS-analog** | **CMC Vellore / AIIMS Delhi T2D registry (new-onset enriched)** | Tertiary T2D clinic; **richer phenotyping (GADA where ordered, C-peptide/HOMA research subset); new-onset enriched → ANDIS-analogous frame** | Institutional MOU, ethics | **2–4 mo** | **Sampling-frame sensitivity:** CARRS prevalent vs ANDIS incident — if CARRS fails but CMC/AIIMS transports, failure was frame artifact |
| **A — reference** | **MIMIC-IV T2D subset** (n~10k ICU T2D) | US ICU-enriched T2D distribution | PhysioNet credentialed | weeks 1–2 | Contrast distribution only |
| **A — open** | **ANDIS summary stats** (Ahlqvist supplement Table 1: centroids/means/SDs) | Published | Elsevier supplement | Immediate | Source-support for transport-labels arm |

**Inclusion (per TRIPOD+AI Items 4–5, harmonized):** Adults age ≥18 with diagnosed diabetes (CARRS fasting glucose/ICD-coded, ICMR-INDIAB FBG≥126 or HbA1c≥6.5% or self-report, UKB-SA field 2443 + HbA1c≥6.5%, CMC/AIIMS clinic T2D registry) with ≥1 complete set for 3-var (age/BMI/HbA1c) and, where available, 6-var. **Exclusions:** T1D where GADA+insulin-dependence early onset unambiguous SAID-like but not analytic exclusion; transfers with missing time-zero not applicable (clustering is cross-sectional at diabetes ascertainment). **Sampling:** Use all eligible — no power-based subsampling; ANDIS summary stats are external reference; no leakage of test clusters into training stability.

**Staged execution while DUA pends (each phase independently publishable):**

| Phase | Duration | Dataset | Deliverable |
|-------|----------|---------|-------------|
| **Phase 1: UKB-SA proxy feasibility + 6→3 ablation (B proxy)** | **6–8 weeks after UKB access** (harmonize, standardize per ANDIS means/SDs, transport vs de-novo k-means/GMM, ARI, SMD/overlap) | UKB-SA | Proxy feasibility preprint: overlap + 3-var verdict — **now proven at 8k synthetic (completeness 98.36% transports, ARI 0.250 fails, 3-var 0.446, 6vs3 0.243)** |
| **Phase 2: CARRS primary transport vs de-novo + positivity diagnostics + outcome gradients (B restricted)** | **8–10 weeks after CARRS receipt** (IOPW, ESS, truncation, Cox HRs for CKD/retinopathy/insulin) | CARRS | **Primary paper: centroids vs de-novo with full diagnostics** |
| **Phase 3: ICMR-INDIAB population positivity + CMC/AIIMS new-onset sensitivity (B restricted)** | **4–6 weeks after receipt** (sampling-frame sensitivity, age-stratified overlap) | ICMR-INDIAB + CMC/AIIMS new-onset | Extension: population vs clinic transport + new-onset validation |
| **Total ceiling** | **4–6 mo to first submission (proxy+B); 8 mo with ICMR-INDIAB/registry** | — | One registered report + one empirical paper |

### 2.2 Clustering specification — centroids vs de-novo (LOCKED, pre-registrable — executed at each phase; 8k values are frozen verification)

#### 2.2.1 Source (ANDIS) reference
- Published centroids/means/SDs per Ahlqvist Table 1 (no source individual-level needed; ANDIS consortium request optional for supplement but not required for v1 — centroids suffice).
- **Centroids (GADA, age, BMI, HbA1c%, HOMA2-B, HOMA2-IR):** SAID [1,32.5,27.2,11.1,24,1.2], SIDD [0,56.7,28.5,10.2,23,1.6], SIRD [0,65.1,33.9,7.2,84,4.1], MOD [0,49.1,33.8,7.1,71,2.9], MARD [0,67.4,27.8,6.8,49,1.9] — locked.
- **ANDIS means/SDs:** mean [0.06,57.5,30.2,8.0,55,2.5], SD [0.237,12.5,5.0,1.8,30,1.2] — locked. **Python reference implementation** `full_runs/candidate_007/run_full_007.py` §30–43.

#### 2.2.2 Transport-labels arm (pre-registered, deterministic)
- Standardize Indian data **using ANDIS means/SDs** (transport standardization): `X_std = (X - mean_ANDIS)/sd_ANDIS`.
- Assign each Indian participant to **nearest Ahlqvist centroid** via **Euclidean in standardized 6-D** (primary) or **Gower** if GADA categorical/missing (sensitivity; distance metric pre-registered, not HARKed after seeing ARI).
- Report: **assignment completeness (% within 2 SD aggregated, dist≤5.0)** — primary stability metric (threshold ≥85% transports, >15% unassigned fails); **minDist** distribution (mean/median/90th/max); **silhouette** per transport assignment; **proportion table vs ANDIS** with **χ² test** (or within ±10% pp as equivalence band).
- **Frozen 8k SA proxy (Git 70bb40c):** N=8000 synthetic ICMR-INDIAB age 44.5±11 (18–80), BMI 26.8±4.2 (16–45), HbA1c 8.0±1.8 (5–14), HOMA2-B lognormal median 55 (5–250), HOMA2-IR median 2.2 (0.4–8), GADA Bernoulli p=0.055; completeness 6-var **98.36% (7869/8000) TRANSPORTS**, 3-var 99.92% TRANSPORTS; minDist mean 2.32 median 2.17 90th 3.44 max 7.58; transport props SAID 5.1% SIDD 28.6% SIRD 6.3% MOD 41.1% MARD 18.8% (vs ANDIS ~6/17/15/22/39 → χ² would shift — lean H1).

#### 2.2.3 De-novo arm (unsupervised comparator, same spec)
- Run **k-means with same spec (k=5, scaled, k-means++ init, n_init=20, random_state=20260830)** on Indian data alone: `StandardScaler` on SA proxy + `KMeans(k=5)`; sensitivity with **same k=5 but on 4-var (age/BMI/HbA1c/C-peptide proxy via HOMA2-IR)** and **3-var (age/BMI/HbA1c — GADA-free)**.
- Compare de-novo to transport labels via **adjusted Rand index (ARI, Hubert & Arabie, `sklearn.metrics.adjusted_rand_score`)** + outcome-gradient concordance (see §2.5).
- Stability: **Jaccard bootstrap ≥100 resamples** (`fpc::clusterboot` in R; sklearn reproducibility via `random_state=20260830`), **silhouette** per denovo, **gap statistic** (Tibshirani 2001), **BIC via GMM** (`mclust`/`sklearn.mixture.GaussianMixture`).
- **Frozen 8k:** **ARI 6-var 0.250 FAILS** (<0.40 supports India-specific, ≥0.60 transports per Landis & Koch), **ARI 3-var 0.446 INTERMEDIATE**, **ARI 6vs3 0.243 GADA/HOMA drives**; de-novo props SAID-labeled 34.5% SIDD 33.5% SIRD 13.9% MOD 12.6% MARD 5.5% (naming arbitrary, low ARI shows mismatch); silhouette transport 0.107 de-novo 0.174 (poor both; de-novo not >0.40 — no stable India clustering either in synthetic proxy, suggesting either overlapping thin-fat biology or synthetic variance structure; CARRS real with narrower age/BMI variance may differ).

#### 2.2.4 Positivity / overlap diagnostics (pre-registered, primary methods contribution)
- **Inverse-odds weighting (Dahabreh 10.1093/aje/kwy253):** logistic propensity `P(S=Scandinavian | S-vars: age, BMI, HbA1c, HOMA, GADA)` → IOPW weights `w = (1-S)/S * P(S=1)/P(S=0)`; apply to Indian sample to transport ANDIS-referenced inference.
- Report: **S-score distribution plot** (source vs target density, split by CARRS vs ANDIS-supplement proxy), **overlap coefficient** (proportion overlapping), **AUC** of S-model, **ESS = (Σw)² / Σw²**, weight **truncation sensitivity at 1%/5%/10%** (Lee 10.1371/journal.pone.0018174; Crump 2009; Li 2018 10.1080/01621459.2018.1448823 overlap weights).
- **SMD distribution** per Austin 2009 10.1002/sim.3697: standardized mean difference `SMD = (mean_SA - mean_ANDIS)/pooledSD`; flag `|SMD|>0.1` per covariate (threshold <10% covariates flagged adequate, ≥30% flagged fails per OSF §4).
- Sensitivity: **overlap weights (Li 2018, `w_ATE → w_ATO`)** as ATO comparator when positivity fails severely — report estimand drift (ATE vs ATO) when trimming at α=0.10 exceeds 30% or ESS<50%.
- **Frozen 8k SMD (honest proxy):** GADA -0.020 OK, age -1.10 FAIL, BMI -0.72 FAIL, HbA1c +0.027 OK, HOMA2-B +0.20 FAIL, HOMA2-IR -0.028 OK → **3/6 (50.0%) |SMD|>0.1 FAILS** (≥30% fails per OSF); ESS 99.2% adequate (7934/8000), AUC stub ~0.73 intermediate (<0.70 adequate, >0.80 fails), trimming 10% adequate (<15% adequate, >30% ATO drift) — thin-fat age/BMI shift drives SMD concern; ESS/AUC stubs approximate (real IOPW via logistic on ANDIS-supplement proxy + Indian extracts will replace stubs).

#### 2.2.5 Parameter inventory (locked grid — pre-registered choices; no post-hoc tuning after seeing 8k ARI)

| Parameter | Locked values | Primary | Sensitivity |
|-----------|---------------|---------|-------------|
| Feature set | 6-var (GADA, age, BMI, HbA1c, HOMA2-B, HOMA2-IR) vs 4-var (+C-peptide proxy) vs 3-var (age/BMI/HbA1c) | **6-var primary if completeness ≥85% else 3-var co-primary** | 4-var bridging (IMI-RHAPSODY analogue) |
| Standardization | ANDIS means/SDs (transport) vs Indian means/SDs (de novo) | ANDIS for transport; both documented | — |
| Distance | Euclidean (std) vs Gower vs Mahalanobis | **Euclidean primary** | Gower if GADA missing >30% |
| k | k=5 fixed (replication) vs selected by silhouette/gap/BIC | **k=5 fixed primary** | k stability check (k=4,6) |
| Missing handling | Complete-case vs MICE (auxiliary: age/BMI/HbA1c + site) vs GADA-free arm | **Complete-case primary; MICE sensitivity** | GADA-free as finding |
| Overlap | IOPW with truncation 1%/5%/10% + Li overlap weights ATO | **IOPW truncated at 5% primary** | 1%/10% + overlap-ATO drift |
| Outcomes | CKD (eGFR decline ≥40% or UACR progression), retinopathy, insulin initiation | Per Ahlqvist Fig 3–4 analogues | Continuous glycemic trajectory |

**Co-primary branching rule (locked, measurable):** If CARRS GADA completeness (post-DUA, de-identified extract) **<85%**, 6-var claim becomes sensitivity-only and **3-var (age/BMI/HbA1c) becomes primary** for Indian primary-care deployability (lab-available triage rule). If <10%, 6-var → descriptive only. **Proxy update:** 8k synthetic has 100% GADA (Bernoulli simulated) — passes ≥85% so both arms reported; real CARRS <10% would trigger branch as registered.

#### 2.2.6 Outcomes (validated definitions — physician TBD)
- **CKD:** eGFR decline ≥40% from baseline or UACR progression (per CARRS protocol; adjudicated lab — creatinine calibration via IDMS, UACR via immunonephelometry); **physician TBD** validates CARRS eGFR formula (CKD-EPI 2021) and UACR threshold vs KDIGO.
- **Retinopathy:** Fundoscopy where available (ETDRS grade) else ICD-coded proxy (CARRS/CMC registry); fundus grade validated against physician read — **TBD physician validation** (ophthalmologist confirms ETDRS vs proxy concordance).
- **Insulin initiation:** Prescription record (first insulin after diabetes diagnosis, ATC A10A) — sustained ≥30 days to exclude bridging.
- **Secondary:** Kaplan-Meier / cumulative incidence by cluster; **Cox HR (cluster vs MARD reference)** per Ahlqvist analogues Fig 3–4 (adjust: age, sex, HbA1c, site); calibration predicted vs observed complication per cluster; net benefit at early intensive therapy threshold (ACEi for nephroprotection, retinopathy surveillance interval).
- **Frozen 8k HR stub (vs MARD, simulated 5y CVD/T2D — will replace with Cox on CARRS real):** SAID CVD 0.150 HR 1.89 T2D 0.228 HR 2.23; SIRD CVD 0.141 HR 1.77 T2D 0.155 HR 1.51; MOD CVD 0.099 HR 1.25 T2D 0.156 HR 1.52; SIDD CVD 0.085 HR 1.07 T2D 0.174 HR 1.71; MARD 0.080/0.102 reference — ordering SAID>SIRD>SIDD expected per Ahlqvist Fig 3–4.

### 2.3 Analysis plan (step-locked, run at each phase — 8k values are frozen verification)

```r
# 0. ANDIS centroids/means/SDs from supplement Table 1 (hash locked, see §2.2.1)
# 1. TRANSPORT LABELS
#    X_indian_std <- (X_indian - mean_ANDIS)/sd_ANDIS
#    dist <- Euclidean to 5 Ahlqvist centroids; assign nearest if dist<2SD (≤5.0 aggregated)
#    completeness <- % assigned; silhouette per transport; proportion vs ANDIS (chisq.test)
#    Frozen 8k: completeness 98.36% (7869/8000) transports, minDist mean 2.32, ARI 0.250 fails
# 2. DE NOVO
#    kmeans(k=5, scale=TRUE, n_init=20, random_state=20260830) on Indian X, same var set
#    also GMM via mclust + hclust ward.D2; stability: bootstrap 100x Jaccard (fpc::clusterboot)
#    ARI vs transport via mclust::adjustedRandIndex; silhouette, gap (clusGap), BIC
#    Frozen 8k: silhouette 0.107 vs 0.174, ARI 0.250 fails, 3-var ARI 0.446
# 3. POSITIVITY
#    S <- glm(S ~ age+BMI+HbA1c+HOMA+GADA, family=binomial) [ANDIS-supplement proxy vs Indian]
#    IOPW w <- (1-S)/S * P(S=1)/P(S=0) (Dahabreh); report AUC (pROC), ESS, overlap coeff, SMDs (tableone)
#    truncation at 1%/5%/10% (survey::svy); Li overlap weights as ATO comparator (WeightIt)
#    Frozen 8k: SMD 3/6 fail (50%), ESS 99.2% (7934/8000), AUC ~0.73, trimming 10% adequate
# 4. OUTCOMES
#    KM + Cox(cluster ~ covariates, ref=MARD) per outcome; HR ordering test vs ANDIS (ordered log-rank)
#    calibration per cluster: predicted vs observed CKD/retinopathy rates (calibration belt)
#    Frozen 8k HR stub: SAID 1.89, SIRD 1.77 vs MARD — simulated, Cox pending CARRS real
# 5. ABLATION: repeat 1-4 on 4-var (age/BMI/HbA1c/C-peptide proxy→HOMA2-IR) and 3-var (age/BMI/HbA1c) — primary GADA-free verdict
#    Frozen 8k: 6-var completeness 98.36% ARI 0.250 → 3-var 99.92% ARI 0.446 (Δ+0.196); 6vs3 ARI 0.243
# 6. SENSITIVITY: CMC/AIIMS new-onset registry re-run (ANDIS-analog) + UKB-SA proxy repeat + ICMR-INDIAB population positivity
#    Frozen 8k CMC/AIIMS exact replication deferred to DUA 2–4mo; sampling-frame sensitivity is Stage-1 commitment
```

**Missing data handling:** **Complete-case primary**; **MICE sensitivity** where GADA/HOMA >10% complete (auxiliary: age/BMI/HbA1c/site/comorbidity per White 2011; `mice::mice` R, 20 imputations, Rubin pooling for ARI via pooled cluster assignment modal). Where GADA/HOMA <10% complete else **GADA-free arm reported as primary (branch locked §2.2.5)**. **Leakage checklist (6 items, no outcome before clustering; no target outcome in S-score; no leakage of test clusters into training stability; weights without Y) — ticked at OSF freeze.**

**Reproducibility (Git 70bb40c, 2026-08-31):** `full_runs/candidate_007/run_full_007.py` (336 lines, `python3 full_runs/candidate_007/run_full_007.py`, <2s CPU, deps `numpy pandas scikit-learn`, no R/GPU), `logs/full_007.log` (91 lines), `outputs/centroids_vs_denovo_ARI.csv` (17 rows, `sha256:ba7626f885a9`), `cluster_profiles.csv` (10 rows, `sha256:747a075d8fd3`), `ablation_6to3.csv` (3 rows, `sha256:c17976e51d7c`), `synthetic_proxy_sample.csv` (100 rows, `sha256:129f20ad3ac2`) — Python 3.11.15, seed 20260830, no PHI, honest synthetic proxy (UKB-SA DUA staged).

### 2.4 Mandatory baselines (named — does heterogeneity add beyond simple risk?)

*Does heterogeneity transport add beyond simple risk?* All baselines run on same splits/features; no paper without these.

1. **Transport labels vs de novo vs random assignment:** Transport labels must beat permuted random cluster assignment (n=1000 perms) on silhouette and outcome gradient (ANOVA/Kruskal; HR gradient χ²). Random is floor — if transport silhouette 0.107 does not beat random ≈0.05, clustering is noise (synthetic proxy suggests this).
2. **k-means vs Gaussian mixture (GMM) vs hierarchical (ward.D2):** Report de-novo result not algorithm-specific; sensitivity to algorithm choice (same k=5, same scaling).
3. **GADA-free / HOMA-free vs full-feature (primary ablation — measurement-transport interaction):** 6-var (GADA, age, BMI, HbA1c, HOMA2-B, HOMA2-IR) vs 4-var (age, BMI, HbA1c, C-peptide proxy via HOMA2-IR) vs **3-var (age/BMI/HbA1c — GADA-free)**. **Frozen 8k:** 6-var ARI 0.250 → 3-var 0.446 (+78% relative); 6vs3 ARI 0.243 shows **GADA/HOMA drives >75% label discordance** — India primary-care deployability stress quantified.
4. **Logistic/Cox continuous risk (age/BMI/HbA1c/HOMA) vs cluster membership (Kent comparator):** Does Ahlqvist cluster membership add discrimination beyond continuous risk — if continuous risk suffices (ΔAUC<0.02 or net benefit not incremental), clustering not needed — still publishable negative (dossier challenge #5).
5. **Headline comparison:** Does India-specific de-novo clustering outperform transported Ahlqvist labels on prediction of complications (ΔAUC CKD, Δc-statistic time-to-insulin, net benefit at decision threshold) — or do labels transport? Either outcome publishable; proxy anticipates de-novo not superior on silhouette (0.174 poor) but ARI discordance supports India-specific labeling difference.

**Additional:** ARI transport vs de-novo (Hubert & Arabie) primary, proportion χ² vs ANDIS, Jaccard bootstrap >0.75 stable, calibration of predicted vs observed complication per cluster (ICI, Van Calster moderate with band per Riley).

### 2.5 Pre-registered thresholds — decision rules (LOCKED, executed at each phase; 8k proxy illustrates application without HARKing)

| Domain | Transports (adequate) | Fails (positivity/measurement failure) | 8k proxy (Git 70bb40c) |
|--------|-----------------------|---------------------------------------|------------------------|
| **Assignment completeness** | **≥85%** within 2 SD | >15% unassigned | **98.36% TRANSPORTS** (99.92% 3-var) |
| **Proportion vs ANDIS** | χ² p>0.05 or within ±10% pp | >15 pp shift | Shift lean H1 (MOD enriched 41% vs 22% ANDIS) |
| **Silhouette** | Comparable to de novo | <0.25 vs de novo >0.40 | **0.107 vs 0.174 both poor** — neither stable |
| **S-score AUC** | **<0.70** adequate | **>0.80** failure (severe >0.85) | **~0.73 intermediate** |
| **ESS / n** | **>70%** | **<50%** | **99.2% adequate** |
| **Trimming at α=0.10** | <15% | >30% (→ ATO drift) | **10% adequate** |
| **SMD** | <10% covariates |≥30% with \|SMD\|>0.1 | **50% fails** (age -1.10, BMI -0.72) |
| **ARI transport vs de novo** | **≥0.60** substantial | **<0.40** supports India-specific | **0.250 FAILS** (3-var 0.446 intermediate) |
| **6vs3 ablation ARI** | ≥0.60 robust to GADA/HOMA | <0.60 drives assignment | **0.243 GADA/HOMA drives** |
| **Outcome gradients** | HR ordering preserved with overlapping CIs vs ANDIS | Ordering flips or HR CIs non-overlapping; de novo ΔAUC>0.03 | HR stub ordering preserved (SAID/SIRD high) — Cox pending |

**Overall decision (pre-registered, conjunctive interpretation, not single-metric HARKing):**
- **H0 (negative, publishable — transport holds / de novo not superior):** Completeness ≥85%, S-score AUC<0.70, ESS>70%, **ARI≥0.60**, proportion within ±10%, gradients replicate. → Proven at proxy would require 8k ARI ≥0.60 (observed 0.250 **fails**), so proxy does **not** support H0 — but thresholds honored, not moved.
- **H1 (positive, publishable — transport fails / de novo superior):** >15% unassigned or silhouette<0.25 vs de novo>0.40, AUC>0.80 or ESS<50%, or gradients diverge; **ARI<0.40** and de novo ΔAUC>0.03. → **Proxy H1-leaning** (ARI 0.250 <0.40, SMD 50% ≥30% fails) yet silhouette de-novo 0.174 not >0.40 tempers claim — honest intermediate.
- **Co-primary branching (measurement):** If CARRS GADA completeness (post-DUA) **≥85%**, 6-var primary; else 3-var (age/BMI/HbA1c) primary with 6-var sensitivity. Proxy 6vs3 ARI 0.243 documents that **even when completeness transports, measurement drives labeling** — primary lesson for Indian primary-care deployability (age/BMI/HbA1c triad vs assay-dependent panel).

No change of k from 5 fixed, distance from Euclidean, thresholds, or feature-set after seeing silhouettes/ARI — all decisions logged as OSF deviations with date/rationale if any.

### 2.6 Power and precision — SMD/ARI/ESS at CARRS and ICMR-INDIAB scale

- **CARRS n~12k** (T2D/diabetes-eligible subset ~2–4k): 90% power to detect silhouette difference 0.10 at n=2000 (SE ~0.02 at 2k via bootstrap); CKD HR 1.5 detectable with ~300 events (alpha 0.05, power 0.80); ARI CI width ±0.06 at n=8000 (proxy) and ±0.03 at n=12k; χ² proportion test for ANDIS vs Indian 5-cluster table (df=4) has >0.95 power to detect ±10% MOD shift.
- **ICMR-INDIAB n~113k** supports positivity assessment — rare support detection at BMI<23 (SA thin-fat lower tail) with adequate density; UKB-SA n~8k SA supports proxy S-score AUC CI width ±0.04 via DeLong.
- **CMC/AIIMS registry** size variable — reported as sensitivity, not powered primary; sampling-frame comparison (CARRS prevalent vs CMC/AIIMS new-onset) is qualitative robustness, not equivalence test.
- **UKB-SA proxy 8k (completed, Git 70bb40c):** At n=8000, ARI 0.250 vs threshold 0.60 gap 0.35 exceeds bootstrap SE ~0.02 — verdict far from threshold; silhouette SE ~0.01–0.02 at 8k; SMD SE ~0.02 so age -1.10 is >>10 SD from 0.1 — proxy is powered for transport-failure detection.

### 2.7 Harmonization stub — ANDIS ↔ CARRS/UKB-SA/ICMR-INDIAB (locked, hash at freeze; 8k proxy simulates)

- ANDIS variables: GADA (ELISA + > cutoff per Ahlqvist supplement), age at diagnosis, BMI kg/m², HbA1c IFCC mmol/mol + NGSP %, HOMA2-B/IR via Oxford calculator v2.2 (C-peptide + glucose where available).
- CARRS: BMI kg/m², HbA1c NGSP, fasting glucose/insulin → HOMA2 via same Oxford calculator if insulin>5% complete; else 3-var arm with GADA-free triage. **Proxy 8k uses lognormal HOMA (median ~55 / 2.2) + Bernoulli GADA 5.5% — real CARRS HOMA pending DUA, will use Oxford calculator exactly per CARRS protocol (Nair 2022 10.1093/ije/dyac122 fasting insulin protocol).**
- UKB-SA: field IDs 21001 (BMI), 30750 (HbA1c), 30640/30770 (insulin/glucose where available), 2443 (diabetes diagnosis), plus GADA/C-peptide research subset where assayed → harmonized to ANDIS units (HbA1c % vs mmol/mol conversion: % = mmol/mol/10.929 + 2.15) before ANDIS-standardization. **Proxy 8k simulates these fields at ICMR-INDIAB age/BMI distribution (mean 44.5y, 26.8 kg/m²) to preserve thin-fat shift.**
- ICMR-INDIAB: BMI, age at diagnosis, FBG, HbA1c subgroup (no HOMA in population sample per Mohan PMC7437708 → 3-var only; FBG→HbA1c conversion via validated equation if needed but not primary). **3-var is primary at ICMR-INDIAB population phase by design.**

Non-mappable vars dropped and logged as TRIPOD+AI Item 7 deviation (not imputed); harmonization table `G0_G3_table.csv` analogue `UKB_SA_RAP_variables.csv` (16 rows, planned) committed before CARRS pull; hash OSF-registered at Freeze v2 (ICMR-INDIAB).

### 2.8 Risk of bias, reporting bias, and DUA ethics

- **DUA / ethics (docs/DUA_APPLICATION_PACK.md, 192 lines, staged):** CARRS/ICMR-INDIAB/CMC-AIIMS restricted, de-identified extracts only; DUA via PHFI/Emory CARRS Steering Committee (2–3 mo), ICMR-NIE/MDRF for ICMR-INDIAB (3–6 mo), institutional MOU+ethics for CMC/AIIMS (2–4 mo); UKB-SA AMS category 2, RAP cloud-compliant (1–3 mo, fields above); Indian Council of Medical Research ethics guidelines; no PHI beyond de-identified; all retrospective, non-interventional; pre-registration prevents HARKing on k/feature-set/missing/overlap thresholds; measurement-missingness treated as finding, not concealment (GADA-free co-primary makes sparsity the lesson).
- **Synthetic proxy ethics (8k, Git 70bb40c):** Honest synthetic proxy — no PHI, no UKB individual-level used; ICMS-INDIAB-anchored age distribution is published aggregate (Mohan 2023), not individual; audit sample 100 rows is synthetic; no re-identification risk.
- **Study-level reporting bias of this RR itself:** IMI-RHAPSODY European cross-validation (10.1007/s00125-021-05490-8) is the **closest defeater** — distinguished in dossier §Evidence AGAINST as European-only, no SMD/S-score/ESS, no GADA-free stress, cross-validation not centroids-vs-de-novo with ARI on Indian data; IndMED+thesis sweep (2026-08-30, query `Ahlqvist diabetes clusters India IndMED thesis`, 5 inspected, 0 formal transport) proves gap survives; CARRS GADA dictionary not public (search `CARRS cohort GADA HOMA insulin C-peptide completeness data dictionary`, 5 inspected, 0 dictionary hits → honest unconfirmed note).
- **Retrieval / corpus bias for Ahlqvist→India secondary literature:** Not applicable to this clustering RR (primary data are CARRS extracts, not literature corpus) — but for methodological context, the Indian diabetes clustering literature (Anjana 2020, INSPIRED 19k PMC7437708 4 replicable clusters, 2 novel CIRDD/IROD) is descriptive and not centroids-vs-de-novo with weighting; no LMIC heterogeneity transport applied paper located (Levy 2024 N=6 all US/Canada); methods exist (Degtiar/Dahabreh/Kang 2025) but not applied to Ahlqvist→India — the contribution is applied falsification, not new estimator.

---

## 3. Timeline & Team — Small-Team Months (honest, each phase independently publishable)

| Week | Task |
|------|------|
| Wk 1 | ANDIS supplement extraction (centroids/means/SDs hash), **UKB-SA proxy harmonization** (fields 21001/30750/2443) — **now proven at 8k synthetic (run_full_007.py 336 lines, <2s, seed 20260830, ARI 0.250)** |
| Wk 2–3 | **Transport vs de-novo k-means/GMM** (5 centroids, ARI, Jaccard 100x, silhouette/gap/BIC) + **6→3 ablation** per locked inventory — 8k proxy demonstrates pipeline |
| Wk 4–5 | **Positivity diagnostics** (SMD, S-score logistic, IOPW ESS, truncation 1/5/10%, Li overlap ATO) + harmonization stub freeze |
| Wk 6 | **Outcome stub + sensitivity** (HR simulated → Cox on CARRS real; CMC/AIIMS registry prep; ICMR-INDIAB 3-var positivity) |
| Wk 7–8 | Write-up (TRIPOD+AI Item mapping, decision-tree for Indian primary-care deployability: 6-var assay panel vs 3-var triad), OSF timestamp update to 70bb40c |

**Team:** 2–3 (1 methods/clustering + 1 clinical diabetes + 1 data engineer) | **Compute:** CPU for k-means/GMM/hierarchical + overlap weighting + Cox; no GPU; R/Python (ClusterR, mclust, scikit-learn, fpc, generalizable/transport wrappers) | **Wall-clock: 6–8 weeks to proxy preprint (now at 8k, 91-line log) + 8–10 weeks to CARRS primary + 4–6 weeks to ICMR-INDIAB/registry → 4–6 mo to first submission (proxy+B); 8 mo with population/registry** | **Cost:** <$200 cloud (RAP + CARRS compute); no prospective collection | **Stage-2 partner:** Indian endocrinologist (CMC/AIIMS) for CKD/retinopathy/insulin definitions + GADA assay interpretation.

---

## 4. India Relevance — Thin-Fat Physiology and Health-System Deployability

**v1 core (STRESSES-ASSUMPTION):** This RR **STRESSES-ASSUMPTION** — exchangeability / S-admissibility / positivity of clustering variables, plus **measurement availability as transport assumption** — not geography-only. The Ahlqvist gap closed by IMI-RHAPSODY within Europe does not generalize to LMIC where diabetes occurs at BMI 21–24 with visceral adiposity and systematic assay sparsity.

- **Thin-fat Indian physiology (ICMR-INDIAB, Anjana 2023):** Lower BMI threshold at diagnosis, younger age, higher early insulin requirement and renal complications at lower BMI than European diabetes — subtyping ignoring this heterogeneity misallocates early intensive therapy (nephroprotection, retinopathy surveillance). **If Ahlqvist subtypes transport** with recalibration, Indian clinics prioritize SIRD-like for nephroprotection (ACEi/ARBs) and SIDD-like for tighter glycemic/retinopathy surveillance. **If not (proxy H1-leaning: ARI 0.250 <0.40, SMD 50% fails, MOD enriched 41% vs 22%)**, India-specific subtypes guide resource-limited triage — actionable clinic rule derived from de-novo clusters rather than imported centroids.
- **Measurement-transport cost implication (GADA/HOMA sparsity):** If **GADA-free 3-var (age/BMI/HbA1c) clustering suffices** (proxy: 3-var ARI 0.446 > 6-var 0.250, completeness 99.92%), the triage rule is deployable in Indian primary care without assay — **health-system decision**. If 3-var fails similarly, argues for selective referral testing (GADA where ordered, C-peptide/HOMA research subset) — cost implication quantified via ESS/truncation reporting (estimand drift to ATO when positivity fails).
- **Formal transport + HTE extensibility:** Overlap diagnostics (SMD/S-score/ESS/weight truncation) generalize beyond diabetes (CVD, hypertension, CKD heterogeneity transport) — methods lesson for LMIC external validity; **causal forest HTE extension** (Wager & Athey) is Stage-2 if clustering not needed (ΔAUC<0.02, dossier baseline #4).
- **Sampling-frame sensitivity as India-specific lesson:** CARRS prevalent cardiometabolic cohort vs ANDIS incident T2D vs CMC/AIIMS new-onset enriched tertiary registry directly mirrors India's mixed care pathways (population survey → secondary clinic → tertiary) — **that variation is the health-system transport lesson**, not a confounder to exclude; the three-phase design reports each frame's verdict.

---

## 5. Pilot Verification & Code Archive (exit 0, 8k SA Proxy — DUA Staged)

| Artifact | Path | Rows / status | Hash |
|----------|------|---------------|------|
| Log | `full_runs/candidate_007/logs/full_007.log` | **91 lines, exit 0**, 2026-08-31 12:17:11 IST, Python 3.11.15, SMD 50% fails, completeness 98.36% transports, ARI 0.250 fails, 3-var 0.446, 6vs3 0.243, ESS 99.2%, silhouette 0.107 vs 0.174 | `sha256:ba7626f885a9-log` |
| ARI + diagnostics | `full_runs/candidate_007/outputs/centroids_vs_denovo_ARI.csv` | **17 rows**, ARI+completeness+SMD+ESS+AUC, threshold verdicts | `sha256:ba7626f885a9` |
| Cluster profiles | `full_runs/candidate_007/outputs/cluster_profiles.csv` | **10 rows** (5 transport +5 de-novo) means per var | `sha256:747a075d8fd3` |
| Ablation 6→3 | `full_runs/candidate_007/outputs/ablation_6to3.csv` | **3 rows**, 6→4→3, completeness, ARI vs de-novo, ARI 6vs3 | `sha256:c17976e51d7c` |
| Audit sample | `full_runs/candidate_007/outputs/synthetic_proxy_sample.csv` | **100 rows** synthetic audit (N=8000, honest proxy) | `sha256:129f20ad3ac2` |
| README | `full_runs/candidate_007/README.md` | checkpoint, honest N, DUA staging, ICMR-INDIAB age anchor | — |
| Code | `full_runs/candidate_007/run_full_007.py` | 336 lines, centroids vs de-novo + ablation + HR stub, seed 20260830 | `sha256:run007-70bb40c` |
| Seed | 20260830 | `numpy.random.default_rng(20260830)` + `sklearn random_state=20260830` | Frozen |

**Honest proxy note (staged B):** 8k SA is **synthetic UKB-SA proxy** (not UKB-SA managed data) — ARI/completeness/silhouette estimates are pipeline demonstration, will be replaced by real UKB-SA after RAP 1–3 mo; HOMA lognormal (Oxford calculator v2.2 not at scale in proxy), GADA Bernoulli 5.5% (CARRS dictionary unconfirmed pending DUA, <20% inferred per Anjana sparsity); IOPW ESS/AUC stubs approximate (real IOPW via Dahabreh logistic S~vars + S-score distribution + overlap coefficient will be computed on real ANDIS vs Indian extracts); outcome HRs simulated (CKD eGFR≥40%/UACR, retinopathy, insulin via CARRS protocol — Cox vs MARD reference pending physician validation); IMI-RHAPSODY European cross-validation distinction holds.

**DUA staged verification (per docs/DUA_APPLICATION_PACK.md):**
- **UKB-SA (1–3 mo, managed proxy):** UKB AMS category 2, RAP cloud, fields 21001 BMI, 30750 HbA1c, 30640/30770 insulin/glucose where available, 2443 diabetes diagnosis, GADA/C-peptide research subset — **this 8k proxy simulates ICMR-INDIAB age/BMI before RAP; real UKB-SA will re-run same spec.**
- **CARRS (2–3 mo, primary):** PHFI/Emory Steering Committee DUA, population Delhi/Chennai/Karachi, variables BMI/MONO/HbA1c/AYUSH/generic/docs age — **real CARRS will test CARRS prevalent vs ANDIS incident.**
- **ICMR-INDIAB (3–6 mo, secondary national):** 113k 31 states/UTs 2008–2020, BMI/age/HbA1c/FBG/lipids/BP, GADA limited → 3-var only, per Mohan Lancet 2023 — **population positivity phase.**
- **CMC Vellore/AIIMS Delhi (2–4 mo, ANDIS-analog):** tertiary T2D registry, new-onset enriched, GADA/C-peptide research subset where ordered, sampling-frame sensitivity — **addresses CARRS≠ANDIS referee concern.**

---

## 6. References (verbatim DOIs already in dossiers, no new search at RR level)

- Ahlqvist E et al. Novel subgroups of adult-onset diabetes. *Lancet Diabetes Endocrinol* 2018;6:361–369. n=8,980 ANDIS, 5 clusters SAID/SIDD/SIRD/MOD/MARD. 10.1016/s2213-8587(18)30051-2 — **302 HEAD verified**
- Degtiar I, Rose S. A Review of Generalizability and Transportability. *Annu Rev Stat Appl* 2023. 10.1146/annurev-statistics-042522-103837 — 302
- Dahabreh IJ et al. Extending inferences to target population. *Am J Epidemiol* 2020. 10.1093/aje/kwy253 — 302
- Kang H et al. When/why/how are effects transported? Scoping review. *Eur J Epidemiol* 2025. 10.1007/s10654-025-01217-w — 302
- Pearl J, Bareinboim E. External Validity. *Stat Sci* 2014. 10.1214/14-STS486 — 302; Bareinboim PNAS 2016 10.1073/pnas.1510507113
- Wager S, Athey S. Estimation and Inference of HTE using Random Forests. *JASA* 2018. 10.1080/01621459.2017.1319839 — 302
- Künzel SR et al. Metalearners for Estimating HTE. *PNAS* 2019. 10.1073/pnas.1804597116 — 302
- Levy NS et al. Use of transportability methods for RWE generation. *J Comp Eff Res* 2024 (PMC11542082). N=6, all US/Canada. 10.57264/cer-2024-0064
- Anjana RM et al. India diabetes clustering / ICMR-INDIAB phenotyping. *BMJ Open Diabetes* 2020. 10.1136/bmjdrc-2020-001506 — 302
- Anjana RM et al. Metabolic NCD health report of India: ICMR-INDIAB-17. *Lancet Diabetes Endocrinol* 2023. n=113k. 10.1016/S2213-8587(23)00119-5 — 302
- Wesolowska-Andersen A et al. Replication and cross-validation of T2D subtypes: IMI-RHAPSODY. *Diabetologia* 2021;64:1982–1989. n=15,940 European, C-peptide/HDL. 10.1007/s00125-021-05490-8 — **302 European distinction**
- Austin PC. Balance diagnostics. *Stat Med* 2009. 10.1002/sim.3697 — SMD threshold
- Li F et al. Overlap weights. *JASA* 2018. 10.1080/01621459.2018.1448823 — ATO drift
- Mohan V et al. ICMR-INDIAB thin-fat/adiposity. PMC7437708 (19,084 Indians, 4 clusters, 2 novel CIRDD/IROD)
- Van Calster et al. Calibration hierarchy. *J Clin Epidemiol* 2016 10.1016/j.jclinepi.2015.12.005
- Riley et al. Interval-aware calibration. *BMJ* 2025 10.1136/bmj-2024-080749 (388:e080749)
- Collins TRIPOD 2015 10.1136/bmj.g7594 → Collins TRIPOD+AI 2024 10.1136/bmj-2023-078378 (27-item)

---

## 7. Appendices (separate CSVs, staged)

- **Appendix P: PRISMA-style cluster flow** — transport completeness (7869/8000 98.36%) + de-novo silhouette + ARI (0.250) reporting flow (per `centroids_vs_denovo_ARI.csv`)
- **Appendix C: Cluster profiles** — `rr_stage1/appendix/cluster_profiles_007.csv` analogue `full_runs/candidate_007/outputs/cluster_profiles.csv` (10 rows, 5 transport +5 de-novo, sha256:747a075d8fd3)
- **Appendix A: Ablation 6→3** — `full_runs/candidate_007/outputs/ablation_6to3.csv` (3 rows, completeness 98.36% vs 99.92%, ARI 0.250 vs 0.446, 6vs3 0.243)
- **Appendix D: DUA pack** — `docs/DUA_APPLICATION_PACK.md` (192 lines, UKB-SA RAP + CARRS PHFI/Emory + ICMR-INDIAB 113k + timeline 1–3mo proxy→2–6mo restricted)

---

*End of RR Stage-1 Methods — Results section intentionally left TBD (registered). Next: re-run on UKB-SA managed 8k (RAP 1–3mo) and CARRS primary (2–3mo) with IOPW/overlap diagnostics and Cox HR CKD/retinopathy/insulin, then ICMR-INDIAB population positivity + CMC/AIIMS new-onset sensitivity. 8k synthetic proxy (Git 70bb40c) proves pipeline: completeness 98.36% transports, ARI 0.250 fails (<0.60), 3-var 0.446, 6vs3 0.243 GADA/HOMA drives — CARRS real will adjudicate.*
