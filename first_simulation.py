from quantum_healing import QuantumCTHealingSystem
import matplotlib.pyplot as plt

# Initialize the quantum healing system
healing_system = QuantumCTHealingSystem()

# Generate a sample heart healing dataset
heart_data = healing_system.generate_realistic_heart_data()

# Run basic analysis
print("Heart Healing Data Summary:")
print(f"Sample size: {len(heart_data)}")
print(f"Columns: {list(heart_data.columns)}")

# Plot tissue viability progression
plt.figure(figsize=(10, 6))
plt.plot(heart_data['time_hours'], heart_data['tissue_viability'])
plt.title('Heart Tissue Viability Over Time')
plt.xlabel('Time (hours)')
plt.ylabel('Viability (%)')
plt.grid(True, alpha=0.3)
plt.show()