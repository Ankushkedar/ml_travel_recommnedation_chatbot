import pandas as pd
 
def load_data(path="data/pune_destinations.csv"):
    return pd.read_csv(path)
 
def get_filtered_data(df, category=None, subtype=None):
    filtered = df
    if category:
        filtered = filtered[filtered['category'] == category]
    if subtype:
        filtered = filtered[filtered['subtype'] == subtype]
    return filtered
