# PDPBioGen — Benchmarks & Reproducibility Suite

This folder contains the smoke tests and benchmark drivers for PDPBioGen.
The test suite is split into:
- `bci/` — EEG/BCI smoke tests (small EDF/GDF files included).
- `omics/` — Genomics / transcriptomics / metabolomics smoke tests.
- `integration/` — Neural → biological mapping E2E smoke tests.
- `agents/` — Multi-agent determinism and replay tests.
- `reproducibility/` — Determinism and LLM-variance checks.

## Quick start (local)
1. Ensure you have Python 3.9+ and the test dependencies installed:
