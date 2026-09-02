---
name: skills-global-promote
description: Promote a repository-scoped Agent Skill into the personal Skill collection shared by Codex and Claude Code. Use when the user asks to promote, graduate, or make a project Skill available across projects. Do not publish the Skill or package it as a plugin.
---

# Skills Global Promote

Move one repository-scoped Skill into the user's personal Skill collection.
Keep one source of truth: do not copy the Skill or create a per-Skill symlink.

## Resolve the source and destination

1. Use a candidate path explicitly provided by the user. Otherwise, search
   applicable `.agents/skills/` directories from the current working directory
   through the repository root for the exact requested Skill name. Proceed
   only when this resolves to one candidate.
2. Require a detectable source repository root. The candidate and its parent
   `.agents/skills/` must be real directories rather than symlinks, every
   repository-relative path component from the root through the candidate must
   be non-symlinked, and the candidate's canonical path must be inside that
   repository. Require it to be a direct child of `.agents/skills/`, contain
   `SKILL.md`, and have a frontmatter `name` exactly matching its directory
   name. That matched value is `<skill-name>`. If candidate resolution fails or
   is ambiguous, ask the user which path to use.
3. Search the source repository worktree, without following symlinked
   directories or descending into nested repository worktrees or submodules,
   for every `.agents/skills/` child outside version-control metadata. Match
   both directory names and frontmatter `name` values. If a direct child's
   frontmatter cannot be read, report it and stop because a duplicate cannot be
   ruled out. If any other Skill matches `<skill-name>`, stop until every match
   has an explicit rename, removal, or other disposition that will leave no
   repository-scoped duplicate; choosing only which one to promote is not
   sufficient.
4. Inspect the personal Skill roots without changing them:
   - Codex: `~/.agents/skills`
   - Claude Code: `~/.claude/skills`
5. Require both roots to exist as directories and resolve symlinks to the same
   canonical directory. That canonical directory is the personal collection.
   If either condition fails, stop and ask how the user wants personal Skills
   managed. Do not silently choose one root, duplicate the Skill, or rewrite
   the installation layout.
6. Set the destination to `<personal-collection>/<skill-name>`. Stop before
   overwriting any existing file, directory, or symlink.

## Prepare the candidate

1. Read the applicable instructions and inspect any working trees containing
   the source or destination.
2. Inventory every entry in the candidate directory, then read `SKILL.md` and
   its directly referenced resources. Inspect unreferenced code, executables,
   generated files, credentials, and login state rather than moving them
   unnoticed. Confirm that the complete directory remains useful and safe
   outside its source repository. Determine its source, reuse permission, and
   required attribution, including any repository-level `LICENSE` or `NOTICE`.
   If a required notice lives outside the candidate, stop and ask how to
   preserve it before moving. Preserve repository-specific behavior only when
   its description, triggers, or preconditions clearly restrict it to the
   applicable repositories so that it cannot misfire elsewhere. Otherwise
   treat adaptation as a substantive change and ask before editing it. Never
   promote credentials, private keys, tokens, or login state.
3. Inspect every symlink inside the candidate. Proceed only when its target will
   remain valid and intentional after the move; otherwise treat correction as a
   substantive change and ask before editing it.
4. Use `skills-format-validate` to check the candidate. Do not promote it while
   validation is failing or unavailable.
5. Run tests documented by the candidate for bundled scripts. Do not invent
   unrelated tests or execute untrusted external code merely to complete the
   promotion.
6. Follow the rename authorization rule in `skills-format-validate` when fixing
   a naming failure. Ask before any other candidate change.

## Confirm and promote

1. Show the exact source and destination, the personal roots that will expose
   the Skill, and every working tree affected by the move.
2. Request confirmation immediately before moving the directory. Promotion
   removes the repository-scoped source and changes personal agent behavior.
3. After confirmation, re-resolve both personal roots and require their
   canonical target to be unchanged. Also recheck the source canonical path,
   reviewed contents and internal symlinks, repository-scoped duplicate scan,
   and destination absence, counting a dangling symlink as existing. If any
   reviewed state changed, return to preparation and request confirmation again.
4. Move the whole Skill directory with a no-clobber operation that refuses any
   existing destination. Do not merge with a destination or leave another copy
   with the same `name` in repository scope.
5. After confirming the move succeeded, remove the source `.agents/skills/`
   directory and its `.agents/` parent only when the move made them empty and
   neither path is a symlink. Use only non-recursive removal that fails when a
   directory is non-empty; if it fails, leave the directory intact.

## Verify

1. Run `skills-format-validate` against the destination and rerun documented
   script tests.
2. Verify that the source is absent, no direct child of any `.agents/skills/`
   directory in the source repository has the same directory name or
   frontmatter `name`, and both personal roots expose the same destination
   `SKILL.md`.
3. From each affected repository, run only checks required by applicable
   instructions and directly relevant to the Skill or move, then review the
   affected status and diffs. Do not run unrelated whole-project checks or
   assume a particular runtime, task runner, dotfiles manager, or layout.
4. Report promotion as complete only after every verification step passes. If
   verification fails, report that promotion is incomplete, the current source
   and destination state, and the remaining recovery or corrective action.
5. On success, report the promoted Skill, resolved destination, validation
   performed, and any harness restart or reload needed for discovery. Do not
   commit or push unless the user explicitly requests it.
