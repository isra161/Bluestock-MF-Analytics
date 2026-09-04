import pandas as pd
from pathlib import Path

# Raw data folder
raw_dir = Path("data/raw")

# Find all CSV files
csv_files = sorted(raw_dir.glob("*.csv"))

print(f"Total CSV files found: {len(csv_files)}")

for file in csv_files:
    try:
        df = pd.read_csv(file)

        print("\n" + "=" * 80)
        print(f"FILE: {file.name}")
        print("=" * 80)

        # Shape
        print("\nShape:")
        print(df.shape)

        # Data types
        print("\nData Types:")
        print(df.dtypes)

        # First 5 rows
        print("\nFirst 5 Rows:")
        print(df.head())

        # Missing values
        print("\nMissing Values:")
        print(df.isnull().sum())

        # Duplicate rows
        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"\nError reading {file.name}: {e}")