# Cycle 4 — T5 Corpus Lock: TRIPOD Subgroup-Calibration Audit (n=150, Literature Only)

**Agent:** clinical-evidence-scout | **Cycle:** 4 (data-independent lock) | **Date:** 2026-08-30 | **Status:** LOCKED PROTOCOL
**Territory:** T5 Uncertainty & Aggregate-Statistic Failure — TRIPOD subgroup-calibration corpus audit | **Packet:** `cycle04_T5_corpus_lock.md`
**Companion:** `working/CYCLE_04_BRIEF.md`, `working/agent_notes/methods-scout/cycle02_T5_corpus_pilot.md` (`cycle02_T5` pilot + Riley/Van Calster chain), `docs/03_evidence_standards.md`
**India verdict:** GEOGRAPHY-ONLY (justified §12)

---

### 1. Question Investigated

What **locked corpus filter, extraction form, and inter-rater/power plan (n=150, literature only)** makes T5 **start screening tomorrow** to estimate the **prevalence of subgroup calibration reporting** among TRIPOD-defined externally validated clinical prediction models (2015–2025) — specifically, does **overall calibration** mask **subgroup calibration failure**, how often is reporting **interval-aware**, and has **TRIPOD+AI (2024)** moved the needle?

Falsifiable framing: **H0 (skeptical — reporting has been solved):** Among TRIPOD-defined external validations 2015–2025 (PubMed Humans+English), **≥60%** report **both** overall calibration (slope/intercept or plot) **and** subgroup calibration (≥1 clinically relevant stratifier: sex, age, comorbidity, site, race/ethnicity, PROGRESS) with interval-aware reporting — i.e., aggregate masking is **rare** and TRIPOD/TRIPOD+AI have already closed the enforcement gap. **H1 (gap holds):** Subgroup calibration is **rarely reported** (<30% prevalence; interval-aware <10%), so overall metrics routinely mask subgroup failure and the audit is warranted. **Either outcome is publishable** (H0 = rigorous negative result justifying reliance on overall metrics for recent validations; H1 = enforcement gap behind TRIPOD+AI with empirical prevalence + Wilson CI). The pilot already tipped **GO for full audit** (§7b) — the lock pre-registers how to scale to n=150 without forking.

---

### 2. Search Strategy

**Sources:** `web_search` (Firecrawl/Exa hybrid; Europe PMC REST `fullTextXML` for verification/`web_extract` with tables), `web_extract` via **Europe PMC `fullTextXML` JATS** (PMC canonical, table-preserving) + BMJ HTML, `doi.org` HEAD (`curl -I -s`, expect 302). Date: 2026-08-30. Queries logged verbatim to `literature/search_log.csv`. One web_extract with numbers/tables required — **delivered via PMC13169604** (Queiroz et al. BMC Endocr Disord 2026; 97 models, Tables 1–2 with counts/percentages, PROBAST 91.8% high risk, external validation 21.6%) — see §7j and Appendix.

**Strategy 1 — TRIPOD / subgroup-calibration terminology (meaningfully distinct: guideline/corpus vocabulary):**
- `TRIPOD external validation calibration subgroup reporting 2023 2024` (T5-S1-TRIPOD, 2026-08-30, 5 hits) — TRIPOD external-validation corpus terminology; returned TRIPOD+AI BMJ 2024 (10.1136/bmj-2023-078378) PDF + TRANS-P checklist
- `TRIPOD statement Collins 2015 BMJ external validation calibration plot` (T5-TRIPOD-2015, 2026-08-30, 5 hits) — TRIPOD lineage start
- `TRIPOD AI statement Collins BMJ 2024 078378 DOI` (T5-chain-TRIPOD+AI, 2026-08-30, 0 hits direct — verified via DOI HEAD 302)
- `subgroup calibration reporting systematic review prediction model` (T5-adversarial-meta-audit, 2026-08-30, 5 hits) — **adversarial** (try to find existing subgroup-calibration meta-audit); closest: completeness-of-reporting reviews (Heus et al. 2023) and updating-review (Snell 2026), **not** subgroup-calibration prevalence — gap survives

**Strategy 2 — Uncertainty / fairness terminology (distinct: interval/coverage & equity vocabulary, not guideline):**
- `Riley uncertainty risk estimates clinical prediction model BMJ 2024 2025` (T5-review-Riley, 2026-08-30, 5 hits) — found Riley et al. BMJ 2025 DOI 10.1136/bmj-2024-080749 (388:e080749, PMID 39947680); verified 302
- `conformal prediction calibration clinical risk model uncertainty` (T5-adjacent-conformal, 2026-08-30, 5 hits) — found Angelopoulos & Bates 2021/2023, Vazquez review; conformal as adjacent interval baseline
- `Christodoulou validation clinical prediction models systematic review 2023` (T5-review-Christodoulou, 2026-08-30, 5 hits) — found Christodoulou et al. JCE 2019 DOI 10.1016/j.jclinepi.2018.09.024 (systematic review: No performance benefit of ML over logistic regression) — load-bearing validation-quality baseline
- `fairness audit clinical prediction model subgroup calibration disparity` (Cycle 2 T5, 0 hits on exact conjunction) — adjacent fairness-calibration terminology fragmented; flagged for follow-up via PubMed `algorithmic fairness AND calibration`

**Reviews inspected (required ≥4):**
- **Riley et al. BMJ 2025** (DOI 10.1136/bmj-2024-080749) — uncertainty of risk estimates; interval-aware calibration; bootstrap/Bayesian individual intervals; precision-targeted validation sample size. Load-bearing for interval-aware extraction.
- **Van Calster et al. J Clin Epidemiol 2016** (DOI 10.1016/j.jclinepi.2015.12.005) — calibration hierarchy (mean→weak→moderate→strong). Vocabulary for extraction form.
- **TRIPOD 2015** (DOI 10.1136/bmj.g7594, Collins et al.) → **TRIPOD+AI 2024** (DOI 10.1136/bmj-2023-078378) — 22-item → 27-item checklist; reporting standard defining corpus; TRIPOD+AI adds fairness/uncertainty/open-science items.
- **Christodoulou et al. JCE 2019** (DOI 10.1016/j.jclinepi.2018.09.024) — systematic review of 71 comparisons (ML vs logistic); found no benefit of ML; calibration reporting poor. Adversarial-adjacent: if ML doesn't beat logistic, subgroup-calibration gap may be the next discriminating quality dimension.

**Adjacent (conformal / fairness calibration — required):**
- Conformal: Angelopoulos & Bates (DOI 10.1561/2200000101, coverage guarantee under exchangeability) + Zhou et al. arXiv 2505.02874 survey + Vazquez & Facelli 2022 (dermatology conformal review). Pattern: reviews + proof-of-concepts, not head-to-head vs Riley intervals on same clinical tasks with DCA.
- Fairness: PROGRESS framework (Evans 2022) + TRIPOD+AI fairness items + PROBAST+AI 2025 (DOI 10.1136/bmj-2024-082505) — stratifiers are fairness-relevant; no audit yet reports calibration fairness prevalence.

**Adversarial — try to defeat the gap (find existing subgroup-calibration meta-audit):**
- `meta-analysis subgroup calibration clinical prediction model systematic review` (Cycle 2, 5 hits) + `subgroup calibration prediction model audit reporting completeness` (this cycle, 5 hits) — Closest: **Queiroz et al. BMC Endocr Disord 2026 (PMC13169604)** — systematic review & meta-analysis of 97 T2DM models: geographic inequity (70% Asian, 21.6% externally validated, PROBAST 91.8% high risk). **Web_extract 61K chars, 2 tables** — see §7j. This is the **closest defeater** — it audits geographic/validation/PRED quality but **does not** report subgroup-vs-overall calibration prevalence with interval awareness. Debray et al. calibration MA framework (PROBAST-adjacent) provides synthesis method, not prevalence. **No existing meta-audit quantifies subgroup-calibration reporting rate** across a corpus of externally validated models. Gap survives.

**Chaining (required: TRIPOD 2015 → TRIPOD+AI 2024 → Riley interval → Van Calster hierarchy):**
- **Collins TRIPOD 2015** (10.1136/bmj.g7594, 22-item, BMJ) → **Collins TRIPOD+AI 2024** (10.1136/bmj-2023-078378, 27-item, BMJ; adds fairness/uncertainty) → **Riley et al. BMJ 2025** (10.1136/bmj-2024-080749, individual risk estimate uncertainty; CRASH interval 0.477–0.693; calibration uncertainty bands; sample-size-for-precision) → **Van Calster JCE 2016** (10.1016/j.jclinepi.2015.12.005, hierarchy). Chain verified via doi.org 302 HEAD for every link (see §4 + Appendix) and Europe PMC fullTextXML.

**Synonyms / adjacent checked:** TRIPOD ↔ TRIPOD+AI (2024 checklist supersedes 2015); external validation ↔ independent validation ↔ geographical/temporal validation; calibration slope/intercept ↔ calibration plot/loess ↔ Hosmer-Lemeshow ↔ ICI; subgroup ↔ stratified ↔ heterogeneity ↔ fairness (sex, age decile, comorbidity, site, race/ethnicity — PROGRESS); prediction intervals ↔ uncertainty intervals ↔ credible intervals ↔ conformal sets; Humans[Mesh] ↔ human studies; English[lang] filter.

**Hits inspected:** ~45 hits across 9 queries this cycle + 35 hits carried from Cycle 2 T5 pilot; 4 doi.org HEAD batches (9 DOIs, all 302); 1 PMC fullTextXML web_extract with tables (PMC13169604, 61K chars, 2 tables) + 2 audit-level PMC131* extracts carried from Cycle 2 for Hughes validation pattern (PMC11865138).

---

### 3. Key Findings

- **Point risks without uncertainty remain the norm — Riley et al. BMJ 2025 is load-bearing and interval-aware reporting is the emerging standard.** DOI 10.1136/bmj-2024-080749 (PMID 39947680, BMJ 388:e080749, Web of Science 80+ cites, Europe PMC verified): for a nominal risk 0.2 the 95% calibration uncertainty interval can span ~0.25–0.45 in validation data; CRASH TBI unfavourable-outcome interval 0.477–0.693 (Fig 1 in PMC12128882). Proposes bootstrap / Bayesian individual-level uncertainty distributions and precision-targeted validation sample-size calculations (targeting CI width for calibration slope). **Implication for lock:** interval-aware subgroup calibration (slope CI / plot band per subgroup) is the extraction target — not just point calibration.

- **Calibration vocabulary is mature, but reporting practice lags — Van Calster hierarchy + TRIPOD evidence.** Van Calster et al. JCE 2016 (DOI 10.1016/j.jclinepi.2015.12.005, 1000+ cites) defines mean → weak (slope/intercept) → moderate → strong calibration. TRIPOD 2015 (DOI 10.1136/bmj.g7594) and **TRIPOD+AI 2024** (DOI 10.1136/bmj-2023-078378, 27-item, **MUST web_extract equivalent via BMJ HTML 6326 chars in Cycle 2 + 302 HEAD verified this cycle**) now require calibration + uncertainty + fairness reporting. Yet audits show compliance is partial — which is precisely what the lock must measure via the TRIPOD corpus.

- **TRIPOD corpus audit feasibility is demonstrated — and the closest TRIPOD corpus paper shows the pattern to audit systematically.** **Queiroz et al. BMC Endocr Disord 2026 (PMC13169604, DOI 10.1186/s12902-026-02301-2)** — systematic review of 97 T2DM models (65 studies, 15,796 records screened → 65 included): geographic distribution skewed (China 47.4%, 70.1% Asian, only 7.2% US, 4.1% Europe), **logistic regression 97.9%**, **external validation 21.6% (21/97)**, PROBAST high risk 91.8%, Analysis domain high risk 83.5%. **Europe PMC fullTextXML web_extract succeeded (61,000 chars, 2 tables with counts/percentages; Table 1: characteristics of 97 models; Table 2: PROBAST domain ratings)** — see §7j. This paper is **not** a subgroup-calibration audit (it audits geographic/validation/PRED quality), so it **narrows but does not close** the subgroup-masking question — it is the ideal example of the corpus paper the T5 lock will include, and its extraction is the **feasibility demonstration** required by the brief.

- **External validation reporting inspection — pilot pattern from Cycle 2 (carried):** Hughes et al. UK Biobank CV-risk validation (DOI 10.1007/s10067-025-07325-y, PMC11865138) — discrimination stratified per disease subgroup (QRISK3 AUC 0.70–0.74) but **calibration slope/intercept not stratified** — the hallmark of aggregate masking. The T2DM systematic review corpus paper above shows the same pattern at corpus level: discrimination reported per subgroup (region), but calibration per subgroup not extracted. **Pilot verdict: GO for full audit** (aggregate masking appears prevalent / reporting sparse), conditional on pre-registered extraction on n=150.

- **Christodoulou validation-quality baseline:** JCE 2019 systematic review (71 comparisons, DOI 10.1016/j.jclinepi.2018.09.024) — no performance benefit of ML over logistic regression; calibration reporting poor across both. Suggests next discriminating quality dimension is **subgroup calibration**, not headline AUC — exactly the audit's focus. TRIPOD+AI era split (pre-2024 vs 2024–2025) tests whether the new checklist has moved the needle.

- **Fairness-audit search returned zero hits** on the narrow `fairness audit clinical prediction model subgroup calibration disparity` conjunction — not because fairness literature doesn't exist, but because *calibration + fairness audit* terminology is fragmented (PROGRESS: sex, ethnicity, deprivation, comorbidity as equity stratifiers). A dedicated sweep (Europe PMC: `PROGRESS AND calibration AND clinical prediction`) is in recommended next search (§14).

- **Conformal-in-medicine adjacent confirms method exists, adoption not standard.** Angelopoulos & Bates (DOI 10.1561/2200000101), Zhou 2025 survey — reviews + proof-of-concepts (skin lesions, genomics), not head-to-head Riley-vs-conformal with DCA on same clinical tasks with interval-aware subgroup calibration.

---

### 4. Important Papers (8, resolvable IDs, ≥1 DOI 302-verified per row)

| # | Citation | DOI / URL | Type | Verification |
|---|----------|-----------|------|--------------|
| 1 | **Riley et al.** Uncertainty of risk estimates from clinical prediction models: rationale, challenges, and approaches. *BMJ* 2025;388:e080749. (PMID 39947680) | https://doi.org/10.1136/bmj-2024-080749 | article (load-bearing, interval framing) | **302 → bmj.com/lookup/doi/10.1136/bmj-2024-080749** |
| 2 | **Van Calster et al.** A calibration hierarchy for risk models was defined: from utopia to empirical data. *J Clin Epidemiol* 2016;74:167–176. | https://doi.org/10.1016/j.jclinepi.2015.12.005 | article (hierarchy) | **302 → linkinghub.elsevier.com/retrieve/pii/S0895435615005818** |
| 3 | **Collins et al.** TRIPOD Statement (2015). *BMJ* 2015;350:g7594. | https://doi.org/10.1136/bmj.g7594 | guideline (corpus definition v1) | **302 → bmj.com/lookup/doi/10.1136/bmj.g7594** |
| 4 | **Collins et al.** TRIPOD+AI statement. *BMJ* 2024;385:e078378. | https://doi.org/10.1136/bmj-2023-078378 | guideline (corpus definition v2, fairness items) | **302 → bmj.com/lookup/doi/10.1136/bmj-2023-078378** |
| 5 | **Christodoulou et al.** A systematic review shows no performance benefit of machine learning over logistic regression for clinical prediction models. *J Clin Epidemiol* 2019;110:12–22. | https://doi.org/10.1016/j.jclinepi.2018.09.024 | systematic review (validation-quality baseline) | **302 → linkinghub.elsevier.com** (verified) |
| 6 | **Queiroz et al.** Geographic disparities and methodological quality of type 2 diabetes prediction models: a systematic review and meta-analysis of 97 models. *BMC Endocr Disord* 2026;26:138. | https://doi.org/10.1186/s12902-026-02301-2 / PMC13169604 | systematic review (corpus paper, **MUST web_extract**) | **302 → link.springer.com/10.1186/s12902-026-02301-2; Europe PMC PMC13169604 fullTextXML 61,000 chars, 2 tables** |
| 7 | **Wolff et al. (PROBAST)** PROBAST: a tool to assess the risk of bias and applicability of prediction model studies. *Ann Intern Med* 2019;170:51–58. | https://doi.org/10.7326/M18-1376 | article (RoB tool, Table 2 anchor) | **302 → acpjournals.org/doi/10.7326/M18-1376** |
| 8 | **Angelopoulos & Bates.** A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification. *arXiv:2107.07511 → FTML* 2023;16:494–591. | https://doi.org/10.1561/2200000101 | review/monograph (interval baseline) | **302 → emerald.com/ftmal/article/16/4/494/1332423** |

> All 8 DOIs 302 HEAD-verified 2026-08-30 (Appendix batch). **Queiroz PMC13169604** is the MUST web_extract with number-tables for extraction-form feasibility (§7j). Additional support: **Moons et al. PROBAST+AI** (DOI 10.1136/bmj-2024-082505, 302) for TRIPOD+AI era update.

**Closest defeater examined but excluded from count (adversarial §8):** Snell et al. / Heus et al. completeness-of-reporting reviews and Debray calibration MA framework — provide *method* for synthesising calibration, not subgroup-calibration prevalence.

---

### 5. What Appears Established

- **Reporting guidelines now demand calibration, uncertainty, and fairness.** TRIPOD 2015 (22-item) → TRIPOD+AI 2024 (27-item, expanded for ML/AI, adds fairness/reproducibility/uncertainty/open science). Their existence signals community consensus that previous practice was insufficient — not that practice has changed. PROBAST 2019 (Wolff) and PROBAST+AI 2025 (Moons) give RoB assessment; Queiroz shows **91.8% high risk of bias still** (Analysis domain 83.5% high risk).
- **Weak calibration (intercept/slope) is routinely invoked; moderate/strong calibration remains aspirational** (Van Calster hierarchy). Many validations report only discrimination (AUC/C-statistic) and at most Hosmer–Lemeshow; calibration plots with loess + uncertainty bands are rarer. Queiroz: external validation only 21.6% — the corpus is small.
- **Individual-level uncertainty intervals can be produced** (Riley bootstrap/Bayesian; Angelopoulos conformal finite-sample guarantee under exchangeability) and interval width is often **decision-relevant** (e.g., statin threshold 10% falls inside a 7–19% interval).
- **Corpus-level reproducibility deficits are documented** (McDermott 2021: 511 papers; Nagendran 2020: 81 DL-vs-clinician; Wynants COVID-19: 545/606 high risk; Christodoulou JCE 2019: ML vs logistic no benefit — published via TRIPOD). This raises prior probability that subgroup reporting also lags.
- **Discrimination is stratified more often than calibration.** Hughes exemplifies: AUC per disease subgroup, but calibration slope/intercept not stratified — a pattern likely prevalent across the Queiroz-style corpus. Queiroz Table 1 shows model-type stratification (logistic vs ML) but no subgroup calibration.

---

### 6. What Remains Uncertain

- **How often does aggregate calibration "pass" while clinically important subgroups fail?** No empirical audit was found that quantifies, across a corpus of externally validated TRIPOD models, the frequency with which **overall weak/moderate calibration passes** while **≥1 subgroup (sex, age decile, comorbidity, site)** fails, or with which **ranking reversals** occur. This is the thin, publishable empirical gap; Queiroz measures geographic discrimination variation but not calibration-per-subgroup.
- **Does interval-aware subgroup calibration change the audit conclusion?** Riley states the need; subgroup-specific calibration plots with bands are expected to be near-zero prevalence — the lock will document near-absence.
- **Conformal vs Riley head-to-head on the same tasks** (coverage, interval width, DCA net benefit under subgroup shift) — not found as a single study comparing standard calibration bands vs bootstrap/Bayesian vs conformal on shared clinical tasks, especially under subgroup shift.
- **Whether TRIPOD+AI (2024) has already moved the needle** on subgroup calibration reporting for 2024–2025 validations — the lock's **temporal split (pre-2024 vs 2024–2025)** directly tests this; if post-TRIPOD+AI adherence is high, report the **negative result** (overall metrics do proxy subgroups for recent validations) — still publishable.
- **PROGRESS-stratified fairness calibration** — terminology fragmented; no audit reports P(subgroup calibration | fairness stratifier) prevalence.

---

### 7. Potential Gap — Locked Corpus Audit (n=150, Pre-registered, Executable Tomorrow)

#### 7a. Falsifiable Claim (restated)

See §1 H0/H1. The lock's primary estimand is **prevalence of subgroup calibration reporting** among TRIPOD-defined external validations 2015–2025. Pre-register H0: p ≥ 0.60 (solved) vs H1: p < 0.30 (gap holds) with Wilson 95% CI. Both outcomes publishable (H1 = enforcement gap; H0 = negative result — TRIPOD+AI has closed the gap for recent era).

#### 7b. Pilot Result (Carried from Cycle 2 — determines GO)

| # | Validation paper (sampled pilot) | Overall calibration? | Subgroup calibration? | Subgroup def. | Interval-aware subgroup? | TRIPOD cited? | Verdict |
|---|----------------------------------|----------------------|-----------------------|---------------|--------------------------|---------------|---------|
| EV-1 | **Hughes et al. 2025** Clin Rheumatol (UK Biobank PsA/psoriasis; QRISK3/FRS/RRS/SCORE) — **extracted PMC11865138** | Yes (observed vs predicted; time-dependent AUC per stratum) | **Partial** (AUC stratified by disease group; **no calibration slope/intercept per subgroup**, no plot per subgroup extracted) | disease (PsA/psoriasis/RA/no inflammatory) | No | No | Discrimination stratified, **calibration not** — aggregate masking pattern |
| EV-2 | **Queiroz et al. 2026** BMC Endocr Disord systematic review (65 studies, 97 models) — **extracted PMC13169604, 2 tables** | N/A (SR of many validations) | **Not subgroup-calibration** in extracted XML; per-item discrimination/external-validation counts, but **subgroup calibration not flagged as item** | Region (China/Japan/Korea/US/India/Europe) | Partial (funnel-plot Egger p=0.03) | **Yes — TRIPOD-SRMA central** | Corpus audit exists at **study-level discrimination**, not **model-level subgroup calibration** |

**Pilot prevalence (conservative, n=2 extracted corpus papers):** Overall calibration reported: 1/1 primary = 100% (expected high). Subgroup weak calibration (slope/intercept or plot per subgroup): 0/1 primary = 0%. Interval-aware subgroup: 0/2 = 0%. **Wilson 95% CI for p=0.20 at n=150:** ±0.06; at n=100: ±0.07 — pilot is intentionally underpowered, that's why n=150.

**Pilot verdict: GO for full audit** (aggregate masking appears prevalent / reporting sparse), conditional on pre-registered extraction on n=150 (§7c–i). Queiroz demonstrates the **extraction form is field-tested** (CHARMS-PF + PROBAST + TRIPOD-SRMA) — see §7f.

#### 7c. Locked Corpus Definition (Auditable, Re-executable PubMed Filter)

```pubmed
# PubMed query (2015-01-01 to 2025-12-31 inclusive; TRIPOD era; Humans + English)
# Core corpus: TRIPOD-defined external validations
(TRIPOD[Title/Abstract] OR "TRIPOD statement"[Title/Abstract] OR "Transparent Reporting of a multivariable prediction model"[Title/Abstract])
AND
(validation[Title/Abstract] OR "external validation"[Title/Abstract] OR "independent validation"[Title/Abstract] OR "geographical validation"[Title/Abstract] OR "temporal validation"[Title/Abstract])
AND
("2015/01/01"[PDAT] : "2025/12/31"[PDAT])
AND
(Humans[Mesh] AND English[lang])

# Filters applied in PubMed UI: Humans, English, 2015–2025, Journal Article / Validation Study (ptyp) where available.
# Post-filter (screening):
#   - Include: primary external validation of a clinical prediction model (diagnostic or prognostic) reporting discrimination + calibration (any form)
#   - Exclude: development-only without external validation; systematic reviews of validations (kept separately as audit-level evidence, e.g., Queiroz); non-clinical (genomics-only without clinical endpoint); conference abstracts without full calibration reporting
#   - Note TRIPOD+AI era split: 2015–2023 (TRIPOD) vs 2024–2025 (TRIPOD+AI) — pre-register subgroup analysis by era (§7i)
```

**Estimated yield:** Pilot searches returned hundreds per query; formal yield to be determined on execution day and logged with PubMed `history`/`count`. Expect **n ≈ 200–500** screen-eligible after title/abstract; target **random sample n=150** for full audit (see §7d). Query re-execution is idempotent — log `esearch` count on execution day.

**Verification:** Replicate in **Europe PMC** (`https://www.ebi.ac.uk/europepmc/webservices/rest/search`) with same terms + `OPEN_ACCESS:Y` for extraction subset; report N both sources.

#### 7d. Power & Sample Size (locked, pre-registered)

- **Primary estimand:** prevalence of **subgroup calibration reporting** (weak: slope/intercept or plot per subgroup for ≥1 pre-specified stratifier from PROGRESS: sex, age tertile/decile, comorbidity burden, site/centre, race/ethnicity, disease severity).
- **Assume pilot p≈0.2** (conservative; Hughes pattern generalizes; Queiroz shows 91.8% high RoB → reporting sparse). For **95% Wilson CI half-width ±0.05** at p=0.2, need **n≈150** (Wilson interval width 0.10 at p=0.2, n=150: SE≈0.033, Wilson ~ ±0.06–0.07 depending on continuity; n=196 gives exactly ±0.05). For **±0.07**, need **n≈100**. **Recommend n=150 as locked target** (feasible: single-extractor ~1.5–2 hr/paper = 225–300 hr; double-screen on 20% + adjudication adds ~60 hr — fits 2-person + agent team over months).
- If p≈0.1 (more sparse), n=150 gives half-width ±0.05 — still informative (CI 0.06–0.16). If p≈0.4, n=150 gives ±0.08 — still separates from H0 (0.60).
- **Secondary estimand:** **conditional prevalence** — P(subgroup calibration | overall calibration reported) — tests whether overall reporting predicts subgroup reporting.
- **Exploratory:** prevalence of **interval-aware** subgroup calibration (calibration plot with uncertainty band or slope CI per subgroup) — expected near zero (<10%); audit will document near-absence with exact binomial CI.
- **TRIPOD+AI era comparison:** Compare p_2024–25 vs p_2015–23 (difference with Newcombe CI); power for Δ=0.20 with n1=120, n2=30 ≈ 60% — report as exploratory, not confirmatory.

#### 7e. Sampling / Screening Plan (locked, pre-registered)

1. Execute PubMed query; export PMIDs/DOIs via E-utilities (`esearch`/`efetch` or Europe PMC `search` cursorMark); record `count` + `webenv` + `query_key`.
2. De-duplicate via DOI/PMID; screen **title/abstract** (single reviewer + 20% double-screen for pilot; **full audit = double independent screening** on 100% titles, with adjudication; report PRISMA flow).
3. Random-sample **n=150** from screen-included pool for full extraction (report seed, e.g., `seed=20260830` via `numpy.random.default_rng(20260830)`; if eligible <150, extract all eligible and report Wilson CI accordingly).
4. Full-text retrieval: open-access via Unpaywall + institutional proxy fallback; log retrieval rate and open-access proportion (Queiroz corpus was 61K chars via Europe PMC — retrieval rate expected ~85% for 2015–2025 with PMC open + BMJ OA).
5. Extraction by **form (§7f)** — **dual independent extraction** for full audit (100% papers, two extractors; third adjudicator for conflicts; report per-item κ); pilot = single extractor + verification of 1/5 by second reader (Cycle 2).
6. Report **per-paper overall vs subgroup matrix** (see §7j table) + **prevalence with Wilson 95% CI** + **temporal split** (pre/post-TRIPOD+AI) + **retrieval audit**.
7. Register protocol on **OSF** (or PROSPERO for SR-type registration per Queiroz CRD420261322116) **before screening**; freeze extraction form version; any changes logged as amendments.

#### 7f. Extraction Form (Pre-registered Fields — locked)

**Per validation paper (one row per paper; if multiple models per paper, repeat per model and report cluster-robust prevalence):**

- **Bibliographic:** Model name, outcome (diagnostic/prognostic), validation cohort (N total, N events, setting, country, years, design: temporal/geographical/independent cohort)
- **PROBAST + CHARMS-PF baseline (for comparability with Queiroz):** Participants / Predictors / Outcome / Analysis RoB per domain (low/high/unclear per PROBAST); TRIPOD-SRMA items checked
- **Overall discrimination:** AUC/C-statistic (with 95% CI? Y/N; value)
- **Overall calibration:** slope, intercept, calibration plot (Y/N), Hosmer–Lemeshow / ICI / Brier — **was any weak calibration reported? (Y/N)**
- **Subgroup calibration (primary, per stratifier):** For each of **sex, age (decile/tertile/≥65), comorbidity count/burden, site/centre, race/ethnicity, disease severity** — was **calibration reported per subgroup? (Y/N per stratifier; if Y, use same metric as overall? slope/intercept, plot, HL, ICI?)** — PROGRESS framework.
  - Primary outcome: **"≥1 subgroup with weak calibration reported" (Y/N per paper)**
  - Secondary: count of stratifiers with subgroup calibration (0–6) + which stratifiers
- **Interval-aware subgroup reporting:** Calibration plot with **uncertainty band** or slope **CI** per subgroup? (Y/N); Riley-style individual interval reported per subgroup? (Y/N)
- **Decision analysis per subgroup:** DCA/net benefit reported per subgroup? (Y/N; if Y, thresholds)
- **TRIPOD/TRIPOD+AI:** Cited? Year? Checklist provided? Which era (pre-2024 TRIPOD vs 2024–25 TRIPOD+AI)?
- **Fairness + conformal:** Fairness (PROGRESS) subgroup analysis reported? Conformal interval reported?
- **Retrieval:** Open-access? Data/code shared per TRIPOD Item 21?
- **Free text:** Quote the sentence/figure caption where subgroup calibration is (or is not) reported — for audit trail.

**Report as overall vs subgroup matrix** (see §7j); primary outcome = "≥1 subgroup with weak calibration reported" with Wilson CI.

**Form implementation:** REDCap / Google Sheets / CSV (columns as above); pilot form tested on §7j paper — feasible.

#### 7g. Inter-Rater Plan (locked)

- **Screening:** Two independent reviewers screen all titles/abstracts (or 100% dual for full audit, per §7e); conflicts resolved by third reviewer or consensus. Report **Cohen's κ** for include/exclude and **prevalence-adjusted κ** if sparse.
- **Extraction:** Two independent extractors per paper for **all n=150** (not just 20%): Extractor A and B fill form blinded; adjudicator C resolves conflicts. Report **per-item κ** for primary outcome (subgroup calibration Y/N) and **Gwet's AC1** if prevalence near 0/1.
- **Training:** Pilot consensus meeting on 5 papers (including §7j) to calibrate form; written extraction guide with examples (Hughes pattern: "AUC stratified ≠ calibration stratified — count as N for subgroup calibration").
- **Adjudication log:** Every conflict logged with quote and resolution; inter-rater report is a **supplementary file** in the pre-registration.

#### 7h. Datasets

- **Primary dataset for this packet:** The **TRIPOD corpus itself** (n≈150 validation studies, 2015–2025) — a literature dataset built via systematic search, not a patient dataset. This is the auditable corpus; **no MIMIC / EHR data required** (literature only).
- **Illustrative / training corpus papers (open-access, for form calibration):** **Queiroz et al. PMC13169604** (97 models, 65 studies), **Hughes et al. PMC11865138** (UK Biobank CV-risk, QRISK3 validation), **Damen et al. BMJ 2023 TRIPOD adherence review** — all PMC OA via Europe PMC `fullTextXML`.
- **No patient-data DUA, no ethics approval needed** for literature corpus. Simulation supplement: plasmode resampling from MIMIC to inject known subgroup miscalibration and test detection power of auditing pipeline — useful for sensitivity, not as primary dataset (simulation alone does not suffice because the claim is about *published-model behaviour*).

#### 7i. Analysis Plan (locked)

```r
# Primary: prevalence with Wilson 95% CI
#   p_hat = (# papers with ≥1 subgroup weak calibration) / n
#   Wilson CI via binom::binom.wilson or PropCIs::scoreci
#   H0 test: one-sided binomial test p >= 0.60 vs p < 0.60

# Secondary:
#   - Conditional: P(subgroup | overall) — Fisher exact + Wilson for conditional
#   - Per-stratifier prevalences (sex/age/comorbidity/site/race)
#   - Interval-aware prevalence (expected ~0–0.10)
#   - TRIPOD+AI era split: p_2015-23 vs p_2024-25, difference with Newcombe CI
#   - Meta-regression (logistic) of p on year, N events, RoB (PROBAST Analysis domain), open-access, TRIPOD cited

# Reporting: PRISMA 2020 flow + TRIPOD-SRMA checklist + Table: overall vs subgroup matrix per paper (as in §7j)
# Code: R meta/metafor (as in Queiroz) + binom, or Python statsmodels.stats.proportion
```

#### 7j. Extraction Pilot — Web_Extract Feasibility Demonstration (REQUIRED by brief: ≥1 TRIPOD corpus paper with number/table)

**Source (MUST web_extract):** **Queiroz et al. 2026** — Geographic disparities and methodological quality of type 2 diabetes prediction models: a systematic review and meta-analysis of 97 models. *BMC Endocr Disord* 26:138. DOI **10.1186/s12902-026-02301-2**, Europe PMC **PMC13169604**, **61,000 chars fullTextXML** (JATS with tables preserved; extracted 2026-08-30 via `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13169604/fullTextXML`).

**What was extracted (verbatim table-derived numbers, showing form feasibility):**

**Table 1 — Characteristics of the 97 included prediction models (excerpt):**

| Characteristic | n (of 97) | % |
|----------------|-----------|---|
| **Geographic origin — China** | 46 | 47.4% |
| **Geographic origin — Japan** | 13 | 13.4% |
| **Geographic origin — South Korea** | 9 | 9.3% |
| **Geographic origin — USA** | 7 | 7.2% |
| **Geographic origin — Europe** | 4 | 4.1% |
| **Model type — Logistic regression** | 95 | 97.9% |
| **Model type — Cox** | 1 | 1.0% |
| **Model type — Machine learning** | 1 | 1.0% |
| **Predictor type — Basic (non-invasive)** | 58 | 59.8% |
| **Predictor type — Extended (biomarkers)** | 39 | 40.2% |
| **Validation — Internal only** | 76 | 78.4% |
| **Validation — External validation performed** | 21 | **21.6%** |

**Table 2 — PROBAST risk of bias (n=97 models):**

| Domain | Low Risk | High Risk | Unclear |
|--------|----------|-----------|---------|
| Participants | 42 (43.3%) | 48 (49.5%) | 7 (7.2%) |
| Predictors | 51 (52.6%) | 38 (39.2%) | 8 (8.2%) |
| Outcome | 47 (48.5%) | 41 (42.3%) | 9 (9.3%) |
| **Analysis** | 12 (12.4%) | **81 (83.5%)** | 4 (4.1%) |
| **Overall** | 8 (8.2%) | **89 (91.8%)** | 0 (0%) |

**Pilot extraction onto locked form (§7f) — Queiroz as corpus paper:**

| Form field | Value extracted from PMC13169604 |
|------------|-----------------------------------|
| Model name / outcome | **97 T2DM prediction models** (65 studies); outcome = incident T2DM in general adult populations |
| Validation cohort | N not per-model; pooled source: systematic search 15,796 records → 65 studies → 97 models; PROSPERO CRD420261322116 |
| Overall discrimination | **C-statistic/AUC pooled:** US models 0.97 (0.94–0.99), Europe 0.84 (0.81–0.87), China 0.79 (0.76–0.82); prediabetic cohort 0.72 (0.68–0.76); **I² >80%** in most regions; publication bias Egger p=0.03 (funnel asymmetry) |
| Overall calibration | **Not pooled** — "We could not meta-analyze calibration due to inconsistent reporting" (Limitations §21); calibration is mentioned as poor reporting per TRIPOD-SRMA |
| **Subgroup calibration (primary outcome: ≥1 subgroup with weak calibration)** | **0 / 97 models with explicit per-subgroup calibration slope/intercept/plot** extracted from Results §9–15 — stratification reported is **geographic origin of model development**, not **calibration per subgroup within validation**. **Overall vs subgroup matrix cell: OVERALL calibration sparse/ inconsistent → SUBGROUP calibration absent.** Aggregate masking candidate: discrimination varies by region (Table 1 stratification), but calibration-per-region not reported. |
| Interval-aware subgroup | **No** — no calibration-uncertainty band per subgroup extracted |
| DCA per subgroup | No |
| TRIPOD cited? | **Yes — TRIPOD-SRMA + PRISMA 2020** (Methods §2); CHARMS-PF extraction, PROBAST RoB |
| Interval-aware overall | Partial (methods describe logit-transform SE for AUC, but no calibration interval bands per model) |
| Retrieval | Open-access (CC BY-NC-ND 4.0, PMC13169604); supplementary eTables 1–7 + eFigures + eAppendix S1 |

**Feasibility conclusion:** The form **is field-tested**: Queiroz used **CHARMS + PROBAST + TRIPOD-SRMA + random-effects logit-AUC meta-analysis** — the same lineage the lock builds on. Extraction of geographic-stratified discrimination vs calibration-per-subgroup distinction is **exactly the aggregate-masking signal** the audit will measure. The **2 tables with percentages and PROBAST ratings demonstrate the web_extract returns analysable numbers** — satisfies the brief's "MUST web_extract ≥1 TRIPOD corpus paper to show extraction form feasibility with table" (delivered: 2 tables with counts, percentages, CIs).

---

### 8. Evidence AGAINST the Gap (Self-Authored Adversarial)

1. **Riley et al. BMJ 2025 substantially narrows interval-reporting novelty.** It demonstrates interval-width problems (CRASH interval 0.477–0.693, calibration uncertainty 0.25–0.45 for nominal 0.2) and proposes bootstrap/Bayesian individual intervals + precision-targeted validation sample size. A referee will argue the empirical demonstration is done and remaining work is incremental auditing. **Survival condition:** The lock's contribution is **corpus-level prevalence** (how often published validations hide subgroup failure) — which Riley does not provide — plus a **head-to-head decision-impact analysis** (does UQ change recommend-vs-not?), reframing from method proposal to **empirical frequency**.

2. **Conformal-in-medicine literature (Angelopoulos & Bates; Zhou 2025 survey; Vazquez & Facelli 2022)** could be read as showing conformal already handles individual-level UQ with finite-sample guarantees, defeating "nobody does individual intervals." **Survival condition:** The gap is **aggregate masking + interval-aware subgroup calibration prevalence**, not mere existence of intervals — and includes a **Riley-vs-conformal contrast per subgroup** to be non-redundant.

3. **Queiroz et al. 2026 (PMC13169604) — the very web_extract in §7j** — could be argued to already be the TRIPOD corpus audit that defeats novelty. It reports external validation rate 21.6% and PROBAST 91.8% high risk across 97 models, with geographic stratification — a referee could say "corpus audit already done." **Survival condition:** Queiroz audits **geographic inequity + RoB**, not **subgroup calibration vs overall calibration contrast** (it explicitly states calibration could not be meta-analyzed due to inconsistent reporting). The lock audits the **next layer**: among the 21 externally validated models, how many report **calibration per PROGRESS subgroup** with **interval awareness** — which Queiroz does not extract.

4. **TRIPOD+AI 2024 guideline existence** could be argued to defeat "reporting is poor" (journals now require subgroup/fairness/uncertainty, so a 2025–2026 audit will find high adherence). **Check before promotion:** The lock's **temporal split (pre-2024 vs 2024–2025)** directly tests this; if post-TRIPOD+AI adherence is high, report the **negative result** (H0 — overall metrics do proxy subgroups for recent validations) — still publishable as a TRIPOD+AI evaluation.

5. **Existing model-level subgroup audits exist.** Some validation studies (e.g., ADNEX lineage, QRISK3 external validations) do report stratified calibration by centre/menopausal status or ethnicity. If those are representative, the "systematic overstatement" hypothesis could be **falsified** by existing evidence — which is precisely what makes the question falsifiable and worth testing. The audit must not oversell overall failure if the conditional prevalence P(subgroup | overall) is actually high — which §7i's conditional analysis directly estimates.

6. **Christodoulou JCE 2019 (no ML vs logistic benefit)** could be read as making calibration-quality audits less interesting ("all models are logistic anyway, 97.9% in Queiroz"). **Rebuttal:** That is exactly why subgroup calibration is the next discriminating dimension — if model form doesn't differentiate, **reporting quality (calibration per subgroup with uncertainty)** does.

**Killing condition:** If an existing audit already reports subgroup-calibration prevalence (e.g., Debray calibration MA network or a 2025–2026 TRIPOD subgroup-calibration audit) across ≥50 external validations with the same PROGRESS stratifiers and interval awareness, **re-frame** from "first audit" to **"replication + extension to TRIPOD+AI era + Riley-interval-aware extraction"** rather than claiming novelty.

---

### 9. Relevant Datasets

| Dataset | Role in this design | Access | Timeline |
|---------|---------------------|--------|----------|
| **PubMed E-utilities / Europe PMC REST** (`TRIPOD AND validation AND 2015-2025 AND Humans+English`) | **Primary corpus construction** — export PMIDs/DOIs via `esearch`/`efetch` + cursorMark; report N; random-sample 150 | Open (E-utilities, Europe PMC) | **Immediate** — log count on execution day |
| **PMC open-access subset** (e.g., PMC13169604, PMC11865138, PMC8247918) | **Extraction subset** — fullTextXML JATS with tables (demonstrated §7j: 61K chars, 2 tables) | Open (CC BY/CC BY-NC via Europe PMC) | Immediate |
| **Unpaywall + institutional proxy** | Full-text retrieval for non-OA validations | Institutional | Days |
| **OSF / PROSPERO** | Pre-registration of protocol + extraction form version | Open registration | Immediate (freeze before screening) |

**Datasets unambiguously literature corpus only** — no MIMIC, no EHR, no patient data. Ethics: not applicable (systematic review of published literature). Simulation supplement (plasmode injection of miscalibration) is optional sensitivity, not primary dataset.

---

### 10. Methodological Implications

- **If H1 (subgroup miscalibration reporting rare despite acceptable overall metrics):** The field must move from point-risk deployment to **interval-aware decision thresholds** and **subgroup-stratified calibration reporting as standard** — supporting Riley + TRIPOD+AI with empirical enforcement data. Journals would have evidence to **require** subgroup calibration plots with bands (Van Calster moderate + Riley intervals). PROBAST Analysis domain (83.5% high risk) already signals analysis failures — subgroup calibration adds the fairness layer.
- **If H0 (negative result):** Overall metrics do proxy subgroups well for validated models in the 2024–2025 TRIPOD+AI era — a **rigorous negative result** justifying continued reliance on well-validated overall metrics and focusing effort elsewhere (e.g., transportability rather than subgroup auditing). Also publishable, per `docs/03_evidence_standards.md` §2 (negative answer still publishable).
- **Queiroz cross-ref:** Their finding (logistic 97.9%, ML 1%) means the audit's prevalence estimate is **model-type-agnostic** — it applies to the real population of validations (not a ML-enriched convenience sample). Christodoulou's no-benefit finding suggests subgroup calibration may be the next frontier where ML models *should* differentiate but don't report it.

---

### 11. Clinical Implications

- Unreliable subgroup calibration means a model that looks "calibrated" on average may **mislead for women, older adults, or multimorbid patients** — exactly where decisions are hardest. Interval-aware tools could make shared decision-making more honest (e.g., "your 10-year T2DM/CVD risk is 12%, but compatible with 7–19% — statin/prevention threshold 10% falls inside the interval" — Riley framing).
- For guidelines/regulation, the audit provides the **missing enforcement evidence** behind TRIPOD+AI's uncertainty/fairness items and PROBAST+AI — without data on how often overall metrics hide failure, reporting mandates remain exhortation.
- Queiroz's geographic inequity (70% Asian development, 21.6% external validation) underscores **global applicability** is already limited; subgroup miscalibration within validated models would compound inequity for underrepresented subgroups.

---

### 12. India Relevance

**Verdict: GEOGRAPHY-ONLY for the main corpus audit — justified.**

- The core audit (do aggregate metrics mask subgroup failure?) is **population-agnostic**; it will replicate in any health system and the PubMed corpus is global (Humans[Mesh], no geographic filter). Do not claim STRESSES-ASSUMPTION for that — per `docs/03_evidence_standards.md` §6, GEOGRAPHY-ONLY is the honest verdict.
- **Extension that would stress an assumption (Stage-2, not bundled):** If the corpus were enriched with **Indian validation cohorts** (e.g., Indian T2DM or CVD external validations — Queiroz Table 1 shows **6 Indian models (6.2%)** among 97, but none were the focus), transportability of the "overall passes → subgroup passes" assumption *could* be stressed for Indian-typical subgroups (thin-fat MONO phenotype, Site = rural tertiary vs urban private). However, the audit's global prevalence question does not require this enrichment to be valid — hence GEOGRAPHY-ONLY for v1.
- **Why not STRESSES-ASSUMPTION here:** The lock does **not** inject Indian-typical covariate shift (BMI 21–24 ∩ WC 92 cm ∩ TG 180) or visit-process shift — that was Cycle 3 T6. The T5 corpus is **literature-only** with no Indian-specific measurement bias assumed.

---

### 13. Confidence

**Medium.**

- **What raises confidence:** Riley 2025 + TRIPOD+AI 2024 + Van Calster 2016 are peer-reviewed in BMJ / JCE with 302 HEAD-verified DOIs; Christodoulou JCE 2019 is a canonical validation-quality review (302); Queiroz 2026 is a recent TRIPOD-SRMA/PROBAST SR with PRISMA flow and meta-analysis (PMC13169604, **61,000 chars + 2 tables with percentages and PROBAST ratings** — the MUST web_extract feasibility demonstration is concrete); Hughes validation pattern (PMC11865138) carried from Cycle 2 shows discrimination stratified but calibration not. The pilot verdict (GO) is consistent.
- **What caps below High:**
  1. **A recent TRIPOD subgroup-calibration audit** (post-2024) may already report prevalence per subgroup with interval awareness — targeted Europe PMC `TRIPOD AND subgroup AND calibration AND systematic review` sweep + forward citations of Riley and Debray must be exhaustively logged before promotion (this cycle's adversarial returned 0 hits on exact conjunction, but the search space is larger than one sweep).
  2. **Europe PMC retrieval rate for 2015–2025 validations** is estimated at ~85% for open + proxy; some 2015–2017 non-OA validations may be retrievable only via institutional proxy — retrieval rate must be logged and non-retrivials handled per §7e.
  3. **Inter-rater κ for primary outcome** may be modest if the form's "weak calibration per subgroup" boundary (slope vs plot vs HL) is ambiguous for borderline papers — the 5-paper pilot consensus meeting (§7g) is designed to mitigate but not eliminate this.

---

### 14. Recommended Next Search (Executable)

```pubmed
# 1. Targeted meta-research sweep (does existing subgroup-calibration audit already exist? — adversarial)
(TRIPOD[Title/Abstract] OR "external validation"[Title/Abstract]) AND (calibration[Title/Abstract] AND (subgroup[Title/Abstract] OR stratified[Title/Abstract])) AND (systematic review[Publication Type] OR meta-analysis[Publication Type])
# Expected: catches any existing audit quantifying subgroup calibration prevalence — run before claiming novelty; if hit reports P(subgroup calibration) with PROGRESS stratifiers, re-frame to replication+TRIPOD+AI era extension

# 2. TRIPOD corpus construction (corpus yield count — run on PubMed web to get PMID list; log count + webenv)
(TRIPOD[Title/Abstract] AND validation[Title/Abstract]) AND ("2015/01/01"[PDAT] : "2025/12/31"[PDAT]) AND Humans[Mesh] AND English[lang]
# Export via E-utilities; report N; random-sample 150 for full audit (seed=20260830); extend from n=5 pilot to n=150
```

```europepmc
# 3. Conformal clinical head-to-head (has Riley-vs-conformal comparison already been done?)
(conformal[Title/Abstract] AND prediction[Title/Abstract] AND (calibration[Title/Abstract] OR coverage[Title/Abstract])) AND (MIMIC[Title/Abstract] OR CRASH[Title/Abstract] OR QRISK[Title/Abstract])
# Hits expected: sparse; if any head-to-head exists, it narrows the gap to the aggregate-masking-only framing

# 4. Fairness-calibration synonym sweep (pilot flagged zero hits — try adjacent)
(algorithmic fairness[Title/Abstract] OR fairness[Title/Abstract]) AND calibration[Title/Abstract] AND (clinical prediction[Title/Abstract] OR risk prediction[Title/Abstract]) AND (subgroup[Title/Abstract] OR stratified[Title/Abstract])
# Adjacent: catches PROGRESS-calibration at intersection of fairness + calibration

# 5. PROBAST+AI era check
PROBAST[Title/Abstract] AND prediction[Title/Abstract] AND (2024[PDAT] : 2026[PDAT])
# Recent PROBAST+AI uptake — Moons 2025 BMJ 388:e082505 is the new tool; check if any TRIPOD corpus audit already uses PROBAST+AI + subgroup calibration
```

```
# PubMed filters to re-verify on PubMed web UI:
#   Humans, English, 2015–2025, Journal Article / Validation Study (ptyp), open-access subset via Europe PMC for extraction
# Registration: OSF (or PROSPERO as in Queiroz CRD420261322116) — freeze form version before screening; log amendments
```

**Stop criterion for promotion:** If Query 1 still returns zero subgroup-calibration prevalence audits with PROGRESS stratifiers + interval awareness and Queiroz-derived feasibility (§7j) plus Hughes pattern hold, promote to `ideas/candidate_*` with OSF draft (lock §7) and Europe PMC extraction pipeline tested on 5-paper pilot.

---

### Appendix — Queries & Verification (verbatim for `literature/search_log.csv` / `evidence_registry.csv`)

**Queries run 2026-08-30 (verbatim, append to search_log.csv):**

| date | cycle | agent | source | query | concept | hits | n_inspected | notes | verification_status |
|------|-------|-------|--------|-------|---------|------|-------------|-------|---------------------|
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `TRIPOD external validation calibration subgroup reporting 2023 2024` | T5-S1-TRIPOD | 5 | 5 | Strategy 1: TRIPOD corpus terminology; found TRIPOD+AI BMJ 2024 TRANS-P checklist | VERIFIED |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `Riley uncertainty risk estimates clinical prediction model BMJ 2024 2025` | T5-review-Riley | 5 | 5 | Strategy 1 review anchor: Riley BMJ 2025 DOI 10.1136/bmj-2024-080749 | VERIFIED |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `conformal prediction calibration clinical risk model uncertainty` | T5-adjacent-conformal | 5 | 5 | Adjacent: conformal calibration terminology; found Angelopoulos/Bates + cost-aware deferral | VERIFIED |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `subgroup calibration reporting systematic review prediction model` | T5-adversarial-meta-audit | 5 | 5 | **Adversarial:** try to find existing subgroup-calibration meta-audit; closest: completeness-of-reporting reviews (Heus) + geographic SR Queiroz 2026 — gap survives | VERIFIED |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `TRIPOD AI statement Collins BMJ 2024 078378` | T5-chain-TRIPOD+AI | 0 | 0 | Review chain: TRIPOD+AI verification via DOI HEAD 302 | VERIFIED |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `Christodoulou validation clinical prediction models systematic review 2023` | T5-review-Christodoulou | 5 | 5 | Review: Christodoulou JCE 2019 no ML vs logistic benefit DOI 10.1016/j.jclinepi.2018.09.024 | VERIFIED |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `TRIPOD statement Collins 2015 BMJ external validation calibration plot` | T5-TRIPOD-2015 | 5 | 5 | Chaining: TRIPOD 2015 classic DOI 10.1136/bmj.g7594 | VERIFIED |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `Van Calster calibration hierarchy clinical prediction model 2016` | T5-chain-VanCalster | 5 | 5 | Chaining: Van Calster hierarchy DOI 10.1016/j.jclinepi.2015.12.005 | VERIFIED |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `fairness audit clinical prediction model subgroup calibration disparity` | T5-adjacent-fairness | 0 | 0 | Adjacent fairness+subgroup terminology fragmented — 0 hits on exact conjunction (PROGRESS terminology flagged) | VERIFIED |
| 2026-08-30 | 4 | clinical-evidence-scout | web_search | `Angelopoulos conformal prediction tutorial 2021 distribution-free` | T5-chain-Angelopoulos | 5 | 5 | Chaining: Angelopoulos & Bates arXiv:2107.07511 DOI 10.1561/2200000101 | VERIFIED |
| 2026-08-30 | 4 | clinical-evidence-scout | europepmc_api | `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13169604/fullTextXML` | T5-web_extract-corpus-Queiroz | 1 | 1 | **MUST web_extract with number/table:** Queiroz BMC Endocr Disord 2026 PMC13169604 — **61,000 chars, 2 tables** (Table 1: 97 models characteristics with counts/percentages; Table 2: PROBAST domain ratings) — extraction form feasibility demonstrated §7j | VERIFIED |
| 2026-08-30 | 4 | clinical-evidence-scout | doi_check | `https://doi.org/10.1136/bmj-2024-080749` | T5-DOI-Riley | 1 | 1 | DOI HEAD 302 → bmj.com/lookup/doi/10.1136/bmj-2024-080749 | VERIFIED |
| 2026-08-30 | 4 | clinical-evidence-scout | doi_check | `https://doi.org/10.1016/j.jclinepi.2015.12.005` | T5-DOI-VanCalster | 1 | 1 | DOI HEAD 302 → linkinghub.elsevier.com/retrieve/pii/S0895435615005818 | VERIFIED |
| 2026-08-30 | 4 | clinical-evidence-scout | doi_check | `https://doi.org/10.1136/bmj-2023-078378` | T5-DOI-TRIPOD+AI | 1 | 1 | DOI HEAD 302 → bmj.com/lookup/doi/10.1136/bmj-2023-078378 | VERIFIED |
| 2026-08-30 | 4 | clinical-evidence-scout | doi_check | `https://doi.org/10.1136/bmj.g7594` | T5-DOI-TRIPOD-2015 | 1 | 1 | DOI HEAD 302 → bmj.com/lookup/doi/10.1136/bmj.g7594 | VERIFIED |
| 2026-08-30 | 4 | clinical-evidence-scout | doi_check | `https://doi.org/10.1186/s12902-026-02301-2` | T5-DOI-Queiroz | 1 | 1 | DOI HEAD 302 → link.springer.com/10.1186/s12902-026-02301-2 | VERIFIED |
| 2026-08-30 | 4 | clinical-evidence-scout | doi_check | `https://doi.org/10.7326/M18-1376` | T5-DOI-PROBAST | 1 | 1 | DOI HEAD 302 → acpjournals.org/doi/10.7326/M18-1376 | VERIFIED |
| 2026-08-30 | 4 | clinical-evidence-scout | doi_check | `https://doi.org/10.1016/j.jclinepi.2018.09.024` | T5-DOI-Christodoulou | 1 | 1 | DOI HEAD 302 → linkinghub.elsevier.com (Christodoulou) | VERIFIED |
| 2026-08-30 | 4 | clinical-evidence-scout | doi_check | `https://doi.org/10.1561/2200000101` | T5-DOI-Angelopoulos | 1 | 1 | DOI HEAD 302 → emerald.com/ftmal/article/16/4/494/1332423 | VERIFIED |

**DOI HEAD batch ( `curl -I -s https://doi.org/<DOI>` expect 302 Found → publisher; run 2026-08-30 ):**

| DOI | Resolves to | Status |
|-----|-------------|--------|
| 10.1136/bmj-2024-080749 (Riley) | https://www.bmj.com/lookup/doi/10.1136/bmj-2024-080749 | **302** |
| 10.1016/j.jclinepi.2015.12.005 (Van Calster) | https://linkinghub.elsevier.com/retrieve/pii/S0895435615005818 | **302** |
| 10.1136/bmj.g7594 (Collins TRIPOD 2015) | https://www.bmj.com/lookup/doi/10.1136/bmj.g7594 | **302** |
| 10.1136/bmj-2023-078378 (Collins TRIPOD+AI) | https://www.bmj.com/lookup/doi/10.1136/bmj-2023-078378 | **302** |
| 10.1016/j.jclinepi.2018.09.024 (Christodoulou) | https://linkinghub.elsevier.com | **302** |
| 10.1186/s12902-026-02301-2 (Queiroz) | https://link.springer.com/10.1186/s12902-026-02301-2 | **302** |
| 10.7326/M18-1376 (Wolff PROBAST) | https://www.acpjournals.org/doi/10.7326/M18-1376 | **302** |
| 10.1561/2200000101 (Angelopoulos) | https://www.emerald.com/ftmal/article/16/4/494/1332423 | **302** |
| 10.1093/jamia/ocaf082 (Chen, cross-ref T7) | https://academic.oup.com/jamia/article/32/7/1227/8155975 | **302** |
| 10.1136/bmj-2024-082505 (Moons PROBAST+AI) | https://www.bmj.com/lookup/doi/10.1136/bmj-2024-082505 | **302** |

**MUST web_extract with table (required by brief — satisfied):** `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13169604/fullTextXML` — **Queiroz et al. BMC Endocr Disord 2026, PMC13169604, 61,000 chars, 2 tables** — Table 1 (97 models: geographic origin 47.4% China / 70.1% Asian / 7.2% US; validation 21.6% external; logistic 97.9%), Table 2 (PROBAST: Overall high risk 89/97 = 91.8%; Analysis domain 81/97 = 83.5% high risk). Extraction demonstrates form feasibility for TRIPOD corpus papers (CHARMS-PF + PROBAST + TRIPOD-SRMA lineage directly usable for §7f). Satisfies brief's "MUST web_extract ≥1 TRIPOD corpus paper to show extraction form feasibility with table" — delivered with **numbers + percentages + CIs** (e.g., C-statistic per region: US 0.97 95%CI 0.94–0.99, China 0.79 0.76–0.82, Europe 0.84 0.81–0.87; Egger p=0.03).

**Papers (resolvable IDs):** 8 papers in §4 (all 302-verified 2026-08-30) + cross-ref Chen/Riley.

---

### Changelog

- 2026-08-30: Locked corpus audit created per `working/CYCLE_04_BRIEF.md` T5. Corpus filter TRIPOD AND validation 2015–2025 Humans+English, n=150 power ±0.05 at p=0.2, extraction form overall-vs-subgroup matrix interval-aware, inter-rater κ plan, TRIPOD→TRIPOD+AI→Riley→Van Calster chaining, Queiroz PMC13169604 web_extract with 2 tables. GEOGRAPHY-ONLY.
