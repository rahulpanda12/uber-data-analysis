import pandas as pd
import numpy as np

# Load raw dataset
df = pd.read_csv("data/raw/UberDataset.csv")

print("Original shape:", df.shape)

# 1. Remove the summary/total row
df = df[df["START_DATE"] != "Totals"].copy()

# 2. Remove exact duplicate rows
df = df.drop_duplicates()

# 3. Convert mixed date formats to datetime
df["START_DATE"] = pd.to_datetime(
    df["START_DATE"],
    format="mixed",
    errors="coerce"
)

df["END_DATE"] = pd.to_datetime(
    df["END_DATE"],
    format="mixed",
    errors="coerce"
)

# 4. Fix location encoding issues
df["START"] = df["START"].replace({
    "Kar?chi": "Karachi",
    "R?walpindi": "Rawalpindi"
})

df["STOP"] = df["STOP"].replace({
    "Kar?chi": "Karachi",
    "R?walpindi": "Rawalpindi"
})

# 5. Handle missing PURPOSE
df["PURPOSE"] = df["PURPOSE"].fillna("Unknown")

# 6. Remove rows where essential trip information is missing
df = df.dropna(subset=["CATEGORY", "START", "STOP"])

# 7. Create useful time features
df["MONTH"] = df["START_DATE"].dt.month
df["DAY_OF_WEEK"] = df["START_DATE"].dt.day_name()
df["HOUR"] = df["START_DATE"].dt.hour

# 8. Classify trips by distance using NumPy
df["DISTANCE_TYPE"] = np.where(
    df["MILES"] <= 5,
    "Short",
    np.where(df["MILES"] <= 15, "Medium", "Long")
)

# 9. Save cleaned dataset
df.to_csv("data/processed/uber_cleaned.csv", index=False)

print("Cleaned shape:", df.shape)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nFirst 5 cleaned rows:")
print(df.head())

print("\nCleaning completed!")