#!/usr/bin/env python3
"""
Validation test suite for PDPBioGen
"""

import pandas as pd
import json
import os
import sys

def test_validation_files_exist():
    """Test that all validation files are present"""
    required_files = [
        'validation/results/ibd_validation_results.tsv',
        'validation/results/t2d_validation_results.tsv', 
        'validation/benchmarks/performance_metrics.json',
        'validation/benchmarks/tool_comparison.tsv'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing validation files: {missing_files}")
        return False
    else:
        print("✅ All validation files present")
        return True

def test_ibd_validation_results():
    """Test IBD validation results format and content"""
    try:
        df = pd.read_csv('validation/results/ibd_validation_results.tsv', sep='\t')
        
        # Check required columns
        required_cols = ['rank', 'gene', 'score', 'known_gene', 'evidence_source']
        missing_cols = [col for col in required_cols if col not in df.columns]
        
        if missing_cols:
            print(f"❌ Missing columns in IBD results: {missing_cols}")
            return False
        
        # Check known genes are recovered
        known_genes = df[df['known_gene'] == 'Established']
        if len(known_genes) < 10:
            print(f"❌ Insufficient known genes recovered: {len(known_genes)}")
            return False
            
        # Check scores are reasonable
        if df['score'].max() > 1.0 or df['score'].min() < 0:
            print("❌ Scores outside expected range (0-1)")
            return False
            
        print(f"✅ IBD validation: {len(known_genes)} known genes recovered")
        return True
        
    except Exception as e:
        print(f"❌ Error reading IBD results: {e}")
        return False

def test_performance_metrics():
    """Test performance metrics format"""
    try:
        with open('validation/benchmarks/performance_metrics.json', 'r') as f:
            metrics = json.load(f)
        
        required_sections = ['validation_studies', 'runtime_benchmarks', 'hardware_used']
        missing_sections = [section for section in required_sections if section not in metrics]
        
        if missing_sections:
            print(f"❌ Missing metrics sections: {missing_sections}")
            return False
            
        # Check AUC values are reasonable
        ibd_auc = metrics['validation_studies']['IBD']['auc']
        t2d_auc = metrics['validation_studies']['Type_2_Diabetes']['auc']
        
        if ibd_auc < 0.8 or t2d_auc < 0.8:
            print(f"❌ Low AUC values: IBD={ibd_auc}, T2D={t2d_auc}")
            return False
            
        print(f"✅ Performance metrics: IBD AUC={ibd_auc}, T2D AUC={t2d_auc}")
        return True
        
    except Exception as e:
        print(f"❌ Error reading performance metrics: {e}")
        return False

def main():
    """Run all validation tests"""
    print("Running PDPBioGen validation tests...")
    print("=" * 50)
    
    tests = [
        test_validation_files_exist,
        test_ibd_validation_results, 
        test_performance_metrics
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"❌ Test {test.__name__} failed with error: {e}")
            results.append(False)
    
    passed = sum(results)
    total = len(results)
    
    print("=" * 50)
    if passed == total:
        print(f"🎉 All {passed}/{total} validation tests passed!")
        return 0
    else:
        print(f"❌ {passed}/{total} validation tests passed")
        return 1

if __name__ == "__main__":
    sys.exit(main())
