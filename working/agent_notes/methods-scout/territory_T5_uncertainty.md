# Territory T5 — Uncertainty Quantification & Aggregate-Statistic Failure
**Agent:** methods-scout | **Cycle:** 1 | **Date:** 2026-08-30

---

### Question investigated
Do current clinical prediction models report uncertainty in a way that is decision-relevant — and do aggregate performance summaries (mean calibration slope, overall AUC/C-statistic, average treatment effect) mask subgroup or individual-level failure, including Simpson’s-paradox-type reversals and ecological misinterpretation? Landscape question: where are the *methods-forward* gaps between single-point risk estimates and distributional/interval predictions that survive calibration scrutiny?

### Search strategy
**Sources:** web_search (Firecrawl) + web_extract verification via doi.org / BMJ / PMC.

**Query concepts & dates (2026-08-30, verbatim in `literature/search_log.csv`):**
- **Strategy A1 (UQ / calibration terminology):** `uncertainty quantification calibration prediction intervals clinical risk prediction systematic review`; `Van Calster calibration hierarchy clinical prediction model 2016`; `Riley Collins age calibration prediction intervals clinical prediction model BMJ 2025`; `Riley Collins Snell uncertainty risk estimates clinical prediction models BMJ 2025 DOI`
- **Strategy A2 (aggregate-failure terminology):** `Simpson paradox ecological fallacy clinical aggregate statistics calibration failure`; `Simpson paradox aggregate statistics clinical prediction misleading subgroup`
- **Synonyms / adjacent methods checked:** conformal prediction (`Angelopoulos Bates conformal prediction tutorial 2021 DOI`; `conformal prediction medical EHR uncertainty quantification 2024`; `conformal prediction calibration clinical prediction model systematic review 2023 2024`), prediction intervals vs confidence intervals vs credible intervals, distributional prediction, calibration slope/intercept, TRIPOD reporting (`Austin Steyerberg TRIPOD reporting prediction model external validation`; `TRIPOD AI statement BMJ 2024 Collins 078378 DOI`)
- **Systematic reviews inspected:** Riley et al BMJ 2025 (the BMJ “Rationale, challenges, and approaches” article — effectively a review/position piece on uncertainty of risk estimates); Angelopoulos & Bates (2021/2023) gentle introduction / FTML monograph on conformal prediction (methods review); Zhou et al arXiv 2505.02874 survey *Uncertainty Quantification for ML in Healthcare* (2025); TRIPOD+AI (Collins et al BMJ 2024) as reporting synthesis. For Simpson/ecological fallacy, no recent clinical-prediction-specific systematic review was located — only general/statistical expositions (e.g., Pearl R414 understanding Simpson’s paradox, Statology explainer) and scattered clinical examples.
- **Backward/forward chaining:** From Riley 2025 → Van Calster 2016 calibration hierarchy (J Clin Epidemiol, 1k+ citations), Steyerberg calibration texts, Collins TRIPOD lineage; from Angelopoulos & Bates → Lu et al skin-lesion conformal, Papangelou genomics conformal, Chen et al conformal-UNet survey; from TRIPOD+AI → fairness/uncertainty checklist items.
- **Adversarial search (try to defeat the gap):** `conformal prediction applied EHR calibration already established clinical` (explicitly sought papers showing conformal intervals already routine in clinical EHR prediction). Result: 403-limited search + fragmentary evidence that conformal is cited in reviews but not shown as standard practice.

**Hits inspected:** ~35 search hits across 9+ queries; 3 full-text extractions for verification (Riley PMC, Van Calster DOI redirect, Angelopoulos arXiv/FTML).

### Key findings
- **Point risks without uncertainty are still the norm.** Riley et al (BMJ 2025, DOI 10.1136/bmj-2024-080749, PMID 39947680, 80 citations) make the central empirical claim: most published clinical prediction models report only a point estimate of risk (e.g., QRISK3 10-year CVD, CRASH/IMPACT TBI) without the uncertainty interval around that risk. They demonstrate (Fig 5 in PMC12128882) that for nominal risk 0.2 the 95% calibration uncertainty interval can be ~0.25–0.45 in validation data — wide enough to change management. They propose bootstrap- and Bayesian-derived individual-level uncertainty distributions and precision-targeted validation sample-size calculations. This is recent, high-visibility, and explicitly notes that the problem is under-addressed.
- **Calibration vocabulary is mature but practice is not.** Van Calster et al (J Clin Epidemiol 2016, DOI 10.1016/j.jclinepi.2015.12.005) defined the hierarchy mean → weak → moderate → strong calibration (548–1k+ citations depending on source). Collateral evidence from methodological audits (e.g., Wynants et al COVID-19 models, 545/606 high risk of bias) is invoked by Riley to show miscalibration is common. Yet external validation studies rarely report calibration curves with uncertainty bands or subgroup calibration.
- **Conformal prediction is the mature “simple baseline” for distribution-free intervals — but clinical adoption is survey-level, not routine.** Angelopoulos & Bates (arXiv:2107.07511 → FTML 2023, DOI 10.1561/2200000101) provide coverage guarantees under exchangeability; Vazquez & Facelli (J Healthcare Inform Res 2022) and the 2025 UQ-for-ML-in-Healthcare survey (arXiv:2505.02874) catalog medical-image and EHR applications (skin lesions Lu et al 2021, genomics Papangelou 2024). The pattern: conformal methods appear in reviews and proof-of-concepts, not in head-to-head clinical utility evaluations against standard calibration approaches.
- **Aggregate-statistic failure is acknowledged abstractly but not audited empirically in clinical prediction.** No systematic review was found that quantifies how often aggregate calibration/overall AUC masks subgroup miscalibration or Simpson reversal in validated clinical models. Individual cases (e.g., kidney-stone treatment Simpson reversal, sex/age subgroup calibration drift) are classic pedagogical examples, not a body of empirical auditing work. This is the thin area.
- **Reporting guidelines now demand uncertainty, but compliance is partial.** TRIPOD+AI (BMJ 2024, DOI 10.1136/bmj-2023-078378) now “emphasizes fairness, reproducibility, open science, and uncertainty” as checklist items. The guideline’s existence does not imply the field has solved UQ; if anything it signals the gap.

### Important papers (resolvable IDs only)

| # | Citation | DOI / URL | Type |
|---|----------|-----------|------|
| 1 | Riley et al. Uncertainty of risk estimates from clinical prediction models: rationale, challenges, and approaches. *BMJ* 2025;388:e080749. | https://doi.org/10.1136/bmj-2024-080749 **(VERIFIED via PMC12128882 extract + PMID 39947680)** | article (load-bearing) |
| 2 | Van Calster et al. A calibration hierarchy for risk models was defined: from utopia to empirical data. *J Clin Epidemiol* 2016;74:167-176. | https://doi.org/10.1016/j.jclinepi.2015.12.005 **(VERIFIED via search metadata, 548-1025 cites)** | article |
| 3 | Angelopoulos & Bates. A Gentle Introduction to Conformal Prediction and Distribution-Free UQ. *arXiv:2107.07511* → *FTML* 2023;16:494-591. | https://doi.org/10.1561/2200000101 / https://arxiv.org/abs/2107.07511 **(VERIFIED)** | review/monograph |
| 4 | Vazquez & Facelli. Conformal Prediction in Clinical Medical Sciences. *J Healthcare Inform Res* 2022;6:241-252. | https://doi.org/10.1007/s41666-021-00113-8 | article |
| 5 | Collins et al. TRIPOD+AI statement. *BMJ* 2024;385:e078378. | https://doi.org/10.1136/bmj-2023-078378 **(VERIFIED)** | guideline |
| 6 | Collins et al. TRIPOD Statement (2015). *BMJ* 2015;350:g7594. | https://doi.org/10.1136/bmj.g7594 | guideline |
| 7 | Zhou et al. Uncertainty Quantification for Machine Learning in Healthcare: A Survey. *arXiv:2505.02874* 2025. | https://doi.org/10.48550/arXiv.2505.02874 | review (survey) |
| 8 | Pearl. Understanding Simpson’s Paradox. *UCLA Tech Rep R-414* (via ftp.cs.ucla.edu). | https://ftp.cs.ucla.edu/pub/stat_ser/r414.pdf | tech report (causal resolution) |

> Verification note: #1 extract confirms Fig 1 CRASH risk 0.59 with 95% interval, discussion of epistemic uncertainty and bootstrap/Bayesian intervals, and PMC full text access. #5 DOI resolves to open-access BMJ TRIPOD+AI checklist paper.

### What appears established
- A four-level calibration hierarchy provides a shared language (mean → strong); weak calibration (intercept/slope) is routinely reported, strong (individual-level) is aspirational.
- At least in principle, bootstrapped or Bayesian posterior intervals around individual risks and calibration curves can be produced and should be reported; Riley et al give concrete interval examples (e.g., CRASH unfavourable-outcome interval 0.477–0.693 for a single TBI patient) and link interval width to validation sample size.
- Conformal prediction provides finite-sample, distribution-free coverage guarantees under exchangeability — the cleanest formal baseline for prediction intervals/sets.
- Aggregate metrics can mislead: textbook Simpson reversals (treatment appears worse overall but better within strata) are pedagogically settled.

### What remains uncertain
- **How often do deployed/validated clinical models exhibit consequential aggregate masking?** No empirical audit was found quantifying, across a corpus of externally validated models, the frequency with which overall calibration “passes” while one or more clinically important subgroups (sex, age, comorbidity burden, site) fails moderate/weak calibration, or with which ranking reversals occur between subgroups.
- **Does adding individual-level UQ change decisions or outcomes?** Riley states the need but the clinical-utility evidence (decision-curve benefit of interval-aware thresholds vs point thresholds) is thin.
- **Conformal vs standard calibration in EHR practice:** No identified head-to-head on the same clinical prediction tasks comparing conformal intervals, Van Calster calibration bands, and Bayesian credible intervals on discrimination, coverage, interval width, and decision utility — especially under distribution shift.
- **Simpson / ecological fallacy in modern EHR risk models:** The causal-resolution account (Pearl) vs descriptive account is settled theoretically, but the *detection rate* in contemporary EHR-derived models (not textbook kidney-stone examples) is unknown.

### Potential gap
**Falsifiable, methods-forward question:** *Among a corpus of externally validated clinical prediction models (e.g., TRIPOD-defined validation studies, 2015–2025), aggregate calibration and overall AUC systematically overstate subgroup calibration and clinical utility — such that weak/moderate calibration fails in ≥X% of clinically relevant subgroups despite acceptable overall metrics, and conformal or Riley-style individual uncertainty intervals would change the recommend-vs-not decision for a non-trivial fraction of patients.*

- **Alternative experimental form (single-model deep dive):** Take one widely cited clinical prediction model with available validation data (e.g., QRISK-family, CRASH/IMPACT, or a MIMIC-derived mortality model) and pre-register subgroup calibration + conformal-coverage auditing with decision-threshold analysis, testing whether point-risk decisions are reproducible under honest UQ.
- **Gap type:** Empirical auditing / methods evaluation; systematic-review-adjacent but requiring new computation on published data.
- **Why it may be a gap:** No directly equivalent study was identified in searches performed so far that (a) systematically audits published validated models for subgroup-calibration failure / aggregate masking, or (b) head-to-head compares Riley bootstrap/Bayesian intervals vs conformal intervals vs Van Calster bands on the same clinical tasks with decision analysis. Closest are (i) Riley position/review (proposes but does not carry out the audit), (ii) generic Simpson expositions, (iii) conformal proof-of-concepts in imaging/genomics.
- **Mandatory simple baselines:** Overall calibration intercept/slope + calibration plot with loess, stratified calibration (sex, age decile, comorbidity count, site), standard prediction interval via bootstrap, conformal prediction (split/inductive conformal with correct coverage target, e.g., 90%), and Brier score decomposition. **“Beat the baseline or show it suffices” = “does UQ change decisions beyond point estimate?”**
- **Data need:** **Real data required** for the audit (published models’ validation cohorts or public datasets). For the single-model deep dive, **public / restricted-public suffices:** MIMIC-III/IV (PhysioNet), CRASH trial data (LSHTM repository), QRISK open validation cohorts, or UK Biobank-linked outcomes. Simulation alone does not suffice because the claim is about published-model behaviour in the wild.

### Evidence AGAINST the gap (adversarial: closest prior work that defeats the gap)
- **Riley et al BMJ 2025 itself** substantially narrows the gap: it already demonstrates interval-width problems on real validation data (calibration-curve bands that may not contain point estimates; individual CRASH intervals 0.477–0.693), proposes bootstrap/Bayesian methods, and cites TRIPOD/BMJ sample-size guidance for validation studies targeting calibration precision. A generous reader could argue the core empirical demonstration is done and the remaining work is “just apply Riley to more datasets” — reducing novelty to incremental auditing.
- **Conformal-in-medicine literature (Vazquez & Facelli 2022; Zhou 2025 survey; Lu 2021 skin lesions; Papangelou 2024 genomics)** could be read as showing conformal already handles the individual-level UQ problem with guarantees. This defeats a gap framed as “nobody does individual intervals.” The surviving gap must therefore be specific to *aggregate masking* and *decision impact*, not the mere existence of intervals.
- **Pearl R-414 and the broader Simpson-paradox literature** fully resolve the statistical/casual interpretation of reversals. This defeats a naive gap (“Simpson’s paradox is under-appreciated”). The viable gap is not conceptual but *empirical frequency* in contemporary clinical prediction — which must be framed with that precision to avoid dismissal as textbook exposition.
- **Methodological audits of calibration exist at model-level:** e.g., Collins/TRIPOD-related validation studies and Steyerberg’s calibration work do report some subgroup calibration. If those audits already show rare subgroup failure, the “systematic overstatement” hypothesis could be falsified by existing evidence — which is precisely what makes the question falsifiable and worth testing.

### Relevant datasets (named: public / restricted / simulation; access route if restricted)
- **Public / open — preferred for audit:**
  - **CRASH-2 / CRASH-3 trial data** and **IMPACT TBI** validation cohorts — referenced by Riley; CRASH risk calculator data via LSHTM (https://www.crash.lshtm.ac.uk/) and associated trial repositories (application-based but openly documented).
  - **MIMIC-III / MIMIC-IV** (PhysioNet credentialed) — for single-model deep dive: train/validate mortality or readmission models and run subgroup/conformal auditing with known covariates.
  - **UK Biobank** (restricted-public, application via UKB Access Management System) — for QRISK-family or CVD risk recalibration audits; optional.
- **Published validation Study Data:** Any TRIPOD-compliant external validation study that shares individual-participant or aggregate-subgroup calibration data (increasingly required by journals) — corpus built via systematic search, not a single dataset purchase.
- **Simulation — supplementary, not sufficient alone:** Plasmode resampling from MIMIC to inject known subgroup miscalibration and test detection power of auditing pipeline; useful for power analysis but not as the primary dataset.
- **Software:** `rms`/`CalibrationCurves` (R), `conformalInference` / `MAPIE` (Python), `TRIPOD checklist` extraction scripts, Riley et al supplementary code (Utrecht repository / hbiostat.org/papers/ril25unc.pdf).

### Methodological implications
- Either outcome is informative. **If** subgroup miscalibration is common despite acceptable overall metrics, the field must move from point-risk deployment to interval-aware decision thresholds and subgroup-stratified calibration reporting as standard (supporting Riley + TRIPOD+AI). **If not** (overall metrics do proxy subgroups well for validated models), that is a rigorous negative result that justifies continued reliance on well-validated overall metrics — also publishable.
- Head-to-head of Riley bootstrap/Bayesian intervals vs conformal intervals on the same tasks clarifies trade-offs: formal guarantee (conformal) vs model-based interpretability (Bayesian) vs bootstrap practicality, informing guidance for different clinical contexts (ICU vs primary care).

### Clinical implications
- For the bedside, unreliable subgroup calibration means a model that looks “calibrated” on average may mislead for women, older adults, or multimorbid patients — the exact groups where decisions are hardest. Interval-aware tools could make shared decision-making more honest (e.g., “your 10-year CVD risk is 12%, but compatible with 7–19% given model uncertainty — statin threshold 10% falls inside the interval”).
- For guidelines and regulation, an audit provides the missing enforcement evidence behind TRIPOD+AI’s new uncertainty/fairness items: without data on how often overall metrics hide failure, reporting mandates remain exhortation.

### India relevance
**Verdict: GEOGRAPHY-ONLY for the main audit; STRESSES-ASSUMPTION for a well-specified extension.**

- The core audit (do aggregate metrics mask subgroup failure?) is population-agnostic; it will likely replicate in any health system. Do not claim STRESSES-ASSUMPTION for that.
- **Extension that would stress an assumption:** Indian populations differ in baseline risk, risk-factor distributions, and measurement availability (e.g., lipid subfractions, competing risks). If the audit corpus included Indian validation cohorts (e.g., Indian CVD or TBI validations), transportability of the “overall calibration passes → subgroup passes” assumption would be genuinely stressed. This would be scientifically meaningful but requires Indian validation data; it should be framed as a Stage-2 transportability question, not as the v1 gap.

### Confidence
**Medium.** Riley 2025 sharply narrows the uncertainty-interval novelty, but the *aggregate-masking audit* and *conformal-vs-Riley head-to-head with decision analysis* were not found as executed studies. Risk is that a recent TRIPOD meta-research audit (e.g., Najafabadi-style calibration meta-analysis) already covers subgroup calibration frequency — systematic-review-of-reviews search should be expanded before promotion.

### Recommended next search
1. **Targeted meta-research sweep:** `TRIPOD systematic review external validation calibration subgroup sex age` + `calibration slope intercept meta-analysis clinical prediction` — to exhaust existing audits of subgroup calibration.
2. **TRIPOD corpus construction:** Build a TRIPOD-defined cohort (2015–2025 external validations) via PubMed `TRIPOD[Title/Abstract] AND validation` and screen first 50 for subgroup calibration reporting rate — establishes base rate for the audit.
3. **Conformal clinical head-to-head:** Search `conformal prediction clinical risk CRASH MIMIC QRISK coverage interval width` — to check whether any study already ran the Riley-vs-conformal decision-threshold comparison.
