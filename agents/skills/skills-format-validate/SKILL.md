---
name: skills-format-validate
description: Validate the personal three-part Agent Skill directory naming convention after creation, updates, or renaming and before or after promotion. Check naming shape only; do not validate or judge SKILL.md contents.
---

# Skills Format Validate

## Naming convention

This personal convention supplements the official Agent Skills format. Every
Skill name checked by this Skill must consist of exactly three lowercase
alphanumeric segments separated by two hyphens:

```text
<domain>-<subject>-<action>
```

- `domain`: the broad area, such as `skills`.
- `subject`: the narrower concern within that area, such as `format`.
- `action`: the operation the Skill performs, such as `validate`.

Read names from broad to narrow, ending with the action. Do not omit a
component or add a fourth component.

The bundled script checks only the directory name's three-segment shape.
Whether the words are good choices for the domain, subject, and action is a
semantic review, not a reason for this mechanical check to fail. Mention it
only when name review is also in scope.

Run it only against Skill directories changed by the current task or explicitly
named in a standalone validation request:

```text
uv run <this-skill>/scripts/check_skill_name.py <skill-directory> [...]
```

The active Skill metadata identifies this Skill's `SKILL.md`; use that file's
parent directory as `<this-skill>`. Do not assume the current working directory.

For a standalone validation request, report failures without editing the
candidate. A rename changes the Skill identifier, so ask before applying one
unless the expected new name was already authorized.

Report the checked paths and final pass or fail status. Do not claim that a
passing name check establishes anything about `SKILL.md` contents or behavioral
quality.
