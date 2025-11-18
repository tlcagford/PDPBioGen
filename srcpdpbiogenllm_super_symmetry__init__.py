# src/pdpbiogen/llm_super_symmetry/__init__.py
"""
Adapted llm-super-symmetry for multi-agent biological collaboration
"""

from .multi_agent_collaboration import MultiAgentCollaboration
from .domain_agents import DomainAgent, NeuralAgent, GenomicAgent, MetabolicAgent
from .conflict_resolver import ConflictResolver

__all__ = [
    'MultiAgentCollaboration', 
    'DomainAgent', 
    'NeuralAgent', 
    'GenomicAgent', 
    'MetabolicAgent',
    'ConflictResolver'
]