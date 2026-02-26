from pathlib import Path
import pandas as pd

# Direct path to CSV (same folder as script)
CSV = Path('data/user_data.csv')

if not CSV.exists():
    raise FileNotFoundError(f"{CSV} does not exist!")

print("Using:", CSV.name)

# Load first 5000 rows to inspect
df = pd.read_csv(CSV, nrows=5000)
print("Columns:", df.columns.tolist())
print(df.dtypes)
print(df.head())

# Example cleaning
df = df.drop_duplicates().reset_index(drop=True)

# Save a small sample for GitHub push
sample = df.sample(frac=0.01, random_state=42)
sample.to_csv("sample_cleaned_events.csv", index=False)
print("Sample cleaned CSV saved: sample_cleaned_events.csv")


