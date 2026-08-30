# Cycle 3 — India / Transportability Opportunities (science not geography)
**Date:** 2026-08-30 · **Agents:** Research Lead + clinical-evidence-scout + methods-scout (adversarial-reviewer DARK until candidate promotion) · **Rate-limit incidents:** none

## Objective
Make India transportability *executable*: (a) define graded Indian shift with concrete numbers, (b) translate audit prevalences into E-value/bias parameters, (c) identify which influential models remain un-replicated for a public-data direct replication, and (d) test whether celebrated heterogeneity (Ahlqvist 5 clusters) transports to Indian covariate support.

## Questions for this cycle
1. What concrete shift magnitudes define Indian-typical plasmode injection (BMI/diabetes threshold, CVD age, measurement frequency, selective ordering, formulary/cost switching)?
2. Can WHO audit proportions + AYUSH co-use prevalence be turned into VanderWeele E-value RR parameters for anchored sensitivity?
3. Which 3-5 top-cited clinical-ML models lack a pre-registered MIMIC→eICU replication — and which is the cleanest first target?
4. Do Ahlqvist diabetes 5 clusters transport to Indian/CARRS cohorts or fail overlap under Indian support?

## Assignments
- **clinical-evidence-scout:** cycle03_T6_indian_shift_implementation (graded shift injection table), cycle03_T4_audit_numbers_extraction (audit→RR translation, ≥2 audit extracts with numbers)
- **methods-scout:** cycle03_T8_named_model_sweep (per-model replication search, 3-5 models), cycle03_T2_HTE_transport (Ahlqvist→Indian transport)
- Brief: `working/CYCLE_03_BRIEF.md` (4 packets, 13-section, self-adversarial, India verdict).

## Rate discipline
Global pool muse-spark-1.2-contributor-free (opencode-zen) ~40/min, target ≤24, ceiling 30, max 2 concurrent. 84 model calls in ~20m (~4.2/min, no 429s).

## Findings
**4/4 packets COMPLETE. Ledgers: search_log 118→172 (170 VERIFIED / 2 UNVERIFIED-timeout), evidence 94→133 (130 VERIFIED / 2 TRUE / 1 UNVERIFIED-T2-06 flagged).**

| Packet | Established | Failure demonstrated | Design delivered | India | Conf. |
|---|---|---|---|---|---|
| **T6 graded Indian shift** | ICMR-INDIAB-17 n=113k (11.4% diabetes, 35.5% HTN) + ICMR-INDIAB-23 MONO 43.3% thin-fat (MOO 28.3%, rural 46% vs 39.6% urban, Tripura 56.7%, T2D OR MONO 6.90) + CARRS/UKB-SA 5–10 yr earlier CVD; transport formalism (Degtiar, Dahabreh, Kang/Inoue) | Visit-process sweep returned federated-learning not Indian selective ordering; adversarial `Indian shift plasmode` zero hits; audits Kaur 2026 ED (2.65 drugs/Rx, 90.3% injections, 8.5% diagnosis) + Khanna 2025 Ward (6.8 drugs/Rx, 4.7% generic) extracted via PMCs now anchor shift | G0→G3 injection table: BMI 28.3→22.8, MONO 0→56.7%, age 62→48, WC high 0→82%, HbA1c 78%→15% (selective P 0.20 asymptomatic), generic 100→4.7%, AYUSH 0→96%, docs 100→8.5%; propensity-tilting + S_visit censoring; diagnostics primary (SMD, AUC, ESS, trimming) | **STRESSES-ASSUMPTION** — positivity/S-admissibility/consistency/exchangeability/missingness all stressed | Med |
| **T4 audit→RR translation** | E-value 10.7326/M16-2607 + B(p1,p0) + Zhang 10.1136/bmjmed-2022-000366 (<15% QBA), Lipsitch NC 10.1097/EDE.0b013e3181d61eeb expected <20% used, Hernán target trial | Audit ↔ causal sensitivity corpora do not cite each other; adversarial `audit→E-value bridge` returned calculators not prevalence-anchored translation; MUST audits extracted (Kaur PMC13312064 Tables 1-10 + Khanna PMC12813935 Tables 2-6) + AYUSH Galib 95.9% (44% simultaneous) | Audit→RR bridge: p1/p0 imputed per contrast → B → R* where E(R*)=B (e.g., RR_obs 1.45 E=2.26 vs B 1.31 robust; R*≈1.4–2.0 titration); NC ladder alongside; plasmode calibration at P(U)=0.10/0.44/0.96 | **STRESSES-ASSUMPTION** — AYUSH EHR-invisible exchangeability, FDC treatment-version, polypharmacy positivity | Med |
| **T8 named-model sweep** | Reproducibility worst in ML-for-health (McDermott scitranslmed, 511 papers), TRIPOD+AI 10.1136/bmj-2023-078378 27-item, MIMIC→eICU/AmsterdamUMCdb stack mature; sepsis review 22 studies only 3 ext. validated | Per-model adversarial queries (Harutyunyan 10.1038/s41597-019-0103-9/Rajkomar 10.1038/s41746-018-0029-1/Moor GRU-D) → **zero pre-registered direct replication with TRIPOD+AI** for any flagship; Harutyunyan re-used as baseline suite not replication; Rajkomar FHIR not openly replicated | Harutyunyan multitask LSTM frozen → MIMIC-III/IV train → eICU primary + AmsterdamUMCdb/HiRID secondary, leakage controls, co-primary AUROC/AUPRC/calibration/Brier/DCA+subgroups, baselines LR+SOFA+GBM; failure rule AUROC>0.05 or slope <0.8 | **GEOGRAPHY-ONLY v1** — universal stationarity; Stage-2 Indian ICU extension | **Med-High** |
| **T2 Ahlqvist HTE transport** | Ahlqvist 10.1016/s2213-8587(18)30051-2 5 clusters 2086 cites; Scandinavian replication stable; East Asian shift SIRD↓ SIDD/MOD↑ at lower BMI; Indian descriptive clusters exist (Anjana) | Indian replications are de novo clustering, not falsifiable transport test (centroids vs de novo + positivity/overlap + outcome gradients); adversarial `Ahlqvist Indian CARRS` zero formal transport; GADA/HOMA systematically unavailable = measurement-transport asymmetry | ANDIS centroids → CARRS/ICMR-INDIAB/CMC registry + UKB-SA proxy; transport-labels vs de novo (k=5, 6→3 var arms), inverse-odds weighting diagnostics (Dahabreh), ARR + outcome gradients (CKD/retinopathy/insulin) | **STRESSES-ASSUMPTION** — exchangeability/positivity of clustering features, S-admissibility (measurement) | Med |

Synthesis: `reports/india_opportunities_cycle_03.md` (8-design portfolio; promotion set below). T6+T4 share G0→G3 plasmode — diagnostics (T6) + thresholds (T4) on same titration.

## Decisions
**Promotion set for candidate dossiers (pending Lead next-searches at full-text level per packet appendices + adversarial activation):**

| Rank | Seed | Packet | India | Feasibility | Decision |
|---|---|---|---|---|---|
| 1 | T8 Harutyunyan LSTM direct replication | cycle03_T8 | GEOGRAPHY-ONLY v1 | Public/credentialed weeks | **PROMOTE** |
| 2 | T7 fidelity vs τ threshold (from Cycle 2) | cycle02_T7 | GEOGRAPHY-ONLY | Open data | PROMOTE |
| 3 | T1 plasmode DL-vs-classical | cycle02_T1 | GEOGRAPHY-ONLY | Simulation | PROMOTE |
| 4 | T5 corpus subgroup-calibration audit | cycle02_T5 | GEOGRAPHY-ONLY | Literature | PROMOTE |
| 5a | T6 graded Indian shift plasmode | cycle03_T6 | STRESSES-ASSUMPTION | Plasmode+proxy | **PROMOTE India flagship A** |
| 5b | T4 anchored E-value + NC | cycle03_T4 | STRESSES-ASSUMPTION | Plasmode+audits | **PROMOTE India flagship B (joint with T6)** |
| 6 | T2 Ahlqvist transport → CARRS | cycle03_T2 | STRESSES-ASSUMPTION | Restricted ~3mo | PROMOTE India HTE flagship |

Gate: executable PubMed/arXiv II next-searches per packet appendix at full-text level must return empty; adversarial-reviewer kill round at ≥6 candidates (next cycle).

## Candidates created/weakened/killed
Created dossiers deferred to `ideas/candidate_NNN.md` (next cycle after Lead next-searches). Weakened/killed: none this cycle. CARRS/UKB-SA DUA lane opens (India flagships staged on UKB-SA proxy while CARRS pends).

## Rate-limit incidents
None (84 calls, ~4.2/min, ceiling 30, no 429s; adversarial still dark).

## Ledgers updated
- `literature/search_log.csv` 118→**172 rows (170 VERIFIED / 2 UNVERIFIED-timeout)** — 54 new this cycle (incl. 14 doi_check + 4 europepmc_api extracts + 28 web_search); spot-check 4/4 302 (ICMR-INDIAB-23, Ahlqvist, Harutyunyan, Kaur ED).
- `literature/evidence_registry.csv` 94→**133 rows (130 VERIFIED / 2 TRUE / 1 UNVERIFIED-T2-06 flagged — same single flagged as Cycle 2)** — 39 new, all VERIFIED.

## State
- Candidates: 0→0 (dossiers pending next cycle) · Rejections: 0 · Search log rows: 118 → 172 · Evidence rows: 94 → 133
- Packets: 4/4 Cycle 3 + cumulative 9 distinct designs (5 Cycle 2 + 4 Cycle 3; T8 strengthens)

## Next cycle
Cycle 4 — Data-independent first projects: lock first-project protocol for highest-feasibility candidate (expected T8/T7/T1). Submit CARRS DUA + UKB RAP SA application (India flagships proxy). Run Lead next-searches (4–5 queries per packet) + adversarial kill round.
