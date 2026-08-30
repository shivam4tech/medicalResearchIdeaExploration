# Cycle 2 — Shared Brief (Methodological Failure Points)
Companion: docs/01..03, working/CYCLE_01_BRIEF.md, reports/landscape_cycle_01.md, journal/cycles/cycle_01.md.
Cycle 2 asks: WHERE DO EXISTING METHODS DEMONSTRABLY BREAK? Not "can we apply ML," but "where do published/standard methods fail, disagree, miscalibrate, or hide behind aggregates?"

## Binding constraints (same as Cycle 1)
- Global pool muse-spark-1.2-contributor-free ~40/min, target ≤24, ceiling 30, max 2 model-intensive concurrent.
- Every claim = resolvable DOI/PMID/URL or [UNVERIFIED]. Log verbatim to literature/search_log.csv + evidence_registry.csv (append-only).
- Adversarial-reviewer still DARK (no ≥6 candidates). Use self-authored adversarial sections.
- Write packets to working/agent_notes/<agent>/cycle02_*.md — checkpoint early.

## Packets required this cycle
### Clinical-evidence-scout → 2 packets
1. **cycle02_T6_positivity_diagnostics.md** — Positivity / overlap / selection diagnostics for transportability to Indian targets.
   - Q: How do published transportability methods diagnose positivity/S-admissibility? What diagnostics (standardized mean differences, weight trimming, overlap weights, propensity overlap plots) are reported, and are they calibrated on LMIC-shifted covariate distributions?
   - Tasks: 2+ strategies (transportability diagnostics terminology vs weighting/positivity literature) + systematic reviews + adjacent (domain shift diagnostics) + adversarial (search for Indian overlap diagnostics already published) + backward/forward chaining (Dahabreh 2020 → Degtiar & Rose 2023 → Kang 2025 + weighting diagnostics papers). Must include: 5-10 papers with resolvable IDs, what positivity diagnostics appear established vs uncertain, closest work defeating the gap, at least one Indian proxy dataset discussion (UK Biobank South Asian, CARRS, ICMR-INDIAB structure), methodological implication (when does weighting break?), clinical implication (risk-score transport), India verdict (STRESSES-ASSUMPTION justified if diagnostics shift), Confidence, Next search.
2. **cycle02_T4_prescribing_audit.md** — Anchoring unmeasured confounding sensitivity to Indian prescribing audits.
   - Q: What local prescribing evidence (cost-driven switching, informal polypill/Ayurvedic co-use, formulary restriction) exists to anchor an E-value / quantitative bias analysis for Indian EHR emulation? How do negative controls / falsification endpoints perform in routine care?
   - Tasks: 2+ strategies (prescribing pattern India + RWE sensitivity terminology) + audits/inspections (Indian prescribing surveys, pharmacoepi) + adjacent (negative control outcomes) + adversarial (search for Indian emulation already with negative controls) + chaining (VanderWeele Ding 2017 → Hernan 2024/2025 → Zhang BMJ Medicine 2023 + Indian pharmacoepi). Must include: 5-10 papers (mix US causal + Indian prescribing/policy), established vs uncertain, closest defeater, named datasets (same public MIMIC/plasmode + Indian audits), methodological + clinical implications, India verdict, Confidence, Next search.

### Methods-scout → 3 packets
3. **cycle02_T1_plasmode_design.md** — Full plasmode/simulation design for DL-irregularity vs classical benchmark.
   - Q: What is a publishable, falsifiable plasmode design that varies visit informativeness, sparsity, noise with KNOWN ground truth, and specifies mandatory baselines?
   - Tasks: 2+ strategies (plasmode simulation design + irregular time series benchmarking) + reviews (Schneider PMC12070788, Sun 2026) + synonyms (informative visit/observation decomposition) + adversarial (search for existing plasmode already comparing DL vs LMM on calibration/coverage) + chaining (JMVL-Liang 2410.13113 → Schneider → Naemi → Franklin/Schuler plasmode). Must deliver: 5-10 papers, simulation parameter inventory (N, visits/patient, SNR, informativeness strength), generative model spec (3-process joint: visit+observation+longitudinal with shared frailty + outcome model), mandatory baselines (LMM random intercept/slope, joint longitudinal-survival JMbayes2, LOCF+logistic, MICE+pooled, GRU-D, SeFT) + metrics (AUC, calibration slope/intercept, Brier, prediction-interval coverage, decision-curve), software (R/JMbayes2, Python torchdiffeq/GRU-D), data need (simulation primary, MIMIC replication secondary), India transport extension note, adversarial, India verdict (GEOGRAPHY-ONLY for v1), Confidence, Next search.
4. **cycle02_T5_corpus_pilot.md** — Pilot audit design + tiny corpus execution for aggregate-masking.
   - Q: What is an auditable corpus definition (TRIPOD 2015-2025 external validations) and what is the PILOT reporting rate of subgroup calibration on 5 sampled papers — does aggregate masking appear prevalent enough to justify a full audit?
   - Tasks: 2+ strategies (TRIPOD external validation + calibration subgroup terminology) + reviews (Riley BMJ 2025, Van Calster 2016, TRIPOD+AI 2024) + adjacent (fairness/subgroup) + adversarial (search for existing meta-audit of subgroup calibration) + chaining (Riley → Van Calster → Collins TRIPOD audit literature). Must include: 5-10 papers (Riley, Van Calster, TRIPOD, at least 2 recent external validations, 1 fairness audit, 1 conformal-medicine paper), corpus definition (PubMed TRIPOD[Title/Abstract] AND validation, 2015-2025 inclusive, filters), sampling/pilot method on 5 papers (extraction of overall vs subgroup calibration reporting), pilot result (reported rate), power consideration for full audit, closest defeater, datasets (TRIPOD corpus itself + MIMIC/CRASH for deep dive), adversarial, India verdict, Confidence, Next search. MUST do web_extract on at least 2 external validation papers to demonstrate reporting inspection.
5. **cycle02_T7_threshold_pilot.md** — SynthEHRella instrument pilot: rank preservation threshold.
   - Q: What fidelity/utility threshold (MMD, RMSPE, TSTR AUC gap) predicts preservation of method ranking, and what is a minimal pilot design using synthEHRella on MIMIC-III→MIMIC-IV?
   - Tasks: 2+ strategies (synthetic rank correlation + fidelity threshold terminology) + reviews (Chen JAMIA 2025, synthEHRella docs) + synonyms (TSTR, fidelity, plasmode Generate-Treatment vs Outcome) + adversarial (search for existing real-vs-synthetic rank correlation study) + chaining (Chen 2025 → Liu 2504.11740 → Yan 2022 → synthEHRella GitHub). Must include: 5-10 papers, design: 1-2 method comparisons (e.g., logistic vs GRU-D or calibration methods) evaluated on real MIMIC-III held-out vs synthEHRella-generated synthetic + plasmode, metric: Kendall τ / Spearman, pilot expectation (do rankings shift MIMIC-III→IV already per Chen), closest defeater, datasets (MIMIC-III/IV, Synthea, synthEHRella), software, India extension note, adversarial, India verdict (GEOGRAPHY-ONLY), Confidence, Next search. Must inspect synthEHRella GitHub README via web_extract.

## Output contract (all packets)
Use same 13-section template as Cycle 1 (Question … Confidence … Recommended next search) plus Recommended next search should be executable PubMed/arXiv queries. Every packet must have explicit Evidence AGAINST and India verdict justification.

## Completion checklist per packet
- [ ] ≥5 resolvable papers, ≥1 load-bearing DOI HEAD-verified (curl -I https://doi.org/DOI → 302)
- [ ] search_log rows verbatim, evidence_registry rows with verification_status
- [ ] packet at working/agent_notes/<agent>/cycle02_*.md with all sections, self-authored adversarial

## Non-goals
No candidate promotion in Cycle 2 — deepening only. Candidate matrix stays empty until Cycle 2 synthesis ranks refined seeds for Cycle 3.
