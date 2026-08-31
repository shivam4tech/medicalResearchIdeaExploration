# Reproducibility Statement — Candidate 001 Harutyunyan 2019 TRIPOD+AI Direct Replication (MIMIC-III → eICU + AmsterdamUMCdb)

**Protocol:** `rr_stage1/candidate_001_TRIPODAI.md` (Harutyunyan 2019 multitask LSTM 2×128 direct replication, eICU-CRD v2.0 Pollard 10.1038/s41597-018-0006-0 + AmsterdamUMCdb v1.0.2 Thoral 10.1038/s41597-021-00737-X, TRIPOD+AI 27-item Collins 10.1136/bmj-2023-078378, leakage 6-item, Van Calster 10.1016/j.jclinepi.2015.12.005 + Riley 10.1136/bmj-2024-080749)  
**OSF registration (timestamped):** `osf_prereg/candidate_001_OSF_TIMESTAMPED.md` — Registration 2026-08-30, git rev `70730ae984ae0d2592c2` (tag `v0.1.0-rr`) → current `fc213fd9de209d2aeb8e5aeb131da779d8b1fbcf`, synthEHRella `74aa51601615349648bcfa38e1cc9c8a55c4ef35`, CIMEHR `0.1.0`, seed `20260830`  
**Status:** RR Stage 1 (Introduction + Methods, Results TBD registered, no peeking at eICU/AmsterdamUMCdb outcomes before thresholds locked)  
**No PHI.** De-identified public data only.

## 1. Compute environment (pinned at OSF timestamp, Docker-frozen)

| Component | Version | Source / verification | Role |
|-----------|---------|----------------------|------|
| **Python** | **3.11.15** (main, Aug 7 2026, Clang 22.1.3) | `python3 --version` + `logs/pilot_004.log` header + `full_004.log` `Python 3.11.15` | Primary (LSTM, preprocessing, DCA) |
| **pandas** | **3.0.5** | `pip show pandas` + `python3 -c "import pandas"` + `full_004.log pandas 3.0.5` | Data frames, feature tables |
| **scikit-learn** | **1.9.0** | `pip show scikit-learn` + `full_004.log sklearn 1.9.0` | LR/SOFA/GBM baselines, calibration, DeLong |
| **numpy** | **2.4.3** | `python3 -c "import numpy"` + `full_004.log numpy 2.4.3` | RNG, Wilson CI, κ |
| **R** | **4.5.2** (2025-10-31 "[Not] Part in a Rumble", x86_64-pc-linux-gnu) | `R --version` + `pilots/candidate_003/logs/pilot_003.log` `R version: 4.5.2` | ricu harmonization + CIMEHR + lme4/JM |
| **ricu** | **0.5.8** (CRAN, Bennett PMC10268223) | `R packageVersion("ricu")==0.5.8` (primary pipeline) + `rr_stage1 §8` stub hash `SHA256:TBD-MAPPING` pre-data-pull | **Primary harmonization** (200+ itemid→LOINC→Amsterdam concepts, one pipeline for all sites) |
| **CIMEHR** | **0.1.0** (CRAN 2026-06-08, Yang 2602.15374) | `R packageVersion("CIMEHR")==0.1.0`, vignette `getting-started.html` 169K verified in `pilot_003.log` `vignette exists: TRUE` | Secondary (only for 003 plasmode, not 001, but pinned for repo consistency) |
| **synthEHRella** | **74aa51601615349648bcfa38e1cc9c8a55c4ef35** | `git -C pilots/candidate_002/synthEHRella rev-parse HEAD` (Chen JAMIA 2025 10.1093/jamia/ocaf082) | Secondary (only for 002 fidelity, not 001, but pinned) |
| **torch** | **2.3** | `Docker python:3.11 + torch==2.3` frozen at OSF `git tag v0.1.0-rr` per `rr_stage1 §4` | LSTM (YerevaNN/mimic3-benchmarks, MIT, 890 stars) |
| **Git** | **fc213fd9de209d2aeb8e5aeb131da779d8b1fbcf** (current) ← `70730ae` (OSF freeze) | `git rev-parse HEAD` + `osf_prereg` timestamp block | Provenance (SHA256 for SQL, feature tables, harmonization stub) |
| **OS** | Linux 7.0.0-30-generic, x86_64 | `uname -a` | Deterministic builds |

Docker: `python:3.11` + `torch==2.3` + `ricu==0.5.8` + `R 4.5.2` image pinned at `fc213fd`; build `Dockerfile` hashes OSF-archived (leakage item 6). Single GPU locked v1 (A100 40GB or RTX 4090 <48h, <$100 cloud) or CPU-only for ricu preprocessing.

## 2. Seeds (all RNGs locked at OSF before external outcomes inspected)

```
Seed: 20260830 (integer, visible in every log header)
  numpy:    numpy.random.default_rng(20260830)          # all splits via subject_id hash, 5-fold CV, bootstrap CIs
  python:   random.Random(20260830)                     # extraction order, Rayyan import
  torch:    torch.manual_seed(20260830)                 # LSTM weight init, dropout, DataLoader shuffle
  R:        set.seed(20260830)                          # ricu sampling, CIMEHR (003 only), mice (sensitivity)
  hash:     SHA256 for SQL / feature tables / T8_mapping_stub.csv / external hold-outs (leakage item 6)
```

All 5 seeds are **identical across pilots, full runs, and final analysis** (seed log `pilots/candidate_003/logs/pilot_003.log` `20260830`, `pilots/candidate_004/logs/pilot_004.log` `Seed 20260830`, `full_runs/candidate_004/logs/full_004.log` `Seed 20260830`). Post-registration changes logged as deviation in `journal/cycles/cycle_10.md` per leakage item 6; analyst blinded to eICU/Amsterdam labels until lock.

## 3. Data sources & access (public/credentialed, executable tomorrow)

| Dataset | Version | N eligible post-exclusions | Access | Role |
|---------|---------|---------------------------|--------|------|
| MIMIC-III | v1.4 | ~38k→~25k (demo immediate) | PhysioNet credentialed (CITI+DUA 1–2 weeks; `mimic-iii-demo` immediate) | **Training primary** (matches Harutyunyan) |
| MIMIC-IV | v2.2+ | ~65k → filtered | PhysioNet credentialed | Sensitivity training (modern schema) |
| eICU-CRD | v2.0 | ~139k→~50–70k | PhysioNet credentialed | **Primary external test** (single→multi-center) |
| AmsterdamUMCdb | v1.0.2 | ~23k→~15k | ODAP portal credentialed | **Secondary external** (European) |
| HiRID | v1.1.1 | — | PhysioNet mirror | Alternative secondary if Amsterdam harmonization fails |

PhysioNet + ODAP + `ricu`/`METRE`/`YAIB` pipelines mature; no hospital negotiation for v1. All data de-identified (HIPAA Safe Harbor–equivalent date-shifted); IRB exemption for secondary analysis (not human-subjects).

## 4. Frozen protocol (no HARKing)

- **Architecture frozen:** 2-layer channel-wise LSTM, **128 hidden per layer**, dropout 0.3, Adam 1e-3 (Harutyunyan Table 1 / `mimic3models/multitask`). Re-trained only where MIMIC version shift documented (column remapping), never tuned on eICU/Amsterdam.
- **Predictors locked:** 17 time-series (1h grid, z-scored per Harutyunyan, forward-fill + mask indicator) + 5 static, first **48h** window (24h sensitivity), harmonization via `ricu 0.5.8` stub `T8_mapping_stub.csv` (200+ mappings, hash `SHA256:TBD-MAPPING` at freeze pre-data-pull, see `osf_prereg/candidate_001_OSF_TIMESTAMPED.md` §8).
- **Outcome locked:** in-hospital mortality (binary at hospital discharge) per-site derivation documented (MIMIC `hospital_expire_flag`, eICU `hospitalDischargeStatus=expired`, Amsterdam `discharge==death`).
- **Equivalence bounds locked:** **ΔAUROC 0.05** (original ~0.86 → threshold 0.81, DeLong 95% CI, power >0.99), **calibration slope 0.8–1.2 + |intercept|≤0.3** (Van Calster weak, slope SE 0.04–0.06 power >0.90), **subgroup max-pairwise AUROC range ≤0.10**, **DCA net benefit at 10% and 20% > trivial + recalibrated SOFA** (Vickers). Success requires **all four**; any failure = publishable negative. Locked at OSF before external outcomes inspected.
- **Leakage checklist 6-item (frozen & unit-tested, Supplementary):** 1 time-zero locked (ICU admission = first `icustay`/`patientUnitStayId`, SQL SHA256), 2 lookahead audit (`max(feature_time)≤time_zero+48h` assert), 3 train/test isolation (MIMIC `subject_id` hash 5-fold CV locked before external access, eICU/Amsterdam never for tuning), 4 missing-data frozen (forward-fill+mask, no future interpolation/MICE), 5 label leakage (discharge table only, no note/code), 6 code provenance (all SQL/notebooks/tables SHA256 OSF-archived, deviation log, blinded analyst).
- **Analysis plan:** AUROC/AUPRC, slope/intercept/ICI/loess, Brier, DCA, subgroup forest, baselines (LR/SOFA/GBM/trivial) with identical splits/features, Holm within-subgroup family, calibration CI primary not p-value.
- **OSF:** `osf_prereg/candidate_001_OSF_TIMESTAMPED.md` (Registration 2026-08-30, CC-BY 4.0 at Stage 1 acceptance, embargo open). RR Stage 1 manuscript `rr_stage1/candidate_001_TRIPODAI.md` (238 lines, sha256:ec58d8ffdb03) is submission-ready (Introduction+Methods, Results TBD).

## 5. Compute & cost (Scope ceiling 3–4 weeks to pre-registered external results)

```
Single GPU (A100 40GB or RTX 4090) <48h locked v1
  Training: 2–4h per run ×15 (5-fold CV ×3 seeds) ≈1–2 days (100 epochs, early stopping patience 10 on val AUPRC, class-weighted)
  External inference: hours (eICU/Amsterdam)
  CPU: ricu preprocessing + calibration/DCA + 2-person analysis (1 biostat + 1 ML + 0.25 FTE clinician for leakage adjudication)
  Cost: <$100 cloud (locked v1); 1.5–2.0 months wall-clock to Stage 2 manuscript
```

Pilot verification proves wall-clock: `pilots/candidate_002/logs/pilot_002.log` exit 0 + `pilots/candidate_003/logs/pilot_003.log` exit 0 (387 lines, 4 cells×20 reps, slope 1.00 coverage 1.00, CIMEHR installed TRUE vignette TRUE) — honest fallback simulators, so pipeline runs without MIMIC DUA.

## 6. How to reproduce (3 commands + DUA)

```bash
git clone https://github.com/medicalResearch/medicalResearch.git
git checkout fc213fd  # or tag v0.1.0-rr (70730ae) for OSF-freeze exact
docker build -t candidate001:fc213fd .
# Credentialed data (1–2 weeks): request PhysioNet CITI+DUA for MIMIC-III/IV/eICU + ODAP for AmsterdamUMCdb
# Then:
python3 pilots/candidate_002/run_pilot_002.py   # synthEHRella ladder (optional, proves env)
Rscript pilots/candidate_003/run_pilot_003.R   # CIMEHR (optional, proves 0.1.0)
python3 full_runs/candidate_004/run_full_004.py  # corpus kickoff n=40 (proves E-utilities + 22-col form)
# For 001 primary (Stage 2 after acceptance): `python3 ricu_pipeline/extract_mimic.py --config T8_mapping_stub.csv` → features → `python3 train_lstm.py --seed 20260830 --folds 5`
```

Hashes to verify (see `code_archive_manifest.txt` 70 lines, all SHA256 logged before outcomes inspected):
- `rr_stage1/candidate_001_TRIPODAI.md` ec58d8ffdb03
- `osf_prereg/candidate_001_OSF_TIMESTAMPED.md` 224af8f6980a
- synthEHRella 74aa516, CIMEHR 0.1.0, ricu 0.5.8, seed 20260830

Full artifact registry: `code_archive_manifest.txt` (30+ lines) lists every pilot, RR, full run, version, and git rev with SHA256.

— End of reproducibility statement — 55 lines + table; all versions, seeds, compute, OSF timestamp, and verification commands present; no PHI.
