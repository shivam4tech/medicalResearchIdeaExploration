# Landscape Report — Cycle 1 (2026-08-30)
**Scope:** T1–T8 breadth map. **Agents:** clinical-evidence-scout (T2/T4/T6) + methods-scout (T1/T5/T7/T8); adversarial dark. **Status:** COMPLETE — 7 packets, 54 search queries, 49 evidence rows (48 VERIFIED, 1 UNVERIFIED correctly flagged).

## Summary
All 7 territories surveyed with ≥2 meaningfully different search strategies + systematic-review inspection + adjacent synonyms + backward/forward chaining + adversarial defeat search. Every load-bearing citation verified via DOI/PMID/PMC resolution (spot-checked 8/8 DOIs resolve 302). No candidate promoted yet — this is landscape only (per protocol §4, candidates require adversarial packet + named data pathway + falsifiable framing).

**Key pattern:** Methods are theory-rich, benchmarking-poor. Formal transportability (T6), causal forests (T2), target-trial emulation (T4), DL-for-irregularity (T1), and conformal/UQ (T5) all have mature estimators but thin head-to-head evaluation on realistic clinical noise — especially under informative missingness / visit-process differences that characterize routine care. Synthetic/plasmode (T7) now has an open benchmark (Chen JAMIA 2025) but instrument-validity (does synthetic preserve *method ranking*?) remains unanswered. Reproducibility (T8) has corpus-level audits but no pre-registered direct-replication corpus on public EHR.

**Confidence:** Medium across all 7 territories (reviews exist, but terminology fragmentation + grey literature + rapid 2024-2025 preprints cap confidence below High).

## Territory snapshots

| Terr. | Title | Confidence | Seed papers | Gap (one-line) | Data need | India verdict | Feasibility (small team) |
|---|---|---|---|---|---|---|---|
| **T6** | Transportability & external validity | Medium | 8 (Degtiar & Rose 2023 An Rev 10.1146/….., Pearl/Bareinboim, Levy 2024 PMC11542082 N=6, Ramspek 2023, Dahabreh AJE kwy253) | Formal transportability (inverse-odds weighting, selection diagrams) vs simple recalibration on Indian EHR under informative missingness — no Located comparison | MIMIC→Indian target (ICMR-INDIAB/CMC Vellore) or plasmode mimicking Indian measurement | **STRESSES-ASSUMPTION** (positivity, S-admissibility, visit-process) | Medium — needs Indian partner or plasmode |
| **T2** | Heterogeneity & hidden subgroups | Medium | 8 (Wager & Athey JASA 10.1080/01621459.2017.1319839, Künzel PNAS, Ahlqvist Lancet Diab 10.1016/S2213-8587(18)30051-2, CoINcIDE, JAMA Network Open 2024 28 trials) | Pre-registered null-result HTE/subtyping study: causal forests/metalearners + clustering vs risk-model baseline with prespecified stability (Jaccard>0.75, ARI) on MIMIC→eICU | MIMIC→eICU/AmsterdamUMCdb; Ahlqvist→Indian extension | STRESSES-ASSUMPTION *if* framed as transportability of Ahlqvist clusters; else GEOGRAPHY-ONLY | Medium — public data suffices for core |
| **T4** | Causal inference from observational data | Medium | 8 (Hernán Ann Int Med 10.7326/ANNALS-24-01871, VanderWeele E-value 10.7326/M16-2607, Rosenbaum Biometrika, Hernán JAMA 10.1001/jamanetworkopen.2025.58262) | Target-trial emulation + PS/IPTW + E-value with falsification, stress-tested on Indian practice-pattern confounding (cost-driven switching, MNAR labs, time-zero ambiguity) | MIMIC/plasmode with Indian-typical confounding + Indian EHR if obtainable | **STRESSES-ASSUMPTION** (exchangeability, positivity, consistency, time-zero) | Medium — plasmode first |
| **T1** | Longitudinal & irregular time series | Medium | 7 (Sun Health Data Sci 2026 10.34133/hds.0456, GRU-D 10.1038/s41598-018-24271-9, SeFT, Schneider PMC12070788, arXiv 2410.13113 JMVL-Liang, Naemi 2401.15290) | Plasmode benchmark: DL irregular-series models (GRU-D/SeFT/neural ODE) vs LMM/joint model on calibration/coverage under tunable visit informativeness | Simulation/plasmode from MIMIC + MIMIC replication | GEOGRAPHY-ONLY | **High** — no PHI needed |
| **T5** | Uncertainty & aggregate-statistic failure | Medium | 8 (Riley BMJ 2025 10.1136/bmj-2024-080749, Van Calster J Clin Epi 10.1016/j.jclinepi.2015.12.005, Angelopoulos & Bates 10.1561/2200000101, TRIPOD+AI 10.1136/bmj-2023-078378, Zhou arXiv 2505.02874) | Audit: do aggregate calibration/AUC mask subgroup miscalibration? + Riley bootstrap/Bayesian vs conformal intervals head-to-head with decision-curve analysis | Published validation cohorts / MIMIC / CRASH; TRIPOD corpus | GEOGRAPHY-ONLY (extension India transportability Stage-2) | Medium-High — public data |
| **T7** | Simulation & synthetic data as instruments | Medium | 7 (Chen JAMIA 2025 10.1093/jamia/ocaf082, Liu arXiv2504.11740 cautionary plasmode, Synthea 10.1093/jamia/ocx079, MedGAN, EHRDiff, synthEHRella) | Instrument-validity meta-benchmark: does real-vs-synthetic/plasmode preserve method ranking (Kendall τ) and at what fidelity threshold does it break? | MIMIC-III→synthetic via synthEHRella→MIMIC-IV (TSTR); Synthea baseline | GEOGRAPHY-ONLY | **High** — open data + toolkit |
| **T8** | Reproducibility & robustness | Medium | 7 (McDermott Sci Transl Med 10.1126/scitranslmed.abb1655 511 papers, Beam JAMA 10.1001/jama.2020.2166, Nagendran BMJ m689, TRIPOD+AI, Ioannidis PLoS Med 10.1371/journal.pmed.0020124, Nestor MLHC 2019) | Pre-registered direct replication of influential clinical-ML claim on independent public EHR (MIMIC→eICU) with TRIPOD+AI + feature-robustness | MIMIC-III/IV + eICU + AmsterdamUMCdb (all credentialed, weeks) | GEOGRAPHY-ONLY (Stage-2 India extension natural) | **High** — lowest-risk first paper |

## Adversarial summary (what defeats each gap if found)
- **T6:** One Indian-target transportability application with weighting + positivity diagnostics, or a Valley Health P33-style applied paper on Indian data, collapses novelty; recalibration literature (Sri Lanka Framingham) argues formal correction is decoration if recalibration suffices.
- **T2:** Ahlqvist 2018 replications (Scandinavia/East Asia) partially defeat “no replication”; CoINcIDE framework defeats “no multi-dataset method”; Nature 2024 precision-trial review defeats retrospective-subtyping framing.
- **T4:** Hernán JAMA 2025 emulation + PLOS Digital Health step-by-step causal EHR with negative controls defeats “no rigorous emulation”; BMJ Medicine 2023 E-value rate defeats “sensitivity never done.”
- **T1:** Naemi MIMIC-IV benchmark defeats “no benchmark”; Schneider 2025 simulation guidelines defeat weaker joint-vs-Cox gap; Sun supplement companion code could already contain head-to-head.
- **T5:** Riley BMJ 2025 itself demonstrates individual-interval problem and proposes solution; conformal-in-medicine surveys defeat “no individual intervals”; Pearl R-414 settles Simpson’s interpretation.
- **T7:** Chen JAMIA 2025 *is* the comprehensive benchmark + toolkit — defeats any “benchmark synthetic generators” proposal; Liu cautionary note defeats “plasmode unstudied”; surviving gap is meta-benchmark of *methods on synthetic* not generators.
- **T8:** McDermott/Beam corpus audits defeat “crisis undocumented”; Johnson/Harutyunyan MIMIC mortality benchmarks defeat “no ICU prediction replications”; TRIPOD+AI defeats “no reporting standard.” Surviving gap is *named-model, pre-registered, independent-data* direct replication.

## Datasets inventory (named, with access routes)
- **Open/physionet credentialed (weeks, CITI+DUA):** MIMIC-III/MIMIC-IV (ED/ICU), eICU, AmsterdamUMCdb, PhysioNet Challenges 2012/2019.
- **Managed access:** UK Biobank (managed), CPRD Aurum/GOLD (licensed), CARRS, PURE South Asia, YODA/Vivli (trial data).
- **Restricted/Indian (requires proposals/DUA, non-trivial):** ICMR-INDIAB, CMC Vellore EHR, AIIMS Delhi, CARRS, HEALTHSTACK/ABDM federated (NDHM sandbox).
- **Open synthetic/plasmode (immediate, preferred for T1/T7):** Synthea (10.1093/jamia/ocx079), synthEHRella toolkit (github.com/chenxran/synthEHRella), plasmode resampling from MIMIC (preferred per Liu Generate-Treatment framework).

## India relevance — honest accounting
- **STRESSES-ASSUMPTION:** T6, T4, T2 (only under transportability framing). Indian care stresses positivity/overlap, S-admissibility, measurement-frequency, informative missingness, practice-pattern confounding, baseline risk, multimorbidity structure — all core identifying assumptions. Re-running within US/Canada would not expose these violations.
- **GEOGRAPHY-ONLY:** T1/T5/T7/T8 for v1 as framed — core questions are population-agnostic; Indian extension is a defensible Stage-2 transportability question but decoration if forced into v1.

## Candidate seeds (for Cycle 2 deepening — not yet promoted)
All require adversarial packet + named data pathway + falsifiable framing + mandatory baselines before promotion (gate §3). Ordered by methods-forward priority + small-team feasibility:

1. **T8-direct-replication** — Pre-registered direct replication of a named influential clinical-ML model (e.g., Harutyunyan MIMIC mortality benchmark) on MIMIC→eICU with TRIPOD+AI, subgroup/feature-robustness. Public data, falsifiable, publishable as negative. *Feasibility: HIGH.*
2. **T7-instrument-validity** — Real-vs-synthetic/plasmode rank preservation (Kendall τ) for a T1/T5 methods comparison via synthEHRella. *Feasibility: HIGH, no PHI.*
3. **T1-irregularity benchmark** — Plasmode with tunable visit informativeness: GRU-D/SeFT/neural ODE vs LMM/joint model on calibration/coverage. *Feasibility: HIGH.*
4. **T5-aggregate-masking audit** — TRIPOD corpus (2015-2025) audit for subgroup miscalibration despite passing overall metrics + Riley vs conformal head-to-head with decision analysis. *Feasibility: MEDIUM-HIGH, needs corpus curation.*
5. **T6-transportability-vs-recalibration** — Inverse-odds weighting with selection diagrams vs simple recalibration, real MIMIC→plasmode mimicking Indian measurement patterns; Indian EHR extension Stage-2. *Feasibility: MEDIUM (plasmode v1 HIGH).*
6. **T4-emulation-falsification** — Target-trial emulation with E-value anchored to Indian prescribing audits + negative controls, MIMIC/plasmode first. *Feasibility: MEDIUM.*
7. **T2-falsifiable-heterogeneity** — Pre-registered null-result HTE: causal forests vs risk-model HTE with prespecified stability on MIMIC→eICU. *Feasibility: MEDIUM.*
8. (Optional) **T6/T2-India-transport extension** — Ahlqvist 5-cluster transportability to ICMR-INDIAB / CMC Vellore (requires Indian partner; Stage-2).

## Recommended Cycle 2 focus (deepening: failure points)
Per protocol Cycle 2 = “Methodological failure points: where existing approaches demonstrably break.” Recommend bounded assignments:
- **Methods-scout:** T1 irregularity benchmark design + T5 aggregate-masking pilot audit (corpus construction method) + T7 instrument threshold pilot (one generator, one methods comparison).
- **Clinical-evidence-scout:** T6 transportability assumption stress inventory (positivity diagnostics on Indian proxy data) + T4 confounding-anchoring feasibility (local prescribing audit literature).

## Citation integrity (Lead audit)
- DOIs spot-checked 8/8 resolve 302 (Sun 10.34133/hds.0456, GRU-D 10.1038/s41598-018-24271-9, Degtiar 10.1146/…, Wager & Athey 10.1080/…, VanderWeele 10.7326/M16-2607, Riley 10.1136/bmj-2024-080749, Chen 10.1093/jamia/ocaf082, McDermott 10.1126/…). One evidence row (T2-06 JAMA Network Open) correctly flagged UNVERIFIED (DOI pending, URL-only). Two search_log rows flagged UNVERIFIED for 403/timeout — correctly marked, not used to support gaps. All packets include explicit Evidence AGAINST sections and India verdict justifications.

## Artifacts
- Packets: `working/agent_notes/clinical-evidence-scout/territory_T*.md` (3), `working/agent_notes/methods-scout/territory_T*.md` (4)
- Ledgers: `literature/search_log.csv` (54 data rows, 6-9 queries per territory, verbatim), `literature/evidence_registry.csv` (49 rows, 48 VERIFIED)
- This report: `reports/landscape_cycle_01.md`
- Journal: `journal/cycles/cycle_01.md` (updated), `journal/research_log.md` (appended on commit)

*Next gate:* Cycle 2 deepening + adversarial kill preparation (reviewer stays dark until ≥6 candidates or a REVIEW promotion; use self-authored adversarial challenges meanwhile).
