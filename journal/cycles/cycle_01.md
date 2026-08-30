# Cycle 1 — Landscape: map strongest methodological territories
**Date:** 2026-08-30 · **Agents:** Research Lead + clinical-evidence-scout + methods-scout (adversarial-reviewer DARK) · **Rate-limit incidents:** none

## Objective
Breadth-first map of T1–T8: which territories have genuine methodological gaps that are clinically meaningful, feasibility-bounded, and transportability-aware. Produce verifiable landscape packets — not candidates yet.

## Questions for this cycle
1. Which territories have ≥1 demonstrable failure point (existing methods break/disagree/overfit/fail to transport)?
2. Where do Indian clinical realities plausibly stress an assumption of Western-derived methods?
3. Which gaps are already saturated by recent systematic reviews vs genuinely open?

## Assignments
- **clinical-evidence-scout** (max 2 concurrent budget): T6 Transportability & external validity, T2 Heterogeneity & hidden subgroups, T4 Causal inference from observational data — 3 packets
- **methods-scout**: T1 Longitudinal & irregular time series, T5 Uncertainty & aggregate-statistic failure, T7 Simulation & synthetic data, T8 Reproducibility & robustness — 4 packets
- Each territory → packet in `working/agent_notes/<agent>/territory_*.md` + rows in `search_log.csv` + `evidence_registry.csv` (brief: `working/CYCLE_01_BRIEF.md`)

## Rate discipline
Global pool muse-spark-1.2-contributor-free (opencode-zen) ~40 req/min. Target ≤24/min, ceiling 30, max 2 model-intensive concurrent. Verification ~1 per 3-4 searches. Actual: 27 + 27 = 54 model calls across ~9 min (~6/min average, well under ceiling, no 429s).

## Findings
**7/7 territories completed, all Medium confidence.** No candidate promoted — landscape only.

- **T6 Transportability:** Formal theory mature (Degtiar & Rose 2023 An Rev 10.1146/annurev-statistics-042522-103837, Pearl/Bareinboim), applied RWE scarce (Levy 2024 PMC11542082 N=6 all US/Canada). Risk-score miscalibration replicated (Sri Lanka Framingham 10.1186/s12889-023-17601-8, Ramspek BMC Med Res Methodol) but formal transportability (inverse-odds weighting, Dahabreh AJE kwy253) vs simple recalibration under informative missingness uncompared for Indian EHR. Gap survives marginally; adversary = one Indian transportability application or proof recalibration suffices. **India STRESSES-ASSUMPTION** (positivity, measurement frequency, practice patterns).
- **T2 Heterogeneity:** Causal forests (Wager & Athey JASA 10.1080/01621459.2017.1319839) + metalearners (Künzel PNAS) rigorous but EHR validation thin; subtyping replication fails (CoINcIDE, Parkinson 2024, JAMA Network Open 2024 28 trials). Celebrated Ahlqvist 5 diabetes clusters (Lancet Diab 10.1016/S2213-8587(18)30051-2) replicates in Nordics but contested elsewhere. Gap = pre-registered null-result HTE study (falsifiable “no replicable heterogeneity at N”) on MIMIC→eICU vs risk-model baseline. **India STRESSES-ASSUMPTION only if framing transportability of Ahlqvist.**
- **T4 Causal:** Target-trial emulation standardized (Hernán Ann Int Med 10.7326/ANNALS-24-01871, JAMA 10.1001/jamanetworkopen.2025.58262), PS/IPTW dominates (Rosenbaum Biometrika, Chesnaye PMC8757413, 2025 SR), E-value (VanderWeele 10.7326/M16-2607) widely cited but under-applied (BMJ Medicine 2023). Adversarial EHR→RCT replications exist but US-centric. Gap = emulation with falsification + E-value anchored to Indian prescribing/MNAR structure. **India STRESSES-ASSUMPTION** (exchangeability, positivity, time-zero, consistency).
- **T1 Longitudinal:** Architecture-saturated (Sun 2026 10.34133/hds.0456 review, GRU-D 10.1038/s41598-018-24271-9, SeFT), benchmark-poor. Joint models are mature baseline (Li IJERPH 2024 SR, Schneider PMC12070788 simulation guidelines, JMVL-Liang arXiv 2410.13113 three-process). Naemi MIMIC-IV benchmark (arXiv 2401.15290) exists but not vs LMM/joint; calibration/coverage head-to-head under tunable informativeness missing. Gap = plasmode benchmark DL irregular vs LMM/joint. **GEOGRAPHY-ONLY.**
- **T5 Uncertainty:** Point risks without uncertainty still norm (Riley BMJ 2025 10.1136/bmj-2024-080749 — CRASH intervals 0.477-0.693, calibration uncertainty can span 0.25-0.45). Calibration hierarchy (Van Calster J Clin Epi 10.1016/j.jclinepi.2015.12.005) + TRIPOD+AI (10.1136/bmj-2023-078378) now require uncertainty but practice lags; conformal (Angelopoulos 10.1561/2200000101) mature but not routine. Gap = audit of aggregate-masking (overall passes, subgroup fails) + Riley vs conformal decision impact. **GEOGRAPHY-ONLY** (India extension Stage-2).
- **T7 Simulation:** Chen JAMIA 2025 10.1093/jamia/ocaf082 is load-bearing scoping+benchmark (48 studies, 7 methods on MIMIC-III/IV, synthEHRella toolkit); Liu arXiv2504.11740 shows plasmode fragile (Generate-Treatment vs Outcome). Gap = instrument-validity meta-benchmark (does synthetic preserve method ranking? Kendall τ, fidelity threshold?). **GEOGRAPHY-ONLY.** Highest feasibility — open data.
- **T8 Reproducibility:** McDermott Sci Transl Med 10.1126/scitranslmed.abb1655 (511 papers, ML-for-health worst), Nagendran BMJ m689 (81 DL-vs-clinician), Ioannidis PLoS Med 10.1371/journal.pmed.0020124, Beam JAMA 10.1001/jama.2020.2166. Corpus-level crisis documented; Nestor MLHC 2019 feature drift shown. Gap = pre-registered direct replication of named influential model on independent public EHR (MIMIC→eICU) with TRIPOD+AI + feature-robustness. **GEOGRAPHY-ONLY.** Lowest-risk first paper.

All packets include: 5-10 seed papers with resolvable DOI/PMID/URL, What’s established vs uncertain, Potential gap (falsifiable), explicit Evidence AGAINST (closest defeaters), named datasets with access routes, methodological + clinical implications, India verdict (STRESSES-ASSUMPTION / GEOGRAPHY-ONLY / NONE-CLAIMED), Confidence, Recommended next search.

## Decisions
- No candidate promoted in Cycle 1 — landscape synthesis only (per protocol: candidates require adversarial challenge + named data pathway + falsifiable negative-result framing). 8 candidate seeds identified for Cycle 2 deepening, ranked by feasibility × novelty × clinical value: T8-direct-replication (1), T7-instrument-validity (2), T1-irregularity benchmark (3), T5-aggregate-masking audit (4), T6-transportability-vs-recalibration (5), T4-emulation-falsification (6), T2-falsifiable-heterogeneity (7), T6/T2-India-transport extension Stage-2 (8). See `reports/landscape_cycle_01.md` for full ranking and next searches.
- Cycle 2 focus approved: **Methodological failure points** — deep dives on T1 (does complexity pay?), T5 (aggregate masking audit pilot), T7 (instrument threshold pilot), plus T6/T4 assumption-stress inventory (positivity diagnostics, prescribing-audit anchoring).

## Candidates created/weakened/killed this cycle
- Created: 0 (seeds listed above for Cycle 2)
- Weakened: 0
- Killed: 0

## Rate-limit incidents
None. Actual throughput ~6 req/min (27+27 calls over ~9 min, well under 24/min target). No 429s. 2 search_log rows flagged UNVERIFIED (403 timeout) correctly marked; 1 evidence row (T2-06 JAMA Network Open) correctly UNVERIFIED (URL-only, DOI pending).

## Ledgers updated
- `literature/search_log.csv` — 54 data rows (header + 54 = 55 lines): T6 5, T2 5, T4 6, T1 8, T5 9, T7 5, T8 4 + verification extracts (5) + doi_checks (4); all queries verbatim, 52 VERIFIED / 2 UNVERIFIED
- `literature/evidence_registry.csv` — 49 data rows (header + 49 = 50 lines): T6 8, T2 8, T4 8, T1 7, T5 8, T7 7, T8 7 → 48 VERIFIED / 1 UNVERIFIED (T2-06, correctly flagged, not load-bearing); all resolvable = TRUE
- `working/agent_notes/clinical-evidence-scout/territory_T{2,4,6}_*.md` — 3 packets
- `working/agent_notes/methods-scout/territory_T{1,5,7,8}_*.md` — 4 packets
- `reports/landscape_cycle_01.md` — synthesis

## Citation integrity (Lead spot-checks)
8 load-bearing DOIs HEAD-checked 302: 10.34133/hds.0456, 10.1038/s41598-018-24271-9, 10.1146/annurev-statistics-042522-103837, 10.1080/01621459.2017.1319839, 10.7326/M16-2607, 10.1136/bmj-2024-080749, 10.1093/jamia/ocaf082, 10.1126/scitranslmed.abb1655. 49 evidence rows: resolvable TRUE for all 49; verification 48 VERIFIED / 1 UNVERIFIED. Adversarial sections present in all 7 packets.

## State
- Candidates: 0 · Rejections: 0 · Search log rows: 54 · Evidence rows: 49
- Git: pending commit `research(cycle-01): landscape — 7 territories mapped, 54 queries, 49 evidence, 8 seeds`

## Next cycle
**Cycle 2 — Methodological failure points:** Deep dives on T1/T5/T7 (where fancy methods demonstrably break or hide) + T6/T4 assumption stress. Bounded assignments: methods-scout = T1 plasmode design + T5 corpus audit pilot + T7 threshold pilot; clinical-scout = T6 positivity diagnostics on proxy data + T4 prescribing-audit anchoring.
