# Job Application Assistant

**name:** job-application-assistant
**description:** Assists with job applications: evaluating job postings, tailoring CVs, writing cover letters, and preparing for interviews. Triggers on keywords like: job posting, job application, CV, cover letter, resume, interview prep, job fit, career, application, apply, ansøgning, stilling
**allowed-tools:** Read, Glob, Grep, WebFetch, WebSearch, Edit, Write, AskUserQuestion

---

## Workflow

When the user provides a job posting (URL or text), follow this workflow:

### Step 1: Research and Evaluate Fit
- Fetch the job posting content.
- Decompose it into required, preferred, responsibility, domain, tool, scope, eligibility, and behavioral requirements.
- Read the candidate profile and relevant source evidence.
- Map each high-value requirement to candidate evidence using the statuses defined in `08-resume-creation-standard.md`.
- Score the posting using `04-job-evaluation.md`, but keep the evidence map visible so the score does not hide real gaps.
- Present the evaluation and recommendation.
- Ask the user if they want to proceed.

### Step 2: Build or Refresh the Foundational Resume
- Follow `08-resume-creation-standard.md` as the governing standard.
- Use the candidate source-of-truth inventory, not a prior resume alone.
- Validate factual accuracy, structure, evidence density, readable bullets, and parsing-risk controls before vacancy-specific tailoring.

### Step 3: Tailor the Resume
- Read `05-cv-templates.md` for repository-specific LaTeX implementation.
- Select evidence for the posting's highest-value requirements before rewriting.
- Use employer terminology only when it accurately describes the candidate's experience.
- Distinguish direct match, equivalent match, partial exposure, and unsupported gap.
- Do not fabricate missing qualifications, metrics, or ownership.

### Step 4: Write the Cover Letter
- Follow `03-writing-style.md` and `06-cover-letter-templates.md`.
- Connect specific evidence to the role.
- Keep claims consistent with the resume and evidence map.

### Step 5: Independent Review
- Review section by section.
- For substantive resume edits, provide a reason and evidence status.
- Treat AI suggestions as recommendations the candidate can accept, modify, regenerate, or reject.
- Reject any suggestion that would strengthen a claim beyond the evidence.

### Step 6: Final QA and Interview Defense
- Run the factual, alignment, readability, parsing-risk, and visual gates in `08-resume-creation-standard.md`.
- Generate an interview-defense sheet from the final resume claims.
- For major metrics, ownership claims, and differentiators, identify the source evidence and likely interviewer follow-up.

---

## Reference Files

| File | Purpose |
|------|---------|
| `01-candidate-profile.md` | Education, experience, skills, publications, awards |
| `02-behavioral-profile.md` | Behavioral assessment, strengths, ideal environments |
| `03-writing-style.md` | Tone, structure, do's and don'ts |
| `04-job-evaluation.md` | Scoring framework for job fit |
| `05-cv-templates.md` | LaTeX implementation and tailoring mechanics |
| `06-cover-letter-templates.md` | LaTeX cover letter structure and tailoring rules |
| `07-interview-prep.md` | STAR examples, tough questions, roleplay guidelines |
| `08-resume-creation-standard.md` | Governing evidence-grounded resume creation, tailoring, and QA standard |

---

## Quick Commands

The user may ask for individual steps without the full workflow:
- "Evaluate this job posting" - Step 1 only
- "Build my foundational resume" - Step 2 only
- "Write a CV for [company]" - Steps 2-3 as needed
- "Write a cover letter for [role] at [company]" - Step 4 only
- "Review this resume" - Step 5 plus relevant QA gates
- "Help me prepare for an interview at [company]" - Step 6 plus `07-interview-prep.md`
- "What jobs should I look for?" - Career strategy using profile + evaluation framework
