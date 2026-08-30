# Cycle 4 — Data-Independent First Projects (lock protocols that start tomorrow)
**Date:** 2026-08-30 · **Agents:** Research Lead + clinical-evidence-scout + methods-scout (adversarial-reviewer DARK until promotion) · **Rate-limit incidents:** none (60 calls in ~12m, ~5.0/min, ceiling 30)

## Objective
Lock executable protocols for the 4 data-independent flagships so coding/screening can start without waiting on restricted data: T8 Harutyunyan replication (public MIMIC→eICU), T1 plasmode DL-vs-classical (simulation), T7 rank-preservation threshold (synthetic), T5 corpus audit (literature). India flagships (T6/T4/T2) staged on UKB-SA proxy while CARRS/ICMR-INDIAB DUA pends.

## Questions for this cycle
1. What exact OSF/RR pre-registration (leakage controls, TRIPOD+AI mapping, equivalence bounds) makes T8 unambiguously falsifiable?
2. What locked 16-cell + twin plasmode variants + baselines/coverage/DCA lets T1 be coded tomorrow with known compute?
3. What locked fidelity ladder + τ/DCA analysis makes T7 executable on MIMIC-III→IV?
4. What locked corpus filter + extraction form + inter-rater/power makes T5 start screening tomorrow?

## Assignments
- **methods-scout:** cycle04_T8_replication_lock (OSF template, leakage checklist, TRIPOD+AI mapping, harmonization), cycle04_T1_plasmode_lock (generative spec, code pointers, compute)
- **clinical-evidence-scout:** cycle04_T7_threshold_lock (fidelity ladder, rank-preservation, DCA), cycle04_T5_corpus_lock (corpus filter, extraction form, ≥1 web_extract)
- Brief: `working/CYCLE_04_BRIEF.md` (4 packets, 13-section, self-adversarial, India verdict).

## Rate discipline
Global pool muse-spark-1.2-contributor-free (opencode-zen) ~5.0/min observed (59 calls / 12.3m), target ≤24, ceiling 30, max 2 concurrent. No 429s. Active chat now `muse-spark-1.2-contributor-free` via `opencode-free` shares pool — respected via 2-concurrent cap.

## Findings
**4/4 packets COMPLETE. All locks runnable this week without restricted data.**

- **T8 Replication Lock** (`working/agent_notes/methods-scout/cycle04_T8_replication_lock.md`, 50K chars, 10 papers, Medium-High): Pre-registered Harutyunyan 2019 multitask LSTM (2×128, dropout 0.3, Adam 1e-3) MIMIC→eICU TRIPOD+AI direct replication. Delivers: OSF/RR template items, harmonization stub (17 time-series +5 static via ricu/YAIB/METRE), leakage checklist (time-zero ICU admission, no lookahead, forward-fill+mask frozen, feature-freeze audit), equivalence bounds (AUROC Δ0.05, slope 0.8–1.2, |α|≤0.2 logit, subgroup heterogeneity 0.10), TRIPOD+AI 27-item mapping, mandatory baselines LR+SOFA+GBM+trivial. Per-model adversarial sweep → zero TRIPOD+AI replication for any flagship; 2026 domain-shift corpus is task-level, not frozen-arch. GEOGRAPHY-ONLY v1; Stage-2 Indian ICU staged.

- **T1 Plasmode Lock** (`working/agent_notes/methods-scout/cycle04_T1_plasmode_lock.md`, 47K chars, 10 papers, Medium): Locked 3-process joint (λ_V, logit P(O), Y=Xβ+Zb+ε, outcome θ1 f(Y*)) with shared frailty b_i inducing informativeness. Delivers: twin plasmode variants (Generate-Treatment vs Outcome — Liu fragility test), 16-cell fractional core ×200 MC (≈22.4k fits, 200–300 GPU-h checkpointed), code pointers (JMbayes2/joineRML, lme4, torch GRU-D/SeFT/ODE, mice), metrics (AUC + calibration slope/intercept + Brier + coverage + DCA 10/20/30%), decision rule (DL wins only if non-inferior calibration/coverage AND superior DCA). GEOGRAPHY-ONLY v1.

- **T7 Threshold Lock** (`working/agent_notes/clinical-evidence-scout/cycle04_T7_threshold_lock.md`, 47K chars, 8 papers, Medium): synthEHRella fidelity ladder S1 plasmode-G-Treatment / S1′ G-Outcome / S2 GAN / S3 Synthea / S4 Resample-perfect / S5 Random (5–8 points) + rank preservation (Kendall τ primary, Spearman, pairwise concordance) on logistic/Cox vs GRU-D synthetic-TRAIN vs real-TRAIN evaluated on MIMIC-III held-out + MIMIC-IV transport, with DCA 10/20% utility preservation. Decision rule τ≥0.7 LB≥0.5 on both tests; otherwise cautionary negative. GEOGRAPHY-ONLY.

- **T5 Corpus Lock** (`working/agent_notes/clinical-evidence-scout/cycle04_T5_corpus_lock.md`, 56K chars, 8 papers, Medium): TRIPOD corpus audit n=150 power (±0.06 at p=0.2; Wilson CI). Delivers: corpus filter `(TRIPOD AND validation AND 2015-2025 AND Humans+English)` random n=150, extraction form overall-vs-subgroup matrix interval-aware (overall calibration vs subgroup slope/intercept/plot per age/sex/race/comorbidity/site + interval + DCA), inter-rater dual 20% κ≥0.7, pilot GO (Hughes 0/1 subgroup calibration, Diagn Progn Res study-level not model-level), MUST web_extract Queiroz PMC13169604 61k chars 2 tables (97 models, 91.8% PROBAST high risk) proving form feasibility. GEOGRAPHY-ONLY main; India-enriched Stage-2.

All 4 survive adversarial search; each includes Evidence AGAINST with termination conditions.

## Decisions
Portfolio narrows 8 designs → 4 first projects runnable without DUA. Promotion requires Lead-anchored PubMed/arXiv next-searches per packet appendix (4–5 queries each, LMIC+methods conjunction at full-text) returning empty → `ideas/candidate_NNN.md` dossiers + adversarial-reviewer kill round at ≥6 candidates (next cycle). India flagships (T6/T4 graded G0→G3 shared plasmode, T2 Ahlqvist transport) staged on UKB-SA proxy (≈1–3 mo) and share infrastructure with T1/T8 — not dropped, parallel track.

## Candidates created/weakened/killed
0 created this cycle (gate requires Lead next-searches + adversarial). 4 promotion-ready locks staged for dossiers: T8, T7, T1, T5 (first wave) → T6+T4 combined + T2 (India wave) in Cycle 5. 0 weakened/killed this cycle (adversarial DARK by protocol).

## Rate-limit incidents
None. 59 model calls in 12.3m (~5.0/min), no 429s, 2 concurrent respected.

## Ledgers updated
- `literature/search_log.csv`: 172 → **232** (+60 this cycle: T8 15 + T1 13 + T7 13 + T5 19, all 60 VERIFIED, 0 new UNVERIFIED; global 230 VERIFIED / 2 UNVERIFIED-timeout same as Cycle 1)
- `literature/evidence_registry.csv`: 133 → **170** (+37 this cycle: +36 VERIFIED/+1 TRUE-type; global 166 VERIFIED / 2 TRUE / 1 UNVERIFIED-T2-06 + 1 cycle-tag typo; no new UNVERIFIED)
- `reports/locked_protocols_cycle_04.md` (synthesis, 19.9K chars)

## State
- Candidates: 0 · Rejections: 0 · Search log rows: 172 → 232 · Evidence rows: 133 → 170
- First-project locks: 4/4 runnable (OSF/RR, plasmode code, synthEHRella ladder, Rayyan corpus) — public/simulation/literature only, no PHI.

## Next cycle
Cycle 5 — Promote + kill round: Lead next-searches → 5–7 `ideas/candidate_NNN.md` dossiers → adversarial-reviewer activation (≥6) → convergence. Methods-scout pre-registers T8 on OSF + RR stage-1; clinical-evidence-scout launches T7 pilot + T5 screening. India proxy path (UKB-SA) parallelized.

