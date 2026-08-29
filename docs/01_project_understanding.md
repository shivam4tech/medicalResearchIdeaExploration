# Project Understanding & Exploration Plan
**Stage 1 deliverable — Research Lead (solo phase)**
*Date: 2026-08-28 · Source of truth: `IDEA.md`*

---

## 1. What we are actually trying to accomplish

We are building a **methods-research programme**, not a product and not a single study.
The scientific object of study is *the inference process itself*: how reliably can
researchers extract knowledge from clinical data that is small, noisy, irregular,
heterogeneous, biased, missing-not-at-random, confounded, or drawn from populations
underrepresented in the literature.

The twin questions structuring everything:

1. **The data question** — "What does this kind of clinical data actually support concluding?"
2. **The methods question** — "Can we develop, adapt, or rigorously test a *better way of
   learning* from this kind of data?"

A project qualifies only if question 2 is genuinely in play. "We applied model X to
dataset Y and got AUC 0.83" is out of scope unless it tests a methodological claim.

The concrete near-term output (per IDEA.md): a literature map, a shortlist with
per-idea feasibility/novelty/failure analysis, a ranked set of **3–5 serious candidate
projects**, and a research journal documenting the search itself. The first chosen
project must be *small enough to finish, serious enough to publish* — including as a
rigorous negative result.

## 2. How this differs from ordinary "AI in healthcare" work

| Dimension | Typical "AI in healthcare" | This programme |
|---|---|---|
| Goal | Best predictive performance / a deployable tool | Better *inference* — validity, uncertainty, transportability |
| Success metric | AUC, leaderboard, app shipped | A defensible claim about a method, robust to hostile replication |
| Failure | Model doesn't beat baseline | Equally valuable: *showing* baseline was already adequate, or that a popular method fails on a new population |
| ML's role | The point | One tool among many; causal inference, simulation, mature biostatistics often more appropriate |
| Population | Whatever dataset is convenient | Deliberate attention to transportability (Western-developed methods → Indian clinical reality) where scientifically justified |
| Publication logic | Novelty of application | Novelty of the *question*; negative/null results publishable |

The differentiator is **epistemic, not technical**: we are willing to spend effort
disproving ourselves, and we treat "the gap doesn't exist" as a finding.

## 3. Research territories worth mapping (not yet committing)

Grouped by methodological theme, with the India-relevant edge where one plausibly exists:

**T1. Longitudinal & irregular clinical time series.** Irregular sampling, informative
visit processes, disease-trajectory modelling (latent-state models, Gaussian processes,
point processes, neural-ODE-style approaches vs. classical mixed models). Open question:
when do fancy models actually beat well-specified regression on realistic clinical noise?

**T2. Heterogeneity & hidden subgroups.** Treatment-effect heterogeneity (causal forests,
meta-learners), latent subtyping, clustering instability. Key skeptical angle: most
"discovered subtypes" don't replicate — studying *replication failure itself* is
publishable territory.

**T3. Missing data & informative observation.** MNAR sensitivity analysis, selection
bias, informative missingness in EHR. Deeply understudied in low-resource settings where
"who gets measured" is strongly selective.

**T4. Causal inference from observational clinical data.** Confounding, target-trial
emulation, negative controls, sensitivity to unmeasured confounding. India angle:
treatment pathways and prescribing patterns differ → natural stress tests for methods
calibrated on US/EU data.

**T5. Uncertainty quantification & aggregate-statistic failure.** Calibration,
prediction intervals, when averages mislead (Simpson's paradox, ecological fallacy),
distributional rather than point prediction.

**T6. Transportability & external validity across populations.** Do risk scores,
thresholds, and subgroups validated on Western cohorts degrade or shift on Indian
patients? This is both a clinical-equity question and a clean *methodological* question
(domain shift / dataset shift theory meets clinical epidemiology). Strong candidate
territory: abundant prior art on specific scores, but meta-methodological gaps.

**T7. Simulation & synthetic data as methodological instruments.** Plasmode simulation
to benchmark methods under known ground truth; privacy-preserving synthetic EHR
generation quality assessment. Low data-access barrier — attractive for a first project.

**T8. Reproducibility & robustness of published clinical-computational findings.**
Direct replication of an influential published method on an independent (possibly
public) dataset. Highest feasibility, guaranteed publishable contribution if rigorous.

*Note: T1–T8 are a map, not commitments. The multi-agent phase stress-tests each.*

## 4. Standards for judging a candidate (the "gate")

An idea must survive **all** of the following before it enters the ranked shortlist:

1. **Gap verification** — ≥2 independent search strategies (different databases,
   terminology, backward/forward citation chasing) fail to find the question already
   answered. A gap claimed after one keyword search is not a gap.
2. **Adversarial self-review** — a dedicated skeptic pass must explicitly attempt to
   kill the idea (existing adequate method, unfalsifiable framing, data impossible,
   novelty illusory). Survival, not enthusiasm, earns promotion.
3. **Data realism** — named, obtainable data source(s): public/semi-public cohorts,
   openly licensed EHR extracts, or a concrete ethical pathway. "We could get hospital
   data" without a named route fails.
4. **Falsifiable framing** — the question must admit a negative answer that is still
   informative and publishable.
5. **Independence of outcome** — is the paper still worth writing if the result is
   null/negative? If no, the framing is wrong, not the result.
6. **Scale honesty** — completable by 2 people + agents in a bounded period (target:
   months, not years). Explicit scope ceiling per idea.
7. **Clinical grounding** — the clinician confirms the question matters to actual
   practice or understanding, not just to methodology for its own sake.
8. **Ethics feasibility** — privacy, consent, and regulatory path identified *before*
   selection, not after.

## 5. Record-keeping protocol (process reproducibility)

The research *process* is itself an experiment and gets logged like one:

- `journal/JOURNAL.md` — append-only chronological log: date, action, query, result, decision.
- `literature/` — search logs (exact queries, databases, dates, hit counts) + notes per
  paper; searchable corpus folders.
- `ideas/` — one file per candidate idea, structured per IDEA.md §"What the Exploration
  Phase Should Produce" (significance, novelty, data, feasibility, ethics, difficulty,
  publication potential, failure modes).
- `rejected/` — nothing is deleted; rejected ideas are archived *with the reason for
  rejection*. Rejection reasons are data.
- `decisions/` — decision records (ADR-style): context, options, choice, rationale,
  reversibility.
- **Claim discipline:** every factual claim in the shortlist carries a citation or a
  logged search. Unsourced claims are marked `[UNVERIFIED]` and cannot survive the gate.

## 6. Major risks / failure modes

1. **Gap illusion** — believing a niche is empty because searches were narrow, then
   discovering a saturated field mid-project. *Mitigation: gap-verification standard #1,
   skeptic agent.*
2. **Data-access fantasy** — designing around clinical data we cannot ethically or
   practically obtain. *Mitigation: gate #3 names the source; T7/T8-style first projects
   need no private data at all.*
3. **Topic drift / scope creep** — "improve methods for clinical data" is unbounded;
   without hard scoping the programme never ships a first paper. *Mitigation: gate #6,
   explicit scope ceilings.*
4. **Tool worship** — drifting into "apply latest ML to whatever data." *Mitigation:
   the two-question test, clinician veto on clinical irrelevance.*
5. **Fabrication/hallucinated literature** — LLM agents inventing citations or
   overstating findings. (My other labs have hit agent-fabrication incidents twice.)
   *Mitigation: every citation must resolve to a real retrievable source; spot re-audits;
   no agent claim enters `ideas/` without verification.*
6. **Ethics as an afterthought.** *Mitigation: gate #8 before selection.*
7. **Negative-result self-deception** — calling a sloppy null result "rigorous."
   Null results need *more* statistical care (power, sensitivity), not less.
8. **Rate-limit/budget constraints** (≈40 req/min) throttling multi-agent breadth.
   *Mitigation: see next section — batched, staged parallelism, cheap retrieval first.*

## 7. Recommended structure for the multi-agent exploration phase

**Phase 0 (done):** this document + journal scaffold.

**Phase 1 — Map (breadth, cheap).** 2–3 literature-scout agents, each assigned 2–3
territories from §3, with strict output schema: per territory, the canonical reviews,
the live debates, the claimed open problems, the 5–10 seed papers (citations verified).
Sequential-ish dispatch in small batches to respect the rate limit; shared search-log
protocol so coverage is auditable and non-overlapping.

**Phase 2 — Generate (narrow).** From the map, I (as Lead) plus the clinician distill
~8–12 candidate questions into `ideas/` using the standard template. Deliberately fewer
than feels comfortable — generation is cheap, verification is expensive.

**Phase 3 — Attack (skeptic pass).** A dedicated adversarial reviewer agent attempts to
kill each candidate against the gate criteria in §4, with explicit instructions to
search for *defeating* prior work. Survivors and corpses both documented
(`rejected/` keeps the corpses).

**Phase 4 — Rank & pre-register intent.** Survivors scored on feasibility × novelty ×
clinical value × publication-of-null robustness → ranked shortlist of 3–5 → presented
to you and the clinician for the go/no-go. First project preferably from T6/T7/T8 class
(obtainable data, bounded scope, methods-forward).

**Operational rules for agents** (given the 40 req/min budget):
- Small dispatches (2–3 workers), compact briefs, checkpointed write-as-you-go outputs.
- Verification budget reserved: ~1 verification call per 3–4 search calls.
- No agent writes to the shortlist directly; only I promote an idea after gate checks.

---

## 8. Immediate next actions (awaiting your go-ahead)

1. Your sign-off (or corrections) on this charter and the gate criteria.
2. Brief intake session with the clinician to capture their clinical-priority areas
   (constrains which territories get scouted first).
3. Define specialist agent role specs (scout, methodologist, skeptic, archivist) —
   *roles defined on paper first; no agents spawned until you approve.*
4. Launch Phase 1 scouting.
