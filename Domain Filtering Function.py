def filter_domains(domains_df, min_domain_length=0, group_similar_domains=True):
    """
    Filter domains for better visualization of large proteins
    
    Args:
        min_domain_length: Minimum domain length to include
        group_similar_domains: Group identical consecutive domains
    """
    if min_domain_length > 0:
        domains_df = domains_df[
            (domains_df['end'] - domains_df['start']) >= min_domain_length
        ].copy()
    
    if group_similar_domains and len(domains_df) > 1:
        domains_df = domains_df.sort_values('start').reset_index(drop=True)
        grouped_domains = []
        i = 0
        
        while i < len(domains_df):
            current = domains_df.iloc[i]
            count = 1
            
            # Count consecutive identical domains
            while (i + count < len(domains_df) and
                   domains_df.iloc[i + count]['domain_name'] == current['domain_name'] and
                   domains_df.iloc[i + count]['start'] - domains_df.iloc[i + count - 1]['end'] <= 20):
                count += 1
            
            if count > 1:
                # Create grouped domain
                grouped = current.copy()
                grouped['end'] = domains_df.iloc[i + count - 1]['end']
                grouped['domain_name'] = f"{current['domain_name']} (x{count})"
                grouped_domains.append(grouped)
            else:
                grouped_domains.append(current)
            
            i += count
        
        domains_df = pd.DataFrame(grouped_domains)
    
    return domains_df
