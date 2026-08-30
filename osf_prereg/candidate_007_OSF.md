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
| **Version hash** | `sha256:PENDING-007-` + commit hash at freeze |
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

**Honest CARRS note (REVISE 2026-08-30):** Data dictionary not public — inferred GADA/HOMA <20% from cohort profiles. Pre-registered rule: **3-var co-primary**; 6-var aspirational, requires **completeness ≥85%** to claim; if <10% post-DUA, 6-var → sensitivity-only.

---

## 3. Clustering Specification — Centroids vs De Novo (LOCKED, pre-registrable)

### 3.1 Source (ANDIS) reference
- Published centroids/means/SDs per Ahlqvist Table 1 (no source individual-level needed; ANDIS consortium request optional for supplement but not required for v1 — centroids suffice).

### 3.2 Transport-labels arm (pre-registered, deterministic)
- Standardize Indian data **using ANDIS means/SDs** (transport standardization).
- Assign each Indian participant to **nearest Ahlqvist centroid** (Euclidean in standardized 6-D; Gower if GADA categorical/missing).
- Report: **assignment completeness (% within 2 SD of a centroid)** — primary stability metric; silhouette; proportion table vs ANDIS (χ²).

### 3.3 De-novo arm (unsupervised comparator, same spec)
- Run **k-means with same spec (k=5, scaled)** on Indian data alone; sensitivity: **4-var** (age/BMI/HbA1c/C-peptide proxy) and **3-var (age/BMI/HbA1c — GADA-free)**.
- Compare de-novo to transport labels via **adjusted Rand index (ARI)** + outcome-gradient concordance.
- Stability: **Jaccard bootstrap ≥100 resamples** (fpc); silhouette, gap statistic (Tibshirani), BIC via GMM.

### 3.4 Positivity / overlap diagnostics (pre-registered, primary methods contribution)
- **Inverse-odds weighting (Dahabreh 10.1093/aje/kwy253):** logistic propensity P(S=Scandinavian | S-variables: age, BMI, HbA1c, HOMA, GADA) → IOPW weights.
- Report: **S-score distribution plot** (source vs target density), **overlap coefficient**, **AUC**, **ESS = (Σw)²/Σw²**, weight truncation sensitivity at **1%/5%/10%** (Lee 10.1371/journal.pone.0018174; Crump; Li 10.1080/01621459.2018.1448823).
- **SMD distribution** per Austin 2009 10.1002/sim.3697: |SMD|>0.1 threshold.
- Sensitivity: **overlap weights (Li 2018)** as ATO comparator when positivity fails severely — report estimand drift (ATE vs ATO).

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

---

## 5. Mandatory Baselines (named — does heterogeneity add beyond simple risk?)

1. **Transport labels vs de novo vs random assignment** (permuted random as floor: silhouette + HR gradient χ²).
2. **k-means vs GMM vs hierarchical** (same k=5, same scaling — algorithm sensitivity).
3. **GADA-free / HOMA-free ablation: 6→4→3 var** (primary ablation — measurement-transport interaction).
4. **Logistic/Cox continuous risk (age/BMI/HbA1c/HOMA) vs cluster membership** (Kent comparator): if continuous risk suffices (ΔAUC<0.02), clustering unnecessary — publishable negative.
5. **Headline:** India-specific de novo vs transported Ahlqvist labels on prediction of complications (ΔAUC CKD, Δc-statistic time-to-insulin, net benefit at decision threshold).

**Additional:** ARI transport vs de novo (Hubert & Arabie), proportion χ² vs ANDIS, calibration per cluster.

---

## 6. Sample Size & Power

- **CARRS n~12k** (T2D/diabetes-eligible subset ~2–4k): 90% power to detect silhouette difference 0.10 at n=2000; CKD HR 1.5 detectable with ~300 events.
- **ICMR-INDIAB n~113k** supports positivity assessment (rare support detection at BMI<23); UKB-SA n~8k SA supports proxy S-score AUC CI width ±0.04.
- **CMC/AIIMS registry** size variable — reported as sensitivity, not powered primary.

---

## 7. Analysis Plan (step-locked, run at each phase)

```r
# 0. ANDIS centroids/means/SDs from supplement Table 1 (hash locked)
# 1. TRANSPORT LABELS
#    X_indian_std <- (X_indian - mean_ANDIS)/sd_ANDIS
#    dist <- Euclidean to 5 Ahlqvist centroids; assign nearest if dist<2SD
#    completeness <- % assigned; silhouette, proportion vs ANDIS (chisq)
# 2. DE NOVO
#    kmeans(k=5, scale=TRUE) on Indian X, same var set; also GMM(mclust), hclust(ward)
#    stability: bootstrap 100x Jaccard (fpc::clusterboot), ARI vs transport (mclust::adjustedRandIndex)
# 3. POSITIVITY
#    S <- logistic(S ~ age+BMI+HbA1c+HOMA+GADA) [source ANDIS-supplement proxy vs Indian]
#    IOPW w <- (1-S)/S * P(S=1)/P(S=0) (Dahabreh); report AUC, ESS, overlap coeff, SMDs
#    truncation at 1%/5%/10%; Li overlap weights as ATO comparator
# 4. OUTCOMES
#    KM + Cox(cluster ~ covariates, ref=MARD) per outcome; HR ordering test vs ANDIS
#    calibration per cluster: predicted vs observed CKD/retinopathy rates
# 5. ABLATION: repeat 1-4 on 4-var and 3-var (age/BMI/HbA1c) — primary GADA-free verdict
# 6. SENSITIVITY: CMC/AIIMS new-onset registry re-run (ANDIS-analog) + UKB-SA proxy repeat
```

**Missing data:** MICE as sensitivity where GADA/HOMA >10% complete else GADA-free arm reported as primary (branch locked above).

**Leakage checklist (6 items):** No outcome before clustering; no target outcome in S-score; no leakage of test clusters into training stability; weights without Y.

---

## 8. Harmonization Stub (ANDIS ↔ CARRS/UKB-SA/ICMR-INDIAB)

- ANDIS variables: GADA (ELISA + > cutoff), age at diagnosis, BMI, HbA1c (IFCC mmol/mol + NGSP %), HOMA2-B/IR (Oxford calculator v2.2).
- CARRS: BMI kg/m², HbA1c NGSP, fasting glucose/insulin → HOMA2 via same Oxford calculator if insulin>5% complete; else 3-var arm.
- UKB-SA: field IDs 21001 (BMI), 30750 (HbA1c), 30640/30770 (insulin/glucose where available), 2443 (diabetes diagnosis) → harmonized to ANDIS units before standardization.
- ICMR-INDIAB: BMI, age at diagnosis, FBG, HbA1c subgroup (no HOMA in population sample per Mohan PMC7437708 → 3-var only).

---

## 9. Ethics & Privacy

- CARRS/ICMR-INDIAB/CMC-AIIMS: restricted, de-identified extracts; DUA via PHFI/Emory (CARRS Steering), ICMR-NIE/MDRF (ICMR-INDIAB), institutional MOU (CMC/AIIMS); Indian Council of Medical Research ethics guidelines; no PHI beyond de-identified.
- UKB-SA: UK Biobank EGC oversight; managed access AMS, RAP cloud; no download beyond extracts.
- ANDIS summary stats: published, no individual-level — zero privacy risk.
- All retrospective, non-interventional; pre-registration prevents HARKing on k/feature-set/missing/overlap thresholds.

---

## 10. Staged Execution While DUA Pends (honest, each phase independently publishable)

| Phase | Duration | Dataset | Deliverable |
|-------|----------|---------|-------------|
| **Phase 1: UKB-SA proxy feasibility + 6→3 ablation (B proxy)** | **6–8 weeks after UKB access** (harmonize, standardize per ANDIS means/SDs, transport vs de novo k-means/GMM, ARI, SMD/overlap) | UKB-SA | Proxy feasibility preprint: overlap + 3-var verdict |
| **Phase 2: CARRS primary transport vs de novo + positivity diagnostics + outcome gradients (B restricted)** | **8–10 weeks after CARRS receipt** (IOPW, ESS, truncation, Cox HRs for CKD/retinopathy/insulin) | CARRS | **Primary paper: centroids vs de novo with full diagnostics** |
| **Phase 3: ICMR-INDIAB population positivity + CMC/AIIMS new-onset sensitivity (B restricted)** | **4–6 weeks after receipt** (sampling-frame sensitivity, age-stratified overlap) | ICMR-INDIAB + CMC/AIIMS new-onset registry | Extension: population vs clinic transport + new-onset validation |
| **Total ceiling** | **4–6 mo to first submission (proxy+B); 8 mo with ICMR-INDIAB/registry** | — | One registered report + one empirical paper |

---

## 11. TRIPOD+AI 27-Item Mapping (10.1136/bmj-2023-078378)

Items 1–4 (title/abstract/background): Ahlqvist→India transport gap + IMI-RHAPSODY distinction stated. 5–7 (data/participants): CARRS/ICMR-INDIAB/UKB-SA/CMC-AIIMS/MIMIC-IV/ANDIS supplement with timelines. 8–12 (sample, outcome, predictors, missing): n~12k/113k/8k; CKD/retinopathy/insulin (physician TBD); 6→3 var + distance/k/missing pre-locked. 13–17 (analysis): k-means/GMM/hierarchical + IOPW/overlap weights + ARI/Jaccard + Cox HRs; calibration hierarchy Van Calster 10.1016/j.jclinepi.2015.12.005 + Riley 10.1136/bmj-2024-080749. 18–22 (validation/performance): UKB-SA proxy → CARRS → ICMR-INDIAB staged; silhouette/ARI/AUC/ESS/HR discrimination + net benefit. 23–27 (availability/limitations): code/hashes at OSF; honest CARRS GADA unconfirmed; ANDIS-vs-CARRS frame sensitivity via CMC/AIIMS.

---

## 12. Sensitivity & Decision Rules Recap (what we will NOT change post-lock)

- No change of k from 5 fixed after seeing silhouettes.
- No change of distance from Euclidean after seeing ARI.
- No change of thresholds (≥85% / <0.70 / >70% / ≥0.60) after seeing assignments.
- **If CARRS GADA completeness <85%:** pre-registered branch to 3-var primary, 6-var sensitivity-only (documented, not HARKed).
- **If CARRS overlap fails but CMC/AIIMS registry transports:** reported as frame-driven failure, not biological heterogeneity.
