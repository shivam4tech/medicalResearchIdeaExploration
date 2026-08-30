# Cycle 4 — Shared Brief (Data-Independent First Projects)
Companion: docs/01..03, working/CYCLE_01..03_BRIEF.md, reports/landscape_cycle_01.md, reports/failure_points_cycle_02.md, reports/india_opportunities_cycle_03.md, journal/cycles/cycle_03.md.
Cycle 4 asks: LOCK FIRST-PROJECT PROTOCOLS that need no restricted data — so T8/T7/T1/T5 can start tomorrow on public/synthetic/literature data. India flagships (T6/T4/T2) staged on UKB-SA proxy while CARRS/ICMR-INDIAB DUA pends.

## Binding constraints (same pool)
- Global pool muse-spark-1.2-contributor-free ~40/min, target ≤24, ceiling 30, max 2 concurrent.
- Every claim = resolvable DOI/PMID/URL or [UNVERIFIED]. Append verbatim to literature/search_log.csv + evidence_registry.csv.
- Adversarial-reviewer stays DARK until candidate promotion (Cycle 5/6 kill round). Packets include self-adversarial per 03 evidence standards.
- Write packets to working/agent_notes/<agent>/cycle04_*.md — checkpoint early.

## Packets required this cycle (4 packets — 2 per scout)

### Methods-scout → 2 packets
1. **cycle04_T8_replication_lock.md** — Locked pre-registration protocol for Harutyunyan 2019 multitask LSTM direct replication (MIMIC→eICU TRIPOD+AI).
   - Q: What exact pre-registration (OSF/Registered Report) makes Harutyunyan→eICU replication falsifiable with calibration/subgroup/DCA and leakage controls, with compute/access timeline?
   - Tasks: 2+ strategies (Harutyunyan replication terminology + leakage/calibration terminology distinct) + systematic reviews (McDermott/Nagendran/TRIPOD+AI lineage + recent 2024–2026 replications) + adjacent (many-analysts/feature-drift) + adversarial (find existing exact replication) + chaining (Harutyunyan → METRE/ricu/YAIB harmonization → Nestor drift → Van Calster/Riley calibration). Must include: 5-10 papers (Harutyunyan + TRIPOD+AI + calibration + harmonization), 1 DOI 302-verified, closest defeater, named datasets (MIMIC-III/IV, eICU, AmsterdamUMCdb/HiRID), executable protocol (OSF template items, harmonization mapping table stub, leakage checklist, power/equivalence bounds, TRIPOD+AI item mapping, mandatory baselines LR+SOFA+GBM), India GEOGRAPHY-ONLY, Confidence, Next search.
2. **cycle04_T1_plasmode_lock.md** — Locked plasmode implementation (3-process joint) with code pointers and compute budget.
   - Q: What locked 16-cell core + twin plasmode variants + mandatory baselines implementation lets T1 start coding tomorrow?
   - Tasks: 2+ strategies (plasmode/joint-model + irregular-series DL terminology) + reviews (Sun, Schneider, Rizopoulos/JMbayes2) + adjacent (neural ODE/GRU-D) + adversarial (find existing joint-plasmode DL-vs-classical with calibration/coverage/DCA) + chaining (Franklin→Schuler→Liang→Sun→Schneider). Must include: 5-10 papers, 1 verified, defeater, datasets (simulation only), generative spec restated with code package pointers (JMbayes2/joineRML, lme4, torch for GRU-D/SeFT/GRU-ODE), compute estimate (fits ≈16×200×baselines), decision rule restated, Confidence, Next search.

### Clinical-evidence-scout → 2 packets (methods-leaning but feasible for clinical profile; T7/T5 are literature/synthetic)
3. **cycle04_T7_threshold_lock.md** — Locked threshold pilot via synthEHRella with clinical decision-curve framing.
   - Q: What locked fidelity ladder (S1/S1′/S2/S3/S4/S5) and rank-preservation analysis (Kendall τ, Spearman, pairwise concordance) makes T7 executable on MIMIC-III→IV with DCA clinical thresholds?
   - Tasks: 2+ strategies (synthetic EHR fidelity + rank-preservation/decision-curve terminology) + reviews (Chen JAMIA, Yan, Angelopoulos conformal) + adjacent (plasmode fragility Liu) + adversarial (find existing fidelity→τ methods-ranking study) + chaining (Chen→synthEHRella README→Liu fragility→Van Calster calibration). Must include: 5-10 papers, 1 verified, web_extract synthEHRella README if needed, defeater, datasets (MIMIC-III/IV public), clinical implication (when synthetic is cautionary), Confidence, Next search.
4. **cycle04_T5_corpus_lock.md** — Locked corpus audit protocol (TRIPOD subgroup-calibration, n=150).
   - Q: What locked corpus filter, extraction form, and inter-rater/power plan makes T5 start screening tomorrow?
   - Tasks: 2+ strategies (TRIPOD/subgroup-calibration + uncertainty/fairness terminology) + reviews (Riley, Van Calster, TRIPOD+AI, Christodoulou) + adjacent (conformal/fairness calibration) + adversarial (find existing subgroup-calibration meta-audit) + chaining (TRIPOD 2015→TRIPOD+AI 2024→Riley interval→Van Calster hierarchy). Must include: 5-10 papers, 1 verified, MUST web_extract ≥1 TRIPOD corpus paper with extraction pilot table (as in Cycle 2 but updated), defeater, datasets (literature corpus only), Confidence, Next search. MUST web_extract ≥1 corpus paper to show extraction form feasibility.

## Output contract (all packets)
13-section template (Question → Confidence + Recommended next search) with explicit Evidence AGAINST and India verdict justification. Every packet ≥5 resolvable papers, ≥1 load-bearing DOI HEAD-verified (curl -I 302). Checkpoint early.

## Non-goals
Candidate promotion happens in Cycle 5 after Lead next-searches (executable queries in appendices) at full-text level. Scouts deliver locked protocols; Lead promotes.

## Completion checklist per packet
- [ ] ≥5 resolvable papers, ≥1 verified 302
- [ ] search_log verbatim + evidence_registry rows
- [ ] packet at working/agent_notes/<agent>/cycle04_*.md with all sections, self-adversarial
- [ ] T8 packet MUST have OSF/RR template + leakage checklist; T1 MUST have compute estimate; T7 MUST have fidelity ladder; T5 MUST have ≥1 corpus web_extract
