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

## Quality & Safety

- Prefer TDD when practical; add or update tests for behavior changes.
- When tests fail, check test assumptions, fixtures, and mocks before production code.
- After 3 similar failed attempts, summarize and ask.
- Make small, logically scoped Conventional Commits.
- Never push without explicit user approval.
