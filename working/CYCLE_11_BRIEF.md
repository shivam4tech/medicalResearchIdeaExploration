# Cycle 11 — Tier 2 India Transport + 007 Ahlqvist + n=150 Completion Prep
Companion: shortlist/SHORTLIST.md TIER 2 (005+006 paired G0->G3, STRESSES-ASSUMPTION) + TIER 3 (007), osf_prereg/candidate_005_006_OSF.md 258 lines + candidate_007_OSF.md 205 lines, pilots/candidate_005_006 (99-line log, G0_G3_table 9 rows, ESS collapse 0.332->0.012), full_runs 45+120+n40 (8824caa/f0929c6), rr_stage1 4 packs fc213fd. Git rev 8824caa. Adversarial MONITOR.

**Why this cycle:** Tier 1 (001/002/003/004) now RR Stage-1 frozen + scaled full runs proven toward N. Tier 2 India was staged pending UKB-SA/CARRS DUAs (SHORTLIST: proxy 1–3 mo → restricted 2–6 mo). Cycle 11 executes D-phase India plasmode at full granularity + 007 centroids vs de-novo on UKB-SA proxy data (synthetic UKB-SA 8k SA EHR when DUA not yet), and pushes 004 to n=80 (of 150) midpoint — so Tier 2 is submission-ready by Cycle 12.

## Binding constraints (same pool, no sudo, no PHI)
- Pool muse-spark-1.2-contributor-free ~40/min target ≤24 ceiling30 max2 concurrent. Compute is synthetic India tilting (N=10k×4 grades) + 007 IOPW (N=8k SA proxy) + 004 20 extra screens — bounded, no MIMIC-IV credential needed (synthetic honestly logged).
- No sudo/pkexec — R ~/R/library, python hermes venv. UKB-SA/CARRS remain staged: produce `docs/DUA_APPLICATION_PACK.md` (RAP application checklist + CARRS contact + variables needed: BMI/MONO/HbA1c/AYUSH/generic/docs age) not the data itself.
- Real python/R logs + CSVs + seeds 20260830 required. Checkpoint early. At most 1–2 verification searches verbatim (e.g., UKB RAP portal URL) if needed.

## Assignments (2 scouts, compute+clinical)

### methods-scout → 005+006 G0->G3 full plasmode + R* 9-cell full (compute India)
1. **005+006 India tilting full:** Extend pilots/candidate_005_006 (N=5k ESS 0.332->0.012, R* 1.01-1.63, 9-cell) to **N=10k per grade (40k total synthetic)** using audit-anchored G0_G3_table (BMI 28.3->22.8 MONO 0->56.7% etc) with entropy-balancing/IPW tilting (or synthetic resampling stub if ebal not available). Compute per-grade diagnostics SMD/S-score AUC/ESS, trim10, S_visit logit P(O) calibration, then 9-cell plasmode (3×P(U) 0.10/0.44/0.96 ×3×RR_UD 1.5/2.0/3.0) full R* contour with B=[p1(RR-1)+1]/[p0(RR-1)+1], E=RR+√RR(RR-1), threshold 9-cell sensitivity. Deliver `full_runs/candidate_005_006/` with `run_full_005_006.py` + `logs/full_005_006.log` + `outputs/G0_G3_table_verified.csv` + `outputs/india_diagnostics_full.csv` (4 rows) + `outputs/india_Rstar_9cell_full.csv` (9 rows) + `outputs/UKB_SA_RAP_variables.csv` + README extrapolation to full CARRS validation (40k → 8k SA + 113k ICMR-INDIAB).

### clinical-evidence-scout → 007 Ahlqvist + 004 n=40→80 + DUA pack (clinical + literature)
2. **007 Ahlqvist centroids vs de-novo IOPW:** From osf_prereg/candidate_007_OSF.md (205 lines, centroids vs de-novo, ARI≥0.60, C-peptide/HDL European gap IMI-RHAPSODY, IndMED 0 hits, CARRS GADA pending, 6→3 ablation), build **N=8k synthetic UKB-SA proxy** (age/BMI/HbA1c/HOMA2-B/HOMA2-IR/GADA simulation per Ahlqvist 2018 + ICMR-INDIAB age distribution) — honest synthetic proxy (DUA staged). Run k-means 5 clusters centroids (European) vs de-novo k=5 on SA proxy, compute ARI, cluster-wise SMD, completeness 85% threshold, GADA-free 6→3 ablation ARI, outcome association (CVD/T2D HR stub). Deliver `full_runs/candidate_007/` with `run_full_007.py` + `logs/full_007.log` + `outputs/centroids_vs_denovo_ARI.csv` + `outputs/cluster_profiles.csv` + `outputs/ablation_6to3.csv` + README with DUA staging.
3. **004 n=40→80 completion + DUA pack:** Extend full_runs/candidate_004 n=40 (κ0.615) with **20 NEW PMIDs** (total 60 of 150, 40% midpoint) via E-utilities, update 22-col extraction, n=15 overlap (of n=30 target) interim κ + Wilson + era-split update, refreshed PRISMA 570→60, Rayyan import update (60+90). Plus draft `docs/DUA_APPLICATION_PACK.md` (UK Biobank RAP UKB-SA 8-10k SA cohort application steps, CARRS PHFI/Emory contact, ICMR-INDIAB 113k, variables needed: BMI, MONO, HbA1c selection, AYUSH, generic/docs, timeline 1-3 mo proxy →2-6 mo restricted). Deliver updated `full_runs/candidate_004/` append + DUA doc. Checkpoint early, real E-utilities.

## Output contract
- `full_runs/candidate_005_006/` 5 outputs + log + README (India diagnostics + 9-cell + RAP vars)
- `full_runs/candidate_007/` 3+ outputs + log + README (ARI + ablation, honest synthetic proxy)
- `full_runs/candidate_004/` extended to 60 + `docs/DUA_APPLICATION_PACK.md` (DUA pack)
- All real execution, seeds 20260830, git rev 8824caa, hashes logged; extrapolation to full N honest; no phi.

## Non-goals
Actual UKB-SA data release (requires RAP 1–3 mo) — synthetic proxy proves pipeline; full n=150 screening completes over weeks.

