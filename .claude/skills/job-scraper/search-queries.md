# Search Queries for Jason's Job Radar

This file replaces the original Denmark-focused search plan with a U.S./Minnesota strategy aligned to Jason's target roles, salary floor, hybrid constraints, and innovation-oriented career direction.

## Search Sites

Primary sources:
- **LinkedIn Jobs**: highest priority for Twin Cities hybrid, remote-first, technology strategy, analytics, product, CSM, and AI-adjacent roles.
- **Indeed**: broad coverage, useful for financial services, business analyst, credit risk, governance, and operations roles.
- **Built In / Built In Minneapolis**: technology, SaaS, AI, product, customer success, analytics, startup roles.
- **Wellfound**: startup and AI-adjacent roles, especially remote-first companies.
- **Company career pages**: direct searches for high-fit targets and local employers.
- **Google Search with `site:` filters**: use when job boards are stale, gated, or noisy.

Secondary sources:
- **U.S. Bank careers**
- **Medtronic careers**
- **Deloitte careers**
- **Ramp careers**
- **Cresta careers**
- **Tesla careers**
- **Local Twin Cities employers with hybrid roles**

## Date Filter

Default to roles posted or refreshed within the last 14 days. Prefer last 7 days when volume is high. If posting date is missing, include only when the role is highly relevant and flag `date unknown`.

## Location Filter

Acceptable:
- Remote roles that explicitly allow Minnesota or U.S. remote work.
- Hybrid roles in the Twin Cities metro.
- Minneapolis, St. Paul, Bloomington, Eden Prairie, St. Louis Park, Minnetonka, Plymouth, Maple Grove, Brooklyn Park, Shoreview, Arden Hills, Blaine, Coon Rapids, Fridley, Roseville, Eagan, Woodbury, and similar metro locations.

Borderline:
- Roles requiring more than 3 days per week onsite.
- Roles with unclear remote eligibility.
- Roles outside the metro that appear unusually strong.

Reject unless user explicitly overrides:
- Relocation-required roles.
- Remote roles excluding Minnesota.
- Primarily training/instructional roles.
- Roles below Jason's level, especially entry-level analyst or junior implementation roles.
- Niche-certification traps where the certification is the real gate rather than adjacent learning.

## Salary Filter

Target salary: **$100k+**.

If salary is listed:
- Strong: $115k+
- Acceptable: $100k-$115k if role quality is high
- Borderline: $90k-$100k only if unusually strategic, remote-first, or strong pivot value
- Reject: below $90k unless user explicitly asks for bridge roles

If salary is not listed, infer cautiously from title, company, seniority, and market norms. Flag as `salary unknown` rather than guessing.

## Priority 1: Technology Strategy, Business Strategy, AI Strategy

Use for roles that convert Jason's governance, risk, lending, investigative, and AI project work into strategy-facing positions.

```text
site:linkedin.com/jobs "technology strategy consultant" Minnesota OR Minneapolis OR remote
site:linkedin.com/jobs "AI strategy" "business" "remote" "United States"
site:linkedin.com/jobs "strategy consultant" "technology" "Minneapolis"
site:linkedin.com/jobs "business technology consultant" "financial services" "Minneapolis"
site:linkedin.com/jobs "digital transformation consultant" "financial services" "remote"
site:linkedin.com/jobs "process improvement consultant" "AI" "remote"
site:usbank.com/careers "technology strategy consultant"
site:careers.deloitte.com "AI" "senior consultant" "finance" "Minneapolis"
```

## Priority 2: Risk, Governance, Controls, Analytics

These are high-transfer roles from Jason's financial services and governance background.

```text
site:linkedin.com/jobs "risk analytics consultant" "Minneapolis"
site:linkedin.com/jobs "business controls consultant" "Minneapolis" OR remote
site:linkedin.com/jobs "governance analyst" "financial services" "remote"
site:linkedin.com/jobs "model governance" "financial services" "remote"
site:linkedin.com/jobs "credit risk analytics" "Minnesota" OR remote
site:linkedin.com/jobs "operational risk consultant" "Minneapolis"
site:linkedin.com/jobs "conduct risk" "financial services" "remote"
site:linkedin.com/jobs "audit analytics" "financial services" "remote"
```

## Priority 3: Product, Finance Analytics, Business Analytics

Use for product owner, finance analytics, and business analyst roles where domain expertise and structured decision logic matter.

```text
site:linkedin.com/jobs "finance analytics product owner" "Minneapolis" OR remote
site:linkedin.com/jobs "product owner" "analytics" "financial services" "remote"
site:linkedin.com/jobs "business analyst" "AI" "Minneapolis"
site:linkedin.com/jobs "senior business analyst" "automation" "Minneapolis"
site:linkedin.com/jobs "analytics product owner" "healthcare" "Minneapolis"
site:jobs.medtronic.com "finance analytics" "product owner"
site:jobs.medtronic.com "analytics" "Minneapolis"
```

## Priority 4: AI Customer Success / Enterprise CSM / Implementation Strategy

Use when the role values enterprise communication, stakeholder management, regulated-domain judgment, and practical AI fluency.

```text
site:linkedin.com/jobs "enterprise customer success manager" "AI" remote
site:linkedin.com/jobs "customer success manager" "automation" "remote"
site:linkedin.com/jobs "AI implementation consultant" "remote"
site:linkedin.com/jobs "solutions consultant" "AI" "financial services" remote
site:ramp.com/careers "enterprise customer success"
site:cresta.com/careers "customer success" OR "solutions consultant"
```

## Priority 5: Local Hybrid Business Analyst / Credit / Banking Roles

Use for safer options, but score career alignment strictly. Do not over-prioritize roles that merely repeat old work without growth.

```text
site:linkedin.com/jobs "lead credit analyst" "St. Louis Park"
site:linkedin.com/jobs "senior credit analyst" "Minneapolis"
site:linkedin.com/jobs "business accountability" "Minneapolis"
site:linkedin.com/jobs "risk consultant" "Twin Cities"
site:linkedin.com/jobs "senior business analyst" "financial services" "Minneapolis"
```

## Red-Flag Keywords

Flag for review:
- heavy cold calling
- commission-only
- travel 50%+
- must relocate
- on-site five days
- trainer, instructor, curriculum, learning designer
- junior, entry level, associate analyst when clearly below Jason's level
- requires active clearance
- requires CPA, CFA, PMP, CRCM, CAMS, or other hard credential Jason does not have, unless listed as preferred only

## Fit Labels

Use these labels in job radar results:

- **A-fit**: Strong salary probability, realistic experience bridge, strategic or AI/analytics direction, location viable.
- **B-fit**: Good role but with one meaningful gap or weaker career acceleration.
- **C-fit**: Possible bridge, but compensation, scope, or alignment is questionable.
- **Reject**: Fails salary, location, level, or career direction constraints.

## Output Priorities

For each radar run, present only the strongest 8-12 roles unless the user asks for a broad dump. For each role include:

| Fit | Role | Company | Location | Salary | Why it fits | Concern | URL |
|-----|------|---------|----------|--------|-------------|---------|-----|

Then include:
- Top 3 apply-now targets.
- Roles to monitor but not apply yet.
- One upskill or resume-positioning note that appears repeatedly across the strongest postings.
