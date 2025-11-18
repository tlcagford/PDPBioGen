#!/usr/bin/env python3
"""
Neuro-Symmetry Mapper - 5 Minute Quick Start
Demo that shows triple-domain integration in action
"""

import os
import sys
import time
from pathlib import Path

# Add src to path for package development
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from neuro_symmetry_mapper.core.evolutionary_pipeline import DomainEvolver
from neuro_symmetry_mapper.core.multi_agent_collab import MultiAgentCollaboration
from neuro_symmetry_mapper.core.critic_verifier import BiologicalCritic
from neuro_symmetry_mapper.data.sample_data import create_sample_data

class QuickStartDemo:
    def __init__(self):
        self.results_dir = Path("./quick_start_results")
        self.results_dir.mkdir(exist_ok=True)
        
    def banner(self):
        print("🧬" * 50)
        print("          NEURO-SYMMETRY MAPPER QUICK START")
        print("🧬" * 50)
        print()
        
    def step1_load_sample_data(self):
        """Step 1: Load or create sample data"""
        print("📥 STEP 1: Loading sample data...")
        
        # Create synthetic sample data for demo purposes
        sample_data = create_sample_data()
        
        print(f"   • Neural data: {sample_data['neural']['eeg'].shape if 'eeg' in sample_data['neural'] else 'Generated'}")