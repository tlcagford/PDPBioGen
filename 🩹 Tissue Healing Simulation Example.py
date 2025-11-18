# examples/tissue_healing_demo.py

def run_tissue_healing_demo():
    """
    Demonstration of tissue healing simulation using PDPBioGen framework
    """
    print("🏥 TISSUE HEALING SIMULATION DEMO")
    print("=" * 50)
    
    # Create a simulated wound (missing tissue region)
    tissue_size = (50, 50, 5)  # 3D tissue slice
    wound_region = create_circular_wound(tissue_size, center=(25, 25), radius=15)
    
    # Initialize simulator with PDPBioGen parallel processing
    simulator = PDPTissueHealingSimulator(
        tissue_size=tissue_size,
        num_processes=4  # Use 4 parallel processes
    )
    
    # Run healing simulation
    healing_progress, final_tissue = simulator.simulate_healing_process(
        initial_wound=wound_region,
        simulation_steps=50
    )
    
    # Analyze results
    analyze_healing_results(healing_progress, final_tissue)
    
    return healing_progress, final_tissue

def create_circular_wound(tissue_size, center, radius):
    """Create a circular wound region in tissue"""
    wound = np.zeros(tissue_size, dtype=bool)
    x, y = center
    for i in range(tissue_size[0]):
        for j in range(tissue_size[1]):
            if np.sqrt((i - x)**2 + (j - y)**2) <= radius:
                wound[i, j, :] = True  # Wound region
    return wound

def analyze_healing_results(healing_progress, final_tissue):
    """Analyze and visualize healing results"""
    print("\n📊 Healing Simulation Results")
    print("=" * 30)
    
    # Extract metrics
    wound_sizes = [step['wound_size'] for step in healing_progress]
    stem_cell_counts = [step['stem_cell_count'] for step in healing_progress]
    angiogenesis_levels = [step['angiogenesis'] for step in healing_progress]
    
    final_wound_size = wound_sizes[-1]
    healing_percentage = (1 - final_wound_size / wound_sizes[0]) * 100
    
    print(f"📈 Healing Progress:")
    print(f"   • Initial wound size: {wound_sizes[0]:.1f}")
    print(f"   • Final wound size: {final_wound_size:.1f}")
    print(f"   • Healing achieved: {healing_percentage:.1f}%")
    print(f"   • Stem cell recruitment: {stem_cell_counts[-1]} cells")
    print(f"   • Angiogenesis level: {angiogenesis_levels[-1]:.3f}")
    
    # Determine healing quality
    if healing_percentage > 90:
        healing_quality = "Excellent regeneration"
    elif healing_percentage > 70:
        healing_quality = "Good healing"
    elif healing_percentage > 50:
        healing_quality = "Partial healing"
    else:
        healing_quality = "Poor healing - intervention needed"
    
    print(f"   • Healing quality: {healing_quality}")
    
    # Simulated therapeutic insights
    print(f"\n💡 Therapeutic Insights:")
    therapeutic_actions = generate_therapeutic_recommendations(healing_progress)
    for i, action in enumerate(therapeutic_actions, 1):
        print(f"   {i}. {action}")

def generate_therapeutic_recommendations(healing_progress):
    """Generate therapeutic recommendations based on simulation"""
    recommendations = []
    
    # Analyze healing patterns
    final_metrics = healing_progress[-1]
    
    if final_metrics['stem_cell_count'] < 100:
        recommendations.append("Apply stem cell recruitment factors (SDF-1, VEGF)")
    
    if final_metrics['angiogenesis'] < 0.5:
        recommendations.append("Enhance angiogenesis with VEGF supplementation")
    
    if final_metrics['inflammation'] > 0.7:
        recommendations.append("Control inflammation with anti-inflammatory signals")
    
    if final_metrics['ecm_quality'] < 0.6:
        recommendations.append("Improve ECM deposition with TGF-β modulation")
    
    recommendations.append("Apply mechanical stimulation to enhance healing")
    recommendations.append("Optimize oxygen delivery to wound site")
    
    return recommendations

# Run the demo
if __name__ == "__main__":
    healing_results, final_tissue = run_tissue_healing_demo()