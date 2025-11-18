# src/pdpbiogen/__init__.py
"""
PDPBioGen: Unified Framework for Brain-Guided Biological Simulation
Integrating:
- llm-verified-critic → Biological plausibility verification
- llm-super-symmetry → Multi-agent domain collaboration  
- evo-pipeline-ai → Evolutionary optimization
- PDPBioGen → Parallel distributed processing
"""

__version__ = "1.0.0"
__author__ = "TL Cagford"
__email__ = "your-email@example.com"

from .core.integrator import PDPBioGenIntegrator
from .translation.brain_signal_translator import PDPBrainSignalTranslator
from .healing.tissue_simulator import PDPTissueHealingSimulator
from .domains.cross_domain_integrator import CrossDomainIntegrator
from .verification.biological_critic import BiologicalCritic

__all__ = [
    'PDPBioGenIntegrator',
    'PDPBrainSignalTranslator', 
    'PDPTissueHealingSimulator',
    'CrossDomainIntegrator',
    'BiologicalCritic'
]