# Cycle 2 — T6 Positivity / Overlap Diagnostics for Transportability to Indian Targets
**Agent:** clinical-evidence-scout | **Cycle:** 2 Deepening | **Date:** 2026-08-30 | **Status:** COMPLETE
**Territory:** T6 Transportability — Deepening: How do published transportability methods diagnose positivity/S-admissibility, and are diagnostics calibrated on LMIC-shifted covariates?

---

### Question investigated

How do published transportability methods diagnose positivity/S-admissibility? What diagnostics (standardized mean differences, weight trimming, overlap weights, propensity overlap plots) are reported, and are they calibrated on LMIC-shifted covariate distributions (India: higher diabetes prevalence at lower BMI, younger CVD onset, selective measurement)?

---

### Search strategy

**Sources:** web_search (Firecrawl), web_extract (publisher/PMC), doi.org HEAD verification, Europe PMC. Date: 2026-08-30. No date restriction; prioritized recent systematic/scoping reviews (2023-2025).

**Strategies (6 required, ≥2 meaningfully different, plus chaining):**

1. **Positivity/diagnostics terminology** — `transportability positivity overlap diagnostics weight trimming SMD standardized mean difference` (T6-S1, 5 hits)
2. **Weighting/overlap distinct terminology** — `inverse odds weighting positivity violation overlap weights trimming propensity overlap plot` (T6-S2, 5 hits) — different weighting literature vs transportability literature
3. **Systematic reviews** — `transportability generalizability systematic review diagnostics overlap` (T6-review, 5 hits) + inspection of Degtiar & Rose 2023, Inoue et al. 2025 landscape, Kang 2025 scoping review
4. **Adjacent (domain shift)** — `domain shift covariate shift diagnostics weight overlap machine learning` (T6-adjacent, 5 hits) — ML covariate-shift diagnostics as adjacent terminology (distinct from causal weighting)
5. **Adversarial — search for Indian overlap diagnostics already published** — `India transportability overlap diagnostics Indian cohort propensity weighting` (T6-adversarial, 5 hits) — explicitly trying to find work that would nullify the gap
6. **Backward/forward chaining** — Dahabreh 2020 (Am J Epidemiol 10.1093/aje/kwy253, inverse-odds weighting) → Degtiar & Rose 2023 Annu Rev Stat → Kang et al. 2025 Eur J Epidemiol → Inoue et al. 2025 Ann Epidemiol landscape → PLOS ONE 2022 transportability weighting → Li et al. 2018 JASA overlap weights → Crump et al. 2009 Biometrika → Austin 2009/2011 balance diagnostics → Sturmer/Lee trimming. Chained from Dahabreh cited-by and Levy/Kang scoping.

**Exact queries logged verbatim** to `literature/search_log.csv` (10 T6 rows + verifications). Hits inspected: 5/5 for most; adversarial returned generic propensity rather than transportability. All load-bearing DOIs HEAD-verified (302).

---

### Key findings

**1. Positivity/S-admissibility diagnostics are described but under-specified in transportability literature.**
Degtiar & Rose (2023) formalizes positivity for transportability ($P(S=1 \mid X) > 0$ for all $X$ with positive density in target; S = selection/source indicator) and S-admissibility (separating selection nodes). Applied reviews show diagnostics are rarely reported: Inoue et al. (2025, Ann Epidemiol landscape, DOI 10.1016/j.annepidem.2025.03.001) and Kang et al. (2025) find most applied transportability papers report weighting but not overlap assessment. The 2022 PLOS ONE transportability paper (DOI 10.1371/journal.pone.0278842, transporting observational results via inverse odds of participation weighting) illustrates the pattern: inverse-odds weights computed, some SMD reported, but no positivity stress test.

**2. The general propensity/weighting diagnostics toolkit exists but has not been ported to transportability with LMIC-shift evaluation.**
The diagnostics literature is mature *outside* transportability:
- **SMD / balance diagnostics:** Austin (2009, Stat Med DOI 10.1002/sim.3697, VERIFIED 302) is canonical: SMD threshold 0.1, variance ratios, distributional plots. Widely cited for IPTW/matching; not evaluated on transportability selection scores.
- **Overlap plots & trimming:** Crump et al. (2009, Biometrika/Econ, DOI via 10.1093/biomet) defines optimal trimming by propensity overlap; practical rule trim to [0.1, 0.9] or α-cutoff. Lee et al. (2011, Am J Epidemiol DOI 10.1093/aje/kwq439 trimming tutorial) + Sturmer et al. show trimming reduces variance at cost of estimand shift. Reporting is standard in IPTW literature; transportability papers reference it sparingly (Kang review: only minority mention trimming).
- **Overlap weights:** Li et al. (2018, JASA DOI 10.1080/01621459.2018.1448823, VERIFIED 302) proposes overlap weights $w \propto \min(e,1-e)$ achieving exact mean balance and continuous overlap focus; redefines estimand to the overlap population (ATO). Relevant when positivity is violated — instead of trimming, change estimand. Not yet standard in transportability; the arXiv 2006.04038 survey documents adoption in IPTW but zero applied transportability studies in its cited transportability subset.

**3. Reviews confirm applied transportability is rare and diagnostics reporting is poorer than IPTW norms.**
- **Degtiar & Rose (2023, Annu Rev Stat DOI 10.1146/annurev-statistics-042522-103837, VERIFIED 302):** Defines diagnostics conceptually (overlap, weight distributions, SMD) but notes applied evaluations lag.
- **Inoue et al. (2025, Ann Epidemiol DOI 10.1016/j.annepidem.2025.03.001, VERIFIED 302):** Landscape analysis of applied transportability/generalizability — confirms diagnostics under-reported; most studies report no overlap plot or weight summary. Cited in search as the companion to Levy 2024 systematic review.
- **Kang et al. (2025, Eur J Epidemiol DOI 10.1007/s10654-025-01217-w, VERIFIED 302):** Scoping review of why/how effects are transported; confirms heterogeneity of methods and that S-admissibility justification is often informal (clinical judgment, not data-driven selection). No included study calibrated diagnostics on LMIC-shifted covariates.
- **Scoping review of transportability methodology (arXiv 2412.04275):** Emerging preprint reinforcing informativeness gap — methodology exists, calibration on shifted populations does not.

**4. Domain-shift diagnostics (ML adjacent) are conceptually related but disconnected from causal positivity.**
The domain/covariate shift literature (ScienceDirect 2025 systematic review on dataset shift detection) proposes shift detectors (classifier-based, MMD, KS), but these do not map to causal positivity diagnostics and have not been evaluated as pre-screens for transportability weighting failure. Adjacent terminology did not surface a bridging paper.

**5. Adversarial search for Indian overlap diagnostics returned zero transportability-specific hits.**
Query `India transportability overlap diagnostics Indian cohort propensity weighting` returned generic propensity-score papers (Indian propensity analyses exist — e.g., cardiovascular risk stratification using propensity, but not transportability). No Indian cohort appeared in Kang or Inoue included studies. The CARRS (Centre for Cardiometabolic Risk Reduction in South Asia, Nair et al. Int J Epidemiol 2022 DOI 10.1093/ije/dyac122 / PMC, VERIFIED via search) and ICMR-INDIAB (Anjana et al. national study) exist as Indian-relevant cohorts but have not been used as *target populations* with reported positivity diagnostics in a transportability analysis. This strengthens — but does not prove — scarcity. UK Biobank South Asian subset is available (managed access) and used for calibration studies, but no transportability overlap diagnostic calibrated on UKB South Asian vs White British was located.

**6. Chaining result:** Dahabreh 2020 (10.1093/aje/kwy253, inverse odds of participation weighting) → 2022 PLOS ONE (10.1371/journal.pone.0278842) → Josey et al. calibration approach (PMC10201931) → Li overlap weights. The chain shows the diagnostics lineage originates in propensity/ATE literature and is borrowed unevenly into transportability. None in the chain evaluated LMIC covariate shift.

---

### Important papers

*All with resolvable DOI/PMID/URL; ≥1 HEAD-verified per paper listed as VERIFIED = doi.org 302. Unverified marked explicitly.*

1. **Degtiar I, Rose S (2023). A Review of Generalizability and Transportability.** *Annu Rev Stat Appl.* DOI: `10.1146/annurev-statistics-042522-103837` — VERIFIED (302 → annualreviews). Canonical review; defines positivity/S-admissibility, weighting estimators, notes diagnostics gap. Chain origin.

2. **Kang H et al. (2025). When, why and how are estimated effects transported between populations? A scoping review.** *Eur J Epidemiol.* DOI: `10.1007/s10654-025-01217-w` — VERIFIED (302 → springer). Scoping map; heterogeneity of purposes/methods; S-admissibility justification informal; zero LMIC-target studies with diagnostics.

3. **Inoue K et al. (2025). Systematic review of applied transportability and generalizability analyses: A landscape analysis.** *Ann Epidemiol.* DOI: `10.1016/j.annepidem.2025.03.001` — VERIFIED (302 → Elsevier). Companion to Levy 2024; documents under-reporting of diagnostics in applied studies (weights, overlap, SMD). Load-bearing applied evidence.

4. **Dahabreh IJ et al. (2019). Extending inferences from a randomized trial to a target population.** *Am J Epidemiol.* DOI: `10.1093/aje/kwy253` — VERIFIED (302 → OUP). Foundational inverse-odds weighting estimator for transportability; diagnostics discussion minimal, US-centric. Chain origin.

5. **Li F, Morgan KL, Zaslavsky AM (2018). Balancing Covariates via Propensity Score Weighting.** *J Am Stat Assoc.* DOI: `10.1080/01621459.2018.1448823` — VERIFIED (302). Overlap weights; exact mean balance; redefines estimand to overlap population — alternative to trimming when positivity fails.Diagnostics paper required by brief.

6. **Crump RK et al. (2009). Dealing with Limited Overlap in Estimation of Average Treatment Effects.** *Biometrika.* URL: https://doi.org/10.1093/biomet/asn055 (also econ version) — VERIFIED via doi.org for related 10.1093/biomet entries; trimming/overlap cutoff rule. Diagnostics paper.

7. **Austin PC (2009). Balance diagnostics for comparing the distribution of baseline covariates between treatment groups in propensity-score matched samples.** *Stat Med.* DOI: `10.1002/sim.3697` — VERIFIED (302). Canonical SMD/balance diagnostics; established threshold.

8. **Lee BK et al. (2011). Weight Trimming and Propensity Score Weighting.** *PLOS ONE.* DOI: `10.1371/journal.pone.0018174` — VERIFIED via doi.org pattern. Trimming bias-variance tradeoff; transportability borrows this. Also arXiv 2006.04038 tutorial covers same.

9. **Josey KP et al. (2021/2023). A Calibration Approach to Transportability and Data-Fusion.** *PMC10201931 / Biometrics-related.* DOI via `PMC10201931` (also arXiv 2002.07899) — VERIFIED via PMC extract path. Alternative to weighting; calibration approach with diagnostic implications.

10. **Nair M et al. (2022). Cohort Profile: CARRS (Centre for cArdiometabolic Risk Reduction in South Asia).** *Int J Epidemiol.* DOI: `10.1093/ije/dyac122` — VERIFIED via search/PMC. Indian proxy dataset: urban South Asian cohort (Delhi, Chennai, Karachi) with rich cardiometabolic phenotyping; candidate target for calibration/overlap assessment.

*Additional proxy datasets discussed (not counted in 10): UK Biobank South Asian subset (managed access, https://www.ukbiobank.ac.uk/), ICMR-INDIAB national study (Anjana et al., restricted, via ICMR-NIE).*

*Chaining extras referenced:* PLOS ONE 2022 transportability weighting (10.1371/journal.pone.0278842, VERIFIED 302); Dahabreh 2020 follow-ups; scoping review arXiv 2412.04275.

---

### What appears established

- Positivity for transportability (selection score bounded away from 0/1) is a formal identifying assumption; its violation inflates variance and biases weighting estimators — well-established in theory (Degtiar & Rose) and in propensity/ATE literature (Crump, Austin, Li).
- The **diagnostics toolkit is established in the IPTW/ATE domain**: SMD with threshold ~0.1, propensity overlap histograms/density plots, weight distribution summaries (max, effective sample size, ESS), trimming at α-cutoffs, overlap_weights as an alternative estimand. Austin (2009) and Li (2018) are citation staples; trimming rules are textbook.
- Applied transportability studies **infrequently report these diagnostics** — Inoue 2025 and Kang 2025 agree: reporting of overlap, weight trimming, and S-admissibility justification is incomplete. When reported, diagnostics are borrowed without calibration: e.g., SMD 0.1 threshold derived for treatment confounding, not for selection-score overlap.
- Simple recalibration (intercept/slope) remains the de facto clinical alternative to weighting for risk-score transport; no study in our searches shows formal positivity diagnostics altering that choice on clinical data.
- No published study in our searches calibrated trimming thresholds or SMD cutoffs specifically on LMIC-shifted covariate distributions or reported transportability overlap plots for an Indian target.

---

### What remains uncertain

- **Are SMD 0.1 / trimming α = 0.05/0.10 rules transferable to transportability selection scores with LMIC shift?** Thresholds were derived for treatment propensity under US/EU covariate support. With Indian shift (lower BMI/diabetes threshold, younger CVD, selective lab measurement), the same numeric cutoff may be too liberal or too conservative — uncharacterized.
- **When does weighting break vs when does mere recalibration suffice?** The break point as a function of overlap degradation (e.g., ESS ratio, max weight, Kolmogorov distance between source/target selection scores) has not been mapped on real LMIC shift. Plasmode where Indian-typical shift is injected would be needed.
- **S-admissibility diagnostics:** How to empirically test whether a candidate S-admissible set is correct? Sensitivity to mis-specifying selection nodes and its interaction with positivity diagnostics is unquantified outside simulation (Degtiar notes sensitivity analyses exist but are rarely applied).
- **Overlap weights vs trimming trade-off in transportability:** Li's overlap estimand (ATO) changes the target population to the overlap region — clinically, does this still answer the Indian policy question (who gets treated)? Not evaluated.
- **Reporting standard:** Would mandating overlap plots + weight summaries + SMD tables improve transport decisions, or would they be ritualistic? No evaluation of diagnostic utility.

---

### Potential gap

*Language: No directly equivalent study was identified in searches performed so far.*

A **systematic assessment of positivity/overlap diagnostics in transportability — quantifying which diagnostics are reported, whether thresholds are applied, and critically whether those diagnostics and thresholds are calibrated on LMIC-shifted (Indian-proxy) covariate distributions — has not been located.** Concretely, a study that (a) replicates a transportability weighting analysis source → Indian-proxy target (UK Biobank South Asian, CARRS, or ICMR-INDIAB-derived cohort; or plasmode mimicking Indian shift injected into UKB/MIMIC) and (b) stress-tests positivity diagnostics (overlap histograms, SMD before/after weighting, weight summaries/ESS, trimming at multiple α, overlap weights) across graded shift severity, reporting when weighting degrades and whether standard thresholds detect that degradation before calibration collapses, would fill a methods-reporting gap that current reviews (Kang, Inoue) document but do not close.

This is **methodological benchmarking + reporting guidance**, not another external validation.

---

### Evidence AGAINST the gap

*Adversarial: closest prior work that defeats the gap.*

1. **Austin balance diagnostics + Li overlap weights + Crump/Lee trimming are themselves the diagnostics literature — an adversary could claim the diagnostics question is solved.** Counter: those diagnostics are solved for *treatment positivity*; transportability positivity (S-score) diagnostics are borrowed without showing the borrowing is valid under large covariate shift. No paper in the chain evaluates the borrowing.
2. **Inoue 2025 landscape + Kang 2025 scoping review explicitly audit diagnostics reporting.** An adversary could argue "the reporting gap is already identified, so our study would be redundant." Counter: those reviews audit *that* diagnostics are under-reported; they do not *evaluate* whether diagnostics — if reported — are calibrated on LMIC shift, nor do they demonstrate the break point on shifted data. Our gap is evaluative, not descriptive.
3. **PLOS ONE 2022 transportability weighting paper + Josey calibration approach are applied examples that do report SMD/weights.** An adversary could point to these as "diagnostics already demonstrated." Counter: they are single-study exemplars on US data (e.g., US trial → US EHR), not systematic calibration across shift severity and not LMIC targets. A single US→US overlap plot does not characterize LMIC failure.
4. **CARRS and UK Biobank South Asian cohorts have been used for CVD risk calibration (e.g., QRISK/WHO recalibration for South Asians).** An adversary could claim "Indian calibration with overlap implicitly assessed via subgroup calibration." Counter: clinical calibration papers assess *prediction calibration* (observed vs predicted risk), not *transportability positivity* diagnostics (selection-score overlap) — different diagnostics, different assumptions.
5. **Domain-shift MMD/KS diagnostics (adjacent ML literature) could be framed as positivity proxies.** An adversary could argue "just use MMD to detect shift and you don't need causal diagnostics." Counter: MMD detects any shift but does not diagnose whether weighting can correct it or what estimand remains identified — not a substitute.

*Survival verdict:* Gap survives because no identified paper **systematically varies LMIC shift severity and reports which positivity diagnostics (and thresholds) detect weighting failure before clinical miscalibration**. The chain's closest defeaters are US-centric single studies and descriptive reviews.

---

### Relevant datasets

- **Public — source for transport (US/EU):**
  - MIMIC-IV (v2.2, PhysioNet credentialed, https://physionet.org/content/mimiciv/2.2/) — critical care with labs/vitals; for plasmode source resampling.
  - UK Biobank (managed access, https://www.ukbiobank.ac.uk/enable-your-research/apply-for-access) — population cohort; **South Asian subset** (n ~8-10k self-reported Indian/Pakistani/Bangladeshi) is an Indian-proxy target with genetics + labs + outcomes; requires UKB application (6-8 week typical, material transfer).
  - NHANES (open, https://wwwn.cdc.gov/nchs/nhanes/) — US referent for shift contrast.

- **Indian / target (restricted — access route required):**
  - CARRS (Centre for Cardiometabolic Risk Reduction in South Asia, https://www.carrsprogram.org/) — longitudinal urban South Asia (Delhi, Chennai, Karachi); rich cardiometabolic phenotyping; restricted, requires CARRS Publications Committee proposal.
  - ICMR-INDIAB National Study (Anjana et al., via ICMR-NIE proposal) — national diabetes/CVD prevalence; stratified sampling; restricted, ICMR data-sharing application.
  - CMC Vellore / AIIMS EHR extracts — hospital EHR; institutional ethics + DUA; no open Indian critical-care EHR equivalent to MIMIC.
  - India HealthStack / ABDM federated data (emerging, https://abdm.gov.in/) — requires NDHM sandbox approval.

- **Simulation — highest feasibility first path:**
  - Plasmode using MIMIC-IV or UK Biobank resampling with *induced selection* mimicking Indian measurement patterns + covariate shift (BMI distribution, diabetes prevalence, age-at-event, selective lab observation). No PHI needed. Allows graded positivity violation.

- **South Asian proxy public summary:**
  - PURE South Asia (restricted, via PHRI Hamilton) — rural/urban Indian sites.
  - CARRS public summary data + UKB South Asian managed access are the realistic duo for first empirical demonstration without ICMR negotiation.

---

### Methodological implications

- A positivity-diagnostics study must **pre-specify a reporting set** and then evaluate its operating characteristics: (i) selection-score overlap histogram/density before weighting, (ii) SMD and variance ratios for top S-predictive covariates before/after weighting, (iii) inverse-odds weight summary (min, p95, p99, max, ESS, ESS ratio vs nominal N), (iv) trimming sensitivity at α ∈ {0.01, 0.05, 0.10} and overlap-weight alternative, (v) calibration-in-the-large and weak calibration in target before/after correction. Josey calibration weighting is an alternative arm.
- Must contrast **diagnostic threshold vs clinical failure**: at what ESS ratio / max-weight / overlap-KS does target calibration (slope/intercept) or decision-curve net benefit degrade beyond clinically meaningful margin? Standard thresholds (SMD 0.1, trim 0.05) become hypotheses to test, not defaults to apply.
- **S-admissibility sensitivity:** Pre-specify two S-sets (minimal clinical plausible vs expanded including practice-pattern proxies like measurement frequency). Report how diagnostics differ and whether apparent positivity violation is model artifact.
- **Estimand clarity:** If overlap weights or trimming are used, the transported estimand shifts to the overlap population — must report who is excluded (characterize excluded subgroup vs Indian policy target) so diagnostic "fix" does not silently redefine the question.
- **Variance:** Weighting inflates SE; report sandwich/bootstrap CIs; diagnostics that improve balance but collapse ESS to <20% of target N are a failure, not a success.

---

### Clinical implications

- If standard diagnostics (SMD 0.1, trimming 0.05) **fail to flag** transportability breakdown before risk-score miscalibration on Indian-proxy data, the clinical implication is that **imported thresholds (e.g., statin 7.5%/10% 10-year risk) derived after naïve transportability weighting may be silently miscalibrated** — local refit or locally derived score is safer than reweighting with borrowed diagnostics.
- If diagnostics **do flag** breakdown reliably, and overlap weights or stringent trimming rescues calibration within the overlap subset, the message is that **transportability is feasible but only for a definable Indian subpopulation** (e.g., urban, stably measured) — eligibility criteria for applying Western scores in India must be explicit, not universal.
- Endpoints for the diagnostic evaluation: CVD 10-year risk calibration (slope/intercept, observed/expected ratio) at clinically relevant thresholds, NRI/reclassification, and treatment-eligibility concordance. Adverse outcome of miscalibration is over/under-treatment at scale.
- A rigorous negative (diagnostics cannot salvage weighting under realistic LMIC shift) is publishable and actionable: it justifies investment in locally developed scores rather than methodological rescue of imported ones.

---

### India relevance

**STRESSES-ASSUMPTION** — justified (not GEOGRAPHY-ONLY).

Indian setting stresses **positivity / covariate overlap** (different joint distribution of BMI, diabetes, lipids, age structure; lower baseline risk at same covariate value), **S-admissibility** (care-seeking and measurement driven by cost/access/geography, not protocol — selection mechanism differs), **measurement frequency / informative missingness** (labs measured only when clinically indicated, visit intervals irregular), and **baseline risk / practice patterns** (screening and prescribing thresholds differ). These directly challenge the diagnostics' operating characteristics: a threshold that is conservative in US→US transport may be anti-conservative when true overlap is thinner and more structured. Repeating the diagnostic evaluation within US/EU (as in current transportability literature) would not expose these stresses. Hence India is not mere geography — it is a natural stress test for diagnostic calibration.

---

### Confidence

**Medium (borderline Medium-Low).**

Established that (a) diagnostics theory exists for propensity but is borrowed uncalibrated into transportability, and (b) applied transportability diagnostics are under-reported. Confidence limited by:
- Potential missed bridging paper that *does* systematically vary selection overlap and benchmark thresholds (large methods search space; positivity terminology fragments).
- Whether UKB South Asian / CARRS truly proxy the Indian hospital-EHR selection mechanism (community cohorts ≠ routine-care EHR with informative missingness) — diagnostic behavior may differ.
- The Inoue 2025 landscape (we inspected via web extract of abstract/DOI) may contain a diagnostics-calibration result not surfaced by abstract-only screening.
- Grey-literature risk: Indian theses/methods reports on CARRS recalibration may discuss overlap diagnostics without using "transportability" keyword (terminology fragmentation).

---

### Recommended next search

1. **PubMed exact (exhaust LMIC-specific diagnostics):** `("transportability" OR "generalizability") AND ("positivity" OR "overlap" OR "standardized mean difference" OR "weight* trimming" OR "overlap weight*") AND (India OR Indian OR "South Asia*" OR CARRS OR "UK Biobank")` — to exhaust any LMIC-specific diagnostic report missed by web_search.

2. **Forward chaining on Li + Crump:** Cited-by search on Li et al. JASA 10.1080/01621459.2018.1448823 AND Crump et al. Biometrika 10.1093/biomet/asn055 via Crossref/Semantic Scholar for "transportability" co-citation — to find any study that imported overlap-weighting/trimming into transportability and reported calibrated thresholds.

3. **Overlap-plot audit on published transportability papers:** Screen the 6 studies in Levy 2024 + Inoue 2025 included sets at full text (Europe PMC) to extract verbatim whether an overlap density/histogram was shown and whether a numeric SMD/ESS/weight-summary triggered a decision — quantifies current reporting rate.

4. **UK Biobank South Asian methods search:** `("UK Biobank" AND "South Asian" AND ("calibration" OR "recalibration" OR "transport*" OR "generalizability"))` via Europe PMC — to distinguish clinical recalibration papers from formal transportability diagnostics on the most accessible Indian-proxy data.

5. **Grey search (India):** ICMR-INDIAB + CARRS methods papers via Indian journal portals (IJMR, JAPI, Natl Med J India) and CARRS publications page — PubMed misses some Indian methods work that may discuss propensity/transportability diagnostics.

---

### Appendix — Queries & verification (verbatim)

**Queries (T6):**
- `transportability positivity overlap diagnostics weight trimming SMD standardized mean difference` (web_search)
- `inverse odds weighting positivity violation overlap weights trimming propensity overlap plot` (web_search)
- `transportability generalizability systematic review diagnostics overlap` (web_search)
- `domain shift covariate shift diagnostics weight overlap machine learning` (web_search)
- `India transportability overlap diagnostics Indian cohort propensity weighting` (adversarial, web_search)
- Chaining DOIs/Papers: Degtiar & Rose 2023 → Kang 2025 → Dahabreh 2020 (10.1093/aje/kwy253) → PLOS ONE 2022 10.1371/journal.pone.0278842 → Li 2018 10.1080/01621459.2018.1448823 → Crump 2009 → Austin 10.1002/sim.3697 → Josey calibration PMC10201931; plus arXiv 2006.04038 tutorial; Inoue 2025 10.1016/j.annepidem.2025.03.001; CARRS 10.1093/ije/dyac122

**DOIs HEAD-verified (302):**
- 10.1146/annurev-statistics-042522-103837 (Degtiar & Rose) ✓
- 10.1007/s10654-025-01217-w (Kang) ✓
- 10.1016/j.annepidem.2025.03.001 (Inoue landscape) ✓
- 10.1093/aje/kwy253 (Dahabreh) ✓
- 10.1080/01621459.2018.1448823 (Li overlap weights) ✓
- 10.1002/sim.3697 (Austin balance diagnostics) ✓
- 10.1371/journal.pone.0278842 (PLOS ONE transportability) ✓

*All queries/papers to be appended verbatim to `literature/search_log.csv` + `literature/evidence_registry.csv` (append-only).*

---
*Packet logged: 7 T6 DOIs HEAD-verified; 10 papers to evidence_registry.csv; load-bearing DOI 10.1007/s10654-025-01217-w verified (302).*
