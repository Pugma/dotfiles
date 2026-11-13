---
name: pr-local-discuss
description: Start a read-only, local discussion of a pull request or similar change proposal. Use when the user wants to review a GitHub or other hosting service PR together, explore possible findings, or discuss review comments privately before any external review. Keep the discussion in the current conversation and never publish to the hosting service during this session.
---

# Discuss a change review locally

Help the user think through a pull request or comparable change in the current
conversation. This is an initial, private review session: findings are proposals
for discussion, not a review to submit on the user's behalf.

## Session boundary

- Do not post, submit, publish, or otherwise send anything to GitHub or any
  other external service. This includes comments, draft or submitted reviews,
  reactions, issues, messages, approvals, and requests for changes. Do not
  invoke an API or command that creates or modifies remote state, even to save
  a draft. If asked to publish during this session, explain the boundary and
  suggest a separate session; do not seek approval to bypass it here.
- Keep local work read-only: do not edit files, change branches, fetch into the
  repository, commit, or run commands that can change local or remote state.
  Do not execute tests or code unless their effects are known to be read-only.
  Inspect existing local data or use read-only service APIs instead.
- Do not create a local review artifact unless the user explicitly requests one
  in a separate session. Draft wording may be shown in the conversation.

## Review and discuss

1. Identify the target from the user's PR link, repository and number, or
   unambiguous local context. If it cannot be identified, ask for the missing
   information. Use a connected service's read-only capabilities when
   available; otherwise use an appropriate read-only local or browser method.
2. Read the change description and diff, then inspect relevant surrounding
   code, tests, requirements, and existing discussion as available. Respect
   the user's requested scope. Do not assume a local checkout matches the PR;
   identify the revision reviewed and note any mismatch or inaccessible data.
3. Look for consequential bugs, regressions, missing boundary coverage, and
   mismatches with stated requirements. Trace claims to evidence and consider
   alternative explanations. Separate demonstrated problems from hypotheses,
   questions, and stylistic preferences; avoid manufacturing findings.
4. Discuss the most useful observations in the conversation. For each potential
   finding, identify the location, concrete trigger and impact, evidence, and
   uncertainty; propose a question or possible remedy when helpful. Invite the
   user's perspective on ambiguous tradeoffs and refine the assessment together.
   Mention meaningful review limitations and say so if no material issue is
   found. Only draft review-comment wording in the conversation if useful or
   requested; never submit it.
