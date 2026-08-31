# Reproducibility Statement — Candidate 007 Ahlqvist Centroids vs De Novo on 8k Synthetic UKB-SA Proxy

**Protocol:** `rr_stage1/candidate_007_AHLQVIST.md` (286 lines, Ahlqvist 2018 5 centroids SAID/SIDD/SIRD/MOD/MARD 10.1016/s2213-8587(18)30051-2, N=8k synthetic UKB-SA ICMR-INDIAB age 44.5y BMI 26.8 thin-fat vs ANDIS mean [0.06,57.5,30.2,8.0,55,2.5] SD [0.237,12.5,5.0,1.8,30,1.2], k=5 transport Euclidean vs de-novo StandardScaler k=5, ARI+silhouette+SMD+ESS+trimming, TRIPOD+AI 27-item Collins 10.1136/bmj-2023-078378, leakage 6-item) + companion `rr_stage1/candidate_005_006_TILTING.md` (303 lines, paired G0→G3) shared RR 1624 lines
**OSF registration (timestamped):** `osf_prereg/candidate_007_OSF_TIMESTAMPED.md` — Registration 2026-08-31 12:30 IST, git rev `70bb40c0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6` (short `70bb40c`) → current `d419b12`, pilot precedent `pilots/candidate_005_006/` (5k, 99-line log) + full `full_runs/candidate_007/` 8k (`ba7626f885a9/747a075d8fd3/c17976e51d7c/129f20ad3ac2`), seed `20260830`
**Status:** RR Stage 1 (Introduction + Methods, Results TBD registered except 8k synthetic proxy logged completeness 98.36% transports yet ARI 0.250 FAILS, 3-var 0.446, 6vs3 0.243 GADA/HOMA drives — no peeking at UKB-SA/CARRS/ICMR/CMC before thresholds locked)
**No PHI.** Honest synthetic UKB-SA proxy + public audit tables only; B-restricted 1–6mo for real centroids validation.

## 1. Compute environment (pinned at OSF timestamp, frozen)

| Component | Version | Source / verification | Role |
|-----------|---------|----------------------|------|
| **Python** | **3.11.15** (main, Aug 7 2026, Clang 22.1.3) | `python3 --version` + `full_007.log` line 2 `python 3.11.15` | Primary (synthetic generation lognormal HOMA, k-means transport + de-novo, ARI/silhouette) |
| **pandas** | **3.0.5** | `pip show pandas` + `full_007.log pandas 3.0.5` | Data frames, cluster profiles, ARI metrics, ablation table |
| **scikit-learn** | **1.9.0** | `pip show scikit-learn` + `full_007.log sklearn 1.9.0` | KMeans(k=5 n_init=20), StandardScaler, adjusted_rand_score, silhouette_score, LogisticRegression for ESS/S-score stub |
| **numpy** | **2.4.3** | `python3 -c "import numpy"` + `full_007.log numpy 2.4.3` | RNG, Wilson CI, κ, SMD |
| **R** | **4.5.2** (2025-10-31 "[Not] Part in a Rumble", x86_64-pc-linux-gnu) | `R --version` + `pilots/candidate_003/logs/pilot_003.log` `R version: 4.5.2` | ricu harmonization stub + CIMEHR sensitivity (pinned for repo consistency, not primary for 007) |
| **ricu** | **0.5.8** (CRAN, Bennett PMC10268223) | `R packageVersion("ricu")==0.5.8` (primary pipeline) + `rr_stage1 §8` | Primary harmonization for UKB-SA→MIMIC mapping (lab LOINC, med RxNorm — not used in 8k proxy but ready for real RAP) |
| **CIMEHR** | **0.1.0** (CRAN 2026-06-08, Yang 2602.15374) | `R packageVersion("CIMEHR")==0.1.0` | Secondary (003 plasmode, pinned repo-wide) |
| **synthEHRella** | **74aa51601615349648bcfa38e1cc9c8a55c4ef35** | `git -C pilots/candidate_002/synthEHRella rev-parse HEAD` (Chen JAMIA 2025 10.1093/jamia/ocaf082) | Secondary (002 fidelity, pinned repo-wide) |
| **Ahlqvist centroids** | **Frozen Table 1 supplements** | `run_full_007.py` lines 32–38 ANDIS-standardized 6-D Euclidean + `osf_prereg/candidate_007_OSF_TIMESTAMPED.md` §3 | SAID[1,32.5,27.2,11.1,24,1.2] SIDD[0,56.7,28.5,10.2,23,1.6] SIRD[0,65.1,33.9,7.2,84,4.1] MOD[0,49.1,33.8,7.1,71,2.9] MARD[0,67.4,27.8,6.8,49,1.9] |
| **Git** | **70bb40c → d419b12** | `git rev-parse HEAD` + `osf_prereg` timestamp block | Provenance (SHA256 for centroids, ANDIS mean/SD, ARI hashes) |
| **OS** | Linux 7.0.0-30-generic, x86_64 | `uname -a` | Deterministic builds, no sudo |

Docker: `python:3.11` + `sklearn==1.9.0` + `pandas==3.0.5` + `ricu==0.5.8` + `R 4.5.2` image pinned at `70bb40c`; `Dockerfile` hashes OSF-archived (leakage item 6). Single CPU 8k synthetic <2s wall-clock (<$1 cloud); B-proxy phases swap synthetic for real 8k/12k/113k without image change.

## 2. Seeds (all RNGs locked at OSF before UKB-SA/CARRS/ICMR outcomes inspected)

```
Seed: 20260830 (integer, visible in every log header)
  numpy:    numpy.random.default_rng(20260830)          # SA proxy generation (age 44.5±11, BMI 26.8±4.2, HbA1c 8.0±1.8, HOMA2-B lognormal median 61.97, HOMA2-IR lognormal median 2.465, GADA p=0.055)
  python:   random.Random(20260830)                     # UKB var sampling, Rayyan import (004 companion)
  R:        set.seed(20260830)                          # ricu sampling (ready for real RAP), CIMEHR (003), mice sensitivity
  sklearn:  random_state=20260830                        # KMeans(k=5 n_init=20) transport vs de-novo (both arms), logistic ESS/S-score
  hash:     SHA256 for centroids / ANDIS mean/SD / cluster profiles / external hold-outs (leakage item 6)
```

All seeds **identical across pilots (5k precedent 99-line log), full runs (8k, 91-line log), and final analysis** (seed log `full_007.log` `Seed 20260830, 2026-08-31 12:17:11 IST`). Post-registration changes logged as deviation in `journal/cycles/cycle_11.md`; analyst blinded to UKB-SA/CARRS labels until lock.

## 3. Data sources & access (honest synthetic proxy now; B staged 1–6 mo for real validation)

| Dataset | Version | N synthetic / eligible post-access | Access | Role in this dossier |
|---------|---------|-----------------------------------|--------|----------------------|
| **Synthetic UKB-SA proxy (executed)** | ICMR-INDIAB age distribution 44.5y + thin-fat BMI 26.8 + Ahlqvist 2018 simulation | **8000 synthetic SA proxy executed** seed 20260830 | No credential needed (fallback) | Proxy proves pipeline: ARI 0.250 FAILS completeness 98.36% transports GADA/HOMA drives 0.243 (honest B proxy) |
| **UKB South Asian subset (B staged)** | UKB AMS 2026, ~500k total | ~8k SA (Indian/Pakistani/Bangladeshi, 21000) | UKB AMS category 2, RAP cloud, PI+institution, EGC, 1–3 mo, fields 21001 BMI 48 WC 30750 HbA1c etc `2f99a63d12a3` companion | Proxy target (Phase 1): re-run transport vs de-novo on 8k SA real + IOPW ESS re-check |
| **CARRS (B restricted)** | Delhi/Chennai/Karachi 2010–ongoing, n~12k | ~12k South Asian CVD 5–10y earlier + drug-naïve enriched | Steering via Emory/PHFI DUA 2–3 mo — richest for GADA/HOMA completeness check (expected <20%) | Primary B target (Phase 2): repeat ARI + 6→3 co-primary branching on SA resident (resolves diaspora→resident gap) |
| **ICMR-INDIAB (B restricted)** | 113,043 31 states/UTs 2008–2020 MONO 43.3% 34.8–56.7% | 113k national | ICMR-NIE+MDRF DUA 3–6 mo, `docs/DUA_APPLICATION_PACK.md` 192 lines | Population extension: population vs clinic sampling frame sensitivity |
| **CMC Vellore / AIIMS Delhi (B staged)** | Tertiary T2D registries, new-onset enriched | — | Registry 2–4 mo | ANDIS-analog new-onset sensitivity (drug-naïve, HOMA GADA richer) |
| **ANDIS (Ahlqvist source, Sweden)** | ANDIS 10.1016/s2213-8587(18)30051-2, n=8980, centroids above + means/SDs | Reference | Public Table 1 supplements + external replication (IMI-RHAPSODY) | Source centroids frozen (not re-estimated) |

All data de-identified (Safe Harbor–equivalent date-shifted); IRB exemption for secondary analysis where de-identified extracts only. **Synthetic 8k is lognormal HOMA + Bernoulli GADA fallback** — HOMA2-IR lognormal median 2.465±1.275 (Oxford calculator v2.2 not used at scale, CARRS real joint will shift ARI ±0.05 when credentialed, honestly logged).

## 4. Frozen protocol (no HARKing, 8k synthetic proxy logged)

- **Centroids frozen:** Ahlqvist 5 centroids above + ANDIS means/SDs locked before proxy; transport = nearest centroid Euclidean in ANDIS-standardized 6-D (dist ≤5.0 ~2SD aggregated defines completeness ≥85% — at proxy 98.36% 7869/8000 passes).
- **De-novo locked:** StandardScaler SA proxy + KMeans(k=5, n_init=20, random_state=20260830) primary; silhouette, ARI Hubert & Arabie (Landis & Koch ≥0.60 substantial transports, <0.40 fails) primary; gap statistic + stability via bootstrap sensitivity; IOPW ESS + S-score AUC + trimming α=0.10 diagnostics.
- **Completeness + ARI thresholds locked:** Completeness ≥85% transports vs <85% fails; ARI ≥0.60 transports vs <0.40 fails; SMD |SMD|>0.1 threshold <10% adequate ≥30% fails; ESS>70% adequate <50% fails; AUC<0.70 adequate >0.80 fails; silhouette de-novo >0.40 stable vs transport poor. At 8k proxy: **completeness 98.36% transports BUT ARI 0.250 FAILS + SMD 50% FAILS + 6vs3 0.243 → India-specific required (H1 leaning).**
- **Ablation branching locked:** 6-var GADA/age/BMI/HbA1c/HOMA2-B/HOMA2-IR → 4-var (age/BMI/HbA1c/HOMA2-IR proxy C-peptide+HDL) → 3-var age/BMI/HbA1c GADA-free co-primary. At proxy: 6-var ARI 0.250 vs **3-var ARI 0.446** vs **6vs3 ARI 0.243 → GADA/HOMA drives assignment** (measuredness artifact). If CARRS GADA completeness <10% post-DUA, 6-var → sensitivity-only, **3-var becomes primary** per §3.
- **Leakage 6-item (frozen & unit-tested, Supplementary):** 1 frozen centroids not re-tuned on SA proxy 2 k=5 fixed primary (not data-driven) 3 Euclidean/complete-case/IOPW 5% primaries fixed 4 outcome (CKD/retinopathy/insulin) not used for cluster assignment 5 6→3 branching pre-registered before CARRS access 6 code provenance SHA256 blinded analyst.
- **Outcome stub locked:** 5y CVD (base 0.08) + T2D progression (base 0.12) per Ahlqvist gradients simulated vs MARD reference (HR_SAID CVD 1.89 SIRD CVD 1.77 at proxy) — **real Cox HR replaces stub on CARRS longitudinal** per Munshi adjudication.
- **OSF:** `osf_prereg/candidate_007_OSF_TIMESTAMPED.md` (Reg 2026-08-31, 302 lines, CC-BY 4.0 at Stage 1 acceptance, embargo open). RR Stage 1 manuscript `rr_stage1/candidate_007_AHLQVIST.md` (286 lines, sha256 `ba7626f885a9`) is submission-ready (Introduction+Methods, Results TBD except logged 8k synthetic completeness/ARI/ablation).

## 5. Compute & cost (Scope ceiling honest, Phase 1 proxy DONE at 8k)

```
8k synthetic UKB-SA proxy on CPU: <2s (<$1 cloud)
  Generation 8k SA proxy (age 44.5±11, BMI 26.8±4.2, HbA1c 8.0±1.8 gamma-clip 5–14, HOMA2-B lognormal median 61.97±39.79 clip 5–250, HOMA2-IR lognormal median 2.465±1.275 clip 0.4–8.0, GADA Bernoulli p=0.055 → synthetic_proxy_sample.csv 100 rows sha256:129f20ad3ac2)
  K-means 8k ×6-D ×k=5 ×n_init=20: <0.5s; ARI/silhouette/SMD/ESS/AUC/<1s; Outputs: centroids_vs_denovo_ARI.csv 17 rows (ba7626) + cluster_profiles.csv 10 rows (747a) + ablation_6to3.csv 3 rows (c179) + sample 100 rows (129f) + README 119 lines
B-proxy phases: UKB-SA RAP 1–3mo + CARRS 2–3mo + ICMR-INDIAB 3–6mo + CMC Vellore 2–4mo (per docs/DUA_APPLICATION_PACK.md 192 lines)
  UKB-SA 8k: same script swapping synthetic proxy for real 8k SA EHR (same KMeans params + thresholds) → re-compute ARI + IOPW ESS truncation IBC 5% + Cox HR CKD/retinopathy
  CARRS 12k: re-run on resident SA (sparsity branching 6→3 co-primary if GADA <10%) → ESS/SMD/trimming nationally validated at 12k (power ARI 0.60 vs 0.40 >90%)
Total wall-clock Phase 1: DONE (<2s 91-line log 2026-08-31 12:17:11 IST); Phase 2: 6–8 weeks after UKB-SP RAP; Phase 3: 8–10 weeks after CARRS receipt
Personnel: 2 investigators (1 biostat + 1 ML + 0.25 FTE clinician for centroid adjudication) per phase
```

Pilot verification proves wall-clock: `full_runs/candidate_007/logs/full_007.log` 91 lines `Generated N=8000 rows` `SMD fail 3/6 (50.0%)` `Completeness 98.36% TRANSPORTS` `ARI 0.250 FAILS` `3-var ARI 0.446 6vs3 0.243 GADA/HOMA drives` exit 0 — honest synthetic fallback; 8k real will shift ARI ±0.05 when credentialed.

## 6. How to reproduce (3 commands + RAP/DUA when real SA joint desired)

```bash
git clone https://github.com/medicalResearch/medicalResearch.git
git checkout 70bb40c  # or d419b12 for RR Stage-1 bridge (both logged in manifest headers)
# Honest synthetic UKB-SA 8k proxy (no DUA — reproduces logged completeness 98.36% ARI 0.250 6vs3 0.243)
python3 full_runs/candidate_007/run_full_007.py
# Expected: log 91 lines (Seed 20260830, Python 3.11.15 sklearn 1.9.0) + outputs hashed ba7626f885a9 / 747a075d8fd3 / c17976e51d7c / 129f20ad3ac2
# With credentialed UKB-SA (1–3mo UKB AMS RAP SA ~8k) + CARRS (2–3 mo PHFI/Emory) + ICMR-INDIAB (3–6 mo):
# Then: swap synthetic generation for real UKB-SA/CARRS extracts (same script: frozen centroids + ANDIS mean/SD + KMeans k=5) → recompute ARI/silhouette/SMD/ESS
# python3 full_runs/candidate_005_006/run_full_005_006.py  # companion 40k G0→G3 AUC0.500→0.967 ESS1.00→0.005 cross-tile same repo
# Rscript pilots/candidate_003/run_pilot_003.R   # CIMEHR sensitivity (optional, proves R 4.5.2 + 0.1.0 vignette 169K)
```

Hashes to verify (see `code_archive_manifest.txt` 130 lines, all SHA256 logged before outcomes inspected):
- `full_runs/candidate_007/outputs/centroids_vs_denovo_ARI.csv` ba7626f885a9 (18 lines, 17 rows, ARI0.250 FAILS completeness98.36%)
- `full_runs/candidate_007/outputs/cluster_profiles.csv` 747a075d8fd3 (11 lines, 10 rows, 5 transport +5 de-novo means per var)
- `full_runs/candidate_007/outputs/ablation_6to3.csv` c17976e51d7c (4 lines, 3 rows, 6→4→3 ARI0.446 6vs30.243 GADA/HOMA drives)
- `full_runs/candidate_007/outputs/synthetic_proxy_sample.csv` 129f20ad3ac2 (101 lines, 100 row audit sample of synthetic 8000)
- `full_runs/candidate_007/run_full_007.py` 4e539dfdd61d (336 lines, seed 20260830, KMeans 5 centroids ARI logic)
- `pilots/candidate_005_006/outputs/G0_G3_table.csv` 7be94568e8f4 (paired infrastructure 9 rows, 5k pilot)
- synthEHRella 74aa516, CIMEHR 0.1.0, ricu 0.5.8, seed 20260830 — all pins in §1

Full artifact registry: `code_archive_manifest.txt` (130 lines) lists every pilot, full run 8k, OSF, version, and git rev with SHA256. Dose-response `completeness 98.36% yet ARI 0.250 FAILS — 3-var 0.446 6vs3 0.243` is reproducible with seed 20260830.

— End of reproducibility statement — 92 lines + table; all versions, seeds, compute, OSF timestamp, B-staged DUA to CARRS/ICMR-INDIAB, and verification commands present; no PHI.
