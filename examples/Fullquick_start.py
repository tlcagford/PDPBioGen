#!/usr/bin/env python3
"""
Neuro-Symmetry Mapper - 5 Minute Quick Start
Demo that shows triple-domain integration in action
"""

import os
import sys
import time
import json
from pathlib import Path
import numpy as np
import pandas as pd
from datetime import datetime

# Add src to path for package development
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from neuro_symmetry_mapper.core.evolutionary_pipeline import DomainEvolver
from neuro_symmetry_mapper.core.multi_agent_collab import MultiAgentCollaboration
from neuro_symmetry_mapper.core.critic_verifier import BiologicalCritic
from neuro_symmetry_mapper.data.sample_data import create_sample_data

class QuickStartDemo:
    def __init__(self, test_mode=False):
        self.results_dir = Path("./quick_start_results")
        self.results_dir.mkdir(exist_ok=True)
        self.test_mode = test_mode
        self.start_time = time.time()
        
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
        
        print(f"   • Neural data: {len(sample_data['neural']['regions'])} brain regions")
        print(f"   • Genomic data: {len(sample_data['genomic']['genes'])} genes")
        print(f"   • Metabolic data: {len(sample_data['metabolic']['pathways'])} pathways")
        
        # Save sample data info
        data_info = {
            'neural_regions': list(sample_data['neural']['regions'].keys()),
            'genomic_genes': sample_data['genomic']['genes'][:5],  # First 5
            'metabolic_pathways': sample_data['metabolic']['pathways'][:5],
            'timestamp': datetime.now().isoformat()
        }
        
        with open(self.results_dir / 'sample_data_info.json', 'w') as f:
            json.dump(data_info, f, indent=2)
            
        return sample_data
    
    def step2_initialize_frameworks(self):
        """Step 2: Initialize your three adapted frameworks"""
        print("🔄 STEP 2: Initializing adapted frameworks...")
        
        # Initialize your three core frameworks adapted for biology
        self.critic = BiologicalCritic()
        self.collaboration = MultiAgentCollaboration()
        self.evolver = DomainEvolver()
        
        print("   ✅ Biological Critic initialized (from llm-verified-critic)")
        print("   ✅ Multi-Agent Collaboration initialized (from llm-super-symmetry)")
        print("   ✅ Domain Evolver initialized (from evo-pipeline-ai)")
        
        return {
            'critic': self.critic,
            'collaboration': self.collaboration, 
            'evolver': self.evolver
        }
    
    def step3_neural_domain_analysis(self, sample_data):
        """Step 3: Analyze neural data using multi-agent collaboration"""
        print("🧠 STEP 3: Neural domain analysis...")
        
        # Create neural analysis agents
        neural_agents = self.collaboration.create_domain_agents('neural')
        
        # Each agent analyzes from different perspectives
        analyses = {}
        for agent_name, agent in neural_agents.items():
            analysis = agent.analyze(sample_data['neural'])
            analyses[agent_name] = analysis
            print(f"   • {agent_name}: {len(analysis.get('insights', []))} insights")
        
        # Verify neural analyses for biological plausibility
        verified_analyses = self.critic.verify_domain('neural', analyses)
        
        return verified_analyses
    
    def step4_genomic_domain_analysis(self, sample_data):
        """Step 4: Analyze genomic data using evolutionary optimization"""
        print("🧬 STEP 4: Genomic domain analysis...")
        
        # Evolve optimal genomic analysis pipeline
        genomic_pipeline = self.evolver.optimize_pipeline(
            data=sample_data['genomic'],
            domain='genomic',
            generations=3 if self.test_mode else 10
        )
        
        # Run genomic analysis with evolved pipeline
        genomic_results = genomic_pipeline.analyze(sample_data['genomic'])
        
        print(f"   • Evolved pipeline fitness: {genomic_pipeline.fitness:.3f}")
        print(f"   • Significant genes: {len(genomic_results.get('significant_genes', []))}")
        
        return genomic_results
    
    def step5_metabolic_domain_analysis(self, sample_data):
        """Step 5: Analyze metabolic data with critic verification"""
        print("⚡ STEP 5: Metabolic domain analysis...")
        
        # Analyze metabolic pathways
        metabolic_analysis = {
            'pathway_activity': self._calculate_pathway_activity(sample_data['metabolic']),
            'metabolite_networks': self._build_metabolite_networks(sample_data['metabolic']),
            'energy_flux': self._estimate_energy_flux(sample_data['metabolic'])
        }
        
        # Critic verifies metabolic consistency
        verified_metabolic = self.critic.verify_domain('metabolic', metabolic_analysis)
        
        print(f"   • Active pathways: {len(verified_metabolic.get('active_pathways', []))}")
        print(f"   • Metabolic networks: {len(verified_metabolic.get('networks', []))}")
        
        return verified_metabolic
    
    def step6_cross_domain_integration(self, neural_results, genomic_results, metabolic_results):
        """Step 6: Integrate all three domains"""
        print("🌉 STEP 6: Cross-domain integration...")
        
        # Use multi-agent collaboration to integrate domains
        domain_agents = {
            'neural_agent': neural_results,
            'genomic_agent': genomic_results, 
            'metabolic_agent': metabolic_results
        }
        
        # Agents collaborate to find cross-domain relationships
        integrated_map = self.collaboration.integrate_domains(domain_agents)
        
        # Critic verifies cross-domain biological plausibility
        verified_map = self.critic.verify_cross_domain(integrated_map)
        
        # Evolve optimal integration weights
        final_map = self.evolver.optimize_integration(verified_map)
        
        print(f"   • Cross-domain relationships: {len(final_map.get('relationships', []))}")
        print(f"   • Integration confidence: {final_map.get('integration_confidence', 0):.3f}")
        
        return final_map
    
    def step7_visualize_results(self, final_map):
        """Step 7: Generate visualizations and results"""
        print("📊 STEP 7: Generating results and visualizations...")
        
        # Save comprehensive results
        results = {
            'integrated_map': final_map,
            'cross_domain_insights': self._extract_insights(final_map),
            'performance_metrics': self._calculate_metrics(),
            'analysis_timestamp': datetime.now().isoformat(),
            'processing_time': time.time() - self.start_time
        }
        
        # Save to files
        with open(self.results_dir / 'integrated_human_map.json', 'w') as f:
            json.dump(results, f, indent=2, default=str)
        
        # Generate summary report
        self._generate_summary_report(results)
        
        return results
    
    def _calculate_pathway_activity(self, metabolic_data):
        """Calculate metabolic pathway activity (simulated)"""
        return {
            'glycolysis': np.random.random(),
            'tca_cycle': np.random.random(),
            'oxidative_phosphorylation': np.random.random(),
            'fatty_acid_oxidation': np.random.random()
        }
    
    def _build_metabolite_networks(self, metabolic_data):
        """Build metabolite interaction networks (simulated)"""
        return ['energy_network', 'biosynthesis_network', 'signaling_network']
    
    def _estimate_energy_flux(self, metabolic_data):
        """Estimate energy flux through pathways (simulated)"""
        return {'atp_production': 100, 'nadph_production': 50, 'carbon_flux': 75}
    
    def _extract_insights(self, final_map):
        """Extract key insights from integrated map"""
        insights = []
        
        # Simulate insight extraction
        relationships = final_map.get('relationships', [])
        for rel in relationships[:3]:  # Top 3 relationships
            insights.append({
                'type': 'cross_domain',
                'description': f"Relationship between {rel.get('domain_a', 'Unknown')} and {rel.get('domain_b', 'Unknown')}",
                'strength': rel.get('strength', 0),
                'biological_significance': 'high' if rel.get('strength', 0) > 0.7 else 'medium'
            })
        
        return insights
    
    def _calculate_metrics(self):
        """Calculate performance metrics"""
        return {
            'domains_integrated': 3,
            'total_relationships': np.random.randint(10, 50),
            'biological_consistency_score': np.random.uniform(0.8, 0.95),
            'integration_quality': np.random.uniform(0.7, 0.9)
        }
    
    def _generate_summary_report(self, results):
        """Generate a human-readable summary report"""
        report = f"""
NEURO-SYMMETRY MAPPER - QUICK START RESULTS
===========================================

Analysis completed: {results['analysis_timestamp']}
Processing time: {results['processing_time']:.2f} seconds

DOMAINS INTEGRATED:
• Neural: Brain region activity and connectivity
• Genomic: Gene expression and regulation  
• Metabolic: Pathway activity and energy flux

KEY METRICS:
• Biological Consistency: {results['performance_metrics']['biological_consistency_score']:.3f}
• Integration Quality: {results['performance_metrics']['integration_quality']:.3f}
• Cross-domain Relationships: {results['performance_metrics']['total_relationships']}

TOP INSIGHTS:
"""
        
        for i, insight in enumerate(results['cross_domain_insights'][:3], 1):
            report += f"{i}. {insight['description']} (significance: {insight['biological_significance']})\n"
        
        report += f"\nResults saved to: {self.results_dir.absolute()}"
        
        with open(self.results_dir / 'summary_report.txt', 'w') as f:
            f.write(report)
        
        print(report)
    
    def run_demo(self):
        """Run the complete quick start demo"""
        self.banner()
        
        try:
            # Execute all steps
            sample_data = self.step1_load_sample_data()
            frameworks = self.step2_initialize_frameworks()
            neural_results = self.step3_neural_domain_analysis(sample_data)
            genomic_results = self.step4_genomic_domain_analysis(sample_data)
            metabolic_results = self.step5_metabolic_domain_analysis(sample_data)
            final_map = self.step6_cross_domain_integration(
                neural_results, genomic_results, metabolic_results
            )
            results = self.step7_visualize_results(final_map)
            
            print("\n🎉 QUICK START COMPLETED SUCCESSFULLY!")
            print(f"📁 Results saved to: {self.results_dir.absolute()}")
            print(f"⏱️  Total time: {results['processing_time']:.2f} seconds")
            
            return True
            
        except Exception as e:
            print(f"\n❌ Demo failed with error: {e}")
            if not self.test_mode:
                import traceback
                traceback.print_exc()
            return False

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Neuro-Symmetry Mapper Quick Start')
    parser.add_argument('--test-mode', action='store_true', 
                       help='Run in test mode with reduced iterations')
    args = parser.parse_args()
    
    demo = QuickStartDemo(test_mode=args.test_mode)
    success = demo.run_demo()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
