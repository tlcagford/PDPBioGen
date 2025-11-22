# Quantum Drop-In for PDPBioGen

## Overview
Self-contained quantum BCI module using primordial entanglement for non-contact neural symmetry mapping. Integrates with PDPBioGen's multi-domain healing framework.

## Installation
1. Add this `quantum/` dir to PDPBioGen.
2. `pip install -r quantum/requirements.txt`
3. In PDPBioGen root: `pip install -e .` (for package discovery)

## Quick Start
```python
from pdpbiogen.quantum.mapper import QuantumNeuroSymmetryMapper

mapper = QuantumNeuroSymmetryMapper()
result = mapper.create_quantum_human_map(
    neural_flux=np.random.rand(100, 14),  # EEG/biophoton array
    genomic_data='ATGC...',               # Seq string
    metabolic_data=np.random.rand(100, 20), # Flux rates
    gap_mm=5  # Non-contact distance
)
print(result['symmetry_score'])  # e.g., 0.91
