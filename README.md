# 🧬 PDPBioGen  
### Parallel Distributed Processing for Multi-Scale Biological Integration & Brain-Guided Healing Simulation

**PDPBioGen** is an open-source research framework integrating:

- **EEG / BCI signals**  
- **Neuro-Symmetry Mapper (NSM)**  
- **Gene-expression surrogate modeling**  
- **Constraint-based metabolic simulation (COBRA)**  
- **Healing-state flux prediction**  

The system is designed for computational exploration of brain-guided biological modulation — **not** clinical use — and aims to provide a **deterministic, fully reproducible scientific workflow** with sample data, tests, and containerized execution.

---

# 🌐 Project Architecture

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

The NSM computes a **Neuro-Symmetry Vector** using:

- 🔹 Hemispheric Symmetry  
- 🔹 Alpha-band Coherence  
- 🔹 Neural Entropy  
- 🔹 Spectral Resonance Bands  
  - delta, theta, alpha, beta  

This NSV becomes the brain-side driver for downstream biological simulation.

Example output (`symmetry.json`):

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

The healing engine maps NSM → gene-delta → metabolic model → flux shifts.

Includes:

    Deterministic gene-delta mapping

    Constraint-based modeling via COBRApy

    Automatic result manifests

    Flux balance plots + JSON output

This forms a complete end-to-end healing simulation using real EEG and real SBML models.
📂 Repository Structure

dpbiogen/
    neuro/
        neuro_symmetry_mapper.py    ← restored NSM module
    quantum/
        ... healing engines, gene mapping, metabolism
benchmarks/
    bci/                             ← sample EEG (EEGMMIDB)
    metabolomics/                    ← toy SBML model
tests/
    test_neuro_symmetry.py
    test_healing_sim.py
nextflow/
    main.nf                          ← full pipeline
Dockerfile
environment.yml
README.md

🚀 Quick Start
Option 1 — Conda (Dev Mode)

conda env create -f environment.yml
conda activate pdpbiogen
pip install -r requirements.txt

Option 2 — Docker (Recommended)

docker build -t pdpbiogen:latest .

Test container:

docker run -it pdpbiogen:latest python -c "import dpbiogen; print('OK')"

▶ Run a Full Healing Simulation
Direct Python (simple run)

python dpbiogen/quantum/demo_full_body.py \
    --eeg benchmarks/bci/sample.edf \
    --sbml benchmarks/metabolomics/sample.xml \
    --out results/healing_demo

Produces:

    symmetry.json

    eeg_features.json

    gene_delta.json

    flux_results.json

    manifest.json

Nextflow Pipeline (full reproducibility)

./nextflow run . -profile docker \
    -with-report results/run_report.html \
    -with-trace results/trace.txt \
    -with-timeline results/timeline.html

Pipeline includes:
EEG → NSM → Gene Mapper → Metabolism → Healing Simulation
📊 Benchmarking Suite

PDPBioGen includes real datasets & test harness:
Included:

    PhysioNet EEGMMIDB samples

    Toy SBML metabolic model

    Pytest suite

    Determinism tests

    Performance benchmarks

    Environment reproducibility checks

Run all tests:

pytest -q

📁 Outputs

Every run produces:

results/
    symmetry.json
    eeg_features.json
    gene_delta.json
    flux_results.json
    manifest.json

manifest.json logs:

    software versions

    dataset hashes

    execution pipeline

    parameters

    reproducibility flags

⚠️ Disclaimer

PDPBioGen is NOT a medical device.
It does NOT claim to diagnose, treat, or cure anything.
It is a computational research/simulation framework only.

All biological predictions require:

    empirical validation

    proper lab controls

    ethical review

🤝 Contributing

We welcome:

    NSM extensions

    New EEG datasets

    More SBML models

    New mappings (ML, mechanistic, hybrid)

    Improved documentation

    Visualization modules

Steps:

    Fork

    Create feature branch

    Add & run tests

    Submit pull request

📖 Citation

Create a CITATION.cff:

cff-version: 1.2.0
message: "Please cite PDPBioGen if you use it."
authors:
  - family-names: Ford
    given-names: Tony
title: "PDPBioGen: Brain-Guided Multi-Scale Biological Simulation"
version: "2025.1"

📬 Contact

For discussions, collaborations, and research inquiries:

Tony E. Ford
Independent Researcher – Neurophysics & Quantum Systems
Email: your contact here
🧩 Appendix A — Example: NSM API

from dpbiogen.neuro.neuro_symmetry_mapper import NeuroSymmetryMapper

nsm = NeuroSymmetryMapper()
brain_state = nsm.compute("sample.edf")
print(brain_state)

🧩 Appendix B — Example: Integrating NSM Into Healing Pipeline

from dpbiogen.neuro.neuro_symmetry_mapper import NeuroSymmetryMapper
from dpbiogen.quantum.gene_mapper import GeneMapper
from dpbiogen.quantum.metabolism import MetabolismEngine

nsm = NeuroSymmetryMapper()
gene = GeneMapper()
met = MetabolismEngine()

state = nsm.compute(eeg_path)
delta = gene.map(state)
flux = met.run(delta)

🧩 Appendix C — Example: Nextflow Process (NSM Step)

process NEURO_SYMMETRY {
  input:
    path eeg
  output:
    path "symmetry.json"

  script:
    """
    python -m dpbiogen.neuro.run_symmetry_mapper \
        --eeg $eeg \
        --out symmetry.json
    """
}
