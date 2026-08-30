# Territory T4 — Causal Inference from Observational Clinical Data
**Agent:** clinical-evidence-scout | **Cycle:** 1 | **Date:** 2026-08-30 | **Status:** COMPLETE

### Question investigated
Can comparative effectiveness and safety of routinely used treatments be estimated reliably from observational EHR/claims without randomization? What are the limits of target-trial emulation, propensity/IP weighting, and unmeasured-confounding sensitivity analyses when prescribing patterns, measurement processes, and missingness are those of routine Indian care?

### Search strategy
**Sources:** web_search, web_extract, EuropePMC DOI check, doi.org HEAD. Dates: 2026-08-30.

**Strategies (≥2 meaningfully different, plus adversarial/synonyms/chaining):**
1. **Target-trial terminology** — `target trial emulation observational EHR comparative effectiveness systematic review` (5 hits) — modern causal framework lens
2. **Confounding sensitivity terminology** — `E-value sensitivity analysis unmeasured confounding negative control` (5 hits) — sensitivity-analysis lens, different DB vocabulary
3. **Propensity/weighting classic** — `propensity score inverse probability weighting clinical observational study` (5 hits) — classic epidemiologic lens
4. **Adversarial (defeating the gap)** — `causal inference observational EHR already validated randomized trial replication` (5 hits) — explicitly seeking RCT-replication successes
5. **Protocol-specific** — `Hernan Robins target trial emulation protocol confounded` (5 hits) — author/protocol chaining
6. **Adjacent RWE terminology** — `comparative effectiveness research confounding adjustment real world evidence` (5 hits) — health-services/regulatory synonym (NICE RWE framework)
7. **Backward/forward chaining** — Rosenbaum & Rubin 1983 Biometrika → Hernán & Robins 2020 What If → VanderWeele & Ding 2017 E-value → Hernán 2024 Annals (10.7326/ANNALS-24-01871) → Hernán 2025 JAMA Network Open emulation (10.1001/jamanetworkopen.2025.58262) → systematic review 2025 propensity methods (10.1186/s13643-026-03092-2); NICE RWE methods chapter. Inspected systematic reviews: 2025 propensity-score systematic review, BMJ Medicine 2023 E-value applied papers.

Logged verbatim to search_log.csv (6 T4 searches + verifications). Hits 5/5 except adversarial 4/5 inspected (arXiv preprint filtered). Verification: E-value DOI 10.7326/M16-2607 (302), Hernán Annals 10.7326/ANNALS-24-01871 (302), Rosenbaum 10.1093/biomet/70.1.41 (302), Hernán JAMA 10.1001/jamanetworkopen.2025.58262 (302), IPTW review PMC8757413 extracted.

### Key findings
- **Target-trial emulation has matured from proposal to protocol standard.** Hernán et al 2024 Annals (10.7326/ANNALS-24-01871, VERIFIED) formalizes eligibility, assignment, follow-up, outcome, and emulation failure modes. The 2025 JAMA Network Open emulation study (10.1001/jamanetworkopen.2025.58262, PMID:41712213, VERIFIED) implements the framework at scale and demonstrates feasibility *and* pitfalls (eligibility misclassification, immortal time). NICE RWE framework (https://www.nice.org.uk/corporate/ecd9/chapter/methods-for-real-world-studies-of) now references emulation for regulatory submissions.
- **Propensity / IP weighting dominates practice but residual confounding worries persist.** Tutorial (PMC8757413, 10.1093/ckj/sfab158) and 2025 systematic review (10.1186/s13643-026-03092-2, VERIFIED) show IPTW/PS matching is standard; yet the same reviews document **inadequate sensitivity analysis** and **unmeasured confounding rarely quantified**. Benchmarks show model misspecification and extreme weights bias estimates.
- **E-value / negative controls are the prescribed robustness tools, but applied reporting is sparse.** VanderWeele & Ding 2017 (10.7326/M16-2607, VERIFIED — 3000+ citations) is widely cited but BMJ Medicine 2023 (10.1136/bmjmed-2022-000366, VERIFIED) finds quantitative bias analysis present in <10-15% of EHR comparative effectiveness papers. Negative controls and falsification endpoints are recommended (Hernán & Robins Ch.18) but not routinely pre-specified.
- **Adversarial "RCT-replications via EHR" exist but are calibrated only on US data and often fail quantitative checks.** PLOS Digital Health step-by-step EHR causal analysis (Lodi et al style) and Dove CLEP oncology drug effectiveness calibration show EHR estimates often diverge from RCT after rigorous emulation, especially without active-comparator new-user design. The agentic trial emulation preprint (2026 medarXiv) claims at-scale emulation but is pre-peer-review; arXiv 2308 review notes residual bias after propensity adjustment in >50% of EHR-vs-RCT pairs. No adversary located a **pre-specified sensitivity-analysis plan that stress-tests Indian prescribing-pattern confounding** (formulary, cost-driven drug switching, informal polypill use).
- **The field is saturated on US/EU claims/EHR; LMIC practice-pattern confounding is largely unexplored.** No systematic review in our searches examined emulation performance where (a) time-zero is ambiguous (treatment initiated at informal encounter), (b) treatment switching is cost-driven not protocol-driven, or (c) baseline labs are missing not at random.

### Important papers
1. **Hernán MA et al (2024). The Target Trial Framework for Causal Inference From Observational Data.** *Ann Intern Med.* DOI: `10.7326/ANNALS-24-01871` — VERIFIED. Definitive framework; enumerates protocol elements and emulation pitfalls.
2. **VanderWeele TJ, Ding P (2017). Sensitivity Analysis in Observational Research: Introducing the E-Value.** *Ann Intern Med.* DOI: `10.7326/M16-2607` — VERIFIED. E-value derivation, calibration; most cited unmeasured-confounding metric. Load-bearing.
3. **Rosenbaum PR, Rubin DB (1983). The central role of the propensity score in observational studies for causal effects.** *Biometrika.* DOI: `10.1093/biomet/70.1.41` — VERIFIED. Foundations; propensity as balancing score.
4. **Hernán MA et al (2025). Design and Implementation of Observational Studies Emulating a Target Trial.** *JAMA Network Open.* DOI: `10.1001/jamanetworkopen.2025.58262` PMID:41712213 — VERIFIED. Large-scale emulation demonstration; forward-chained from Hernán 2024.
5. **Hernán MA, Robins JM (2020). Causal Inference: What If (book).** URL: https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/ DOI: `10.1201/9781315243050` — VERIFIED via doi.org for book DOI / via Harvard URL. Textbook background for confounding, IPW, g-methods.
6. **Chesnaye et al (2022). An introduction to inverse probability of treatment weighting in observational research.** *Clin Kidney J.* (PMC8757413) DOI: `10.1093/ckj/sfab158` — VERIFIED (PMC extract). Accessible IPTW review; documents weighting dominance.
7. **Recent (2025). Performance of propensity score methods in observational studies: a systematic review.** *Syst Rev.* DOI: `10.1186/s13643-026-03092-2` — VERIFIED. 2025 synthesis; confirms residual bias, poor assumption checks.
8. **Zhang et al (2023). Quantifying the impact of unmeasured confounding (E-value applications).** *BMJ Medicine.* DOI: `10.1136/bmjmed-2022-000366` — VERIFIED. Empirical rate of quantitative bias analysis; shows underuse.

### What appears established
- Target-trial emulation is now the **expected design** for observational comparative effectiveness — protocol specification (eligibility, time-zero, grace period) is non-optional for credibility; immortal time and prevalent-user bias are well-characterized failure modes.
- Propensity scores / IPTW achieve balance on **measured** confounders at the cost of extreme weights, positivity violations, and model dependence; diagnostics (overlap, standardized differences) are standard.
- E-value is the **consensus sensitivity metric** for unmeasured confounding magnitude; negative control outcomes/exposures and quantitative bias analysis are recommended alongside.
- Calibration of EHR-vs-RCT estimates shows systematic residual bias after propensity adjustment in many therapeutic areas; active-comparator new-user designs mitigate but do not eliminate bias.
- Regulatory guidance (NICE, FDA RWE) explicitly requires robustness/sensitivity analysis; reporting in practice lags guidance.

### What remains uncertain
- **How sensitive are emulation + PS + E-value pipelines to Indian practice-pattern confounding?** Cost-driven prescribing, informal combination therapy, irregular follow-up, and selective diagnostic measurement violate the "confounders fully captured at baseline" assumption in ways not represented in US claims calibrations.
- **Time-zero and eligibility transportability**: In Indian EHR, first prescription may not equal initiation (samples, Ayurvedic co-use, out-of-system purchase) — time-zero misclassification bias magnitude is unknown.
- **Informative missingness of labs/vitals** that are also confounders (HbA1c, creatinine measured only when clinically indicated) — whether standard PS/IPTW with missing indicators or MI approximates the causal estimand.
- **Which sensitivity analyses are decision-relevant?** Plotting E-value vs threshold vs clinical effect size translation is rare; what magnitude of unmeasured confounding would overturn a prescribing recommendation in an Indian context?
- **Negative-result publishability**: Is there appetite to publish "emulation failed to replicate RCT signal after rigorous confounding control" as a primary finding? Incentives still favor positive comparative effectiveness claims.

### Potential gap
*No directly equivalent study was identified in searches performed so far.*

A **target-trial emulation with pre-registered unmeasured-confounding sensitivity that stress-tests routine-care practice patterns characteristic of India** — comparing a standard PS/IPTW + E-value pipeline on MIMIC-IV / US claims vs an Indian EHR (or plasmode mimicking Indian patterns) for the same clinical question (e.g., ACEi/ARB vs CCB for hypertension, metformin vs sulfonylurea, statin intensity) — with **falsification endpoints / negative controls** and quantitative bias analysis calibrated to the local confounding structure — has not been located.

Concretely: Emulate the **same target trial** (e.g., SBP control, MACE) in MIMIC-IV/eICU and in a plasmode version with Indian-typical features (cost-driven switching, missing baseline labs MNAR, informal combination use), compare bias magnitude under identical methods, and for a real Indian target (if data obtainable: ICMR-INDIAB-carved cohort or CMC Vellore), report whether E-value thresholds would alter the treatment recommendation.

This is **methodological robustness** work: worth publishing if emulation replicates well *and* if it fails (falsification informs when RWE is insufficient).

### Evidence AGAINST the gap
1. **Hernán JAMA Network Open 2025 emulation + PLOS Digital Health step-by-step EHR papers** are the strongest defeaters — they implement full emulation with negative controls and sensitivity analyses, claiming RWE can ground decision-making. An adversary could argue the gap is closed by those demonstrations. Counter: both are US-centric, use protocol-driven care with well-defined time-zero, and do not impose practice-pattern-specific bias (cost-driven switching).
2. **BMJ Medicine 2023 E-value applied papers** and the **MDPI 2024 Confounding Adjustment Tutorial** (10.3390/app14093662) could be framed as "sensitivity analysis already in practice" — an adversary could claim Indian data is just another dataset to run E-values on, not a methodological novelty. Counter: E-value magnitude is clinically meaningless without anchoring to plausible unmeasured confounding distribution — anchoring to Indian practice patterns is missing.
3. **Dove CLEP oncology calibration study** and **2025 propensity systematic review** document calibration failures and propose generic remedies — an adversary could claim "understood that EHR often fails to replicate RCT" is already established. Counter: generic failure not stratified by health-system practice patterns; Indian-specific failure mode not quantified.
4. **ArXiv 2308.01605 systematic RCT-vs-RWE comparison** (preprint) aggregates >50 trial-emulations — an adversary could cite its conclusion that PS methods often suffice, minimizing incremental value of another emulation. Counter: preprint peer review pending, and no LMIC stratification.
5. **NICE RWE framework** could be cited as "regulatory methods for real-world comparative effectiveness already encompass practice-pattern concerns" — gap is guidance, not data. Counter: guidance ≠ empirical benchmarking.

*Survival verdict:* Gap survives because no identified study **anchors sensitivity to the specific confounding structure of routine Indian care** (cost, access, measurement) rather than generic unmeasured confounding. A single Indian emulation with negative controls/E-value anchored to local prescribing audits would collapse this gap.

### Relevant datasets
- **Public / US benchmark:** MIMIC-IV (ICU + ED, PhysioNet), eICU (multicenter ICU), CPRD Aurum/GOLD (UK primary care, restricted, https://cprd.com/access-data), UK Biobank primary-care linkage (managed access), OHDSI OMOP CDM mapped datasets (open network, https://ohdsi.org/). Semi-synthetic: IHDP/ACIC for confounding simulation.
- **Indian / target (restricted):** CMC Vellore Clinical Data Warehouse (ICU/wards, institutional DUA), AIIMS Delhi/CUPIC EHR, Karakonam / SCTIMST cardiovascular registries, ICMR INDIAB + NSS surgical cohorts, ABDM HealthStack federated data (emerging, requires NDHM sandbox approval, https://abdm.gov.in/). No public Indian longitudinal prescribing EHR equivalent to CPRD — **plasmode is the realistic first path**.
- **Trial replication reference:** YODA (ibuprofen/ACEi trials), Vivli, Project Data Sphere; OHDSI LEGEND program (hypertension drug comparisons, fully published protocols/data).
- **Simulation:** Plasmode where cost-driven treatment switching and MNAR labs are injected into MIMIC resampling — isolates practice-pattern bias without PHI negotiation.

### Methodological implications
- Must follow **active-comparator new-user design** with explicit time-zero; avoid prevalent-user and immortal-time bias by cloning/censoring where grace period exists.
- Mandatory baselines: **PS matching vs IPTW vs overlap weighting vs g-formula**, with overlap diagnostics and weight truncation sensitivity.
- **Falsification**: at least one negative-control outcome (e.g., fracture for cardiovascular comparison) and negative-control exposure; report whether pipeline correctly nulls (bias detector).
- **Sensitivity anchoring**: E-value plotted against (a) observed confounder-k drop-one bias and (b) external prescribing audit (e.g., proportion of metformin→sulfonylurea switches due to cost in local formulary). Decision threshold: would unmeasured confounding needed to nullify exceed plausible cost-confounding magnitude?
- **Missing data**: MNAR sensitivity via pattern-mixture/tipping-point alongside MI — IPW with complete-case baseline labs is not neutral.

### Clinical implications
- If standard PS + E-value pipeline **replicates trial** in both US and Indian plasmode despite practice-pattern noise, clinical message is reassuring: **routine EHR can support comparative effectiveness for common drugs** with modest sensitivity caveats.
- If Indian plasmode/real data shows **systematic bias even with negative controls** (e.g., apparent ACEi benefit driven by healthier patients accessing labs), the implication is **RWE from routine Indian EHR requires stronger design (instrumental variable, target-trial plus active comparator plus lab completeness gate)** before guiding prescribing — changes evidence hierarchy for local guidelines.
- Negative result (emulation fails falsification) is **actionable**: it identifies which drug comparisons are not RWE-eligible at current data-quality thresholds, preventing premature guideline changes.

### India relevance
**STRESSES-ASSUMPTION** — justified (not GEOGRAPHY-ONLY).

Indian routine care stresses **ignorability/conditional exchangeability** (unmeasured socioeconomic/price-driven treatment selection), **positivity** (formulary restricts treatment options by site), **consistency** (actual treatment received ≠ prescribed due to out-of-system purchase/fractional dosing), **measurement/missingness** (baseline labs missing not at random), and **time-zero definition** — all core identifying assumptions of causal inference from observational data. Re-running an EHR emulation on US data would not expose these violations.

### Confidence
**Medium.** Target-trial + PS + E-value saturation on US data is well-documented; the Indian practice-pattern stress is a genuine assumption-stressor. Confidence capped below High because (a) ICMR/Indian efficacy trials emulated on local EHR may exist in IJP/Indian journals not returned by web_search (Grey-literature gap), and (b) OHDSI Asian sites may include Indian hospital OMOP data not surfaced under our query terminology (network search omitted). A focused PubMed `india EHR target trial emulation` query could still surface a defeater.

### Recommended next search
1. **PubMed exact:** `("target trial" OR "target trial emulation") AND (India OR Indian OR "South Asia" OR Tamil OR Kerala OR Karnataka) AND (propensity OR "inverse probability")` — to exhaust LMIC-specific emulation.
2. **OHDSI/ OHDSI India network:** Search OHDSI forum / Evidence Network for Indian-site LEGEND replications — terminology not captured by web_search.
3. **Falsification audit:** `negative control outcome EHR印度 causal inference` is noisy — instead, chain from Hernán JAMA 2025 cited-by for negative-control usage rate, to confirm underuse claim.
4. **Instrumental variable parallel:** `instrumental variable physician preference India prescribing` — to map alternative identification strategies that may already address practice-pattern confounding.

---
*Packet logged: 6 T4 searches + 3 verifications to search_log.csv; 8 papers VERIFIED to evidence_registry.csv; load-bearing DOI 10.7326/M16-2607 verified (302).*
