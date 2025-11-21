#!/usr/bin/env python3
"""
Quick Biological Validation for PDPBioGen
Tests core functionality with real biological scenarios
"""

import subprocess
import os
from pathlib import Path

def test_installation():
    """Test basic installation and dependencies"""
    try:
        result = subprocess.run([
            'poetry', 'run', 'python', '-m', 'pdpbiogen', '--help'
        ], capture_output=True, text=True, cwd='PDPBioGen')
        return "blast_to_align" in result.stdout
    except:
        return False

def create_test_sequence():
    """Create a test hemoglobin sequence"""
    test_fasta = """
>HBA_HUMAN_test
MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHG
KKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTP
AVHASLDKFLASVSTVLTSKYR
"""
    with open('test_hemoglobin.fasta', 'w') as f:
        f.write(test_fasta.strip())
    return 'test_hemoglobin.fasta'

def run_blast_to_align():
    """Test the core biological workflow"""
    cmd = [
        'poetry', 'run', 'python', '-m', 'pdpbiogen',
        'blast_to_align',
        '--sequence', 'test_hemoglobin.fasta',
        '--database', 'swissprot', 
        '--output', 'test_alignment.fasta',
        '--aligner', 'mafft',
        '--max-sequences', '10'  # Keep it small for testing
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd='PDPBioGen')
        return result.returncode == 0
    except:
        return False

def main():
    print("🧬 PDPBioGen Biological Quick Test")
    print("=" * 40)
    
    # Test 1: Installation
    print("1. Testing installation...", end=" ")
    if test_installation():
        print("✅ PASS")
    else:
        print("❌ FAIL - Check poetry installation")
        return
    
    # Test 2: Create test data
    print("2. Creating test sequence...", end=" ")
    test_file = create_test_sequence()
    print(f"✅ Created {test_file}")
    
    # Test 3: Run biological workflow
    print("3. Running BLAST-to-Alignment...", end=" ")
    if run_blast_to_align():
        print("✅ PASS")
        
        # Check output
        if os.path.exists('PDPBioGen/test_alignment.fasta'):
            with open('PDPBioGen/test_alignment.fasta', 'r') as f:
                lines = f.readlines()
                seq_count = sum(1 for line in lines if line.startswith('>'))
            print(f"   Generated alignment with {seq_count} sequences")
    else:
        print("❌ FAIL - Check BLAST/MAFFT installation")

if __name__ == "__main__":
    main()