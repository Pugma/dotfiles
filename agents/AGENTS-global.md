# Codex Global Guidelines

## Language

- Respond to users in Japanese.
- Prefer English for non-user-facing work.

## Context Management

- Treat the main agent's context window and reasoning budget as scarce resources.
- Prefer using sub-agents whenever deep shared context is not required.
- Delegate investigation, search, code discovery, summarization, and analysis to sub-agents by default.
- Prefer lightweight models (e.g. Haiku) for delegated tasks unless higher capability is required.
- Use the main agent primarily for planning, synthesis, decision making, and integrating sub-agent results.
- Sub-agents should return concise summaries and conclusions rather than raw output.
- Keep Todos accurate and up to date. Use them as the primary source of truth for task progress instead of conversation history.
- Keep Memory concise. Store only durable project knowledge, never transient task details.
- Compress context proactively. Preserve decisions, remaining work, and essential rationale while discarding unnecessary detail.
- Minimize unnecessary command output and respect `.claudeignore`.
- If the same permission request occurs repeatedly, suggest an appropriate project-level or global configuration instead of repeatedly requesting approval.
- If permission is denied, do not repeatedly retry the same action.

## Preserve Existing Behavior

- Use git status or git diff to understand the current state before exploring files.
- Understand before modifying.
- Ask rather than assume when assumptions could affect implementation.
- Prefer existing patterns, conventions, and solutions over introducing new ones.
- Prefer preserving existing behavior unless a change is explicitly required.

## Environment

- Use mise for runtimes and tools.
- Use uv for Python package and script management.
- Respect existing project configuration.

## Agent Skills

- After creating, updating, renaming, or promoting an Agent Skill, run the `skills-format-validate` skill before considering the work complete.

## Quality & Safety

- Prefer test-driven development when practical.
- Add or update tests for behavior changes.
- When tests fail, verify test assumptions, fixtures, mocks, and setup before modifying production code.
- After ~3 similar failed attempts, summarize findings and ask before continuing.
- Never push to a remote repository without explicit user approval.
- Keep commits logically scoped.
- Prefer small, meaningful commits over large mixed changes.
- Follow Conventional Commits unless the repository uses a different convention.
- Write down commit message in English.

## Priority

- Project-level AGENTS.md overrides this file.
