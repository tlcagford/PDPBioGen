#!/usr/bin/env python3
"""
PDPBioGen Real Data Validation Runner
Downloads real datasets and runs scientific validation
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from real_data_validator import RealDataValidator

def main():
    print("🔬 PDPBioGen Scientific Validation")
    print("Downloading real datasets and running analysis...")
    
    validator = RealDataValidator()
    datasets, analysis = validator.run_complete_validation()
    
    print("\n🎉 Validation complete! Check generated files:")
    print("   - pdpbiogen_validation_report.json")
    print("   - pdpbiogen_validation_plots.png")
    print("   - pdpbiogen_statistical_summary.json")
    print("   - pdpbiogen_scientific_analysis.md")

if __name__ == "__main__":
    main()
