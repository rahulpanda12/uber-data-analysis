import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/processed/uber_cleaned.csv")

# Trips by Purpose
purpose_counts = df["PURPOSE"].value_counts()

purpose_percentage = df["PURPOSE"].value_counts(normalize=True) * 100

purpose_miles = df.groupby("PURPOSE")["MILES"].agg(
    ["count", "sum", "mean"]
).sort_values("count", ascending=False)

print("Trips by Purpose:")
print(purpose_counts)

print("\nPercentage of Trips:")
print(purpose_percentage.round(2))

print("\nMiles by Purpose:")
print(purpose_miles.round(2))