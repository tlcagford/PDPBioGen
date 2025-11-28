cd PDPBioGen

# Create and run verification script
cat > verify_completeness.sh << 'EOF'
#!/bin/bash
echo "=================================================="
echo "🔍 PDPBioGen COMPLETENESS VERIFICATION"
echo "=================================================="
echo ""

# Function to check items
check_item() {
    if [ -e "$1" ]; then
        echo "✅ $1"
        return 0
    else
        echo "❌ $1 - MISSING"
        return 1
    fi
}

echo "1. CORE PIPELINE FILES:"
check_item "pdpbiogen.nf"
check_item "environment.yml" 
check_item "Dockerfile"
check_item ".nextflow.config"
check_item "LICENSE"
check_item "README.md"
check_item "CITATION.cff"
check_item "docker/Dockerfile"
check_item ".dockerignore"

echo ""
echo "2. VALIDATION STRUCTURE:"
check_item "validation/"
check_item "validation/results/"
check_item "validation/benchmarks/"
check_item "validation/datasets/"
check_item "validation/results/ibd_validation_results.tsv"
check_item "validation/benchmarks/performance_metrics.json"

echo ""
echo "3. EXAMPLES STRUCTURE:"
check_item "examples/"
check_item "examples/ibd_minimal_gwas.tsv"

echo ""
echo "4. TESTING STRUCTURE:"
check_item "test/"
check_item "test/test_validation.py"

echo ""
echo "5. DOCUMENTATION STRUCTURE:"
check_item "docs/"
check_item "docs/quickstart.md"

echo ""
echo "6. SCRIPTS STRUCTURE:"
check_item "bin/"
check_item "bin/setup_environment.sh"

echo ""
echo "7. GITHUB STRUCTURE:"
check_item ".github/"
check_item ".github/FUNDING.yml"

echo ""
echo "=================================================="

# Count missing items
missing=$(grep -c "❌" verify_completeness.sh) || true
total=$(grep -c "check_item" verify_completeness.sh) || true
present=$((total - missing))

echo "SUMMARY: $present/$total items present"
echo "=================================================="

if [ $missing -eq 0 ]; then
    echo "🎉 ALL FILES PRESENT - READY TO PUSH!"
else
    echo "🚨 $missing FILES MISSING - NEED TO CREATE"
fi
EOF

chmod +x verify_completeness.sh
./verify_completeness.sh
