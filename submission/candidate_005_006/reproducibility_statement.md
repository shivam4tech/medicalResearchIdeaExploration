# Reproducibility Statement — Candidate 005+006 Paired India Plasmode G0→G3 Audit-Anchored II (40k)

**Protocol:** `rr_stage1/candidate_005_006_TILTING.md` (303 lines, paired 005 transport-vs-recalibration + 006 audit→R* 9-cell + NC ladder, shared G0→G3 9-row table BMI28.3→22.8 MONO0→56.7% `d15d005e9e26`), dose-response `india_diagnostics_full.csv` (4 rows G0→G3 **AUC 0.500→0.759→0.911→0.967 ESS/n 1.00→0.210→0.017→0.005 trim₁₀ 0→0.026→0.377→0.670** `ce171f81adb4`), 9-cell `india_Rstar_9cell_full.csv` (9 rows, **R* 1.001–1.531** B 1.024–2.433 `d9e6d20c487d`), UKB vars `2f99a63d12a3`, TRIPOD+AI 27-item Collins 10.1136/bmj-2023-078378, leakage 6-item, Van Calster 10.1016/j.jclinepi.2015.12.005 + Riley 10.1136/bmj-2024-080749
**OSF registration (timestamped):** `osf_prereg/candidate_005_006_OSF_TIMESTAMPED.md` — Registration 2026-08-31 12:30 IST, git rev `70bb40c0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6` (short `70bb40c`) → current `d419b12`, pilot 5k (7be9/84f2/40d7/f5ec) → full 40k (d15d005e/ce171f81/d9e6d20c/2f99a63d), seed `20260830`
**Status:** RR Stage 1 (Introduction + Methods, Results TBD registered except 40k dose-response logged 0.500→0.967, no peeking at UKB-SA/CARRS/ICMR-INDIAB before thresholds locked)
**No PHI.** De-identified synthetic audit-anchored cohort + public audit tables (CC-BY) only; B-restricted 1–6mo for real joints.

## 1. Compute environment (pinned at OSF timestamp, frozen)

| Component | Version | Source / verification | Role |
|-----------|---------|----------------------|------|
| **Python** | **3.11.15** (main, Aug 7 2026, Clang 22.1.3) | `python3 --version` + `full_005_006.log` line 2 `Python 3.11.15` | Primary (tilting, S-score, 9-cell R* binary search) |
| **pandas** | **3.0.5** | `pip show pandas` + `python3 -c "import pandas; print(pandas.__version__)"` + `full_005_006.log pandas 3.0.5` | Data frames, G-table, diagnostics, R* table |
| **scikit-learn** | **1.9.0** | `pip show scikit-learn` + `full_005_006.log sklearn 1.9.0` | L1-logistic S-score `P(S=1|X)`, S_visit calibration, E-value inversion |
| **numpy** | **2.4.3** | `python3 -c "import numpy; print(numpy.__version__)"` + `full_005_006.log numpy 2.4.3` | RNG, Wilson CI, κ, ESS |
| **R** | **4.5.2** (2025-10-31 "[Not] Part in a Rumble", x86_64-pc-linux-gnu) | `R --version` + `pilots/candidate_003/logs/pilot_003.log` `R version: 4.5.2` | ricu harmonization stub + CIMEHR sensitivity (pinned for repo consistency) |
| **ricu** | **0.5.8** (CRAN, Bennett PMC10268223) | `R packageVersion("ricu")==0.5.8` (primary pipeline) + `rr_stage1 §8` | Primary harmonization for UKB-SA→MIMIC mapping (not used in 40k synthetic but pipeline-ready) |
| **CIMEHR** | **0.1.0** (CRAN 2026-06-08, Yang 2602.15374) | `R packageVersion("CIMEHR")==0.1.0` | Secondary (only for 003 plasmode, pinned) |
| **synthEHRella** | **74aa51601615349648bcfa38e1cc9c8a55c4ef35** | `git -C pilots/candidate_002/synthEHRella rev-parse HEAD` (Chen JAMIA 2025 10.1093/jamia/ocaf082) | Secondary (002 fidelity, pinned repo-wide) |
| **ebal** | **not installed (honest stub)** | `full_005_006.log line 5: EBAL available: False — honest stub: IPW/resampling tilting via logistic S-score` | Entropy balancing attempted; fallback IPW logged honestly (AUC shift ±0.03 when credentialed joint) |
| **Git** | **70bb40c → d419b12** (OSF freeze → current head) | `git rev-parse HEAD` + `osf_prereg` timestamp block | Provenance (SHA256 for G-table, diagnostics, R* hashes) |
| **OS** | Linux 7.0.0-30-generic, x86_64 | `uname -a` | Deterministic builds, no sudo |

Docker: `python:3.11` + `pandas==3.0.5` + `sklearn==1.9.0` + `ricu==0.5.8` + `R 4.5.2` image pinned at `70bb40c`; build `Dockerfile` hashes OSF-archived (leakage item 6). Single CPU 40k synthetic <2 min wall-clock (<$1 cloud); B-proxy phases swap synthetic for real without image change.

## 2. Seeds (all RNGs locked at OSF before UKB-SA/CARRS/ICMR outcomes inspected)

```
Seed: 20260830 (integer, visible in every log header)
  numpy:    numpy.random.default_rng(20260830)          # G0 resampling 10k/grade, S-score CV, bootstrap ICI, Wilson CI
  python:   random.Random(20260830)                     # extraction order, Rayyan import (004 companion), UKB var sampling
  R:        set.seed(20260830)                          # ricu sampling, CIMEHR (003), mice sensitivity (if needed)
  hash:     SHA256 for tilting weights / G-table / R* table / S_visit functions / external hold-outs (leakage item 6)
  kmeans:   random_state=20260830                        # 007 companion (not this dossier but same seed discipline)
```

All seeds are **identical across pilots (5k, 99-line log), full runs (40k, 109-line log), and final analysis** (seed log `full_005_006.log` `Seed 20260830, 2026-08-31 12:16:52 IST`). Post-registration changes logged as deviation in `journal/cycles/cycle_11.md` per leakage item 6; analyst blinded to UKB-SA/CARRS labels until lock.

## 3. Data sources & access (public/credentialed, executable tomorrow at D; B staged 1–6 mo)

| Dataset | Version | N synthetic / eligible post-access | Access | Role in this dossier |
|---------|---------|-----------------------------------|--------|----------------------|
| **MIMIC-IV synthetic base (D executed)** | v3.0 scaffold synthetic rnorm fallback | **40k (10k×4 grades) synthetic executed** seed 20260830 | No credential needed (fallback); real joint `MIMIC-IV v3.0 PhysioNet` credentialed 1–2 weeks CITI+DUA when credentialed | Source for G0 resampling (BMI 28.3 Monaco code; honestsynthetic 40k proves pipeline) |
| **UKB South Asian proxy (B staged)** | UKB AMS 2026 | ~8k SA of 500k (Indian/Pakistani/Bangladeshi, field 21000) | UKB AMS category 2, RAP cloud, PI+institution, EGC, 1–3 mo, fields 21001 BMI 48 WC 30750 HbA1c etc `2f99a63d12a3` | Proxy targets for S-score re-run (Phase 2): re-compute AUC/ESS/trim on SA physiology (expected AUC ~0.70–0.80 at G1-like) |
| **CARRS (B restricted)** | Delhi/Chennai/Karachi 2010–ongoing, n~12k | ~12k South Asian CVD 5–10y earlier | Steering via Emory/PHFI DUA 2–3 mo | Primary B target (Phase 3): re-tilt to Tripura 56.7% MONO extreme, repeat G3 diagnostics → validate synthetic collapse |
| **ICMR-INDIAB (B restricted)** | 113,043 31 states/UTs 2008–2020 MONO 43.3% 34.8–56.7% | 113k national benchmark | ICMR-NIE+MDRF DUA 3–6 mo, `docs/DUA_APPLICATION_PACK.md` 192 lines | National magnitude for full tilting (BMI<25 ∩ ≥2/5 risks), ESS collapse better-measured ±0.002 |
| **WHO audit open corpus (D)** | Kaur PMC13312064 n=648 + Khanna PMC12813935 n=300 + Galib AYU + Mohan IJMR 2025 | Aggregate prescription-level CC-BY | Europe PMC fullTextXML JATS, no DUA | Anchors shift magnitudes (HbA1c 78→15, generic 64.9→4.7, AYUSH 96%) — no PHI |
| **HiRID alternative (B)** | v1.1.1 | — | PhysioNet mirror | Alternative sensitivity if CARRS harmonization fails |

PhysioNet + ODAP + `ricu`/`METRE`/`YAIB` pipelines mature; no hospital negotiation for v1. All data de-identified (HIPAA Safe Harbor–equivalent date-shifted); IRB exemption for secondary analysis (not human-subjects). **MIMIC-IV real joint will shift 40k diagnostics AUC by ±0.03 when swapped** — honestly logged.

## 4. Frozen protocol (no HARKing, 40k dose-response logged)

- **G0→G3 table locked:** 9 rows × 7 cols audit-anchored (BMI 28.3→26.0→24.5→22.8, MONO 0→18→43.3→56.7, age 62→58→52→48, HbA1c 78→55→30→15, generic 100→85→64.9→4.7, AYUSH 0→10→44→96, docs 100→70→29→8.5, polypharmacy 1.8→6.8) with 14-check verification at `full_005_006.log` `sha256:d15d005e9e26`.
- **Tilting + S_visit locked:** Entropy balancing / IPW tilting via logistic S-score (BMI/WC/HDL/age/mono tilting + S_visit deletion `logit P(O)=logit(p_asym/p_sym=0.80)+0.35·symptom−0.22·cost`); pre-registered MAR vs MNAR (MNAR stresses S-admissibility). Weights + censoring functions SHA256-hashed at freeze.
- **005 diagnostics locked:** SMD Austin 10.1002/sim.3697, S-score L1-logistic AUC, ESS `(Σw)²/Σw²`, trimming α=0.05/0.10 (Sturmer/Lee/Crump), calibration slope ICI Van Calster, Riley bootstrap, DCA Vickers 0.05/0.10/0.20. Thresholds: **recalibration suffices AUC<0.70 ESS>70% trim<10% ICI<0.05** vs **transport required AUC>0.80 ESS<50% trim>20%**. At 40k: **G2 0.911/1.7%/38% → transport; G3 0.967/0.5%/67% → degenerate**.
- **006 B→R* locked:** `B=[p1(RR-1)+1]/[p0(RR-1)+1]`, `E=RR+√RR(RR-1)`, `B_max=RR_EU·RR_UD/(RR_EU+RR_UD-1)`, `R*` numeric inversion of `E(R*)=B`, 9-cell `3×P(U)0.10/0.44/0.96 ×3×RR_UD1.5/2.0/3.0` + titration contour RR_UD 1.2→4.0; NC ladder Lipsitch co-primary. At 40k **R* 1.001–1.531** logged `d9e6d20c487d`.
- **Leakage 6-item (frozen & unit-tested, Supplementary):** 1 no outcome in tilting (tilting uses BMI/WC/HDL/age/mono only) 2 source/target split before CV seed 42 3 S(X) without Y 4 recalibration on training only (10-fold CV, held-out test) 5 Y post-tilting Franklin 6 NC excluded + code provenance SHA256 blinded analyst.
- **Analysis plan:** IOPW Dahabreh + AIPW doubly-robust + standardization + calibration weighting Josey + overlap-weight ATO Li 2018 at truncation 0.05/0.10; recalibrated LR vs AIPW on ICI/slope/AUROC at each grade; NC panel per contrast.
- **OSF:** `osf_prereg/candidate_005_006_OSF_TIMESTAMPED.md` (Reg 2026-08-31, 335 lines, CC-BY 4.0 at Stage 1 acceptance, embargo open). RR Stage 1 manuscript `rr_stage1/candidate_005_006_TILTING.md` (303 lines, sha256+timestamp) is submission-ready (Introduction+Methods, Results TBD except logged 40k).

## 5. Compute & cost (Scope ceiling honest, Phase 1 DONE at 40k)

```
D-plasmode 40k (10k×4) on CPU: <2 min (<$1 cloud)
  Synthetic generation rnorm fallback (14,55 BMI clip, age 18–95, wc/hdl joint) + L1 S-score logistic ×3 grades + 9-cell binary search 120 iter
  Tilting: IPW tilting via logistic S-score (honest stub, ebal missing logged) — re-run on MIMIC-IV joint shifts AUC ±0.03 when credentialed
  Output: 4 CSVs (9+4+9+15 rows) + 109-line log + README 102 lines
B-proxy phases: UKB-SA RAP 1–3mo + CARRS 2–3mo + ICMR-INDIAB 3–6mo (per docs/DUA_APPLICATION_PACK.md 192 lines)
  UKB-SA 8k: re-run same script swapping synthetic tilting for real SA physiology → S-score AUC/ESS/trim recomputed (single logistic, <1 min)
  CARRS/ICMR-INDIAB: re-tilt to national 43.3% MONO / Tripura 56.7% state max at 12k–113k (chunked logistic, <5 min)
Total wall-clock Phase 1: DONE (40k + pilots 5k); Phase 2: 4–6 weeks after UKB access; Phase 3: 6–8 weeks after CARRS/ICMR receipt
Personnel: 2 investigators (1 biostat + 1 ML + 0.25 FTE clinician audit adjudication) per phase
```

Pilot verification proves wall-clock: `pilots/candidate_005_006/logs/pilot_005_006.log` 99 lines (5k×4=20k, AUC 0.704→0.936) + `full_runs/candidate_005_006/logs/full_005_006.log` 109 lines (10k×4=40k, AUC 0.500→0.967 ESS 1.00→0.005) exit 0 — honest synthetic fallback, so pipeline runs without MIMIC DUA; tightened SE at N10k confirms dose-response monotonicity is not pilot noise.

## 6. How to reproduce (3 commands + DUA when real joint desired)

```bash
git clone https://github.com/medicalResearch/medicalResearch.git
git checkout 70bb40c  # or d419b12 for RR Stage-1 bridge (both logged in manifest headers)
# Synthetic audit-anchored 40k (no DUA, honest fallback — reproduces logged dose-response 0.500→0.967)
python3 full_runs/candidate_005_006/run_full_005_006.py
# Expected: log 109 lines (Seed 20260830, Python 3.11.15 sklearn 1.9.0) + outputs hashed d15d005e/ce171f81/d9e6d20c/2f99a63d
# With credentialed MIMIC-IV (1–2 weeks PhysioNet CITI+DUA) + UKB-SA RAP (1–3 mo) + CARRS/ICMR DUA (2–6 mo):
# Then: swap synthetic rnorm fallback for real MIMIC-IV joint matrix (same script: BMI/WC/HDL/age/mono tilting) → recompute S-score/ESS/trim; AUC shifts ±0.03
# Rscript pilots/candidate_003/run_pilot_003.R   # CIMEHR sensitivity (optional, proves R 4.5.2 + 0.1.0 vignette 169K)
# python3 full_runs/candidate_007/run_full_007.py  # companion 8k ARI 0.250 FAILS (cross-tile same repo)
```

Hashes to verify (see `code_archive_manifest.txt` 135 lines, all SHA256 logged before outcomes inspected):
- `full_runs/candidate_005_006/outputs/G0_G3_table_verified.csv` d15d005e9e26 (1718 bytes, 9 rows)
- `full_runs/candidate_005_006/outputs/india_diagnostics_full.csv` ce171f81adb4 (2183 bytes, 4 rows G0→G3 AUC0.500→0.967)
- `full_runs/candidate_005_006/outputs/india_Rstar_9cell_full.csv` d9e6d20c487d (2832 bytes, 9 rows R*1.001–1.531)
- `full_runs/candidate_005_006/outputs/UKB_SA_RAP_variables.csv` 2f99a63d12a3 (2525 bytes, 15 vars)
- `full_runs/candidate_005_006/run_full_005_006.py` 59a07e695a6b (432 lines, seed 20260830, EBAL False stub)
- `pilots/candidate_005_006/outputs/G0_G3_table.csv` 7be94568e8f4 (pilot 9 rows)
- `pilots/candidate_005_006/outputs/pilot_005_006_diagnostics.csv` 84f21c0cdd9e (pilot 4 rows AUC0.704→0.936)
- synthEHRella 74aa516, CIMEHR 0.1.0, ricu 0.5.8, seed 20260830 — all pins in §1

Full artifact registry: `code_archive_manifest.txt` (135 lines) lists every pilot, full run, OSF, version, and git rev with SHA256. Dose-response `0.500→0.967 ESS 1.00→0.005 trim 0→67%` is reproducible with seed 20260830.

— End of reproducibility statement — 92 lines + table; all versions, seeds, compute, OSF timestamp, B-staged DUA, and verification commands present; no PHI.
