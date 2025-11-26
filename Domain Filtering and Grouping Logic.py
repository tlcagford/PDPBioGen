def _filter_and_group_domains(domains_df, protein_length, **kwargs):
    """Apply filtering and grouping to domain data"""
    
    filtered_df = domains_df.copy()
    
    # Length-based filtering
    if kwargs.get('min_domain_length'):
        filtered_df = filtered_df[
            filtered_df['end'] - filtered_df['start'] + 1 >= kwargs['min_domain_length']
        ]
    
    if kwargs.get('max_domain_length'):
        filtered_df = filtered_df[
            filtered_df['end'] - filtered_df['start'] + 1 <= kwargs['max_domain_length']
        ]
    
    # Group similar consecutive domains
    if kwargs.get('group_similar', True) and len(filtered_df) > 1:
        filtered_df = filtered_df.sort_values('start')
        grouped_domains = []
        
        current_group = [filtered_df.iloc[0]]
        
        for i in range(1, len(filtered_df)):
            current_domain = filtered_df.iloc[i]
            last_domain = current_group[-1]
            
            # Group if same domain type and close together (within 50aa)
            if (current_domain['domain_name'] == last_domain['domain_name'] and
                current_domain['start'] - last_domain['end'] <= 50):
                current_group.append(current_domain)
            else:
                grouped_domains.append(current_group)
                current_group = [current_domain]
        
        grouped_domains.append(current_group)
        
        # Create new dataframe with grouped domains
        new_rows = []
        for group in grouped_domains:
            if len(group) == 1:
                new_rows.append(group[0])
            else:
                # Create a merged domain entry
                first = group[0]
                last = group[-1]
                merged_row = first.copy()
                merged_row['end'] = last['end']
                merged_row['domain_name'] = f"{first['domain_name']} (x{len(group)})"
                new_rows.append(merged_row)
        
        filtered_df = pd.DataFrame(new_rows)
    
    # Limit number of domains for very large proteins
    max_display = kwargs.get('max_domains_display', 50)
    if len(filtered_df) > max_display:
        print(f"Warning: Limiting display to {max_display} of {len(filtered_df)} domains")
        # Keep largest domains by length
        filtered_df['domain_length'] = filtered_df['end'] - filtered_df['start'] + 1
        filtered_df = filtered_df.nlargest(max_display, 'domain_length')
        filtered_df = filtered_df.drop('domain_length', axis=1)
    
    return filtered_df
