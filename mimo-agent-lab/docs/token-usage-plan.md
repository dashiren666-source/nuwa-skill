# Token Usage Plan

This plan explains why MiMo Agent Lab requires a high token quota during the Xiaomi MiMo Orbit creator program.

## Per-Task Token Estimate

A realistic coding-agent benchmark task includes more than a short prompt. A single run may include:

| Input Component | Estimated Tokens |
| --- | ---: |
| User requirement and acceptance criteria | 1,000-3,000 |
| Repository tree and file summaries | 5,000-20,000 |
| Source files relevant to the issue | 20,000-150,000 |
| Test logs, stack traces, and previous attempts | 5,000-50,000 |
| Agent planning and verification context | 10,000-100,000 |
| Final report, review, and benchmark metadata | 5,000-30,000 |

A full task run is expected to consume roughly 100,000-500,000 tokens when multi-round planning and verification are included.

## Monthly Experiment Estimate

Early-stage experiments will likely run:

- 100-300 benchmark tasks.
- 2-5 prompt variants per task.
- 2-4 model or parameter configurations per task.
- Additional reruns for failed tests, regression comparison, and report generation.

This produces an estimated monthly usage from tens of millions to hundreds of millions of tokens.

## Why a Small Quota Is Not Enough

A small quota is sufficient for single-turn chat or small snippets, but not for a serious coding-agent benchmark. The project needs to process multi-file context, preserve run records, compare model families, and repeat experiments under controlled prompt versions.

## Responsible Usage

The project will prioritize:

- Reproducible benchmark tasks rather than random chat usage.
- Structured run records for each experiment.
- Prompt and context compression when possible.
- Public summary reports so the community can learn from the MiMo experiments.
