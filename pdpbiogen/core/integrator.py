from pdpbiogen.core.domain_manager import DomainManager
from pdpbiogen.core.agent_system import AgentSystem
from pdpbiogen.validation.validators import validate_combined_output

class Integrator:
    """
    Simple orchestrator: load domain data, dispatch to mappers, collect outputs,
    run an agent step, then validate.
    """
    def __init__(self, domain_manager: DomainManager = None, agent_system: AgentSystem = None):
        self.domain_manager = domain_manager or DomainManager()
        self.agent_system = agent_system or AgentSystem()

    def run(self, inputs: dict) -> dict:
        """Run end-to-end pipeline on a dict of domain inputs."""
        outputs = {}
        for domain, payload in inputs.items():
            map_out = self.domain_manager.map(domain, payload)
            outputs[domain] = map_out

        # Combine domain outputs (simple merge for demo)
        combined = {"domains": outputs}
        # run one agent step (placeholder)
        agent_result = self.agent_system.step(combined)
        result = {"combined": combined, "agent": agent_result}

        # Validate result
        validate_combined_output(result)
        return result
