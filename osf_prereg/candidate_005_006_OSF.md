# OSF Pre-registration — Candidate 005 + 006 Paired India Plasmode (STRESSES-ASSUMPTION)
**Shared G0→G3 Audit-Anchored Infrastructure | Cycle 6 OSF-Ready (2026-08-30)**
**Companion dossiers:** `ideas/candidate_005.md` (G0→G3 Transport vs Recalibration) + `ideas/candidate_006.md` (Audit→RR Anchored E-value + NC Ladder)
**Authors:** clinical-evidence-scout + methods-scout (paired)
**OSF registration type:** Registered Report Stage 1 — paired D+B staged plasmode
**TRIPOD+AI:** 10.1136/bmj-2023-078378 (27-item mapping §11) | Calibration hierarchy: Van Calster 10.1016/j.jclinepi.2015.12.005 + Riley 10.1136/bmj-2024-080749
**Data availability tier:** D (plasmode, no PHI) + B (UKB-SA managed proxy 1–3 mo; CARRS/ICMR-INDIAB restricted 2–6 mo)

---

## 0. Administrative

| Field | Value |
|-------|-------|
| **Title** | Graded Indian shift plasmode G0→G3: shared audit-anchored infrastructure for (005) transport-vs-recalibration and (006) audit→RR E-value + NC ladder |
| **Version hash (pre-freeze placeholder)** | `sha256:PENDING-005006-` + commit hash at OSF freeze — replace at submission |
| **Random seed (locked)** | 20260830 (plasmode resampling) + 42 (train/test); all R `set.seed()` + Python `random.seed()`/`numpy` recorded |
| **Analysis date lock** | Analysis scripts locked at freeze; no peeking at target outcomes before thresholds fixed (below) |
| **Embargo** | Open at Stage 1 acceptance |

---

## 1. Background & Aims (2 pages max at submission)

**Problem:** US-trained models transported to Indian care face covariate and visit-process shifts that stress positivity/S-admissibility/consistency. Indian epidemiology (ICMR-INDIAB-23 MONO 43.3% 10.25259/IJMR_328_2025; CARRS; UKB-SA risk-equivalent BMI 21–22 vs 30 White) + health-system measurement shift (WHO audits: HbA1c 78%→15% observed, generic 4.7–64.9%, AYUSH 44–96%, diagnosis docs 8.5–100%) are quantifiable but unlinked to model diagnostics.

**Paired aims sharing one graded plasmode:**
- **005:** Does graded Indian shift G0→G3 require inverse-odds weighting (IOPW/AIPW) or does recalibration suffice? Diagnostic dose-response (SMD/S-score/ESS/trimming) adjudicates.
- **006:** Does WHO-audit-derived confounding (irrational FDC, generic non-compliance, AYUSH, polypharmacy) translated to VanderWeele E-value bounding factor B explain away typical RR_obs ≈1.2–1.8? Fixed-point R* threshold + NC ladder calibrates.

**Shared infrastructure thesis:** One audit-anchored tilting + S_visit censoring plasmode powers both questions, halving engineering/staff cost.

---

## 2. Data & Participants

### 2.1 Source scaffold — D (immediate, no PHI)
- **Source:** MIMIC-IV v3.0 (PhysioNet, credentialed ~1–2 weeks, CITI+DUA). n=20k encounters resampled **with replacement** from MIMIC-IV covariate matrix (real X). **No PHI beyond de-identified; no new collection.**
- **Participants (plasmode):** Adults with T2D/CVD risk eligible for ICU admission or T2D complication risk model (mirror candidate 005 §4 and 006 §4). Real X preserves US critical-care joint support (mean BMI 28.3, CVD onset ~62y, labs protocol-driven ~78% complete).
- **Outcome mechanism (known truth, Franklin Generate-Outcome):** Logistic/hazard outcome Y ~ f(X) + shift artifacts; true effect known, so calibration/diagnostics evaluated against truth not deployment risk. Dual framework (Liu 2504.11740: Generate-Outcome + Generate-Treatment) as sensitivity.

### 2.2 Proxy target — B (UKB-SA, managed, 1–3 months)
- **UK Biobank South Asian subset (UKB-SA):** n~8k SA (Indian/Pakistani/Bangladeshi) of ~500k total; RAP application category 2; BMI/WC/HbA1c/lipids/BP/meds/supplements deep phenotyping. Role: **proxy target** for S-score overlap diagnostics before CARRS/ICMR-INDIAB arrive; validates tilting realism.

### 2.3 Restricted targets — B (CARRS 2–3 mo; ICMR-INDIAB 3–6 mo)
- **CARRS** (n~12k Delhi/Chennai/Karachi; CVD 5–10y earlier) and **ICMR-INDIAB** (n=113,043, 31 states; MONO 43.3% state 34.8–56.7%) — National target magnitudes for tilting resampling; CARRS longitudinal for NC ladder (006) after DUA.

### 2.4 Open audit corpus — D (immediate)
- **WHO audit open corpus:** Kaur 2026 PMC13312064 (ED n=648: generic 64.9%, NLEM 87.3%, injections 90.3%, diagnosis 8.5%, 2.65 drugs/Rx) + Khanna 2025 PMC12813935 (Medicine OPD n=300: generic 4.7%, NLEM 61%, injections 4%, polypharmacy 71%, 6.8 drugs/Rx) + Galib 2020 AYU 10.4103/ayu.ayu_81_20 (AYUSH 95.9% ever, 44% simultaneous) + Mohan IJMR 2025 MONO table — **all CC-BY, Europe PMC fullTextXML JATS extracted.** Anchors shift magnitudes (no PHI).

---

## 3. Shared G0→G3 Audit-Anchored Table (LOCKED — all thresholds co-registered)

*All % are marginal target prevalences for tilting; G0 = MIMIC reference, G1 mild lean-urban, G2 moderate national avg (MAIN), G3 severe rural Tripura.*

| Dimension | Parameter | **G0 — MIMIC ref (no shift)** | **G1 — Mild (lean urban India)** | **G2 — Moderate (national avg, MAIN)** | **G3 — Severe (rural Tripura)** | Anchor / justification |
|-----------|-----------|-------------------------------|----------------------------------|----------------------------------------|---------------------------------|------------------------|
| **BMI (mean)** | Mean BMI, kg/m² | **28.3** | 26.0 | 24.5 | **22.8** | MIMIC-IV mean ~28–29; ICMR-INDIAB gen obesity 28.6% → thin-fat distributed phenotype 10.25259/IJMR_328_2025 |
| **MONO prevalence** | BMI<25 ∩ ≥2/5 risks, % | **0** (screened) | 18% | **43.3%** (national) | **56.7%** (Tripura) | Mohan IJMR 2025 PMC12550443 |
| **Age at event** | Median CVD/T2D onset, y | **62** | 58 | **52** (5–10y earlier) | **48** | CARRS IJE 10.1093/ije/dyac122; MDRF Young Diabetes Registry |
| **HbA1c measurement** | % eligible with HbA1c observed | **78%** | 55% | 30% | **15%** | MIMIC ~78% protocol; ICMR-INDIAB every-5th 20% → real-world lower; Kaur/Khanna tables |
| **Selective observation** | P(test \| asymptomatic) | 0.78 (MAR) | 0.45 | 0.20 | **0.20** vs P(test\|sympt)=0.80 gating | Cost/availability gating; diagnosis 91.5% missing ED |
| **Generic prescribing** | Generic % | **100%** (coded) | 85% | 64.9% (Kaur ED) | **4.7%** (Khanna Medicine) | Kaur Table 2 64.9%, Khanna Table 2 4.7% — 60-point spread |
| **AYUSH concomitant** | Ever herbo-mineral, % | **0** | 10% (UKB proxy) | **44%** simultaneous | **96%** ever (Galib) | Galib AYU 10.4103/ayu.ayu_81_20 95.9%/44%; NSS 10–40% |
| **Documentation** | Diagnosis recorded, % | **100%** (structured) | 70% | 29% (Khanna) | **8.5%** (Kaur ED) | Kaur Table 3 8.5%, Khanna 70→29% |
| **Polypharmacy** | Drugs per prescription | 1.8–2.0 | 2.65 (Kaur) | 4.5 | **6.8** (Khanna ward) | Kaur 2.65±1.59, Khanna 6.8±1.7 |

*Implementation (locked):* Covariate tilting via **entropy balancing / iterative proportional fitting** to match ICMR-INDIAB marginals (BMI×WC×HDL×TG×FBG joint where available); **S_visit censoring** via `S_visit(X,cost)=1/(1+exp(−α·score))` deletion, α graded to hit marginal observation rates; pre-register MAR (conditioning on full X) vs MNAR (intermittent labs unconditioned) — latter stresses S-admissibility more. Dual plasmode frameworks per Liu 2025 as sensitivity. **Hashes of tilting weights + censoring functions stored at freeze.**

---

## 4. Predictor / Covariate Specification

- **Covariates for shift (S-variables):** BMI, WC, WHR, HbA1c, FBG, HDL, TG, SBP/DBP, age, sex, SES, medication counts.
- **Visit-process:** `S_visit` score = f(cost, distance, shift staffing, generic availability) → deletion for labs/meds; `S_formulary` (NLEM compliance) and `U_AYUSH` (herbal co-use) as separate nodes in selection diagram.
- **AYUSH U:** Binary U = ever concomitant (44–96%); simultaneous sub-definition at 44% for moderate dose.
- **Standardization:** Pre-registered: tilting preserves MIMIC joint covariance, only margins shifted; S_visit depends on cost quintile + symptom status.

---

## 5. Outcomes & Estimands

### Candidate 005 (transport vs recalibration)
- **Primary:** Calibration (ICI, calibration slope/intercept per Van Calster 10.1016/j.jclinepi.2015.12.005), AUROC, Brier; diagnostics **SMD>0.1 exceedance, S-score AUC, ESS/n, trimming fraction** (primary dose-response); DCA net benefit at p_t 0.05/0.10/0.20 (Vickers).
- **Estimand:** ATE on target (ICMR-INDIAB national) via IOPW; ATO drift when positivity fails (overlap weights Li 2018).

### Candidate 006 (audit→RR)
- **Primary:** Bounding factor **B(p1,p0,RR_UD)** vs **E-value(RR_obs)=RR_obs+√[RR_obs(RR_obs−1)]**; fixed-point **R*** solves E-value(R*)=B; titration contour over RR_UD∈[1.2,4.0] and (p1,p0) from audit envelope.
- **Negative-control ladder (Lipsitch 10.1097/EDE.0b013e3181d61eeb):** ≥2 NC outcomes per contrast (HTN contrast → trauma/appendicitis; T2D contrast → viral URI/derm visit) — **co-primary falsification**: RR_NC≈1 with upper CI < R* supports robustness; RR_NC>1 undermines.

---

## 6. Analysis Plan (pre-registered, pseudo-code locked)

### Shared plasmode pipeline (executed once, analyzed twice)

```r
# SHARED: G0 -> G3 tilting + S_visit censoring (seed 20260830)
# Input: MIMIC-IV n=20k X matrix (real)
# Tilting: entropy balancing to ICMR-INDIAB MONO/BMI/WC/HDL joint at G1/G2/G3 targets
# S_visit: delete lab/meds with p=1-1/(1+exp(-alpha*S_visit)), alpha graded to hit observation % table
# Store: weights_G1..G3, censor_masks, hashes
# Sensitivity: Generate-Outcome vs Generate-Treatment (Liu dual)
```

### 005 — Staged transport vs recalibration (pre-registered sequence)
1. At each G0→G3: compute SMDs (Austin 10.1002/sim.3697), train L1-logistic **S-score = P(S=1|X)** source vs proxy-target, report **AUC**, overlap coefficient, overlap plot, weight distribution.
2. Estimate **IOPW (Dahabreh)** + **AIPW doubly-robust** + **outcome-model standardization** + **calibration weighting (Josey)** + **overlap-weight ATO (Li)** — at truncation α=0.05/0.10 (Sturmer/Lee/Crump).
3. Compare **recalibrated LR (Steyerberg intercept+slope via 10-fold CV, Platt)** vs AIPW on ICI/slope/AUROC at each grade; declare **recalibration suffices** if ICI<0.05 & slope 0.9–1.1 & ΔAUROC<0.03 and diagnostics benign, else **transport required** if ICI>0.08 or ΔAUROC>0.04 and AUC>0.80/ESS<50%/trimming>20%.
4. Report **dose-response decision**: at which grade AUC crosses 0.80/0.85, trimming >20%, ESS<50%.

**Pre-registered thresholds (005):**

| Diagnostic | Adequate (recalibration suffices) | Failure (transport required) |
|------------|-----------------------------------|------------------------------|
| Mean \|SMD\| >0.1 exceedance | <10% covariates | ≥30% covariates |
| S-score AUC | <0.70 | >0.80 (severe >0.85) |
| ESS / n | >70% | <50% |
| Trimming at α=0.10 | <10% | >20% (→ estimand drifts to ATO) |
| Recalibration ICI | <0.05, slope 0.9–1.1 | >0.08 or slope <0.85 |
| ΔAUROC vs source | <0.03 | >0.04 |

### 006 — B→R* titration + 9-cell plasmode + NC ladder

```r
# 006: Audit -> RR imputation locked
# Extract audit marginals + dispersion (Kaur/Khanna/Galib tables)
# Impute (p1,p0) per contrast:
#   Contrast A (irrational-FDC vs NLEM single): p1~0.15-0.25, p0~0.02 -> RR_EU~7.5-12
#   Contrast B (AYUSH-plus vs allopathy-only on LFT/ADR): p1=0.44-0.96, p0=0.10 -> RR_EU~4.4-9.6
# For B: B(p1,p0,RR_UD) = [p1*(RR_UD-1)+1]/[p0*(RR_UD-1)+1]; B_max = RR_EU*RR_UD/(RR_EU+RR_UD-1)
# For RR_obs from emulated trial (Hernán target-trial): E-value = RR_obs + sqrt(RR_obs*(RR_obs-1))
# Decision: Robust if E-value(RR_obs) > B_audit at sweep median; else fragile
# Fixed-point R*: solve E-value(R*)=B -> R* (report 1.4-2.3 typical)
# Titration contour: RR_UD 1.2->4.0 x (p1,p0) audit envelope -> B and R* curve
# 9-cell plasmode: 3 x P(U) = 0.10/0.44/0.96 x 3 x RR_UD = 1.5/2.0/3.0 with known RR_true=1 vs 1.5
#   Measure false-robust rate (RR_true=1 declared robust) <5% at calibrated R*
# NC ladder: pre-spec 2 NC outcomes per contrast; report RR_NC + E-value_NC; null RR_NC~1 supports robustness
```

**Titration table (locked, per 006 §Audit→RR):** Generic 35% excess R*1.4–1.6; Khanna 95% excess 1.7–2.0; Irr FDC 1.4–1.5; AYUSH 44% 1.4–1.7; AYUSH 96% 1.8–2.3; polypharmacy 1.5–1.7. Interpretation: RR_obs 1.2 never robust; 1.8–2.2 may survive typical but not extreme AYUSH.

---

## 7. Sample Size, Power & 9-Cell Plasmode

- **Plasmode:** 20k resampled × 4 grades × dual frameworks = 160k synthetic-like rows (no PHI); 9-cell calibration (3 P(U) × 3 RR_UD) each n=2000 simulated emulations → false-robust/power curves with Wilson 95% CI.
- **Proxy target (UKB-SA):** ~8k SA gives ±1% precision on BMI-monkey S-score; power to detect AUC 0.65 vs 0.70.
- **Equivalence power (005):** ΔAUROC <0.03 at ~80% power with n=2000 per grade (Riley 10.1136/bmj-2024-080749 bootstrap CI width).
- **006:** R* decision has no sample-size test — it is a threshold property; NC ladder power depends on NC event rate (trauma ~2% → 8k SA gives ~160 events, CI width ±40%).

---

## 8. Baselines & Comparisons (paired but distinct)

### 005 baselines
1. LR + recalibration (Platt / intercept+slope)
2. SOFA / QRISK3 / Framingham recalibrated (clinical score)
3. GBM/XGBoost tuned on source
4. IOPW + standardization + AIPW + calibration weighting
5. Overlap-weight ATO (Li JASA 10.1080/01621459.2018.1448823)

### 006 baselines
1. LR/Cox PH unadjusted vs IPTW (measured only)
2. SOFA/QRISK3-adjusted
3. GBM/IPTW-ML PS
4. **Unanchored generic E-value** (no audit) as comparator — anchoring should tighten bound (B_audit ≤ generic)
5. NC falsification panel (Lipsitch) as empirical baseline

---

## 9. Diagnostics — SMD / S-score / ESS / Trimming (SHARED LOCKED)

- **SMD:** |SMD|>0.1 per Austin 2009 10.1002/sim.3697; histogram + % violated per grade.
- **S-score overlap:** L1-logistic P(S=1|X) source vs proxy-target; report **AUC** (benign 0.62 → severe 0.85+), overlap coefficient, density plot, weight distribution quantiles.
- **ESS:** (Σw)²/Σw²; ESS/n collapse at G3 signals failure.
- **Trimming:** At α=0.05 and 0.10 (Lee 10.1371/journal.pone.0018174; Crump Biometrika; Li JASA), report trimming fraction, ATE vs ATO drift, bias-variance bias.
- **Calibration hierarchy (reused per shortlist):** Van Calster 10.1016/j.jclinepi.2015.12.005 (mean/slope/ICI) + Riley 10.1136/bmj-2024-080749 (bootstrap/CIs) → reported under TRIPOD+AI 10.1136/bmj-2023-078378.

---

## 10. Harmonization Map Stub (ricu / METRE / YAIB)

- **Source scaffold:** MIMIC-IV via `ricu` (R) and METRE/YAIB harmonized feature store (MIMIC-IV→OHDSI) — labs mapped to LOINC, meds to RxNorm, derived BMI/WC/HbA1c unified units.
- **Proxy/target:** UKB-SA field IDs (BMI 21001, HbA1c 30750, medication 20003, supplement 20084) mapped to MIMIC equivalents; CARRS field dictionary (pending DUA) stubbed to same codebook.
- **Audit corpus:** No harmonization needed — aggregate tables only.
- **Preprint watch (cross-dossier):** Patel 10.64898/2026.05.03.26352335 (YAIB/METRE) — monitor for harmonization drift; if YAIB updates South Asian mappings, re-run S-score diagnostics.

---

## 11. Leakage Checklist (6 items — locked, checked at each phase)

- [ ] No target outcome (HbA1c/CKD/ADR) used to engineer tilting weights
- [ ] No proxy-target rows in source training folds (source/target split locked before CV)
- [ ] Propensity S(X) trained without outcome Y
- [ ] Recalibration fitted only on proxy-target *training* fold (10-fold CV, held-out test for ICI)
- [ ] Plasmode Y-mechanism not used as feature
- [ ] NC outcomes excluded from main outcome model selection

---

## 12. TRIPOD+AI 27-Item Mapping (paired, 10.1136/bmj-2023-078378)

| Item | 005/006 handling |
|------|------------------|
| Title/Abstract | Transport + E-value plasmode distinction stated |
| Background | IMI-RHAPSODY / Anjana / MONO / WHO audit gaps cited |
| Objectives | 005: G0→G3 diagnostic dose-response; 006: audit→R* threshold |
| Data | MIMIC-IV (D), UKB-SA (B), CARRS/ICMR-INDIAB (B), audits (D) — timelines honest |
| Participants | Resampled MIMIC adultos; proxy UKB-SA SA subset; audit aggregates |
| Outcome | 005: ICI/slope/AUROC/DCA; 006: B vs E-value + R*+ NC |
| Predictors | BMI/WC/HbA1c/generic/AYUSH/S_visit as S-variables (selection diagram) |
| Sample size | 20k plasmode; 9-cell ×2k; UKB-SA 8k power noted |
| Missing data | S_visit censoring pre-registered as MNAR stress |
| Analysis | IOPW/AIPW/AIPW+calibration vs recalibration; B→R* titration |
| Risk groups | G0→G3 dose-response; MONO vs non-MONO subgroup |
| Model development | Tibshirani L1 for S-score; entropy balancing for tilting |
| Calibration | Van Calster + Riley hierarchy |
| Discrimination | AUROC + c-statistic |
| Clinical utility | DCA at 0.05/0.10/0.20 |
| Validation | UKB-SA proxy first; CARRS/ICMR-INDIAB staged |
| Results reporting | SMD/AUC/ESS/trimming curves + R* contour per grade |
| Limitations | P(U) arm-level imputed; RR_UD sweep not Indian-outcome-linked; NC transport |
| Ethics | De-identified MIMIC; UKB EGC; CARRS/ICMR DUA; CC-BY audits — no PHI beyond |
| Availability | Code + hashes + weights at OSF on Stage 1 acceptance |
| Funding | TBD |
| Supplementary | Tilting hashes + S_visit functions + NC outcome codelists |

---

## 13. Paired Submission Plan (staged, 1–3 mo proxy + 2–6 mo restricted)

| Phase | Duration | Dossiers active | Deliverable |
|-------|----------|-----------------|-------------|
| **Phase 1: Plasmode-only (D, weeks 1–2 scaffold + 6–8 weeks analysis)** | **6–8 weeks** (immediate) | 005+006 shared: tilting + S_visit + diagnostics pipeline + 9-cell + NC ladder piloted on MIMIC alone | **OSF Pre-reg (this) + code + G0→G3 diagnostic curves (SMD/AUC/ESS/trimming) + R* contour** — independently publishable as methods Registered Report |
| **Phase 2: UKB-SA RAP proxy (B, 1–3 mo wait + 4–6 weeks analysis)** | **4–6 weeks after UKB access** | 005: S-score validation on SA physiology; 006: AYUSH/generic proxy titration | **Proxy-target validation preprint:** S-score + recalibration-vs-AIPW on UKB-SA; R* survivorship on SA prescribing |
| **Phase 3: CARRS/ICMR-INDIAB restricted (B, 2–6 mo DUA + 6–8 weeks analysis)** | **6–8 weeks after data receipt** | 005: national/rural re-tilt (Tripura 56.7% MONO); 006: prescribing footprints → refined P(U), NC validation longitudinal | **Restricted-target extension:** graded rural vs urban diagnostic extension |

**Paired economy:** One plasmode engineering sprint serves both papers; diagnostic curves (SMD/AUC/ESS) are shared figure panels; audit corpus extraction done once. Two preprints converge to two papers but share first-author engineering credit.

**Authors / contributorship:** clinical-evidence-scout (India relevance, audits) + methods-scout (plasmode, weighting) paired; physician validator TBD for HbA1c/generic plausibility.

---

## 14. Ethics, Privacy & Limitations

- **MIMIC-IV:** HIPAA Safe Harbor, PhysioNet credentialed, IRB exemption for de-identified secondary analysis.
- **UKB-SA:** UKB EGC, RAP cloud, PI sign-off — no download beyond extracts.
- **CARRS/ICMR-INDIAB:** PHFI/Emory + ICMR-NIE/MDRF DUAs, de-identified extracts, ICMR ethics.
- **Audits:** Aggregate prescription-level, CC-BY, no identifiers.
- **Limitations to report:** Audit prevalences are marginal not arm-level (p1–p0 imputed via shift-gradient, bracketed); RR_UD for AYUSH/FDC not Indian-outcome-linked (sweep); US NCs (trauma) may not transport to Indian trauma admission patterns; UKB-SA is diaspora not India-resident proxy.

---

## 15. Verbatim Searches for this OSF (append to literature/search_log.csv)

See dossiers candidate_005/006 — this OSF adds 0 new concept searches (reuses audit + MONO + WHO sweeps); searches logged at dossier level. OSF locks G0→G3 table as pre-registered truth.
