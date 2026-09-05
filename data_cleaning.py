import pandas as pd
from pathlib import Path

raw_dir = Path("data/raw")
processed_dir = Path("data/processed")
processed_dir.mkdir(parents=True, exist_ok=True)

files = list(raw_dir.glob("*scheme_performance*.csv"))

if not files:
    print("scheme_performance CSV not found!")
else:
    file = files[0]
    print("Processing:", file.name)

    df = pd.read_csv(file)

    print("Columns found:")
    print(df.columns.tolist())

    # Remove duplicates
    df = df.drop_duplicates()

    # Convert numeric columns
    for col in df.columns:
        if "return" in col.lower() or "expense" in col.lower():
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Check expense ratio
    expense_cols = [c for c in df.columns if "expense" in c.lower()]

    if expense_cols:
        col = expense_cols[0]
        df["expense_ratio_anomaly"] = ~df[col].between(0.1, 2.5)

    # Save cleaned file
    output_file = processed_dir / "scheme_performance_cleaned.csv"
    df.to_csv(output_file, index=False)

    print("\nCleaning completed!")
    print("Rows:", len(df))
    print("Saved to:", output_file)