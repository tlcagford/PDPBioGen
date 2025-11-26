#!/usr/bin/env python3
"""
Test script for enhanced PDPBioGen features
"""

import os
import subprocess
from pdpbiogen import generate_protein_domain_plot


def test_enhanced_features():
    """Test all new features"""
    test_fasta = "examples/example.fasta"
    
    if not os.path.exists(test_fasta):
        print("❌ Test FASTA file not found")
        return
    
    print("🧪 Testing Enhanced PDPBioGen Features")
    print("=" * 50)
    
    # Test 1: Basic functionality
    print("\n1. Testing basic functionality...")
    try:
        fig, domains = generate_protein_domain_plot(test_fasta)
        print("✅ Basic functionality working")
    except Exception as e:
        print(f"❌ Basic test failed: {e}")
        return
    
    # Test 2: Static exports
    print("\n2. Testing static exports...")
    try:
        fig, domains = generate_protein_domain_plot(
            test_fasta,
            output_html="test_basic.html",
            output_static="test_static"
        )
        static_files = ["test_static.png", "test_static.pdf", "test_static.svg"]
        for f in static_files:
            if os.path.exists(f):
                print(f"✅ {f} created")
            else:
                print(f"❌ {f} missing")
    except Exception as e:
        print(f"❌ Static export test failed: {e}")
    
    # Test 3: Domain filtering
    print("\n3. Testing domain filtering...")
    try:
        fig, domains = generate_protein_domain_plot(
            test_fasta,
            output_html="test_filtered.html",
            min_domain_length=10
        )
        print("✅ Domain filtering working")
    except Exception as e:
        print(f"❌ Filtering test failed: {e}")
    
    # Test 4: Custom dimensions
    print("\n4. Testing custom dimensions...")
    try:
        fig, domains = generate_protein_domain_plot(
            test_fasta,
            output_html="test_custom.html",
            width=800,
            height=500
        )
        print("✅ Custom dimensions working")
    except Exception as e:
        print(f"❌ Custom dimensions test failed: {e}")
    
    # Test 5: Command line interface
    print("\n5. Testing command line interface...")
    try:
        result = subprocess.run([
            "python", "pdpbiogen.py", test_fasta,
            "--output", "test_cli.html",
            "--static", "test_cli",
            "--min-length", "20",
            "--width", "1200"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ CLI working")
        else:
            print(f"❌ CLI failed: {result.stderr}")
    except Exception as e:
        print(f"❌ CLI test failed: {e}")
    
    print("\n" + "=" * 50)
    print("🎯 Testing completed!")


if __name__ == "__main__":
    test_enhanced_features()