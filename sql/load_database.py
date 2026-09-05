import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

processed_dir = Path("data/processed")

# SQLite database connection
engine = create_engine("sqlite:///bluestock_mf.db")

# Load each cleaned CSV
for file in processed_dir.glob("*.csv"):
    df = pd.read_csv(file)

    print("\nLoading:", file.name)

    # Choose database table
    if "nav_history" in file.name:
        table_name = "fact_nav"

    elif "investor_transactions" in file.name:
        table_name = "fact_transactions"

    elif "scheme_performance" in file.name:
        table_name = "fact_performance"

    else:
        print("Skipped:", file.name)
        continue

    # Load data into SQLite
    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False
    )

    print("Loaded into:", table_name)
    print("Rows:", len(df))

print("\nAll cleaned data loaded successfully!")