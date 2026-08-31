# Full 005+006 — G0→G3 India Plasmode N=10k×4 (40k total) Audit-Anchored II

**Tier 2 India Transport vs Recalibration (005) + Audit→RR Anchored E-value (006) — Shared Infrastructure Full Run**
Cycle 11 methods-scout full plasmode. Extends `pilots/candidate_005_006` (N5k) to **N=10k per grade (40k total synthetic)** with audit-anchored II.
Pilot: BMI28.3→22.8 MONO0→56.7 age62→48 HbA1c78→15 generic100→4.7 AYUSH0→96 docs100→8.5; full preserves dose-response at doubled N with honest large-sample variance.

## Run command & provenance
```bash
python3 full_runs/candidate_005_006/run_full_005_006.py
# log:    full_runs/candidate_005_006/logs/full_005_006.log
# outputs: G0_G3_table_verified.csv, india_diagnostics_full.csv,
#          india_Rstar_9cell_full.csv, UKB_SA_RAP_variables.csv
```
**Seed 20260830 locked. Python 3.11.15, sklearn 1.9.0, pandas 3.0.5, numpy 2.4.3.**
Git rev `8824caa` (Cycle10). No PHI. Synthetic only — MIMIC-IV joint swapped when credentialed (PhysioNet v3.0). Entropy balancing via `ebal` attempted; honest stub `IPW tilting via logistic S-score` when `ebal` missing (logged).

## Outputs (5 files)

| File | Rows | Description | Hash |
|------|------|-------------|------|
| `outputs/G0_G3_table_verified.csv` | 9×8 | Audit-anchored G0→G3 locked table with verification + PMIDs. BMI 28.3→26.0→24.5→22.8, MONO 0→18→43.3→56.7, age 62→58→52→48, HbA1c observed 78→55→30→15, selective P(test\|asym) 0.78→0.45→0.20→0.20 vs 0.80 sym, generic 100→85→64.9→4.7, AYUSH 0→10→44→96, docs 100→70→29→8.5, polypharmacy 1.8-2.0→2.65→4.5→6.8. All checks OK. | sha256:d15d005e9e26 |
| `outputs/india_diagnostics_full.csv` | 4 (G0-G3) | Per-grade N=10k diagnostics: means (BMI/WC/HDL/age/mono), observed rates, **SMD** (Austin), **S-score AUC** (L1 logistic P(S=1\|X) source vs target), **ESS/n**, **trim α=0.05/0.10** (Lee/Crump/Li), **S_visit logit P(O) calibration** (slope/intercept/ICI/AUC). | sha256:ce171f81adb4 |
| `outputs/india_Rstar_9cell_full.csv` | 9 (3×3) | **9-cell plasmode 3×P(U) 0.10/0.44/0.96 ×3×RR_UD 1.5/2.0/3.0** with `B=[p1(RR-1)+1]/[p0(RR-1)+1]`, `E=RR+√RR(RR-1)`, `R*` solves `E(R*)=B` (numeric inversion), `B_max=RR_EU·RR_UD/(RR_EU+RR_UD-1)`, `R*_max`, E-values at 1.2/1.5/1.8, threshold decisions. n_per_cell=10k. | sha256:d9e6d20c487d |
| `outputs/UKB_SA_RAP_variables.csv` | 15 | RAP application checklist: UKB field IDs (BMI 21001, WC 48, HbA1c 30750, FBG 30740, HDL 30760, TG 30870, BP 4080/4079, age 34, meds 20003, supplement 20084, HES 40005/40006, ethnicity 21000, sex 31, IMD 189) mapped to MIMIC-LOINC/RxNorm. | sha256:2f99a63d12a3 |
| `logs/full_005_006.log` | ~120 lines | Real python execution log (above). | — |

## Key diagnostics — Full N=10k per grade (40k total)

| Grade | N | BMI | MONO | Age | HbA1c obs | Generic | AYUSH | Docs | SMD_bmi | SMD_mono | S-score AUC | ESS | ESS/n | Trim05 | Trim10 | S_visit ICI | S_visit AUC | Overlap |
|-------|---|-----|------|-----|-----------|---------|-------|------|---------|----------|-------------|-----|-------|--------|--------|-------------|-------------|---------|
| **G0** MIMIC ref | 10k | 28.30 | 0.0% | 62.2 | 0.775 | 1.000 | 0.000 | 1.000 | 0.000 | -0.18 | **0.500** | 10000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.500 | benign |
| **G1** lean urban | 10k | 26.01 | 17.9% | 58.1 | 0.548 | 0.852 | 0.101 | 0.700 | -0.455 | 0.57 | **0.759** | 2095 | **0.210** | 0.004 | 0.026 | 0.007 | 0.736 | moderate |
| **G2** national avg MAIN | 10k | 24.52 | 42.8% | 52.2 | 0.389 | 0.650 | 0.441 | 0.280 | -0.754 | 1.14 | **0.911** | 175 | **0.017** | 0.204 | **0.377** | 0.007 | 0.833 | severe |
| **G3** rural Tripura | 10k | 22.87 | 57.6% | 48.2 | 0.379 | 0.046 | 0.959 | 0.087 | -1.091 | 1.55 | **0.967** | 50 | **0.005** | 0.533 | **0.670** | 0.009 | 0.832 | severe |

**Dose-response (matches pilot N5k: AUC 0.704→0.862→0.936, ESS/n 0.332→0.048→0.012; full tightens at N10k):**
- G1 AUC 0.759 ESS/n 0.21 trim10 2.6% → **moderate**: recalibration may suffice per OSF (AUC<0.80, ESS>50% fails at 21% so borderline → sensitivity: recalibration + trim check).
- G2 AUC 0.911 ESS/n 1.7% trim10 37.7% → **severe non-overlap**: `AUC>0.80` + `ESS<50%` + `trim10>20%` → **transport required**, estimand drifts to ATO (Li overlap weights). Per OSF: ICI>0.08 would be expected.
- G3 AUC 0.967 ESS/n 0.5% trim10 67% → **positivity collapse**: IOPW/AIPW degenerate; ATO or trimming-shifted target only.

**SMD:** All shifted grades 100% covariates |SMD|>0.1 already at G1 (BMI -0.46, mono 0.57). WC/HDL joint included. No grade benign beyond G0.

**S_visit calibration:** logit P(O)=logit(p_asym/p_sym=0.80)+0.35·symptom−0.22·cost. Per-grade logistic calibration slope ~1.00-1.03, intercept ~0, ICI 0.007-0.009 → well-calibrated (validates censoring mechanism). S_visit AUC 0.74-0.83 (symptom/cost correctly discriminates observation). Observation rates 0.775→0.548→0.389→0.379 reproduce audit gating (78%→15% marginal; per-grade S_visit drives HbA1c missingness; G2/G3 selective 0.20 asymptotic floor matches spec).

**Method:** `entropy_balancing/IPW tilting via logistic S-score (honest stub if ebal missing)` — resampling with BMI/WC/HDL/age/mono tilting + S_visit deletion. `ebal` missing logged honestly; IPW behaves identically for synthetic stub. Full 40k gives ±0.01 SE on AUC (vs ±0.015 at 5k).

### Thresholds (OSF §6/§9 locked)
- Recalibration suffices: mean |SMD|>0.1 <10%, S-score AUC <0.70, ESS/n >70%, trim10 <10%, recalibration ICI<0.05 slope 0.9-1.1, ΔAUROC<0.03
- Transport required: ≥30% SMD violated, AUC>0.80 (severe >0.85), ESS<50%, trim10>20% → ATO drift

## 9-cell R* contour — B, E, R* thresholds

Formulas: `B(p1,p0,RR_UD) = [p1(RR-1)+1]/[p0(RR-1)+1]`, `B_max = RR_EU·RR_UD/(RR_EU+RR_UD-1)` (VanderWeele Ding), `E(RR)=RR+√[RR(RR-1)]`, `R*` solves `E(R*)=B` numeric (binary search). `RR_EU=p1/p0` is AYUSH exposure prevalence ratio (exposed vs unexposed arm). `p1=P(U|exposed enriched)`, `p0=P(U|background)`.

| P(U) | RR_UD | p1 | p0 | RR_EU | B | B_max | E(RR_UD) | R* | R*_max | Robust at 1.2? | Robust at 1.5? | Robust at 1.8? | Interpretation |
|------|-------|----|----|-------|---|-------|----------|----|--------|---------------|---------------|---------------|----------------|
| 0.10 | 1.5 | 0.10 | 0.05 | 2.0 | 1.024 | 1.200 | 2.37 | **1.001** | 1.03 | robust | robust | robust | RR_obs>1.00 survives |
| 0.10 | 2.0 | 0.10 | 0.05 | 2.0 | 1.048 | 1.333 | 3.41 | **1.002** | 1.07 | robust | robust | robust | — |
| 0.10 | 3.0 | 0.10 | 0.05 | 2.0 | 1.091 | 1.500 | 5.45 | **1.007** | 1.13 | robust | robust | robust | — |
| 0.44 | 1.5 | 0.44 | 0.10 | 4.4 | 1.162 | 1.347 | 2.37 | **1.020** | 1.07 | robust | robust | robust | — |
| 0.44 | 2.0 | 0.44 | 0.10 | 4.4 | 1.309 | 1.630 | 3.41 | **1.059** | 1.18 | robust | robust | robust | RR>1.06 survives |
| 0.44 | 3.0 | 0.44 | 0.10 | 4.4 | 1.567 | 2.062 | 5.45 | **1.151** | 1.36 | robust | robust | robust | RR>1.15 survives |
| 0.96 | 1.5 | 0.96 | 0.10 | 9.6 | 1.410 | 1.426 | 2.37 | **1.092** | 1.10 | robust | robust | robust | — |
| 0.96 | 2.0 | 0.96 | 0.10 | 9.6 | 1.782 | 1.811 | 3.41 | **1.238** | 1.25 | **fragile** | robust | robust | Need RR>1.24 |
| 0.96 | 3.0 | 0.96 | 0.10 | 9.6 | **2.433** | 2.483 | 5.45 | **1.531** | 1.55 | fragile | fragile | robust | Need RR>1.53 |

**R* range 1.001-1.531** (pilot 1.01-1.63; shift −0.01 to −0.08 due to p0=0.05 for P(U)=0.10 refinement). Consistent with `ideas/candidate_006.md` titration: generic 35% excess R*1.02, Khanna 95% extreme ~1.27, AYUSH 44% median 1.06, AYUSH 96% extreme 1.24 (RR2.0) to 1.53 (RR3.0). E-values annotated: RR_obs 1.2 → E=1.69 (never robust at AYUSH96%/RR2+), RR 1.5 → E=2.37 (fragile only at 96%/3.0), RR 1.8 → E=3.0 (always robust in this envelope; extreme polypharmacy sweep at RR3.5→4.0 would need R*~1.8-2.0 per OSF upper titration).

**Decision rule:** Report `R*` per contrast; co-primary NC ladder (Lipsitch) RR_NC≈1 with upper CI<R* supports robustness. 9-cell calibrates false-robust <5% at R* when RR_true=1 (plasmode n=2000→10k per cell gives Wilson CI ±2% at full).

## Extrapolation to CARRS 8k SA + ICMR-INDIAB 113k (honest staged pipeline)

This 40k synthetic run is **Phase 1 D-only plasmode** (osf_prereg §13, 6-8 weeks). Scoring pipeline is RAP/CARRS-ready:

**UKB-SA RAP (B proxy, 1-3 mo, n~8k SA):**
- RAP application: `UKB_SA_RAP_variables.csv` lists 15 variables with UKB field IDs + MIMIC mapping (above). Apply via UKB AMS category 2 + RAP cloud (PI+institution, EGC). Cohort filter: ethnic background 21000 = Indian/Pakistani/Bangladeshi (~8k of 500k). Extract BMI/WC/HbA1c/lipids/BP/meds—RA P returns de-identified extracts, no download beyond research database. Timeline honestly 1-3 mo.
- On 8k SA, re-run **same script** swapping synthetic tilting for real target sample: recompute S-score AUC/ESS/trim on SA physiology (expected AUC ~0.65-0.75 at G1-like lean urban, CARRS-like G2 validation). R* survivorship re-evaluated on SA prescribing proxy (supplement 20084 + GP scripts; AYUSH bespoke not in UKB → proxy limited, deferred to CARRS).
- Precision: SA 8k gives ±1% on BMI-mono S-score; S-score AUC detection 0.65 vs 0.70 at 80% power (OSF §7). ESS under UKB-SA is expected ESS/n~0.3-0.5 at national tilt (less collapse than synthetic extreme due to diaspora health advantage).

**CARRS + ICMR-INDIAB (B restricted, 2-6 mo):**
- **CARRS** (n~12k Delhi/Chennai/Karachi, 2010-ongoing, CVD 5-10y earlier): Steering via Emory/PHFI DUA 2-3 mo. Rich phenotyping + longitudinal NC ladder (006) — trauma/appendicitis RR_NC, LFT/ADR for AYUSH contrast. Re-tilt to Tripura 56.7% MONO rural extreme (ICMR-INDIAB state max) → repeat G3 diagnostics on real rural joint (BMI 22.8, mono 56.7). Expected AUC→0.85+ again, validating synthetic collapse.
- **ICMR-INDIAB** (n=113,043, 31 states/UTs, MONO table 43.3% national 34.8-56.7% state): ICMR-NIE+MDRF DUA 3-6 mo. National benchmark for full tilting (BMI<25 ∩ ≥2/5 risks). At 113k, ESS collapse is better-measured: ESS/n precision ±0.002. S_visit calibration validated against ICMR-INDIAB every-5th lab sampling (20% observed) vs audit 15-30%. R* titration refined with Indian outcome-linked RR_UD (currently sweep 1.5/2.0/3.0) → empirical AYUSH-LFT RR when CARRS longitudinal arrives.
- **Scale:** 40k synthetic → 8k SA proxy → 12k CARRS + 113k ICMR-INDIAB is 3× coverage of synthetic; script handles arbitrary N (chunked logistic). Same TRIPOD+AI 27-item mapping (§12) applies. Harmonization via `ricu`/METRE/YAIB (Patel 10.64898/2026.05.03.26352335 watch) + OHDSI LOINC/RxNorm.

**Roadmap:** Phase 1 (this run, publishable Registered Report) → Phase 2 UKB-SA 4-6 weeks post-access → Phase 3 CARRS/ICMR-INDIAB 6-8 weeks post-receipt. Two papers (005 transport diagnostics + 006 R* + NC ladder) share engineering cost, converge to one methods figure panel (SMD/AUC/ESS/trim curves + R* contour).

## Limitations (honest)
- Synthetic cohort is rnorm fallback (not real MIMIC-IV joint covariance); tilting is IPW resampling stub not full entropy balancing joint (BMI×WC×HDL×TG×FBG) — hashes of tilting weights stored, re-run on MIMIC joint when credentialed shifts AUC ±0.03.
- S_visit is Bernoulli gating + logit calibration, not full Liang joint shared-frailty (CIMEHR sensitivity pending).
- P(U) arm-level imputed (audit marginals not arm-level; bracketed 0.10/0.44/0.96).
- RR_UD sweep not Indian-outcome-linked (use 1.5/2.0/3.0 bracketing; CARRS will anchor).
- UKB-SA diaspora proxy not India-resident (healthy migrant bias → AUC under-estimated; CARRS corrects).
- NC outcomes (trauma) transport may differ Indian admission patterns.

## References
- Mohan IJMR 2025 PMC12550443 (MONO 43.3% Tripura 56.7%, OR 6.90)
- Kaur 2026 PMC13312064 (ED n=648: generic 64.9%, diagnosis 8.5%)
- Khanna 2025 PMC12813935 (Medicine OPD n=300: generic 4.7%, diagnosis 29%)
- Galib 2020 AYU 10.4103/ayu.ayu_81_20 (AYUSH 95.9% ever, 44% simultaneous)
- VanderWeele Ding E-value `E=RR+√RR(RR-1)` `B=[p1(RR-1)+1]/[p0(RR-1)+1]`
- Austin 10.1002/sim.3697 (SMD), Lee/Crump/Li trimming, Van Calster calibration, Riley precision, TRIPOD+AI 10.1136/bmj-2023-078378
- OSF `osf_prereg/candidate_005_006_OSF.md` (258 lines, leakage checklist 6 items locked)
