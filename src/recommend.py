import pandas as pd

def load_data(path="data/destinations.csv"):
    return pd.read_csv(path)

def recommend_destinations(df, continent=None, weather=None, budget=None, interest=None):
    filtered = df.copy()

    if continent:
        filtered = filtered[filtered['continent'].str.lower() == continent.lower()]
    if weather:
        filtered = filtered[filtered['weather'].str.lower() == weather.lower()]
    if budget:
        filtered = filtered[filtered['budget'].str.lower() == budget.lower()]
    if interest:
        filtered = filtered[filtered['activities'].str.contains(interest, case=False)]

    return filtered[['destination', 'activities']].reset_index(drop=True)
 
