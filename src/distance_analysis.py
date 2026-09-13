import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/processed/uber_cleaned.csv")

# Distance Analysis
print("Distance Statistics:")
print(df["MILES"].describe().round(2))

# Distance Type Analysis
distance_counts = df["DISTANCE_TYPE"].value_counts()

distance_percentage = (
    df["DISTANCE_TYPE"].value_counts(normalize=True) * 100
)

print("\nTrips by Distance Type:")
print(distance_counts)

print("\nPercentage by Distance Type:")
print(distance_percentage.round(2))

# Longest Trips
longest_trips = df.nlargest(10, "MILES")[
    ["START_DATE", "CATEGORY", "START", "STOP", "MILES", "PURPOSE"]
]

print("\nTop 10 Longest Trips:")
print(longest_trips)

# Median vs Mean
mean_distance = df["MILES"].mean()
median_distance = df["MILES"].median()

print("\nMean Distance:", round(mean_distance, 2))
print("Median Distance:", round(median_distance, 2))

# Outlier Threshold
Q1 = df["MILES"].quantile(0.25)
Q3 = df["MILES"].quantile(0.75)

IQR = Q3 - Q1

upper_limit = Q3 + 1.5 * IQR

outliers = df[df["MILES"] > upper_limit]

print("\nOutlier Threshold:", round(upper_limit, 2))
print("Number of Outliers:", len(outliers))
print("Total Miles from Outliers:", round(outliers["MILES"].sum(), 2))

import matplotlib.pyplot as plt

# Distance Distribution
plt.figure(figsize=(8, 5))

plt.boxplot(df["MILES"])

plt.title("Distribution of Trip Distances")
plt.ylabel("Miles")

plt.tight_layout()

plt.savefig("reports/distance_boxplot.png")

plt.show()

plt.close()