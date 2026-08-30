# Cycle 3 — Shared Brief (India / Transportability Opportunities)
Companion: docs/01..03, working/CYCLE_01_BRIEF.md, working/CYCLE_02_BRIEF.md, reports/landscape_cycle_01.md, reports/failure_points_cycle_02.md, journal/cycles/cycle_02.md.
Cycle 3 asks: WHERE DOES THE INDIAN SETTING GENUINELY STRESS AN ASSUMPTION? Not "repeat on Indian patients" — which assumption (positivity, S-admissibility, exchangeability, consistency, time-zero, informative missingness) does it break, and can we make it executable with named data or plasmode?

## Binding constraints (same pool)
- Global pool muse-spark-1.2-contributor-free ~40/min, target ≤24, ceiling 30, max 2 concurrent.
- Every claim = resolvable DOI/PMID/URL or [UNVERIFIED]. Append verbatim to literature/search_log.csv + evidence_registry.csv.
- Adversarial-reviewer still DARK until ≥6 candidates (Stage: Cycle 3 generates candidate dossiers for adversarial activation next cycle).
- Write packets to working/agent_notes/<agent>/cycle03_*.md — checkpoint early.

## Packets required this cycle (4 packets — 2 per scout)

### Clinical-evidence-scout → 2 packets
1. **cycle03_T6_indian_shift_implementation.md** — Graded Indian shift plasmode: how to implement Indian-typical covariate/visit-process shift concretely.
   - Q: What concrete numbers define Indian-typical shift for transportability plasmode (BMI/diabetes prevalence at lower thresholds, CVD age distribution, measurement frequency, selective lab ordering, formulary restriction, cost-driven switching)?
   - Tasks: 2+ strategies (Indian epidemiology + visit-process shift terminology) + systematic reviews (ICMR-INDIAB structure, CARRS phenotyping, UKB South Asian calibration) + adjacent (domain shift implementation) + adversarial (existing Indian shift plasmode already) + chaining (ICMR-INDIAB → CARRS → UKB South Asian → Degtiar & Rose → Dahabreh → Inoue/Kang). Must include: 5-10 papers (mix Indian epidemiology + transportability methods), 1 DOI 302-verified, what shift magnitudes appear established vs uncertain, closest defeater, named datasets (MIMIC-IV source, UKB-SA/CARRS/ICMR-INDIAB proxy targets, plasmode spec with shift injection table), India verdict STRESSES-ASSUMPTION justified, Confidence, Next search.
2. **cycle03_T4_audit_numbers_extraction.md** — Audit→RR translation: extract concrete prevalences/RRs from 5 Indian prescribing audits to parameterize E-value anchor.
   - Q: Can audit-derived proportions (irrational FDC %, generic/EDL compliance, cost-switching, AYUSH co-use prevalence, polypharmacy) be translated into VanderWeele bias parameters (confounder-treatment RR, confounder-outcome RR, prevalence) for an E-value anchored decision threshold?
   - Tasks: 2+ strategies (WHO indicator audit extraction + quantitative bias translation terminology) + reviews (WHO prescribing audits 2022-2024, India pharmacoepi, E-value empirical audits) + adjacent (bias analysis parameterization) + adversarial (existing audit→E-value bridge already) + chaining (VanderWeele 2017 → Zhang 2023 → J Clin Epidemiol E-value review → Lipsitch 2010 → Hernán 2024 + Indian audit chain). MUST web_extract ≥2 Indian audit papers to extract concrete numbers (prevalence tables). Must include: 5-10 papers (US causal + Indian audits/surveys), 1 verified, defeater, datasets (WHO audits open + MIMIC/plasmode + CARRS/UKB-SA), methodological implication (translation formula + sensitivity), clinical implication, India verdict, Confidence, Next search.

### Methods-scout → 2 packets
3. **cycle03_T8_named_model_sweep.md** — Named-model sweep for direct replication (T8 feasibility).
   - Q: For 3-5 top-cited influential clinical-ML models, has a pre-registered direct replication on independent public EHR (MIMIC→eICU) with TRIPOD+AI already been published — and if not, which model is the cleanest first-project target?
   - Tasks: 2+ strategies (influential model name + replication terminology) + systematic reviews (McDermott, Nagendran) + adjacent (many-analysts) + adversarial (try to find existing replication for each named model) + chaining per model (Harutyunyan 2019 MIMIC mortality benchmark → Rajkomar 2018 scalable DL EHR → PhysioNet 2019 sepsis winners (Moor et al etc) → subsequent citations). For each of 3-5 models: run `replication reproducibility external validation MIMIC-IV eICU <model name>` as separate queries, log verbatim. Must include: 5-10 papers (models themselves + any replications + TRIPOD+AI + McDermott/Beam), 1 verified, established vs uncertain (which models appear un-replicated), closest defeater (existing replication corpus), named datasets (MIMIC-III/IV, eICU, AmsterdamUMCdb), India transport extension note (GEOGRAPHY-ONLY for v1), Confidence, Next search. MUST verify ≥1 model DOI 302.
4. **cycle03_T2_HTE_transport.md** — Transportability of heterogeneity: Ahlqvist 5 clusters → Indian/CARRS.
   - Q: Do Ahlqvist 2018 diabetes 5-cluster subtypes transport to Indian/CARRS cohorts, or do they fail positivity/overlap under Indian covariate support — is "re-discover clusters de novo vs transport labels" the falsifiable test?
   - Tasks: 2+ strategies (Ahlqvist cluster transport terminology + HTE heterogeneity transport) + reviews (Ahlqvist 2018, diabetes subtyping reviews, Wager & Athey causal forests) + adjacent (multimorbidity clustering) + adversarial (existing Ahlqvist Indian replication already) + chaining (Ahlqvist 10.1016/S2213-8587(18)30051-2 → Scandinavian replications → East Asian replications → CoINcIDE → Indian diabetes cohorts). Must include: 5-10 papers (Ahlqvist + ≥1 Scandinavian replication + ≥1 Indian diabetes cohort descriptive + ≥1 clustering/HTE methods + ≥1 transportability), 1 verified, closest defeater, named datasets (ICMR-INDIAB, CARRS, CMC/AIIMS registries, UKB-SA as proxy, MIMIC optional), India verdict STRESSES-ASSUMPTION (exchangeability of clustering features), Confidence, Next search.

## Output contract (all packets)
13-section template (Question → Confidence + Recommended next search) with explicit Evidence AGAINST and India verdict justification. Every packet ≥5 resolvable papers, ≥1 load-bearing DOI HEAD-verified (curl -I 302). Checkpoint early.

## Non-goals
Candidate promotion happens in Cycle 3 synthesis by Lead after Lead-anchored II next-searches (executable queries in appendices) are checked at full-text level. Scouts deliver deepening; Lead promotes.

## Completion checklist per packet
- [ ] ≥5 resolvable papers, ≥1 verified 302
- [ ] search_log verbatim + evidence_registry rows
- [ ] packet at working/agent_notes/<agent>/cycle03_*.md with all sections, self-adversarial
- [ ] T4 packet MUST have ≥2 audit web_extracts with number tables; T8 packet MUST have per-model query log
