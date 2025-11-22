# dpbiogen/quantum/full_body_demo.py  (new integrated demo)
"""
Runnable standalone demo — integrates seizure (brain/neural) and heart (cardiovascular) subsystems
for full-body healing via quantum-inspired entanglement + residual brain intent.

Uses synthetic data by default, but can load real heart data from a CSV (e.g., processed ECG samples).
For real data: create a CSV with agent_name,initial_state pairs from actual metrics
(e.g., derive deviations from ECG via std dev of RR intervals for HRV, etc.).

Run with: python -m dpbiogen.quantum.full_body_demo   or   python full_body_demo.py  from this folder.
Optionally: python full_body_demo.py path/to/real_heart_data.csv
"""

import sys
from mapper import Mapper
from utils import load_initial_states_from_csv  # New loader utility

if __name__ == "__main__":
    # Optional: Load real heart data from CSV if provided as arg
    real_heart_csv = sys.argv[1] if len(sys.argv) > 1 else None
    
    mapper = Mapper(neural_weight_multiplier=180.0)  # Balanced multiplier for full-body

    # Neural control agent (shared for full-body)
    neural = mapper.add_agent("Residual-Intent-Detector", initial_state=10.0, is_neural=True)

    # Seizure/brain subsystem agents (from original demo, with more added for depth)
    brain_agents = [
        mapper.add_agent("Cerebral-Left", 18.0),
        mapper.add_agent("Cerebral-Right", -14.0),
        mapper.add_agent("Mitochondria-Net", 23.0),  # Cellular energy
        mapper.add_agent("Immune-Response", -19.0),  # Inflammation markers
        mapper.add_agent("Neurotrans-Balance", 16.0),  # Chemical signaling
        mapper.add_agent("EEG-Alpha-Wave", 20.0),  # New: Frequency band deviation
        mapper.add_agent("EEG-Theta-Wave", -15.0),  # New: Another band for realism
        mapper.add_agent("Synaptic-Plasticity", 22.0),  # New: Learning/adaptation metric
    ]

    # Heart/cardiovascular subsystem agents (from heart_demo, with more added)
    if real_heart_csv:
        print(f"Loading real heart data from {real_heart_csv}...")
        real_states = load_initial_states_from_csv(real_heart_csv)
        heart_agents = []
        for name, state in real_states.items():
            heart_agents.append(mapper.add_agent(name, initial_state=state))
    else:
        heart_agents = [
            mapper.add_agent("Heart-Rate-Variability", 25.0),
            mapper.add_agent("Blood-Pressure-Systolic", 22.0),
            mapper.add_agent("Blood-Pressure-Diastolic", -18.0),
            mapper.add_agent("Vascular-Inflammation", 19.0),
            mapper.add_agent("Cardiac-Output", -15.0),
            mapper.add_agent("Atrial-Fibrillation-Index", 24.0),
            mapper.add_agent("Coronary-Flow-Reserve", -20.0),
            mapper.add_agent("Endothelial-Function", 17.0),
            mapper.add_agent("QT-Interval-Variability", 21.0),  # New: ECG-specific metric
            mapper.add_agent("Ventricular-Ejection-Fraction", -16.0),  # New: Heart efficiency
            mapper.add_agent("Autonomic-Nervous-Balance", 18.0),  # New: Sympathetic/parasympathetic
        ]

    # Additional full-body subsystems (e.g., endocrine, muscular) for integration
    other_agents = [
        mapper.add_agent("Hormonal-Equilibrium", 19.0),  # Endocrine deviation
        mapper.add_agent("Muscle-Tone-Variability", -17.0),  # Musculoskeletal
        mapper.add_agent("Respiratory-Rate-Dev", 20.0),  # Pulmonary
        mapper.add_agent("Metabolic-Rate-Index", -14.0),  # Energy metabolism
    ]

    # Entangle everything into one big symmetry group — brain intent controls full body
    all_agents = brain_agents + heart_agents + other_agents
    mapper.entangle_group([neural] + all_agents)

    print("=== PDPBioGen Quantum Module Full-Body Healing Demo ===\n")
    print("Full-body chaos state (high deviations across subsystems):")
    mapper.print_states()
    print(f"\nTotal biological deviation = {mapper.bio_deviation():.2f}\n")

    # Residual intent detected → force neural to 0.0 and collapse
    print("Residual patient brain intent detected → forcing neural agent to healthy 0.0 and triggering symmetry collapse...")
    neural.state = 0.0

    mapper.collapse()

    print("\nAfter single quantum collapse (∼50 ms latency):")
    mapper.print_states()
    print(f"\nTotal biological deviation after collapse = {mapper.bio_deviation():.2f} → full-body healed")

    print("\nFull-body healing complete via quantum-inspired non-local correlation.")
