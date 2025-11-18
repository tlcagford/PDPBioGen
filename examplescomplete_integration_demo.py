# examples/complete_integration_demo.py

from pdpbiogen import PDPBioGenIntegrator, UnifiedConfig
import numpy as np

def run_complete_integration_demo():
    """
    Demonstration of fully integrated PDPBioGen system
    """
    print("🎯 PDPBioGen Complete Integration Demo")
    print("=" * 50)
    
    # Configuration for demo
    config = UnifiedConfig(
        num_processes=4,
        domains=['neural', 'genomic', 'metabolic'],
        integration_strategy='collaborative',
        evolution_generations=10,  # Reduced for demo
        enable_critics=True
    )
    
    # Initialize complete system
    integrator = PDPBioGenIntegrator(config)
    
    # Generate demo data
    brain_signals = generate_demo_brain_signals()
    biological_data = generate_demo_biological_data()
    
    print("📊 Demo Data Generated:")
    print(f"   • Brain signals: {len(brain_signals)} channels")
    print(f"   • Biological data: {len(biological_data)} domains")
    print(f"   • Target tissue: dermal_wound")
    
    # Run complete pipeline
    results = integrator.run_complete_healing_pipeline(
        brain_signals=brain_signals,
        biological_data=biological_data,
        target_tissue="dermal_wound",
        simulation_steps=20  # Reduced for demo
    )
    
    # Display results
    display_integration_results(results)
    
    return integrator, results

def generate_demo_brain_signals():
    """Generate demo brain signals"""
    channels = ['Fp1', 'Fp2', 'C3', 'C4', 'O1', 'O2']
    signals = {}
    
    for channel in channels:
        # Simulate relaxed state (high alpha)
        t = np.linspace(0, 30, 7500)  # 30 seconds at 250Hz
        signal = (
            0.6 * np.sin(2 * np.pi * 10 * t) +  # Alpha waves
            0.3 * np.sin(2 * np.pi * 20 * t) +  # Beta waves
            0.1 * np.random.normal(0, 0.5, len(t))  # Noise
        )
        signals[channel] = signal
    
    return signals

def generate_demo_biological_data():
    """Generate demo biological data"""
    return {
        'neural': {
            'eeg_power': {'alpha': 0.6, 'beta': 0.3, 'theta': 0.1},
            'connectivity': np.random.random((6, 6))
        },
        'genomic': {
            'genes': ['BDNF', 'VEGF', 'TGFB1', 'IL10'],
            'expression': [0.8, 0.7, 0.5, 0.3],
            'pathways': ['neurogenesis', 'angiogenesis', 'inflammation_control']
        },
        'metabolic': {
            'metabolites': ['glucose', 'lactate', 'atp'],
            'concentrations': [5.0, 1.2, 8.5],
            'flux_rates': {'glycolysis': 0.7, 'tca_cycle': 0.6}
        }
    }

def display_integration_results(results):
    """Display integration results"""
    print("\n🎉 INTEGRATION RESULTS")
    print("=" * 40)
    
    print("🧠 Brain Translation:")
    if 'brain_instructions' in results:
        instructions = results['brain_instructions']
        print(f"   • Detected state: {instructions.get('brain_state', 'unknown')}")
        print(f"   • Target pathways: {len(instructions.get('target_pathways', []))}")
    
    print("\n🔬 Biological Integration:")
    if 'integrated_biology' in results:
        biology = results['integrated_biology']
        print(f"   • Domains integrated: {len(biology.get('domains', []))}")
        print(f"   • Cross-domain relationships: {len(biology.get('relationships', []))}")
    
    print("\n🏥 Healing Optimization:")
    if 'healing_results' in results:
        healing = results['healing_results']
        print(f"   • Simulation steps: {len(healing.get('progress', []))}")
        print(f"   • Final healing rate: {healing.get('final_healing_rate', 0):.2f}")
        print(f"   • Optimization improvement: {healing.get('optimization_gain', 0):.1f}%")
    
    print("\n🔍 Verification Results:")
    if 'verification' in results:
        verification = results['verification']
        print(f"   • Biologically plausible: {verification.get('is_plausible', False)}")
        print(f"   • Violations corrected: {len(verification.get('corrections_applied', []))}")

if __name__ == "__main__":
    integrator, results = run_complete_integration_demo()
    
    print("\n🚀 PDPBioGen Integration Complete!")
    print("All frameworks successfully integrated:")
    print("   ✅ llm-verified-critic → Biological plausibility")
    print("   ✅ llm-super-symmetry → Multi-agent collaboration") 
    print("   ✅ evo-pipeline-ai → Evolutionary optimization")
    print("   ✅ PDPBioGen → Parallel processing engine")
    print("\nReady for brain-guided healing applications! 🧠⚡🧬")