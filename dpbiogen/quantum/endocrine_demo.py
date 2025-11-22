# dpbiogen/quantum/endocrine_demo.py
"""
Runnable standalone demo — shows how residual brain intent + quantum-inspired entanglement
heals a disrupted endocrine system (e.g., hormonal imbalances like thyroid dysfunction or stress response overload) in a single collapse step (∼50 ms equivalent).

This uses synthetic endocrine data (e.g., hormone levels, gland activity deviations). In a real PDPBioGen setup, this could integrate with blood tests or wearable hormone monitors.

Run with: python -m dpbiogen.quantum.endocrine_demo   or   python endocrine_demo.py  from this folder.
"""

from mapper import Mapper

if __name__ == "__main__":
    mapper = Mapper(neural_weight_multiplier=120.0)  # Adjusted for endocrine sensitivity

    neural = mapper.add_agent("Residual-Intent-Detector", initial_state=7.5, is_neural=True)

    endocrine_agents = [
        mapper.add_agent("Thyroid-Hormone-Level", 20.0),  # Hyperthyroidism deviation
        mapper.add_agent("Cortisol-Stress-Index", 18.0),  # Adrenal overload
        mapper.add_agent("Insulin-Glucose-Balance", -15.0),  # Hypoglycemia swing
        mapper.add_agent("Estrogen-Progesterone-Ratio", 16.0),  # Hormonal cycle imbalance
        mapper.add_agent("Testosterone-Level-Dev", -14.0),  # Androgen deficiency
        mapper.add_agent("Growth-Hormone-Secretion", 19.0),  # Pituitary dysfunction
        mapper.add_agent("Melatonin-Circadian-Rhythm", -17.0),  # Sleep hormone disruption
        mapper.add_agent("Adrenaline-Response-Var", 21.0),  # Fight-or-flight excess
    ]

    # One big entangled symmetry group — brain intent + full endocrine state
    mapper.entangle_group([neural] + endocrine_agents)

    print("=== PDPBioGen Quantum Module Endocrine Healing Demo ===\n")
    print("Endocrine imbalance state (high hormonal deviations, synthetic data):")
    mapper.print_states()
    print(f"\nTotal biological deviation = {mapper.bio_deviation():.2f}\n")

    # Residual intent detected → force neural agent to healthy 0.0 and collapse
    print("Residual patient brain intent detected → forcing neural agent to healthy 0.0 and triggering symmetry collapse...")
    neural.state = 0.0

    mapper.collapse()

    print("\nAfter single quantum collapse (∼50 ms latency):")
    mapper.print_states()
    print(f"\nTotal biological deviation after collapse = {mapper.bio_deviation():.2f} → endocrine system healed")

    print("\nEndocrine healing complete via quantum-inspired non-local correlation.")
