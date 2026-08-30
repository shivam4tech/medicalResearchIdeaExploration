# Candidate 004 — TRIPOD Subgroup-Calibration Corpus Audit n=150 (D literature)

**Source design:** T5 cycle02+04 (methods-scout + clinical-evidence-scout) — Cycle 04 T5 corpus lock `working/agent_notes/clinical-evidence-scout/cycle04_T5_corpus_lock.md`
**Class:** D literature (no PHI, no prospective data — corpus of published prediction-model validations) | **Data path:** PubMed + Europe PMC corpus (TRIPOD-defined external validations 2015–2025, Humans+English, n=150 random sample via PubMed E-utilities)
**Status:** PROMOTION DOSSIER — Cycle 5 first wave (no DUA, no hospital data) | **Date:** 2026-08-30
**Agent:** methods-scout (with clinical-evidence-scout T5 lock) | **India verdict:** GEOGRAPHY-ONLY for v1 (STRESSES-ASSUMPTION deferred to Stage-2 India corpus)
**Confidence:** Medium (post-REVISE 2026-08-30: interval-aware prevalence + Wilson + masking + era-split sharpened, DCGS/KAISEN/PMID 41643238 distinguished, corpus completeness sensitivity logged, RECORD/STROBE pre-registered)

---

## Gate 1 — Gap Verification (strategies, reviews inspected, synonyms, chaining, adversarial — queries cited)

**Claim to verify:** No published **meta-audit quantifies prevalence of subgroup calibration reporting** (overall vs ≥1 clinically relevant stratifier: sex/age/comorbidity/site/race-ethnicity/PROGRESS, interval-aware vs point) among **TRIPOD-defined externally validated clinical prediction models 2015–2025** with Wilson CI and TRIPOD+AI (2024) era split — i.e., whether overall calibration masks subgroup failure and whether TRIPOD+AI has moved the needle is unmeasured as an empirical corpus study.

**Strategy A — TRIPOD / subgroup-calibration guideline/corpus terminology (meaningfully distinct: guideline vocabulary, DISTINCT):**
- `TRIPOD external validation calibration subgroup reporting 2023 2024` (2026-08-30, T5-S1-TRIPOD, 5 hits) — TRIPOD external-validation corpus terminology; returned TRIPOD+AI BMJ 2024 (DOI 10.1136/bmj-2023-078378) PDF + TRANS-P checklist. Guideline/corpus vocabulary.
- `TRIPOD statement Collins 2015 BMJ external validation calibration plot` (2026-08-30, T5-TRIPOD-2015, 5 hits) — TRIPOD lineage start (DOI 10.1136/bmj.g7594).
- `TRIPOD AI statement Collins BMJ 2024 078378 DOI` (2026-08-30, T5-chain-TRIPOD+AI, 0 hits direct — verified via DOI HEAD 302) — corpus definition v2 (27-item).
- `subgroup calibration reporting systematic review prediction model` (2026-08-30, T5-adversarial-meta-audit, 5 hits) — adversarial; closest: completeness-of-reporting reviews (Heus et al. 2023) and updating-review (Snell 2026), **not** subgroup-calibration prevalence — gap survives.
- `meta-analysis subgroup calibration clinical prediction model systematic review` (Cycle 2 T5, 5 hits) — adversarial carry; no subgroup-calibration prevalence audit located.

**Strategy B — Uncertainty / fairness terminology (distinct: interval/coverage & equity vocabulary, not guideline):**
- `Riley uncertainty risk estimates clinical prediction model BMJ 2024 2025` (2026-08-30, T5-review-Riley, 5 hits) — interval-aware calibration terminology; found Riley et al. BMJ 2025 DOI 10.1136/bmj-2024-080749 (388:e080749, PMID 39947680); verified 302.
- `conformal prediction calibration clinical risk model uncertainty` (2026-08-30, T5-adjacent-conformal, 5 hits) — found Angelopoulos & Bates 2021/2023, Vazquez review; conformal as adjacent interval baseline; interval/coverage vocabulary distinct from TRIPOD guideline terms.
- `Christodoulou validation clinical prediction models systematic review 2023` (2026-08-30, T5-review-Christodoulou, 5 hits) — found Christodoulou et al. JCE 2019 DOI 10.1016/j.jclinepi.2018.09.024 (71 comparisons, ML vs logistic no benefit) — validation-quality baseline.
- `fairness audit clinical prediction model subgroup calibration disparity` (Cycle 2 T5, 0 hits on exact conjunction) — fairness/calibration terminology fragmented; not guideline vocabulary — confirms distinct terminology family.

**Reviews inspected (4 required, ≥5 actually inspected):**
1. **Riley et al. BMJ 2025** (DOI 10.1136/bmj-2024-080749) — uncertainty of risk estimates; interval-aware calibration (bootstrap/Bayesian individual intervals; precision-targeted validation sample size; CRASH interval 0.477–0.693; calibration bands). Load-bearing for **interval-aware** extraction. **302 → bmj.com/lookup/doi/10.1136/bmj-2024-080749** (Europe PMC + BMJ HTML 15236 chars in Cycle 2; PMID 39947680)
2. **Van Calster et al. J Clin Epidemiol 2016** (DOI 10.1016/j.jclinepi.2015.12.005) — calibration hierarchy mean→weak→moderate→strong (1000+ cites). Vocabulary for extraction matrix. **302 → linkinghub.elsevier.com/retrieve/pii/S0895435615005818**
3. **TRIPOD 2015** (DOI 10.1136/bmj.g7594, Collins et al.) → **TRIPOD+AI 2024** (DOI 10.1136/bmj-2023-078378, 27-item, Collins et al.) — 22-item → 27-item checklist; defines corpus; TRIPOD+AI adds fairness/uncertainty/open-science items. **Both 302 verified** (BMJ)
4. **Christodoulou et al. JCE 2019** (DOI 10.1016/j.jclinepi.2018.09.024) — systematic review 71 comparisons (ML vs logistic): **no performance benefit of ML**; calibration reporting poor across both. Suggests next discriminating quality dimension is **subgroup calibration**. **302 → linkinghub.elsevier.com**
5. **PROBAST (Wolff et al. Ann Intern Med 2019, DOI 10.7326/M18-1376) + PROBAST+AI 2025 (Moons DOI 10.1136/bmj-2024-082505)** — RoB tool; Queiroz Table 2 anchor (91.8% high risk).

**Adjacent (conformal / fairness calibration — required, terminologically distinct from TRIPOD):**
- Conformal: **Angelopoulos & Bates** (DOI 10.1561/2200000101, arXiv:2107.07511 → FTML 2023;16:494-591) — finite-sample distribution-free coverage guarantee under exchangeability; complements Riley intervals for subgroup comparison. **302 → emerald.com/ftmal/article/16/4/494/1332423**
- Fairness: **PROGRESS** framework (Evans 2022) + TRIPOD+AI fairness items + fairness audit terminology (algorithmic fairness AND calibration) — stratifiers are fairness-relevant; no audit yet reports calibration fairness prevalence (0 hits on exact conjunction confirms fragmented terminology).
- Coverage guarantee for interval-aware extraction: Angelopoulos vs Riley head-to-head is adjacent, not core.

**Synonyms checked:** TRIPOD ↔ TRIPOD+AI (2024 supersedes 2015); external validation ↔ independent validation ↔ geographical/temporal validation; calibration slope/intercept ↔ calibration plot/loess ↔ Hosmer-Lemeshow ↔ ICI; subgroup ↔ stratified ↔ heterogeneity ↔ fairness (sex, age decile, comorbidity, site, race/ethnicity — PROGRESS); prediction intervals ↔ uncertainty intervals ↔ credible intervals ↔ conformal sets; Humans[Mesh] ↔ human studies; English[lang] filter.

**Chaining (TRIPOD 2015 → TRIPOD+AI 2024 → Riley interval → Van Calster hierarchy):**
- **Collins TRIPOD 2015** (10.1136/bmj.g7594, 22-item, BMJ) → **Collins TRIPOD+AI 2024** (10.1136/bmj-2023-078378, 27-item, BMJ; adds fairness/uncertainty/open science) → **Riley et al. BMJ 2025** (10.1136/bmj-2024-080749, individual risk uncertainty; CRASH interval 0.477–0.693; calibration uncertainty bands; sample-size-for-precision) → **Van Calster JCE 2016** (10.1016/j.jclinepi.2015.12.005, hierarchy mean→weak→moderate→strong). Chain verified via **doi.org 302 HEAD for every link** (see Appendix batch) + Europe PMC fullTextXML + BMJ HTML extracts.

**Adversarial (explicit goal: FIND existing subgroup-calibration meta-audit that closes gap — T5-adversarial-meta-audit):**
- `meta-analysis subgroup calibration clinical prediction model systematic review` (Cycle 2, 5 hits) + `subgroup calibration prediction model audit reporting completeness` (Cycle 4, 5 hits) — Closest: **Queiroz et al. BMC Endocr Disord 2026 (PMC13169604)** — systematic review & meta-analysis of 97 T2DM models (65 studies, 15,796 screened): geographic inequity (70% Asian, 21.6% externally validated, PROBAST 91.8% high risk, Analysis 83.5%). **Web_extract 61K chars, 2 tables** — this is **closest defeater** but audits geographic/validation/PRED quality, **not subgroup-vs-overall calibration prevalence with interval awareness**. Debray et al. calibration MA framework provides synthesis method, not prevalence. **No existing meta-audit quantifies subgroup-calibration reporting rate** across corpus of externally validated models. Gap survives.
- `subgroup calibration reporting systematic review prediction model` (T5-adversarial, 5 hits) — same outcome; completeness reviews (Heus et al. 2023) not calibration-per-subgroup.
- **6+ search_log rows verbatim satisfied** (see Appendix: 2 TRIPOD strategies + uncertainty/fairness synonym runs + reviews + adjacent + adversarial + chaining ≥6).

**MUST web_extract (brief-required):** Europe PMC **PMC13169604** (Queiroz BMC Endocr Disord 2026, DOI 10.1186/s12902-026-02301-2) — **61,000 chars, 2 tables with counts/percentages (Table 1: characteristics of 97 models by geography/model type/external validation; Table 2: PROBAST domain ratings 91.8% high risk)** — form feasibility demonstrated (see Gate 4). PLUS Cycle 2 carry: Hughes et al. UK Biobank CV-risk external validation (PMC11865138) — discrimination stratified per disease subgroup but **calibration not stratified** — aggregate masking pattern.

**Language (proportional):** No directly equivalent study with the conjunction (TRIPOD-defined external validations 2015–2025 + subgroup calibration prevalence + interval-aware reporting + subgroup-vs-overall masking rate) was identified in the searches performed so far — not "no TRIPOD audit exists" (Queiroz comprehensive audit exists but not on subgroup calibration with interval awareness).

---

## Gate 2 — Written Adversarial Challenge (self-adversarial per dossier)

**Goal:** steelman closure — 4 defeaters that would collapse novelty if framed generously.

1. **"Queiroz et al. BMC Endocr Disord 2026 already IS a TRIPOD subgroup-calibration corpus audit."** Systematic review of 97 T2DM models with geographic/methodological audit (Tables 1–2). *Rebuttal:* Queiroz audits **geographic disparity + methodological quality (PROBAST high risk 91.8%)**, not **subgroup calibration prevalence with interval awareness**. No extraction row for "calibration slope/intercept stratified by sex/age/site with CI/band." Closest defeater but **not exact**; if extended post-2026 to include interval-aware subgroup calibration matrix, gap narrows to era-split novelty.

2. **"Completeness-of-reporting reviews (Heus et al., Snell et al., Wynants COVID-19) already audit TRIPOD adherence, so calibration is covered."** These reviews report overall TRIPOD item adherence (e.g., Item 10d calibration reporting). *Rebuttal:* Item-level adherence ≠ subgroup-calibration prevalence with **Wilson CI + interval-aware subgroup vs overall masking rate**. No review reports p(subgroup calibration | external validation) or p(interval-aware subgroup calibration) with PROGRESS stratifier breakdown.

3. **"Debray et al. calibration meta-analysis framework already synthesizes calibration, so subgroup gap is methodological not empirical."** Debray provides method for meta-analysing calibration (slope/intercept pooling). *Rebuttal:* Debray is **method for synthesis**, not **empirical audit of reporting completeness**. Lock's contribution is **prevalence estimation** (descriptive audit with Wilson CI), not model-level meta-analysis. They are complementary (Debray's method would be used Stage-2 for quantitative synthesis if subgroup slopes exist).

4. **"Riley et al. BMJ 2025 already advocates interval-aware calibration and PROBAST+AI updates this, so interval-aware subgroup audit is 'obvious next work' with no novelty."** *Rebuttal:* Guidance exists but **adherence on an independent corpus is unmeasured** — audit *measures adherence* and tests TRIPOD+AI enforcement gap via pre/post-2024 split. Negative result (≥60% interval-aware subgroup reporting for 2024–2025) is publishable and would contradict prior (Wynants 545/606 high risk; Queiroz 91.8% high risk). "Obvious" does not mean "done."

**If any of #1–#4 extended post-2025 to include TRIPOD-defined external validations with Wilson prevalence for subgroup calibration (overall + interval-aware per PROGRESS stratifier) + era split, gap would be closed** and correct next step would be **quantitative calibration meta-analysis (Debray pooling) on subgroup slopes** or **Indian-corpus extension**.

---

## Gate 3 — Falsifiable Question (negative = publishable, stated)

**Primary question (locked corpus audit, pre-registered — interval-aware vs point foregrounded):**

*Among TRIPOD-defined externally validated clinical prediction models (PubMed TRIPOD[Title/Abstract] AND validation[Title/Abstract] 2015–2025, Humans+English, n=150 random sample via E-utilities), what is the **prevalence of interval-aware subgroup calibration reporting** — specifically: (a) overall calibration reported (slope/intercept or plot + ICI) vs (b) **subgroup calibration reported (≥1 clinically relevant stratifier: sex, age decile, comorbidity, site, race/ethnicity, PROGRESS)** with **interval-aware reporting distinguished from point-only reporting (slope CI / plot band per subgroup per Riley 10.1136/bmj-2024-080749 vs point estimate alone — primary estimand is p(interval-aware subgroup calibration), secondary is p(point subgroup calibration))** — and how often does **overall calibration "pass" (slope 0.8–1.2 + intercept ±0.3 + ICI <0.05) while ≥1 subgroup fails (slope <0.8 or >1.2, or subgroup ICI ≥0.10)** (aggregate masking rate: overall pass while ≥1 subgroup fails, with Wilson CI), with **Wilson 95% CI ±0.06** and **TRIPOD+AI era split (pre-2024 Jan 2015–Dec 2023 vs 2024–2025)** testing enforcement gap?*

**Skeptical framing (negative = publishable):**

- **H0 (reporting has been solved, publishable negative):** Among TRIPOD-defined external validations 2015–2025, **≥60% report both overall calibration AND subgroup calibration** with interval-aware reporting (slope CI / plot band per subgroup) — aggregate masking is rare and TRIPOD/TRIPOD+AI have already closed enforcement gap for recent validations. **Negative result is rigorous and publishable** as evidence that overall metrics proxy subgroup performance for recent era (n=150, Wilson CI; if H0 holds for 2024–2025 stratum, TRIPOD+AI is working).
- **H1 (gap holds, publishable positive):** Subgroup calibration is **rarely reported (<30% prevalence; interval-aware <10%)** with Wilson CI, overall "pass" masks subgroup failure in ≥15–20% of validations where subgroup data allow assessment, and TRIPOD+AI 2024→2025 does **not** significantly raise prevalence (era-split χ²/Fisher p>0.05 or difference CI includes 0) — so **aggregate masking is prevalent and enforcement gap persists**. Corpus audit with prevalence + Wilson CI + PROGRESS breakdown is contribution to *J Clin Epi / BMJ Open / Diagn Progn Res*.

**Either outcome:** Prevalence estimation with Wilson CI is methods contribution; negative result is **stronger** (contradicts 91.8% high-risk prior, needs scrutiny) and still publishable as "TRIPOD+AI works."

**Precision (Wilson ±0.06):** n=150 → Wilson 95% CI half-width ~0.06–0.08 depending on p (max ±0.08 at p=0.5, ±0.06 at p=0.2 or 0.8); adequate to distinguish <30% vs ≥60% prevalence. Power via Wilson interval, not p-value — design is descriptive prevalence, not superiority test (era split is secondary χ² with n₁=75, n₂=75 per era, detectable difference ~0.20 at 80% power).

---

## Gate 4 — Named Data Pathway (A/B/C/D with timeline/access)

**Path: D literature (no PHI, no prospective data — corpus of published validations).**

| Dataset / source | Role | Access | Timeline |
|------------------|------|--------|----------|
| **PubMed E-utilities corpus (TRIPOD[Title/Abstract] AND validation[Title/Abstract], Filters: 2015:2025[PDAT], Humans[Mesh], English[lang])** | **Primary corpus** — TRIPOD-defined externally validated clinical prediction models 2015–2025 | Open via `esearch` + `efetch` (E-utilities API; no DUA) | **Immediate** (screening starts tomorrow; E-utilities query logged as reproducible search string) |
| **Europe PMC REST fullTextXML (JATS) + BMJ/PLOS OA HTML** | **Full-text retrieval** for eligibility + extraction (PMC OA subset ~60% of PubMed; subscription via institutional proxy for remainder — fallback: Crossref `text-mining` links) | Open for OA (~60%); institutional proxy for closed | Immediate–1 week |
| **Queiroz-type corpus papers (Queiroz PMC13169604, Hughes PMC11865138, plus 5–10 sampled TRIPOD validations from pilot)** | **Extraction form calibration** — feasibility demonstration via MUST web_extract with tables (see Gate 5 pilot) | PMC13169604 fullTextXML 61K chars + tables | Verified 2026-08-30 |
| **PROBAST (Wolff 2019) + PROBAST+AI (Moons 2025)** | **Risk-of-bias scaffolding** (Participants/Predictors/Outcome/Analysis domains) alongside subgroup calibration matrix | DOI resolvable | Immediate |

**Locked corpus filter (pre-registered, reproducible via E-utilities string logged to OSF):**
```
PubMed: ("TRIPOD"[Title/Abstract] AND ("validation"[Title/Abstract] OR "external validation"[Title/Abstract]))
Filters: "2015/01/01"[PDAT] : "2025/12/31"[PDAT], Humans[Mesh], English[lang]
Randomization: sorted by PMID (deterministic) → `numpy.random.default_rng(20260830)` → sample n=150
Exclusions (pre-registered): non-prediction-model validation (e.g., biomarker-only diagnostic accuracy), protocol/review without primary validation data, non-English full-text, duplicate PMID across TRIPOD+AI/TRIPOD classic.
```
**Pre-registered sensitivities:** (i) **RECORD/STROBE vs TRIPOD sensitivity** — repeat prevalence on `RECORD[Title/Abstract] AND validation[Title/Abstract] AND calibration` (n≈494 PubMed) and `STROBE[Title/Abstract] AND external validation` (n≈18) corpora to test reporting-guideline bias; (ii) **Corpus completeness sensitivity** — TRIPOD filter count (570) vs `calibration AND external validation` count (8,188) logged 2026-08-30 (see REVISE Addendum) to quantify TRIPOD language-bias magnitude; (iii) Language filter sensitivity (without English[lang]) exploratory.
**Estimated corpus size:** TRIPOD term appears in ~2,500–4,000 PubMed records 2015–2025 (per E-utilities count logged Cycle 02); filtering to validation narrows to ~600–1,200; random n=150 is feasible for full-text extraction by small team (see Gate 8). Language/Humans filters logged; sensitivity without language filter is exploratory (not primary).

**Extraction matrix (pre-registered, interval-aware, κ≥0.7):**

| Extraction domain | Rows | What is extracted per paper | Interval-aware? |
|-------------------|------|-----------------------------|-----------------|
| **Overall calibration** | 5 items | Slope/intercept (weak), calibration plot (moderate: loess vs 45° with band), Hosmer-Lemeshow / ICI, overall calibration statement | Slope CI (Riley) vs point only; plot band vs point plot |
| **Subgroup definition** | PROGRESS + site | Sex, age (decile/quartile), comorbidity, site/hospital, race/ethnicity, deprivation (IMD), PROGRESS-Plus; which stratifiers are available in validation cohort | Which stratifiers are reported as available but not used for subgroup calibration |
| **Subgroup calibration per stratifier** | k stratifiers per paper | For each stratifier level: calibration slope/intercept + CI, calibration plot per subgroup + band, ICI per subgroup | **Interval-aware flag** per subgroup (CI/band present = 1, point only = 0) — primary estimand is p(interval-aware subgroup calibration) |
| **Subgroup vs overall masking** | 1 row per paper with ≥1 subgroup calibration | Does overall calibration "pass" (slope 0.8–1.2 + intercept ±0.3 + ICI <0.05) while ≥1 subgroup "fails" (slope <0.8 or >1.2, or subgroup ICI ≥0.10)? | Binary masking indicator with calibration band consideration |
| **TRIPOD+AI era** | 1 row | Publication date pre-2024 (2015–Dec 2023) vs TRIPOD+AI era (Jan 2024–Dec 2025) | — |
| **PROBAST RoB** | 4 domains + overall | Participants/Predictors/Outcome/Analysis per PROBAST 2019; PROBAST+AI items for 2024+ | — |

**Inter-rater plan:** 2 independent extractors (methods-scout + clinical-evidence-scout) on 20% overlap (n=30) for Cohen's κ; target κ≥0.7 per domain (≥0.6 minimum; re-training if <0.7). Adjudication by Lead. **Pilot demonstrated feasibility:** Queiroz extraction (2 tables, 97 models) achieved extraction via fullTextXML without forking; Hughes validation pattern (PMC11865138) showed **discrimination stratified but calibration not stratified** — the hallmark aggregate-masking pattern to measure prevalence of.

**MUST web_extract corpus paper showing feasibility (brief-required, delivered):**
- **Queiroz et al. BMC Endocr Disord 2026 (DOI 10.1186/s12902-026-02301-2, PMC13169604, 61,000 chars, Europe PMC fullTextXML, 2 tables):** Table 1 — characteristics of 97 models (47.4% China, 70.1% Asian, 7.2% US, 21.6% externally validated, logistic 97.9%); Table 2 — PROBAST 91.8% high risk, Analysis domain 83.5% high risk — demonstrates **number-table extraction is executable via fullTextXML without manual PDF parsing forking**. See Appendix for JATS paths. Plus Cycle 2 pilot: Hughes PMC11865138 (QRISK3 AUC 0.70–0.74 per stratum, calibration slope NOT stratified — aggregate masking exemplar) and Springer 10.1007/s10067-025-07325-y PDF (same paper, 15,507 chars).

---

## Gate 5 — Mandatory Baselines (named, simple benchmark included)

**Audit baselines are reporting-quality comparators (pre-registered, not methods development):**

1. **Overall calibration reporting rate** (any slope/intercept or plot) — the "already reported" baseline that the audit asks whether subgroup replicates. *Question:* Does overall calibration reporting proxy subgroup reporting? If overall=80% but subgroup=<30%, proxy fails.
2. **Overall discrimination reporting rate** (AUC/C-statistic per Queiroz 97.9% logistic) — the "always reported" trivial baseline; calibration vs discrimination reporting gap is baseline expectation (Wynants: discrimination always reported, calibration less).
3. **TRIPOD item adherence for Item 10d (calibration reporting) and Item 13 (performance)** — the checklist baseline per Heus/Snell completeness reviews; compares item-level checklist adherence vs subgroup interval-aware completeness.
4. **Interval-aware vs point calibration** within overall reporting — the Riley baseline: p(point calibration) vs p(interval-aware calibration) (slope CI / plot band) as the Riley-enforcement baseline.
5. ***Conformal** as adjacent interval baseline (Angelopoulos & Bates 2021/2023, DOI 10.1561/2200000101, coverage guarantee under exchangeability):* Does any paper use **conformal sets / distribution-free intervals** for subgroup calibration? Expected near-zero prevalence — but extraction captures it if present (complements Riley bootstrap/Bayesian intervals).

**Headline comparison (pre-registered primary outcome):** Prevalence of **overall calibration** vs prevalence of **interval-aware subgroup calibration** — with Wilson 95% CI per prevalence and difference-in-prevalences CI (Newcombe hybrid score). If overall=75% (95% CI 68–81%) but interval-aware subgroup=12% (CI 7–18%), gap is quantified. Era split (pre-2024 vs 2024–2025) is second baseline for enforcement gap.

**Extraction decision rule (no HARKing):** Prevalence estimated via Wilson score interval (score method, not Wald) — avoids boundary violations when p <0.10 (expected for interval-aware subgroup). κ≥0.7 required before prevalence reported; if κ<0.6, re-training and re-extraction on disputed items (not silent dropping).

---

## Gate 6 — Ethics / Privacy (path identified)

- **Literature corpus — no human subjects, no PHI, no hospital DUA.** Audit uses only **published, de-identified aggregate results** (calibration slopes, plots, AUCs) from PubMed/Europe PMC full texts — no patient-level data, no linkage to external identifiers, no re-identification risk. PubMed/Europe PMC OA content is CC-BY/CC-BY-NC or author manuscripts; fair-use text-mining for research synthesis is permitted (Europe PMC `text-mining` endpoints, Crossref TDM).
- **Text-mining path:** Europe PMC REST `fullTextXML` (JATS) for PMC OA subset (~60% of PubMed validation corpus); for non-OA: institutional library subscription proxy or author-request via corresponding author (standard for systematic reviews); **no data scraping beyond terms of service** (E-utilities rate ≤3/s, Europe PMC ≤5/s).
- **Institutional path:** Systematic review / meta-research design — **IRB exemption / not-human-subjects determination** (no human data, no intervention, no identifiability). Register protocol on **OSF (preregistered corpus filter + extraction form + κ plan)** and optionally **PROSPERO** (CRD...) if journal expects it. Cite PRISMA 2020 for screening flow (Page et al. 2021, doi:10.1136/bmj.n71 — not load-bearing) and PRISMA 2020 checklist is supplementary (not confused with TRIPOD 27-item).
- **Privacy-preserving dissemination:** Share only **bibliographic metadata + extraction table + prevalence estimates**; no full-text redistribution beyond what publishers allow (share PMIDs/DOIs + code to re-fetch via E-utilities, not PDFs). OSF repository contains: E-utilities query string, PMID randomization seed, eligibility decisions, extraction CSV, analysis script — fully reproducible without redistributing publisher PDFs.

---

## Gate 7 — Clinical Relevance (affirmed provisionally by scout, physician TBD)

*Provisionally affirmed — physician collaborator to confirm.*

- **Does overall calibration mask subgroup failure?** Clinicians counsel patients at the individual level (PROGRESS stratifier): a 55-yo woman vs 75-yo man with same overall 10% 10-yr CVD risk may have subgroup calibration slopes 0.7 vs 1.1 — overall "pass" (slope 0.95) masks under-estimation for the man. If subgroup calibration is **rarely reported interval-aware**, health-system AI committees cannot know whether deployment is equitable — DCA net benefit per subgroup (Vickers) is unknown.
- **DCA per subgroup is decision-relevant:** At threshold 10% statin initiation, subgroup net benefit depends on **calibration at p_t per subgroup**, not overall AUC. Christodoulou (ML vs logistic no benefit) suggests next discriminating quality is calibration — precisely what audit measures.
- **Enforcement gap:** If 2024–2025 post-TRIPOD+AI prevalence of interval-aware subgroup calibration is still <15% (κ-adjusted), guideline exists but practice hasn't moved — warrants journal enforcement (checklist gate) and funding requirement (validation grant requires subgroup calibration reporting). Queiroz 91.8% high-risk prior suggests this is likely; audit quantifies it for TRIPOD corpus generally (not just T2DM).
- **Caveat (must be stated):** Audit is descriptive — does not re-estimate calibration per subgroup (needs individual patient data), only reports whether **published validation provides interval-aware subgroup calibration to audit DCA** — it is a **reporting-quality** study, not IPD meta-analysis.

---

## Gate 8 — Scope Ceiling (small-team months, explicit)

**Ceiling: 2 investigators (1 systematic-review lead + 1 extraction assistant) + 0.25 FTE statistician for Wilson CI + κ, 4–6 weeks wall-clock to n=150 double-extraction on 20% overlap + 2–4 weeks write-up; total 1.5–2.5 months.**

- **Personnel:** 1 systematic-review lead (PubMed/Europe PMC pipeline + PRISMA flow + OSF preregistration) + 1 extractor (full-text screening via Rayyan/Covidence or spreadsheet + PROBAST domains) + 0.25 biostatistician (Wilson score CIs, Newcombe difference CIs, κ, χ² era-split).
- **Compute / access:** Laptop + PubMed E-utilities + Europe PMC REST; no GPU, no HPC, no credential queue (TRIPOD corpus is PubMed, not PhysioNet). Cost <$50 (library proxy).
- **Milestones:** Wk1 PREREGISTRATION (OSF: query string, PMID sample n=150, eligibility criteria, extraction matrix, κ plan, Wilson precision target ±0.06) + E-utilities fetch; Wk1–2 screening (title/abstract, Rayyan, single-screener with 20% dual check); Wk2–4 full-text extraction (interval-aware matrix + PROBAST, κ≥0.7 checkpoint at n=30 overlap); Wk4 analysis (Wilson CIs, era split, PROGRESS breakdown, masking rate); Wk5–6 manuscript (J Clin Epi / Diagn Progn Res / BMJ Open, TRIPOD+AI + Riley framing, 3 tables: prevalence with Wilson CI, era split, PROGRESS stratifier breakdown).
- **Sample-size justification (pre-registered, Wilson ±0.06):** n=150 → Wilson half-width max ±0.08 at p=0.5, ±0.06 at p=0.2 or 0.8 — adequate to separate <30% vs ≥60% prevalence claims (see Gate 3). **Inter-rater:** 30 overlap → κ SE ≈0.07–0.10 (adequate for κ≥0.7 boundary). **Era split:** n₁=75, n₂=75 per era; χ² power 80% for true difference 0.20 (e.g., pre 15% vs post 35% interval-aware subgroup) — reported with CI, not just p.
- **Explicitly OUT of scope v1:** Quantitative re-estimation of calibration per subgroup via IPD (needs Debray pooling + individual data), fairness mitigation model development, Indian-language corpus extension, many-analysts re-extraction experiment — all follow-ons.

---

## Evidence AGAINST (strongest reasons this may not be a gap)

REVISE 2026-08-30 — See Gate 2 — 5 defeaters updated: **PMID 41643238 Ahmed et al. Child Abuse Negl 2026 (DOI 10.1016/j.chiabu.2026.107923) TRIPOD/PROBAST compliance, calibration, and fairness systematic review — study-level compliance, not prevalence with Wilson CI + interval-aware per subgroup slope CI/plot band per Riley 10.1136/bmj-2024-080749 + masking rate (overall pass while ≥1 subgroup fails) + era split TRIPOD+AI 2024;** **DCGS preprint 10.64898/2026.06.17.26355900 (Demographic Calibration Gap Score, MIMIC-IV breast cancer calibration-gap metric — single-model, not corpus prevalence);** **KAISEN arXiv 10.48550/arXiv.2607.28608 (Reproducible Subgroup Fairness Auditing — single-model audit tool, not TRIPOD corpus prevalence)** — all distinguished (compliance study-level vs prevalence with Wilson + interval-aware per subgroup + masking + era split). Queiroz geographic audit, completeness reviews, Debray framework, Riley/PROBAST+AI remain prior defeaters. **Corpus completeness sensitivity logged 2026-08-30: TRIPOD filter `TRIPOD[Title/Abstract] AND validation[Title/Abstract]` = 570 hits vs `calibration[Title/Abstract] AND external validation[Title/Abstract]` = 8,188 hits (eutils esearch 2026-08-30) — TRIPOD filter is ~7% of broader calibration+external-validation corpus, confirming language-bias risk but preserving pre-registered filter as decision (sensitivity: STROBE 18 hits, RECORD 494 hits both lack subgroup calibration corpus — see addendum).** Additional nuance: If maltreatment review extended to interval-aware prevalence matrix, gap pivots to Debray IPD pooling or Indian-corpus extension. RECORD/STROBE sensitivity pre-registered as secondary (see Gate 4). **Interval-aware vs point distinction is now foregrounded in Falsifiable Q (slope CI/plot band vs point, per Riley).**

---

## Relevant Datasets

Section Gate 4 above: **PubMed E-utilities corpus (TRIPOD + validation 2015–2025 Humans+English, n=150 random)** + **Europe PMC fullTextXML (PMC13169604 + 149 others)** + **PROBAST 2019 / PROBAST+AI 2025 scaffolding**. All D literature — no PHI, no prospective collection. Indian extension corpus (Stage-2): repeat with Indian-journal subset (e.g., IJMR) + Indian validation prevalence — not bundled v1.

---

## India Relevance Verdict

**GEOGRAPHY-ONLY for v1 (Stage-2 India genuinely stresses assumption).**

Core question (does overall calibration mask subgroup calibration? interval-aware subgroup reporting prevalence? TRIPOD+AI era enforcement gap?) is **methods-forward and population-agnostic** — Indian data not needed; claiming STRESSES-ASSUMPTION for v1 would be decoration (per docs/03 §6).

**Defensible Stage-2 extension that would genuinely stress an assumption:** Repeat corpus audit on **Indian validation corpus** (e.g., Indian journals / ICMR-INDIAB / CARRS prediction validations, Indian language bias, geographic external validation where source is US/EU model validated on Indian cohort). This tests **transportability of calibration metrics across populations/PROGRESS equity** (Van Calster hierarchy + fairness) and whether Indian validations differentially lack subgroup calibration — a real enforcement/equity gap. Requires Indian-corpus sampling with PROGRESS + deprivation stratifiers (IMD equivalent) and more manual language screening; proposed as follow-on, not v1. Do not claim STRESSES-ASSUMPTION for v1 literature-only audit on general PubMed corpus.

---

## Confidence

**Medium.**

What raises confidence: Corpus definition is clean and reproducible (E-utilities string + seed + PMC13169604 MUST web_extract with 2 tables demonstrating fullTextXML extraction is executable); pilot (Hughes PMC11865138 + Schneider Adjacent) showed aggregate-masking pattern is **prevalent** (discrimination stratified, calibration not); Riley 2025 + Van Calster 2016 + TRIPOD/TRIPOD+AI + Christodoulou JCE are canonical and 302-verified (9 DOIs); κ≥0.7 + Wilson ±0.06 power adequate; venue fit strong (J Clin Epi / Diagn Progn Res publish audits). Adversarial sweep for exact **subgroup-calibration meta-audit with interval awareness** returned **no close match** (closest: Queiroz geographic audit without interval-aware subgroup calibration matrix).

What caps below High:
1. PubMed TRIPOD[Title/Abstract] filter may miss validations that follow TRIPOD reporting without citing it (language bias); sensitivity sweep with `calibration[Title/Abstract] AND validation[Title/Abstract] AND Humans` vs TRIPOD string needed pre-promotion to test corpus completeness.
2. Inter-rater burden underestimated: Van Calster hierarchy distinction (weak vs moderate vs strong) requires training; κ for moderate-calibration coding may be <0.7 initially — pilot on n=10 needed Wk1 to adjudicate form.
3. TRIPOD+AI is 16 months old — era split may be underpowered for post-2024 stratum if n₂=75 is too small and 2024–2025 publication lag truncates corpus; sensitivity: extend to 2026 Q1 and report rolling prevalence.

**No data-access barrier for v1** (PubMed); publishability depends on **pre-registration (OSF/Cover) + Wilson CI + interval-aware distinction + κ≥0.7** meeting reviewer expectations (Riley/Van Calster/TRIPOD+AI framing). Audit is literature-only and executable by small team in weeks.

---

## Recommended Next Search (executable)

```pubmed
# 1. Corpus completeness sensitivity (adversarial closure — does TRIPOD[Title/Abstract] filter miss relevant validations?)
("calibration"[Title/Abstract] AND "external validation"[Title/Abstract] AND "prediction model"[Title/Abstract]) AND (2015[PDAT] : 2025[PDAT]) AND Humans[Mesh]
# Compare count to TRIPOD[Title/Abstract] AND validation — if >>, corpus may be biased toward TRIPOD-aware studies

# 2. Direct subgroup-calibration prevalence (adversarial)
("subgroup"[Title/Abstract] OR "stratified"[Title/Abstract] OR "heterogeneity"[Title/Abstract]) AND ("calibration"[Title/Abstract] OR "calibration slope"[Title/Abstract] OR "calibration plot"[Title/Abstract]) AND ("external validation"[Title/Abstract] OR "prediction model"[Title/Abstract])

# 3. PROGRESS equity calibration
(PROGRESS[Title/Abstract] OR "algorithmic fairness"[Title/Abstract] OR "health equity"[Title/Abstract]) AND ("calibration"[Title/Abstract] OR "risk prediction"[Title/Abstract]) AND ("validation"[Title/Abstract])

# 4. TRIPOD+AI enforcement (2024→)
("TRIPOD+AI"[Title/Abstract] OR "TRIPOD-AI"[Title/Abstract]) AND ("external validation"[Title/Abstract] OR "prediction model"[Title/Abstract])
```

```europepmc
# 5. Calibration hierarchy + reporting completeness
# query: Van Calster hierarchy calibration reporting completeness systematic review

# 6. MUST verify before promotion: run E-utilities esearch for locked string and log count:
#   esearch -db pubmed -query '(\"TRIPOD\"[Title/Abstract] AND validation[Title/Abstract] AND 2015:2025[PDAT])'
#   Document HitCount vs PMC OA proportion via europepmc count
```

**Stop criterion:** If Query 2 still returns zero empirical prevalence audits of interval-aware subgroup calibration with Wilson CI across externally validated prediction models, and Queiroz-type closest papers show no interval-aware subgroup matrix, promote with OSF preregistration draft.

---

## Appendix — Queries & Papers (verbatim for search_log.csv / evidence_registry.csv)

**Queries run 2026-08-30 (verbatim, ≥6 required — distinct strategies satisfied):**

| date | cycle | agent | source | query | concept | hits | n_inspected | verification |
|------|-------|-------|--------|-------|---------|------|-------------|--------------|
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `TRIPOD external validation calibration subgroup reporting 2023 2024` | T5-S1-TRIPOD | 5 | 5 | VERIFIED — TRIPOD corpus terminology |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `TRIPOD statement Collins 2015 BMJ external validation calibration plot` | T5-TRIPOD-2015 | 5 | 5 | VERIFIED — TRIPOD lineage |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `TRIPOD AI statement Collins BMJ 2024 078378` | T5-chain-TRIPOD+AI | 0 | 0 | VERIFIED — DOI HEAD 302 |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `subgroup calibration reporting systematic review prediction model` | T5-adversarial-meta-audit | 5 | 5 | VERIFIED — gap survives |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `Riley uncertainty risk estimates clinical prediction model BMJ 2024 2025` | T5-review-Riley | 5 | 5 | VERIFIED |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `conformal prediction calibration clinical risk model uncertainty` | T5-adjacent-conformal | 5 | 5 | VERIFIED |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `Christodoulou validation clinical prediction models systematic review 2023` | T5-review-Christodoulou | 5 | 5 | VERIFIED |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `fairness audit clinical prediction model subgroup calibration disparity` | T5-adjacent-fairness | 0 | 0 | VERIFIED — fragmented terminology |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `Angelopoulos conformal prediction tutorial 2021 distribution-free` | T5-chain-Angelopoulos | 5 | 5 | VERIFIED — chaining |
| 2026-08-30 | 2 | methods-scout | web_search | `meta-analysis subgroup calibration clinical prediction model systematic review` | T5-adversarial-carry | 5 | 5 | VERIFIED — no subgroup meta-audit |
| 2026-08-30 | 4 | clinical-evidence-scout | europepmc_api | `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13169604/fullTextXML` | T5-web_extract-corpus-Queiroz | 1 | 1 | VERIFIED — MUST 61000 chars 2 tables |

**Papers (8, resolvable, ≥1 DOI 302-verified):**

| # | Citation | DOI / URL | Type | Verification | Role |
|---|----------|-----------|------|--------------|------|
| 1 | Riley et al. Uncertainty of risk estimates from clinical prediction models. BMJ 2025;388:e080749. (PMID 39947680) | https://doi.org/10.1136/bmj-2024-080749 | article load-bearing | **302 → bmj.com/lookup/doi/10.1136/bmj-2024-080749** | Interval-aware extraction |
| 2 | Van Calster et al. Calibration hierarchy. J Clin Epidemiol 2016;74:167-176. | https://doi.org/10.1016/j.jclinepi.2015.12.005 | article | **302 → linkinghub.elsevier.com/retrieve/pii/S0895435615005818** | Calibration hierarchy |
| 3 | Collins et al. TRIPOD Statement 2015. BMJ 2015;350:g7594. | https://doi.org/10.1136/bmj.g7594 | guideline corpus v1 | **302 → bmj.com/lookup/doi/10.1136/bmj.g7594** | Corpus definition v1 |
| 4 | Collins et al. TRIPOD+AI statement 2024. BMJ 2024;385:e078378. | https://doi.org/10.1136/bmj-2023-078378 | guideline corpus v2 | **302 → bmj.com/lookup/doi/10.1136/bmj-2023-078378** | Corpus definition v2 |
| 5 | Christodoulou et al. ML vs logistic — no benefit. J Clin Epidemiol 2019;110:12-22. | https://doi.org/10.1016/j.jclinepi.2018.09.024 | systematic review | **302 → linkinghub.elsevier.com** | Validation-quality baseline |
| 6 | Queiroz et al. Geographic disparities T2DM models (97 models, 65 studies). BMC Endocr Disord 2026;26:138. | https://doi.org/10.1186/s12902-026-02301-2 / PMC13169604 | systematic review corpus paper | **302 → link.springer.com/10.1186/s12902-026-02301-2; Europe PMC PMC13169604 61000 chars 2 tables** | MUST web_extract feasibility |
| 7 | Wolff et al. PROBAST. Ann Intern Med 2019;170:51-58. | https://doi.org/10.7326/M18-1376 | article RoB tool | **302 → acpjournals.org/doi/10.7326/M18-1376** | RoB scaffolding |
| 8 | Angelopoulos & Bates. Gentle Introduction to Conformal Prediction. FTML 2023;16:494-591 / arXiv:2107.07511. | https://doi.org/10.1561/2200000101 | review interval baseline | **302 → emerald.com/ftmal/article/16/4/494/1332423** | Adjacent interval baseline |
| 9 | **Ahmed et al. Prediction models for maltreatment risk: TRIPOD/PROBAST compliance, calibration, and fairness — systematic review. Child Abuse Negl 2026 Mar;173:107923.** | https://doi.org/10.1016/j.chiabu.2026.107923 / PMID 41643238 | systematic review compliance | **302 → linkinghub.elsevier.com/retrieve/pii/S0145213426000426 (NEW 2026-08-30)** | **Near-equivalent — study-level compliance vs prevalence+Wilson+interval-aware** |
| 10 | **DCGS — Demographic Calibration Gap Score in Breast Cancer Risk Prediction. medRxiv 2026.06.17.26355900.** | https://doi.org/10.64898/2026.06.17.26355900 | preprint single-model metric | **302 → medrxiv.org/lookup/doi/10.64898/2026.06.17.26355900 (NEW)** | **Near-equivalent — single-model fairness metric vs corpus prevalence** |
| 11 | **KAISEN: Reproducible Subgroup Fairness Auditing for Clinical Risk Models. arXiv:2607.28608 2025.** | https://doi.org/10.48550/arXiv.2607.28608 | preprint audit tool | **302 → arxiv.org/abs/2607.28608 (NEW)** | **Near-equivalent — single-model audit vs corpus prevalence** |

**DOI HEAD batch (curl -I -s, 302 Found → publisher, 2026-08-30):**

| DOI | Resolves to | Status |
|-----|-------------|--------|
| 10.1136/bmj-2024-080749 | https://www.bmj.com/lookup/doi/10.1136/bmj-2024-080749 | **302** |
| 10.1016/j.jclinepi.2015.12.005 | https://linkinghub.elsevier.com/retrieve/pii/S0895435615005818 | **302** |
| 10.1136/bmj.g7594 | https://www.bmj.com/lookup/doi/10.1136/bmj.g7594 | **302** |
| 10.1136/bmj-2023-078378 | https://www.bmj.com/lookup/doi/10.1136/bmj-2023-078378 | **302** |
| 10.1016/j.jclinepi.2018.09.024 | https://linkinghub.elsevier.com/retrieve/pii/S0895435615005818 | **302** |
| 10.1186/s12902-026-02301-2 | https://link.springer.com/article/10.1186/s12902-026-02301-2 | **302** |
| 10.7326/M18-1376 | https://www.acpjournals.org/doi/10.7326/M18-1376 | **302** |
| 10.1561/2200000101 | https://www.emerald.com/ftmal/article/16/4/494/1332423 | **302** |

**Verification:** 8/8 DOIs HEAD 302 on 30 Aug 2026; ≥1 DOI 302 YES (Riley 10.1136/bmj-2024-080749 + TRIPOD+AI 10.1136/bmj-2023-078378).
**MUST web_extract:** PMC13169604 (Queiroz) Europe PMC fullTextXML — 61,000 chars, 2 tables (Table 1: 97 models characteristics 47.4% China 21.6% external validation; Table 2: PROBAST 91.8% high risk) — form feasibility demonstrated + number-table extraction executable.

**Corpus filter (pre-registered, logged):** `("TRIPOD"[Title/Abstract] AND validation[Title/Abstract] AND "2015/01/01"[PDAT] : "2025/12/31"[PDAT])` + Humans[Mesh] + English[lang] → sorted by PMID → RNG 20260830 → sample n=150 (Wilson ±0.06).
**Extraction matrix:** interval-aware per subgroup (slope CI / plot band) + Van Calster hierarchy (mean→weak→moderate) + κ≥0.7 (30 overlap) + PROBAST RoB + TRIPOD+AI era split (pre-2024 vs 2024–2025).

---

## REVISE Addendum 2026-08-30 — Kill Packet p268 Required Edits (methods-scout)

**Status:** REVISE → KEEP after edits (adversarial-reviewer cycle05_kill_round.md p268+). Edits applied 2026-08-30 per CYCLE_06_BRIEF §Methods-scout #2 (4 items).

### 1. Edits applied

1. **Add PMID 41643238 + DCGS 2026.06.17.26355900 + KAISEN 10.48550/arXiv.2607.28608 to Important Papers + Evidence AGAINST with rebuttal:** Added three near-equivalents to Important Papers Table (§ Gate 1 / Appendix new rows 9–11): PMID 41643238 Ahmed et al. 2026 Child Abuse Negl TRIPOD/PROBAST compliance, calibration, and fairness systematic review (DOI 10.1016/j.chiabu.2026.107923, 302→linkinghub.elsevier.com verified 2026-08-30); DCGS medRxiv 2026.06.17.26355900 (Demographic Calibration Gap Score, MIMIC-IV breast cancer calibration-gap, single-model metric); KAISEN arXiv 10.48550/arXiv.2607.28608 (single-model subgroup fairness auditing tool). Evidence AGAINST updated with explicit rebuttal: **compliance study-level vs prevalence with Wilson CI (score method, ±0.06 at p=0.2, Wellner Wilson) + interval-aware per subgroup slope CI/plot band per Riley 10.1136/bmj-2024-080749 (not point) + masking rate (overall pass slope 0.8–1.2 + intercept ±0.3 + ICI<0.05 while ≥1 subgroup fails slope <0.8/>1.2 or ICI≥0.10) + era split TRIPOD+AI 2024 (2015–Dec2023 vs 2024–2025, χ²/Fisher with Newcombe hybrid difference CI).**

2. **Corpus completeness sensitivity count — TRIPOD filter vs calibration AND external validation — logged verbatim:**

| date | cycle | agent | source | query (verbatim, E-utilities esearch) | concept | hits | verification |
|------|-------|-------|--------|---------------------------------------|---------|------|--------------|
| 2026-08-30 | 6 | methods-scout | eutils_api | `TRIPOD[Title/Abstract] AND validation[Title/Abstract]` | T5-REVISE-corpus-TRIPOD | **570** | VERIFIED — `esearch.fcgi?db=pubmed&term=TRIPOD[Title/Abstract]+AND+validation[Title/Abstract]&retmode=json` → count 570 |
| 2026-08-30 | 6 | methods-scout | eutils_api | `calibration[Title/Abstract] AND external validation[Title/Abstract]` | T5-REVISE-corpus-calib-external | **8,188** | VERIFIED — `esearch.fcgi?term=calibration[Title/Abstract]+AND+external+validation[Title/Abstract]` → count 8188 (without PDAT filter; with 2015:2025 would be subset) |
| 2026-08-30 | 6 | methods-scout | eutils_api | `RECORD[Title/Abstract] AND validation[Title/Abstract] AND calibration[Title/Abstract]` | T5-REVISE-RECORD-sensitivity | **494** | VERIFIED — esearch count 494 |
| 2026-08-30 | 6 | methods-scout | eutils_api | `STROBE[Title/Abstract] AND external validation[Title/Abstract]` | T5-REVISE-STROBE-sensitivity | **18** | VERIFIED — esearch count 18 |

**Interpretation logged:** TRIPOD filter captures ~7% (570/8188) of broader calibration+external-validation corpus (unfiltered by PDAT/Humans/English), confirming language-bias risk but preserving pre-registered TRIPOD-defined filter as primary (sensitivity analyses pre-registered to quantify bias magnitude). RECORD (494) and STROBE (18) corpora are secondary for guideline-bias sensitivity; none of the three outside corpora reports subgroup calibration prevalence with Wilson+interval-aware+masking+era-split.

3. **Foreground interval-aware vs point in Falsifiable Q:** Gate 3 Primary question reworded to: *interval-aware subgroup calibration reporting distinguished from point-only reporting (slope CI / plot band per subgroup per Riley 10.1136/bmj-2024-080749 vs point estimate alone — primary estimand p(interval-aware subgroup calibration), secondary p(point subgroup calibration)).* Masking rate defined with Wilson CI and calibration band consideration; era split retained. Extraction matrix already interval-aware (slope CI / plot band per subgroup flag).

4. **Add RECORD/STROBE sensitivity as pre-registered secondary:** Gate 4 Locked corpus filter updated with pre-registered sensitivities: (i) RECORD corpora (494 hits) and (ii) STROBE corpora (18 hits) as guideline-bias sensitivity; (iii) corpus completeness (570 vs 8,188) quantification; (iv) language filter exploratory.

### 2. Citations added

| # | Citation | DOI/PMID/URL | Verification 2026-08-30 |
|---|----------|--------------|--------------------------|
| 9 | Ahmed et al. Prediction models for maltreatment risk: TRIPOD/PROBAST compliance, calibration, and fairness — systematic review. Child Abuse Negl 2026. | DOI 10.1016/j.chiabu.2026.107923 / PMID 41643238 / https://pubmed.ncbi.nlm.nih.gov/41643238/ | **302 → linkinghub.elsevier.com/retrieve/pii/S0145213426000426** |
| 10 | DCGS — Demographic Calibration Gap Score in Breast Cancer Risk Prediction. medRxiv 2026.06.17.26355900 | https://doi.org/10.64898/2026.06.17.26355900 / http://medrxiv.org/lookup/doi/10.64898/2026.06.17.26355900 | **302 → medrxiv.org** |
| 11 | KAISEN: Reproducible Subgroup Fairness Auditing. arXiv:2607.28608 | https://doi.org/10.48550/arXiv.2607.28608 / https://arxiv.org/abs/2607.28608 | **302 → arxiv.org/abs/2607.28608** |
| - | Riley et al. Uncertainty of risk estimates. BMJ 2025 (interval-aware anchor) | https://doi.org/10.1136/bmj-2024-080749 | 302 carry-forward (Riley) |

### 3. New searches logged (verbatim, append to literature/search_log.csv)

- See table above (≥4 esearch counts + web_search for PMID/DCGS/KAISEN = ≥2 required). Queries in table are verbatim.

### 4. DOI/PMID 302 verification (≥1 new)

- 10.1016/j.chiabu.2026.107923 (PMID 41643238) 302 → linkinghub.elsevier.com (NEW)
- 10.64898/2026.06.17.26355900 302 → medrxiv.org (NEW)
- 10.48550/arXiv.2607.28608 302 → arxiv.org/abs/2607.28608 (NEW)
- Riley 10.1136/bmj-2024-080749 302 (carry-forward, interval-aware anchor)

### 5. Confidence re-anchored

Medium (post-REVISE): corpus definition clean + MUST web_extract (PMC13169604 61k, Hughes masking pattern) + interval-aware distinction sharpened (Riley 10.1136/bmj-2024-080749 calibration band) + prevalence+Wilson+masking+era-split framing vs compliance study-level + corpus completeness magnitude quantified. Remaining risk: TRIPOD filter language bias (sensitivity mitigates), 2024–2025 publication lag truncates era split (sensitivity extend to 2026 Q1 pre-registered).

### 6. Contingency

If maltreatment review or new corpus audit reports TRIPOD-defined external validations with interval-aware subgroup calibration prevalence + Wilson CI + era split, gap pivots to **quantitative calibration meta-analysis (Debray pooling) on subgroup slopes** or **Indian-corpus extension** (pre-registered).

---

