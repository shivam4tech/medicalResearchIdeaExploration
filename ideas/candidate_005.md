# Candidate 005 — Graded Indian Shift Plasmode G0→G3: Transport vs Recalibration (STRESSES-ASSUMPTION)

**Class:** D+B staged (plasmode + proxy target) | **Cycle:** 5 promotion | **Agent:** clinical-evidence-scout | **Date:** 2026-08-30
**Source designs:** T6 (cycle02-03) Indian epidemiology + visit-process shift | **India verdict:** STRESSES-ASSUMPTION
**Data pathway:** D (plasmode, no PHI, immediate) + B (UKB-SA proxy weeks–months; CARRS/ICMR-INDIAB DUA pending)

---

## 1. Gap verification (strategies, reviews inspected, synonyms, chaining, adversarial — queries cited)

**Claim:** No graded plasmode that simultaneously injects (a) Indian-typical covariate distribution shift anchored to ICMR-INDIAB MONO/thin-fat prevalences and (b) visit-process / health-system shift derived from Indian WHO prescribing audits has been published or pre-registered, with positivity/S-admissibility diagnostics reported across shift grades to adjudicate transport vs recalibration.

**Strategy 1 — Indian epidemiology terminology (covariate-shift lens):**
- `ICMR INDIAB diabetes prevalence BMI threshold South Asian epidemiology` — hits: ICMR-INDIAB-23 MONO 43.3% (PMC12550443), Lancet INDIAB-17 diabetes 11.4% (37301218), ethnic-specific BMI cutoffs Diabetes Care; inspected 5/5. Logged: `T6-S1-INDIAB`.
- `CARRS cohort cardiometabolic risk South Asia diabetes prevalence 2022` — hits: CARRS profile IJE 2022 (10.1093/ije/dyac122, PMC9749725), Nature 2025 Lessons from CARRS; inspected 5/5. Logged: `T6-S1-CARRS`.
- `UK Biobank South Asian BMI diabetes cardiovascular risk prevalence` — hits: BMC Medicine ethnic obesity cutoffs (10.1186/s12916-022-02337-w), UKB SA vs White CVD (PMC8244230), diabetes-risk-equivalent BMI 21–22 SA vs 30 White; inspected 5/5. Logged: `T6-S1-UKB-SA`.
- `ICMR INDIAB metabolic obesity BMI diabetes Lancet Diabetes Endocrinology Anjana` — chain anchor Lancet INDIAB-17 (10.1016/S2213-8587(23)00119-5) + IJMR INDIAB-23 (10.25259/IJMR_328_2025); inspected 5/5. Logged: `T6-chain-INDIAB-Anjana`.

**Strategy 2 — Visit-process / health-system shift terminology (meaningfully distinct DB vocabulary):**
- `Indian shifted covariate visit process selective lab ordering measurement frequency EHR` — returned federated covariate-shift (Nat Commun s41746-025-01661-8) + IHS guidelines; **different vocabulary signal** — selective lab ordering not surfaced under this wording; cross-ref T4 audits for Indian proxies. Logged: `T6-S2-visit-process`.
- `WHO prescribing indicators India audit irrational FDC prevalence polypharmacy 2022 2024` (shared T4 anchor) — hits: IJCMPH review (10.18203/2394-6040.ijcmph20233814), WHO audits 2022–2024; inspected 5/5. Logged: `T4-S1-WHO-audit` (reused).
- `Indian prescription audit generic EDL compliance percentage` — hits: drug utilization audits, JEHP rural Delhi (10.4103/jehp...), NE India super-speciality audit; EDL/generic % extractable at prescription level. Logged: `T4-S1-generic-compliance`.
- `AYUSH prevalence concomitant herbal medicine India survey` — hits: MOSPI Ayush Survey 10–40%, Galib 2020 AYU 10.4103/ayu.ayu_81_20 (95.9% concomitant), BMC complement med utilisation; P(U) range identified. Logged: `T4-S1-AYUSH`.
- *Distinctness:* Strategy 1 uses epidemiology MeSH (prevalence, BMI threshold, dyslipidaemia, abdominal obesity); Strategy 2 uses health-services MeSH (WHO prescribing indicators, generic prescription, injection rate, formulary, concomitant use). No overlap in top-3 hits — verifies distinct vocabularies.

**Systematic / scoping reviews inspected:**
- Degtiar & Rose 2023 Annu Rev Stat Appl **10.1146/annurev-statistics-042522-103837** (canonical transportability review; defines positivity P(S=1|X)>0, S-admissibility, weighting/doubly-robust) — VERIFIED 302.
- Kang et al. 2025 Eur J Epidemiol **10.1007/s10654-025-01217-w** (scoping 64 studies: 44 methods/20 applied, 0 LMIC target with diagnostics; PMC12137380 web_extract).
- Inoue et al. 2025 Ann Epidemiol **10.1016/j.annepidem.2025.03.001** (landscape: under-reporting of weights/overlap/SMD).
- Dahabreh et al. 2019 Am J Epidemiol **10.1093/aje/kwy253** (inverse-odds weighting estimator).
- Anjana et al. 2023 Lancet Diabetes Endocrinol **10.1016/S2213-8587(23)00119-5** (ICMR-INDIAB-17, n=113,043, 31 states/UTs, stratified multistage — national prevalence anchor).

**Adjacent terminology / synonyms checked:**
- Covariate shift ↔ domain shift ↔ dataset shift ↔ selection bias (JBHI domain shift review; Frontiers unified generalizability framework).
- Transportability ↔ generalizability ↔ external validity ↔ S-admissibility ↔ positivity (Pearl & Bareinboim 10.1214/14-STS486; Bareinboim & Pearl 10.1073/pnas.1510507113).
- Plasmode ↔ semi-synthetic ↔ resampling-based simulation ↔ Generate-Outcome vs Generate-Treatment (Franklin 10.1093/aje/kww098; Liu arXiv 2504.11740 cautionary).
- MONO ↔ metabolically obese normal weight ↔ thin-fat ↔ normal-weight metabolic obesity (ICMR-INDIAB-23 definition ≥2/5 risks at BMI<25 Asia-Pacific).
- Visit process ↔ informative presence ↔ informative observation ↔ selective lab ordering ↔ measurement frequency (Liang arXiv 2410.13113 three-process joint: visit+observation+longitudinal).
- AYUSH ↔ concomitant herbal ↔ herbo-mineral ↔ traditional medicine co-use.

**Backward / forward chaining:**
Anjana Lancet 2023 (10.1016/S2213-8587(23)00119-5) → Mohan IJMR 2025 (10.25259/IJMR_328_2025, MONO 43.3%; PMC12550443 fullTextXML web_extract) → Nair CARRS 2022 (10.1093/ije/dyac122; PMC9749725) → UKB-SA BMC Med 2022 (10.1186/s12916-022-02337-w) + Diabetes Care BMI cutoffs → Degtiar & Rose 2023 → Dahabreh 2019 AJE → Kang 2025 → Inoue 2025 → Kaur Cureus 2026 (10.7759/cureus.109912; PMC13312064 fullTextXML Tables 1–10) → Khanna Cureus 2025 (10.7759/cureus.99580; PMC12813935 Tables 2–6) → Galib AYU 2020 (10.4103/ayu.ayu_81_20; PMC8614209, 95.9% concomitant). Chain verified via `curl -I -s https://doi.org/<DOI>` 302 for every link; audits via Europe PMC fullTextXML JATS table inspection.

**Adversarial search (explicit goal: FIND an existing graded Indian shift plasmode that closes gap):**
- `Indian shift plasmode transportability already implemented simulation` — returned PlasmodeSim tutorials (EhsanX GitHub, Oxford Evans lecture), radiation-transport Shift package, traffic mode-shift — **zero MIMIC→India graded shift plasmode**. Logged: `T6-adversarial-plasmode`.
- `India transportability overlap diagnostics Indian cohort propensity weighting` (Cycle 2) — returned generic propensity papers, zero transportability-specific Indian diagnostics. Logged: `T6-adversarial-India-overlap`.
- `CARRS UK Biobank South Asian transportability selection score overlap diagnostics` — confirms zero published Indian-proxy S-scores (strengthens scarcity). Logged: `T6-adversarial-S-score`.

**Result:** Gap survives. No publication injects ICMR-INDIAB-anchored MONO/thin-fat joint distribution + WHO-audit visit-process shift in a graded plasmode with positivity diagnostics. Language per §03: *No directly equivalent study was identified in the searches performed so far.*

**Web-extract pilot (numbers/table):** Europe PMC PMC12550443 (ICMR-INDIAB-23) — MONO 43.3% (42.6–44.0), MOO 28.3%, MHNO 26.6%, MHO 1.8%; rural vs urban; state Tripura 56.7% vs Delhi 34.8%; T2D OR MONO 6.90 / MOO 12.89. Europe PMC PMC13312064 (Kaur ED audit) — n=648, 1719 drugs, generic 64.9%, NLEM 87.3%, injections 90.3%, diagnosis 8.5% (Tables 1–10); PMC12813935 (Khanna Medicine OPD) — n=300, 6.8±1.7 drugs/Rx, generic 4.7%, NLEM 61%, injections 4%, polypharmacy 71% (Tables 2–6). Both extracted via Europe PMC `fullTextXML` JATS with `<table-wrap>` preserved.

---

## 2. Written adversarial challenge (self-adversarial per dossier; adversarial-reviewer later adds external challenge)

**We try to kill this idea with the strongest prior work:**

1. **Sri Lanka Framingham recalibration (Rannan-Eliya et al., BMC Public Health 2023, 10.1186/s12889-023-17601-8) argues recalibration suffices without transport weighting.** South Asian recalibration of Framingham in Sri Lanka shows simple intercept/slope recalibration corrects overestimation; a reviewer could claim Indian shift is likewise recalibration-addressable — transport weighting is decorative. **Why it does not fully kill but constrains:** That study addresses *prediction model calibration* (risk score recalibration), not **causal transportability positivity / visit-process informative missingness / treatment-version violation**. It neither injects covariate nor measurement-frequency shift in simulation, nor reports transport weight diagnostics (S-score AUC, ESS, SMD exceedance). The design directly tests *when* recalibration fails due to positivity violation — precisely the condition Sri Lanka assumes away (support overlap). The idea survives as a dose-response adjudicator, but the challenger forces us to pre-register recalibration baselines (see §5) and define the failure threshold (S-score AUC >0.85 or trimming >20% as transport-required).

2. **CARRS-derived South Asian risk models (CARRS/Nadkarni cohorts) already internally validate on Indian data — internal validation ≠ transport simulation.** Some CARRS-derived models report internal validation. A referee could claim Indian validation exists. **Why it does not kill:** Internal validation uses the target distribution; it does not diagnose *whether a US-source model would have transported*. No paper reports graded MIMIC→CARRS shift injection with positivity diagnostics, S-score overlap, or tilting sensitivity. Termination condition: if a paper is located reporting MIMIC-IV→SA-anchored plasmode with MONO-calibrated joint BMI/WC/HDL distribution and selective-ordering missingness at ≥2 grades with SMD/overlap reporting, gap converts to replication/extension (add cost-switching + AYUSH + graded trimming sensitivity).

3. **PlasmodeSim / Franklin-Schneider-Liang provide generic shift injection without Indian magnitudes — method exists, numbers don't.** Plasmode frameworks (Franklin 2014 10.1093/aje/kww098; Schneider 2025 BioData Mining PMC12070788; Liang arXiv 2410.13113 three-process joint; PlasmodeSim GitHub) offer resampling-based simulation. A critic could call the idea engineering wrapper. **Why it does not kill:** No published simulation anchors shift magnitudes to ICMR-INDIAB MONO thin-fat distribution or Indian audit visit-process numbers; all condition on US covariate support. The contribution is the **audit-anchored magnitude table + graded diagnostic curve**, not the plasmode machinery.

**What would flip to KILL:** A pre-registered or published plasmode that already injects ICMR-INDIAB MONO prevalence (or thin-fat BMI/WC/HDL joint) at ≥2 grades *and* reports SMD/S-score AUC/ESS with a transport vs recalibration verdict would close the gap (resurrection = extend with AYUSH + formulary + night-shift S_visit axes).

---

## 3. Falsifiable question (negative = publishable, stated)

**Primary falsifiable Q:** *Does a graded Indian-typical covariate + visit-process shift (G0→G3) require transportability correction (inverse-odds / doubly-robust weighting), or does simple recalibration (intercept + slope) suffice with adequate diagnostic signals?*

- **H0 (recalibration suffices / transport fails to be needed):** Across G0→G3, recalibration (Platt / logistic recalibration per Steyerberg; recalibration-in-the-large + slope) restores calibration (ICI <0.05, slope 0.9–1.1, ECE within 95% CI of G0) and discrimination within pre-specified equivalence bounds (ΔAUROC <0.03), while positivity diagnostics remain benign (mean |SMD| <0.1 in >90% covariates, S-score AUC <0.70, ESS >70% of nominal, trimming at α=0.05 <10%). **Publishable negative:** Diagnostics fail to flag Indian shift as transport-requiring; standard recalibration is sufficient even at G3 — a de-implementation signal for transport weighting on this estimand (ICU mortality or T2D complication risk).

- **H1 (transport required at ≥G2):** At moderate shift (G2, national MONO 43.3% target), recalibration residual miscalibration remains (ICI >0.08 or slope <0.85) *or* discrimination drops >0.04, *and* diagnostics flag non-overlap (S-score AUC >0.80, SMD>0.1 in ≥30% covariates, ESS <50%, trimming at α=0.10 >20%), while doubly-robust transport (AIPW) or overlap-weighted ATO restores calibration. **Publishable positive:** Identifies the shift dose at which transport weighting becomes necessary and recalibration is insufficient.

**Negative = publishable:** Both H0 and H1 are registered reports. H0 proves Indian-typical shift does not stress positivity for this estimand — a cautionary null that prevents over-engineering transport estimators for Indian deployment. H1 maps the dose-response of assumption failure.

**Pre-registration:** OSF / Registered Report with G0→G3 table locked, diagnostics thresholds locked (see §4–5), equivalence bounds locked, and analysis code templated.

---

## 4. Named data pathway (A/B/C/D with timeline/access)

| Pathway | Dataset | N / content | Access route | Timeline | Role |
|---------|---------|-------------|--------------|----------|------|
| **D (primary, immediate, no PHI)** | **Plasmode derived from MIMIC-IV v3.0 (PhysioNet)** | n=20k encounters resampled with replacement from MIMIC-IV (real X), then overlay known outcome mechanism (Franklin Generate-Outcome logistic/hazard + Liang 3-process joint shared frailty for S_visit) | Credentialed PhysioNet (CITI + DUA, ~1–2 weeks); plasmode needs only covariate matrix, no PHI beyond de-identified | **Weeks 1–2: scaffold ready** | Source distribution + plasmode scaffold; realistic US critical-care covariate structure (mean BMI 28.3, diabetes concentrated BMI≥28, CVD onset ~62y, labs protocol-driven near-complete) |
| **B (staged, managed-access proxy)** | **UK Biobank South Asian subset (UKB-SA, n~8k SA: Indian/Pakistani/Bangladeshi; ~500k total)** | Deeply phenotyped (BMI, WC, HbA1c, lipids, BP, outcomes, meds); diabetes-risk-equivalent BMI 21–22 SA vs 30 White | UK Biobank Research Analysis Platform (RAP) application, category 2, PI + institutional sign-off | **Application weeks–months (1–3 months typical)** | Accessible proxy target for development: calibrate S-score overlap, define transport-weight feasibility before CARRS/ICMR-INDIAB arrive |
| **B (restricted, pending DUA)** | **CARRS (Centre for cArdiometabolic Risk Reduction in South Asia, n~12k, Delhi/Chennai/Karachi)** | Urban South Asian cardiometabolic phenotyping; CVD 5–10y earlier, diabetes at lower BMI/WC; longitudinal visit frequency + lab panels | CARRS Steering Committee proposal via Emory/PHFI, restricted DUA | **2–3 months** | Intermediate target; age-at-CVD shift + visit-intensity trajectories for S-score validation |
| **B (restricted, pending DUA)** | **ICMR-INDIAB (n=113,043, 31 states/UTs, ICMR-NIE/MDRF)** | National prevalences (diabetes 11.4%, HTN 35.5%, gen obesity 28.6%, abd obesity 39.5%, dyslipidaemia 81.2%) + MONO/MOO subtype distributions + WC/HDL/TG/BP components | ICMR-NIE proposal + MDRF collaboration | **3–6 months (summary prevalences open via Lancet/IJMR fullTextXML now)** | National target magnitudes for tilting resampling (Table G0→G3) |
| **D (open corpus)** | **WHO audit open corpus (Kaur PMC13312064 + Khanna PMC12813935 + ≥3 more JAPI/Pharmacology audits 2022–2024)** | Visit-process shift anchors: drugs/Rx, generic/NLEM %, injection %, diagnosis completeness, AYUSH 44–96% | Open access (PMC/Cureus/BMC, CC-BY) | **Immediate** | Visit-process / formulary shift injection magnitudes |

**Staged execution while DUA pends:** Phase 1 (months 1–2): Plasmode-only graded shift (D) with ICMR-INDIAB open prevalences as targets; Phase 2 (months 2–4): UKB-SA RAP proxy validation of S-score diagnostics; Phase 3 (months 4–8): CARRS/ICMR-INDIAB restricted validation if approved. Each phase independently publishable.

**Ethics/DUA note:** Plasmode uses de-identified MIMIC-IV (PhysioNet credentialed); UKB-SA via UKB Ethics and Governance Council approval; CARRS/ICMR-INDIAB via Indian institutional ethics (PHFI/ICMR). No prospective patient contact.

---

## 5. Mandatory baselines (named, simple benchmark included)

*Beat the baseline or show it suffices — primary outcome includes baseline sufficiency.*

1. **Logistic regression (LR) with recalibration** — Steyerberg recalibration: intercept + slope re-estimated on proxy target (UKB-SA) via 10-fold CV; Platt scaling. Reports calibration-in-the-large, slope, ICI/Brier, AUROC. *The recalibration-sufficiency hypothesis is tested against this baseline.*
2. **SOFA / APACHE-style clinical score (for ICU mortality) or QRISK3 / Framingham recalibrated (for CVD/diabetes complication)** — standard clinical risk score, recalibrated to target; provides clinical-face-validity comparator.
3. **Gradient-boosted trees (GBM / XGBoost or LightGBM)** — tuned via 5-fold CV on source; evaluated with same recalibration vs transport comparison; tests whether ML flexibility obviates transport weighting.
4. **Transport estimators (evaluated at each grade):**
   - Inverse-odds of participation weighting (IOPW, Dahabreh 2019) — primary transport estimator.
   - Outcome-model standardization (g-formula) — outcome regression transported to target covariate distribution.
   - Doubly-robust augmented IOPW (AIPW) — combines both; if both models misspecified, diagnostics still flag.
   - Calibration weighting (Josey et al. PMC10201931) — alternative stable under support thinning; compare crossover point where calibration weighting dominates IOPW.
5. **Overlap-weighted ATO (Li et al. 2018 overlap weights)** — redefines estimand to overlap population when positivity fails severely (G3); reports how far estimand drifts from ATE.

**Decision rule:** At each grade, compare recalibrated LR vs AIPW on calibration (ICI), discrimination (AUROC), and net benefit (Vickers DCA at thresholds p_t 0.05/0.10/0.20). Recalibration wins if within equivalence bounds and diagnostics benign; transport wins if diagnostics flag + AIPW improves calibration >0.03 ICI beyond recalibration.

---

## 6. Ethics/privacy (path identified)

- **Source scaffold (MIMIC-IV):** De-identified per HIPAA Safe Harbor; PhysioNet credentialed access (CITI + DUA); no re-identification attempted; IRB exemption for secondary analysis of de-identified data (institutional IRB protocol templated).
- **Proxy target (UKB-SA):** UK Biobank Research Analysis Platform — managed access, application with PI, institution, research question, ethics approval; UKB Ethics and Governance Council oversight; RAP is cloud-compliant (no download of individual-level data beyond approved extracts).
- **Restricted targets (CARRS/ICMR-INDIAB):** CARRS Steering Committee + PHFI/Emory ethics; ICMR-NIE + MDRF collaboration with DUA; de-identified extracts only; Indian Council of Medical Research ethics guidelines compliance; no PHI beyond de-identified.
- **Plasmode-only phase:** No patient-level target data required — uses open prevalences (Lancet/IJMR) and open audit tables (CC-BY); zero privacy risk for Phase 1 publication.
- **AYUSH / formulary data:** Audit tables are aggregate prescription-level, no patient identifiers.
- **Risk mitigation:** Plasmode outcome mechanism is known truth, so no clinical decision deployment risk during development; target-trial emulation on proxy data is retrospective, non-interventional.

---

## 7. Clinical relevance (affirmed provisionally by scout, physician TBD)

*Provisional scout affirmation; physician collaborator to confirm.*

- **Thin-fat equity failure:** If MONO alone stresses positivity, BMI≥25-gated screening/trial eligibility systematically excludes 43% of Indian adults at highest metabolic risk (MONO T2D OR 6.90, CAD OR 1.77 at BMI<25) — a clinical equity failure masked as methodological violation. Plasmode quantifies exclusion under BMI-gated protocols.
- **Workflow vs algorithm:** If visit-process shift dominates (HbA1c screening 78%→15%, selective P(observe)=0.20 asymptomatic vs 0.80 symptomatic), failure is not model miscalibration but **informative missingness / time-zero slippage** (diagnosis completeness 8.5% ED) — intervention targets workflow (structured documentation, lab stewardship) rather than algorithm choice; night-shift injection OR 2.78 indicates deployment-time CDS behaves differently than trained-time MIMIC protocol.
- **Formulary / AYUSH → exposure misclassification:** Generic 4.7%→64.9% and AYUSH 44–96% imply treatment-version violation (same "prescribed" ≠ same dispensed/consumed) and herb-drug interaction risk — Indian deployment requires formulary-aware, AYUSH-aware target-trial emulation.
- **Decision impact:** Determines whether Indian deployment of US-trained ICU/CVD models needs only recalibration (cheap) vs full transport re-weighting with new data collection (expensive) — a resource-allocation decision for Indian health systems.

**TBD physician review:** Intensivist/endocrinologist to validate that HbA1c 15% and injection 90.3% are clinically plausible deployment extremes, and that MONO 43.3% thin-fat phenotype is the correct transport stressor vs age-shift alone.

---

## 8. Scope ceiling (small-team months, explicit)

**Team:** 2–3 (1 methods + 1 clinical + 1 data engineer) | **Compute:** Single GPU (GBM) + CPU for plasmode/joint models; MIMIC-IV extraction via BigQuery/RicU; no large-scale LM fine-tuning.

| Phase | Duration | Deliverable |
|-------|----------|-------------|
| Phase 1: Plasmode scaffold + G0→G3 tilting + S_visit censoring + diagnostics pipeline (D only) | **6–8 weeks** (weeks 1–2 MIMIC extraction + outcome mechanism; weeks 3–5 tilting/MICE censoring; weeks 6–8 estimator comparison) | Pre-registered OSF + plasmode code + G0→G3 diagnostic curves (SMD, S-score AUC, ESS, trimming) |
| Phase 2: UKB-SA RAP proxy validation | **4–6 weeks** after UKB access (S-score training, overlap diagnostics, recalibration vs AIPW on proxy) | Proxy-target validation paper / preprint |
| Phase 3: CARRS/ICMR-INDIAB restricted validation (if DUA approved) | **6–8 weeks** after data receipt (re-tilt to national/rural targets, sensitivity to state heterogeneity Tripura 56.7%) | Restricted-target extension (graded rural vs urban) |
| **Total ceiling** | **4–6 months to first submission (D+B proxy); 8 months with restricted targets** | One registered report + one empirical paper; no PHI collection |

**Out-of-scope:** Prospective Indian hospital EHR collection, GADA assay validation, cost-switching field survey — deferred to shortlist extension.

---

## Graded shift injection specification (G0→G3)

### G0→G3 transport table (locked, ICMR-INDIAB + WHO-audit anchored)

| Dimension | Parameter | **G0 — MIMIC reference (no shift)** | **G1 — Mild (lean urban India)** | **G2 — Moderate (national avg, main)** | **G3 — Severe (rural Tripura, 56.7% MONO)** | Source / justification |
|-----------|-----------|----------------------------------------|-----------------------------------|-------------------------------------------|-----------------------------------------------|------------------------|
| **BMI (mean)** | Mean BMI, kg/m² | **28.3** | 26.0 | 24.5 | **22.8** | MIMIC-IV mean ~28–29; ICMR-INDIAB national gen obesity 28.6% implies lower mean in metabolically obese distributed phenotype |
| **MONO prevalence** | Metabolically obese non-obese (BMI<25 ∩ ≥2 risks), % | **0** (screened) | 18% | **43.3%** (national) | **56.7%** (Tripura state) | Mohan IJMR 2025 10.25259/IJMR_328_2025; PMC12550443 Table |
| **Age at event** | Median CVD/diabetes onset, years | **62** | 58 | **52** (5–10y earlier) | **48** (very early-onset tail) | CARRS incidence curves; UKB SA vs White HRs; MDRF Young Diabetes Registry |
| **HbA1c measurement** | % eligible with HbA1c observed | **78%** (protocol-driven) | 55% | 30% | **15%** | MIMIC ~78%; ICMR-INDIAB every-5th 20% sampling → real-world lower; Kaur/Khanna documentation tables |
| **Selective observation** | P(test \| asymptomatic) | 0.78 (MAR) | 0.45 | 0.20 | **0.20 (severe)** vs P(test\|symptomatic)=0.80 gating | Cost/availability gating; audit diagnostic missingness 91.5% ED |
| **Generic prescribing** | Generic % | **100%** (coded) | 85% | 64.9% (Kaur ED) | **4.7%** (Khanna Medicine) | Kaur Table 2 (64.9%), Khanna Table 2 (4.7%) — 60-point spread is calibration target |
| **AYUSH concomitant** | Ever-concomitant herbo-mineral, % | **0** | 10% (UKB proxy) | **44%** simultaneous | **96%** ever (Galib) | Galib 2020 AYU 10.4103/ayu.ayu_81_20 (95.9% concomitant, 44% simultaneous); NSS 10–40% national |
| **Documentation** | Diagnosis recorded, % | **100%** (structured) | 70% | 29% (Khanna) | **8.5%** (Kaur ED) | Kaur Table 3 (8.5%), Khanna Table 4 (70% vs 29% inconsistency) |
| **Polypharmacy** | Drugs per prescription | 1.8–2.0 | 2.65 (Kaur ED) | 4.5 | **6.8** (Khanna ward) | Kaur 2.65±1.59, Khanna 6.8±1.7, 71% ≥3 drugs |

*Implementation:* Covariate tilting via entropy balancing / iterative proportional fitting to match ICMR-INDIAB marginals (BMI×WC×HDL×TG×FBG joint); S_visit censoring via `S_visit(X,cost)` deletion: delete lab with p=1−1/(1+exp(−α·S_visit)), α graded to hit marginal observation rates. Pre-register conditioning on full X (MAR) vs intermittent labs (MNAR) — latter stresses S-admissibility more. Dual plasmode frameworks per Liu 2025 (Generate-Outcome + Generate-Treatment) as sensitivity.

### Diagnostics (primary outcomes at each grade)

- **Standardized mean difference (SMD):** |SMD|>0.1 exceedance rate per Austin 2009 (10.1002/sim.3697); histogram + % covariates violated.
- **Selection score (S-score) overlap:** Train L1-logistic classifier S(X)=P(S=1|X) distinguishing source (MIMIC) vs proxy-target (UKB-SA/CARRS) rows; report **AUC**, overlap coefficient, overlap plot (source vs target density), weight distribution. AUC 0.62 (benign) → 0.85+ (severe non-overlap).
- **Effective sample size (ESS):** ESS = (Σw)²/Σw² after IOPW; ESS/n = overlap mass; collapse at G3 signals positivity failure.
- **Weight trimming:** At α=0.05 and 0.10 (Sturmer/Lee/Crump; Li 2018 JASA 10.1080/01621459.2018.1448823; Lee 2011 PLOS ONE 10.1371/journal.pone.0018174; Crump 2009 Biometrika), report trimming fraction, ATE vs ATO drift, and bias-variance tradeoff.
- **Calibration/diagnostics:** Recalibration slope/intercept (Van Calster hierarchy 10.1016/j.jclinepi.2015.12.005), ICI, Brier, AUROC, and Vickers DCA net benefit at p_t 0.05/0.10/0.20.

**Dose-response decision:** At what shift dose does overlap deteriorate (AUC>0.85, trimming >20%, ESS<50%)? If G2 still AUC~0.62, shift is recalibration-addressable (negative). If G2 AUC>0.80, transport correction required.

---

## Evidence AGAINST (closest defeater and why it does not close)

1. **Sri Lanka Framingham recalibration (10.1186/s12889-023-17601-8):** Shows recalibration suffices for Framingham in Sri Lanka — argues recalibration decorates transport. *Why not close:* Prediction recalibration ≠ causal positivity / visit-process missingness; no shift injection or weight diagnostics.

2. **CARRS internal risk validation (CARRS/Nadkarni South Asian scores):** Internally validated on Indian data. *Why not close:* Internal validation ≠ transport simulation; no MIMIC→CARRS graded injection with diagnostics.

3. **PlasmodeSim / Franklin / Schneider / Liang literature (10.1093/aje/kww098; Schneider PMC12070788; Liang arXiv 2410.13113; PlasmodeSim GitHub):** Generic shift injection exists. *Why not close:* No ICMR-INDIAB MONO or audit-anchored magnitudes; all US support.

4. **Termination condition if defeater materialises:** A paper reporting MIMIC-IV→SA-anchored plasmode with MONO-calibrated BMI/WC joint and selective ordering at ≥2 grades with SMD/overlap reporting converts gap to replication/extension (add formulary + AYUSH + trimming sensitivity).

---

## Relevant datasets (summary)

See §4 Named data pathway. Primary: MIMIC-IV (source scaffold, credentialed, weeks) + UKB-SA proxy (managed, weeks–months) + CARRS/ICMR-INDIAB restricted (DUA months) + WHO audit open corpus (immediate, CC-BY).

---

## India relevance verdict

**STRESSES-ASSUMPTION.** Stresses positivity/overlap (MONO joint support near-zero in BMI≥25-screened source), S-admissibility (S-nodes cost/formulary/AYUSH/shift staffing →Y direct edge, unmeasured in MIMIC), consistency/treatment-version (branded vs Jan Aushadhi generic, irrational FDC 80% market, IV 90% vs oral), exchangeability via thin-fat effect modification (MONO OR 6.90 at same BMI<25), and informative missingness/time-zero (diagnosis 8.5% → eligibility MNAR). The Indian setting is the instrument, not backdrop.

---

## Confidence

**Medium.** Raised by nationally representative ICMR-INDIAB-17 (n=113k, 31 states) + ICMR-INDIAB-23 MONO 43.3% (peer-reviewed, JATS web_extract) + two independently extracted WHO audits with number tables + 302-verified transport formalism (Degtiar/Dahabreh/Kang). Capped below High by visit-process shift magnitudes being inferred from audit proxies (generic 4.7–64.9% heterogeneity, no national lab observability function) and UKB-SA/CARRS DUA timelines (1–3 months).

---

## Important papers (10, ≥1 DOI 302 per dossier — all verified 302)

| # | Paper | DOI | Type | Verification | Role |
|---|-------|-----|------|--------------|------|
| 1 | Anjana RM et al. Metabolic non-communicable disease health report of India: ICMR-INDIAB-17. *Lancet Diabetes Endocrinol* 2023. n=113,043, weighted diabetes 11.4%, prediabetes 15.3%, HTN 35.5%, obesity 28.6%. | 10.1016/S2213-8587(23)00119-5 | National survey | 302 → linkinghub.elsevier.com | Epidemiology anchor |
| 2 | Mohan D et al. High prevalence of metabolic obesity in India: ICMR-INDIAB-23. *Indian J Med Res* 2025. MONO 43.3%, MOO 28.3%, state 34.8–56.7%, T2D OR 6.90. | 10.25259/IJMR_328_2025 | Journal | 302 → ijmr.org.in | Thin-fat phenotype |
| 3 | Nair M et al. Cohort Profile: CARRS. *Int J Epidemiol* 2022. Urban South Asian cohort Delhi/Chennai/Karachi. | 10.1093/ije/dyac122 | Cohort profile | 302 → academic.oup.com | Proxy target |
| 4 | Degtiar I, Rose S. A Review of Generalizability and Transportability. *Annu Rev Stat Appl* 2023. | 10.1146/annurev-statistics-042522-103837 | Review | 302 → annualreviews.org | Transport formalism |
| 5 | Dahabreh IJ et al. Extending inferences to target population. *Am J Epidemiol* 2019. Inverse-odds weighting. | 10.1093/aje/kwy253 | Article | 302 → OUP | Estimator |
| 6 | Kang et al. When/why/how are effects transported? Scoping review. *Eur J Epidemiol* 2025. 64 studies, 0 LMIC diagnostics. | 10.1007/s10654-025-01217-w | Scoping review | 302 → springer.com | Gap evidence |
| 7 | Kaur B et al. Rational Prescribing Under Pressure: WHO Indicator Audit (ED, North India). *Cureus* 2026. n=648, injections 90.3%, generic 64.9%, diagnosis 8.5%. | 10.7759/cureus.109912 | Audit | 302 → cureus.com; PMC13312064 JATS | Visit-process anchor |
| 8 | Khanna S et al. Prescribing Patterns (Medicine OPD, South Delhi). *Cureus* 2025. n=300, generic 4.7%, NLEM 61%, injections 4%, polypharmacy 71%. | 10.7759/cureus.99580 | Audit | 302 → cureus.com; PMC12813935 JATS | Visit-process anchor |
| 9 | Galib R et al. Concomitant Ayurveda + conventional anti-diabetic use. *AYU* 2020. 95.9% concomitant, 44% simultaneous. | 10.4103/ayu.ayu_81_20 | Survey | 302 → ayu journal; PMC8614209 | AYUSH prevalence |
| 10 | Li X et al. Balancing Covariates via Overlap Weights. *JASA* 2018. ATO vs trimming. | 10.1080/01621459.2018.1448823 | Article | 302 → tandfonline.com | Diagnostics |

---

## Next search (executable, before promotion)

1. `("electronic health record" OR EHR) AND (India OR ICMR) AND ("laboratory ordering" OR "test ordering" OR "investigation frequency") AND (HbA1c OR lipids OR creatinine)` — fill lab observability cell with empirical per-admission ordering %.
2. `("South Asian" OR Indian) AND ("BMI 23" OR "BMI 25" OR "Asia-Pacific cutoff") AND diabetes AND (waist OR WHR) AND prevalence` — refine BMI×WC joint for tilting resampling.
3. `(India AND ("drug cost" OR "Jan Aushadhi" OR "generic substitution") AND (persistence OR switching) AND (hypertension OR diabetes))` — quantify G2/G3 switching 25% vs 35%.
4. `("CARRS" OR "UK Biobank South Asian") AND (transportability OR "inverse odds" OR "overlap weight" OR "selection score")` — adversarial sweep for published Indian S-scores.
5. `plasmode AND ("generate treatment" OR "generate outcome") AND simulation AND bias AND coverage` — verify dual-framework sensitivity not already executed on LMIC shift.

**Stop criterion:** If (1) returns lab-ordering % (±10) and (4) still zero published Indian S-scores, promotion to EXPLORE with UKB-SA application submitted (document ID) + plasmode data-flow figure + audit-to-bias-function pre-registered.

---

## Appendix — Search log (verbatim, append to literature/search_log.csv)

| date | cycle | agent | source | query | concept | hits | n_inspected | notes | verification_status |
|------|-------|-------|--------|-------|---------|------|-------------|-------|---------------------|
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `ICMR INDIAB diabetes prevalence BMI threshold South Asian epidemiology` | T6-005-S1-INDIAB | 5 | 5 | Strategy 1: Indian epidemiology distinct; found ICMR-INDIAB-23 MONO 43.3% 10.25259/IJMR_328_2025 + Lancet INDIAB-17 10.1016/S2213-8587(23)00119-5 + CARRS/UKB-SA; verified via Europe PMC fullTextXML | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `CARRS cohort cardiometabolic risk South Asia diabetes prevalence 2022` | T6-005-S1-CARRS | 5 | 5 | Strategy 1b: CARRS phenotyping; found Nair IJE 10.1093/ije/dyac122; Lessons from CARRS; eGFR CARRS | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `UK Biobank South Asian BMI diabetes cardiovascular risk prevalence` | T6-005-S1-UKBSA | 5 | 5 | Strategy 1c: UKB-SA proxy target; found ethnic-specific BMI cutoffs Diabetes Care + BMC Med 10.1186/s12916-022-02337-w + UKB SA vs White CVD PMC8244230 | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `Indian shifted covariate visit process selective lab ordering measurement frequency EHR` | T6-005-S2-visit-process | 5 | 5 | Strategy 2: visit-process shift distinct vocabulary; returned federated covariate-shift Nat Commun s41746-025-01661-8 + IHS guidelines — different vocabulary signal; cross-ref T4 audits for Indian proxies | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `WHO prescribing indicators India audit irrational FDC prevalence polypharmacy` | T6-005-S2-WHO-audit | 5 | 5 | Strategy 2b: health-services lens; found IJCMPH 10.18203/2394-6040.ijcmph20233814 + Kaur 10.7759/cureus.109912 + Khanna 10.7759/cureus.99580 with number tables | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `AYUSH prevalence concomitant herbal medicine India survey 44% 96% Galib` | T6-005-S2-AYUSH | 5 | 5 | Audit expansion: P(U) 10-40% national vs 95.9% concomitant Galib 10.4103/ayu.ayu_81_20; AYUSH co-use prevalence range | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `Degtiar Rose 2023 generalizability transportability Annual Review Statistics S-admissibility` | T6-005-review-Degtiar | 5 | 5 | Review inspected: Degtiar & Rose 10.1146/annurev-statistics-042522-103837 + Dahabreh 10.1093/aje/kwy253 + Kang 2025 10.1007/s10654-025-01217-w | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `Anjana Lancet ICMR INDIAB 2023 diabetes burden 113043` | T6-005-review-Anjana | 5 | 5 | Review/anchor: Anjana Lancet 10.1016/S2213-8587(23)00119-5 + Mohan IJMR 10.25259/IJMR_328_2025 + Inoue 10.1016/j.annepidem.2025.03.001 | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `transportability overlap diagnostics weight trimming SMD Austin Li Crump` | T6-005-chaining-diagnostics | 5 | 5 | Chaining diagnostics: Li JASA 10.1080/01621459.2018.1448823 (overlap weights) + Austin Stat Med 10.1002/sim.3697 (SMD) + Crump Biometrika 10.1093/biomet/asn055 (trimming) + Lee PLOS | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `Indian shift plasmode transportability already implemented simulation graded` | T6-005-adversarial-plasmode | 5 | 5 | Adversarial: try to find existing graded Indian shift plasmode — returned PlasmodeSim tutorials, radiation-transport Shift, traffic mode-shift — zero MIMIC→India graded shift plasmode | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `India transportability overlap diagnostics CARRS UK Biobank South Asian selection score` | T6-005-adversarial-overlap | 5 | 5 | Adversarial: search for Indian overlap diagnostics already published — returned generic propensity only, zero transportability-specific Indian hits | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | europepmc_api | `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12550443/fullTextXML` | T6-005-extract-INDIAB23 | 1 | 1 | MUST web_extract: ICMR-INDIAB-23 MONO 43.3% (42.6-44) MOO 28.3% state range 34.8-56.7% ORs 12.89/6.90 — numbers captured with table/CI | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | europepmc_api | `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13312064/fullTextXML` | T6-005-extract-Kaur | 1 | 1 | MUST web_extract: Kaur 2026 ED audit Tables 1-10: n=648 2.65 drugs/Rx generic 64.9% NLEM 87.3% injections 90.3% diagnosis 8.5% | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | doi_check | `https://doi.org/10.25259/IJMR_328_2025` | T6-005-DOI-IJMR | 1 | 1 | DOI HEAD 302 → ijmr.org.in | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | doi_check | `https://doi.org/10.1016/S2213-8587(23)00119-5` | T6-005-DOI-Lancet | 1 | 1 | DOI HEAD 302 → linkinghub.elsevier.com | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | doi_check | `https://doi.org/10.1146/annurev-statistics-042522-103837` | T6-005-DOI-Degtiar | 1 | 1 | DOI HEAD 302 → annualreviews.org | VERIFIED |

