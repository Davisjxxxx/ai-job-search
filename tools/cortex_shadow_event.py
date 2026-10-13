#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import uuid
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Emit one Job Radar Cortex shadow event")
    parser.add_argument("--gate", required=True)
    parser.add_argument("--action", required=True)
    parser.add_argument("--risk", choices=("LOW", "MEDIUM", "HIGH", "CRITICAL"), required=True)
    parser.add_argument("--authority", choices=("AUTHORIZED", "REQUIRES_HUMAN", "DENIED", "INDETERMINATE"), required=True)
    parser.add_argument("--evidence", choices=("PASS", "FAIL", "INDETERMINATE"), required=True)
    parser.add_argument("--decision", choices=("EXECUTE", "ESCALATE", "CONTAIN", "DENY"), required=True)
    parser.add_argument("--baseline", choices=("WOULD_EXECUTE", "WOULD_ESCALATE", "WOULD_NOT_ACT", "UNKNOWN"), required=True)
    parser.add_argument("--reason", action="append", default=[])
    args = parser.parse_args()

    if os.getenv("CORTEX_FIELD_VALIDATION", "").strip().lower() not in {"1", "true", "yes", "on"}:
        return 0

    event = {
        "schema_version": "cortex.field-decision.v1",
        "event_id": f"cfv1-{uuid.uuid4()}",
        "timestamp_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "project_id": "job_radar",
        "lane": "JOB_APPLICATION_EVIDENCE_AND_AUTHORITY",
        "mode": "SHADOW",
        "actor": {},
        "requested_effect": {
            "action": args.action,
            "target_class": "job_application_workflow",
            "external_effect": args.gate in {"JOB_G5_EXTERNAL_CONTACT", "JOB_G6_APPLICATION_SUBMISSION", "JOB_G7_WITHDRAW_OR_PROFILE_MUTATION"},
            "reversible": args.gate not in {"JOB_G5_EXTERNAL_CONTACT", "JOB_G6_APPLICATION_SUBMISSION"},
            "effect_ref": args.gate,
        },
        "risk_class": args.risk,
        "authority_status": args.authority,
        "evidence_status": args.evidence,
        "freshness_status": "NOT_APPLICABLE",
        "independence_status": "NOT_APPLICABLE",
        "world_state_status": "NOT_APPLICABLE",
        "consent_status": "NOT_APPLICABLE",
        "evidence_refs": [],
        "cortex_decision": args.decision,
        "reason_codes": list(dict.fromkeys(["SHADOW_OBSERVATION_ONLY", *args.reason])),
        "baseline_behavior": args.baseline,
        "actual_behavior": None,
        "outcome_review": None,
        "latency_ms": None,
        "metadata": {"gate": args.gate},
    }

    target = Path(os.getenv("CORTEX_FIELD_LOG", ".cortex/field-events.jsonl"))
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, sort_keys=True, separators=(",", ":")) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
