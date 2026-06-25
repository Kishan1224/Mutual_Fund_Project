import pandas as pd

files = [
    "01_fund_master",
    "03_aum_by_fund_house",
    "04_monthly_sip_inflows",
    "05_category_inflows",
    "06_industry_folio_count",
    "09_portfolio_holdings",
    "10_benchmark_indices"
]

for file in files:

    df = pd.read_csv(f"data/raw/{file}.csv")

    df = df.drop_duplicates()

    df.to_csv(
        f"data/processed/{file}_cleaned.csv",
        index=False
    )

    print(f"{file} processed.")