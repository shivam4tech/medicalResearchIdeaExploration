# Territory T7 — Simulation & Synthetic Data as Methodological Instruments
**Agent:** methods-scout | **Cycle:** 1 | **Date:** 2026-08-30

---

### Question investigated
Can simulation and synthetic EHR — especially **plasmode simulation** and modern generative models (GANs, VAEs, diffusion, LLM-prompted) — serve as *trustworthy methodological instruments* for benchmarking clinical-computational methods under known ground truth? Two linked landscape questions: (a) How should synthetic-EHR quality be measured (fidelity vs utility vs privacy trade-offs), and (b) when do current generators already suffice — or fail — as substitutes for real data in methods evaluation?

### Search strategy
**Sources:** web_search (Firecrawl) + web_extract verification via doi.org / PMC.

**Query concepts & dates (2026-08-30, verbatim in `literature/search_log.csv`):**
- **Strategy A1 (plasmode-centric):** `plasmode simulation synthetic EHR generation evaluation quality metrics`; `synthetic data validation framework fidelity utility privacy plasmode Synthea MIMIC`
- **Strategy A2 (generative-model-centric):** `synthetic electronic health records GAN diffusion model validation utility privacy`; `MIMIC IV Synthea plasmode benchmarking synthetic EHR 2024`; `Chen et al generating synthetic EHR review JAMIA 2025 DOI`
- **Synonyms / adjacent methods checked:** Synthea (rule-based), MedGAN/CorGAN, VAE, EHRDiff/PromptEHR, diffusion models, LLM-based synthetic generation; evaluation dimensions fidelity / utility (analytical + predictive) / privacy / compute; plasmode variants (Generate-Treatment vs Generate-Outcome).
- **Systematic reviews inspected:** **Chen et al JAMIA 2025** — *methodological scoping review + benchmarking* (48 studies, 5 categories, 7 methods + 2 baselines benchmarked) — is the definitive recent synthesis; it explicitly cites and critiques Yan et al 2022 (multifaceted benchmarking limited to GANs on closed data), Goncalves 2020, Hernandez 2022, Budu 2024 etc. The Chen paper *is* the review-to-beat. Earlier synthEHR-specific reviews (Mendelevitch 2021 fidelity, Hernandez 2022, Ghosheh 2022, Achterberg 2024, Budu 2024 evaluation) are summarized within Chen and noted as non-benchmarking.
- **Backward/forward chaining:** From Chen 2025 → Yan 2022 benchmarking limitation, Synthea (Walonoski 2018), MedGAN (Choi 2017), CorGAN, EHRDiff, Silva 2023 utility frameworks, synthEHRella toolkit (github.com/chenxran/synthEHRella). From plasmode → Franklin 2017 / Schuler / Liu 2025 causality-specific frameworks (arXiv 2504.11740 cautionary note). Examined Chen tables on methods vs evaluation metrics inventory.
- **Adversarial search (try to defeat the gap):** `synthetic EHR plasmode already high fidelity replication study no gap` — deliberately seeking papers showing synthetic data already achieves near-perfect fidelity/utility with no meaningful gap, or that plasmode evaluation is already solved and stable.

**Hits inspected:** ~30 hits; 2 full-text extractions for verification (Chen via doi.org → JAMIA HTML extraction; plasmode cautionary note); synthEHRella GitHub inspected via snippet.

### Key findings
- **Chen et al JAMIA 2025 (DOI 10.1093/jamia/ocaf082, 10.48550/arXiv.2411.04281) is load-bearing.** It does four things that together narrow many naive “synthetic EHR” gaps: (1) scopes 48 studies into five generation categories, (2) benchmarks seven methods (CorGAN, MedGAN, VAE, EHRDiff, PromptEHR, Synthea, Plasmode) + two baselines (Resample, Prevalence-based Random) on **open-source MIMIC-III/IV phenotype data**, (3) evaluates across **four dimensions** — fidelity (MMD, RMSPE, correlation metrics), analytical utility (logistic regression association recovery), predictive utility (ML classifier train-synthetic-test-real), privacy (membership & attribute inference), and compute, and (4) releases **SynthEHRella**, an extensible on-premises benchmarking toolkit (methods, data generation, fidelity/utility/privacy evaluation modules). DOI extraction confirmed the full Introduction/Methods contribution framing and the MIMIC-III→MIMIC-IV transportability experiment. **Cited 3+ times already; benchmarking is on open data, which prior Gan-only benchmarks lacked.**
- **Gap perception reverses depending on question:** For “*which generator is best overall*” the answer from Chen is already “none dominates; trade-offs are stark” (GANs lead on fidelity/utility on MIMIC-III but not on privacy; Synthea/Plasmode lead on privacy but lag on utility; performance shifts MIMIC-III→IV). That question is saturated. For “*can synthetic data serve as a valid instrument for methods benchmarking under known truth*” — the methods-instrument question — the gap remains thin but falsifiable (see Potential gap).
- **Plasmode is fragile if mis-specified.** Liu et al arXiv 2504.11740 (cautionary note for plasmode in causal inference) shows that the two plasmode frameworks (Generate-Treatment vs Generate-Outcome) have different theoretical guarantees; the outcome-generating variant can make standard propensity-score estimators *appear* overly biased with under-coverage even at large N, including on real EHR data and RCT data. This directly warns that “plasmode as instrument” is not plug-and-play — the instrument itself needs validation.
- **Evaluation language is stabilizing but incomplete.** The field has converged on fidelity / utility / privacy as the triad (often + compute), with concrete metrics: MMD, RMSPE, correlation recovery, TSTR (train-synthetic-test-real) AUC/ACC gaps, membership inference AUC, attribute inference accuracy. Yet Chen explicitly notes substantial fidelity gaps remain and “considerable performance gaps in fidelity, necessitating future research” — so synthetic data is not yet high-fidelity enough to replace real data without caveats.
- **Transportability of synthetic generators is tested and fails gracefully.** Chen’s MIMIC-III-trained → MIMIC-IV-tested experiment shows degradation / rank changes, which is itself a methodological contribution (generators don’t transport cleanly even between MIMIC versions).

### Important papers (resolvable IDs only)

| # | Citation | DOI / URL | Type |
|---|----------|-----------|------|
| 1 | Chen et al. Generating synthetic EHR data: methodological scoping review with benchmarking on phenotype data and open-source software. *JAMIA* 2025;32:1227-1240. | https://doi.org/10.1093/jamia/ocaf082 **(VERIFIED via doi.org extract)** | review + benchmark (load-bearing) |
| 2 | Liu et al. A cautionary note for plasmode simulation studies in the setting of causal inference. *arXiv:2504.11740* 2025. | https://doi.org/10.48550/arXiv.2504.11740 **(VERIFIED via search snippet)** | preprint |
| 3 | Walonoski et al. Synthea: An approach, method, and software mechanism for generating synthetic patients. *JAMIA* 2018;25:230-238. | https://doi.org/10.1093/jamia/ocx079 (PMID 29036597) | article |
| 4 | Choi et al. Generating Multi-label Discrete Patient Records using GAN (MedGAN). *arXiv:1703.03427 / AMIA* 2017. | https://doi.org/10.48550/arXiv.1703.03427 | conference |
| 5 | Yuan et al. EHRDiff: Exploring Realistic EHR Synthesis with Diffusion Models. *arXiv:2301.07014* 2023. | https://doi.org/10.48550/arXiv.2301.07014 | conference |
| 6 | Yan et al. Multifaceted benchmarking of synthetic EHR generation (GAN-only, closed-data limitation critique point). *Patterns* 2022. | https://doi.org/10.1016/j.patter.2022.100655 | article |
| 7 | SynthEHRella benchmarking toolkit (Chen lab) — code & docs. *GitHub* 2025. | https://github.com/chenxran/synthEHRella | software |

> Verification note: #1 extract via doi.org returned full JAMIA HTML (Introduction, four contributions, MIMIC-III/IV design, “synthEHRella” toolkit description). #2 snippet confirms the Generate-Treatment vs Generate-Outcome theoretical comparison and EHR/RCT empirical demonstrations.

### What appears established
- No single synthetic generator dominates across fidelity, utility, privacy, and compute; **trade-offs are consistent** across papers: GAN/CorGAN competitive on utility, rule-based (Synthea/Plasmode) best on privacy against attribute inference, diffusion/LLM methods emerging but not clearly superior in published open benchmark.
- Open benchmarking on MIMIC-III/IV with standardized metrics is now possible and has been done (Chen); closed-source benchmarks are no longer a defensible excuse.
- Privacy–utility tension is genuine: Plasmode’s dimension-by-dimension generation omits real associations → better privacy, worse utility (attacker accuracy 0.595 vs 0.622–higher for others in Chen’s attribute-inference test).
- TSTR predictive utility (train-synthetic-test-real) is the pragmatic litmus test; many methods show marginal TSTR gains on narrow tasks (e.g., MedGAN +0.0003 AUC on MIMIC-III, +0.004 ACC) — not transformative.

### What remains uncertain
- **When is synthetic/plasmode good *enough* to support a methods claim?** No precision-calibrated decision rule (e.g., “MMD < ε and TSTR gap < δ → method ranking preserves ordering vs real data”) was found. Whether method benchmarking on synthetic data preserves *rank ordering* vs real-data benchmarking — the core instrument-validity question — is unsettled.
- **Plasmode specification robustness:** Under what real-data resampling regimes does plasmode maintain nominal coverage for causal estimators, calibrated prediction intervals (T1/T5 questions), or longitudinal models (T1)? Liu shows one failure mode; generality is unclear.
- **Transportability of synthetic utility:** Why do rankings shift MIMIC-III→IV? Is it temporal shift, coding shift (ICD-9→ICD-10 / PhecodeX), or prevalence shift — and can a synthetic generator be made transportable?
- **Privacy measurement realism:** Current privacy metrics (membership / attribute inference with naïve attackers) may understate realistic linkage attacks; stronger threat models are discussed but not benchmarked comparably.

### Potential gap
**Falsifiable, methods-forward question (instrument-validity frame — preferred for this territory):** *Does benchmarking of clinical-computational methods on current synthetic/plasmode EHR preserve the rank ordering obtained on matched real data, and at what fidelity/privacy settings does the instrument break? Concretely: for a suite of prediction or causal methods (e.g., T1 mixed-model-vs-GRU-D suite, or T5 calibration methods), does TSTR / plasmode-derived ranking agree with real-data ranking (Kendall τ / rank-correlation), and can we characterize the fidelity threshold below which disagreement occurs?*

- **Gap type:** Methods-instrument evaluation / meta-benchmarking.
- **Why it may be a gap:** No directly equivalent study was identified in searches performed so far that (a) takes a defined methods comparison (not just data fidelity), (b) evaluates its conclusion on real vs synthetic/plasmode across multiple generators and the four quality dimensions, and (c) reports rank preservation and coverage. Chen comes closest but evaluates *data generators*, not *methods evaluated on those generators*. Liu 2025 evaluates plasmode correctness for causal estimators but not synthetic EHR generators broadly.
- **Alternative experimental form (same gap, single-generator deep dive):** Stress-test **SynthEHRella-plasmode** specifically: generate many plasmode replicates from MIMIC-III, benchmark one T1 or T5 method comparison on each, and measure variability / coverage of the methods conclusion as a function of plasmode resampling depth and transport to MIMIC-IV.
- **Mandatory simple baselines:** Resample (bootstrap real data) and Prevalence-based Random as null generators; logistic regression / Cox with standard handling alongside any DL comparator; plasmode-Generate-Treatment as the preferred causal-benchmark baseline per Liu. **“Beat the baseline or show it suffices” = “does synthetic ranking match real ranking?” — a negative result (synthetic fails to preserve ranking) is still a publishable instrument-validity result.**
- **Data need:** **Simulation / plasmode + public data suffices** (no private data). Core pathway: **MIMIC-III (training) → synthetic/plasmode via SynthEHRella → TSTR evaluation on MIMIC-III held-out + MIMIC-IV (transport)**. Optionally augment with **Synthea** as a non-MIMIC synthetic baseline. No ethics approval needed beyond PhysioNet credentialing (~1–2 weeks). A negative-result paper (“synthetic does not preserve ranking”) would still be valuable without ever collecting new clinical data.

### Evidence AGAINST the gap (adversarial: closest prior work that defeats the gap)
- **Chen et al JAMIA 2025 itself is the strongest defeating evidence.** It *already* delivers a comprehensive benchmarking framework (fidelity/utility/privacy/compute), open toolkit, and open data (MIMIC-III/IV). A referee will argue the field does not need another benchmarking paper; any new proposal must be clearly a *meta-benchmark of the instrument* (does synthetic preserve method ranking?), not a *benchmark of generators*. If the proposal is framed as “another generator comparison,” it is defeated.
- **Yan et al 2022 (multifaceted benchmarking)** and the Hernandez/Budu/Goncalves reviews could be cited as prior benchmarking attempts, narrowing claims about “no comprehensive benchmarking.” Chen’s critique (GAN-only, closed data) limits their force, but they do reduce perceived novelty if not distinguished cleanly.
- **Liu et al arXiv 2504.11740** already demonstrates plasmode fragility for causal inference (estimators appear biased under misspecified plasmode). This defeats a naive gap (“plasmode validity is unstudied”) — the refined gap must be broader than causal point-treatment effects (e.g., extending to longitudinal models / prediction calibration / TSTR ranking).
- **SynthEHRella documentation + Chen’s MIMIC-III→IV transport experiment** already shows that generator rankings shift across datasets, partially answering the transportability piece of the gap. The surviving question is whether *methods rankings* (not generator rankings) also shift — a subtle distinction that must be made crisp to survive review.

### Relevant datasets (named: public / restricted / simulation; access route if restricted)
- **Public — primary (verified open):**
  - **MIMIC-III** & **MIMIC-IV** phenotype data (PhysioNet, credentialed; the exact datasets Chen benchmarked). Chen’s preprocessing maps ICD-9/SNOMED-CT → PhecodeX; code in synthEHRella.
  - **Synthea** synthetic patients (fully synthetic, open download; rule-based baseline independent of MIMIC).
  - **SynthEHRella-generated synthetic datasets** (open-source, generated on-premises; no data-sharing barrier).
- **Simulation / plasmode — preferred instrument pathway:**
  - **Plasmode** per Chen / Franklin / Liu frameworks: resample from MIMIC-III real covariate/outcome structure then overlay known synthetic outcome/treatment mechanism. Both “Generate-Treatment” (Liu-recommended) and “Generate-Outcome” variants should be tested to demonstrate instrument sensitivity.
  - **Fully synthetic simulation** with known DAG and longitudinal structure (for causal/longitudinal extensions): preserves ground truth for bias/coverage assessment.
- **Restricted — optional for transportability extension:**
  - **eICU Collaborative Research Database** or **AmsterdamUMCdb** (PhysioNet credentialed) as a second real-data target for transportability of synthetic-utility claims (optional Stage-2).
- **Access routes:** PhysioNet credentialing = CITI training + signed DUA (typically days–2 weeks); Synthea/SynthEHRella = immediate open download; no hospital negotiation required — this is why T7 is a strong first-project candidate.

### Methodological implications
- A **positive result** (synthetic/plasmode preserves method ranking above a calibrated fidelity threshold) would license cheap, privacy-safe methods development and plasmode-based sample-size / power calculations — expanding the feasible space for small teams.
- A **negative result** (ranking not preserved, or only under unrealistic fidelity not achieved by current generators) would be equally important: it would set a *cautionary standard* for methods papers that rely solely on synthetic evaluation, and motivate fidelity-threshold guidelines before synthetic-supported claims are accepted by journals.
- In either case, the study produces a *decision rule* (MMD/utility thresholds, generator-choice guidance) rather than a leaderboard.

### Clinical implications
- Indirect but real: if validated, synthetic/plasmode benchmarking enables safer development of risk models and causal tools without repeated patient-data access, accelerating equity-relevant adaptations (e.g., testing a model’s behavior on synthetic cohorts enriched for underrepresented subgroups) before clinical validation.
- Caveat: clinical readers should not expect synthetic EHR to replace clinical validation — the claim is about *methods benchmarking*, not deployment readiness.

### India relevance
**Verdict: GEOGRAPHY-ONLY for v1; STRESSES-ASSUMPTION framing is plausible for a well-motivated extension but should not be claimed for the core instrument-validity question.**

- The core question (does synthetic preserve method ranking?) is population-agnostic; Indian data are not needed and claiming them would be decoration.
- **Meaningful India-relevant extension (Stage-2):** Indian routine EHR (where available) has higher fragmentation, more paper-mediated missingness, and different coding prevalence. Testing whether a synthetic generator trained on US MIMIC data preserves method ranking when evaluated against an Indian hospital distribution would genuinely stress the transportability assumption — but that is a deliberate follow-on requiring Indian partner data and should not be bundled into the v1 simulation/plasmode design.

### Confidence
**Medium.** Chen 2025 substantially narrows the “benchmark synthetic EHR” space, but the *instrument-validity* (ranking preservation) question is not directly answered by that work and remains falsifiable. Risk: a recent (late-2024/2025) preprint performing the exact meta-benchmark (real-vs-synthetic *methods* ranking) may have been missed by open-web search; targeted arXiv stat.ME/stat.AP + JAMIA forward-citation sweep is needed before promotion.

### Recommended next search
1. **Instrument-specific sweep:** `plasmode synthetic TSTR rank correlation methods comparison real data` on arXiv (stat.ME, stat.AP, cs.LG) + PubMed “plasmode” MeSH — to exhaust meta-benchmark studies that already compare real-vs-synthetic *conclusions*, not just fidelities.
2. **Chen forward chaining:** Inspect all 2025 citations of Chen et al (DOI 10.1093/jamia/ocaf082) and of synthEHRella GitHub for post-publication meta-evaluations using the toolkit.
3. **Privacy–utility trade-off deep dive:** Search `membership inference attribute inference synthetic EHR strong attacker 2024 2025` — to assess whether current privacy metrics understate risk and thus bias the instrument-validity conclusion.
