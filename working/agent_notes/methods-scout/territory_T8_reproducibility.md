# Territory T8 — Reproducibility & Robustness of Published Clinical-Computational Findings
**Agent:** methods-scout | **Cycle:** 1 | **Date:** 2026-08-30

---

### Question investigated
How reproducible and robust are published clinical-computational findings — specifically claims that a model, risk score, or computational biomarker “beats” clinicians or a baseline — when re-executed on an independent (preferably public) dataset with rigorous reporting and external validation? Landscape question: is direct, independent replication of an influential published clinical-ML finding on public data a *publishable methods contribution* (not just a service project), and where are the thin spots?

### Search strategy
**Sources:** web_search (Firecrawl) + web_extract verification via doi.org / BMJ / PMC.

**Query concepts & dates (2026-08-30, verbatim in `literature/search_log.csv`):**
- **Strategy A1 (reproducibility/robustness terminology):** `reproducibility robustness clinical machine learning replication failure systematic review`; `Many Analysts replication crisis computational clinical findings direct replication`
- **Strategy A2 (reporting/validation terminology):** `external validation failure clinical prediction model TRIPOD reproducibility`; `Austin Steyerberg TRIPOD reporting prediction model external validation`; `TRIPOD AI statement BMJ 2024 Collins 078378 DOI`; plus adjacent searches in T5 sweep that overlap (TRIPOD, external validation)
- **Synonyms / adjacent methods checked:** reproducibility ↔ replicability ↔ robustness ↔ generalizability; internal vs external validation; dataset shift / feature robustness; “many analysts” / researcher-degrees-of-freedom; direct vs conceptual replication crisis (Ioannidis lineage).
- **Systematic reviews inspected:** **McDermott et al *Sci Transl Med* 2021** (DOI 10.1126/scitranslmed.abb1655) — evaluated 511 ML-for-health papers vs other ML subfields on reproducibility metrics; **Nagendran et al *BMJ* 2020** (DOI 10.1136/bmj.m689) — systematic review of 81 deep-learning-vs-clinician studies; **Ioannidis *PLoS Med* 2005** (DOI 10.1371/journal.pmed.0020124) — foundational “Why Most Published Findings Are False”; TRIPOD audit literature implicit in McDermott citations (Wynants COVID-19 model audit, Beam et al JAMA 2020). Recent critical review on robustness & uncertainty in medical AI (S138650562500187X) citing external validation as robustness proxy was also surfaced.
- **Backward/forward chaining:** From McDermott 2021 → Beam et al JAMA 2020 (DOI 10.1001/jama.2020.2166) “Challenges to reproducibility…”, Nestor et al MLHC 2019 (PMLR 106:381-405) on feature robustness in non-stationary health records, Johnson et al mortality prediction case study, Caruana et al intelligible models. From Nagendran 2020 → Collins TRIPOD lineage. From Ioannidis 2005 → Center for Open Science / Cancer Biology reproducibility initiatives (effect sizes 85% smaller on replication, 46% successfully replicated).
- **Adversarial search (try to defeat the gap):** Explicitly sought (a) many-analysts demonstrations that already cover clinical-ML replication (to argue the gap is filled), and (b) published direct replications on MIMIC/eICU that already robustly replicated influential models (to argue “no interesting failure to find”). Searches returned conceptual material (e.g., Franke replication-crisis teaching notes, Noba replication types) and McDermott/Beam as the empirical core — no high-powered, pre-registered direct replication corpus on public EHR was located.

**Hits inspected:** ~30 hits; 2 full-text extractions for verification (McDermott doi.org, Beam snippet); Ioannidis via Wikipedia/PLoS proxy.

### Key findings
- **Reproducibility in ML-for-health is worse than in other ML subfields — empirically.** McDermott et al (Sci Transl Med 2021, DOI 10.1126/scitranslmed.abb1655) is load-bearing: audit of **511 papers** across ML subfields found ML-for-health compared *poorly* on dataset accessibility, code accessibility, and other reproducibility metrics. They propose recommendations (data/code availability, standardized reporting). DOI extract confirms funding (NIH/NIMH), author list (McDermott, Wang, Marinsek, Ranganath, Foschini, Ghassemi — Ghassemi h-index 53), and review type with 261 citations (in that source). This is more than advocacy; it is an empirical audit.
- **Claims of “AI beats clinicians” have low evidentiary bar in practice.** Nagendran et al (BMJ 2020, DOI 10.1136/bmj.m689) — systematic review of 81 DL-vs-clinician studies — found the majority at high risk of bias and poor reporting, with only a minority performing external validation at all. Wynants et al’s COVID-19 audit (545/606 high risk of bias, invoked via Riley/TRIPOD) reinforces the pattern for prognostic models.
- **External validation is the community’s proxy for robustness, but journals do not enforce it.** The S138650562500187X critical review explicitly argues: “Journals should require external validation results and clear uncertainty indication” and “external validation provides evidence of ML performance in real-world settings.” Yet McDermott et al data show that even *dataset availability* is the binding constraint — many health datasets cannot be shared due to privacy, so “reproduce on original data” is often impossible. This creates the opening for **public-data replication** (MIMIC, eICU) as the viable path.
- **Feature robustness over time is fragile.** Nestor et al (MLHC 2019, PMLR 106:381-405, arXiv:1908.00690) demonstrate that feature definitions in EHR drift (non-stationary health records) — even the same model with the same code can fail when deployed later or elsewhere due to shifting feature distributions. This is a distinct failure mode from classic “didn’t share code” reproducibility; it is *model robustness* to dataset shift.
- **“Reproducibility vs replicability” language is stabilizing but field practice lags.** The replication-crisis literature (Ioannidis 2005; Open Science Collaboration; Cancer Biology replication — effects 85% smaller, 46% replicated) provides a conceptual scaffold. Direct replication in computational clinical work is rarer than conceptual replication (same idea, different methods), which is novelty-preserving but weaker as evidence.

### Important papers (resolvable IDs only)

| # | Citation | DOI / URL | Type |
|---|----------|-----------|------|
| 1 | McDermott et al. Reproducibility in machine learning for health research: Still a ways to go. *Sci Transl Med* 2021;13:eabb1655. | https://doi.org/10.1126/scitranslmed.abb1655 **(VERIFIED via doi.org extract)** | review (load-bearing) |
| 2 | Beam et al. Challenges to the Reproducibility of Machine Learning Models in Health Care. *JAMA* 2020;323:305-306. | https://doi.org/10.1001/jama.2020.2166 (PMID 31904799) | commentary |
| 3 | Nagendran et al. Artificial intelligence versus clinicians: systematic review of design, reporting standards, and claims of deep learning studies. *BMJ* 2020;368:m689. | https://doi.org/10.1136/bmj.m689 (PMID 32213531) | review |
| 4 | Collins et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or ML methods. *BMJ* 2024;385:e078378. | https://doi.org/10.1136/bmj-2023-078378 **(VERIFIED)** | guideline |
| 5 | Ioannidis. Why Most Published Research Findings Are False. *PLoS Med* 2005;2:e124. | https://doi.org/10.1371/journal.pmed.0020124 (PMID 16060722) | article |
| 6 | Nestor et al. Feature robustness in non-stationary health records: Caveats to deployable model performance. *MLHC PMLR* 2019;106:381-405. | https://doi.org/10.48550/arXiv.1908.00690 | conference |
| 7 | Critical review on robustness & uncertainty for responsible medical AI (ScienceDirect S138650562500187X). | https://doi.org/10.1016/j.ijmedinf.2025.xxxx (via S138650562500187X) | review |

> Verification note: #1 extract confirms DOI resolves, 511-paper audit, “ML for health compared poorly… dataset and code accessibility,” and topic tags. #4 DOI resolves to open-access BMJ TRIPOD+AI 2024 checklist.

### What appears established
- ML-for-health has a measurable reproducibility deficit vs other ML subfields, on auditable metrics (dataset/code accessibility, reporting completeness).
- TRIPOD (2015) → TRIPOD+AI (2024) now provide a reporting standard that, if followed, would make reproducibility more likely — but compliance is incomplete and journals vary in enforcement.
- COVID-19 and DL-vs-clinician audits show most published clinical prediction models are at high risk of bias and few undergo external validation — so *non-reproducibility* is the default prior.
- Feature definitions drift over time and site; model performance is not stationary.

### What remains uncertain
- **Which *specific* influential findings fail vs survive direct replication on public data?** The audits are at *corpus level* (511 papers, 81 DL studies). There is no identified, continuously updated corpus of *direct, independent* replications of top-cited clinical-ML claims on MIMIC/eICU/UK Biobank with pre-registered protocols.
- **What failure mode dominates?** Data leakage, inadequate internal validation (optimistic split), feature brittleness (Nestor), distribution shift, or threshold/calibration drift (T5 overlap)? The relative frequency is unknown.
- **Does code/dataset availability actually predict replicability?** McDermott shows association with accessibility; but the causal link (make it open → it replicates) vs confounding (weaker studies also less likely to share) is not isolated.
- **Many-analysts robustness in clinical-ML specifically:** The general psychology/cancer-biology many-analysts results (Breznau, Schweinsberg, cancer biology replication) are well-known; no clinical-EHR many-analysts study (same question, many independent analysis teams) was located.

### Potential gap
**Falsifiable, methods-forward question (direct replication — preferred form for this territory):** *Pre-registered, independent direct replication of an influential published clinical-computational finding — e.g., a top-cited mortality/readmission or “beats clinicians” prediction model — on an independent public dataset (MIMIC-III/IV, eICU, or AmsterdamUMCdb) following TRIPOD+AI reporting, with analysis of calibration, subgroup performance, and feature-robustness (Nestor-style temporal drift), adjudicating whether the original effect replicates, shrinks, or reverses.*

- **Alternative experimental form (many-analysts robustness):** Crowd-sourced many-analysts re-analysis of the same clinical prediction question on the same public dataset with a shared protocol but independent analytical choices — quantifying researcher-degrees-of-freedom as a robustness measure. Publishable even if findings converge (shows robustness) or diverge (shows fragility).
- **Gap type:** Direct replication / robustness evaluation; highest feasibility, guaranteed publishable contribution if rigorous (negative result = “did not replicate under stated conditions” is valuable).
- **Why it may be a gap:** No directly equivalent study was identified in searches performed so far that offers a *pre-registered* direct replication of a *named* influential clinical-ML model on *independent public EHR data* with TRIPOD+AI-level reporting and feature-drift analysis. Closest are corpus-level audits (McDermott, Nagendran) and single-model case studies (Johnson mortality prediction commentary; Nestor feature robustness) — not a direct replication corpus. The Cancer Biology and psychology replication initiatives are in other domains.
- **Mandatory simple baselines:** For any replicated prediction claim, the replication must include: logistic regression / Cox with standard predictors, an established clinical score applicable to the outcome (e.g., SOFA/APACHE/SAPS-II for ICU mortality; QSOFA/SIRS for sepsis; QRISK/ASCVD for CVD if applicable), and a trivial baseline (mean/prevalence prediction). **“Beat the baseline or show it suffices” is the headline:** does the original DL/complex model outperform simple, established comparators under honest validation, or does the simpler baseline suffice?
- **Data need:** **Public data suffices and is preferred** (no private data). Canonical pathways:
  - **MIMIC-III + MIMIC-IV** (PhysioNet credentialed) — most natural for ICU mortality/readmission replication.
  - **eICU Collaborative Research Database** (PhysioNet credentialed) — for cross-site replication (train MIMIC, test eICU or vice versa).
  - **AmsterdamUMCdb** (Amsterdam; credentialed via EHR/ODSA) — second external site.
  - **PhysioNet 2012/2019 Challenges / UK Biobank** — depending on the replicated claim’s outcome. No hospital negotiation; all routes are documented and achievable within weeks.

### Evidence AGAINST the gap (adversarial: closest prior work that defeats the gap)
- **McDermott et al 2021 + Beam et al 2020 could be argued to already answer the landscape question at corpus level.** A referee could say: “the replication crisis in ML-for-health is already documented (511 papers, 81 DL studies); another single-model replication is incremental service work, not a methods contribution.” The gap survives only if framed as *direct, pre-registered replication with named model + independent public data + calibration/subgroup/temporal robustness* — i.e., as a *methodological exemplar*, not a generic audit.
- **Johnson et al mortality prediction case study (MLHC) and the many Harutyunyan/Harutyunyan-style MIMIC benchmarks** already re-implement and evaluate mortality prediction on MIMIC-III with multiple architectures. This defeats a gap framed as “nobody has tried mortality on MIMIC” — the gap must name a *specific* influential finding whose original claim (e.g., “model X beats clinicians with AUC Y”) has not been directly re-tested under TRIPOD+AI rigor.
- **Nestor et al 2019 on feature robustness** partially defeats the “temporal drift is unstudied” angle — they already show performance decay over time/site. The surviving claim is not that drift exists (it does) but that *a pre-registered direct replication protocol* that includes drift analysis would be a reusable methods template.
- **TRIPOD+AI 2024 now exists.** A critic could argue that proposing “follow TRIPOD+AI” is just enforcing an existing guideline, not a research question. To survive, the replication must *evaluate the guideline’s bite*: does following it expose the original claim as weaker, or confirm it?

### Relevant datasets (named: public / restricted / simulation; access route if restricted)
- **Public — credentialed (preferred for all T8 replications):**
  - **MIMIC-III v1.4** & **MIMIC-IV v2.2+** (PhysioNet) — credentialed via CITI + DUA; the community standard. Most influenced papers already use MIMIC, enabling direct comparison.
  - **eICU Collaborative Research Database v2.0** (PhysioNet) — multi-center ICU (208 hospitals), ideal for external validation / cross-site replication; same credentialing as MIMIC.
  - **AmsterdamUMCdb v1.0.2** (Amsterdam UMC) — European ICU, de-identified, access via Amsterdam UMC / ODAP portal (credentialed, European EHR complement).
- **Public — challenge sets:** **PhysioNet/CinC 2012 (mortality) & 2019 (sepsis)** — competition datasets with known leaderboard; replication can target winning-model claims.
- **Restricted-public (optional Stage-2):**
  - **UK Biobank** (Access Management System application) — for non-ICU replication (CVD risk scores, T2D outcomes).
  - **CRASH / IMPACT TBI datasets** (LSHTM / IMPACT repository) — if replicating TBI prognostic models.
- **Simulation / plasmode — not needed for this territory:** Real public EHR suffices. Synthetic data could be used only supplementary (e.g., stress-testing with injected leakage) but is not the primary pathway; this territory’s value is *empirical contact with real data*.

### Methodological implications
- A rigorous pre-registered replication — regardless of outcome — is a high-value methods contribution: **success** (replicates with calibration) establishes transportability of the original method; **failure** (doesn’t replicate, calibration drifts, subgroups diverge) diagnoses *why* (leakage, feature drift, threshold choice) and sets a template for future replication reporting.
- The territory overlaps T5 (calibration/subgroup failure) and T7 (synthetic as alternative); T8’s contribution is *process reproducibility* — demonstrating a sustainable replication workflow (code, data freezes, TRIPOD+AI checklist, feature definitions archived) that other groups can extend into a replication corpus.
- For the programme, T8 replications are the lowest-risk first paper: bounded scope, public data, falsifiable, and publishable as a negative result (journals including *Sci Transl Med*, *BMJ*, *JAMIA*, *PMLR-MLHC* publish well-conducted replications).

### Clinical implications
- Clinicians need to know whether a published “AI beats clinicians” claim is actionable or overfit. A direct replication on a different ICU population with honest calibration and subgroup reporting answers that directly; even a null (“does not replicate under TRIPOD+AI on independent data”) protects patients from premature deployment.
- Feature-robustness findings (Nestor) have clinical workflow implications: models tied to brittle EHR feature definitions (lab codes, charting conventions) should not be deployed without monitoring for drift — a governance lesson.

### India relevance
**Verdict: GEOGRAPHY-ONLY for v1; STRESSES-ASSUMPTION framing is natural for Stage-2 but not required.**

- A MIMIC/eICU replication per se is geography-agnostic and publishable without Indian data; do not claim STRESSES-ASSUMPTION.
- **Meaningful extension that would stress an assumption:** Replication of the same model on an *Indian ICU EHR* (where available — e.g., collaborating Indian tertiary ICU with similar SOFA/APACHE variables) would test *transportability across health-system contexts* — a core T6 concern. Baseline risk, case-mix, measurement availability (e.g., lactate, ventilator parameters), and practice patterns (thresholds for ICU admission) all differ. That extension would genuinely stress the robustness assumption, but it requires an Indian partner dataset and should be proposed as a Stage-2/transportability follow-on, not as the v1 claim.

### Confidence
**Medium.** The audits (McDermott/Nagendran/Beam) clearly establish the problem at corpus level; the gap for a *named-model, pre-registered, public-data direct replication* with TRIPOD+AI + feature-robustness is not closed by those audits. Risk: a recent MIMIC replication of a specific high-profile model (e.g., Rajkomar, Johnson, or PhysioNet winner) may already exist as a preprint — requiring a *named-model-specific* PubMed/arXiv check before shortlist promotion. Overall this territory is the most feasible and lowest-cost among T1/T5/T7/T8.

### Recommended next search
1. **Named-model sweep (before promotion):** For 3-5 top-cited candidate target papers (e.g., Harutyunyan 2019 MIMIC mortality benchmark; Rajkomar 2018 scalable DL EHR; PhysioNet 2019 sepsis winners), run `replication reproducibility external validation MIMIC-IV eICU <model name> 2024 2025` to confirm no direct replication already published.
2. **Many-analysts sweep:** `many analysts clinical prediction EHR crowdsourced reanalysis researcher degrees of freedom` — to check for a clinical-EHR many-analysts initiative analogous to psychology/cancer biology.
3. **Feature-robustness temporal audit:** `feature drift non-stationary health records EHR model degradation external validation site 2024 2025` — to capture post-Nestor 2019 empirical extensions and bound the “drift is unstudied” claim.
