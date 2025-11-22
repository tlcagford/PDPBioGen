# tutorial_1_basic_scan.py
from quantum_healing import QuantumCTHealingSystem
import numpy as np

# Initialize system
system = QuantumCTHealingSystem()

# Generate 3D quantum CT scan
scan_data = system.generate_quantum_ct_scan('heart_tissue')

# Analyze scan results
print("Scan Results:")
for metric, data in scan_data.items():
    print(f"{metric}: {np.mean(data):.1f} ± {np.std(data):.1f}")

# Visualize
system.visualize_quantum_ct_scan('heart_tissue')