import pandas as pd
from pathlib import Path


def recommend_schemes(age, risk_profile, investment_amount, top_n=3):
    """
    Simple rule-based mutual fund recommender.

    Inputs:
    age                : Investor age
    risk_profile       : Low / Moderate / High / Very High
    investment_amount  : Investment amount in INR
    top_n              : Number of schemes to recommend
    """

    project_dir = Path(__file__).resolve().parent
    raw_dir = project_dir / "data" / "raw"

    # Load fund master
    fund_files = list(raw_dir.glob("*fund_master*.csv"))

    if not fund_files:
        raise FileNotFoundError("Fund master CSV not found.")

    df = pd.read_csv(fund_files[0])

    # Match risk profile
    risk_profile = risk_profile.strip().title()

    df = df[df["risk_category"] == risk_profile].copy()

    # Investment eligibility
    df = df[
        df["min_lumpsum_amount"] <= investment_amount
    ].copy()

    if df.empty:
        return pd.DataFrame()

    # Age-based category preference
    if age < 30:
        preferred_categories = ["Equity"]
    elif age < 50:
        preferred_categories = ["Equity", "Hybrid"]
    else:
        preferred_categories = ["Debt", "Hybrid", "Equity"]

    df["category_score"] = df["category"].apply(
        lambda x: 2 if x in preferred_categories else 1
    )

    # Lower expense ratio gets preference
    df = df.sort_values(
        ["category_score", "expense_ratio_pct"],
        ascending=[False, True]
    )

    return df[
        [
            "amfi_code",
            "scheme_name",
            "category",
            "risk_category",
            "min_lumpsum_amount"
        ]
    ].head(top_n)


if __name__ == "__main__":

    recommendations = recommend_schemes(
        age=25,
        risk_profile="Moderate",
        investment_amount=10000
    )

    print("\nTop 3 Recommended Schemes")
    print("=========================")
    print(recommendations.to_string(index=False))