# Task: Chinese PR Review For Multi-File Change

## ID

`pr-review-task-001`

## Family

`pr_review`

## User Request

请审查一个涉及前端表单、后端接口校验和数据库迁移的 PR。重点找出用户数据丢失、重复提交、权限校验和错误提示方面的风险。输出中文 review findings，并按严重程度排序。

## Context Package

A real benchmark task would include:

- Pull request diff.
- Relevant unchanged source files.
- API route definitions.
- Database schema migration.
- Existing tests and CI failure logs if any.

## Expected Agent Output

The model should produce:

1. Review findings before summary.
2. Tight file and line references.
3. Severity labels.
4. Test gap analysis.
5. A short final summary.

## Token Estimate

- Diff and related files: 40,000-120,000 tokens.
- CI logs and test context: 10,000-50,000 tokens.
- Review reasoning and final report: 20,000-80,000 tokens.

Estimated full run: 80,000-250,000 tokens.
