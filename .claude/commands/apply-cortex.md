# /apply-cortex — Job Radar application workflow with Cortex shadow telemetry

This command is a field-validation wrapper around the existing `/apply` workflow.

## Non-negotiable behavior

1. Read `.claude/commands/apply.md` first.
2. Execute that workflow exactly as written.
3. Cortex is **SHADOW ONLY**. Cortex telemetry must never change whether the workflow continues, stops, drafts, revises, or presents output.
4. Do not include job-posting text, resume/profile contents, company-confidential data, or generated application text in Cortex telemetry.
5. Telemetry is emitted only when `CORTEX_FIELD_VALIDATION=1`; otherwise the helper exits successfully without writing anything.

## Gate observations

### JOB_G2_FIT_EVALUATION

Immediately after Step 1 fit evaluation and before asking whether to proceed, emit:

```bash
python tools/cortex_shadow_event.py \
  --gate JOB_G2_FIT_EVALUATION \
  --action FIT_EVALUATE \
  --risk LOW \
  --authority AUTHORIZED \
  --evidence PASS \
  --decision EXECUTE \
  --baseline WOULD_EXECUTE \
  --reason EVIDENCE_SUFFICIENT \
  --reason AUTHORITY_VALID
```

If the posting could not be adequately parsed or the candidate profile evidence is insufficient to support a meaningful fit evaluation, change only:

```text
--evidence INDETERMINATE
--decision ESCALATE
--reason EVIDENCE_INDETERMINATE
```

Do not change the normal `/apply` behavior because of the shadow result.

### JOB_G3_CLAIM_VERIFICATION

During Step 6, after completing the existing factual-accuracy verification checklist, emit PASS only when every material CV/cover-letter claim is grounded in the candidate profile or other explicitly verified source used by the workflow.

PASS example:

```bash
python tools/cortex_shadow_event.py \
  --gate JOB_G3_CLAIM_VERIFICATION \
  --action VERIFY_CLAIMS \
  --risk HIGH \
  --authority AUTHORIZED \
  --evidence PASS \
  --decision EXECUTE \
  --baseline WOULD_EXECUTE \
  --reason EVIDENCE_SUFFICIENT \
  --reason AUTHORITY_VALID
```

If a material claim cannot be verified, emit:

```text
--evidence FAIL
--decision CONTAIN
--reason EVIDENCE_FAILED
```

Again, this remains observational; follow the existing `/apply` rules for correcting unsupported content.

### JOB_G4_DRAFT_GENERATION

After the final PDFs/output pass the existing workflow checks, emit:

```bash
python tools/cortex_shadow_event.py \
  --gate JOB_G4_DRAFT_GENERATION \
  --action DRAFT \
  --risk LOW \
  --authority AUTHORIZED \
  --evidence PASS \
  --decision EXECUTE \
  --baseline WOULD_EXECUTE \
  --reason AUTHORITY_VALID
```

## External-effect boundary

The current `/apply` workflow prepares materials; it does not authorize sending recruiter messages, submitting applications, withdrawing applications, or durable profile mutations.

If any future workflow proposes one of those actions, emit the applicable gate before the action:

- `JOB_G5_EXTERNAL_CONTACT`
- `JOB_G6_APPLICATION_SUBMISSION`
- `JOB_G7_WITHDRAW_OR_PROFILE_MUTATION`

Until a separate enforcement decision exists, shadow Cortex should represent those effects as at least:

```text
risk: HIGH
authority: REQUIRES_HUMAN
decision: ESCALATE
reason: EXTERNAL_EFFECT_REQUIRES_HUMAN
```

Shadow telemetry does not itself grant or deny the action.
