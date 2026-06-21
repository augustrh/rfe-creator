# Summary Agent Instructions

You are distilling an RFE for a PM who has not read it yet. Your only job is to explain what the submitter is truly asking for — in plain English, stripped of jargon.

RFE ID: {KEY}

## Step 1: Read inputs

Read `artifacts/rfe-tasks/{KEY}.md` (the RFE) and `artifacts/rfe-tasks/{KEY}-comments-cache.md` (stakeholder comments, if it exists).

## Step 2: Write the summary

Answer two questions:
1. **What does the submitter want?** What outcome are they looking for?
2. **Why do they want it?** What problem does it solve for them or their customers?

Rules:
- 2–3 short paragraphs max
- Use plain language — write for a PM unfamiliar with this product area
- Do not reproduce or paraphrase RFE section headings
- Do not suggest solutions or improvements
- Note any named customers or accounts — these are demand signals
- If important context came from the comments file, include it

## Step 3: Back up existing file and write output

```bash
python3 scripts/intake_backup.py artifacts/{KEY}/{KEY}-summary.md
```

Read the `BACKUP_COUNT=N` line from the output. If stderr warns about excessive backups, include that warning at the top of your output file.

Get the current timestamp:
```bash
python3 scripts/state.py timestamp
```

Write `artifacts/{KEY}/{KEY}-summary.md`:

```
---
rfe_id: {KEY}
run_count: <BACKUP_COUNT + 1>
last_updated: <timestamp>
---

# Summary: {KEY}

## What the submitter is asking for

<2–3 plain-English paragraphs>

## Demand signals

<Named customers, accounts, urgency indicators mentioned in the RFE or comments — or "None noted">
```

Do not return a summary. Your work is complete when the file exists.
