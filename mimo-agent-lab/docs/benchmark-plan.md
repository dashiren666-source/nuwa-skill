# Benchmark Plan

This document defines the initial benchmark design for MiMo Agent Lab. The goal is to evaluate MiMo and other model families on realistic Chinese software engineering tasks rather than isolated toy prompts.

## Task Families

| Family | Goal | Input Size | Expected Output |
| --- | --- | --- | --- |
| Codebase reading | Understand architecture, modules, and data flow | 20-80 files | Chinese architecture summary, key modules, risks |
| Bug localization | Find likely root cause from logs and failing tests | 5-30 files + logs | Root cause analysis, patch plan, validation checklist |
| Patch planning | Produce an implementation plan before editing code | 10-60 files | Step-by-step plan, affected files, test strategy |
| Test generation | Add or improve unit/integration tests | 5-30 files | Test cases, edge cases, coverage rationale |
| PR review | Review a diff for correctness and regression risk | Diff + context files | Chinese review findings with severity and line references |
| Documentation | Generate docs from code and examples | Code + README | Developer-facing Chinese documentation |

## Initial Task Count

The first public milestone will target 100-300 tasks:

- 40% bug fixing and regression analysis.
- 20% test generation.
- 20% PR review.
- 10% codebase explanation.
- 10% documentation and migration tasks.

## Evaluation Dimensions

Each run will be evaluated along these dimensions:

1. Requirement understanding: whether the answer matches the original Chinese instruction.
2. Code-grounded reasoning: whether claims are backed by source files, logs, or tests.
3. Patch usefulness: whether the proposed changes are actionable and scoped.
4. Test quality: whether generated tests cover the failure mode or important edge cases.
5. Review precision: whether PR review findings are specific, non-generic, and line-grounded.
6. Reproducibility: whether the run can be repeated with the same input package.

## Run Record

Each task run should store:

- Task id and task family.
- Model family and model name.
- Prompt version.
- Input token estimate.
- Output token estimate.
- Number of reasoning/verification rounds.
- Final answer and structured evaluation notes.

## Why MiMo Is Relevant

MiMo Agent Lab is designed for long-context, multi-step software engineering workflows. MiMo's API can be evaluated in workflows involving repository analysis, Chinese requirement understanding, code review, and iterative planning. These are exactly the scenarios where large token quota is needed for meaningful experimentation.
