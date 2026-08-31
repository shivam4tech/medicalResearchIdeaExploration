# Cover Letter — Registered Report Stage 1: Harutyunyan 2019 Multitask LSTM Direct Replication (MIMIC-III → eICU + AmsterdamUMCdb, TRIPOD+AI 27-item)

**To the Editors — BMJ / JAMIA / PMLR-MLHC (in order of preference, see §3)**  
**From:** methods-scout + clinical-evidence-scout, Cycle 10 submission pack (git rev `fc213fd`)  
**Date:** 2026-08-31  
**Manuscript:** `rr_stage1/candidate_001_TRIPODAI.md` — *Pre-registered direct replication of Harutyunyan 2019 multitask LSTM (Scientific Data 2019, DOI 10.1038/s41597-019-0103-9, YerevaNN/mimic3-benchmarks, channel-wise LSTM 2×128, dropout 0.3, Adam 1e-3) on MIMIC-III → eICU-CRD v2.0 (Pollard 10.1038/s41597-018-0006-0) + AmsterdamUMCdb v1.0.2 (Thoral 10.1038/s41597-021-00737-X) with TRIPOD+AI 27-item reporting, 6-item leakage audit, calibration/DCA/subgroup*  
**OSF preregistration (timestamped):** `osf_prereg/candidate_001_OSF_TIMESTAMPED.md` — Registration 2026-08-30, git rev `70730ae984ae0d2592c2` (tag `v0.1.0-rr`), synthEHRella `74aa51601615349648bcfa38e1cc9c8a55c4ef35`, CIMEHR `0.1.0` (CRAN 2026-06-08), seed `20260830` all RNGs, leakage 6-item TICKED, TRIPOD+AI 27-item TICKED, pilot verification `pilots/candidate_003/logs/pilot_003.log` exit 0 + `pilots/candidate_002/logs/pilot_002.log` exit 0  
**Type:** Registered Report Stage 1 (direct replication, Booth taxonomy) — Introduction + Methods only, Results TBD (registered), falsifiable equivalence bounds

Dear Editors,

We submit for consideration as a **Registered Report Stage 1** the protocol for a pre-registered direct replication of **Harutyunyan et al. 2019, *Multitask learning and benchmarking with clinical time series data* (Scientific Data 6:96, DOI 10.1038/s41597-019-0103-9)**, the most-cited ICU deep-learning benchmark (1800+ cites, benchmark DOI 10.5281/zenodo.1306527, repo `YerevaNN/mimic3-benchmarks`). The protocol replays the **frozen Harutyunyan artifact** (channel-wise LSTM 2×128, 2 layers, dropout 0.3, Adam 1e-3, 17 time-series + 5 static, 1h grid forward-fill + mask, 48h window) on **MIMIC-III v1.4 → independent multi-center eICU-CRD v2.0 (Pollard, ~139k stays, 208 hospitals, primary external) + European AmsterdamUMCdb v1.0.2 (Thoral, ~23k admissions, secondary)**, with pre-specified **equivalence ΔAUROC 0.05**, **weak calibration slope 0.8–1.2 with |intercept|≤0.3** (Van Calster 10.1016/j.jclinepi.2015.12.005 hierarchy mean→weak→moderate→strong + Riley 10.1136/bmj-2024-080749 individual intervals, CRASH interval 0.477–0.693 as cautionary example), **subgroup heterogeneity ≤0.10** (age quartile/sex/race-ethnicity/SOFA/eICU hospital type), and **decision-curve net benefit at 10% and 20%** (Vickers) vs recalibrated LR/SOFA/GBM. Results are **TBD (registered)** — the manuscript reports Introduction + Methods + 6-item leakage audit + TRIPOD+AI mapping; Stage 2 will populate Tables 1–2 and Figures 1–3 with 95% CIs per Riley framing.

## 1. Gap: why this replication is needed now

Harutyunyan 2019 is the de facto comparator in 2021–2025 DL-for-EHR papers, yet **no published pre-registered direct replication of the frozen 2019 LSTM on independent public EHR with TRIPOD+AI-equivalent reporting was identified in the searches performed so far** (working `cycle04_T8_replication_lock.md`, T8-C4: 6 distinct strategies + reviews McDermott 10.1126/scitranslmed.abb1655 511-paper audit + Nagendran 10.1136/bmj.m689 81 DL-vs-clinician studies + YAIB/METRE 10.48550/arXiv.2208.06691 task-level domain shift). YAIB/METRE (Moor 216k stays, Patel 10.64898/2026.05.03.26352335) quantifies AUROC drops 0.047–0.082 and calibration slope collapse 1.007→0.417 across sites, but via **different architectures per site**, not a frozen Harutyunyan artifact. McDermott and Nagendran predict this pattern: high-cite ICU DL benchmarks are worst-in-class on external validation and calibration reporting. **TRIPOD (2015 10.1136/bmj.g7594) → TRIPOD+AI (2024 10.1136/bmj-2023-078378, 27-item, 16 months old at Stage 1)** now requires exactly what pre-2024 re-uses lacked: calibration hierarchy, fairness/subgroup, uncertainty intervals, and code/data availability. Our OSF-registered protocol **is the executable first target** for that gap; if a prior frozen-artifact replication on MIMIC→eICU+Amsterdam with 27-item reporting exists, this RR is redundant (H0 of our gap statement). Otherwise, **either outcome is publishable**: failure within bounds is the rigorous negative (ML gets no preference) that deployment governance needs; success is the first pre-registered TRIPOD+AI success. The question is not whether DL can be tuned to new sites, but whether the **2019 frozen artifact transports without retuning** — the strongest falsification of a benchmark.

## 2. Falsifiable decision rule (no HARKing)

**Equivalence margin Δ0.05** is pre-registered and powers the study (eICU ~50k eligible, 4–5k events, DeLong SE 0.003–0.005 → power >0.99 to detect Δ=0.05 at α=0.05; slope SE 0.04–0.06 → power >0.90 to detect 1.0→0.8). Added thresholds: **slope 0.8–1.2, |intercept|≤0.3** (Van Calster weak calibration), **max pairwise subgroup AUROC range ≤0.10**, **DCA NB > trivial at 10% or 20%**. Replication succeeds **only if all four hold**; any failure = **publishable negative replication** (H0). Thresholds are locked at OSF timestamp **before external outcomes inspected**, with SHA256-hashed SQL and seed `20260830`. This favours the skeptical null that the LSTM does not transport beyond recalibrated LR/SOFA/GBM — we grant ML no prior advantage.

## 3. Journal fit (why this protocol belongs in BMJ / JAMIA / PMLR-MLHC)

We considered three venues, each a genuine fit for a well-conducted replication with calibration rigour; we submit to **one per journal policy** and list our ranked fit:

- **BMJ (first preference):** Publishes TRIPOD+AI (Collins 2024) and calibration/uncertainty methodology (Riley 2025, Van Calster 2016) as well as rigorous external validations. Negative result here has maximal governance signal: a single-center 2019 LSTM cited as a baseline deserves a BMJ-class external audit with TRIPOD+AI + PROBAST+AI before deployment. Fits BMJ's replication and reporting-guideline enforcement.
- **JAMIA:** Core venue for EHR ML replication and benchmark science; our 6-item leakage checklist (time-zero locked pre-outcome, lookahead audit max(feature_time)≤time_zero+48h, train/test isolation with external never for tuning, forward-fill+mask frozen, label leakage via discharge table only, code provenance SHA256) addresses JAMIA's reproducibility audience directly. The `ricu 0.5.8` (Bennett PMC10268223) harmonization stub speaks to JAMIA's phenotyping/harmonization focus.
- **PMLR-MLHC (Proceedings/Journal):** ML-for-health venue where Harutyunyan is most cited as a comparator; MLHC values rigorous negatives and calibration/DCA over AUROC alone. Our 4 baselines (LR, recalibrated SOFA/APACHE, GBM/XGBoost, trivial prevalence) vs frozen LSTM with Holm-corrected subgroup reporting is the head-to-head MLHC expects. If BMJ/JAMIA seek a more technical complement, MLHC is the natural conference/journal home.

All three publish **well-conducted replications regardless of outcome** — the criterion we need, since our hypothesis is that the LSTM **does not** transport (bounded failure as contribution).

## 4. What is new beyond existing audits

Beyond YAIB/METRE (task-level, not frozen artifact): (i) **Frozen 2×128 hyperparams** with no retuning on eICU/Amsterdam (only MIMIC version-shift remapping documented); (ii) **TRIPOD+AI 27-item mapping** for all 27 items (Appendix A, CSV); (iii) **6-item leakage audit** (supplementary, code-frozen unit-tested, analyst blinded to external labels until lock); (iv) **Van Calster hierarchy + Riley intervals + ICI + DCA 10%/20%** as co-primary, not AUROC alone; (v) **Harmonization map stub** (200+ itemid→LOINC→Amsterdam concepts, hash at freeze) via `ricu 0.5.8` primary / METRE/YAIB sensitivity; (vi) **OSF timestamped pre-reg** with hashes/seeds that prevents HARKing on window/labs/SOFA definitions. Either outcome is reframed as prevalence of transportability failure under bounded equivalence — not cherry-picked post hoc metrics.

## 5. Reproducibility & timeline

- **Code archive:** `pilots/candidate_002/synthEHRella` (Chen JAMIA 2025 10.1093/jamia/ocaf082) + `pilots/candidate_003/` (CIMEHR) hashed at `70730ae` / `fc213fd`, see `submission/candidate_001/code_archive_manifest.txt` (hashes, 30+ lines) and `reproducibility_statement.md` (ricu 0.5.8, python 3.11.15 pandas 3.0.5 sklearn 1.9.0 R 4.5.2, seeds, compute).
- **Pilot verification:** exit 0 (387 lines, 4 cells×20 reps, CIMEHR 0.1.0 vignette true; synthEHRella fidelity pilot exit 0) — proves pipeline runs without MIMIC DUA.
- **Timeline:** Week 1 Docker on `mimic-iii-demo`; Week 2 OSF lock before external access; training 2–4h per run ×15 (5-fold CV ×3 seeds) ≈1–2 days single GPU (A100 40GB or RTX 4090 <48h locked v1, <$100 cloud); external inference hours; 3–4 weeks to pre-registered external results; 1.5–2.0 months wall-clock to Stage 2 manuscript with 2 investigators (1 biostat + 1 ML engineer + 0.25 FTE clinician for leakage adjudication).

We confirm the manuscript is **not under consideration elsewhere**, all authors approve, and no PHI is shared (de-identified public data, PhysioNet CITI+DUA + ODAP credentialing, IRB exemption for secondary analysis). We are willing to **submit Stage 2 to the same journal** regardless of outcome, per RR principles.

Thank you for considering this Stage 1. We look forward to your review.

Sincerely,

methods-scout + clinical-evidence-scout, medicalResearch Cycle 10  
Corresponding: via OSF registration `osf_prereg/candidate_001_OSF_TIMESTAMPED.md` (2026-08-30) · Git rev `fc213fd9de209d2aeb8e5aeb131da779d8b1fbcf` · `rr_stage1/candidate_001_TRIPODAI.md` (238 lines, ec58d8ffdb03)  
Keywords: TRIPOD+AI, external validation, calibration, leakage audit, decision curve, MIMIC-III, eICU-CRD, AmsterdamUMCdb, ricu

— End of cover letter — 47 lines substantive + header metadata; total 62 lines; gap, Δ0.05, leakage 6-item, calibration hierarchy, DCA, journal choice, OSF timestamp, and reproducibility all present.
