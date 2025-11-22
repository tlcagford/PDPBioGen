# dpbiogen/quantum/mapper.py
"""
Core classes for quantum-inspired symmetry mapping in PDPBioGen.

- Agent: holds a state (float deviation from healthy equilibrium; healthy = 0.0)
- Entangler: manages entanglement groups and performs "collapse_symmetry" (weighted sync)
- Mapper: convenience wrapper that creates/manages agents and triggers collapse

The key quantum-inspired mechanism is the weighted average collapse: neural/control agents
have massively amplified weight (default 100×), so even forcing the neural agent to the
healthy state 0.0 (detected residual intent) instantly pulls the entire entangled
biological system to near-zero deviation — simulating non-local, 50-ms latency healing.
"""

class Agent:
    def __init__(self, name: str, initial_state: float = 0.0, is_neural: bool = False):
        self.name = name
        self.state = float(initial_state)
        self.is_neural = is_neural

    def __repr__(self) -> str:
        tag = " (Neural Control)" if self.is_neural else " (Bio)"
        return f"{self.name}{tag}: {self.state:+.3f}"


class Entangler:
    def __init__(self, neural_weight_multiplier: float = 100.0):
        self.groups: list[list[Agent]] = []
        self.neural_weight_multiplier = neural_weight_multiplier

    def entangle(self, agents: list[Agent]):
        """Create a quantum-entangled group — all agents will instantly synchronize when collapse_symmetry is called."""
        if len(agents) > 1:
            self.groups.append(agents.copy())

    def collapse_symmetry(self):
        """Quantum-inspired collapse: weighted synchronization (neural agents dominate)."""
        for group in self.groups:
            if len(group) < 2:
                continue

            weighted_sum = 0.0
            total_weight = 0.0
            for a in group:
                w = self.neural_weight_multiplier if a.is_neural else 1.0
                weighted_sum += w * a.state
                total_weight += w

            if total_weight == 0:
                continue

            target_state = weighted_sum / total_weight

            for a in group:
                a.state = target_state


class Mapper:
    """Main interface used by the wider PDPBioGen framework."""
    def __init__(self, neural_weight_multiplier: float = 100.0):
        self.agents: list[Agent] = []
        self.entangler = Entangler(neural_weight_multiplier)

    def add_agent(self, name: str, initial_state: float = 0.0, is_neural: bool = False) -> Agent:
        agent = Agent(name, initial_state, is_neural)
        self.agents.append(agent)
        return agent

    def entangle_group(self, agents: list[Agent]):
        self.entangler.entangle(agents)

    def collapse(self):
        """Trigger quantum collapse / symmetry restoration."""
        self.entangler.collapse_symmetry()

    def print_states(self):
        for a in self.agents:
            print(a)

    def bio_deviation(self) -> float:
        return sum(abs(a.state) for a in self.agents if not a.is_neural)
