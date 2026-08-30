# Cycle 5 — Promotion + Kill Round (deep dossier + adversarial)
Companion: docs/01..03, working/CYCLE_01..04_BRIEF.md, reports/landscape_cycle_01.md, reports/failure_points_cycle_02.md, reports/india_opportunities_cycle_03.md, reports/locked_protocols_cycle_04.md, journal/cycles/cycle_04.md.

Cycle 5 asks: PROMOTE 5–7 `ideas/candidate_NNN.md` dossiers from the 8 locked/executable designs (Cycles 2–4) and survive a pointed adversarial kill round — so only falsifiable, data-realistic, publishable-negatives reach shortlist.

## Binding constraints (same pool)
- Global pool muse-spark-1.2-contributor-free ~40/min, target ≤24, ceiling 30, max 2 concurrent model-intensive bots. Active chat shares pool — respect cap.
- Every claim = resolvable DOI/PMID/URL or [UNVERIFIED]. Append verbatim to literature/search_log.csv + evidence_registry.csv.
- Adversarial-reviewer ACTIVATES this cycle at ≥6 candidates (per bots/adversarial-reviewer.md 13 criteria). Previous DARK now WAKE — kill weak ideas with citations.
- Write dossiers to ideas/candidate_NNN.md and adversarial packets to working/agent_notes/adversarial-reviewer/cycle05_*.md — checkpoint early.

## Dossiers required (7 candidates → promotion gate docs/03 §3)
| # | Dossier | Source design | Class | Data path |
|---|---|---|---|---|
| 001 | Harutyunyan MIMIC→eICU TRIPOD+AI direct replication | T8 cycle03+04 | A public | MIMIC-III/IV + eICU + AmsterdamUMCdb (credentialed, weeks) |
| 002 | Fidelity→τ threshold via synthEHRella | T7 cycle02+04 | A/D | MIMIC-III/IV + synthEHRella (open) |
| 003 | 3-process joint plasmode DL-vs-classical | T1 cycle02+04 | D simulation | No PHI (first wave) |
| 004 | TRIPOD subgroup-calibration corpus audit n=150 | T5 cycle02+04 | D literature | No PHI (corpus) |
| 005 | Graded Indian shift plasmode G0→G3 (transport vs recalibration) | T6 cycle02+03 | D+B staged | Plasmode + UKB-SA proxy (CARRS/ICMR-INDIAB DUA pending) |
| 006 | Audit→RR anchored E-value + NC (audit WHOs → B/R*) | T4 cycle02+03 | D+B staged | Plasmode + WHO audits + UKB-SA proxy |
| 007 | Ahlqvist 5-cluster transport (centroids vs de novo, GADA-free stress) | T2 cycle03 | B restricted | CARRS/ICMR-INDIAB + UKB-SA proxy (empirical) |

Each dossier must satisfy promotion gate 1–8: gap verification (§2: 2 strategies+reviews+synonyms+chaining+adversarial), adversarial section exists, falsifiable Q with publishable negative, named data pathway A/B/C/D with timeline, mandatory baselines, ethics/privacy, clinical relevance, scope ceiling (small-team months). India verdict per dossier (STRESSES-ASSUMPTION vs GEOGRAPHY-ONLY).

## Assignments this cycle (3 agents, deep work)

### clinical-evidence-scout → dossiers 005, 006, 007 (India-stressing) + supporting evidence for corpus framing
- Tasks per dossier: 2+ distinct strategies (e.g., T6: Indian epidemiology + visit-process shift; T4: E-value + WHODAS/audit terminology; T2: Ahlqvist cluster + HTE transport terminology) + reviews (ICMR-INDIAB/CARRS, VanderWeele E-value, Ahlqvist/transfer transport) + synonyms + chaining + adversarial (try to close gap) — log exact queries verbatim to search_log. Re-chain T6 Indian shift numbers (MONO 43.3% 10.25259/IJMR_328_2025, audit injections 90.3% generic 4.7%→64.9%) and T4 B/R* titration values and T2 CARRS HTE archive.
- Deliver 3 dossiers to ideas/candidate_005.md, 006.md, 007.md with full 8-gate structure + Evidence AGAINST + India verdict + named DUA route + power/equivalence + scope ceiling.
- Must web_extract ≥1 CARRS/ICMR-INDIAB-adjacent page or TRIPOD corpus to keep extraction pilot live; 5-10 resolvable papers per dossier, ≥1 DOI 302 per dossier.

### methods-scout → dossiers 001, 002, 003, 004 (first-wave, no DUA)
- Tasks per dossier: 2+ strategies (T8: replication terminology + leakage/calibration terminology; T1: plasmode/joint-model + DL irregular-series; T7: synthetic fidelity + rank-preservation; T5: TRIPOD calibration + uncertainty/fairness) + reviews + synonyms + chaining + adversarial (find existing exact replication/plasmode/threshold/meta-audit that closes gap). Log queries verbatim.
- Deliver 4 dossiers to ideas/candidate_001.md, 002.md, 003.md, 004.md with full 8-gate structure + Evidence AGAINST + named data/compute + mandatory baselines + scope ceiling. Each dossier ≥5 resolvable papers, ≥1 DOI 302.

### adversarial-reviewer → kill round (WAKE, pointed)
- Trigger: ≥6 dossiers exist (this cycle creates 7). Review ALL dossiers 001–007 after they land (wait for both scouts to finish — Lead will sequence adversarial as follow-on if needed, but attempt parallel with checkpoint polling if dossiers appear early).
- Per dossier: 13-criteria checklist, 2+ pointed literature searches trying to kill (exact prior replication, near-equivalent with different MeSH like STROBE/PROBAST/RECORD vs TRIPOD, alternative leakage/benchmark terminology, LMIC-specific hits at full-text). Every kill attempt backed by resolvable citation or logged as failed-to-kill.
- Output: working/agent_notes/adversarial-reviewer/cycle05_kill_round.md with per-candidate verdict KEEP/REVISE/KILL + strongest FOR/AGAINST + closest prior work (DOI) + novelty/data/statistical/clinical/publication challenges + what evidence would flip verdict. A KILL is productive and preserved to rejected/ with cause of death.

## Output contract (dossiers)
Each ideas/candidate_NNN.md must contain (gate 1–8 explicit headings):
1. Gap verification (strategies, reviews inspected, synonyms, chaining, adversarial — queries cited)
2. Written adversarial challenge (self-adversarial per dossier; adversarial-reviewer later adds external challenge)
3. Falsifiable question (negative = publishable, stated)
4. Named data pathway (A/B/C/D with timeline/access)
5. Mandatory baselines (named, simple benchmark included)
6. Ethics/privacy (path identified)
7. Clinical relevance (affirmed provisionally by scout, physician TBD)
8. Scope ceiling (small-team months, explicit)
+ Evidence AGAINST, Relevant datasets, India relevance verdict, Confidence, Next search.

## Non-goals
No new data collection. No `rejected/` moves until adversarial verdicts land — Lead decides. Domain exclusivity deferred to shortlist.

## Completion checklist per dossier
- [ ] ≥5 resolvable papers, ≥1 verified 302, all logged to evidence_registry.csv
- [ ] ≥6 search_log rows per dossier (2 strategies + reviews + synonyms + chasing + adversarial) verbatim
- [ ] 8-gate headings explicit + Evidence AGAINST + India verdict + scope ceiling
- [ ] Falsifiable Q + publishable negative + named data pathway + baselines
- [ ] Adversarial-reviewer packet covers all 7 with KEEP/REVISE/KILL + citations

