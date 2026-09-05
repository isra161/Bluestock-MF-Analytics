from sqlalchemy import create_engine, text
from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent
db_path = project_dir / "bluestock_mf.db"

engine = create_engine(f"sqlite:///{db_path}")

schema_file = project_dir / "sql" / "schema.sql"
schema = schema_file.read_text(encoding="utf-8")

with engine.connect() as connection:

    # Remove old tables
    connection.execute(text("DROP TABLE IF EXISTS fact_transactions"))
    connection.execute(text("DROP TABLE IF EXISTS fact_nav"))
    connection.execute(text("DROP TABLE IF EXISTS fact_performance"))
    connection.execute(text("DROP TABLE IF EXISTS fact_aum"))
    connection.execute(text("DROP TABLE IF EXISTS dim_date"))
    connection.execute(text("DROP TABLE IF EXISTS dim_fund"))

    # Create tables again using schema.sql
    for statement in schema.split(";"):
        if statement.strip():
            connection.execute(text(statement))

    connection.commit()

print("Database recreated successfully!")
print(f"File: {db_path}")