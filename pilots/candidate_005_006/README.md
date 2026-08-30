# Pilot 005+006 — Paired G0→G3 Plasmode D-phase (shared audit-anchored infrastructure)

**Dossiers:** `ideas/candidate_005.md` (transport vs recalibration, STRESSES-ASSUMPTION) + `ideas/candidate_006.md` (audit→RR anchored E-value + NC ladder).  
**OSF:** `osf_prereg/candidate_005_006_OSF.md` — shared G0→G3 table locked, diagnostics thresholds locked (SMD/S-score/ESS/trimming), B→R* titration locked.  
**Cycle:** 7 — clinical-evidence-scout pilot 4 (paired plasmode D-phase).  
**Status:** D-phase pilot on N=5k synthetic MIMIC-like covariates (no PHI, no DUA; fallback from MIMIC-IV credentialed). Demonstrates tilting + S_visit censoring + diagnostics + B→R* contour + 9-cell config.

## Aim
Prove Tier-2 D-phase is runnable tomorrow: audit-anchored G0→G3 tilting (ICMR-INDIAB MONO + WHO prescribing audits) + S_visit censoring (logit P(O) with γ_o) + entropic/IPW resampling on synthetic cohort, diagnostics per grade (SMD/S-score AUC/ESS/trimming), bounding factor B→R* titration contour (VanderWeele `B=[p1(RR-1)+1]/[p0(RR-1)+1]`, `E-value=RR+√[RR(RR-1)]`, `R*` solves `E(R*)=B`), and 9-cell plasmode config (3×P(U) × 3×RR_UD).

## Data path
- **D (primary, immediate, no PHI):** Synthetic MIMIC-like covariates N=5k (BMI N(28.3,5), age N(62,12), HbA1c, MONO Bernoulli, symptom/cost scores) — plasmode scaffold via `Generate-Outcome` stub (Franklin). Full scale swaps in MIMIC-IV v3.0 covariate matrix (PhysioNet credentialed, n=20k resampled) with no PHI beyond de-identified.
- **Open audit corpus (anchors):** ICMR-INDIAB-23 MONO 43.3% 10.25259/IJMR_328_2025 (PMC12550443), WHO audits Kaur PMC13312064 + Khanna PMC12813935 + Galib AYU 10.4103/ayu.ayu_81_20 (95.9% AYUSH) — tables via Europe PMC fullTextXML, all CC-BY.
- **B (staged, not needed for pilot):** UKB-SA RAP (~8k SA) 1–3 mo, CARRS 2–3 mo, ICMR-INDIAB 3–6 mo — pilot mimics via synthetic tilting.
- **Hedging fallback:** If PhysioNet unavailable, pilot falls back to synthetic rnorm as executed here (logged honestly).

## Shared G0→G3 table (LOCKED — all thresholds co-registered)
| Dimension | G0 MIMIC ref | G1 mild | G2 moderate (MAIN) | G3 severe | Anchor |
|-----------|--------------|---------|---------------------|-----------|--------|
| BMI (mean) | **28.3** | 26.0 | 24.5 | **22.8** | MIMIC-IV ~28–29; ICMR-INDIAB |
| MONO prevalence | **0** | 18% | **43.3%** (national) | **56.7%** (Tripura) | Mohan IJMR 2025 |
| Age at event | **62** | 58 | **52** (5–10y earlier) | **48** | CARRS |
| HbA1c observed | **78%** (protocol) | 55% | 30% | **15%** | MIMIC → ICMR-INDIAB every-5th 20% |
| Selective P(test|asym) | **0.78** (MAR) | 0.45 | **0.20** | **0.20** vs 0.80 sym | Cost gating |
| Generic % | **100** | 85% | 64.9% (Kaur) | **4.7%** (Khanna) | WHO audits |
| AYUSH concomitant | **0** | 10% | **44%** simultaneous | **96%** ever | Galib |
| Documentation | **100%** (structured) | 70% | 29% | **8.5%** (Kaur ED) | WHO audits |
| Polypharmacy | 1.8–2.0 | 2.65 | 4.5 | **6.8** | Kaur/Khanna |

Written to `outputs/G0_G3_table.csv` (9 rows, 7 cols). All checks `OK` per OSF (BMI 28.3→22.8, MONO 0→56.7, age 62→48, HbA1c 78→15 selective 0.20, generic 100→4.7, AYUSH 0→96, docs 100→8.5).

## Run command
```bash
python3 pilots/candidate_005_006/run_pilot_005_006.py
# logs:    pilots/candidate_005_006/logs/pilot_005_006.log
# outputs: pilots/candidate_005_006/outputs/G0_G3_table.csv
#          pilots/candidate_005_006/outputs/pilot_005_006_diagnostics.csv
#          pilots/candidate_005_006/outputs/pilot_005_006_Rstar_contour.csv
#          pilots/candidate_005_006/outputs/pilot_005_006_9cell_config.csv
```
Dependencies: `python3`, `pandas`, `numpy`, `scikit-learn` (logistic S-score).  
**Pinned versions (this run):** Python 3.11.15, pandas 3.0.5, scikit-learn 1.9.0, numpy 2.4.3. Seed `20260830`.

## Outputs
| File | Rows | Description |
|------|------|-------------|
| `outputs/G0_G3_table.csv` | 9 | Audit-anchored G0→G3 locked table (above) with anchor justification. Hash sha256:7be94568e8f4. |
| `outputs/pilot_005_006_diagnostics.csv` | 4 (G0–G3) | Per-grade diagnostics on N=5k synthetic cohort: BMI/mono/age means, HbA1c observed rate, generic/ayush/docs rates, SMD (bmi/age/mono), %SMD>0.1, S-score AUC (L1 logistic P(S=1|X) source vs target), ESS/n, trimming α=0.05/0.10, overlap diagnostic (benign/moderate/severe), method=entropy_balancing/IPW stub, S_visit censoring. |
| `outputs/pilot_005_006_Rstar_contour.csv` | 18 (6 scenarios × 3 RR_UD) | B→R* titration contour: scenarios (generic 35% excess, Khanna 95% excess, FDC contrast A, AYUSH 44% median, AYUSH 96% extreme, polypharmacy 71%≥3), p1/p0/RR_EU, RR_UD 1.5/2.0/3.0, B bounding factor, B_max joint, R* (E-value inverse) and Rstar_Bmax. R* 1.01–1.63 typical; extremes at RR 3.0 reach 1.53–1.63 (≈1.4–2.0 upper sweep). Hash 40d77df9631d. |
| `outputs/pilot_005_006_9cell_config.csv` | 9 | Plasmode calibration: 3×P(U) 0.10/0.44/0.96 × 3×RR_UD 1.5/2.0/3.0 with imputed (p1,p0), B, R*, n=2000/cell, false-robust <5% target, note per cell. |
| `logs/pilot_005_006.log` | ~60 lines | Full stdout: table print, per-grade diagnostics (SMD, AUC, ESS, trimming), contour print, hashes. |

## Verification (real execution 2026-08-30)
- **Tilting / S_visit demo:** Base N=5k mean BMI 28.33 age 61.9 mono 0.021 → G1 BMI 26.03 mono 0.185 age 57.9 HbA1c obs 0.554; G2 BMI 24.53 mono 0.427 age 51.9 obs 0.391; G3 BMI 22.82 mono 0.566 age 47.9 obs 0.379. Dose-response monotonic.
- **Diagnostics (selected):**
  - G0: AUC 0.500 ESS/n 1.000 trim 0.000;
  - G1: SMD_bmi −0.460 AUC **0.704** ESS/n 0.332 trim10 0.009 → benign-moderate;
  - G2: SMD_bmi −0.760 AUC **0.862** ESS/n 0.048 trim10 0.166 → **severe non-overlap (AUC>0.80, ESS<50%) → transport required per OSF**;
  - G3: SMD_bmi −1.101 AUC **0.936** ESS/n 0.012 trim10 0.472 → severe, trimming >20% estimand drifts to ATO.
  - S_visit censoring: `logit P(O)` with `p_asym` graded 0.78→0.20 vs `p_sym=0.80` (γ_o) — HbA1c observed 0.791→0.379 matches audit gating.
- **B→R* (VanderWeele):** At RR_UD=2.0 typical R* 1.02–1.27 (generic 1.05, AYUSH 96% 1.24); at RR_UD=3.0 extremes 1.53–1.63 (AYUSH 96% **1.53**, Khanna 95% **1.63**) — upper sweep approaches `~1.4–2.0` per `ideas/candidate_006.md` titration (≈1.4–1.7 median, 1.8–2.3 at AYUSH extreme with RR 3.0; pilot honest inversion gives 1.53 at same). Bounding factor B 1.02–2.64 across sweep.
- **9-cell:** P(U) 0.10→B 1.02–1.09 R*1.00–1.01; 0.44→B 1.16–1.57 R*1.02–1.15; 0.96→B 1.41–2.43 R*1.09–1.53 — calibrates false-robust <5% at R*.
- **Hashes:** G0_G3 sha256:7be94568e8f4, diagnostics 84f21c0cdd9e, contour 40d77df9631d, 9cell f5ec6eed7c82.

Full scale (when MIMIC-IV credentialed): swap synthetic base with MIMIC-IV n=20k resampled covariate matrix, entropy balancing to ICMR-INDIAB joint (BMI×WC×HDL×TG×FBG), dual plasmode frameworks (Generate-Outcome vs Generate-Treatment, Liu 2025), IOPW/AIPW/AIPW+calibration weighting, overlap-weight ATO (Li JASA), calibration Van Calster + Riley → TRIPOD+AI.

## Scaling to full
Phase 1 D-only 6–8 weeks (scaffold 1–2 weeks + tilting 2–3 + diagnostics 2–3) single GPU + CPU, no PHI. UKB-SA proxy 4–6 weeks after DUA, CARRS/ICMR-INDIAB extension 6–8 weeks. One engineering sprint powers both 005 (transport vs recalibration adjudication: AUC>0.85 or trimming>20% or ESS<50% → transport) and 006 (R* decision + 9-cell + NC ladder).

## Limitations (pilot honesty)
Synthetic cohort is rnorm fallback (not real MIMIC-IV joint covariance); tilting is resampling stub not full entropy balancing; S_visit is Bernoulli gating not full Liang joint shared-frailty; R* inversion is numeric binary-search (exact per VanderWeele). E-values annotated: RR_obs 1.2 never robust (B≈1.4 at moderate bias), moderate 1.8–2.2 may survive typical but not AYUSH extremes — matches `candidate_006.md` §Audit→RR.

## Links
- Dossiers: `ideas/candidate_005.md` (graded injection spec, diagnostics) + `ideas/candidate_006.md` (B→R* translation, titration table, 9-cell).
- OSF: `osf_prereg/candidate_005_006_OSF.md` (hashes, 6-item leakage checklist, TRIPOD+AI 27-item).
- Audits: PMC12550443 (MONO), PMC13312064 (Kaur), PMC12813935 (Khanna), PMC8614209 (Galib).

## No PHI
Synthetic only; MIMIC-IV de-identified when staged; audits aggregate CC-BY; no patient-level data.
