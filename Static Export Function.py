def export_static_plot(fig, filename_base, width=1000, height=400):
    """
    Export plot to static formats (PNG, PDF, SVG)
    
    Requires: pip install kaleido
    """
    try:
        import plotly.io as pio
        
        for fmt in ['png', 'pdf', 'svg']:
            output_file = f"{filename_base}.{fmt}"
            pio.write_image(fig, output_file, width=width, height=height, scale=2)
            print(f"Static plot saved: {output_file}")
            
    except ImportError:
        print("Kaleido not installed. Run: pip install kaleido")
    except Exception as e:
        print(f"Error exporting static plot: {e}")
