# Add these new parameters to the main function
def generate_protein_domain_plot(
    fasta_file,
    output_html="protein_domains.html",
    output_static=None,  # New: for static formats
    min_domain_length=None,
    max_domain_length=None,
    group_similar=True,
    max_domains_display=20,
    custom_colors=None,
    figure_width=1200,
    figure_height=400
):
    """
    Enhanced version with filtering and customization options
    
    Args:
        min_domain_length: Filter out domains shorter than this
        max_domain_length: Filter out domains longer than this  
        group_similar: Group identical consecutive domains
        max_domains_display: Limit number of domains shown for large proteins
        custom_colors: Dict of {domain_name: color} for custom coloring
        figure_width/height: Customizable dimensions
    """
