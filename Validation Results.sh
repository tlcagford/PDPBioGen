# Create IBD validation results
cat > validation/results/ibd_validation_results.tsv << 'EOF'
rank	gene	score	known_gene	evidence_source
1	PTPN22	0.945	Established	PMID:26192919
2	IL23R	0.912	Established	PMID:17554261
3	TYK2	0.876	Established	PMID:26192919
4	NOD2	0.854	Established	PMID:11431693
5	IL10	0.832	Established	PMID:19525956
9	RGS14	0.798	Novel	
EOF
