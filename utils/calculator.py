# utils/calculator.py
import pandas as pd

# Load emission factor table
df = pd.read_csv("data/emission_factors.csv")

def calculate_emission(category, activity, value):
    row = df[(df['category'] == category) & (df['activity'] == activity)]
    if not row.empty:
        factor = row.iloc[0]['emission_factor']
        return round(value * factor, 3)
    else:
        return None
