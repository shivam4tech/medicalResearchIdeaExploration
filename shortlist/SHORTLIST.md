# Shortlist Freeze — 7-Candidate Shortlist (Cycle 6, 2026-08-30)
**Status: FROZEN — no open REVISE. All 3 REVISE dossiers (003, 004, 007) patched 2026-08-30. OSF pre-registrations cut for 001, 002, 005+006, 007.**
**Agents:** methods-scout + clinical-evidence-scout + adversarial-reviewer (cycle05 kill round p190/p268/p421)
**Reference:** `reports/candidate_matrix.csv` (KEEP 4 →7, REVISE 3→0, KILL 0) + `reports/promotion_cycle_05.md` + `shortlist/REVISE_LOG.md` (3 addenda)
**Companion:** `ideas/candidate_*.md` ×7 + `osf_prereg/` ×4

---

## 0. Freeze banner

This file is the single frozen shortlist for Cycle 6. All 7 dossiers are promotion dossiers with named data pathway + falsifiable framing + mandatory baselines. **No dossier carries an open REVISE** — kill packet p190/p268/p421 edits are applied and logged (REVISE_LOG.md). OSF hashes/seed placeholders are in `osf_prereg/`. Pilots may start tomorrow under this freeze. **FROZEN 2026-08-30 — Lead verifies before pilots.**

---

## 1. Priority tiers (execution order)

### Tier 1 — First-wave immediate (A/D; no DUA; code tomorrow on single GPU)
| Rank | Dossier | Class | Why tier 1 | Start | Scope ceiling |
|------|---------|-------|------------|-------|---------------|
| **1.1** | **001 Harutyunyan→TRIPOD+AI direct replication** | A public | Credentialed MIMIC-III/IV+eICU available weeks; frozen LSTM 2×128 dropout 0.3 Adam 1e-3; 27-item TRIPOD+AI; equivalence AUROC Δ0.05 slope 0.8–1.2 \|α\|≤0.3 subgroup≤0.10 | **Tomorrow** | **1.5–2.0 mo**, 2 persons (methods+clinical validator), single GPU for LSTM replay + CPU for calibration/DCA |
| **1.2** | **002 synthEHRella fidelity→τ threshold (S1–S5 ladder)** | A/D | MIMIC-III→IV + synthEHRella synthetic lake; 1500 fits pilot; Kendall τ≥0.7 LB≥0.5 + DCA 10/20% | **Tomorrow** | **1.5–2.0 mo**, 2 persons, single GPU for synth + CPU for τ/DCA |
| **1.3** | **004 TRIPOD subgroup-calibration corpus audit n=150 (REVISED)** | D literature | PubMed TRIPOD-defined validations 2015–2025, interval-aware extraction (slope CI/plot band per Riley, not point) + Wilson CI + masking rate + era-split TRIPOD+AI 2024 + RECORD/STROBE sensitivity; no PHI | **Tomorrow** | **1.5 mo**, 2 persons, CPU only |
| **1.4** | **003 3-process joint plasmode DL-vs-classical (REVISED)** | D simulation | **CIMEHR** as load-bearing engine: Yang 2026 10.48550/arXiv.2602.15374 + CRAN cran.r-project.org/web/packages/CIMEHR + GitHub ysph-dsde/CIMEHR; 16-cell core + Liang 2410.13113 sensitivity; Sun supplement + Frontiers LMM-robustness inspection logged; fully synthetic `rnorm` fallback allows coding before MIMIC extraction | **Tomorrow** | **2.0–2.5 mo**, 2 persons, single GPU for GRU-D/SeFT + CPU for LMM/JM |

**Tier 1 common:** Calibration hierarchy **Van Calster 10.1016/j.jclinepi.2015.12.005** (mean/weak/moderate/strong) + **Riley 10.1136/bmj-2024-080749** (individual bootstrap/Bayesian intervals, precision-targeted size) → **TRIPOD+AI 10.1136/bmj-2023-078378** 27-item. No DUA blocking; single-GPU budget (<$100–300 GPU-h); each phase independently publishable.

### Tier 2 — Staged India D+B (proxy-first while restricted DUA pends)
| Dossier | Class | Shared infrastructure | Proxy-first | Restricted |
|---------|-------|----------------------|-------------|------------|
| **005 Graded G0→G3 shift plasmode (transport vs recalibration)** | D+B staged | **Shared audit-anchored table** BMI 28.3→22.8, MONO 0→56.7%, age 62→48, HbA1c observed 78%→15%, generic 100→4.7%, AYUSH 0→96%, docs 100→8.5% + tilting (entropy balancing) + S_visit censoring + diagnostics SMD/S-score/ESS/trimming | **MIMIC-IV (weeks 1–2) + UKB-SA 1–3 mo** → 6–8-week plasmode + diagnostic curves (AUC 0.62→0.85+) publishable | **CARRS 2–3 mo + ICMR-INDIAB 3–6 mo** → national/rural re-tilt |
| **006 Audit→RR anchored E-value + NC ladder** | D+B staged | **Same G0→G3 table** → B→R* titration + 9-cell plasmode (3×P(U) 0.10/0.44/0.96 ×3×RR_UD 1.5/2.0/3.0) + NC ladder (Lipsitch) | MIMIC-IV benchmark + **UKB-SA 1–3 mo** AYUSH proxy → R* 1.4–2.3 titration | **CARRS longitudinal 2–3 mo** → prescribing + NC validation |

**Paired 005+006 submission plan:** One plasmode engineering sprint serves both papers. Phase 1 (months 1–2): plasmode-only G0→G3 + R* contour (joint OSF `osf_prereg/candidate_005_006_OSF.md`) → Registered Report Stage 1. Phase 2 (1–3 mo): UKB-SA RAP proxy validation. Phase 3 (2–6 mo): CARRS/ICMR-INDIAB restricted extension. **Two papers, one engineering cost.** Scope **2.0–2.5 mo effective each** (4–6 mo joint, shared).

### Tier 3 — Restricted B (proxy now)
| Dossier | Class | Immediate proxy | Restricted |
|---------|-------|-----------------|------------|
| **007 Ahlqvist centroids vs de-novo + GADA-free 6→3 ablation + overlap diagnostics (REVISED)** | B restricted | **UKB-SA managed proxy 1–3 mo**: centroids-vs-de-novo + ARI + S-score/ESS on SA diaspora — independently publishable while CARRS pends | **CARRS 2–3 mo (primary) + ICMR-INDIAB 3–6 mo + CMC/AIIMS new-onset T2D enriched 2–4 mo (ANDIS-analogous sampling-frame sensitivity)** → primary paper (see osf_prereg/candidate_007_OSF.md: IOPW, 6→3 ablation, CKD/retinopathy/insulin HRs, GMM/hierarchical + continuous risk) |

**Tier 3 scope:** **4–6 mo proxy+B; 8 mo with ICMR-INDIAB/registry**. CPU only. Per-dossier **1.5–2.5 mo** effective (staged).

---

## 2. The 7 dossiers at a glance (frozen)

| # | Title | Territory | Class | Verdict | Data pathway | Total (matrix) | Confidence |
|---|-------|-----------|-------|---------|--------------|----------------|------------|
| 001 | Harutyunyan 2019 MIMIC→eICU TRIPOD+AI direct replication (leakage audit + calibration/DCA/subgroup) | T8 | A | KEEP | MIMIC-III/IV + eICU + AmsterdamUMCdb (weeks) | 94 | Medium-High |
| 002 | Fidelity→τ threshold via synthEHRella (S1–S5 ladder + Kendall τ≥0.7 + DCA) | T7 | A/D | KEEP | MIMIC-III/IV + synthEHRella toolkit | 90 | Medium |
| 003 | 3-process joint plasmode DL-vs-classical (GRU-D/SeFT vs LMM/JM) — **REVISED CIMEHR engine** | T1 | D | REVISE→KEEP | D simulation (CIMEHR + Liang sensitivity) | 84 | Medium (engine CIMEHR) |
| 004 | TRIPOD subgroup-calibration corpus audit n=150 (interval-aware + era-split) — **REVISED** | T5 | D | REVISE→KEEP | PubMed/Europe PMC corpus | 86 | Medium |
| 005 | Graded Indian shift G0→G3 plasmode (transport vs recalibration + diagnostics) **paired with 006** | T6 | D+B | KEEP | MIMIC-IV (D) + UKB-SA (B proxy) + CARRS/ICMR-INDIAB (B restricted) | 95 | Medium-High |
| 006 | Audit→RR anchored E-value + NC ladder (WHO audit → B/R* titration + 9-cell) **paired with 005** | T4 | D+B | KEEP | WHO audits (D) + MIMIC (A) + UKB-SA/CARRS (B) | 94 | Medium-High |
| 007 | Ahlqvist 5-cluster transport centroids vs de novo + GADA-free 6→3 + overlap — **REVISED** | T2 | B | REVISE→KEEP | UKB-SA (proxy) + CARRS/ICMR-INDIAB/CMC-AIIMS (restricted) | 85 | Medium-High (core) |

**Mean 89.7 — 8-gate preserved. No dossier carries open REVISE.**

---

## 3. India relevance — STRESSES-ASSUMPTION framing (clinical half)

**Which dossiers STRESS assumptions vs are GEOGRAPHY-ONLY:**

- **STRESSES-ASSUMPTION (India is the instrument):** **005, 006, 007**. Indian care stresses *positivity/overlap, S-admissibility, consistency/treatment-version, exchangeability via thin-fat effect (MONO OR 6.90), and informative missingness/time-zero*. Transporting to US/Canada would **not** expose these violations.
  - **005:** MONO joint support near-zero in BMI≥25-screened source; S-admissibility via cost/formulary/AYUSH/shift-staffing → Y; generic 4.7–64.9% treatment-version.
  - **006:** AYUSH 44–96% unmeasured U → exchangeability + consistency violation; polypharmacy 71% → positivity collapse; formulary NLEM 61–87% → exposure misclassification.
  - **007:** Younger/low-BMI diabetes (BMI 21–22 SA vs 30 White, 5–10y earlier), GADA/HOMA scarcity → positivity + measurement transport. **IMI-RHAPSODY 10.1007/s00125-021-05490-8 European cross-validation does NOT generalize here** (see §9).
- **GEOGRAPHY-ONLY for v1 (Stage-2 India extension natural):** **001, 002, 003, 004**. V1 questions population-agnostic; Indian extension at Stage-2 defensible but decorative if forced into v1.

**Shared audit anchors:** ICMR-INDIAB-17/-23 (MONO 43.3%, state 34.8–56.7%, T2D OR 6.90); CARRS phenotyping; WHO audits (generic 64.9→4.7%, injections 4→90%, diagnosis docs 8.5%); NSS AYUSH 10–40% vs Galib 95.9%. All 302-verified, JATS-extracted.

---

## 4. DUA routes + honest timelines (clinical half)

| Dossier | Dataset | Route | Timeline (honest) | Mitigation while pending |
|---------|---------|-------|-------------------|--------------------------|
| 001,002,003,004 | MIMIC-III/IV, eICU, corpus, simulation | PhysioNet credentialed (CITI+DUA) / open | **Weeks 1–2** | Code/plasmode scaffold runs before data lands |
| 005+006 | **UKB-SA proxy** | UKB AMS category 2 + RAP, PI+institution, EGC | **1–3 months** | Phases 1 plasmode-only publishable without proxy |
| 005+006, 007 | **CARRS** (n~12k) | CARRS Steering via Emory/PHFI, restricted DUA | **2–3 months** | UKB-SA proxy + plasmode-only de-risk |
| 005+006, 007 | **ICMR-INDIAB** (n~113k, 31 states) | ICMR-NIE + MDRF collaboration | **3–6 months (open prevalences via Lancet/IJMR immediately)** | Tilting targets from published MONO tables |
| 007 | **CMC Vellore / AIIMS Delhi new-onset T2D registry** | Institutional MOU + ethics, tertiary clinic | **2–4 months** | ANDIS (incident) vs CARRS (prevalent) sampling-frame sensitivity |
| — | **CARRS GADA/HOMA dictionary** | *Not public — honest note* | **Unconfirmed pending DUA** | Pre-registered branch: 3-var co-primary if 6-var completeness <85% |

**Scope ceiling honesty:** Per dossier **1.5–2.5 mo personnel/compute** (Tier 1: 1.5–2.0 mo, Tiers 2–3: 2.0–2.5 mo effective via shared plasmode). Total wall 4–8 mo staggered, not 7× sequential.

---

## 5. Scope ceilings & compute (methods half — merged)

_All ceilings are wall-clock with 2 investigators (1 biostatistician + 1 ML engineer) + 0.25 FTE clinician. Compute via CIMEHR pipeline where applicable._

| Dossier | Question (1 line) | Tier | Compute (via CIMEHR / GPU) | Cost | Timeline (wall-clock) | First-wave? |
|---------|-------------------|------|-----------------------------|------|-----------------------|-------------|
| **001** Harutyunyan OSF | MIMIC-III→eICU/AmsterdamUMCdb frozen 2×128 LSTM | A public | Single GPU <48h locked v1 (2–4h per run ×15 runs 5-fold×3 seeds); inference hours | **<$100 cloud** | **3–4 weeks** to pre-registered external results (Week 1 Docker on demo; Week 2 OSF lock; training 1–2 days) | **YES — tomorrow** |
| **002** synthEHRella τ ladder | Fidelity→ranking τ≥0.7 LB≥0.5 + DCA 10/20% + MIMIC-III→IV | D simulation | **200–300 GPU-h** (1,500 fits pilot: LSTM ~400 fits ×2–4h, LR/GBM CPU parallel; 4 GPUs →2–3 days naive → ~5–8 days single+parallel) | **≈$150–250** | **6–8 weeks** to pilot preprint | **YES — tomorrow** |
| **003** T1 plasmode DL-vs-classical | 3-process joint (CIMEHR engine) 16×200 benchmark GRU-D/SeFT vs LMM/JMbayes2 | D simulation | **Via CIMEHR pipeline:** simData 1–3s/repl; `lme4` 2–5s + `JMbayes2` 30–90s + `mice` 10–20s + GRU-D 45–90s GPU + SeFT 30–60s GPU. **Total 16×200×~5 min ≈267 GPU-h naive; Snakemake 4 workers wall-clock ≈80–120 GPU-h +180–260 CPU-h ≈5–8 days single+1 GPU.** Practical N=2k ≈30h parallel (scaffold 2 toy cells N=500×20 Week1 CPU-only). | **<$50 N=2k core; ~$150–250 N=10k ext.** | **4–6 weeks** core + 2–4 weeks write → **1.5–2.5 mo** | **YES after REVISE (CIMEHR reframe 2026-08-30)** |
| **004** T5 TRIPOD corpus audit | n=150 TRIPOD external validations prevalence interval-aware | D literature | **Laptop only, no GPU** — PubMed E-utils + Europe PMC REST + Rayyan | **<$50** | **4–6 weeks** extraction + 2–4 weeks write → **1.5–2.5 mo** | **YES after REVISE (interval-aware + corpus sensitivity 2026-08-30)** |
| **005+006 Paired G0→G3** | Graded Indian shift shared audit-anchored plasmode + NC ladder | D+B staged | Plasmode weeks + UKB-SA/CARRS DUA-waits 1–6 mo (honest) | — | Plasmode-only 6–8 weeks publishable now; full staged 4–8 mo | **Paired — shared infrastructure** |
| **007 Ahlqvist transport** | Centroids vs de novo GADA-free overlap diagnostics | B restricted | CARRS/ICMR/UKB-SA 2–6 mo DUA waits, CPU | — | Proxy 6–8 weeks, restricted 4–6 mo | **B — UKB-SA proxy first** |

**Out-of-scope Stage-2:** Indian-typical plasmode beyond λ_V/γ_v (003), fairness mitigation, many-analysts re-extraction (004), Indian ICU transport (001). **Shared plasmode+MIMIC+UKB-SA infrastructure** powers 003(D), 002(D), 005+006(D→B); 001(A) public provides independent path. All first-wave D/A executable tomorrow without restricted data.

---

## 6. Paired 005+006 — shared audit-anchored table + tilting + S_visit + diagnostics + submission (clinical+methods)

**One G0→G3 table powers two questions** — see `osf_prereg/candidate_005_006_OSF.md` (shared table + tilting + S_visit censoring + staged D+B for 005 transport vs recalibration + 006 B→R* titration + 9-cell plasmode + diagnostics SMD/S-score/ESS/trimming + paired submission plan + harmonization stub via ricu/METRE/YAIB + 27-item TRIPOD+AI + leakage checklist):

- **Shared dimensions:** BMI 28.3→22.8, MONO 0→56.7%, age 62→48, HbA1c 78→15% observed, generic 100→4.7%, AYUSH 0→96%, docs 100→8.5%, polypharmacy 1.8→6.8 drugs/Rx — entropy-balanced tilting + Liang 3-process S_visit censoring (shared frailty).
- **005 diagnostics (pre-registered):** SMD (\|SMD\|>0.1 Austin 10.1002/sim.3697), S-score AUC (L1 logistic P(S=1\|X)), ESS, trimming α=0.05/0.10 (Sturmer/Lee/Crump) → dose-response decision: **recalibration suffices** (ICI<0.05, slope 0.9–1.1, ΔAUROC<0.03) vs **transport required** (ICI>0.08, ΔAUROC>0.04, AUC>0.80, ESS<50%, trimming>20% → ATO drift Li).
- **006 diagnostics:** Audit→RR translation B(p1,p0,RR_UD) = [p1·(RR_UD−1)+1]/[p0·(RR_UD−1)+1] → **R* fixed-point** E-value(R*)=B; titration RR_UD 1.2→4.0; 9-cell plasmode P(U)=0.10/0.44/0.96; **NC ladder** (Lipsitch 10.1097/EDE.0b013e3181d61eeb) as co-primary falsification (trauma/appendicitis).
- **Harmonization stub:** `ricu`/METRE/YAIB (Patel 10.64898/2026.05.03.26352335 watch) — MIMIC-IV→OHDSI LOINC/RxNorm; UKB-SA field-ID mapping; CARRS stub pending DUA.
- **Economy:** Audit tables + MIMIC extraction + tilting code written once; single OSF covers both; two papers with shared methods figure.

---

## 7. Calibration hierarchy & reporting standards (reused 4×)

All applicable dossiers (001, 002-benchmark framing, 003, 005, 007) reuse:

- **Van Calster 10.1016/j.jclinepi.2015.12.005** — calibration hierarchy: mean → weak (intercept+slope) → moderate → strong.
- **Riley 10.1136/bmj-2024-080749** — individual-level bootstrap/Bayesian intervals around risks (precision-targeted validation size); equivalence bounds and CI-based inference.
- **→ TRIPOD+AI 10.1136/bmj-2023-078378** — 27-item checklist mapped in each OSF (including leakage items, fairness/subgroup, code availability). Item-level mapping tables in `osf_prereg/candidate_001_OSF.md`, `002_OSF.md`, `005_006_OSF.md`, `007_OSF.md`.

No dossier invents a new reporting standard — all map to TRIPOD+AI.

---

## 8. Preprint watch — Patel YAIB/METRE (cross-dossier)

- **Patel et al. 10.64898/2026.05.03.26352335** (YAIB/METRE — preprinted 2026-05-03, medRxiv `10.64898/…` namespace) — benchmark for MIMIC harmonization. **Action:** Monitor for MIMIC→OHDSI mapping updates for SA labs/meds. If YAIB/METRE revises SA phenotype definitions, re-run 005+006 S-score and 007 UKB-SA harmonization. Dossiers that depend on YAIB mappings (001 leakage harmonization, 005/006/007 UKB-SA overlap) will add a sensitivity note at proofs if a new YAIB version drops before submission. No dossier is blocked pending this — it is a watch, not a dependency.

---

## 9. Cross-dossier risks (honest, mitigation)

| Risk | Affected | Mitigation |
|------|----------|------------|
| **CARRS GADA/HOMA <10% complete** (REVISE 007) | 007 primary | Pre-registered branch: 6-var aspirational → sensitivity-only; **3-var (age/BMI/HbA1c) co-primary** if completeness ≥85% not met |
| **CARRS indicator delay 3–4 mo** | 005/006/007 | Staged D+B: proxy-first (UKB-SA 1–3 mo) + plasmode-only publishable; no idle time |
| **ANDIS (incident) vs CARRS (prevalent) frame mismatch** | 007 | **CMC/AIIMS new-onset T2D registry (2–4 mo)** as ANDIS-analogous secondary target (tertiary, new-onset enriched, GADA/C-peptide research subset) |
| **Audit arm-level P(U\|E) imputed not observed** | 006 | Bracketed translation + titration contour over (p1,p0) envelope + 9-cell plasmode false-robust calibration |
| **Preprint closes gap before submission (e.g., 2025–2026 Ahlqvist→India overlap)** | 007 highest, 005 | Adversarial IndMED+thesis sweep 2026-08-30 (0 closing hits); resurrect as HTE extension if closes (causal forest) |
| **IMI-RHAPSODY misread as defeater** | 007 | **4-part distinction logged:** European cross-validation (15,940) not Indian LMIC; C-peptide/HDL substitution sens 80–91% but no SMD/S-score/ESS/IOPW and no GADA-free 6→3 ablation — strengthens European stability, makes Indian stress test informative (see idea 007 Addendum §1) |
| **UKB-SA ≠ India-resident SA (diaspora proxy bias)** | 005/006/007 | Reported as limitation; ICMR-INDIAB/CARRS validate proxy S-scores at Stage 2 |
| **YAIB/METRE harmonization drift** | 001/005/006/007 | Preprint watch + sensitivity re-run (see §8) |
| **NC ladder outcome (trauma) unavailable on Indian EHR** | 006 | Pre-spec alternative NCs (dermatology/viral URI) per Lipsitch; TBD |

---

## 10. Outcome definitions — physician validation TBD (clinical half)

| Dossier | Outcome(s) | Definition (pre-registered) | Physician validator |
|---------|------------|-----------------------------|---------------------|
| 001 | In-hospital mortality | MIMIC-III/IV in-hospital death + Harutyunyan time-zero (ICU admit); eICU hospital-discharge mortality | **Intensivist TBD** (time-zero / leakage validation) |
| 002 | Methods ranking preservation (Kendall τ) + DCA | AUROC-ranking over MIMIC-III real vs S1–S5 synthetic; net benefit at 10%/20% (Vickers) | Methods TBD |
| 003 | Discrimination + calibration + interval coverage + DCA | 16-cell simulation joint criterion (Schneider template) | Methods TBD |
| 004 | Subgroup calibration reporting prevalence | Overall pass vs ≥1 subgroup fails (masking rate); Wilson CI + interval-aware (slope CI/plot band per Riley) + era-split TRIPOD+AI 2024 | **Epidemiologist TBD** (RECORD/STROBE adjudication) |
| 005 | ICI/slope/AUROC/DCA per G0→G3 + SMD/AUC/ESS/trimming | Van Calster hierarchy + Riley intervals; diagnostics thresholds locked | TBD (HbA1c/generic plausibility) |
| 006 | RR_obs E-value vs B_audit + R* + NC RR_NC | VanderWeele E-value; Hernán target-trial; Lipsitch NC (trauma/appendicitis) | **Pharmacoepidemiologist TBD** (RR_UD sweep; NC appropriateness) |
| **007** | **CKD (eGFR decline ≥40% or UACR progression) + retinopathy (fundoscopy/ICD proxy) + insulin initiation (Rx record)** | **Per Ahlqvist Fig 3–4 analogues; Cox HR vs MARD reference; HR gradient replication rule (SIRD→CKD highest, SIDD→retinopathy highest) with pre-registered thresholds completeness≥85%/AUC<0.70/ESS>70%/ARI≥0.60** | **Endocrinologist TBD — validate 3-var triage rule actionability + CARRS phenotype capture (eGFR/UACR, fundoscopy availability, prescription records)** |

All outcomes retrospective, de-identified; biomarker (GADA/HOMA) measured as research subset where available, not clinical mandate.

---

## 11. Ethics & privacy (clinical + methods)

- **MIMIC-IV / eICU / AmsterdamUMCdb:** HIPAA Safe Harbor de-identified; PhysioNet credentialed (CITI+DUA); IRB exemption for secondary analysis.
- **UKB-SA:** UK Biobank EGC oversight; AMS + RAP cloud-compliant; PI sign-off; no download beyond extracts.
- **CARRS / ICMR-INDIAB / CMC-AIIMS:** Restricted de-identified extracts only; DUA via PHFI/Emory (CARRS Steering), ICMR-NIE/MDRF (ICMR-INDIAB), institutional MOU (CMC/AIIMS); ICMR ethics guidelines.
- **Corpora/simulation (003,004,005-G0,006-G0):** Open or de-identified — no PHI; WHO audits CC-BY aggregate prescription-level; simulation uses `rnorm` fallback before MIMIC extraction if needed.
- **Pre-registration:** OSF prevents HARKing on k/feature-set/missing/overlap thresholds (007 thresholds locked: completeness≥85%, S-score AUC<0.70, ESS>70%, ARI≥0.60).

---

## 12. Linked artifacts & ranking (methods half prioritization)

**Ranked order to start (methods half):**
1. **001** — cleanest v1, no DUA, highest method rigor signal, Medium-High confidence — **run tomorrow**
2. **002** — methods-ranking τ is novel decision threshold, DCA 10/20% clinically framed — **run tomorrow**
3. **003** — REVISE→KEEP after CIMEHR reframe (Yang 2602.15374 as engine, 16-cell core + Schneider 10.1186/s13040-025-00450-z preserved; compute via CIMEHR pipeline explicit) — **run after 1-page sign-off**
4. **004** — REVISE→KEEP after interval-aware vs point sharpened + Wilson+masking+era-split vs DCGS/KAISEN/PMID 41643238 study-level compliance + corpus sensitivity (570 vs 8188) + RECORD/STROBE — **run after sign-off**

**Artifacts:**
- OSF Preregs: `osf_prereg/candidate_001_OSF.md` (Harutyunyan 17+5 vars, 2×128 LSTM, 6 leakage items, ricu/METRE/YAIB stub, 27-item TRIPOD+AI, equivalence Δ0.05 slope 0.8–1.2 \|α\|≤0.3 subgroup ≤0.10, LR/SOFA/GBM/trivial + hashes/seeds)
- `osf_prereg/candidate_002_OSF.md` (S1–S5 ladder + τ≥0.7 LB≥0.5 + DCA 10/20% + MIMIC-III→IV + 1500 fits pilot)
- `osf_prereg/candidate_005_006_OSF.md` (paired G0→G3 shared table + tilting + S_visit + diagnostics SMD/S-score/ESS/trimming + B→R* + 9-cell + harmonization stub via ricu/METRE/YAIB) — **clinical pair**
- `osf_prereg/candidate_007_OSF.md` (Ahlqvist centroids vs de-novo with IOPW/6→3/GMM/hierarchical + thresholds + outcomes CKD/retinopathy/insulin) — **clinical**
- Patched dossiers: `ideas/candidate_003.md` + `ideas/candidate_004.md` + `ideas/candidate_007.md` (REVISE Addenda 2026-08-30 — 3/3)
- REVISE log: `shortlist/REVISE_LOG.md` (entries for 003 p190, 004 p268, 007 p421)
- This shortlist: **single frozen file all 7, 0 open REVISE** — pilots released on Lead verify.

---

## 13. Frozen checklist — so pilots can start with no HARKing risk

- [x] All 7 dossiers patched (003 CIMEHR engine + 004 interval-aware + 007 IMI-RHAPSODY/IndMED/GADA/thresholds) — **no open REVISE**
- [x] Priority tiers (1) First-wave A/D 001/002/004-revised/003-revised single GPU **code tomorrow**; (2) Staged D+B 005+006 paired proxy-first + MIMIC+UKB-SA 1–3 mo → CARRS/ICMR-INDIAB 2–6 mo; (3) Restricted B 007 proxy now
- [x] India STRESSES-ASSUMPTION framing (005/006/007 vs GEOGRAPHY-ONLY 001–004)
- [x] DUA routes + honest timelines + scope ceilings (1.5–2.5 mo per dossier)
- [x] Paired 005+006 shared plasmode+MIMIC+UKB-SA infrastructure + submission plan + 9-cell + paired OSF
- [x] Calibration hierarchy reuse (Van Calster + Riley → TRIPOD+AI) + preprint watch Patel 10.64898/2026.05.03.26352335 YAIB/METRE
- [x] Cross-dossier risks + outcome definitions (physician TBD) + ethics/privacy
- [x] OSF pre-regs cut: `candidate_001_OSF.md`, `candidate_002_OSF.md`, `candidate_005_006_OSF.md`, `candidate_007_OSF.md` (004 supplement via 004 dossier OSF note)
- [x] Candidate matrix `reports/candidate_matrix.csv` KEEP 7 frozen
- [x] This file is **single frozen file all 7** per Cycle 6 Output contract — **Lead verify then release pilots.**

