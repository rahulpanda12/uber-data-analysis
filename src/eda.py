import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/processed/uber_cleaned.csv")

# Convert START_DATE to datetime
df["START_DATE"] = pd.to_datetime(df["START_DATE"])


# =====================================
# 1. Trips by Day of Week
# =====================================

day_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

day_counts = df["DAY_OF_WEEK"].value_counts().reindex(day_order)

print("Trips by day of week:")
print(day_counts)

plt.figure(figsize=(8, 5))
day_counts.plot(kind="bar")

plt.title("Number of Uber Trips by Day")
plt.xlabel("Day of Week")
plt.ylabel("Number of Trips")
plt.xticks(rotation=45)

plt.tight_layout()

# Save chart
plt.savefig("reports/trips_by_day.png")

plt.show()
plt.close()


# =====================================
# 2. Trips by Month
# =====================================

month_counts = df["MONTH"].value_counts().sort_index()

print("\nTrips by month:")
print(month_counts)

plt.figure(figsize=(8, 5))
month_counts.plot(kind="bar")

plt.title("Number of Uber Trips by Month")
plt.xlabel("Month")
plt.ylabel("Number of Trips")

plt.tight_layout()

# Save chart
plt.savefig("reports/trips_by_month.png")

plt.show()
plt.close()


# =====================================
# 3. Trips by Hour
# =====================================

hour_counts = df["HOUR"].value_counts().sort_index()

print("\nTrips by hour:")
print(hour_counts)

plt.figure(figsize=(8, 5))
hour_counts.plot(kind="line", marker="o")

plt.title("Number of Uber Trips by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Trips")
plt.xticks(range(0, 24))

plt.grid(True)

plt.tight_layout()

# Save chart
plt.savefig("reports/trips_by_hour.png")

plt.show()
plt.close()


print("\nCharts saved successfully in the reports folder!")