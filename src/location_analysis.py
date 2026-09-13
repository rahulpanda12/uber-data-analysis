import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/processed/uber_cleaned.csv")

# Start and Stop Location Analysis
start_counts = df["START"].value_counts()

stop_counts = df["STOP"].value_counts()

print("Top 10 Start Locations:")
print(start_counts.head(10))

print("\nTop 10 Stop Locations:")
print(stop_counts.head(10))

# Locations common to both start and stop
location_summary = pd.DataFrame({
    "Start_Count": start_counts,
    "Stop_Count": stop_counts
}).fillna(0)

location_summary["Total_Activity"] = (
    location_summary["Start_Count"] +
    location_summary["Stop_Count"]
)

location_summary = location_summary.sort_values(
    "Total_Activity",
    ascending=False
)

print("\nTop 10 Locations by Total Activity:")
print(location_summary.head(10))

# Most Common Routes
known_routes = df[
    (df["START"] != "Unknown Location") &
    (df["STOP"] != "Unknown Location")
]

route_counts = (
    known_routes.groupby(["START", "STOP"])
    .size()
    .sort_values(ascending=False)
)

print("\nTop 10 Most Common Known Routes:")
print(route_counts.head(10))