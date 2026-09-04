import requests
import pandas as pd
from pathlib import Path

# 5 key mutual fund schemes
schemes = {
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_Large_Cap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841"
}

output_dir = Path("data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

for scheme_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()

        df = pd.DataFrame(data["data"])

        # Add scheme information
        df.insert(0, "amfi_code", scheme_code)
        df.insert(1, "scheme_name", scheme_name)

        # Save CSV
        output_file = output_dir / f"live_nav_{scheme_code}.csv"
        df.to_csv(output_file, index=False)

        print(f"SUCCESS: {scheme_name} ({scheme_code})")
        print(f"Rows: {len(df)}")
        print(f"Saved: {output_file}\n")

    except Exception as e:
        print(f"ERROR: {scheme_name} ({scheme_code})")
        print(e)