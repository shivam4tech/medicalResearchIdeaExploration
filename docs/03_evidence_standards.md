# 03 — Evidence Standards

*What must be true before we call something a gap, a candidate, or a survivor.*

## 1. Citations: the non-negotiable

Every paper used as evidence must be independently retrievable. Record in
`literature/evidence_registry.csv`: title, authors, year, venue, DOI and/or PMID,
stable URL, publication type, preprint status, relevance, and **verification state**
(`VERIFIED` / `UNVERIFIED` / `FABRICATED`).

- A citation that cannot be resolved is marked `UNVERIFIED` and cannot support a gate.
- A citation shown to be invented is logged as a fabrication incident (agent, date,
  model noted) and discarded. Repeat offenders lose assignments.
- Bot-supplied citations are independently spot-checked by the Lead before promotion
  (≥1 per packet; 100% of load-bearing citations).

## 2. Gap verification standard

A scarce result from one keyword search is not a gap. Before claiming one:

1. ≥2 meaningfully different search strategies (different databases **and** terminology).
2. Inspection of recent systematic reviews/meta-analyses where they exist.
3. Adjacent terminology and methodological synonyms checked.
4. Near-equivalent studies explicitly searched for.
5. Reference lists and citing papers of key works (backward + forward chaining).
6. An adversarial search whose explicit goal is *finding* the imagined prior work.

Exact queries logged in `literature/search_log.csv`. Language stays proportional:
*"No directly equivalent study was identified in the searches performed so far"*
— never "nobody has ever studied this".

## 3. Candidate promotion gate

All of the following before `ideas/` entry is marked EXPLORE-or-better:

1. Gap verification (§2) survived.
2. Written adversarial challenge exists (self-authored in early cycles;
   `adversarial-reviewer` packet once it is active) with explicit attempts to defeat
   on: prior work, adequacy of existing simple methods, data realism, confounding,
   missingness, sample size, clinical meaning.
3. Falsifiable question whose **negative answer is still publishable**.
4. Named data pathway: (A) public dataset w/ verified access, (B) restricted dataset
   w/ realistic application route, (C) precisely specified prospective requirement the
   physician can evaluate, or (D) simulation/plasmode needing no patient data.
5. Mandatory baselines named (simple, credible: regression, Cox, mixed models,
   established scores, standard imputation…). "Beat the baseline or show it suffices"
   is an acceptable primary outcome.
6. Ethics/privacy path identified before selection.
7. Clinical relevance affirmed in writing (ultimately by the physician collaborator;
   provisionally by Clinical Scout with explicit uncertainty).
8. Scope fits a small team; explicit ceiling stated.

## 4. Evidence packet format (what bots hand back)

```
### Question investigated
### Search strategy            (sources, query concepts, dates)
### Key findings
### Important papers           (resolvable IDs only)
### What appears established
### What remains uncertain
### Potential gap
### Evidence AGAINST the gap
### Relevant datasets
### Methodological implications
### Clinical implications
### India relevance            (only if genuine — which assumption does it stress?)
### Confidence                 (High / Medium / Low)
### Recommended next search
```

## 5. Adversarial verdicts

`KEEP` / `REVISE` / `KILL`, each with evidence. A KILL is a productive output and is
preserved in `rejected/` with cause of death and resurrection conditions.

## 6. India relevance test

Genuine only if the Indian setting **stresses an assumption** of the method/ evidence
base (transportability, calibration, baseline risk, practice patterns, measurement
frequency, informative missingness, multimorbidity structure…). "Repeat Western study
on Indian patients" without an assumption stressed is decoration. Verdict per idea:
`STRESSES-ASSUMPTION` / `GEOGRAPHY-ONLY` / `NONE-CLAIMED`.

## 7. Data access realism

"Use hospital data" is not a dataset. Shortlist requires §3.4 to be satisfied by name.
Restricted datasets need the actual application route stated (dataset, controller,
requirements, typical timeline).

## 8. Honesty about uncertainty

Scores are decision support. Confidence flags are mandatory. Where we lack evidence we
say `UNKNOWN`, not a guess. The programme's credibility rests on refusing to look more
certain than it is.
