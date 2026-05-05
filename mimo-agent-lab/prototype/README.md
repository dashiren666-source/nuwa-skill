# Prototype Scaffold

This directory contains a minimal Python workflow scaffold for MiMo Agent Lab.

The current prototype does not call the MiMo API yet. It defines the planned benchmark task structure, multi-agent stages, and run record format. This is enough to show how the project will organize experiments once API credits are available.

## Run Locally

```bash
python workflow.py
```

Expected output is a dictionary-like run record with:

- task id
- model family
- prompt version
- planned workflow stages
- estimated input/output tokens
- reproducibility notes

## Next Steps

1. Add MiMo API client integration.
2. Load task definitions from `schemas/task.schema.json` compatible JSON files.
3. Store run records as JSONL.
4. Add evaluator scripts for review precision and test strategy quality.
