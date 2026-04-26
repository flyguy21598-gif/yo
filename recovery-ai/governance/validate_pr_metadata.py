from __future__ import annotations

import argparse
from datetime import UTC, datetime
import json
from pathlib import Path
import re
import sys

FIELD_PATTERN = re.compile(r"^([A-Za-z][A-Za-z0-9\- ]+):\s*(.+)$")


def parse_pr_fields(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        match = FIELD_PATTERN.match(line)
        if not match:
            continue
        key = match.group(1).strip()
        value = match.group(2).strip()
        fields[key] = value
    return fields


def validate_fields(fields: dict[str, str], policy: dict[str, object]) -> list[str]:
    errors: list[str] = []
    required_fields = [str(item) for item in policy.get("required_fields", [])]
    for field in required_fields:
        if field not in fields or not fields[field]:
            errors.append(f"missing required field: {field}")

    allowed_change_types = [str(item) for item in policy.get("allowed_change_types", [])]
    change_type = fields.get("Change-Type", "")
    if change_type and change_type not in allowed_change_types:
        errors.append(f"invalid Change-Type: {change_type}")

    allowed_promotion_targets = [str(item) for item in policy.get("allowed_promotion_targets", [])]
    promotion_target = fields.get("Promotion-Target", "")
    if promotion_target and promotion_target not in allowed_promotion_targets:
        errors.append(f"invalid Promotion-Target: {promotion_target}")

    return errors


def append_log(log_path: Path, payload: dict[str, object]) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate PR metadata policy fields.")
    parser.add_argument("--event", required=True, help="Path to GitHub event JSON")
    parser.add_argument("--policy", required=True, help="Path to policy JSON")
    parser.add_argument("--log", required=True, help="Path to append JSONL policy check logs")
    args = parser.parse_args()

    event = json.loads(Path(args.event).read_text(encoding="utf-8"))
    policy = json.loads(Path(args.policy).read_text(encoding="utf-8"))

    body = str(event.get("pull_request", {}).get("body", ""))
    pr_number = int(event.get("pull_request", {}).get("number", 0))
    fields = parse_pr_fields(body)
    errors = validate_fields(fields, policy)

    payload = {
        "checked_at": datetime.now(tz=UTC).isoformat(),
        "pr_number": pr_number,
        "result": "pass" if not errors else "fail",
        "errors": errors,
        "fields": fields,
    }
    append_log(Path(args.log), payload)

    if errors:
        print("PR metadata policy failed:")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print("PR metadata policy passed")


if __name__ == "__main__":
    main()
