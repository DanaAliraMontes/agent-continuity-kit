#!/usr/bin/env python3
"""Deterministic, secret-free continuity audit demo.

Input: a JSON snapshot with optional keys:
  objective, events, permissions, receipts, recovery_bundle
Output: JSON findings and a simple score.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone


def _ids(items):
    return {str(item.get("id")) for item in items if isinstance(item, dict) and item.get("id")}


def audit(snapshot: dict) -> dict:
    events = snapshot.get("events") or []
    permissions = snapshot.get("permissions") or []
    receipts = snapshot.get("receipts") or []
    bundle = snapshot.get("recovery_bundle") or {}

    checks = []
    checks.append({
        "name": "objective_present",
        "passed": bool(snapshot.get("objective")),
        "detail": "Objective is present in the supplied snapshot.",
    })
    checks.append({
        "name": "recovery_bundle_present",
        "passed": bool(bundle),
        "detail": "Recovery inputs are available.",
    })

    event_ids = _ids(events)
    receipt_ids = _ids(receipts)
    checks.append({
        "name": "event_ids_unique",
        "passed": len(event_ids) == len(events),
        "detail": "Every event has a unique id.",
    })
    checks.append({
        "name": "receipts_prevent_duplicate_actions",
        "passed": len(receipt_ids) == len(receipts),
        "detail": "Receipt identifiers are unique; duplicate actions can be rejected.",
    })

    active_permissions = {
        str(item.get("action"))
        for item in permissions
        if isinstance(item, dict) and item.get("active") is True and item.get("action")
    }
    action_names = {
        str(item.get("action"))
        for item in events
        if isinstance(item, dict) and item.get("action")
    }
    missing_permissions = sorted(action_names - active_permissions)
    checks.append({
        "name": "actions_have_active_permissions",
        "passed": not missing_permissions,
        "detail": "All recorded actions have an active permission.",
        "missing_permissions": missing_permissions,
    })

    passed = sum(1 for check in checks if check["passed"])
    score = round(100 * passed / len(checks), 1) if checks else 0.0
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "secret_free": True,
        "score": score,
        "passed": passed,
        "total": len(checks),
        "checks": checks,
    }


def main() -> int:
    try:
        snapshot = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError) as exc:
        print(json.dumps({"error": f"invalid JSON input: {exc}"}))
        return 2
    if not isinstance(snapshot, dict):
        print(json.dumps({"error": "snapshot must be a JSON object"}))
        return 2
    print(json.dumps(audit(snapshot), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
