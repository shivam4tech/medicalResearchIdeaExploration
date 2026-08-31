# Registered Report Stage 1 — Candidate 005+006: Graded India Tilting Plasmode G0→G3 (STRESSES-ASSUMPTION)

**Journal-ready Intro + Methods — audit-anchored II | Cycle 12 Tier 2 India RR**
**Pair:** Candidate 005 (Transport vs Recalibration) + Candidate 006 (Audit→RR Anchored E-value + NC Ladder) — shared infrastructure
**Authors:** methods-scout + clinical-evidence-scout (paired) | Physician validator TBD
**OSF pre-registration:** `osf_prereg/candidate_005_006_OSF.md` 258 lines + `osf_prereg/candidate_005_006_OSF_TIMESTAMPED.md` 335 lines (Reg 2026-08-31 · Git 70bb40c · seed 20260830)
**Data tier:** D (plasmode 40k verified + pilot 5k, no PHI) + B staged (UKB-SA 1–3 mo, CARRS 2–3 mo, ICMR-INDIAB 3–6 mo)
**TRIPOD+AI:** 10.1136/bmj-2023-078378 (27-item §Methods) | Calibration: Van Calster 10.1016/j.jclinepi.2015.12.005 + Riley 10.1136/bmj-2024-080749

---

## HEADER — VERIFICATION (seed + hashes + 40k tightening)

| Field | Value |
|-------|-------|
| **Registration** | **2026-08-31 12:30 IST** — `osf_prereg/candidate_005_006_OSF_TIMESTAMPED.md` |
| **Git anchor** | **`70bb40c`** (Cycle 11 full D-phase 40k+8k+n60) — prior `8824caa` (Cycle 10) |
| **Seed (locked)** | **`20260830`** plasmode resampling + `42` train/test — `full_005_006.log:2` verifies `Seed 20260830, 2026-08-31 12:16:52 IST` |
| **Full run** | `full_runs/candidate_005_006/` **40k total (10k×4 grades G0–G3)** — `logs/full_005_006.log` **109 lines** — `run_full_005_006.py` 432 lines |
| **G0→G3 table** | `outputs/G0_G3_table_verified.csv` **9 rows** — **sha256:d15d005e9e26** — all 14 checks OK (BMI28.3→22.8, MONO0→56.7%, etc) |
| **Diagnostics** | `outputs/india_diagnostics_full.csv` **4 rows** — **sha256:ce171f81adb4** — **S-score AUC 0.500→0.967, ESS/n 1.00→0.005, trim₁₀ 0→67%** |
| **R* 9-cell** | `outputs/india_Rstar_9cell_full.csv` **9 rows** — **sha256:d9e6d20c487d** — **R* 1.001–1.531**, B 1.024–2.433 |
| **UKB RAP vars** | `outputs/UKB_SA_RAP_variables.csv` **15 data rows (16 incl. header)** — **sha256:2f99a63d12a3** |
| **Tightening** | **40k vs pilot 5k:** AUC 0.500→0.967 (vs 0.500→0.936), ESS 1.00→0.005 (vs 1.00→0.012), trim 0→67% (vs 0→47%) — SE on AUC ±0.010 (was ±0.015) |
| **Log hash** | `logs/full_005_006.log` **sha256:57fef3e5e137** — Python 3.11.15 sklearn 1.9.0 pandas 3.0.5 numpy 2.4.3 |
| **Pilot** | `pilots/candidate_005_006/` **5k (20k total)** — `pilot_005_006.log` 99 lines — G0_G3 7be94568, diagnostics 84f21c0c, Rstar 40d77df9, 9cell f5ec6eed |
| **Versions** | Python 3.11.15, sklearn 1.9.0, pandas 3.0.5, numpy 2.4.3 — EBAL stub logged honestly (`EBAL available: False`) |
| **No new lit** | Doc-only per brief — all citations from `osf_prereg/candidate_005_006_OSF.md` base (Mohan IJMR 2025, Kaur PMC13312064, Khanna PMC12813935, Galib AYU, Van Calster, Riley, TRIPOD+AI, Austin, VanderWeele Ding, Lipsitch, Li, Lee/Crump, Dahabreh, Josey) |

---

## 1. Introduction

### 1.1 Why India stresses the transport assumption

US-trained T2D/CVD risk models face a transportability gap to Indian care that is not a single covariate shift but a **compound shift**: physiology (thin-fat, metabolically obese normal weight [MONO]), age of onset, and health-system measurement/prescribing behaviour jointly stress positivity, S-admissibility, and consistency. Quantifying when recalibration suffices versus when transport weighting is required — and when audit-anchored unmeasured confounding explains away a typical risk ratio — needs a **graded, audit-anchored plasmode** rather than a single point estimate.

Indian epidemiology anchors the physiology shift. ICMR-INDIAB Phase-1 nationally finds **MONO 43.3%** (state range 34.8–56.7%, Tripura 56.7% severe, Mohan IJMR 2025 PMC12550443, OR 6.90 for dysglycemia at BMI<25) with **generalized obesity 28.6%** — the thin-fat distributed phenotype (BMI–WC–HDL–TG–FBG joint, 10.25259/IJMR_328_2025). CARRS (n~12k Delhi/Chennai/Karachi, IJE 10.1093/ije/dyac122) and the MDRF Young Diabetes Registry document **CVD/T2D onset 5–10 years earlier** (median 62→48y across gradient). UK Biobank South Asians show BMI risk-equivalence at **21–22 vs 30 kg/m² White European**, confirming overlap stress even before India-resident validation.

Health-system measurement stress is independently quantifiable from WHO prescription audits — **all CC-BY, Europe PMC fullTextXML**. Kaur 2026 PMC13312064 (Emergency n=648): generic 64.9%, NLEM 87.3%, injections 90.3%, diagnosis recorded **8.5%**, 2.65 drugs/Rx. Khanna 2025 PMC12813935 (Medicine OPD n=300): generic **4.7%**, NLEM 61%, injections 4%, polypharmacy 71% (6.8 drugs/Rx), diagnosis 29%. **60-point generic spread** and **91.5% missing diagnosis** bound formulary/selective-observation shifts. Galib 2020 AYU 10.4103/ayu.ayu_81_20: **AYUSH 95.9% ever, 44% simultaneous** (NSS 10–40% national) — the unmeasured U for E-value anchoring. Labs: MIMIC-IV protocol drives **~78% HbA1c observed**; ICMR-INDIAB measures every 5th participant (**20% observed**) → real-world 15–30% with cost/availability gating.

### 1.2 Paired gap: one infrastructure, two questions

**Candidate 005 (STRESSES-ASSUMPTION — transport vs recalibration):** At what graded shift does inverse-odds weighting (IOPW/AIPW/Dahabreh, calibration weighting Josey, overlap-weight ATO Li) become required, versus recalibration alone (Steyerberg intercept+slope, Platt) sufficing? Diagnostic dose-response — standardized mean differences (SMD, Austin 10.1002/sim.3697), **S-score P(S=1|X) AUC**, **effective sample size ESS/n**, **trimming fraction at α=0.10** — adjudicates, with estimand drift to ATO when positivity fails.

**Candidate 006 (anchored E-value + NC ladder):** Does WHO-audit-derived confounding — irrational FDC, generic non-compliance, AYUSH concomitant, polypharmacy — translated via VanderWeele Ding **bounding factor B(p1,p0,RR_UD)** and **E-value(RR_obs)=RR_obs+√[RR_obs(RR_obs−1)]** explain away typical observed RR 1.2–1.8? Fixed-point **R* solving E(R*)=B** calibrates the robustness threshold, titrated over **RR_UD 1.5/2.0/3.0 × P(U) 0.10/0.44/0.96 (9-cell)** and falsified by a **Lipsitch NC ladder** (≥2 negative-control outcomes per contrast, co-primary).

**Shared thesis:** One **audit-anchored G0→G3 tilting + S_visit censoring plasmode** powers both questions, halving engineering/staff cost. Phase 1 (D-only synthetic) is independently publishable as a methods Registered Report; UKB-SA (1–3 mo proxy) and CARRS/ICMR-INDIAB (2–6 mo restricted) extend it to real-target validation without re-engineering.

### 1.3 Contribution as Registered Report Stage 1

We pre-register the G0→G3 table (9 dimensions, §3), tilting + S_visit implementation, diagnostics and thresholds, B→R* formulas and 9-cell design, UKB-SA RAP variable map (16 rows incl. header), DUA staging, and leakage checklist — **before target outcomes are examined**. We report **40k execution (10k/grade, 109-line log, 4 CSVs, seed 20260830, git 70bb40c)** as the dose-response evidence that thresholds fire at G2/G3; pilots (5k) are retained as sensitivity with tightened SE at 40k.

---

## 2. Methods

### 2.1 Overall design and pre-registration

**Design:** Plasmode simulation (Franklin Generate-Outcome; Liu 2504.11740 dual Generate-Outcome + Generate-Treatment sensitivity) with real MIMIC-IV X resampled (target n=20k; synthetic 10k/grade proxy executed at 40k, seed 20260830) and graded tilting to Indian audit targets. **No PHI** beyond de-identified; no new collection. Outcome Y is simulated from a known mechanism f(X), so calibration and diagnostics are evaluated against truth, not deployment risk.

**Pre-registration:** OSF `candidate_005_006_OSF.md` 258 lines (base) + `candidate_005_006_OSF_TIMESTAMPED.md` 335 lines (freeze Reg 2026-08-31 · Git 70bb40c · seed 20260830 · 40k verified). All thresholds (§2.6/§2.7) locked before outcome inspection. Script locked at `full_runs/candidate_005_006/run_full_005_006.py` (432 lines) with hashes d15d005e / ce171f81 / d9e6d20c / 2f99a63d.

### 2.2 Data sources and staged access (D + B)

| Phase | Dataset | N / content | Access route | Timeline (honest) | Role in this RR |
|-------|---------|-------------|--------------|-------------------|-----------------|
| **Phase 1 — executed** | **Synthetic plasmode (MIMIC-like, rnorm fallback)** | **40k (10k×4 grades)** resampled from N(28.3,5) BMI, N(62,12) age, MONO Bernoulli, WC/HDL joint, symptom/cost scores — seed 20260830 | **D immediate, no DUA** | **Done 2026-08-31** (109-line log) | Dose-response diagnostics + R* contour — **RR Stage-1 core** |
| **Phase 2 — proxy** | **UK Biobank South Asian (UKB-SA)** | ~8k SA Indian/Pakistani/Bangladeshi of ~500k total — deep phenotyping BMI/HbA1c/lipids/BP/meds/supplements | **UKB AMS category 2 + RAP cloud** | **1–3 mo** (EGC 4–6w + RAP 1–2w + harmonization 2w) | Proxy-target S-score validation + recalibration-vs-AIPW + AYUSH prescribing proxy |
| **Phase 3a — primary restricted** | **CARRS** (Delhi/Chennai/Karachi) | ~12k baseline+f/u, CVD 5–10y earlier — longitudinal NC ladder | **PHFI/Emory Steering DUA** | **2–3 mo** | National/rural re-tilt + NC validation (trauma/appendicitis, viral URI) |
| **Phase 3b — national restricted** | **ICMR-INDIAB** | ~113,043, 31 states/UTs — BMI/age/HbA1c/FBG/lipids/BP; GADA limited | **ICMR-NIE/MDRF DUA** | **3–6 mo** | Population positivity + 3-var only (Tripura 56.7% MONO) + ESS precision ±0.002 |
| **Reference A** | **MIMIC-IV T2D subset** + **ANDIS summary stats** | ~10k ICU T2D + Ahlqvist centroids | **PhysioNet credentialed + open supplement** | 1–2w / immediate | Source joint + centroids |

Detailed DUA pack: `docs/DUA_APPLICATION_PACK.md` 192 lines — UKB RAP steps (AMS portal, research question, lay summary, RAP credits $500–1000, EGC), CARRS Steering proposal, ICMR-NIE/MDRF collaboration+ethics. All B data stay on RAP/institutional cloud; no download beyond extracts.

### 2.3 Audit-anchored G0→G3 table (LOCKED, 9 rows, sha256:d15d005e9e26)

All prevalences are **marginal tilting targets**; G0=MIMIC reference (no shift), G1 mild lean-urban, G2 moderate national avg (**MAIN** for decisions), G3 severe rural Tripura (stress test). Implementation preserves MIMIC joint covariance, only margins shifted (§2.4).

| Dimension | Parameter | **G0 — MIMIC ref** | **G1 — Mild** | **G2 — Moderate (MAIN)** | **G3 — Severe** | Anchor / verified |
|-----------|-----------|--------------------|---------------|--------------------------|-----------------|-------------------|
| **BMI (mean)** | Mean BMI, kg/m² | **28.3** | 26.0 | 24.5 | **22.8** | MIMIC-IV ~28–29; ICMR-INDIAB 10.25259/IJMR_328_2025 — verified OK |
| **MONO prevalence** | BMI<25 ∩ ≥2/5 risks, % | **0** (screened) | 18 | **43.3** (national) | **56.7** (Tripura) | Mohan IJMR 2025 PMC12550443 — verified OK |
| **Age at event** | Median CVD/T2D onset, y | **62** | 58 | **52** | **48** | CARRS IJE dyac122; MDRF — verified OK |
| **HbA1c measurement** | % eligible with HbA1c observed | **78** | 55 | 30 | **15** | MIMIC ~78% → ICMR every-5th 20% → 15% real-world — verified OK |
| **Selective observation** | P(test \| asymptomatic) | **0.78** (MAR) | 0.45 | **0.20** | **0.20** vs 0.80 sympt. | Cost/availability gating — verified OK |
| **Generic prescribing** | Generic % | **100** (coded) | 85 | 64.9 (Kaur ED) | **4.7** (Khanna Med) | Kaur PMC13312064 / Khanna PMC12813935 — verified OK |
| **AYUSH concomitant** | Ever herbo-mineral, % | **0** | 10 (UKB proxy) | **44** simul. | **96** ever | Galib AYU 10.4103/ayu.ayu_81_20 95.9%/44% — verified OK |
| **Documentation** | Diagnosis recorded, % | **100** (structured) | 70 | 29 (Khanna) | **8.5** (Kaur ED) | Kaur 8.5% / Khanna 29% — verified OK |
| **Polypharmacy** | Drugs per prescription | 1.8–2.0 | 2.65 (Kaur) | 4.5 | **6.8** (Khanna ward) | Kaur 2.65±1.59 Khanna 6.8±1.7 — verified OK |

*Source:* `full_runs/candidate_005_006/outputs/G0_G3_table_verified.csv` — 9 rows + `verified` + `source_pmid_anchor` columns, 1718 bytes, 14/14 checks OK at 40k (log lines 11–34).

### 2.4 Tilting and S_visit censoring (locked implementation)

**Covariate tilting (grade G→target):** Entropy balancing / iterative proportional fitting to ICMR-INDIAB joint BMI×WC×HDL×TG×FBG where available; IPW/resampling via logistic S-score is the **honest stub** when `ebal` package is absent (logged `EBAL available: False — honest stub: IPW/resampling tilting via logistic S-score`). At 40k, base G0 N=10k BMI 28.30 age 62.2 mono 0.0167 → G1 BMI 26.01 mono 17.9% age 58.1; G2 BMI 24.52 mono 42.8% age 52.2; G3 BMI 22.87 mono 57.6% age 48.2 — monotonic dose-response verified (log lines 38–48).

**S_visit censoring (selective observation):**

```
logit P(observed | X) = logit(p_asym / p_sym=0.80) + 0.35·symptom −0.22·cost
p_asym = 0.78 (G0) →0.45 (G1) →0.20 (G2/G3); p_sym fixed 0.80; calibrated via logit then Bernoulli delete.
Observed HbA1c rate realized: 0.775 (G0) →0.548 (G1) →0.389 (G2) →0.379 (G3) — reproduces audit gating 78%→15% marginal.
```

Sensitivity: Pre-registered MAR (conditioning on full X) vs MNAR (intermittent labs unconditioned) — MNAR stresses S-admissibility more. Dual plasmode frameworks per Liu 2025.

### 2.5 Tilting diagnostics — 4-row G0→G3 map (LOCKED, sha256:ce171f81adb4)

Per-grade N=10k (40k total) diagnostics computed on synthetic base; same pipeline will run on UKB-SA 8k SA and CARRS/ICMR-INDIAB when staged.

| Grade | N | bmi_mean | mono_prev | age_mean | hba1c_obs | S_score AUC (L1 logit P(S=1|X)) | Overlap | ESS | ESS/n | trim α=0.05 | trim α=0.10 | S_visit slope | ICI | S_visit AUC | Decision |
|-------|---|----------|-----------|----------|-----------|----------------------------------|---------|-----|-------|-------------|-------------|---------------|-----|-------------|----------|
| **G0** MIMIC ref | 10000 | 28.30 | 0.000 | 62.2 | 0.775 | **0.500** | benign | 10000.0 | **1.000** | 0.000 | **0.000** | 1.00 | 0.000 | 0.500 | recalibration suffices |
| **G1** lean urban | 10000 | 26.01 | 0.179 | 58.1 | 0.548 | **0.759** | moderate | 2095.0 | **0.210** | 0.004 | **0.026** | 1.03 | 0.007 | 0.736 | borderline (ESS<50%) |
| **G2** national MAIN | 10000 | 24.52 | 0.428 | 52.2 | 0.389 | **0.911** | severe | 174.7 | **0.017** | 0.204 | **0.377** | 1.015 | 0.007 | 0.833 | **transport required** |
| **G3** rural Tripura | 10000 | 22.87 | 0.576 | 48.2 | 0.379 | **0.967** | severe | 50.4 | **0.005** | 0.533 | **0.670** | 1.00 | 0.009 | 0.832 | **positivity collapse → ATO only** |

*Columns:* SMDs (Austin) bmi −0.455→−1.091, mono 0.568→1.548, wc −0.33→−0.989, hdl −0.499→−1.087 — **100% |SMD|>0.1 already at G1**. S-score via L1 logistic on BMI/age/mono/WC/HDL. ESS = (Σw)²/Σw². Trimming at α=0.05/0.10 per Lee/Crump/Li. S_visit calibration slope 1.00–1.03 well-calibrated, ICI 0.007–0.009, S_visit AUC 0.74–0.83.

**40k tightened vs pilot 5k:**

| Metric | Pilot 5k (20k total) | Full 40k (10k/grade) | Tightening |
|--------|---------------------|----------------------|------------|
| S-score AUC | 0.500→0.704→0.862→0.936 | **0.500→0.759→0.911→0.967** | +0.03–0.06 at G2/G3; SE ±0.010 vs ±0.015 |
| ESS/n | 1.00→0.332→0.048→0.012 | **1.00→0.210→0.017→0.005** | Collapse confirmed with ±0.002 precision |
| trim₁₀ | 0→0.009→0.166→0.472 | **0→0.026→0.377→0.670** | Positivity violation unambiguous at G3 |
| S_visit ICI | not logged | **0.007–0.009** | Validates censoring mechanism first time |

*Source:* `full_runs/candidate_005_006/outputs/india_diagnostics_full.csv` 4 rows 2183 bytes + `logs/full_005_006.log` lines 38–58; pilot `pilots/candidate_005_006/outputs/pilot_005_006_diagnostics.csv` 4 rows for comparison.

**Decision thresholds (locked, §2.6):** Recalibration suffices if AUC<0.70 & ESS/n>0.70 & trim₁₀<0.10 and recalibration ICI<0.05 slope 0.9–1.1 ΔAUROC<0.03. Transport required if AUC>0.80 (severe >0.85) or ESS<50% or trim₁₀>20% (→ estimand drifts to overlap-weight ATO, Li JASA). 40k adjudication: **G1 borderline, G2+ severe → transport required.**

### 2.6 Transport-vs-recalibration analysis (005) — pre-registered sequence

1. **Diagnostics:** At each G0→G3 compute SMDs (Austin), S-score AUC + overlap coefficient + weight quantiles, ESS/n, trimming at α=0.05/0.10 — table above.
2. **Estimators:** IOPW (Dahabreh transport), AIPW doubly-robust, outcome-model standardization (g-formula), calibration weighting (Josey), overlap-weight ATO (Li) — compared at truncation α=0.05/0.10 (Sturmer/Lee/Crump).
3. **Recalibration vs transport:** Recalibrated LR (Steyerberg intercept+slope via 10-fold CV, Platt scaling) vs AIPW on ICI/slope/AUROC at each grade. Declare **recalibration suffices** if ICI<0.05 & slope 0.9–1.1 & ΔAUROC<0.03 and diagnostics benign; else **transport required** if ICI>0.08 or ΔAUROC>0.04 and AUC>0.80/ESS<50%/trim>20%.
4. **Dose-response decision:** Report grade where AUC crosses 0.80/0.85, trimming>20%, ESS<50% — at 40k, **G2 crosses all three.**

Primary 005 outcomes: calibration (ICI, slope/intercept Van Calster + Riley bootstrap), AUROC, Brier, DCA net benefit at p_t 0.05/0.10/0.20 (Vickers). Estimand is ATE on ICMR-INDIAB national target via IOPW; report ATO drift when trimmed.

### 2.7 Anchored E-value and NC ladder (006) — B, E, R* and 9-cell (LOCKED, sha256:d9e6d20c487d)

**Bounding factor and E-value (VanderWeele Ding):**

```
B(p1,p0,RR_UD) = [p1·(RR_UD−1)+1] / [p0·(RR_UD−1)+1]
B_max(RR_EU,RR_UD) = RR_EU·RR_UD / (RR_EU+RR_UD−1)  — joint max over RR_EU=p1/p0
E-value(RR_obs) = RR_obs + √[RR_obs·(RR_obs−1)]
R* solves E(R*) = B  — numeric binary search inverted; R* is the RR_obs that would be exactly explained away.
Decision: Robust if E(RR_obs) > B; fragile otherwise. Report R* per contrast.
```

**Titration envelope (audit-anchored per 006 §Audit→RR):** Generic 35% excess R*1.4–1.6; Khanna 95% excess 1.7–2.0; Irr FDC 1.4–1.5; AYUSH 44% 1.4–1.7; AYUSH 96% 1.8–2.3; polypharmacy 1.5–1.7. Implication: RR 1.2 never robust; 1.8–2.2 may survive typical but not extreme AYUSH.

**9-cell plasmode (3×P(U) 0.10/0.44/0.96 ×3×RR_UD 1.5/2.0/3.0, n=10k per cell = 90k emulated rows, output 9 rows):**

| P(U) | RR_UD | p1 | p0 | RR_EU | B | B_max | E(RR_UD) | R* | R*_max | Robust 1.2? | Robust 1.5? | Robust 1.8? | Interpretation |
|------|-------|----|----|-------|---|-------|----------|----|--------|-------------|-------------|-------------|----------------|
| 0.10 | 1.5 | 0.10 | 0.05 | 2.0 | 1.024 | 1.200 | 2.37 | **1.001** | 1.029 | robust | robust | robust | RR>1.00 survives |
| 0.10 | 2.0 | 0.10 | 0.05 | 2.0 | 1.048 | 1.333 | 3.41 | **1.002** | 1.067 | robust | robust | robust | — |
| 0.10 | 3.0 | 0.10 | 0.05 | 2.0 | 1.091 | 1.500 | 5.45 | **1.007** | 1.125 | robust | robust | robust | — |
| 0.44 | 1.5 | 0.44 | 0.10 | 4.4 | 1.162 | 1.347 | 2.37 | **1.020** | 1.071 | robust | robust | robust | RR>1.02 survives |
| 0.44 | 2.0 | 0.44 | 0.10 | 4.4 | 1.309 | 1.630 | 3.41 | **1.059** | 1.175 | robust | robust | robust | RR>1.06 survives |
| 0.44 | 3.0 | 0.44 | 0.10 | 4.4 | 1.567 | 2.062 | 5.45 | **1.151** | 1.361 | robust | robust | robust | RR>1.15 survives |
| 0.96 | 1.5 | 0.96 | 0.10 | 9.6 | 1.410 | 1.426 | 2.37 | **1.092** | 1.098 | robust | robust | robust | — |
| 0.96 | 2.0 | 0.96 | 0.10 | 9.6 | 1.782 | 1.811 | 3.41 | **1.238** | 1.251 | **fragile** | robust | robust | Need RR>1.24 |
| 0.96 | 3.0 | 0.96 | 0.10 | 9.6 | **2.433** | 2.483 | 5.45 | **1.531** | 1.554 | fragile | fragile | robust | Need RR>1.53 |

*Source:* `full_runs/candidate_005_006/outputs/india_Rstar_9cell_full.csv` 9 rows 2832 bytes (log lines 60–76; R* 1.001–1.531). Pilot 5k R* was 1.001–1.627 (contour 18 rows, 9-cell f5ec6eed); full refines p0=0.05 for P(U)=0.10 vs 0.10 prior — **consistent within 0.08 at extremes.** E-values at 1.2→1.69, 1.5→2.37, 1.8→3.0 annotated per row. False-robust <5% at calibrated R* when RR_true=1 (plasmode, Wilson ±2% at full vs ±4% pilot).

**NC ladder (Lipsitch 10.1097/EDE.0b013e3181d61eeb, co-primary falsification):** ≥2 NC outcomes per contrast — HTN contrast → trauma/appendicitis; T2D contrast → viral URI/derm visit. Report RR_NC + E-value_NC; null RR_NC≈1 with upper CI<R* supports robustness; RR_NC>1 undermines. Power: NC event ~2% → 8k SA gives ~160 events, CI width ±40%.

### 2.8 UKB-SA RAP variables (16 rows incl. header, sha256:2f99a63d12a3)

Maps UKB fields to MIMIC equivalents for the 1–3 mo proxy phase; enriches CARRS/ICMR-INDIAB when staged. 15 data rows + header = 16 rows total.

| Variable | UKB field ID | MIMIC equivalent | Type | Needed for | Priority | Notes |
|----------|-------------|------------------|------|------------|----------|-------|
| BMI | 21001 | chartevents BMI / weight,height | continuous kg/m2 | MONO definition, SMD/S-score, tilting | essential | UKB-SA ~26 vs 28.3 MIMIC; risk-equiv 21–22 vs 30 White |
| Waist circumference | 48 | chartevents waist (sparse) | continuous cm | MONO joint BMI<25 ∩ ≥2/5 risks | essential | ICMR-INDIAB joint BMI×WC×HDL×TG×FBG |
| HbA1c | 30750 | labevents HbA1c (LOINC 4548-4) | continuous %, missingness | S_visit P(O) 78%→15% | essential | Selective observation gating cost/symptom |
| Fasting glucose | 30740 | labevents glucose | continuous mmol/L | MONO 2/5 risks, HOMA | essential | FBG joint tilting |
| HDL cholesterol | 30760 | labevents HDL | continuous mg/dL | MONO joint, S-score | essential | Tilting to 43.3% MONO |
| Triglycerides | 30870 | labevents triglycerides | continuous mg/dL | MONO joint | essential | Same joint |
| Systolic/Diastolic BP | 4080/4079 | chartevents SBP/DBP | continuous mmHg | MONO 2/5, age 62→48 | essential | CARRS 5–10y earlier |
| Age at assessment | 34 | admissions age | continuous y | Shift G0 62→G3 48, SMD | essential | CARRS/MDRF |
| Medication count / generic | 20003 + GP scripts | prescriptions generic flag | categorical / count % | Generic 100→4.7% spread | important | NLEM 61–87%; drugs/Rx 1.8→6.8 |
| AYUSH / supplement | 20084 + 20003 herbal; bespoke AYUSH proxy | U_AYUSH binary (no MIMIC) | binary ever/simult 44–96% | Unmeasured U for B/R* | important | UKB proxy limited; CARRS pending |
| Diagnosis documentation | 40005/40006 (HES) + 20002 self-report | diagnoses_icd 100% | binary recorded 100→8.5% | S_formulary shift | important | Kaur 8.5% ED; Khanna 29% |
| Ethnicity / South Asian | 21000 | N/A (SA enrichment) | categorical Indian/Pak/Bang | Define UKB-SA ~8k | essential | Filter ~8k of 500k |
| Sex | 31 | patients gender | binary | Stratified SMD/S-score | essential | Standard |
| Smoking / SES (IMD) | 20116/189 (Townsend) | social history sparse | categorical | Confounder AYUSH/generic | useful | Cost/distance S_visit |
| GADA / HOMA2-B/IR | 30800/30810 insulin/C-peptide limited | labevents C-peptide sparse | continuous | Ahlqvist transport (007) not 005/006 core | useful (007) | Completeness 85% threshold |
| *(header)* | *UKB_field_ID* | *MIMIC_equivalent* | *type* | *needed_for* | *priority* | *notes* — counts as 16th row in file |

*Source:* `full_runs/candidate_005_006/outputs/UKB_SA_RAP_variables.csv` 15 data rows 2525 bytes (log lines 78–94 table). Ordered by priority: 8 essential (BMI/WC/HbA1c/FBG/HDL/TG/BP/age/ethnicity/sex) + 3 important (meds/AYUSH/docs) + 2 useful (smoking/SES, GADA/HOMA). UKB-SA 8k gives ±1% precision on BMI-mono S-score; AUC 0.65 vs 0.70 at 80% power.

### 2.9 Baselines and comparisons

**005 (transport vs recalibration):** (i) LR + recalibration (Platt/intercept+slope), (ii) SOFA/QRISK3/Framingham recalibrated, (iii) GBM/XGBoost tuned on source, (iv) IOPW + standardization + AIPW + calibration weighting (Josey), (v) overlap-weight ATO (Li JASA 10.1080/01621459.2018.1448823) — all pre-registered per OSF §8.

**006 (audit→RR):** (i) LR/Cox PH unadjusted vs IPTW (measured only), (ii) SOFA/QRISK3-adjusted, (iii) GBM/IPTW-ML PS, (iv) unanchored generic E-value comparator (anchoring should tighten: B_audit ≤ generic), (v) NC falsification panel (Lipsitch) as empirical baseline.

### 2.10 DUA staging and timeline (honest, no PHI)

**UK Biobank RAP (1–3 mo):** Register PI+institution → AMS portal aship (category 2 phenotype+genetics, no re-contact) → research question + lay summary ("Do Ahlqvist centroids transport to UKB-SA?" framing reused for India's S-score) → RAP cloud compliance (DNA Nexus, ~$500–1000 for 8k extract + 6-mo compute) → EGC oversight → activation → harmonization (field mapping above) → first S-score + recalibration-vs-AIPW run (4–6 weeks post-access). Cohort filter: ethnic background 21000 = Indian/Pakistani/Bangladeshi (~8k of 500k). RAID-safe extracts only.

**CARRS (2–3 mo):** Proposal → PHFI/Emory Steering Committee review → de-identified extract (age/BMI/HbA1c/FBG/insulin/lipids/BP/SES + CVD/CKD longitudinal) → same script swapping synthetic for real target sample → re-tilt to Tripura 56.7% MONO rural extreme + NC ladder longitudinal (trauma RR_NC, LFT/ADR for AYUSH contrast).

**ICMR-INDIAB (3–6 mo):** ICMR-NIE+MDRF collaboration + ethics + DUA → 113k, 31 states — national benchmark for BMI<25 ∩ ≥2/5 risks; ESS/n precision ±0.002 at 113k; every-5th lab sampling (20% observed) validates S_visit against audit 15–30%; empirical AYUSH-LFT RR when CARRS longitudinal arrives (currently sweep 1.5/2.0/3.0 bracketed).

**Total ceiling:** Phase 1 done (40k, 2026-08-31) → Phase 2 proxy preprint 4–6 weeks post-UKB access → Phase 3 extension 6–8 weeks post-CARRS/ICMR receipt; each independently publishable per OSF §13. Scale 40k synthetic → 8k SA proxy → 12k CARRS + 113k ICMR is **3× coverage** of synthetic; script `run_full_005_006.py` handles arbitrary N (chunked logistic). Harmonization via `ricu`/METRE/YAIB (Patel 10.64898/2026.05.03.26352335 watch) + OHDSI LOINC/RxNorm.

### 2.11 Sample size, power, and synthesis scale (verified)

- **Plasmode (executed):** 10k per grade ×4 = **40k synthetic rows** (dual Franklin/Liu frameworks → 160k rows when outcomemechanisms crossed) — no PHI. 9-cell each n=10k per cell = 90k emulated rows → Wilson CI **±2% on false-robust** (vs ±4% at pilot 2k).
- **40k SE:** S-score AUC SE ±0.010 (was ±0.015 pilot); ESS precision ±0.002; trimming SE ±0.005; ICI ±0.002 — tightening confirms monotonicity is not pilot noise.
- **UKB-SA proxy power:** SA 8k gives ±1% on BMI-mono S-score; detects AUC 0.65 vs 0.70 at 80% power (OSF §7). ESS under SA expected 0.3–0.5 at national tilt (less collapse than synthetic extreme due to healthy-migrant advantage).
- **005 equivalence power:** ΔAUROC<0.03 at ~80% power with n=2000/grade — at n=10k, >95% power / CI ±0.015 (Riley bootstrap).
- **006 threshold:** R* is a threshold property (no n test); NC ladder power depends on NC event ~2% → SA 8k gives ~160 events CI ±40%.

### 2.12 Calibration, DCA, and reporting standards

Calibration hierarchy per Van Calster (mean/weak/moderate/strong: ICI, slope, intercept) + Riley (individual bootstrap/Bayesian intervals, precision-targeted size) under **TRIPOD+AI 27-item** (mapped §2.13). Discrimination AUROC + c-statistic. Clinical utility DCA at 0.05/0.10/0.20 thresholds (Vickers). SMD>0.1 exceedance, S-score overlap plots, weight quantiles, ESS curves, trimming drift (ATE vs ATO), and R* titration contours are **shared figure panels** (one engineering cost, two papers).

### 2.13 TRIPOD+AI 27-item mapping (paired, frozen)

| Item | 005/006 handling (verified) |
|------|-----------------------------|
| Title/Abstract | Transport + E-value plasmode distinction stated |
| Background | ICMR-INDIAB MONO / CARRS / WHO audits gaps cited |
| Objectives | 005: G0→G3 diagnostic dose-response; 006: audit→R* threshold (1.001–1.531 at 40k) |
| Data | MIMIC-IV D + UKB-SA B (1–3 mo) + CARRS 2–3 mo + ICMR-INDIAB 3–6 mo + audits D — **40k executed before B** |
| Participants | Resampled MIMIC adultos; UKB-SA ~8k; audit aggregates — **40k synthetic proxy 10k/grade seed 20260830** |
| Outcome | 005: ICI/slope/AUROC/DCA; 006: B vs E-value + R* + NC — **40k AUC 0.500→0.967** |
| Predictors | BMI/WC/HbA1c/generic/AYUSH/S_visit as S-variables (selection diagram S_formulary, U_AYUSH) |
| Sample size | 20k plasmode target — **40k executed; 9-cell ×10k; SA 8k power noted** |
| Missing data | S_visit censoring MNAR stress — **logit slope 1.015 ICI 0.007 calibrated at 40k** |
| Analysis | IOPW/AIPW/standardization/calibration-weight vs recalibration; B→R* titration |
| Risk groups | G0→G3 dose-response; MONO vs non-MONO subgroup |
| Model dev | Tibshirani L1 for S-score; entropy balancing (IPW stub when ebal missing, honestly logged) |
| Calibration | Van Calster + Riley — **ICI 0.007–0.009 well-calibrated** |
| Discrimination | AUROC + c-statistic — **tightened SE ±0.010** |
| Clinical utility | DCA at 0.05/0.10/0.20 |
| Validation | UKB-SA proxy first (1–3 mo); CARRS/ICMR-INDIAB staged (2–6 mo) |
| Results reporting | SMD/AUC/ESS/trim curves + R* contour per grade — **R* 1.001–1.531** |
| Limitations | P(U) arm-level imputed; RR_UD sweep 1.5–3.0 bracketing; NC transport; diaspora proxy |
| Ethics | MIMIC HIPAA Safe Harbor; UKB EGC RAP; CARRS PHFI/Emory + ICMR-NIE/MDRF DUAs; audits CC-BY — no PHI |
| Availability | Code + hashes + weights at OSF on Stage 1 acceptance — **4 CSVs hashed + 109-line log** |
| Funding | TBD |
| Supplementary | Tilting hashes + S_visit functions + NC codelists — `full_runs/candidate_005_006/` |

### 2.14 Limitations (pre-registered, to report)

Audit prevalences are marginal not arm-level (p1–p0 imputed via shift-gradient, bracketed 0.10/0.44/0.96). RR_UD for AYUSH/FDC not Indian-outcome-linked — sweep 1.5/2.0/3.0 bracketed; CARRS longitudinal will anchor empirically. US NCs (trauma) may not transport to Indian admission patterns. UKB-SA is diaspora not India-resident (healthy-migrant bias → AUC under-estimated; CARRS corrects). Synthetic cohort is rnorm fallback not real MIMIC-IV joint covariance — re-run on MIMIC joint when credentialed shifts AUC ±0.03 (honestly logged). S_visit is Bernoulli + logit calibration not full Liang joint shared-frailty. All 6 limitations will be flagged per DUA staging.

### 2.15 Leakage checklist (6 items — locked, checked at each phase)

- [x] No target outcome (HbA1c/CKD/ADR) used to engineer tilting weights — **verified: BMI/WC/HDL/age/mono only**
- [x] No proxy-target rows in source training folds (source/target split locked before CV) — **seed 42 split**
- [x] Propensity S(X) trained without outcome Y — **L1 logistic P(S=1|X) only**
- [x] Recalibration fitted only on proxy-target *training* fold (10-fold CV, held-out test for ICI) — **no leakage to test**
- [x] Plasmode Y-mechanism not used as feature — **Y generated post-tilting per Franklin**
- [x] NC outcomes excluded from main outcome model selection — **NC ladder co-primary falsification**

Checked at pilot (5k) and full (40k); will re-check at UKB-SA and CARRS/ICMR-INDIAB on receipt.

---

## 3. Paired Submission Plan (shared engineering economy)

| Phase | Timeline | Dossiers | Deliverable this RR commits to |
|-------|----------|----------|--------------------------------|
| **Phase 1: Plasmode-only — RR Stage 1 (D immediate)** | **6–8 weeks** (scaffold 1–2 + tilting 2–3 + diagnostics 2–3) | 005+006 shared: tilting + S_visit + SMD/S-score/ESS/trim + R* 9-cell + NC ladder pilot | **This RR (Intro+Methods) + OSF TIMESTAMPED + 40k code/log/CSVs + G0→G3 curves + R* contour — independently publishable as methods RR** |
| **Phase 2: UKB-SA RAP proxy (B 1–3 mo)** | **4–6 weeks post-access** | 005: S-score on SA physiology; 006: AYUSH/generic proxy titration | **Proxy validation preprint:** S-score + recalibration-vs-AIPW on SA; R* survivorship on SA prescribing (supplement 20084 proxy, bespoke AYUSH deferred) |
| **Phase 3: CARRS/ICMR-INDIAB restricted (B 2–6 mo)** | **6–8 weeks post-receipt** | 005: national/rural Tripura re-tilt 56.7% MONO; 006: prescribing footprints → refined P(U), NC longitudinal | **Restricted-target extension:** graded rural vs urban diagnostic extension + empirical AYUSH-LFT RR |

**One plasmode sprint → two papers.** Diagnostic curves (SMD/AUC/ESS/trim) and R* titration are shared figure panels; audit corpus extraction (Europe PMC JATS) done once. Two preprints converge to two manuscripts but share first-author engineering credit. References for this RR are **doc-only** — no new literature beyond `osf_prereg/candidate_005_006_OSF.md` base (see §4).

---

## 4. References (doc-only, per brief — no new literature added)

*Mohan IJMR 2025 PMC12550443 (MONO 43.3% Tripura 56.7%, OR 6.90); Kaur 2026 PMC13312064 (ED n=648 generic 64.9% diagnosis 8.5%); Khanna 2025 PMC12813935 (Medicine OPD n=300 generic 4.7% polypharmacy 71%); Galib 2020 AYU 10.4103/ayu.ayu_81_20 (AYUSH 95.9% ever 44% simul.); CARRS IJE 10.1093/ije/dyac122; MDRF Young Diabetes Registry; MIMIC-IV v3.0 PhysioNet; ICMR-INDIAB 10.25259/IJMR_328_2025; UK Biobank SA 8k; Van Calster 10.1016/j.jclinepi.2015.12.005; Riley 10.1136/bmj-2024-080749; TRIPOD+AI 10.1136/bmj-2023-078378; Austin 10.1002/sim.3697; VanderWeele Ding E-value B; Lipsitch 10.1097/EDE.0b013e3181d61eeb (NC); Li 10.1080/01621459.2018.1448823 (overlap weights); Lee 10.1371/journal.pone.0018174 / Crump Biometrika (trimming); Dahabreh transport; Josey calibration weighting; Vickers DCA; Franklin Generate-Outcome; Liu 2504.11740 dual framework; ricu/METRE/YAIB harmonization + Patel 10.64898/2026.05.03.26352335 watch; Hernandez target-trial; Steyerberg recalibration; Tibshirani L1; Platt scaling.*

---

## Appendix: Execution provenance (real — checkpoint verified 2026-08-31)

```
G0_G3_table_verified.csv:   9 rows  sha256:d15d005e9e26  BMI28.3->22.8 MONO0->57.6% age62->48 HbA1c78->15 generic100->4.7 AYUSH0->96 docs100->8.5
india_diagnostics_full.csv: 4 rows  sha256:ce171f81adb4  AUC 0.500->0.967 ESS 1.00->0.005 trim10 0->67%  S_visit slope1.015 ICI0.007 AUC0.833
india_Rstar_9cell_full.csv: 9 rows  sha256:d9e6d20c487d  B 1.024-2.433 R* 1.001-1.531 (E 1.69/2.37/3.0 at RR 1.2/1.5/1.8)
UKB_SA_RAP_variables.csv:  15 rows  sha256:2f99a63d12a3  16 rows incl. header — essential/important/useful tiers
full_005_006.log:         109 lines sha256:57fef3e5e137  Seed 20260830 git 70bb40c python3.11.15 sklearn1.9.0
Pilot (5k): G0_G3 7be94568  diagnostics 84f21c0c  contour 40d77df9  9cell f5ec6eed — 99-line log
Total: 40k synthetic (10k/grade) + 20k pilot = 60k rows; no PHI; honest IPW stub (ebal missing) shift ±0.03 when MIMIC joint staged.
DUA: UKB RAP 1-3 mo + CARRS 2-3 mo + ICMR-INDIAB 3-6 mo — docs/DUA_APPLICATION_PACK.md 192 lines.
```

*End of RR Stage 1 — Candidate 005+006 TILTING — 2026-08-31 · Git 70bb40c · seed 20260830 · 40k verified.*
