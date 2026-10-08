# Global Guidelines

## Language

- Respond to users in Japanese.
- Prefer English for non-user-facing work such as thinking.
- Write commit messages in English.

## Environment

- Use mise for runtimes & tools.
- Use uv for Python.
- After changing Agent Skills, run the `skills-format-validate` skill.

## Context

- One task per session; on switching the topic, suggest another session & a handoff note.
- Respond briefly, but explain your reasoning.
- Delegate read-heavy tasks to sub-agents, excluding minor tasks.
- Prefer lightweight models for sub-agents.
- Keep command output small, e.g. with quiet flags.
- Use Todos as the source of truth for progress. Keep Memory, handoff notes, and plans concise & durable.
- On repeated permission requests, propose a configuration change; on denial, stop and ask.

## Scope

- Check `git status`/`git diff` before exploring to decide which files to read.
- Make only requested or clearly necessary changes; follow existing patterns and preserve existing behavior.

## Code, Tests & Commits

- Code — How: make the implementation clear through naming and structure.
- Tests — What: express expected behavior and boundary conditions.
- Commits — What + Why: state what changed in the subject and explain why in the body when needed.
- Comments — Why not: when an apparently better approach is easy to spot, explain why it is unnecessary or unsuitable here.
- Avoid comments that merely repeat what the code does.

## Quality & Safety

- Prefer TDD when practical; add or update tests for behavior changes.
- When tests fail, check test assumptions, fixtures, and mocks before production code.
- After 3 similar failed attempts, summarize and ask.
- Make small, logically scoped Conventional Commits.
- Never push without explicit user approval.
