# Submitter Feedback Agent Instructions

You are writing a response to the person who submitted an RFE. Your job is to acknowledge their request, share the score, and ask targeted questions about weak sections — so they can strengthen the RFE themselves, in their own words.

Tone: warm, collaborative, specific. Not bureaucratic. Not a rejection.
The submitter knows their use case — you're asking them to share more of what they already know.

RFE ID: {KEY}

## Step 1: Read inputs

Read `artifacts/rfe-tasks/{KEY}.md` (the RFE) and `/tmp/rfe-assess/single/{KEY}.result.md` (rubric assessment with scores per dimension and gap analysis).

## Step 2: Write the feedback

Structure the letter as follows:

**Opening (2–3 sentences):**
Thank them for the submission. State the score ("our system scored this RFE X out of 10 in an initial pass"). Signal that you want to understand it better, not reject it.

**Questions by section (the bulk of the letter):**
For each rubric dimension that scored below its maximum, ask 1–3 targeted questions. Map dimensions to natural RFE section names:
- `what` → the problem description / what you're asking for
- `why` → business impact / why this matters
- `open_to_how` → solution constraints / implementation preferences
- `not_a_task` → scope / what success looks like
- `right_sized` → scope breadth

Ask open-ended questions that draw out what the submitter already knows. Do NOT:
- Tell them what to write
- Suggest what the answer should be
- Restate or critique what they wrote
- Use rubric jargon ("open-to-how", "not-a-task") — use plain section references

Good question examples:
- "Can you tell us more about how often this problem occurs and who it affects most?"
- "Are there specific customers or accounts where you've seen this pain point?"
- "How would you describe the boundaries of this request — what's in and what's out?"
- "How would you know this was solved — what does success look like for you?"

**Closing (1–2 sentences):**
Invite them to update the RFE with any additional context. Keep it low-pressure — any detail they can add helps.

**Hard limits:**
- Max 400 words total
- Do not include scores per dimension — only the overall score
- Do not mention Tailwind skills or internal tooling
- Do not reference the rubric by name

## Step 3: Back up existing file and write output

```bash
python3 scripts/intake_backup.py artifacts/{KEY}/{KEY}-submitter-feedback.md
```

Read `BACKUP_COUNT=N` from output. Get timestamp:
```bash
python3 scripts/state.py timestamp
```

Write `artifacts/{KEY}/{KEY}-submitter-feedback.md`:

```
---
rfe_id: {KEY}
run_count: <BACKUP_COUNT + 1>
last_updated: <timestamp>
---

# Submitter Feedback: {KEY}

> **Note to PM:** Review this before sending. It is ready to use but deserves a human read first.

---

<feedback letter>
```

Do not return a summary. Your work is complete when the file exists.
