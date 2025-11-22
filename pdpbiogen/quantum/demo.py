# Demo: Run quantum mapper with synthetic data (or mock OpenBCI/Emotiv)
from mapper import QuantumNeuroSymmetryMapper

# Synthetic inputs (PDPBioGen-style)
neural_flux = np.random.rand(100, 14) + np.sin(np.linspace(0, 10, 100))[:, None]  # Biophoton/EEG proxy
genomic = 'ATGC' * 1250
metabolic = np.random.rand(100, 20)

mapper = QuantumNeuroSymmetryMapper(g=0.01)
result = mapper.create_quantum_human_map(neural_flux, genomic, metabolic, gap_mm=5)

print("Quantum Human Map:")
for k, v in result.items():
    if isinstance(v, np.ndarray):
        print(f"- {k}: Shape {v.shape}")
    else:
        print(f"- {k}: {v}")
