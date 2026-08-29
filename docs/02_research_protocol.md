# 02 — Research Protocol

*How this programme operates: cycles, roles, budgets, records. Companion to
`01_project_understanding.md` (strategy) and `03_evidence_standards.md` (proof bar).*

## 1. Governance

- **Research Lead** (`@medical-research-lead`, this profile): sole coordinator, sole Git
  authority, final arbiter of promotion/rejection of candidates.
- **Specialist bots** (3, persistent): produce evidence packets in their own working
  areas. They never commit, never push, never edit `ideas/`, `rejected/`,
  `decisions/`, `journal/research_log.md`, or `reports/` directly — the Lead integrates.

## 2. Exploration cycles

Work proceeds in numbered cycles. Each cycle: question → bounded bot assignments →
evidence packets → synthesis → candidate/rejection updates → journal entry →
commit + push.

Planned sequence (guide, not straitjacket):

| Cycle | Focus |
|---|---|
| 0 | Infrastructure (Git, hygiene, bot specs, schemas) |
| 1 | Landscape: map strongest methodological territories |
| 2 | Methodological failure points: where existing approaches demonstrably break |
| 3 | India/transportability opportunities (science, not geography) |
| 4 | Data-independent first projects (simulation, plasmode, replication, benchmarking) |
| 5 | Candidate deepening |
| 6 | Adversarial kill round |
| 7 | Convergence & shortlist dossiers |

Target: 4–8 substantive cycles. Stop when new searches mostly rediscover known
material, 6–12 candidates have been seriously assessed, and 3–5 clearly dominate.

## 3. Bot deployment pattern

- New evidence gathering: **Clinical Evidence Scout + Methods Scout**, complementary
  bounded assignments, at most 2 model-intensive bots concurrently.
- Adversarial Reviewer stays **dark** until ≥6 candidates exist or a specific candidate
  is promoted to REVIEW status — it never does broad unguided search.
- Cross-bot deliberation only at genuine conflict/convergence points, never for routine
  searching.

## 4. Rate-limit policy (binding)

Global shared pool ≈ 40 req/min (Kimi). This is one pool across Lead + all bots.

- **Normal target: ≤24 model requests/min globally. Internal ceiling: 30.**
- Max 2 model-intensive bots at once; third idle.
- Bounded assignments ("one clearly defined question") over open-ended loops.
- Reuse retrieved evidence; no near-duplicate searches; reserve ~1 verification call
  per 3–4 search calls.
- **429 policy:** stop launching, preserve state, back off 60s → 120s → longer; resume
  at reduced target (~18/min for the rest of that cycle); log the incident in the
  journal.

## 5. Records kept per cycle

- `journal/cycles/cycle_NN.md` — questions, assignments, findings, decisions, candidates
  created/weakened/killed, rate-limit incidents, commit hash, push status.
- `journal/research_log.md` — append-only chronological summary across cycles.
- `literature/search_log.csv` — date, agent, database, exact query, hits inspected,
  notes. Queries recorded verbatim; hit counts never invented.
- `literature/evidence_registry.csv` — one row per important paper: title, authors,
  year, venue, DOI/PMID/URL, type, peer-review status, relevance, verification state.
- `ideas/candidate_NNN.md` — full candidate template (`docs/03` §5).
- `rejected/rejected_NNN.md` — corpse with cause of death and resurrection conditions.
- `reports/candidate_matrix.csv` — scoring per the rubric in `01` §? (see below).

## 6. Scoring rubric (decision support, not fake precision)

| Dimension | Points |
|---|---|
| Methodological contribution | 20 |
| Evidence a real gap exists | 15 |
| Clinical significance | 15 |
| Data feasibility | 15 |
| Small-team feasibility | 10 |
| Value of a null/negative result | 10 |
| Reproducibility | 5 |
| Ethics/privacy feasibility | 5 |
| Scientifically meaningful India relevance | 5 |

Plus three confidence flags: evidence, novelty, data (High/Med/Low). The Adversarial
Reviewer can veto any score. Numbers never override judgment.

## 7. Commit discipline

Commit + push after every completed cycle. Convention:
`research(cycle-NN): <what changed>`. No force-push ever. Before every commit: inspect
diff for secrets/PHI. If push fails: diagnose, document, notify operator if it can't be
restored.

## 8. Physician intake (parallel, non-blocking)

Questions for the clinician collected in `docs/04_physician_intake_questions.md`;
exploration proceeds on public knowledge meanwhile.
