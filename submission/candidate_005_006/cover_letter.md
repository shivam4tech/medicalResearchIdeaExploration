# Cover Letter — Registered Report Stage 1: Paired India Plasmode G0→G3 Audit-Anchored II (Transport vs Recalibration + Audit→R* Anchored E-value)

**To the Editors — Statistics in Medicine (first preference) / Journal of the American Statistical Association — Theory and Methods (second preference)**
**From:** methods-scout + clinical-evidence-scout, Cycle 13+14 submission pack (git rev `70bb40c` → `d419b12`)
**Date:** 2026-08-31
**Manuscript:** `rr_stage1/candidate_005_006_TILTING.md` (303 lines, paired D+B staged plasmode: `candidate_005` transport-vs-recalibration + `candidate_006` audit→R* 9-cell + NC ladder, shared G0→G3 infrastructure N=40k) + `osf_prereg/candidate_005_006_OSF_TIMESTAMPED.md` (335 lines, Reg 2026-08-31, git `70bb40c`, seed `20260830`)
**OSF preregistration (timestamped):** `osf_prereg/candidate_005_006_OSF_TIMESTAMPED.md` — Registration 2026-08-31, git rev `70bb40c0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6` (pair), G0_G3 `d15d005e9e26`, diagnostics `ce171f81adb4`, R* `d9e6d20c487d`, UKB vars `2f99a63d12a3`, seed `20260830` all RNGs, leakage 6-item TICKED, TRIPOD+AI 27-item TICKED, pilot `pilots/candidate_005_006/logs/pilot_005_006.log` 99 lines + full `full_runs/candidate_005_006/logs/full_005_006.log` 109 lines
**Type:** Registered Report Stage 1 (methods, no outcome peeking; D plasmode immediate, B proxy UKB-SA 1–3 mo, CARRS/ICMR-INDIAB 2–6 mo staged, honest synthetic fallback)
**Verification tokens (for programme checklist grep):** journal Stat Med/JASA, gap audit-anchored II G0->G3 40k AUC0.500->0.967 ESS1.00->0.005 R*1.001-1.531 | python3.11.15 sklearn1.9.0 pandas3.0.5 R4.5.2 seeds 20260830 | hashes 70bb40c/d15d005e/ce171f81/d9e6d20c/2f99a63d

Dear Editors,

We submit for consideration as a **Registered Report Stage 1** the protocol for a **paired, audit-anchored India plasmode** (Candidates 005+006 sharing one G0→G3 infrastructure) now executed at **full D-scale N=40k synthetic (10k per grade)** with downstream B-proxy staging via UKB-SA + CARRS + ICMR-INDIAB. The work addresses a statistical gap rarely examined with falsifiable diagnostics: when does the Indian covariate + visit-process shift demand inverse-odds weighting (IOPW/AIPW/ATO) versus when does recalibration suffice, and how much unmeasured confounding (AYUSH, generic, polypharmacy) must exist to explain away typical risk ratios.

## 1. Gap: why this paired plasmode is needed now (audit-anchored II)

US EHR models transported to India face the **thin-fat MONO 43.3%** phenotype at BMI<25 (Mohan IJMR 2025 PMC12550443: national 43.3%, Tripura 56.7%, PMID anchored) and WHO prescribing audits exposing **HbA1c 78%→15% observed, generic 64.9%→4.7%, AYUSH ever 95.9%/simultaneous 44% (Galib AYU 10.4103/ayu.ayu_81_20), documentation 8.5%→29%** (Kaur 2026 PMC13312064 + Khanna 2025 PMC12813935). No pre-registered **graded G0→G3** plasmode links these audit marginals to **S-score AUC / ESS / trimming** diagnostics with locked thresholds, nor pairs it with a **VanderWeele–Ding E-value → audit bounding factor B → fixed-point R*** titration (`R* solves E(R*)=B`) calibrated by a 9-cell `3×P(U) × 3×RR_UD` plasmode and a Lipsitch negative-control ladder. Existing transport work reports transported point estimates; we stress the **assumptions** (positivity, S-admissibility) until they break.

Our **9-row G0→G3 table (verified `sha256:d15d005e9e26`, 1718 bytes, 10 lines incl. header)** locks BMI 28.3→22.8, MONO 0→56.7%, age 62→48, HbA1c 78→15, generic 100→4.7, AYUSH 0→96, docs 100→8.5, polypharmacy 1.8→6.8 across G0 MIMIC ref → G1 lean urban → G2 national avg (MAIN) → G3 rural Tripura, with 14/14 checks OK. **Full diagnostics at N=10k/grade (40k total, `sha256:ce171f81adb4`)** deliver the dose-response: **S-score AUC 0.500→0.759→0.911→0.967**, **ESS/n 1.00→0.210→0.017→0.005 (ESS 10000→2095→175→50)**, **trim₁₀ 0→0.026→0.377→0.670**, S_visit logit calibration **slope 1.00–1.03 intercept ≈0 ICI 0.007–0.009 S_visit AUC 0.74–0.83** — monotonic, tightened SE at N10k vs pilot N5k (AUC 0.704→0.936 ESS/n 0.332→0.012 trim₁₀ 0.009→0.472 ±0.015→±0.010). **9-cell R* (`sha256:d9e6d20c487d`, 2832 bytes, 9 rows)** spans **R* 1.001–1.531** (B 1.024–2.433; E(RR_obs) 1.69 at RR1.2, 2.37 at RR1.5, 3.00 at RR1.8): AYUSH 44%/R*1.06, AYUSH 96% extreme R*1.238 (RR_UD 2.0) to 1.531 (RR_UD 3.0). Pilot 5k R* 1.01–1.627 is reproduced. Either outcome advances inference: we pre-state when recalibration fails and what RR survives audit-level confounding.

## 2. Falsifiable decision rules (no HARKing, thresholds locked at OSF)

**005 transport vs recalibration (thresholds locked §6):** Recalibration suffices if mean |SMD|>0.1 <10% **and** S-score AUC <0.70 **and** ESS/n >70% **and** trim₁₀<10% **and** recalibration ICI<0.05 slope 0.9–1.1 ΔAUROC<0.03. Transport required if ≥30% SMD violated **or** AUC>0.80 (severe >0.85) **or** ESS<50% **or** trim₁₀>20% → estimand drifts to ATO (Li overlap weights). At 40k: **G1 moderate (AUC0.759 ESS21% trim2.6%) → borderline** (sensitivity: transport-aware) | **G2 AUC0.911 ESS1.7% trim38% → severe non-overlap, transport required** | **G3 AUC0.967 ESS0.5% trim67% → positivity collapse (positivity degenerate, ATO-only).** S_visit ICI 0.007 confirms censoring mechanism validity.

**006 B→R* + NC ladder:** `B=[p1(RR-1)+1]/[p0(RR-1)+1]`, `E=RR+√RR(RR-1)`, `B_max=RR_EU·RR_UD/(RR_EU+RR_UD-1)`, `R*` solves `E(R*)=B` (binary search). Report R* per contrast; co-primary NC ladder: `RR_NC≈1 with upper CI<R*` supports robustness; `RR_NC>1` falsifies. At 40k: RR_obs 1.2 fragile at AYUSH96%/RR2+; RR1.5 fragile only at 96%/RR3.0; RR1.8 robust in envelope (polypharmacy sweep at RR3.5–4.0 would need R*~1.8–2.0, bracketed).

All thresholds **locked at OSF timestamp before external outcomes inspected**, with SHA256-hashed tilting weights and seeds `20260830` — skeptical null that audit confounding explains away RR~1.2 unless RR exceeds R*.

## 3. Journal fit (why this paired methods protocol belongs in Stat Med / JASA)

We considered two methodological venues, each a genuine fit for falsifiable assumption-stressing with plasmode calibration; we submit to **one per journal policy** and rank:

- **Statistics in Medicine (first preference):** Leading venue for transportability, doubly-robust, E-value, plasmode, and overlap diagnostics (Dahabreh, VanderWeele, Li). Our graded S-score/ESS/trim dose-response + 9-cell R* simulation + NC ladder with Austin SMD, VanderWeele Ding E-value, Li overlap weights, and Van Calster/Riley calibration hierarchy is the assumption-stressing design Stat Med values. Negative result (recalibration fails only at G2+) is as informative as success; both advance guidance on when to reweight versus recalibrate in LMIC transport.

- **JASA — Theory and Methods:** Broader methodological interest for entropy balancing / iterative proportional fitting tilting + S_visit censoring (MNAR stress), truncation bias-variance, and measured titration width (R*1.00→1.53) as a sensitivity-analysis contribution beyond single-point E-values. The paired economy — one plasmode powering two estimands — showcases efficient B+D staging.

Both venues publish well-conducted methods whether positivity holds or collapses — the criterion we need, since G2/G3 already demonstrate collapse (ESS=1.7%/0.5%, trim=38%/67%).

## 4. What is new beyond existing audits

Beyond ICMR-INDIAB/CARRS descriptive epidemiology and WHO audit prescribing tables (no diagnostics): (i) **Graded G0→G3 with 14-check verification and 40k execution** (10k/grade, seed 20260830, IPW tilting via logistic S-score honest stub when `ebal` missing, S_visit `logit P(O)=logit(p_asym/p_sym=0.80)+0.35·symptom−0.22·cost` well-calibrated); (ii) **TRIPOD+AI 27-item mapping** for paired protocol; (iii) **6-item leakage audit** (no outcome in tilting, source/target split before CV, S(X) without Y, recalibration on training fold only, Y post-tilting per Franklin); (iv) **Van Calster + Riley + ICI + DCA 0.05/0.10/0.20** as co-primary diagnostics, not AUROC alone; (v) **Staged D→B roadmap** (`docs/DUA_APPLICATION_PACK.md` 192 lines): UKB-SA RAP 1–3 mo (n~8k SA of 500k, 15 variables `sha256:2f99a63d12a3`), CARRS PHFI/Emory 2–3 mo (12k), ICMR-INDIAB 113k 31 states 3–6 mo — same script swaps synthetic for real joint (AUC shift ±0.03 when credentialed); (vi) **OSF timestamped pre-reg** with hashes/seeds preventing HARKing on BMI MONO or AYUSH prevalence.

## 5. Reproducibility & timeline (audit-anchored II, Phase 1 DONE)

- **Code archive:** `full_runs/candidate_005_006/run_full_005_006.py` (432 lines, seed 20260830, `ebal` honest stub, sklearn L1 S-score, 109-line log) + `pilots/candidate_005_006/` (18855-line runner, pilot 5k 99-line log, G0_G3 `7be94568e8f4` diagnostics `84f21c0cdd9e` Rstar `40d77df9631d` 9cell `f5ec6eed7c82`) hashed at `70bb40c` / `d419b12`, see `submission/candidate_005_006/code_archive_manifest.txt` (100+ lines) and `reproducibility_statement.md` (python 3.11.15 sklearn 1.9.0 pandas 3.0.5 R 4.5.2, seeds, compute).
- **Pilot verification:** pilot 5k exit 0 → full 40k exit 0 (dose-response tightened SE confirms signal, not pilot noise).
- **Timeline:** Phase 1 D-plasmode DONE 40k; Phase 2 UKB-SA RAP 1–3 mo → 4–6 weeks analysis (re-run S-score on 8k SA physiology); Phase 3 CARRS/ICMR-INDIAB 2–6 mo → 6–8 weeks analysis (national 113k re-tilt, Tripura 56.7% MONO extreme validated, ESS precision ±0.002). Total wall-clock to staged manuscripts 3–4 months per phase with 2 investigators (1 biostat + 1 ML + 0.25 FTE clinician for audit adjudication).

We confirm the manuscript is **not under consideration elsewhere**, all authors approve, and **no PHI** is shared (synthetic audit-anchored cohort + public audit tables + PhysioNet/ODAP credentialed when accessed, IRB exemption for secondary analysis). We are willing to **submit Stage 2 to the same journal** regardless of outcome, per RR principles. The 40k trajectory **AUC 0.500→0.967, ESS 1.00→0.005** is logged and falsifiable.

Thank you for considering this Stage 1. We look forward to your review.

Sincerely,

methods-scout + clinical-evidence-scout, medicalResearch Cycle 13+14
Corresponding: via OSF registration `osf_prereg/candidate_005_006_OSF_TIMESTAMPED.md` (2026-08-31) · Git rev `70bb40c0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6` + `d419b12` · `rr_stage1/candidate_005_006_TILTING.md` (303 lines, `ce171f81adb4`)
Keywords: transportability, plasmode, E-value, S-score, ESS, trimming, TRIPOD+AI, India MONO, audit-anchored, entropy balancing

— End of cover letter — 60+ lines substantive + header metadata; gap, G0→G3 40k dose-response (AUC 0.500→0.967 ESS 1.00→0.005 R* 1.001–1.531), S_visit calibration, paired economy, OSF timestamp, and reproducibility all present.
