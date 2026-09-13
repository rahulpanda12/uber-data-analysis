import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/processed/uber_cleaned.csv")

# Time-Based Analysis
# Trips by hour
trips_by_hour = df["HOUR"].value_counts().sort_index()

print("Trips by Hour:")
print(trips_by_hour)

# Trips by Day of Week
trips_by_day = df["DAY_OF_WEEK"].value_counts()

print("\nTrips by Day of Week:")
print(trips_by_day)

# Day of Week + Hour Analysis
day_hour = pd.crosstab(
    df["DAY_OF_WEEK"],
    df["HOUR"]
)

pd.set_option("display.max_columns", None)

print("\nTrips by Day and Hour:")
print(day_hour)

# Average Distance by Hour
avg_distance_by_hour = df.groupby("HOUR")["MILES"].mean()

print("\nAverage Distance by Hour:")
print(avg_distance_by_hour.round(2))

# Average Distance by Hour Chart
plt.figure(figsize=(8, 5))

plt.plot(
    avg_distance_by_hour.index,
    avg_distance_by_hour.values,
    marker="o"
)

plt.title("Average Trip Distance by Hour")
plt.xlabel("Hour")
plt.ylabel("Average Distance (Miles)")

plt.tight_layout()

plt.savefig("reports/avg_distance_by_hour.png")

plt.show()

plt.close()