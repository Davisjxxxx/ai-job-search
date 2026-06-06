# Job Scraper / Job Radar

**name:** job-scraper
**description:** Searches U.S./Minnesota and remote job sources for new roles matching Jason's target profile. Deduplicates across runs, screens for salary/location/fit, and produces a prioritized job radar. Triggers on: job scrape, find jobs, search jobs, new jobs, job search, scrape jobs, job radar, /scrape.
**allowed-tools:** Read, Write, Edit, Glob, Grep, WebFetch, WebSearch, Agent, AskUserQuestion

---

## Purpose

This skill is not a generic job-board scraper. It is Jason's job radar.

Primary objective: find roles that convert his financial-services, credit-risk, investigative, governance, analytics, AI-project, and automation background into stronger-paying roles with better career trajectory.

Target outcomes:
- Salary probability at or above $100k.
- Remote from Minnesota or Twin Cities hybrid.
- Strategy, analytics, governance, product, AI, automation, customer success, or business transformation direction.
- Avoid stale, fake, junior, relocation-required, or purely instructional postings.

---

## Invocation

The user can trigger this skill with:
- "Find new jobs"
- "Run job radar"
- "Scrape for jobs"
- "Any new positions?"
- "/scrape"

Optional arguments:
- Focus area, e.g. `/scrape AI strategy`, `/scrape risk analytics`, `/scrape CSM`.
- `broad` to run all query categories.
- `tight` to show only A-fit roles.
- `local` to prioritize Twin Cities hybrid.
- `remote` to prioritize U.S. remote roles that allow Minnesota.

---

## Execution Steps

### Step 0: Load State

1. Read `job_scraper/seen_jobs.json`. If missing, create:

```json
{"seen": {}}
```

2. Read `job_search_tracker.csv` if present. If not present, proceed and note that tracker deduplication was skipped.
3. Read `.claude/skills/job-scraper/search-queries.md` for search categories, filters, and red flags.
4. Read `.claude/skills/job-application-assistant/01-candidate-profile.md` and `04-job-evaluation.md` only if deeper profile grounding is needed.

### Step 1: Select Search Scope

Default run:
- Priority 1: Technology Strategy, Business Strategy, AI Strategy
- Priority 2: Risk, Governance, Controls, Analytics
- Priority 3: Product, Finance Analytics, Business Analytics
- Priority 4: AI CSM / Enterprise Success if role volume is low

Use the user's focus argument to narrow the search. Do not run every query blindly if the user asks for a targeted radar.

### Step 2: Search

Use WebSearch with the query sets in `search-queries.md`.

Rules:
- Prefer jobs posted/refreshed within 14 days.
- Prefer last 7 days when the source allows date filtering.
- Search LinkedIn, Indeed, Built In, company career pages, and direct `site:` queries.
- For company career pages, search the specific company plus role family rather than browsing large listings manually.
- Do not present roles that are obviously closed, expired, relocation-only, or outside constraints.

### Step 3: Fetch & Parse

For each promising result, use WebFetch when accessible and extract:
- Job title
- Company
- Location and remote/hybrid policy
- Salary range if listed
- Posting date or freshness signal
- URL
- Key requirements
- Preferred qualifications
- Application deadline if listed
- Red flags

If the page is inaccessible, use the search snippet only when the role appears high value. Mark `source limited`.

### Step 4: Deduplicate

Skip if:
- URL already appears in `seen_jobs.json`.
- Same company plus substantially same title already appears in `seen_jobs.json`.
- Same company plus role appears in `job_search_tracker.csv`.

Add all reviewed roles to `seen_jobs.json`, including skipped roles, using:

```json
{
  "seen": {
    "<url_or_company_title_key>": {
      "title": "...",
      "company": "...",
      "url": "...",
      "location": "...",
      "salary": "...",
      "first_seen": "YYYY-MM-DD",
      "fit": "A/B/C/Reject",
      "status": "new/skipped/evaluated/rejected",
      "reason": "one-line reason"
    }
  }
}
```

### Step 5: Quick Fit Screen

This is a fast screen, not the full `/apply` evaluation.

Score each role using:

| Dimension | Weight | Screen |
|----------|--------|--------|
| Experience bridge | 30% | Does Jason have credible adjacent or direct evidence? |
| Career direction | 25% | Does it move toward strategy, analytics, AI, governance, product, or higher-value advisory work? |
| Salary probability | 20% | Is $100k+ realistic? |
| Location/logistics | 15% | Remote from MN or Twin Cities hybrid? |
| Friction/risk | 10% | Credential trap, junior scope, relocation, heavy sales, vague posting? |

Fit labels:
- **A-fit:** Apply-now candidate.
- **B-fit:** Worth detailed evaluation if user is interested.
- **C-fit:** Monitor or use for market signal, but probably not worth tailoring.
- **Reject:** Do not present unless it explains a repeated market issue.

### Step 6: Present Results

Return concise, ranked results:

```markdown
## Job Radar - YYYY-MM-DD

Found X new roles: A-fit: X, B-fit: X, C-fit: X, rejected/skipped: X.

| # | Fit | Role | Company | Location | Salary | Why it fits | Concern | URL |
|---|-----|------|---------|----------|--------|-------------|---------|-----|
| 1 | A | ... | ... | ... | ... | ... | ... | ... |

### Top Apply-Now Targets
1. ...
2. ...
3. ...

### Market Signal
One short note about recurring requirements, title patterns, salary signals, or resume keywords.

### Recommended Next Step
Suggest the exact role number(s) to run through `/apply` or `/upskill`.
```

Do not produce a giant undifferentiated list. If there are more than 12 viable roles, show the top 12 and summarize the rest.

### Step 7: Update Tracker When User Chooses

If the user decides to apply, add a row to `job_search_tracker.csv`:

```csv
date,company,sector,role,role_type,channel,status,contact_person,fit_rating,notes,cv_file,cover_letter_file,source
```

Status values:
- radar_found
- evaluating
- applying
- applied
- interview
- rejected
- closed
- skipped

---

## Important Rules

1. Never fabricate job postings. Only present jobs found through actual WebSearch/WebFetch results.
2. Never hide uncertainty. If salary, freshness, or remote eligibility is unclear, say so.
3. Do not over-score jobs just because they contain AI keywords.
4. Reject roles below Jason's level unless they are clearly strategic bridge roles.
5. Avoid training/instructional roles unless Jason explicitly asks for them.
6. Do not claim credentials, board-level strategy, executive-committee work, or technical depth that is not in the profile.
7. Treat the search as a decision filter, not a volume game.
