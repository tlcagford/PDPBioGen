# 🧬 PDPBioGen
![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Tests](https://img.shields.io/badge/tests-100%25-blue)
![Python](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-purple)
![Docs](https://img.shields.io/badge/docs-MkDocs%20Material-orange)
![Docker](https://img.shields.io/badge/container-docker-blue)

### Parallel Distributed Processing for Multi-Scale Biological Integration & Brain-Guided Healing Simulation

**PDPBioGen** is an open-source research framework integrating:

- EEG / BCI signals  
- Neuro-Symmetry Mapper (NSM)  
- Gene-expression surrogate modeling  
- Constraint-based metabolic simulation (COBRA)  
- Healing-state flux prediction

---

# 🌐 Project Architecture
![Architecture Diagram](architecture.svg)

EEG / BCI Data
↓
Neuro-Symmetry Mapper (NSM)
↓
Neuro-Symmetry Vector (NSV)
↓
Gene-Delta Mapper
↓
Metabolic Model (SBML)
↓
Flux-Balance Healing Simulation
↓
Results / Reports / Visualization


---

# 🧠 Neuro-Symmetry Mapper (NSM)

Computes Neuro-Symmetry Vector (NSV) with:

- Hemispheric symmetry  
- Alpha-band coherence  
- Neural entropy  
- Spectral resonance bands: delta, theta, alpha, beta  

**Example output (`symmetry.json`):**

```json
{
  "symmetry": 0.93,
  "coherence": 0.61,
  "entropy": 4.82,
  "resonance": {
    "delta": 0.12,
    "theta": 0.19,
    "alpha": 0.33,
    "beta": 0.27
  }
}

🧬 Healing Simulation Engine

    Gene-delta mapping (deterministic)

    Constraint-based modeling (COBRApy)

    Flux-balance simulation & manifest generation

    JSON + plots output

📂 Repository Structure

dpbiogen/
    neuro/
        neuro_symmetry_mapper.py
    quantum/
        gene_mapper.py
        metabolism.py
benchmarks/
tests/
nextflow/
Dockerfile
environment.yml
README.md
docs/

🚀 Quick Start

Conda:

conda env create -f environment.yml
conda activate pdpbiogen
pip install -r requirements.txt

Docker:

docker build -t pdpbiogen:latest .
docker run -it pdpbiogen:latest python -c "import dpbiogen; print('OK')"

▶ Run a Healing Simulation

Python:

python dpbiogen/quantum/demo_full_body.py \
    --eeg benchmarks/bci/sample.edf \
    --sbml benchmarks/metabolomics/sample.xml \
    --out results/healing_demo

Nextflow:

nextflow run . -profile docker \
  -with-report results/run_report.html \
  -with-trace results/trace.txt \
  -with-timeline results/timeline.html

📊 Benchmarking Suite

    PhysioNet EEGMMIDB

    Toy SBML metabolic model

    Pytest suite & determinism tests

pytest -q

📁 Outputs

results/
    symmetry.json
    eeg_features.json
    gene_delta.json
    flux_results.json
    manifest.json

⚠️ Disclaimer

Research only. Not a medical device.
🤝 Contributing

    Fork

    Create feature branch

    Add & run tests

    Submit pull request

📖 Citation

cff-version: 1.2.0
message: "Please cite PDPBioGen if you use it."
authors:
  - family-names: Ford
    given-names: Tony
title: "PDPBioGen: Brain-Guided Multi-Scale Biological Simulation"
version: "2025.1"

🧩 API Examples

NSM:

from dpbiogen.neuro.neuro_symmetry_mapper import NeuroSymmetryMapper
nsm = NeuroSymmetryMapper()
brain_state = nsm.compute("sample.edf")
print(brain_state)

Full Pipeline:

from dpbiogen.neuro.neuro_symmetry_mapper import NeuroSymmetryMapper
from dpbiogen.quantum.gene_mapper import GeneMapper
from dpbiogen.quantum.metabolism import MetabolismEngine

nsm = NeuroSymmetryMapper()
gene = GeneMapper()
met = MetabolismEngine()

state = nsm.compute(eeg_path)
delta = gene.map(state)
flux = met.run(delta)


---

## 2️⃣ `architecture.svg`  

Already provided in the previous step. Drop into repo root for README reference.

---

## 3️⃣ MkDocs `docs/` Folder

- `index.md` – Home page  
- `installation.md` – Conda & Docker  
- `architecture.md` – Pipeline + SVG  
- `datasets.md` – EEG / SBML table  
- `api.md` – API reference (NSM + GeneMapper + MetabolismEngine)  
- `pipeline.md` – Python & Nextflow usage  

---

## 4️⃣ `mkdocs.yml`  

```yaml
site_name: PDPBioGen Documentation
theme:
  name: material
  features:
    - navigation.expand
    - navigation.sections
    - content.tabs.link
markdown_extensions:
  - admonition
  - codehilite
  - toc:
      permalink: true
nav:
  - Home: index.md
  - Installation: installation.md
  - Architecture: architecture.md
  - Datasets: datasets.md
  - Pipeline: pipeline.md
  - API Reference: api.md
![Architecture Diagram](architecture.svg)

