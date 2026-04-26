from __future__ import annotations

import argparse
from datetime import UTC, datetime
import json
from pathlib import Path
import sys


def parse_fields(body: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in body.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if key and value:
            fields[key] = value
    return fields


def append_log(log_path: Path, payload: dict[str, object]) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Enforce two-person approval and emergency override logging.")
    parser.add_argument("--event", required=True)
    parser.add_argument("--approval-count", required=True, type=int)
    parser.add_argument("--log", required=True)
    args = parser.parse_args()

    event = json.loads(Path(args.event).read_text(encoding="utf-8"))
    body = str(event.get("pull_request", {}).get("body", ""))
    fields = parse_fields(body)

    promotion_target = fields.get("Promotion-Target", "none")
    emergency_reason = fields.get("Emergency-Override-Reason", "")
    emergency_used = bool(emergency_reason)

    errors: list[str] = []
    if promotion_target == "production" and args.approval_count < 2:
        errors.append("production promotions require at least 2 approvals")
    if emergency_used and len(emergency_reason) < 20:
        errors.append("Emergency-Override-Reason must be at least 20 characters")

    payload = {
        "checked_at": datetime.now(tz=UTC).isoformat(),
        "pr_number": int(event.get("pull_request", {}).get("number", 0)),
        "promotion_target": promotion_target,
        "approval_count": args.approval_count,
        "emergency_used": emergency_used,
        "emergency_reason": emergency_reason,
        "result": "pass" if not errors else "fail",
        "errors": errors,
    }
    append_log(Path(args.log), payload)

    if errors:
        print("approval policy failed:")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print("approval policy passed")


if __name__ == "__main__":
    main()
