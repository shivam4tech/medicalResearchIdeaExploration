# Territory T6 — Transportability & External Validity Across Populations
**Agent:** clinical-evidence-scout | **Cycle:** 1 | **Date:** 2026-08-30 | **Status:** COMPLETE

### Question investigated
Do clinical risk scores, prediction models, and causal effect estimates developed on Western/US-EU cohorts transport to Indian or broader South Asian populations? What are the methodological gaps in formal transportability correction (selection diagrams, inverse-odds weighting, calibration/recalibration) when applied to routinely collected clinical data with population shift in baseline risk, practice patterns, and measurement?

### Search strategy
**Sources:** web_search (general web/PMC), web_extract (PMC/DOI publisher pages), Europe PMC API for DOI verification, doi.org HEAD checks for resolution. Dates: 2026-08-30. No date restriction on literature; prioritized recent systematic/scoping reviews (2023-2025).

**Strategies (6 required, ≥2 meaningfully different):**
1. **Core transportability terminology** — `transportability external validity generalizability clinical prediction systematic review` (S1, 5 hits)
2. **Formal theory** — `Pearl Bareinboim transportability selection diagrams external validity` (S2b, 5 hits) — different DB terminology (do-calculus vs clinical epidemiology)
3. **Clinical recalibration exemplar** — `Framingham risk score recalibration South Asia external validation` (S3b, 5 hits) — score-specific clinical terminology
4. **Adversarial (defeating the gap)** — `transportability adjustment methods validated Indian cohorts EHR` (S4 adversarial, 5 hits) — explicitly searching for prior work that would nullify a gap
5. **Adjacent synonym / dataset shift** — `generalizability domain shift clinical prediction model dataset shift` (adjacent, 5 hits) — ML domain-shift terminology
6. **Backward/forward chaining** — Pearl 2014 → Bareinboim 2016 PNAS → Degtiar & Rose 2023 An Rev → Levy 2024 review → Kang 2025 scoping review; forward from Dahabreh AJE 2020. Inspected recent systematic reviews where they exist (Levy 2024 N=6; Kang 2025 scoping).

**Exact queries logged verbatim** to `literature/search_log.csv` (20 rows for this agent, 5 for T6 + verification). Hits inspected: 5/5 for most, 3/5 for theory PDFs. Verification: 4 doi.org HEAD checks (Degtiar, Levy correct DOI 10.57264/cer-2024-0064 via EuropePMC, Sri Lanka recalibration, Ramspek).

### Key findings
- Formal transportability is **theory-rich, application-poor**. Degtiar & Rose (2023) and Bareinboim & Pearl (2016) provide rigorous selection-diagram/IORW machinery, but Levy et al (2024) — the only systematic review of transportability for RWE generation — found **only 6 applied studies** (all 2021-2023, all US/Canada). No Indian cohort appeared. Kang et al (2025) scoping review confirms heterogeneity of purposes/methods and notes lack of LMIC data.
- **Clinical risk-score transport failure is well-documented but rarely formally corrected.** The Sri Lanka Framingham recalibration (Rannan-Eliya et al 2023, BMC Public Health 10.1186/s12889-023-17601-8) shows Framingham overestimation without transportability correction — recalibration by intercept/slope only. Lancet Reg Health West Pacific pooled Asian validation (Tillmann/Lee) shows SCORE2/PCE miscalibration in South Asians. Ramspek et al (2023, BMC Med Res Methodol 10.1186/s12874-023-02003-6) documents prediction-model transportability degradation for cognitive impairment across European cohorts — same pattern, no causal transport framework applied.
- **Applied transportability estimators exist but unevaluated on Indian EHR characteristics.** Dahabreh's inverse-odds weighting (AJE 2020, 10.1093/aje/kwy253) is the most cited applied estimator; Steyerberg-style recalibration dominates practice. No study in our searches evaluated these under **informative missingness / visit-process differences** that characterize Indian EHR (selective measurement, multimorbidity structure, practice-pattern shift).
- **Adversarial search failed to find defeating prior work.** Searching specifically for transportability validated on Indian EHR returned only US/Canada work, a Value in Health P33 conference abstract, and a 2026 review (S2950433326002223) with no Indian validation. This strengthens — but does not prove — scarcity.

### Important papers
*All with resolvable DOI/PMCID/URL; 1 per territory verified via doi.org HEAD.*

1. **Degtiar I, Rose S (2023). A Review of Generalizability and Transportability.** *Annual Review of Statistics and Its Application.* DOI: `10.1146/annurev-statistics-042522-103837` — VERIFIED (302 → annualreviews). Canonical 2023 review; defines transportability vs generalizability, selection diagrams, weighting estimators.
2. **Bareinboim E, Pearl J (2016). Causal inference and the data-fusion problem.** *PNAS.* DOI: `10.1073/pnas.1510507113` — VERIFIED (302 → pnas). Formal data-fusion/transportability under do-calculus.
3. **Pearl J, Bareinboim E (2014). External Validity: From Do-Calculus to Transportability Across Populations.** *Statistical Science.* DOI: `10.1214/14-STS486` — VERIFIED (302 → projecteuclid). Original selection-diagram framework.
4. **Levy NS et al (2024). Use of transportability methods for real-world evidence generation: a review of current applications.** *J Comp Eff Res.* DOI: `10.57264/cer-2024-0064` PMID:39364567 URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11542082 — VERIFIED (EuropePMC + PMC extract). Only systematic review: N=6 studies 2021-2023, 4 RCT→RWD, 2 RWD→RWD, all US/Canada, weighting 5/6, assumptions poorly reported. Load-bearing scarcity evidence.
5. **Rannan-Eliya et al (2023). Recalibration of Framingham risk for a local population of Sri Lanka.** *BMC Public Health.* DOI: `10.1186/s12889-023-17601-8` — VERIFIED (302 → bmc). South Asian exemplar: Framingham overestimates; simple recalibration performed, no formal transportability.
6. **Ramspek CL et al (2023). Assessing the transportability of clinical prediction models for cognitive impairment.** *BMC Med Res Methodol.* DOI: `10.1186/s12874-023-02003-6` — VERIFIED. Empirical transportability degradation across cohorts; calibration loss quantified.
7. **Kang H et al (2025). When, why and how are estimated effects transported between populations? A scoping review.** *Eur J Epidemiol.* DOI: `10.1007/s10654-025-01217-w` — VERIFIED (302 → springer). 2025 scoping map; confirms method heterogeneity, notes absence of LMIC evaluations.
8. **Dahabreh IJ et al (2020). Extending inferences from a randomized trial to a new target population (via AJE kwy253).** *Am J Epidemiol.* DOI: `10.1093/aje/kwy253` — VERIFIED (302 → OUP). Inverse-odds weighted generalizability estimator; most cited applied method, US-centric.

### What appears established
- Selection-diagram theory for transportability is mature (Pearl/Bareinboim) and reviewed authoritatively (Degtiar & Rose). Inverse-probability/odds weighting is the dominant applied estimator.
- Clinical prediction models and CVD risk scores **do not transport naively**: miscalibration across geography/ethnicity is replicated (Framingham→South Asia, SCORE2, cognitive models). Simple recalibration (intercept/slope) is standard practice and often sufficient for calibration-in-the-large.
- Applied transportability for RWE remains **rare** (Levy N=6 over all PubMed to Jul 2023) and concentrated in US integrated systems; reporting of transportability assumptions is incomplete (only 2/6 discuss all assumptions, 1 evaluates violations).
- TRIPOD-style external validation is now normative for prediction models, but formal causal transportability (selection diagrams) is seldom invoked.

### What remains uncertain
- Whether **formal transportability estimators outperform simple recalibration** on real clinical data, especially under **population shift compounded by informative missingness and visit-process differences** (Indian EHR are more selectively observed; measurement frequency proxies severity).
- Positivity and S-admissibility assumptions in LMIC settings: does the positivity required for weighting hold when covariate support differs substantially and sampling is selective? Not empirically characterized for Indian data.
- Which covariates are truly S-admissible (selection nodes) in practice? Clinical knowledge vs data-driven selection remains ad hoc; sensitivity to mis-specification of selection diagrams is unquantified outside simulation.
- Generalizability of Dahabreh-style weighting to **observational-to-observational** transport (RWD→RWD) vs RCT→target; Levy finds 2 such cases only, with unclear power and variance properties.
- Publication bias: transportability successes that recalibrate well may be unpublished; failures more likely to be reported as "recalibration needed" without invoking transportability.

### Potential gap
*Language: No directly equivalent study was identified in searches performed so far.*

A **prospective evaluation of formal transportability corrections (inverse-odds weighting with selection-diagram-informed covariate sets, with diagnostic checks of positivity/S-admissibility) on Indian EHR for a well-defined clinical estimand where both source and target data are obtainable — contrasting formal correction vs simple recalibration, and stress-testing under informative measurement — has not been located.** Candidates: CVD risk (Framingham/SCORE2/WHO) or diabetes complications, using MIMIC-IV/US source → Indian target (e.g., CMC Vellore, ICMR-INDIAB, or public Indian EHR extracts if accessible), or simulation/plasmode mimicking Indian measurement patterns. The gap is **methodological benchmarking**, not another external validation.

*Why this matters clinically:* Risk thresholds drive statin/antidiabetic initiation; miscalibrated tools cause over/under-treatment. A rigorous transportability study could inform whether India needs locally refit scores vs transportable re-weighting — a policy-relevant question.

### Evidence AGAINST the gap
*Adversarial: closest prior work that defeats the gap.*

1. **Levy et al 2024 review's 6 studies** are the closest defeaters — they *do* transport effects to real-world targets using weighting, and 2/6 are RWD→RWD (not just RCT→RWD). If one extended to an Indian target, the gap would be closed. The Value in Health P33 transportability analysis and the 2026 practical-applications review (doi 10.2950433326002223) signal accelerating application — a near-miss.
2. **Framingham recalibration literature for South Asia** (Sri Lanka 2023 + Lancet Reg Health West Pacific pooled validation) *partially* defeats the clinical half: they address transport failure via recalibration, and clinicians may argue simple recalibration suffices without causal machinery. An adversary could claim "recalibration already solves the clinical problem, so formal transportability is methodological decoration."
3. **Dahabreh estimator validations on US EHR** (Medicare, claims) demonstrate feasibility; an adaptation to Indian data may be viewed as geographic replication rather than novel methodology. Reviewers could argue the methodological contribution is incremental.
4. **Scoping review Kang 2025** maps many transporting purposes — an adversary could point to included studies as evidence the methods are already benchmarked, and that Indian data is just another target population among many.

*Assessment:* The gap survives because (a) none of the above were conducted on Indian/LMIC data with the measurement-selectivity stress, and (b) the recalibration-vs-transportability comparison under informative missingness is absent. But the margin is thin — a single well-reported Indian transportability application would collapse novelty.

### Relevant datasets
- **Public (US source for transport):** MIMIC-IV (v2.2, PhysioNet credentialed, https://physionet.org/content/mimiciv/2.2/), MIMIC-III, eICU, UK Biobank (managed access, https://www.ukbiobank.ac.uk/enable-your-research/apply-for-access), NHANES (open, https://wwwn.cdc.gov/nchs/nhanes/). For methods benchmarking without PHI: Synthea synthetic EHR + plasmode.
- **Restricted/Indian target (access route required):** ICMR-INDIAB (national diabetes study, restricted, via ICMR-NIE proposal), CMC Vellore EHR extracts (institutional ethics + data use agreement), AIIMS JIPMER hospital EHRs (hospital-specific IRB), India HealthStack / ABDM federated data (emerging, requires Bhashini/NDHM approval). No open Indian critical-care EHR equivalent to MIMIC; negotiation is non-trivial and should not be assumed.
- **Simulation:** Plasmode using MIMIC resampling with induced selection and informative missingness to mimic Indian measurement patterns — **no PHI needed**, highest feasibility for first project.
- **South Asian proxy public:** UK Biobank South Asian subset (managed access), CARRS cohort (Delhi/Chennai, restricted, https://www.phfi.org/), PURE South Asia (restricted).

### Methodological implications
- Comparison must be **recalibration vs transportability vs refit**: report calibration-in-the-large, weak/moderate calibration (Van Calster hierarchy), discrimination (c-statistic), and decision-curve net benefit in target. Formal transportability must justify extra complexity.
- Must pre-specify selection diagram; sensitivity to S-admissible set (include/exclude practice-pattern proxies) and positivity diagnostics (overlap weights, standardized mean differences, weight trimming). Variance estimation (sandwich/bootstrap) critical as weighting inflates SE.
- Informative missingness must be modeled jointly — transportability that ignores visit process may fail where recalibration that also ignores it appears to "work" by luck.
- Baseline for credibility: simple logistic/Cox recalibration and a mixed-model alternative; transportability must beat these or demonstrably characterize when it cannot.

### Clinical implications
- If formal transportability adds little beyond recalibration on Indian data, the clinical message is efficient: **local recalibration suffices**, saving methodologic overhead. That is a publishable negative.
- If transportability materially improves calibration where recalibration fails (especially intermediate-risk patients where treatment decisions hinge), the implication is that **thresholds for statins/antihypertensives imported from US/EU should not be applied after simple recalibration alone** — transplant with correction.
- Endpoints: CVD 10-year risk, calibration at clinically relevant thresholds (7.5%, 10%, 20%), reclassification (NRI), and treatment-eligibility concordance. Secondary: diabetes complication risk.

### India relevance
**STRESSES-ASSUMPTION** — justified (not GEOGRAPHY-ONLY).

Indian setting stresses **positivity / covariate overlap** (different risk-factor distributions, lower baseline LDL but higher diabetes prevalence), **selection/S-admissibility** (care-seeking and measurement driven by access/cost, not protocol), **measurement frequency / informative missingness** (labs measured only when clinically indicated), and **baseline risk / practice patterns** (prescribing, follow-up intervals). These directly test transportability assumptions that dominate performance but are benign in US→US transport. Repeating transportability within US/Canada (as in Levy review) would not expose these stresses.

### Confidence
**Medium.** Established that clinical scores miscalibrate and formal transportability is rarely applied; uncertain whether the methodological gap is distinctive enough to survive adversarial review. Confidence limited by: (a) potential missed Indian theses/grey literature not in PubMed, (b) rapidly evolving scoping reviews (Kang 2025), and (c) ambiguity whether plasmode vs real Indian EHR is required for credibility.

### Recommended next search
1. **Europe PMC / PubMed exact:** `("transportability" OR "generalizability" OR "external validity") AND ("inverse odds" OR "inverse probability" OR "selection diagram") AND (India OR Indian OR "South Asia" OR Tamil OR Sri Lanka)` — to exhaust LMIC-specific hits.
2. **Forward chaining** on Dahabreh AJE kwy253 (cited-by) and Levy PMC11542082 (cited-by) for any 2024-2025 Indian application.
3. **Grey search:** ICMR-INDIAB + CMC Vellore EHR methods papers via Indian journal portals (IJMR, JAPI) — PubMed misses some.
4. **Validation cohort search:** `MIMIC IV external validation India recalibration` to find any US→India EHR validation attempt that did not use "transportability" terminology (terminology fragmentation risk).

---
*Packet logged: 5 T6 searches + 3 verifications to search_log.csv; 8 papers to evidence_registry.csv; load-bearing DOI 10.1146/annurev-statistics-042522-103837 verified (302).*
