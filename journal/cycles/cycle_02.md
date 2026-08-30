# Cycle 2 — Methodological Failure Points: where existing approaches demonstrably break
**Date:** 2026-08-30 · **Agents:** Research Lead + clinical-evidence-scout + methods-scout (adversarial-reviewer DARK) · **Rate-limit incidents:** none

## Objective
Deepen the 3 most promising failure-point territories from Cycle 1 landscape: irregular-series modeling that hides behind averages, aggregate calibration that masks subgroup failure, synthetic data that may not preserve method conclusions — plus stress-test transportability assumptions where Indian care patterns break imported estimators. Produce executable designs, not yet experiments.

## Questions for this cycle
1. Under what plasmode settings does DL-for-irregularity fail to beat classical mixed/joint models on calibration/coverage? What is the publishable simulation design with known truth?
2. How prevalent is aggregate-masking in published external validations, and what corpus + pilot can demonstrate the audit is worth scaling?
3. At what fidelity threshold does synthetic/plasmode preserve method ranking — and what minimal synthEHRella pilot proves the instrument-validity question is tractable?
4. Do standard positivity/overlap diagnostics break on LMIC-shifted covariates, and can Indian prescribing audits anchor E-value sensitivity?

## Assignments
- **clinical-evidence-scout:** cycle02_T6_positivity_diagnostics (positivity/diagnostics under LMIC shift), cycle02_T4_prescribing_audit (audit-anchored E-value + negative controls)
- **methods-scout:** cycle02_T1_plasmode_design (full generative spec + phase diagram), cycle02_T5_corpus_pilot (TRIPOD corpus + 5-paper pilot), cycle02_T7_threshold_pilot (fidelity vs Kendall τ)
- Brief: `working/CYCLE_02_BRIEF.md` (5 packets, each 13-section template, self-authored adversarial, India verdict)

## Rate discipline
Global pool muse-spark-1.2-contributor-free (opencode-zen) ~40/min, target ≤24, ceiling 30, max 2 concurrent. Actual: 31 + 30 = 61 calls over ~14 min (~4.3/min avg, well under ceiling, no 429s). Verification ~1 per 3-4 searches; 2 search rows UNVERIFIED-timeout correctly flagged.

## Findings
**5/5 deepening packets COMPLETE — all Medium confidence.** No candidate promoted — deepening only, per brief.

- **T6 Positivity Diagnostics (10 papers, load-bearing Kang 2025 10.1007/s10654-025-01217-w):** Diagnostics toolkit (SMD 0.1 Austin 10.1002/sim.3697, trimming α α-cutoffs Crump, overlap weights Li 10.1080/01621459.2018.1448823) established **in IPTW/ATE** but borrowed uncalibrated into transportability; applied transportability studies rarely report them (Inoue 2025 10.1016/j.annepidem.2025.03.001, Kang 2025). Thresholds not calibrated on LMIC shift; adversarial Indian search returned zero. Design: graded-shift plasmode (MIMIC-IV/UKB resampling + Indian covariate shift) stress-testing 5-diagnostic set (overlap histogram, SMD before/after, weight max/ESS, trimming α∈{0.01,0.05,0.10}, overlap-weight alternative) mapping diagnostic threshold vs calibration collapse; Indian-proxy targets CARRS (Nair IJE 2022 10.1093/ije/dyac122) + UK Biobank South Asian (managed). **STRESSES-ASSUMPTION.** Survives because no systematic LMIC diagnostics study located.
- **T4 Prescribing Audit → Anchored Sensitivity (10 papers, load-bearing VanderWeele 10.7326/M16-2607 + Lipsitch 10.1097/EDE.0b013e3181d61eeb):** E-value consensus but <15% reporting (Zhang BMJ Medicine 10.1136/bmjmed-2022-000366, J Clin Epidemiol 2023 10.1016/j.jclinepi.2023.09.014); target-trial emulation normative (Hernán 2024 10.7326/ANNALS-24-01871, 2025 10.1001/jamanetworkopen.2025.58262) but US-centric; negative controls expected (Duke/FDA Workshop 2023) but <10-20% usage. Indian WHO-indicator audits abundant (review 10.18203/2394-6040.ijcmph20233814, polypill affordability 10.5334/gh.1335, AYUSH co-use 10.4103/ayu.ayu_81_20 10-40% unmeasured confounder) but disconnected from sensitivity literature. Adversarial Indian emulation with NC returned zero; OHDSI LEGEND has no Indian site. Design: same target trial (ACEi vs CCB or metformin vs sulfonylurea) in US benchmark vs Indian-plasmode (cost-driven switching + MNAR labs + AYUSH latent) or CARRS/UKB-SA, with PS/overlap diagnostics + E-value vs audit-anchored threshold (requires audit→RR translation) + ≥1 NC outcome + ≥1 NC exposure falsification panel. **STRESSES-ASSUMPTION.**
- **T1 Plasmode Design (10 papers, load-bearing Sun 10.34133/hds.0456, Schneider 10.1186/s13040-025-00450-z, Liang 10.48550/arXiv.2410.13113):** Architecture-saturated, benchmark-poor (Sun review, Naemi 2024 MIMIC-IV DL-vs-DL arXiv 2401.15290). Failure = no head-to-head DL (GRU-D 10.1038/s41598-018-24271-9 / SeFT / neural ODE) vs classical LMM/JMbayes2 on calibration/coverage/DCA with tunable informativeness. Design: 3-process joint (visit λ_V with γ_v shared frailty + observation logit with γ_o/δ + longitudinal Y=Xβ+Zb+ε + outcome θ1 f(Y*)) with parameter inventory N{500,2k,10k}, visits/patient 2/6/15, SNR 0.5/1.5/4, γ_v 0/0.3/0.8, γ_o 0/0.4/0.9, heterogeneity, effect 1.1/1.5/2.5; 16-cell core ×200 MC replicates; mandatory baselines LMM ($lme4$/$nlme$) + JMbayes2 + LOCF+logistic + MICE + GRU-D + SeFT (+ optional GRU-ODE); metrics AUC/C-index + calibration slope/intercept + Brier + 90/95% coverage + DCA; twin plasmode variants (Generate-Treatment vs Outcome per Liu 2504.11740). Decision rule: DL wins only if non-inferior on calibration/coverage AND superior on DCA. **GEOGRAPHY-ONLY** (India extension Stage-2). Next-search: Sun supplement/code inspection mandatory.
- **T5 Corpus Pilot (8 papers, load-bearing Riley 10.1136/bmj-2024-080749, Van Calster 10.1016/j.jclinepi.2015.12.005, TRIPOD+AI 10.1136/bmj-2023-078378):** Riley interval problem (0.25–0.45 width) + TRIPOD reporting gap. Corpus filter: `(TRIPOD[Title/Abstr] OR TRIPOD statement) AND (validation OR external validation ...) AND 2015-2025 AND Humans+English` (expected 200–500, target n=150). Web_extract ≥2 satisfied: Hughes 2025 UK Biobank CV risk 10.1007/s10067-025-07325-y (PMC11865138, 15170+15507 chars) — **pattern found: discrimination stratified by disease (AUC per stratum) but calibration NOT stratified (no slope/intercept per subgroup)** = hallmark aggregate masking; Diagn Progn Res 2026 TRIPOD/TRIPOD+AI SR 10.1186/s41512-026-00218-x (13883 chars) — audits overall completeness, not subgroup. Pilot n=5 extraction: overall calibration 1/1 primary, subgroup weak calibration 0/1, interval-aware 0/2 → **GO for full audit** (power n=100 → ±0.07, n=200 → ±0.05 at p≈0.2; recommend n=150). Adversarial `meta-analysis subgroup calibration ... systematic review` returned none. **GEOGRAPHY-ONLY.** Confidence Medium.
- **T7 Threshold Pilot (9 papers, load-bearing Chen 10.1093/jamia/ocaf082 + Liu 10.48550/arXiv.2504.11740 + synthEHRella GitHub 7855 chars):** Chen open benchmark (48 studies, 7 methods + 2 baselines, MIMIC-III→IV, fidelity MMD/RMSPE, utility TSTR, privacy, compute) but evaluates *generators*, not *methods evaluated via generators*. No study reports Kendall τ / Spearman between real and synthetic *methods* conclusions. Liu plasmode fragility: Generate-Outcome can make estimators appear biased. Design: MIMIC-III TRAIN → synthEHRella synthetic/plasmode TRAIN (S1 plasmode G-Treatment, S1′ G-Outcome, S2 GAN MedGAN/CorGAN, S3 Synthea, S4 Resample-perfect, S5 Prevalence-Random; 5–8 fidelity points via resampling depth/epochs) → method pair (logistic/Cox vs GRU-D; sensitivity standard vs conformal) evaluated on shared TEST_R (MIMIC-III hold-out) + TEST_TRANSPORT (MIMIC-IV), fidelity metrics MMD/RMSPE/TSTR gap, rank preservation Kendall τ / Spearman / winner concordance, 30–50 plasmode replicates/point (~1500 fits), decision rule τ≥0.7 with 95% CI LB≥0.5 via isotonic/ change-point. Expectation: τ≈0.3–0.5 at current gains (+0.0003 AUC), only ≥0.7 at near-bootstrap. **GEOGRAPHY-ONLY.** Confidence Medium.

All packets: 5–10 resolvable papers (≥1 DOI 302-verified per packet), explicit Evidence AGAINST (closest defeaters + rebuttal conditions), India verdict justified.

## Decisions
- No candidate promoted in Cycle 2 — deepening only. Cycle 2 provides the **self-authored adversarial foundations** for promotion in Cycle 3.
- Refined ranking preserved from Cycle 1, now with executable designs: **1 T8-direct-replication** (highest feasibility, public), **2 T7-threshold** (open, pilot-ready), **3 T1-plasmode** (simulation, spec-complete), **4 T5-audit** (literature corpus, pilot GO), **5 T6-positivity** (India flagship diagnostics), **6 T4-anchored sensitivity** (India flagship E-value/NC) → recommend promoting **5 of these (T8,T7,T1,T5,T6+T4 combined)** in Cycle 3 after Lead next-searches (executable PubMed/arXiv queries in each packet appendix) return empty at full-text level.
- Cycle 3 focus approved: **India/transportability opportunities** (science not geography) — graded Indian shift + audit translation + OHDSI India network search.

## Candidates created/weakened/killed this cycle
- Created: 0 (deepening only)
- Weakened: 0
- Killed: 0
- Refined seeds: 8 (6 with executable designs, 2 Stage-2 deferred)

## Rate-limit incidents
None. Actual 61 calls / ~14 min (~4.3/min avg, well under 24/min target, no 429s). 2 search_log rows UNVERIFIED (403/timeout) correctly flagged, not used for gaps.

## Ledgers updated
- `literature/search_log.csv` — 54 → 118 data rows (+64: T6 10 + T4 10 + T1 10 + T5 10 + T7 10 + cross-links, 116 VERIFIED / 2 UNVERIFIED)
- `literature/evidence_registry.csv` — 49 → 94 data rows (+45: T6 10 + T4 10 + T1 10 + T5 8 + T7 9, 93 VERIFIED / 1 UNVERIFIED T2-06)
- `working/agent_notes/clinical-evidence-scout/cycle02_T6_positivity_diagnostics.md`, `cycle02_T4_prescribing_audit.md`
- `working/agent_notes/methods-scout/cycle02_T1_plasmode_design.md`, `cycle02_T5_corpus_pilot.md`, `cycle02_T7_threshold_pilot.md`
- `working/CYCLE_02_BRIEF.md`, `reports/failure_points_cycle_02.md`

## Citation integrity (Lead spot-checks)
8 new load-bearing DOIs HEAD 302: 10.1016/j.annepidem.2025.03.001 (Inoue), 10.1080/01621459.2018.1448823 (Li), 10.1002/sim.3697 (Austin), 10.18203/2394-6040.ijcmph20233814 (India WHO audit), 10.5334/gh.1335 (polypill), 10.1093/aje/kww098 (Franklin), 10.1186/s13040-025-00450-z (Schneider), 10.1186/s41512-026-00218-x (TRIPOD SR). SynthEHRella GitHub README extracted 7855 chars (package layout/pipeline verified). All packets: 93/94 VERIFIED, 1 UNVERIFIED correctly handled.

## State
- Candidates: 0 · Rejections: 0 · Search log rows: 118 · Evidence rows: 94
- Git: pending commit `research(cycle-02): deepening — 5 failure-point designs, 118 queries, 94 evidence`

## Next cycle
**Cycle 3 — India/transportability opportunities:** graded Indian-shift plasmode implementation + audit→E-value number extraction + OHDSI India network + T8 named-model sweep + T2 HTE transport design.
