# rfe.intake — Quick Start

Takes an RFE you received from field or a customer. Scores it, summarises it, gives you investigation actions, and drafts a feedback letter to send back. No rewriting — the submitter's words stay theirs.

## Before you run

- **Jira access:** Atlassian MCP configured in Claude Code, **or** `JIRA_SERVER` / `JIRA_USER` / `JIRA_TOKEN` set
- **Internet access:** first run clones the rubric scorer automatically — nothing else to install

## Run it

```
/rfe.intake ACM-1234
/rfe.intake ACM-1234 ACM-1235 ACM-1236
```

With STRAT lookup (searches your strategy backlog and names the best match):

```
/rfe.intake ACM-1234 --strat-project HPSTRAT
```

## What you get

Three files in `artifacts/ACM-1234/`:

| File | What it is |
|------|------------|
| `ACM-1234-summary.md` | Plain-English summary — what the submitter actually wants |
| `ACM-1234-pm-actions.md` | Rubric score, engagement signal, investigation actions, Tailwind skill suggestions |
| `ACM-1234-submitter-feedback.md` | Scored feedback letter — review before sending |

Re-runs back up previous files automatically.

## Not the right tool?

If **you** wrote the RFE and want it improved before submitting → use `/rfe.review` instead.

## More detail

See `README.md` in this directory.
