# /apply - Evidence-Grounded Drafter-Reviewer Job Application Workflow

You are orchestrating a job-application workflow. The job posting is provided as `$ARGUMENTS` (URL or pasted text).

Follow the steps in order. The governing resume standard is:

`.claude/skills/job-application-assistant/08-resume-creation-standard.md`

If older instructions conflict with that standard, the governing standard wins.

## Operating rules

- Do not fabricate skills, metrics, credentials, achievements, ownership, or scope.
- Do not strengthen an ambiguous claim. Downgrade it until evidence supports it.
- Use employer terminology only when it accurately describes candidate evidence.
- Tailoring is evidence selection plus accurate reframing, not keyword insertion.
- Preserve the user's ability to reject substantive AI edits.
- Do not re-read files already in context unless an edit failed or source verification is required.
- Compile and visually inspect final PDFs before presentation.

---

## Step 0 - Parse the Vacancy

If `$ARGUMENTS` is a URL, fetch it. Otherwise use the pasted text directly.

Extract:
- company;
- role title;
- department/team if named;
- location/work arrangement;
- posting language;
- required qualifications;
- preferred qualifications;
- core responsibilities;
- domain knowledge;
- named tools/platforms;
- leadership/scope expectations;
- eligibility or knockout criteria; and
- behavioral/cultural signals.

Create a requirement map. Mark importance as REQUIRED, PREFERRED, or CONTEXTUAL.

---

## Step 1 - Evaluate Fit and Build the Evidence Map

Read:
- `.claude/skills/job-application-assistant/08-resume-creation-standard.md`
- `.claude/skills/job-application-assistant/04-job-evaluation.md`
- `.claude/skills/job-application-assistant/01-candidate-profile.md`

Use available source material to map each important vacancy requirement to candidate evidence.

Assign one evidence status:
- `VERIFIED_DIRECT`
- `VERIFIED_EQUIVALENT`
- `PARTIAL`
- `UNVERIFIED`
- `UNSUPPORTED_GAP`

For every REQUIRED requirement, show:
1. requirement;
2. evidence status;
3. supporting experience/source;
4. whether it should appear explicitly in the resume; and
5. any boundary that must not be overstated.

Then present:
1. skills match;
2. experience/domain match;
3. behavioral/culture match;
4. material gaps;
5. salary benchmark if configured; and
6. overall fit recommendation.

A fit score may summarize the analysis, but it must not replace the evidence map.

Ask the user whether to proceed. If no, stop.

---

## Step 2 - Establish the Foundational Resume State

Read:
- `.claude/skills/job-application-assistant/03-writing-style.md`
- `.claude/skills/job-application-assistant/05-cv-templates.md`
- `.claude/skills/job-application-assistant/06-cover-letter-templates.md`

Read the most relevant existing CV only as a structural and candidate-history reference. Do not assume every claim in an old CV is current or fully supported if it conflicts with the candidate profile or source evidence.

Before vacancy-specific wording changes, check the foundational resume against the governing standard:
- factual accuracy;
- standard section structure;
- ATS-safe single-column reading order;
- readable bullet length;
- relevance-weighted evidence;
- no obsolete references section unless required;
- no unsupported claims; and
- no compression solely to satisfy an arbitrary page count.

For the current experienced-candidate workflow, two pages are the normal target, not a hard technical gate.

---

## Step 3 - Select Evidence, Then Draft the Tailored Resume

Create `cv/main_<company>.tex`.

Do not start by rewriting every existing bullet. First select the strongest evidence for the highest-value vacancy requirements.

For each selected claim, retain its evidence status in working notes.

### Resume rules

- Always in English unless the user explicitly requests otherwise.
- Follow the governing standard and `05-cv-templates.md`.
- Keep the summary concise and role-specific.
- Put concrete evidence in experience bullets rather than relying on abstract summary claims.
- Use the employer's wording when accurate.
- Use metrics only when source-supported.
- State partial exposure narrowly.
- Do not claim unsupported gaps.
- Keep most bullets to one or two lines when rendered.
- Front-load results, scope, or differentiating facts.

### Vacancy coverage check

Before moving on, confirm that each high-value `VERIFIED_DIRECT` or `VERIFIED_EQUIVALENT` requirement is either:
- stated plainly in the resume; or
- intentionally omitted for a documented reason such as low relevance or space.

Do not use repeated keywords as a substitute for evidence.

---

## Step 4 - Draft the Cover Letter

Create `cover_letters/cover_<company>_<role>.tex`.

- Match the language of the posting unless the user requests otherwise.
- Follow `03-writing-style.md` and `06-cover-letter-templates.md`.
- Connect specific source-supported experience to the role.
- Keep claims consistent with the resume evidence map.
- If the role has a real gap, do not disguise it. Emphasize adjacent evidence only when the relationship is defensible.
- Verify external company-specific claims before including them.

---

## Step 5 - Independent Reviewer Critique

Use a reviewer agent with the job posting, evidence map, resume draft, and cover-letter draft supplied inline.

The reviewer must return two outputs.

### Part A - Grounded structured edits

For each proposed substantive edit:

```json
{
  "file": "cv/main_<company>.tex",
  "old_string": "exact current text",
  "new_string": "proposed replacement",
  "reason": "why this improves evidence, fit, readability, or accuracy",
  "requirement": "vacancy requirement addressed, if any",
  "evidence_status": "VERIFIED_DIRECT | VERIFIED_EQUIVALENT | PARTIAL | UNVERIFIED | UNSUPPORTED_GAP"
}
```

Do not propose wording that upgrades `PARTIAL`, `UNVERIFIED`, or `UNSUPPORTED_GAP` into a stronger claim.

### Part B - Narrative review

Address every category:
- missed supported requirements;
- unsupported or overstated claims;
- stronger evidence that should replace weaker evidence;
- company/department-specific angles;
- action-oriented reframing;
- tone/style issues;
- redundancy and low-signal content; and
- interview-defensibility risks.

The reviewer may recommend removing a claim if it cannot be defended.

---

## Step 6 - Revise With Evidence Boundaries Intact

Apply reviewer edits only when they remain consistent with source evidence.

For every reviewer recommendation:
- accept if grounded and useful;
- modify if directionally useful but too strong;
- reject if unsupported; or
- flag for user confirmation if evidence may exist but is not available.

No `UNVERIFIED` claim may survive into the final resume.

When cutting for space, use relevance-weighted cutting from `05-cv-templates.md`. Do not mechanically cut the oldest content first if older evidence is more relevant.

---

## Step 7 - Compile and Visually Inspect PDFs

Compile:

```bash
cd cv && lualatex -interaction=nonstopmode main_<company>.tex
cd ../cover_letters && xelatex -interaction=nonstopmode cover_<company>_<role>.tex
```

Inspect every rendered page.

### Resume checks

- page count is justified by relevant content;
- for this experienced-candidate workflow, two pages are normally preferred but not mandatory;
- no orphaned role/education titles;
- no isolated section headings;
- no clipping or overlap;
- no awkward whitespace caused by manual spacing;
- most bullets remain one or two lines;
- contact information is visible in the body layout;
- standard headings and dates are consistent; and
- PDF text is selectable/extractable.

### Cover letter checks

- approximately one page unless content or local convention justifies otherwise;
- signature block is visible;
- no clipping or overflow;
- typography is consistent.

Do not reduce readability merely to hit page count.

---

## Step 8 - Final Quality Gates

Run each gate from `08-resume-creation-standard.md`.

### Gate A - Factual integrity
- all material claims supported;
- no fabricated metrics/skills/ownership;
- dates, titles, employers, credentials, and contact details correct;
- no `UNVERIFIED` claim remains.

### Gate B - Vacancy alignment
- supported required qualifications stated plainly;
- genuine gaps are not disguised;
- strongest evidence is prominent;
- employer terminology used only when accurate.

### Gate C - Human readability
- strong first page;
- standard headings;
- concise bullets;
- outcomes front-loaded;
- no filler.

### Gate D - Parsing-risk reduction
- single-column reading order;
- no essential information in graphics, floating text boxes, or layout tables;
- standard dates/headings;
- text-based PDF.

### Gate E - Interview defensibility
- every high-salience metric and ownership claim has a clear proof point;
- claim boundaries are known;
- interview-defense sheet generated.

---

## Step 9 - Generate the Interview-Defense Sheet

Create a concise supporting artifact based on the final resume.

For each high-salience claim, include:
- exact final claim;
- evidence/source;
- likely interviewer follow-up;
- concise proof point or STAR example; and
- boundary not to overstate.

Prioritize:
- numbers;
- leadership/ownership claims;
- unusual achievements;
- technologies central to the posting;
- domain expertise; and
- claims the reviewer substantially strengthened.

---

## Step 10 - Present Final Output

Provide:
1. final fit verdict;
2. material gaps, if any;
3. 3-5 key tailoring decisions;
4. pass/fail results for the five quality gates;
5. files created;
6. interview-defense summary; and
7. any claims that still require user confirmation before submission.

The user has final authority over all substantive application content.
