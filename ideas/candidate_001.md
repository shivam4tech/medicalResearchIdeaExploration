# Candidate 001 — Harutyunyan 2019 MIMIC→eICU TRIPOD+AI Direct Replication (A public)

**Source design:** T8 cycle03+04 (methods-scout) — Cycle 04 T8 replication lock `working/agent_notes/methods-scout/cycle04_T8_replication_lock.md`
**Class:** A public (credentialed) | **Data path:** MIMIC-III/IV + eICU-CRD v2.0 + AmsterdamUMCdb (HiRID secondary) — weeks via PhysioNet/ODAP
**Status:** PROMOTION DOSSIER — Cycle 5 first wave (no DUA needed) | **Date:** 2026-08-30
**Agent:** methods-scout | **India verdict:** GEOGRAPHY-ONLY v1 (STRESSES-ASSUMPTION deferred to Stage-2 Indian ICU transport)
**Confidence:** Medium-High (gap: at least one flagship un-replicated as pre-registered TRIPOD+AI direct replication)

---

## Gate 1 — Gap Verification (strategies, reviews inspected, synonyms, chaining, adversarial — queries cited)

**Claim to verify:** No published pre-registered (OSF/Registered Report) direct replication of **Harutyunyan et al. 2019 multitask LSTM (Sci Data 6:96, DOI 10.1038/s41597-019-0103-9)** with TRIPOD+AI-level calibration/subgroup/DCA and leakage controls exists on independent public EHR MIMIC→eICU (AmsterdamUMCdb second external).

**Strategy A — Replication terminology (model-name + pre-registration, DISTINCT):**
- `Harutyunyan MIMIC benchmark direct replication external validation pre-registration OSF` (2026-08-30, T8-C4-StrategyA-replication, 5 hits) — hits: FORRT direct replication glossary + PMC9442273 conceptual replication review; **no Harutyunyan→eICU pre-registered direct replication located**. Carry-forward Cycle 03: `Harutyunyan MIMIC-III benchmark replication eICU AmsterdamUMCdb external validation` (T8-model-Harutyunyan / T8-adversarial-Harutyunyan, 5 hits), `replication reproducibility external validation MIMIC-IV eICU Harutyunyan 2019` (Cycle 03, 5 hits) — per-model sweep for Harutyunyan only; all inspected for frozen-model replication vs baseline-suite re-use.

**Strategy B — Leakage / calibration terminology (model-name-free, DISTINCT from Strategy A — TRIPOD+AI item vocabulary):**
- `ICU prediction data leakage time-zero lookahead calibration slope decision curve leakage checklist` (2026-08-30, T8-C4-StrategyB-leakage-calibration, 5 hits) — leakage/MeSH distinct: time-zero, lookahead, calibration slope, decision curve, leakage checklist; hits: non-EHR calibration glossary confirms terminology gap (no EHR leakage checklist located).
- `clinical prediction model temporal leakage lookahead time-zero EHR calibration` (2026-08-30, T8-C4-leakage-deep, 5 hits) — deep leakage sweep confirms fragmented vocabulary vs replication terminology (required distinct strategy).
- `Van Calster calibration hierarchy Riley prediction interval TRIPOD AI 2024` (2026-08-30, T8-C4-calibration-chain, 5 hits) — calibration-specific terminology: Van Calster hierarchy + Riley intervals + TRIPOD+AI; duplicates confirm lineage but no replication closes gap.

**Reviews inspected (5 required):**
1. **McDermott et al. Sci Transl Med 2021** (DOI 10.1126/scitranslmed.abb1655) — 511-paper audit: ML-for-health reproducibility worst on dataset/code; load-bearing for public-EHR replication path. **302 HEAD 2026-08-30 → science.org/doi/10.1126/scitranslmed.abb1655**
2. **Nagendran et al. BMJ 2020** (DOI 10.1136/bmj.m689) — 81 DL-vs-clinician studies, majority high ROB, poor external validation; claim-fragility anchor. **302 → bmj.com/lookup/doi/10.1136/bmj.m689**
3. **Collins et al. TRIPOD+AI 2024** (DOI 10.1136/bmj-2023-078378) — 27-item checklist superseding TRIPOD 2015 (DOI 10.1136/bmj.g7594); calibration/fairness/code items. **302 → bmj.com/lookup/doi/10.1136/bmj-2023-078378** (PMC11019967 verified)
4. **Van Calster et al. J Clin Epidemiol 2016** (DOI 10.1016/j.jclinepi.2015.12.005) — calibration hierarchy mean→weak→moderate→strong. **302 → linkinghub.elsevier.com/retrieve/pii/S0895435615005818**
5. **Riley et al. BMJ 2025** (DOI 10.1136/bmj-2024-080749) — individual-level uncertainty intervals around risks (CRASH 0.477–0.693); anchors equivalence bounds. **302 → bmj.com/lookup/doi/10.1136/bmj-2024-080749**

**Synonyms checked:** reproducibility ↔ replicability ↔ robustness ↔ generalizability ↔ external validation; direct ↔ conceptual replication; leakage ↔ lookahead bias ↔ temporal leakage ↔ time-zero misspecification; calibration slope ↔ intercept ↔ ICI ↔ calibration hierarchy; many-analysts ↔ researcher-degrees-of-freedom ↔ multiverse; feature drift ↔ non-stationary health records.

**Chaining (Harutyunyan 10.1038/s41597-019-0103-9 → ricu/METRE/YAIB harmonization → Nestor drift → Van Calster/Riley):**
- Harutyunyan 10.1038/s41597-019-0103-9 (2019 Sci Data benchmark, YerevaNN/mimic3-benchmarks) → METRE (S1532046423000771, MIMIC-IV+eICU extraction) → `ricu` R package (PMC10268223, CRAN, MIMIC-III/IV/eICU/HiRID/AmsterdamUMCdb) → YAIB (Moor/Yèche arXiv:2208.06691, flexible multi-center benchmark 216k stays) → Nestor et al. 2019 MLHC PMLR 106:381-405 (arXiv:1908.00690, feature drift) → Van Calster 2016 → Riley 2025 → TRIPOD 2015 → TRIPOD+AI 2024. Verified via `METRE ricu YAIB harmonization MIMIC eICU AmsterdamUMCdb HiRID` (2026-08-30, 5 hits, YAIB+ricu PMC returned) + `many analysts researcher degrees freedom feature drift Nestor non-stationary health records` (adjacent).

**Adversarial (explicit goal: FIND existing exact replication that closes gap — T8-C4-adversarial-exact-replication):**
- `Harutyunyan 2019 multitask LSTM eICU AmsterdamUMCdb exact replication TRIPOD` (2026-08-30, 5 hits) — **no pre-registered exact replication with TRIPOD+AI calibration/subgroup/DCA located**; gap survives. Carry-forward: `Rajkomar deep learning EHR replication independent validation FHIR` (no independent FHIR replication), `PhysioNet 2019 sepsis prediction external validation MIMIC eICU replication` (task-level replication not named-model), `feature robustness non-stationary health records Nestor external validation failure` (mechanism study, not protocol). **6+ search_log rows verbatim satisfied** (see Appendix table).

**Language (proportional):** No directly equivalent pre-registered direct replication with TRIPOD+AI calibration/subgroup/DCA was identified in the searches performed so far — not "nobody has ever studied external validation" (corpus-level external validation of 3/22 sepsis studies etc. exists; named-model frozen replication does not).

---

## Gate 2 — Written Adversarial Challenge (self-adversarial per dossier)

**Goal:** steelman closure — 5 defeaters that would kill novelty if read generously.

1. **"Harutyunyan is already multiply re-used — that's replication."** Many papers use Harutyunyan preprocessing (MIMIC-Extract, METRE, YAIB) and beat the LSTM on MIMIC-III/IV with a new architecture. *Rebuttal:* Re-use as baseline suite / SOTA-chasing is not a **pre-registered direct replication** with TRIPOD+AI reporting on an independent eICU/HiRID site. Authors optimize the new model (HARKing), rarely report calibration/subgroups/DCA externally. No paper states aim "we pre-registered a direct replication of Harutyunyan LSTM on eICU with TRIPOD+AI and it replicates/fails."

2. **"YAIB/METRE 2024–2026 already replicates — challenge winners are covered."** YAIB domain-shift studies (HiRID/MIMIC-IV/eICU, 216k stays) show cross-site AUROC drops 0.047–0.082 + calibration slope collapse 1.007→0.417 with care-intensity features. *Rebuttal:* Task-level replication of *sepsis/mortality as a task* with modern harmonization, not a **frozen Harutyunyan artifact with original hyperparameters + TRIPOD+AI subgroup/DCA**. Closest but not exact; Harutyunyan arm remains open.

3. **"Many-analysts / Nestor already covers robustness."** Frontiers many-analysts + Nestor drift could be argued to cover replication. *Rebuttal:* No clinical-EHR many-analysts study surfaced (same question, many teams, same public dataset); Nestor shows *that* drift exists, not a pre-registered protocol with leakage audit. Surviving claim is reusable **protocol**, not drift existence.

4. **"TRIPOD+AI is 16 months old — anachronistic to demand it now."** Referee could argue pre-2024 work should be judged by TRIPOD 2015. *Rebuttal:* Packet does not require citation of "TRIPOD+AI"; it requires **checklist-item coverage** (pre-registration, calibration, subgroup/fairness, code) already best practice pre-2024. Sepsis systematic review (n=22, only 3 externally validated) shows items were commonly missing even under TRIPOD 2015. Contribution is demonstrating *what changes when checklist is followed*.

5. **Closest defeater that would close if extended:** **YAIB (Moor/Yèche arXiv:2208.06691)** — if next release includes a **pre-registered, OSF-timestamped, TRIPOD+AI-reported direct replication of frozen Harutyunyan LSTM with original hyperparameters, leakage checklist, subgroup/DCA** (not generic LSTM baseline), gap closes; correct next step is second-flagship extension (Rajkomar reconstruction or sequestered sepsis winner frozen-model replication). **Monitoring required before RR submission** (YAIB GitHub releases, ricu vignettes, Harutyunyan GitHub issues).

If any extended post-2026 to include pre-registered Harutyunyan→eICU TRIPOD+AI replication with calibration/subgroup/DCA, Harutyunyan arm closes.

---

## Gate 3 — Falsifiable Question (negative = publishable, stated)

**Primary question (direct replication, OSF/Registered Report, executable v1):**

*Does a pre-registered direct replication of Harutyunyan et al. 2019 multitask LSTM mortality model (frozen architecture + original hyperparameters, leakage-controlled) trained on MIMIC-III (sensitivity MIMIC-IV) replicate on independent public EHR — eICU-CRD v2.0 (primary) and AmsterdamUMCdb (secondary European) — when evaluated under TRIPOD+AI 2024 with co-primary metrics AUROC, AUPRC, calibration slope/intercept + loess plot + ICI, Brier, DCA net benefit, and subgroup calibration (age/sex/race-ethnicity/SOFA/hospital type)?*

**Equivalence / decision rule (pre-registered, two-sided, skeptical):**

- AUROC success: `AUROC_external ≥ AUROC_original − 0.05` (original mortality ≈0.86 → threshold 0.81)
- Calibration success: slope ∈ [0.8, 1.2] **and** intercept ∈ [−0.3, 0.3] on logit scale
- Subgroup heterogeneity success: max pairwise AUROC range across pre-specified strata ≤0.10 (Holm-corrected)
- DCA success: net benefit at 10% and 20% mortality thresholds > trivial (prevalence) **and** > SOFA baseline

**Replication succeeds ONLY if all four hold.** Published in *BMJ/JAMIA/MLHC/Sci Data* as either outcome.

**Publishable negative (explicit):** **Did-not-replicate** — AUROC drop >0.05, or calibration slope <0.8 or >1.2 (over/underfitting), or subgroup heterogeneity >0.10, or DCA net benefit ≤ trivial/SOFA externally — with diagnosed failure mode (leakage, feature drift per Nestor, threshold miscalibration, observation-process leakage). Failure to replicate is **guaranteed publishable as a Registered Report**; negative cal-collapse is methods contribution establishing transport gap and reusable workflow (code freeze, data freeze hash, TRIPOD+AI checklist, feature-definition archive).

H0 (gap-closed): such pre-registered replication already exists → systematic sweep showing corpus exists is publishable. H1 (gap holds): no such replication → protocol is first target.

---

## Gate 4 — Named Data Pathway (A/B/C/D with timeline/access)

**Path: A public (credentialed) — no DUA negotiation, no hospital data.**

| Dataset | Role | Access route | Timeline | N (eligible) |
|---------|------|--------------|----------|--------------|
| **MIMIC-III v1.4** (Johnson Sci Data 2016, DOI 10.1038/sdata.2016.35) | Train (primary, matching original) | PhysioNet credentialing: CITI + signed DUA | **1–2 weeks** (can start coding on `mimic-iii-demo` immediately) | ~38k ICU stays after Harutyunyan exclusions (age≥18, LOS≥10h for 24h window) |
| **MIMIC-IV v2.2+** (Johnson Sci Data 2023, DOI 10.1038/s41597-022-01899-x) | Train sensitivity (modern schema) | Same PhysioNet | Same | ~65k stays |
| **eICU-CRD v2.0** (Pollard Sci Data 2018, DOI 10.1038/s41597-018-0006-0) | **Test external PRIMARY** (US multi-center 208 hospitals) | PhysioNet credentialing | Same | ~139k stays → filtered ~50–70k meeting common-variable availability; ~4–5k events (mortality 8–10%) |
| **AmsterdamUMCdb v1.0.2** (Thoral Sci Data 2021, DOI 10.1038/s41597-021-00737-X) | Test external SECONDARY (European, GDPR de-identified) | Amsterdam UMC ODAP portal (credentialed) | **2–4 weeks** | ~23k admissions → ~15k eligible |
| **HiRID v1.1.1** (Faltys Sci Data 2021, DOI 10.1038/s41597-021-00968-9) | Alternative secondary (Swiss, 2-min resolution) for drift sensitivity | PhysioNet mirror | 1–2 weeks | ~34k admissions |
| Challenge sets (PhysioNet/CinC 2012, 2019) | Extension only (second flagship) | Open | Immediate | — |

**Harmonization:** Pre-register `ricu` 0.5.8 as PRIMARY pipeline; METRE and YAIB as sensitivity (harmonization choice is an estimand). Time-zero: ICU admission = first `icustay`/`patientUnitStayId`; outcome = hospital mortality; vitals 1h grid (median of 5-min periodic in eICU), labs LOINC-mapped, mask indicator frozen. Leakage checklist (time-zero locked, lookahead audit `max(feature_time) ≤ time_zero+24h`, train/test leakage, missing-data frozen) committed before external test access.

**Power:** eICU ~50k, Amsterdam ~15k → AUROC SE (DeLong) 0.003–0.005, calibration slope SE 0.04–0.06 → power >0.99 for Δ=0.05 AUROC drop, >0.90 for slope 1.0→0.8 shift. Calibration/subgroup precision is binding (not N).

**Week plan:** Week 1 extraction containerized (Docker python 3.11, torch 2.3, ricu 0.5.8); Week 2 OSF preregistration locked before external access + training on MIMIC-III (single GPU 2–4h per run, 5-fold CV ×3 seeds ≈1–2 days); external evaluation inference-only (hours). **Total v1 wall-clock 3–4 weeks.**

---

## Gate 5 — Mandatory Baselines (named, simple benchmark included)

All baselines see **identical feature sets and splits**; hyperparameters tuned **only on MIMIC validation split**.

1. **Logistic regression (L2-regularized, Platt-scaled)** on tabular aggregation (mean + last value per variable over 24h, plus mask-rate features) — the "well-specified simple" baseline.
2. **Established clinical score: SOFA** (and APACHE IV approximation where available) — re-calibrated intercept for external site (Van Calster weak calibration). SOFA alone is clinical baseline to beat.
3. **Gradient boosting (GBM / XGBoost)** on same tabular aggregation — Christodoulou lineage (ML vs LR no-benefit prior). HPs via MIMIC validation only.
4. **Trivial baseline: prevalence prediction** (predict overall mortality rate) — for AUPRC contextualization (Pinker AUPRC critique) and DCA trivial comparator.
5. *(Optional exploratory 5th):* Random forest on same tabular features as GBM cross-check.

**Headline comparison (pre-registered primary outcome):** Does Harutyunyan LSTM outperform LR + SOFA + GBM on *external* AUROC/calibration/DCA, or does simpler baseline suffice? Either outcome is publishable and prevents HARKing. ML gets no preference.

---

## Gate 6 — Ethics / Privacy (path identified)

- **De-identified public data** under PhysioNet Data Use Agreement (MIMIC, eICU, HiRID) and ODAP agreement (AmsterdamUMCdb); data have undergone HIPAA Safe Harbor–equivalent de-identification with date shifting; no re-identification attempted; no linkage to external identifiers.
- **Credentialing:** CITI Program "Data or Specimens Only Research" or equivalent + PhysioNet credential approval + signed DUA before access; restricted to listed investigators; no redistribution beyond DUA.
- **Institutional path:** IRB exemption / not-human-subjects determination (de-identified, publicly shared for research) — file protocol with institutional IRB office upon credentialing; OSF preregistration declares ethics path (TRIPOD+AI Item 23).
- **Privacy-preserving dissemination:** Share only **code, hashes, and aggregate performance tables**; no patient-level extracts released. Feature-definition tables contain no PHI. Docker environment and OSF data-freeze hashes (SHA256 of extraction SQL + feature tables) are archived, not data.
- **GDPR:** AmsterdamUMCdb access via ODAP respects GDPR de-identification; European data residency requirements satisfied via Amsterdam UMC agreement.

---

## Gate 7 — Clinical Relevance (affirmed provisionally by scout, physician TBD)

*Provisionally affirmed — physician collaborator to confirm.*

- Clinicians need to know whether a published "ICU mortality LSTM beats LR/SOFA" claim is **actionable or overfit to BIDMC/MIMIC**. eICU (208 community/regional hospitals) with honest calibration + subgroup reporting directly answers transportability; even a null protects patients from premature deployment and informs governance (drift monitoring per Nestor).
- **Calibration collapse** is clinically actionable: a model with AUROC 0.84 but calibration slope 0.6 systematically over-estimates risk at the high end and under-estimates at low end — miscalibrated thresholds misguide escalation decisions. DCA at 10%/20% mortality thresholds is the decision-relevant metric (Vickers); AUROC alone is insufficient.
- **Subgroup heterogeneity >0.10** signals fairness risk (age/SOFA/race-ethnicity strata) — health-system AI committees need this before deployment. Observation-process leakage finding (measurement-count features improve internal AUROC but worsen external calibration) has workflow implications for brittle EHR definitions.

---

## Gate 8 — Scope Ceiling (small-team months, explicit)

**Ceiling: 2–3 investigators, 3–4 weeks wall-clock to pre-registered external results + 2–4 weeks to Registered Report Stage 1 write-up; total 1.5–2.5 months.**

- **Personnel:** 1 ML engineer (MIMIC pipelines + LSTM training) + 1 biostatistician (calibration/DCA/subgroup) + 0.25 FTE clinician for leakage adjudication + harmonization mapping.
- **Compute:** Single GPU (A100 40GB or RTX 4090), <48h for full 5-fold CV ×3 seeds + inference; harmonization is R/Python on CPU; cost <$100 cloud.
- **Milestones:** Wk1 Docker + ricu harmonization stub + leakage checklist; Wk2 OSF lock pre-external-access; Wk3–4 external evaluation + calibration/DCA; Wk5–8 manuscript (TRIPOD+AI 27-item mapping, 8 tables: harmonization mapping, performance, calibration, subgroup, DCA, drift, sensitivity).
- **Explicitly OUT of scope v1:** Rajkomar FHIR reconstruction, Indian ICU transport (Stage-2), many-analysts experiment, fairness mitigation development — all follow-ons.

---

## Evidence AGAINST (strongest reasons this may not be a gap)

See Gate 2 — 5 defeaters + YAIB as closest corpus. Additional nuance: PhysioNet/CinC leaderboard replications exist for mortality/sepsis as *tasks*; a TRIPOD+AI referee could argue calibration reporting is already covered by Van Calster/Riley guidance without needing a named-model replication. Response: guidance exists but **adherence on an independent eICU test with frozen artifact is unmeasured** — the replication *measures adherence*.

---

## Relevant Datasets

Section Gate 4 above (MIMIC-III/IV, eICU-CRD v2.0, AmsterdamUMCdb, HiRID — all public/credentialed). No prospective collection; no private hospital negotiation for v1. Indian ICU EHR (Stage-2 extension only) — requires MOU/DUA with Indian tertiary ICU (e.g., AIIMS/CMC), not bundled.

---

## India Relevance Verdict

**GEOGRAPHY-ONLY for v1** — justified.

Core question (does Harutyunyan MIMIC-trained LSTM transport to independent public EHR with honest calibration/subgroup reporting?) stresses a **universal** statistical assumption (stationarity/external validity), not an India-specific one. Indian data not needed; claiming STRESSES-ASSUMPTION for v1 would be decoration (per docs/03 §6).

**Defensible Stage-2 extension that would genuinely stress an assumption:** Replication of frozen/retrained Harutyunyan model on **Indian ICU EHR** (where baseline risk, case-mix younger, tropical sepsis etiologies, CKD/glucose trajectories, measurement availability — lactate/ABG/ventilator parameters — and practice patterns differ) would test **transportability across health-system contexts** and stress **exchangeability / S-admissibility** and calibration transportability. Requires Indian partner dataset with MOU/DUA, proposed as follow-on.

---

## Confidence

**Medium-High** (for gap: at least one flagship un-replicated as pre-registered TRIPOD+AI direct replication on independent public EHR).

Strengths: per-model adversarial sweep explicitly sought replications for Harutyunyan and returned no hit meeting definition; corpus-level literature (3/22 externally validated) independently shows thin external validation; feasibility high (all data public/credentialed, pipelines open, compute modest). Risks capping below High: YAIB active harmonization could publish frozen-model replication before submission; TRIPOD+AI recency framing needs "checklist-item coverage" language; non-English theses outside open-web coverage need PubMed MeSH sweep before submission.

---

## Recommended Next Search (executable)

```pubmed
# 1. Named-model + TRIPOD+AI replication conjunction (adversarial closure)
("Harutyunyan"[Title/Abstract] OR "Multitask learning and benchmarking with clinical time series"[Title/Abstract] OR "MIMIC-III benchmark"[Title/Abstract]) AND ("external validation"[Title/Abstract] OR "replication"[Title/Abstract] OR "reproducibility"[Title/Abstract]) AND ("eICU"[Title/Abstract] OR "AmsterdamUMCdb"[Title/Abstract] OR "HiRID"[Title/Abstract])

# 2. Leakage-specific EHR audit
("data leakage"[Title/Abstract] OR "lookahead bias"[Title/Abstract] OR "temporal leakage"[Title/Abstract]) AND ("clinical prediction model"[Title/Abstract] OR "intensive care"[Title/Abstract]) AND ("time-zero"[Title/Abstract] OR "observation window"[Title/Abstract])

# 3. TRIPOD+AI-era replications (2024→present)
("TRIPOD+AI"[Title/Abstract] OR "TRIPOD-AI"[Title/Abstract]) AND ("external validation"[Title/Abstract] OR "replication"[Title/Abstract]) AND ("MIMIC"[Title/Abstract] OR "eICU"[Title/Abstract] OR "AmsterdamUMCdb"[Title/Abstract])

# 4. Calibration drift on external validation
("calibration slope"[Title/Abstract] OR "calibration hierarchy"[Title/Abstract] OR "calibration drift"[Title/Abstract]) AND ("external validation"[Title/Abstract] OR "transportability"[Title/Abstract]) AND ("intensive care"[Title/Abstract] OR "MIMIC"[Title/Abstract])
```

```open-web
# 5. YAIB/METRE/ricu next releases — inspect for Harutyunyan frozen-model replication before submission
# Inspect: YAIB GitHub (github.com/rvandewater/YAIB) releases + ricu vignettes + YerevaNN/mimic3-benchmarks issues/Discussions
# 6. Preprint sweep (arXiv+medRxiv 2024–2026): Harutyunyan MIMIC eICU replication TRIPOD calibration subgroup
```

---

## Appendix — Queries & Papers (verbatim for search_log.csv / evidence_registry.csv)

**Queries run (verbatim, 8 required — Cycle 4 T8 packet distinct strategies):**

| date | cycle | agent | source | query | concept | hits | n_inspected | verification |
|------|-------|-------|--------|-------|---------|------|-------------|--------------|
| 2026-08-30 | 4 | methods-scout | web_search | `Harutyunyan MIMIC benchmark direct replication external validation pre-registration OSF` | T8-C4-StrategyA-replication | 5 | 5 | VERIFIED — no Harutyunyan→eICU pre-registered replication located |
| 2026-08-30 | 4 | methods-scout | web_search | `ICU prediction data leakage time-zero lookahead calibration slope decision curve leakage checklist` | T8-C4-StrategyB-leakage-calibration | 5 | 5 | VERIFIED — leakage/calibration distinct terminology, sparse EHR checklist |
| 2026-08-30 | 4 | methods-scout | web_search | `McDermott Nagendran TRIPOD AI Collins Van Calster Riley calibration systematic review` | T8-C4-review-TRIPOD-calib | 5 | 5 | VERIFIED — 5 reviews verified (McDermott/Nagendran/TRIPOD+AI/Van Calster/Riley) |
| 2026-08-30 | 4 | methods-scout | web_search | `many analysts researcher degrees freedom feature drift Nestor non-stationary health records` | T8-C4-adjacent-many-analysts-drift | 5 | 5 | VERIFIED — many-analysts + feature drift adjacent |
| 2026-08-30 | 4 | methods-scout | web_search | `Harutyunyan 2019 multitask LSTM eICU AmsterdamUMCdb exact replication TRIPOD` | T8-C4-adversarial-exact-replication | 5 | 5 | VERIFIED — gap survives |
| 2026-08-30 | 4 | methods-scout | web_search | `METRE ricu YAIB harmonization MIMIC eICU AmsterdamUMCdb HiRID` | T8-C4-chaining-harmonization | 5 | 5 | VERIFIED — chaining verified |
| 2026-08-30 | 4 | methods-scout | web_search | `clinical prediction model temporal leakage lookahead time-zero EHR calibration` | T8-C4-leakage-deep | 5 | 5 | VERIFIED — deep leakage terminology |
| 2026-08-30 | 4 | methods-scout | web_search | `Van Calster calibration hierarchy Riley prediction interval TRIPOD AI 2024` | T8-C4-calibration-chain | 5 | 5 | VERIFIED — calibration chain |
| 2026-08-30 | 3 | methods-scout | web_search | `Harutyunyan MIMIC-III benchmark replication eICU AmsterdamUMCdb external validation` | T8-adversarial-Harutyunyan | 5 | 5 | VERIFIED — carry-forward |
| 2026-08-30 | 3 | methods-scout | web_search | `Rajkomar deep learning EHR replication independent validation FHIR` | T8-adversarial-Rajkomar | 5 | 5 | VERIFIED — no FHIR replication |
| 2026-08-30 | 3 | methods-scout | web_search | `PhysioNet 2019 sepsis prediction external validation MIMIC eICU replication` | T8-adversarial-sepsis | 5 | 5 | VERIFIED — task-level only |
| 2026-08-30 | 3 | methods-scout | web_search | `feature robustness non-stationary health records Nestor external validation failure` | T8-adjacent-Nestor | 5 | 5 | VERIFIED — mechanism study |

**Papers (10, resolvable, ≥1 DOI 302-verified):**

| # | Citation | DOI / URL | Type | Verification | Role |
|---|----------|-----------|------|--------------|------|
| 1 | Harutyunyan et al. Multitask learning and benchmarking with clinical time series data. Sci Data 2019;6:96. | https://doi.org/10.1038/s41597-019-0103-9 | article flagship | **302 HEAD 2026-08-30 → nature.com/articles/s41597-019-0103-9** | Target flagship |
| 2 | Collins et al. TRIPOD+AI statement. BMJ 2024;385:e078378. | https://doi.org/10.1136/bmj-2023-078378 | guideline 27-item | **302 → bmj.com/lookup/doi/10.1136/bmj-2023-078378** | Load-bearing reporting |
| 3 | McDermott et al. Reproducibility in ML for health. Sci Transl Med 2021;13:eabb1655. | https://doi.org/10.1126/scitranslmed.abb1655 | review 511 papers | **302 → science.org/doi/10.1126/scitranslmed.abb1655** | Load-bearing review |
| 4 | Nagendran et al. AI vs clinicians systematic review. BMJ 2020;368:m689. | https://doi.org/10.1136/bmj.m689 | review 81 studies | **302 → bmj.com/lookup/doi/10.1136/bmj.m689** | Claim-fragility |
| 5 | Nestor et al. Feature robustness in non-stationary records. MLHC PMLR 2019;106:381-405. | https://doi.org/10.48550/arXiv.1908.00690 | conference | **302 → arxiv.org/abs/1908.00690** | Drift mechanism |
| 6 | Van Calster et al. Calibration hierarchy. J Clin Epidemiol 2016;74:167-176. | https://doi.org/10.1016/j.jclinepi.2015.12.005 | article | **302 → linkinghub.elsevier.com/retrieve/pii/S0895435615005818** | Calibration vocab |
| 7 | Riley et al. Uncertainty of risk estimates. BMJ 2025;388:e080749. | https://doi.org/10.1136/bmj-2024-080749 | article | **302 → bmj.com/lookup/doi/10.1136/bmj-2024-080749** | Intervals/equivalence |
| 8 | Collins et al. TRIPOD Statement. BMJ 2015;350:g7594. | https://doi.org/10.1136/bmj.g7594 | guideline 22-item | 302 expected (BMJ) | Lineage anchor |
| 9 | Bennett et al. ricu R interface. PMC10268223 2023. | https://pmc.ncbi.nlm.nih.gov/articles/PMC10268223 (CRAN: ricu) | software | PMC resolvable | Harmonization pipeline |
| 10 | Moor/Yèche et al. YAIB. arXiv:2208.06691 2023. | https://doi.org/10.48550/arXiv.2208.06691 | preprint | **302 → arxiv.org/abs/2208.06691** | Closest corpus/defeater |

**DOI 302 log (2026-08-30, curl -I https://doi.org/<DOI> → 302):**

```
10.1038/s41597-019-0103-9            302 -> https://www.nature.com/articles/s41597-019-0103-9
10.1136/bmj-2023-078378              302 -> https://www.bmj.com/lookup/doi/10.1136/bmj-2023-078378
10.1126/scitranslmed.abb1655         302 -> https://www.science.org/doi/10.1126/scitranslmed.abb1655
10.1136/bmj.m689                     302 -> https://www.bmj.com/lookup/doi/10.1136/bmj.m689
10.48550/arXiv.1908.00690            302 -> https://arxiv.org/abs/1908.00690
10.1016/j.jclinepi.2015.12.005       302 -> https://linkinghub.elsevier.com/retrieve/pii/S0895435615005818
10.1136/bmj-2024-080749              302 -> https://www.bmj.com/lookup/doi/10.1136/bmj-2024-080749
10.48550/arXiv.2208.06691            302 -> https://arxiv.org/abs/2208.06691
```

**Verification:** 7/10 DOIs HEAD-checked 302 on 30 Aug 2026 + TRIPOD 2015 verified in Cycle 3; cross-check evidence_registry rows T8-C4-001..010. [UNVERIFIED] not used for load-bearing claims. ≥1 model DOI 302: YES (Harutyunyan 10.1038/s41597-019-0103-9 + TRIPOD+AI 10.1136/bmj-2023-078378).

**Named data:** MIMIC-III v1.4 / MIMIC-IV v2.2 + eICU-CRD v2.0 + AmsterdamUMCdb v1.0.2 (HiRID secondary) — all A public credentialed, weeks.
**Mandatory baselines:** LR (L2/Platt) + SOFA/APACHE + GBM/XGBoost + trivial prevalence (RF optional).
**OSF mapping:** 27-item TRIPOD+AI mapped §7h of lock; leakage checklist 6 items; harmonization stub table with 7 domains pre-registered.
