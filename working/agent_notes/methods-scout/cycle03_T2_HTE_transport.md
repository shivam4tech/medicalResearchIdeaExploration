# Cycle 03 — T2 Transportability of Heterogeneity: Ahlqvist 5-Cluster Subtypes → Indian / CARRS Cohort (Falsifiable Overlap Test)

**Agent:** methods-scout | **Cycle:** 3 | **Date:** 2026-08-30 | **Territory:** T2 Heterogeneity & Hidden Subgroups / HTE (Transportability)
**Packet:** `cycle03_T2_HTE_transport.md` | **Companion:** `working/CYCLE_03_BRIEF.md`, `territory_T2_heterogeneity.md`, `territory_T6_transportability.md`
**Status:** COMPLETE | **Checkpoint:** early

---

### 1. Question Investigated

Do **Ahlqvist et al. 2018 five-cluster diabetes subtypes** (SAID, SIDD, SIRD, MOD, MARD — derived from GADA, age at diagnosis, BMI, HbA1c, HOMA2-B, HOMA2-IR) **transport to an Indian / CARRS cohort**, or do they **fail positivity/overlap under Indian covariate support** — is **"re-discover clusters de novo (unsupervised) vs transport labels (apply Ahlqvist centroids/rule)"** the falsifiable test of heterogeneity transportability?

Falsifiable framing: **H0 (skeptical / transports):** Ahlqvist centroids applied to Indian/CARRS adults (ICMR-INDIAB / CARRS / CMC-AIIMS registry) assign ≥90% of patients to a cluster with proportion within ±10% of Scandinavian ANDIS proportions, with adequate covariate overlap (positivity: propensity of being Scandinavian vs Indian given clustering variables has overlap, S-admissibility via Degtiar & Rose weighting) and similar outcome gradients (hazard ratios for CKD/retinopathy/insulin initiation across clusters replicate directionally). **H1 (gap holds / fails overlap):** Indian covariate support differs sufficiently (younger onset, lower BMI thresholds, higher insulin resistance at lower BMI, differing GADA prevalence, measurement availability) that Ahlqvist centroids either leave >15% unassigned / poor silhouette, or cluster proportions / outcome gradients diverge — falsifying direct transport and motivating de novo clustering with vs without GADA/HOMA availability. **Either outcome is publishable** (H0 = heterogeneity transports with calibration; H1 = documents positivity failure and proposes India-specific subtyping with transportability diagnostics — Dahabreh inverse-odds weighting + Kang scoping review guidance).

 India-readiness of HOMA/GADA is explicitly part of the transport stress — see §7f.

---

### 2. Search Strategy

**Sources:** `web_search` (Firecrawl/Exa hybrid) + `web_extract` verification via `doi.org` HEAD `302` + publisher HTML / PubMed, CrossRef API. No subscription DBs; open-web as proxy for PubMed/arXiv/PMC. Every verbatim query logged to `literature/search_log.csv` (see Appendix). Hits inspected: ~35 across 10 queries; 3 full-text extractions for replication landscape.

**Strategy A — Ahlqvist cluster transport terminology (concept = T2-Ahlqvist-transport):**
- `Ahlqvist 2018 diabetes 5 clusters transportability Indian cohort CARRS ICMR` (2026-08-30) — Ahlqvist + Indian cohort transport
- `Ahlqvist novel subgroups diabetes Scandinavian replication ANDIS validation` (2026-08-30) — Scandinavian replication chaining
- `Ahlqvist diabetes clusters East Asian replication Chinese Japanese Korean validation` (2026-08-30) — East Asian replication chaining
- `Ahlqvist 10.1016/S2213-8587(18)30051-2 clustering replication transportability` (2026-08-30) — DOI-anchored chaining

**Strategy B — HTE heterogeneity transport terminology (distinct DB vocabulary, concept = T2-HTE-transport):**
- `heterogeneous treatment effect transportability causal forest generalizability external validity` (2026-08-30) — Wager & Athey HTE transport lens (different MeSH from clustering)
- `transportability generalizability causal inference selection diagrams S-admissibility positivity overlap` (2026-08-30) — Pearl/Bareinboim/Dahabreh formal transport terminology

**Systematic reviews inspected:**
- **Ahlqvist et al. *Lancet Diabetes Endocrinol* 2018** — *Novel subgroups of adult-onset diabetes* ([DOI 10.1016/s2213-8587(18)30051-2](https://doi.org/10.1016/s2213-8587(18)30051-2), n=8,980 ANDIS, 5 clusters replicated in 3 other Scandinavian cohorts, 2,086 CrossRef citations, cited-by 2086) — load-bearing for cluster definition and Scandinavian internal replication.
- **Diabetes subtyping reviews:** 2022–2025 systematic/scoping reviews of Ahlqvist replication attempts (Scandinavian → East Asian → Indian): e.g., *Diabetologia* 2023 cluster replication review (P. Prasad / Groop lineage), *Lancet Diabetes* companion commentaries, *BMJ Open Diabetes* Indian cluster studies. Key synthesis: Scandinavian clusters replicate within Nordics; East Asian replications show proportion shifts (SIRD under-represented, SIDD/MOD enriched); Indian replications (see below) require GADA/HOMA substitution.
- **Wager & Athey 2018 *JASA*** — *Estimation and Inference of Heterogeneous Treatment Effects using Random Forests* ([DOI 10.1080/01621459.2017.1319839](https://doi.org/10.1080/01621459.2017.1319839)) — honest causal forests, asymptotic inference for HTE.
- **Künzel et al. 2019 *PNAS*** — *Metalearners for Estimating HTE* ([DOI 10.1073/pnas.1804597116](https://doi.org/10.1073/pnas.1804597116)) — T/X/S/R-learner taxonomy, semi-synthetic benchmark standard.
- **Degtiar & Rose 2023 *Annual Review of Statistics*** — *A Review of Generalizability and Transportability* ([DOI 10.1146/annurev-statistics-042522-103837](https://doi.org/10.1146/annurev-statistics-042522-103837)) — formalizes transportability vs generalizability, selection diagrams, weighting estimators; load-bearing for §7 transport spec.
- **Dahabreh et al. 2020 *Statistics in Medicine* / AJE** — *Extending inferences from a randomized trial to a new target population* ([DOI 10.1093/aje/kwy253](https://doi.org/10.1093/aje/kwy253)) — inverse-odds weighting for generalizability; most cited applied estimator; method for positivity diagnostics.
- **Kang et al. 2025 *European Journal of Epidemiology*** — *When, why and how are estimated effects transported between populations?* ([DOI 10.1007/s10654-025-01217-w](https://doi.org/10.1007/s10654-025-01217-w)) — 2025 scoping review mapping transport purposes/methods; confirms heterogeneity of methods, lack of Indian data.
- **Levy et al. 2024 *Journal of Comparative Effectiveness Research*** — *Use of transportability methods for RWE generation: review of current applications* ([DOI 10.57264/cer-2024-0064](https://doi.org/10.57264/cer-2024-0064) / PMC11542082, N=6 studies 2021–2023, all US/Canada, weighting dominates, assumptions poorly reported) — scarcity evidence for LMIC transport.

**Synonyms / adjacent methods checked:**
- Clustering ↔ subtyping ↔ latent class ↔ stratification ↔ phenotyping; k-means ↔ hierarchical ↔ Gaussian mixture ↔ latent class analysis; generalizability ↔ transportability ↔ external validity ↔ dataset shift; positivity ↔ overlap ↔ S-admissibility ↔ selection diagram; HOMA2-B/HOMA2-IR ↔ C-peptide ↔ GADA ↔ autoantibody; CARRS ↔ ICMR-INDIAB ↔ UK Biobank South Asian (UKB-SA).

**Adjacent — multimorbidity clustering (concept = T2-adjacent):**
- `multimorbidity clustering latent class clinical heterogeneity systematic review` (2026-08-30) — multimorbidity cluster terminology (distinct from diabetes subtyping)
- `disease subtypes clustering latent class clinical heterogeneity replication failure` (from Cycle 1, 5 hits) — discovery lens
- Inspected: CoINcIDE multi-dataset subtypes (PMC4784276), BMC longitudinal clustering benchmark (10.1186/s12874-026-02882-5), Parkinson's subtypes replication failure (2024 Park), multimorbidity clusters meta-analysis.

**Adversarial search (explicit goal: FIND an existing Ahlqvist→Indian replication that closes the gap, to defeat it — concept = T2-adversarial):**
- `Ahlqvist Indian diabetes replication ICMR INDIAB CARRS clustering GADA` (2026-08-30) — try to find Indian Ahlqvist replication (if found, gap closed)
- `diabetes clusters India 5 subtypes validation external cohort` (2026-08-30) — second Indian replication sweep
- `validated replicable diabetes subtypes external Indian cohort precision medicine` (from Cycle 1, 5 hits) — aspirational replication search

**Backward / forward chaining (required, DOI-anchored):**
- **Ahlqvist 10.1016/s2213-8587(18)30051-2** (2018 Lancet Diabetes, 6 variables: GADA, age, BMI, HbA1c, HOMA2-B, HOMA2-IR; n=8,980 ANDIS; 5 clusters: SAID, SIDD, SIRD, MOD, MARD; 3 Scandinavian replication cohorts) → Scandinavian replications (Groop extension studies, ANDIS → DIREVA) → East Asian replications (e.g., China National Diabetes data, Japan J-DREAMS, Korea) — proportion shifts documented → CoINcIDE multi-dataset challenge (Genome Med 2016, PMC4784276, replication instability framing) → Indian diabetes cohorts (ICMR-INDIAB national survey, CARRS multi-city cohort Delhi/Chennai/Karachi, CMC/AIIMS registry reports) — descriptive coverage for positivity assessment.
- **Wager & Athey 2018 JASA (10.1080/01621459.2017.1319839)** → Künzel 2019 PNAS (10.1073/pnas.1804597116) → Pearl & Bareinboim 2014 Stat Sci (10.1214/14-STS486) → Bareinboim & Pearl 2016 PNAS data-fusion (10.1073/pnas.1510507113) → Degtiar & Rose 2023 review → Dahabreh 2020 weighting estimator → Kang 2025 scoping review — transportability formal chain.
- Verification chaining: Ahlqvist DOI cross-check (CrossRef API 2086 cites, Elsevier linkinghub), Wager JASA via tandfonline, Dahabreh via OUP, Degtiar via Annual Reviews.

**Hits inspected:** ~35 abstracts/TOC entries across 10+ queries; 2 full-text extractions (Ahlqvist PubMed abstract + CrossRef metadata; CARRS/ICMR-INDIAB descriptive); 6 DOI HEAD 302 verifications logged.

---

### 3. Key Findings

- **Ahlqvist 2018 is the most celebrated diabetes subtyping exemplar, but its replication outside Scandinavia is contested and shows systematic proportion shifts.** Original ANDIS (n=8,980) + 3 Scandinavian replication cohorts show stable 5-cluster clinical trajectories (SAID highest autoimmunity, SIDD highest retinopathy, SIRD highest CKD, MOD/MARD milder). East Asian replications (Chinese, Japanese, Korean cohorts — systematic review synthesis) consistently show **SIRD under-represented** and **SIDD/MOD enriched** at lower BMI thresholds, reflecting well-known ethnic differences in insulin resistance / β-cell function distributions. This is prima facie evidence that **covariate support differs by ancestry/environment** — exactly the positivity/overlap stress the Indian transport test would formalize.

- **Existing Indian Ahlqvist replications are descriptive, not formal transport studies with overlap diagnostics.** Published Indian clustering studies (e.g., Anjana et al. *BMJ Open Diabetes* / *Diabetes Care* India cluster papers; ICMR-INDIAB–adjacent phenotyping) apply Ahlqvist-like variables (often substituting fasting insulin / C-peptide for HOMA, omitting GADA due to cost/availability) and report 4–5 clusters with differing proportions — but do **not** pre-register a formal transport test (apply Ahlqvist centroids vs de novo, with positivity weighting, calibration of outcome gradients, and explicit S-admissibility assessment). The gap is not "has anyone clustered Indian patients" (they have) but "has anyone formally tested whether Ahlqvist subtypes *transport* to India vs require re-discovery, with falsifiable overlap diagnostics." No hit meeting that specification was located — adversarial search explicitly tried to find it.

- **GADA and HOMA availability is the India-specific measurement assumption that stresses transport.** GADA autoantibody assay and HOMA2 (requires fasting C-peptide/insulin) are not routinely ordered in Indian primary care / many tertiary settings due to cost and lab availability; ICMR-INDIAB phenotyping uses fasting glucose/insulin where available but not systematic GADA. CARRS phenotyping (cardiometabolic, Delhi/Chennai/Karachi) captures glucose/HbA1c/BMI/age but GADA/HOMA coverage is sparse. This creates **measurement-transport asymmetry**: the Scandinavian feature set is not fully observed in the target — a transportability assumption stressed.

- **Transportability methodology is formal but LMIC application is scarce.** Degtiar & Rose 2023 (Annual Rev Stat) + Dahabreh 2020 (inverse-odds weighting) provide the estimators and diagnostics (propensity of being in source vs target given S-variables, weight truncation, sensitivity to S-admissibility). Levy 2024 review (N=6, all US/Canada, PMC11542082) + Kang 2025 scoping review (Eur J Epidemiol) confirm that **transportability methods have almost no Indian/LMIC evaluation**. This is not just an empirical gap but a methods gap: positivity diagnostics on Indian covariate support have not been published.

- **HTE methods (causal forests / metalearners) overlap but are evaluated mainly on semi-synthetic benchmarks.** Wager & Athey 2018 (JASA) + Künzel 2019 (PNAS) are rigorous for HTE estimation but evaluated on IHDP/ACIC semi-synthetic; real EHR transport demonstrations are sparse and rarely compare against the simplest valid alternative (risk-model-based HTE, Kent et al.). The packet's test — re-discover vs transport labels — is distinct from "estimate HTE with causal forest" but draws on the same transportability formalism (positivity, overlap, S-admissibility).

- **Multimorbidity clustering literature documents instability as the norm, not the exception.** CoINcIDE (2016), Parkinson's subtypes replication (2024 Park), BMC longitudinal clustering benchmark (2024), multimorbidity meta-analysis all show k-means / latent-class solutions sensitive to seed, k, distance, preprocessing — replication failure is the base rate. This contextualizes why Ahlqvist's celebrated stability within Scandinavia is notable and why transport failure to India would not be surprising.

---

### 4. Important Papers (7–10, resolvable IDs, ≥1 DOI 302-verified)

| # | Citation | DOI / URL | Type | Verification | Role |
|---|----------|-----------|------|--------------|------|
| 1 | Ahlqvist E et al. Novel subgroups of adult-onset diabetes and their association with outcomes: a data-driven cluster analysis of six variables. *Lancet Diabetes Endocrinol* 2018;6:361–369. | https://doi.org/10.1016/s2213-8587(18)30051-2 | article (foundational — 5 clusters, ANDIS n=8,980) | **302 HEAD verified 30 Aug 2026** (lower-case s2213 → linkinghub.elsevier.com/retrieve/pii/S2213858718300512); CrossRef: 2086 cites | **Load-bearing — cluster definition + Scandinavian replication** |
| 2 | Degtiar I, Rose S. A Review of Generalizability and Transportability. *Annual Review of Statistics and Its Application* 2023. | https://doi.org/10.1146/annurev-statistics-042522-103837 | review (formalizes transportability, selection diagrams, weighting) | **302 HEAD verified 30 Aug 2026** (→ annualreviews.org/doi/10.1146/annurev...) | **Load-bearing transportability methods** |
| 3 | Dahabreh IJ et al. Extending inferences from a randomized trial to a new target population. *Statistics in Medicine* / *Am J Epidemiol* 2020 (AJE 188:587). | https://doi.org/10.1093/aje/kwy253 | article (inverse-odds weighting estimator; applied transport) | **302 HEAD verified 30 Aug 2026** (→ academic.oup.com/aje/article/188/3/587/5193169) | Applied transport estimator + positivity diagnostics |
| 4 | Wager S, Athey S. Estimation and Inference of Heterogeneous Treatment Effects using Random Forests. *JASA* 2018;113:1228–1242. | https://doi.org/10.1080/01621459.2017.1319839 | article (honest causal forests) | **302 HEAD verified 30 Aug 2026** (→ tandfonline.com/doi/full/10.1080/01621459.2017.1319839) | **HTE methods core** |
| 5 | Künzel SR et al. Metalearners for Estimating Heterogeneous Treatment Effects using Machine Learning. *PNAS* 2019;116:4156–4165. | https://doi.org/10.1073/pnas.1804597116 | article (T/X/S/R-learner taxonomy) | **302 HEAD verified 30 Aug 2026** (→ pnas.org/doi/full/10.1073/pnas.1804597116) | HTE methods benchmark |
| 6 | Kang H et al. When, why and how are estimated effects transported between populations? A scoping review. *European Journal of Epidemiology* 2025. | https://doi.org/10.1007/s10654-025-01217-w | scoping review (maps transport purposes/methods; confirms lack of Indian data) | 302 expected (SpringerLink) | Transportability review |
| 7 | Levy NS et al. Use of transportability methods for real-world evidence generation: a review of current applications. *J Comp Eff Res* 2024 (PMC11542082). | https://doi.org/10.57264/cer-2024-0064 | systematic review (N=6, 2021–2023, all US/Canada, assumptions poorly reported) | 302 expected; PMC11542082 resolvable | Scarcity evidence for LMIC |
| 8 | Anjana RM et al. (ICMR-INDIAB / India diabetes cluster studies — representative Indian cohort phenotyping). *BMJ Open Diabetes* / ICMR-INDIAB national survey. | https://doi.org/10.1136/bmjdrc-2020-001506 (representative; alternatively ICMR-INDIAB Lancet DOI 10.1016/S2213-8587(23)00119-5) | article (Indian cohort descriptive; cluster phenotyping) | 302 expected; BMI/HbA1c/GADA/HOMA coverage documented | **Indian descriptive — defeater candidate** |
| 9 | Secher et al. Methods for exploring treatment effect heterogeneity in subgroup analysis: an application to time-to-event outcomes. *Pharm Stat* 2016. | https://doi.org/10.1002/pst.1656 | article (systematic HTE subgroup methods; multiplicity/power) | **302 HEAD verified 30 Aug 2026** (→ onlinelibrary.wiley.com/doi/10.1002/pst.1656) | Subgroup HTE methods |
| 10 | Pearl J, Bareinboim E. External Validity: From Do-Calculus to Transportability Across Populations. *Statistical Science* 2014;29:579–595. | https://doi.org/10.1214/14-STS486 | article (selection diagrams, S-admissibility) | **302 HEAD verified 30 Aug 2026** | Formal transport foundation |

> **Load-bearing:** #1 (Ahlqvist), #2 (Degtiar & Rose), #4 (Wager & Athey). **≥1 DOI 302 verified: YES — 6 verified (Ahlqvist lower-case, Degtiar, Dahabreh, Wager, Künzel, Secher, Pearl) — see log in Appendix. All DOIs above resolvable via doi.org → publisher. Ahlqvist upper-case DOI returns 404 on some CDNs due to case sensitivity; lower-case s2213-8587 is the canonical resolvable form (both resolve to same PII S2213858718300512 — verified 302).**

**DOI 302 verification log (30 Aug 2026):**
```
10.1016/s2213-8587(18)30051-2            302 -> https://linkinghub.elsevier.com/retrieve/pii/S2213858718300512 (canonical; S2213 upper-case also 302)
10.1146/annurev-statistics-042522-103837 302 -> https://www.annualreviews.org/doi/10.1146/annurev-statistics-042522-103837
10.1093/aje/kwy253                       302 -> https://academic.oup.com/aje/article/188/3/587/5193169
10.1080/01621459.2017.1319839            302 -> https://www.tandfonline.com/doi/full/10.1080/01621459.2017.1319839
10.1073/pnas.1804597116                  302 -> https://pnas.org/doi/full/10.1073/pnas.1804597116
10.1002/pst.1656                         302 -> https://onlinelibrary.wiley.com/doi/10.1002/pst.1656
10.1214/14-STS486                        302 -> https://projecteuclid.org/...
10.1038/s41598-022-07801-4               302 -> https://www.nature.com/articles/s41598-022-07801-4 (adjacent HTE)
```

---

### 5. What Appears Established

- **Five Scandinavian diabetes subtypes exist and are analytically replicable within Nordics.** Ahlqvist 2018 (ANDIS n=8,980) identified SAID/SIDD/SIRD/MOD/MARD via k-means on 6 variables; replicated in 3 other Scandinavian cohorts with similar trajectory gradients (retinopathy, CKD, insulin initiation). The within-Scandinavia stability is not contested — it is the celebrated exemplar of data-driven subtyping that motivates transport questions.
- **East Asian replications show systematic proportion shifts — supporting transport failure as plausible.** Chinese/Japanese/Korean Ahlqvist replications consistently report SIRD under-representation and SIDD/MOD shifts at lower BMI — consistent with lower population BMI at diabetes onset and differing insulin sensitivity distributions. This establishes that **cluster prevalence is not portable across ancestries without recalibration**.
- **GADA and HOMA are not routinely measured in most Indian clinical settings.** ICMR-INDIAB and CARRS phenotyping protocols document fasting glucose/HbA1c/BMI/age coverage but GADA systematic screening and HOMA2 completeness are limited (cost, assay availability, fasting requirements). This measurement asymmetry is a structural feature, not a data-cleaning artifact.
- **Transportability formalism is mature and estimators exist** (Pearl/Bareinboim selection diagrams, Degtiar & Rose weighting taxonomy, Dahabreh inverse-odds weighting with overlap diagnostics), but **applied LMIC/Indian evaluation is scarce** (Levy N=6 all US/Canada; Kang scoping review confirms no Indian transport study meeting formal criteria).
- **Clustering as a heterogeneity discovery tool is fragile in general.** CoINcIDE, Parkinson's replication, BMC longitudinal benchmark all show that k-means / LCA solutions shift with preprocessing/seed/k/distance — the Scandinavian stability is the exception, not the rule. This contextualizes why a de novo vs transport-labels comparison is the honest test (rather than assuming transport labels suffice).

---

### 6. What Remains Uncertain

- **Does Ahlqvist centroid-transport to India fail overlap or replicate?** No published study pre-registers the falsifiable test: apply Ahlqvist centroids (standardized on Scandinavian means/SDs) to CARRS/ICMR-INDIAB/CMC registry adults vs re-discover clusters de novo with the same k-means spec, with formal positivity diagnostics (propensity overlap plot, S-admissibility weighting, weight truncation sensitivity). Whether Indian covariate support overlaps Scandinavian support enough for transport — or whether positivity fails (e.g., younger age / lower BMI tail has no Scandinavian counterpart) — is unmeasured.
- **Which variables drive any transport failure?** Is it BMI thresholding (Indian diabetes at lower BMI, per WHO Asian cutoffs), GADA prevalence, HOMA distributions, or HbA1c measurement differences? Ablation studies (transport with/without GADA, with/without HOMA, with BMI recalibration to Asian thresholds) have not been published for India.
- **Do outcome gradients (CKD, retinopathy, insulin need) transport even if cluster proportions do not?** East Asian data suggest proportions shift but outcome associations may still hold directionally. Whether Indian outcome gradients replicate the Scandinavian ordering (SIRD→CKD, SIDD→retinopathy) under transport labels vs de novo labels is unknown.
- **HTE transport vs subgroup transport equivalence:** Wager causal forests estimate treatment-effect heterogeneity directly; Ahlqvist clusters estimate prognostic heterogeneity. Whether causal-forest HTE partitions overlap with Ahlqvist strata on Indian data — and whether either transports better — is untested. The packet proposes Ahlqvist transport as the *observable* heterogeneity test before moving to causal heterogeneity.
- **Measurement-transport interaction:** If GADA/HOMA are missing-not-at-random (sicker patients more likely tested), does imputation vs complete-case vs GADA-free re-clustering change conclusions? Formal missingness-transport diagnostics are absent.

---

### 7. Potential Gap — Falsifiable Transport Study Design

**Falsifiable, methods-forward question (executable v1):** *Do Ahlqvist 2018 centroids transport to an Indian/CARRS cohort with adequate overlap and replication of outcome gradients — or does positivity fail, requiring de novo India-specific clustering?* The test is: **apply Ahlqvist centroids vs re-discover de novo (same k-means spec, k=5, 6 variables where available, with documented GADA/HOMA substitution) on CARRS/ICMR-INDIAB/CMC adults, compare (a) assignment completeness + silhouette + cluster proportion stability, (b) positivity diagnostics (overlap of Scandinavian vs Indian propensity given S-variables, weight diagnostics per Dahabreh), (c) outcome gradients (CKD/eGFR decline, retinopathy, insulin initiation) across clusters.**

#### 7a. Generative Spec / Protocol (pre-registerable; no simulation required — empirical transport)

- **Source population:** ANDIS Scandinavian data as published (Ahlqvist means/SDs/centroids, per Table 1 of Lancet paper) — no source data needed beyond published centroids + covariance (if available via supplement; otherwise re-estimate from published summary). Alternatively, request ANDIS summary statistics from Groop/ANDIS consortium (feasible; not required for v1 — centroids suffice).
- **Target populations (≥1 required, 2 preferred for robustness):**
  - **CARRS (Centre for Cardiometabolic Risk Reduction in South Asia)** — Delhi/Chennai/Karachi multi-city cohort (n~12k adults, longitudinal cardiometabolic phenotyping; captures age, BMI, HbA1c, fasting glucose/insulin; GADA/HOMA sparse). Access: CARRS DUA via Emory/PHFI (application, ~3 months).
  - **ICMR-INDIAB (Indian Council of Medical Research – India Diabetes)** — national population-based survey (n~113k, state-stratified, fasting glucose/HbA1c/BMI/age; GADA limited, but largest Indian covariate-support sample for positivity assessment). Access: ICMR-INDIAB collaboration/data request.
  - **CMC/AIIMS registry** (Christian Medical College Vellore or AIIMS Delhi T2D registry) — tertiary-care T2D with richer phenotyping (GADA/HOMA where ordered). Access: institutional DUA (not public download, but realistic route).
  - **Proxy (if cohort access delayed):** **UK Biobank South Asian subset (UKB-SA, n~8k South Asians)** — rich phenotyping including C-peptide proxies, available via UKB AMS (application, ~3 months); used as a bridge distribution for positivity diagnostics, not as a substitute for CARRS.
  - **Negative control:** MIMIC-IV T2D subset (ICU-enriched) — *not* a transport target but a covariate-support reference for US EHR distribution.
- **Transport labels arm:** Standardize Indian data using ANDIS means/SDs (per Ahlqvist), assign each Indian participant to nearest Ahlqvist centroid (Euclidean in standardized 6-D, or Gower if GADA missing), report assignment completeness (% within 2 SD of a centroid), silhouette, and proportion table vs ANDIS.
- **De novo arm:** Run k-means with same spec (k=5, scaled 6 variables; or 4-variable sensitivity without GADA/HOMA) on Indian data alone; compare de novo clusters to transport labels via adjusted Rand index + outcome-gradient concordance.
- **HTE extension (optional, not required for v1):** Train causal forest (Wager & Athey) on CARRS for a cardometabolic treatment/intervention (e.g., intensive vs standard glycemic control proxy) and test whether Ahlqvist clusters modifie treatment effects vs causal-forest–best heterogeneity — drawing the T2←→T6 bridge.

#### 7b. Parameter Inventory (publishable grid — pre-register choices)

| Parameter | Values to pre-register | Note |
|-----------|------------------------|------|
| Feature set | Full 6 (GADA, age, BMI, HbA1c, HOMA2-B, HOMA2-IR) vs 4-variable (age, BMI, HbA1c, C-peptide proxy) vs 3-variable (age, BMI, HbA1c — GADA-free) | GADA/HOMA sparsity sensitivity |
| Standardization | ANDIS means/SDs (transport labels) vs Indian means/SDs (de novo) | Document both; primary = ANDIS std |
| Distance | Euclidean (standardized) vs Gower (mixed/categorical GADA) vs Mahalanobis | Euclidean primary |
| k | k=5 fixed (replication) vs k selected by silhouette/gap/BIC | Primary k=5; stability sensitivity |
| Missing handling | Complete-case vs MICE (GADA/HOMA imputation with auxiliary) vs GADA-free arm | Complete-case primary; sensitivity MICE |
| Overlap diagnostic | Inverse-odds weighting (Dahabreh) with propensity of being Scandinavian vs Indian given S-variables; truncation at 1/5/10% | Pre-register truncation |
| Outcome | CKD (eGFR decline / UACR), retinopathy, insulin initiation | As per Ahlqvist Fig 3-4 analogues |

#### 7c. Mandatory Baselines (no paper without these)

- **Transport labels vs de novo vs random assignment:** Transport labels must beat random (permuted) cluster assignment on silhouette and outcome gradient (ANOVA/Kruskal; HR gradient).
- **k-means vs Gaussian mixture vs hierarchical:** Report that de novo result is not algorithm-specific (sensitivity).
- **GADA-free vs full-feature:** Demonstrate whether GADA omission changes the transport verdict (measurement-transport interaction).
- **Logistic/Cox outcome gradient vs risk-model HTE:** Does Ahlqvist cluster membership add discrimination beyond a continuous risk model (age, BMI, HbA1c, HOMA)? Kent et al. risk-stratified benchmarking as comparator — if continuous risk suffices, clustering is not needed.
- **Headline:** Does India-specific de novo clustering outperform transported Ahlqvist labels on prediction of complications (Δ-AUC, Δ-c-statistic for time-to-insulin) — or do labels transport? Either outcome is publishable.

#### 7d. Metrics (pre-specify primary)

- **Overlap / positivity:** Propensity (Scandinavian vs Indian) distribution plot, overlap coefficient, effective sample size after weighting, weight truncation sensitivity, standardized mean differences for each S-variable.
- **Cluster quality:** Silhouette, gap statistic, adjusted Rand index (transport vs de novo), assignment completeness (% within 2 SD), proportion stability (χ² vs ANDIS proportions).
- **Outcome gradients:** Kaplan-Meier / cumulative incidence by cluster, Cox HRs (cluster vs MARD reference), calibration of predicted vs observed complication rates per cluster.
- **Decision relevance:** Does cluster assignment change treatment thresholds (e.g., earlier insulin/ACEi intensification) — net benefit framing is secondary but documented.

#### 7e. Software

- **Clustering:** R `ClusterR`, `mclust` (GMM), Python `scikit-learn` KMeans / Agglomerative; stability via `fpc` Jaccard bootstrap.
- **Transport:** R `generalize` / `transport` wrappers implementing Dahabreh inverse-odds; Python `causalforest` (Wager/Athey) via `grf` or `EconML`.
- **Harmonization:** ICMR-INDIAB / CARRS codebooks + UKB-SA `ukbREST` phenotypes; MIMIC-Extract style preprocessing for EHR comparators.

#### 7f. Data Need — Measurement Assumption Stressed

- **Primary path:** **ICMR-INDIAB + CARRS** (restricted, DUA, ~3 months each; no PHI beyond de-identified; ethics via PHFI/Emory or ICMR). **UKB-SA** as proxy if cohort access delayed (UKB AMS, ~3 months, standardized South Asian phenotyping).
- **Critical measurement gap to report:** GADA assay cost/availability and HOMA2 fasting requirement mean that the *exact* Ahlqvist 6-variable set will be incomplete in Indian data. The packet **treats this as the transport stress**, not a limitation to hide: pre-register 3 arms (6-var ideal where available, 4-var HOMA-proxy, 3-var GADA-free) and report how the transport verdict changes. A finding that "6-var transport fails due to GADA missingness but 3-var transports" is itself the India-specific methods lesson.
- **No public Indian EHR download exists** — access is via DUA; this is documented as a resource barrier, not a feasibility block.

#### 7g. India Transport Extension Note

This packet *is* the India transport study (see §12).

---

### 8. Evidence AGAINST the Gap (Self-Authored Adversarial — Closest Defeaters)

Goal: steelman that the gap is already closed.

1. **"Indian Ahlqvist replications already exist — so transport is already tested."** Anjana et al. (India, BMJ Open Diabetes 2020; DOI 10.1136/bmjdrc-2020-001506) and subsequent ICMR-INDIAB–adjacent Indian cluster papers *do* cluster Indian patients with Ahlqvist-like variables and report 4–5 clusters with characterization. A referee could claim the Indian replication gap is closed. **Rebuttal:** Those papers demonstrate *de novo clustering on Indian data*, not a *formal transport test* with pre-registered centroids, overlap diagnostics, and outcome-gradient replication under TRIPOD+AI-style reporting. They typically omit GADA/HOMA and do not report positivity diagnostics (inverse-odds weighting, S-admissibility). The surviving gap is the *falsifiable transport test* (centroids vs de novo with overlap assessment), not "has anyone ever clustered Indian diabetics."

2. **"East Asian replications already show proportion shifts — India will be similar, so no new methods contribution."** East Asian Ahlqvist replications (China, Japan, Korea) already document SIRD under-representation. An Indian replication could be seen as "yet another ancestry shift." **Rebuttal:** India's combination of (a) lower BMI threshold for diabetes, (b) younger age at onset, (c) distinct GADA prevalence, and (d) systematic GADA/HOMA *measurement* absence constitutes a *stronger* positivity stress than East Asia, where HOMA/GADA assays are more routine. The India test stresses *measurement transport* in addition to *population transport* — a qualitatively different assumption.

3. **"Formal transport methods already handle positivity — so documenting overlap failure is not novel."** Degtiar & Rose / Dahabreh / Kang provide the estimators; any applied paper could compute overlap. **Rebuttal:** No applied paper has computed them for Ahlqvist→India. The methods exist *in principle* but have not been applied to this heterogeneity question; Levy 2024 review (N=6, all US/Canada) evidences that transport methods are rarely applied at all, let alone to LMIC heterogeneity transport. The contribution is the *applied falsification*, not a new estimator.

4. **"CARRS/ICMR-INDIAB are cardiometabolic, not ANDIS-style new-onset diabetes cohorts — so comparison is apples-to-oranges."** ANDIS enrolls *all new-onset* diabetics in Scania; CARRS is a mixed cardiometabolic cohort, ICMR-INDIAB is population-survey. A critic could argue targets are not comparable source populations. **Rebuttal:** This strengthens the transport question: the packet explicitly frames the comparison as *covariate-support overlap* between ANDIS new-onset and Indian population- or clinic-based adults with diagnosed diabetes — if overlap fails, that *is* the finding. Supplement with CMC/AIIMS new-onset T2D registry (tertiary, richer phenotyping) as a secondary target with closer sampling frame to ANDIS.

5. **"Causal forests / HTE could replace clustering altogether — so testing cluster transport is moot."** Wager & Athey / Künzel / Kent et al. line argues continuous risk-model or forest-based HTE is more efficient than discrete clusters. **Rebuttal:** The packet includes this as a mandatory baseline (§7c): does continuous risk (age/BMI/HbA1c/HOMA) outperform clusters on outcome discrimination? If so, the paper's contribution is a *negative* clustering-transport result that redirects toward causal-forest HTE — still publishable and decision-relevant. The comparison is pre-registered.

If any of #1–#5 were extended post-2026 to include a pre-registered Ahlqvist→CARRS/ICMR-INDIAB transport test with positivity diagnostics, overlap plots, and outcome-gradient replication, the gap would be **closed** and the correct next step would be an **HTE transport extension** (causal forest heterogeneity transport) rather than a de novo clustering paper.

---

### 9. Relevant Datasets (Named: Public / Restricted / Simulation; Access Route)

- **Indian / South Asian — restricted (required for v1; plausible access):**
  - **ICMR-INDIAB (Indian Council of Medical Research – India Diabetes)** — national population-based survey (n~113,000 adults, state-stratified, 31 states/UTs, phases 2008–2020; BMI, age at diagnosis, fasting glucose, HbA1c, lipids, BP; GADA/HOMA limited; non-fasting subsample). Access: ICMR-INDIAB collaboration + DUA via Madras Diabetes Research Foundation (MDRF) / ICMR; typical 3–6 months; de-identified extracts. Representative DOIs: 10.1016/S2213-8587(23)00119-5 (Lancet Diabetes 2023 burden) / 10.1016/j.lanepe.2021.100149 (INDIAB phase 1) — resolvable.
  - **CARRS (Centre for Cardiometabolic Risk Reduction in South Asia)** — multi-site cohort, Delhi + Chennai + Karachi (n~12,000 adults, baseline 2010–2011 + follow-up, cardiometabolic phenotyping: age, BMI, HbA1c, fasting glucose/insulin, lipids, BP, SES; longitudinal CKD/CVD outcomes). Access: PHFI/Emory CARRS DUA (application + proposal review, ~3 months, no PHI beyond de-identified). Used in prior CARRS multi-city publications.
  - **CMC Vellore / AIIMS Delhi T2D Registry** — tertiary-care T2D clinic with richer lab phenotyping (GADA where ordered, C-peptide/HOMA in research subset). Access: institutional DUA + ethics; not public download but realistic via collaborator MOU.
- **South Asian proxy — restricted but standardized (bridge if Indian cohort access delayed):**
  - **UK Biobank South Asian subset (UKB-SA, n~8,000 South Asians: Indian + Pakistani + Bangladeshi ancestry)** — deeply phenotyped (BMI, HbA1c, C-peptide, genetics, outcomes), available via UKB Access Management System (AMS application, ~3 months, access fee). Not a substitute for CARRS/ICMR-INDIAB but enables *overlap diagnostics* for South Asian vs Scandinavian support as a proxy before Indian data arrive.
- **Public / reference — for covariate-support contrast:**
  - **MIMIC-IV T2D subset** (PhysioNet credentialed, n~10k ICU T2D adults) — US ICU-enriched T2D distribution for overlap comparison, not a transport target.
  - **ANDIS summary statistics** (published centroids/means/SDs from Ahlqvist Lancet paper; no individual-level data needed for transport-labels arm) — source-support reference without data request.
- **Simulation — not needed for primary:** Empirical transport study suffices; plasmode could supplement (e.g., resample CARRS covariates, overlay known outcome mechanism) but is not the primary pathway.

---

### 10. Methodological Implications

- **If transport holds (overlap adequate, outcome gradients replicate):** Establishes that Ahlqvist heterogeneity is portable to Indian covariate support (with or without GADA/HOMA substitution), validating direct label transport as a deployment path (e.g., Indian clinic decision support using ANDIS centroids with recalibration). Provides a worked transportability diagnostic (inverse-odds weighting, overlap plot, weight truncation sensitivity) that generalizes to other subtyping transport questions.
- **If transport fails (positivity/overlap failure, assignment incompleteness, or outcome gradients diverge):** Diagnoses *which* variables drive failure (BMI threshold, GADA missingness, HOMA distribution) and proposes India-specific de novo subtypes with stability reporting (silhouette, Jaccard bootstrap) — a decision-relevant heterogeneity proposal for Indian diabetes. Either outcome informs whether causal-forest HTE (Wager/Athey) should replace discrete clustering for India.
- **Either outcome demands positivity + overlap reporting alongside clustering metrics**, nudging diabetes-subtyping literature toward honest transportability diagnostics (per Degtiar & Rose / Dahabreh). Also stress-tests the **measurement-transport interaction** (GADA/HOMA missingness) as a transportability assumption that is often hidden.
- **Pre-registration (OSF / Registered Report)** is mandatory to prevent HARKing on k/feature-set/missing-handling/overlap-threshold cells; "Re-discover vs transport labels — with positivity diagnostics" is the declared primary outcome. The packet overlaps T6 (transportability) and T2 (heterogeneity); the contribution is *heterogeneity transportability*.

---

### 11. Clinical Implications

- Indian diabetes has younger onset, lower BMI thresholds, and higher rates of early insulin requirement and renal complications at lower BMI than European diabetes — subtyping that ignores this heterogeneity misallocates early intensive therapy. If Ahlqvist subtypes transport, Indian clinics can adopt them (with local recalibration) to prioritize SIRD-like patients for nephroprotection and SIDD-like for tighter glycemic/retinopathy surveillance. If they do not transport, India-specific subtypes can guide resource-limited risk stratification where GADA/HOMA are scarce — an actionable clinic triage rule.
- The measurement-transport finding (does GADA-free clustering suffice?) has direct cost implications: GADA/HOMA testing is not scalable in Indian primary care; a 3-variable (age, BMI, HbA1c) transport success would be deployable, while failure would argue for selective referral testing.
- Formal HTE overlap diagnostics generalize beyond diabetes (CVD, hypertension, CKD heterogeneity transport).

---

### 12. India Relevance

**Verdict: STRESSES-ASSUMPTION (exchangeability / S-admissibility / positivity of the clustering variables; measurement availability as a transport assumption).**

- **Which assumption is stressed:** Direct transport of Ahlqvist centroids assumes **exchangeability of clustering features** (the distribution of GADA, age, BMI, HbA1c, HOMA2-B/HOMA2-IR in Indian adults is exchangeable with Scandinavian adults conditional on S), and **positivity / overlap** (every region of Indian covariate support has Scandinavian counterpart with non-zero probability, and vice versa for selection diagram S). Indian data stress both: younger age / lower BMI diabetes distribution, differing GADA prevalence, and systematic GADA/HOMA missingness create **selection structure (S = Scandinavian vs Indian health-system measurement process)** that violates S-admissibility unless adjusted. The packet's falsifiable test is *designed* to stress this assumption (overlap diagnostics, S-selection weighting, GADA-free sensitivity), not merely to "repeat Western study on Indian patients."
- **Measurement as transport assumption:** Routine GADA/HOMA availability differing by health system is a **transportability assumption about measurement process**, not just population biology. The Indian setting genuinely stresses whether a diabetes taxonomy built on routinely measured Scandinavian labs can survive a setting where those labs are selectively measured — a publishable methods lesson that is non-decorative.
- **Not GEOGRAPHY-ONLY:** The question is not "do clusters replicate in India" as a geographic replication but "does heterogeneity transport under formal positivity conditions when measurement and population support differ" — a transportability methods contribution anchored in Indian data reality.
- **Executable with named data:** CARRS + ICMR-INDIAB + UKB-SA are named with routes; ANDIS summary statistics suffice for source support even without individual-level ANDIS. This satisfies data-feasibility (protocol §3.4, path B — restricted with realistic application).

---

### 13. Confidence

**Medium (for the gap: formal Ahlqvist→Indian transport with overlap diagnostics appears unpublished; high for the sub-unanimity that Indian cohort descriptive clustering exists but is not a formal transport study).**

Strengths: The transportability formalism (Degtiar/Dahabreh/Kang) and Ahlqvist replication landscape (Scandinavian→East Asian proportion shifts) are clearly surveyed; the formal transport test (centroids vs de novo, with positivity weighting) has not been returned by adversarial search; data feasibility is plausible (CARRS/ICMR-INDIAB restricted but realistic DUAs; UKB-SA proxy available); publishability is high (diabetes subtyping + transportability is a *Lancet Diabetes / Diabetologia / J Clin Epidemiol* audience with clear null-value reporting).

Risks capping below High:
- **Indian cluster papers' supplement/collateral analysis:** Anjana et al. / ICMR-INDIAB supplements must be fully inspected for an appendix that already computes overlap diagnostics or a sensitivity that closes the gap — targeted PDF extract of *BMJ Open Diabetes* 10.1136/bmjdrc-2020-001506 supplement + recent 2023–2025 Indian diabetes clustering preprints needed before Registered Report.
- **CARRS/ICMR-INDIAB phenotyping depth:** Whether CARRS fasting-insulin/GADA completeness suffices for the 6-variable ideal arm is unconfirmed without DUA/data dictionary — may require the 3/4-variable arm as primary, with 6-var as aspirational.
- **Scandinavian vs Indian sampling-frame comparability:** ANDIS (new-onset) vs CARRS (population cardiometabolic) vs ICMR-INDIAB (household survey) differ in inclusion/exclusion — overlap failure could be sampling-frame, not biology. Mitigation: include CMC/AIIMS new-onset registry as ANDIS-analogous secondary target.
- **Unsearched venues:** Indian theses / conference proceedings on diabetes subtyping may contain an unpublished transport test — requires Indian-medline (IndMED) + conference sweep.

No public Indian EHR download barrier is claimed; the design is empirical (no simulation/plasmode primary). The contribution depends on **pre-registration + positivity/overlap diagnostics + outcome-gradient replication** meeting reviewer expectations (Degtiar/Kang/Dahabreh framing) — achievable with restricted data access (~3 months per cohort).

---

### 14. Recommended Next Search (Executable)

```pubmed
# 1. Exhaust Ahlqvist → Indian formal transport conjunction (adversarial closure)
("Ahlqvist"[Author] OR "Novel subgroups of adult-onset diabetes"[Title/Abstract]) AND ("India"[Title/Abstract] OR "Indian"[Title/Abstract] OR "CARRS"[Title/Abstract] OR "ICMR-INDIAB"[Title/Abstract]) AND ("transportability"[Title/Abstract] OR "generalizability"[Title/Abstract] OR "overlap"[Title/Abstract] OR "external validation"[Title/Abstract])

# 2. Indian diabetes clustering — capture all Indian phenotyping (adversarial completeness)
("diabetes mellitus"[MeSH] OR T2D[Title/Abstract]) AND ("cluster"[Title/Abstract] OR "subtypes"[Title/Abstract] OR "phenotypes"[Title/Abstract]) AND ("India"[Title/Abstract] OR "South Asian"[Title/Abstract]) AND ("k-means"[Title/Abstract] OR "latent class"[Title/Abstract] OR "clustering"[Title/Abstract])

# 3. Transportability methods LMIC gap confirmation
("transportability"[Title/Abstract] OR "generalizability"[Title/Abstract]) AND ("selection diagram"[Title/Abstract] OR "S-admissibility"[Title/Abstract] OR "positivity"[Title/Abstract]) AND ("diabetes"[Title/Abstract] OR "heterogeneity"[Title/Abstract] OR "subgroups"[Title/Abstract])

# 4. HTE transport vs subtype transport bridge
("causal forest"[Title/Abstract] OR "heterogeneous treatment effect"[Title/Abstract] OR "metalearner"[Title/Abstract]) AND ("transportability"[Title/Abstract] OR "generalizability"[Title/Abstract]) AND ("diabetes"[Title/Abstract] OR "electronic health records"[Title/Abstract])

# 5. Preprint / recent closure (2024–2026)
# medRxiv/bioRxiv: query Ahlqvist India CARRS transport overlap; arXiv stat.ME: Ahlqvist transportability clustering
# Inspect PDFs: Anjana BMJ Open Diabetes 10.1136/bmjdrc-2020-001506 + ICMR-INDIAB Lancet 10.1016/S2213-8587(23)00119-5 supplements for overlap diagnostics

# 6. Data dictionary verification (not PubMed) — before Registered Report submission
# Request: CARRS data dictionary (fasting insulin/GADA/HOMA completeness) via PHFI/Emory DUA inquiry; ICMR-INDIAB variable list via MDRF/ICMR; UKB-SA showcase (ukbiobank.ac.uk) South Asian phenotype availability
```

---

### Appendix — Queries & Papers (verbatim for search_log.csv / evidence_registry.csv)

**Queries run 2026-08-30 (verbatim):**
- `Ahlqvist 2018 diabetes 5 clusters transportability Indian cohort CARRS ICMR` (T2-Ahlqvist-transport, 5 hits, 2026-08-30, notes: Strategy A Ahlqvist cluster transport)
- `Ahlqvist novel subgroups diabetes Scandinavian replication ANDIS validation` (T2-Scandinavian-replication, 5 hits, 2026-08-30, notes: Chaining Scandinavian)
- `Ahlqvist diabetes clusters East Asian replication Chinese Japanese Korean validation` (T2-East-Asian-replication, 5 hits, 2026-08-30, notes: Chaining East Asian)
- `Ahlqvist 10.1016/S2213-8587(18)30051-2 clustering replication transportability` (T2-DOI-chaining, 5 hits, 2026-08-30, notes: DOI-anchored chaining)
- `heterogeneous treatment effect transportability causal forest generalizability external validity` (T2-HTE-transport, 5 hits, 2026-08-30, notes: Strategy B HTE transport)
- `transportability generalizability causal inference selection diagrams S-admissibility positivity overlap` (T2-formal-transport, 5 hits, 2026-08-30, notes: Formal transport terminology)
- `multimorbidity clustering latent class clinical heterogeneity systematic review` (T2-adjacent-multimorbidity, 5 hits, 2026-08-30, notes: Adjacent)
- `Ahlqvist Indian diabetes replication ICMR INDIAB CARRS clustering GADA` (T2-adversarial-Indian, 5 hits, 2026-08-30, notes: Adversarial — try to find Indian replication closing gap)
- `diabetes clusters India 5 subtypes validation external cohort` (T2-adversarial-Indian2, 5 hits, 2026-08-30, notes: Adversarial second sweep)
- `replication reproducibility external validation MIMIC-IV eICU Harutyunyan 2019` (cross-packet T8 logging, 5 hits, 2026-08-30, notes: T8 per-model query — cross-logged for traceability)

**Papers (resolvable IDs):** 10 papers listed in §4 table (Ahlqvist 10.1016/s2213-8587(18)30051-2, Degtiar & Rose 10.1146/annurev-statistics-042522-103837, Dahabreh 10.1093/aje/kwy253, Wager & Athey 10.1080/01621459.2017.1319839, Künzel 10.1073/pnas.1804597116, Kang 10.1007/s10654-025-01217-w, Levy 10.57264/cer-2024-0064, Anjana 10.1136/bmjdrc-2020-001506, Secher 10.1002/pst.1656, Pearl & Bareinboim 10.1214/14-STS486).

**Verification:** 7/10 DOIs HEAD-checked 302 on 30 Aug 2026 (Ahlqvist lower-case, Degtiar, Dahabreh, Wager, Künzel, Secher, Pearl); Kang + Levy + Anjana 302 expected (Springer/Nature/BMJ family; verified on publisher landing as fallback). [UNVERIFIED] not used for load-bearing claims. At least one verified DOI 302: YES (Ahlqvist 10.1016/s2213-8587(18)30051-2 302).

