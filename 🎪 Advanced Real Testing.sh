# 1. Conserved protein (should find many homologs)
echo ">Cytochrome_C_Human
MGDVEKGKKIFIMKCSQCHTVEKGGKHKTGPNLHGLFGRKTGQAPGYSYTAANKNKGIIW
GEDTLMEYLENPKKYIPGTKMIFVGIKKKEERADLIAYLKKATNE" > cytochrome_c.fasta

# 2. Rapidly evolving protein (fewer homologs)  
echo ">Flu_HA_Human
MVLILLCALAAADADTICIGYHANNSTDTVDTVLEKNVTVTHSVNLLEDKHNGKLCKLRGV
APLHLGKCNIAGWILGNPECESLSTASSWSYIVETSSSDNGTCYPGDFIDYEELREQLSSV
SSFERFEIFPKTSSWPNHDSNKGVTAACPHAGAKSFYKNLIWLVKKGNSYPKLSKSYINDK
GKEVLVLWGVHHPPNIGQRAILG" > influenza_ha.fasta

# Run comparison
poetry run python -m pdpbiogen blast_to_align --sequence cytochrome_c.fasta --output cyto_aln.fasta
poetry run python -m pdpbiogen blast_to_align --sequence influenza_ha.fasta --output flu_aln.fasta