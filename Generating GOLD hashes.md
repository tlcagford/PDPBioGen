## Generating GOLD hashes
Some tests compare artifacts to committed golden hashes.
- Run the preprocessing pipeline once in a controlled environment (use the same Python versions, pinned libs).
- Hash generated artifact(s) with `sha256sum` and paste results into the test file where `GOLD_HASH = "TODO_GENERATE"` is placed.

## CI strategy
- Pull requests run smoke tests (sample files) only.
- Nightly workflow runs full benchmark suite (configured in `.github/workflows/benchmark.yml`).

## Notes
- For agent tests we include a deterministic mock LLM mode; see `benchmarks/agents/mock_llm.py`.
- For full dataset runs use the dataset manifest in `benchmarks/datasets.yaml`.
- Replace example dataset access URLs with your preferred mirrors if needed.
