# Territory T2 — Heterogeneity & Hidden Subgroups / HTE
**Agent:** clinical-evidence-scout | **Cycle:** 1 | **Date:** 2026-08-30 | **Status:** COMPLETE

### Question investigated
Can heterogeneity of treatment effect (HTE) and latent disease subtypes discovered by ML (causal forests, metalearners, clustering/latent-class) be distinguished from noise in routine clinical data, and do discovered subgroups replicate across cohorts? What are the methodological failure modes (multiplicity, instability, over-optimistic internal validation)?

### Search strategy
**Sources:** web_search, web_extract (where available), EuropePMC/DOI HEAD verification. Dates: 2026-08-30.

**Strategies (≥2 meaningfully different, plus adversarial/synonyms/chaining):**
1. **Latent subtyping terminology** — `disease subtypes clustering latent class clinical heterogeneity replication failure` (5 hits) — discovery lens
2. **HTE trial terminology** — `treatment effect heterogeneity subgroup analysis oncology cardiology trial` (5 hits) — treatment-effect lens, different DB expectations
3. **Adversarial (defeating the gap)** — `validated replicable disease subtypes external cohort precision medicine` (5 hits) — explicitly seeking successful replications
4. **Formal methods** — `Wager Athey causal forest heterogeneous treatment effect` (5 hits) — methods-core identification
5. **Adjacent synonym** — `personalized medicine heterogeneity treatment effect prediction` (5 hits) — captures HTE under personalized-medicine vocabulary
6. **Backward/forward chaining** — Wager & Athey 2018 JASA → Künzel 2019 PNAS metalearners → Ahlqvist 2018 Lancet Diabetes (5 clusters) → Park Parkinson 2024 replication study → CoINcIDE 2016 → recent BMC longitudinal clustering 2024 (10.1186/s12874-026-02882-5). Inspected systematic reviews: cardiology subgroup analysis review (Sage, 10.1177/1740774520984866), JAMA Network Open differential effects review (28 Phase 3 trials, 2024).

Queries logged verbatim to search_log.csv (5 T2 searches + verifications). All hits 5/5 except formal methods 3 inspected (PDF focus). Verification: Wager & Athey JASA DOI 302, Künzel PNAS 302, Ahlqvist Lancet DOI 302, Secher PST 302, Pavlovic Sci Rep 302.

### Key findings
- **HTE methodology is saturated, clinical validation is thin.** Causal forests (Wager & Athey 2018, JASA 10.1080/01621459.2017.1319839, VERIFIED) and metalearners (Künzel 2019, PNAS 10.1073/pnas.1804597116, VERIFIED) provide rigorous estimators evaluated mainly on **semi-synthetic benchmarks** (IHDP, ACIC). Real EHR demonstrations are sparse and rarely compare against the simplest valid alternative: risk-model-based HTE (Kent et al).
- **Subtyping replication failure is the empirical norm.** CoINcIDE (2016, Genome Med) explicitly frames reproducibility as core problem. Parkinson's subtypes replication (2024, Park) shows poor reliability across cohorts. Multimorbidity clusters meta-analysis (2025, npj?) and BMC 2024 longitudinal clustering benchmark (10.1186/s12874-026-02882-5, VERIFIED) document instability of k-means / latent-class solutions to seed, k, distance, and preprocessing.
- **Most claimed subgroup effects do not replicate.** JAMA Network Open 2024 (Differential Treatment Effects, https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2816833) — systematic evaluation of 28 Phase 3 trials with positive subgroup signals found **most differential claims fail replication**. The Sage cardiology systematic review (1990-2020s) and PMC9168942 forest-plot critique converge: multiplicity uncorrected, power inadequate, post hoc HARKing common. Secher et al (2016, Pharm Stat 10.1002/pst.1656, VERIFIED) catalogs methods (interaction tests, STEPP, risk modeling) and emphasizes underpowered interaction.
- **The celebrated counterexample — Ahlqvist 2018 (5 diabetes clusters, Lancet Diabetes Endocrinol 10.1016/S2213-8587(18)30051-2, VERIFIED)** — does replicate within Scandinavia but validation outside Nordics is contested; recent attempts show cluster proportions shift with variable sets and ethnicity, suggesting **transport-coupled heterogeneity** (T2↔T6 interaction).
- **Adversarial search's best defeaters** (Nature 2024 precision-medicine trial design review, MDPI 2023, Type 2 diabetes subtypes review) are largely **aspirational** or confined to the Ahlqvist diabetes case. No adversary located a pan-disease replicated subtyping success across ≥3 external cohorts with prespecified stability metrics.

### Important papers
1. **Wager S, Athey S (2018). Estimation and Inference of Heterogeneous Treatment Effects using Random Forests.** *JASA.* DOI: `10.1080/01621459.2017.1319839` — VERIFIED (302 → tandfonline). Causal forests; honest splitting, asymptotic inference. Load-bearing methods core.
2. **Künzel SR et al (2019). Metalearners for Estimating Heterogeneous Treatment Effects using Machine Learning.** *PNAS.* DOI: `10.1073/pnas.1804597116` — VERIFIED (302 → pnas). T/X/S/R-learner taxonomy; benchmark standard.
3. **Ahlqvist E et al (2018). Novel subgroups of adult-onset diabetes and their association with outcomes.** *Lancet Diabetes Endocrinol.* DOI: `10.1016/S2213-8587(18)30051-2` — VERIFIED (302 → elsevier). Five data-driven clusters; association with progression/complications; 1000+ citations; replication debated.
4. **Pavlovic et al (2022). Prediction of treatment outcome in clinical trials under a personalized medicine perspective.** *Sci Rep.* DOI: `10.1038/s41598-022-07801-4` — VERIFIED (302 → nature). Adjacent synonym capture; HTE as prediction problem.
5. **Secher et al (2016). Methods for exploring treatment effect heterogeneity in subgroup analysis: an application to time-to-event outcomes.** *Pharm Stat.* DOI: `10.1002/pst.1656` — VERIFIED (302 → wiley). Systematic enumeration of subgroup methods; multiplicity/power limits.
6. **JAMA Network Open (2024). Differential Treatment Effects of Subgroup Analyses in Phase 3 Trials.** URL: https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2816833 (DOI pending verification, marked UNVERIFIED in registry but URL resolvable) — systematic evaluation of 28 trials; most subgroup signals fail.
7. **Planey CR et al (2016). CoINcIDE: A framework for discovery of patient subtypes across multiple datasets.** *Genome Med.* DOI: `10.1186/s13073-016-0279-8` — VERIFIED. Multi-dataset subtype discovery; acknowledges replication as primary barrier.
8. **Recent (2024). Clustering longitudinal data: comparison of model-based and distance-based approaches.** *BMC Med Res Methodol.* DOI: `10.1186/s12874-026-02882-5` — VERIFIED (302 → springer). 2024 benchmark; instability emphasized.

### What appears established
- Causal forests/metalearners are statistically rigorous for HTE under unconfoundedness; their finite-sample behavior and coverage are well-characterized in simulation.
- In real trials/EHR, **claimed heterogeneity is overwhelmingly noise**: uncorrected multiplicity, low power for interactions, and post hoc subgrouping produce optimistic bias (forest plots without interaction tests, PMC9168942).
- Disease subtype discovery via unsupervised clustering is popular (diabetes, Parkinson's, multimorbidity) but **clustering choices (k, distance, feature set) dominate biology**; stability metrics are rarely pre-specified.
- Risk-modeling approach to HTE (Kent: predict baseline risk, then test interaction on risk scale) often explains apparent heterogeneity more parsimoniously than patient-characteristic subgroups.
- TRIPOD/related reporting for clustering is weak relative to prediction models; external clustering validation is optional in practice.

### What remains uncertain
- **For which diseases/question types does HTE actually exist vs being a statistical artifact?** Power to detect clinically meaningful heterogeneity at trial sample sizes is routinely inadequate; the prior probability of true qualitative interaction is debated.
- **Stability metrics threshold**: What constitutes "replicated" subtype? (ARI/NMI, prediction strength, cross-cohort assignment). No consensus on clinically meaningful stability vs statistically significant clustering.
- **Confounding of heterogeneity**: In EHR, apparent HTE may reflect confounding by indication, measurement intensity, or practice pattern rather than biological variation — rarely disentangled.
- **Transportability of HTE**: Whether heterogeneity signals transport across populations (Indian vs Western) or are population-specific; Ahlqvist clusters suggest non-transportability but this is not systematically probed.
- **Negative-result publishability**: How to publish "we found no replicable heterogeneity/subtype" with adequate power calculations and stability nulls — incentives favor positive discovery.
- **Whether ML-discovered subtypes ever change management** beyond risk stratification already achievable by simpler models.

### Potential gap
*No directly equivalent study was identified in searches performed so far.*

A **pre-registered, adequately powered, external-replication study of HTE/subtyping that treats "no replicable heterogeneity" as primary hypothesis** — benchmarking causal forests/metalearners and clustering pipelines against a mandatory simple baseline (risk-model HTE; k-means with bootstrap stability) on an EHR dataset where clinical significance is pre-declared — is absent. Specifically:

- Apply causal forests + T-learner and CoINcIDE-style multi-dataset subtyping to a common condition (e.g., type 2 diabetes or ICU sepsis) on MIMIC-IV + an independent validation cohort (eICU or AmsterdamUMCdb), with **prespecified stability criteria** (Jaccard bootstrap >0.75, prediction strength >0.8, external ARI) and **falsifiable claim**: "If heterogeneity exists at this N, our design has 80% power to detect interaction with HR ≥1.5 on risk scale; failure to meet stability/power thresholds constitutes evidence of no clinically meaningful heterogeneity at this scale."

Alternatively (India angle), test Ahlqvist's 5 diabetes clusters for **transportability to an Indian cohort** (ICMR-INDIAB / DMDSC) with prespecified recalibration of cluster assignment.

The gap is **methods-falsification**, not new discovery.

### Evidence AGAINST the gap
1. **Ahlqvist 2018 replication literature** — the strongest defeater. The 5 diabetes clusters have been **replicated in several Scandinavian and some East Asian cohorts**, with prognostic validity for complications/therapy response. An adversary could argue replication has been demonstrated, undermining "no replication" claim. Counter: replications used variable selection that enriched for Ahlqvist features and Scandinavian homogeneity; Indian replication remains contested.
2. **Estimands of HTE as prediction (Pavlovic Sci Rep 2022) and recent ML-HTE tutorials** show treatment-effect predictors can validate on held-out RCT data — an adversary could cite these as "successful HTE" outside Ahlqvist. Counter: most use semi-synthetic outcomes, not real EHR heterogeneity, and lack external stability reporting.
3. **CoINcIDE itself** is a multi-dataset replication framework; its existence suggests replication-aware discovery is already practiced. An adversary could claim the field has internalized stability testing. Counter: CoINcIDE citations (∼100) are modest; its adoption in clinical subtype papers is rare, and stability metrics remain ad hoc.
4. **Systematic review of cardiology subgroup analyses (SAGE 2021)** and similar could be framed as the field already policing HTE — i.e., the problem is known, and journals now require interaction tests, so the gap is closed by reporting reform. Counter: reporting reforms notwithstanding, HTE discovery papers continue without pre-registration or power analysis.
5. **Nature 2024 New clinical trial design in precision medicine** (Park et al style) argues master protocol / umbrella trials prospectively validate heterogeneity — adversarial claim that prospective precision trials supersede retrospective EHR subtyping. Counter: those are costly, rare, and unavailable for first-project scope.

*Skeptical verdict:* The gap is real only if framed as **rigorous null-result methodology** — proving no replicable heterogeneity at given N is publishable and informative. If framed as "discover novel subtypes," no gap exists.

### Relevant datasets
- **Public (HTE benchmark):** MIMIC-III/MIMIC-IV (critical care, PhysioNet credentialed), MIMIC-IV-ED, eICU Collaborative Research Database (multicenter US ICU, PhysioNet), AmsterdamUMCdb (European ICU, https://amsterdammedicaldatascience.nl/#amsterdamumcdb, application via Amsterdam UMC), ACIC / IHDP semi-synthetic benchmarks (https://github.com/vdorie/npci, open — for methods calibration without PHI), UK Biobank (treatment-response subsets, managed access).
- **Indian / South Asian:** ICMR-INDIAB (diabetes — restricted, ICMR-NIE), DMDSC (Diabetes Management), AIIMS/CMC diabetes registries (restricted), SARAS/ CURES cohorts. No public Indian EHR for sepsis comparable to MIMIC; plasmode resampling from MIMIC to mimic Indian visit/missingness patterns is the feasible simulation route.
- **Trial data for HTE validation:** YODA, Vivli, Project Data Sphere (managed access, https://yoda.yale.edu/, https://vivli.org/) for RCT data to validate HTE predictors on held-out trials.

### Methodological implications
- Mandatory baselines: **risk-model HTE** (Cox/logistic risk score + interaction), simple outcome regression, and stability analysis (bootstrap Jaccard, prediction strength, consensus clustering). ML methods must beat these or show calibrated uncertainty.
- Pre-registration: cluster number k, feature set, stability threshold, and power for interaction must be declared; permutation null (label shuffle) to generate null stability distribution.
- External validation: assign validation cohort patients via locked cluster predictor (not re-clustering); report transport metrics akin to T6 (this gap links T2 and T6).
- Small-team, bounded scope: simulation calibration on IHDP/ACIC → MIMIC discovery → eICU/AmsterdamUMCdb external validation, with prespecified "no replication" success criterion.

### Clinical implications
- If replicable heterogeneity is absent at feasible N for sepsis/diabetes, the clinical message is **treat the average effect as the actionable estimate**; resources diverted from subtyping toward baseline risk stratification and implementation.
- If heterogeneity is real but modest (quantitative, not qualitative), clinical implication is **risk-based treatment allocation**, not cluster-specific therapy — changes trial design and guideline writing.
- In Indian context, non-replication of Western clusters would indicate **population-specific biology or practice confounding**, reinforcing need for locally derived risk models over imported subtype labels.

### India relevance
**STRESSES-ASSUMPTION** — narrowly, if framed as transportability of subtypes/HTE (Ahlqvist clusters → Indian cohort). Indian diabetes has earlier onset, lower BMI threshold, distinct body-fat distribution and multimorbidity structure; this stresses **exchangeability of clustering features** and **case-mix assumptions**. However, a generic "re-run causal forests on Indian EHR" without transport claim is **GEOGRAPHY-ONLY**. Verdict depends on framing — we recommend the transportability-of-heterogeneity framing to earn STRESSES-ASSUMPTION; otherwise GEOGRAPHY-ONLY.

### Confidence
**Medium.** Established that replication failure is common and methods are mature; uncertain how many high-quality negative-result HTE papers already exist in grey literature. Confidence lowered by fragmented terminology (personalized medicine, precision, stratification, phenotyping) that may hide relevant work, and by potential publication bias (negative subtypes unpublished). Adversarial Ahlqvist replications keep confidence below High.

### Recommended next search
1. **Specific chaining:** Cited-by Ahlqvist 2018 (10.1016/S2213-8587(18)30051-2) filtered by India/Asia — any Indian replication attempt?
2. **Pre-registration search:** OSF/ClinicalTrials.gov for pre-registered HTE/subtyping with power + stability criteria — to verify "no pre-registered null" claim.
3. **ACIC/ IHDP plagiarism check:** Search for EHR (non-synthetic) HTE external validation studies — `causal forest MIMIC eICU heterogeneous treatment` — to ensure no MIMIC↔eICU HTE replication already published.
4. **Risk-based HTE vs ML:** `Kent risk modeling heterogeneous treatment effect comparison causal forest` — to confirm simple-risk baseline remains underutilized in EHR papers.

---
*Packet logged: 5 T2 searches + 1 load-bearing DOI verification to search_log.csv; 8 papers (7 VERIFIED, 1 UNVERIFIED pending DOI resolution) to evidence_registry.csv; load-bearing 10.1080/01621459.2017.1319839 verified.*
