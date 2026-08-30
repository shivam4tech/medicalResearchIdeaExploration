# Cycle 1 — Shared Worker Brief (Landscape)
Source of truth: docs/01_project_understanding.md (T1-T8), docs/02_research_protocol.md (rate limits, cycles), docs/03_evidence_standards.md (gap bar, packet format, citation discipline).

## Rate & budget (binding, shared pool 40 req/min opencode-zen)
- Global target ≤24/min, hard ceiling 30, max 2 model-intensive bots concurrent (Lead + 2 scouts = 3rd idle). ~1 verification per 3-4 search calls. Backoff 60s→120s on 429.
- Bounded assignments only. Reuse evidence. No near-duplicate queries.

## Citation discipline (non-negotiable)
- EVERY paper = resolvable identifier (DOI or PMID or stable URL). No invention. Unresolvable = UNVERIFIED, cannot support a gap.
- Log ALL searches verbatim to literature/search_log.csv: date,cycle,agent,source,query,concept,hits,n_inspected,notes,verification_status
- Log important papers to literature/evidence_registry.csv: id,title,authors,year,venue,doi,pmid,url,type,peer_reviewed,cycle,agent,territory,relevance_notes,verification_status,resolvable
- Spot-check: every load-bearing citation must resolve (crossref/doi.org/pubmed/semantic scholar). If you cannot verify, mark UNVERIFIED and do NOT use it to claim a gap.
- Language: "No directly equivalent study was identified in searches performed so far" — never "nobody has ever studied this".

## Output contract (per territory → one packet)
Write to your assigned working/agent_notes/<you>/territory_*.md — checkpoint write-as-you-go (create file early, append).
Packet template (docs/03 §4):
```
### Question investigated
### Search strategy            (sources, query concepts, dates, exact queries)
### Key findings
### Important papers           (resolvable IDs only, 5-10 seed papers)
### What appears established
### What remains uncertain
### Potential gap
### Evidence AGAINST the gap   (adversarial: closest prior work that defeats the gap)
### Relevant datasets          (named: public/restricted/simulation; access route if restricted)
### Methodological implications
### Clinical implications
### India relevance            (STRESSES-ASSUMPTION / GEOGRAPHY-ONLY / NONE-CLAIMED — justify)
### Confidence                 (High / Medium / Low per territory)
### Recommended next search
```
## Git discipline
- NEVER commit/push or edit ideas/, rejected/, decisions/, journal/research_log.md, reports/ — Lead integrates.
- Only write to working/agent_notes/<you>/ and append to literature/search_log.csv + evidence_registry.csv (append-only, never overwrite headers).

## What counts as a gap (all 6 required before claiming)
1. ≥2 meaningfully different strategies (different databases AND terminology)
2. Recent systematic reviews/meta-analyses inspected where they exist
3. Adjacent/methodological synonyms checked
4. Near-equivalent studies explicitly searched for
5. Backward+forward chaining on key works
6. Adversarial search explicitly trying to FIND the imagined prior work

## India relevance test
Genuine only if Indian setting stresses an assumption (transportability, calibration, baseline risk, practice patterns, measurement frequency, informative missingness, multimorbidity). Else GEOGRAPHY-ONLY.

## Completion checklist per territory
- [ ] ≥6-10 papers with resolvable IDs, ≥1 verified via DOI/PMID resolution
- [ ] search_log.csv rows for every query (verbatim)
- [ ] evidence_registry.csv rows for important papers
- [ ] packet file exists in working/agent_notes/<you>/ with all 13 sections
- [ ] explicit Evidence AGAINST the gap + Closest prior work
