# Create examples directory
os.makedirs('examples', exist_ok=True)
print("✅ Created examples/ directory")

# Create basic_usage.py
basic_usage_content = '''"""
PDPBioGen Basic Usage Example
Simple demonstration of core functionality
"""
import sys
import os
import matplotlib.pyplot as plt

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from heart_healing import HeartHealingSimulator, run_closed_loop_test, run_open_loop_test
    from quantum_simulation import QuantumBiologicalSimulator
    print("✅ All modules imported successfully!")
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Please make sure you've installed the requirements:")
    print("pip install -r requirements.txt")
    sys.exit(1)


def demonstrate_basic_functionality():
    """Demonstrate basic PDPBioGen functionality"""
    print("🚀 PDPBioGen Basic Usage Demo")
    print("=" * 50)
    
    # 1. Initialize simulators
    print("1. Initializing simulators...")
    heart_simulator = HeartHealingSimulator()
    quantum_simulator = QuantumBiologicalSimulator(n_states=5)
    
    print(f"   Heart simulator: {type(heart_simulator).__name__}")
    print(f"   Quantum simulator: {type(quantum_simulator).__name__}")
    
    # 2. Generate sample data
    print("2. Generating sample data...")
    heart_data = heart_simulator.generate_heart_data(n_samples=200)
    quantum_data = quantum_simulator.simulate_healing_dynamics(time_steps=100)
    
    print(f"   Heart data: {len(heart_data)} samples, {len(heart_data.columns)} features")
    print(f"   Quantum data: {len(quantum_data)} time steps")
    
    # 3. Run comparative tests
    print("3. Running comparative tests...")
    closed_loop_data = run_closed_loop_test(n_samples=100)
    open_loop_data = run_open_loop_test(n_samples=100)
    
    print(f"   Closed loop test: {len(closed_loop_data)} samples")
    print(f"   Open loop test: {len(open_loop_data)} samples")
    
    return {
        'heart_data': heart_data,
        'quantum_data': quantum_data,
        'closed_loop': closed_loop_data,
        'open_loop': open_loop_data
    }


def create_basic_visualization(results):
    """Create basic visualization of results"""
    print("4. Creating visualizations...")
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Plot 1: Heart healing progression
    heart_data = results['heart_data']
    axes[0, 0].plot(heart_data['time_hours'], heart_data['tissue_viability'])
    axes[0, 0].set_title('Tissue Viability Over Time')
    axes[0, 0].set_xlabel('Time (hours)')
    axes[0, 0].set_ylabel('Viability (%)')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Plot 2: Cellular coherence
    axes[0, 1].plot(heart_data['time_hours'], heart_data['cellular_coherence'], color='green')
    axes[0, 1].set_title('Cellular Coherence Over Time')
    axes[0, 1].set_xlabel('Time (hours)')
    axes[0, 1].set_ylabel('Coherence')
    axes[0, 1].grid(True, alpha=0.3)
    
    # Plot 3: Quantum entanglement
    quantum_data = results['quantum_data']
    time_steps = [d['time_step'] for d in quantum_data]
    entanglement = [d['entanglement'] for d in quantum_data]
    axes[1, 0].plot(time_steps, entanglement, color='purple')
    axes[1, 0].set_title('Quantum Entanglement Dynamics')
    axes[1, 0].set_xlabel('Time Steps')
    axes[1, 0].set_ylabel('Entanglement Strength')
    axes[1, 0].grid(True, alpha=0.3)
    
    # Plot 4: Treatment comparison
    closed_viability = results['closed_loop']['tissue_viability']
    open_viability = results['open_loop']['tissue_viability']
    axes[1, 1].plot(closed_viability, label='Closed Loop', alpha=0.7)
    axes[1, 1].plot(open_viability, label='Open Loop', alpha=0.7)
    axes[1, 1].set_title('Closed vs Open Loop Performance')
    axes[1, 1].set_xlabel('Sample Index')
    axes[1, 1].set_ylabel('Tissue Viability')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('pdpbiogen_basic_demo.png', dpi=150, bbox_inches='tight')
    print("   ✅ Saved visualization as 'pdpbiogen_basic_demo.png'")
    
    return fig


if __name__ == "__main__":
    print("PDPBioGen Basic Usage Example")
    print("This demo shows core functionality and generates sample visualizations.")
    print()
    
    # Run the demonstration
    results = demonstrate_basic_functionality()
    
    # Create visualizations
    fig = create_basic_visualization(results)
    
    print()
    print("🎉 Demo completed successfully!")
    print("📊 Check the generated 'pdpbiogen_basic_demo.png' for results.")
    print()
    print("Next steps:")
    print("  - Run 'python examples/heart_healing_demo.py' for advanced cardiac analysis")
    print("  - Run 'python examples/quantum_demo.py' for quantum simulation details")
    print("  - Run 'pytest tests/' to run the test suite")
'''

with open('examples/basic_usage.py', 'w') as f:
    f.write(basic_usage_content)
print("✅ Created examples/basic_usage.py")

# Create heart_healing_demo.py
heart_demo_content = '''"""
Advanced Heart Healing Demonstration
Comprehensive demonstration of cardiac tissue regeneration simulation
"""
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from heart_healing import HeartHealingSimulator
    print("✅ Heart healing module imported successfully!")
except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)


def demonstrate_advanced_heart_healing():
    """Demonstrate advanced heart healing capabilities"""
    print("💓 Advanced Heart Healing Demo")
    print("=" * 50)
    
    # Initialize simulator with different parameters
    simulators = {
        'Control': HeartHealingSimulator(healing_rate=0.08, treatment_type='control'),
        'Standard': HeartHealingSimulator(healing_rate=0.14, treatment_type='standard'),
        'Quantum Enhanced': HeartHealingSimulator(healing_rate=0.23, treatment_type='quantum_enhanced')
    }
    
    results = {}
    
    # Run simulations for each treatment type
    for treatment, simulator in simulators.items():
        print(f"Running {treatment} treatment simulation...")
        
        # Generate multi-scale data
        multi_scale_data = simulator.generate_multi_scale_data(n_samples=300)
        
        # Run both test types
        closed_data = simulator.run_closed_loop_test(n_samples=150)
        open_data = simulator.run_open_loop_test(n_samples=150)
        
        results[treatment] = {
            'multi_scale': multi_scale_data,
            'closed_loop': closed_data,
            'open_loop': open_data,
            'simulator': simulator
        }
    
    return results


def create_advanced_visualizations(results):
    """Create comprehensive visualizations"""
    print("Creating advanced visualizations...")
    
    # Create a comprehensive figure
    fig = plt.figure(figsize=(16, 12))
    
    # 1. Multi-scale progression
    ax1 = plt.subplot(2, 3, 1)
    treatments = list(results.keys())
    
    for treatment in treatments:
        tissue_data = results[treatment]['multi_scale']['tissue']
        viability = tissue_data['tissue_viability'].values
        ax1.plot(viability, label=treatment, alpha=0.8, linewidth=2)
    
    ax1.set_title('Tissue Viability Progression\nby Treatment Type')
    ax1.set_xlabel('Time (hours)')
    ax1.set_ylabel('Viability (%)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 2. Healing rate comparison
    ax2 = plt.subplot(2, 3, 2)
    healing_rates = []
    
    for treatment in treatments:
        closed_data = results[treatment]['closed_loop']
        improvement = closed_data['tissue_viability'].iloc[-1] - closed_data['tissue_viability'].iloc[0]
        healing_rates.append(improvement)
    
    bars = ax2.bar(treatments, healing_rates, color=['red', 'orange', 'green'], alpha=0.7)
    ax2.set_title('Total Healing Improvement\nby Treatment Type')
    ax2.set_ylabel('Improvement (%)')
    
    # Add value labels on bars
    for bar, rate in zip(bars, healing_rates):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{rate:.1f}%', ha='center', va='bottom')
    
    # 3. Cellular-level analysis
    ax3 = plt.subplot(2, 3, 3)
    
    for treatment in treatments:
        cellular_data = results[treatment]['multi_scale']['cellular']
        coherence = cellular_data['cellular_coherence'].values
        ax3.plot(coherence, label=treatment, alpha=0.8)
    
    ax3.set_title('Cellular Coherence Dynamics')
    ax3.set_xlabel('Time (hours)')
    ax3.set_ylabel('Coherence Level')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # 4. Molecular-level activity
    ax4 = plt.subplot(2, 3, 4)
    
    quantum_treatment = results['Quantum Enhanced']['multi_scale']['molecular']
    ax4.plot(quantum_treatment['time'], quantum_treatment['protein_synthesis'], 
             label='Protein Synthesis', linewidth=2)
    ax4.plot(quantum_treatment['time'], quantum_treatment['gene_expression'], 
             label='Gene Expression', linewidth=2)
    ax4.plot(quantum_treatment['time'], quantum_treatment['metabolic_rate'], 
             label='Metabolic Rate', linewidth=2)
    
    ax4.set_title('Molecular-Level Activities\n(Quantum Enhanced Treatment)')
    ax4.set_xlabel('Time (hours)')
    ax4.set_ylabel('Activity Level')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    # 5. Control signal comparison
    ax5 = plt.subplot(2, 3, 5)
    
    for treatment in treatments:
        closed_data = results[treatment]['closed_loop']
        control_signals = closed_data['control_signal'].values[:50]  # First 50 samples
        ax5.plot(control_signals, label=treatment, alpha=0.7)
    
    ax5.set_title('Adaptive Control Signals\n(Closed Loop)')
    ax5.set_xlabel('Time Step')
    ax5.set_ylabel('Control Signal')
    ax5.legend()
    ax5.grid(True, alpha=0.3)
    
    # 6. Performance metrics heatmap
    ax6 = plt.subplot(2, 3, 6)
    
    metrics_data = []
    for treatment in treatments:
        closed_data = results[treatment]['closed_loop']
        metrics = [
            closed_data['tissue_viability'].mean(),  # Average viability
            closed_data['tissue_viability'].std(),   # Stability
            closed_data['control_signal'].std(),     # Control activity
            closed_data['feedback_error'].abs().mean()  # Error magnitude
        ]
        metrics_data.append(metrics)
    
    metrics_data = np.array(metrics_data)
    metric_names = ['Avg Viability', 'Stability', 'Control Activity', 'Error']
    
    sns.heatmap(metrics_data, annot=True, fmt='.2f', xticklabels=metric_names,
                yticklabels=treatments, ax=ax6, cmap='YlOrRd')
    ax6.set_title('Performance Metrics Comparison')
    
    plt.tight_layout()
    plt.savefig('pdpbiogen_advanced_heart_demo.png', dpi=150, bbox_inches='tight')
    print("✅ Saved advanced visualization as 'pdpbiogen_advanced_heart_demo.png'")
    
    return fig


def print_statistical_analysis(results):
    """Print statistical analysis of results"""
    print("\\n📊 Statistical Analysis")
    print("=" * 40)
    
    for treatment in results.keys():
        closed_data = results[treatment]['closed_loop']
        open_data = results[treatment]['open_loop']
        
        closed_improvement = closed_data['tissue_viability'].iloc[-1] - closed_data['tissue_viability'].iloc[0]
        open_improvement = open_data['tissue_viability'].iloc[-1] - open_data['tissue_viability'].iloc[0]
        
        advantage = ((closed_improvement - open_improvement) / open_improvement) * 100
        
        print(f"\\n{treatment}:")
        print(f"  Closed Loop Improvement: {closed_improvement:.1f}%")
        print(f"  Open Loop Improvement: {open_improvement:.1f}%")
        print(f"  Closed Loop Advantage: {advantage:+.1f}%")


if __name__ == "__main__":
    print("PDPBioGen Advanced Heart Healing Demonstration")
    print("This demo shows comprehensive cardiac tissue regeneration analysis.")
    print()
    
    # Run advanced demonstration
    results = demonstrate_advanced_heart_healing()
    
    # Create visualizations
    create_advanced_visualizations(results)
    
    # Print statistical analysis
    print_statistical_analysis(results)
    
    print()
    print("🎉 Advanced demo completed!")
    print("📈 Check the generated visualization and statistical analysis above.")
    print()
    print("Key insights demonstrated:")
    print("  - Multi-scale biological integration")
    print("  - Treatment efficacy comparison") 
    print("  - Closed vs open loop performance")
    print("  - Quantum-enhanced treatment benefits")
'''

with open('examples/heart_healing_demo.py', 'w') as f:
    f.write(heart_demo_content)
print("✅ Created examples/heart_healing_demo.py")
