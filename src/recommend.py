import pandas as pd

def load_data(path="data/pune_destinations.csv"):
    return pd.read_csv(path)

def recommend_destinations(df, category=None, subtype=None):
    filtered = df.copy()
    if category:
        filtered = filtered[filtered['category'].str.lower() == category.lower()]
    if subtype:
        filtered = filtered[filtered['subtype'].str.lower() == subtype.lower()]
    return filtered[['destination','category','notes']]
 
