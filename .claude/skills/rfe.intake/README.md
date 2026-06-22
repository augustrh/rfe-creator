# rfe.intake

Intake skill for RFEs received from field or customers. Produces three outputs per RFE — **without rewriting or revising content**.

## When to use this skill

| | `rfe.intake` | `rfe.review` |
|---|---|---|
| **Built for** | PM who **received** the RFE | PM who **wrote** the RFE |
| **Rewrites content?** | No — never touches the submitter's words | Yes — produces a submission-ready artifact |
| **Output** | Summary + PM action list + submitter feedback | Revised RFE ready to submit |

**Rule of thumb:** if someone else wrote it and sent it to you, use `rfe.intake`. If you wrote it yourself, use `rfe.review`.

---

## Prerequisites

### Jira access

The skill fetches RFE content from Jira. Configure one of the following:

**Option A: Atlassian MCP server (preferred)**

Configure the Atlassian MCP server in your Claude Code session. See your org's MCP setup docs or `mcp/README.md` in this repo. Once configured, no further setup is needed.

**Option B: REST API fallback**

Set the following environment variables:

```
JIRA_SERVER=https://your-site.atlassian.net
JIRA_USER=your-email@example.com
JIRA_TOKEN=your-api-token
```

To create an API token: https://id.atlassian.com/manage-profile/security/api-tokens

If neither is configured, the skill will fail at the fetch step. RFEs already present in `artifacts/rfe-tasks/` are used as-is and do not require Jira access.

### assess-rfe rubric

The skill scores each RFE using the `assess-rfe` rubric. This is bootstrapped automatically on first run via:

```
bash scripts/bootstrap-assess-rfe.sh
```

Requires internet access to clone `https://github.com/opendatahub-io/assess-rfe`. Set `RFE_SKIP_BOOTSTRAP=1` to skip if you don't need scoring.

---

## Usage

```
/rfe.intake <JIRA-KEY>
/rfe.intake <KEY1> <KEY2> <KEY3>
/rfe.intake <KEY> --strat-project <PROJECT-KEY>
```

Examples:

```
/rfe.intake ACM-1234
/rfe.intake RHAIRFE-1595 RHAIRFE-1601
/rfe.intake ACM-1234 --strat-project HPSTRAT
```

### `--strat-project`

Optional. Pass your team's strategy project key (e.g. `HPSTRAT`) to have the pm-actions agent search Jira for STRATs relevant to the RFE and name the best candidates directly in the output. Without this flag, the STRAT section gives generic guidance to check your strategy backlog manually.

---

## Outputs

All outputs are written to `artifacts/<JIRA-KEY>/`:

```
artifacts/
  ACM-1234/
    ACM-1234-summary.md            — plain-English summary of the request
    ACM-1234-pm-actions.md         — prioritised action list with Tailwind skill suggestions
    ACM-1234-submitter-feedback.md — ready to review and send to the submitter
    backups/                       — previous runs, timestamped
```

Re-runs overwrite current files. Previous versions are preserved in `backups/` with a timestamp suffix. A warning is shown if more than 5 backups accumulate for a single RFE.

### Summary

Plain-English distillation of what the submitter is asking for. Written for a PM who hasn't read the RFE — strips jargon, surfaces the real user need. Draws on both the RFE body and any comment thread.

### PM action list

Rubric score broken into concrete investigative tasks. Also includes:

- **Engagement signal** — volume, substance, and source diversity of the comment thread (None / Low / Medium / High)
- **Tailwind skill suggestions** — where relevant, maps gaps to skills that can help:

| Gap | Suggested skill |
|-----|----------------|
| Thin customer demand | `/tailwind:support-cases` |
| Weak business impact | `/tailwind:dataverse-query` |
| Unclear investment value | `/tailwind:productize` |
| Needs prioritisation | `/tailwind:rice-score` |

- **STRAT lookup** — if `--strat-project` was passed, names specific strategy issues the RFE should roll up into

Suggestions are framed as "might help — use your judgment."

### Submitter feedback

A scored, gap-targeted letter directed back at the person who filed the RFE. States the overall rubric score, asks open-ended questions for weak sections, and encourages the submitter to fill in what they know in their own words.

> **Review before sending** — the file is ready to use but warrants a human read first.
