def generate_protein_domain_plot(fasta_file, output_html="protein_domains.html", 
                               output_static=None, min_domain_length=0, 
                               group_similar=True, figure_width=1000):
    """
    Enhanced protein domain plot generation with filtering and static exports
    """
    # Parse FASTA and get protein length
    from Bio import SeqIO
    record = SeqIO.read(fasta_file, "fasta")
    protein_length = len(record.seq)
    
    # Run InterProScan
    interpro_output = run_interproscan(fasta_file)
    
    # Parse domains
    domains_df = parse_interpro_output(interpro_output)
    
    print(f"Found {len(domains_df)} domains in protein of length {protein_length} aa")
    
    # Apply domain filtering
    if min_domain_length > 0 or group_similar:
        domains_df = filter_domains(domains_df, min_domain_length, group_similar)
        print(f"After filtering: {len(domains_df)} domains")
    
    # Create the plot
    fig = create_protein_domain_plot(domains_df, protein_length)
    
    # Update figure size
    fig.update_layout(width=figure_width)
    
    # Save interactive HTML
    fig.write_html(output_html)
    print(f"Interactive plot saved: {output_html}")
    
    # Export static formats if requested
    if output_static:
        export_static_plot(fig, output_static, width=figure_width, height=400)
    
    # Save domain data to CSV
    csv_file = output_html.replace('.html', '_domains.csv')
    domains_df.to_csv(csv_file, index=False)
    print(f"Domain data saved: {csv_file}")
    
    return fig, domains_df
