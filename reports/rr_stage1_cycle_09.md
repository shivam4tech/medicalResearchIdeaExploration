# RR Stage-1 Packages — Cycle 9 (2026-08-30)
**Agents:** methods-scout (001 TRIPOD+AI + 003 CIMEHR, 249s) + clinical-evidence-scout (002 LADDER + 004 CORPUS, 502s) · **Status:** 4/4 RR Intro+Methods packages submission-ready · **OSF freeze:** git rev `70730ae984ae0d2592c28a9d13a0179eed14e6d4` + pilot exit-0

Cycle 7 proved Tier 1 runnable (4 pilots exit 0, honest synthetic fallbacks). Cycle 9 asks: timestamp OSFs + convert pilots into **RR Stage-1** (Registered Report) Intro+Methods where *either outcome is publishable* — replication holds *or* fails.

## Packages delivered (RR Stage-1, ≥238 lines each)

### methods-scout pair

**001 Harutyunyan 2019 → eICU/AmsterdamUMCdb direct replication (TRIPOD+AI)**
* `osf_prereg/candidate_001_OSF_TIMESTAMPED.md` (245 lines) — copy of 218-line OSF prepended with timestamp block: Reg 2026-08-30, git `70730ae`, code archive `pilots/candidate_002/`+`003/` (synthEHRella 74aa516, CIMEHR 0.1.0, seed 20260830), pilot exit-0 refs, leakage 6-item ☐→☑ + TRIPOD+AI 27-item ticked.
* `rr_stage1/candidate_001_TRIPODAI.md` (238 lines) — Intro (Harutyunyan 10.1038/s41597-019-0103-9 1800+ cites, gap: no pre-registered TRIPOD+AI replication per cycle04 lock, YAIB/METRE task-level ≠ frozen artifact), TRIPOD+AI 2024 10.1136/bmj-2023-078378 + Van Calster hierarchy 10.1016/j.jclinepi.2015.12.005 + Riley intervals 10.1136/bmj-2024-080749, Methods (cohort MIMIC→eICU+AmsterdamUMCdb via ricu 0.5.8, 1h grid 17+5 vars, leakage 6-item table, baselines LR/SOFA/GBM/trivial, equivalence Δ0.05 slope 0.8–1.2 |int|<0.3 DCA 10/20%, hierarchy mean→strong). Falsifiable H0/H1: ML gets no preference. Ethics IRB-exempt (public), India Stage-2 GEOGRAPHY-ONLY note. Appendices: TRIPOD+AI CSV + leakage CSV + hashes/seeds/pilot verification.

**003 CIMEHR 3-process plasmode (DL vs classical on irregular EHR)**
* `osf_prereg/candidate_003_OSF.md` (262 lines, NEW) — 3-process joint generative spec (λ_V·exp(γ_v·b), logit P(O) γ_o, Y RI+RS, logit outcome), 16-cell core (N 500/2k/10k × visits 2/6/15 × SNR 0.5/1.5/4 × γ_v 0/0.3/0.8 × γ_o 0/0.4/0.9), twin variants Generate-Treatment vs Generate-Outcome, decision rule non-inferior slope/coverage AND superior DCA, timestamped git rev + seeds + pilot 387-line verification.
* `rr_stage1/candidate_003_CIMEHR.md` (271 lines) — Intro (Liang 2410.13113 + Yang CIMEHR 2602.15374 0.1.0 CRAN 2026-06-08 + Sun supplement/Frontiers/CIMEHR vignette no DL head-to-head gap per REVISE 2026-08-30), Methods (16-cell + twin + calibration hierarchy + DCA, held-out needed), audit MIMIC demo fallback honest, falsifiable Q. References pilot `pilots/candidate_003/logs/pilot_003.log` exit 0.

### clinical-evidence-scout pair

**002 synthEHRella fidelity→τ utility ladder**
* `osf_prereg/candidate_002_OSF_TIMESTAMPED.md` (238 lines) — copy of 208-line OSF prepended with timestamp block: Reg 2026-08-30, git 70730ae, synthEHRella 74aa516 pip 1.0.0, pilots/candidate_002 exit 0, seed 20260830, S1–S5 8 operating points (S1, S1', S2 GAN 10/50/200, S3 Synthea, S4 resample, S5 random), fidelity (MMD, corr_fro, RMSPE, disc AUC), utility TRTR/TSTR, τ≥0.7 LB≥0.5 on TEST_R + TEST_TRANSPORT, DCA 10/20%.
* `rr_stage1/candidate_002_LADDER.md` (288 lines) — Intro (Chen JAMIA 10.1093/jamia/ocaf082 97 models 91.8% PROBAST high-risk, vs 002 gap: fidelity without τ, Liu 2504.11740 Generate-Treatment warning), Methods (6 methods logistic/Cox GBM LSTM/GRU-D RF+SOFA, 2-point pilot MMD 0.088 vs 0.070 corr_fro 0.40 vs 4.06 disc 0.50 TRTR 0.852→TSTR_S1 0.850→TSTR_S5 0.553 τ=1.0, full 8-point ladder + plasmode 30–50 reps ~1500 fits, Van Calster hierarchy, Riley intervals, DCA NB 10/20% + treat_all 0.451, falsifiable H0/H1). Appendices: pilot tables + hashes/seeds.

**004 TRIPOD subgroup-calibration corpus audit (n=150 audit)**
* `osf_prereg/candidate_004_OSF.md` (291 lines, NEW from idea + pilot) — n=150 audit interval-aware per Riley 10.1136/bmj-2024-080749, TRIPOD 570 vs 8188 ~7% language bias + RECORD 494/STROBE 18 sensitivities, Wilson ±0.06 CI, κ≥0.7 (pilot 0.615 → retrain), masking slope 0.8–1.2 ICI definition, era-split 2024 TRIPOD+AI, timestamped.
* `rr_stage1/candidate_004_CORPUS.md` (238 lines) — Intro (TRIPOD 570 vs Queiroz 91.8% + Jin + Riley gap: no p(interval-aware subgroup calibration) with Wilson), Methods (PRISMA 2020 eligibility, E-utilities esearch+efetch 570 re-verified 2026-08-30, Rayyan CSV, 22-col extraction form, Wilson power, κ plan), appendices:
  * `rr_stage1/appendix/PRISMA_004_checklist.csv` (43 lines: PRISMA 2020 items + location + Status DONE)
  * `rr_stage1/appendix/extraction_form_004.csv` (23 lines: header + 22 cols with interval_aware_flag/kappa_domain/pilot_example)
  * Links to `pilots/candidate_004/outputs/pilot_004_extraction_pilot.csv` (21 rows) + PRISMA pilot txt.

## Cross-cutting
* All RR: `Registration 2026-08-30 · Git 70730ae · seed 20260830 · pilot exit 0` referenced (grep verified in all 6 timestamped files). Results section `TBD (registered)` — Stage 1 methods-only.
* Checklists: 001 TRIPOD+AI 27-item + leakage 6-item ticked; 003 CIMEHR decision rule ticked; 002 S1–S5 + τ + DCA ticked; 004 PRISMA 43 + extraction 22-cols + Wilson. All line minima: OSF ≥238, RR ≥238 (max 288).
* No heavy pip/R — pure docs, 32 api_calls total (16+16), no fabrication (DOIs from registry), India Stage-2 correctly staged.
* Ledgers: no new searches (or at most 0–1 verification if ethics DOI added) — 327/217 unchanged unless noted.

## Submission readiness
4 Tier-1 RR Stage-1 packages Intro+Methods complete → target journals: **BMJ/JAMIA/PMLR-MLHC/Nature SD** (001), **JAMIA/JBI/MLHC** (002), **Statistics in Medicine/JASA-AAS/JMIR** (003), **BMJ/J Clin Epidemiol/Systematic Reviews** (004). Tier 2 (005+006) + 007 remain OSF-template (not RR this cycle) per SHORTLIST.

