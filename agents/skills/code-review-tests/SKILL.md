---
name: code-review-tests
description: Review existing tests and the design of the implemented code they exercise. Use after implementation when asked to assess test intent, testability, or table-driven suitability, not for routine test implementation or a general code review.
---

# Code Review: Tests

Review implemented behavior and the existing tests that exercise it. First,
assess whether the tests verify the **what** required by the defined
specification without meaningful gaps or unnecessary cases or assertions.
Compare the specification with the cases and assertions, and identify where an
unclear specification prevents a judgment.

Review the requested tests from both the perspective of what they verify and
the design that makes them easy to express and understand. This is a review by
default; implement changes only when the user requests them.

## Establish context

- Respect the user's specified scope. If no target is named, use the relevant
  current changes or code context when unambiguous; otherwise ask for a target.
- Confirm that the behavior has been implemented and identify its relevant
  tests. If either is missing or incomplete, state the limitation and review
  only the available evidence; do not imply absent tests were reviewed.
- Read the available tests and implementation, plus relevant requirements or
  existing contracts. Run focused existing tests when that would resolve
  uncertainty. Distinguish observed behavior from intended behavior and flag
  assumptions when the intended contract is unclear.

## Review what the tests express

- Check that names, cases, and assertions describe meaningful observable
  behavior, including important boundaries, errors, and side effects when
  relevant. Look for important missing or misleading scenarios, weak
  assertions, and expected values derived from the implementation rather than
  an independent contract.
- Check whether fixtures and mocks reflect realistic assumptions and whether
  they hide the behavior under test. Prefer a small number of meaningful
  findings over additions justified only by coverage or symmetry.

## Review design and test structure

- Examine responsibilities in the tests and, where they affect testability,
  the code under test. Identify setup, side effects, dependencies, helpers, or
  mixed responsibilities that obscure the scenario or make cases difficult
  to construct. Suggest a separation or test seam only when it addresses an
  observed problem.
- Consider table-driven or parameterized tests when cases share the same
  behavior and setup and their differences read clearly as inputs and expected
  outcomes. Keep cases separate when their meaning, setup, or assertions differ
  enough that a table would hide intent. Do not recommend abstraction or
  production refactoring solely to remove repetition or force a table.

## Report

Address both perspectives, noting when no material issue is found. For each
finding, cite the relevant file and location, explain its impact, and suggest a
concrete improvement or small example; indicate priority when useful. Separate
demonstrated problems from possible risks or contract questions, and mention
any material limits to the review or test execution.
