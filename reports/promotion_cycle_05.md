# Promotion + Kill Round Report — Cycle 5 (2026-08-30)
**Agents:** methods-scout (4 dossiers 001–004) + clinical-evidence-scout (3 dossiers 005–007) + **adversarial-reviewer WAKE** (first activation, 27 kill-try searches, 10 closest defeaters). **Status:** 7/7 dossiers COMPLETE + 1 kill-round packet (74K chars, 535 lines). **Ledgers:** search_log 306 lines (305 data rows: 303 VERIFIED / 2 UNVERIFIED-timeout from Cycle 1, 0 new UNVERIFIED) — +74 this cycle (27 adversarial + 47 dossier); evidence 210 lines (209 data rows: 204 VERIFIED / 2 TRUE / 1 UNVERIFIED-T2-06 + 1 cycle-tag + 1 compliance-typed — 0 new UNVERIFIED) — +40 this cycle. Spot-check 5/5 new adversarial DOIs 302 (Patel 10.64898/2026.05.03.26352335, CIMEHR 10.48550/arXiv.2602.15374, CoMedBench 10.48550/arXiv.2608.12805, K-IPO 10.48550/arXiv.2607.16478, IMI-RHAPSODY 10.1007/s00125-021-05490-8). All dossiers ≥8 papers, ≥1 DOI 302; all include Evidence AGAINST + 8-gate headings + India verdict.

## Executive summary
Cycle 5 asked *which of the 8 designs survive promotion to shortlist when an adversarial tries to kill them under alternative indexing?* Deep dossier work (7 dossiers, 252–329 lines each, Medium to Medium-High) plus the first-ever adversarial WAKE (27 pointed searches exhausting STROBE/RECORD/PROBAST vs TRIPOD, fairness vs subgroup calibration, LMIC+overlap, plasmode/observation-process synonyms, HTE causal-forest, LMIC full-text) delivers a clean verdict: **4 KEEP (shortlist-ready with citation fixes), 3 REVISE (fixable with stated edits, then shortlist-ready), 0 KILL**. No dossier is unfixable; no gap closed outright. The kill round's closest defeaters are all **near-equivalents distinguished as task-level, feature-importance, study-level compliance, European-only, or generative-engine** — not exact defeaters — and each dossier's rebuttal is pre-written with resurrection conditions. Together they form a **7-candidate shortlist** (4 immediate A/D public, 2 staged India D+B, 1 restricted B) with no PHI for the first wave and a paired India submission (005+006 shared G0→G3 plasmode) for the second wave.

## Kill-round ledger (27 searches, verbatim)
| # | Dossier | Kill query (verbatim) | Hits | Verdict |
|---|---------|------------------------|------|---------|
| 1 | 001 T8 | `STROBE RECORD PROBAST MIMIC eICU external validation prediction model` | 5 | NEAR-KILL — Patel 2026 MIMIC→eICU calibration (task-level, not Harutyunyan frozen) |
| 2 | 001 T8 | `calibration slope intercept decision curve analysis external validation MIMIC ICU` | 5 | NEAR-KILL — Patel framework + PMC13225492 task-level |
| 3 | 001 T8 | `many analysts multiverse researcher degrees freedom benchmark drift intensive care` | 0 | **FAILED-TO-KILL** — no clinical-EHR many-analysts (gap survives) |
| 4 | 002 T7 | `synthetic data fidelity rank correlation Kendall tau TSTR MIMIC` | 5 | NEAR-KILL — K-IPO 2607.16478 feature-importance τ (not methods ranking) |
| 5 | 002 T7 | `plasmode simulation synthetic EHR methods ranking preservation fidelity threshold` | 5 | FAILED-TO-KILL — Liu fragility (not τ threshold) |
| 6 | 002 T7 | `synthetic EHR validation utility privacy fidelity threshold MMD TSTR train synthetic test real` | 5 | FAILED-TO-KILL — frameworks, no τ threshold |
| 7 | 003 T1 | `joint model plasmode informative visit observation irregular time series deep learning` | 5 | NEAR-KILL — Yang 2026 CIMEHR 2602.15374 shared random effects engine published |
| 8 | 003 T1 | `GRU-D SeFT neural ODE vs linear mixed model longitudinal EHR calibration coverage` | 0 | **FAILED-TO-KILL** — no joint-plasmode DL-vs-LMM on calibration/coverage/DCA (strong signal) |
| 9 | 003 T1 | `informative presence observation process longitudinal EHR joint model simulation` | 5 | FAILED-TO-KILL — Liang within-joint, no DL comparator |
| 10 | 004 T5 | `algorithmic fairness calibration subgroup reporting prediction model external validation` | 5 | NEAR-KILL — KAISEN 2607.28608 + DCGS 2026.06.17.26355900 (fairness metrics, not prevalence audit) |
| 11 | 004 T5 | `PROBAST CHARMS TRIPOD subgroup calibration systematic review prediction model` | 5 | NEAR-KILL — maltreatment TRIPOD/PROBAST compliance review PMID 41643238 (compliance not prevalence+Wilson+era-split) |
| 12 | 004 T5 | `STROBE RECORD reporting guideline calibration subgroup external validation prediction model` | 5 | FAILED-TO-KILL — no subgroup corpus audit under STROBE/RECORD |
| 13 | 005 T6 | `Indian prescribing audit WHO indicators LMIC transportability overlap weighting` | 5 | FAILED-TO-KILL — WHO audits alone, no transport/overlap |
| 14 | 005 T6 | `LMIC transportability generalizability overlap weighting propensity South Asia` | 0 | **FAILED-TO-KILL** — zero LMIC overlap-weighting hits (strong gap signal) |
| 15 | 005 T6 | `India health system shift plasmode covariate shift measurement frequency` | 5 | FAILED-TO-KILL — generic decomposition, no Indian-anchored plasmode |
| 16 | 006 T4 | `E-value bias analysis prescribing audit India unmeasured confounding` | 5 | FAILED-TO-KILL — E-value generic, no audit-anchored prevalence |
| 17 | 006 T4 | `negative control outcome India EHR target trial emulation` | 5 | FAILED-TO-KILL — TTE generic, not audit-anchored NC |
| 18 | 007 T2 | `Ahlqvist diabetes clusters South Asian India validation transportability` | 5 | NEAR-KILL — MDPI cluster review + Helda thesis (descriptive, not transport+overlap) |
| 19 | 007 T2 | `diabetes subtypes clustering heterogeneity treatment effect causal forest transport` | 0 | **FAILED-TO-KILL** — no HTE causal-forest transport |
| 20 | 007 T2 | `Ahlqvist 5 clusters latent class diabetes transport generalizability` | 5 | NEAR-KILL — ML reproducible prediction PMC11519166 (description, not centroids-vs-de-novo) |
| 21 | 001 follow | `Calibration Drift Under Cross-Institutional Deployment MIMIC eICU Patel` | 5 | CONFIRMS Patel medRxiv 10.64898/2026.05.03.26352335 / rs-9602675 |
| 22 | 001 follow | `Postoperative stroke MIMIC eICU external validation Random Forest calibration` | 5 | CONFIRMS postoperative stroke RF MDPI 2673-7426/6/2/16 |
| 23 | 002 follow | `CoMedBench synthetic medical data fidelity downstream utility Kendall` | 5 | NEAR-KILL — CoMedBench 2608.12805 (+ PMC12546680) |
| 24 | 004 follow | `Demographic Calibration Gap Score DCGS calibration error subgroup` | 5 | NEAR-KILL — DCGS single-model metric (not corpus prevalence) |
| 25 | 007 follow | `Replication and cross-validation of type 2 diabetes subtypes 2021` | 5 | NEAR-KILL — IMI-RHAPSODY 10.1007/s00125-021-05490-8 (European, not Indian+overlap) |
| 26 | 003 follow | `Joint Modeling Longitudinal EHR Informative Visiting Observation 2025 shared random effects` | 5 | NEAR-KILL — CIMEHR 2602.15374 + CRAN + GitHub ysph-dsde/CIMEHR |
| 27 | 002 follow | `Shoshan synthetic data model selection rank correlation 2023` | 0 | **FAILED-TO-KILL** |

Rate-limit: ≤2 concurrent, sequential 2s delay, <24/min, bounded.

## Verdicts per dossier (adversarial output contract)

### 001 — Harutyunyan MIMIC→eICU TRIPOD+AI Direct Replication — **KEEP** (shortlist-ready)
- **Closest prior:** Patel 2026 medRxiv **10.64898/2026.05.03.26352335** / Research Square rs-9602675 (MIMIC-IV 52k → eICU 114k, LR/RF/XGBoost, slope≈1.0, DCA) — **task-level calibration-aware external validation, NOT frozen Harutyunyan LSTM, NOT pre-registered OSF, NOT TRIPOD+AI 27-item, NOT leakage checklist, NOT subgroup heterogeneity**. Secondary: postoperative stroke RF MIMIC→eICU MDPI (calibration reported, task-level). YAIB 216k stays task-level drift.
- **Strongest FOR:** Per-model sweep (Harutyunyan/Rajkomar/Moor/GRU-D × TRIPOD+AI + STROBE/RECORD/PROBAST + calibration/slope) returns **zero pre-registered frozen-Harutyunyan with original hyperparameters, leakage-controlled, eICU/AmsterdamUMCdb, AUROC+AUPRC+slope/intercept+ICI+Brier+DCA+subgroup**. Gap is existence claim for pre-registered replication, not "external validation is scarce." RR guarantees negative (did-not-replicate) publication.
- **Strongest AGAINST:** Patel proves MIMIC→eICU calibration-aware validation publishes without Harutyunyan; YAIB covers task-level transport. If YAIB adds OSF+TRIPOD+AI for frozen Harutyunyan before RR, gap closes. Mitigation: foreground leakage audit + subgroup heterogeneity + equivalence bounds + 27-item mapping as contributions; cite Patel as closest and distinguish.
- **Challenges:** Data none (A public PhysioNet/ODAP weeks); Stats sound (slope SE 0.04–0.06, power >0.90); Clinical actionable (threshold misguidance, fairness); Publication RR fit. **Flip if:** OSF-timestamped frozen Harutyunyan TRIPOD+AI replication appears → pivot to Rajkomar FHIR or sequestered sepsis winner.
- **Gate anchor:** Medium-High. 8-gate dossier complete with harmonization stub (17+5 vars via ricu), leakage checklist 6 items, equivalence Δ0.05/slope 0.8–1.2, baselines LR/SOFA/GBM/trivial, scope 1.5–2.5 mo, GEOGRAPHY-ONLY v1.

### 002 — Fidelity→τ Threshold via synthEHRella — **KEEP** (shortlist-ready, wording fix)
- **Closest prior:** CoMedBench **10.48550/arXiv.2608.12805** (multi-source fidelity+utility) + K-IPO **10.48550/arXiv.2607.16478** + PMC12546680 — all **feature-importance Kendall τ, not methods-ranking τ with DCA+transport**. Chen JAMIA **10.1093/jamia/ocaf082** benchmarks generators, not methods via generators.
- **FOR:** No calibrated fidelity threshold f* where synthetic-supported **methods ranking (logistic/Cox vs GRU-D)** preserves real ranking via τ≥0.7 LB≥0.5 + DCA 10/20% + MIMIC-III→IV transport exists. S1–S5 ladder (plasmode G-Treatment → S1′ G-Outcome → GAN → Synthea → Resample → Prevalence-random) + plasmode twin fragility (Liu 2504.11740) is immediately runnable, publishable cautionary.
- **AGAINST:** Referee claims "τ for synthetic already done" via K-IPO/CoMedBench feature-importance. Mitigation: crisp title distinction — **benchmark of generators vs meta-benchmark of instrument**, foreground DCA fragility (AUC agrees while DCA flips).
- **Challenges:** Data zero (MIMIC-III/IV + synthEHRella open); Stats SE 0.06–0.10 at τ≈0.5 adequate; Clinical DCA per threshold decision-relevant. **Flip if:** real-vs-synthetic methods-ranking τ + fidelity sweep + DCA + MIMIC-III→IV transport preprint appears.
- Medium.

### 003 — 3-Process Joint Plasmode DL-vs-Classical — **REVISE → KEEP after edits** (generative novelty narrowed, benchmark survives)
- **Closest prior:** Yang 2026 **10.48550/arXiv.2602.15374** + **CIMEHR** CRAN/GitHub ysph-dsde/CIMEHR — **unified 3-process joint (visit+observation+longitudinal shared frailty) now open-source; generative spec no longer novel**. Schneider **10.1186/s13040-025-00450-z** (joint vs Cox), Sun **10.34133/hds.0456** catalogue — no DL-vs-joint on joint criterion. T1-KILL2 (GRU-D vs LMM calibration) returned **0 hits** — strong gap signal for the surviving claim.
- **FOR:** No joint-plasmode pits GRU-D/SeFT/GRU-ODE-Bayes vs LMM (lme4/nlme) + joint (JMbayes2/joineRML) on **joint criterion (AUC + calibration slope/intercept + coverage + DCA) with tunable γ_v, γ_o, λ_V, σ, effect θ1**. 16×200 core + twin Generate-Treatment/Generate-Outcome variants is rigorous.
- **AGAINST / Required edits:** Reframe from "we propose 3-process spec" to **"we benchmark using CIMEHR as engine"** (cite Yang+CIMEHR as load-bearing), add CIMEHR as mandatory generator baseline, inspect Sun supplement + Frontiers + CIMEHR vignettes (log result), state compute via CIMEHR pipeline, keep decision rule (non-inferior calibration/coverage AND superior DCA).
- **Flip if:** Sun supplement / CIMEHR vignette / Frontiers table already runs LMM/joint vs GRU-D/SeFT on calibration/coverage/DCA across γ_v/γ_o. **Edits fixable in days.**

### 004 — TRIPOD Subgroup-Calibration Corpus Audit n=150 — **REVISE → KEEP after edits** (scope must be sharpened vs fairness metrics)
- **Closest prior:** Maltreatment TRIPOD/PROBAST compliance review **PMID 41643238** (study-level compliance with calibration+fairness) + DCGS **2026.06.17.26355900** + KAISEN **10.48550/arXiv.2607.28608** (single-model fairness metrics, not prevalence audit) + Queiroz **10.1186/s12902-026-02301-2** (geographic quality, not subgroup calibration prevalence). All near-equivalents distinguished: compliance vs prevalence-with-Wilson+interval-aware-per-subgroup+masking+era-split.
- **FOR:** No meta-audit quantifies **prevalence of interval-aware subgroup calibration (overall vs ≥1 PROGRESS stratifier, slope CI/plot band per Riley) among TRIPOD-defined externally validated models 2015–2025 with Wilson CI and TRIPOD+AI era split**; whether overall masks subgroup failure unmeasured. Power n=150 → ±0.06 at p=0.2.
- **AGAINST / Required edits:** Must sharpen title to **"interval-aware prevalence + Wilson + masking rate + era split"** vs compliance study; add DCGS/KAISEN/PMID 41643238 to Important Papers + Evidence AGAINST with rebuttal; run corpus completeness sensitivity (TRIPOD filter vs `calibration AND external validation`), add RECORD/STROBE sensitivity.
- **Flip if:** paper reports TRIPOD external validations with interval-aware subgroup prevalence + Wilson + era split → pivot to Debray IPD pooling or Indian-corpus extension.

### 005 — Graded Indian Shift Plasmode G0→G3 — **KEEP** (shortlist-ready; strongest STRESSES-ASSUMPTION)
- **Closest prior:** Degtiar & Rose **10.1146/annurev-statistics-042522-103837** (formal), Kang scoping **10.1007/s10654-025-01217-w** (64 studies, **0 LMIC with diagnostics**) — gap evidence, Dahabreh **10.1093/aje/kwy253** estimator. **T6-KILL2 LMIC+overlap+SA returned 0 hits** — strongest adversarial confirmation.
- **FOR:** No graded plasmode injects **(a) Indian covariate shift anchored to ICMR-INDIAB MONO 43.3% (Mohan 10.25259/IJMR_328_2025, Tripura 56.7%) and (b) visit-process shift from WHO audits (Kaur injections 90.3% generic 64.9%; Khanna generic 4.7% NLEM 61% polypharmacy 71%)** with **diagnostics SMD/S-score AUC/ESS/trimming 0.05/0.10 across grades to adjudicate transport vs recalibration**. Duo variants + staged D+B (MIMIC immediate + UKB-SA 1–3 mo + CARRS/ICMR-INDIAB) de-risking.
- Clinical: thin-fat equity failure (BMI≥25 excludes 43%) + 91.5% diagnosis missingness vs algorithm failure distinction actionable.
- **Flip if:** MIMIC→SA-anchored plasmode with MONO-calibrated joint distribution + selective ordering at ≥2 grades with SMD/overlap appears.

### 006 — Audit→RR Anchored E-value + NC Ladder — **KEEP** (shortlist-ready, companion to 005)
- **Closest prior:** VanderWeele **10.7326/M16-2607** (E-value), Zhang **10.1136/bmjmed-2022-000366** (<15% anchored), J Clin Epi **10.1016/j.jclinepi.2023.09.014**, Lipsitch **10.1097/EDE.0b013e3181d61eeb** (NC), Hernán **10.7326/ANNALS-24-01871** (TTE). **Audit→E-value cross-vocabulary sweep zero co-occurrence** — disconnected corpora confirmed.
- **FOR:** No study translates **WHO-audit prevalences into bias parameters (RR_EU, RR_UD, B) and E-value-anchored threshold R* (≈1.4–2.0) + titration contour + NC ladder** with plasmode 9 cells (P(U) 0.10/0.44/0.96) for Indian target-trial emulation. E-value "could bias explain?" paired with NC "does bias manifest on falsification endpoint?" calibrates threshold's false-positive rate where US NCs do not transport.
- **Flip if:** paper computes E-values/bias factors with Indian WHO prevalences substituted. **Paired submission with 005 recommended (shared G0→G3 table, complementary estimands).**

### 007 — Ahlqvist 5-Cluster Transport (GADA-free stress) — **REVISE → KEEP after edits** (formal transport gap survives, descriptive literature saturated)
- **Closest prior:** Ahlqvist **10.1016/s2213-8587(18)30051-2** + Anjana **10.1136/bmjdrc-2020-001506** + IMI-RHAPSODY **10.1007/s00125-021-05490-8** (European 5-cluster cross-validation, 3 cohorts, k=5 routine vars) — **closest formal replication but European, no Indian transport+overlap+GADA-free ablation**, no centroids-vs-de-novo ARI. HTE transport (Wager 10.1080/01621459.2017.1319839 + Künzel) returned **0 hits** for subtype transport.
- **FOR:** No formal test **Ahlqvist centroids (transport labels) vs de novo unsupervised (k-means/GMM/hierarchical k=5) on Indian/CARRS/ICMR-INDIAB/UKB-SA with inverse-odds weighting overlap (Dahabreh) + SMD/ESS/truncation + outcome gradient replication (CKD/retinopathy/insulin) + 6→3 var ablation (GADA/HOMA-free)** exists. Indian replications are descriptive de novo, not transport.
- **AGAINST / Required edits:** Literature saturated (MDPI review, East Asian proportion shifts); must foreground **measurement-transport deployment lesson (6→3 ablation: <₹100 per patient vs selective referral)** not "ancestry shift." Add IMI-RHAPSODY distinction, IndMED + thesis sweep before RR, confirm CARRS GADA completeness with data dictionary, add CMC/AIIMS new-onset secondary target to address ANDIS-vs-CARRS sampling mismatch, pre-register thresholds (completeness ≥85%, AUC<0.70, ESS>70%, ARI≥0.60).
- **Flip if:** pre-registered Ahlqvist→CARRS/ICMR-INDIAB transport with overlap + outcome gradient + GADA-free sensitivity appears.

## Global synthesis table

| Dossier | Title | Class | Verdict | Shortlist? | Resurrection if KILL |
|---------|-------|-------|---------|------------|----------------------|
| **001** | Harutyunyan MIMIC→eICU TRIPOD+AI direct replication | A public | **KEEP** | **YES — shortlist-ready** | — |
| **002** | Fidelity→τ threshold via synthEHRella | A/D | **KEEP** | **YES — shortlist-ready** | — |
| **003** | 3-process joint plasmode DL-vs-classical | D sim | **REVISE** | **REVISE→KEEP after CIMEHR reframing + supplement inspection** | — |
| **004** | TRIPOD subgroup-calibration corpus n=150 | D lit | **REVISE** | **REVISE→KEEP after interval-aware + Wilson + masking + era-split sharpening** | — |
| **005** | Graded Indian shift G0→G3 | D+B staged | **KEEP** | **YES — shortlist-ready** | — |
| **006** | Audit→RR anchored E-value + NC | D+B staged | **KEEP** | **YES — shortlist-ready** | — |
| **007** | Ahlqvist 5-cluster transport | B restricted | **REVISE** | **REVISE→KEEP after IndMED/thesis + IMI-RHAPSODY + threshold locks** | — |

**Summary:** KEEP 4 / REVISE 3 / KILL 0. **No dossier is unfixable; no gap closed outright under 27 kill-try searches with alternative indexing.** Strongest threats: Patel 2026 task-level calibration (001), K-IPO/CoMedBench feature-importance τ (002), CIMEHR engine publication (003), DCGS/KAISEN/maltreatment compliance (004), IMI-RHAPSODY European replication (007) — all distinguished as near-equivalents.

### Priority order for Lead triage
1. **First-wave immediate (no DUA, code tomorrow):** 001 (Medium-High), 002 (Medium), 004-revised, 003-revised — all A/D. Total 4 dossiers, staggered starts share single GPU.
2. **Staged India-stressing (proxy first):** 005 + 006 — **paired submission** (same G0→G3 table, complementary estimands: transport-vs-recalibration + E-value robustness); D-only phase immediate while UKB-SA/CARRS DUA pends.
3. **Restricted empirical (B):** 007 — UKB-SA proxy overlap + 3-var ablation now; CARRS/ICMR-INDIAB DUAs honest 2–6 mo.

### Cross-dossier risks flagged
- Preprint watch (001 + 005/006): Patel medRxiv 10.64898/2026.05.03.26352335 under review — monitor weekly; YAIB/METRE releases may close Harutyunyan arm.
- Measurement missingness as finding: 003 (γ_v/γ_o) and 007 (GADA/HOMA) both stress informative missingness — harmonize S_visit vs S_lab definitions across T6/T4/T2.
- Calibration hierarchy reuse (001/002/003/004): consistent thresholds (slope 0.8–1.2, interval-aware) per Van Calster 10.1016/j.jclinepi.2015.12.005 + Riley 10.1136/bmj-2024-080749 → TRIPOD+AI 10.1136/bmj-2023-078378 mapping across dossiers.
- India proxy volunteer bias: UKB-SA healthier; overlap failure conservative — log limitation explicitly.

## Citation integrity (Lead audit — Cycle 5)
- **Search:** +73 data rows this cycle (305 data rows = 306 lines: 303 VERIFIED / 2 UNVERIFIED-timeout, same 2 from Cycle 1). Cycle 5: dossiers 48 + adversarial 25 (27 searches, 2 combined follow-ups) = 73; all VERIFIED. No new UNVERIFIED.
- **Evidence:** +39 data rows this cycle (209 data rows = 210 lines: 204 VERIFIED / 2 TRUE / 1 UNVERIFIED-T2-06 + 1 cycle-tag + 1 compliance-typed). +40 lines includes adversarial ADV-001..010 (Patel, CoMedBench, K-IPO, CIMEHR, maltreatment PMID 41643238, DCGS, IMI-RHAPSODY, CIMEHR software, postoperative stroke RF) all resolvable.
- **Spot-check 5 load-bearing new adversarial DOIs 302:** 10.64898/2026.05.03.26352335 (Patel calibration drift → medRxiv), 10.48550/arXiv.2602.15374 (CIMEHR/Yang → arxiv), 10.48550/arXiv.2608.12805 (CoMedBench → arxiv), 10.48550/arXiv.2607.16478 (K-IPO → arxiv), 10.1007/s00125-021-05490-8 (IMI-RHAPSODY → springer) — all 302; plus carry-forward 10.1038/s41597-019-0103-9, 10.1136/bmj-2023-078378, 10.1093/jamia/ocaf082, 10.34133/hds.0456 already 302.
- Every dossier: 8-gate headings explicit + Evidence AGAINST with termination conditions + India verdict justified; adversarial packet includes 13-criteria (≈15-item) checklist per candidate + what-would-flip + resurrection conditions. No fabrication; [UNVERIFIED] not used for load-bearing claims.
- Adversarial-reviewer remains advisory — Lead integrates; no `rejected/` moves this cycle (KILL 0), but REVISE edits are mandatory before shortlist freeze.

## Recommended Cycle 6 — Shortlist freeze + OSF pre-registrations
- **Lead (days):** Apply 3 REVISE edits (003 CIMEHR citation + Sun suppl. inspection; 004 interval-aware sharpening + DCGS/KAISEN + corpus sensitivity; 007 IMI-RHAPSODY distinction + IndMED/thesis sweep + threshold locks) — then all 7 dossiers shortlist-eligible. Generate `shortlist/SHORTLIST.md` with frozen scope ceilings + DUA timelines.
- **Assignments:** methods-scout: OSF pre-registration for 001 (TRIPOD+AI mapping + leakage checklist) + RR Stage-1 draft; clinical-evidence-scout: launch 004 corpus screening (Rayyan, n=150) + 002 synthEHRella pilot (5-point ladder, ~1500 fits); staged India plasmode (005+006) D-phase on MIMIC.
- **No new data collection for first wave** — all A/D public/simulation/literature; India proxy path (UKB-SA) parallelizes without blocking first wave. Convergence after 7-dossier freeze.

*No data fabrication — all designs supported by cited, resolvable literature with HEAD-verified DOIs or marked [UNVERIFIED] where flagged. Audit prevalences cited from open PMC fullTextXML with tables; plasmode magnitudes simulated.*
