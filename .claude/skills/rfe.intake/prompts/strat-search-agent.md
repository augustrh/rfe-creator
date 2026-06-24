# STRAT Search Agent Instructions

You are patching the "Find the parent STRAT" section of an existing PM actions file. This agent runs when `--strat-only` is used — the full intake pipeline has already run; only the STRAT lookup was missed.

RFE ID: {KEY}
STRAT project: {STRAT_PROJECT}

## Step 1: Read inputs

Read `artifacts/rfe-tasks/{KEY}.md` to understand the RFE's capability area, customer segment, and core themes. Identify 2–3 search terms that best characterise what this RFE is asking for — these become your Jira queries.

## Step 2: Search Jira for matching STRATs

Use the Atlassian MCP Jira search tool. Run 2–3 searches with different terms from the RFE:

```
project = {STRAT_PROJECT} AND issuetype = STRAT AND text ~ "<term>"
```

**Issue type fallback:** `issuetype = STRAT` is not universal — some projects use different names (e.g. HPSTRAT uses `Outcome`). If your first search returns zero results, retry without the `issuetype` clause:

```
project = {STRAT_PROJECT} AND text ~ "<term>"
```

Collect all matching keys, titles, and statuses from the results. De-duplicate across searches. Assess relevance — not every text match will be meaningful; pick the items whose scope genuinely covers this RFE's capability area or customer segment.

## Step 3: Back up and prepare to patch

```bash
python3 scripts/intake_backup.py artifacts/{KEY}/{KEY}-pm-actions.md
```

Read `BACKUP_COUNT=N` from output. Get timestamp:

```bash
python3 scripts/state.py timestamp
```

## Step 4: Read and patch the existing pm-actions file

Read `artifacts/{KEY}/{KEY}-pm-actions.md` in full.

Locate the `## Find the parent STRAT` section. It begins at that heading and ends at the `---` separator that precedes `## Notes` (or at end-of-file if no Notes section exists). You will replace everything **between** the `## Find the parent STRAT` heading and that boundary — preserving the heading itself, the `---` separator that follows the section, and everything before and after.

Replace the section body with:

```
## Find the parent STRAT

STRATs set the high-level themes and initiatives your team is investing in. Before acting on this RFE, find the STRAT it belongs to — RFEs should roll up into a STRAT, and making that link early is important for prioritisation, roadmap coherence, and showing that this request is part of a larger requirement rather than a one-off ask.

**STRAT project searched:** {STRAT_PROJECT}

**Matches found:**

- **KEY** — Title (Status) — one sentence on why this RFE rolls up here

**Recommended:** <which key(s) to link first, and why — one sentence. If none found, write "None found — this may be new territory or ahead of strategy.">
```

Fill in the actual STRAT keys, titles, statuses, and rationale from your Jira search. Keep the list to the most relevant matches (max 4). If no STRATs matched any search, write "None found — check whether `{STRAT_PROJECT}` is the correct project key and consider searching manually for related themes" under Matches.

Also update the frontmatter fields:
- `run_count:` → `BACKUP_COUNT + 1`
- `last_updated:` → the timestamp from Step 3

Write the fully patched content to `artifacts/{KEY}/{KEY}-pm-actions.md`.

## Step 5: Write sentinel

```bash
python3 scripts/state.py init tmp/strat-search-done-{KEY}.txt status=done
```

Your work is complete when this file exists.
