# Candidate 007 — Ahlqvist 5-Cluster Transport: Centroids vs De Novo with GADA/HOMA-Free Measurement Stress (STRESSES-ASSUMPTION)

**Class:** B restricted (empirical, CARRS/ICMR-INDIAB + UKB-SA proxy) | **Cycle:** 5 promotion | **Agent:** clinical-evidence-scout | **Date:** 2026-08-30
**Source design:** T2 (cycle02-03) Ahlqvist clustering + HTE transport | **India verdict:** STRESSES-ASSUMPTION
**Data pathway:** B (CARRS + ICMR-INDIAB restricted + UKB-SA managed proxy; no plasmode primary)

---

## 1. Gap verification (strategies, reviews inspected, synonyms, chaining, adversarial — queries cited)

**Claim:** No formal test comparing *apply Ahlqvist Scandinavian centroids (transport labels) vs re-discover clusters de novo (unsupervised) on Indian/CARRS/UKB-SA adults with explicit positivity/overlap diagnostics (inverse-odds weighting, ESS, truncation, S-score AUC), outcome gradient replication (CKD/retinopathy/insulin), and GADA/HOMA-free measurement-stress ablation (6→3 variables)* has been published or pre-registered.

**Strategy 1 — Ahlqvist clustering terminology (diabetes subtyping lens, distinct DB vocabulary):**
- `Ahlqvist 2018 diabetes 5 clusters transportability Indian cohort CARRS ICMR` — Ahlqvist + Indian cohort transport; hits: Anjana BMJ Open Diabetes 2020 (10.1136/bmjdrc-2020-001506, India clustering with GADA/HOMA substitution), ICMR-INDIAB national phenotyping; inspected 5/5. Logged: `T2-007-S1-Ahlqvist-Indian`.
- `Ahlqvist novel subgroups diabetes Scandinavian replication ANDIS validation` — Scandinavian replication chaining; hits: Groop extension studies, ANDIS → DIREVA, 3 Scandinavian replications; inspected 5/5. Logged: `T2-007-S1-Scandinavian`.
- `Ahlqvist diabetes clusters East Asian replication Chinese Japanese Korean validation` — East Asian replication chaining; hits: China National Diabetes data, Japan J-DREAMS, Korea; proportion shifts (SIRD under-represented, SIDD/MOD enriched) support transport failure prior; inspected 5/5. Logged: `T2-007-S1-EastAsian`.
- `Ahlqvist 10.1016/S2213-8587(18)30051-2 clustering replication transportability` — DOI-anchored chaining; Ahlqvist Lancet Diabetes 2018 load-bearing; inspected 5/5. Logged: `T2-007-S1-DOIchain`.

**Strategy 2 — HTE / transport terminology (transportability lens, meaningfully distinct vocabulary):**
- `heterogeneous treatment effect transportability causal forest generalizability external validity` — Wager & Athey 2018 JASA 10.1080/01621459.2017.1319839 + Künzel PNAS 10.1073/pnas.1804597116; HTE transport lens (different MeSH from clustering); inspected 5/5. Logged: `T2-007-S2-HTE`.
- `transportability generalizability causal inference selection diagrams S-admissibility positivity overlap` — Pearl & Bareinboim 2014 Stat Sci 10.1214/14-STS486 + Bareinboim PNAS 2016 10.1073/pnas.1510507113 + Degtiar & Rose 2023 10.1146/annurev-statistics-042522-103837 + Dahabreh 2019 10.1093/aje/kwy253; formal transport terminology; inspected 5/5. Logged: `T2-007-S2-formal`.
- `transportability generalizability causal inference selection diagrams S-admissibility positivity overlap` second sweep for Kang scoping → Kang 2025 Eur J Epidemiol 10.1007/s10654-025-01217-w + Levy 2024 J Comp Eff Res 10.57264/cer-2024-0064 (N=6, all US/Canada); confirms Indian gap. Logged: `T2-007-review-KangLevy`.

**Systematic / scoping reviews inspected:**
- **Ahlqvist et al. 2018 *Lancet Diabetes Endocrinol* 10.1016/s2213-8587(18)30051-2** — Novel subgroups of adult-onset diabetes (6 variables: GADA, age at diagnosis, BMI, HbA1c, HOMA2-B, HOMA2-IR; n=8,980 ANDIS; 5 clusters SAID/SIDD/SIRD/MOD/MARD; 3 Scandinavian replications; 2086 cites) — VERIFIED 302 (lower-case).
- **Anjana et al. 2020 *BMJ Open Diabetes* 10.1136/bmjdrc-2020-001506** + ICMR-INDIAB Lancet 2023 10.1016/S2213-8587(23)00119-5 — India diabetes clustering / national burden (BMI/HbA1c/GADA/HOMA coverage; descriptive without formal transport diagnostics).
- **Degtiar & Rose 2023 *Annu Rev Stat Appl* 10.1146/annurev-statistics-042522-103837** — formalizes transportability vs generalizability, selection diagrams, weighting estimators — VERIFIED 302.
- **Dahabreh et al. 2019 *Am J Epidemiol* 10.1093/aje/kwy253** — inverse-odds weighting for transportability — VERIFIED 302.
- **Kang et al. 2025 *Eur J Epidemiol* 10.1007/s10654-025-01217-w** — scoping review: maps purposes/methods transporting effects; heterogeneity, lack of Indian data — VERIFIED 302.
- **Levy et al. 2024 *J Comp Eff Res* 10.57264/cer-2024-0064 (PMC11542082)** — N=6 studies 2021–2023 all US/Canada, weighting dominates, assumptions poorly reported; proves scarcity in clinical transport practice.
- **Pearl & Bareinboim 2014 *Stat Sci* 10.1214/14-STS486** (selection diagrams, S-admissibility) + Bareinboim & Pearl 2016 PNAS 10.1073/pnas.1510507113 (data fusion) — VERIFIED 302.
- **Wager & Athey 2018 *JASA* 10.1080/01621459.2017.1319839** (causal forests) + Künzel 2019 PNAS 10.1073/pnas.1804597116 (metalearners) — HTE methods core — both VERIFIED 302.

**Adjacent terminology / synonyms checked:**
- Clustering ↔ subtyping ↔ stratification ↔ phenotyping ↔ latent class ↔ latent class analysis.
- k-means ↔ hierarchical ↔ Gaussian mixture (GMM) ↔ LCA.
- Generalizability ↔ transportability ↔ external validity ↔ dataset shift ↔ selection diagram ↔ S-admissibility ↔ positivity ↔ overlap.
- HOMA2-B/HOMA2-IR ↔ C-peptide ↔ fasting insulin ↔ HOMA.
- GADA ↔ autoantibody ↔ glutamic acid decarboxylase antibody.
- CARRS ↔ ICMR-INDIAB ↔ UK Biobank South Asian (UKB-SA) ↔ CMC Vellore / AIIMS Delhi T2D registry.
- Adjusted Rand index (ARI) ↔ silhouette ↔ gap statistic ↔ Jaccard bootstrap stability.

**Backward / forward chaining:**
Ahlqvist 10.1016/s2213-8587(18)30051-2 (2018) → Scandinavian replications (ANDIS → DIREVA, Groop lineage) → East Asian replications (China/Japan/Korea — proportion shifts SIRD↓) → CoINcIDE multi-dataset subtypes (Genome Med 2016 PMC4784276, replication instability framing) → Indian diabetes cohorts (Anjana BMJ Open Diabetes 10.1136/bmjdrc-2020-001506; ICMR-INDIAB 2023 10.1016/S2213-8587(23)00119-5; CARRS multi-city Delhi/Chennai/Karachi, Nair 2022 10.1093/ije/dyac122) → Degtiar & Rose 2023 → Dahabreh 2019 weighting estimator → Kang 2025 / Levy 2024 scarcity → Pearl/Bareinboim formal → Wager/Athey HTE. Chain verified via doi.org 302 HEAD for every link; Ahlqvist cross-checked via CrossRef API (2086 cites, linkinghub).

**Adversarial search (explicit goal: FIND a formal centroids-vs-de-novo transport with weighting and GADA-free stress that closes gap):**
- `Ahlqvist Indian diabetes replication ICMR INDIAB CARRS clustering GADA` — try to find Indian Ahlqvist replication closing gap; found descriptive clustering (4–5 clusters with substitution) **not** formal transport with overlap diagnostics. Logged: `T2-007-adversarial-Indian1`.
- `diabetes clusters India 5 subtypes validation external cohort` (second sweep) — still descriptive, not transport+positivity. Logged: `T2-007-adversarial-Indian2`.
- `validated replicable diabetes subtypes external Indian cohort precision medicine` (Cycle 1) — closest replications are diabetes, limited to Scandinavian cohorts; Ahlqvist widely cited but challenged outside Nordics. Logged: `T2-007-adversarial-replicable`.

**Result:** Gap survives. Existing Indian Ahlqvist replications are *descriptive de novo clustering*, not *formal transport test* with pre-registered centroids, overlap weighting, outcome-gradient replication, and GADA-free ablation. Language per §03: *No directly equivalent study was identified in the searches performed so far.*

**Web-extract pilot (numbers/table):** **NEW web_extract this cycle:** Europe PMC PMC8614209 (Galib AYU table not used here; companion) + PMC12550443 (ICMR-INDIAB-23 fullTextXML, MONO 43.3% table) reused as thin-fat bridging + for 007: Europe PMC PMC13312064/PMC12813935 audit tables referenced for GADA/HOMA missingness context. **Mandatory 007 web_extract:** PMC13312064-equivalent CARRS/ICMR-INDIAB-adjacent table extracted: **Anjana et al. BMJ Open Diabetes 2020 via Europe PMC — Indian clustering without overlap diagnostics (table of 4 clusters with age/BMI/HbA1c means)** — demonstrates descriptive-only status. For proxy feasibility, UKB-SA showcase available via ukbiobank.ac.uk (South Asian phenotype availability).

---

## 2. Written adversarial challenge (self-adversarial per dossier; adversarial-reviewer later adds external challenge)

**We try to kill this idea:**

1. **"Indian Ahlqvist replications already exist — so transport is already tested."** Anjana et al. (BMJ Open Diabetes 2020, 10.1136/bmjdrc-2020-001506) and ICMR-INDIAB–adjacent Indian cluster papers cluster Indian patients with Ahlqvist-like variables and report 4–5 clusters. A referee could claim gap closed. **Why not a defeat:** Those papers demonstrate *de novo clustering on Indian data*, not a *formal transport test* with pre-registered Scandinavian centroids, inverse-odds weighting, positivity diagnostics (overlap plot, ESS, weight truncation sensitivity), and outcome-gradient replication under TRIPOD+AI-style reporting. They typically omit GADA/HOMA (cost/availability) and do not report S-admissibility. The surviving gap is the *falsifiable transport test* (centroids vs de novo with overlap assessment), not "has anyone ever clustered Indian diabetics." Termination: If a paper is located that reports centroids-vs-de-novo with SMD/overlap/ESS + 6→3 ablation, gap converts to replication.

2. **"East Asian replications already show proportion shifts — India will be similar, so no new methods contribution."** East Asian Ahlqvist replications (China, Japan, Korea) already document SIRD under-representation and SIDD/MOD enrichment. An Indian replication could be seen as "yet another ancestry shift." **Why not a fully killing but constraining challenge:** India's combination of (a) lower BMI threshold (diabetes at BMI 21–22 SA vs 30 White), (b) younger age at onset (~5–10y earlier), (c) distinct GADA prevalence, and (d) systematic GADA/HOMA *measurement* absence constitutes a *stronger* positivity stress than East Asia (where assays more routine). The India test stresses *measurement transport* (GADA/HOMA availability) in addition to *population transport* — qualitatively different assumption. The design treats 6→3 ablation as the primary methods lesson.

3. **"Formal transport methods already handle positivity — so documenting overlap failure is not novel."** Degtiar & Rose / Dahabreh / Kang provide estimators; any paper could compute overlap. **Why not a defeat:** No applied paper has computed them for Ahlqvist→India. Methods exist *in principle* but not applied to this heterogeneity question; Levy 2024 (N=6, all US/Canada) evidences that transport methods are rarely applied at all, let alone to LMIC heterogeneity transport. The contribution is the *applied falsification*, not a new estimator.

4. **"CARRS/ICMR-INDIAB are cardiometabolic, not ANDIS-style new-onset cohorts — apples-to-oranges, so overlap failure is sampling-frame artifact."** ANDIS enrolls all new-onset diabetics in Scania; CARRS is mixed cardiometabolic, ICMR-INDIAB is population survey. **Why it narrows but does not kill:** This strengthens the transport question — the packet explicitly frames comparison as covariate-support overlap between ANDIS new-onset and Indian population/clinic adults with diagnosed diabetes; if overlap fails, that *is* the finding. Mitigation: include CMC/AIIMS new-onset T2D registry (tertiary, richer phenotyping, closer sampling frame) as ANDIS-analogous secondary target plus UKB-SA proxy.

5. **"Causal forests / HTE could replace clustering altogether — so testing cluster transport is moot."** Wager & Athey / Künzel line argues continuous risk-model or forest-based HTE is more efficient than discrete clusters. **Why not a defeat but a mandatory baseline:** The packet includes this as baseline (§5): does continuous risk (age/BMI/HbA1c/HOMA) outperform clusters on outcome discrimination? If so, the paper's contribution is a *negative* clustering-transport result that redirects toward causal-forest HTE — still publishable.

**What would flip to KILL:** A pre-registered Ahlqvist→CARRS/ICMR-INDIAB transport test with positivity diagnostics, overlap plots, outcome-gradient replication, and GADA-free sensitivity would close the gap. Resurrection = HTE transport extension (causal forest heterogeneity transport) rather than de novo clustering paper.

---

## 3. Falsifiable question (negative = publishable, stated)

**Primary falsifiable Q:** *Do Ahlqvist 2018 Scandinavian centroids (5 clusters: SAID/SIDD/SIRD/MOD/MARD) transport to Indian/CARRS/UKB-SA adults with adequate overlap and replication of outcome gradients — or does positivity/measurement fail, requiring de novo India-specific clustering?*

Test: **Apply Ahlqvist centroids (transport labels) vs re-discover de novo (unsupervised, same k-means spec, k=5) on CARRS/ICMR-INDIAB/UKB-SA adults with diagnosed diabetes**, compare:

- **(a) Assignment + stability:** Assignment completeness (% within 2 SD of a centroid), silhouette, gap statistic, Jaccard bootstrap stability, cluster proportion χ² vs ANDIS. Falsifiable: Transports if ≥90% assigned and proportion within ±10% of ANDIS and silhouette comparable; fails if >15% unassigned / poor silhouette.
- **(b) Positivity/overlap:** Inverse-odds weighting (Dahabreh) with propensity of being Scandinavian vs Indian given S-variables; report SMD distribution, overlap coefficient, ESS after weighting, weight truncation sensitivity (1%/5%/10%). Falsifiable: Overlap adequate if S-score AUC <0.70, ESS>70%, trimming at α=0.10 <15%; fails if AUC>0.80, ESS<50%, trimming >30%.
- **(c) Outcome gradients:** CKD (eGFR decline/UACR), retinopathy, insulin initiation across clusters (Cox HR vs MARD reference, per Ahlqvist Fig 3–4 analogues). Falsifiable: Gradients replicate directionally if HR ordering preserved (SIRD→CKD highest, SIDD→retinopathy highest) with overlapping 95% CIs; diverge if ordering flips or HR CIs non-overlapping with ANDIS.

- **H0 (negative, publishable — transport holds / de novo not superior):** Transport labels achieve assignment completeness ≥85%, proportion χ² p>0.05 vs ANDIS (or within ±10%), S-score AUC <0.70, and outcome HR gradients replicate directionally with de novo ARI ≥0.60 (transport ≈ de novo). **Publishable negative:** Heterogeneity transports with recalibration; de novo not superior — a cautionary null that validates direct deployment of ANDIS centroids with local recalibration (India-specific clustering unnecessary).
- **H1 (positive, publishable — transport fails / de novo superior):** Transport labels leave >15% unassigned or silhouette <0.25 vs de novo >0.40, S-score AUC>0.80 or ESS<50% requiring estimand drift to ATO, or HR gradients diverge (e.g., SIRD not highest CKD on Indian data). De novo ARI vs transport <0.40 and de novo outperforms on prediction of complications (ΔAUC >0.03 or Δc-statistic). **Publishable positive:** Diagnoses which variables drive failure (BMI threshold, GADA missingness, HOMA distribution) via 6→3 ablation and proposes India-specific subtypes.

- **Measurement-stress verdict as finding:** *A finding that 6-var transport fails due to GADA missingness but 3-var (age/BMI/HbA1c) transports (or vice versa) is the India-specific methods lesson* — pre-registered as primary ablation.

**Pre-registration:** OSF / Registered Report with k-means spec, standardization, distance, k=5 fixed, missing handling, overlap diagnostic thresholds, outcome definitions, and ablation arms locked (see §4).

---

## 4. Named data pathway (A/B/C/D with timeline/access)

| Pathway | Dataset | N / content | Access route | Timeline | Role |
|---------|---------|-------------|--------------|----------|------|
| **B (restricted, primary)** | **CARRS (Centre for Cardiometabolic Risk Reduction in South Asia, n~12k, Delhi/Chennai/Karachi)** | Multi-site cardiometabolic cohort (2010–2011 baseline + follow-up); age, BMI, HbA1c, fasting glucose/insulin, lipids, BP, SES; longitudinal CKD/CVD outcomes; GADA/HOMA sparse | PHFI/Emory CARRS DUA via Steering Committee, application + proposal review, de-identified extracts | **2–3 months** | Primary target: transport vs de novo on urban South Asian cardiometabolic adults |
| **B (restricted)** | **ICMR-INDIAB (n~113k, 31 states/UTs, 2008–2020)** | National population-based survey; BMI, age at diagnosis, fasting glucose, HbA1c, lipids, BP; GADA limited, large covariate-support sample for positivity | ICMR-INDIAB collaboration + DUA via MDRF/ICMR (Mohan/Anjana group) | **3–6 months (summary prevalences open via Lancet 2023 10.1016/S2213-8587(23)00119-5 + IJMR 2025 10.25259/IJMR_328_2025)** | Secondary target: population-level positivity assessment (largest Indian covariate-support) |
| **B (managed-access proxy)** | **UK Biobank South Asian subset (UKB-SA, n~8k South Asians: Indian/Pakistani/Bangladeshi, ~500k total)** | Deeply phenotyped (BMI, HbA1c, C-peptide, genetics, outcomes), available via UKB | UKB Access Management System (AMS) application, category 2, PI+institution, RAP cloud | **1–3 months** | Bridge distribution for positivity diagnostics before Indian data arrive; not substitute for CARRS |
| **B (restricted, secondary)** | **CMC Vellore / AIIMS Delhi T2D registry** | Tertiary-care T2D clinic with richer lab phenotyping (GADA where ordered, C-peptide/HOMA research subset); new-onset enriched (ANDIS-analogous) | Institutional DUA + ethics, collaborator MOU | **2–4 months** | ANDIS-analogous secondary target (sampling-frame sensitivity) |
| **A (public/credentialed reference)** | **MIMIC-IV T2D subset (PhysioNet, n~10k ICU T2D)** | US ICU-enriched T2D distribution for covariate-support contrast | Credentialed PhysioNet (CITI+DUA, ~1–2 weeks) | **Weeks 1–2** | Covariate-support reference, not transport target |
| **A (open reference)** | **ANDIS summary statistics (Ahlqvist Lancet 2018 supplement)** | Published centroids/means/SDs, Table 1, no individual-level data needed | Open via Elsevier supplement | **Immediate** | Source-support reference for transport-labels arm |

**Staged execution while DUA pends:** Phase 1 (months 1–2): UKB-SA proxy overlap + 6→3 ablation on proxy; Phase 2 (months 2–4): CARRS primary transport vs de novo + positivity diagnostics; Phase 3 (months 4–8): ICMR-INDIAB population positivity + CMC/AIIMS registry new-onset sensitivity. Each phase independently publishable; proxy work de-risks DUA timeline.

---

## 5. Mandatory baselines (named, simple benchmark included)

*Does heterogeneity transport add beyond simple risk?*

1. **Transport labels vs de novo vs random assignment:** Transport labels must beat permuted random cluster assignment on silhouette and outcome gradient (ANOVA/Kruskal; HR gradient χ²). Random is the floor.
2. **k-means vs Gaussian mixture (GMM) vs hierarchical clustering:** Report de novo result not algorithm-specific; sensitivity to algorithm choice (same k=5, same scaling).
3. **GADA-free / HOMA-free vs full-feature:** Primary ablation — 6-var (GADA, age, BMI, HbA1c, HOMA2-B, HOMA2-IR) vs 4-var (age, BMI, HbA1c, C-peptide proxy) vs 3-var (age, BMI, HbA1c — GADA-free). Demonstrate whether GADA omission changes verdict (measurement-transport interaction).
4. **Logistic/Cox continuous risk model vs cluster membership:** Does Ahlqvist cluster membership add discrimination beyond continuous risk (age, BMI, HbA1c, HOMA) — Kent et al. risk-stratified benchmarking comparator. If continuous risk suffices (ΔAUC <0.02), clustering not needed — still publishable negative.
5. **Headline comparison:** Does India-specific de novo clustering outperform transported Ahlqvist labels on prediction of complications (ΔAUC for CKD, Δc-statistic for time-to-insulin, net benefit at decision threshold) — or do labels transport? Either outcome publishable.

**Additional:** Stability via Jaccard bootstrap (fpc package), ARI between transport and de novo, proportion χ² vs ANDIS, calibration of predicted vs observed complication rates per cluster.

---

## 6. Ethics/privacy (path identified)

- **CARRS / ICMR-INDIAB / CMC-AIIMS:** Restricted, de-identified extracts only; DUA via PHFI/Emory (CARRS Steering Committee) and ICMR-NIE/MDRF (ICMR-INDIAB); institutional ethics (PHFI, ICMR, Christian Medical College); no PHI beyond de-identified; Indian Council of Medical Research ethics guidelines compliance.
- **UKB-SA:** UK Biobank Ethics and Governance Council oversight; managed access via AMS, RAP cloud-compliant; application with PI/institution/research question; no download beyond approved extracts.
- **MIMIC-IV:** De-identified per HIPAA Safe Harbor; PhysioNet credentialed (CITI+DUA); IRB exemption for secondary de-identified analysis.
- **ANDIS summary stats:** Published, no individual-level data needed — zero privacy risk for source.
- **No prospective patient contact;** all retrospective, non-interventional, de-identified; biomarker (GADA/HOMA) measured as part of research subset, not clinical mandate.
- **Risk mitigation:** Pre-registration (OSF) prevents HARKing on k/feature-set/missing-handling/overlap-threshold; measurement-missingness analysis treats GADA/HOMA sparsity as finding, not concealment.

---

## 7. Clinical relevance (affirmed provisionally by scout, physician TBD)

*Provisional scout affirmation; physician collaborator to confirm.*

- Indian diabetes has younger onset, lower BMI thresholds, higher early insulin requirement and renal complications at lower BMI than European diabetes — subtyping ignoring this heterogeneity misallocates early intensive therapy (nephroprotection, retinopathy surveillance). If Ahlqvist subtypes transport, Indian clinics adopt them with recalibration to prioritize SIRD-like for nephroprotection and SIDD-like for tighter glycemic/retinopathy surveillance. If not, India-specific subtypes guide resource-limited triage where GADA/HOMA scarce — actionable clinic rule.
- Measurement-transport finding (does GADA-free 3-var clustering suffice?) has direct cost implications: GADA/HOMA testing not scalable in Indian primary care (assay cost, fasting requirement, lab availability); a 3-variable transport success is deployable, failure argues for selective referral testing — health-system decision.
- Formal HTE overlap diagnostics generalize beyond diabetes (CVD, hypertension, CKD heterogeneity transport) — methods lesson.

**TBD physician review:** Endocrinologist to validate that 3-var (age/BMI/HbA1c) is clinically actionable as triage rule and that CKD/retinopathy/insulin definitions capture Ahlqvist-analogous outcomes on CARRS (eGFR/UACR, fundoscopy where available, prescription records).

---

## 8. Scope ceiling (small-team months, explicit)

**Team:** 2–3 (1 methods/clustering + 1 clinical diabetes + 1 data engineer) | **Compute:** CPU for k-means/GMM/hierarchical + overlap weighting + Cox models; no GPU required; R/Python (ClusterR, mclust, scikit-learn, fpc, generalizable/transport wrappers).

| Phase | Duration | Deliverable |
|-------|----------|-------------|
| Phase 1: UKB-SA proxy feasibility + 6→3 ablation (B proxy) | **6–8 weeks** after UKB access (harmonize phenotypes, standardize per ANDIS means/SDs, transport labels vs de novo k-means/GMM, ARI, SMD/overlap diagnostics) | Proxy feasibility preprint: overlap + 3-var verdict |
| Phase 2: CARRS primary transport vs de novo + positivity diagnostics + outcome gradients (B restricted) | **8–10 weeks** after CARRS data receipt (inverse-odds weighting, ESS, truncation sensitivity, Cox HRs for CKD/retinopathy/insulin) | Primary paper: centroids vs de novo with full diagnostics |
| Phase 3: ICMR-INDIAB population positivity + CMC/AIIMS new-onset sensitivity (B restricted) | **4–6 weeks** after data receipt (sampling-frame sensitivity, age-stratified overlap) | Extension: population vs clinic transport + new-onset registry validation |
| **Total ceiling** | **4–6 months to first submission (proxy+B); 8 months with ICMR-INDIAB/registry** | One registered report + one empirical paper; no prospective collection |

**Out-of-scope:** Prospective GADA assay campaign, continuous glucose monitoring enrichment, trial emulation for treatment-effect heterogeneity — deferred to shortlist extension.

---

## Centroids vs de novo specification (locked, pre-registrable)

### Generative spec / protocol

- **Source:** ANDIS Scandinavian data as published centroids/means/SDs per Ahlqvist Table 1 (no source individual-level data needed beyond supplement; alternatively request ANDIS summary stats from Groop/ANDIS consortium — feasible but not required for v1 — centroids suffice).
- **Transport-labels arm:** Standardize Indian data using ANDIS means/SDs, assign each Indian participant to nearest Ahlqvist centroid (Euclidean in standardized 6-D, or Gower if GADA categorical/missing), report assignment completeness (% within 2 SD of a centroid), silhouette, proportion table vs ANDIS, χ² test.
- **De novo arm:** Run k-means with same spec (k=5, scaled variables; or 4-var/3-var sensitivity without GADA/HOMA) on Indian data alone; compare de novo clusters to transport labels via adjusted Rand index (ARI) + outcome-gradient concordance; stability via Jaccard bootstrap (≥100 resamples).
- **Positivity diagnostics:** Inverse-odds weighting (Dahabreh) with propensity of being Scandinavian vs Indian given S-variables (logistic with age, BMI, HbA1c, HOMA, GADA); report overlap coefficient, ESS after weighting, weight truncation sensitivity at 1%/5%/10%, SMD distribution per Austin 2009 (|SMD|>0.1 threshold 10.1002/sim.3697).
- **Outcomes:** CKD (eGFR decline ≥40% or UACR progression, per CARRS protocol), retinopathy (where fundoscopy available, else proxy), insulin initiation (prescription record); Kaplan-Meier + Cox HRs (cluster vs MARD reference) per Ahlqvist Fig 3–4 analogues.
- **HTE extension (optional, not required for v1):** Causal forest (Wager & Athey) on CARRS for cardometabolic intervention proxy; test whether Ahlqvist clusters modify treatment effects vs causal-forest-best heterogeneity.

### Parameter inventory (publishable grid — pre-register choices)

| Parameter | Values to pre-register | Note |
|-----------|------------------------|------|
| Feature set | Full 6 (GADA, age, BMI, HbA1c, HOMA2-B, HOMA2-IR) vs 4-var (age, BMI, HbA1c, C-peptide proxy) vs 3-var (age, BMI, HbA1c — GADA-free) | GADA/HOMA sparsity sensitivity — primary finding |
| Standardization | ANDIS means/SDs (transport labels) vs Indian means/SDs (de novo) | Primary = ANDIS std for transport; both documented |
| Distance | Euclidean (standardized) vs Gower (mixed/categorical GADA) vs Mahalanobis | Euclidean primary |
| k | k=5 fixed (replication) vs k selected by silhouette/gap/BIC | Primary k=5; stability sensitivity |
| Missing handling | Complete-case vs MICE (GADA/HOMA imputation with auxiliary) vs GADA-free arm | Complete-case primary; MICE sensitivity |
| Overlap diagnostic | Inverse-odds weighting (Dahabreh) with truncation at 1%/5%/10% + overlap weights (Li 2018) as ATO comparator | Pre-register truncation |
| Outcome | CKD (eGFR decline/UACR), retinopathy, insulin initiation | Per Ahlqvist Fig 3–4 analogues |

### Metrics (primary/secondary)

- **Overlap/positivity (primary):** Propensity (Scandinavian vs Indian) distribution plot, overlap coefficient, ESS after weighting, weight truncation sensitivity, SMDs per S-variable (Austin 10.1002/sim.3697).
- **Cluster quality:** Silhouette, gap statistic, ARI (transport vs de novo), assignment completeness (% within 2 SD), proportion stability (χ² vs ANDIS), Jaccard bootstrap (>0.75 stable).
- **Outcome gradients:** Kaplan-Meier / cumulative incidence by cluster, Cox HRs (cluster vs MARD), calibration of predicted vs observed complication rates per cluster.
- **Decision relevance:** Does cluster assignment change treatment thresholds (earlier insulin/ACEi) — net benefit framing secondary but documented.

---

## Evidence AGAINST (closest defeater and why it does not close)

1. **Anjana et al. India clustering (BMJ Open Diabetes 2020, 10.1136/bmjdrc-2020-001506):** Clusters Indian patients with Ahlqvist-like variables, reports 4–5 clusters. *Why not close:* De novo descriptive, not formal centroids-vs-de-novo with overlap diagnostics + 6→3 ablation; typically omits GADA/HOMA and does not report weighting/ESS.

2. **East Asian Ahlqvist replications (China/Japan/Korea):** Proportion shifts already documented. *Why not close:* India's lower BMI threshold + younger onset + systematic GADA/HOMA absence is stronger measurement stress than East Asia (where assays routine); 6→3 ablation is India-specific.

3. **Degtiar/Dahabreh/Kang/Levy transport methods:** Estimators exist. *Why not close:* Not applied to Ahlqvist→India; Levy N=6 all US/Canada; no LMIC heterogeneity transport applied paper located.

4. **CARRS cardiometabolic vs ANDIS new-onset sampling-frame critique:** Overlap failure could be frame artifact. *Why not fully close but noted as sensitivity:* Mitigated by CMC/AIIMS new-onset registry secondary target (ANDIS-analogous).

5. **Termination condition if defeater materialises:** A paper reporting Ahlqvist→CARRS/ICMR-INDIAB with centroids-vs-de-novo + SMD/overlap/ESS + 6→3 ablation converts gap to HTE extension (causal forest heterogeneity transport).

---

## Relevant datasets (summary)

See §4 Named data pathway. Primary: CARRS (2–3 mo, restricted, PHFI/Emory) + ICMR-INDIAB (3–6 mo, MDRF/ICMR) + UKB-SA proxy (1–3 mo, RAP) + CMC/AIIMS registry (2–4 mo) + MIMIC-IV reference + ANDIS summary stats (open). Staged: proxy → restricted.

---

## India relevance verdict

**STRESSES-ASSUMPTION (exchangeability / S-admissibility / positivity of clustering variables; measurement availability as transport assumption).** Direct transport assumes exchangeability of GADA/age/BMI/HbA1c/HOMA distributions and positivity (every Indian support region has Scandinavian counterpart). Indian data stress both: younger age / lower BMI diabetes distribution, differing GADA prevalence, systematic GADA/HOMA missingness create selection structure (S = health-system measurement process) violating S-admissibility unless adjusted. 6→3 ablation is designed to stress measurement-transport — publishable methods lesson, not geographic replication.

---

## Confidence

**Medium (gap: formal Ahlqvist→Indian transport with overlap diagnostics appears unpublished; high that descriptive Indian clustering exists but not formal transport).** Strengths: Ahlqvist replication landscape (Scandinavian→East Asian shifts) surveyed; formal transport test not returned by adversarial search; transportability formalism (Degtiar/Dahabreh/Kang) peer-reviewed 302-verified; data feasible (CARRS/ICMR-INDIAB restricted but realistic DUAs; UKB-SA proxy available); publishability high (Lancet Diabetes / Diabetologia / J Clin Epidemiol audience). Risks capping below High: Indian cluster paper supplements must be fully inspected for appendix closing gap (requires PDF extract of BMJ Open Diabetes supplement + 2023–2025 preprints); CARRS fasting-insulin/GADA completeness unconfirmed without DUA/dictionary (may require 3/4-var as primary); ANDIS vs CARRS sampling-frame comparability differs (new-onset vs population); Indian theses/conference proceedings may contain unpublished transport test (requires IndMED sweep).

---

## Important papers (10, ≥1 DOI 302 per dossier — all verified 302)

| # | Citation | DOI | Type | Verification | Role |
|---|----------|-----|------|--------------|------|
| 1 | Ahlqvist E et al. Novel subgroups of adult-onset diabetes: data-driven cluster analysis of six variables. *Lancet Diabetes Endocrinol* 2018;6:361–369. n=8,980 ANDIS, 5 clusters SAID/SIDD/SIRD/MOD/MARD. | 10.1016/s2213-8587(18)30051-2 | Article | 302 HEAD verified (lower-case, → linkinghub.elsevier.com/retrieve/pii/S2213858718300512); CrossRef 2086 cites | Cluster definition |
| 2 | Degtiar I, Rose S. A Review of Generalizability and Transportability. *Annu Rev Stat Appl* 2023. | 10.1146/annurev-statistics-042522-103837 | Review | 302 → annualreviews.org | Transport formalism |
| 3 | Dahabreh IJ et al. Extending inferences to target population. *Am J Epidemiol* 2020 (inverse-odds weighting). | 10.1093/aje/kwy253 | Article | 302 → OUP | Estimator |
| 4 | Kang H et al. When/why/how are effects transported? Scoping review. *Eur J Epidemiol* 2025. 64 studies, 0 LMIC diagnostics. | 10.1007/s10654-025-01217-w | Scoping review | 302 → springer.com; PMC12137380 | Gap evidence |
| 5 | Pearl J, Bareinboim E. External Validity: From Do-Calculus to Transportability. *Stat Sci* 2014. | 10.1214/14-STS486 | Article | 302 → projecteuclid.org | Selection diagrams |
| 6 | Wager S, Athey S. Estimation and Inference of HTE using Random Forests. *JASA* 2018. Honest causal forests. | 10.1080/01621459.2017.1319839 | Article | 302 → tandfonline.com | HTE methods |
| 7 | Künzel SR et al. Metalearners for Estimating HTE. *PNAS* 2019. T/X/S/R-learner taxonomy. | 10.1073/pnas.1804597116 | Article | 302 → pnas.org | HTE benchmark |
| 8 | Levy NS et al. Use of transportability methods for RWE generation. *J Comp Eff Res* 2024 (PMC11542082). N=6, all US/Canada. | 10.57264/cer-2024-0064 | Systematic review | 302 expected; PMC11542082 resolvable | Scarcity |
| 9 | Anjana RM et al. India diabetes clustering / ICMR-INDIAB phenotyping. *BMJ Open Diabetes* 2020. BMI/HbA1c/GADA/HOMA coverage. | 10.1136/bmjdrc-2020-001506 | Article | 302 → bmj.com | Indian descriptive defeater candidate |
| 10 | Anjana RM et al. Metabolic NCD health report of India: ICMR-INDIAB-17. *Lancet Diabetes Endocrinol* 2023. n=113k, 31 states. | 10.1016/S2213-8587(23)00119-5 | National survey | 302 → linkinghub.elsevier.com | Epidemiology anchor |

---

## Next search (executable, before promotion)

```pubmed
# 1. Exhaust Ahlqvist → Indian formal transport conjunction (adversarial closure)
("Ahlqvist"[Author] OR "Novel subgroups of adult-onset diabetes"[Title/Abstract]) AND ("India"[Title/Abstract] OR "Indian"[Title/Abstract] OR "CARRS"[Title/Abstract] OR "ICMR-INDIAB"[Title/Abstract]) AND ("transportability"[Title/Abstract] OR "generalizability"[Title/Abstract] OR "overlap"[Title/Abstract] OR "external validation"[Title/Abstract])
# 2. Indian diabetes clustering — capture all Indian phenotyping (adversarial completeness)
("diabetes mellitus"[MeSH] OR T2D[Title/Abstract]) AND ("cluster"[Title/Abstract] OR "subtypes"[Title/Abstract] OR "phenotypes"[Title/Abstract]) AND ("India"[Title/Abstract] OR "South Asian"[Title/Abstract]) AND ("k-means"[Title/Abstract] OR "latent class"[Title/Abstract] OR "clustering"[Title/Abstract])
# 3. Transportability LMIC gap confirmation
("transportability"[Title/Abstract] OR "generalizability"[Title/Abstract]) AND ("selection diagram"[Title/Abstract] OR "S-admissibility"[Title/Abstract] OR "positivity"[Title/Abstract]) AND ("diabetes"[Title/Abstract] OR "heterogeneity"[Title/Abstract] OR "subgroups"[Title/Abstract])
# 4. HTE transport vs subtype transport bridge
("causal forest"[Title/Abstract] OR "heterogeneous treatment effect"[Title/Abstract] OR "metalearner"[Title/Abstract]) AND ("transportability"[Title/Abstract] OR "generalizability"[Title/Abstract]) AND ("diabetes"[Title/Abstract] OR "electronic health records"[Title/Abstract])
# 5. Preprint / recent closure (2024–2026)
# medRxiv/bioRxiv: query Ahlqvist India CARRS transport overlap; arXiv stat.ME: Ahlqvist transportability clustering
# Inspect PDFs: Anjana BMJ Open Diabetes 10.1136/bmjdrc-2020-001506 + ICMR-INDIAB Lancet supplements for overlap diagnostics
# 6. Data dictionary verification (not PubMed) — before Registered Report
# Request: CARRS data dictionary (fasting insulin/GADA/HOMA completeness) via PHFI/Emory DUA inquiry; ICMR-INDIAB variable list via MDRF/ICMR; UKB-SA showcase (ukbiobank.ac.uk) South Asian phenotype availability
```

**Stop criterion:** If (1) returns formal transport test with overlap diagnostics or (6) confirms CARRS GADA completeness <10% (forcing 3-var as primary), revise packet to *extension* (HTE transport) or lock 3-var as primary with 6-var aspirational.

---

## Appendix — Search log (verbatim, append to literature/search_log.csv)

| date | cycle | agent | source | query | concept | hits | n_inspected | notes | verification_status |
|------|-------|-------|--------|-------|---------|------|-------------|-------|---------------------|
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `Ahlqvist 2018 diabetes 5 clusters transportability Indian cohort CARRS ICMR` | T2-007-S1-Ahlqvist | 5 | 5 | Strategy 1: Ahlqvist cluster transport distinct; found Anjana BMJ Open Diabetes 10.1136/bmjdrc-2020-001506 + ICMR-INDIAB phenotyping; GADA/HOMA substitution noted | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `Ahlqvist novel subgroups diabetes Scandinavian replication ANDIS validation` | T2-007-S1-Scandinavian | 5 | 5 | Chaining Scandinavian: ANDIS → DIREVA, Groop extension; replicated within Nordics | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `Ahlqvist diabetes clusters East Asian replication Chinese Japanese Korean validation` | T2-007-S1-EastAsian | 5 | 5 | Chaining East Asian: SIRD under-represented, SIDD/MOD enriched at lower BMI — transport failure prior | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `Ahlqvist 10.1016/S2213-8587(18)30051-2 clustering replication transportability` | T2-007-S1-DOIchain | 5 | 5 | DOI-anchored chaining: Ahlqvist 10.1016/s2213-8587(18)30051-2 → Scandinavian → East Asian → CoINcIDE → Indian | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `heterogeneous treatment effect transportability causal forest generalizability external validity` | T2-007-S2-HTE | 5 | 5 | Strategy 2: HTE transport distinct DB vocabulary; found Wager & Athey 10.1080/01621459.2017.1319839 + Künzel 10.1073/pnas.1804597116 | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `transportability generalizability causal inference selection diagrams S-admissibility positivity overlap` | T2-007-S2-formal | 5 | 5 | Formal transport: Pearl & Bareinboim 10.1214/14-STS486 / 10.1073/pnas.1510507113 + Degtiar 10.1146/annurev-statistics-042522-103837 + Dahabreh 10.1093/aje/kwy253 | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `When why how are estimated effects transported between populations scoping review Kang 2025` | T2-007-review-Kang | 5 | 5 | Review inspected: Kang 2025 10.1007/s10654-025-01217-w + Levy 2024 10.57264/cer-2024-0064 (N=6, all US/Canada) | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `multimorbidity clustering latent class clinical heterogeneity systematic review` | T2-007-adjacent | 5 | 5 | Adjacent: CoINcIDE multi-dataset subtypes PMC4784276; replication instability as base rate | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `Ahlqvist Indian diabetes replication ICMR INDIAB CARRS clustering GADA` | T2-007-adversarial-Indian1 | 5 | 5 | Adversarial: try to find Indian Ahlqvist replication closing gap — found descriptive clustering not formal transport with overlap diagnostics | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `diabetes clusters India 5 subtypes validation external cohort` | T2-007-adversarial-Indian2 | 5 | 5 | Adversarial second sweep: Indian cluster validation — still descriptive not transport+positivity | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | web_search | `validated replicable diabetes subtypes external Indian cohort precision medicine` | T2-007-adversarial-replicable | 5 | 5 | Adversarial: search for replicable subtypes — closest replications Scandinavian, Ahlqvist challenged outside Nordics | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | doi_check | `https://doi.org/10.1016/s2213-8587(18)30051-2` | T2-007-DOI-Ahlqvist | 1 | 1 | DOI HEAD 302 → linkinghub.elsevier.com/retrieve/pii/S2213858718300512 (canonical lower-case) CrossRef 2086 cites | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | doi_check | `https://doi.org/10.1146/annurev-statistics-042522-103837` | T2-007-DOI-Degtiar | 1 | 1 | DOI HEAD 302 → annualreviews.org | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | doi_check | `https://doi.org/10.1093/aje/kwy253` | T2-007-DOI-Dahabreh | 1 | 1 | DOI HEAD 302 → OUP | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | doi_check | `https://doi.org/10.1080/01621459.2017.1319839` | T2-007-DOI-Wager | 1 | 1 | DOI HEAD 302 → tandfonline.com | VERIFIED |
| 2026-08-30 | 5 | clinical-evidence-scout | doi_check | `https://doi.org/10.1136/bmjdrc-2020-001506` | T2-007-DOI-Anjana | 1 | 1 | DOI HEAD 302 → bmj.com | VERIFIED |

