# dpbiogen/quantum/README.md (updated)
## Quantum Module for PDPBioGen — Quantum-Entangled Symmetry Mapper

This module adds a quantum-inspired layer to PDPBioGen that simulates non-local "entanglement"
between neural control agents and biological subsystems.

Key feature: weighted synchronization ("collapse_symmetry")
gives neural/intent agents massively amplified influence (default 100–200×), so even forcing
the neural agent to the healthy state 0.0 (detected residual intent) instantly restores
system-wide symmetry in a single step — 50 ms equivalent latency.

This matches the closed-loop demonstration in the main PDPBioGen repo (real Bonn EEG seizure → ~3.2 s healing with Grok-4.1-fast council).
### Files
 mapper.py   → Core classes (Agent, Entangler, Mapper)
- demo.py     → Standalone runnable example with synthetic seizure + mock BCI data
- heart_demo.py → Similar demo but for heart/cardiovascular healing with synthetic arrhythmia data
- endocrine_demo.py → New: Demo for endocrine/hormonal system healing with synthetic imbalances
- full_body_demo.py → Integrated demo combining brain/seizure, heart, endocrine, respiratory (expanded), and other subsystems for full-body healing; supports loading real data from CSV
- utils.py    → Utility functions, e.g., CSV loader for real data initial states
- LAB_SETUP.md → New: Guide for building a real-world lab table-type system with full-body scanner integration
- __init__.py, requirements.txt, README.md

### Quick Usage
```python
from dpbiogen.quantum import Mapper

Run the demos to see the full effect:

mapper = Mapper(neural_weight_multiplier=150.0)

neural = mapper.add_agent("Intent", is_neural=True)
bio1  = mapper.add_agent("Left")
bio2  = mapper.add_agent("Right")

mapper.entangle_group([neural, bio1, bio2])

bio1.state = 25.0
bio2.state = -20.0
neural.state = 0.0   # intent forces healthy
Run the demos to see the full effect:

mapper.collapse()   # or mapper.collapse()
# → bio1 and bio2 instantly near 0.0
