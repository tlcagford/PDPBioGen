def _export_static_plots(fig, base_filename, formats=['png', 'pdf', 'svg']):
    """Export plot in multiple static formats"""
    
    import plotly.io as pio
    
    for format in formats:
        filename = f"{base_filename}.{format}"
        try:
            if format == 'pdf':
                pio.write_image(fig, filename, format='pdf', width=1200, height=600)
            elif format == 'png':
                pio.write_image(fig, filename, format='png', width=1200, height=600, scale=2)
            elif format == 'svg':
                pio.write_image(fig, filename, format='svg')
            print(f"Static plot saved: {filename}")
        except Exception as e:
            print(f"Could not export {format}: {e}")

# Add to main function
def generate_protein_domain_plot(fasta_file, output_html="protein_domains.html", 
                               output_static=None, **kwargs):
    # ... existing code ...
    
    # Generate the interactive plot
    fig = _create_domain_plot(filtered_domains, protein_length, 
                            custom_colors=kwargs.get('custom_colors'),
                            width=kwargs.get('figure_width', 1200),
                            height=kwargs.get('figure_height', 400))
    
    # Save interactive HTML
    fig.write_html(output_html)
    print(f"Interactive plot saved: {output_html}")
    
    # Save static formats if requested
    if output_static:
        _export_static_plots(fig, output_static, 
                           formats=kwargs.get('static_formats', ['png', 'pdf', 'svg']))
