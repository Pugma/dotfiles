#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Check the personal three-part Agent Skill directory naming convention."""

import re
import sys
from pathlib import Path


NAME_PATTERN = re.compile(r"^[a-z0-9]+-[a-z0-9]+-[a-z0-9]+$")


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: check_skill_name.py <skill-directory> [...]", file=sys.stderr)
        return 2

    failed = False
    for argument in sys.argv[1:]:
        skill = Path(argument).expanduser()

        if not skill.is_dir():
            print(f"FAIL: {skill}: directory not found")
            failed = True
        elif not NAME_PATTERN.fullmatch(skill.name):
            print(f"FAIL: {skill}: expected <domain>-<subject>-<action>")
            failed = True
        else:
            print(f"PASS: {skill}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
