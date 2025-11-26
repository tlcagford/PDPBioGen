# Example 1: Basic usage with static outputs
generate_enhanced_domain_plot(
    "protein.fasta",
    output_html="my_protein_domains.html",
    output_static="my_protein_domains",
    static_formats=['png', 'pdf']
)

# Example 2: Large protein with filtering
generate_enhanced_domain_plot(
    "titin.fasta",
    output_html="titin_domains.html",
    min_domain_length=50,           # Filter small domains
    max_domains_display=25,         # Limit display
    group_similar=True,             # Group repeated domains
    figure_width=1400,              # Wider for large protein
    title="Titin Domain Architecture (Top 25 Domains)"
)

# Example 3: Custom colors and dimensions
custom_colors = {
    "Kinase": "#ff0000",
    "SH2": "#00ff00", 
    "SH3": "#0000ff"
}

generate_enhanced_domain_plot(
    "receptor.fasta",
    output_html="custom_receptor.html",
    output_static="receptor_domains",
    custom_colors=custom_colors,
    figure_width=1000,
    figure_height=500,
    static_formats=['pdf', 'svg']  # High-quality for publication
)
