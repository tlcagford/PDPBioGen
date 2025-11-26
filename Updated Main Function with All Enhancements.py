def generate_enhanced_domain_plot(
    fasta_file,
    output_html="protein_domains.html",
    output_static=None,
    # Filtering options
    min_domain_length=None,
    max_domain_length=None,
    group_similar=True,
    max_domains_display=30,
    # Customization options
    custom_colors=None,
    figure_width=1200,
    figure_height=None,  # Auto-adjust if None
    static_formats=['png', 'pdf', 'svg'],
    title="Protein Domain Architecture"
):
    """
    Enhanced protein domain visualization with filtering and multi-format output
    """
    try:
        # Parse protein sequence
        protein_sequence, protein_length = parse_fasta(fasta_file)
        
        # Run InterProScan
        interpro_results = run_interproscan(fasta_file)
        
        # Parse and filter domains
        domains_df = parse_interpro_output(interpro_results)
        
        # Apply filtering and grouping
        filtered_domains = _filter_and_group_domains(
            domains_df, 
            protein_length,
            min_domain_length=min_domain_length,
            max_domain_length=max_domain_length,
            group_similar=group_similar,
            max_domains_display=max_domains_display
        )
        
        # Auto-adjust height based on number of domains
        if figure_height is None:
            figure_height = max(400, len(filtered_domains) * 30 + 150)
        
        # Create visualization
        fig = _create_domain_plot(
            filtered_domains, 
            protein_length,
            custom_colors=custom_colors,
            width=figure_width,
            height=figure_height
        )
        
        # Update title
        fig.update_layout(title=title)
        
        # Save outputs
        fig.write_html(output_html)
        print(f"✓ Interactive plot saved: {output_html}")
        
        if output_static:
            _export_static_plots(fig, output_static, formats=static_formats)
        
        # Save filtered domain data
        csv_output = output_html.replace('.html', '_domains.csv')
        filtered_domains.to_csv(csv_output, index=False)
        print(f"✓ Domain data saved: {csv_output}")
        
        print(f"✓ Processing complete: {len(filtered_domains)} domains visualized")
        return fig, filtered_domains
        
    except Exception as e:
        print(f"Error in enhanced processing: {e}")
        raise
