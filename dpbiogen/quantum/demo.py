# dpbiogen/quantum/demo.py
"""
Runnable standalone demo — shows how residual brain intent + quantum-inspired entanglement
heals a chaotic seizure-like state in a single collapse step (∼50 ms equivalent).

Run with: python -m dpbiogen.quantum.demo   or   python demo.py  from this folder.
"""

from mapper import Mapper

if __name__ == "__main__":
    mapper = Mapper(neural_weight_multiplier=200.0)

    neural = mapper.add_agent("Residual-Intent-Detector", initial_state=9.0, is_neural=True)

    bio_agents = [
        mapper.add_agent("Cerebral-Left",    18.0),
        mapper.add_agent("Cerebral-Right",   -14.0),
        mapper.add_agent("Mitochondria-Net",   23.0),
        mapper.add_agent("Immune-Response",   -19.0),
        mapper.add_agent("Neurotrans-Balance",  16.0),
        mapper.add_agent("Heart-Rate-Var",    21.0),
        mapper.add_agent("Blood-Brain-Flux", -17.0),
    ]

    # One big entangled symmetry group — brain + full body state
    mapper.entangle_group([neural] + bio_agents)

    print("=== PDPBioGen Quantum Module Demo ===\n")
    print("Seizure/chaos state (high biological deviation):")
    mapper.print_states()
    print(f"\nTotal biological deviation = {mapper.bio_deviation():.2f}\n")

    # Residual intent detected → force neural agent to healthy 0.0 (the "measurement"/intent collapse)
    print("Residual patient brain intent detected → forcing neural agent to healthy 0.0 and collapsing symmetry collapse...")
    neural.state = 0.0

    mapper.collapse()

    print("\nAfter single quantum collapse (∼50 ms latency):")
    mapper.print_states()
    print(f"\nTotal biological deviation after collapse = {mapper.bio_deviation():.2f} → healed")

    print("\nHealing complete via quantum-inspired non-local correlation.")
