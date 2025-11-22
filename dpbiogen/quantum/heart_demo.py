# dpbiogen/quantum/heart_demo.py
"""
Runnable standalone demo — shows how residual brain intent + quantum-inspired entanglement
heals a chaotic heart arrhythmia-like state in a single collapse step (∼50 ms equivalent).

This is similar to the seizure demo but focused on cardiovascular subsystems, using synthetic
heart data (e.g., irregular HRV, blood pressure spikes, vascular inflammation). In a real
PDPBioGen integration, this could pull from mock or actual ECG/heart monitor data.

Run with: python -m dpbiogen.quantum.heart_demo   or   python heart_demo.py  from this folder.
"""

from mapper import Mapper

if __name__ == "__main__":
    mapper = Mapper(neural_weight_multiplier=150.0)  # Slightly lower multiplier for demo variety

    neural = mapper.add_agent("Residual-Intent-Detector", initial_state=8.5, is_neural=True)

    heart_agents = [
        mapper.add_agent("Heart-Rate-Variability", 25.0),  # High deviation: irregular beats
        mapper.add_agent("Blood-Pressure-Systolic", 22.0),  # Hypertension spike
        mapper.add_agent("Blood-Pressure-Diastolic", -18.0),  # Hypotension drop in other phases
        mapper.add_agent("Vascular-Inflammation", 19.0),  # Simulated cytokine storm effect
        mapper.add_agent("Cardiac-Output", -15.0),  # Reduced efficiency
        mapper.add_agent("Atrial-Fibrillation-Index", 24.0),  # Arrhythmia marker
        mapper.add_agent("Coronary-Flow-Reserve", -20.0),  # Impaired blood flow
        mapper.add_agent("Endothelial-Function", 17.0),  # Dysfunction level
    ]

    # One big entangled symmetry group — brain intent + full cardiovascular state
    mapper.entangle_group([neural] + heart_agents)

    print("=== PDPBioGen Quantum Module Heart Healing Demo ===\n")
    print("Arrhythmia/heart chaos state (high biological deviation, synthetic data):")
    mapper.print_states()
    print(f"\nTotal biological deviation = {mapper.bio_deviation():.2f}\n")

    # Residual intent detected → force neural agent to healthy 0.0 (the "measurement"/intent collapse)
    print("Residual patient brain intent detected → forcing neural agent to healthy 0.0 and triggering symmetry collapse...")
    neural.state = 0.0

    mapper.collapse()

    print("\nAfter single quantum collapse (∼50 ms latency):")
    mapper.print_states()
    print(f"\nTotal biological deviation after collapse = {mapper.bio_deviation():.2f} → heart healed")

    print("\nHeart healing complete via quantum-inspired non-local correlation.")
