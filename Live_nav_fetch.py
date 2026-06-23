import requests
import pandas as pd
import os

# Create output folder path
output_folder = os.path.join("data", "raw")

# Scheme codes to fetch
schemes = {
    "HDFC_Top100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            nav_df = pd.DataFrame(data["data"])

            file_path = os.path.join(
                output_folder,
                f"{fund_name}.csv"
            )

            nav_df.to_csv(file_path, index=False)

            print(f"{fund_name} data saved successfully.")

        else:
            print(f"Unable to fetch data for {fund_name}")

    except Exception as error:
        print(f"Error while fetching {fund_name}")
        print(error)