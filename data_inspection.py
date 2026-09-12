import pandas as pd

df = pd.read_csv("data/raw/UberDataset.csv")

print(df.head())
print(df.shape)
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nBasic Statistics:")
print(df.describe())

print("\nCATEGORY values:")
print(df["CATEGORY"].value_counts(dropna=False))

print("\nPURPOSE values:")
print(df["PURPOSE"].value_counts(dropna=False))

print("\nSTART locations:")
print(df["START"].value_counts().head(15))

print("\nSTOP locations:")
print(df["STOP"].value_counts().head(15))

print("\nRows with missing values:")
print(df[df.isnull().any(axis=1)])

print("\nPotential extreme mileage:")
print(df.nlargest(10, "MILES")[["START_DATE", "START", "STOP", "MILES", "PURPOSE"]])

print("\nDuplicate row:")
print(df[df.duplicated(keep=False)])

print("\n--- SUSPICIOUS ROWS ---")

# 1. Totals row
print("\nTotals row:")
print(df[df["START_DATE"] == "Totals"])

# 2. Row with missing CATEGORY/START/STOP
print("\nRow with missing CATEGORY/START/STOP:")
print(df[df["CATEGORY"].isna() | df["START"].isna() | df["STOP"].isna()])

# 3. Largest legitimate-looking trips
print("\nTop 10 mileage records excluding Totals:")
print(
    df[df["START_DATE"] != "Totals"]
    .nlargest(10, "MILES")[["START_DATE", "START", "STOP", "MILES", "PURPOSE"]]
)

# 4. Encoding issue
print("\nLocations containing '?':")
print("START:")
print(df[df["START"].astype(str).str.contains(r"\?", regex=True)]["START"].value_counts())

print("STOP:")
print(df[df["STOP"].astype(str).str.contains(r"\?", regex=True)]["STOP"].value_counts())

print("\n--- DATE VALUES ---")

print("\nFirst 20 START_DATE values:")
print(df["START_DATE"].head(20).to_string(index=False))

print("\nLast 20 START_DATE values:")
print(df["START_DATE"].tail(20).to_string(index=False))

print("\nUnique START_DATE formats/examples:")
print(df["START_DATE"].dropna().astype(str).head(50).to_string(index=False))