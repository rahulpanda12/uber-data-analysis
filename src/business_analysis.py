import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/processed/uber_cleaned.csv")

# Business vs Personal Trips

trip_count = df["CATEGORY"].value_counts()

trip_percentage = df["CATEGORY"].value_counts(normalize=True) * 100

miles_analysis = df.groupby("CATEGORY")["MILES"].agg(
    ["count", "sum", "mean"]
)

print("Trips by Category:")
print(trip_count)

print("\nPercentage of Trips:")
print(trip_percentage.round(2))

print("\nMiles Analysis:")
print(miles_analysis.round(2))