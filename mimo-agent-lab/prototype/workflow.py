"""Minimal workflow scaffold for MiMo Agent Lab.

This prototype does not call a live model API yet. It defines the planned
multi-agent stages and the run record structure used by benchmark tasks.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from enum import Enum
from typing import Iterable


class Stage(str, Enum):
    CONTEXT_ANALYSIS = "context_analysis"
    REQUIREMENT_UNDERSTANDING = "requirement_understanding"
    PLANNING = "planning"
    PATCH_PROPOSAL = "patch_proposal"
    TEST_STRATEGY = "test_strategy"
    REVIEW = "review"
    REPORT = "report"


@dataclass
class BenchmarkTask:
    task_id: str
    family: str
    user_request: str
    files: list[str]
    logs: list[str]
    expected_outputs: list[str]


@dataclass
class RunRecord:
    task_id: str
    model_family: str
    prompt_version: str
    stages: list[str]
    estimated_input_tokens: int
    estimated_output_tokens: int
    notes: list[str]


def estimate_tokens(texts: Iterable[str]) -> int:
    """Rough CJK-friendly token estimate for planning purposes."""
    total_chars = sum(len(text) for text in texts)
    return max(1, total_chars // 2)


def plan_run(task: BenchmarkTask, model_family: str = "mimo-series") -> RunRecord:
    context_items = [task.user_request, *task.files, *task.logs]
    input_tokens = estimate_tokens(context_items)
    stages = [stage.value for stage in Stage]
    return RunRecord(
        task_id=task.task_id,
        model_family=model_family,
        prompt_version="v0.1-plan",
        stages=stages,
        estimated_input_tokens=input_tokens,
        estimated_output_tokens=12000,
        notes=[
            "Use Chinese requirement understanding as the primary interface.",
            "Keep code-grounded evidence in every analysis stage.",
            "Store final review and benchmark metadata for reproducibility.",
        ],
    )


def main() -> None:
    task = BenchmarkTask(
        task_id="bugfix-task-001",
        family="bug_localization",
        user_request="定位批量导入在中文文件名场景下错误显示成功的问题，并给出测试方案。",
        files=["src/importer.ts", "src/validators/file-name.ts", "tests/importer.test.ts"],
        logs=["Expected 3 imported files, got 1. UI state: success=true"],
        expected_outputs=["root cause", "patch plan", "test strategy", "Chinese PR summary"],
    )
    record = plan_run(task)
    print(asdict(record))


if __name__ == "__main__":
    main()
