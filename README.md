# PDPBioGen

**Parallel Distributed Processing for Multi-Scale Biological Integration & Brain-Guided Simulation**  
*(“PDP” + “BioGen / Bio-Integration / Biological Generation”) — EEG ↔ Genomics ↔ Metabolism simulation framework*

---

## 🔎 What is PDPBioGen

PDPBioGen is an open-source Python framework combining EEG/BCI, gene-expression modeling, and metabolic simulation — enabling reproducible, end-to-end **in silico** “healing simulations”:  
- Load EEG / neural data, preprocess and extract features.  
- Map neural features to a **surrogate gene-expression perturbation signature**.  
- Apply perturbations to a constraint-based metabolic model and compute metabolic flux changes.  
- Produce deterministic output (feature files, gene-delta tables, flux-balance results) inside a reproducible environment (conda / Docker + Nextflow workflow).  

The goal is *not* to make clinical or therapeutic claims, but to provide a **research tool** for hypothesis generation, exploratory simulations, and reproducible computational biology experiments.

---

## 🚀 Quick Start (Development or Smoke Test)

### Requirements
- Docker (recommended) or conda (Python 3.11)  
- For conda: `mamba` or `conda`  

### Install (conda)

```bash
conda env create -f environment.yml   # creates env named `pdpbiogen`
conda activate pdpbiogen
pip install -r requirements.txt       # if you use a requirements file instead
