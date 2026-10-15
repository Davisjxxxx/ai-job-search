# CV Templates and Tailoring Guide

<!-- SETUP: Profile statements and candidate-specific content are personalized by running /setup -->

## Governing Standard

**Read `.claude/skills/job-application-assistant/08-resume-creation-standard.md` before creating or tailoring any CV.** It is the governing content and QA standard. If this file conflicts with it, the governing standard wins.

This file contains implementation guidance for the repository's LaTeX output.

## Output

**Output file:** `cv/main_<company>.tex`  
**Compile with:** `lualatex` on MiKTeX/TeX Live  
**Master candidate source:** candidate profile and verified source documents. Existing CV files are structural references, not independent factual authority.

```bash
cd cv && lualatex -interaction=nonstopmode main_<company>.tex
```

## Resume Architecture

The generated resume must preserve a simple single-column reading order and conventional section labels.

Recommended order for most experienced candidates:

1. Name and contact information
2. Professional Summary
3. Core Skills
4. Professional Experience
5. Education
6. Certifications
7. Selected Projects or Publications, only when relevant

Do not include a references section unless the employer or local convention specifically requests it.

## Contact Information

Include:
- name;
- city/state or equivalent location;
- phone;
- email;
- LinkedIn; and
- GitHub/portfolio when relevant.

Do not require a full street address. Do not place essential contact information only in a PDF header or footer.

## Page Length

Page count is a content decision, not an ATS rule.

For the current experienced-candidate workflow, **two pages are the normal target**, but not a hard technical requirement. A strong one-page resume is acceptable when it preserves all important evidence. Do not add filler to reach two pages, and do not delete relevant outcomes merely to force one page.

A third page normally indicates poor prioritization for a standard private-sector resume and should trigger relevance-weighted cutting unless the role or jurisdiction calls for a longer CV.

## Professional Summary

Keep the summary concise, normally about 2-4 lines.

It must:
- state the strongest role-relevant positioning;
- use employer terminology only when accurate;
- avoid generic personality claims;
- avoid repeating the skills list; and
- contain no unsupported scope or proficiency claims.

## Core Skills

Use plain-text skill categories. Emphasize terms that are both:
1. genuinely supported by evidence; and
2. relevant to the vacancy.

Do not use skill bars, rating dots, charts, or self-assigned percentages.

## Professional Experience

Prioritize evidence over duty descriptions.

Strong bullets normally show a result, scale, decision authority, risk controlled, process changed, quality improved, stakeholder impact, time/cost reduction, volume, or a complex problem solved.

### Bullet length

- One line is ideal when complete.
- Two lines are normal.
- Three or more lines should usually be split or cut.
- Front-load the result, scope, or differentiating fact.

### Relevance-weighted bullet count

Typical guidance:
- most recent/relevant role: 4-6 bullets;
- prior relevant role: 2-4 bullets;
- older/less relevant role: 0-2 bullets or compressed earlier-experience line.

Relevance overrides recency when an older achievement is the clearest proof of a critical requirement.

## Evidence-Grounded Tailoring

Before writing, use the process in `08-resume-creation-standard.md`:

1. parse vacancy requirements;
2. map requirements to candidate evidence;
3. assign evidence status;
4. select the strongest proof;
5. rewrite only after evidence selection; and
6. run the claim-grounding audit before finalization.

Allowed evidence statuses:
- `VERIFIED_DIRECT`
- `VERIFIED_EQUIVALENT`
- `PARTIAL`
- `UNVERIFIED`
- `UNSUPPORTED_GAP`

No `UNVERIFIED` claim may remain in the final resume.

Do not fabricate a metric, skill, credential, ownership level, or achievement to improve match quality.

## Relevance-Weighted Cutting

Cut by signal, not by static section order.

Score each candidate line on:
1. relevance to this posting;
2. uniqueness; and
3. narrative/evidence load.

Cut the lowest-value content first.

Practical cut order:
1. redundancy;
2. duty statements;
3. generic summary language;
4. low-relevance bullets;
5. low-relevance supporting content;
6. duplicated skills already proven in experience, unless useful for recruiter search; and
7. low-relevance older material.

Protect quantified outcomes, dates, employer names, and job titles.

## ATS and Parsing-Risk Rules

Use:
- single-column reading order;
- standard section headings;
- standard bullets;
- conventional date formats; and
- text-based PDF output.

Avoid:
- layout tables;
- floating text boxes or shapes;
- essential information in headers/footers;
- multi-column designs;
- graphics that carry essential information;
- creative section headings;
- white-text keywords; and
- keyword stuffing.

Bold, italics, underlining, standard bullets, and a normal skills section are acceptable.

## LaTeX Spacing Rules

Do not place `\vspace{...}` between `\item` entries in an `itemize` list. Let the list use uniform native spacing.

A small `\vspace` between top-level role blocks is acceptable when visually verified.

Do not solve overflow by shrinking body text below readable size or compressing margins below the governing standard's range.

## Compile-and-Inspect Loop (MANDATORY)

After drafting:

1. Compile with `lualatex -interaction=nonstopmode main_<company>.tex`.
2. Inspect every rendered page visually.
3. Verify no clipping, overlap, orphaned role titles, awkward page breaks, or dense paragraph bullets.
4. Confirm contact information, dates, and section order render correctly.
5. Confirm the final PDF contains selectable/extractable text.
6. Iterate until clean.

### Orphan protection

If a role title is stranded at the bottom of a page, use `needspace` rather than compressing the whole document:

```latex
\usepackage{needspace}
...
\needspace{5\baselineskip}
\cventry{...}
```

For a near-miss page break, modest `\enlargethispage{...}` use is acceptable only after verifying it does not create visual crowding.

## Final Resume Gates

Before release, all gates in `08-resume-creation-standard.md` must pass:
- factual integrity;
- vacancy alignment;
- human readability;
- parsing-risk reduction; and
- interview defensibility.

The resume is not final until a separate interview-defense sheet has been generated from the final claims.
