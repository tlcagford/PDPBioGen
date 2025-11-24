#!/usr/bin/env python3
import subprocess, sys

suites = [
    "benchmarks/bci/bench_smoke.py",
    "benchmarks/omics/bench_smoke.py",
    "benchmarks/integration/bench_smoke.py",
    "benchmarks/agents/bench_smoke.py",
    "benchmarks/reproducibility/bench_smoke.py"
]

for s in suites:
    print("Running:", s)
    r = subprocess.run(["python3", s])
    if r.returncode != 0:
        print("Suite failed:", s)
        sys.exit(r.returncode)
print("All smoke suites passed.")
