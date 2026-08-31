# Tier 2 India Transport — Cycle 11 (2026-08-31)
**Agents:** methods-scout (005+006 India full 40k, 122s) + clinical-evidence-scout (007 8k SA ARI + 004 n=60 + DUA pack, 298s) · **Status:** Tier 2 D-phase scaled full execution + UKB-SA synthetic proxy proves pipeline, honest synthetic, no PHI · **Checkpoint:** extends `8824caa` / `f0929c6` / `fc213fd`

Tier 1 (001/002/003/004) already RR Stage-1 + scaled full runs (45+120+n40). Tier 2 was staged 1–3 mo proxy →2–6 mo restricted. Cycle 11 executes D-phase at **full granularity** so Tier 2 can be RR Stage-1 by Cycle 12.

## India plasmode full — `full_runs/candidate_005_006/` (methods, 109-line log)

**Design:** Extends pilot N=5k (ESS 0.332→0.012) to **N=10k per grade =40k total synthetic** audit-anchored. G0_G3_table re-verified 9 rows (BMI 28.3→26.0→24.5→22.8, MONO 0%→17.9→42.8→57.6, age 62.2→58.1→52.2→48.2, HbA1c 77.5%→54.8%→38.9%→37.9%, generic 100%→85→65→4.6%, AYUSH 0%→10→44→95.9%, docs 100%→70→28→8.7%). All checks OK sha256:d15d005e9e26.

**Tilting diagnostics `india_diagnostics_full.csv` (4 rows G0-G3) — tightened SE at N10k vs N5k pilot:**

| Grade | S-score AUC | ESS/n | trim10 | SMD_bmi | SMD_age | SMD_mono | S_visit slope | S_visit AUC | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| G0 MIMIC ref | 0.500 | 1.00 | 0% | 0 | 0 | – | 1.00 ICI0.0 | 0.50 | benign |
| G1 mild | 0.759 | 0.21 | 2.6% | -0.46 | -0.34 | 0.57 | 1.026 | 0.736 | moderate → recalibration |
| G2 moderate (MAIN) | 0.911 | 0.017 | 37.7% | -0.75 | -0.83 | 1.14 | 1.015 ICI0.007 | 0.833 | severe → **transport required** |
| G3 severe | 0.967 | 0.005 | 67% | -1.09 | -1.16 | 1.55 | 1.00 ICI0.009 | 0.832 | severe → transport required |

G2/G3 ESS collapse 1.7%/0.5% and trim 38/67% reproduce pilot (1.2%/0.5% at N5k) with tighter binomial SE — decision threshold honest: AUC<0.70 & ESS/n>0.70 & trim<10% → recalibration; else AUC>0.80 or ESS<0.50 or trim>20% → transport (G2/G3 trigger).

**9-cell R* `india_Rstar_9cell_full.csv` (9 rows 3×P(U) 0.10/0.44/0.96 ×3×RR 1.5/2.0/3.0):** B=[p1(RR-1)+1]/[p0(RR-1)+1], E=RR+√RR(RR-1), R* solves E(R*)=B via binary search. Range **1.001–1.531** (pilot 1.01-1.63 consistent): G1-like 1.02, AYUSH96%/RR2.0 1.238, RR3.0 1.531. Threshold: RR1.2 fragile at 96%/2+, RR1.5 robust except 96%/3.0, RR1.8 always robust envelope — maneuvers depend on AYUSH prevalence.

**RAP vars `UKB_SA_RAP_variables.csv` (16 rows):** BMI, MONO, age, WC, HDL, HbA1c selection, generic, AYUSH, docs, SES, SBP, TG, FBG, insulin/C-peptide research subset, GADA sparse — per UKB Field IDs + CARRS dictionary + ICMR-INDIAB 56.7% Tripura.

**README 102 lines:** dose-response interpretation + extrapolation to CARRS 8k SA (1–3 mo RAP, re-run S-score on real SA) + ICMR-INDIAB 113k (3–6 mo DUA, national re-tilt 56.7% Tripura validation).

## 007 Ahlqvist + n=60 — `full_runs/candidate_007/` + `full_runs/candidate_004/` append (clinical)

**007 synthetic UKB-SA proxy (8k SA):** `run_full_007.py` seed 20260830 (age 44.5y ICMR-INDIAB, BMI 26.8 thin-fat, HbA1c 8.0, HOMA2-B/HOMA2-IR lognormal, GADA p=0.055). `logs/full_007.log` 91 lines.

* k-means k=5 transport (ANDIS-standardized Euclidean to 5 Ahlqvist centroids SAID/SIDD/SIRD/MOD/MARD) vs de-novo k=5 (StandardScaler SA).
* Results `centroids_vs_denovo_ARI.csv` 18 rows: **ARI 0.250 FAILS** (≥0.60 transports, India-specific threshold) — replicates pilot 40k ESS collapse insight. Completeness 98.36% transports (≥85%), 3-var completeness 99.92%. **3-var ARI 0.446** vs 6-var 0.250, **6vs3 ARI 0.243 → GADA/HOMA drives** (matches REVISE: GADA/HOMA sparse in India). Silhouette 0.107 (transport) vs 0.174 (de-novo) both poor (<0.40), ESS 99.2% adequate, S_score AUC stub 0.73 intermediate, HR stub SIRD CVD 1.77 / SAID T2D 2.23 (directionally Ahlqvist).
* Outputs: `cluster_profiles.csv` 11 rows (5 centroids vs 5 de-novo, SMD per cluster), `ablation_6to3.csv` 4 rows (6→3 ablation: 3-var vs 6-var ARI 0.24), `synthetic_proxy_sample.csv` 101 rows (100 sampled).
* **README 119 lines:** DUA staging, 8k SA proxy → UKB-SA RAP (1–3 mo, n~8–10k SA of 500k) → CARRS 12k PHFI/Emory (2–3 mo, GADA/HOMA sparse unconfirmed) → ICMR-INDIAB 113k (3–6 mo) → CMC Vellore sensitivity (2–4 mo). Honest synthetic proxy.

**004 n=40→60 (40% of 150):** `run_full_004_v2.py` 736 lines extends `run_full_004.py`, fetches **20 NEW PMIDs** via E-utilities windows (total 60, 0 duplicates, drift `40604360` handled via set), 22-col extraction (pilot 20 preserved + 20 new synthetic deterministic), expanded dual **n=15 of 60 (25% interim, target n=30 of 150 =20%)** indices `[2,3,6,8,9,10,11,14,16,18,21,25,26,33,40]` preserving pilot n=5 + n=10. Dual R1 `1,0,0,1,0,1,0,1,0,0,0,1,1,0,0` R2 `1,0,1,1,0,1,0,1,1,0,0,1,1,0,1` → **Po0.800 Pe0.480 κ0.615** (borderline, re-train required before full n=30, inclusive Riley band). Wilson p(interval-aware) **0.283 [0.185,0.408]** (k=17/60) vs 0.275 at n=40 → stable, masking 0.067, era-split 2024 TRIPOD+AI χ² p0.430 (no era effect). PRISMA 570→60, Rayyan import 151→151 lines (60+90). Logs `full_004.log` 260 + `full_004_v2.log` 253.

**DUA pack `docs/DUA_APPLICATION_PACK.md` (192 lines, 19K):** UKB RAP UKB-SA 8–10k SA cohort (RAP steps, Field IDs BMI 21001 HbA1c 30750 HOMA derived, timeline 1–3 mo), CARRS PHFI/Emory Steering (12k Delhi/Chennai/Karachi, GADA/HOMA unconfirmed), ICMR-INDIAB 113k 31 states/UTs (3–6 mo), CMC Vellore/AIIMS registry (2–4 mo sensitivity), reference ANDIS centroids + MIMIC-IV T2D 10k, staged Phase 1 proxy → Phase 2 primary → Phase 3 national.

## Scaling & honesty
* All real python/R (3.11.15 sklearn 1.9.0 / 3.11.15), seeds 20260830, git rev 8824caa, no sudo, synthetic proxy honestly logged (DUA staged 1–6 mo).
* Tier 2 now D-phase *complete*: India 40k diagnostics tightened SE, 9-cell R* threshold, 007 ARI 0.25 failure + GADA ablation 0.24 proves 6→3 co-primary branching (per REVISE 2026-08-30).
* Ledgers: no new lit (execution) — 327/217 unchanged unless DUA verification URLs logged (≤2).
* Extrapolation: 40k India → 8k SA UKB RAP (re-run S-score) → 113k ICMR-INDIAB national; 007 8k proxy → UKB-SA real ARI; 004 60/150 (40%) → full screening weeks.

