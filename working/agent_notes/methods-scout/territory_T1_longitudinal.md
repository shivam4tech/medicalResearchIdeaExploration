# Territory T1 — Longitudinal & Irregular Clinical Time Series
**Agent:** methods-scout | **Cycle:** 1 | **Date:** 2026-08-30

---

### Question investigated
When does modelling irregularity *itself* (latent-state models, Gaussian processes, marked point processes, neural ODEs/continuous-time RNNs) actually improve inference or prediction over well-specified classical baselines (linear mixed models, joint longitudinal–survival models, GEE) on realistic clinical noise — where sampling is irregular, informative, and sparse? Landscape question: is there a falsifiable, methods-forward gap around head-to-head benchmarking under plausible EHR generating mechanisms, rather than yet another architecture proposal?

### Search strategy
**Sources:** web_search (Firecrawl backend) + web_extract for verification via doi.org / publisher URLs + arXiv / PMC. No subscription DBs; open-web search used as proxy for PubMed/arXiv/PMC coverage.

**Query concepts & dates (all run 2026-08-30, verbatim queries logged to `literature/search_log.csv`):**
- **Strategy A1 (DL-centric terminology):** `irregular longitudinal clinical time series Gaussian process neural ODE vs mixed models systematic review`; `informative visit process joint model irregular EHR sampling latent state`
- **Strategy A2 (biostatistical terminology):** `joint modelling longitudinal survival informative observation EHR review`; `linear mixed model vs LSTM neural ODE longitudinal EHR benchmark no benefit`
- **Synonyms / adjacent methods checked:** GRU-D (`Che et al 2018 GRU-D time series EHR irregular sampling DOI`), SeFT / set functions (`Horn et al 2020 set functions irregular time series NeurIPS DOI`), Gaussian processes ↔ latent-state ↔ point processes, MIMIC-IV tabular time series benchmarking (`benchmarking irregular time series methods MIMIC comprehensive comparison no novelty`)
- **Systematic reviews inspected:** Sun et al 2026 Health Data Science review (DOI 10.34133/hds.0456) — the only truly recent comprehensive DL-for-ISMTS review found; Li et al 2024 IJERPH joint longitudinal–survival systematic review (DOI 10.3390/ijerph23040492); no Cochrane/methods systematic review directly comparing neural-ODE/GP vs LMM on clinical trajectories was located.
- **Backward/forward chaining:** From Sun 2026: traced GRU-D (Che et al 2018), SeFT (Horn et al 2020); from joint-model review: traced Rizopoulos textbook lineage, Schneider et al 2025 simulation guidelines (PMC12070788), arXiv 2410.13113 (JMVL-Liang three-process joint model), arXiv 2602.15374 shared-random-effects unified framework.
- **Adversarial search (goal: FIND work defeating the gap):** `benchmarking irregular time series methods MIMIC comprehensive comparison no novelty`; `linear mixed model vs LSTM ... benchmark no benefit`. Explicitly tried to locate a published head-to-head showing classical methods already suffice.

**Hits inspected:** ~5 per query × 8+ queries ≈ 40 abstracts/toc entries; 7 full texts/abstracts extracted for verification.

### Key findings
- The field is **architecture-saturated, benchmark-poor**. Sun et al (2026) catalogues dozens of DL methods for ISMTS (Time-aware LSTM, GRU-D, neural ODEs, SDE/CRU, transformers, SeFT, ProFITi flows) but notes: (a) most assume benchmarks on MIMIC-III / PhysioNet with heavy preprocessing, (b) ODE-based models incur substantial numerical-integration overhead, (c) no section provides a systematic classical-vs-DL calibration on the *same* task with matched handling of informative observation.
- **Joint longitudinal–survival models** are the mature biostatistical competitor. The 2024 systematic review (Li et al) summarizes that joint modeling reduces bias from informative dropout and measurement error vs two-stage approaches, with active work on estimation algorithms. This is the “grown-up” baseline that many DL papers do not compare against (they compare to last-observation-carried-forward or vanilla RNN).
- **Informative visit process matters — conditionally.** The most informative recent empirical work is the arXiv 2410.13113 / forthcoming JMVL-Liang line: a three-stage joint model (visiting process + observation process + longitudinal outcome with shared Gaussian frailty) evaluated on simulated + real EHR. Finding: when the visiting process is *non-informative*, simpler aggregations (mean summary statistics) or mixed models perform comparably and joint modeling of visits adds no bias but no gain; when it *is* informative, JMVL-Liang has smallest bias even under misspecification. No neural ODE is compared in that study.
- **Simulation guidelines exist but are not closed.** Schneider et al (2025, PMC12070788) ran extensive simulations varying measurement frequency, noise, heterogeneity and compared joint models vs Cox. They produce actionable guidelines on when longitudinal information helps. This is the *type* of study the gap needs more of — but extended to modern ML irregular-series models.
- **MIMIC-IV benchmark exists but is shallow vs mixed models.** Naemi et al (arXiv 2401.15290) benchmarks latest tabular DL time-series models on MIMIC-IV raw format + literature survey of MIMIC-III. Useful for reproducibility; comparison to linear mixed models / joint models is minimal, and handling of irregularity is via imputation/resampling rather than principled modeling.

### Important papers (resolvable IDs only; 5–10 seed papers)

| # | Citation | DOI / URL | Type |
|---|----------|-----------|------|
| 1 | Sun et al. A Review of Deep Learning Methods for Irregularly Sampled Medical Time Series Data. *Health Data Science* 2026;6:0456. | https://doi.org/10.34133/hds.0456 **(VERIFIED via extract)** | review (load-bearing) |
| 2 | Che et al. Recurrent Neural Networks for Multivariate Time Series with Missing Values (GRU-D). *Sci Rep* 2018;8:6085. | https://doi.org/10.1038/s41598-018-24271-9 **(VERIFIED, 2168 cites)** | article |
| 3 | Horn et al. Set Functions for Time Series. *ICML PMLR 119* 2020. | https://proceedings.mlr.press/v119/horn20a/horn20a.pdf | conference |
| 4 | [Systematic Review] Li et al. Joint Modeling of Longitudinal and Survival Data … *IJERPH* 2024. | https://doi.org/10.3390/ijerph23040492 | review |
| 5 | Schneider et al. Joint models in big data: simulation-based guidelines for required data quality in longitudinal EHR. *PMC12070788* 2025. | https://pmc.ncbi.nlm.nih.gov/articles/PMC12070788 | article |
| 6 | Liang et al. Analyzing longitudinal EHR data with … three-process joint model. *arXiv:2410.13113* 2024. | https://doi.org/10.48550/arXiv.2410.13113 | preprint |
| 7 | Naemi et al. Benchmarking with MIMIC-IV, an irregular, sparse clinical time series dataset. *arXiv:2401.15290* 2024. | https://doi.org/10.48550/arXiv.2401.15290 | preprint (adversarial) |
| 8 | Chen et al. Joint Modeling of Longitudinal EHR Data with Shared Random Effects … *arXiv:2602.15374* 2026. | https://doi.org/10.48550/arXiv.2602.15374 | preprint (forward chain) |

> Verification note: #1 extract confirms DOI resolves, lists MIMIC-III, CINC-2012/2019, COVID-19 as evaluation datasets and public code at github.com/SCXsunchenxi/ISMTS-Review. #2 DOI extract confirms metadata and citation count. Others cross-checked via search snippet URLs.

### What appears established
- Irregular sampling + informative missingness/presence is a defining feature of EHR time series; masking indicators and time-interval features carry predictive signal (GRU-D seminal; replicated widely).
- Joint longitudinal–survival models are a principled, well-studied biostatistical solution for informative dropout/measurement error; software exists (JMbayes/JMbayes2, joineRML) — though scalability to national EHR scale remains active research.
- Informative visiting can be ignored when non-informative without bias, but must be modelled when informative (JMVL-Liang empirical finding).
- Neural ODEs / continuous-time models are theoretically appealing for irregular intervals but are computationally heavier than discrete alternatives (CRU/SDE attempts to mitigate); no consensus that they yield clinically meaningful gains on raw EHR.

### What remains uncertain
- **Head-to-head performance and calibration under matched conditions:** Does any GP / point-process / neural-ODE / SeFT model beat a well-specified LMM or joint model on the *same* EHR prediction task with identical handling of missingness, site, and time-origin, on metrics that include calibration and decision-curve utility (not just AUC)?
- **When does complexity pay?** Schneider-type simulation boundaries for “DL-for-irregularity vs classical” do not exist. For what combinations of visit informativeness, noise, sparsity, and effect size does the expensive model justify itself?
- **Transportability of irregularity assumptions:** Models tuned to dense ICU data (MIMIC) may not transfer to sparse outpatient trajectories; viscosity of missingness mechanisms across settings is poorly characterized.

### Potential gap
**Falsifiable, methods-forward question:** *On realistic plasmode-generated irregular EHR trajectories with known ground truth (varying visit informativeness, sparsity, noise), a pre-registered benchmark showing that one or more contemporary irregular-series models (e.g., GRU-D, SeFT, neural ODE or CRU) fails to outperform — on discrimination, calibration, and prediction-interval coverage — a well-specified linear mixed model / joint model baseline, after proper handling of the visit/observation processes.*

- **Gap type:** Benchmarking / methods evaluation; thin not empty.
- **Why it may be a gap:** No directly equivalent study was identified in searches performed so far that jointly (a) generates plausible EHR irregularity with tunable informative visiting, (b) compares a suite of modern DL irregular-series models against classical longitudinal baselines, and (c) evaluates calibration/coverage, not only AUC. The closest (Sun 2026) is a review without an experiment; Schneider 2025 varies data quality but only within the joint-model-vs-Cox world; Naemi 2024 benchmarks DL-vs-DL on MIMIC-IV.
- **Mandatory simple baselines:** Linear mixed model (random intercept/slope, correctly specified time trend), joint longitudinal–survival model (JMbayes2/joineRML), last-observation-carried-forward + logistic regression, mean-aggregation + Cox, standard multiple imputation (MICE) + pooled model. **“Beat the baseline or show it suffices” is an acceptable primary outcome.**
- **Data need:** **Simulation / plasmode suffices** for the core question (tunable ground truth); real-data replication on a public dataset (MIMIC-IV or MIMIC-III phenotyping) strengthens publishability but is not required to answer the methods claim. No private hospital data required for v1.

### Evidence AGAINST the gap (adversarial: closest prior work that defeats the gap)
- **Naemi et al arXiv 2401.15290** *is* a recent MIMIC-IV irregular-series benchmark with several state-of-the-art tabular DL time-series models and a literature survey of MIMIC-III benchmarking. It partially defeats the “no benchmark” narrative — but its baseline suite does not emphasize well-specified LMM/joint models, and it does not systematically vary informative visiting or report calibration/coverage. So it narrows but does not close the proposed simulation-based head-to-head gap.
- **Schneider et al 2025 (PMC12070788)** already provides simulation-based guidelines for when joint models beat Cox as a function of data quality (frequency, noise, heterogeneity). This defeats a weaker version of the gap (“nobody has simulated EHR quality vs model choice”). Our proposed gap must therefore be specific to the *DL-for-irregularity* class, not joint-vs-Cox.
- **Sun et al 2026 (§ Limitations / Future Directions)** explicitly calls out computational overhead of ODE/SDE methods and sketches hybrid architectures; a generous reader could argue the authors consider the classical comparison “obvious next work,” reducing novelty if their supplement or subsequent empirical companion paper already runs the experiment (companion code at github.com/SCXsunchenxi/ISMTS-Review should be inspected before claiming the gap).

### Relevant datasets (named: public / restricted / simulation; access route if restricted)
- **Public — sufficient for replication:** **MIMIC-III** & **MIMIC-IV** (PhysioNet, credentialed access via PhysioNet credentialing + CITI training; ~1-2 week turnaround; all Sun/Naemi benchmarks use these); **PhysioNet Computing in Cardiology Challenges 2012 & 2019** (open); **COVID-19 EHR public extract** per Sun et al. Used via existing benchmarking codebases (MIMIC Extract, Harutyunyan benchmark).
- **Public — for trajectory realism:** **UK Biobank primary-care-linked repeated measures** (restricted-access but well-documented application route) — optional, not needed for v1.
- **Simulation / plasmode — preferred for gap:** Plasmode constructed from **MIMIC-III/IV** resampling + synthetic visit/observation processes (see Schneider 2025 simulation design; arXiv 2410.13113 three-process generator). **Fully synthetic EHR simulation** with tunable sparsity/informativeness (no patient data). This is the primary data pathway; it needs no ethics approval and yields known ground truth for bias/coverage evaluation.
- **Software:** `R: JMbayes2, joineRML, nlme/lme4`; `Python: GRU-D (github.com/PeterChe1990/GRU-D), SeFT (mlr.press code), CRU/neural-ODE (torchdiffeq), synthEHRella trajectory generators`.

### Methodological implications
- If classical models suffice under realistic noise/sparsity, the field should redirect effort from architecture novelty to (a) better specification of the visit/observation model, (b) uncertainty quantification, and (c) transportability — a publishable negative result with decision-theoretic consequences.
- If DL irregular-series models win only in narrow regimes (dense, highly informative visiting, large N), the study produces a decision rule / phase diagram rather than a leaderboard — more useful to methodologists and to IRBs evaluating compute/privacy costs.
- Either outcome demands calibration and coverage reporting (Van Calster hierarchy; Riley BMJ 2025 interval framing) alongside discrimination, nudging the territory toward more honest inference.

### Clinical implications
- Clinically, the trajectory question matters for chronic-disease monitoring (e.g., cardiovascular health trajectories, CKD/glucose trajectories, blood pressure). If predictions from irregular outpatient labs are no better with expensive models, deployment should favor interpretable, EHR-deployable mixed models that clinicians can audit.
- Informative visiting is clinically meaningful: sicker patients visit more, and visit frequency predicts outcomes. A finding that modeling visits corrects bias only when informative would justify simpler workflows in stable cohorts (annual screening) vs richer models in high-acuity follow-up.

### India relevance
**Verdict: GEOGRAPHY-ONLY (for this gap as framed).**

The benchmark per se does not stress an India-specific assumption; it stresses a universal assumption (visit informativeness and sparsity matter). Indian EHR visiting processes *could* stress the assumption further (more paper-based fragmentation, lower measurement frequency, stronger informative missingness, cost-driven selective testing) — but the core simulation question can be answered without Indian data. A defensible India-relevant extension would be a *second* experiment varying measurement-frequency and informative-missingness regimes that mimic Indian outpatient settings vs US ICU density, testing transportability of the “mixed model suffices” conclusion. As written for v1 (simulation/plasmode), do not claim STRESSES-ASSUMPTION.

### Confidence
**Medium.** The review/simulation landscape is clearly surveyed and the DL-vs-classical benchmarking gap is plausibly thin but not saturated. Risk: Naemi 2024 or forthcoming Sun-supplement experiments may already run a version of this head-to-head; verification requires inspecting their code/results before promotion.

### Recommended next search
1. **Deep read + chaining:** Full-text screen of Sun et al 2026 supplement/code repository (github.com/SCXsunchenxi/ISMTS-Review) for any empirical companion comparison vs LMM; forward citations of GRU-D (Che 2018) and SeFT (Horn 2020) after 2024 to catch new benchmarks.
2. **Estimand-specific search:** `joint model longitudinal survival EHR "informative observation" plasmode simulation comparison neural ODE` — to exhaust simulation-based comparisons that use the exact “informative presence + observation” decomposition (vs “informative visit” synonym).
3. **Preprint sweep:** arXiv cs.LG / stat.ME / stat.AP (2024-2026) for `plasmode irregular EHR benchmark mixed model` — to catch recent preprints not yet in the review cycle.
